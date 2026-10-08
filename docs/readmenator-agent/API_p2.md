# API (page 2 of 2)
Previous: [API.md](API.md)

## views/auth.py
Depends on: `controllers/auth.py`, `controllers/contact.py`, `models/user.py`, `utils/mailer.py`, `utils/security.py`, `utils/utils.py`
Imported by: `app_factory.py`, `views/admin.py`, `views/file.py`, `views/message.py`, `views/subscription.py`
- `role_required` (function) `views/auth.py:71` `def role_required()` -- Restrict a route to authenticated users holding one of the given roles.
- `decorator` (method) `views/auth.py:85` `def decorator(f)`
- `decorated_function` (method) `views/auth.py:87` `def decorated_function()`
- `LoginForm.get_auth_controller` (method) `views/auth.py:132` `def get_auth_controller()`
- `LoginForm.show_register` (method) `views/auth.py:143` `def show_register()`
- `LoginForm.handle_register` (method) `views/auth.py:150` `def handle_register()`
- `LoginForm.login` (method) `views/auth.py:234` `def login()`
- `LoginForm.recover` (method) `views/auth.py:242` `def recover()` -- Render the QV-RECOVERY-1 account-recovery page.
- `LoginForm.srp_hello` (method) `views/auth.py:278` `def srp_hello()` -- First SRP-6a step: receive the client public value A, return salt and B.
- `LoginForm.srp_verify` (method) `views/auth.py:299` `def srp_verify()` -- Second SRP-6a step: verify the client proof M1 and return server proof M2.
- `LoginForm.logout` (method) `views/auth.py:337` `def logout()`
- `LoginForm.confirm_email` (method) `views/auth.py:344` `def confirm_email(token)`
- `LoginForm.verify_phone` (method) `views/auth.py:367` `def verify_phone()`
- `LoginForm.resend_phone_verification` (method) `views/auth.py:384` `def resend_phone_verification()` -- Re-send the phone verification code for an account.
- `LoginForm.verify_mfa` (method) `views/auth.py:407` `def verify_mfa()`
- `LoginForm.toggle_mfa` (method) `views/auth.py:429` `def toggle_mfa()`
- `LoginForm.contact` (method) `views/auth.py:454` `def contact()` -- Render the contact form and persist a message from the current user.
- `LoginForm.get_public_key` (method) `views/auth.py:485` `def get_public_key()` -- Return a user's hybrid public key so the browser can wrap data to them.
- `LoginForm.get_user_keys` (method) `views/auth.py:503` `def get_user_keys()` -- Provide the keys a user needs to decrypt their data client-side.
- `LoginForm.get_recovery_bundle` (method) `views/auth.py:534` `def get_recovery_bundle()` -- Return the QV-RECOVERY-1 bundle for a username, if one was generated.
- `LoginForm.reset_with_recovery` (method) `views/auth.py:559` `def reset_with_recovery()` -- Reset SRP credentials and the password-wrapped private key via QV-RECOVERY-1.
- `LoginForm.get_csrf_token` (method) `views/auth.py:619` `def get_csrf_token()` -- Issue the CSRF token used by the SPA for state-changing JSON calls.

## views/facade.py
Depends on: `controllers/facade.py`
Imported by: `app_factory.py`
- `register_facade` (function) `views/facade.py:33` `def register_facade(app)` -- Install the facade on ``app`` when it is enabled and configured.
- `render_cover` (function) `views/facade.py:41` `def render_cover()`
- `facade_gate` (function) `views/facade.py:60` `def facade_gate()`

## views/faq.py
Depends on: `models/plans.py`, `utils/utils.py`
Imported by: `app_factory.py`
- `faq` (function) `views/faq.py:7` `def faq()` -- Render the About page.
- `landing` (function) `views/faq.py:12` `def landing()` -- Render the About page.

## views/file.py
Depends on: `views/auth.py`
Imported by: `app_factory.py`
- `UploadForm.upload` (method) `views/file.py:25` `def upload()` -- Maneja la subida de archivos cifrados desde el cliente.
- `UploadForm.download` (method) `views/file.py:56` `def download(filename)` -- Provide the encrypted file and its key for client-side decryption.

## views/message.py
Depends on: `controllers/message.py`, `views/auth.py`
Imported by: `app_factory.py`
- `MessageForm.messages` (method) `views/message.py:29` `def messages()` -- Render the messages page; the browser handles all crypto.
- `MessageForm.api_secure_message` (method) `views/message.py:49` `def api_secure_message()` -- Accept an opaque end-to-end encrypted message envelope.

## views/privacy.py
Imported by: `app_factory.py`
- `privacy` (function) `views/privacy.py:6` `def privacy()` -- Render the About page.

## views/subscription.py
Depends on: `models/plans.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`
Imported by: `app_factory.py`
- `SubscriptionForm.__init__` (method) `views/subscription.py:26` `def __init__(self)`
- `SubscriptionForm.subscribe` (method) `views/subscription.py:37` `def subscribe()` -- Maneja la selección de planes y el proceso de pago.
- `SubscriptionForm.payment_success` (method) `views/subscription.py:86` `def payment_success()` -- Maneja el éxito del pago y actualiza el plan del usuario.

## views/sync.py
Depends on: `utils/security.py`, `utils/utils.py`
Imported by: `app_factory.py`
- `secure_sync` (function) `views/sync.py:29` `def secure_sync()` -- Receive an already-encrypted file + wrapped FEK and persist them.
- `sync_page` (function) `views/sync.py:79` `def sync_page()`

## views/terms.py
Imported by: `app_factory.py`
- `terms` (function) `views/terms.py:6` `def terms()` -- Render the About page.

## views/views.py
Depends on: `models/user.py`, `utils/utils.py`
Imported by: `app_factory.py`
- `MFAEnableForm.home` (method) `views/views.py:21` `def home()` -- Render the landing/home page.

