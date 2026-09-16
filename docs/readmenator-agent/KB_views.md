# Subsystem: views

## views/__init__.py
- Layer: presentation
- Language: py

## views/about.py
- Layer: presentation
- Language: py
- Symbols:
  - `about` (function, line 6) `def about()`
- Imported by: `app_factory.py`

## views/account.py
- Layer: presentation
- Language: py
- Symbols:
  - `get_deniable_vault_controller` (function, line 51) `def get_deniable_vault_controller()`
  - `settings` (function, line 65) `def settings()`
  - `get_vault` (function, line 85) `def get_vault()`
  - `put_vault` (function, line 107) `def put_vault()`
  - `delete_vault` (function, line 130) `def delete_vault()`
- Depends on: `controllers/deniable_vault.py`, `controllers/facade.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

## views/admin.py
- Layer: presentation
- Language: py
- Symbols:
  - `UserEditForm` (class, line 24) `class UserEditForm(FlaskForm)`
  - `PlanForm` (class, line 57) `class PlanForm(FlaskForm)`
  - `admin` (method, line 69) `def admin()`
  - `superadmin_edit_user` (method, line 91) `def superadmin_edit_user(username)`
  - `manage_plans` (method, line 196) `def manage_plans()`
  - `edit_plan` (method, line 220) `def edit_plan(plan_name)`
  - `superadmin` (method, line 256) `def superadmin()`
  - `superadmin_reset_mfa` (method, line 343) `def superadmin_reset_mfa(username)`
  - `superadmin_resend_confirmation` (method, line 391) `def superadmin_resend_confirmation(username)`
  - `superadmin_toggle_suspend` (method, line 439) `def superadmin_toggle_suspend(username)`
  - `admin_contacts` (method, line 490) `def admin_contacts()`
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

## views/auth.py
- Layer: presentation
- Language: py
- Symbols:
  - `role_required` (function, line 71) `def role_required()`
  - `PhoneVerificationForm` (class, line 98) `class PhoneVerificationForm(FlaskForm)`
  - `MFAForm` (class, line 103) `class MFAForm(FlaskForm)`
  - `ContactForm` (class, line 108) `class ContactForm(FlaskForm)`
  - `RegisterForm` (class, line 114) `class RegisterForm(FlaskForm)`
  - `LoginForm` (class, line 124) `class LoginForm(FlaskForm)`
  - `get_auth_controller` (method, line 132) `def get_auth_controller()`
  - `show_register` (method, line 143) `def show_register()`
  - `handle_register` (method, line 150) `def handle_register()`
  - `login` (method, line 234) `def login()`
  - `recover` (method, line 242) `def recover()`
  - `_srp_key` (method, line 255) `def _srp_key()`
  - `_recovery_key` (method, line 266) `def _recovery_key()`
  - `srp_hello` (method, line 278) `def srp_hello()`
  - `srp_verify` (method, line 299) `def srp_verify()`
  - `logout` (method, line 337) `def logout()`
  - `confirm_email` (method, line 344) `def confirm_email(token)`
  - `verify_phone` (method, line 367) `def verify_phone()`
  - `resend_phone_verification` (method, line 384) `def resend_phone_verification()`
  - `verify_mfa` (method, line 407) `def verify_mfa()`
  - `toggle_mfa` (method, line 429) `def toggle_mfa()`
  - `contact` (method, line 454) `def contact()`
  - `get_public_key` (method, line 485) `def get_public_key()`
  - `get_user_keys` (method, line 503) `def get_user_keys()`
  - `get_recovery_bundle` (method, line 534) `def get_recovery_bundle()`
  - `reset_with_recovery` (method, line 559) `def reset_with_recovery()`
  - `get_csrf_token` (method, line 619) `def get_csrf_token()`
  - `decorator` (method, line 85) `def decorator(f)`
  - `decorated_function` (method, line 87) `def decorated_function()`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

## views/facade.py
- Layer: presentation
- Language: py
- Symbols:
  - `register_facade` (function, line 33) `def register_facade(app)`
  - `_build_cover_service` (function, line 71) `def _build_cover_service(config)`
  - `_ticket_mode` (function, line 86) `def _ticket_mode(gate)`
  - `render_cover` (function, line 41) `def render_cover()`
  - `_facade_cover` (function, line 48) `def _facade_cover()`
  - `facade_gate` (function, line 60) `def facade_gate()`
- Depends on: `controllers/facade.py`
- Imported by: `app_factory.py`

## views/faq.py
- Layer: presentation
- Language: py
- Symbols:
  - `faq` (function, line 7) `def faq()`
  - `landing` (function, line 12) `def landing()`
- Depends on: `models/plans.py`, `utils/utils.py`
- Imported by: `app_factory.py`

## views/file.py
- Layer: presentation
- Language: py
- Symbols:
  - `UploadForm` (class, line 15) `class UploadForm(FlaskForm)`
  - `upload` (method, line 25) `def upload()`
  - `download` (method, line 56) `def download(filename)`
- Depends on: `views/auth.py`
- Imported by: `app_factory.py`

## views/message.py
- Layer: presentation
- Language: py
- Symbols:
  - `MessageForm` (class, line 19) `class MessageForm(FlaskForm)`
  - `messages` (method, line 29) `def messages()`
  - `api_secure_message` (method, line 49) `def api_secure_message()`
- Depends on: `controllers/message.py`, `views/auth.py`
- Imported by: `app_factory.py`

## views/privacy.py
- Layer: presentation
- Language: py
- Symbols:
  - `privacy` (function, line 6) `def privacy()`
- Imported by: `app_factory.py`

## views/subscription.py
- Layer: presentation
- Language: py
- Symbols:
  - `SubscriptionForm` (class, line 24) `class SubscriptionForm(FlaskForm)`
  - `subscribe` (method, line 37) `def subscribe()`
  - `payment_success` (method, line 86) `def payment_success()`
  - `__init__` (method, line 26) `def __init__(self)`
- Depends on: `models/plans.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`

## views/sync.py
- Layer: presentation
- Language: py
- Symbols:
  - `secure_sync` (function, line 29) `def secure_sync()`
  - `sync_page` (function, line 79) `def sync_page()`
- Depends on: `utils/security.py`, `utils/utils.py`
- Imported by: `app_factory.py`

## views/terms.py
- Layer: presentation
- Language: py
- Symbols:
  - `terms` (function, line 6) `def terms()`
- Imported by: `app_factory.py`

## views/views.py
- Layer: presentation
- Language: py
- Symbols:
  - `MFAEnableForm` (class, line 15) `class MFAEnableForm(FlaskForm)`
  - `home` (method, line 21) `def home()`
- Depends on: `models/user.py`, `utils/utils.py`
- Imported by: `app_factory.py`
