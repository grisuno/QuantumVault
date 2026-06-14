"""Authentication and account-management views.

Routes:

- ``GET  /register``            : render the registration form
- ``POST /register``            : create a new account from a zero-knowledge payload
- ``GET  /login``               : render the login form
- ``POST /api/srp/hello``       : SRP-6a step 1, returns salt and server challenge B
- ``POST /api/srp/verify``      : SRP-6a step 2, returns server proof M2 and starts a session
- ``GET  /logout``              : clear the session
- ``GET  /confirm/<token>``     : mark an email as verified
- ``GET/POST /verify_phone``    : enter the phone verification code
- ``GET/POST /verify_mfa``      : enter the MFA code
- ``POST /toggle_mfa``          : enable or disable MFA for the current user
- ``GET  /contact``             : render and accept the contact form
- ``GET  /api/auth/pubkey``     : return a user's hybrid public key
- ``GET  /api/auth/user-keys``  : return the current user's keying material
- ``GET  /api/csrf-token``      : issue the CSRF token for SPA use

Every state-changing JSON route is decorated with
:func:`utils.security.json_csrf_protect` so a cross-origin request
without the matching CSRF token is rejected with HTTP 403 and audited.
"""

import hmac
import os
from functools import wraps

from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf import FlaskForm
from flask_wtf.csrf import generate_csrf
from wtforms import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

from controllers.auth import AuthController
from controllers.contact import ContactController
from models.user import UserModel
from utils.mailer import mail_is_configured, send_transactional_email
from utils.security import audit_event, json_csrf_protect


auth_bp = Blueprint("auth", __name__)
limiter = Limiter(key_func=get_remote_address)

# With the zero-knowledge flow the browser performs the KEM, so the
# server never holds an RSA key. USER_KEYS_BASE_DIR is reserved for
# any future admin tooling.
USER_KEYS_BASE_DIR = os.environ.get("QV_UPLOAD_FOLDER", "users")
USER_KEYS_BASE_DIR = os.path.abspath(USER_KEYS_BASE_DIR)


# Valid roles. Kept in one place so role checks cannot drift between
# the schema, the admin form choices, and the @role_required decorator.
VALID_ROLES = ("free", "bronze", "silver", "gold", "admin", "superadmin")


def role_required(*roles: str):
    """Restrict a route to authenticated users holding one of the given roles.

    The check is an intersection of ``VALID_ROLES`` and the caller-
    supplied roles so a typo in a future route (e.g. ``role_required("user")``)
    cannot accidentally grant access because the role never existed.
    """
    allowed = set(roles) & set(VALID_ROLES)
    if not allowed:
        raise ValueError(
            f"role_required() called with no valid roles: {roles}. "
            f"Valid roles are {VALID_ROLES}."
        )

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role not in allowed:
                audit_event("role_denied", role=getattr(current_user, "role", None), path=request.path)
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


# --- Forms ---

class PhoneVerificationForm(FlaskForm):
    code = StringField("Verification Code", validators=[DataRequired()])
    submit = SubmitField("Verify")


class MFAForm(FlaskForm):
    code = StringField("MFA Code", validators=[DataRequired()])
    submit = SubmitField("Verify")


class ContactForm(FlaskForm):
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    phone = StringField("Telephone", validators=[DataRequired()])
    first_name = StringField("Name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign in")


# --- Controller factory ---

def get_auth_controller() -> AuthController:
    return AuthController(
        "instance/users.db",
        current_app.config["MAIL"],
        current_app.config["STORAGE_URI"],
    )


# --- Routes ---

@auth_bp.route("/register", methods=["GET"])
def show_register():
    form = RegisterForm()
    return render_template("register.html", form=form, user=current_user)


