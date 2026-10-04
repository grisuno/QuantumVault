# views

*Community 0 | 53 files | cohesion 0.99*

## Definition

This community groups 53 file(s) rooted at `views` with dominant language py (cohesion 0.99). Central symbols: `AssetReference`, `AuthController`, `ChannelMode`, `ChannelStatus`, `Config`, `ContactController`, `ContactDB`, `ContactForm`. Core file: `tests/test_secure_channel.py` (67 symbols). Documented purpose: Local development entry point.  This script exists for the ``make run`` workflow: the Werkzeug dev server with SSL on the loopback port. It is the only place in.

## Files

### `views` (13 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `views/about.py` | py | presentation | 1 | no |
| `views/account.py` | py | presentation | 5 | yes |
| `views/admin.py` | py | presentation | 19 | no |

### `tests` (11 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/conftest.py` | py | testing | 8 | yes |
| `tests/test_account_facade.py` | py | testing | 6 | yes |
| `tests/test_cover.py` | py | testing | 52 | yes |

### `controllers` (8 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `controllers/auth.py` | py | presentation | 14 | yes |
| `controllers/contact.py` | py | presentation | 4 | no |
| `controllers/deniable_vault.py` | py | presentation | 22 | yes |

### `models` (6 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `models/contact.py` | py | presentation | 9 | no |
| `models/deniable_vault.py` | py | business_logic | 6 | yes |

### `utils` (6 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `utils/integrity.py` | py | utility | 8 | yes |
| `utils/mailer.py` | py | presentation | 3 | yes |

### `.` (3 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 2 | yes |
| `app_factory.py` | py | presentation | 8 | yes |

### `scripts` (3 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `scripts/email_tool.py` | py | presentation | 6 | yes |
| `scripts/makeadmin.py` | py | utility | 5 | yes |

### `tools` (2 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tools/generate_sri.py` | py | utility | 5 | yes |
| `tools/verify_build.py` | py | presentation | 11 | yes |

### `static/js` (1 files)

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `static/js/qv-padding.js` | js | infrastructure | 5 | yes |

*... and 33 more files in this community.*


## Key Symbols

- `main` (function, `app.py:21`) `def main()`
- `_is_production_like` (function, `app.py:58`) `def _is_production_like()` - Return True if the runtime looks like a public-facing deployment.
- `_is_production` (function, `app_factory.py:71`) `def _is_production()` - Return True unless the operator explicitly opts into dev mode.
- `_build_csp` (function, `app_factory.py:82`) `def _build_csp()` - Return the strict Content-Security-Policy used in production.
- `_build_talisman_kwargs` (function, `app_factory.py:119`) `def _build_talisman_kwargs()` - Return kwargs to pass to ``Talisman`` based on the runtime env.
- `_configure_secret_key` (function, `app_factory.py:160`) `def _configure_secret_key(app, config)` - Set ``app.config['SECRET_KEY']`` from env, payload.json, or a random value.
- `_configure_session` (function, `app_factory.py:203`) `def _configure_session(app)` - Apply session lifetime and cookie hardening.
- `_configure_logging` (function, `app_factory.py:220`) `def _configure_logging(app)` - Wire up a structured application logger.
- `create_app` (function, `app_factory.py:237`) `def create_app(config_overrides, security_overrides)` - Build and return a fully-configured Flask application.
- `load_user` (function, `app_factory.py:416`) `def load_user(user_id)`
- `_now_utc` (function, `controllers/auth.py:49`) `def _now_utc()` - Return the current time as a timezone-aware UTC datetime.
- `AuthController` (class, `controllers/auth.py:58`) `class AuthController` - Handles zero-knowledge registration and SRP-6a authentication.
- `__init__` (method, `controllers/auth.py:61`) `def __init__(self, db_path, mail, storage_uri)` - Initialize the controller.
- `register` (method, `controllers/auth.py:76`) `def register(self, username, srp_salt, srp_verifier, public_key, encrypted_priva` - Register a user from client-generated zero-knowledge credentials.
- `send_confirmation_email` (method, `controllers/auth.py:156`) `def send_confirmation_email(self, email, username, token)` - Email the account-confirmation link to a freshly registered user.
- `srp_hello` (method, `controllers/auth.py:202`) `def srp_hello(self, username, client_a_hex)` - Begin an SRP-6a login and return the salt and server challenge B.
- `srp_verify` (method, `controllers/auth.py:221`) `def srp_verify(self, username, client_m1_hex)` - Complete an SRP-6a login and return the authenticated user and proof.
- `send_sms_verification` (method, `controllers/auth.py:253`) `def send_sms_verification(self, phone, code, username)` - Send a verification code via SMS.
- `verify_phone_code` (method, `controllers/auth.py:274`) `def verify_phone_code(self, username, code)` - Verify a phone verification code for a user.
- `resend_phone_code` (method, `controllers/auth.py:310`) `def resend_phone_code(self, username)` - Issue and send a fresh phone verification code.
- `_is_code_valid` (method, `controllers/auth.py:349`) `def _is_code_valid(self, expires_at)` - Return True if a verification code has not yet expired.
- `verify_mfa_code` (method, `controllers/auth.py:369`) `def verify_mfa_code(self, username, code)` - Verify a multi-factor authentication code for a user.
- `send_mfa_code` (method, `controllers/auth.py:393`) `def send_mfa_code(self, username)` - Generate, store, and send an MFA code to the user's phone.
- `toggle_mfa` (method, `controllers/auth.py:416`) `def toggle_mfa(self, username, enable)` - Enable or disable MFA for a user.
- `ContactController` (class, `controllers/contact.py:4`) `class ContactController` - Handles logic related to contact messages.
- `__init__` (method, `controllers/contact.py:6`) `def __init__(self, db_path)` - Initialize the ContactController with the database path.
- `create_contact` (method, `controllers/contact.py:14`) `def create_contact(self, user_id, subject, message)` - Create a new contact message.
- `get_user_contacts` (method, `controllers/contact.py:36`) `def get_user_contacts(self, user_id)` - Retrieve all contact messages for a user.
- `_base64_length` (function, `controllers/deniable_vault.py:81`) `def _base64_length(byte_length)` - Return the length of the standard base64 encoding of ``byte_length`` bytes.
- `canonical_json` (function, `controllers/deniable_vault.py:86`) `def canonical_json(envelope)` - Serialize an envelope deterministically for storage and sizing.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 112
- Cross-boundary resolved imports (EXTRACTED): 1

