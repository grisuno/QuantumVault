"""Behaviour contracts for QV-TUNNEL disposable secure channels.

Covers SecureChannelConfig resolution, URL validation, manager
lifecycle with injected process launcher, atomic state redaction in
audit details, and superadmin HTTP gating.
"""

from __future__ import annotations

import json
import os

from controllers.secure_channel import (
    ChannelMode,
    ChannelStatus,
    SecureChannelConfig,
    SecureChannelManager,
    _as_port,
    _as_scheme,
    _default_killer,
    _default_launcher,
    _normalize_onion,
    _wait_for_file,
    _wait_for_pattern,
    is_cloudflare_url,
    is_onion_url,
)


def test_config_defaults_to_disabled_without_binaries() -> None:
    """Unconfigured environment resolves to a disabled channel."""
    config = SecureChannelConfig.from_mapping({}, env={})
    assert config.mode == ChannelMode.DISABLED
    assert config.configured is False


def test_config_reads_mode_and_port_from_env() -> None:
    """Mode and local port resolve from environment with bounds."""
    config = SecureChannelConfig.from_mapping(
        {}, env={"QV_CHANNEL_MODE": "hybrid", "QV_CHANNEL_LOCAL_PORT": "4443"}
    )
    assert config.mode == ChannelMode.HYBRID
    assert config.local_port == 4443
    assert config.configured is True


def test_config_rejects_out_of_range_port() -> None:
    """Ports outside 1..65535 fall back to the default."""
    config = SecureChannelConfig.from_mapping(
        {}, env={"QV_CHANNEL_MODE": "tor", "QV_CHANNEL_LOCAL_PORT": "99999"}
    )
    assert config.local_port == SecureChannelConfig().local_port


def test_url_validators_accept_only_expected_shapes() -> None:
    """Validators accept quick-tunnel and v3 onion shapes only."""
    assert is_cloudflare_url("https://abc-def-123.trycloudflare.com") is True
    assert is_cloudflare_url("https://evil.example.com") is False
    onion = "http://" + "a" * 56 + ".onion"
    assert is_onion_url(onion) is True
    assert is_onion_url("http://short.onion") is False


def test_manager_starts_hybrid_with_injected_launcher(tmp_path) -> None:
    """Start launches both backends and persists redacted state."""

    def fake_launcher(cmd: list[str], log_path: str) -> int:
        Path = __import__("pathlib").Path
        if "cloudflared" in cmd[0]:
            Path(log_path).write_text(
                "https://demo-tunnel-1.trycloudflare.com\n", encoding="utf-8"
            )
        elif "tor" in cmd[0]:
            service_dir = Path(log_path).parent / "hidden_service"
            service_dir.mkdir(parents=True, exist_ok=True)
            (service_dir / "hostname").write_text(("b" * 56) + ".onion\n", encoding="utf-8")
        return 4242

    manager = SecureChannelManager(
        state_dir=str(tmp_path), local_port=4443, launcher=fake_launcher
    )
    status = manager.start(ChannelMode.HYBRID)
    assert status.cloud_url == "https://demo-tunnel-1.trycloudflare.com"
    assert status.onion_url == "http://" + "b" * 56 + ".onion"
    assert status.active is True
    stored = json.loads((tmp_path / "state.json").read_text(encoding="utf-8"))
    assert stored["mode"] == "hybrid"


def test_manager_rejects_invalid_mode(tmp_path) -> None:
    """Disabled mode cannot be started explicitly."""
    manager = SecureChannelManager(state_dir=str(tmp_path))
    try:
        manager.start(ChannelMode.DISABLED)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_manager_stop_clears_state_with_killer(tmp_path) -> None:
    """Stop kills tracked pids and removes persisted state."""
    killed: list[int] = []

    def fake_launcher(cmd: list[str], log_path: str) -> int:
        return 9999

    manager = SecureChannelManager(
        state_dir=str(tmp_path),
        launcher=fake_launcher,
        killer=killed.append,
    )
    manager._write_state(
        manager._status_for(ChannelMode.TOR, None, "http://" + "c" * 56 + ".onion", [9999])
    )
    status = manager.stop()
    assert status.active is False
    assert killed == [9999]
    assert not (tmp_path / "state.json").exists()


