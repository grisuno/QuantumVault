# Subsystem: views

## views/__init__.py
- Layer: presentation
- Language: py

## views/about.py
- Doc: about: Render the About page.
- Layer: presentation
- Language: py
- Symbols:
  - `about` (function, line 6) `def about()`
- Imported by: `quantumvault/app_factory.py`

## views/account.py
- Doc: Account settings page and the deniable vault JSON API (QV-DENIABLE-1).
- Layer: presentation
- Language: py
- Symbols:
  - `get_deniable_vault_controller` (function, line 51) `def get_deniable_vault_controller()`
  - `settings` (function, line 65) `def settings()`
  - `get_vault` (function, line 85) `def get_vault()`
  - `put_vault` (function, line 107) `def put_vault()`
  - `delete_vault` (function, line 130) `def delete_vault()`
- Depends on: `controllers/deniable_vault.py`, `controllers/facade.py`, `models/deniable_vault.py`, `utils/security.py`
- Imported by: `quantumvault/app_factory.py`

## views/admin.py
- Doc: UserEditForm: Form for editing user details.
- Layer: presentation
- Language: py
- Symbols:
  - `_audit_action` (function, line 31) `def _audit_action(actor, action, target_user, ip, details)`
  - `_channel_manager` (function, line 48) `def _channel_manager()`
  - `_s3_reachable` (function, line 54) `def _s3_reachable(timeout)`
  - `_read_log_tail` (function, line 84) `def _read_log_tail(state_dir, limit)`
  - `_channel_diagnostics` (function, line 116) `def _channel_diagnostics(manager)`
  - `UserEditForm` (class, line 141) `class UserEditForm(FlaskForm)`
  - `PlanForm` (class, line 174) `class PlanForm(FlaskForm)`
  - `admin` (function, line 186) `def admin()`
  - `superadmin_edit_user` (function, line 208) `def superadmin_edit_user(username)`
  - `manage_plans` (function, line 313) `def manage_plans()`
  - `edit_plan` (function, line 337) `def edit_plan(plan_name)`
  - `superadmin` (function, line 373) `def superadmin()`
  - `superadmin_reset_mfa` (function, line 476) `def superadmin_reset_mfa(username)`
  - `superadmin_resend_confirmation` (function, line 523) `def superadmin_resend_confirmation(username)`
  - `superadmin_toggle_suspend` (function, line 570) `def superadmin_toggle_suspend(username)`
  - `superadmin_channel_start` (function, line 620) `def superadmin_channel_start()`
  - `superadmin_channel_stop` (function, line 659) `def superadmin_channel_stop()`
  - `superadmin_channel_rotate` (function, line 682) `def superadmin_channel_rotate()`
  - `admin_contacts` (function, line 705) `def admin_contacts()`
