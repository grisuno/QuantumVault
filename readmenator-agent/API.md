# API

## app.py

### main `def main()`
- Defined: `app.py:21`
- Depends on: `app_factory.py`, `utils/utils.py`
- Imported by: `scripts/test_bloque1.py`

### _is_production_like `def _is_production_like()`
- Defined: `app.py:58`
- Doc: Return True if the runtime looks like a public-facing deployment.
- Depends on: `app_factory.py`, `utils/utils.py`
- Imported by: `scripts/test_bloque1.py`

## app_factory.py

### _is_production `def _is_production()`
- Defined: `app_factory.py:70`
- Doc: Return True unless the operator explicitly opts into dev mode.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `wsgi.py`

### _build_csp `def _build_csp()`
- Defined: `app_factory.py:81`
- Doc: Return the strict Content-Security-Policy used in production.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `wsgi.py`

### _build_talisman_kwargs `def _build_talisman_kwargs()`
- Defined: `app_factory.py:112`
- Doc: Return kwargs to pass to ``Talisman`` based on the runtime env.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `wsgi.py`

### _configure_secret_key `def _configure_secret_key(app, config)`
- Defined: `app_factory.py:153`
- Doc: Set ``app.config['SECRET_KEY']`` from env, payload.json, or a random value.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `wsgi.py`

### _configure_session `def _configure_session(app)`
- Defined: `app_factory.py:196`
- Doc: Apply session lifetime and cookie hardening.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `wsgi.py`

### _configure_logging `def _configure_logging(app)`
- Defined: `app_factory.py:213`
- Doc: Wire up a structured application logger.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `wsgi.py`

### create_app `def create_app(config_overrides, security_overrides)`
- Defined: `app_factory.py:230`
- Doc: Build and return a fully-configured Flask application.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `wsgi.py`

### load_user `def load_user(user_id)`
- Defined: `app_factory.py:408`
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `wsgi.py`

## client.go

### main `func main(`
- Defined: `client.go:13`

## controllers/auth.py

### _now_utc `def _now_utc()`
- Defined: `controllers/auth.py:48`
- Doc: Return the current time as a timezone-aware UTC datetime.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### __init__ `def __init__(self, db_path, mail, storage_uri)`
- Defined: `controllers/auth.py:60`
- Doc: Initialize the controller.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### register `def register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, recovery_salt, encrypted_private_key_recovery)`
- Defined: `controllers/auth.py:75`
- Doc: Register a user from client-generated zero-knowledge credentials.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### send_confirmation_email `def send_confirmation_email(self, email, username, token)`
- Defined: `controllers/auth.py:155`
- Doc: Email the account-confirmation link to a freshly registered user.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### srp_hello `def srp_hello(self, username, client_a_hex)`
- Defined: `controllers/auth.py:201`
- Doc: Begin an SRP-6a login and return the salt and server challenge B.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### srp_verify `def srp_verify(self, username, client_m1_hex)`
- Defined: `controllers/auth.py:220`
- Doc: Complete an SRP-6a login and return the authenticated user and proof.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### send_sms_verification `def send_sms_verification(self, phone, code, username)`
- Defined: `controllers/auth.py:252`
- Doc: Send a verification code via SMS.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### verify_phone_code `def verify_phone_code(self, username, code)`
- Defined: `controllers/auth.py:273`
- Doc: Verify a phone verification code for a user.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### resend_phone_code `def resend_phone_code(self, username)`
- Defined: `controllers/auth.py:309`
- Doc: Issue and send a fresh phone verification code.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### _is_code_valid `def _is_code_valid(self, expires_at)`
- Defined: `controllers/auth.py:348`
- Doc: Return True if a verification code has not yet expired.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### verify_mfa_code `def verify_mfa_code(self, username, code)`
- Defined: `controllers/auth.py:368`
- Doc: Verify a multi-factor authentication code for a user.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### send_mfa_code `def send_mfa_code(self, username)`
- Defined: `controllers/auth.py:392`
- Doc: Generate, store, and send an MFA code to the user's phone.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### toggle_mfa `def toggle_mfa(self, username, enable)`
- Defined: `controllers/auth.py:415`
- Doc: Enable or disable MFA for a user.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

## controllers/contact.py

### __init__ `def __init__(self, db_path)`
- Defined: `controllers/contact.py:6`
- Doc: Initialize the ContactController with the database path.
- Depends on: `models/contact.py`
- Imported by: `views/admin.py`, `views/auth.py`

### create_contact `def create_contact(self, user_id, subject, message)`
- Defined: `controllers/contact.py:14`
- Doc: Create a new contact message.
- Depends on: `models/contact.py`
- Imported by: `views/admin.py`, `views/auth.py`

### get_user_contacts `def get_user_contacts(self, user_id)`
- Defined: `controllers/contact.py:36`
- Doc: Retrieve all contact messages for a user.
- Depends on: `models/contact.py`
- Imported by: `views/admin.py`, `views/auth.py`

## controllers/deniable_vault.py

### _base64_length `def _base64_length(byte_length)`
- Defined: `controllers/deniable_vault.py:81`
- Doc: Return the length of the standard base64 encoding of ``byte_length`` bytes.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### canonical_json `def canonical_json(envelope)`
- Defined: `controllers/deniable_vault.py:86`
- Doc: Serialize an envelope deterministically for storage and sizing.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### _coerce_int `def _coerce_int(value, default)`
- Defined: `controllers/deniable_vault.py:108`
- Doc: Return ``value`` coerced to int, falling back to ``default``.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### _coerce_kdf `def _coerce_kdf(value, default)`
- Defined: `controllers/deniable_vault.py:118`
- Doc: Return an allow-list of KDF identifiers from a value.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### from_mapping `def from_mapping(cls, mapping, env)`
- Defined: `controllers/deniable_vault.py:148`
- Doc: Build a config from a mapping, with environment overrides.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### expected_ct_b64_length `def expected_ct_b64_length(self)`
- Defined: `controllers/deniable_vault.py:213`
- Doc: Return the exact base64 length every slot ciphertext must have.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### random_container `def random_container(self)`
- Defined: `controllers/deniable_vault.py:222`
- Doc: Return a well-formed container filled with random, unopenable data.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### public_parameters `def public_parameters(self)`
- Defined: `controllers/deniable_vault.py:250`
- Doc: Return the parameters the browser needs to build a container.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### __init__ `def __init__(self, config)`
- Defined: `controllers/deniable_vault.py:281`
- Doc: Bind the validator to a configuration.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### validate `def validate(self, envelope)`
- Defined: `controllers/deniable_vault.py:285`
- Doc: Validate ``envelope``, raising on the first violation.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### _validate_slot `def _validate_slot(self, index, slot)`
- Defined: `controllers/deniable_vault.py:339`
- Doc: Validate a single slot.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### _validate_hex `def _validate_hex(value, expected_length, index, field)`
- Defined: `controllers/deniable_vault.py:376`
- Doc: Validate that ``value`` is hex of exactly ``expected_length``.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### __init__ `def __init__(self, db, config, validator)`
- Defined: `controllers/deniable_vault.py:401`
- Doc: Initialize the controller.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### load_or_provision `def load_or_provision(self, username)`
- Defined: `controllers/deniable_vault.py:419`
- Doc: Return ``username``'s container, minting a random one if absent.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### save `def save(self, username, envelope)`
- Defined: `controllers/deniable_vault.py:441`
- Doc: Validate and persist a container for ``username``.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### reset `def reset(self, username)`
- Defined: `controllers/deniable_vault.py:456`
- Doc: Overwrite ``username``'s container with a fresh random one.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### exists `def exists(self, username)`
- Defined: `controllers/deniable_vault.py:474`
- Doc: Return True if ``username`` already has a stored container.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### read `def read(key)`
- Defined: `controllers/deniable_vault.py:171`
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