def test_audit_details_never_carry_urls() -> None:
    """Audit helper redacts full URLs to mode plus fingerprint."""
    manager = SecureChannelManager(state_dir="/tmp/qv-test-noop")
    details = manager.audit_details(
        "start", ChannelMode.HYBRID, "https://x.trycloudflare.com", "http://" + "d" * 56 + ".onion"
    )
    assert "trycloudflare.com" not in details
    assert ("d" * 56) not in details
    assert "hybrid" in details


def test_superadmin_channel_routes_require_superadmin(client) -> None:
    """Anonymous POST to channel endpoints redirects to login."""
    response = client.post("/superadmin-channel-start", data={"mode": "tor"})
    assert response.status_code in (302, 401, 403, 404)


def test_env_template_documents_channel_keys() -> None:
    """Repository env template exposes every channel key."""
    text = open(".env.example", encoding="utf-8").read()
    for key in (
        "QV_CHANNEL_MODE",
        "QV_CHANNEL_LOCAL_PORT",
        "QV_CHANNEL_LOCAL_SCHEME",
        "QV_CHANNEL_CLOUDFLARED_BIN",
        "QV_CHANNEL_TOR_BIN",
        "QV_CHANNEL_STATE_DIR",
    ):
        assert key in text


def test_channel_state_file_permissions(tmp_path) -> None:
    """Persisted state is owner-only."""
    manager = SecureChannelManager(state_dir=str(tmp_path))
    manager._write_state(
        manager._status_for(ChannelMode.TOR, None, "http://" + "e" * 56 + ".onion", [1])
    )
    mode = oct((tmp_path / "state.json").stat().st_mode & 0o777)
    assert mode == "0o600"
    assert os.path.exists(str(tmp_path / "state.json"))


def test_validators_reject_non_string_inputs() -> None:
    """Non-string values never validate as backend addresses."""
    assert is_cloudflare_url(None) is False
    assert is_cloudflare_url(12345) is False
    assert is_cloudflare_url("") is False
    assert is_cloudflare_url("  https://abc-def-123.trycloudflare.com  ") is True
    assert is_onion_url(None) is False
    assert is_onion_url(12345) is False
    assert is_onion_url("") is False


def test_port_boundaries_accept_edges_and_reject_outside() -> None:
    """TCP port coercion honors 1 and 65535 as valid edges."""
    assert _as_port("1", 4443) == 1
    assert _as_port("65535", 4443) == 65535
    assert _as_port("0", 4443) == 4443
    assert _as_port("65536", 4443) == 4443
    assert _as_port("-1", 4443) == 4443
    assert _as_port("notaport", 4443) == 4443
    assert _as_port(None, 4443) == 4443


def test_config_blank_values_fall_back_to_defaults() -> None:
    """Empty or whitespace binary and dir values resolve to defaults."""
    defaults = SecureChannelConfig()
    config = SecureChannelConfig.from_mapping(
        {},
        env={
            "QV_CHANNEL_MODE": "tor",
            "QV_CHANNEL_CLOUDFLARED_BIN": "   ",
            "QV_CHANNEL_TOR_BIN": "",
            "QV_CHANNEL_STATE_DIR": "  ",
        },
    )
    assert config.cloudflared_bin == defaults.cloudflared_bin
    assert config.tor_bin == defaults.tor_bin
    assert config.state_dir == defaults.state_dir


def test_config_explicit_values_are_preserved() -> None:
    """Explicit binary and dir values survive resolution."""
    config = SecureChannelConfig.from_mapping(
        {},
        env={
            "QV_CHANNEL_MODE": "cloudflared",
            "QV_CHANNEL_CLOUDFLARED_BIN": "/usr/local/bin/cloudflared",
            "QV_CHANNEL_TOR_BIN": "/usr/bin/tor",
            "QV_CHANNEL_STATE_DIR": "custom/state",
        },
    )
    assert config.cloudflared_bin == "/usr/local/bin/cloudflared"
    assert config.tor_bin == "/usr/bin/tor"
    assert config.state_dir == "custom/state"