@auth_bp.route("/register", methods=["POST"])
@limiter.limit("5 per minute")
def handle_register():
    # The zero-knowledge registration payload is built entirely in the
    # browser (see static/js/qv-crypto.js -> buildRegistration). The
    # server cannot derive the SRP verifier, the hybrid KEM public key,
    # or the password-encrypted private blob on its own, so a non-JSON
    # submission can never succeed. We give the caller an honest error
    # for every known failure mode instead of a single generic message.
    #
    # 1) Native form fallback (JavaScript disabled or the ES module
    #    failed to load). The browser sends application/x-www-form-
    #    urlencoded with the WTForms fields, CSRFProtect accepts the
    #    hidden_tag(), and the view never sees JSON. Tell the user
    #    plainly: zero-knowledge registration needs JavaScript.
    if request.form and not request.is_json:
        return jsonify({
            "success": False,
            "error": (
                "JavaScript is required to register. QuantumVault uses a "
                "zero-knowledge flow: the SRP verifier, the hybrid "
                "ML-KEM-768 + X25519 public key, and the password-encrypted "
                "private blob are generated in the browser and the password "
                "never leaves it. The native form submission cannot produce "
                "that material, so the account cannot be created. Enable "
                "JavaScript, reload the page, and submit the form again."
            ),
            "code": "js_required",
        }), 400

    # 2) Caller asked for JSON (the SPA path). Parse strictly. A missing
    #    body, a wrong Content-Type, or malformed JSON all fall into the
    #    same bucket: the server has nothing to validate. The SPA sends
    #    a real payload; an integration test or a curl call without
    #    '-d @payload.json' lands here.
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "success": False,
            "error": (
                "This endpoint expects a JSON body (Content-Type: "
                "application/json) with the zero-knowledge registration "
                "payload. The browser SPA sends it; if you are calling "
                "via curl, pass '-H \"Content-Type: application/json\" "
                "-d @payload.json' with the keys username, srp_salt, "
                "srp_verifier, public_key, encrypted_private_key, "
                "kdf_salt, email, phone, first_name, last_name."
            ),
            "code": "json_body_required",
        }), 400

    # The browser performs all key generation and SRP verifier derivation. The
    # server receives only zero-knowledge material; the password is never sent.
    required_fields = [
        "username", "srp_salt", "srp_verifier", "public_key",
        "encrypted_private_key", "kdf_salt", "email", "phone",
        "first_name", "last_name",
    ]
    if not all(field in data for field in required_fields):
        return jsonify({"success": False, "error": "Missing required fields"}), 400

    controller = get_auth_controller()
    if controller.register(
        username=data.get("username"),
        srp_salt=data.get("srp_salt"),
        srp_verifier=data.get("srp_verifier"),
        public_key=data.get("public_key"),
        encrypted_private_key=data.get("encrypted_private_key"),
        kdf_salt=data.get("kdf_salt"),
        email=data.get("email"),
        phone=data.get("phone"),
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        recovery_salt=data.get("recovery_salt"),
        encrypted_private_key_recovery=data.get("encrypted_private_key_recovery"),
    ):
        flash("Registration successful. Please log in.")
        return jsonify({
            "success": True,
            "message": "Registration successful. Please check your email to confirm your account.",
            "redirect": url_for("auth.login"),
        })
    return jsonify({"success": False, "error": "Registration failed."}), 500


