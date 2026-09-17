# Subsystem: scripts

## scripts/doctor.py
- Layer: utility
- Doc: Doctor: import every project module and report the first error.  Used by `make doctor`. Exits 0 on success, 1 on any imp
- Language: py

## scripts/email_tool.py
- Layer: presentation
- Doc: Operator email tooling for QuantumVault.  Three subcommands, all runnable from any Linux host or AWS VPS that has the pr
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
- Layer: utility
- Doc: Bootstrap a fresh Garage deployment for QuantumVault.  What this does: 1. Waits for the admin API to respond. 2. Connect
- Language: sh
- Symbols:
  - `upsert_env` (function, line 35)

## scripts/garage-native.sh
- Layer: utility
- Doc: Run Garage (S3-compatible object storage) natively, without Docker.  Idempotent: if the S3 API is already reachable on :
- Language: sh
- Symbols:
  - `upsert_env` (function, line 46)
  - `s3_reachable` (function, line 56)
  - `gcmd` (function, line 141)

## scripts/makeadmin.py
- Layer: utility
- Doc: Operator tooling to promote QuantumVault users to a privileged role.  Two subcommands, runnable from any Linux host that
- Language: py
- Symbols:
  - `_resolve_db_path` (function, line 51) `def _resolve_db_path()`
  - `_print_user_summary` (function, line 64) `def _print_user_summary(user)`
  - `cmd_promote` (function, line 75) `def cmd_promote(args)`
  - `build_parser` (function, line 126) `def build_parser()`
  - `main` (function, line 152) `def main()`
- Depends on: `models/user.py`

## scripts/test_bloque1.py
- Layer: testing
- Doc: Bloque 1 test: superadmin_edit_user endpoint.  Renders the user-edit form via Flask's test client, then verifies GET (20
- Language: py
- Symbols:
  - `_FakeUser` (class, line 48) `class _FakeUser`
  - `_load_user` (method, line 62) `def _load_user(uid)`
  - `check` (method, line 86) `def check(name, ok, detail)`
  - `__init__` (method, line 49) `def __init__(self, row)`
  - `is_authenticated` (method, line 54) `def is_authenticated(self)`
  - `is_active` (method, line 56) `def is_active(self)`
  - `is_anonymous` (method, line 58) `def is_anonymous(self)`
  - `get_id` (method, line 59) `def get_id(self)`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`