def test_config_env_beats_mapping() -> None:
    """Environment takes precedence over the mapping for every key."""
    config = SecureChannelConfig.from_mapping(
        {"QV_CHANNEL_MODE": "tor", "QV_CHANNEL_LOCAL_PORT": "1111"},
        env={"QV_CHANNEL_MODE": "cloudflared", "QV_CHANNEL_LOCAL_PORT": "2222"},
    )
    assert config.mode == ChannelMode.CLOUDFLARED
    assert config.local_port == 2222


def test_channel_status_defaults_and_single_side_active() -> None:
    """Ephemeral defaults True and either backend alone counts as active."""
    assert ChannelStatus(
        mode=ChannelMode.DISABLED, cloud_url=None, onion_url=None, pids=()
    ).ephemeral is True
    cloud_only = ChannelStatus(
        mode=ChannelMode.CLOUDFLARED,
        cloud_url="https://abc-def-123.trycloudflare.com",
        onion_url=None,
        pids=(1,),
    )
    assert cloud_only.active is True
    onion_only = ChannelStatus(
        mode=ChannelMode.TOR,
        cloud_url=None,
        onion_url="http://" + "f" * 56 + ".onion",
        pids=(1,),
    )
    assert onion_only.active is True
    idle = ChannelStatus(
        mode=ChannelMode.DISABLED, cloud_url=None, onion_url=None, pids=()
    )
    assert idle.active is False


def test_default_launcher_detaches_process(monkeypatch) -> None:
    """Launcher spawns detached daemons with piped stdio."""
    import subprocess as _subprocess

    captured: dict = {}

    class _FakeProcess:
        pid = 7777

    def _fake_popen(cmd, **kwargs):
        captured.update(kwargs)
        captured["cmd"] = cmd
        return _FakeProcess()

    monkeypatch.setattr(_subprocess, "Popen", _fake_popen)
    pid = _default_launcher(["tor", "-f", "torrc"], "/tmp/qv-test-launcher.log")
    assert pid == 7777
    assert captured["start_new_session"] is True
    assert captured["close_fds"] is True
    assert captured["stdin"] is _subprocess.DEVNULL


def test_default_killer_ignores_non_positive_pid(monkeypatch) -> None:
    """Zero and negative pids never reach os.kill."""
    calls: list = []
    monkeypatch.setattr(os, "killpg", lambda *a: calls.append(("pg", a)))
    monkeypatch.setattr(os, "kill", lambda *a: calls.append(("kill", a)))
    _default_killer(0)
    _default_killer(-3)
    assert calls == []


def test_default_killer_falls_back_to_kill(monkeypatch) -> None:
    """Group kill failure falls back to plain kill before giving up."""
    calls: list = []

    def _raise_pg(pid, sig):
        raise PermissionError("no pg")

    def _record_kill(pid, sig):
        calls.append((pid, sig))

    monkeypatch.setattr(os, "killpg", _raise_pg)
    monkeypatch.setattr(os, "kill", _record_kill)
    _default_killer(4242)
    assert len(calls) == 1


def test_manager_init_blank_binaries_fall_back() -> None:
    """Blank constructor binaries resolve to shipped defaults."""
    manager = SecureChannelManager(
        state_dir="/tmp/qv-test-noop", cloudflared_bin="", tor_bin=""
    )
    assert manager.cloudflared_bin == SecureChannelConfig().cloudflared_bin
    assert manager.tor_bin == SecureChannelConfig().tor_bin


def test_rotate_without_state_raises(tmp_path) -> None:
    """Rotate with no persisted channel raises instead of crashing."""
    manager = SecureChannelManager(state_dir=str(tmp_path))
    try:
        manager.rotate()
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_rotate_disabled_state_raises(tmp_path) -> None:
    """Rotate on a disabled record raises instead of starting."""
    manager = SecureChannelManager(state_dir=str(tmp_path))
    manager._write_state(manager._status_for(ChannelMode.DISABLED, None, None, ()))
    try:
        manager.rotate()
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_audit_details_default_verb_and_empty_urls() -> None:
    """Empty action and absent urls still yield a safe detail string."""
    manager = SecureChannelManager(state_dir="/tmp/qv-test-noop")
    assert manager.audit_details("", ChannelMode.TOR, None, None) == "channel mode=tor"
    assert (
        manager.audit_details("   ", ChannelMode.TOR, None, None)
        == "channel mode=tor"
    )
    details = manager.audit_details(
        "start", ChannelMode.HYBRID, "https://x.trycloudflare.com", None
    )
    assert details.startswith("start mode=hybrid")