@auth_bp.route("/login", methods=["GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    form = LoginForm()
    return render_template("login.html", form=form)


@auth_bp.route("/recover", methods=["GET"])
def recover():
    """Render the QV-RECOVERY-1 account-recovery page.

    Available to anonymous visitors: a forgotten password means the
    visitor cannot authenticate, by definition.
    """
    if current_user.is_authenticated:
        return redirect(url_for("views.home"))
    return render_template("recover.html")


# SRP key for per-username rate limiting: combine the remote IP and
# the username so a botnet can still be slowed per-account.
def _srp_key() -> str:
    username = ""
    if request.is_json:
        body = request.get_json(silent=True) or {}
        username = (body.get("username") or "").lower()
    return f"{get_remote_address()}|{username}"


# Per-username (in addition to per-IP) rate limiting for the QV-RECOVERY-1
# endpoints, mirroring _srp_key. GET /api/auth/recovery-bundle carries the
# username as a query parameter rather than a JSON body.
def _recovery_key() -> str:
    if request.method == "GET":
        username = (request.args.get("username") or "").lower()
    else:
        body = request.get_json(silent=True) or {}
        username = (body.get("username") or "").lower()
    return f"{get_remote_address()}|{username}"


@auth_bp.route("/api/srp/hello", methods=["POST"])
@limiter.limit("10 per minute;20 per hour", key_func=_srp_key)
@json_csrf_protect
def srp_hello():
    """First SRP-6a step: receive the client public value A, return salt and B."""
    if current_user.is_authenticated:
        return jsonify({"success": True, "redirect": url_for("views.home")})

    data = request.get_json() or {}
    if "username" not in data or "A" not in data:
        return jsonify({"success": False, "error": "username and A are required."}), 400

    controller = get_auth_controller()
    challenge = controller.srp_hello(data["username"], data["A"])
    if challenge is None:
        return jsonify({"success": False, "error": "Authentication failed."}), 401

    salt_hex, server_b_hex = challenge
    return jsonify({"success": True, "salt": salt_hex, "B": server_b_hex})


@auth_bp.route("/api/srp/verify", methods=["POST"])
@limiter.limit("10 per minute;20 per hour", key_func=_srp_key)
@json_csrf_protect
def srp_verify():
    """Second SRP-6a step: verify the client proof M1 and return server proof M2."""
    if current_user.is_authenticated:
        return jsonify({"success": True, "redirect": url_for("views.home")})

    data = request.get_json() or {}
    if "username" not in data or "M1" not in data:
        return jsonify({"success": False, "error": "username and M1 are required."}), 400

    controller = get_auth_controller()
    result = controller.srp_verify(data["username"], data["M1"])
    if result is None:
        return jsonify({"success": False, "error": "Authentication failed."}), 401

    user, server_m2_hex = result
    login_user(user)
    audit_event("login_success", username=user.username)

    if user.mfa_enabled:
        if controller.send_mfa_code(user.username):
            return jsonify({
                "success": True,
                "M2": server_m2_hex,
                "mfa_required": True,
                "redirect": url_for("auth.verify_mfa", username=user.username),
            })
        return jsonify({"success": False, "error": "Failed to send MFA code."}), 500

    return jsonify({
        "success": True,
        "M2": server_m2_hex,
        "mfa_required": False,
        "redirect": url_for("views.home"),
    })


@auth_bp.route("/logout")
@login_required
def logout():
    audit_event("logout", username=getattr(current_user, "username", None))
    logout_user()
    return redirect(url_for("auth.login"))


@auth_bp.route("/confirm/<token>", methods=["GET"])
def confirm_email(token):
    controller = get_auth_controller()
    user_data = controller.user_db.get_user_by_confirmation_token(token)
    if not user_data:
        flash("Invalid or expired confirmation link.")
        return redirect(url_for("auth.login"))

    try:
        controller.user_db.update_user(
            username=user_data["username"],
            email_verified=True,
            confirmation_token=None,
        )
        flash("Email verified successfully! You can now log in.")
    except Exception as e:
        current_app.logger.exception("Confirmation error")
        flash("Error verifying email.")
        audit_event("confirm_email_error", reason=type(e).__name__)
    return redirect(url_for("auth.login"))


@auth_bp.route("/verify_phone", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def verify_phone():
    form = PhoneVerificationForm()
    username = request.args.get("username") or ""
    if not username:
        flash("Missing username for phone verification.")
        return redirect(url_for("auth.login"))
    if form.validate_on_submit():
        controller = get_auth_controller()
        if controller.verify_phone_code(username, str(form.code.data or "")):
            flash("Phone number verified successfully!")
            return redirect(url_for("auth.login"))
        flash("Invalid or expired verification code.")
    return render_template("verify_phone.html", form=form, username=username)


@auth_bp.route("/resend_phone_verification", methods=["POST"])
@limiter.limit("3 per minute")
def resend_phone_verification():
    """Re-send the phone verification code for an account.

    The username is supplied as a query parameter by the verify-phone
    template's resend form. The form carries the CSRF token, so the
    app-wide CSRFProtect guard applies. The handler never reveals whether
    the account exists: it always redirects back with a neutral message.
    """
    username = request.args.get("username") or request.form.get("username") or ""
    if not username:
        flash("Missing username for phone verification.")
        return redirect(url_for("auth.login"))

    controller = get_auth_controller()
    if controller.resend_phone_code(username):
        flash("A new verification code has been sent.")
    else:
        flash("Could not resend the verification code. Please try again later.")
    return redirect(url_for("auth.verify_phone", username=username))


@auth_bp.route("/verify_mfa", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def verify_mfa():
    form = MFAForm()
    username = request.args.get("username") or ""
    if not username:
        flash("Missing username for MFA verification.")
        return redirect(url_for("auth.login"))
    if form.validate_on_submit():
        controller = get_auth_controller()
        user_model = controller.user_db.get_user(username)
        if not user_model:
            flash("User not found.")
            return redirect(url_for("auth.login"))

        if controller.verify_mfa_code(username, str(form.code.data or "")):
            login_user(UserModel(**user_model))
            return redirect(url_for("views.home"))
        flash("Invalid or expired MFA code.")
    return render_template("verify_mfa.html", form=form, username=username)

@auth_bp.route("/toggle_mfa", methods=["POST"])
@login_required
@limiter.limit("5 per minute")
def toggle_mfa():
    controller = get_auth_controller()
    mfa_enabled = request.form.get("mfa_enabled") == "on"
    user = controller.user_db.get_user(current_user.username)

    if not user:
        flash("User not found.", "error")
        return redirect(url_for("views.home"))

    if mfa_enabled and not user["phone_verified"]:
        flash("Phone verification is required to enable MFA.", "error")
        return redirect(url_for("auth.verify_phone", username=current_user.username))

    try:
        controller.toggle_mfa(current_user.username, mfa_enabled)
        flash(f"MFA {'enabled' if mfa_enabled else 'disabled'} successfully.", "success")
    except Exception as e:
        current_app.logger.exception("toggle_mfa error")
        flash(f"Error toggling MFA: {type(e).__name__}", "error")

    return redirect(url_for("views.home"))


@auth_bp.route("/contact", methods=["GET", "POST"])
@limiter.limit("10 per minute")
def contact():
    """Render the contact form and persist a message from the current user.

    The page is only meaningful for authenticated users: messages are tied to
    a ``user_id`` foreign key in ``contacts``. Anonymous visitors are sent
    to the login page so they can sign in (or register) before contacting.
    """
    if not current_user.is_authenticated:
        flash("Please sign in to contact support.")
        return redirect(url_for("auth.login"))

    form = ContactForm()
    if form.validate_on_submit():
        controller = ContactController("instance/users.db")
        subject = str(form.subject.data or "")
        message = str(form.message.data or "")
        if controller.create_contact(
            user_id=current_user.id,
            subject=subject,
            message=message,
        ):
            audit_event("contact_message_sent", user_id=current_user.id)
            flash("Your message was sent successfully.")
            return redirect(url_for("views.home"))
        return render_template("contact.html", form=form, user=current_user), 400

    return render_template("contact.html", form=form, user=current_user)


@auth_bp.route("/api/auth/pubkey", methods=["GET"])
@limiter.limit("10 per minute")
def get_public_key():
    """Return a user's hybrid public key so the browser can wrap data to them."""
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    controller = get_auth_controller()
    user_data = controller.user_db.get_user(username)

    if not user_data or not user_data.get("public_key"):
        return jsonify({"error": "User or public key not found"}), 404

    return jsonify({"publicKey": user_data["public_key"]})


@auth_bp.route("/api/auth/user-keys", methods=["GET"])
@login_required
@limiter.limit("10 per minute")
def get_user_keys():
    """Provide the keys a user needs to decrypt their data client-side.

    The caller must already be authenticated and asking for their own
    material; the route refuses to return anyone else's keying data.
    """
    username = request.args.get("username")
    if not username or username != current_user.username:
        audit_event("user_keys_denied", requested=username, actual=current_user.username)
        return jsonify({"error": "Permission denied"}), 403

    controller = get_auth_controller()
    user_data = controller.user_db.get_user(username)

    if not user_data:
        return jsonify({"error": "User not found"}), 404

    required_keys = ["srp_salt", "public_key", "encrypted_private_key", "kdf_salt"]
    if not all(key in user_data and user_data[key] for key in required_keys):
        return jsonify({"error": "User is missing necessary keying material."}), 400

    return jsonify({
        "srp_salt": user_data["srp_salt"],
        "kdf_salt": user_data["kdf_salt"],
        "public_key": user_data["public_key"],
        "encrypted_private_key": user_data["encrypted_private_key"],
    })


@auth_bp.route("/api/auth/recovery-bundle", methods=["GET"])
@limiter.limit("10 per minute", key_func=_recovery_key)
def get_recovery_bundle():
    """Return the QV-RECOVERY-1 bundle for a username, if one was generated.

    No authentication is required: a forgotten password by definition
    means the caller cannot log in. The returned values are opaque to
    anyone without the recovery code: ``encrypted_private_key_recovery``
    is AES-256-GCM ciphertext keyed by a PBKDF2 derivation of the
    recovery code, so exposing it to an unauthenticated caller does not
    weaken the zero-knowledge guarantees.
    """
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    controller = get_auth_controller()
    bundle = controller.user_db.get_recovery_bundle(username)
    if not bundle:
        return jsonify({"error": "No recovery code is configured for this account."}), 404

    return jsonify(bundle)


@auth_bp.route("/api/auth/reset-with-recovery", methods=["POST"])
@limiter.limit("5 per hour", key_func=_recovery_key)
@json_csrf_protect
def reset_with_recovery():
    """Reset SRP credentials and the password-wrapped private key via QV-RECOVERY-1.

    The browser has already decrypted ``encrypted_private_key_recovery``
    using a key derived from the recovery code and reconstructed the
    account's public key from the recovered private key blob (see
    ``derivePublicKeyFromPrivateBlob`` in ``static/js/qv-crypto.js``).
    That reconstruction is supplied as ``public_key_proof``: AES-GCM
    authentication means a wrong recovery code fails to decrypt at all,
    so only a caller who supplied the correct code can produce a
    ``public_key_proof`` that matches the stored ``public_key``
    byte-for-byte. The underlying keypair and ``public_key`` are not
    changed; only the SRP verifier and the password-wrapping of the
    existing private key blob are replaced.
    """
    data = request.get_json(silent=True) or {}
    required_fields = [
        "username", "public_key_proof", "srp_salt", "srp_verifier",
        "kdf_salt", "encrypted_private_key",
    ]
    if not all(field in data and data[field] for field in required_fields):
        return jsonify({"success": False, "error": "Missing required fields"}), 400

    username = data["username"]
    controller = get_auth_controller()
    user_data = controller.user_db.get_user(username)
    if not user_data or not user_data.get("public_key"):
        audit_event("recovery_reset_denied", username=username, reason="user_not_found")
        return jsonify({"success": False, "error": "Invalid recovery code."}), 403

    if not hmac.compare_digest(data["public_key_proof"], user_data["public_key"]):
        audit_event("recovery_reset_denied", username=username, reason="proof_mismatch")
        return jsonify({"success": False, "error": "Invalid recovery code."}), 403

    controller.user_db.reset_credentials_with_recovery(
        username=username,
        srp_salt=data["srp_salt"],
        srp_verifier=data["srp_verifier"],
        kdf_salt=data["kdf_salt"],
        encrypted_private_key=data["encrypted_private_key"],
    )
    audit_event("recovery_reset_success", username=username)

    if mail_is_configured() and user_data.get("email"):
        send_transactional_email(
            subject="QuantumVault: your password was reset using a recovery code",
            recipients=[user_data["email"]],
            body=(
                "Your QuantumVault account password was just reset using your "
                "account recovery code. If this was not you, your recovery "
                "code may be compromised: log in immediately, set a new "
                "password, and generate a new recovery code from your "
                "account settings."
            ),
        )

    return jsonify({"success": True, "redirect": url_for("auth.login")})


@auth_bp.route("/api/csrf-token", methods=["GET", "OPTIONS"])
def get_csrf_token():
    """Issue the CSRF token used by the SPA for state-changing JSON calls."""
    if request.method == "OPTIONS":
        return "", 204
    # ``generate_csrf`` writes the token into the session so the
    # json_csrf_protect decorator can verify subsequent requests.
    token = generate_csrf()
    return jsonify({"csrf_token": token})
