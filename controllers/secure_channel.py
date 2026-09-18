"""QV-TUNNEL disposable secure channels over Cloudflare and Tor.

Inspiration comes from LazyOwn operator practice: a disposable
``cloudflared`` quick tunnel exposing a local port through a
``*.trycloudflare.com`` URL, and a disposable Tor onion service
exposing the same port as a ``*.onion`` address. LazyOwn runs both
with interactive prompts and host-wide side effects. This module
replaces that workflow with an unprivileged deterministic
supervisor suited to QuantumVault zero-trust operation.

Contract summary:

- Channel modes are ``disabled``, ``cloudflared``, ``tor``, and
  ``hybrid``. Hybrid runs both backends so traffic can use either
  path and rotation disposes both addresses at once.
- Cloudflare uses ``cloudflared tunnel --url`` against loopback
  only. The origin scheme follows ``QV_CHANNEL_LOCAL_SCHEME``
  (``http`` or ``https``): an ``https`` origin adds
  ``--no-tls-verify`` so a self-signed dev listener stays reachable
  instead of answering Bad Gateway. The public URL is parsed from
  process output with a closed allow-list pattern. No account token
  is required for quick tunnels and none is accepted here, which
  keeps rotation fully disposable.
- Tor uses an unprivileged ``tor`` process with a generated data
  directory under the configured state directory. No system
  ``torrc`` file is modified and no sudo is required. The onion
  hostname is read from the disposable data directory.
- State persists atomically as owner-only JSON. Audit records
  carry mode plus short fingerprints, never full URLs.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import tempfile
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Mapping, Optional, Sequence


_DEFAULT_MODE = "disabled"
_DEFAULT_LOCAL_PORT = 4443
_DEFAULT_LOCAL_SCHEME = "http"
_DEFAULT_CLOUDFLARED_BIN = "cloudflared"
_DEFAULT_TOR_BIN = "tor"
_DEFAULT_STATE_DIR = "instance/secure_channels"
_DEFAULT_START_TIMEOUT_SECONDS = 45
_DEFAULT_TOR_SOCKS_PORT = 0

_CLOUDFLARE_PATTERN = re.compile(r"https://[-0-9a-z]+\.trycloudflare\.com")
_BARE_ONION_PATTERN = re.compile(r"^[a-z2-7]{56}\.onion$")
_ONION_PATTERN = re.compile(r"^http://[a-z2-7]{56}\.onion$")
_MODE_VALUES = frozenset({"disabled", "cloudflared", "tor", "hybrid"})
_STATE_FILENAME = "state.json"
_TRUTHY = frozenset({"1", "true", "yes", "on"})


class ChannelMode(Enum):
    """Selectable disposable channel mode."""

    DISABLED = "disabled"
    CLOUDFLARED = "cloudflared"
    TOR = "tor"
    HYBRID = "hybrid"

    @classmethod
    def parse(cls, raw: Any) -> "ChannelMode":
        """Parse free-form input into a mode, defaulting to disabled."""
        text = str(raw or "").strip().lower()
        if text not in _MODE_VALUES:
            return cls.DISABLED
        return cls(text)


def is_cloudflare_url(value: object) -> bool:
    """Return whether value is a quick-tunnel HTTPS URL."""
    if not isinstance(value, str):
        return False
    return _CLOUDFLARE_PATTERN.fullmatch(value.strip()) is not None


def is_onion_url(value: object) -> bool:
    """Return whether value is a v3 onion HTTP address."""
    if not isinstance(value, str):
        return False
    return _ONION_PATTERN.match(value.strip()) is not None


def _as_port(value: Any, default: int) -> int:
    """Coerce input to a TCP port, falling back on default."""
    try:
        port = int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return default
    if 1 <= port <= 65535:
        return port
    return default


def _as_scheme(value: Any, default: str) -> str:
    """Coerce input to an origin scheme, accepting http or https only."""
    text = str(value or "").strip().lower()
    if text in ("http", "https"):
        return text
    return default


@dataclass(frozen=True)
class SecureChannelConfig:
    """Immutable secure channel configuration from env and mapping."""

    mode: ChannelMode = ChannelMode.DISABLED
    local_port: int = _DEFAULT_LOCAL_PORT
    local_scheme: str = _DEFAULT_LOCAL_SCHEME
    cloudflared_bin: str = _DEFAULT_CLOUDFLARED_BIN
    tor_bin: str = _DEFAULT_TOR_BIN
    state_dir: str = _DEFAULT_STATE_DIR
    start_timeout_seconds: int = _DEFAULT_START_TIMEOUT_SECONDS
    tor_socks_port: int = _DEFAULT_TOR_SOCKS_PORT

    @property
    def configured(self) -> bool:
        """Return whether a disposible channel mode is selected."""
        return self.mode is not ChannelMode.DISABLED

    @classmethod
    def from_mapping(
        cls,
        mapping: Mapping[str, Any],
        env: Optional[Mapping[str, str]] = None,
    ) -> "SecureChannelConfig":
        """Resolve configuration with environment, mapping, then default order."""
        source = os.environ if env is None else env

        def read(key: str) -> Any:
            if key in source:
                return source[key]
            if key in mapping:
                return mapping[key]
            return None

        defaults = cls()
        raw_mode = read("QV_CHANNEL_MODE")
        raw_port = read("QV_CHANNEL_LOCAL_PORT")
        raw_scheme = read("QV_CHANNEL_LOCAL_SCHEME")
        raw_cloudflared = read("QV_CHANNEL_CLOUDFLARED_BIN")
        raw_tor = read("QV_CHANNEL_TOR_BIN")
        raw_state = read("QV_CHANNEL_STATE_DIR")
        raw_timeout = read("QV_CHANNEL_START_TIMEOUT")
        raw_socks = read("QV_CHANNEL_TOR_SOCKS_PORT")
        return cls(
            mode=ChannelMode.parse(raw_mode),
            local_port=_as_port(raw_port, defaults.local_port),
            local_scheme=_as_scheme(raw_scheme, defaults.local_scheme),
            cloudflared_bin=str(raw_cloudflared or defaults.cloudflared_bin).strip()
            or defaults.cloudflared_bin,
            tor_bin=str(raw_tor or defaults.tor_bin).strip() or defaults.tor_bin,
            state_dir=str(raw_state or defaults.state_dir).strip() or defaults.state_dir,
            start_timeout_seconds=_as_port(raw_timeout, defaults.start_timeout_seconds),
            tor_socks_port=_as_port(raw_socks, defaults.tor_socks_port)
            if raw_socks not in (None, "", 0, "0")
            else 0,
        )


@dataclass(frozen=True)
class ChannelStatus:
    """Point-in-time view of disposable channel state."""

    mode: ChannelMode
    cloud_url: Optional[str]
    onion_url: Optional[str]
    pids: tuple[int, ...]
    ephemeral: bool = True

    @property
    def active(self) -> bool:
        """Return whether any backend address is currently published."""
        return bool(self.cloud_url or self.onion_url)


Launcher = Callable[[list[str], str], int]
Killer = Callable[[int], None]


def _default_launcher(cmd: Sequence[str], log_path: str) -> int:
    """Spawn a backend daemon detached from the web worker."""
    with open(log_path, "ab") as log_handle:
        process = subprocess.Popen(
            list(cmd),
            stdin=subprocess.DEVNULL,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
            close_fds=True,
        )
    return int(process.pid)


def _default_killer(pid: int) -> None:
    """Terminate one tracked backend process group."""
    if pid <= 0:
        return
    try:
        os.killpg(pid, signal.SIGTERM)
    except (ProcessLookupError, PermissionError, OSError):
        try:
            os.kill(pid, signal.SIGTERM)
        except (ProcessLookupError, PermissionError, OSError):
            return


class SecureChannelManager:
    """Supervise disposable Cloudflare and Tor backends."""

    def __init__(
        self,
        state_dir: str = _DEFAULT_STATE_DIR,
        local_port: int = _DEFAULT_LOCAL_PORT,
        local_scheme: str = _DEFAULT_LOCAL_SCHEME,
        cloudflared_bin: str = _DEFAULT_CLOUDFLARED_BIN,
        tor_bin: str = _DEFAULT_TOR_BIN,
        start_timeout_seconds: int = _DEFAULT_START_TIMEOUT_SECONDS,
        launcher: Optional[Launcher] = None,
        killer: Optional[Killer] = None,
    ) -> None:
        """Bind the manager to a state directory and backend binaries."""
        self.state_dir = state_dir
        self.local_port = _as_port(local_port, _DEFAULT_LOCAL_PORT)
        self.local_scheme = _as_scheme(local_scheme, _DEFAULT_LOCAL_SCHEME)
        self.cloudflared_bin = cloudflared_bin or _DEFAULT_CLOUDFLARED_BIN
        self.tor_bin = tor_bin or _DEFAULT_TOR_BIN
        self.start_timeout_seconds = _as_port(
            start_timeout_seconds, _DEFAULT_START_TIMEOUT_SECONDS
        )
        self._launcher = launcher or _default_launcher
        self._killer = killer or _default_killer

    @property
    def origin_url(self) -> str:
        """Return the loopback origin URL both backends forward to."""
        return f"{self.local_scheme}://127.0.0.1:{self.local_port}"

    @classmethod
    def from_config(
        cls,
        config: SecureChannelConfig,
        launcher: Optional[Launcher] = None,
        killer: Optional[Killer] = None,
    ) -> "SecureChannelManager":
        """Build a manager sharing binary paths and ports with config."""
        return cls(
            state_dir=config.state_dir,
            local_port=config.local_port,
            local_scheme=config.local_scheme,
            cloudflared_bin=config.cloudflared_bin,
            tor_bin=config.tor_bin,
            start_timeout_seconds=config.start_timeout_seconds,
            launcher=launcher,
            killer=killer,
        )

    def status(self) -> ChannelStatus:
        """Return live status, pruning dead pids without side effects."""
        stored = self._read_state()
        if stored is None:
            return self._status_for(ChannelMode.DISABLED, None, None, ())
        pids = tuple(pid for pid in stored.pids if self._pid_live(pid))
        cloud_url = stored.cloud_url if pids else None
        onion_url = stored.onion_url if pids else None
        mode = stored.mode if pids else ChannelMode.DISABLED
        return self._status_for(mode, cloud_url, onion_url, pids)

    def start(self, mode: ChannelMode) -> ChannelStatus:
        """Start backends for mode, replacing any running channel."""
        if mode is ChannelMode.DISABLED:
            raise ValueError("refusing to start a disabled channel")
        self.stop()
        cloud_url: Optional[str] = None
        onion_url: Optional[str] = None
        pids: list[int] = []
        if mode in (ChannelMode.CLOUDFLARED, ChannelMode.HYBRID):
            pid, url = self._start_cloudflared()
            pids.append(pid)
            cloud_url = url
        if mode in (ChannelMode.TOR, ChannelMode.HYBRID):
            pid, url = self._start_tor()
            pids.append(pid)
            onion_url = url
        current = self._status_for(mode, cloud_url, onion_url, tuple(pids))
        self._write_state(current)
        return current

    def stop(self) -> ChannelStatus:
        """Terminate tracked backends and remove persisted state."""
        stored = self._read_state()
        if stored is not None:
            for pid in stored.pids:
                try:
                    self._killer(int(pid))
                except (ValueError, TypeError):
                    continue
        self._remove_state()
        self._cleanup_scratch()
        return self._status_for(ChannelMode.DISABLED, None, None, ())

    def rotate(self) -> ChannelStatus:
        """Dispose current addresses and start the same mode again."""
        stored = self._read_state()
        if stored is None or stored.mode is ChannelMode.DISABLED:
            raise ValueError("no active channel to rotate")
        return self.start(stored.mode)

    def audit_details(
        self,
        action: str,
        mode: ChannelMode,
        cloud_url: Optional[str],
        onion_url: Optional[str],
    ) -> str:
        """Return an audit-safe detail string without full addresses."""
        verb = str(action or "channel").strip().lower() or "channel"
        parts = [f"{verb} mode={mode.value}"]
        if cloud_url:
            parts.append(f"cf={_fingerprint(cloud_url)}")
        if onion_url:
            parts.append(f"onion={_fingerprint(onion_url)}")
        return " ".join(parts)

    def _status_for(
        self,
        mode: ChannelMode,
        cloud_url: Optional[str],
        onion_url: Optional[str],
        pids: tuple[int, ...] | list[int],
    ) -> ChannelStatus:
        """Build a status after validating backend address shapes."""
        clean_cloud = cloud_url if is_cloudflare_url(cloud_url) else None
        clean_onion = onion_url if is_onion_url(onion_url) else None
        clean_pids = tuple(int(pid) for pid in pids if int(pid) > 0)
        return ChannelStatus(
            mode=mode, cloud_url=clean_cloud, onion_url=clean_onion, pids=clean_pids
        )

    def _state_path(self) -> Path:
        """Return the persisted state file path."""
        return Path(self.state_dir) / _STATE_FILENAME

    def _read_state(self) -> Optional[ChannelStatus]:
        """Load persisted state, returning None when absent or corrupt."""
        try:
            raw = json.loads(self._state_path().read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return None
        if not isinstance(raw, dict):
            return None
        mode = ChannelMode.parse(raw.get("mode"))
        cloud_url = raw.get("cloud_url")
        onion_url = raw.get("onion_url")
        pids_raw = raw.get("pids") or []
        pids = tuple(int(pid) for pid in pids_raw if isinstance(pid, int))
        return self._status_for(mode, cloud_url, onion_url, pids)

    def _write_state(self, current: ChannelStatus) -> None:
        """Persist state atomically with owner-only permissions."""
        target = self._state_path()
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "mode": current.mode.value,
            "cloud_url": current.cloud_url,
            "onion_url": current.onion_url,
            "pids": list(current.pids),
            "ephemeral": True,
        }
        descriptor, tmp_name = tempfile.mkstemp(
            dir=str(target.parent), prefix=".state-", suffix=".tmp"
        )
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                json.dump(payload, handle, sort_keys=True)
            os.chmod(tmp_name, 0o600)
            os.replace(tmp_name, target)
        finally:
            try:
                os.unlink(tmp_name)
            except OSError:
                pass

    def _remove_state(self) -> None:
        """Remove persisted state when present."""
        try:
            self._state_path().unlink()
        except FileNotFoundError:
            return
        except OSError:
            return

    def _cleanup_scratch(self) -> None:
        """Remove stale per-boot scratch directories left by Tor."""
        parent = Path(self.state_dir)
        if not parent.is_dir():
            return
        for entry in parent.glob("tor-data-*"):
            shutil.rmtree(entry, ignore_errors=True)
        for entry in parent.glob("*.log"):
            try:
                entry.unlink()
            except OSError:
                continue

    def _start_cloudflared(self) -> tuple[int, str]:
        """Launch a disposable quick tunnel and parse its public URL."""
        binary = self._resolve_binary(self.cloudflared_bin)
        log_path = str(Path(self.state_dir) / "cloudflared.log")
        Path(self.state_dir).mkdir(parents=True, exist_ok=True)
        cmd = [
            binary,
            "tunnel",
            "--no-autoupdate",
            "--url",
            self.origin_url,
        ]
        if self.local_scheme == "https":
            cmd.append("--no-tls-verify")
        pid = int(self._launcher(cmd, log_path))
        url = _wait_for_pattern(log_path, _CLOUDFLARE_PATTERN, self.start_timeout_seconds)
        if not is_cloudflare_url(url):
            raise RuntimeError("cloudflared did not publish a tunnel URL")
        return pid, str(url)

    def _start_tor(self) -> tuple[int, str]:
        """Launch an unprivileged disposable onion service."""
        binary = self._resolve_binary(self.tor_bin)
        base = Path(self.state_dir)
        base.mkdir(parents=True, exist_ok=True)
        data_dir = Path(
            tempfile.mkdtemp(prefix="tor-data-", dir=str(base))
        )
        os.chmod(data_dir, 0o700)
        service_dir = data_dir / "hidden_service"
        service_dir.mkdir(mode=0o700)
        torrc_path = data_dir / "torrc"
        torrc_path.write_text(
            "\n".join(
                [
                    f"DataDirectory {data_dir}",
                    "SocksPort 0",
                    f"HiddenServiceDir {service_dir}",
                    f"HiddenServicePort 80 127.0.0.1:{self.local_port}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        os.chmod(torrc_path, 0o600)
        log_path = str(data_dir / "tor.log")
        pid = int(self._launcher([binary, "-f", str(torrc_path)], log_path))
        hostname_file = service_dir / "hostname"
        onion = _normalize_onion(_wait_for_file(hostname_file, self.start_timeout_seconds))
        if not is_onion_url(onion):
            raise RuntimeError("tor did not publish an onion address")
        return pid, onion

    def _resolve_binary(self, binary: str) -> str:
        """Resolve a backend binary without trusting PATH alone."""
        candidate = str(binary or "").strip()
        if not candidate:
            raise RuntimeError("backend binary is not configured")
        if self._launcher is not _default_launcher and "/" not in candidate:
            return candidate
        if "/" in candidate:
            path = Path(candidate)
            if path.is_file():
                return str(path)
            raise RuntimeError(f"backend binary not found: {candidate}")
        found = shutil.which(candidate)
        if found:
            return found
        raise RuntimeError(f"backend binary not found: {candidate}")

    def _pid_live(self, pid: int) -> bool:
        """Return whether a tracked pid still exists."""
        if pid <= 0:
            return False
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return False
        except PermissionError:
            return True
        except OSError:
            return False
        return True


def _fingerprint(value: str) -> str:
    """Return a short non-reversible fingerprint for audit records."""
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return digest[:12]


def _normalize_onion(raw: str) -> str:
    """Normalize a Tor hostname file payload to a full onion URL."""
    text = str(raw or "").strip()
    if _BARE_ONION_PATTERN.match(text):
        return f"http://{text}"
    return text


def _wait_for_pattern(path: str, pattern: re.Pattern[str], timeout_seconds: int) -> Optional[str]:
    """Poll a log file for the first regex match within a timeout."""
    import time as _time

    deadline = _time.monotonic() + max(1, int(timeout_seconds))
    while _time.monotonic() <= deadline:
        try:
            text = Path(path).read_text(encoding="utf-8", errors="replace")
        except (FileNotFoundError, OSError):
            _time.sleep(0.2)
            continue
        match = pattern.search(text)
        if match:
            return match.group(0)
        _time.sleep(0.2)
    return None


def _wait_for_file(path: Path, timeout_seconds: int) -> str:
    """Poll for a small text file such as the onion hostname file."""
    import time as _time

    deadline = _time.monotonic() + max(1, int(timeout_seconds))
    while _time.monotonic() <= deadline:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except (FileNotFoundError, OSError):
            _time.sleep(0.2)
            continue
        if text.strip():
            return text
        _time.sleep(0.2)
    return ""
