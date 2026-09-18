#!/usr/bin/env python
"""Doctor: verify and repair the QuantumVault operator environment.

Used by ``make doctor`` (check only) and ``make doctor-fix`` (check
plus install every missing piece that has an unattended installer).

Stdlib only, so it runs even when no project dependency is installed.
Every knob is overridable through the environment; module-level
constants are the single source of truth for defaults.

Checks cover Python modules, system binaries (openssl, redis-server,
tor, cloudflared, docker, node), the ``.env`` file, and TCP
reachability of Redis and the Garage S3 endpoint. ``--fix`` installs
Python dependencies from ``requirements.txt``, Debian packages via
apt, the cloudflared binary from the official Cloudflare release,
and the garage binary from the official release server. Anything
that cannot be installed unattended is reported in plain English
with the exact command to run or the instruction to contact the
server administrator.
"""

from __future__ import annotations

import argparse
import importlib
import os
import platform
import shutil
import socket
import subprocess
import sys
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent

_MIN_PYTHON = (3, 10)
_DEFAULT_STORAGE_URI = "redis://localhost:6379"
_DEFAULT_S3_ENDPOINT_URL = "http://localhost:3900"
_DEFAULT_CLOUDFLARED_VERSION = os.environ.get(
    "QV_DOCTOR_CLOUDFLARED_VERSION", "latest"
)
_DEFAULT_GARAGE_VERSION = os.environ.get("QV_DOCTOR_GARAGE_VERSION", "1.0.1")
_DEFAULT_GARAGE_BIN = os.environ.get(
    "QV_DOCTOR_GARAGE_BIN", str(_PROJECT_ROOT / ".run" / "garage-bin" / "garage")
)
_DEFAULT_BIN_DIR = os.environ.get(
    "QV_DOCTOR_BIN_DIR", str(Path.home() / ".local" / "bin")
)
_APT_PACKAGES = ("openssl", "tor", "redis-server")
_CLOUDFLARE_RELEASE_BASE = (
    "https://github.com/cloudflare/cloudflared/releases"
)
_GARAGE_RELEASE_BASE = "https://garagehq.deuxfleurs.fr/_releases"
_ARCH_DEB_MAP = {"x86_64": "amd64", "aarch64": "arm64"}
_ARCH_GARAGE_MAP = {"x86_64": "linux-amd64", "aarch64": "linux-arm64"}

MODULES = [
    "flask",
    "flask_login",
    "flask_wtf",
    "flask_cors",
    "flask_limiter",
    "flask_mail",
    "pydantic",
    "cryptography",
    "boto3",
    "botocore",
    "redis",
    "pytz",
    "dotenv",
    "apscheduler",
    "paypalrestsdk",
    "clicksend_client",
    "werkzeug",
    "utils.utils",
    "utils.srp6a",
    "utils.scheduler",
    "utils.mailer",
    "utils.cache",
    "models.user",
    "models.message",
    "models.plans",
    "models.contact",
    "controllers.auth",
    "controllers.file",
    "controllers.message",
    "controllers.sync",
    "controllers.contact",
    "controllers.secure_channel",
    "controllers.facade",
    "controllers.cover",
]


@dataclass(frozen=True)
class CheckResult:
    """Outcome of one environment check with a repair hint."""

    name: str
    ok: bool
    detail: str
    remedy: str = ""


@dataclass
class DoctorReport:
    """Accumulated check results with derived exit status."""

    results: list[CheckResult] = field(default_factory=list)

    def add(self, result: CheckResult) -> None:
        """Append one check result."""
        self.results.append(result)

    @property
    def failures(self) -> list[CheckResult]:
        """Return every failing check."""
        return [item for item in self.results if not item.ok]

    @property
    def exit_code(self) -> int:
        """Return 0 when every check passes, 1 otherwise."""
        return 0 if not self.failures else 1


def load_env_file(path: Path) -> dict[str, str]:
    """Parse a dotenv file into a dict without third-party imports."""
    values: dict[str, str] = {}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return values
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key:
            values[key] = value
    return values


def effective_env() -> dict[str, str]:
    """Return process env overlaid with ``.env`` file values."""
    merged = load_env_file(_PROJECT_ROOT / ".env")
    merged.update(os.environ)
    return merged