def test_status_for_drops_non_positive_pids() -> None:
    """Pid zero and negatives never survive status construction."""
    manager = SecureChannelManager(state_dir="/tmp/qv-test-noop")
    current = manager._status_for(
        ChannelMode.TOR, None, "http://" + "a" * 56 + ".onion", [0, -5, 42]
    )
    assert current.pids == (42,)


def test_read_state_filters_bad_pids(tmp_path) -> None:
    """Corrupt pid entries in state are filtered, valid ones kept."""
    import json as _json

    manager = SecureChannelManager(state_dir=str(tmp_path))
    (tmp_path / "state.json").write_text(
        _json.dumps(
            {
                "mode": "tor",
                "cloud_url": None,
                "onion_url": "http://" + "b" * 56 + ".onion",
                "pids": [0, -1, "x", 42, None],
            }
        ),
        encoding="utf-8",
    )
    stored = manager._read_state()
    assert stored is not None
    assert stored.pids == (42,)


def test_write_state_is_sorted_and_ephemeral(tmp_path) -> None:
    """Persisted payload is deterministic JSON with ephemeral set."""
    manager = SecureChannelManager(state_dir=str(tmp_path))
    manager._write_state(
        manager._status_for(
            ChannelMode.HYBRID,
            "https://abc-def-123.trycloudflare.com",
            "http://" + "c" * 56 + ".onion",
            [4242],
        )
    )
    text = (tmp_path / "state.json").read_text(encoding="utf-8")
    assert '"ephemeral": true' in text
    assert text.index('"cloud_url"') < text.index('"ephemeral"')
    assert text.index('"ephemeral"') < text.index('"mode"')
    assert text.index('"mode"') < text.index('"onion_url"')
    assert text.index('"onion_url"') < text.index('"pids"')


def test_write_state_twice_in_existing_dir(tmp_path) -> None:
    """Repeated writes into an existing directory never raise."""
    manager = SecureChannelManager(state_dir=str(tmp_path))
    first = manager._status_for(
        ChannelMode.TOR, None, "http://" + "d" * 56 + ".onion", [1]
    )
    manager._write_state(first)
    manager._write_state(first)
    assert (tmp_path / "state.json").exists()


def test_write_state_creates_nested_dirs(tmp_path) -> None:
    """Nested state directories are created recursively."""
    nested = tmp_path / "level-a" / "level-b"
    manager = SecureChannelManager(state_dir=str(nested))
    manager._write_state(manager._status_for(ChannelMode.DISABLED, None, None, ()))
    assert (nested / "state.json").exists()


def test_start_creates_nested_state_dirs(tmp_path) -> None:
    """Backend start creates nested state dirs recursively."""

    def fake_launcher(cmd: list[str], log_path: str) -> int:
        Path = __import__("pathlib").Path
        if "cloudflared" in cmd[0]:
            Path(log_path).write_text(
                "https://nested-tunnel-1.trycloudflare.com\n", encoding="utf-8"
            )
        elif "tor" in cmd[0]:
            service_dir = Path(log_path).parent / "hidden_service"
            service_dir.mkdir(parents=True, exist_ok=True)
            (service_dir / "hostname").write_text(
                ("a" * 56) + ".onion\n", encoding="utf-8"
            )
        return 4243

    nested = tmp_path / "deep" / "deeper"
    manager = SecureChannelManager(
        state_dir=str(nested), local_port=4443, launcher=fake_launcher
    )
    current = manager.start(ChannelMode.HYBRID)
    assert current.active is True
    assert (nested / "state.json").exists()


