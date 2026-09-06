# Subsystem: utils

## utils/__init__.py
- Layer: utility
- Language: py

## utils/cache.py
- Layer: infrastructure
- Doc: /home/grisun0/src/postcuantum/v1/utils/cache.py
- Language: py
- Symbols:
  - `Cache` (class, line 6) `class Cache`
  - `__init__` (method, line 8) `def __init__(self)`
  - `get` (method, line 11) `def get(self, key)`
  - `set` (method, line 16) `def set(self, key, value, ttl)`
  - `delete` (method, line 20) `def delete(self, key)`

## utils/mailer.py
- Layer: presentation
- Language: py
- Symbols:
  - `external_url` (function, line 22) `def external_url(path)`
  - `mail_is_configured` (function, line 38) `def mail_is_configured()`
  - `send_transactional_email` (function, line 51) `def send_transactional_email(subject, recipients, body)`
- Imported by: `controllers/auth.py`, `scripts/email_tool.py`, `utils/scheduler.py`, `views/auth.py`

## utils/plans.py
- Layer: utility
- Language: py
- Symbols:
  - `SubscriptionPlans` (class, line 3) `class SubscriptionPlans`
  - `get_plan` (method, line 30) `def get_plan(plan_name)`
  - `validate_plan_payment` (method, line 42) `def validate_plan_payment(plan_name, amount_paid)`

## utils/scheduler.py
- Layer: presentation
- Language: py
- Symbols:
  - `_now_utc` (function, line 32) `def _now_utc()`
  - `init_scheduler` (function, line 37) `def init_scheduler(app, mail)`
  - `_is_trial_elapsed` (function, line 54) `def _is_trial_elapsed(user)`
  - `check_trial_expiration` (function, line 72) `def check_trial_expiration()`
  - `cleanup_old_messages` (function, line 118) `def cleanup_old_messages()`
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

## utils/security.py
- Layer: presentation
- Language: py
- Symbols:
  - `_get_audit_logger` (function, line 46) `def _get_audit_logger()`
  - `_correlation_id` (function, line 72) `def _correlation_id()`
  - `audit_event` (function, line 86) `def audit_event(event)`
  - `constant_time_compare` (function, line 123) `def constant_time_compare(a, b)`
  - `hash_secret` (function, line 135) `def hash_secret(secret)`
  - `verify_secret` (function, line 156) `def verify_secret(secret, expected_hash)`
  - `new_one_time_code` (function, line 163) `def new_one_time_code(length)`
  - `_extract_csrf_token` (function, line 172) `def _extract_csrf_token()`
  - `json_csrf_protect` (function, line 193) `def json_csrf_protect(view)`
  - `wrapper` (function, line 207) `def wrapper()`
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

## utils/srp6a.py
- Layer: utility
- Language: py
- Symbols:
  - `i2osp` (function, line 47) `def i2osp(value)`
  - `_hash` (function, line 60) `def _hash()`
  - `_hash_int` (function, line 68) `def _hash_int()`
  - `compute_k` (function, line 73) `def compute_k()`
  - `compute_u` (function, line 78) `def compute_u(server_a, server_b)`
  - `generate_server_challenge` (function, line 91) `def generate_server_challenge(verifier)`
  - `compute_proofs` (function, line 107) `def compute_proofs(username, salt_hex, verifier, server_a, server_b, server_b_secret)`
  - `SRPSessionStore` (class, line 150) `class SRPSessionStore`
  - `hello` (method, line 224) `def hello(store, username, client_a_hex, salt_hex, verifier_hex)`
  - `verify` (method, line 260) `def verify(store, username, client_m1_hex)`
  - `__init__` (method, line 158) `def __init__(self, storage_uri)`
  - `_key` (method, line 168) `def _key(username)`
  - `save` (method, line 172) `def save(self, username, salt_hex, verifier_hex, server_a_hex, server_b_hex, server_b_secret_hex)`
  - `load` (method, line 202) `def load(self, username)`

## utils/utils.py
- Layer: utility
- Doc: utils/utils.py
- Language: py
- Symbols:
  - `as_bool` (function, line 11) `def as_bool(value, default)`
  - `sanitize_path` (function, line 31) `def sanitize_path(path)`
  - `Payload` (class, line 62) `class Payload(TypedDict)`
  - `Config` (class, line 85) `class Config`
  - `load_payload` (method, line 150) `def load_payload()`
  - `__init__` (method, line 127) `def __init__(self, config_dict)`
  - `__getitem__` (method, line 147) `def __getitem__(self, key)`
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/file.py`, `scripts/email_tool.py`, `tests/test_srp.py`, `utils/security.py`, `views/admin.py`, `views/sync.py`