def check_python(minimum: tuple[int, int] = _MIN_PYTHON) -> CheckResult:
    """Verify the interpreter meets the minimum supported version."""
    current = sys.version_info[:2]
    ok = current >= minimum
    return CheckResult(
        name="python",
        ok=ok,
        detail=".".join(str(part) for part in current),
        remedy=(
            ""
            if ok
            else "Install Python 3.10 or newer, or contact your administrator."
        ),
    )


def check_module(name: str) -> CheckResult:
    """Verify one Python module imports cleanly."""
    if str(_PROJECT_ROOT) not in sys.path:
        sys.path.insert(0, str(_PROJECT_ROOT))
    try:
        importlib.import_module(name)
    except Exception as exc:
        return CheckResult(
            name=f"python:{name}",
            ok=False,
            detail=f"{type(exc).__name__}: {exc}",
            remedy="Run `make doctor-fix` (reinstalls requirements.txt).",
        )
    return CheckResult(name=f"python:{name}", ok=True, detail="import ok")


def check_binary(name: str, env_override: str = "") -> CheckResult:
    """Verify one system binary resolves via PATH or an override path."""
    candidates = [env_override] if env_override else []
    candidates.append(name)
    for candidate in candidates:
        if not candidate:
            continue
        if "/" in candidate:
            if Path(candidate).is_file():
                return CheckResult(
                    name=f"bin:{name}", ok=True, detail=candidate
                )
            continue
        found = shutil.which(candidate)
        if found:
            return CheckResult(name=f"bin:{name}", ok=True, detail=found)
    return CheckResult(
        name=f"bin:{name}",
        ok=False,
        detail="not found on PATH",
        remedy="Run `make doctor-fix` or contact your administrator.",
    )


def check_env_file() -> CheckResult:
    """Verify the operator ``.env`` file exists."""
    path = _PROJECT_ROOT / ".env"
    if path.is_file():
        return CheckResult(name="env", ok=True, detail=str(path))
    return CheckResult(
        name="env",
        ok=False,
        detail="missing .env",
        remedy="Run `make env` to create it from .env.example.",
    )


def parse_host_port(uri: str, default_port: int) -> tuple[str, int]:
    """Extract a TCP host and port from a Redis or HTTP(S) URL."""
    work = uri.strip()
    for scheme in ("redis://", "http://", "https://"):
        if work.startswith(scheme):
            work = work[len(scheme):]
            break
    work = work.split("/", 1)[0]
    if "@" in work:
        work = work.rsplit("@", 1)[1]
    if ":" in work:
        host, _, port_text = work.rpartition(":")
        try:
            return host or "localhost", int(port_text)
        except ValueError:
            return host or "localhost", default_port
    return work or "localhost", default_port


def check_tcp(name: str, host: str, port: int, timeout: float = 3.0) -> CheckResult:
    """Verify a TCP endpoint accepts connections."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return CheckResult(
                name=name, ok=True, detail=f"{host}:{port} reachable"
            )
    except OSError as exc:
        return CheckResult(
            name=name,
            ok=False,
            detail=f"{host}:{port} refused ({exc})",
            remedy=(
                "Start the service (e.g. `make garage-up`, `make redis-up`, "
                "or `make compose-up`), or contact your administrator."
            ),
        )


def debian_arch(deb: bool = True) -> str:
    """Map the host CPU to a Cloudflare or Garage release architecture."""
    machine = platform.machine()
    mapping = _ARCH_DEB_MAP if deb else _ARCH_GARAGE_MAP
    if machine not in mapping:
        raise ValueError(f"unsupported architecture: {machine}")
    return mapping[machine]


def cloudflared_deb_url(version: str, arch: str) -> str:
    """Build the official cloudflared .deb URL for a version and arch."""
    if version == "latest":
        return (
            f"{_CLOUDFLARE_RELEASE_BASE}/latest/download/"
            f"cloudflared-linux-{arch}.deb"
        )
    return (
        f"{_CLOUDFLARE_RELEASE_BASE}/download/{version}/"
        f"cloudflared-linux-{arch}.deb"
    )


def garage_bin_url(version: str, target: str) -> str:
    """Build the official garage binary URL for a version and target."""
    return f"{_GARAGE_RELEASE_BASE}/v{version}/{target}/garage"


def apt_command(packages: tuple[str, ...]) -> list[str]:
    """Build an apt install command, prefixed with sudo outside root."""
    base = ["apt-get", "install", "-y", *packages]
    if os.geteuid() == 0:
        return base
    if shutil.which("sudo"):
        return ["sudo", *base]
    return base


def run_command(cmd: list[str]) -> tuple[bool, str]:
    """Run one shell command and capture its outcome."""
    try:
        completed = subprocess.run(
            cmd, capture_output=True, text=True, check=False
        )
    except FileNotFoundError as exc:
        return False, str(exc)
    if completed.returncode != 0:
        tail = (completed.stderr or completed.stdout or "").strip().splitlines()
        last = tail[-1] if tail else f"exit {completed.returncode}"
        if "a password is required" in last:
            last = (
                "sudo needs your login password; run "
                f"`{' '.join(cmd)}` in your own terminal, "
                "or contact your administrator."
            )
        return False, last
    return True, "ok"


def download_file(url: str, destination: Path) -> tuple[bool, str]:
    """Fetch a URL with curl when present, else urllib."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    curl = shutil.which("curl")
    if curl:
        return run_command(
            [curl, "-fSL", "--retry", "3", "-o", str(destination), url]
        )
    try:
        urllib.request.urlretrieve(url, str(destination))
    except Exception as exc:
        return False, str(exc)
    return True, "ok"


