# API (page 1 of 2)
Pages: [API.md](API.md), [API_p2.md](API_p2.md)

## app.py
Depends on: `app_factory.py`, `utils/utils.py`
Imported by: `scripts/test_bloque1.py`
- `main` (function) `app.py:21` `def main()`

## app_factory.py
Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`
- `create_app` (function) `app_factory.py:237` `def create_app(config_overrides, security_overrides)` -- Build and return a fully-configured Flask application.
- `load_user` (function) `app_factory.py:416` `def load_user(user_id)`

## client.go
- `main` (function) `client.go:13` `func main(`

## controllers/auth.py
Depends on: `models/plans.py`, `models/user.py`, `utils/__init__.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
Imported by: `views/auth.py`
- `AuthController.__init__` (method) `controllers/auth.py:61` `def __init__(self, db_path, mail, storage_uri)` -- Initialize the controller.
- `AuthController.register` (method) `controllers/auth.py:76` `def register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone...` -- Register a user from client-generated zero-knowledge credentials.
- `AuthController.send_confirmation_email` (method) `controllers/auth.py:156` `def send_confirmation_email(self, email, username, token)` -- Email the account-confirmation link to a freshly registered user.
- `AuthController.srp_hello` (method) `controllers/auth.py:202` `def srp_hello(self, username, client_a_hex)` -- Begin an SRP-6a login and return the salt and server challenge B.
- `AuthController.srp_verify` (method) `controllers/auth.py:221` `def srp_verify(self, username, client_m1_hex)` -- Complete an SRP-6a login and return the authenticated user and proof.
- `AuthController.send_sms_verification` (method) `controllers/auth.py:253` `def send_sms_verification(self, phone, code, username)` -- Send a verification code via SMS.
- `AuthController.verify_phone_code` (method) `controllers/auth.py:274` `def verify_phone_code(self, username, code)` -- Verify a phone verification code for a user.
- `AuthController.resend_phone_code` (method) `controllers/auth.py:310` `def resend_phone_code(self, username)` -- Issue and send a fresh phone verification code.
- `AuthController.verify_mfa_code` (method) `controllers/auth.py:369` `def verify_mfa_code(self, username, code)` -- Verify a multi-factor authentication code for a user.
- `AuthController.send_mfa_code` (method) `controllers/auth.py:393` `def send_mfa_code(self, username)` -- Generate, store, and send an MFA code to the user's phone.
- `AuthController.toggle_mfa` (method) `controllers/auth.py:416` `def toggle_mfa(self, username, enable)` -- Enable or disable MFA for a user.

## controllers/contact.py
Depends on: `models/contact.py`
Imported by: `views/admin.py`, `views/auth.py`
- `ContactController.__init__` (method) `controllers/contact.py:6` `def __init__(self, db_path)` -- Initialize the ContactController with the database path.
- `ContactController.create_contact` (method) `controllers/contact.py:14` `def create_contact(self, user_id, subject, message)` -- Create a new contact message.
- `ContactController.get_user_contacts` (method) `controllers/contact.py:36` `def get_user_contacts(self, user_id)` -- Retrieve all contact messages for a user.

## controllers/deniable_vault.py
Depends on: `models/deniable_vault.py`, `utils/security.py`
Imported by: `tests/test_deniable_vault.py`, `views/account.py`
- `canonical_json` (function) `controllers/deniable_vault.py:86` `def canonical_json(envelope)` -- Serialize an envelope deterministically for storage and sizing.
- `DeniableVaultConfig.from_mapping` (method) `controllers/deniable_vault.py:148` `def from_mapping(cls, mapping, env)` -- Build a config from a mapping, with environment overrides.
- `DeniableVaultConfig.read` (method) `controllers/deniable_vault.py:171` `def read(key)`
- `DeniableVaultConfig.expected_ct_b64_length` (method) `controllers/deniable_vault.py:213` `def expected_ct_b64_length(self)` -- Return the exact base64 length every slot ciphertext must have.
- `DeniableVaultConfig.random_container` (method) `controllers/deniable_vault.py:222` `def random_container(self)` -- Return a well-formed container filled with random, unopenable data.
- `DeniableVaultConfig.public_parameters` (method) `controllers/deniable_vault.py:250` `def public_parameters(self)` -- Return the parameters the browser needs to build a container.
- `EnvelopeValidator.__init__` (method) `controllers/deniable_vault.py:281` `def __init__(self, config)` -- Bind the validator to a configuration.
- `EnvelopeValidator.validate` (method) `controllers/deniable_vault.py:285` `def validate(self, envelope)` -- Validate ``envelope``, raising on the first violation.
- `DeniableVaultController.__init__` (method) `controllers/deniable_vault.py:401` `def __init__(self, db, config, validator)` -- Initialize the controller.
- `DeniableVaultController.load_or_provision` (method) `controllers/deniable_vault.py:419` `def load_or_provision(self, username)` -- Return ``username``'s container, minting a random one if absent.
- `DeniableVaultController.save` (method) `controllers/deniable_vault.py:441` `def save(self, username, envelope)` -- Validate and persist a container for ``username``.
- `DeniableVaultController.reset` (method) `controllers/deniable_vault.py:456` `def reset(self, username)` -- Overwrite ``username``'s container with a fresh random one.
- `DeniableVaultController.exists` (method) `controllers/deniable_vault.py:474` `def exists(self, username)` -- Return True if ``username`` already has a stored container.

## controllers/facade.py
Depends on: `utils/security.py`
Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`
- `FacadeConfig.gate_configured` (method) `controllers/facade.py:154` `def gate_configured(self)` -- Return whether the facade is enabled and holds a real gate hash.
- `FacadeConfig.cover_context` (method) `controllers/facade.py:158` `def cover_context(self)` -- Return the cosmetic cover context, never carrying a gate hash.
- `FacadeConfig.cover_variables` (method) `controllers/facade.py:166` `def cover_variables(self)` -- Return the sanitizable cover variable payload.
- `FacadeConfig.from_mapping` (method) `controllers/facade.py:181` `def from_mapping(cls, mapping, env)` -- Resolve configuration with environment, mapping, then default order.
- `FacadeConfig.read` (method) `controllers/facade.py:189` `def read(key)`
- `GatePhraseHasher.__init__` (method) `controllers/facade.py:265` `def __init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)` -- Bind the hasher to explicit Argon2id cost parameters.
- `GatePhraseHasher.hash` (method) `controllers/facade.py:282` `def hash(self, phrase)` -- Return a salted Argon2id digest of ``phrase``.
- `GatePhraseHasher.verify` (method) `controllers/facade.py:286` `def verify(self, phrase, encoded)` -- Return whether ``phrase`` matches ``encoded`` without raising.
- `GatePhraseHasher.from_config` (method) `controllers/facade.py:296` `def from_config(cls, config)` -- Build a hasher using the cost parameters of ``config``.
- `GateTicket.__init__` (method) `controllers/facade.py:308` `def __init__(self, secret_key, ttl_seconds)` -- Bind the ticket signer to the app secret and a lifetime.
- `GateTicket.issue` (method) `controllers/facade.py:316` `def issue(self, mode)` -- Return a signed ticket for ``mode`` or raise for an unknown mode.
- `GateTicket.verify` (method) `controllers/facade.py:322` `def verify(self, token)` -- Return the ticket mode, or ``None`` if expired, tampered, or absent.
- `FacadeGate.__init__` (method) `controllers/facade.py:339` `def __init__(self, config, hasher, ticket)` -- Bind the gate to its configuration and collaborators.
- `FacadeGate.build` (method) `controllers/facade.py:351` `def build(cls, config, secret_key)` -- Build a gate from configuration and the application secret.
- `FacadeGate.evaluate` (method) `controllers/facade.py:359` `def evaluate(self, phrase)` -- Classify a phrase and emit only a generic audit event.

## controllers/file.py
Depends on: `utils/padding.py`, `utils/utils.py`
Imported by: `app_factory.py`, `tests/test_padding.py`
- `safe_filename` (function) `controllers/file.py:33` `def safe_filename(name)` -- Return a filename safe to embed in an S3 key.
- `FileController.__init__` (method) `controllers/file.py:54` `def __init__(self, users_path, s3_bucket, s3_client)`
- `FileController.get_storage_usage` (method) `controllers/file.py:71` `def get_storage_usage(self, username)` -- Sum the bytes used by ``username``'s encrypted files in S3.
- `FileController.upload_encrypted_file` (method) `controllers/file.py:85` `def upload_encrypted_file(self, username, file_storage, wrapped_fek)` -- Persist an already-encrypted file and its wrapped FEK to S3.
- `FileController.get_encrypted_file_and_key` (method) `controllers/file.py:118` `def get_encrypted_file_and_key(self, username, filename)` -- Fetch a user's encrypted file and its wrapped FEK from S3.
- `FileController.list_encrypted_files` (method) `controllers/file.py:148` `def list_encrypted_files(self, username)` -- List the encrypted files that belong to ``username``.

## controllers/message.py
Depends on: `models/message.py`, `models/user.py`, `utils/padding.py`, `utils/utils.py`
Imported by: `tests/test_padding.py`, `views/message.py`
- `MessageController.__init__` (method) `controllers/message.py:22` `def __init__(self, users_path, users_db_path)` -- Initialize the controller.
- `MessageController.send_encrypted_message` (method) `controllers/message.py:36` `def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)` -- Persist an opaque message envelope for the recipient.
- `MessageController.get_messages` (method) `controllers/message.py:90` `def get_messages(self, username, page, per_page)` -- Return opaque message envelopes for the user.

## controllers/secure_channel.py
Imported by: `tests/test_secure_channel.py`, `views/admin.py`
- `ChannelMode.parse` (method) `controllers/secure_channel.py:74` `def parse(cls, raw)` -- Parse free-form input into a mode, defaulting to disabled.
- `ChannelMode.is_cloudflare_url` (method) `controllers/secure_channel.py:82` `def is_cloudflare_url(value)` -- Return whether value is a quick-tunnel HTTPS URL.
- `ChannelMode.is_onion_url` (method) `controllers/secure_channel.py:89` `def is_onion_url(value)` -- Return whether value is a v3 onion HTTP address.
- `SecureChannelConfig.configured` (method) `controllers/secure_channel.py:129` `def configured(self)` -- Return whether a disposible channel mode is selected.
- `SecureChannelConfig.from_mapping` (method) `controllers/secure_channel.py:134` `def from_mapping(cls, mapping, env)` -- Resolve configuration with environment, mapping, then default order.
- `SecureChannelConfig.read` (method) `controllers/secure_channel.py:142` `def read(key)`
- `ChannelStatus.active` (method) `controllers/secure_channel.py:184` `def active(self)` -- Return whether any backend address is currently published.
- `SecureChannelManager.__init__` (method) `controllers/secure_channel.py:223` `def __init__(self, state_dir, local_port, local_scheme, cloudflared_bin, tor_bin, start_timeout_seconds, launcher...` -- Bind the manager to a state directory and backend binaries.
- `SecureChannelManager.origin_url` (method) `controllers/secure_channel.py:247` `def origin_url(self)` -- Return the loopback origin URL both backends forward to.
- `SecureChannelManager.from_config` (method) `controllers/secure_channel.py:252` `def from_config(cls, config, launcher, killer)` -- Build a manager sharing binary paths and ports with config.
- `SecureChannelManager.status` (method) `controllers/secure_channel.py:270` `def status(self)` -- Return live status, pruning dead pids without side effects.
- `SecureChannelManager.start` (method) `controllers/secure_channel.py:281` `def start(self, mode)` -- Start backends for mode, replacing any running channel.
- `SecureChannelManager.stop` (method) `controllers/secure_channel.py:301` `def stop(self)` -- Terminate tracked backends and remove persisted state.
- `SecureChannelManager.rotate` (method) `controllers/secure_channel.py:314` `def rotate(self)` -- Dispose current addresses and start the same mode again.
- `SecureChannelManager.audit_details` (method) `controllers/secure_channel.py:321` `def audit_details(self, action, mode, cloud_url, onion_url)` -- Return an audit-safe detail string without full addresses.

## controllers/sync.py
Imported by: `app_factory.py`
- `SyncController.__init__` (method) `controllers/sync.py:8` `def __init__(self, users_path, s3_bucket, s3_client, file_controller)`
- `SyncController.get_storage_usage` (method) `controllers/sync.py:14` `def get_storage_usage(self, username)` -- Calcula el uso de almacenamiento del usuario en S3.

## enc_dec.go
- `deriveAESKey` (function) `enc_dec.go:20` `func deriveAESKey(`
- `encryptFile` (function) `enc_dec.go:24` `func encryptFile(`
- `decryptFile` (function) `enc_dec.go:45` `func decryptFile(`
- `main` (function) `enc_dec.go:69` `func main(`

## enc_dec.py
- `derive_aes_key` (function) `enc_dec.py:36` `def derive_aes_key(shared_secret)` -- Derive a 32-byte AES key from an ML-KEM shared secret.
- `encrypt_file_in_memory` (function) `enc_dec.py:49` `def encrypt_file_in_memory(data, aes_key)` -- Encrypt ``data`` in memory with AES-256-GCM and return nonce + ciphertext.
- `decrypt_file_in_memory` (function) `enc_dec.py:65` `def decrypt_file_in_memory(nonce, ciphertext, aes_key)` -- Decrypt ``ciphertext`` in memory with AES-256-GCM and return the plaintext.
- `main` (function) `enc_dec.py:103` `def main()` -- Run the offline admin CLI (encrypt or decrypt a single object).

## models/contact.py
Imported by: `controllers/contact.py`
- `ContactDB.__init__` (method) `models/contact.py:29` `def __init__(self, db_path)` -- Initialize the ContactDB with the database path.
- `ContactDB.create_contact` (method) `models/contact.py:52` `def create_contact(self, user_id, subject, message)` -- Create a new contact message.
- `ContactDB.get_user_contacts` (method) `models/contact.py:89` `def get_user_contacts(self, user_id)` -- Retrieve all contact messages for a user.
- `ContactDB.get_all_contacts` (method) `models/contact.py:139` `def get_all_contacts(self, page, per_page)` -- Retrieve all contact messages with pagination.

## models/deniable_vault.py
Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`
- `DeniableVaultDB.__init__` (method) `models/deniable_vault.py:33` `def __init__(self, db_path)` -- Initialize the store and ensure its table exists.
- `DeniableVaultDB.upsert` (method) `models/deniable_vault.py:57` `def upsert(self, username, envelope)` -- Insert or replace the container for ``username``.
- `DeniableVaultDB.get` (method) `models/deniable_vault.py:82` `def get(self, username)` -- Return the stored container for ``username``, or ``None``.
- `DeniableVaultDB.exists` (method) `models/deniable_vault.py:101` `def exists(self, username)` -- Return True if ``username`` has a stored container.

## models/message.py
Imported by: `controllers/message.py`, `utils/scheduler.py`
- `MessageDB.__init__` (method) `models/message.py:46` `def __init__(self, base_path)` -- Initialize the MessageDB with the base directory for per-user mailboxes.
- `MessageDB.save_message` (method) `models/message.py:55` `def save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipient, cek_for_sender, message_id)` -- Persist an opaque message envelope for the recipient.
- `MessageDB.get_messages` (method) `models/message.py:87` `def get_messages(self, recipient, page, per_page)` -- Return opaque message envelopes for the recipient.
- `MessageDB.delete_old_messages` (method) `models/message.py:172` `def delete_old_messages(self, recipient, days)` -- Delete messages older than ``days`` days from the recipient's mailbox.

## models/plans.py
Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`
- `PlanDB.__init__` (method) `models/plans.py:6` `def __init__(self, db_path)` -- Initialize the PlanDB with the database path.
- `PlanDB.get_plan` (method) `models/plans.py:37` `def get_plan(self, plan_name)` -- Retrieve a plan by name.
- `PlanDB.get_all_plans` (method) `models/plans.py:50` `def get_all_plans(self)` -- Retrieve all plans.
- `PlanDB.create_plan` (method) `models/plans.py:60` `def create_plan(self, name, storage_quota, trial_days, price)` -- Create a new plan.
- `PlanDB.update_plan` (method) `models/plans.py:78` `def update_plan(self, name, storage_quota, trial_days, price)` -- Update an existing plan.
- `PlanDB.delete_plan` (method) `models/plans.py:113` `def delete_plan(self, name)` -- Delete a plan by name.
- `PlanDB.validate_plan_payment` (method) `models/plans.py:139` `def validate_plan_payment(self, plan_name, amount_paid)` -- Validate that the paid amount matches the plan price.

## models/superadmin_audit.py
Imported by: `views/admin.py`
- `SuperadminAuditDB.__init__` (method) `models/superadmin_audit.py:35` `def __init__(self, db_path)` -- Initialize the audit log and ensure its table exists.
- `SuperadminAuditDB.record` (method) `models/superadmin_audit.py:75` `def record(self, actor, action, target_user, ip, details)` -- Append one audit row and return its id.
- `SuperadminAuditDB.recent` (method) `models/superadmin_audit.py:119` `def recent(self, limit)` -- Return the most recent ``limit`` audit rows, newest first.

## models/user.py
Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`
- `UserModel.get_id` (method) `models/user.py:52` `def get_id(self)` -- Return the user ID as a string (required by Flask-Login).
- `UserModel.is_active` (method) `models/user.py:70` `def is_active(self)` -- Return True while the user can use the application.
- `UserDB.__init__` (method) `models/user.py:85` `def __init__(self, db_path)` -- Initialize the UserDB with the database path.
- `UserDB.create_user` (method) `models/user.py:325` `def create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone...` -- Persist a new user from client-provided zero-knowledge credentials.
- `UserDB.update_user_phone_status` (method) `models/user.py:362` `def update_user_phone_status(self, username, phone_verified, phone_verification_code_hash, phone_code_expires)` -- Update phone verification status and related fields.
- `UserDB.update_user_mfa_status` (method) `models/user.py:396` `def update_user_mfa_status(self, username, mfa_code_hash, mfa_code_expires, mfa_enabled)` -- Update MFA code, expiration, and enabled status.
- `UserDB.update_user` (method) `models/user.py:430` `def update_user(self, username, email_verified, confirmation_token)` -- Update specific user fields.
- `UserDB.get_user` (method) `models/user.py:454` `def get_user(self, username)` -- Retrieve a user by username.
- `UserDB.get_user_by_id` (method) `models/user.py:468` `def get_user_by_id(self, user_id)` -- Retrieve a user by ID.
- `UserDB.get_user_by_email` (method) `models/user.py:482` `def get_user_by_email(self, email)` -- Retrieve a user by email address.
- `UserDB.get_user_by_phone` (method) `models/user.py:496` `def get_user_by_phone(self, phone)` -- Retrieve a user by phone number.
- `UserDB.get_user_by_confirmation_token` (method) `models/user.py:510` `def get_user_by_confirmation_token(self, token)` -- Retrieve a user by confirmation token.
- `UserDB.get_recovery_bundle` (method) `models/user.py:524` `def get_recovery_bundle(self, username)` -- Return the QV-RECOVERY-1 bundle for a username, if one exists.
- `UserDB.reset_credentials_with_recovery` (method) `models/user.py:548` `def reset_credentials_with_recovery(self, username, srp_salt, srp_verifier, kdf_salt, encrypted_private_key)` -- Replace a user's password-derived credentials after a verified recovery.
- `UserDB.update_role` (method) `models/user.py:579` `def update_role(self, username, role, storage_quota, subscription_status)` -- Update a user's role, storage quota, and subscription status.
- `UserDB.count_users` (method) `models/user.py:592` `def count_users(self)` -- Return the total number of users.
- `UserDB.get_all_users` (method) `models/user.py:603` `def get_all_users(self)` -- Retrieve all users.
- `UserDB.value` (method) `models/user.py:655` `def value(name, default)`
- `UserDB.fetch_one` (method) `models/user.py:694` `def fetch_one(self, query, params)` -- Execute a query and return the first result as a dictionary.

## scripts/doctor.py
- `DoctorReport.add` (method) `scripts/doctor.py:113` `def add(self, result)` -- Append one check result.
- `DoctorReport.failures` (method) `scripts/doctor.py:118` `def failures(self)` -- Return every failing check.
- `DoctorReport.exit_code` (method) `scripts/doctor.py:123` `def exit_code(self)` -- Return 0 when every check passes, 1 otherwise.
- `DoctorReport.load_env_file` (method) `scripts/doctor.py:128` `def load_env_file(path)` -- Parse a dotenv file into a dict without third-party imports.
- `DoctorReport.effective_env` (method) `scripts/doctor.py:147` `def effective_env()` -- Return process env overlaid with ``.env`` file values.
- `DoctorReport.check_python` (method) `scripts/doctor.py:154` `def check_python(minimum)` -- Verify the interpreter meets the minimum supported version.
- `DoctorReport.check_module` (method) `scripts/doctor.py:170` `def check_module(name)` -- Verify one Python module imports cleanly.
- `DoctorReport.check_binary` (method) `scripts/doctor.py:186` `def check_binary(name, env_override)` -- Verify one system binary resolves via PATH or an override path.
- `DoctorReport.check_env_file` (method) `scripts/doctor.py:210` `def check_env_file()` -- Verify the operator ``.env`` file exists.
- `DoctorReport.parse_host_port` (method) `scripts/doctor.py:223` `def parse_host_port(uri, default_port)` -- Extract a TCP host and port from a Redis or HTTP(S) URL.
- `DoctorReport.check_tcp` (method) `scripts/doctor.py:242` `def check_tcp(name, host, port, timeout)` -- Verify a TCP endpoint accepts connections.
- `DoctorReport.debian_arch` (method) `scripts/doctor.py:261` `def debian_arch(deb)` -- Map the host CPU to a Cloudflare or Garage release architecture.
- `DoctorReport.cloudflared_deb_url` (method) `scripts/doctor.py:270` `def cloudflared_deb_url(version, arch)` -- Build the official cloudflared .deb URL for a version and arch.
- `DoctorReport.garage_bin_url` (method) `scripts/doctor.py:283` `def garage_bin_url(version, target)` -- Build the official garage binary URL for a version and target.
- `DoctorReport.apt_command` (method) `scripts/doctor.py:288` `def apt_command(packages)` -- Build an apt install command, prefixed with sudo outside root.
- `DoctorReport.run_command` (method) `scripts/doctor.py:298` `def run_command(cmd)` -- Run one shell command and capture its outcome.
- `DoctorReport.download_file` (method) `scripts/doctor.py:319` `def download_file(url, destination)` -- Fetch a URL with curl when present, else urllib.
- `DoctorReport.upsert_env` (method) `scripts/doctor.py:334` `def upsert_env(key, value, path)` -- Set one KEY=value pair in ``.env``, preserving other lines.
- `DoctorReport.fix_python_deps` (method) `scripts/doctor.py:352` `def fix_python_deps()` -- Install project requirements with the running interpreter.
- `DoctorReport.fix_apt` (method) `scripts/doctor.py:360` `def fix_apt(packages)` -- Install Debian system packages, using sudo outside root.
- `DoctorReport.fix_cloudflared` (method) `scripts/doctor.py:373` `def fix_cloudflared(version, bin_dir)` -- Install the cloudflared binary into a user-writable bin directory.
- `DoctorReport.fix_garage` (method) `scripts/doctor.py:417` `def fix_garage(version, destination)` -- Download the garage binary and verify it against its checksum.
- `DoctorReport.collect_report` (method) `scripts/doctor.py:449` `def collect_report()` -- Run every check and return the aggregated report.
- `DoctorReport.print_report` (method) `scripts/doctor.py:476` `def print_report(report)` -- Render the report in plain English for operators.
- `DoctorReport.apply_fixes` (method) `scripts/doctor.py:493` `def apply_fixes(report)` -- Install every missing piece that has an unattended installer.
- `DoctorReport.main` (method) `scripts/doctor.py:530` `def main(argv)` -- Entry point for ``make doctor`` and ``make doctor-fix``.

## scripts/email_tool.py
Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`
- `cmd_test_smtp` (function) `scripts/email_tool.py:63` `def cmd_test_smtp(args)` -- Send a test email through the configured SMTP server.
- `cmd_link` (function) `scripts/email_tool.py:91` `def cmd_link(args)` -- Print the confirmation URL for a user without sending email.
- `cmd_confirm` (function) `scripts/email_tool.py:114` `def cmd_confirm(args)` -- Mark a user's email as verified directly in the database.
- `build_parser` (function) `scripts/email_tool.py:133` `def build_parser()` -- Construct the argument parser for the three subcommands.
- `main` (function) `scripts/email_tool.py:153` `def main()` -- Parse arguments and dispatch to the selected subcommand.

## scripts/garage-init.sh
- `upsert_env` (function) `scripts/garage-init.sh:35` -- Insert or update a KEY=value line in .env without disturbing other lines.

## scripts/garage-native.sh
- `upsert_env` (function) `scripts/garage-native.sh:46` -- Insert or update a KEY=value line in .env without disturbing other lines.
- `s3_reachable` (function) `scripts/garage-native.sh:56`
- `gcmd` (function) `scripts/garage-native.sh:141`

## scripts/makeadmin.py
Depends on: `models/user.py`
- `cmd_promote` (function) `scripts/makeadmin.py:75` `def cmd_promote(args)` -- Promote ``args.username`` to the requested role (default: superadmin).
- `build_parser` (function) `scripts/makeadmin.py:126` `def build_parser()` -- Construct the argument parser for the makeadmin subcommands.
- `main` (function) `scripts/makeadmin.py:152` `def main()` -- Parse arguments and dispatch to the selected subcommand.

## server.go
- `main` (function) `server.go:11` `func main(`
- `handleConnection` (function) `server.go:40` `func handleConnection(`

## static/js/account.js
Depends on: `static/js/qv-deniable.js`
- `setStatus` (function) `static/js/account.js:19`
- `csrfToken` (function) `static/js/account.js:30`
- `apiRequest` (function) `static/js/account.js:36`
- `loadState` (function) `static/js/account.js:54`
- `collectSlots` (function) `static/js/account.js:59`
- `handleConfigure` (function) `static/js/account.js:73`
- `handleOpen` (function) `static/js/account.js:103`
- `handleReset` (function) `static/js/account.js:125`
- `init` (function) `static/js/account.js:138`

## static/js/coded-text.js
- `randomChar` (function) `static/js/coded-text.js:12`
- `animateElement` (function) `static/js/coded-text.js:18`
- `init` (function) `static/js/coded-text.js:49`

## static/js/login.js
Depends on: `static/js/qv-crypto.js`
Imported by: `static/js/qv-crypto.js`
- `handleLogin` (function) `static/js/login.js:11`
- `init` (function) `static/js/login.js:43`

## static/js/messages.js
Depends on: `static/js/qv-crypto.js`
- `getCsrfToken` (function) `static/js/messages.js:11`
- `handleSend` (function) `static/js/messages.js:17`
- `collectEnvelopes` (function) `static/js/messages.js:43`
- `handleDecryptInbox` (function) `static/js/messages.js:60`
- `initEditor` (function) `static/js/messages.js:87`
- `init` (function) `static/js/messages.js:108`

## static/js/qv-crypto.js
Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`
- `concatBytes` (function) `static/js/qv-crypto.js:58` -- -- Encoding helpers ---
- `hexToBytes` (function) `static/js/qv-crypto.js:69`
- `bytesToHex` (function) `static/js/qv-crypto.js:78`
- `bytesToBase64` (function) `static/js/qv-crypto.js:84`
- `bytesToBase32` (function) `static/js/qv-crypto.js:95`
- `base64ToBytes` (function) `static/js/qv-crypto.js:113`
- `bytesToBigInt` (function) `static/js/qv-crypto.js:120`
- `i2osp` (function) `static/js/qv-crypto.js:127`
- `mod` (function) `static/js/qv-crypto.js:137`
- `modPow` (function) `static/js/qv-crypto.js:141`
- `randomBytes` (function) `static/js/qv-crypto.js:159`
- `H` (function) `static/js/qv-crypto.js:168`
- `Hint` (function) `static/js/qv-crypto.js:172`
- `deriveKeyFromPassphrase` (function) `static/js/qv-crypto.js:184` -- Derive a 256-bit key from a passphrase with a caller-chosen PBKDF2 iteration count.
- `deriveMasterKey` (function) `static/js/qv-crypto.js:205`
- `aesGcmEncrypt` (function) `static/js/qv-crypto.js:209`
- `aesGcmDecrypt` (function) `static/js/qv-crypto.js:220`
- `computeK` (function) `static/js/qv-crypto.js:250` -- -- SRP-6a (QV-SRP-1), mirrors utils/srp6a.py ---
- `deriveVerifier` (function) `static/js/qv-crypto.js:255`
- `srpLogin` (function) `static/js/qv-crypto.js:263` -- Run a full SRP-6a login against the server, verifying the server proof M2.
- `generateIdentity` (function) `static/js/qv-crypto.js:315`
- `parsePublicKey` (function) `static/js/qv-crypto.js:343`
- `parsePrivateBlob` (function) `static/js/qv-crypto.js:351`
- `deriveWrapKey` (function) `static/js/qv-crypto.js:359`
- `wrapKey` (function) `static/js/qv-crypto.js:371` -- Seal a file encryption key to a recipient's hybrid public key.
- `unwrapKey` (function) `static/js/qv-crypto.js:395` -- Recover a file encryption key using the recipient's hybrid private blob.
- `generateRecoveryCode` (function) `static/js/qv-crypto.js:417` -- Generate a QV-RECOVERY-1 code: 20 random bytes (160 bits) Base32-encoded (RFC 4648, no padding) and grouped as...
- `normalizeRecoveryCode` (function) `static/js/qv-crypto.js:428` -- Normalize a user-entered recovery code: strip surrounding whitespace, remove group separators, and uppercase, so...
- `wrapPrivateKeyForRecovery` (function) `static/js/qv-crypto.js:436` -- Re-wrap an existing privateBlob under a key derived from a recovery code, using the same PBKDF2-SHA256 + AES-256-GCM...
- `derivePublicKeyFromPrivateBlob` (function) `static/js/qv-crypto.js:455` -- Reconstruct the public key (the same {v, mlkem, x} structure produced by generateIdentity) from a decrypted privateBlob.
- `postJson` (function) `static/js/qv-crypto.js:473`
- `buildRegistration` (function) `static/js/qv-crypto.js:496` -- Build the zero-knowledge registration payload entirely in the browser.
- `register` (function) `static/js/qv-crypto.js:530`
- `recoverAccount` (function) `static/js/qv-crypto.js:541` -- Reset SRP credentials and the password-encrypted private key using a QV-RECOVERY-1 recovery code, without ever...
- `login` (function) `static/js/qv-crypto.js:592`
- `encryptAndUpload` (function) `static/js/qv-crypto.js:599` -- Generate a fresh file key, encrypt the padded file, wrap the key, and upload.
- `downloadAndDecrypt` (function) `static/js/qv-crypto.js:629` -- Download an encrypted file and its key, then decrypt it in the browser.
- `fetchPublicKey` (function) `static/js/qv-crypto.js:668` -- Fetch a user's hybrid public key so the browser can wrap content to them.
- `sendSecureMessage` (function) `static/js/qv-crypto.js:683` -- Encrypt a message to a recipient (keeping a sender-readable outbox copy) and POST the opaque envelope.
- `decryptInbox` (function) `static/js/qv-crypto.js:714` -- Decrypt a batch of inbox envelopes with the user's password.

## static/js/qv-deniable.js
Depends on: `static/js/qv-crypto.js`
Imported by: `static/js/account.js`
- `toBytes` (function) `static/js/qv-deniable.js:47`
- `frame` (function) `static/js/qv-deniable.js:55` -- Frame a payload as [len(4) | payload | random padding] of exactly `paddedLength` bytes.
- `unframe` (function) `static/js/qv-deniable.js:64`
- `sealSlot` (function) `static/js/qv-deniable.js:82` -- Encrypt one slot's framed plaintext under a passphrase, returning the {salt, nonce, ct} object the envelope stores.
- `openSlot` (function) `static/js/qv-deniable.js:102` -- Attempt to open one slot with a passphrase.
- `buildDeniableVault` (function) `static/js/qv-deniable.js:125` -- Build a deniable container from a list of slot specifications.
- `openDeniableVault` (function) `static/js/qv-deniable.js:170` -- Open a container with a passphrase.

## static/js/qv-padding.js
Depends on: `utils/padding.py`
Imported by: `static/js/qv-crypto.js`
- `tableFor` (function) `static/js/qv-padding.js:15`
- `bucketFor` (function) `static/js/qv-padding.js:20`
- `randomPad` (function) `static/js/qv-padding.js:33`
- `padFramed` (function) `static/js/qv-padding.js:42`
- `unframeFramed` (function) `static/js/qv-padding.js:54`

## static/js/recover.js
Depends on: `static/js/qv-crypto.js`
- `setStatus` (function) `static/js/recover.js:14`
- `handleRecover` (function) `static/js/recover.js:22`
- `init` (function) `static/js/recover.js:79`

## static/js/register.js
Depends on: `static/js/qv-crypto.js`
Imported by: `static/js/qv-crypto.js`
- `showRecoveryCode` (function) `static/js/register.js:16` -- Display the one-time QV-RECOVERY-1 code in a modal and wait for the user to acknowledge they have saved it before...
- `handleRegister` (function) `static/js/register.js:42`
- `init` (function) `static/js/register.js:109`

## static/js/upload.js
Depends on: `static/js/qv-crypto.js`
- `getCsrfToken` (function) `static/js/upload.js:11`
- `getUsername` (function) `static/js/upload.js:16`
- `getPublicKey` (function) `static/js/upload.js:23`
- `handleUpload` (function) `static/js/upload.js:40`
- `handleDownload` (function) `static/js/upload.js:74`
- `init` (function) `static/js/upload.js:96`

## templates/terms.py
- `terms` (function) `templates/terms.py:6` `def terms()` -- Render the About page.

## tools/generate_sri.py
Depends on: `utils/integrity.py`
- `collect_local_assets` (function) `tools/generate_sri.py:41` `def collect_local_assets()` -- Hash every first-party script and stylesheet under ``static/``.
- `fetch_cdn_assets` (function) `tools/generate_sri.py:56` `def fetch_cdn_assets()` -- Download every pinned CDN URL and hash its exact bytes.
- `build_manifest` (function) `tools/generate_sri.py:66` `def build_manifest(cdn, local)` -- Assemble the deterministic manifest document.
- `render_manifest` (function) `tools/generate_sri.py:76` `def render_manifest(manifest)` -- Render the manifest deterministically with a trailing newline.
- `main` (function) `tools/generate_sri.py:81` `def main(argv)` -- Generate the manifest, or verify it is current with ``--check``.

## tools/verify_build.py
Depends on: `utils/integrity.py`, `utils/padding.py`
Imported by: `tests/test_integrity.py`
- `AssetReference.__init__` (method) `tools/verify_build.py:37` `def __init__(self)` -- Initialize the reference collector.
- `AssetReference.handle_starttag` (method) `tools/verify_build.py:42` `def handle_starttag(self, tag, attrs)` -- Record one script or link tag with its integrity attribute.
- `AssetReference.load_manifest` (method) `tools/verify_build.py:71` `def load_manifest()` -- Load and return the SRI manifest document.
- `AssetReference.expected_for_reference` (method) `tools/verify_build.py:76` `def expected_for_reference(manifest, ref)` -- Resolve the pinned integrity value for one template reference.
- `AssetReference.integrity_attribute_ok` (method) `tools/verify_build.py:85` `def integrity_attribute_ok(integrity, ref, expected)` -- Accept a literal pin or the ``sri_integrity`` template expression.
- `AssetReference.check_local_hashes` (method) `tools/verify_build.py:95` `def check_local_hashes(manifest, failures)` -- Recompute every pinned local asset and record mismatches.
- `AssetReference.check_template_references` (method) `tools/verify_build.py:110` `def check_template_references(manifest, failures)` -- Require manifest-backed integrity on every template reference.
- `AssetReference.check_bucket_parity` (method) `tools/verify_build.py:126` `def check_bucket_parity(failures)` -- Require identical bucket tables in Python and JavaScript.
- `AssetReference.main` (method) `tools/verify_build.py:141` `def main()` -- Run every check and report failures.

## utils/cache.py
- `Cache.__init__` (method) `utils/cache.py:8` `def __init__(self)`
- `Cache.get` (method) `utils/cache.py:11` `def get(self, key)` -- Retrieve a value from the cache.
- `Cache.set` (method) `utils/cache.py:16` `def set(self, key, value, ttl)` -- Store a value in the cache with an optional TTL (seconds).
- `Cache.delete` (method) `utils/cache.py:20` `def delete(self, key)` -- Delete a key from the cache.

## utils/integrity.py
Imported by: `app_factory.py`, `tests/test_integrity.py`, `tools/generate_sri.py`, `tools/verify_build.py`
- `manifest_path` (function) `utils/integrity.py:25` `def manifest_path()` -- Return the manifest path resolved from this file, never hardcoded.
- `compute_sri` (function) `utils/integrity.py:30` `def compute_sri(data, algorithm)` -- Return the SRI string ``<algorithm>-<base64 digest>`` for ``data``.
- `compute_file_sri` (function) `utils/integrity.py:36` `def compute_file_sri(path, algorithm)` -- Return the SRI string for the bytes stored at ``path``.
- `load_manifest` (function) `utils/integrity.py:47` `def load_manifest()` -- Return the parsed SRI manifest, or an empty mapping when absent.
- `integrity_for` (function) `utils/integrity.py:55` `def integrity_for(key)` -- Return the pinned integrity string for one manifest key.
- `clear_manifest_cache` (function) `utils/integrity.py:72` `def clear_manifest_cache()` -- Drop the cached manifest text so tests see a regenerated file.
- `template_integrity` (function) `utils/integrity.py:77` `def template_integrity(key)` -- Return the integrity string for a template asset reference.

## utils/mailer.py
Imported by: `controllers/auth.py`, `scripts/email_tool.py`, `utils/scheduler.py`, `views/auth.py`
- `external_url` (function) `utils/mailer.py:22` `def external_url(path)` -- Build an absolute URL for a root-relative path using the public host.
- `mail_is_configured` (function) `utils/mailer.py:38` `def mail_is_configured()` -- Return True when SMTP credentials are present so a send can succeed.
- `send_transactional_email` (function) `utils/mailer.py:51` `def send_transactional_email(subject, recipients, body)` -- Send a plain-text transactional email through the configured server.

## utils/padding.py
Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`
- `PaddingConfig.buckets_for` (method) `utils/padding.py:84` `def buckets_for(self, kind)` -- Return the bucket table for ``kind``.
- `PaddingConfig.max_plaintext_bytes` (method) `utils/padding.py:90` `def max_plaintext_bytes(self, kind)` -- Return the largest plaintext that fits ``kind``.
- `PaddingConfig.config_from_env` (method) `utils/padding.py:109` `def config_from_env()` -- Build a :class:`PaddingConfig` from the environment.
- `PaddingConfig.cached_tables` (method) `utils/padding.py:142` `def cached_tables(config)` -- Return the process-wide cached bucket tables for ``config``.
- `PaddingConfig.bucket_for` (method) `utils/padding.py:149` `def bucket_for(plaintext_len, kind, config)` -- Return the smallest bucket holding ``plaintext_len`` plus prefix.
- `PaddingConfig.pad` (method) `utils/padding.py:169` `def pad(plaintext, kind, config)` -- Pad ``plaintext`` to its bucket with fresh CSPRNG bytes.
- `PaddingConfig.unpad` (method) `utils/padding.py:183` `def unpad(padded, kind, config)` -- Remove bucket framing and return the original plaintext.
- `PaddingConfig.wire_ciphertext_len` (method) `utils/padding.py:209` `def wire_ciphertext_len(bucket)` -- Return the AES-256-GCM ciphertext length for one padded bucket.
- `PaddingConfig.is_allowed_ciphertext_len` (method) `utils/padding.py:214` `def is_allowed_ciphertext_len(ciphertext_len, kind, config)` -- Return True when ``ciphertext_len`` matches a bucket plus GCM overhead.

## utils/plans.py
- `SubscriptionPlans.get_plan` (method) `utils/plans.py:30` `def get_plan(plan_name)` -- Obtiene los detalles de un plan.
- `SubscriptionPlans.validate_plan_payment` (method) `utils/plans.py:42` `def validate_plan_payment(plan_name, amount_paid)` -- Valida que el monto pagado coincide con el plan.

## utils/scheduler.py
Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`
- `init_scheduler` (function) `utils/scheduler.py:37` `def init_scheduler(app, mail)` -- Start the background scheduler with the production job schedule.
- `check_trial_expiration` (function) `utils/scheduler.py:72` `def check_trial_expiration()`
- `cleanup_old_messages` (function) `utils/scheduler.py:118` `def cleanup_old_messages()`

## utils/security.py
Depends on: `utils/utils.py`
Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`
- `audit_event` (function) `utils/security.py:86` `def audit_event(event)` -- Emit a structured audit record.
- `constant_time_compare` (function) `utils/security.py:123` `def constant_time_compare(a, b)` -- Return True if the two strings match in constant time.
- `hash_secret` (function) `utils/security.py:135` `def hash_secret(secret)` -- Hash a short-lived secret (phone code, MFA, recovery code) for storage.
- `verify_secret` (function) `utils/security.py:156` `def verify_secret(secret, expected_hash)` -- Verify a short-lived secret against its stored hash.
- `new_one_time_code` (function) `utils/security.py:163` `def new_one_time_code(length)` -- Return a cryptographically random numeric verification code.
- `json_csrf_protect` (function) `utils/security.py:193` `def json_csrf_protect(view)` -- Decorator: require a valid CSRF token on JSON state-changing requests.
- `wrapper` (function) `utils/security.py:207` `def wrapper()`

## utils/srp6a.py
- `i2osp` (function) `utils/srp6a.py:47` `def i2osp(value)` -- Encode an integer as a big-endian byte string padded to the length of N.
- `compute_k` (function) `utils/srp6a.py:73` `def compute_k()` -- Compute the SRP-6a multiplier parameter ``k = H(N | PAD(g))``.
- `compute_u` (function) `utils/srp6a.py:78` `def compute_u(server_a, server_b)` -- Compute the random scrambling parameter ``u = H(PAD(A) | PAD(B))``.
- `generate_server_challenge` (function) `utils/srp6a.py:91` `def generate_server_challenge(verifier)` -- Generate the server ephemeral key pair (b, B) for a login challenge.
- `compute_proofs` (function) `utils/srp6a.py:107` `def compute_proofs(username, salt_hex, verifier, server_a, server_b, server_b_secret)` -- Compute the expected client proof M1 and the server proof M2.
- `SRPSessionStore.__init__` (method) `utils/srp6a.py:158` `def __init__(self, storage_uri)` -- Initialize the store from a Redis connection URI.
- `SRPSessionStore.save` (method) `utils/srp6a.py:172` `def save(self, username, salt_hex, verifier_hex, server_a_hex, server_b_hex, server_b_secret_hex)` -- Persist the ephemeral SRP challenge state for a username.
- `SRPSessionStore.load` (method) `utils/srp6a.py:202` `def load(self, username)` -- Load and consume the ephemeral SRP state for a username.
- `SRPSessionStore.hello` (method) `utils/srp6a.py:224` `def hello(store, username, client_a_hex, salt_hex, verifier_hex)` -- Process the SRP ``hello`` step and return the server challenge B.
- `SRPSessionStore.verify` (method) `utils/srp6a.py:260` `def verify(store, username, client_m1_hex)` -- Process the SRP ``verify`` step and return the server proof M2.

## utils/utils.py
Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/file.py`, `controllers/message.py`, `scripts/email_tool.py`, `tests/test_utils.py`, `utils/security.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/subscription.py`, `views/sync.py`, `views/views.py`
- `database_path` (function) `utils/utils.py:12` `def database_path()` -- Return the SQLite database path from config, with a legacy fallback.
- `as_bool` (function) `utils/utils.py:29` `def as_bool(value, default)` -- Coerce an environment or payload value into a real boolean.
- `sanitize_path` (function) `utils/utils.py:49` `def sanitize_path(path)` -- Sanitiza una ruta de archivo para prevenir LFI y path traversal. - Elimina caracteres peligrosos - Normaliza la ruta...
- `Config.__init__` (method) `utils/utils.py:145` `def __init__(self, config_dict)`
- `Config.load_payload` (method) `utils/utils.py:168` `def load_payload()` -- Load non-secret application configuration from ``payload.json``.

## views/about.py
Imported by: `app_factory.py`
- `about` (function) `views/about.py:6` `def about()` -- Render the About page.

## views/account.py
Depends on: `controllers/deniable_vault.py`, `controllers/facade.py`, `models/deniable_vault.py`, `utils/security.py`
Imported by: `app_factory.py`
- `get_deniable_vault_controller` (function) `views/account.py:51` `def get_deniable_vault_controller()` -- Build a controller bound to the active app's database and config.
- `settings` (function) `views/account.py:65` `def settings()` -- Render the account settings page.
- `get_vault` (function) `views/account.py:85` `def get_vault()` -- Return the user's container and the build parameters.
- `put_vault` (function) `views/account.py:107` `def put_vault()` -- Validate and store a container for the user.
- `delete_vault` (function) `views/account.py:130` `def delete_vault()` -- Reset the user's container to a fresh random one.

## views/admin.py
Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`
- `PlanForm.admin` (method) `views/admin.py:186` `def admin()` -- Plan catalog read view.
- `PlanForm.superadmin_edit_user` (method) `views/admin.py:208` `def superadmin_edit_user(username)` -- Full profile edit for a single user.
- `PlanForm.manage_plans` (method) `views/admin.py:313` `def manage_plans()` -- Handle plan management.
- `PlanForm.edit_plan` (method) `views/admin.py:337` `def edit_plan(plan_name)` -- Handle editing of plan details.
- `PlanForm.superadmin` (method) `views/admin.py:373` `def superadmin()` -- Superadmin identity-recovery and inventory panel.
- `PlanForm.superadmin_reset_mfa` (method) `views/admin.py:476` `def superadmin_reset_mfa(username)` -- Disable MFA and clear the pending code for ``username``.
- `PlanForm.superadmin_resend_confirmation` (method) `views/admin.py:523` `def superadmin_resend_confirmation(username)` -- Issue a fresh ``confirmation_token`` for ``username``.
- `PlanForm.superadmin_toggle_suspend` (method) `views/admin.py:570` `def superadmin_toggle_suspend(username)` -- Flip ``subscription_status`` between active and inactive.
- `PlanForm.superadmin_channel_start` (method) `views/admin.py:620` `def superadmin_channel_start()` -- Start a disposable secure channel in the requested mode.
- `PlanForm.superadmin_channel_stop` (method) `views/admin.py:659` `def superadmin_channel_stop()` -- Dispose the running channel and remove its addresses.
- `PlanForm.superadmin_channel_rotate` (method) `views/admin.py:682` `def superadmin_channel_rotate()` -- Dispose current addresses and publish fresh ones in the same mode.
- `PlanForm.admin_contacts` (method) `views/admin.py:705` `def admin_contacts()`


Next: [API_p2.md](API_p2.md)
