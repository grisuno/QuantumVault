# Symbols (page 1 of 2)
Pages: [SYMBOLS.md](SYMBOLS.md), [SYMBOLS_p2.md](SYMBOLS_p2.md)

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `_is_production_like` | function | `app.py:58` | `def _is_production_like()` |
| `main` | function | `app.py:21` | `def main()` |
| `_build_csp` | function | `app_factory.py:82` | `def _build_csp()` |
| `_build_talisman_kwargs` | function | `app_factory.py:119` | `def _build_talisman_kwargs()` |
| `_configure_logging` | function | `app_factory.py:220` | `def _configure_logging(app)` |
| `_configure_secret_key` | function | `app_factory.py:160` | `def _configure_secret_key(app, config)` |
| `_configure_session` | function | `app_factory.py:203` | `def _configure_session(app)` |
| `_is_production` | function | `app_factory.py:71` | `def _is_production()` |
| `create_app` | function | `app_factory.py:237` | `def create_app(config_overrides, security_overrides)` |
| `load_user` | function | `app_factory.py:416` | `def load_user(user_id)` |
| `main` | function | `client.go:13` | `func main(` |
| `AuthController` | class | `controllers/auth.py:58` | `class AuthController` |
| `__init__` | method | `controllers/auth.py:61` | `def __init__(self, db_path, mail, storage_uri)` |
| `_is_code_valid` | method | `controllers/auth.py:349` | `def _is_code_valid(self, expires_at)` |
| `_now_utc` | function | `controllers/auth.py:49` | `def _now_utc()` |
| `register` | method | `controllers/auth.py:76` | `def register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone...` |
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
| `FileController` | class | `controllers/file.py:51` | `class FileController` |
| `__init__` | method | `controllers/file.py:54` | `def __init__(self, users_path, s3_bucket, s3_client)` |
| `_key` | method | `controllers/file.py:59` | `def _key(self, username, filename, suffix)` |
| `_log_s3_error` | function | `controllers/file.py:28` | `def _log_s3_error(operation, error)` |
| `get_encrypted_file_and_key` | method | `controllers/file.py:118` | `def get_encrypted_file_and_key(self, username, filename)` |
| `get_storage_usage` | method | `controllers/file.py:71` | `def get_storage_usage(self, username)` |
| `list_encrypted_files` | method | `controllers/file.py:148` | `def list_encrypted_files(self, username)` |
| `safe_filename` | function | `controllers/file.py:33` | `def safe_filename(name)` |
| `upload_encrypted_file` | method | `controllers/file.py:85` | `def upload_encrypted_file(self, username, file_storage, wrapped_fek)` |
| `MessageController` | class | `controllers/message.py:19` | `class MessageController` |
| `__init__` | method | `controllers/message.py:22` | `def __init__(self, users_path, users_db_path)` |
| `get_messages` | method | `controllers/message.py:90` | `def get_messages(self, username, page, per_page)` |
| `send_encrypted_message` | method | `controllers/message.py:36` | `def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)` |
| `ChannelMode` | class | `controllers/secure_channel.py:65` | `class ChannelMode(Enum)` |
| `ChannelStatus` | class | `controllers/secure_channel.py:174` | `class ChannelStatus` |
| `SecureChannelConfig` | class | `controllers/secure_channel.py:116` | `class SecureChannelConfig` |
| `SecureChannelManager` | class | `controllers/secure_channel.py:220` | `class SecureChannelManager` |
| `__init__` | method | `controllers/secure_channel.py:223` | `def __init__(self, state_dir, local_port, local_scheme, cloudflared_bin, tor_bin, start_timeout_seconds, launcher...` |
| `_as_port` | method | `controllers/secure_channel.py:96` | `def _as_port(value, default)` |
| `_as_scheme` | method | `controllers/secure_channel.py:107` | `def _as_scheme(value, default)` |
| `_cleanup_scratch` | method | `controllers/secure_channel.py:405` | `def _cleanup_scratch(self)` |
| `_default_killer` | method | `controllers/secure_channel.py:207` | `def _default_killer(pid)` |
| `_default_launcher` | method | `controllers/secure_channel.py:193` | `def _default_launcher(cmd, log_path)` |
| `_fingerprint` | method | `controllers/secure_channel.py:503` | `def _fingerprint(value)` |
| `_normalize_onion` | method | `controllers/secure_channel.py:509` | `def _normalize_onion(raw)` |
| `_pid_live` | method | `controllers/secure_channel.py:488` | `def _pid_live(self, pid)` |
| `_read_state` | method | `controllers/secure_channel.py:356` | `def _read_state(self)` |
| `_remove_state` | method | `controllers/secure_channel.py:396` | `def _remove_state(self)` |
| `_resolve_binary` | method | `controllers/secure_channel.py:471` | `def _resolve_binary(self, binary)` |
| `_start_cloudflared` | method | `controllers/secure_channel.py:418` | `def _start_cloudflared(self)` |
| `_start_tor` | method | `controllers/secure_channel.py:438` | `def _start_tor(self)` |
| `_state_path` | method | `controllers/secure_channel.py:352` | `def _state_path(self)` |
| `_status_for` | method | `controllers/secure_channel.py:337` | `def _status_for(self, mode, cloud_url, onion_url, pids)` |
| `_wait_for_file` | method | `controllers/secure_channel.py:535` | `def _wait_for_file(path, timeout_seconds)` |
| `_wait_for_pattern` | method | `controllers/secure_channel.py:517` | `def _wait_for_pattern(path, pattern, timeout_seconds)` |
| `_write_state` | method | `controllers/secure_channel.py:371` | `def _write_state(self, current)` |
| `active` | method | `controllers/secure_channel.py:184` | `def active(self)` |
| `audit_details` | method | `controllers/secure_channel.py:321` | `def audit_details(self, action, mode, cloud_url, onion_url)` |
| `configured` | method | `controllers/secure_channel.py:129` | `def configured(self)` |
| `from_config` | method | `controllers/secure_channel.py:252` | `def from_config(cls, config, launcher, killer)` |
| `from_mapping` | method | `controllers/secure_channel.py:134` | `def from_mapping(cls, mapping, env)` |
| `is_cloudflare_url` | method | `controllers/secure_channel.py:82` | `def is_cloudflare_url(value)` |
| `is_onion_url` | method | `controllers/secure_channel.py:89` | `def is_onion_url(value)` |
| `origin_url` | method | `controllers/secure_channel.py:247` | `def origin_url(self)` |
| `parse` | method | `controllers/secure_channel.py:74` | `def parse(cls, raw)` |
| `read` | method | `controllers/secure_channel.py:142` | `def read(key)` |
| `rotate` | method | `controllers/secure_channel.py:314` | `def rotate(self)` |
| `start` | method | `controllers/secure_channel.py:281` | `def start(self, mode)` |
| `status` | method | `controllers/secure_channel.py:270` | `def status(self)` |
| `stop` | method | `controllers/secure_channel.py:301` | `def stop(self)` |
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
| `create_user` | method | `models/user.py:325` | `def create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone...` |
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
| `CheckResult` | class | `scripts/doctor.py:98` | `class CheckResult` |
| `DoctorReport` | class | `scripts/doctor.py:108` | `class DoctorReport` |
| `add` | method | `scripts/doctor.py:113` | `def add(self, result)` |
| `apply_fixes` | method | `scripts/doctor.py:493` | `def apply_fixes(report)` |
| `apt_command` | method | `scripts/doctor.py:288` | `def apt_command(packages)` |
| `check_binary` | method | `scripts/doctor.py:186` | `def check_binary(name, env_override)` |
| `check_env_file` | method | `scripts/doctor.py:210` | `def check_env_file()` |
| `check_module` | method | `scripts/doctor.py:170` | `def check_module(name)` |
| `check_python` | method | `scripts/doctor.py:154` | `def check_python(minimum)` |
| `check_tcp` | method | `scripts/doctor.py:242` | `def check_tcp(name, host, port, timeout)` |
| `cloudflared_deb_url` | method | `scripts/doctor.py:270` | `def cloudflared_deb_url(version, arch)` |
| `collect_report` | method | `scripts/doctor.py:449` | `def collect_report()` |
| `debian_arch` | method | `scripts/doctor.py:261` | `def debian_arch(deb)` |
| `download_file` | method | `scripts/doctor.py:319` | `def download_file(url, destination)` |
| `effective_env` | method | `scripts/doctor.py:147` | `def effective_env()` |
| `exit_code` | method | `scripts/doctor.py:123` | `def exit_code(self)` |
| `failures` | method | `scripts/doctor.py:118` | `def failures(self)` |
| `fix_apt` | method | `scripts/doctor.py:360` | `def fix_apt(packages)` |
| `fix_cloudflared` | method | `scripts/doctor.py:373` | `def fix_cloudflared(version, bin_dir)` |
| `fix_garage` | method | `scripts/doctor.py:417` | `def fix_garage(version, destination)` |
| `fix_python_deps` | method | `scripts/doctor.py:352` | `def fix_python_deps()` |
| `garage_bin_url` | method | `scripts/doctor.py:283` | `def garage_bin_url(version, target)` |
| `load_env_file` | method | `scripts/doctor.py:128` | `def load_env_file(path)` |
| `main` | method | `scripts/doctor.py:530` | `def main(argv)` |
| `parse_host_port` | method | `scripts/doctor.py:223` | `def parse_host_port(uri, default_port)` |
| `print_report` | method | `scripts/doctor.py:476` | `def print_report(report)` |
| `run_command` | method | `scripts/doctor.py:298` | `def run_command(cmd)` |
| `upsert_env` | method | `scripts/doctor.py:334` | `def upsert_env(key, value, path)` |
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
| `H` | function | `static/js/qv-crypto.js:168` | `` |
| `Hint` | function | `static/js/qv-crypto.js:172` | `` |
| `aesGcmDecrypt` | function | `static/js/qv-crypto.js:220` | `` |
| `aesGcmEncrypt` | function | `static/js/qv-crypto.js:209` | `` |
| `base64ToBytes` | function | `static/js/qv-crypto.js:113` | `` |
| `buildRegistration` | function | `static/js/qv-crypto.js:496` | `` |
| `bytesToBase32` | function | `static/js/qv-crypto.js:95` | `` |
| `bytesToBase64` | function | `static/js/qv-crypto.js:84` | `` |
| `bytesToBigInt` | function | `static/js/qv-crypto.js:120` | `` |
| `bytesToHex` | function | `static/js/qv-crypto.js:78` | `` |
| `computeK` | function | `static/js/qv-crypto.js:250` | `` |
| `concatBytes` | function | `static/js/qv-crypto.js:58` | `` |
| `decryptInbox` | function | `static/js/qv-crypto.js:714` | `` |
| `deriveKeyFromPassphrase` | function | `static/js/qv-crypto.js:184` | `` |
| `deriveMasterKey` | function | `static/js/qv-crypto.js:205` | `` |
| `derivePublicKeyFromPrivateBlob` | function | `static/js/qv-crypto.js:455` | `` |
| `deriveVerifier` | function | `static/js/qv-crypto.js:255` | `` |
| `deriveWrapKey` | function | `static/js/qv-crypto.js:359` | `` |
| `downloadAndDecrypt` | function | `static/js/qv-crypto.js:629` | `` |
| `encryptAndUpload` | function | `static/js/qv-crypto.js:599` | `` |
| `fetchPublicKey` | function | `static/js/qv-crypto.js:668` | `` |
| `generateIdentity` | function | `static/js/qv-crypto.js:315` | `` |
| `generateRecoveryCode` | function | `static/js/qv-crypto.js:417` | `` |
| `hexToBytes` | function | `static/js/qv-crypto.js:69` | `` |
| `i2osp` | function | `static/js/qv-crypto.js:127` | `` |
| `login` | function | `static/js/qv-crypto.js:592` | `` |
| `mod` | function | `static/js/qv-crypto.js:137` | `` |
| `modPow` | function | `static/js/qv-crypto.js:141` | `` |
| `normalizeRecoveryCode` | function | `static/js/qv-crypto.js:428` | `` |
| `parsePrivateBlob` | function | `static/js/qv-crypto.js:351` | `` |
| `parsePublicKey` | function | `static/js/qv-crypto.js:343` | `` |
| `postJson` | function | `static/js/qv-crypto.js:473` | `` |
| `randomBytes` | function | `static/js/qv-crypto.js:159` | `` |
| `recoverAccount` | function | `static/js/qv-crypto.js:541` | `` |
| `register` | function | `static/js/qv-crypto.js:530` | `` |
| `sendSecureMessage` | function | `static/js/qv-crypto.js:683` | `` |
| `srpLogin` | function | `static/js/qv-crypto.js:263` | `` |
| `unwrapKey` | function | `static/js/qv-crypto.js:395` | `` |
| `wrapKey` | function | `static/js/qv-crypto.js:371` | `` |
| `wrapPrivateKeyForRecovery` | function | `static/js/qv-crypto.js:436` | `` |
| `buildDeniableVault` | function | `static/js/qv-deniable.js:125` | `` |
| `frame` | function | `static/js/qv-deniable.js:55` | `` |
| `openDeniableVault` | function | `static/js/qv-deniable.js:170` | `` |
| `openSlot` | function | `static/js/qv-deniable.js:102` | `` |
| `sealSlot` | function | `static/js/qv-deniable.js:82` | `` |
| `toBytes` | function | `static/js/qv-deniable.js:47` | `` |
| `unframe` | function | `static/js/qv-deniable.js:64` | `` |
| `bucketFor` | function | `static/js/qv-padding.js:20` | `` |
| `padFramed` | function | `static/js/qv-padding.js:42` | `` |
| `randomPad` | function | `static/js/qv-padding.js:33` | `` |
| `tableFor` | function | `static/js/qv-padding.js:15` | `` |
| `unframeFramed` | function | `static/js/qv-padding.js:54` | `` |
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
| `_ListLogHandler` | class | `tests/conftest.py:106` | `class _ListLogHandler(Handler)` |
| `__init__` | method | `tests/conftest.py:109` | `def __init__(self)` |
| `_hermetic_env` | function | `tests/conftest.py:26` | `def _hermetic_env(monkeypatch)` |
| `_push_request_context` | function | `tests/conftest.py:58` | `def _push_request_context()` |
| `app` | function | `tests/conftest.py:76` | `def app(tmp_path)` |
| `audit_records` | method | `tests/conftest.py:118` | `def audit_records()` |
| `client` | function | `tests/conftest.py:101` | `def client(app)` |
| `emit` | method | `tests/conftest.py:113` | `def emit(self, record)` |
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
| `test_apt_command_uses_sudo_outside_root` | function | `tests/test_doctor.py:105` | `def test_apt_command_uses_sudo_outside_root()` |
| `test_check_binary_finds_present_binary` | function | `tests/test_doctor.py:23` | `def test_check_binary_finds_present_binary()` |
| `test_check_binary_flags_missing_binary` | function | `tests/test_doctor.py:30` | `def test_check_binary_flags_missing_binary()` |
| `test_check_binary_honors_absolute_override` | function | `tests/test_doctor.py:38` | `def test_check_binary_honors_absolute_override(tmp_path)` |
| `test_check_module_reports_status` | function | `tests/test_doctor.py:48` | `def test_check_module_reports_status()` |
| `test_check_python_accepts_current_runtime` | function | `tests/test_doctor.py:56` | `def test_check_python_accepts_current_runtime()` |
| `test_check_tcp_refused_reports_remedy` | function | `tests/test_doctor.py:83` | `def test_check_tcp_refused_reports_remedy()` |
| `test_load_env_file_parses_assignments` | function | `tests/test_doctor.py:129` | `def test_load_env_file_parses_assignments(tmp_path)` |
| `test_parse_host_port_shapes` | function | `tests/test_doctor.py:62` | `def test_parse_host_port_shapes()` |
| `test_release_url_builders` | function | `tests/test_doctor.py:90` | `def test_release_url_builders()` |
| `test_report_exit_code_reflects_failures` | function | `tests/test_doctor.py:115` | `def test_report_exit_code_reflects_failures()` |
| `test_upsert_env_replaces_and_appends` | function | `tests/test_doctor.py:140` | `def test_upsert_env_replaces_and_appends(tmp_path)` |
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

Next: [SYMBOLS_p2.md](SYMBOLS_p2.md)