def test_start_tor_only_creates_nested_state_dirs(tmp_path) -> None:
    """Tor-only start creates nested state dirs without prior backend."""

    def fake_launcher(cmd: list[str], log_path: str) -> int:
        Path = __import__("pathlib").Path
        service_dir = Path(log_path).parent / "hidden_service"
        service_dir.mkdir(parents=True, exist_ok=True)
        (service_dir / "hostname").write_text(
            ("b" * 56) + ".onion\n", encoding="utf-8"
        )
        return 4244

    nested = tmp_path / "tor-deep" / "tor-deeper"
    manager = SecureChannelManager(
        state_dir=str(nested), local_port=4443, launcher=fake_launcher
    )
    current = manager.start(ChannelMode.TOR)
    assert current.onion_url == "http://" + "b" * 56 + ".onion"
    assert (nested / "state.json").exists()


def test_cleanup_scratch_suppresses_rmtree_errors(tmp_path, monkeypatch) -> None:
    """Unremovable scratch dirs never break stop."""
    import shutil as _shutil

    target = tmp_path / "tor-data-stuck"
    target.mkdir()
    manager = SecureChannelManager(state_dir=str(tmp_path))

    def _raise(*args, **kwargs):
        if kwargs.get("ignore_errors"):
            return
        raise OSError("stuck")

    monkeypatch.setattr(_shutil, "rmtree", _raise)
    manager._cleanup_scratch()


def test_resolve_binary_with_default_launcher_requires_path(tmp_path) -> None:
    """Default launcher resolves bare names through PATH only."""
    manager = SecureChannelManager(state_dir=str(tmp_path))
    try:
        manager._resolve_binary("qv-definitely-missing-binary-xyz")
    except RuntimeError:
        pass
    else:
        raise AssertionError("expected RuntimeError")
    try:
        manager._resolve_binary("  ")
    except RuntimeError:
        pass
    else:
        raise AssertionError("expected RuntimeError")


def test_resolve_binary_with_injected_launcher_skips_which(tmp_path) -> None:
    """Injected launchers accept bare names without PATH lookup."""
    manager = SecureChannelManager(
        state_dir=str(tmp_path), launcher=lambda cmd, log: 1
    )
    assert manager._resolve_binary("cloudflared") == "cloudflared"
    try:
        manager._resolve_binary("")
    except RuntimeError:
        pass
    else:
        raise AssertionError("expected RuntimeError")


def test_resolve_binary_absolute_path_must_exist(tmp_path) -> None:
    """Absolute candidates are accepted only when the file exists."""
    manager = SecureChannelManager(
        state_dir=str(tmp_path), launcher=lambda cmd, log: 1
    )
    real = tmp_path / "bin-fake"
    real.write_text("x", encoding="utf-8")
    assert manager._resolve_binary(str(real)) == str(real)
    try:
        manager._resolve_binary(str(tmp_path / "no-such-bin"))
    except RuntimeError:
        pass
    else:
        raise AssertionError("expected RuntimeError")


def test_pid_live_branches(monkeypatch, tmp_path) -> None:
    """Pid liveness distinguishes dead, forbidden, broken, and live."""
    import errno as _errno

    manager = SecureChannelManager(state_dir=str(tmp_path))
    assert manager._pid_live(0) is False
    assert manager._pid_live(-1) is False
    assert manager._pid_live(os.getpid()) is True

    def _raise_lookup(pid, sig):
        raise ProcessLookupError(_errno.ESRCH, "gone")

    monkeypatch.setattr(os, "kill", _raise_lookup)
    assert manager._pid_live(424242) is False

    def _raise_perm(pid, sig):
        raise PermissionError("denied")

    monkeypatch.setattr(os, "kill", _raise_perm)
    assert manager._pid_live(1) is True

    def _raise_os(pid, sig):
        raise OSError("broken")

    monkeypatch.setattr(os, "kill", _raise_os)
    assert manager._pid_live(1) is False


def test_normalize_onion_shapes() -> None:
    """Bare hostnames gain a scheme while full urls pass through."""
    bare = "a" * 56 + ".onion"
    assert _normalize_onion(bare + "\n") == "http://" + bare
    full = "http://" + bare
    assert _normalize_onion(full) == full
    assert _normalize_onion("http://short.onion") == "http://short.onion"