## controllers/file.py

### _log_s3_error `def _log_s3_error(operation, error)`
- Defined: `controllers/file.py:26`
- Doc: Log a failed S3 operation without raising further.
- Depends on: `utils/utils.py`
- Imported by: `app_factory.py`

### safe_filename `def safe_filename(name)`
- Defined: `controllers/file.py:31`
- Doc: Return a filename safe to embed in an S3 key.
- Depends on: `utils/utils.py`
- Imported by: `app_factory.py`

### __init__ `def __init__(self, users_path, s3_bucket, s3_client)`
- Defined: `controllers/file.py:52`
- Depends on: `utils/utils.py`
- Imported by: `app_factory.py`

### _key `def _key(self, username, filename, suffix)`
- Defined: `controllers/file.py:57`
- Doc: Build the S3 key for a user's encrypted file or FEK.
- Depends on: `utils/utils.py`
- Imported by: `app_factory.py`

### get_storage_usage `def get_storage_usage(self, username)`
- Defined: `controllers/file.py:69`
- Doc: Sum the bytes used by ``username``'s encrypted files in S3.
- Depends on: `utils/utils.py`
- Imported by: `app_factory.py`

### upload_encrypted_file `def upload_encrypted_file(self, username, file_storage, wrapped_fek)`
- Defined: `controllers/file.py:83`
- Doc: Persist an already-encrypted file and its wrapped FEK to S3.
- Depends on: `utils/utils.py`
- Imported by: `app_factory.py`

### get_encrypted_file_and_key `def get_encrypted_file_and_key(self, username, filename)`
- Defined: `controllers/file.py:107`
- Doc: Fetch a user's encrypted file and its wrapped FEK from S3.
- Depends on: `utils/utils.py`
- Imported by: `app_factory.py`

### list_encrypted_files `def list_encrypted_files(self, username)`
- Defined: `controllers/file.py:137`
- Doc: List the encrypted files that belong to ``username``.
- Depends on: `utils/utils.py`
- Imported by: `app_factory.py`

## controllers/message.py

### __init__ `def __init__(self, users_path, users_db_path)`
- Defined: `controllers/message.py:18`
- Doc: Initialize the controller.
- Depends on: `models/message.py`, `models/user.py`
- Imported by: `views/message.py`

### send_encrypted_message `def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)`
- Defined: `controllers/message.py:31`
- Doc: Persist an opaque message envelope for the recipient.
- Depends on: `models/message.py`, `models/user.py`
- Imported by: `views/message.py`

### get_messages `def get_messages(self, username, page, per_page)`
- Defined: `controllers/message.py:73`
- Doc: Return opaque message envelopes for the user.
- Depends on: `models/message.py`, `models/user.py`
- Imported by: `views/message.py`

## controllers/sync.py

### __init__ `def __init__(self, users_path, s3_bucket, s3_client, file_controller)`
- Defined: `controllers/sync.py:8`
- Imported by: `app_factory.py`

### get_storage_usage `def get_storage_usage(self, username)`
- Defined: `controllers/sync.py:14`
- Doc: Calcula el uso de almacenamiento del usuario en S3.
- Imported by: `app_factory.py`

## enc_dec.go

### deriveAESKey `func deriveAESKey(`
- Defined: `enc_dec.go:20`

### encryptFile `func encryptFile(`
- Defined: `enc_dec.go:24`

### decryptFile `func decryptFile(`
- Defined: `enc_dec.go:45`

### main `func main(`
- Defined: `enc_dec.go:69`

## enc_dec.py

### derive_aes_key `def derive_aes_key(shared_secret)`
- Defined: `enc_dec.py:36`
- Doc: Derive a 32-byte AES key from an ML-KEM shared secret.

### encrypt_file_in_memory `def encrypt_file_in_memory(data, aes_key)`
- Defined: `enc_dec.py:49`
- Doc: Encrypt ``data`` in memory with AES-256-GCM and return nonce + ciphertext.

### decrypt_file_in_memory `def decrypt_file_in_memory(nonce, ciphertext, aes_key)`
- Defined: `enc_dec.py:65`
- Doc: Decrypt ``ciphertext`` in memory with AES-256-GCM and return the plaintext.

### _build_s3_client `def _build_s3_client(region)`
- Defined: `enc_dec.py:81`
- Doc: Build a boto3 S3 client honoring the zero-trust environment convention.

### main `def main()`
- Defined: `enc_dec.py:103`
- Doc: Run the offline admin CLI (encrypt or decrypt a single object).

## models/contact.py

### __init__ `def __init__(self, db_path)`
- Defined: `models/contact.py:29`
- Doc: Initialize the ContactDB with the database path.
- Imported by: `controllers/contact.py`

### _init_db `def _init_db(self)`
- Defined: `models/contact.py:38`
- Doc: Initialize the contacts table with all required fields.
- Imported by: `controllers/contact.py`

### create_contact `def create_contact(self, user_id, subject, message)`
- Defined: `models/contact.py:52`
- Doc: Create a new contact message.
- Imported by: `controllers/contact.py`

### get_user_contacts `def get_user_contacts(self, user_id)`
- Defined: `models/contact.py:89`
- Doc: Retrieve all contact messages for a user.
- Imported by: `controllers/contact.py`

### _convert_row_to_dict `def _convert_row_to_dict(self, row)`
- Defined: `models/contact.py:115`
- Doc: Convert an SQLite row to a dictionary.
- Imported by: `controllers/contact.py`

### get_all_contacts `def get_all_contacts(self, page, per_page)`
- Defined: `models/contact.py:139`
- Doc: Retrieve all contact messages with pagination.
- Imported by: `controllers/contact.py`

### _convert_row_to_dict_with_username `def _convert_row_to_dict_with_username(self, row)`
- Defined: `models/contact.py:168`
- Doc: Convert an SQLite row to a dictionary, including username.
- Imported by: `controllers/contact.py`

## models/deniable_vault.py

### __init__ `def __init__(self, db_path)`
- Defined: `models/deniable_vault.py:33`
- Doc: Initialize the store and ensure its table exists.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

### _init_db `def _init_db(self)`
- Defined: `models/deniable_vault.py:43`
- Doc: Create the ``deniable_vaults`` table on first use.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

### upsert `def upsert(self, username, envelope)`
- Defined: `models/deniable_vault.py:57`
- Doc: Insert or replace the container for ``username``.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

### get `def get(self, username)`
- Defined: `models/deniable_vault.py:82`
- Doc: Return the stored container for ``username``, or ``None``.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

### exists `def exists(self, username)`
- Defined: `models/deniable_vault.py:101`
- Doc: Return True if ``username`` has a stored container.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

## models/message.py

### __init__ `def __init__(self, base_path)`
- Defined: `models/message.py:46`
- Doc: Initialize the MessageDB with the base directory for per-user mailboxes.
- Imported by: `controllers/message.py`, `utils/scheduler.py`

### save_message `def save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipient, cek_for_sender, message_id)`
- Defined: `models/message.py:55`
- Doc: Persist an opaque message envelope for the recipient.
- Imported by: `controllers/message.py`, `utils/scheduler.py`

### get_messages `def get_messages(self, recipient, page, per_page)`
- Defined: `models/message.py:87`
- Doc: Return opaque message envelopes for the recipient.
- Imported by: `controllers/message.py`, `utils/scheduler.py`

