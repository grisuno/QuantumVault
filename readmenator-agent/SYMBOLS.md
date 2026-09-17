# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_is_production_like` | function | `app.py:58` | `def _is_production_like()` |
| `main` | function | `app.py:21` | `def main()` |
| `_build_csp` | function | `app_factory.py:81` | `def _build_csp()` |
| `_build_talisman_kwargs` | function | `app_factory.py:112` | `def _build_talisman_kwargs()` |
| `_configure_logging` | function | `app_factory.py:213` | `def _configure_logging(app)` |
| `_configure_secret_key` | function | `app_factory.py:153` | `def _configure_secret_key(app, config)` |
| `_configure_session` | function | `app_factory.py:196` | `def _configure_session(app)` |
| `_is_production` | function | `app_factory.py:70` | `def _is_production()` |
| `create_app` | function | `app_factory.py:230` | `def create_app(config_overrides, security_overrides)` |
| `load_user` | function | `app_factory.py:408` | `def load_user(user_id)` |
| `main` | function | `client.go:13` | `func main(` |
| `AuthController` | class | `controllers/auth.py:58` | `class AuthController` |
| `__init__` | method | `controllers/auth.py:61` | `def __init__(self, db_path, mail, storage_uri)` |
| `_is_code_valid` | method | `controllers/auth.py:349` | `def _is_code_valid(self, expires_at)` |
| `_now_utc` | function | `controllers/auth.py:49` | `def _now_utc()` |
| `register` | method | `controllers/auth.py:76` | `def register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_na` |
| `resend_phone_code` | method | `controllers/auth.py:310` | `def resend_phone_code(self, username)` |
| `send_confirmation_email` | method | `controllers/auth.py:156` | `def send_confirmation_email(self, email, username, token)` |
| `send_mfa_code` | method | `controllers/auth.py:393` | `def send_mfa_code(self, username)` |
| `send_sms_verification` | method | `controllers/auth.py:253` | `def send_sms_verification(self, phone, code, username)` |
| `srp_hello` | method | `controllers/auth.py:202` | `def srp_hello(self, username, client_a_hex)` |
| `srp_verify` | method | `controllers/auth.py:221` | `def srp_verify(self, username, client_m1_hex)` |
| `toggle_mfa` | method | `controllers/auth.py:416` | `def toggle_mfa(self, username, enable)` |
| `verify_mfa_code` | method | `controllers/auth.py:369` | `def verify_mfa_code(self, username, code)` |
| `verify_phone_code` | method | `controllers/auth.py:274` | `def verify_phone_code(self, username, code)` |
| `ContactController` | class | `controllers/contact.py:4` | `class ContactController` |
| `__init__` | method | `controllers/contact.py:6` | `def __init__(self, db_path)` |
| `create_contact` | method | `controllers/contact.py:14` | `def create_contact(self, user_id, subject, message)` |
| `get_user_contacts` | method | `controllers/contact.py:36` | `def get_user_contacts(self, user_id)` |
| `DeniableVaultConfig` | class | `controllers/deniable_vault.py:134` | `class DeniableVaultConfig` |
| `DeniableVaultController` | class | `controllers/deniable_vault.py:393` | `class DeniableVaultController` |
| `EnvelopeValidationError` | class | `controllers/deniable_vault.py:104` | `class EnvelopeValidationError(ValueError)` |
| `EnvelopeValidator` | class | `controllers/deniable_vault.py:272` | `class EnvelopeValidator` |
| `__init__` | method | `controllers/deniable_vault.py:281` | `def __init__(self, config)` |
| `__init__` | method | `controllers/deniable_vault.py:401` | `def __init__(self, db, config, validator)` |
| `_base64_length` | function | `controllers/deniable_vault.py:81` | `def _base64_length(byte_length)` |
| `_coerce_int` | method | `controllers/deniable_vault.py:108` | `def _coerce_int(value, default)` |
| `_coerce_kdf` | method | `controllers/deniable_vault.py:118` | `def _coerce_kdf(value, default)` |
| `_validate_hex` | method | `controllers/deniable_vault.py:376` | `def _validate_hex(value, expected_length, index, field)` |
| `_validate_slot` | method | `controllers/deniable_vault.py:339` | `def _validate_slot(self, index, slot)` |
| `canonical_json` | function | `controllers/deniable_vault.py:86` | `def canonical_json(envelope)` |
| `exists` | method | `controllers/deniable_vault.py:474` | `def exists(self, username)` |
| `expected_ct_b64_length` | method | `controllers/deniable_vault.py:213` | `def expected_ct_b64_length(self)` |
| `from_mapping` | method | `controllers/deniable_vault.py:148` | `def from_mapping(cls, mapping, env)` |
| `load_or_provision` | method | `controllers/deniable_vault.py:419` | `def load_or_provision(self, username)` |
| `public_parameters` | method | `controllers/deniable_vault.py:250` | `def public_parameters(self)` |
| `random_container` | method | `controllers/deniable_vault.py:222` | `def random_container(self)` |
| `read` | method | `controllers/deniable_vault.py:171` | `def read(key)` |
| `reset` | method | `controllers/deniable_vault.py:456` | `def reset(self, username)` |
| `save` | method | `controllers/deniable_vault.py:441` | `def save(self, username, envelope)` |
| `validate` | method | `controllers/deniable_vault.py:285` | `def validate(self, envelope)` |
| `FacadeConfig` | class | `controllers/facade.py:124` | `class FacadeConfig` |
| `FacadeGate` | class | `controllers/facade.py:336` | `class FacadeGate` |
| `GateDecision` | class | `controllers/facade.py:72` | `class GateDecision` |
| `GateOutcome` | class | `controllers/facade.py:63` | `class GateOutcome(Enum)` |
| `GatePhraseHasher` | class | `controllers/facade.py:262` | `class GatePhraseHasher` |
| `GateTicket` | class | `controllers/facade.py:305` | `class GateTicket` |
| `__init__` | method | `controllers/facade.py:265` | `def __init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)` |
| `__init__` | method | `controllers/facade.py:308` | `def __init__(self, secret_key, ttl_seconds)` |
| `__init__` | method | `controllers/facade.py:339` | `def __init__(self, config, hasher, ticket)` |
| `_as_bool` | method | `controllers/facade.py:79` | `def _as_bool(value, default)` |
| `_as_int` | method | `controllers/facade.py:88` | `def _as_int(value, default)` |
| `_as_paths` | method | `controllers/facade.py:111` | `def _as_paths(value, default)` |
| `_as_raw_text` | method | `controllers/facade.py:106` | `def _as_raw_text(value, default)` |
| `_as_text` | method | `controllers/facade.py:98` | `def _as_text(value, default)` |
| `build` | method | `controllers/facade.py:351` | `def build(cls, config, secret_key)` |
| `cover_context` | method | `controllers/facade.py:158` | `def cover_context(self)` |
| `cover_variables` | method | `controllers/facade.py:166` | `def cover_variables(self)` |
| `evaluate` | method | `controllers/facade.py:359` | `def evaluate(self, phrase)` |
| `from_config` | method | `controllers/facade.py:296` | `def from_config(cls, config)` |
| `from_mapping` | method | `controllers/facade.py:181` | `def from_mapping(cls, mapping, env)` |
| `gate_configured` | method | `controllers/facade.py:154` | `def gate_configured(self)` |
| `hash` | method | `controllers/facade.py:282` | `def hash(self, phrase)` |
| `issue` | method | `controllers/facade.py:316` | `def issue(self, mode)` |
| `read` | method | `controllers/facade.py:189` | `def read(key)` |
| `verify` | method | `controllers/facade.py:286` | `def verify(self, phrase, encoded)` |
| `verify` | method | `controllers/facade.py:322` | `def verify(self, token)` |
| `FileController` | class | `controllers/file.py:49` | `class FileController` |
| `__init__` | method | `controllers/file.py:52` | `def __init__(self, users_path, s3_bucket, s3_client)` |
| `_key` | method | `controllers/file.py:57` | `def _key(self, username, filename, suffix)` |
| `_log_s3_error` | function | `controllers/file.py:26` | `def _log_s3_error(operation, error)` |
| `get_encrypted_file_and_key` | method | `controllers/file.py:107` | `def get_encrypted_file_and_key(self, username, filename)` |
| `get_storage_usage` | method | `controllers/file.py:69` | `def get_storage_usage(self, username)` |
| `list_encrypted_files` | method | `controllers/file.py:137` | `def list_encrypted_files(self, username)` |
| `safe_filename` | function | `controllers/file.py:31` | `def safe_filename(name)` |
| `upload_encrypted_file` | method | `controllers/file.py:83` | `def upload_encrypted_file(self, username, file_storage, wrapped_fek)` |
| `MessageController` | class | `controllers/message.py:16` | `class MessageController` |
| `__init__` | method | `controllers/message.py:19` | `def __init__(self, users_path, users_db_path)` |
| `get_messages` | method | `controllers/message.py:75` | `def get_messages(self, username, page, per_page)` |
| `send_encrypted_message` | method | `controllers/message.py:33` | `def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)` |
| `SyncController` | class | `controllers/sync.py:7` | `class SyncController` |
| `__init__` | method | `controllers/sync.py:8` | `def __init__(self, users_path, s3_bucket, s3_client, file_controller)` |
| `get_storage_usage` | method | `controllers/sync.py:14` | `def get_storage_usage(self, username)` |
| `decryptFile` | function | `enc_dec.go:45` | `func decryptFile(` |
| `deriveAESKey` | function | `enc_dec.go:20` | `func deriveAESKey(` |
| `encryptFile` | function | `enc_dec.go:24` | `func encryptFile(` |
| `main` | function | `enc_dec.go:69` | `func main(` |
| `_build_s3_client` | function | `enc_dec.py:81` | `def _build_s3_client(region)` |
| `decrypt_file_in_memory` | function | `enc_dec.py:65` | `def decrypt_file_in_memory(nonce, ciphertext, aes_key)` |
| `derive_aes_key` | function | `enc_dec.py:36` | `def derive_aes_key(shared_secret)` |
| `encrypt_file_in_memory` | function | `enc_dec.py:49` | `def encrypt_file_in_memory(data, aes_key)` |
| `main` | function | `enc_dec.py:103` | `def main()` |
| `ContactDB` | class | `models/contact.py:26` | `class ContactDB` |
| `ContactModel` | class | `models/contact.py:8` | `class ContactModel(BaseModel)` |
| `__init__` | method | `models/contact.py:29` | `def __init__(self, db_path)` |
| `_convert_row_to_dict` | method | `models/contact.py:115` | `def _convert_row_to_dict(self, row)` |
| `_convert_row_to_dict_with_username` | method | `models/contact.py:168` | `def _convert_row_to_dict_with_username(self, row)` |
| `_init_db` | method | `models/contact.py:38` | `def _init_db(self)` |
| `create_contact` | method | `models/contact.py:52` | `def create_contact(self, user_id, subject, message)` |
| `get_all_contacts` | method | `models/contact.py:139` | `def get_all_contacts(self, page, per_page)` |
| `get_user_contacts` | method | `models/contact.py:89` | `def get_user_contacts(self, user_id)` |
| `DeniableVaultDB` | class | `models/deniable_vault.py:30` | `class DeniableVaultDB` |
| `__init__` | method | `models/deniable_vault.py:33` | `def __init__(self, db_path)` |
| `_init_db` | method | `models/deniable_vault.py:43` | `def _init_db(self)` |
| `exists` | method | `models/deniable_vault.py:101` | `def exists(self, username)` |
| `get` | method | `models/deniable_vault.py:82` | `def get(self, username)` |
| `upsert` | method | `models/deniable_vault.py:57` | `def upsert(self, username, envelope)` |
| `MessageDB` | class | `models/message.py:43` | `class MessageDB` |
| `MessageModel` | class | `models/message.py:27` | `class MessageModel(BaseModel)` |
| `__init__` | method | `models/message.py:46` | `def __init__(self, base_path)` |
| `delete_old_messages` | method | `models/message.py:172` | `def delete_old_messages(self, recipient, days)` |
| `get_messages` | method | `models/message.py:87` | `def get_messages(self, recipient, page, per_page)` |
| `save_message` | method | `models/message.py:55` | `def save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipient, cek_for_sender, message_id)` |
| `PlanDB` | class | `models/plans.py:4` | `class PlanDB` |
| `__init__` | method | `models/plans.py:6` | `def __init__(self, db_path)` |
| `_convert_row_to_dict` | method | `models/plans.py:127` | `def _convert_row_to_dict(self, row)` |
| `_init_db` | method | `models/plans.py:15` | `def _init_db(self)` |
| `create_plan` | method | `models/plans.py:60` | `def create_plan(self, name, storage_quota, trial_days, price)` |
| `delete_plan` | method | `models/plans.py:113` | `def delete_plan(self, name)` |
| `get_all_plans` | method | `models/plans.py:50` | `def get_all_plans(self)` |
| `get_plan` | method | `models/plans.py:37` | `def get_plan(self, plan_name)` |
| `update_plan` | method | `models/plans.py:78` | `def update_plan(self, name, storage_quota, trial_days, price)` |
| `validate_plan_payment` | method | `models/plans.py:139` | `def validate_plan_payment(self, plan_name, amount_paid)` |
| `SuperadminAuditDB` | class | `models/superadmin_audit.py:32` | `class SuperadminAuditDB` |
| `__init__` | method | `models/superadmin_audit.py:35` | `def __init__(self, db_path)` |
| `_init_db` | method | `models/superadmin_audit.py:45` | `def _init_db(self)` |
| `recent` | method | `models/superadmin_audit.py:119` | `def recent(self, limit)` |
| `record` | method | `models/superadmin_audit.py:75` | `def record(self, actor, action, target_user, ip, details)` |
| `UserDB` | class | `models/user.py:83` | `class UserDB` |
| `UserModel` | class | `models/user.py:8` | `class UserModel(BaseModel, UserMixin)` |
| `__init__` | method | `models/user.py:85` | `def __init__(self, db_path)` |
| `_convert_row_to_dict` | method | `models/user.py:638` | `def _convert_row_to_dict(self, row)` |
| `_drop_phone_unique_if_present` | method | `models/user.py:214` | `def _drop_phone_unique_if_present(self)` |
| `_has_phone_unique_constraint` | method | `models/user.py:193` | `def _has_phone_unique_constraint(self)` |
| `_init_db` | method | `models/user.py:105` | `def _init_db(self)` |
| `_migrate_from_v7` | method | `models/user.py:271` | `def _migrate_from_v7(self, legacy_columns)` |
| `_parse_datetime` | method | `models/user.py:615` | `def _parse_datetime(value)` |
| `count_users` | method | `models/user.py:592` | `def count_users(self)` |
| `create_user` | method | `models/user.py:325` | `def create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first` |
| `fetch_one` | method | `models/user.py:694` | `def fetch_one(self, query, params)` |
| `get_all_users` | method | `models/user.py:603` | `def get_all_users(self)` |
| `get_id` | method | `models/user.py:52` | `def get_id(self)` |
| `get_recovery_bundle` | method | `models/user.py:524` | `def get_recovery_bundle(self, username)` |
| `get_user` | method | `models/user.py:454` | `def get_user(self, username)` |
| `get_user_by_confirmation_token` | method | `models/user.py:510` | `def get_user_by_confirmation_token(self, token)` |
| `get_user_by_email` | method | `models/user.py:482` | `def get_user_by_email(self, email)` |
| `get_user_by_id` | method | `models/user.py:468` | `def get_user_by_id(self, user_id)` |
| `get_user_by_phone` | method | `models/user.py:496` | `def get_user_by_phone(self, phone)` |
| `is_active` | method | `models/user.py:70` | `def is_active(self)` |
| `reset_credentials_with_recovery` | method | `models/user.py:548` | `def reset_credentials_with_recovery(self, username, srp_salt, srp_verifier, kdf_salt, encrypted_private_key)` |
| `update_role` | method | `models/user.py:579` | `def update_role(self, username, role, storage_quota, subscription_status)` |
| `update_user` | method | `models/user.py:430` | `def update_user(self, username, email_verified, confirmation_token)` |
| `update_user_mfa_status` | method | `models/user.py:396` | `def update_user_mfa_status(self, username, mfa_code_hash, mfa_code_expires, mfa_enabled)` |
| `update_user_phone_status` | method | `models/user.py:362` | `def update_user_phone_status(self, username, phone_verified, phone_verification_code_hash, phone_code_expires)` |
| `value` | method | `models/user.py:655` | `def value(name, default)` |
| `_build_mail_app` | function | `scripts/email_tool.py:40` | `def _build_mail_app(config)` |
| `build_parser` | function | `scripts/email_tool.py:133` | `def build_parser()` |
| `cmd_confirm` | function | `scripts/email_tool.py:114` | `def cmd_confirm(args)` |
| `cmd_link` | function | `scripts/email_tool.py:91` | `def cmd_link(args)` |
| `cmd_test_smtp` | function | `scripts/email_tool.py:63` | `def cmd_test_smtp(args)` |
| `main` | function | `scripts/email_tool.py:153` | `def main()` |
| `upsert_env` | function | `scripts/garage-init.sh:35` | `` |
| `gcmd` | function | `scripts/garage-native.sh:141` | `` |
| `s3_reachable` | function | `scripts/garage-native.sh:56` | `` |
| `upsert_env` | function | `scripts/garage-native.sh:46` | `` |
| `_print_user_summary` | function | `scripts/makeadmin.py:64` | `def _print_user_summary(user)` |
| `_resolve_db_path` | function | `scripts/makeadmin.py:51` | `def _resolve_db_path()` |
| `build_parser` | function | `scripts/makeadmin.py:126` | `def build_parser()` |
| `cmd_promote` | function | `scripts/makeadmin.py:75` | `def cmd_promote(args)` |
| `main` | function | `scripts/makeadmin.py:152` | `def main()` |
| `_FakeUser` | class | `scripts/test_bloque1.py:48` | `class _FakeUser` |
| `__init__` | method | `scripts/test_bloque1.py:49` | `def __init__(self, row)` |
| `_load_user` | method | `scripts/test_bloque1.py:62` | `def _load_user(uid)` |
| `check` | method | `scripts/test_bloque1.py:86` | `def check(name, ok, detail)` |
| `get_id` | method | `scripts/test_bloque1.py:59` | `def get_id(self)` |
| `is_active` | method | `scripts/test_bloque1.py:56` | `def is_active(self)` |
| `is_anonymous` | method | `scripts/test_bloque1.py:58` | `def is_anonymous(self)` |
| `is_authenticated` | method | `scripts/test_bloque1.py:54` | `def is_authenticated(self)` |
| `handleConnection` | function | `server.go:40` | `func handleConnection(` |
| `main` | function | `server.go:11` | `func main(` |
| `apiRequest` | function | `static/js/account.js:36` | `` |
| `collectSlots` | function | `static/js/account.js:59` | `` |
| `csrfToken` | function | `static/js/account.js:30` | `` |
| `handleConfigure` | function | `static/js/account.js:73` | `` |
| `handleOpen` | function | `static/js/account.js:103` | `` |
| `handleReset` | function | `static/js/account.js:125` | `` |
| `init` | function | `static/js/account.js:138` | `` |
| `loadState` | function | `static/js/account.js:54` | `` |
| `setStatus` | function | `static/js/account.js:19` | `` |
| `animateElement` | function | `static/js/coded-text.js:18` | `` |
| `init` | function | `static/js/coded-text.js:49` | `` |
| `randomChar` | function | `static/js/coded-text.js:12` | `` |
| `handleLogin` | function | `static/js/login.js:11` | `` |
| `init` | function | `static/js/login.js:43` | `` |
| `collectEnvelopes` | function | `static/js/messages.js:43` | `` |
| `getCsrfToken` | function | `static/js/messages.js:11` | `` |
| `handleDecryptInbox` | function | `static/js/messages.js:60` | `` |
| `handleSend` | function | `static/js/messages.js:17` | `` |
| `init` | function | `static/js/messages.js:108` | `` |
| `initEditor` | function | `static/js/messages.js:87` | `` |
| `H` | function | `static/js/qv-crypto.js:162` | `` |
| `Hint` | function | `static/js/qv-crypto.js:166` | `` |
| `aesGcmDecrypt` | function | `static/js/qv-crypto.js:214` | `` |
| `aesGcmEncrypt` | function | `static/js/qv-crypto.js:203` | `` |
| `base64ToBytes` | function | `static/js/qv-crypto.js:107` | `` |
| `buildRegistration` | function | `static/js/qv-crypto.js:490` | `` |
| `bytesToBase32` | function | `static/js/qv-crypto.js:89` | `` |
| `bytesToBase64` | function | `static/js/qv-crypto.js:78` | `` |
| `bytesToBigInt` | function | `static/js/qv-crypto.js:114` | `` |
| `bytesToHex` | function | `static/js/qv-crypto.js:72` | `` |
| `computeK` | function | `static/js/qv-crypto.js:244` | `` |
| `concatBytes` | function | `static/js/qv-crypto.js:52` | `` |
| `decryptInbox` | function | `static/js/qv-crypto.js:703` | `` |
| `deriveKeyFromPassphrase` | function | `static/js/qv-crypto.js:178` | `` |
| `deriveMasterKey` | function | `static/js/qv-crypto.js:199` | `` |
| `derivePublicKeyFromPrivateBlob` | function | `static/js/qv-crypto.js:449` | `` |
| `deriveVerifier` | function | `static/js/qv-crypto.js:249` | `` |
| `deriveWrapKey` | function | `static/js/qv-crypto.js:353` | `` |
| `downloadAndDecrypt` | function | `static/js/qv-crypto.js:620` | `` |
| `encryptAndUpload` | function | `static/js/qv-crypto.js:591` | `` |
| `fetchPublicKey` | function | `static/js/qv-crypto.js:658` | `` |
| `generateIdentity` | function | `static/js/qv-crypto.js:309` | `` |
| `generateRecoveryCode` | function | `static/js/qv-crypto.js:411` | `` |
| `hexToBytes` | function | `static/js/qv-crypto.js:63` | `` |
| `i2osp` | function | `static/js/qv-crypto.js:121` | `` |
| `login` | function | `static/js/qv-crypto.js:586` | `` |
| `mod` | function | `static/js/qv-crypto.js:131` | `` |
| `modPow` | function | `static/js/qv-crypto.js:135` | `` |
| `normalizeRecoveryCode` | function | `static/js/qv-crypto.js:422` | `` |
| `parsePrivateBlob` | function | `static/js/qv-crypto.js:345` | `` |
| `parsePublicKey` | function | `static/js/qv-crypto.js:337` | `` |
| `postJson` | function | `static/js/qv-crypto.js:467` | `` |
| `randomBytes` | function | `static/js/qv-crypto.js:153` | `` |
| `recoverAccount` | function | `static/js/qv-crypto.js:535` | `` |
| `register` | function | `static/js/qv-crypto.js:524` | `` |
| `sendSecureMessage` | function | `static/js/qv-crypto.js:673` | `` |
| `srpLogin` | function | `static/js/qv-crypto.js:257` | `` |
| `unwrapKey` | function | `static/js/qv-crypto.js:389` | `` |
| `wrapKey` | function | `static/js/qv-crypto.js:365` | `` |
| `wrapPrivateKeyForRecovery` | function | `static/js/qv-crypto.js:430` | `` |
| `buildDeniableVault` | function | `static/js/qv-deniable.js:125` | `` |
| `frame` | function | `static/js/qv-deniable.js:55` | `` |
| `openDeniableVault` | function | `static/js/qv-deniable.js:170` | `` |
| `openSlot` | function | `static/js/qv-deniable.js:102` | `` |
| `sealSlot` | function | `static/js/qv-deniable.js:82` | `` |
| `toBytes` | function | `static/js/qv-deniable.js:47` | `` |
| `unframe` | function | `static/js/qv-deniable.js:64` | `` |
| `handleRecover` | function | `static/js/recover.js:22` | `` |
| `init` | function | `static/js/recover.js:79` | `` |
| `setStatus` | function | `static/js/recover.js:14` | `` |
| `handleRegister` | function | `static/js/register.js:42` | `` |
| `init` | function | `static/js/register.js:109` | `` |
| `showRecoveryCode` | function | `static/js/register.js:16` | `` |
| `getCsrfToken` | function | `static/js/upload.js:11` | `` |
| `getPublicKey` | function | `static/js/upload.js:23` | `` |
| `getUsername` | function | `static/js/upload.js:16` | `` |
| `handleDownload` | function | `static/js/upload.js:74` | `` |
| `handleUpload` | function | `static/js/upload.js:40` | `` |
| `init` | function | `static/js/upload.js:96` | `` |
| `terms` | function | `templates/terms.py:6` | `def terms()` |
| `_ListLogHandler` | class | `tests/conftest.py:82` | `class _ListLogHandler(Handler)` |
| `__init__` | method | `tests/conftest.py:85` | `def __init__(self)` |
| `_push_request_context` | function | `tests/conftest.py:34` | `def _push_request_context()` |
| `app` | function | `tests/conftest.py:52` | `def app(tmp_path)` |
| `audit_records` | method | `tests/conftest.py:94` | `def audit_records()` |
| `client` | function | `tests/conftest.py:77` | `def client(app)` |
| `emit` | method | `tests/conftest.py:89` | `def emit(self, record)` |
| `_authenticated_client` | function | `tests/test_account_facade.py:55` | `def _authenticated_client(application, db_path)` |
| `_build` | function | `tests/test_account_facade.py:65` | `def _build(tmp_path, fast_hasher)` |
| `_make_user` | function | `tests/test_account_facade.py:27` | `def _make_user(db_path, username)` |
| `fast_hasher` | function | `tests/test_account_facade.py:23` | `def fast_hasher()` |
| `test_facade_disabled_keeps_it_optional` | function | `tests/test_account_facade.py:99` | `def test_facade_disabled_keeps_it_optional(tmp_path, fast_hasher)` |
| `test_facade_enabled_requires_a_deniable_passphrase` | function | `tests/test_account_facade.py:88` | `def test_facade_enabled_requires_a_deniable_passphrase(tmp_path, fast_hasher)` |
| `test_resend_endpoint_is_registered` | function | `tests/test_auth_phone.py:25` | `def test_resend_endpoint_is_registered(app)` |
| `test_resend_route_accepts_only_post` | function | `tests/test_auth_phone.py:31` | `def test_resend_route_accepts_only_post(app)` |
| `test_verify_phone_page_renders` | function | `tests/test_auth_phone.py:18` | `def test_verify_phone_page_renders(client)` |
| `TestCatalog` | class | `tests/test_cover.py:83` | `class TestCatalog` |
| `TestCoverHttp` | class | `tests/test_cover.py:280` | `class TestCoverHttp` |
| `TestCoverService` | class | `tests/test_cover.py:244` | `class TestCoverService` |
| `TestCustomStore` | class | `tests/test_cover.py:189` | `class TestCustomStore` |
| `TestRenderer` | class | `tests/test_cover.py:158` | `class TestRenderer` |
| `TestSanitizer` | class | `tests/test_cover.py:103` | `class TestSanitizer` |
| `_client` | function | `tests/test_cover.py:68` | `def _client(tmp_path, fast_hasher)` |
| `_facade_overrides` | function | `tests/test_cover.py:56` | `def _facade_overrides(fast_hasher)` |
| `fast_hasher` | function | `tests/test_cover.py:42` | `def fast_hasher()` |
| `renderer` | function | `tests/test_cover.py:47` | `def renderer()` |
| `store` | function | `tests/test_cover.py:52` | `def store(tmp_path, renderer)` |
| `test_bad_extension_is_rejected` | method | `tests/test_cover.py:196` | `def test_bad_extension_is_rejected(self, store)` |
| `test_blank_source_is_rejected` | method | `tests/test_cover.py:184` | `def test_blank_source_is_rejected(self, renderer)` |
| `test_builtin_selection_ignores_a_custom_name` | method | `tests/test_cover.py:267` | `def test_builtin_selection_ignores_a_custom_name(self, renderer, store)` |
| `test_catalog_ships_five_distinct_templates` | method | `tests/test_cover.py:84` | `def test_catalog_ships_five_distinct_templates(self)` |
| `test_configured_template_is_served` | method | `tests/test_cover.py:287` | `def test_configured_template_is_served(self, tmp_path, fast_hasher)` |
| `test_control_characters_are_stripped` | method | `tests/test_cover.py:117` | `def test_control_characters_are_stripped(self)` |
| `test_custom_selection_renders_the_custom_marker` | method | `tests/test_cover.py:274` | `def test_custom_selection_renders_the_custom_marker(self, renderer, store)` |
| `test_custom_template_is_rendered` | method | `tests/test_cover.py:260` | `def test_custom_template_is_rendered(self, renderer, store)` |
| `test_default_cover_selects_search_portal` | method | `tests/test_cover.py:281` | `def test_default_cover_selects_search_portal(self, tmp_path, fast_hasher)` |
| `test_default_template_exists` | method | `tests/test_cover.py:89` | `def test_default_template_exists(self)` |
| `test_directory_with_allowed_suffix_is_ignored` | method | `tests/test_cover.py:238` | `def test_directory_with_allowed_suffix_is_ignored(self, store)` |
| `test_disallowed_character_filename_is_rejected` | method | `tests/test_cover.py:221` | `def test_disallowed_character_filename_is_rejected(self, store)` |
| `test_dunder_access_is_rejected` | method | `tests/test_cover.py:168` | `def test_dunder_access_is_rejected(self, renderer)` |
| `test_email_boundary_is_inclusive` | method | `tests/test_cover.py:150` | `def test_email_boundary_is_inclusive(self)` |
| `test_empty_payload_fills_defaults` | method | `tests/test_cover.py:104` | `def test_empty_payload_fills_defaults(self)` |
| `test_every_template_validates_and_renders` | method | `tests/test_cover.py:92` | `def test_every_template_validates_and_renders(self, renderer)` |
| `test_exactly_max_size_is_accepted` | method | `tests/test_cover.py:225` | `def test_exactly_max_size_is_accepted(self, store)` |
| `test_external_form_action_is_rejected` | method | `tests/test_cover.py:176` | `def test_external_form_action_is_rejected(self, renderer)` |
| `test_gate_still_works_with_configured_template` | method | `tests/test_cover.py:298` | `def test_gate_still_works_with_configured_template(self, tmp_path, fast_hasher)` |
| `test_inline_script_is_rejected` | method | `tests/test_cover.py:172` | `def test_inline_script_is_rejected(self, renderer)` |
| `test_invalid_email_is_rejected` | method | `tests/test_cover.py:113` | `def test_invalid_email_is_rejected(self)` |
| `test_missing_custom_template_falls_back_to_default` | method | `tests/test_cover.py:255` | `def test_missing_custom_template_falls_back_to_default(self, renderer, store)` |
| `test_missing_template_raises` | method | `tests/test_cover.py:213` | `def test_missing_template_raises(self, store)` |
| `test_multiline_body_preserves_line_breaks` | method | `tests/test_cover.py:125` | `def test_multiline_body_preserves_line_breaks(self)` |
| `test_multiline_flag_matches_spec` | method | `tests/test_cover.py:137` | `def test_multiline_flag_matches_spec(self, spec)` |
| `test_nested_directory_is_created` | method | `tests/test_cover.py:229` | `def test_nested_directory_is_created(self, tmp_path, renderer)` |
| `test_non_bytes_payload_is_rejected` | method | `tests/test_cover.py:217` | `def test_non_bytes_payload_is_rejected(self, store)` |
| `test_overlong_value_is_rejected` | method | `tests/test_cover.py:121` | `def test_overlong_value_is_rejected(self)` |
| `test_oversize_template_is_rejected` | method | `tests/test_cover.py:200` | `def test_oversize_template_is_rejected(self, store)` |
| `test_path_traversal_is_neutralized` | method | `tests/test_cover.py:204` | `def test_path_traversal_is_neutralized(self, store)` |
| `test_script_template_is_rejected` | method | `tests/test_cover.py:209` | `def test_script_template_is_rejected(self, store)` |
| `test_selects_a_builtin_template` | method | `tests/test_cover.py:245` | `def test_selects_a_builtin_template(self, renderer, store)` |
| `test_single_line_value_flattens_line_breaks` | method | `tests/test_cover.py:129` | `def test_single_line_value_flattens_line_breaks(self)` |
| `test_template_import_is_rejected` | method | `tests/test_cover.py:180` | `def test_template_import_is_rejected(self, renderer)` |
| `test_text_boundary_is_inclusive` | method | `tests/test_cover.py:144` | `def test_text_boundary_is_inclusive(self)` |
| `test_two_templates_share_the_store` | method | `tests/test_cover.py:233` | `def test_two_templates_share_the_store(self, store)` |
| `test_unknown_template_falls_back_to_default` | method | `tests/test_cover.py:250` | `def test_unknown_template_falls_back_to_default(self, renderer, store)` |
| `test_unknown_variable_is_rejected` | method | `tests/test_cover.py:109` | `def test_unknown_variable_is_rejected(self)` |
| `test_unknown_variable_is_rejected` | method | `tests/test_cover.py:164` | `def test_unknown_variable_is_rejected(self, renderer)` |
| `test_valid_template_round_trips` | method | `tests/test_cover.py:190` | `def test_valid_template_round_trips(self, store)` |
| `test_variables_are_autoescaped` | method | `tests/test_cover.py:159` | `def test_variables_are_autoescaped(self, renderer)` |
| `TestDeniableVaultApi` | class | `tests/test_deniable_vault.py:390` | `class TestDeniableVaultApi` |
| `TestDeniableVaultConfig` | class | `tests/test_deniable_vault.py:140` | `class TestDeniableVaultConfig` |
| `TestDeniableVaultController` | class | `tests/test_deniable_vault.py:325` | `class TestDeniableVaultController` |
| `TestDeniableVaultDB` | class | `tests/test_deniable_vault.py:293` | `class TestDeniableVaultDB` |
| `TestEnvelopeValidator` | class | `tests/test_deniable_vault.py:185` | `class TestEnvelopeValidator` |
| `TestRandomContainer` | class | `tests/test_deniable_vault.py:272` | `class TestRandomContainer` |
| `_ciphertext` | function | `tests/test_deniable_vault.py:61` | `def _ciphertext(config, length)` |
| `_controller` | method | `tests/test_deniable_vault.py:326` | `def _controller(self, tmp_path)` |
| `_csrf` | function | `tests/test_deniable_vault.py:130` | `def _csrf(client)` |
| `_login` | function | `tests/test_deniable_vault.py:120` | `def _login(client, app, username, role)` |
| `_make_user` | function | `tests/test_deniable_vault.py:91` | `def _make_user(app, username, role)` |
| `_valid_envelope` | function | `tests/test_deniable_vault.py:71` | `def _valid_envelope(config)` |
| `config` | function | `tests/test_deniable_vault.py:50` | `def config()` |
| `test_accepts_a_well_formed_envelope` | method | `tests/test_deniable_vault.py:186` | `def test_accepts_a_well_formed_envelope(self, validator, config)` |
| `test_allowed_kdf_csv_is_parsed` | method | `tests/test_deniable_vault.py:166` | `def test_allowed_kdf_csv_is_parsed(self, monkeypatch)` |
| `test_audit_is_generic_and_never_contains_ciphertext` | method | `tests/test_deniable_vault.py:373` | `def test_audit_is_generic_and_never_contains_ciphertext(self, app, tmp_path, audit_records)` |
| `test_defaults_are_self_consistent` | method | `tests/test_deniable_vault.py:141` | `def test_defaults_are_self_consistent(self)` |
| `test_environment_overrides_mapping` | method | `tests/test_deniable_vault.py:161` | `def test_environment_overrides_mapping(self, monkeypatch)` |
| `test_exists` | method | `tests/test_deniable_vault.py:313` | `def test_exists(self, tmp_path)` |
| `test_expected_ct_length_matches_base64_formula` | method | `tests/test_deniable_vault.py:150` | `def test_expected_ct_length_matches_base64_formula(self, config)` |
| `test_get_always_returns_an_envelope_and_parameters` | method | `tests/test_deniable_vault.py:406` | `def test_get_always_returns_an_envelope_and_parameters(self, client, app)` |
| `test_get_api_requires_authentication` | method | `tests/test_deniable_vault.py:395` | `def test_get_api_requires_authentication(self, client)` |
| `test_get_missing_returns_none` | method | `tests/test_deniable_vault.py:309` | `def test_get_missing_returns_none(self, tmp_path)` |
| `test_load_or_provision_is_stable` | method | `tests/test_deniable_vault.py:339` | `def test_load_or_provision_is_stable(self, app, tmp_path)` |
| `test_load_or_provision_mints_when_absent` | method | `tests/test_deniable_vault.py:331` | `def test_load_or_provision_mints_when_absent(self, app, tmp_path)` |
| `test_mapping_overrides_defaults` | method | `tests/test_deniable_vault.py:154` | `def test_mapping_overrides_defaults(self)` |
| `test_public_parameters_round_trip_to_json` | method | `tests/test_deniable_vault.py:172` | `def test_public_parameters_round_trip_to_json(self, config)` |
| `test_put_get_reset_round_trip` | method | `tests/test_deniable_vault.py:422` | `def test_put_get_reset_round_trip(self, client, app)` |
| `test_put_rejects_malformed_envelope` | method | `tests/test_deniable_vault.py:447` | `def test_put_rejects_malformed_envelope(self, client, app)` |
| `test_put_without_csrf_is_rejected` | method | `tests/test_deniable_vault.py:414` | `def test_put_without_csrf_is_rejected(self, client, app)` |
| `test_random_container_has_fixed_shape` | method | `tests/test_deniable_vault.py:281` | `def test_random_container_has_fixed_shape(self, config)` |
| `test_random_container_passes_validation` | method | `tests/test_deniable_vault.py:273` | `def test_random_container_passes_validation(self, config, validator)` |
| `test_random_containers_differ` | method | `tests/test_deniable_vault.py:276` | `def test_random_containers_differ(self, config)` |
| `test_rejects_bad_nonce_length` | method | `tests/test_deniable_vault.py:236` | `def test_rejects_bad_nonce_length(self, validator, config)` |
| `test_rejects_bad_salt_length` | method | `tests/test_deniable_vault.py:224` | `def test_rejects_bad_salt_length(self, validator, config)` |
| `test_rejects_ciphertext_of_wrong_length` | method | `tests/test_deniable_vault.py:242` | `def test_rejects_ciphertext_of_wrong_length(self, validator, config)` |
| `test_rejects_invalid_base64_ciphertext` | method | `tests/test_deniable_vault.py:254` | `def test_rejects_invalid_base64_ciphertext(self, validator, config)` |
| `test_rejects_iterations_above_maximum` | method | `tests/test_deniable_vault.py:212` | `def test_rejects_iterations_above_maximum(self, validator, config)` |
| `test_rejects_iterations_below_minimum` | method | `tests/test_deniable_vault.py:206` | `def test_rejects_iterations_below_minimum(self, validator, config)` |
| `test_rejects_missing_slot_keys` | method | `tests/test_deniable_vault.py:260` | `def test_rejects_missing_slot_keys(self, validator, config)` |
| `test_rejects_non_dict` | method | `tests/test_deniable_vault.py:189` | `def test_rejects_non_dict(self, validator)` |
| `test_rejects_non_hex_salt` | method | `tests/test_deniable_vault.py:230` | `def test_rejects_non_hex_salt(self, validator, config)` |
| `test_rejects_unequal_slot_ciphertext_lengths` | method | `tests/test_deniable_vault.py:248` | `def test_rejects_unequal_slot_ciphertext_lengths(self, validator, config)` |
| `test_rejects_unknown_kdf` | method | `tests/test_deniable_vault.py:200` | `def test_rejects_unknown_kdf(self, validator, config)` |
| `test_rejects_wrong_schema_version` | method | `tests/test_deniable_vault.py:194` | `def test_rejects_wrong_schema_version(self, validator, config)` |
| `test_rejects_wrong_slot_count` | method | `tests/test_deniable_vault.py:218` | `def test_rejects_wrong_slot_count(self, validator, config)` |
| `test_reset_replaces_with_a_valid_random_container` | method | `tests/test_deniable_vault.py:363` | `def test_reset_replaces_with_a_valid_random_container(self, app, tmp_path)` |
| `test_save_rejects_invalid_envelope` | method | `tests/test_deniable_vault.py:354` | `def test_save_rejects_invalid_envelope(self, app, tmp_path)` |
| `test_save_then_load_round_trips` | method | `tests/test_deniable_vault.py:346` | `def test_save_then_load_round_trips(self, app, tmp_path)` |
| `test_settings_page_renders_for_authenticated_user` | method | `tests/test_deniable_vault.py:399` | `def test_settings_page_renders_for_authenticated_user(self, client, app)` |
| `test_settings_page_requires_authentication` | method | `tests/test_deniable_vault.py:391` | `def test_settings_page_requires_authentication(self, client)` |
| `test_upsert_replaces_existing_row` | method | `tests/test_deniable_vault.py:303` | `def test_upsert_replaces_existing_row(self, tmp_path)` |
| `test_upsert_then_get_round_trips_verbatim` | method | `tests/test_deniable_vault.py:294` | `def test_upsert_then_get_round_trips_verbatim(self, tmp_path)` |
| `test_vault_is_scoped_to_the_authenticated_user` | method | `tests/test_deniable_vault.py:461` | `def test_vault_is_scoped_to_the_authenticated_user(self, client, app)` |
| `validator` | function | `tests/test_deniable_vault.py:56` | `def validator(config)` |
| `TestFacadeConfig` | class | `tests/test_facade.py:148` | `class TestFacadeConfig` |
| `TestFacadeGate` | class | `tests/test_facade.py:288` | `class TestFacadeGate` |
| `TestFacadeHttp` | class | `tests/test_facade.py:396` | `class TestFacadeHttp` |
| `TestGatePhraseHasher` | class | `tests/test_facade.py:209` | `class TestGatePhraseHasher` |
| `TestGateTicket` | class | `tests/test_facade.py:250` | `class TestGateTicket` |
| `_csrf` | function | `tests/test_facade.py:138` | `def _csrf(client)` |
| `_facade_overrides` | function | `tests/test_facade.py:78` | `def _facade_overrides(fast_hasher)` |
| `_gate` | method | `tests/test_facade.py:289` | `def _gate(self, config)` |
| `_make_user` | function | `tests/test_facade.py:109` | `def _make_user(app_or_path, username)` |
| `facade_client` | function | `tests/test_facade.py:93` | `def facade_client(tmp_path, fast_hasher)` |
| `fast_hasher` | function | `tests/test_facade.py:54` | `def fast_hasher()` |
| `gate_config` | function | `tests/test_facade.py:67` | `def gate_config(fast_hasher)` |
| `test_anonymous_login_page_is_replaced_by_the_cover` | method | `tests/test_facade.py:397` | `def test_anonymous_login_page_is_replaced_by_the_cover(self, facade_client)` |
| `test_anonymous_root_is_replaced_by_the_cover` | method | `tests/test_facade.py:403` | `def test_anonymous_root_is_replaced_by_the_cover(self, facade_client)` |
| `test_audit_is_generic_and_never_contains_the_phrase` | method | `tests/test_facade.py:361` | `def test_audit_is_generic_and_never_contains_the_phrase(self, app, gate_config, audit_records)` |
| `test_authenticated_user_bypasses_the_cover` | method | `tests/test_facade.py:441` | `def test_authenticated_user_bypasses_the_cover(self, tmp_path, fast_hasher)` |
| `test_cover_context_is_cosmetic_and_json_serializable` | method | `tests/test_facade.py:194` | `def test_cover_context_is_cosmetic_and_json_serializable(self)` |
| `test_defaults_are_self_consistent` | method | `tests/test_facade.py:157` | `def test_defaults_are_self_consistent(self)` |
| `test_defaults_keep_duress_alert_off` | method | `tests/test_facade.py:154` | `def test_defaults_keep_duress_alert_off(self)` |
| `test_defaults_keep_the_facade_off` | method | `tests/test_facade.py:149` | `def test_defaults_keep_the_facade_off(self)` |
| `test_disabled_facade_serves_the_real_login` | method | `tests/test_facade.py:469` | `def test_disabled_facade_serves_the_real_login(self, client)` |
| `test_duress_alert_is_opt_in_and_generically_named` | method | `tests/test_facade.py:372` | `def test_duress_alert_is_opt_in_and_generically_named(self, app, fast_hasher, audit_records)` |
| `test_duress_phrase_marks_the_session` | method | `tests/test_facade.py:432` | `def test_duress_phrase_marks_the_session(self, facade_client)` |
| `test_duress_phrase_yields_a_duress_ticket` | method | `tests/test_facade.py:300` | `def test_duress_phrase_yields_a_duress_ticket(self, app, gate_config)` |
| `test_enabled_without_a_hash_fails_open_to_the_real_app` | method | `tests/test_facade.py:474` | `def test_enabled_without_a_hash_fails_open_to_the_real_app(self, tmp_path)` |
| `test_environment_overrides_mapping` | method | `tests/test_facade.py:172` | `def test_environment_overrides_mapping(self, monkeypatch)` |
| `test_from_config_builds_a_working_hasher` | method | `tests/test_facade.py:231` | `def test_from_config_builds_a_working_hasher(self)` |
| `test_gate_configured_requires_enabled_and_a_hash` | method | `tests/test_facade.py:183` | `def test_gate_configured_requires_enabled_and_a_hash(self)` |
| `test_gate_endpoint_is_absent_when_facade_disabled` | method | `tests/test_facade.py:465` | `def test_gate_endpoint_is_absent_when_facade_disabled(self, client)` |
| `test_hash_is_salted_so_two_hashes_differ` | method | `tests/test_facade.py:218` | `def test_hash_is_salted_so_two_hashes_differ(self, fast_hasher)` |
| `test_hash_then_verify_accepts_the_phrase` | method | `tests/test_facade.py:210` | `def test_hash_then_verify_accepts_the_phrase(self, fast_hasher)` |
| `test_issue_rejects_an_unknown_mode` | method | `tests/test_facade.py:256` | `def test_issue_rejects_an_unknown_mode(self)` |
| `test_issue_then_verify_round_trips_the_mode` | method | `tests/test_facade.py:251` | `def test_issue_then_verify_round_trips_the_mode(self)` |
| `test_mapping_overrides_defaults` | method | `tests/test_facade.py:165` | `def test_mapping_overrides_defaults(self)` |
| `test_maximum_length_phrase_is_accepted` | method | `tests/test_facade.py:337` | `def test_maximum_length_phrase_is_accepted(self, app, fast_hasher)` |
| `test_minimum_length_phrase_is_accepted` | method | `tests/test_facade.py:325` | `def test_minimum_length_phrase_is_accepted(self, app, fast_hasher)` |
| `test_miss_without_a_duress_hash` | method | `tests/test_facade.py:314` | `def test_miss_without_a_duress_hash(self, app, fast_hasher)` |
| `test_protected_paths_csv_is_parsed` | method | `tests/test_facade.py:177` | `def test_protected_paths_csv_is_parsed(self)` |
| `test_real_phrase_reveals_the_login` | method | `tests/test_facade.py:417` | `def test_real_phrase_reveals_the_login(self, facade_client)` |
| `test_real_phrase_yields_a_real_ticket` | method | `tests/test_facade.py:292` | `def test_real_phrase_yields_a_real_ticket(self, app, gate_config)` |
| `test_too_long_phrase_is_a_miss` | method | `tests/test_facade.py:355` | `def test_too_long_phrase_is_a_miss(self, app, gate_config)` |
| `test_too_short_phrase_is_a_miss` | method | `tests/test_facade.py:349` | `def test_too_short_phrase_is_a_miss(self, app, gate_config)` |
| `test_verify_rejects_a_malformed_stored_hash` | method | `tests/test_facade.py:224` | `def test_verify_rejects_a_malformed_stored_hash(self, fast_hasher)` |
| `test_verify_rejects_a_non_string_stored_hash` | method | `tests/test_facade.py:227` | `def test_verify_rejects_a_non_string_stored_hash(self, fast_hasher)` |
| `test_verify_rejects_a_non_string_token` | method | `tests/test_facade.py:277` | `def test_verify_rejects_a_non_string_token(self)` |
| `test_verify_rejects_a_ticket_signed_with_another_key` | method | `tests/test_facade.py:267` | `def test_verify_rejects_a_ticket_signed_with_another_key(self)` |
| `test_verify_rejects_a_wrong_phrase` | method | `tests/test_facade.py:214` | `def test_verify_rejects_a_wrong_phrase(self, fast_hasher)` |
| `test_verify_rejects_an_empty_stored_hash` | method | `tests/test_facade.py:221` | `def test_verify_rejects_an_empty_stored_hash(self, fast_hasher)` |
| `test_verify_rejects_an_expired_ticket` | method | `tests/test_facade.py:261` | `def test_verify_rejects_an_expired_ticket(self)` |
| `test_verify_rejects_garbage_and_none` | method | `tests/test_facade.py:272` | `def test_verify_rejects_garbage_and_none(self)` |
| `test_wrong_phrase_is_a_miss_with_no_ticket` | method | `tests/test_facade.py:307` | `def test_wrong_phrase_is_a_miss_with_no_ticket(self, app, gate_config)` |
| `test_wrong_phrase_keeps_the_cover_and_does_not_redirect` | method | `tests/test_facade.py:409` | `def test_wrong_phrase_keeps_the_cover_and_does_not_redirect(self, facade_client)` |
| `test_audit_event_includes_ip_and_ua_by_default` | function | `tests/test_security.py:12` | `def test_audit_event_includes_ip_and_ua_by_default(app, audit_records, monkeypatch)` |
| `test_audit_event_redacts_ip_and_ua_when_disabled` | function | `tests/test_security.py:29` | `def test_audit_event_redacts_ip_and_ua_when_disabled(app, audit_records, monkeypatch)` |
| `test_json_csrf_protect_accepts_valid_header_token` | function | `tests/test_security.py:57` | `def test_json_csrf_protect_accepts_valid_header_token(app)` |
| `test_json_csrf_protect_passes_get_through_without_token` | function | `tests/test_security.py:77` | `def test_json_csrf_protect_passes_get_through_without_token(app)` |
| `test_json_csrf_protect_rejects_missing_token` | function | `tests/test_security.py:45` | `def test_json_csrf_protect_rejects_missing_token(app)` |
| `view` | function | `tests/test_security.py:47` | `def view()` |
| `view` | function | `tests/test_security.py:59` | `def view()` |
| `view` | function | `tests/test_security.py:79` | `def view()` |
| `_client_compute_proof` | function | `tests/test_srp.py:34` | `def _client_compute_proof(username, password, salt_hex, server_a_secret, server_a, server_b)` |
| `_client_derive_verifier` | function | `tests/test_srp.py:27` | `def _client_derive_verifier(username, password, salt_hex)` |
| `_h` | function | `tests/test_srp.py:16` | `def _h()` |
| `_hint` | function | `tests/test_srp.py:23` | `def _hint()` |
| `test_srp6a_full_roundtrip_matches_server_proofs` | function | `tests/test_srp.py:74` | `def test_srp6a_full_roundtrip_matches_server_proofs()` |
| `test_srp6a_wrong_password_produces_mismatched_proof` | function | `tests/test_srp.py:104` | `def test_srp6a_wrong_password_produces_mismatched_proof()` |
| `test_database_path_default_outside_a_context` | function | `tests/test_utils.py:18` | `def test_database_path_default_outside_a_context(monkeypatch)` |
| `test_database_path_honors_env_outside_a_context` | function | `tests/test_utils.py:13` | `def test_database_path_honors_env_outside_a_context(monkeypatch)` |
| `test_database_path_prefers_the_configured_path` | function | `tests/test_utils.py:8` | `def test_database_path_prefers_the_configured_path(app)` |
| `Mutation` | class | `tools/mutation_test.py:56` | `class Mutation` |
| `_is_equivalent_bool` | method | `tools/mutation_test.py:67` | `def _is_equivalent_bool(tokens, index)` |
| `apply_mutation` | method | `tools/mutation_test.py:109` | `def apply_mutation(source, mutation)` |
| `collect` | method | `tools/mutation_test.py:121` | `def collect(targets, limit)` |
| `discover_mutations` | method | `tools/mutation_test.py:79` | `def discover_mutations(path, source)` |
| `main` | method | `tools/mutation_test.py:157` | `def main(argv)` |
| `purge_bytecode` | method | `tools/mutation_test.py:133` | `def purge_bytecode()` |
| `run_suite` | method | `tools/mutation_test.py:142` | `def run_suite(python, tests)` |
| `Cache` | class | `utils/cache.py:6` | `class Cache` |
| `__init__` | method | `utils/cache.py:8` | `def __init__(self)` |
| `delete` | method | `utils/cache.py:20` | `def delete(self, key)` |
| `get` | method | `utils/cache.py:11` | `def get(self, key)` |
| `set` | method | `utils/cache.py:16` | `def set(self, key, value, ttl)` |
| `external_url` | function | `utils/mailer.py:22` | `def external_url(path)` |
| `mail_is_configured` | function | `utils/mailer.py:38` | `def mail_is_configured()` |
| `send_transactional_email` | function | `utils/mailer.py:51` | `def send_transactional_email(subject, recipients, body)` |
| `SubscriptionPlans` | class | `utils/plans.py:3` | `class SubscriptionPlans` |
| `get_plan` | method | `utils/plans.py:30` | `def get_plan(plan_name)` |
| `validate_plan_payment` | method | `utils/plans.py:42` | `def validate_plan_payment(plan_name, amount_paid)` |
| `_is_trial_elapsed` | function | `utils/scheduler.py:54` | `def _is_trial_elapsed(user)` |
| `_now_utc` | function | `utils/scheduler.py:32` | `def _now_utc()` |
| `check_trial_expiration` | function | `utils/scheduler.py:72` | `def check_trial_expiration()` |
| `cleanup_old_messages` | function | `utils/scheduler.py:118` | `def cleanup_old_messages()` |
| `init_scheduler` | function | `utils/scheduler.py:37` | `def init_scheduler(app, mail)` |
| `_correlation_id` | function | `utils/security.py:72` | `def _correlation_id()` |
| `_extract_csrf_token` | function | `utils/security.py:172` | `def _extract_csrf_token()` |
| `_get_audit_logger` | function | `utils/security.py:46` | `def _get_audit_logger()` |
| `audit_event` | function | `utils/security.py:86` | `def audit_event(event)` |
| `constant_time_compare` | function | `utils/security.py:123` | `def constant_time_compare(a, b)` |
| `hash_secret` | function | `utils/security.py:135` | `def hash_secret(secret)` |
| `json_csrf_protect` | function | `utils/security.py:193` | `def json_csrf_protect(view)` |
| `new_one_time_code` | function | `utils/security.py:163` | `def new_one_time_code(length)` |
| `verify_secret` | function | `utils/security.py:156` | `def verify_secret(secret, expected_hash)` |
| `wrapper` | function | `utils/security.py:207` | `def wrapper()` |
| `SRPSessionStore` | class | `utils/srp6a.py:150` | `class SRPSessionStore` |
| `__init__` | method | `utils/srp6a.py:158` | `def __init__(self, storage_uri)` |
| `_hash` | function | `utils/srp6a.py:60` | `def _hash()` |
| `_hash_int` | function | `utils/srp6a.py:68` | `def _hash_int()` |
| `_key` | method | `utils/srp6a.py:168` | `def _key(username)` |
| `compute_k` | function | `utils/srp6a.py:73` | `def compute_k()` |
| `compute_proofs` | function | `utils/srp6a.py:107` | `def compute_proofs(username, salt_hex, verifier, server_a, server_b, server_b_secret)` |
| `compute_u` | function | `utils/srp6a.py:78` | `def compute_u(server_a, server_b)` |
| `generate_server_challenge` | function | `utils/srp6a.py:91` | `def generate_server_challenge(verifier)` |
| `hello` | method | `utils/srp6a.py:224` | `def hello(store, username, client_a_hex, salt_hex, verifier_hex)` |
| `i2osp` | function | `utils/srp6a.py:47` | `def i2osp(value)` |
| `load` | method | `utils/srp6a.py:202` | `def load(self, username)` |
| `save` | method | `utils/srp6a.py:172` | `def save(self, username, salt_hex, verifier_hex, server_a_hex, server_b_hex, server_b_secret_hex)` |
| `verify` | method | `utils/srp6a.py:260` | `def verify(store, username, client_m1_hex)` |
| `Config` | class | `utils/utils.py:103` | `class Config` |
| `Payload` | class | `utils/utils.py:80` | `class Payload(TypedDict)` |
| `__getitem__` | method | `utils/utils.py:165` | `def __getitem__(self, key)` |
| `__init__` | method | `utils/utils.py:145` | `def __init__(self, config_dict)` |
| `as_bool` | function | `utils/utils.py:29` | `def as_bool(value, default)` |
| `database_path` | function | `utils/utils.py:12` | `def database_path()` |
| `load_payload` | method | `utils/utils.py:168` | `def load_payload()` |
| `sanitize_path` | function | `utils/utils.py:49` | `def sanitize_path(path)` |
| `about` | function | `views/about.py:6` | `def about()` |
| `delete_vault` | function | `views/account.py:130` | `def delete_vault()` |
| `get_deniable_vault_controller` | function | `views/account.py:51` | `def get_deniable_vault_controller()` |
| `get_vault` | function | `views/account.py:85` | `def get_vault()` |
| `put_vault` | function | `views/account.py:107` | `def put_vault()` |
| `settings` | function | `views/account.py:65` | `def settings()` |
| `PlanForm` | class | `views/admin.py:57` | `class PlanForm(FlaskForm)` |
| `UserEditForm` | class | `views/admin.py:24` | `class UserEditForm(FlaskForm)` |
| `admin` | method | `views/admin.py:69` | `def admin()` |
| `admin_contacts` | method | `views/admin.py:490` | `def admin_contacts()` |
| `edit_plan` | method | `views/admin.py:220` | `def edit_plan(plan_name)` |
| `manage_plans` | method | `views/admin.py:196` | `def manage_plans()` |
| `superadmin` | method | `views/admin.py:256` | `def superadmin()` |
| `superadmin_edit_user` | method | `views/admin.py:91` | `def superadmin_edit_user(username)` |
| `superadmin_resend_confirmation` | method | `views/admin.py:391` | `def superadmin_resend_confirmation(username)` |
| `superadmin_reset_mfa` | method | `views/admin.py:343` | `def superadmin_reset_mfa(username)` |
| `superadmin_toggle_suspend` | method | `views/admin.py:439` | `def superadmin_toggle_suspend(username)` |
| `ContactForm` | class | `views/auth.py:108` | `class ContactForm(FlaskForm)` |
| `LoginForm` | class | `views/auth.py:124` | `class LoginForm(FlaskForm)` |
| `MFAForm` | class | `views/auth.py:103` | `class MFAForm(FlaskForm)` |
| `PhoneVerificationForm` | class | `views/auth.py:98` | `class PhoneVerificationForm(FlaskForm)` |
| `RegisterForm` | class | `views/auth.py:114` | `class RegisterForm(FlaskForm)` |
| `_recovery_key` | method | `views/auth.py:266` | `def _recovery_key()` |
| `_srp_key` | method | `views/auth.py:255` | `def _srp_key()` |
| `confirm_email` | method | `views/auth.py:344` | `def confirm_email(token)` |
| `contact` | method | `views/auth.py:454` | `def contact()` |
| `decorated_function` | method | `views/auth.py:87` | `def decorated_function()` |
| `decorator` | method | `views/auth.py:85` | `def decorator(f)` |
| `get_auth_controller` | method | `views/auth.py:132` | `def get_auth_controller()` |
| `get_csrf_token` | method | `views/auth.py:619` | `def get_csrf_token()` |
| `get_public_key` | method | `views/auth.py:485` | `def get_public_key()` |
| `get_recovery_bundle` | method | `views/auth.py:534` | `def get_recovery_bundle()` |
| `get_user_keys` | method | `views/auth.py:503` | `def get_user_keys()` |
| `handle_register` | method | `views/auth.py:150` | `def handle_register()` |
| `login` | method | `views/auth.py:234` | `def login()` |
| `logout` | method | `views/auth.py:337` | `def logout()` |
| `recover` | method | `views/auth.py:242` | `def recover()` |
| `resend_phone_verification` | method | `views/auth.py:384` | `def resend_phone_verification()` |
| `reset_with_recovery` | method | `views/auth.py:559` | `def reset_with_recovery()` |
| `role_required` | function | `views/auth.py:71` | `def role_required()` |
| `show_register` | method | `views/auth.py:143` | `def show_register()` |
| `srp_hello` | method | `views/auth.py:278` | `def srp_hello()` |
| `srp_verify` | method | `views/auth.py:299` | `def srp_verify()` |
| `toggle_mfa` | method | `views/auth.py:429` | `def toggle_mfa()` |
| `verify_mfa` | method | `views/auth.py:407` | `def verify_mfa()` |
| `verify_phone` | method | `views/auth.py:367` | `def verify_phone()` |
| `_build_cover_service` | function | `views/facade.py:71` | `def _build_cover_service(config)` |
| `_facade_cover` | function | `views/facade.py:48` | `def _facade_cover()` |
| `_ticket_mode` | function | `views/facade.py:86` | `def _ticket_mode(gate)` |
| `facade_gate` | function | `views/facade.py:60` | `def facade_gate()` |
| `register_facade` | function | `views/facade.py:33` | `def register_facade(app)` |
| `render_cover` | function | `views/facade.py:41` | `def render_cover()` |
| `faq` | function | `views/faq.py:7` | `def faq()` |
| `landing` | function | `views/faq.py:12` | `def landing()` |
| `UploadForm` | class | `views/file.py:15` | `class UploadForm(FlaskForm)` |
| `download` | method | `views/file.py:56` | `def download(filename)` |
| `upload` | method | `views/file.py:25` | `def upload()` |
| `MessageForm` | class | `views/message.py:19` | `class MessageForm(FlaskForm)` |
| `api_secure_message` | method | `views/message.py:49` | `def api_secure_message()` |
| `messages` | method | `views/message.py:29` | `def messages()` |
| `privacy` | function | `views/privacy.py:6` | `def privacy()` |
| `SubscriptionForm` | class | `views/subscription.py:24` | `class SubscriptionForm(FlaskForm)` |
| `__init__` | method | `views/subscription.py:26` | `def __init__(self)` |
| `payment_success` | method | `views/subscription.py:86` | `def payment_success()` |
| `subscribe` | method | `views/subscription.py:37` | `def subscribe()` |
| `secure_sync` | function | `views/sync.py:29` | `def secure_sync()` |
| `sync_page` | function | `views/sync.py:79` | `def sync_page()` |
| `terms` | function | `views/terms.py:6` | `def terms()` |
| `MFAEnableForm` | class | `views/views.py:15` | `class MFAEnableForm(FlaskForm)` |
| `home` | method | `views/views.py:21` | `def home()` |