def test_wait_helpers_respect_deadline_and_content(tmp_path, monkeypatch) -> None:
    """Pattern and file waiters poll until timeout or content."""
    import re as _re
    import time as _time

    log = tmp_path / "cf.log"
    log.write_text("no url yet\n", encoding="utf-8")
    ticks = {"n": 0.0}

    def _fake_mono():
        return ticks["n"]

    def _fake_sleep(secs):
        ticks["n"] += 10.0

    monkeypatch.setattr(_time, "monotonic", _fake_mono)
    monkeypatch.setattr(_time, "sleep", _fake_sleep)
    pattern = _re.compile(r"https://[-0-9a-z]+\.trycloudflare\.com")
    assert _wait_for_pattern(str(log), pattern, 5) is None
    log.write_text("up at https://abc-def-123.trycloudflare.com\n", encoding="utf-8")
    ticks["n"] = 0.0
    assert (
        _wait_for_pattern(str(log), pattern, 5)
        == "https://abc-def-123.trycloudflare.com"
    )
    missing = tmp_path / "hostname"
    ticks["n"] = 0.0
    assert _wait_for_file(missing, 5) == ""
    missing.write_text(("e" * 56) + ".onion\n", encoding="utf-8")
    ticks["n"] = 0.0
    assert "e" * 56 in _wait_for_file(missing, 5)


def test_wait_helpers_include_deadline_instant(tmp_path, monkeypatch) -> None:
    """Polling still checks content at the exact deadline instant."""
    import re as _re
    import time as _time

    log = tmp_path / "edge.log"
    log.write_text("nothing\n", encoding="utf-8")
    ticks = {"n": 0.0}

    def _fake_mono():
        return ticks["n"]

    def _fake_sleep(secs):
        ticks["n"] += 5.0
        if ticks["n"] == 10.0:
            log.write_text(
                "up at https://edge-case-1.trycloudflare.com\n", encoding="utf-8"
            )

    monkeypatch.setattr(_time, "monotonic", _fake_mono)
    monkeypatch.setattr(_time, "sleep", _fake_sleep)
    pattern = _re.compile(r"https://[-0-9a-z]+\.trycloudflare\.com")
    assert (
        _wait_for_pattern(str(log), pattern, 10)
        == "https://edge-case-1.trycloudflare.com"
    )

    target = tmp_path / "edge-host"
    ticks["n"] = 0.0

    def _fake_sleep_file(secs):
        ticks["n"] += 5.0
        if ticks["n"] == 10.0:
            target.write_text(("f" * 56) + ".onion\n", encoding="utf-8")

    monkeypatch.setattr(_time, "sleep", _fake_sleep_file)
    assert ("f" * 56) in _wait_for_file(target, 10)


def test_channel_diagnostics_reports_availability(tmp_path) -> None:
    """Diagnostics resolve absolute paths and flag missing bare names."""
    from views.admin import _channel_diagnostics

    present = tmp_path / "cloudflared-fake"
    present.write_text("x", encoding="utf-8")
    manager = SecureChannelManager(
        state_dir=str(tmp_path),
        cloudflared_bin=str(present),
        tor_bin="qv-definitely-missing-binary-xyz",
        launcher=lambda cmd, log: 1,
    )
    diag = _channel_diagnostics(manager)
    assert diag["cloudflared"]["available"] is True
    assert diag["cloudflared"]["resolved"] == str(present)
    assert diag["tor"]["available"] is False
    assert diag["local_port"] == 4443
    assert diag["state_dir"] == str(tmp_path)


def test_channel_diagnostics_missing_absolute_path(tmp_path) -> None:
    """Absolute candidates that do not exist report as missing."""
    from views.admin import _channel_diagnostics

    manager = SecureChannelManager(
        state_dir=str(tmp_path),
        cloudflared_bin=str(tmp_path / "no-such-bin"),
        tor_bin=str(tmp_path / "no-such-tor"),
        launcher=lambda cmd, log: 1,
    )
    diag = _channel_diagnostics(manager)
    assert diag["cloudflared"]["available"] is False
    assert diag["tor"]["available"] is False