### delete_old_messages `def delete_old_messages(self, recipient, days)`
- Defined: `models/message.py:172`
- Doc: Delete messages older than ``days`` days from the recipient's mailbox.
- Imported by: `controllers/message.py`, `utils/scheduler.py`

## models/plans.py

### __init__ `def __init__(self, db_path)`
- Defined: `models/plans.py:6`
- Doc: Initialize the PlanDB with the database path.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### _init_db `def _init_db(self)`
- Defined: `models/plans.py:15`
- Doc: Initialize the plans table with required fields.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### get_plan `def get_plan(self, plan_name)`
- Defined: `models/plans.py:37`
- Doc: Retrieve a plan by name.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### get_all_plans `def get_all_plans(self)`
- Defined: `models/plans.py:50`
- Doc: Retrieve all plans.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### create_plan `def create_plan(self, name, storage_quota, trial_days, price)`
- Defined: `models/plans.py:60`
- Doc: Create a new plan.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### update_plan `def update_plan(self, name, storage_quota, trial_days, price)`
- Defined: `models/plans.py:78`
- Doc: Update an existing plan.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### delete_plan `def delete_plan(self, name)`
- Defined: `models/plans.py:113`
- Doc: Delete a plan by name.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### _convert_row_to_dict `def _convert_row_to_dict(self, row)`
- Defined: `models/plans.py:127`
- Doc: Convert an SQLite row to a dictionary.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### validate_plan_payment `def validate_plan_payment(self, plan_name, amount_paid)`
- Defined: `models/plans.py:139`
- Doc: Validate that the paid amount matches the plan price.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

## models/superadmin_audit.py

### __init__ `def __init__(self, db_path)`
- Defined: `models/superadmin_audit.py:35`
- Doc: Initialize the audit log and ensure its table exists.
- Imported by: `views/admin.py`

### _init_db `def _init_db(self)`
- Defined: `models/superadmin_audit.py:45`
- Doc: Create the audit table on first use; no-op if it already exists.
- Imported by: `views/admin.py`

### record `def record(self, actor, action, target_user, ip, details)`
- Defined: `models/superadmin_audit.py:75`
- Doc: Append one audit row and return its id.
- Imported by: `views/admin.py`

### recent `def recent(self, limit)`
- Defined: `models/superadmin_audit.py:119`
- Doc: Return the most recent ``limit`` audit rows, newest first.
- Imported by: `views/admin.py`

## models/user.py

### get_id `def get_id(self)`
- Defined: `models/user.py:52`
- Doc: Return the user ID as a string (required by Flask-Login).
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### is_active `def is_active(self)`
- Defined: `models/user.py:70`
- Doc: Return True while the user can use the application.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### __init__ `def __init__(self, db_path)`
- Defined: `models/user.py:85`
- Doc: Initialize the UserDB with the database path.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _init_db `def _init_db(self)`
- Defined: `models/user.py:105`
- Doc: Initialize the users table with all fields for zero-knowledge auth.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _has_phone_unique_constraint `def _has_phone_unique_constraint(self)`
- Defined: `models/user.py:193`
- Doc: Return True if the ``users.phone`` column is UNIQUE.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _drop_phone_unique_if_present `def _drop_phone_unique_if_present(self)`
- Defined: `models/user.py:214`
- Doc: Remove the UNIQUE constraint on ``users.phone``.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _migrate_from_v7 `def _migrate_from_v7(self, legacy_columns)`
- Defined: `models/user.py:271`
- Doc: Rebuild the users table to drop legacy v7 NOT NULL KEM columns.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### create_user `def create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, role, storage_quota, trial_start, trial_end, subscription_status, email_verified, confirmation_token, phone_verified, phone_verification_code_hash, phone_code_expires, mfa_enabled, recovery_salt, encrypted_private_key_recovery)`
- Defined: `models/user.py:325`
- Doc: Persist a new user from client-provided zero-knowledge credentials.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### update_user_phone_status `def update_user_phone_status(self, username, phone_verified, phone_verification_code_hash, phone_code_expires)`
- Defined: `models/user.py:362`
- Doc: Update phone verification status and related fields.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### update_user_mfa_status `def update_user_mfa_status(self, username, mfa_code_hash, mfa_code_expires, mfa_enabled)`
- Defined: `models/user.py:396`
- Doc: Update MFA code, expiration, and enabled status.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### update_user `def update_user(self, username, email_verified, confirmation_token)`
- Defined: `models/user.py:430`
- Doc: Update specific user fields.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user `def get_user(self, username)`
- Defined: `models/user.py:454`
- Doc: Retrieve a user by username.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user_by_id `def get_user_by_id(self, user_id)`
- Defined: `models/user.py:468`
- Doc: Retrieve a user by ID.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user_by_email `def get_user_by_email(self, email)`
- Defined: `models/user.py:482`
- Doc: Retrieve a user by email address.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user_by_phone `def get_user_by_phone(self, phone)`
- Defined: `models/user.py:496`
- Doc: Retrieve a user by phone number.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user_by_confirmation_token `def get_user_by_confirmation_token(self, token)`
- Defined: `models/user.py:510`
- Doc: Retrieve a user by confirmation token.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_recovery_bundle `def get_recovery_bundle(self, username)`
- Defined: `models/user.py:524`
- Doc: Return the QV-RECOVERY-1 bundle for a username, if one exists.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### reset_credentials_with_recovery `def reset_credentials_with_recovery(self, username, srp_salt, srp_verifier, kdf_salt, encrypted_private_key)`
- Defined: `models/user.py:548`
- Doc: Replace a user's password-derived credentials after a verified recovery.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### update_role `def update_role(self, username, role, storage_quota, subscription_status)`
- Defined: `models/user.py:579`
- Doc: Update a user's role, storage quota, and subscription status.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### count_users `def count_users(self)`
- Defined: `models/user.py:592`
- Doc: Return the total number of users.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_all_users `def get_all_users(self)`
- Defined: `models/user.py:603`
- Doc: Retrieve all users.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _parse_datetime `def _parse_datetime(value)`
- Defined: `models/user.py:615`
- Doc: Parse a stored timestamp into a datetime, tolerating the format.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _convert_row_to_dict `def _convert_row_to_dict(self, row)`
- Defined: `models/user.py:638`
- Doc: Convert a name-keyed SQLite row into a plain dictionary.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### fetch_one `def fetch_one(self, query, params)`
- Defined: `models/user.py:694`
- Doc: Execute a query and return the first result as a dictionary.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### value `def value(name, default)`
- Defined: `models/user.py:655`
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_deniable_vault.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

## scripts/email_tool.py

### _build_mail_app `def _build_mail_app(config)`
- Defined: `scripts/email_tool.py:40`
- Doc: Build a minimal Flask app that only carries the mail configuration.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### cmd_test_smtp `def cmd_test_smtp(args)`
- Defined: `scripts/email_tool.py:63`
- Doc: Send a test email through the configured SMTP server.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### cmd_link `def cmd_link(args)`
- Defined: `scripts/email_tool.py:91`
- Doc: Print the confirmation URL for a user without sending email.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### cmd_confirm `def cmd_confirm(args)`
- Defined: `scripts/email_tool.py:114`
- Doc: Mark a user's email as verified directly in the database.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### build_parser `def build_parser()`
- Defined: `scripts/email_tool.py:133`
- Doc: Construct the argument parser for the three subcommands.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### main `def main()`
- Defined: `scripts/email_tool.py:153`
- Doc: Parse arguments and dispatch to the selected subcommand.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

