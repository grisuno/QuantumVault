"""Behaviour contracts for scripts/doctor.py.

Covers binary and module checks, host/port parsing, release URL
builders, apt command construction, and report exit status. No
test touches the network, sudo, or package managers.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "qv_doctor", str(Path(__file__).resolve().parent.parent / "scripts" / "doctor.py")
)
assert _SPEC is not None and _SPEC.loader is not None
_doctor = importlib.util.module_from_spec(_SPEC)
sys.modules["qv_doctor"] = _doctor
_SPEC.loader.exec_module(_doctor)


def test_check_binary_finds_present_binary() -> None:
    """A binary on PATH reports ok with its resolved path."""
    result = _doctor.check_binary("python3")
    assert result.ok is True
    assert result.detail != ""


def test_check_binary_flags_missing_binary() -> None:
    """An unknown binary fails and points at doctor-fix in English."""
    result = _doctor.check_binary("qv-definitely-missing-binary-xyz")
    assert result.ok is False
    assert "make doctor-fix" in result.remedy
    assert "administrator" in result.remedy


def test_check_binary_honors_absolute_override(tmp_path) -> None:
    """Absolute override paths resolve without trusting PATH."""
    present = tmp_path / "tool-fake"
    present.write_text("x", encoding="utf-8")
    assert _doctor.check_binary("tool", str(present)).ok is True
    assert (
        _doctor.check_binary("tool", str(tmp_path / "nope")).ok is False
    )


def test_check_module_reports_status() -> None:
    """Present stdlib modules pass, unknown ones fail with a remedy."""
    assert _doctor.check_module("json").ok is True
    missing = _doctor.check_module("qv_definitely_missing_module_xyz")
    assert missing.ok is False
    assert "make doctor-fix" in missing.remedy


def test_check_python_accepts_current_runtime() -> None:
    """The running interpreter satisfies its own minimum version."""
    assert _doctor.check_python((3, 8)).ok is True
    assert _doctor.check_python((99, 0)).ok is False


def test_parse_host_port_shapes() -> None:
    """Redis and HTTP URLs reduce to host plus port."""
    assert _doctor.parse_host_port("redis://localhost:6379", 6379) == (
        "localhost",
        6379,
    )
    assert _doctor.parse_host_port("http://localhost:3900/quantumvault", 3900) == (
        "localhost",
        3900,
    )
    assert _doctor.parse_host_port("redis://:secret@db.internal:6381/0", 6379) == (
        "db.internal",
        6381,
    )
    assert _doctor.parse_host_port("garbage", 1234) == ("garbage", 1234)
    assert _doctor.parse_host_port("redis://host:notaport", 6379) == (
        "host",
        6379,
    )


def test_check_tcp_refused_reports_remedy() -> None:
    """A closed loopback port fails with operator guidance."""
    result = _doctor.check_tcp("probe", "127.0.0.1", 9, timeout=0.5)
    assert result.ok is False
    assert "administrator" in result.remedy


def test_release_url_builders() -> None:
    """Release URLs follow the official vendor layouts."""
    assert _doctor.cloudflared_deb_url("latest", "amd64").endswith(
        "cloudflared-linux-amd64.deb"
    )
    assert "2026.1.0" in _doctor.cloudflared_deb_url("2026.1.0", "arm64")
    assert _doctor.garage_bin_url("1.0.1", "linux-amd64").endswith(
        "v1.0.1/linux-amd64/garage"
    )
    try:
        _doctor.debian_arch(deb=True)
    except ValueError:
        pass


def test_apt_command_uses_sudo_outside_root() -> None:
    """Apt installs escalate with sudo unless already root."""
    import os as _os

    cmd = _doctor.apt_command(("tor",))
    assert cmd[-2:] == ["-y", "tor"] or cmd[-1] == "tor"
    if _os.geteuid() != 0:
        assert cmd[0] == "sudo"


def test_report_exit_code_reflects_failures() -> None:
    """An empty failure set exits zero, any failure exits one."""
    report = _doctor.DoctorReport()
    report.add(_doctor.CheckResult(name="a", ok=True, detail="fine"))
    assert report.exit_code == 0
    assert report.failures == []
    report.add(
        _doctor.CheckResult(name="b", ok=False, detail="broken", remedy="fix it")
    )
    assert report.exit_code == 1
    assert len(report.failures) == 1
    assert {item.name for item in report.failures} == {"b"}


def test_load_env_file_parses_assignments(tmp_path) -> None:
    """Comment and blank lines are skipped, quotes are stripped."""
    env_file = tmp_path / ".env"
    env_file.write_text(
        "# comment\n\nFOO=bar\nQUOTED='a b'\nEMPTY=\n", encoding="utf-8"
    )
    values = _doctor.load_env_file(env_file)
    assert values == {"FOO": "bar", "QUOTED": "a b", "EMPTY": ""}
    assert _doctor.load_env_file(tmp_path / "absent") == {}


def test_upsert_env_replaces_and_appends(tmp_path) -> None:
    """Existing keys are replaced in place, new keys are appended."""
    env_file = tmp_path / ".env"
    env_file.write_text("A=1\nB=2\n", encoding="utf-8")
    _doctor.upsert_env("B", "22", path=env_file)
    _doctor.upsert_env("C", "3", path=env_file)
    assert env_file.read_text(encoding="utf-8") == "A=1\nB=22\nC=3\n"
