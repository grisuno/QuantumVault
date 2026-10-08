# views: auth

*Community 0 | 14 files | cohesion 0.44*

## Definition

This community groups 14 file(s) rooted at `views` with dominant language py (cohesion 0.44). Central symbols: `AuthController`, `Config`, `ContactForm`, `LoginForm`, `MFAEnableForm`, `MFAForm`, `MessageForm`, `Payload`. Core file: `views/auth.py` (29 symbols). Documented purpose: Zero-knowledge authentication controller for QuantumVault.  Registration accepts cryptographic material that the browser generated and stores it verbatim: the S.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `controllers/auth.py` | py | presentation | 14 | yes |
| `models/plans.py` | py | business_logic | 10 | no |
| `models/user.py` | py | presentation | 27 | no |
| `scripts/email_tool.py` | py | presentation | 6 | yes |
| `scripts/makeadmin.py` | py | utility | 5 | yes |
| `tests/test_utils.py` | py | testing | 3 | yes |
| `utils/mailer.py` | py | presentation | 3 | yes |
| `utils/utils.py` | py | presentation | 8 | yes |
| `views/auth.py` | py | presentation | 29 | yes |
| `views/faq.py` | py | presentation | 2 | no |
| `views/file.py` | py | presentation | 3 | no |
| `views/message.py` | py | presentation | 3 | no |
| `views/subscription.py` | py | presentation | 4 | no |
| `views/views.py` | py | presentation | 2 | yes |

## Key Symbols

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
- `PlanDB` (class, `models/plans.py:4`) `class PlanDB` - Database operations for subscription plans.
- `__init__` (method, `models/plans.py:6`) `def __init__(self, db_path)` - Initialize the PlanDB with the database path.
- `_init_db` (method, `models/plans.py:15`) `def _init_db(self)` - Initialize the plans table with required fields.
- `get_plan` (method, `models/plans.py:37`) `def get_plan(self, plan_name)` - Retrieve a plan by name.
- `get_all_plans` (method, `models/plans.py:50`) `def get_all_plans(self)` - Retrieve all plans.
- `create_plan` (method, `models/plans.py:60`) `def create_plan(self, name, storage_quota, trial_days, price)` - Create a new plan.
- `update_plan` (method, `models/plans.py:78`) `def update_plan(self, name, storage_quota, trial_days, price)` - Update an existing plan.
- `delete_plan` (method, `models/plans.py:113`) `def delete_plan(self, name)` - Delete a plan by name.
- `_convert_row_to_dict` (method, `models/plans.py:127`) `def _convert_row_to_dict(self, row)` - Convert an SQLite row to a dictionary.
- `validate_plan_payment` (method, `models/plans.py:139`) `def validate_plan_payment(self, plan_name, amount_paid)` - Validate that the paid amount matches the plan price.
- `UserModel` (class, `models/user.py:8`) `class UserModel(BaseModel, UserMixin)` - Pydantic model for a user with Flask-Login support.
- `get_id` (method, `models/user.py:52`) `def get_id(self)` - Return the user ID as a string (required by Flask-Login).
- `is_active` (method, `models/user.py:70`) `def is_active(self)` - Return True while the user can use the application.
- `UserDB` (class, `models/user.py:83`) `class UserDB` - Database operations for users.
- `__init__` (method, `models/user.py:85`) `def __init__(self, db_path)` - Initialize the UserDB with the database path.
- `_init_db` (method, `models/user.py:105`) `def _init_db(self)` - Initialize the users table with all fields for zero-knowledge auth.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 23
- Cross-boundary resolved imports (EXTRACTED): 30

## Connections

- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: app.py imports utils/utils.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: app_factory.py imports models/user.py.
- [EXTRACTED] depends_on community 0 <-> 5 (strength 0.9): Extracted import edge crosses communities: controllers/auth.py imports utils/__init__.py.
- [EXTRACTED] depends_on community 0 <-> 4 (strength 0.9): Extracted import edge crosses communities: controllers/auth.py imports utils/security.py.
- [INFERRED] shares_context community 0 <-> 6 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (views: auth) and community 6 (tools).
- [INFERRED] shares_context community 0 <-> 7 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (views: auth) and community 7 (orphans).

## Risks

- [taint high] `tests/test_secure_channel.py` -> `utils/utils.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/user.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `views/auth.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/plans.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `utils/mailer.py` via `subprocess` (3 hops)
- [taint high] `tests/test_secure_channel.py` -> `controllers/auth.py` via `subprocess` (3 hops)
- [layer strict] `scripts/test_bloque1.py` (testing) -> `models/user.py` (presentation)
- [layer strict] `tests/test_account_facade.py` (testing) -> `models/user.py` (presentation)
- [layer strict] `tests/test_deniable_vault.py` (testing) -> `models/user.py` (presentation)
- [layer strict] `tests/test_facade.py` (testing) -> `models/user.py` (presentation)
- [layer strict] `tests/test_utils.py` (testing) -> `utils/utils.py` (presentation)

## Open Questions

- Why do 6 file(s) lack file-level docs (e.g. `models/plans.py`)? What purpose do they serve?
- What would break if the most connected file in views: auth changed?
- Should views: auth be split, given cohesion 0.44?

## Sources

- `controllers/auth.py`
- `models/plans.py`
- `models/user.py`
- `scripts/email_tool.py`
- `scripts/makeadmin.py`
- `tests/test_utils.py`
- `utils/mailer.py`
- `utils/utils.py`
- `views/auth.py`
- `views/faq.py`
- `views/file.py`
- `views/message.py`
- `views/subscription.py`
- `views/views.py`