## scripts/garage-init.sh

### upsert_env
- Defined: `scripts/garage-init.sh:35`
- Doc: Insert or update a KEY=value line in .env without disturbing other lines.

## scripts/garage-native.sh

### upsert_env
- Defined: `scripts/garage-native.sh:46`
- Doc: Insert or update a KEY=value line in .env without disturbing other lines.

### s3_reachable
- Defined: `scripts/garage-native.sh:56`

### gcmd
- Defined: `scripts/garage-native.sh:141`

## scripts/makeadmin.py

### _resolve_db_path `def _resolve_db_path()`
- Defined: `scripts/makeadmin.py:51`
- Doc: Return the absolute users.db path, anchored at the project root.
- Depends on: `models/user.py`

### _print_user_summary `def _print_user_summary(user)`
- Defined: `scripts/makeadmin.py:64`
- Doc: Print the post-update user record so the operator can eyeball it.
- Depends on: `models/user.py`

### cmd_promote `def cmd_promote(args)`
- Defined: `scripts/makeadmin.py:75`
- Doc: Promote ``args.username`` to the requested role (default: superadmin).
- Depends on: `models/user.py`

### build_parser `def build_parser()`
- Defined: `scripts/makeadmin.py:126`
- Doc: Construct the argument parser for the makeadmin subcommands.
- Depends on: `models/user.py`

### main `def main()`
- Defined: `scripts/makeadmin.py:152`
- Doc: Parse arguments and dispatch to the selected subcommand.
- Depends on: `models/user.py`

## scripts/test_bloque1.py

### _load_user `def _load_user(uid)`
- Defined: `scripts/test_bloque1.py:62`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### check `def check(name, ok, detail)`
- Defined: `scripts/test_bloque1.py:86`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### __init__ `def __init__(self, row)`
- Defined: `scripts/test_bloque1.py:49`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### is_authenticated `def is_authenticated(self)`
- Defined: `scripts/test_bloque1.py:54`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### is_active `def is_active(self)`
- Defined: `scripts/test_bloque1.py:56`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### is_anonymous `def is_anonymous(self)`
- Defined: `scripts/test_bloque1.py:58`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### get_id `def get_id(self)`
- Defined: `scripts/test_bloque1.py:59`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

## server.go

### main `func main(`
- Defined: `server.go:11`

### handleConnection `func handleConnection(`
- Defined: `server.go:40`

## static/js/account.js

### setStatus
- Defined: `static/js/account.js:19`
- Depends on: `static/js/qv-deniable.js`

### csrfToken
- Defined: `static/js/account.js:30`
- Depends on: `static/js/qv-deniable.js`

### apiRequest
- Defined: `static/js/account.js:36`
- Depends on: `static/js/qv-deniable.js`

### loadState
- Defined: `static/js/account.js:54`
- Depends on: `static/js/qv-deniable.js`

### collectSlots
- Defined: `static/js/account.js:59`
- Depends on: `static/js/qv-deniable.js`

### handleConfigure
- Defined: `static/js/account.js:73`
- Depends on: `static/js/qv-deniable.js`

### handleOpen
- Defined: `static/js/account.js:98`
- Depends on: `static/js/qv-deniable.js`

### handleReset
- Defined: `static/js/account.js:120`
- Depends on: `static/js/qv-deniable.js`

### init
- Defined: `static/js/account.js:133`
- Depends on: `static/js/qv-deniable.js`

## static/js/coded-text.js

### randomChar
- Defined: `static/js/coded-text.js:12`

### animateElement
- Defined: `static/js/coded-text.js:18`

### init
- Defined: `static/js/coded-text.js:49`

## static/js/login.js

### handleLogin
- Defined: `static/js/login.js:11`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

### init
- Defined: `static/js/login.js:43`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/messages.js

### getCsrfToken
- Defined: `static/js/messages.js:11`
- Depends on: `static/js/qv-crypto.js`

### handleSend
- Defined: `static/js/messages.js:17`
- Depends on: `static/js/qv-crypto.js`

### collectEnvelopes
- Defined: `static/js/messages.js:43`
- Depends on: `static/js/qv-crypto.js`

### handleDecryptInbox
- Defined: `static/js/messages.js:60`
- Depends on: `static/js/qv-crypto.js`

### initEditor
- Defined: `static/js/messages.js:87`
- Depends on: `static/js/qv-crypto.js`

### init
- Defined: `static/js/messages.js:108`
- Depends on: `static/js/qv-crypto.js`

## static/js/qv-crypto.js

### concatBytes
- Defined: `static/js/qv-crypto.js:52`
- Doc: -- Encoding helpers ---
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### hexToBytes
- Defined: `static/js/qv-crypto.js:63`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### bytesToHex
- Defined: `static/js/qv-crypto.js:72`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### bytesToBase64
- Defined: `static/js/qv-crypto.js:78`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### bytesToBase32
- Defined: `static/js/qv-crypto.js:89`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### base64ToBytes
- Defined: `static/js/qv-crypto.js:107`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### bytesToBigInt
- Defined: `static/js/qv-crypto.js:114`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### i2osp
- Defined: `static/js/qv-crypto.js:121`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### mod
- Defined: `static/js/qv-crypto.js:131`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### modPow
- Defined: `static/js/qv-crypto.js:135`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### randomBytes
- Defined: `static/js/qv-crypto.js:153`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### H
- Defined: `static/js/qv-crypto.js:162`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### Hint
- Defined: `static/js/qv-crypto.js:166`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### deriveKeyFromPassphrase
- Defined: `static/js/qv-crypto.js:178`
- Doc: Derive a 256-bit key from a passphrase with a caller-chosen PBKDF2 iteration count. This is the single PBKDF2 implementa
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### deriveMasterKey
- Defined: `static/js/qv-crypto.js:199`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### aesGcmEncrypt
- Defined: `static/js/qv-crypto.js:203`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### aesGcmDecrypt
- Defined: `static/js/qv-crypto.js:214`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### computeK
- Defined: `static/js/qv-crypto.js:244`
- Doc: -- SRP-6a (QV-SRP-1), mirrors utils/srp6a.py ---
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### deriveVerifier
- Defined: `static/js/qv-crypto.js:249`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### srpLogin
- Defined: `static/js/qv-crypto.js:257`
- Doc: Run a full SRP-6a login against the server, verifying the server proof M2.
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### generateIdentity
- Defined: `static/js/qv-crypto.js:309`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### parsePublicKey
- Defined: `static/js/qv-crypto.js:337`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### parsePrivateBlob
- Defined: `static/js/qv-crypto.js:345`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### deriveWrapKey
- Defined: `static/js/qv-crypto.js:353`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### wrapKey
- Defined: `static/js/qv-crypto.js:365`
- Doc: Seal a file encryption key to a recipient's hybrid public key.
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### unwrapKey
- Defined: `static/js/qv-crypto.js:389`
- Doc: Recover a file encryption key using the recipient's hybrid private blob.
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### generateRecoveryCode
- Defined: `static/js/qv-crypto.js:411`
- Doc: Generate a QV-RECOVERY-1 code: 20 random bytes (160 bits) Base32-encoded (RFC 4648, no padding) and grouped as XXXX-XXXX
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### normalizeRecoveryCode
- Defined: `static/js/qv-crypto.js:422`
- Doc: Normalize a user-entered recovery code: strip surrounding whitespace, remove group separators, and uppercase, so "abcd-e
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### wrapPrivateKeyForRecovery
- Defined: `static/js/qv-crypto.js:430`
- Doc: Re-wrap an existing privateBlob under a key derived from a recovery code, using the same PBKDF2-SHA256 + AES-256-GCM sch
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### derivePublicKeyFromPrivateBlob
- Defined: `static/js/qv-crypto.js:449`
- Doc: Reconstruct the public key (the same {v, mlkem, x} structure produced by generateIdentity) from a decrypted privateBlob.
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### postJson
- Defined: `static/js/qv-crypto.js:467`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### buildRegistration
- Defined: `static/js/qv-crypto.js:490`
- Doc: Build the zero-knowledge registration payload entirely in the browser.  Returns `{ payload, recoveryCode }`: `payload` i
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### register
- Defined: `static/js/qv-crypto.js:524`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### recoverAccount
- Defined: `static/js/qv-crypto.js:535`
- Doc: Reset SRP credentials and the password-encrypted private key using a QV-RECOVERY-1 recovery code, without ever exposing 
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### login
- Defined: `static/js/qv-crypto.js:586`
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### encryptAndUpload
- Defined: `static/js/qv-crypto.js:591`
- Doc: Generate a fresh file key, encrypt the file, wrap the key, and upload.
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### downloadAndDecrypt
- Defined: `static/js/qv-crypto.js:620`
- Doc: Download an encrypted file and its key, then decrypt it in the browser.
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### fetchPublicKey
- Defined: `static/js/qv-crypto.js:658`
- Doc: Fetch a user's hybrid public key so the browser can wrap content to them.
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### sendSecureMessage
- Defined: `static/js/qv-crypto.js:673`
- Doc: Encrypt a message to a recipient (keeping a sender-readable outbox copy) and POST the opaque envelope. The plaintext and
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### decryptInbox
- Defined: `static/js/qv-crypto.js:703`
- Doc: Decrypt a batch of inbox envelopes with the user's password. The master key and private blob are derived once and reused
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

