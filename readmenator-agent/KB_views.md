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
  - `get_deniable_vault_controller` (function, line 50) `def get_deniable_vault_controller()`
  - `settings` (function, line 64) `def settings()`
  - `get_vault` (function, line 77) `def get_vault()`
  - `put_vault` (function, line 99) `def put_vault()`
  - `delete_vault` (function, line 122) `def delete_vault()`
- Depends on: `controllers/deniable_vault.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `app_factory.py`

## views/admin.py
- Layer: presentation
- Language: py
- Symbols:
  - `UserEditForm` (class, line 23) `class UserEditForm(FlaskForm)`
  - `PlanForm` (class, line 56) `class PlanForm(FlaskForm)`
  - `admin` (method, line 68) `def admin()`
  - `superadmin_edit_user` (method, line 90) `def superadmin_edit_user(username)`
  - `manage_plans` (method, line 195) `def manage_plans()`
  - `edit_plan` (method, line 219) `def edit_plan(plan_name)`
  - `superadmin` (method, line 255) `def superadmin()`
  - `superadmin_reset_mfa` (method, line 342) `def superadmin_reset_mfa(username)`
  - `superadmin_resend_confirmation` (method, line 390) `def superadmin_resend_confirmation(username)`
  - `superadmin_toggle_suspend` (method, line 438) `def superadmin_toggle_suspend(username)`
  - `admin_contacts` (method, line 489) `def admin_contacts()`
- Depends on: `controllers/contact.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `app_factory.py`, `scripts/test_bloque1.py`

## views/auth.py
- Layer: presentation
- Language: py
- Symbols:
  - `role_required` (function, line 70) `def role_required()`
  - `PhoneVerificationForm` (class, line 97) `class PhoneVerificationForm(FlaskForm)`
  - `MFAForm` (class, line 102) `class MFAForm(FlaskForm)`
  - `ContactForm` (class, line 107) `class ContactForm(FlaskForm)`
  - `RegisterForm` (class, line 113) `class RegisterForm(FlaskForm)`
  - `LoginForm` (class, line 123) `class LoginForm(FlaskForm)`
  - `get_auth_controller` (method, line 131) `def get_auth_controller()`
  - `show_register` (method, line 142) `def show_register()`
  - `handle_register` (method, line 149) `def handle_register()`
  - `login` (method, line 233) `def login()`
  - `recover` (method, line 241) `def recover()`
  - `_srp_key` (method, line 254) `def _srp_key()`
  - `_recovery_key` (method, line 265) `def _recovery_key()`
  - `srp_hello` (method, line 277) `def srp_hello()`
  - `srp_verify` (method, line 298) `def srp_verify()`
  - `logout` (method, line 336) `def logout()`
  - `confirm_email` (method, line 343) `def confirm_email(token)`
  - `verify_phone` (method, line 366) `def verify_phone()`
  - `resend_phone_verification` (method, line 383) `def resend_phone_verification()`
  - `verify_mfa` (method, line 406) `def verify_mfa()`
  - `toggle_mfa` (method, line 428) `def toggle_mfa()`
  - `contact` (method, line 453) `def contact()`
  - `get_public_key` (method, line 484) `def get_public_key()`
  - `get_user_keys` (method, line 502) `def get_user_keys()`
  - `get_recovery_bundle` (method, line 533) `def get_recovery_bundle()`
  - `reset_with_recovery` (method, line 558) `def reset_with_recovery()`
  - `get_csrf_token` (method, line 618) `def get_csrf_token()`
  - `decorator` (method, line 84) `def decorator(f)`
  - `decorated_function` (method, line 86) `def decorated_function()`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`
- Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

## views/faq.py
- Layer: presentation
- Language: py
- Symbols:
  - `faq` (function, line 6) `def faq()`
  - `landing` (function, line 11) `def landing()`
- Depends on: `models/plans.py`
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
- Depends on: `models/plans.py`, `models/user.py`, `views/auth.py`
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
  - `MFAEnableForm` (class, line 14) `class MFAEnableForm(FlaskForm)`
  - `home` (method, line 20) `def home()`
- Depends on: `models/user.py`
- Imported by: `app_factory.py`
