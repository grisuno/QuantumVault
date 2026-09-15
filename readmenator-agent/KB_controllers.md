# Subsystem: controllers

## controllers/__init__.py
- Layer: presentation
- Language: py

## controllers/auth.py
- Layer: presentation
- Language: py
- Symbols:
  - `_now_utc` (function, line 49) `def _now_utc()`
  - `AuthController` (class, line 58) `class AuthController`
  - `__init__` (method, line 61) `def __init__(self, db_path, mail, storage_uri)`
  - `register` (method, line 76) `def register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, recovery_salt, encrypted_private_key_recovery)`
  - `send_confirmation_email` (method, line 156) `def send_confirmation_email(self, email, username, token)`
  - `srp_hello` (method, line 202) `def srp_hello(self, username, client_a_hex)`
  - `srp_verify` (method, line 221) `def srp_verify(self, username, client_m1_hex)`
  - `send_sms_verification` (method, line 253) `def send_sms_verification(self, phone, code, username)`
  - `verify_phone_code` (method, line 274) `def verify_phone_code(self, username, code)`
  - `resend_phone_code` (method, line 310) `def resend_phone_code(self, username)`
  - `_is_code_valid` (method, line 349) `def _is_code_valid(self, expires_at)`
  - `verify_mfa_code` (method, line 369) `def verify_mfa_code(self, username, code)`
  - `send_mfa_code` (method, line 393) `def send_mfa_code(self, username)`
  - `toggle_mfa` (method, line 416) `def toggle_mfa(self, username, enable)`
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

## controllers/contact.py
- Layer: presentation
- Language: py
- Symbols:
  - `ContactController` (class, line 4) `class ContactController`
  - `__init__` (method, line 6) `def __init__(self, db_path)`
  - `create_contact` (method, line 14) `def create_contact(self, user_id, subject, message)`
  - `get_user_contacts` (method, line 36) `def get_user_contacts(self, user_id)`
- Depends on: `models/contact.py`
- Imported by: `views/admin.py`, `views/auth.py`

## controllers/deniable_vault.py
- Layer: presentation
- Language: py
- Symbols:
  - `_base64_length` (function, line 81) `def _base64_length(byte_length)`
  - `canonical_json` (function, line 86) `def canonical_json(envelope)`
  - `EnvelopeValidationError` (class, line 104) `class EnvelopeValidationError(ValueError)`
  - `_coerce_int` (method, line 108) `def _coerce_int(value, default)`
  - `_coerce_kdf` (method, line 118) `def _coerce_kdf(value, default)`
  - `DeniableVaultConfig` (class, line 134) `class DeniableVaultConfig`
  - `EnvelopeValidator` (class, line 272) `class EnvelopeValidator`
  - `DeniableVaultController` (class, line 393) `class DeniableVaultController`
  - `from_mapping` (method, line 148) `def from_mapping(cls, mapping, env)`
  - `expected_ct_b64_length` (method, line 213) `def expected_ct_b64_length(self)`
  - `random_container` (method, line 222) `def random_container(self)`
  - `public_parameters` (method, line 250) `def public_parameters(self)`
  - `__init__` (method, line 281) `def __init__(self, config)`
  - `validate` (method, line 285) `def validate(self, envelope)`
  - `_validate_slot` (method, line 339) `def _validate_slot(self, index, slot)`
  - `_validate_hex` (method, line 376) `def _validate_hex(value, expected_length, index, field)`
  - `__init__` (method, line 401) `def __init__(self, db, config, validator)`
  - `load_or_provision` (method, line 419) `def load_or_provision(self, username)`
  - `save` (method, line 441) `def save(self, username, envelope)`
  - `reset` (method, line 456) `def reset(self, username)`
  - `exists` (method, line 474) `def exists(self, username)`
  - `read` (method, line 171) `def read(key)`
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

## controllers/facade.py
- Layer: presentation
- Language: py
- Symbols:
  - `GateOutcome` (class, line 63) `class GateOutcome(Enum)`
  - `GateDecision` (class, line 72) `class GateDecision`
  - `_as_bool` (method, line 79) `def _as_bool(value, default)`
  - `_as_int` (method, line 88) `def _as_int(value, default)`
  - `_as_text` (method, line 98) `def _as_text(value, default)`
  - `_as_raw_text` (method, line 106) `def _as_raw_text(value, default)`
  - `_as_paths` (method, line 111) `def _as_paths(value, default)`
  - `FacadeConfig` (class, line 124) `class FacadeConfig`
  - `GatePhraseHasher` (class, line 262) `class GatePhraseHasher`
  - `GateTicket` (class, line 305) `class GateTicket`
  - `FacadeGate` (class, line 336) `class FacadeGate`
  - `gate_configured` (method, line 154) `def gate_configured(self)`
  - `cover_context` (method, line 158) `def cover_context(self)`
  - `cover_variables` (method, line 166) `def cover_variables(self)`
  - `from_mapping` (method, line 181) `def from_mapping(cls, mapping, env)`
  - `__init__` (method, line 265) `def __init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)`
  - `hash` (method, line 282) `def hash(self, phrase)`
  - `verify` (method, line 286) `def verify(self, phrase, encoded)`
  - `from_config` (method, line 296) `def from_config(cls, config)`
  - `__init__` (method, line 308) `def __init__(self, secret_key, ttl_seconds)`
  - `issue` (method, line 316) `def issue(self, mode)`
  - `verify` (method, line 322) `def verify(self, token)`
  - `__init__` (method, line 339) `def __init__(self, config, hasher, ticket)`
  - `build` (method, line 351) `def build(cls, config, secret_key)`
  - `evaluate` (method, line 359) `def evaluate(self, phrase)`
  - `read` (method, line 189) `def read(key)`
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

## controllers/file.py
- Layer: presentation
- Language: py
- Symbols:
  - `_log_s3_error` (function, line 26) `def _log_s3_error(operation, error)`
  - `safe_filename` (function, line 31) `def safe_filename(name)`
  - `FileController` (class, line 49) `class FileController`
  - `__init__` (method, line 52) `def __init__(self, users_path, s3_bucket, s3_client)`
  - `_key` (method, line 57) `def _key(self, username, filename, suffix)`
  - `get_storage_usage` (method, line 69) `def get_storage_usage(self, username)`
  - `upload_encrypted_file` (method, line 83) `def upload_encrypted_file(self, username, file_storage, wrapped_fek)`
  - `get_encrypted_file_and_key` (method, line 107) `def get_encrypted_file_and_key(self, username, filename)`
  - `list_encrypted_files` (method, line 137) `def list_encrypted_files(self, username)`
- Depends on: `utils/utils.py`
- Imported by: `app_factory.py`

## controllers/message.py
- Layer: presentation
- Language: py
- Symbols:
  - `MessageController` (class, line 16) `class MessageController`
  - `__init__` (method, line 19) `def __init__(self, users_path, users_db_path)`
  - `send_encrypted_message` (method, line 33) `def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)`
  - `get_messages` (method, line 75) `def get_messages(self, username, page, per_page)`
- Depends on: `models/message.py`, `models/user.py`, `utils/utils.py`
- Imported by: `views/message.py`

## controllers/sync.py
- Layer: presentation
- Doc: controllers/sync.py
- Language: py
- Symbols:
  - `SyncController` (class, line 7) `class SyncController`
  - `__init__` (method, line 8) `def __init__(self, users_path, s3_bucket, s3_client, file_controller)`
  - `get_storage_usage` (method, line 14) `def get_storage_usage(self, username)`
- Imported by: `app_factory.py`