## static/js/qv-deniable.js

### toBytes
- Defined: `static/js/qv-deniable.js:47`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### frame
- Defined: `static/js/qv-deniable.js:55`
- Doc: Frame a payload as [len(4) | payload | random padding] of exactly `paddedLength` bytes. `paddedLength` is shared by ever
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### unframe
- Defined: `static/js/qv-deniable.js:64`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### sealSlot
- Defined: `static/js/qv-deniable.js:82`
- Doc: Encrypt one slot's framed plaintext under a passphrase, returning the {salt, nonce, ct} object the envelope stores.
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### openSlot
- Defined: `static/js/qv-deniable.js:102`
- Doc: Attempt to open one slot with a passphrase. Returns the payload bytes on success or null when the passphrase does not au
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### buildDeniableVault
- Defined: `static/js/qv-deniable.js:125`
- Doc: Build a deniable container from a list of slot specifications.  `slots` is an array of `{ passphrase, data }`; `data` ma
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### openDeniableVault
- Defined: `static/js/qv-deniable.js:170`
- Doc: Open a container with a passphrase. Tries every slot; only the slot whose passphrase matches will authenticate. Returns 
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

## static/js/recover.js

### setStatus
- Defined: `static/js/recover.js:14`
- Depends on: `static/js/qv-crypto.js`

### handleRecover
- Defined: `static/js/recover.js:22`
- Depends on: `static/js/qv-crypto.js`

### init
- Defined: `static/js/recover.js:79`
- Depends on: `static/js/qv-crypto.js`

## static/js/register.js

### showRecoveryCode
- Defined: `static/js/register.js:16`
- Doc: Display the one-time QV-RECOVERY-1 code in a modal and wait for the user to acknowledge they have saved it before contin
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

### handleRegister
- Defined: `static/js/register.js:42`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

### init
- Defined: `static/js/register.js:109`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/upload.js

### getCsrfToken
- Defined: `static/js/upload.js:11`
- Depends on: `static/js/qv-crypto.js`

### getUsername
- Defined: `static/js/upload.js:16`
- Depends on: `static/js/qv-crypto.js`

### getPublicKey
- Defined: `static/js/upload.js:23`
- Depends on: `static/js/qv-crypto.js`

### handleUpload
- Defined: `static/js/upload.js:40`
- Depends on: `static/js/qv-crypto.js`

### handleDownload
- Defined: `static/js/upload.js:74`
- Depends on: `static/js/qv-crypto.js`

### init
- Defined: `static/js/upload.js:96`
- Depends on: `static/js/qv-crypto.js`

## templates/terms.py

### terms `def terms()`
- Defined: `templates/terms.py:6`
- Doc: Render the About page.

## tests/conftest.py

### _push_request_context `def _push_request_context()`
- Defined: `tests/conftest.py:34`
- Doc: Neutralize pytest-flask's autouse request-context push.
- Depends on: `app_factory.py`, `utils/security.py`

### app `def app(tmp_path)`
- Defined: `tests/conftest.py:52`
- Doc: Return a QuantumVault Flask app configured for testing.
- Depends on: `app_factory.py`, `utils/security.py`

### client `def client(app)`
- Defined: `tests/conftest.py:77`
- Doc: Return a Flask test client for the test app.
- Depends on: `app_factory.py`, `utils/security.py`

### audit_records `def audit_records()`
- Defined: `tests/conftest.py:94`
- Doc: Yield a list that is appended with each ``audit_event`` JSON line.
- Depends on: `app_factory.py`, `utils/security.py`

### __init__ `def __init__(self)`
- Defined: `tests/conftest.py:85`
- Depends on: `app_factory.py`, `utils/security.py`

### emit `def emit(self, record)`
- Defined: `tests/conftest.py:89`
- Depends on: `app_factory.py`, `utils/security.py`

## tests/test_auth_phone.py

### test_verify_phone_page_renders `def test_verify_phone_page_renders(client)`
- Defined: `tests/test_auth_phone.py:18`
- Doc: GET /verify_phone must render without a url_for BuildError.

### test_resend_endpoint_is_registered `def test_resend_endpoint_is_registered(app)`
- Defined: `tests/test_auth_phone.py:25`
- Doc: The resend endpoint the template links to must exist.

### test_resend_route_accepts_only_post `def test_resend_route_accepts_only_post(app)`
- Defined: `tests/test_auth_phone.py:31`
- Doc: The resend endpoint is POST-only so a GET cannot trigger an SMS.

## tests/test_deniable_vault.py

