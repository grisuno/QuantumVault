# API

## app.py

### main (function) `def main()`
- Defined: `app.py:21`
- Depends on: `app_factory.py`, `utils/utils.py`
- Imported by: `scripts/test_bloque1.py`

### _is_production_like (function) `def _is_production_like()`
- Defined: `app.py:58`
- Doc: Return True if the runtime looks like a public-facing deployment.
- Depends on: `app_factory.py`, `utils/utils.py`
- Imported by: `scripts/test_bloque1.py`

## app_factory.py

### _is_production (function) `def _is_production()`
- Defined: `app_factory.py:71`
- Doc: Return True unless the operator explicitly opts into dev mode.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`

### _build_csp (function) `def _build_csp()`
- Defined: `app_factory.py:82`
- Doc: Return the strict Content-Security-Policy used in production.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`

### _build_talisman_kwargs (function) `def _build_talisman_kwargs()`
- Defined: `app_factory.py:119`
- Doc: Return kwargs to pass to ``Talisman`` based on the runtime env.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`

### _configure_secret_key (function) `def _configure_secret_key(app, config)`
- Defined: `app_factory.py:160`
- Doc: Set ``app.config['SECRET_KEY']`` from env, payload.json, or a random value.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`

### _configure_session (function) `def _configure_session(app)`
- Defined: `app_factory.py:203`
- Doc: Apply session lifetime and cookie hardening.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`

### _configure_logging (function) `def _configure_logging(app)`
- Defined: `app_factory.py:220`
- Doc: Wire up a structured application logger.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`

### create_app (function) `def create_app(config_overrides, security_overrides)`
- Defined: `app_factory.py:237`
- Doc: Build and return a fully-configured Flask application.
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`

### load_user (function) `def load_user(user_id)`
- Defined: `app_factory.py:416`
- Depends on: `controllers/file.py`, `controllers/sync.py`, `models/user.py`, `utils/integrity.py`, `utils/utils.py`, `views/about.py`, `views/account.py`, `views/admin.py`, `views/auth.py`, `views/facade.py`, `views/faq.py`, `views/file.py`, `views/message.py`, `views/privacy.py`, `views/subscription.py`, `views/sync.py`, `views/terms.py`, `views/views.py`
- Imported by: `app.py`, `tests/conftest.py`, `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `wsgi.py`

## client.go

### main (function) `func main(`
- Defined: `client.go:13`

## controllers/auth.py

### _now_utc (function) `def _now_utc()`
- Defined: `controllers/auth.py:49`
- Doc: Return the current time as a timezone-aware UTC datetime.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### __init__ (method) `def __init__(self, db_path, mail, storage_uri)`
- Defined: `controllers/auth.py:61`
- Doc: Initialize the controller.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### register (method) `def register(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, recovery_salt, encrypted_private_key_recovery)`
- Defined: `controllers/auth.py:76`
- Doc: Register a user from client-generated zero-knowledge credentials.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### send_confirmation_email (method) `def send_confirmation_email(self, email, username, token)`
- Defined: `controllers/auth.py:156`
- Doc: Email the account-confirmation link to a freshly registered user.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### srp_hello (method) `def srp_hello(self, username, client_a_hex)`
- Defined: `controllers/auth.py:202`
- Doc: Begin an SRP-6a login and return the salt and server challenge B.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### srp_verify (method) `def srp_verify(self, username, client_m1_hex)`
- Defined: `controllers/auth.py:221`
- Doc: Complete an SRP-6a login and return the authenticated user and proof.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### send_sms_verification (method) `def send_sms_verification(self, phone, code, username)`
- Defined: `controllers/auth.py:253`
- Doc: Send a verification code via SMS.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### verify_phone_code (method) `def verify_phone_code(self, username, code)`
- Defined: `controllers/auth.py:274`
- Doc: Verify a phone verification code for a user.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### resend_phone_code (method) `def resend_phone_code(self, username)`
- Defined: `controllers/auth.py:310`
- Doc: Issue and send a fresh phone verification code.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### _is_code_valid (method) `def _is_code_valid(self, expires_at)`
- Defined: `controllers/auth.py:349`
- Doc: Return True if a verification code has not yet expired.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### verify_mfa_code (method) `def verify_mfa_code(self, username, code)`
- Defined: `controllers/auth.py:369`
- Doc: Verify a multi-factor authentication code for a user.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### send_mfa_code (method) `def send_mfa_code(self, username)`
- Defined: `controllers/auth.py:393`
- Doc: Generate, store, and send an MFA code to the user's phone.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

### toggle_mfa (method) `def toggle_mfa(self, username, enable)`
- Defined: `controllers/auth.py:416`
- Doc: Enable or disable MFA for a user.
- Depends on: `models/plans.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `views/auth.py`

## controllers/contact.py

### __init__ (method) `def __init__(self, db_path)`
- Defined: `controllers/contact.py:6`
- Doc: Initialize the ContactController with the database path.
- Depends on: `models/contact.py`
- Imported by: `views/admin.py`, `views/auth.py`

### create_contact (method) `def create_contact(self, user_id, subject, message)`
- Defined: `controllers/contact.py:14`
- Doc: Create a new contact message.
- Depends on: `models/contact.py`
- Imported by: `views/admin.py`, `views/auth.py`

### get_user_contacts (method) `def get_user_contacts(self, user_id)`
- Defined: `controllers/contact.py:36`
- Doc: Retrieve all contact messages for a user.
- Depends on: `models/contact.py`
- Imported by: `views/admin.py`, `views/auth.py`

## controllers/deniable_vault.py

### _base64_length (function) `def _base64_length(byte_length)`
- Defined: `controllers/deniable_vault.py:81`
- Doc: Return the length of the standard base64 encoding of ``byte_length`` bytes.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### canonical_json (function) `def canonical_json(envelope)`
- Defined: `controllers/deniable_vault.py:86`
- Doc: Serialize an envelope deterministically for storage and sizing.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### _coerce_int (method) `def _coerce_int(value, default)`
- Defined: `controllers/deniable_vault.py:108`
- Doc: Return ``value`` coerced to int, falling back to ``default``.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### _coerce_kdf (method) `def _coerce_kdf(value, default)`
- Defined: `controllers/deniable_vault.py:118`
- Doc: Return an allow-list of KDF identifiers from a value.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### from_mapping (method) `def from_mapping(cls, mapping, env)`
- Defined: `controllers/deniable_vault.py:148`
- Doc: Build a config from a mapping, with environment overrides.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### expected_ct_b64_length (method) `def expected_ct_b64_length(self)`
- Defined: `controllers/deniable_vault.py:213`
- Doc: Return the exact base64 length every slot ciphertext must have.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### random_container (method) `def random_container(self)`
- Defined: `controllers/deniable_vault.py:222`
- Doc: Return a well-formed container filled with random, unopenable data.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### public_parameters (method) `def public_parameters(self)`
- Defined: `controllers/deniable_vault.py:250`
- Doc: Return the parameters the browser needs to build a container.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### __init__ (method) `def __init__(self, config)`
- Defined: `controllers/deniable_vault.py:281`
- Doc: Bind the validator to a configuration.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### validate (method) `def validate(self, envelope)`
- Defined: `controllers/deniable_vault.py:285`
- Doc: Validate ``envelope``, raising on the first violation.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### _validate_slot (method) `def _validate_slot(self, index, slot)`
- Defined: `controllers/deniable_vault.py:339`
- Doc: Validate a single slot.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### _validate_hex (method) `def _validate_hex(value, expected_length, index, field)`
- Defined: `controllers/deniable_vault.py:376`
- Doc: Validate that ``value`` is hex of exactly ``expected_length``.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### __init__ (method) `def __init__(self, db, config, validator)`
- Defined: `controllers/deniable_vault.py:401`
- Doc: Initialize the controller.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### load_or_provision (method) `def load_or_provision(self, username)`
- Defined: `controllers/deniable_vault.py:419`
- Doc: Return ``username``'s container, minting a random one if absent.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### save (method) `def save(self, username, envelope)`
- Defined: `controllers/deniable_vault.py:441`
- Doc: Validate and persist a container for ``username``.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### reset (method) `def reset(self, username)`
- Defined: `controllers/deniable_vault.py:456`
- Doc: Overwrite ``username``'s container with a fresh random one.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### exists (method) `def exists(self, username)`
- Defined: `controllers/deniable_vault.py:474`
- Doc: Return True if ``username`` already has a stored container.
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

### read (method) `def read(key)`
- Defined: `controllers/deniable_vault.py:171`
- Depends on: `models/deniable_vault.py`, `utils/security.py`
- Imported by: `tests/test_deniable_vault.py`, `views/account.py`

## controllers/facade.py

### _as_bool (method) `def _as_bool(value, default)`
- Defined: `controllers/facade.py:79`
- Doc: Coerce an environment or mapping value to a boolean.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### _as_int (method) `def _as_int(value, default)`
- Defined: `controllers/facade.py:88`
- Doc: Coerce an environment or mapping value to an integer.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### _as_text (method) `def _as_text(value, default)`
- Defined: `controllers/facade.py:98`
- Doc: Coerce a value to non-empty text, falling back to ``default``.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### _as_raw_text (method) `def _as_raw_text(value, default)`
- Defined: `controllers/facade.py:106`
- Doc: Coerce a value to text without substituting an empty default.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### _as_paths (method) `def _as_paths(value, default)`
- Defined: `controllers/facade.py:111`
- Doc: Parse a comma-separated path list into a tuple of stripped paths.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### gate_configured (method) `def gate_configured(self)`
- Defined: `controllers/facade.py:154`
- Doc: Return whether the facade is enabled and holds a real gate hash.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### cover_context (method) `def cover_context(self)`
- Defined: `controllers/facade.py:158`
- Doc: Return the cosmetic cover context, never carrying a gate hash.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### cover_variables (method) `def cover_variables(self)`
- Defined: `controllers/facade.py:166`
- Doc: Return the sanitizable cover variable payload.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### from_mapping (method) `def from_mapping(cls, mapping, env)`
- Defined: `controllers/facade.py:181`
- Doc: Resolve configuration with environment, mapping, then default order.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### __init__ (method) `def __init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)`
- Defined: `controllers/facade.py:265`
- Doc: Bind the hasher to explicit Argon2id cost parameters.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### hash (method) `def hash(self, phrase)`
- Defined: `controllers/facade.py:282`
- Doc: Return a salted Argon2id digest of ``phrase``.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### verify (method) `def verify(self, phrase, encoded)`
- Defined: `controllers/facade.py:286`
- Doc: Return whether ``phrase`` matches ``encoded`` without raising.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### from_config (method) `def from_config(cls, config)`
- Defined: `controllers/facade.py:296`
- Doc: Build a hasher using the cost parameters of ``config``.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### __init__ (method) `def __init__(self, secret_key, ttl_seconds)`
- Defined: `controllers/facade.py:308`
- Doc: Bind the ticket signer to the app secret and a lifetime.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### issue (method) `def issue(self, mode)`
- Defined: `controllers/facade.py:316`
- Doc: Return a signed ticket for ``mode`` or raise for an unknown mode.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### verify (method) `def verify(self, token)`
- Defined: `controllers/facade.py:322`
- Doc: Return the ticket mode, or ``None`` if expired, tampered, or absent.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### __init__ (method) `def __init__(self, config, hasher, ticket)`
- Defined: `controllers/facade.py:339`
- Doc: Bind the gate to its configuration and collaborators.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### build (method) `def build(cls, config, secret_key)`
- Defined: `controllers/facade.py:351`
- Doc: Build a gate from configuration and the application secret.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### evaluate (method) `def evaluate(self, phrase)`
- Defined: `controllers/facade.py:359`
- Doc: Classify a phrase and emit only a generic audit event.
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

### read (method) `def read(key)`
- Defined: `controllers/facade.py:189`
- Depends on: `utils/security.py`
- Imported by: `tests/test_account_facade.py`, `tests/test_cover.py`, `tests/test_facade.py`, `views/account.py`, `views/facade.py`

## controllers/file.py

### _log_s3_error (function) `def _log_s3_error(operation, error)`
- Defined: `controllers/file.py:28`
- Doc: Log a failed S3 operation without raising further.
- Depends on: `utils/padding.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `tests/test_padding.py`

### safe_filename (function) `def safe_filename(name)`
- Defined: `controllers/file.py:33`
- Doc: Return a filename safe to embed in an S3 key.
- Depends on: `utils/padding.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `tests/test_padding.py`

### __init__ (method) `def __init__(self, users_path, s3_bucket, s3_client)`
- Defined: `controllers/file.py:54`
- Depends on: `utils/padding.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `tests/test_padding.py`

### _key (method) `def _key(self, username, filename, suffix)`
- Defined: `controllers/file.py:59`
- Doc: Build the S3 key for a user's encrypted file or FEK.
- Depends on: `utils/padding.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `tests/test_padding.py`

### get_storage_usage (method) `def get_storage_usage(self, username)`
- Defined: `controllers/file.py:71`
- Doc: Sum the bytes used by ``username``'s encrypted files in S3.
- Depends on: `utils/padding.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `tests/test_padding.py`

### upload_encrypted_file (method) `def upload_encrypted_file(self, username, file_storage, wrapped_fek)`
- Defined: `controllers/file.py:85`
- Doc: Persist an already-encrypted file and its wrapped FEK to S3.
- Depends on: `utils/padding.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `tests/test_padding.py`

### get_encrypted_file_and_key (method) `def get_encrypted_file_and_key(self, username, filename)`
- Defined: `controllers/file.py:118`
- Doc: Fetch a user's encrypted file and its wrapped FEK from S3.
- Depends on: `utils/padding.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `tests/test_padding.py`

