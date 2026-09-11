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
| `AuthController` | class | `controllers/auth.py:57` | `class AuthController` |
| `__init__` | method | `controllers/auth.py:60` | `def __init__(self, db_path, mail, storage_uri)` |
| `_is_code_valid` | method | `controllers/auth.py:348` | `def _is_code_valid(self, expires_at)` |
| `_now_utc` | function | `controllers/auth.py:48` | `def _now_utc()` |
| `register` | method | `controllers/auth.py:75` | `def register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_na` |
| `resend_phone_code` | method | `controllers/auth.py:309` | `def resend_phone_code(self, username)` |
| `send_confirmation_email` | method | `controllers/auth.py:155` | `def send_confirmation_email(self, email, username, token)` |
| `send_mfa_code` | method | `controllers/auth.py:392` | `def send_mfa_code(self, username)` |
| `send_sms_verification` | method | `controllers/auth.py:252` | `def send_sms_verification(self, phone, code, username)` |
| `srp_hello` | method | `controllers/auth.py:201` | `def srp_hello(self, username, client_a_hex)` |
| `srp_verify` | method | `controllers/auth.py:220` | `def srp_verify(self, username, client_m1_hex)` |
| `toggle_mfa` | method | `controllers/auth.py:415` | `def toggle_mfa(self, username, enable)` |
| `verify_mfa_code` | method | `controllers/auth.py:368` | `def verify_mfa_code(self, username, code)` |
| `verify_phone_code` | method | `controllers/auth.py:273` | `def verify_phone_code(self, username, code)` |
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
| `FileController` | class | `controllers/file.py:49` | `class FileController` |
| `__init__` | method | `controllers/file.py:52` | `def __init__(self, users_path, s3_bucket, s3_client)` |
| `_key` | method | `controllers/file.py:57` | `def _key(self, username, filename, suffix)` |
| `_log_s3_error` | function | `controllers/file.py:26` | `def _log_s3_error(operation, error)` |
| `get_encrypted_file_and_key` | method | `controllers/file.py:107` | `def get_encrypted_file_and_key(self, username, filename)` |
| `get_storage_usage` | method | `controllers/file.py:69` | `def get_storage_usage(self, username)` |
| `list_encrypted_files` | method | `controllers/file.py:137` | `def list_encrypted_files(self, username)` |
| `safe_filename` | function | `controllers/file.py:31` | `def safe_filename(name)` |
| `upload_encrypted_file` | method | `controllers/file.py:83` | `def upload_encrypted_file(self, username, file_storage, wrapped_fek)` |
| `MessageController` | class | `controllers/message.py:15` | `class MessageController` |
| `__init__` | method | `controllers/message.py:18` | `def __init__(self, users_path, users_db_path)` |
| `get_messages` | method | `controllers/message.py:73` | `def get_messages(self, username, page, per_page)` |
| `send_encrypted_message` | method | `controllers/message.py:31` | `def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)` |
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
| `handleOpen` | function | `static/js/account.js:98` | `` |
| `handleReset` | function | `static/js/account.js:120` | `` |
| `init` | function | `static/js/account.js:133` | `` |
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
| `test_resend_endpoint_is_registered` | function | `tests/test_auth_phone.py:25` | `def test_resend_endpoint_is_registered(app)` |
| `test_resend_route_accepts_only_post` | function | `tests/test_auth_phone.py:31` | `def test_resend_route_accepts_only_post(app)` |
| `test_verify_phone_page_renders` | function | `tests/test_auth_phone.py:18` | `def test_verify_phone_page_renders(client)` |
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
| `Config` | class | `utils/utils.py:85` | `class Config` |
| `Payload` | class | `utils/utils.py:62` | `class Payload(TypedDict)` |
| `__getitem__` | method | `utils/utils.py:147` | `def __getitem__(self, key)` |
| `__init__` | method | `utils/utils.py:127` | `def __init__(self, config_dict)` |
| `as_bool` | function | `utils/utils.py:11` | `def as_bool(value, default)` |
| `load_payload` | method | `utils/utils.py:150` | `def load_payload()` |
| `sanitize_path` | function | `utils/utils.py:31` | `def sanitize_path(path)` |
| `about` | function | `views/about.py:6` | `def about()` |
| `delete_vault` | function | `views/account.py:122` | `def delete_vault()` |
| `get_deniable_vault_controller` | function | `views/account.py:50` | `def get_deniable_vault_controller()` |
| `get_vault` | function | `views/account.py:77` | `def get_vault()` |
| `put_vault` | function | `views/account.py:99` | `def put_vault()` |
| `settings` | function | `views/account.py:64` | `def settings()` |
| `PlanForm` | class | `views/admin.py:56` | `class PlanForm(FlaskForm)` |
| `UserEditForm` | class | `views/admin.py:23` | `class UserEditForm(FlaskForm)` |
| `admin` | method | `views/admin.py:68` | `def admin()` |
| `admin_contacts` | method | `views/admin.py:489` | `def admin_contacts()` |
| `edit_plan` | method | `views/admin.py:219` | `def edit_plan(plan_name)` |
| `manage_plans` | method | `views/admin.py:195` | `def manage_plans()` |
| `superadmin` | method | `views/admin.py:255` | `def superadmin()` |
| `superadmin_edit_user` | method | `views/admin.py:90` | `def superadmin_edit_user(username)` |
| `superadmin_resend_confirmation` | method | `views/admin.py:390` | `def superadmin_resend_confirmation(username)` |
| `superadmin_reset_mfa` | method | `views/admin.py:342` | `def superadmin_reset_mfa(username)` |
| `superadmin_toggle_suspend` | method | `views/admin.py:438` | `def superadmin_toggle_suspend(username)` |
| `ContactForm` | class | `views/auth.py:107` | `class ContactForm(FlaskForm)` |
| `LoginForm` | class | `views/auth.py:123` | `class LoginForm(FlaskForm)` |
| `MFAForm` | class | `views/auth.py:102` | `class MFAForm(FlaskForm)` |
| `PhoneVerificationForm` | class | `views/auth.py:97` | `class PhoneVerificationForm(FlaskForm)` |
| `RegisterForm` | class | `views/auth.py:113` | `class RegisterForm(FlaskForm)` |
| `_recovery_key` | method | `views/auth.py:265` | `def _recovery_key()` |
| `_srp_key` | method | `views/auth.py:254` | `def _srp_key()` |
| `confirm_email` | method | `views/auth.py:343` | `def confirm_email(token)` |
| `contact` | method | `views/auth.py:453` | `def contact()` |
| `decorated_function` | method | `views/auth.py:86` | `def decorated_function()` |
| `decorator` | method | `views/auth.py:84` | `def decorator(f)` |
| `get_auth_controller` | method | `views/auth.py:131` | `def get_auth_controller()` |
| `get_csrf_token` | method | `views/auth.py:618` | `def get_csrf_token()` |
| `get_public_key` | method | `views/auth.py:484` | `def get_public_key()` |
| `get_recovery_bundle` | method | `views/auth.py:533` | `def get_recovery_bundle()` |
| `get_user_keys` | method | `views/auth.py:502` | `def get_user_keys()` |
| `handle_register` | method | `views/auth.py:149` | `def handle_register()` |
| `login` | method | `views/auth.py:233` | `def login()` |
| `logout` | method | `views/auth.py:336` | `def logout()` |
| `recover` | method | `views/auth.py:241` | `def recover()` |
| `resend_phone_verification` | method | `views/auth.py:383` | `def resend_phone_verification()` |
| `reset_with_recovery` | method | `views/auth.py:558` | `def reset_with_recovery()` |
| `role_required` | function | `views/auth.py:70` | `def role_required()` |
| `show_register` | method | `views/auth.py:142` | `def show_register()` |
| `srp_hello` | method | `views/auth.py:277` | `def srp_hello()` |
| `srp_verify` | method | `views/auth.py:298` | `def srp_verify()` |
| `toggle_mfa` | method | `views/auth.py:428` | `def toggle_mfa()` |
| `verify_mfa` | method | `views/auth.py:406` | `def verify_mfa()` |
| `verify_phone` | method | `views/auth.py:366` | `def verify_phone()` |
| `faq` | function | `views/faq.py:6` | `def faq()` |
| `landing` | function | `views/faq.py:11` | `def landing()` |
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
| `MFAEnableForm` | class | `views/views.py:14` | `class MFAEnableForm(FlaskForm)` |
| `home` | method | `views/views.py:20` | `def home()` |