### config `def config()`
- Defined: `tests/test_deniable_vault.py:50`
- Doc: Return the default deniable-vault configuration.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### validator `def validator(config)`
- Defined: `tests/test_deniable_vault.py:56`
- Doc: Return a validator bound to the default configuration.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _ciphertext `def _ciphertext(config, length)`
- Defined: `tests/test_deniable_vault.py:61`
- Doc: Return a base64 ciphertext string of the given (or expected) length.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _valid_envelope `def _valid_envelope(config)`
- Defined: `tests/test_deniable_vault.py:71`
- Doc: Build a structurally valid envelope for ``config``.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _make_user `def _make_user(app, username, role)`
- Defined: `tests/test_deniable_vault.py:91`
- Doc: Create a minimal user row in the test database and return it.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _login `def _login(client, app, username, role)`
- Defined: `tests/test_deniable_vault.py:120`
- Doc: Create and authenticate a user on ``client``'s session.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _csrf `def _csrf(client)`
- Defined: `tests/test_deniable_vault.py:130`
- Doc: Fetch a CSRF token bound to the client's session.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_defaults_are_self_consistent `def test_defaults_are_self_consistent(self)`
- Defined: `tests/test_deniable_vault.py:141`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_expected_ct_length_matches_base64_formula `def test_expected_ct_length_matches_base64_formula(self, config)`
- Defined: `tests/test_deniable_vault.py:150`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_mapping_overrides_defaults `def test_mapping_overrides_defaults(self)`
- Defined: `tests/test_deniable_vault.py:154`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_environment_overrides_mapping `def test_environment_overrides_mapping(self, monkeypatch)`
- Defined: `tests/test_deniable_vault.py:161`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_allowed_kdf_csv_is_parsed `def test_allowed_kdf_csv_is_parsed(self, monkeypatch)`
- Defined: `tests/test_deniable_vault.py:166`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_public_parameters_round_trip_to_json `def test_public_parameters_round_trip_to_json(self, config)`
- Defined: `tests/test_deniable_vault.py:172`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_accepts_a_well_formed_envelope `def test_accepts_a_well_formed_envelope(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:186`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_non_dict `def test_rejects_non_dict(self, validator)`
- Defined: `tests/test_deniable_vault.py:189`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_wrong_schema_version `def test_rejects_wrong_schema_version(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:194`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_unknown_kdf `def test_rejects_unknown_kdf(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:200`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_iterations_below_minimum `def test_rejects_iterations_below_minimum(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:206`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_iterations_above_maximum `def test_rejects_iterations_above_maximum(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:212`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_wrong_slot_count `def test_rejects_wrong_slot_count(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:218`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_bad_salt_length `def test_rejects_bad_salt_length(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:224`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_non_hex_salt `def test_rejects_non_hex_salt(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:230`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_bad_nonce_length `def test_rejects_bad_nonce_length(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:236`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_ciphertext_of_wrong_length `def test_rejects_ciphertext_of_wrong_length(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:242`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_unequal_slot_ciphertext_lengths `def test_rejects_unequal_slot_ciphertext_lengths(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:248`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_invalid_base64_ciphertext `def test_rejects_invalid_base64_ciphertext(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:254`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_missing_slot_keys `def test_rejects_missing_slot_keys(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:260`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_random_container_passes_validation `def test_random_container_passes_validation(self, config, validator)`
- Defined: `tests/test_deniable_vault.py:273`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_random_containers_differ `def test_random_containers_differ(self, config)`
- Defined: `tests/test_deniable_vault.py:276`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_random_container_has_fixed_shape `def test_random_container_has_fixed_shape(self, config)`
- Defined: `tests/test_deniable_vault.py:281`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_upsert_then_get_round_trips_verbatim `def test_upsert_then_get_round_trips_verbatim(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:294`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_upsert_replaces_existing_row `def test_upsert_replaces_existing_row(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:303`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_get_missing_returns_none `def test_get_missing_returns_none(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:309`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_exists `def test_exists(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:313`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _controller `def _controller(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:326`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_load_or_provision_mints_when_absent `def test_load_or_provision_mints_when_absent(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:331`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_load_or_provision_is_stable `def test_load_or_provision_is_stable(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:339`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_save_then_load_round_trips `def test_save_then_load_round_trips(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:346`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_save_rejects_invalid_envelope `def test_save_rejects_invalid_envelope(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:354`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_reset_replaces_with_a_valid_random_container `def test_reset_replaces_with_a_valid_random_container(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:363`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_audit_is_generic_and_never_contains_ciphertext `def test_audit_is_generic_and_never_contains_ciphertext(self, app, tmp_path, audit_records)`
- Defined: `tests/test_deniable_vault.py:373`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_settings_page_requires_authentication `def test_settings_page_requires_authentication(self, client)`
- Defined: `tests/test_deniable_vault.py:391`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_get_api_requires_authentication `def test_get_api_requires_authentication(self, client)`
- Defined: `tests/test_deniable_vault.py:395`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_settings_page_renders_for_authenticated_user `def test_settings_page_renders_for_authenticated_user(self, client, app)`
- Defined: `tests/test_deniable_vault.py:399`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_get_always_returns_an_envelope_and_parameters `def test_get_always_returns_an_envelope_and_parameters(self, client, app)`
- Defined: `tests/test_deniable_vault.py:406`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_put_without_csrf_is_rejected `def test_put_without_csrf_is_rejected(self, client, app)`
- Defined: `tests/test_deniable_vault.py:414`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_put_get_reset_round_trip `def test_put_get_reset_round_trip(self, client, app)`
- Defined: `tests/test_deniable_vault.py:422`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_put_rejects_malformed_envelope `def test_put_rejects_malformed_envelope(self, client, app)`
- Defined: `tests/test_deniable_vault.py:447`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_vault_is_scoped_to_the_authenticated_user `def test_vault_is_scoped_to_the_authenticated_user(self, client, app)`
- Defined: `tests/test_deniable_vault.py:461`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

## tests/test_security.py

### test_audit_event_includes_ip_and_ua_by_default `def test_audit_event_includes_ip_and_ua_by_default(app, audit_records, monkeypatch)`
- Defined: `tests/test_security.py:12`
- Depends on: `utils/security.py`

### test_audit_event_redacts_ip_and_ua_when_disabled `def test_audit_event_redacts_ip_and_ua_when_disabled(app, audit_records, monkeypatch)`
- Defined: `tests/test_security.py:29`
- Depends on: `utils/security.py`

### test_json_csrf_protect_rejects_missing_token `def test_json_csrf_protect_rejects_missing_token(app)`
- Defined: `tests/test_security.py:45`
- Depends on: `utils/security.py`

### test_json_csrf_protect_accepts_valid_header_token `def test_json_csrf_protect_accepts_valid_header_token(app)`
- Defined: `tests/test_security.py:57`
- Depends on: `utils/security.py`

### test_json_csrf_protect_passes_get_through_without_token `def test_json_csrf_protect_passes_get_through_without_token(app)`
- Defined: `tests/test_security.py:77`
- Depends on: `utils/security.py`

### view `def view()`
- Defined: `tests/test_security.py:47`
- Depends on: `utils/security.py`

### view `def view()`
- Defined: `tests/test_security.py:59`
- Depends on: `utils/security.py`

### view `def view()`
- Defined: `tests/test_security.py:79`
- Depends on: `utils/security.py`

## tests/test_srp.py

### _h `def _h()`
- Defined: `tests/test_srp.py:16`
- Depends on: `utils/utils.py`

### _hint `def _hint()`
- Defined: `tests/test_srp.py:23`
- Depends on: `utils/utils.py`

### _client_derive_verifier `def _client_derive_verifier(username, password, salt_hex)`
- Defined: `tests/test_srp.py:27`
- Doc: Mirror ``deriveVerifier`` in qv-crypto.js: v = g^x mod N.
- Depends on: `utils/utils.py`

### _client_compute_proof `def _client_compute_proof(username, password, salt_hex, server_a_secret, server_a, server_b)`
- Defined: `tests/test_srp.py:34`
- Doc: Mirror ``srpLogin`` in qv-crypto.js: derive M1 and the expected M2.
- Depends on: `utils/utils.py`

### test_srp6a_full_roundtrip_matches_server_proofs `def test_srp6a_full_roundtrip_matches_server_proofs()`
- Defined: `tests/test_srp.py:74`
- Depends on: `utils/utils.py`

### test_srp6a_wrong_password_produces_mismatched_proof `def test_srp6a_wrong_password_produces_mismatched_proof()`
- Defined: `tests/test_srp.py:104`
- Depends on: `utils/utils.py`

## utils/cache.py

### __init__ `def __init__(self)`
- Defined: `utils/cache.py:8`

### get `def get(self, key)`
- Defined: `utils/cache.py:11`
- Doc: Retrieve a value from the cache.