### list_encrypted_files (method) `def list_encrypted_files(self, username)`
- Defined: `controllers/file.py:148`
- Doc: List the encrypted files that belong to ``username``.
- Depends on: `utils/padding.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `tests/test_padding.py`

## controllers/message.py

### __init__ (method) `def __init__(self, users_path, users_db_path)`
- Defined: `controllers/message.py:22`
- Doc: Initialize the controller.
- Depends on: `models/message.py`, `models/user.py`, `utils/padding.py`, `utils/utils.py`
- Imported by: `tests/test_padding.py`, `views/message.py`

### send_encrypted_message (method) `def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_for_recipient, cek_for_sender)`
- Defined: `controllers/message.py:36`
- Doc: Persist an opaque message envelope for the recipient.
- Depends on: `models/message.py`, `models/user.py`, `utils/padding.py`, `utils/utils.py`
- Imported by: `tests/test_padding.py`, `views/message.py`

### get_messages (method) `def get_messages(self, username, page, per_page)`
- Defined: `controllers/message.py:90`
- Doc: Return opaque message envelopes for the user.
- Depends on: `models/message.py`, `models/user.py`, `utils/padding.py`, `utils/utils.py`
- Imported by: `tests/test_padding.py`, `views/message.py`

## controllers/secure_channel.py

### is_cloudflare_url (method) `def is_cloudflare_url(value)`
- Defined: `controllers/secure_channel.py:82`
- Doc: Return whether value is a quick-tunnel HTTPS URL.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### is_onion_url (method) `def is_onion_url(value)`
- Defined: `controllers/secure_channel.py:89`
- Doc: Return whether value is a v3 onion HTTP address.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _as_port (method) `def _as_port(value, default)`
- Defined: `controllers/secure_channel.py:96`
- Doc: Coerce input to a TCP port, falling back on default.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _as_scheme (method) `def _as_scheme(value, default)`
- Defined: `controllers/secure_channel.py:107`
- Doc: Coerce input to an origin scheme, accepting http or https only.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _default_launcher (method) `def _default_launcher(cmd, log_path)`
- Defined: `controllers/secure_channel.py:193`
- Doc: Spawn a backend daemon detached from the web worker.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _default_killer (method) `def _default_killer(pid)`
- Defined: `controllers/secure_channel.py:207`
- Doc: Terminate one tracked backend process group.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _fingerprint (method) `def _fingerprint(value)`
- Defined: `controllers/secure_channel.py:503`
- Doc: Return a short non-reversible fingerprint for audit records.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _normalize_onion (method) `def _normalize_onion(raw)`
- Defined: `controllers/secure_channel.py:509`
- Doc: Normalize a Tor hostname file payload to a full onion URL.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _wait_for_pattern (method) `def _wait_for_pattern(path, pattern, timeout_seconds)`
- Defined: `controllers/secure_channel.py:517`
- Doc: Poll a log file for the first regex match within a timeout.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _wait_for_file (method) `def _wait_for_file(path, timeout_seconds)`
- Defined: `controllers/secure_channel.py:535`
- Doc: Poll for a small text file such as the onion hostname file.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### parse (method) `def parse(cls, raw)`
- Defined: `controllers/secure_channel.py:74`
- Doc: Parse free-form input into a mode, defaulting to disabled.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### configured (method) `def configured(self)`
- Defined: `controllers/secure_channel.py:129`
- Doc: Return whether a disposible channel mode is selected.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### from_mapping (method) `def from_mapping(cls, mapping, env)`
- Defined: `controllers/secure_channel.py:134`
- Doc: Resolve configuration with environment, mapping, then default order.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### active (method) `def active(self)`
- Defined: `controllers/secure_channel.py:184`
- Doc: Return whether any backend address is currently published.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### __init__ (method) `def __init__(self, state_dir, local_port, local_scheme, cloudflared_bin, tor_bin, start_timeout_seconds, launcher, killer)`
- Defined: `controllers/secure_channel.py:223`
- Doc: Bind the manager to a state directory and backend binaries.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### origin_url (method) `def origin_url(self)`
- Defined: `controllers/secure_channel.py:247`
- Doc: Return the loopback origin URL both backends forward to.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### from_config (method) `def from_config(cls, config, launcher, killer)`
- Defined: `controllers/secure_channel.py:252`
- Doc: Build a manager sharing binary paths and ports with config.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### status (method) `def status(self)`
- Defined: `controllers/secure_channel.py:270`
- Doc: Return live status, pruning dead pids without side effects.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### start (method) `def start(self, mode)`
- Defined: `controllers/secure_channel.py:281`
- Doc: Start backends for mode, replacing any running channel.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### stop (method) `def stop(self)`
- Defined: `controllers/secure_channel.py:301`
- Doc: Terminate tracked backends and remove persisted state.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### rotate (method) `def rotate(self)`
- Defined: `controllers/secure_channel.py:314`
- Doc: Dispose current addresses and start the same mode again.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### audit_details (method) `def audit_details(self, action, mode, cloud_url, onion_url)`
- Defined: `controllers/secure_channel.py:321`
- Doc: Return an audit-safe detail string without full addresses.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _status_for (method) `def _status_for(self, mode, cloud_url, onion_url, pids)`
- Defined: `controllers/secure_channel.py:337`
- Doc: Build a status after validating backend address shapes.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _state_path (method) `def _state_path(self)`
- Defined: `controllers/secure_channel.py:352`
- Doc: Return the persisted state file path.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _read_state (method) `def _read_state(self)`
- Defined: `controllers/secure_channel.py:356`
- Doc: Load persisted state, returning None when absent or corrupt.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _write_state (method) `def _write_state(self, current)`
- Defined: `controllers/secure_channel.py:371`
- Doc: Persist state atomically with owner-only permissions.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _remove_state (method) `def _remove_state(self)`
- Defined: `controllers/secure_channel.py:396`
- Doc: Remove persisted state when present.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _cleanup_scratch (method) `def _cleanup_scratch(self)`
- Defined: `controllers/secure_channel.py:405`
- Doc: Remove stale per-boot scratch directories left by Tor.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _start_cloudflared (method) `def _start_cloudflared(self)`
- Defined: `controllers/secure_channel.py:418`
- Doc: Launch a disposable quick tunnel and parse its public URL.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _start_tor (method) `def _start_tor(self)`
- Defined: `controllers/secure_channel.py:438`
- Doc: Launch an unprivileged disposable onion service.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _resolve_binary (method) `def _resolve_binary(self, binary)`
- Defined: `controllers/secure_channel.py:471`
- Doc: Resolve a backend binary without trusting PATH alone.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### _pid_live (method) `def _pid_live(self, pid)`
- Defined: `controllers/secure_channel.py:488`
- Doc: Return whether a tracked pid still exists.
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

### read (method) `def read(key)`
- Defined: `controllers/secure_channel.py:142`
- Imported by: `tests/test_secure_channel.py`, `views/admin.py`

## controllers/sync.py

### __init__ (method) `def __init__(self, users_path, s3_bucket, s3_client, file_controller)`
- Defined: `controllers/sync.py:8`
- Imported by: `app_factory.py`

### get_storage_usage (method) `def get_storage_usage(self, username)`
- Defined: `controllers/sync.py:14`
- Doc: Calcula el uso de almacenamiento del usuario en S3.
- Imported by: `app_factory.py`

## enc_dec.go

### deriveAESKey (function) `func deriveAESKey(`
- Defined: `enc_dec.go:20`

### encryptFile (function) `func encryptFile(`
- Defined: `enc_dec.go:24`

### decryptFile (function) `func decryptFile(`
- Defined: `enc_dec.go:45`

### main (function) `func main(`
- Defined: `enc_dec.go:69`

## enc_dec.py

### derive_aes_key (function) `def derive_aes_key(shared_secret)`
- Defined: `enc_dec.py:36`
- Doc: Derive a 32-byte AES key from an ML-KEM shared secret.

### encrypt_file_in_memory (function) `def encrypt_file_in_memory(data, aes_key)`
- Defined: `enc_dec.py:49`
- Doc: Encrypt ``data`` in memory with AES-256-GCM and return nonce + ciphertext.

### decrypt_file_in_memory (function) `def decrypt_file_in_memory(nonce, ciphertext, aes_key)`
- Defined: `enc_dec.py:65`
- Doc: Decrypt ``ciphertext`` in memory with AES-256-GCM and return the plaintext.

### _build_s3_client (function) `def _build_s3_client(region)`
- Defined: `enc_dec.py:81`
- Doc: Build a boto3 S3 client honoring the zero-trust environment convention.

### main (function) `def main()`
- Defined: `enc_dec.py:103`
- Doc: Run the offline admin CLI (encrypt or decrypt a single object).

## models/contact.py

### __init__ (method) `def __init__(self, db_path)`
- Defined: `models/contact.py:29`
- Doc: Initialize the ContactDB with the database path.
- Imported by: `controllers/contact.py`

### _init_db (method) `def _init_db(self)`
- Defined: `models/contact.py:38`
- Doc: Initialize the contacts table with all required fields.
- Imported by: `controllers/contact.py`

### create_contact (method) `def create_contact(self, user_id, subject, message)`
- Defined: `models/contact.py:52`
- Doc: Create a new contact message.
- Imported by: `controllers/contact.py`

### get_user_contacts (method) `def get_user_contacts(self, user_id)`
- Defined: `models/contact.py:89`
- Doc: Retrieve all contact messages for a user.
- Imported by: `controllers/contact.py`

### _convert_row_to_dict (method) `def _convert_row_to_dict(self, row)`
- Defined: `models/contact.py:115`
- Doc: Convert an SQLite row to a dictionary.
- Imported by: `controllers/contact.py`

### get_all_contacts (method) `def get_all_contacts(self, page, per_page)`
- Defined: `models/contact.py:139`
- Doc: Retrieve all contact messages with pagination.
- Imported by: `controllers/contact.py`

### _convert_row_to_dict_with_username (method) `def _convert_row_to_dict_with_username(self, row)`
- Defined: `models/contact.py:168`
- Doc: Convert an SQLite row to a dictionary, including username.
- Imported by: `controllers/contact.py`

## models/deniable_vault.py

### __init__ (method) `def __init__(self, db_path)`
- Defined: `models/deniable_vault.py:33`
- Doc: Initialize the store and ensure its table exists.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

### _init_db (method) `def _init_db(self)`
- Defined: `models/deniable_vault.py:43`
- Doc: Create the ``deniable_vaults`` table on first use.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

### upsert (method) `def upsert(self, username, envelope)`
- Defined: `models/deniable_vault.py:57`
- Doc: Insert or replace the container for ``username``.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

### get (method) `def get(self, username)`
- Defined: `models/deniable_vault.py:82`
- Doc: Return the stored container for ``username``, or ``None``.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

### exists (method) `def exists(self, username)`
- Defined: `models/deniable_vault.py:101`
- Doc: Return True if ``username`` has a stored container.
- Imported by: `controllers/deniable_vault.py`, `tests/test_deniable_vault.py`, `views/account.py`

## models/message.py

### __init__ (method) `def __init__(self, base_path)`
- Defined: `models/message.py:46`
- Doc: Initialize the MessageDB with the base directory for per-user mailboxes.
- Imported by: `controllers/message.py`, `utils/scheduler.py`

### save_message (method) `def save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipient, cek_for_sender, message_id)`
- Defined: `models/message.py:55`
- Doc: Persist an opaque message envelope for the recipient.
- Imported by: `controllers/message.py`, `utils/scheduler.py`

### get_messages (method) `def get_messages(self, recipient, page, per_page)`
- Defined: `models/message.py:87`
- Doc: Return opaque message envelopes for the recipient.
- Imported by: `controllers/message.py`, `utils/scheduler.py`

### delete_old_messages (method) `def delete_old_messages(self, recipient, days)`
- Defined: `models/message.py:172`
- Doc: Delete messages older than ``days`` days from the recipient's mailbox.
- Imported by: `controllers/message.py`, `utils/scheduler.py`

## models/plans.py

### __init__ (method) `def __init__(self, db_path)`
- Defined: `models/plans.py:6`
- Doc: Initialize the PlanDB with the database path.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### _init_db (method) `def _init_db(self)`
- Defined: `models/plans.py:15`
- Doc: Initialize the plans table with required fields.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### get_plan (method) `def get_plan(self, plan_name)`
- Defined: `models/plans.py:37`
- Doc: Retrieve a plan by name.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### get_all_plans (method) `def get_all_plans(self)`
- Defined: `models/plans.py:50`
- Doc: Retrieve all plans.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### create_plan (method) `def create_plan(self, name, storage_quota, trial_days, price)`
- Defined: `models/plans.py:60`
- Doc: Create a new plan.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### update_plan (method) `def update_plan(self, name, storage_quota, trial_days, price)`
- Defined: `models/plans.py:78`
- Doc: Update an existing plan.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### delete_plan (method) `def delete_plan(self, name)`
- Defined: `models/plans.py:113`
- Doc: Delete a plan by name.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### _convert_row_to_dict (method) `def _convert_row_to_dict(self, row)`
- Defined: `models/plans.py:127`
- Doc: Convert an SQLite row to a dictionary.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

### validate_plan_payment (method) `def validate_plan_payment(self, plan_name, amount_paid)`
- Defined: `models/plans.py:139`
- Doc: Validate that the paid amount matches the plan price.
- Imported by: `controllers/auth.py`, `views/admin.py`, `views/faq.py`, `views/subscription.py`

## models/superadmin_audit.py

### __init__ (method) `def __init__(self, db_path)`
- Defined: `models/superadmin_audit.py:35`
- Doc: Initialize the audit log and ensure its table exists.
- Imported by: `views/admin.py`

### _init_db (method) `def _init_db(self)`
- Defined: `models/superadmin_audit.py:45`
- Doc: Create the audit table on first use; no-op if it already exists.
- Imported by: `views/admin.py`

### record (method) `def record(self, actor, action, target_user, ip, details)`
- Defined: `models/superadmin_audit.py:75`
- Doc: Append one audit row and return its id.
- Imported by: `views/admin.py`

### recent (method) `def recent(self, limit)`
- Defined: `models/superadmin_audit.py:119`
- Doc: Return the most recent ``limit`` audit rows, newest first.
- Imported by: `views/admin.py`

## models/user.py

### get_id (method) `def get_id(self)`
- Defined: `models/user.py:52`
- Doc: Return the user ID as a string (required by Flask-Login).
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### is_active (method) `def is_active(self)`
- Defined: `models/user.py:70`
- Doc: Return True while the user can use the application.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### __init__ (method) `def __init__(self, db_path)`
- Defined: `models/user.py:85`
- Doc: Initialize the UserDB with the database path.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _init_db (method) `def _init_db(self)`
- Defined: `models/user.py:105`
- Doc: Initialize the users table with all fields for zero-knowledge auth.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _has_phone_unique_constraint (method) `def _has_phone_unique_constraint(self)`
- Defined: `models/user.py:193`
- Doc: Return True if the ``users.phone`` column is UNIQUE.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _drop_phone_unique_if_present (method) `def _drop_phone_unique_if_present(self)`
- Defined: `models/user.py:214`
- Doc: Remove the UNIQUE constraint on ``users.phone``.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _migrate_from_v7 (method) `def _migrate_from_v7(self, legacy_columns)`
- Defined: `models/user.py:271`
- Doc: Rebuild the users table to drop legacy v7 NOT NULL KEM columns.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### create_user (method) `def create_user(self, username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt, email, phone, first_name, last_name, role, storage_quota, trial_start, trial_end, subscription_status, email_verified, confirmation_token, phone_verified, phone_verification_code_hash, phone_code_expires, mfa_enabled, recovery_salt, encrypted_private_key_recovery)`
- Defined: `models/user.py:325`
- Doc: Persist a new user from client-provided zero-knowledge credentials.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### update_user_phone_status (method) `def update_user_phone_status(self, username, phone_verified, phone_verification_code_hash, phone_code_expires)`
- Defined: `models/user.py:362`
- Doc: Update phone verification status and related fields.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### update_user_mfa_status (method) `def update_user_mfa_status(self, username, mfa_code_hash, mfa_code_expires, mfa_enabled)`
- Defined: `models/user.py:396`
- Doc: Update MFA code, expiration, and enabled status.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### update_user (method) `def update_user(self, username, email_verified, confirmation_token)`
- Defined: `models/user.py:430`
- Doc: Update specific user fields.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user (method) `def get_user(self, username)`
- Defined: `models/user.py:454`
- Doc: Retrieve a user by username.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user_by_id (method) `def get_user_by_id(self, user_id)`
- Defined: `models/user.py:468`
- Doc: Retrieve a user by ID.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user_by_email (method) `def get_user_by_email(self, email)`
- Defined: `models/user.py:482`
- Doc: Retrieve a user by email address.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user_by_phone (method) `def get_user_by_phone(self, phone)`
- Defined: `models/user.py:496`
- Doc: Retrieve a user by phone number.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_user_by_confirmation_token (method) `def get_user_by_confirmation_token(self, token)`
- Defined: `models/user.py:510`
- Doc: Retrieve a user by confirmation token.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_recovery_bundle (method) `def get_recovery_bundle(self, username)`
- Defined: `models/user.py:524`
- Doc: Return the QV-RECOVERY-1 bundle for a username, if one exists.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### reset_credentials_with_recovery (method) `def reset_credentials_with_recovery(self, username, srp_salt, srp_verifier, kdf_salt, encrypted_private_key)`
- Defined: `models/user.py:548`
- Doc: Replace a user's password-derived credentials after a verified recovery.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### update_role (method) `def update_role(self, username, role, storage_quota, subscription_status)`
- Defined: `models/user.py:579`
- Doc: Update a user's role, storage quota, and subscription status.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### count_users (method) `def count_users(self)`
- Defined: `models/user.py:592`
- Doc: Return the total number of users.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### get_all_users (method) `def get_all_users(self)`
- Defined: `models/user.py:603`
- Doc: Retrieve all users.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _parse_datetime (method) `def _parse_datetime(value)`
- Defined: `models/user.py:615`
- Doc: Parse a stored timestamp into a datetime, tolerating the format.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### _convert_row_to_dict (method) `def _convert_row_to_dict(self, row)`
- Defined: `models/user.py:638`
- Doc: Convert a name-keyed SQLite row into a plain dictionary.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### fetch_one (method) `def fetch_one(self, query, params)`
- Defined: `models/user.py:694`
- Doc: Execute a query and return the first result as a dictionary.
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

### value (method) `def value(name, default)`
- Defined: `models/user.py:655`
- Imported by: `app_factory.py`, `controllers/auth.py`, `controllers/message.py`, `scripts/email_tool.py`, `scripts/makeadmin.py`, `scripts/test_bloque1.py`, `tests/test_account_facade.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `utils/scheduler.py`, `views/admin.py`, `views/auth.py`, `views/subscription.py`, `views/views.py`

## scripts/doctor.py

### load_env_file (method) `def load_env_file(path)`
- Defined: `scripts/doctor.py:128`
- Doc: Parse a dotenv file into a dict without third-party imports.

### effective_env (method) `def effective_env()`
- Defined: `scripts/doctor.py:147`
- Doc: Return process env overlaid with ``.env`` file values.

### check_python (method) `def check_python(minimum)`
- Defined: `scripts/doctor.py:154`
- Doc: Verify the interpreter meets the minimum supported version.

### check_module (method) `def check_module(name)`
- Defined: `scripts/doctor.py:170`
- Doc: Verify one Python module imports cleanly.

### check_binary (method) `def check_binary(name, env_override)`
- Defined: `scripts/doctor.py:186`
- Doc: Verify one system binary resolves via PATH or an override path.

### check_env_file (method) `def check_env_file()`
- Defined: `scripts/doctor.py:210`
- Doc: Verify the operator ``.env`` file exists.

### parse_host_port (method) `def parse_host_port(uri, default_port)`
- Defined: `scripts/doctor.py:223`
- Doc: Extract a TCP host and port from a Redis or HTTP(S) URL.

### check_tcp (method) `def check_tcp(name, host, port, timeout)`
- Defined: `scripts/doctor.py:242`
- Doc: Verify a TCP endpoint accepts connections.

### debian_arch (method) `def debian_arch(deb)`
- Defined: `scripts/doctor.py:261`
- Doc: Map the host CPU to a Cloudflare or Garage release architecture.

### cloudflared_deb_url (method) `def cloudflared_deb_url(version, arch)`
- Defined: `scripts/doctor.py:270`
- Doc: Build the official cloudflared .deb URL for a version and arch.

### garage_bin_url (method) `def garage_bin_url(version, target)`
- Defined: `scripts/doctor.py:283`
- Doc: Build the official garage binary URL for a version and target.

### apt_command (method) `def apt_command(packages)`
- Defined: `scripts/doctor.py:288`
- Doc: Build an apt install command, prefixed with sudo outside root.

### run_command (method) `def run_command(cmd)`
- Defined: `scripts/doctor.py:298`
- Doc: Run one shell command and capture its outcome.

### download_file (method) `def download_file(url, destination)`
- Defined: `scripts/doctor.py:319`
- Doc: Fetch a URL with curl when present, else urllib.

### upsert_env (method) `def upsert_env(key, value, path)`
- Defined: `scripts/doctor.py:334`
- Doc: Set one KEY=value pair in ``.env``, preserving other lines.

### fix_python_deps (method) `def fix_python_deps()`
- Defined: `scripts/doctor.py:352`
- Doc: Install project requirements with the running interpreter.

### fix_apt (method) `def fix_apt(packages)`
- Defined: `scripts/doctor.py:360`
- Doc: Install Debian system packages, using sudo outside root.

### fix_cloudflared (method) `def fix_cloudflared(version, bin_dir)`
- Defined: `scripts/doctor.py:373`
- Doc: Install the cloudflared binary into a user-writable bin directory.

### fix_garage (method) `def fix_garage(version, destination)`
- Defined: `scripts/doctor.py:417`
- Doc: Download the garage binary and verify it against its checksum.

### collect_report (method) `def collect_report()`
- Defined: `scripts/doctor.py:449`
- Doc: Run every check and return the aggregated report.

### print_report (method) `def print_report(report)`
- Defined: `scripts/doctor.py:476`
- Doc: Render the report in plain English for operators.

### apply_fixes (method) `def apply_fixes(report)`
- Defined: `scripts/doctor.py:493`
- Doc: Install every missing piece that has an unattended installer.

### main (method) `def main(argv)`
- Defined: `scripts/doctor.py:530`
- Doc: Entry point for ``make doctor`` and ``make doctor-fix``.

### add (method) `def add(self, result)`
- Defined: `scripts/doctor.py:113`
- Doc: Append one check result.

### failures (method) `def failures(self)`
- Defined: `scripts/doctor.py:118`
- Doc: Return every failing check.

### exit_code (method) `def exit_code(self)`
- Defined: `scripts/doctor.py:123`
- Doc: Return 0 when every check passes, 1 otherwise.

## scripts/email_tool.py

### _build_mail_app (function) `def _build_mail_app(config)`
- Defined: `scripts/email_tool.py:40`
- Doc: Build a minimal Flask app that only carries the mail configuration.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### cmd_test_smtp (function) `def cmd_test_smtp(args)`
- Defined: `scripts/email_tool.py:63`
- Doc: Send a test email through the configured SMTP server.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### cmd_link (function) `def cmd_link(args)`
- Defined: `scripts/email_tool.py:91`
- Doc: Print the confirmation URL for a user without sending email.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### cmd_confirm (function) `def cmd_confirm(args)`
- Defined: `scripts/email_tool.py:114`
- Doc: Mark a user's email as verified directly in the database.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### build_parser (function) `def build_parser()`
- Defined: `scripts/email_tool.py:133`
- Doc: Construct the argument parser for the three subcommands.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

### main (function) `def main()`
- Defined: `scripts/email_tool.py:153`
- Doc: Parse arguments and dispatch to the selected subcommand.
- Depends on: `models/user.py`, `utils/mailer.py`, `utils/utils.py`

## scripts/garage-init.sh

### upsert_env (function)
- Defined: `scripts/garage-init.sh:35`
- Doc: Insert or update a KEY=value line in .env without disturbing other lines.

## scripts/garage-native.sh

### upsert_env (function)
- Defined: `scripts/garage-native.sh:46`
- Doc: Insert or update a KEY=value line in .env without disturbing other lines.

### s3_reachable (function)
- Defined: `scripts/garage-native.sh:56`

### gcmd (function)
- Defined: `scripts/garage-native.sh:141`

## scripts/makeadmin.py

### _resolve_db_path (function) `def _resolve_db_path()`
- Defined: `scripts/makeadmin.py:51`
- Doc: Return the absolute users.db path, anchored at the project root.
- Depends on: `models/user.py`

### _print_user_summary (function) `def _print_user_summary(user)`
- Defined: `scripts/makeadmin.py:64`
- Doc: Print the post-update user record so the operator can eyeball it.
- Depends on: `models/user.py`

### cmd_promote (function) `def cmd_promote(args)`
- Defined: `scripts/makeadmin.py:75`
- Doc: Promote ``args.username`` to the requested role (default: superadmin).
- Depends on: `models/user.py`

### build_parser (function) `def build_parser()`
- Defined: `scripts/makeadmin.py:126`
- Doc: Construct the argument parser for the makeadmin subcommands.
- Depends on: `models/user.py`

### main (function) `def main()`
- Defined: `scripts/makeadmin.py:152`
- Doc: Parse arguments and dispatch to the selected subcommand.
- Depends on: `models/user.py`

## scripts/test_bloque1.py

### _load_user (method) `def _load_user(uid)`
- Defined: `scripts/test_bloque1.py:62`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### check (method) `def check(name, ok, detail)`
- Defined: `scripts/test_bloque1.py:86`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### __init__ (method) `def __init__(self, row)`
- Defined: `scripts/test_bloque1.py:49`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### is_authenticated (method) `def is_authenticated(self)`
- Defined: `scripts/test_bloque1.py:54`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### is_active (method) `def is_active(self)`
- Defined: `scripts/test_bloque1.py:56`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### is_anonymous (method) `def is_anonymous(self)`
- Defined: `scripts/test_bloque1.py:58`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

### get_id (method) `def get_id(self)`
- Defined: `scripts/test_bloque1.py:59`
- Depends on: `app.py`, `models/user.py`, `views/admin.py`

## server.go

### main (function) `func main(`
- Defined: `server.go:11`

### handleConnection (function) `func handleConnection(`
- Defined: `server.go:40`

## static/js/account.js

### setStatus (function)
- Defined: `static/js/account.js:19`
- Depends on: `static/js/qv-deniable.js`

### csrfToken (function)
- Defined: `static/js/account.js:30`
- Depends on: `static/js/qv-deniable.js`

### apiRequest (function)
- Defined: `static/js/account.js:36`
- Depends on: `static/js/qv-deniable.js`

### loadState (function)
- Defined: `static/js/account.js:54`
- Depends on: `static/js/qv-deniable.js`

### collectSlots (function)
- Defined: `static/js/account.js:59`
- Depends on: `static/js/qv-deniable.js`

### handleConfigure (function)
- Defined: `static/js/account.js:73`
- Depends on: `static/js/qv-deniable.js`

### handleOpen (function)
- Defined: `static/js/account.js:103`
- Depends on: `static/js/qv-deniable.js`

### handleReset (function)
- Defined: `static/js/account.js:125`
- Depends on: `static/js/qv-deniable.js`

### init (function)
- Defined: `static/js/account.js:138`
- Depends on: `static/js/qv-deniable.js`

## static/js/coded-text.js

### randomChar (function)
- Defined: `static/js/coded-text.js:12`

### animateElement (function)
- Defined: `static/js/coded-text.js:18`

### init (function)
- Defined: `static/js/coded-text.js:49`

## static/js/login.js

### handleLogin (function)
- Defined: `static/js/login.js:11`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

### init (function)
- Defined: `static/js/login.js:43`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/messages.js

### getCsrfToken (function)
- Defined: `static/js/messages.js:11`
- Depends on: `static/js/qv-crypto.js`

### handleSend (function)
- Defined: `static/js/messages.js:17`
- Depends on: `static/js/qv-crypto.js`

### collectEnvelopes (function)
- Defined: `static/js/messages.js:43`
- Depends on: `static/js/qv-crypto.js`

### handleDecryptInbox (function)
- Defined: `static/js/messages.js:60`
- Depends on: `static/js/qv-crypto.js`

### initEditor (function)
- Defined: `static/js/messages.js:87`
- Depends on: `static/js/qv-crypto.js`

### init (function)
- Defined: `static/js/messages.js:108`
- Depends on: `static/js/qv-crypto.js`

## static/js/qv-crypto.js

### concatBytes (function)
- Defined: `static/js/qv-crypto.js:58`
- Doc: -- Encoding helpers ---
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### hexToBytes (function)
- Defined: `static/js/qv-crypto.js:69`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### bytesToHex (function)
- Defined: `static/js/qv-crypto.js:78`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### bytesToBase64 (function)
- Defined: `static/js/qv-crypto.js:84`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### bytesToBase32 (function)
- Defined: `static/js/qv-crypto.js:95`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### base64ToBytes (function)
- Defined: `static/js/qv-crypto.js:113`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### bytesToBigInt (function)
- Defined: `static/js/qv-crypto.js:120`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### i2osp (function)
- Defined: `static/js/qv-crypto.js:127`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### mod (function)
- Defined: `static/js/qv-crypto.js:137`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### modPow (function)
- Defined: `static/js/qv-crypto.js:141`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### randomBytes (function)
- Defined: `static/js/qv-crypto.js:159`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### H (function)
- Defined: `static/js/qv-crypto.js:168`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### Hint (function)
- Defined: `static/js/qv-crypto.js:172`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### deriveKeyFromPassphrase (function)
- Defined: `static/js/qv-crypto.js:184`
- Doc: Derive a 256-bit key from a passphrase with a caller-chosen PBKDF2 iteration count. This is the single PBKDF2 implementa
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### deriveMasterKey (function)
- Defined: `static/js/qv-crypto.js:205`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### aesGcmEncrypt (function)
- Defined: `static/js/qv-crypto.js:209`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### aesGcmDecrypt (function)
- Defined: `static/js/qv-crypto.js:220`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### computeK (function)
- Defined: `static/js/qv-crypto.js:250`
- Doc: -- SRP-6a (QV-SRP-1), mirrors utils/srp6a.py ---
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### deriveVerifier (function)
- Defined: `static/js/qv-crypto.js:255`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### srpLogin (function)
- Defined: `static/js/qv-crypto.js:263`
- Doc: Run a full SRP-6a login against the server, verifying the server proof M2.
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### generateIdentity (function)
- Defined: `static/js/qv-crypto.js:315`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### parsePublicKey (function)
- Defined: `static/js/qv-crypto.js:343`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### parsePrivateBlob (function)
- Defined: `static/js/qv-crypto.js:351`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### deriveWrapKey (function)
- Defined: `static/js/qv-crypto.js:359`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### wrapKey (function)
- Defined: `static/js/qv-crypto.js:371`
- Doc: Seal a file encryption key to a recipient's hybrid public key.
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### unwrapKey (function)
- Defined: `static/js/qv-crypto.js:395`
- Doc: Recover a file encryption key using the recipient's hybrid private blob.
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### generateRecoveryCode (function)
- Defined: `static/js/qv-crypto.js:417`
- Doc: Generate a QV-RECOVERY-1 code: 20 random bytes (160 bits) Base32-encoded (RFC 4648, no padding) and grouped as XXXX-XXXX
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### normalizeRecoveryCode (function)
- Defined: `static/js/qv-crypto.js:428`
- Doc: Normalize a user-entered recovery code: strip surrounding whitespace, remove group separators, and uppercase, so "abcd-e
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### wrapPrivateKeyForRecovery (function)
- Defined: `static/js/qv-crypto.js:436`
- Doc: Re-wrap an existing privateBlob under a key derived from a recovery code, using the same PBKDF2-SHA256 + AES-256-GCM sch
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### derivePublicKeyFromPrivateBlob (function)
- Defined: `static/js/qv-crypto.js:455`
- Doc: Reconstruct the public key (the same {v, mlkem, x} structure produced by generateIdentity) from a decrypted privateBlob.
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### postJson (function)
- Defined: `static/js/qv-crypto.js:473`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### buildRegistration (function)
- Defined: `static/js/qv-crypto.js:496`
- Doc: Build the zero-knowledge registration payload entirely in the browser.  Returns `{ payload, recoveryCode }`: `payload` i
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### register (function)
- Defined: `static/js/qv-crypto.js:530`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### recoverAccount (function)
- Defined: `static/js/qv-crypto.js:541`
- Doc: Reset SRP credentials and the password-encrypted private key using a QV-RECOVERY-1 recovery code, without ever exposing 
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### login (function)
- Defined: `static/js/qv-crypto.js:592`
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### encryptAndUpload (function)
- Defined: `static/js/qv-crypto.js:599`
- Doc: Generate a fresh file key, encrypt the padded file, wrap the key, and upload. The file plaintext is padded to a fixed fi
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### downloadAndDecrypt (function)
- Defined: `static/js/qv-crypto.js:629`
- Doc: Download an encrypted file and its key, then decrypt it in the browser.
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### fetchPublicKey (function)
- Defined: `static/js/qv-crypto.js:668`
- Doc: Fetch a user's hybrid public key so the browser can wrap content to them.
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### sendSecureMessage (function)
- Defined: `static/js/qv-crypto.js:683`
- Doc: Encrypt a message to a recipient (keeping a sender-readable outbox copy) and POST the opaque envelope. The plaintext and
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

### decryptInbox (function)
- Defined: `static/js/qv-crypto.js:714`
- Doc: Decrypt a batch of inbox envelopes with the user's password. The master key and private blob are derived once and reused
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

## static/js/qv-deniable.js

### toBytes (function)
- Defined: `static/js/qv-deniable.js:47`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### frame (function)
- Defined: `static/js/qv-deniable.js:55`
- Doc: Frame a payload as [len(4) | payload | random padding] of exactly `paddedLength` bytes. `paddedLength` is shared by ever
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### unframe (function)
- Defined: `static/js/qv-deniable.js:64`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### sealSlot (function)
- Defined: `static/js/qv-deniable.js:82`
- Doc: Encrypt one slot's framed plaintext under a passphrase, returning the {salt, nonce, ct} object the envelope stores.
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### openSlot (function)
- Defined: `static/js/qv-deniable.js:102`
- Doc: Attempt to open one slot with a passphrase. Returns the payload bytes on success or null when the passphrase does not au
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### buildDeniableVault (function)
- Defined: `static/js/qv-deniable.js:125`
- Doc: Build a deniable container from a list of slot specifications.  `slots` is an array of `{ passphrase, data }`; `data` ma
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

### openDeniableVault (function)
- Defined: `static/js/qv-deniable.js:170`
- Doc: Open a container with a passphrase. Tries every slot; only the slot whose passphrase matches will authenticate. Returns 
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

## static/js/qv-padding.js

### tableFor (function)
- Defined: `static/js/qv-padding.js:15`
- Depends on: `utils/padding.py`
- Imported by: `static/js/qv-crypto.js`

### bucketFor (function)
- Defined: `static/js/qv-padding.js:20`
- Depends on: `utils/padding.py`
- Imported by: `static/js/qv-crypto.js`

### randomPad (function)
- Defined: `static/js/qv-padding.js:33`
- Depends on: `utils/padding.py`
- Imported by: `static/js/qv-crypto.js`

### padFramed (function)
- Defined: `static/js/qv-padding.js:42`
- Depends on: `utils/padding.py`
- Imported by: `static/js/qv-crypto.js`

### unframeFramed (function)
- Defined: `static/js/qv-padding.js:54`
- Depends on: `utils/padding.py`
- Imported by: `static/js/qv-crypto.js`

## static/js/recover.js

### setStatus (function)
- Defined: `static/js/recover.js:14`
- Depends on: `static/js/qv-crypto.js`

### handleRecover (function)
- Defined: `static/js/recover.js:22`
- Depends on: `static/js/qv-crypto.js`

### init (function)
- Defined: `static/js/recover.js:79`
- Depends on: `static/js/qv-crypto.js`

## static/js/register.js

### showRecoveryCode (function)
- Defined: `static/js/register.js:16`
- Doc: Display the one-time QV-RECOVERY-1 code in a modal and wait for the user to acknowledge they have saved it before contin
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

### handleRegister (function)
- Defined: `static/js/register.js:42`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

### init (function)
- Defined: `static/js/register.js:109`
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/upload.js

### getCsrfToken (function)
- Defined: `static/js/upload.js:11`
- Depends on: `static/js/qv-crypto.js`

### getUsername (function)
- Defined: `static/js/upload.js:16`
- Depends on: `static/js/qv-crypto.js`

### getPublicKey (function)
- Defined: `static/js/upload.js:23`
- Depends on: `static/js/qv-crypto.js`

### handleUpload (function)
- Defined: `static/js/upload.js:40`
- Depends on: `static/js/qv-crypto.js`

### handleDownload (function)
- Defined: `static/js/upload.js:74`
- Depends on: `static/js/qv-crypto.js`

### init (function)
- Defined: `static/js/upload.js:96`
- Depends on: `static/js/qv-crypto.js`

## templates/terms.py

### terms (function) `def terms()`
- Defined: `templates/terms.py:6`
- Doc: Render the About page.

## tests/conftest.py

### _hermetic_env (function) `def _hermetic_env(monkeypatch)`
- Defined: `tests/conftest.py:26`
- Doc: Keep the suite hermetic against the operator's local ``.env`` file.
- Depends on: `app_factory.py`, `utils/security.py`

### _push_request_context (function) `def _push_request_context()`
- Defined: `tests/conftest.py:58`
- Doc: Neutralize pytest-flask's autouse request-context push.
- Depends on: `app_factory.py`, `utils/security.py`

### app (function) `def app(tmp_path)`
- Defined: `tests/conftest.py:76`
- Doc: Return a QuantumVault Flask app configured for testing.
- Depends on: `app_factory.py`, `utils/security.py`

### client (function) `def client(app)`
- Defined: `tests/conftest.py:101`
- Doc: Return a Flask test client for the test app.
- Depends on: `app_factory.py`, `utils/security.py`

### audit_records (method) `def audit_records()`
- Defined: `tests/conftest.py:118`
- Doc: Yield a list that is appended with each ``audit_event`` JSON line.
- Depends on: `app_factory.py`, `utils/security.py`

### __init__ (method) `def __init__(self)`
- Defined: `tests/conftest.py:109`
- Depends on: `app_factory.py`, `utils/security.py`

### emit (method) `def emit(self, record)`
- Defined: `tests/conftest.py:113`
- Depends on: `app_factory.py`, `utils/security.py`

## tests/test_account_facade.py

### fast_hasher (function) `def fast_hasher()`
- Defined: `tests/test_account_facade.py:23`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### _make_user (function) `def _make_user(db_path, username)`
- Defined: `tests/test_account_facade.py:27`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### _authenticated_client (function) `def _authenticated_client(application, db_path)`
- Defined: `tests/test_account_facade.py:55`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### _build (function) `def _build(tmp_path, fast_hasher)`
- Defined: `tests/test_account_facade.py:65`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_facade_enabled_requires_a_deniable_passphrase (function) `def test_facade_enabled_requires_a_deniable_passphrase(tmp_path, fast_hasher)`
- Defined: `tests/test_account_facade.py:88`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_facade_disabled_keeps_it_optional (function) `def test_facade_disabled_keeps_it_optional(tmp_path, fast_hasher)`
- Defined: `tests/test_account_facade.py:99`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

## tests/test_auth_phone.py

### test_verify_phone_page_renders (function) `def test_verify_phone_page_renders(client)`
- Defined: `tests/test_auth_phone.py:18`
- Doc: GET /verify_phone must render without a url_for BuildError.

### test_resend_endpoint_is_registered (function) `def test_resend_endpoint_is_registered(app)`
- Defined: `tests/test_auth_phone.py:25`
- Doc: The resend endpoint the template links to must exist.

### test_resend_route_accepts_only_post (function) `def test_resend_route_accepts_only_post(app)`
- Defined: `tests/test_auth_phone.py:31`
- Doc: The resend endpoint is POST-only so a GET cannot trigger an SMS.

## tests/test_cover.py

### fast_hasher (function) `def fast_hasher()`
- Defined: `tests/test_cover.py:42`
- Depends on: `app_factory.py`, `controllers/facade.py`

### renderer (function) `def renderer()`
- Defined: `tests/test_cover.py:47`
- Depends on: `app_factory.py`, `controllers/facade.py`

### store (function) `def store(tmp_path, renderer)`
- Defined: `tests/test_cover.py:52`
- Depends on: `app_factory.py`, `controllers/facade.py`

### _facade_overrides (function) `def _facade_overrides(fast_hasher)`
- Defined: `tests/test_cover.py:56`
- Depends on: `app_factory.py`, `controllers/facade.py`

### _client (function) `def _client(tmp_path, fast_hasher)`
- Defined: `tests/test_cover.py:68`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_catalog_ships_five_distinct_templates (method) `def test_catalog_ships_five_distinct_templates(self)`
- Defined: `tests/test_cover.py:84`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_default_template_exists (method) `def test_default_template_exists(self)`
- Defined: `tests/test_cover.py:89`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_every_template_validates_and_renders (method) `def test_every_template_validates_and_renders(self, renderer)`
- Defined: `tests/test_cover.py:92`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_empty_payload_fills_defaults (method) `def test_empty_payload_fills_defaults(self)`
- Defined: `tests/test_cover.py:104`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_unknown_variable_is_rejected (method) `def test_unknown_variable_is_rejected(self)`
- Defined: `tests/test_cover.py:109`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_invalid_email_is_rejected (method) `def test_invalid_email_is_rejected(self)`
- Defined: `tests/test_cover.py:113`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_control_characters_are_stripped (method) `def test_control_characters_are_stripped(self)`
- Defined: `tests/test_cover.py:117`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_overlong_value_is_rejected (method) `def test_overlong_value_is_rejected(self)`
- Defined: `tests/test_cover.py:121`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_multiline_body_preserves_line_breaks (method) `def test_multiline_body_preserves_line_breaks(self)`
- Defined: `tests/test_cover.py:125`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_single_line_value_flattens_line_breaks (method) `def test_single_line_value_flattens_line_breaks(self)`
- Defined: `tests/test_cover.py:129`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_multiline_flag_matches_spec (method) `def test_multiline_flag_matches_spec(self, spec)`
- Defined: `tests/test_cover.py:137`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_text_boundary_is_inclusive (method) `def test_text_boundary_is_inclusive(self)`
- Defined: `tests/test_cover.py:144`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_email_boundary_is_inclusive (method) `def test_email_boundary_is_inclusive(self)`
- Defined: `tests/test_cover.py:150`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_variables_are_autoescaped (method) `def test_variables_are_autoescaped(self, renderer)`
- Defined: `tests/test_cover.py:159`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_unknown_variable_is_rejected (method) `def test_unknown_variable_is_rejected(self, renderer)`
- Defined: `tests/test_cover.py:164`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_dunder_access_is_rejected (method) `def test_dunder_access_is_rejected(self, renderer)`
- Defined: `tests/test_cover.py:168`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_inline_script_is_rejected (method) `def test_inline_script_is_rejected(self, renderer)`
- Defined: `tests/test_cover.py:172`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_external_form_action_is_rejected (method) `def test_external_form_action_is_rejected(self, renderer)`
- Defined: `tests/test_cover.py:176`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_template_import_is_rejected (method) `def test_template_import_is_rejected(self, renderer)`
- Defined: `tests/test_cover.py:180`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_blank_source_is_rejected (method) `def test_blank_source_is_rejected(self, renderer)`
- Defined: `tests/test_cover.py:184`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_valid_template_round_trips (method) `def test_valid_template_round_trips(self, store)`
- Defined: `tests/test_cover.py:190`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_bad_extension_is_rejected (method) `def test_bad_extension_is_rejected(self, store)`
- Defined: `tests/test_cover.py:196`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_oversize_template_is_rejected (method) `def test_oversize_template_is_rejected(self, store)`
- Defined: `tests/test_cover.py:200`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_path_traversal_is_neutralized (method) `def test_path_traversal_is_neutralized(self, store)`
- Defined: `tests/test_cover.py:204`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_script_template_is_rejected (method) `def test_script_template_is_rejected(self, store)`
- Defined: `tests/test_cover.py:209`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_missing_template_raises (method) `def test_missing_template_raises(self, store)`
- Defined: `tests/test_cover.py:213`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_non_bytes_payload_is_rejected (method) `def test_non_bytes_payload_is_rejected(self, store)`
- Defined: `tests/test_cover.py:217`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_disallowed_character_filename_is_rejected (method) `def test_disallowed_character_filename_is_rejected(self, store)`
- Defined: `tests/test_cover.py:221`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_exactly_max_size_is_accepted (method) `def test_exactly_max_size_is_accepted(self, store)`
- Defined: `tests/test_cover.py:225`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_nested_directory_is_created (method) `def test_nested_directory_is_created(self, tmp_path, renderer)`
- Defined: `tests/test_cover.py:229`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_two_templates_share_the_store (method) `def test_two_templates_share_the_store(self, store)`
- Defined: `tests/test_cover.py:233`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_directory_with_allowed_suffix_is_ignored (method) `def test_directory_with_allowed_suffix_is_ignored(self, store)`
- Defined: `tests/test_cover.py:238`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_selects_a_builtin_template (method) `def test_selects_a_builtin_template(self, renderer, store)`
- Defined: `tests/test_cover.py:245`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_unknown_template_falls_back_to_default (method) `def test_unknown_template_falls_back_to_default(self, renderer, store)`
- Defined: `tests/test_cover.py:250`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_missing_custom_template_falls_back_to_default (method) `def test_missing_custom_template_falls_back_to_default(self, renderer, store)`
- Defined: `tests/test_cover.py:255`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_custom_template_is_rendered (method) `def test_custom_template_is_rendered(self, renderer, store)`
- Defined: `tests/test_cover.py:260`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_builtin_selection_ignores_a_custom_name (method) `def test_builtin_selection_ignores_a_custom_name(self, renderer, store)`
- Defined: `tests/test_cover.py:267`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_custom_selection_renders_the_custom_marker (method) `def test_custom_selection_renders_the_custom_marker(self, renderer, store)`
- Defined: `tests/test_cover.py:274`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_default_cover_selects_search_portal (method) `def test_default_cover_selects_search_portal(self, tmp_path, fast_hasher)`
- Defined: `tests/test_cover.py:281`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_configured_template_is_served (method) `def test_configured_template_is_served(self, tmp_path, fast_hasher)`
- Defined: `tests/test_cover.py:287`
- Depends on: `app_factory.py`, `controllers/facade.py`

### test_gate_still_works_with_configured_template (method) `def test_gate_still_works_with_configured_template(self, tmp_path, fast_hasher)`
- Defined: `tests/test_cover.py:298`
- Depends on: `app_factory.py`, `controllers/facade.py`

## tests/test_deniable_vault.py

### config (function) `def config()`
- Defined: `tests/test_deniable_vault.py:50`
- Doc: Return the default deniable-vault configuration.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### validator (function) `def validator(config)`
- Defined: `tests/test_deniable_vault.py:56`
- Doc: Return a validator bound to the default configuration.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _ciphertext (function) `def _ciphertext(config, length)`
- Defined: `tests/test_deniable_vault.py:61`
- Doc: Return a base64 ciphertext string of the given (or expected) length.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _valid_envelope (function) `def _valid_envelope(config)`
- Defined: `tests/test_deniable_vault.py:71`
- Doc: Build a structurally valid envelope for ``config``.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _make_user (function) `def _make_user(app, username, role)`
- Defined: `tests/test_deniable_vault.py:91`
- Doc: Create a minimal user row in the test database and return it.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _login (function) `def _login(client, app, username, role)`
- Defined: `tests/test_deniable_vault.py:120`
- Doc: Create and authenticate a user on ``client``'s session.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _csrf (function) `def _csrf(client)`
- Defined: `tests/test_deniable_vault.py:130`
- Doc: Fetch a CSRF token bound to the client's session.
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_defaults_are_self_consistent (method) `def test_defaults_are_self_consistent(self)`
- Defined: `tests/test_deniable_vault.py:141`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_expected_ct_length_matches_base64_formula (method) `def test_expected_ct_length_matches_base64_formula(self, config)`
- Defined: `tests/test_deniable_vault.py:150`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_mapping_overrides_defaults (method) `def test_mapping_overrides_defaults(self)`
- Defined: `tests/test_deniable_vault.py:154`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_environment_overrides_mapping (method) `def test_environment_overrides_mapping(self, monkeypatch)`
- Defined: `tests/test_deniable_vault.py:161`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_allowed_kdf_csv_is_parsed (method) `def test_allowed_kdf_csv_is_parsed(self, monkeypatch)`
- Defined: `tests/test_deniable_vault.py:166`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_public_parameters_round_trip_to_json (method) `def test_public_parameters_round_trip_to_json(self, config)`
- Defined: `tests/test_deniable_vault.py:172`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_accepts_a_well_formed_envelope (method) `def test_accepts_a_well_formed_envelope(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:186`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_non_dict (method) `def test_rejects_non_dict(self, validator)`
- Defined: `tests/test_deniable_vault.py:189`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_wrong_schema_version (method) `def test_rejects_wrong_schema_version(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:194`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_unknown_kdf (method) `def test_rejects_unknown_kdf(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:200`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_iterations_below_minimum (method) `def test_rejects_iterations_below_minimum(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:206`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_iterations_above_maximum (method) `def test_rejects_iterations_above_maximum(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:212`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_wrong_slot_count (method) `def test_rejects_wrong_slot_count(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:218`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_bad_salt_length (method) `def test_rejects_bad_salt_length(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:224`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_non_hex_salt (method) `def test_rejects_non_hex_salt(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:230`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_bad_nonce_length (method) `def test_rejects_bad_nonce_length(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:236`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_ciphertext_of_wrong_length (method) `def test_rejects_ciphertext_of_wrong_length(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:242`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_unequal_slot_ciphertext_lengths (method) `def test_rejects_unequal_slot_ciphertext_lengths(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:248`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_invalid_base64_ciphertext (method) `def test_rejects_invalid_base64_ciphertext(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:254`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_rejects_missing_slot_keys (method) `def test_rejects_missing_slot_keys(self, validator, config)`
- Defined: `tests/test_deniable_vault.py:260`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_random_container_passes_validation (method) `def test_random_container_passes_validation(self, config, validator)`
- Defined: `tests/test_deniable_vault.py:273`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_random_containers_differ (method) `def test_random_containers_differ(self, config)`
- Defined: `tests/test_deniable_vault.py:276`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_random_container_has_fixed_shape (method) `def test_random_container_has_fixed_shape(self, config)`
- Defined: `tests/test_deniable_vault.py:281`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_upsert_then_get_round_trips_verbatim (method) `def test_upsert_then_get_round_trips_verbatim(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:294`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_upsert_replaces_existing_row (method) `def test_upsert_replaces_existing_row(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:303`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_get_missing_returns_none (method) `def test_get_missing_returns_none(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:309`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_exists (method) `def test_exists(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:313`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### _controller (method) `def _controller(self, tmp_path)`
- Defined: `tests/test_deniable_vault.py:326`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_load_or_provision_mints_when_absent (method) `def test_load_or_provision_mints_when_absent(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:331`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_load_or_provision_is_stable (method) `def test_load_or_provision_is_stable(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:339`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_save_then_load_round_trips (method) `def test_save_then_load_round_trips(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:346`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_save_rejects_invalid_envelope (method) `def test_save_rejects_invalid_envelope(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:354`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_reset_replaces_with_a_valid_random_container (method) `def test_reset_replaces_with_a_valid_random_container(self, app, tmp_path)`
- Defined: `tests/test_deniable_vault.py:363`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_audit_is_generic_and_never_contains_ciphertext (method) `def test_audit_is_generic_and_never_contains_ciphertext(self, app, tmp_path, audit_records)`
- Defined: `tests/test_deniable_vault.py:373`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_settings_page_requires_authentication (method) `def test_settings_page_requires_authentication(self, client)`
- Defined: `tests/test_deniable_vault.py:391`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_get_api_requires_authentication (method) `def test_get_api_requires_authentication(self, client)`
- Defined: `tests/test_deniable_vault.py:395`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_settings_page_renders_for_authenticated_user (method) `def test_settings_page_renders_for_authenticated_user(self, client, app)`
- Defined: `tests/test_deniable_vault.py:399`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_get_always_returns_an_envelope_and_parameters (method) `def test_get_always_returns_an_envelope_and_parameters(self, client, app)`
- Defined: `tests/test_deniable_vault.py:406`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_put_without_csrf_is_rejected (method) `def test_put_without_csrf_is_rejected(self, client, app)`
- Defined: `tests/test_deniable_vault.py:414`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_put_get_reset_round_trip (method) `def test_put_get_reset_round_trip(self, client, app)`
- Defined: `tests/test_deniable_vault.py:422`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_put_rejects_malformed_envelope (method) `def test_put_rejects_malformed_envelope(self, client, app)`
- Defined: `tests/test_deniable_vault.py:447`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

### test_vault_is_scoped_to_the_authenticated_user (method) `def test_vault_is_scoped_to_the_authenticated_user(self, client, app)`
- Defined: `tests/test_deniable_vault.py:461`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `models/user.py`

## tests/test_doctor.py

### test_check_binary_finds_present_binary (function) `def test_check_binary_finds_present_binary()`
- Defined: `tests/test_doctor.py:23`
- Doc: A binary on PATH reports ok with its resolved path.

### test_check_binary_flags_missing_binary (function) `def test_check_binary_flags_missing_binary()`
- Defined: `tests/test_doctor.py:30`
- Doc: An unknown binary fails and points at doctor-fix in English.

### test_check_binary_honors_absolute_override (function) `def test_check_binary_honors_absolute_override(tmp_path)`
- Defined: `tests/test_doctor.py:38`
- Doc: Absolute override paths resolve without trusting PATH.

### test_check_module_reports_status (function) `def test_check_module_reports_status()`
- Defined: `tests/test_doctor.py:48`
- Doc: Present stdlib modules pass, unknown ones fail with a remedy.

### test_check_python_accepts_current_runtime (function) `def test_check_python_accepts_current_runtime()`
- Defined: `tests/test_doctor.py:56`
- Doc: The running interpreter satisfies its own minimum version.

### test_parse_host_port_shapes (function) `def test_parse_host_port_shapes()`
- Defined: `tests/test_doctor.py:62`
- Doc: Redis and HTTP URLs reduce to host plus port.

### test_check_tcp_refused_reports_remedy (function) `def test_check_tcp_refused_reports_remedy()`
- Defined: `tests/test_doctor.py:83`
- Doc: A closed loopback port fails with operator guidance.

### test_release_url_builders (function) `def test_release_url_builders()`
- Defined: `tests/test_doctor.py:90`
- Doc: Release URLs follow the official vendor layouts.

### test_apt_command_uses_sudo_outside_root (function) `def test_apt_command_uses_sudo_outside_root()`
- Defined: `tests/test_doctor.py:105`
- Doc: Apt installs escalate with sudo unless already root.

### test_report_exit_code_reflects_failures (function) `def test_report_exit_code_reflects_failures()`
- Defined: `tests/test_doctor.py:115`
- Doc: An empty failure set exits zero, any failure exits one.

### test_load_env_file_parses_assignments (function) `def test_load_env_file_parses_assignments(tmp_path)`
- Defined: `tests/test_doctor.py:129`
- Doc: Comment and blank lines are skipped, quotes are stripped.

### test_upsert_env_replaces_and_appends (function) `def test_upsert_env_replaces_and_appends(tmp_path)`
- Defined: `tests/test_doctor.py:140`
- Doc: Existing keys are replaced in place, new keys are appended.

## tests/test_facade.py

### fast_hasher (function) `def fast_hasher()`
- Defined: `tests/test_facade.py:54`
- Doc: Return an Argon2id hasher with cheap parameters for fast tests.
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### gate_config (function) `def gate_config(fast_hasher)`
- Defined: `tests/test_facade.py:67`
- Doc: Return an enabled facade config with real and duress phrases set.
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### _facade_overrides (function) `def _facade_overrides(fast_hasher)`
- Defined: `tests/test_facade.py:78`
- Doc: Return ``create_app`` config overrides that enable the facade.
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### facade_client (function) `def facade_client(tmp_path, fast_hasher)`
- Defined: `tests/test_facade.py:93`
- Doc: Return a test client for an app with the facade enabled.
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### _make_user (function) `def _make_user(app_or_path, username)`
- Defined: `tests/test_facade.py:109`
- Doc: Create a minimal user row in the given database and return it.
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### _csrf (function) `def _csrf(client)`
- Defined: `tests/test_facade.py:138`
- Doc: Fetch a CSRF token bound to the client's session.
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_defaults_keep_the_facade_off (method) `def test_defaults_keep_the_facade_off(self)`
- Defined: `tests/test_facade.py:149`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_defaults_keep_duress_alert_off (method) `def test_defaults_keep_duress_alert_off(self)`
- Defined: `tests/test_facade.py:154`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_defaults_are_self_consistent (method) `def test_defaults_are_self_consistent(self)`
- Defined: `tests/test_facade.py:157`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_mapping_overrides_defaults (method) `def test_mapping_overrides_defaults(self)`
- Defined: `tests/test_facade.py:165`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_environment_overrides_mapping (method) `def test_environment_overrides_mapping(self, monkeypatch)`
- Defined: `tests/test_facade.py:172`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_protected_paths_csv_is_parsed (method) `def test_protected_paths_csv_is_parsed(self)`
- Defined: `tests/test_facade.py:177`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_gate_configured_requires_enabled_and_a_hash (method) `def test_gate_configured_requires_enabled_and_a_hash(self)`
- Defined: `tests/test_facade.py:183`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_cover_context_is_cosmetic_and_json_serializable (method) `def test_cover_context_is_cosmetic_and_json_serializable(self)`
- Defined: `tests/test_facade.py:194`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_hash_then_verify_accepts_the_phrase (method) `def test_hash_then_verify_accepts_the_phrase(self, fast_hasher)`
- Defined: `tests/test_facade.py:210`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_verify_rejects_a_wrong_phrase (method) `def test_verify_rejects_a_wrong_phrase(self, fast_hasher)`
- Defined: `tests/test_facade.py:214`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_hash_is_salted_so_two_hashes_differ (method) `def test_hash_is_salted_so_two_hashes_differ(self, fast_hasher)`
- Defined: `tests/test_facade.py:218`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_verify_rejects_an_empty_stored_hash (method) `def test_verify_rejects_an_empty_stored_hash(self, fast_hasher)`
- Defined: `tests/test_facade.py:221`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_verify_rejects_a_malformed_stored_hash (method) `def test_verify_rejects_a_malformed_stored_hash(self, fast_hasher)`
- Defined: `tests/test_facade.py:224`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_verify_rejects_a_non_string_stored_hash (method) `def test_verify_rejects_a_non_string_stored_hash(self, fast_hasher)`
- Defined: `tests/test_facade.py:227`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_from_config_builds_a_working_hasher (method) `def test_from_config_builds_a_working_hasher(self)`
- Defined: `tests/test_facade.py:231`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_issue_then_verify_round_trips_the_mode (method) `def test_issue_then_verify_round_trips_the_mode(self)`
- Defined: `tests/test_facade.py:251`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_issue_rejects_an_unknown_mode (method) `def test_issue_rejects_an_unknown_mode(self)`
- Defined: `tests/test_facade.py:256`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_verify_rejects_an_expired_ticket (method) `def test_verify_rejects_an_expired_ticket(self)`
- Defined: `tests/test_facade.py:261`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_verify_rejects_a_ticket_signed_with_another_key (method) `def test_verify_rejects_a_ticket_signed_with_another_key(self)`
- Defined: `tests/test_facade.py:267`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_verify_rejects_garbage_and_none (method) `def test_verify_rejects_garbage_and_none(self)`
- Defined: `tests/test_facade.py:272`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_verify_rejects_a_non_string_token (method) `def test_verify_rejects_a_non_string_token(self)`
- Defined: `tests/test_facade.py:277`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### _gate (method) `def _gate(self, config)`
- Defined: `tests/test_facade.py:289`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_real_phrase_yields_a_real_ticket (method) `def test_real_phrase_yields_a_real_ticket(self, app, gate_config)`
- Defined: `tests/test_facade.py:292`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_duress_phrase_yields_a_duress_ticket (method) `def test_duress_phrase_yields_a_duress_ticket(self, app, gate_config)`
- Defined: `tests/test_facade.py:300`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_wrong_phrase_is_a_miss_with_no_ticket (method) `def test_wrong_phrase_is_a_miss_with_no_ticket(self, app, gate_config)`
- Defined: `tests/test_facade.py:307`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_miss_without_a_duress_hash (method) `def test_miss_without_a_duress_hash(self, app, fast_hasher)`
- Defined: `tests/test_facade.py:314`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_minimum_length_phrase_is_accepted (method) `def test_minimum_length_phrase_is_accepted(self, app, fast_hasher)`
- Defined: `tests/test_facade.py:325`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_maximum_length_phrase_is_accepted (method) `def test_maximum_length_phrase_is_accepted(self, app, fast_hasher)`
- Defined: `tests/test_facade.py:337`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_too_short_phrase_is_a_miss (method) `def test_too_short_phrase_is_a_miss(self, app, gate_config)`
- Defined: `tests/test_facade.py:349`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_too_long_phrase_is_a_miss (method) `def test_too_long_phrase_is_a_miss(self, app, gate_config)`
- Defined: `tests/test_facade.py:355`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_audit_is_generic_and_never_contains_the_phrase (method) `def test_audit_is_generic_and_never_contains_the_phrase(self, app, gate_config, audit_records)`
- Defined: `tests/test_facade.py:361`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_duress_alert_is_opt_in_and_generically_named (method) `def test_duress_alert_is_opt_in_and_generically_named(self, app, fast_hasher, audit_records)`
- Defined: `tests/test_facade.py:372`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_anonymous_login_page_is_replaced_by_the_cover (method) `def test_anonymous_login_page_is_replaced_by_the_cover(self, facade_client)`
- Defined: `tests/test_facade.py:397`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_anonymous_root_is_replaced_by_the_cover (method) `def test_anonymous_root_is_replaced_by_the_cover(self, facade_client)`
- Defined: `tests/test_facade.py:403`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_wrong_phrase_keeps_the_cover_and_does_not_redirect (method) `def test_wrong_phrase_keeps_the_cover_and_does_not_redirect(self, facade_client)`
- Defined: `tests/test_facade.py:409`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_real_phrase_reveals_the_login (method) `def test_real_phrase_reveals_the_login(self, facade_client)`
- Defined: `tests/test_facade.py:417`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_duress_phrase_marks_the_session (method) `def test_duress_phrase_marks_the_session(self, facade_client)`
- Defined: `tests/test_facade.py:432`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_authenticated_user_bypasses_the_cover (method) `def test_authenticated_user_bypasses_the_cover(self, tmp_path, fast_hasher)`
- Defined: `tests/test_facade.py:441`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_gate_endpoint_is_absent_when_facade_disabled (method) `def test_gate_endpoint_is_absent_when_facade_disabled(self, client)`
- Defined: `tests/test_facade.py:465`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_disabled_facade_serves_the_real_login (method) `def test_disabled_facade_serves_the_real_login(self, client)`
- Defined: `tests/test_facade.py:469`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

### test_enabled_without_a_hash_fails_open_to_the_real_app (method) `def test_enabled_without_a_hash_fails_open_to_the_real_app(self, tmp_path)`
- Defined: `tests/test_facade.py:474`
- Depends on: `app_factory.py`, `controllers/facade.py`, `models/user.py`

## tests/test_integrity.py

### test_compute_sri_format (function) `def test_compute_sri_format()`
- Defined: `tests/test_integrity.py:19`
- Depends on: `tools/verify_build.py`, `utils/integrity.py`

### test_manifest_exists_and_pins_crypto (function) `def test_manifest_exists_and_pins_crypto()`
- Defined: `tests/test_integrity.py:25`
- Depends on: `tools/verify_build.py`, `utils/integrity.py`

### test_manifest_hashes_match_files (function) `def test_manifest_hashes_match_files()`
- Defined: `tests/test_integrity.py:37`
- Depends on: `tools/verify_build.py`, `utils/integrity.py`

### test_template_integrity_resolves_both_forms (function) `def test_template_integrity_resolves_both_forms()`
- Defined: `tests/test_integrity.py:44`
- Depends on: `tools/verify_build.py`, `utils/integrity.py`

### test_jinja_global_registered (function) `def test_jinja_global_registered(app)`
- Defined: `tests/test_integrity.py:51`
- Depends on: `tools/verify_build.py`, `utils/integrity.py`

### test_verify_build_passes_on_clean_tree (function) `def test_verify_build_passes_on_clean_tree()`
- Defined: `tests/test_integrity.py:55`
- Depends on: `tools/verify_build.py`, `utils/integrity.py`

## tests/test_padding.py

### test_pad_roundtrip_message_sizes (function) `def test_pad_roundtrip_message_sizes()`
- Defined: `tests/test_padding.py:26`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_pad_roundtrip_file_kind (function) `def test_pad_roundtrip_file_kind()`
- Defined: `tests/test_padding.py:33`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_bucket_boundaries (function) `def test_bucket_boundaries()`
- Defined: `tests/test_padding.py:38`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_pad_output_length_is_bucketed (function) `def test_pad_output_length_is_bucketed()`
- Defined: `tests/test_padding.py:44`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_pad_uses_fresh_randomness (function) `def test_pad_uses_fresh_randomness()`
- Defined: `tests/test_padding.py:49`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_pad_rejects_oversize (function) `def test_pad_rejects_oversize()`
- Defined: `tests/test_padding.py:56`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_unpad_rejects_non_bucket_length (function) `def test_unpad_rejects_non_bucket_length()`
- Defined: `tests/test_padding.py:61`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_unpad_rejects_corrupt_prefix (function) `def test_unpad_rejects_corrupt_prefix()`
- Defined: `tests/test_padding.py:66`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_unpad_rejects_wrong_kind (function) `def test_unpad_rejects_wrong_kind()`
- Defined: `tests/test_padding.py:74`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_wire_lengths (function) `def test_wire_lengths()`
- Defined: `tests/test_padding.py:80`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_config_from_env_override (function) `def test_config_from_env_override(monkeypatch)`
- Defined: `tests/test_padding.py:87`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_config_from_env_falls_back_on_garbage (function) `def test_config_from_env_falls_back_on_garbage(monkeypatch)`
- Defined: `tests/test_padding.py:94`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_cache_holds_tables_not_pad_bytes (function) `def test_cache_holds_tables_not_pad_bytes()`
- Defined: `tests/test_padding.py:99`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_message_controller_rejects_unpadded_envelope (function) `def test_message_controller_rejects_unpadded_envelope(app, tmp_path, monkeypatch)`
- Defined: `tests/test_padding.py:105`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_message_controller_rejects_malformed_base64 (function) `def test_message_controller_rejects_malformed_base64(app, tmp_path, monkeypatch)`
- Defined: `tests/test_padding.py:113`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_message_controller_accepts_bucketed_envelope (function) `def test_message_controller_accepts_bucketed_envelope(app, tmp_path, monkeypatch)`
- Defined: `tests/test_padding.py:120`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_file_controller_rejects_unpadded_upload (method) `def test_file_controller_rejects_unpadded_upload(app)`
- Defined: `tests/test_padding.py:146`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### test_file_controller_accepts_bucketed_upload (method) `def test_file_controller_accepts_bucketed_upload(app)`
- Defined: `tests/test_padding.py:152`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### __init__ (method) `def __init__(self)`
- Defined: `tests/test_padding.py:129`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### put_object (method) `def put_object(self, Bucket, Key, Body)`
- Defined: `tests/test_padding.py:132`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### __init__ (method) `def __init__(self, body)`
- Defined: `tests/test_padding.py:139`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

### read (method) `def read(self)`
- Defined: `tests/test_padding.py:142`
- Depends on: `controllers/file.py`, `controllers/message.py`, `utils/padding.py`, `utils/utils.py`

## tests/test_secure_channel.py

### test_config_defaults_to_disabled_without_binaries (function) `def test_config_defaults_to_disabled_without_binaries()`
- Defined: `tests/test_secure_channel.py:30`
- Doc: Unconfigured environment resolves to a disabled channel.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_config_reads_mode_and_port_from_env (function) `def test_config_reads_mode_and_port_from_env()`
- Defined: `tests/test_secure_channel.py:37`
- Doc: Mode and local port resolve from environment with bounds.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_config_rejects_out_of_range_port (function) `def test_config_rejects_out_of_range_port()`
- Defined: `tests/test_secure_channel.py:47`
- Doc: Ports outside 1..65535 fall back to the default.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_url_validators_accept_only_expected_shapes (function) `def test_url_validators_accept_only_expected_shapes()`
- Defined: `tests/test_secure_channel.py:55`
- Doc: Validators accept quick-tunnel and v3 onion shapes only.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_manager_starts_hybrid_with_injected_launcher (function) `def test_manager_starts_hybrid_with_injected_launcher(tmp_path)`
- Defined: `tests/test_secure_channel.py:64`
- Doc: Start launches both backends and persists redacted state.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_manager_rejects_invalid_mode (function) `def test_manager_rejects_invalid_mode(tmp_path)`
- Defined: `tests/test_secure_channel.py:90`
- Doc: Disabled mode cannot be started explicitly.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_manager_stop_clears_state_with_killer (function) `def test_manager_stop_clears_state_with_killer(tmp_path)`
- Defined: `tests/test_secure_channel.py:101`
- Doc: Stop kills tracked pids and removes persisted state.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_audit_details_never_carry_urls (function) `def test_audit_details_never_carry_urls()`
- Defined: `tests/test_secure_channel.py:122`
- Doc: Audit helper redacts full URLs to mode plus fingerprint.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_superadmin_channel_routes_require_superadmin (function) `def test_superadmin_channel_routes_require_superadmin(client)`
- Defined: `tests/test_secure_channel.py:133`
- Doc: Anonymous POST to channel endpoints redirects to login.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_env_template_documents_channel_keys (function) `def test_env_template_documents_channel_keys()`
- Defined: `tests/test_secure_channel.py:139`
- Doc: Repository env template exposes every channel key.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_channel_state_file_permissions (function) `def test_channel_state_file_permissions(tmp_path)`
- Defined: `tests/test_secure_channel.py:153`
- Doc: Persisted state is owner-only.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_validators_reject_non_string_inputs (function) `def test_validators_reject_non_string_inputs()`
- Defined: `tests/test_secure_channel.py:164`
- Doc: Non-string values never validate as backend addresses.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_port_boundaries_accept_edges_and_reject_outside (function) `def test_port_boundaries_accept_edges_and_reject_outside()`
- Defined: `tests/test_secure_channel.py:175`
- Doc: TCP port coercion honors 1 and 65535 as valid edges.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_config_blank_values_fall_back_to_defaults (function) `def test_config_blank_values_fall_back_to_defaults()`
- Defined: `tests/test_secure_channel.py:186`
- Doc: Empty or whitespace binary and dir values resolve to defaults.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_config_explicit_values_are_preserved (function) `def test_config_explicit_values_are_preserved()`
- Defined: `tests/test_secure_channel.py:203`
- Doc: Explicit binary and dir values survive resolution.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_config_env_beats_mapping (function) `def test_config_env_beats_mapping()`
- Defined: `tests/test_secure_channel.py:219`
- Doc: Environment takes precedence over the mapping for every key.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_channel_status_defaults_and_single_side_active (function) `def test_channel_status_defaults_and_single_side_active()`
- Defined: `tests/test_secure_channel.py:229`
- Doc: Ephemeral defaults True and either backend alone counts as active.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_default_launcher_detaches_process (function) `def test_default_launcher_detaches_process(monkeypatch)`
- Defined: `tests/test_secure_channel.py:254`
- Doc: Launcher spawns detached daemons with piped stdio.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_default_killer_ignores_non_positive_pid (function) `def test_default_killer_ignores_non_positive_pid(monkeypatch)`
- Defined: `tests/test_secure_channel.py:276`
- Doc: Zero and negative pids never reach os.kill.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_default_killer_falls_back_to_kill (function) `def test_default_killer_falls_back_to_kill(monkeypatch)`
- Defined: `tests/test_secure_channel.py:286`
- Doc: Group kill failure falls back to plain kill before giving up.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_manager_init_blank_binaries_fall_back (function) `def test_manager_init_blank_binaries_fall_back()`
- Defined: `tests/test_secure_channel.py:302`
- Doc: Blank constructor binaries resolve to shipped defaults.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_rotate_without_state_raises (function) `def test_rotate_without_state_raises(tmp_path)`
- Defined: `tests/test_secure_channel.py:311`
- Doc: Rotate with no persisted channel raises instead of crashing.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_rotate_disabled_state_raises (function) `def test_rotate_disabled_state_raises(tmp_path)`
- Defined: `tests/test_secure_channel.py:322`
- Doc: Rotate on a disabled record raises instead of starting.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_audit_details_default_verb_and_empty_urls (function) `def test_audit_details_default_verb_and_empty_urls()`
- Defined: `tests/test_secure_channel.py:334`
- Doc: Empty action and absent urls still yield a safe detail string.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_status_for_drops_non_positive_pids (function) `def test_status_for_drops_non_positive_pids()`
- Defined: `tests/test_secure_channel.py:348`
- Doc: Pid zero and negatives never survive status construction.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_read_state_filters_bad_pids (function) `def test_read_state_filters_bad_pids(tmp_path)`
- Defined: `tests/test_secure_channel.py:357`
- Doc: Corrupt pid entries in state are filtered, valid ones kept.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_write_state_is_sorted_and_ephemeral (function) `def test_write_state_is_sorted_and_ephemeral(tmp_path)`
- Defined: `tests/test_secure_channel.py:378`
- Doc: Persisted payload is deterministic JSON with ephemeral set.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_write_state_twice_in_existing_dir (function) `def test_write_state_twice_in_existing_dir(tmp_path)`
- Defined: `tests/test_secure_channel.py:397`
- Doc: Repeated writes into an existing directory never raise.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_write_state_creates_nested_dirs (function) `def test_write_state_creates_nested_dirs(tmp_path)`
- Defined: `tests/test_secure_channel.py:408`
- Doc: Nested state directories are created recursively.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_start_creates_nested_state_dirs (function) `def test_start_creates_nested_state_dirs(tmp_path)`
- Defined: `tests/test_secure_channel.py:416`
- Doc: Backend start creates nested state dirs recursively.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_start_tor_only_creates_nested_state_dirs (function) `def test_start_tor_only_creates_nested_state_dirs(tmp_path)`
- Defined: `tests/test_secure_channel.py:442`
- Doc: Tor-only start creates nested state dirs without prior backend.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_cleanup_scratch_suppresses_rmtree_errors (function) `def test_cleanup_scratch_suppresses_rmtree_errors(tmp_path, monkeypatch)`
- Defined: `tests/test_secure_channel.py:463`
- Doc: Unremovable scratch dirs never break stop.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_resolve_binary_with_default_launcher_requires_path (function) `def test_resolve_binary_with_default_launcher_requires_path(tmp_path)`
- Defined: `tests/test_secure_channel.py:480`
- Doc: Default launcher resolves bare names through PATH only.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_resolve_binary_with_injected_launcher_skips_which (function) `def test_resolve_binary_with_injected_launcher_skips_which(tmp_path)`
- Defined: `tests/test_secure_channel.py:497`
- Doc: Injected launchers accept bare names without PATH lookup.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_resolve_binary_absolute_path_must_exist (function) `def test_resolve_binary_absolute_path_must_exist(tmp_path)`
- Defined: `tests/test_secure_channel.py:511`
- Doc: Absolute candidates are accepted only when the file exists.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_pid_live_branches (function) `def test_pid_live_branches(monkeypatch, tmp_path)`
- Defined: `tests/test_secure_channel.py:527`
- Doc: Pid liveness distinguishes dead, forbidden, broken, and live.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_normalize_onion_shapes (function) `def test_normalize_onion_shapes()`
- Defined: `tests/test_secure_channel.py:555`
- Doc: Bare hostnames gain a scheme while full urls pass through.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_wait_helpers_respect_deadline_and_content (function) `def test_wait_helpers_respect_deadline_and_content(tmp_path, monkeypatch)`
- Defined: `tests/test_secure_channel.py:564`
- Doc: Pattern and file waiters poll until timeout or content.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_wait_helpers_include_deadline_instant (function) `def test_wait_helpers_include_deadline_instant(tmp_path, monkeypatch)`
- Defined: `tests/test_secure_channel.py:597`
- Doc: Polling still checks content at the exact deadline instant.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_channel_diagnostics_reports_availability (function) `def test_channel_diagnostics_reports_availability(tmp_path)`
- Defined: `tests/test_secure_channel.py:636`
- Doc: Diagnostics resolve absolute paths and flag missing bare names.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_channel_diagnostics_missing_absolute_path (function) `def test_channel_diagnostics_missing_absolute_path(tmp_path)`
- Defined: `tests/test_secure_channel.py:656`
- Doc: Absolute candidates that do not exist report as missing.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_read_log_tail_returns_trailing_lines (function) `def test_read_log_tail_returns_trailing_lines(tmp_path)`
- Defined: `tests/test_secure_channel.py:671`
- Doc: Log tail surfaces backend output and stays empty when absent.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_superadmin_channel_section_is_readable (function) `def test_superadmin_channel_section_is_readable()`
- Defined: `tests/test_secure_channel.py:685`
- Doc: Channel panel avoids low-contrast muted text and shows diagnostics.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_origin_scheme_parsing (function) `def test_origin_scheme_parsing()`
- Defined: `tests/test_secure_channel.py:696`
- Doc: Only http and https survive scheme coercion.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_config_reads_origin_scheme (function) `def test_config_reads_origin_scheme()`
- Defined: `tests/test_secure_channel.py:706`
- Doc: Origin scheme resolves from env with a safe fallback.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_origin_url_points_at_loopback (function) `def test_origin_url_points_at_loopback()`
- Defined: `tests/test_secure_channel.py:719`
- Doc: Origin URL always targets loopback with the configured scheme.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_cloudflared_cmd_matches_origin_scheme (function) `def test_cloudflared_cmd_matches_origin_scheme(tmp_path)`
- Defined: `tests/test_secure_channel.py:733`
- Doc: Plain origins skip TLS flags, https origins verify nothing.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_s3_probe_skips_dead_endpoint (function) `def test_s3_probe_skips_dead_endpoint(app)`
- Defined: `tests/test_secure_channel.py:763`
- Doc: Unreachable object storage reports down without raising.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### test_s3_probe_detects_live_endpoint (function) `def test_s3_probe_detects_live_endpoint(app)`
- Defined: `tests/test_secure_channel.py:771`
- Doc: A listening socket reports the endpoint as reachable.
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### fake_launcher (function) `def fake_launcher(cmd, log_path)`
- Defined: `tests/test_secure_channel.py:67`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### fake_launcher (function) `def fake_launcher(cmd, log_path)`
- Defined: `tests/test_secure_channel.py:105`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _fake_popen (method) `def _fake_popen(cmd)`
- Defined: `tests/test_secure_channel.py:263`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _raise_pg (method) `def _raise_pg(pid, sig)`
- Defined: `tests/test_secure_channel.py:290`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _record_kill (method) `def _record_kill(pid, sig)`
- Defined: `tests/test_secure_channel.py:293`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### fake_launcher (method) `def fake_launcher(cmd, log_path)`
- Defined: `tests/test_secure_channel.py:419`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### fake_launcher (method) `def fake_launcher(cmd, log_path)`
- Defined: `tests/test_secure_channel.py:445`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _raise (method) `def _raise()`
- Defined: `tests/test_secure_channel.py:471`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _raise_lookup (method) `def _raise_lookup(pid, sig)`
- Defined: `tests/test_secure_channel.py:536`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _raise_perm (method) `def _raise_perm(pid, sig)`
- Defined: `tests/test_secure_channel.py:542`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _raise_os (method) `def _raise_os(pid, sig)`
- Defined: `tests/test_secure_channel.py:548`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _fake_mono (method) `def _fake_mono()`
- Defined: `tests/test_secure_channel.py:573`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _fake_sleep (method) `def _fake_sleep(secs)`
- Defined: `tests/test_secure_channel.py:576`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _fake_mono (method) `def _fake_mono()`
- Defined: `tests/test_secure_channel.py:606`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _fake_sleep (method) `def _fake_sleep(secs)`
- Defined: `tests/test_secure_channel.py:609`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### _fake_sleep_file (method) `def _fake_sleep_file(secs)`
- Defined: `tests/test_secure_channel.py:627`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

### fake_launcher (method) `def fake_launcher(cmd, log_path)`
- Defined: `tests/test_secure_channel.py:737`
- Depends on: `controllers/secure_channel.py`, `views/admin.py`

## tests/test_security.py

### test_audit_event_includes_ip_and_ua_by_default (function) `def test_audit_event_includes_ip_and_ua_by_default(app, audit_records, monkeypatch)`
- Defined: `tests/test_security.py:12`
- Depends on: `utils/security.py`

### test_audit_event_redacts_ip_and_ua_when_disabled (function) `def test_audit_event_redacts_ip_and_ua_when_disabled(app, audit_records, monkeypatch)`
- Defined: `tests/test_security.py:29`
- Depends on: `utils/security.py`

### test_json_csrf_protect_rejects_missing_token (function) `def test_json_csrf_protect_rejects_missing_token(app)`
- Defined: `tests/test_security.py:45`
- Depends on: `utils/security.py`

### test_json_csrf_protect_accepts_valid_header_token (function) `def test_json_csrf_protect_accepts_valid_header_token(app)`
- Defined: `tests/test_security.py:57`
- Depends on: `utils/security.py`

### test_json_csrf_protect_passes_get_through_without_token (function) `def test_json_csrf_protect_passes_get_through_without_token(app)`
- Defined: `tests/test_security.py:77`
- Depends on: `utils/security.py`

### view (function) `def view()`
- Defined: `tests/test_security.py:47`
- Depends on: `utils/security.py`

### view (function) `def view()`
- Defined: `tests/test_security.py:59`
- Depends on: `utils/security.py`

### view (function) `def view()`
- Defined: `tests/test_security.py:79`
- Depends on: `utils/security.py`

## tests/test_srp.py

### _h (function) `def _h()`
- Defined: `tests/test_srp.py:16`
- Depends on: `utils/utils.py`

### _hint (function) `def _hint()`
- Defined: `tests/test_srp.py:23`
- Depends on: `utils/utils.py`

### _client_derive_verifier (function) `def _client_derive_verifier(username, password, salt_hex)`
- Defined: `tests/test_srp.py:27`
- Doc: Mirror ``deriveVerifier`` in qv-crypto.js: v = g^x mod N.
- Depends on: `utils/utils.py`

### _client_compute_proof (function) `def _client_compute_proof(username, password, salt_hex, server_a_secret, server_a, server_b)`
- Defined: `tests/test_srp.py:34`
- Doc: Mirror ``srpLogin`` in qv-crypto.js: derive M1 and the expected M2.
- Depends on: `utils/utils.py`

### test_srp6a_full_roundtrip_matches_server_proofs (function) `def test_srp6a_full_roundtrip_matches_server_proofs()`
- Defined: `tests/test_srp.py:74`
- Depends on: `utils/utils.py`

### test_srp6a_wrong_password_produces_mismatched_proof (function) `def test_srp6a_wrong_password_produces_mismatched_proof()`
- Defined: `tests/test_srp.py:104`
- Depends on: `utils/utils.py`

## tests/test_utils.py

### test_database_path_prefers_the_configured_path (function) `def test_database_path_prefers_the_configured_path(app)`
- Defined: `tests/test_utils.py:8`
- Depends on: `utils/utils.py`

### test_database_path_honors_env_outside_a_context (function) `def test_database_path_honors_env_outside_a_context(monkeypatch)`
- Defined: `tests/test_utils.py:13`
- Depends on: `utils/utils.py`

### test_database_path_default_outside_a_context (function) `def test_database_path_default_outside_a_context(monkeypatch)`
- Defined: `tests/test_utils.py:18`
- Depends on: `utils/utils.py`

## tools/generate_sri.py

### collect_local_assets (function) `def collect_local_assets()`
- Defined: `tools/generate_sri.py:41`
- Doc: Hash every first-party script and stylesheet under ``static/``.
- Depends on: `utils/integrity.py`

### fetch_cdn_assets (function) `def fetch_cdn_assets()`
- Defined: `tools/generate_sri.py:56`
- Doc: Download every pinned CDN URL and hash its exact bytes.
- Depends on: `utils/integrity.py`

### build_manifest (function) `def build_manifest(cdn, local)`
- Defined: `tools/generate_sri.py:66`
- Doc: Assemble the deterministic manifest document.
- Depends on: `utils/integrity.py`

### render_manifest (function) `def render_manifest(manifest)`
- Defined: `tools/generate_sri.py:76`
- Doc: Render the manifest deterministically with a trailing newline.
- Depends on: `utils/integrity.py`

### main (function) `def main(argv)`
- Defined: `tools/generate_sri.py:81`
- Doc: Generate the manifest, or verify it is current with ``--check``.
- Depends on: `utils/integrity.py`

## tools/mutation_test.py

### _is_equivalent_bool (method) `def _is_equivalent_bool(tokens, index)`
- Defined: `tools/mutation_test.py:67`

### discover_mutations (method) `def discover_mutations(path, source)`
- Defined: `tools/mutation_test.py:79`
- Doc: Return every token-level mutation the harness can apply to a module.

### apply_mutation (method) `def apply_mutation(source, mutation)`
- Defined: `tools/mutation_test.py:109`
- Doc: Return source with one token replaced at its exact position.

### collect (method) `def collect(targets, limit)`
- Defined: `tools/mutation_test.py:121`
- Doc: Gather mutations across targets up to a global cap.

### purge_bytecode (method) `def purge_bytecode()`
- Defined: `tools/mutation_test.py:133`
- Doc: Remove compiled caches so restored sources are always reloaded.

### run_suite (method) `def run_suite(python, tests)`
- Defined: `tools/mutation_test.py:142`
- Doc: Return whether the test suite passed.

### main (method) `def main(argv)`
- Defined: `tools/mutation_test.py:157`
- Doc: Run the mutation campaign and report killed versus survived mutants.

## tools/verify_build.py

### _normalize_reference (method) `def _normalize_reference(ref)`
- Defined: `tools/verify_build.py:60`
- Doc: Resolve a ``url_for('static', ...)`` expression to its served path.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

### load_manifest (method) `def load_manifest()`
- Defined: `tools/verify_build.py:71`
- Doc: Load and return the SRI manifest document.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

### expected_for_reference (method) `def expected_for_reference(manifest, ref)`
- Defined: `tools/verify_build.py:76`
- Doc: Resolve the pinned integrity value for one template reference.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

### integrity_attribute_ok (method) `def integrity_attribute_ok(integrity, ref, expected)`
- Defined: `tools/verify_build.py:85`
- Doc: Accept a literal pin or the ``sri_integrity`` template expression.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

### check_local_hashes (method) `def check_local_hashes(manifest, failures)`
- Defined: `tools/verify_build.py:95`
- Doc: Recompute every pinned local asset and record mismatches.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

### check_template_references (method) `def check_template_references(manifest, failures)`
- Defined: `tools/verify_build.py:110`
- Doc: Require manifest-backed integrity on every template reference.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

### check_bucket_parity (method) `def check_bucket_parity(failures)`
- Defined: `tools/verify_build.py:126`
- Doc: Require identical bucket tables in Python and JavaScript.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

### main (method) `def main()`
- Defined: `tools/verify_build.py:141`
- Doc: Run every check and report failures.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

### __init__ (method) `def __init__(self)`
- Defined: `tools/verify_build.py:37`
- Doc: Initialize the reference collector.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

### handle_starttag (method) `def handle_starttag(self, tag, attrs)`
- Defined: `tools/verify_build.py:42`
- Doc: Record one script or link tag with its integrity attribute.
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`

## utils/cache.py

### __init__ (method) `def __init__(self)`
- Defined: `utils/cache.py:8`

### get (method) `def get(self, key)`
- Defined: `utils/cache.py:11`
- Doc: Retrieve a value from the cache.

### set (method) `def set(self, key, value, ttl)`
- Defined: `utils/cache.py:16`
- Doc: Store a value in the cache with an optional TTL (seconds).

### delete (method) `def delete(self, key)`
- Defined: `utils/cache.py:20`
- Doc: Delete a key from the cache.

## utils/integrity.py

### manifest_path (function) `def manifest_path()`
- Defined: `utils/integrity.py:25`
- Doc: Return the manifest path resolved from this file, never hardcoded.
- Imported by: `app_factory.py`, `tests/test_integrity.py`, `tools/generate_sri.py`, `tools/verify_build.py`

### compute_sri (function) `def compute_sri(data, algorithm)`
- Defined: `utils/integrity.py:30`
- Doc: Return the SRI string ``<algorithm>-<base64 digest>`` for ``data``.
- Imported by: `app_factory.py`, `tests/test_integrity.py`, `tools/generate_sri.py`, `tools/verify_build.py`

### compute_file_sri (function) `def compute_file_sri(path, algorithm)`
- Defined: `utils/integrity.py:36`
- Doc: Return the SRI string for the bytes stored at ``path``.
- Imported by: `app_factory.py`, `tests/test_integrity.py`, `tools/generate_sri.py`, `tools/verify_build.py`

### _cached_manifest_text (function) `def _cached_manifest_text()`
- Defined: `utils/integrity.py:42`
- Doc: Return the raw manifest text, cached for the process lifetime.
- Imported by: `app_factory.py`, `tests/test_integrity.py`, `tools/generate_sri.py`, `tools/verify_build.py`

### load_manifest (function) `def load_manifest()`
- Defined: `utils/integrity.py:47`
- Doc: Return the parsed SRI manifest, or an empty mapping when absent.
- Imported by: `app_factory.py`, `tests/test_integrity.py`, `tools/generate_sri.py`, `tools/verify_build.py`

### integrity_for (function) `def integrity_for(key)`
- Defined: `utils/integrity.py:55`
- Doc: Return the pinned integrity string for one manifest key.
- Imported by: `app_factory.py`, `tests/test_integrity.py`, `tools/generate_sri.py`, `tools/verify_build.py`

### clear_manifest_cache (function) `def clear_manifest_cache()`
- Defined: `utils/integrity.py:72`
- Doc: Drop the cached manifest text so tests see a regenerated file.
- Imported by: `app_factory.py`, `tests/test_integrity.py`, `tools/generate_sri.py`, `tools/verify_build.py`

### template_integrity (function) `def template_integrity(key)`
- Defined: `utils/integrity.py:77`
- Doc: Return the integrity string for a template asset reference.
- Imported by: `app_factory.py`, `tests/test_integrity.py`, `tools/generate_sri.py`, `tools/verify_build.py`

## utils/mailer.py

### external_url (function) `def external_url(path)`
- Defined: `utils/mailer.py:22`
- Doc: Build an absolute URL for a root-relative path using the public host.
- Imported by: `controllers/auth.py`, `scripts/email_tool.py`, `utils/scheduler.py`, `views/auth.py`

### mail_is_configured (function) `def mail_is_configured()`
- Defined: `utils/mailer.py:38`
- Doc: Return True when SMTP credentials are present so a send can succeed.
- Imported by: `controllers/auth.py`, `scripts/email_tool.py`, `utils/scheduler.py`, `views/auth.py`

### send_transactional_email (function) `def send_transactional_email(subject, recipients, body)`
- Defined: `utils/mailer.py:51`
- Doc: Send a plain-text transactional email through the configured server.
- Imported by: `controllers/auth.py`, `scripts/email_tool.py`, `utils/scheduler.py`, `views/auth.py`

## utils/padding.py

### _parse_buckets (method) `def _parse_buckets(raw, fallback)`
- Defined: `utils/padding.py:95`
- Doc: Parse a comma-separated bucket list, falling back on any error.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### config_from_env (method) `def config_from_env()`
- Defined: `utils/padding.py:109`
- Doc: Build a :class:`PaddingConfig` from the environment.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### _cached_bucket_table (method) `def _cached_bucket_table(fingerprint)`
- Defined: `utils/padding.py:128`
- Doc: Return the cached immutable bucket tables for one config version.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### cached_tables (method) `def cached_tables(config)`
- Defined: `utils/padding.py:142`
- Doc: Return the process-wide cached bucket tables for ``config``.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### bucket_for (method) `def bucket_for(plaintext_len, kind, config)`
- Defined: `utils/padding.py:149`
- Doc: Return the smallest bucket holding ``plaintext_len`` plus prefix.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### pad (method) `def pad(plaintext, kind, config)`
- Defined: `utils/padding.py:169`
- Doc: Pad ``plaintext`` to its bucket with fresh CSPRNG bytes.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### unpad (method) `def unpad(padded, kind, config)`
- Defined: `utils/padding.py:183`
- Doc: Remove bucket framing and return the original plaintext.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### wire_ciphertext_len (method) `def wire_ciphertext_len(bucket)`
- Defined: `utils/padding.py:209`
- Doc: Return the AES-256-GCM ciphertext length for one padded bucket.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### is_allowed_ciphertext_len (method) `def is_allowed_ciphertext_len(ciphertext_len, kind, config)`
- Defined: `utils/padding.py:214`
- Doc: Return True when ``ciphertext_len`` matches a bucket plus GCM overhead.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### buckets_for (method) `def buckets_for(self, kind)`
- Defined: `utils/padding.py:84`
- Doc: Return the bucket table for ``kind``.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

### max_plaintext_bytes (method) `def max_plaintext_bytes(self, kind)`
- Defined: `utils/padding.py:90`
- Doc: Return the largest plaintext that fits ``kind``.
- Imported by: `controllers/file.py`, `controllers/message.py`, `static/js/qv-padding.js`, `tests/test_padding.py`, `tools/verify_build.py`

## utils/plans.py

### get_plan (method) `def get_plan(plan_name)`
- Defined: `utils/plans.py:30`
- Doc: Obtiene los detalles de un plan.

### validate_plan_payment (method) `def validate_plan_payment(plan_name, amount_paid)`
- Defined: `utils/plans.py:42`
- Doc: Valida que el monto pagado coincide con el plan.

## utils/scheduler.py

### _now_utc (function) `def _now_utc()`
- Defined: `utils/scheduler.py:32`
- Doc: Timezone-aware UTC ``now`` (avoids the deprecated ``datetime.utcnow()``).
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

### init_scheduler (function) `def init_scheduler(app, mail)`
- Defined: `utils/scheduler.py:37`
- Doc: Start the background scheduler with the production job schedule.
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

### _is_trial_elapsed (function) `def _is_trial_elapsed(user)`
- Defined: `utils/scheduler.py:54`
- Doc: Return True if the user is on a free plan and the trial has ended.
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

### check_trial_expiration (function) `def check_trial_expiration()`
- Defined: `utils/scheduler.py:72`
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

### cleanup_old_messages (function) `def cleanup_old_messages()`
- Defined: `utils/scheduler.py:118`
- Depends on: `models/message.py`, `models/user.py`, `utils/mailer.py`

## utils/security.py

### _get_audit_logger (function) `def _get_audit_logger()`
- Defined: `utils/security.py:46`
- Doc: Return the process-wide audit logger, configured on first use.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### _correlation_id (function) `def _correlation_id()`
- Defined: `utils/security.py:72`
- Doc: Return the per-request correlation id, generating one if missing.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### audit_event (function) `def audit_event(event)`
- Defined: `utils/security.py:86`
- Doc: Emit a structured audit record.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### constant_time_compare (function) `def constant_time_compare(a, b)`
- Defined: `utils/security.py:123`
- Doc: Return True if the two strings match in constant time.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### hash_secret (function) `def hash_secret(secret)`
- Defined: `utils/security.py:135`
- Doc: Hash a short-lived secret (phone code, MFA, recovery code) for storage.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### verify_secret (function) `def verify_secret(secret, expected_hash)`
- Defined: `utils/security.py:156`
- Doc: Verify a short-lived secret against its stored hash.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### new_one_time_code (function) `def new_one_time_code(length)`
- Defined: `utils/security.py:163`
- Doc: Return a cryptographically random numeric verification code.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### _extract_csrf_token (function) `def _extract_csrf_token()`
- Defined: `utils/security.py:172`
- Doc: Return the CSRF token from the request header or body.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### json_csrf_protect (function) `def json_csrf_protect(view)`
- Defined: `utils/security.py:193`
- Doc: Decorator: require a valid CSRF token on JSON state-changing requests.
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

### wrapper (function) `def wrapper()`
- Defined: `utils/security.py:207`
- Depends on: `utils/utils.py`
- Imported by: `controllers/auth.py`, `controllers/deniable_vault.py`, `controllers/facade.py`, `tests/conftest.py`, `tests/test_security.py`, `views/account.py`, `views/auth.py`, `views/sync.py`

## utils/srp6a.py

### i2osp (function) `def i2osp(value)`
- Defined: `utils/srp6a.py:47`
- Doc: Encode an integer as a big-endian byte string padded to the length of N.

### _hash (function) `def _hash()`
- Defined: `utils/srp6a.py:60`
- Doc: Return the SHA-256 digest of the concatenated byte chunks.

### _hash_int (function) `def _hash_int()`
- Defined: `utils/srp6a.py:68`
- Doc: Return the SHA-256 digest of the concatenated chunks as an integer.

### compute_k (function) `def compute_k()`
- Defined: `utils/srp6a.py:73`
- Doc: Compute the SRP-6a multiplier parameter ``k = H(N | PAD(g))``.

### compute_u (function) `def compute_u(server_a, server_b)`
- Defined: `utils/srp6a.py:78`
- Doc: Compute the random scrambling parameter ``u = H(PAD(A) | PAD(B))``.

### generate_server_challenge (function) `def generate_server_challenge(verifier)`
- Defined: `utils/srp6a.py:91`
- Doc: Generate the server ephemeral key pair (b, B) for a login challenge.

### compute_proofs (function) `def compute_proofs(username, salt_hex, verifier, server_a, server_b, server_b_secret)`
- Defined: `utils/srp6a.py:107`
- Doc: Compute the expected client proof M1 and the server proof M2.

### hello (method) `def hello(store, username, client_a_hex, salt_hex, verifier_hex)`
- Defined: `utils/srp6a.py:224`
- Doc: Process the SRP ``hello`` step and return the server challenge B.

### verify (method) `def verify(store, username, client_m1_hex)`
- Defined: `utils/srp6a.py:260`
- Doc: Process the SRP ``verify`` step and return the server proof M2.

### __init__ (method) `def __init__(self, storage_uri)`
- Defined: `utils/srp6a.py:158`
- Doc: Initialize the store from a Redis connection URI.

### _key (method) `def _key(username)`
- Defined: `utils/srp6a.py:168`
- Doc: Return the Redis key for a username's pending SRP session.

### save (method) `def save(self, username, salt_hex, verifier_hex, server_a_hex, server_b_hex, server_b_secret_hex)`
- Defined: `utils/srp6a.py:172`
- Doc: Persist the ephemeral SRP challenge state for a username.

### load (method) `def load(self, username)`
- Defined: `utils/srp6a.py:202`
- Doc: Load and consume the ephemeral SRP state for a username.

## utils/utils.py

### database_path (function) `def database_path()`
- Defined: `utils/utils.py:12`
- Doc: Return the SQLite database path from config, with a legacy fallback.
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/auth.py`, `controllers/file.py`, `controllers/message.py`, `scripts/email_tool.py`, `tests/test_padding.py`, `tests/test_srp.py`, `tests/test_utils.py`, `utils/security.py`, `views/admin.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/subscription.py`, `views/sync.py`, `views/views.py`

### as_bool (function) `def as_bool(value, default)`
- Defined: `utils/utils.py:29`
- Doc: Coerce an environment or payload value into a real boolean.
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/auth.py`, `controllers/file.py`, `controllers/message.py`, `scripts/email_tool.py`, `tests/test_padding.py`, `tests/test_srp.py`, `tests/test_utils.py`, `utils/security.py`, `views/admin.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/subscription.py`, `views/sync.py`, `views/views.py`

### sanitize_path (function) `def sanitize_path(path)`
- Defined: `utils/utils.py:49`
- Doc: Sanitiza una ruta de archivo para prevenir LFI y path traversal.
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/auth.py`, `controllers/file.py`, `controllers/message.py`, `scripts/email_tool.py`, `tests/test_padding.py`, `tests/test_srp.py`, `tests/test_utils.py`, `utils/security.py`, `views/admin.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/subscription.py`, `views/sync.py`, `views/views.py`

### load_payload (method) `def load_payload()`
- Defined: `utils/utils.py:168`
- Doc: Load non-secret application configuration from ``payload.json``.
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/auth.py`, `controllers/file.py`, `controllers/message.py`, `scripts/email_tool.py`, `tests/test_padding.py`, `tests/test_srp.py`, `tests/test_utils.py`, `utils/security.py`, `views/admin.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/subscription.py`, `views/sync.py`, `views/views.py`

### __init__ (method) `def __init__(self, config_dict)`
- Defined: `utils/utils.py:145`
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/auth.py`, `controllers/file.py`, `controllers/message.py`, `scripts/email_tool.py`, `tests/test_padding.py`, `tests/test_srp.py`, `tests/test_utils.py`, `utils/security.py`, `views/admin.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/subscription.py`, `views/sync.py`, `views/views.py`

### __getitem__ (method) `def __getitem__(self, key)`
- Defined: `utils/utils.py:165`
- Imported by: `app.py`, `app_factory.py`, `controllers/auth.py`, `controllers/auth.py`, `controllers/file.py`, `controllers/message.py`, `scripts/email_tool.py`, `tests/test_padding.py`, `tests/test_srp.py`, `tests/test_utils.py`, `utils/security.py`, `views/admin.py`, `views/admin.py`, `views/auth.py`, `views/faq.py`, `views/subscription.py`, `views/sync.py`, `views/views.py`

## views/about.py

### about (function) `def about()`
- Defined: `views/about.py:6`
- Doc: Render the About page.
- Imported by: `app_factory.py`

## views/account.py

### get_deniable_vault_controller (function) `def get_deniable_vault_controller()`
- Defined: `views/account.py:51`
- Doc: Build a controller bound to the active app's database and config.
- Depends on: `controllers/deniable_vault.py`, `controllers/facade.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

### settings (function) `def settings()`
- Defined: `views/account.py:65`
- Doc: Render the account settings page.
- Depends on: `controllers/deniable_vault.py`, `controllers/facade.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

### get_vault (function) `def get_vault()`
- Defined: `views/account.py:85`
- Doc: Return the user's container and the build parameters.
- Depends on: `controllers/deniable_vault.py`, `controllers/facade.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

### put_vault (function) `def put_vault()`
- Defined: `views/account.py:107`
- Doc: Validate and store a container for the user.
- Depends on: `controllers/deniable_vault.py`, `controllers/facade.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

### delete_vault (function) `def delete_vault()`
- Defined: `views/account.py:130`
- Doc: Reset the user's container to a fresh random one.
- Depends on: `controllers/deniable_vault.py`, `controllers/facade.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

## views/admin.py

### _audit_action (function) `def _audit_action(actor, action, target_user, ip, details)`
- Defined: `views/admin.py:31`
- Doc: Append one superadmin audit row with a single construction site.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### _channel_manager (function) `def _channel_manager()`
- Defined: `views/admin.py:48`
- Doc: Build the disposable channel manager from env and app config.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### _s3_reachable (function) `def _s3_reachable(timeout)`
- Defined: `views/admin.py:54`
- Doc: Return whether the Garage S3 endpoint answers a TCP probe.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### _read_log_tail (function) `def _read_log_tail(state_dir, limit)`
- Defined: `views/admin.py:84`
- Doc: Return the last lines of backend logs for operator diagnosis.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### _channel_diagnostics (function) `def _channel_diagnostics(manager)`
- Defined: `views/admin.py:116`
- Doc: Collect binary availability and paths without launching anything.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### admin (method) `def admin()`
- Defined: `views/admin.py:186`
- Doc: Plan catalog read view.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### superadmin_edit_user (method) `def superadmin_edit_user(username)`
- Defined: `views/admin.py:208`
- Doc: Full profile edit for a single user.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### manage_plans (method) `def manage_plans()`
- Defined: `views/admin.py:313`
- Doc: Handle plan management.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### edit_plan (method) `def edit_plan(plan_name)`
- Defined: `views/admin.py:337`
- Doc: Handle editing of plan details.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### superadmin (method) `def superadmin()`
- Defined: `views/admin.py:373`
- Doc: Superadmin identity-recovery and inventory panel.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### superadmin_reset_mfa (method) `def superadmin_reset_mfa(username)`
- Defined: `views/admin.py:476`
- Doc: Disable MFA and clear the pending code for ``username``.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### superadmin_resend_confirmation (method) `def superadmin_resend_confirmation(username)`
- Defined: `views/admin.py:523`
- Doc: Issue a fresh ``confirmation_token`` for ``username``.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### superadmin_toggle_suspend (method) `def superadmin_toggle_suspend(username)`
- Defined: `views/admin.py:570`
- Doc: Flip ``subscription_status`` between active and inactive.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### superadmin_channel_start (method) `def superadmin_channel_start()`
- Defined: `views/admin.py:620`
- Doc: Start a disposable secure channel in the requested mode.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### superadmin_channel_stop (method) `def superadmin_channel_stop()`
- Defined: `views/admin.py:659`
- Doc: Dispose the running channel and remove its addresses.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### superadmin_channel_rotate (method) `def superadmin_channel_rotate()`
- Defined: `views/admin.py:682`
- Doc: Dispose current addresses and publish fresh ones in the same mode.
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

### admin_contacts (method) `def admin_contacts()`
- Defined: `views/admin.py:705`
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`, `tests/test_secure_channel.py`

## views/auth.py

### role_required (function) `def role_required()`
- Defined: `views/auth.py:71`
- Doc: Restrict a route to authenticated users holding one of the given roles.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_auth_controller (method) `def get_auth_controller()`
- Defined: `views/auth.py:132`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### show_register (method) `def show_register()`
- Defined: `views/auth.py:143`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### handle_register (method) `def handle_register()`
- Defined: `views/auth.py:150`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### login (method) `def login()`
- Defined: `views/auth.py:234`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### recover (method) `def recover()`
- Defined: `views/auth.py:242`
- Doc: Render the QV-RECOVERY-1 account-recovery page.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### _srp_key (method) `def _srp_key()`
- Defined: `views/auth.py:255`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### _recovery_key (method) `def _recovery_key()`
- Defined: `views/auth.py:266`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### srp_hello (method) `def srp_hello()`
- Defined: `views/auth.py:278`
- Doc: First SRP-6a step: receive the client public value A, return salt and B.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### srp_verify (method) `def srp_verify()`
- Defined: `views/auth.py:299`
- Doc: Second SRP-6a step: verify the client proof M1 and return server proof M2.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### logout (method) `def logout()`
- Defined: `views/auth.py:337`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### confirm_email (method) `def confirm_email(token)`
- Defined: `views/auth.py:344`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### verify_phone (method) `def verify_phone()`
- Defined: `views/auth.py:367`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### resend_phone_verification (method) `def resend_phone_verification()`
- Defined: `views/auth.py:384`
- Doc: Re-send the phone verification code for an account.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### verify_mfa (method) `def verify_mfa()`
- Defined: `views/auth.py:407`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### toggle_mfa (method) `def toggle_mfa()`
- Defined: `views/auth.py:429`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### contact (method) `def contact()`
- Defined: `views/auth.py:454`
- Doc: Render the contact form and persist a message from the current user.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_public_key (method) `def get_public_key()`
- Defined: `views/auth.py:485`
- Doc: Return a user's hybrid public key so the browser can wrap data to them.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_user_keys (method) `def get_user_keys()`
- Defined: `views/auth.py:503`
- Doc: Provide the keys a user needs to decrypt their data client-side.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_recovery_bundle (method) `def get_recovery_bundle()`
- Defined: `views/auth.py:534`
- Doc: Return the QV-RECOVERY-1 bundle for a username, if one was generated.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### reset_with_recovery (method) `def reset_with_recovery()`
- Defined: `views/auth.py:559`
- Doc: Reset SRP credentials and the password-wrapped private key via QV-RECOVERY-1.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### get_csrf_token (method) `def get_csrf_token()`
- Defined: `views/auth.py:619`
- Doc: Issue the CSRF token used by the SPA for state-changing JSON calls.
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### decorator (method) `def decorator(f)`
- Defined: `views/auth.py:85`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

### decorated_function (method) `def decorated_function()`
- Defined: `views/auth.py:87`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

## views/facade.py

### register_facade (function) `def register_facade(app)`
- Defined: `views/facade.py:33`
- Doc: Install the facade on ``app`` when it is enabled and configured.
- Depends on: `controllers/facade.py`
- Imported by: `app_factory.py`

### _build_cover_service (function) `def _build_cover_service(config)`
- Defined: `views/facade.py:71`
- Depends on: `controllers/facade.py`
- Imported by: `app_factory.py`

### _ticket_mode (function) `def _ticket_mode(gate)`
- Defined: `views/facade.py:86`
- Depends on: `controllers/facade.py`
- Imported by: `app_factory.py`

### render_cover (function) `def render_cover()`
- Defined: `views/facade.py:41`
- Depends on: `controllers/facade.py`
- Imported by: `app_factory.py`

### _facade_cover (function) `def _facade_cover()`
- Defined: `views/facade.py:48`
- Depends on: `controllers/facade.py`
- Imported by: `app_factory.py`

### facade_gate (function) `def facade_gate()`
- Defined: `views/facade.py:60`
- Depends on: `controllers/facade.py`
- Imported by: `app_factory.py`

## views/faq.py

### faq (function) `def faq()`
- Defined: `views/faq.py:7`
- Doc: Render the About page.
- Depends on: `models/plans.py`, `utils/utils.py`
- Imported by: `app_factory.py`

### landing (function) `def landing()`
- Defined: `views/faq.py:12`
- Doc: Render the About page.
- Depends on: `models/plans.py`, `utils/utils.py`
- Imported by: `app_factory.py`

## views/file.py

### upload (method) `def upload()`
- Defined: `views/file.py:25`
- Doc: Maneja la subida de archivos cifrados desde el cliente.
- Depends on: `views/auth.py`
- Imported by: `app_factory.py`

### download (method) `def download(filename)`
- Defined: `views/file.py:56`
- Doc: Provide the encrypted file and its key for client-side decryption.
- Depends on: `views/auth.py`
- Imported by: `app_factory.py`

## views/message.py

### messages (method) `def messages()`
- Defined: `views/message.py:29`
- Doc: Render the messages page; the browser handles all crypto.
- Depends on: `controllers/message.py`, `views/auth.py`
- Imported by: `app_factory.py`

### api_secure_message (method) `def api_secure_message()`
- Defined: `views/message.py:49`
- Doc: Accept an opaque end-to-end encrypted message envelope.
- Depends on: `controllers/message.py`, `views/auth.py`
- Imported by: `app_factory.py`

## views/privacy.py

### privacy (function) `def privacy()`
- Defined: `views/privacy.py:6`
- Doc: Render the About page.
- Imported by: `app_factory.py`

## views/subscription.py

### subscribe (method) `def subscribe()`
- Defined: `views/subscription.py:37`
- Doc: Maneja la selección de planes y el proceso de pago.
- Depends on: `models/plans.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`

### payment_success (method) `def payment_success()`
- Defined: `views/subscription.py:86`
- Doc: Maneja el éxito del pago y actualiza el plan del usuario.
- Depends on: `models/plans.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`

### __init__ (method) `def __init__(self)`
- Defined: `views/subscription.py:26`
- Depends on: `models/plans.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`

## views/sync.py

### secure_sync (function) `def secure_sync()`
- Defined: `views/sync.py:29`
- Doc: Receive an already-encrypted file + wrapped FEK and persist them.
- Depends on: `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`

### sync_page (function) `def sync_page()`
- Defined: `views/sync.py:79`
- Depends on: `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`

## views/terms.py

### terms (function) `def terms()`
- Defined: `views/terms.py:6`
- Doc: Render the About page.
- Imported by: `app_factory.py`

## views/views.py

### home (method) `def home()`
- Defined: `views/views.py:21`
- Doc: Render the landing/home page.
- Depends on: `models/user.py`, `utils/utils.py`
- Imported by: `app_factory.py`