def upsert_env(key: str, value: str, path: Path | None = None) -> None:
    """Set one KEY=value pair in ``.env``, preserving other lines."""
    target = path or (_PROJECT_ROOT / ".env")
    try:
        lines = target.read_text(encoding="utf-8").splitlines()
    except OSError:
        lines = []
    prefix = f"{key}="
    replaced = False
    for index, line in enumerate(lines):
        if line.strip() == key or line.strip().startswith(prefix):
            lines[index] = f"{key}={value}"
            replaced = True
    if not replaced:
        lines.append(f"{key}={value}")
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")


def fix_python_deps() -> tuple[bool, str]:
    """Install project requirements with the running interpreter."""
    requirements = _PROJECT_ROOT / "requirements.txt"
    return run_command(
        [sys.executable, "-m", "pip", "install", "-r", str(requirements)]
    )


def fix_apt(packages: tuple[str, ...] = _APT_PACKAGES) -> tuple[bool, str]:
    """Install Debian system packages, using sudo outside root."""
    if not shutil.which("apt-get"):
        return False, "apt-get not found; contact your administrator."
    if os.geteuid() != 0 and not shutil.which("sudo"):
        return (
            False,
            "need root for apt-get and sudo is missing; "
            "contact your administrator.",
        )
    return run_command(apt_command(packages))