def test_read_log_tail_returns_trailing_lines(tmp_path) -> None:
    """Log tail surfaces backend output and stays empty when absent."""
    from views.admin import _read_log_tail

    assert _read_log_tail(str(tmp_path)) == ""
    log = tmp_path / "cloudflared.log"
    log.write_text(
        "\n".join(f"line {index}" for index in range(30)), encoding="utf-8"
    )
    tail = _read_log_tail(str(tmp_path), limit=5)
    assert "line 29" in tail
    assert "line 0" not in tail


def test_superadmin_channel_section_is_readable() -> None:
    """Channel panel avoids low-contrast muted text and shows diagnostics."""
    text = open("templates/superadmin.html", encoding="utf-8").read()
    section = text.split("Disposable Secure Channels", 1)[1].split(
        "<h2", 1
    )[0]
    assert "text-muted" not in section
    assert "channel_diag" in text
    assert "cbd5e1" in text


def test_origin_scheme_parsing() -> None:
    """Only http and https survive scheme coercion."""
    assert _as_scheme("https", "http") == "https"
    assert _as_scheme(" HTTPS ", "http") == "https"
    assert _as_scheme("http", "https") == "http"
    assert _as_scheme("socks5", "http") == "http"
    assert _as_scheme("", "http") == "http"
    assert _as_scheme(None, "http") == "http"


def test_config_reads_origin_scheme() -> None:
    """Origin scheme resolves from env with a safe fallback."""
    config = SecureChannelConfig.from_mapping(
        {}, env={"QV_CHANNEL_MODE": "tor", "QV_CHANNEL_LOCAL_SCHEME": "https"}
    )
    assert config.local_scheme == "https"
    assert SecureChannelConfig().local_scheme == "http"
    fallback = SecureChannelConfig.from_mapping(
        {}, env={"QV_CHANNEL_LOCAL_SCHEME": "ftp"}
    )
    assert fallback.local_scheme == "http"


def test_origin_url_points_at_loopback() -> None:
    """Origin URL always targets loopback with the configured scheme."""
    plain = SecureChannelManager(
        state_dir="/tmp/qv-test-noop", launcher=lambda cmd, log: 1
    )
    assert plain.origin_url == "http://127.0.0.1:4443"
    tls = SecureChannelManager(
        state_dir="/tmp/qv-test-noop",
        local_scheme="https",
        launcher=lambda cmd, log: 1,
    )
    assert tls.origin_url == "https://127.0.0.1:4443"


def test_cloudflared_cmd_matches_origin_scheme(tmp_path) -> None:
    """Plain origins skip TLS flags, https origins verify nothing."""
    seen: list[list[str]] = []

    def fake_launcher(cmd: list[str], log_path: str) -> int:
        from pathlib import Path as _Path

        seen.append(cmd)
        _Path(log_path).write_text(
            "https://scheme-test-1.trycloudflare.com\n", encoding="utf-8"
        )
        return 4251

    plain = SecureChannelManager(
        state_dir=str(tmp_path), launcher=fake_launcher
    )
    plain._start_cloudflared()
    assert "--no-tls-verify" not in seen[-1]
    assert "http://127.0.0.1:4443" in seen[-1]

    secure = SecureChannelManager(
        state_dir=str(tmp_path),
        local_scheme="https",
        launcher=fake_launcher,
    )
    secure._start_cloudflared()
    assert "--no-tls-verify" in seen[-1]
    assert "https://127.0.0.1:4443" in seen[-1]


def test_s3_probe_skips_dead_endpoint(app) -> None:
    """Unreachable object storage reports down without raising."""
    from views.admin import _s3_reachable

    with app.test_request_context("/"):
        assert _s3_reachable(timeout=0.2) is False


def test_s3_probe_detects_live_endpoint(app) -> None:
    """A listening socket reports the endpoint as reachable."""
    import socket as _socket

    from views.admin import _s3_reachable

    server = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    port = server.getsockname()[1]
    try:
        app.config["S3_ENDPOINT_URL"] = f"http://127.0.0.1:{port}"
        with app.test_request_context("/"):
            assert _s3_reachable(timeout=1.0) is True
    finally:
        server.close()