- Depends on: `controllers/contact.py`, `controllers/secure_channel.py`, `models/plans.py`, `models/superadmin_audit.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `quantumvault/app_factory.py`, `scripts/test_bloque1.py`, `tests/test_secure_channel.py`

## views/auth.py
- Doc: Authentication and account-management views.
- Layer: presentation
- Language: py
- Symbols:
  - `role_required` (function, line 71) `def role_required()`
  - `PhoneVerificationForm` (class, line 98) `class PhoneVerificationForm(FlaskForm)`
  - `MFAForm` (class, line 103) `class MFAForm(FlaskForm)`
  - `ContactForm` (class, line 108) `class ContactForm(FlaskForm)`
  - `RegisterForm` (class, line 114) `class RegisterForm(FlaskForm)`
  - `LoginForm` (class, line 124) `class LoginForm(FlaskForm)`
  - `get_auth_controller` (function, line 132) `def get_auth_controller()`
  - `show_register` (function, line 143) `def show_register()`
  - `handle_register` (function, line 150) `def handle_register()`
  - `login` (function, line 234) `def login()`
  - `recover` (function, line 242) `def recover()`
  - `_srp_key` (function, line 255) `def _srp_key()`
  - `_recovery_key` (function, line 266) `def _recovery_key()`
  - `srp_hello` (function, line 278) `def srp_hello()`
  - `srp_verify` (function, line 299) `def srp_verify()`
  - `logout` (function, line 337) `def logout()`
  - `confirm_email` (function, line 344) `def confirm_email(token)`
  - `verify_phone` (function, line 367) `def verify_phone()`
  - `resend_phone_verification` (function, line 384) `def resend_phone_verification()`
  - `verify_mfa` (function, line 407) `def verify_mfa()`
  - `toggle_mfa` (function, line 429) `def toggle_mfa()`
  - `contact` (function, line 454) `def contact()`
  - `get_public_key` (function, line 485) `def get_public_key()`
  - `get_user_keys` (function, line 503) `def get_user_keys()`
  - `get_recovery_bundle` (function, line 534) `def get_recovery_bundle()`
  - `reset_with_recovery` (function, line 559) `def reset_with_recovery()`
  - `get_csrf_token` (function, line 619) `def get_csrf_token()`
  - `decorator` (function, line 85) `def decorator(f)`
  - `decorated_function` (function, line 87) `def decorated_function()`
- Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
- Imported by: `quantumvault/app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`

## views/facade.py
- Doc: Cover facade HTTP integration: before-request cover and the gate endpoint.
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
- Imported by: `quantumvault/app_factory.py`

## views/faq.py
- Doc: faq: Render the About page.
- Layer: presentation
- Language: py
- Symbols:
  - `faq` (function, line 7) `def faq()`
  - `landing` (function, line 12) `def landing()`
- Depends on: `models/plans.py`, `utils/utils.py`
- Imported by: `quantumvault/app_factory.py`

## views/file.py
- Doc: UploadForm: Formulario para la subida de archivos cifrados.
- Layer: presentation
- Language: py
- Symbols:
  - `UploadForm` (class, line 15) `class UploadForm(FlaskForm)`
  - `upload` (function, line 25) `def upload()`
  - `download` (function, line 56) `def download(filename)`
- Depends on: `views/auth.py`
- Imported by: `quantumvault/app_factory.py`

## views/message.py
- Doc: MessageForm: Form for sending messages.
- Layer: presentation
- Language: py
- Symbols:
  - `MessageForm` (class, line 19) `class MessageForm(FlaskForm)`
  - `messages` (function, line 29) `def messages()`
  - `api_secure_message` (function, line 49) `def api_secure_message()`
- Depends on: `controllers/message.py`, `views/auth.py`
- Imported by: `quantumvault/app_factory.py`

## views/privacy.py
- Doc: privacy: Render the About page.
- Layer: presentation
- Language: py
- Symbols:
  - `privacy` (function, line 6) `def privacy()`
- Imported by: `quantumvault/app_factory.py`

## views/subscription.py
- Doc: SubscriptionForm: Formulario para seleccionar un plan de suscripción.
- Layer: presentation
- Language: py
- Symbols:
  - `SubscriptionForm` (class, line 24) `class SubscriptionForm(FlaskForm)`
  - `subscribe` (function, line 37) `def subscribe()`
  - `payment_success` (function, line 86) `def payment_success()`
  - `__init__` (method, line 26) `def __init__(self)`
- Depends on: `models/plans.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
- Imported by: `quantumvault/app_factory.py`

## views/sync.py
- Doc: End-to-end encrypted file synchronization views.
- Layer: presentation
- Language: py
- Symbols:
  - `secure_sync` (function, line 29) `def secure_sync()`
  - `sync_page` (function, line 79) `def sync_page()`
- Depends on: `utils/security.py`, `utils/utils.py`
- Imported by: `quantumvault/app_factory.py`

## views/terms.py
- Doc: terms: Render the About page.
- Layer: presentation
- Language: py
- Symbols:
  - `terms` (function, line 6) `def terms()`
- Imported by: `quantumvault/app_factory.py`

## views/views.py
- Doc: Top-level non-API views: home page, account preferences, etc.
- Layer: presentation
- Language: py
- Symbols:
  - `MFAEnableForm` (class, line 15) `class MFAEnableForm(FlaskForm)`
  - `home` (function, line 21) `def home()`
- Depends on: `models/user.py`, `utils/utils.py`
- Imported by: `quantumvault/app_factory.py`