### set `def set(self, key, value, ttl)`
- Defined: `utils/cache.py:16`
- Doc: Store a value in the cache with an optional TTL (seconds).

### delete `def delete(self, key)`
- Defined: `utils/cache.py:20`
- Doc: Delete a key from the cache.

## utils/mailer.py

### external_url `def external_url(path)`
- Defined: `utils/mailer.py:22`
- Doc: Build an absolute URL for a root-relative path using the public host.
- Imported by: `controllers/auth.py`, `scripts/email_tool.py`, `utils/scheduler.py`, `views/auth.py`

### mail_is_configured `def mail_is_configured()`
- Defined: `utils/mailer.py:38`
- Doc: Return True when SMTP credentials are present so a send can succeed.
- Imported by: `controllers/auth.py`, `scripts/email_tool.py`, `utils/scheduler.py`, `views/auth.py`

### send_transactional_email `def send_transactional_email(subject, recipients, body)`
- Defined: `utils/mailer.py:51`
- Doc: Send a plain-text transactional email through the configured server.
- Imported by: `controllers/auth.py`, `scripts/email_tool.py`, `utils/scheduler.py`, `views/auth.py`

## utils/plans.py

### get_plan `def get_plan(plan_name)`
- Defined: `utils/plans.py:30`
- Doc: Obtiene los detalles de un plan.

### validate_plan_payment `def validate_plan_payment(plan_name, amount_paid)`
- Defined: `utils/plans.py:42`
- Doc: Valida que el monto pagado coincide con el plan.

## utils/scheduler.py

### _now_utc `def _now_utc()`
- Defined: `utils/scheduler.py:32`
- Doc: Timezone-aware UTC ``now`` (avoids the deprecated ``datetime.utcnow()``).
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

### init_scheduler `def init_scheduler(app, mail)`
- Defined: `utils/scheduler.py:37`
- Doc: Start the background scheduler with the production job schedule.
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

### _is_trial_elapsed `def _is_trial_elapsed(user)`
- Defined: `utils/scheduler.py:54`
- Doc: Return True if the user is on a free plan and the trial has ended.
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

### check_trial_expiration `def check_trial_expiration()`
- Defined: `utils/scheduler.py:72`
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

### cleanup_old_messages `def cleanup_old_messages()`
- Defined: `utils/scheduler.py:118`
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

## utils/security.py

### _get_audit_logger `def _get_audit_logger()`
- Defined: `utils/security.py:46`
- Doc: Return the process-wide audit logger, configured on first use.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### _correlation_id `def _correlation_id()`
- Defined: `utils/security.py:72`
- Doc: Return the per-request correlation id, generating one if missing.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### audit_event `def audit_event(event)`
- Defined: `utils/security.py:86`
- Doc: Emit a structured audit record.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### constant_time_compare `def constant_time_compare(a, b)`
- Defined: `utils/security.py:123`
- Doc: Return True if the two strings match in constant time.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### hash_secret `def hash_secret(secret)`
- Defined: `utils/security.py:135`
- Doc: Hash a short-lived secret (phone code, MFA, recovery code) for storage.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### verify_secret `def verify_secret(secret, expected_hash)`
- Defined: `utils/security.py:156`
- Doc: Verify a short-lived secret against its stored hash.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### new_one_time_code `def new_one_time_code(length)`
- Defined: `utils/security.py:163`
- Doc: Return a cryptographically random numeric verification code.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### _extract_csrf_token `def _extract_csrf_token()`
- Defined: `utils/security.py:172`
- Doc: Return the CSRF token from the request header or body.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### json_csrf_protect `def json_csrf_protect(view)`
- Defined: `utils/security.py:193`
- Doc: Decorator: require a valid CSRF token on JSON state-changing requests.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### wrapper `def wrapper()`
- Defined: `utils/security.py:207`
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

## utils/srp6a.py

### i2osp `def i2osp(value)`
- Defined: `utils/srp6a.py:47`
- Doc: Encode an integer as a big-endian byte string padded to the length of N.

### _hash `def _hash()`
- Defined: `utils/srp6a.py:60`
- Doc: Return the SHA-256 digest of the concatenated byte chunks.

### _hash_int `def _hash_int()`
- Defined: `utils/srp6a.py:68`
- Doc: Return the SHA-256 digest of the concatenated chunks as an integer.

### compute_k `def compute_k()`
- Defined: `utils/srp6a.py:73`
- Doc: Compute the SRP-6a multiplier parameter ``k = H(N | PAD(g))``.

### compute_u `def compute_u(server_a, server_b)`
- Defined: `utils/srp6a.py:78`
- Doc: Compute the random scrambling parameter ``u = H(PAD(A) | PAD(B))``.

### generate_server_challenge `def generate_server_challenge(verifier)`
- Defined: `utils/srp6a.py:91`
- Doc: Generate the server ephemeral key pair (b, B) for a login challenge.

### compute_proofs `def compute_proofs(username, salt_hex, verifier, server_a, server_b, server_b_secret)`
- Defined: `utils/srp6a.py:107`
- Doc: Compute the expected client proof M1 and the server proof M2.

### hello `def hello(store, username, client_a_hex, salt_hex, verifier_hex)`
- Defined: `utils/srp6a.py:224`
- Doc: Process the SRP ``hello`` step and return the server challenge B.

### verify `def verify(store, username, client_m1_hex)`
- Defined: `utils/srp6a.py:260`
- Doc: Process the SRP ``verify`` step and return the server proof M2.

### __init__ `def __init__(self, storage_uri)`
- Defined: `utils/srp6a.py:158`
- Doc: Initialize the store from a Redis connection URI.

### _key `def _key(username)`
- Defined: `utils/srp6a.py:168`
- Doc: Return the Redis key for a username's pending SRP session.

### save `def save(self, username, salt_hex, verifier_hex, server_a_hex, server_b_hex, server_b_secret_hex)`
- Defined: `utils/srp6a.py:172`
- Doc: Persist the ephemeral SRP challenge state for a username.

### load `def load(self, username)`
- Defined: `utils/srp6a.py:202`
- Doc: Load and consume the ephemeral SRP state for a username.

## utils/utils.py

### as_bool `def as_bool(value, default)`
- Defined: `utils/utils.py:11`
- Doc: Coerce an environment or payload value into a real boolean.
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/file.py`, `scripts/email_tool.py`, `tests/test_srp.py`, `utils/security.py`, `views/admin.py`, `views/sync.py`

### sanitize_path `def sanitize_path(path)`
- Defined: `utils/utils.py:31`
- Doc: Sanitiza una ruta de archivo para prevenir LFI y path traversal.
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/file.py`, `scripts/email_tool.py`, `tests/test_srp.py`, `utils/security.py`, `views/admin.py`, `views/sync.py`

### load_payload `def load_payload()`
- Defined: `utils/utils.py:150`
- Doc: Load non-secret application configuration from ``payload.json``.
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/file.py`, `scripts/email_tool.py`, `tests/test_srp.py`, `utils/security.py`, `views/admin.py`, `views/sync.py`

### __init__ `def __init__(self, config_dict)`
- Defined: `utils/utils.py:127`
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/file.py`, `scripts/email_tool.py`, `tests/test_srp.py`, `utils/security.py`, `views/admin.py`, `views/sync.py`