def fix_cloudflared(
    version: str = _DEFAULT_CLOUDFLARED_VERSION,
    bin_dir: str = _DEFAULT_BIN_DIR,
) -> tuple[bool, str]:
    """Install the cloudflared binary into a user-writable bin directory."""
    try:
        arch = debian_arch(deb=True)
    except ValueError as exc:
        return False, str(exc)
    url = cloudflared_deb_url(version, arch)
    target_dir = Path(bin_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    deb_path = target_dir / "cloudflared-doctor.deb"
    ok, detail = download_file(url, deb_path)
    if not ok:
        return False, detail
    dpkg_deb = shutil.which("dpkg-deb")
    binary = target_dir / "cloudflared"
    if dpkg_deb:
        ok, detail = run_command(
            [dpkg_deb, "-x", str(deb_path), str(target_dir / "cloudflared-pkg")]
        )
        if not ok:
            return False, detail
        extracted = target_dir / "cloudflared-pkg" / "usr" / "bin" / "cloudflared"
        if not extracted.is_file():
            return False, "unexpected .deb layout; contact your administrator."
        binary.write_bytes(extracted.read_bytes())
        binary.chmod(0o755)
    else:
        ok, detail = run_command(
            ["dpkg", "-i", str(deb_path)]
            if os.geteuid() == 0 or not shutil.which("sudo")
            else ["sudo", "dpkg", "-i", str(deb_path)]
        )
        if not ok:
            return False, detail
    try:
        deb_path.unlink()
    except OSError:
        pass
    return True, str(binary)


def fix_garage(
    version: str = _DEFAULT_GARAGE_VERSION,
    destination: str = _DEFAULT_GARAGE_BIN,
) -> tuple[bool, str]:
    """Download the garage binary and verify it against its checksum."""
    try:
        target = debian_arch(deb=False)
    except ValueError as exc:
        return False, str(exc)
    url = garage_bin_url(version, target)
    dest = Path(destination)
    ok, detail = download_file(url, dest)
    if not ok:
        return False, detail
    checksum_url = f"{url}.sha256sum"
    checksum_path = dest.with_suffix(".sha256sum")
    ok, _ = download_file(checksum_url, checksum_path)
    if ok:
        try:
            expected = checksum_path.read_text(encoding="utf-8").split()[0]
        except (OSError, IndexError):
            expected = ""
        if expected:
            import hashlib

            actual = hashlib.sha256(dest.read_bytes()).hexdigest()
            if actual != expected:
                return False, "checksum mismatch; contact your administrator."
    dest.chmod(0o755)
    return True, str(dest)


def collect_report() -> DoctorReport:
    """Run every check and return the aggregated report."""
    env = effective_env()
    report = DoctorReport()
    report.add(check_python())
    report.add(check_env_file())
    for name in MODULES:
        report.add(check_module(name))
    for binary in ("openssl", "redis-server", "docker", "node"):
        report.add(check_binary(binary))
    report.add(
        check_binary("tor", env.get("QV_CHANNEL_TOR_BIN", ""))
    )
    report.add(
        check_binary(
            "cloudflared", env.get("QV_CHANNEL_CLOUDFLARED_BIN", "")
        )
    )
    storage = env.get("STORAGE_URI", _DEFAULT_STORAGE_URI)
    host, port = parse_host_port(storage, 6379)
    report.add(check_tcp("redis", host, port))
    endpoint = env.get("S3_ENDPOINT_URL", _DEFAULT_S3_ENDPOINT_URL)
    host, port = parse_host_port(endpoint, 3900)
    report.add(check_tcp("garage-s3", host, port))
    return report


def print_report(report: DoctorReport) -> None:
    """Render the report in plain English for operators."""
    for item in report.results:
        mark = "ok  " if item.ok else "FAIL"
        print(f"[{mark}] {item.name}: {item.detail}")
        if not item.ok and item.remedy:
            print(f"       -> {item.remedy}")
    if report.failures:
        print(
            f"\n{len(report.failures)} problem(s) found. "
            "Run `make doctor-fix` to install what is missing, "
            "or contact your administrator."
        )
    else:
        print("\nDoctor: every check passed.")


def apply_fixes(report: DoctorReport) -> DoctorReport:
    """Install every missing piece that has an unattended installer."""
    names = {item.name for item in report.failures}
    if any(name.startswith("python:") for name in names):
        print("[fix] installing Python requirements ...")
        ok, detail = fix_python_deps()
        print(f"[fix] requirements: {'ok' if ok else 'FAILED: ' + detail}")
    apt_missing = {
        "bin:openssl": "openssl",
        "bin:tor": "tor",
        "bin:redis-server": "redis-server",
    }
    wanted = tuple(
        pkg for key, pkg in apt_missing.items() if key in names
    )
    if wanted:
        print(f"[fix] installing system packages: {' '.join(wanted)} ...")
        ok, detail = fix_apt(wanted)
        print(f"[fix] apt: {'ok' if ok else 'FAILED: ' + detail}")
    if "bin:cloudflared" in names:
        print("[fix] installing cloudflared ...")
        ok, detail = fix_cloudflared()
        print(f"[fix] cloudflared: {'ok' if ok else 'FAILED: ' + detail}")
        if ok:
            upsert_env("QV_CHANNEL_CLOUDFLARED_BIN", detail)
            print(f"[fix] pinned QV_CHANNEL_CLOUDFLARED_BIN={detail} in .env")
    garage_binary_missing = (
        not Path(_DEFAULT_GARAGE_BIN).is_file()
        and shutil.which("garage") is None
    )
    if garage_binary_missing:
        print("[fix] downloading garage binary ...")
        ok, detail = fix_garage()
        print(f"[fix] garage: {'ok' if ok else 'FAILED: ' + detail}")
    return collect_report()


def main(argv: list[str] | None = None) -> int:
    """Entry point for ``make doctor`` and ``make doctor-fix``."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fix",
        action="store_true",
        help="install every missing piece, then re-check",
    )
    args = parser.parse_args(argv)
    report = collect_report()
    if args.fix and report.failures:
        report = apply_fixes(report)
    print_report(report)
    return report.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