## Connections

- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: static/js/qv-crypto.js imports static/js/qv-padding.js.
- [INFERRED] shares_context community 0 <-> 2 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (views) and community 2 (orphans).
- [INFERRED] bridges community 0 <-> 1 (strength 0.4): Inferred cross-community bridge: models/contact.py reaches static/js/account.js in 9 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.4): Inferred cross-community bridge: controllers/contact.py reaches static/js/account.js in 8 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.4): Inferred cross-community bridge: controllers/deniable_vault.py reaches static/js/account.js in 8 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.4): Inferred cross-community bridge: controllers/facade.py reaches static/js/account.js in 8 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.4): Inferred cross-community bridge: controllers/secure_channel.py reaches static/js/account.js in 8 hops.

## Risks

- [taint high] `controllers/secure_channel.py` -> `controllers/secure_channel.py` via `subprocess` (0 hops)
- [taint high] `tests/test_secure_channel.py` -> `tests/test_secure_channel.py` via `subprocess` (0 hops)
- [taint high] `tests/test_secure_channel.py` -> `views/admin.py` via `subprocess` (1 hops)
- [taint high] `tests/test_secure_channel.py` -> `controllers/secure_channel.py` via `subprocess` (1 hops)
- [taint high] `tests/test_secure_channel.py` -> `views/auth.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/user.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/superadmin_audit.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `utils/utils.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/plans.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `controllers/contact.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `controllers/auth.py` via `subprocess` (3 hops)
- [taint high] `tests/test_secure_channel.py` -> `utils/mailer.py` via `subprocess` (3 hops)
- [taint high] `tests/test_secure_channel.py` -> `utils/security.py` via `subprocess` (3 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/contact.py` via `subprocess` (3 hops)
- [taint medium] `tools/generate_sri.py` -> `tools/generate_sri.py` via `urllib.request` (0 hops)

## Open Questions

- Why do 12 file(s) lack file-level docs (e.g. `controllers/contact.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `controllers/secure_channel.py` still required, or can it be isolated?
- What would break if the most connected file in views changed?
- Should views be split, given cohesion 0.99?

## Sources

- `app.py`
- `app_factory.py`
- `controllers/auth.py`
- `controllers/contact.py`
- `controllers/deniable_vault.py`
- `controllers/facade.py`
- `controllers/file.py`
- `controllers/message.py`
- `controllers/secure_channel.py`
- `controllers/sync.py`
- `models/contact.py`
- `models/deniable_vault.py`
- `models/message.py`
- `models/plans.py`
- `models/superadmin_audit.py`
- `models/user.py`
- `scripts/email_tool.py`
- `scripts/makeadmin.py`
- `scripts/test_bloque1.py`
- `static/js/qv-padding.js`
- *... and 33 more*