### __getitem__ `def __getitem__(self, key)`
- Defined: `utils/utils.py:147`
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/file.py`, `scripts/email_tool.py`, `tests/test_srp.py`, `utils/security.py`, `views/admin.py`, `views/sync.py`

## views/about.py

### about `def about()`
- Defined: `views/about.py:6`
- Doc: Render the About page.
- Imported by: `app_factory.py`

## views/account.py

### get_deniable_vault_controller `def get_deniable_vault_controller()`
- Defined: `views/account.py:50`
- Doc: Build a controller bound to the active app's database and config.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

### settings `def settings()`
- Defined: `views/account.py:64`
- Doc: Render the account settings page.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

### get_vault `def get_vault()`
- Defined: `views/account.py:77`
- Doc: Return the user's container and the build parameters.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

### put_vault `def put_vault()`
- Defined: `views/account.py:99`
- Doc: Validate and store a container for the user.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

### delete_vault `def delete_vault()`
- Defined: `views/account.py:122`
- Doc: Reset the user's container to a fresh random one.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

## views/admin.py

### admin `def admin()`
- Defined: `views/admin.py:68`
- Doc: Plan catalog read view.
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

### superadmin_edit_user `def superadmin_edit_user(username)`
- Defined: `views/admin.py:90`
- Doc: Full profile edit for a single user.
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

### manage_plans `def manage_plans()`
- Defined: `views/admin.py:195`
- Doc: Handle plan management.
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

### edit_plan `def edit_plan(plan_name)`
- Defined: `views/admin.py:219`
- Doc: Handle editing of plan details.
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

### superadmin `def superadmin()`
- Defined: `views/admin.py:255`
- Doc: Superadmin identity-recovery and inventory panel.
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

### superadmin_reset_mfa `def superadmin_reset_mfa(username)`
- Defined: `views/admin.py:342`
- Doc: Disable MFA and clear the pending code for ``username``.
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

### superadmin_resend_confirmation `def superadmin_resend_confirmation(username)`
- Defined: `views/admin.py:390`
- Doc: Issue a fresh ``confirmation_token`` for ``username``.
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

### superadmin_toggle_suspend `def superadmin_toggle_suspend(username)`
- Defined: `views/admin.py:438`
- Doc: Flip ``subscription_status`` between active and inactive.
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

### admin_contacts `def admin_contacts()`
- Defined: `views/admin.py:489`
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

## views/auth.py

### role_required `def role_required()`
- Defined: `views/auth.py:70`
- Doc: Restrict a route to authenticated users holding one of the given roles.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_auth_controller `def get_auth_controller()`
- Defined: `views/auth.py:131`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### show_register `def show_register()`
- Defined: `views/auth.py:142`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### handle_register `def handle_register()`
- Defined: `views/auth.py:149`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### login `def login()`
- Defined: `views/auth.py:233`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### recover `def recover()`
- Defined: `views/auth.py:241`
- Doc: Render the QV-RECOVERY-1 account-recovery page.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### _srp_key `def _srp_key()`
- Defined: `views/auth.py:254`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### _recovery_key `def _recovery_key()`
- Defined: `views/auth.py:265`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### srp_hello `def srp_hello()`
- Defined: `views/auth.py:277`
- Doc: First SRP-6a step: receive the client public value A, return salt and B.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### srp_verify `def srp_verify()`
- Defined: `views/auth.py:298`
- Doc: Second SRP-6a step: verify the client proof M1 and return server proof M2.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### logout `def logout()`
- Defined: `views/auth.py:336`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### confirm_email `def confirm_email(token)`
- Defined: `views/auth.py:343`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### verify_phone `def verify_phone()`
- Defined: `views/auth.py:366`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### resend_phone_verification `def resend_phone_verification()`
- Defined: `views/auth.py:383`
- Doc: Re-send the phone verification code for an account.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### verify_mfa `def verify_mfa()`
- Defined: `views/auth.py:406`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### toggle_mfa `def toggle_mfa()`
- Defined: `views/auth.py:428`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### contact `def contact()`
- Defined: `views/auth.py:453`
- Doc: Render the contact form and persist a message from the current user.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_public_key `def get_public_key()`
- Defined: `views/auth.py:484`
- Doc: Return a user's hybrid public key so the browser can wrap data to them.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_user_keys `def get_user_keys()`
- Defined: `views/auth.py:502`
- Doc: Provide the keys a user needs to decrypt their data client-side.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_recovery_bundle `def get_recovery_bundle()`
- Defined: `views/auth.py:533`
- Doc: Return the QV-RECOVERY-1 bundle for a username, if one was generated.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### reset_with_recovery `def reset_with_recovery()`
- Defined: `views/auth.py:558`
- Doc: Reset SRP credentials and the password-wrapped private key via QV-RECOVERY-1.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_csrf_token `def get_csrf_token()`
- Defined: `views/auth.py:618`
- Doc: Issue the CSRF token used by the SPA for state-changing JSON calls.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### decorator `def decorator(f)`
- Defined: `views/auth.py:84`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### decorated_function `def decorated_function()`
- Defined: `views/auth.py:86`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

## views/faq.py

### faq `def faq()`
- Defined: `views/faq.py:6`
- Doc: Render the About page.
- Depends on: `models/plans.py`
- Imported by: `app_factory.py`

### landing `def landing()`
- Defined: `views/faq.py:11`
- Doc: Render the About page.
- Depends on: `models/plans.py`
- Imported by: `app_factory.py`

## views/file.py

### upload `def upload()`
- Defined: `views/file.py:25`
- Doc: Maneja la subida de archivos cifrados desde el cliente.
- Depends on: `views/auth.py`
- Imported by: `app_factory.py`

### download `def download(filename)`
- Defined: `views/file.py:56`
- Doc: Provide the encrypted file and its key for client-side decryption.
- Depends on: `views/auth.py`
- Imported by: `app_factory.py`

## views/message.py

### messages `def messages()`
- Defined: `views/message.py:29`
- Doc: Render the messages page; the browser handles all crypto.
- Depends on: `controllers/message.py`, `views/auth.py`
- Imported by: `app_factory.py`

### api_secure_message `def api_secure_message()`
- Defined: `views/message.py:49`
- Doc: Accept an opaque end-to-end encrypted message envelope.
- Depends on: `controllers/message.py`, `views/auth.py`
- Imported by: `app_factory.py`

## views/privacy.py

### privacy `def privacy()`
- Defined: `views/privacy.py:6`
- Doc: Render the About page.
- Imported by: `app_factory.py`

## views/subscription.py

### subscribe `def subscribe()`
- Defined: `views/subscription.py:37`
- Doc: Maneja la selección de planes y el proceso de pago.
- Depends on: `models/plans.py`, `models/user.py`, `views/auth.py`
- Imported by: `app_factory.py`

### payment_success `def payment_success()`
- Defined: `views/subscription.py:86`
- Doc: Maneja el éxito del pago y actualiza el plan del usuario.
- Depends on: `models/plans.py`, `models/user.py`, `views/auth.py`
- Imported by: `app_factory.py`

### __init__ `def __init__(self)`
- Defined: `views/subscription.py:26`
- Depends on: `models/plans.py`, `models/user.py`, `views/auth.py`
- Imported by: `app_factory.py`

## views/sync.py

### secure_sync `def secure_sync()`
- Defined: `views/sync.py:29`
- Doc: Receive an already-encrypted file + wrapped FEK and persist them.
- Depends on: `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`

### sync_page `def sync_page()`
- Defined: `views/sync.py:79`
- Depends on: `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`

## views/terms.py

### terms `def terms()`
- Defined: `views/terms.py:6`
- Doc: Render the About page.
- Imported by: `app_factory.py`

## views/views.py

### home `def home()`
- Defined: `views/views.py:20`
- Doc: Render the landing/home page.
- Depends on: `models/user.py`
- Imported by: `app_factory.py`
