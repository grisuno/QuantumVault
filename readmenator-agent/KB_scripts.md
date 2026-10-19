# Subsystem: scripts

## scripts/doctor.py
- Doc: Doctor: verify and repair the QuantumVault operator environment.
- Layer: utility
- Language: py
- Symbols:
  - `CheckResult` (class, line 98) `class CheckResult`
  - `DoctorReport` (class, line 108) `class DoctorReport`
  - `load_env_file` (function, line 128) `def load_env_file(path)`
  - `effective_env` (function, line 147) `def effective_env()`
  - `check_python` (function, line 154) `def check_python(minimum)`
  - `check_module` (function, line 170) `def check_module(name)`
  - `check_binary` (function, line 186) `def check_binary(name, env_override)`
  - `check_env_file` (function, line 210) `def check_env_file()`
  - `parse_host_port` (function, line 223) `def parse_host_port(uri, default_port)`
  - `check_tcp` (function, line 242) `def check_tcp(name, host, port, timeout)`
  - `debian_arch` (function, line 261) `def debian_arch(deb)`
  - `cloudflared_deb_url` (function, line 270) `def cloudflared_deb_url(version, arch)`
  - `garage_bin_url` (function, line 283) `def garage_bin_url(version, target)`
  - `apt_command` (function, line 288) `def apt_command(packages)`
  - `run_command` (function, line 298) `def run_command(cmd)`
  - `download_file` (function, line 319) `def download_file(url, destination)`
  - `upsert_env` (function, line 334) `def upsert_env(key, value, path)`
  - `fix_python_deps` (function, line 352) `def fix_python_deps()`
  - `fix_apt` (function, line 360) `def fix_apt(packages)`
  - `fix_cloudflared` (function, line 373) `def fix_cloudflared(version, bin_dir)`
  - `fix_garage` (function, line 417) `def fix_garage(version, destination)`
  - `collect_report` (function, line 449) `def collect_report()`
  - `print_report` (function, line 476) `def print_report(report)`
  - `apply_fixes` (function, line 493) `def apply_fixes(report)`
  - `main` (function, line 530) `def main(argv)`
  - `add` (method, line 113) `def add(self, result)`
  - `failures` (method, line 118) `def failures(self)`
  - `exit_code` (method, line 123) `def exit_code(self)`

## scripts/email_tool.py
- Doc: Operator email tooling for QuantumVault.
- Layer: presentation
- Language: py
- Symbols:
  - `_build_mail_app` (function, line 40) `def _build_mail_app(config)`
  - `cmd_test_smtp` (function, line 63) `def cmd_test_smtp(args)`
  - `cmd_link` (function, line 91) `def cmd_link(args)`
  - `cmd_confirm` (function, line 114) `def cmd_confirm(args)`
  - `build_parser` (function, line 133) `def build_parser()`
  - `main` (function, line 153) `def main()`
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

## scripts/garage-init.sh
- Doc: Bootstrap a fresh Garage deployment for QuantumVault.
- Layer: utility
- Language: sh
- Symbols:
  - `upsert_env` (function, line 35)

## scripts/garage-native.sh
- Doc: Run Garage (S3-compatible object storage) natively, without Docker.
- Layer: utility
- Language: sh
- Symbols:
  - `upsert_env` (function, line 46)
  - `s3_reachable` (function, line 56)
  - `gcmd` (function, line 141)

## scripts/makeadmin.py
- Doc: Operator tooling to promote QuantumVault users to a privileged role.
- Layer: utility
- Language: py
- Symbols:
  - `_resolve_db_path` (function, line 51) `def _resolve_db_path()`
  - `_print_user_summary` (function, line 64) `def _print_user_summary(user)`
  - `cmd_promote` (function, line 75) `def cmd_promote(args)`
  - `build_parser` (function, line 126) `def build_parser()`
  - `main` (function, line 152) `def main()`
- Depends on: `models/user.py`

## scripts/test_bloque1.py
- Doc: Bloque 1 test: superadmin_edit_user endpoint.
- Layer: testing
- Language: py
- Symbols:
  - `_FakeUser` (class, line 48) `class _FakeUser`
  - `_load_user` (function, line 62) `def _load_user(uid)`
  - `check` (function, line 86) `def check(name, ok, detail)`
  - `__init__` (method, line 49) `def __init__(self, row)`
  - `is_authenticated` (method, line 54) `def is_authenticated(self)`
  - `is_active` (method, line 56) `def is_active(self)`
  - `is_anonymous` (method, line 58) `def is_anonymous(self)`
  - `get_id` (method, line 59) `def get_id(self)`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`
