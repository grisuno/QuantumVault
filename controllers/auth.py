"""Zero-knowledge authentication controller for QuantumVault.

Registration accepts cryptographic material that the browser generated
and stores it verbatim: the SRP salt and verifier, the user's public
key, the password-encrypted private key blob, and the KDF salt. The
server never sees the password or any private key. Login is a Secure
Remote Password (SRP-6a) challenge/response (see :mod:`utils.srp6a`)
so the password is never transmitted.

Phone verification codes, MFA codes, and recovery codes are never
stored in plaintext. They are hashed with a server-side pepper via
:func:`utils.security.hash_secret` so a database leak does not hand
the attacker ready-to-use codes.
"""

import os
import secrets
from datetime import datetime, timedelta, timezone
from typing import Optional, Tuple

import pytz
from flask import current_app, flash
from flask_mail import Mail

import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException

from models.user import UserModel, UserDB
from models.plans import PlanDB
from utils import srp6a
from utils.mailer import external_url, mail_is_configured, send_transactional_email
from utils.security import (
    audit_event,
    constant_time_compare,
    hash_secret,
    new_one_time_code,
    verify_secret,
)

DISALLOWED_USERNAME_CHARS = [';', '|', '&', '$', '`', '\'', '"', '\\', '<', '>']

configuration = clicksend_client.Configuration()
configuration.username = os.environ.get('CLICKSEND_USERNAME', '')
configuration.password = os.environ.get('CLICKSEND_API_KEY', '')


def _now_utc() -> datetime:
    """Return the current time as a timezone-aware UTC datetime.

    Avoids the deprecated ``datetime.utcnow()`` which returns a naive
    value and triggers a DeprecationWarning in Python 3.12+.
    """
    return datetime.now(timezone.utc)


class AuthController:
    """Handles zero-knowledge registration and SRP-6a authentication."""

    def __init__(self, db_path: str, mail: Mail, storage_uri: str):
        """Initialize the controller.

        Args:
            db_path: Path to the SQLite user database.
            mail: Configured Flask-Mail instance for transactional email.
            storage_uri: Redis URI backing the ephemeral SRP session store.
        """
        self.user_db = UserDB(db_path)
        self.mail = mail
        self.srp_store = srp6a.SRPSessionStore(storage_uri)

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------
    def register(self, username: str, srp_salt: str, srp_verifier: str, public_key: str,
                 encrypted_private_key: str, kdf_salt: str, email: str, phone: str,
                 first_name: str, last_name: str, recovery_salt: Optional[str] = None,
                 encrypted_private_key_recovery: Optional[str] = None) -> bool:
        """Register a user from client-generated zero-knowledge credentials.

        Args:
            username: The desired unique username.
            srp_salt: SRP salt (hex) generated on the client.
            srp_verifier: SRP verifier (hex) generated on the client.
            public_key: The user's hybrid public key blob (opaque).
            encrypted_private_key: The password-encrypted private key blob (opaque).
            kdf_salt: Salt (hex) for the client-side key derivation function.
            email: The user's email address.
            phone: The user's phone number.
            first_name: The user's first name.
            last_name: The user's last name.
            recovery_salt: Optional QV-RECOVERY-1 PBKDF2 salt (hex), generated on the client.
            encrypted_private_key_recovery: Optional QV-RECOVERY-1 AES-256-GCM
                wrapping of the same private key blob, keyed by a
                client-generated recovery code instead of the password.

        Returns:
            True on success, False if validation fails or persistence errors.
        """
        try:
            if any(char in username for char in DISALLOWED_USERNAME_CHARS):
                flash('The username contains disallowed characters.')
                return False

            required = (username, srp_salt, srp_verifier, public_key, encrypted_private_key, kdf_salt)
            if not all(required):
                flash('Missing required cryptographic material.')
                return False

            confirmation_token = secrets.token_urlsafe(32)
            phone_verification_code = new_one_time_code(6)
            phone_code_expires = _now_utc() + timedelta(minutes=30)

            plan_db = PlanDB('instance/users.db')
            plan = plan_db.get_plan("free")
            trial_start = _now_utc()
            trial_end = trial_start + timedelta(days=plan["trial_days"])

            self.user_db.create_user(
                username=username,
                srp_salt=srp_salt,
                srp_verifier=srp_verifier,
                public_key=public_key,
                encrypted_private_key=encrypted_private_key,
                kdf_salt=kdf_salt,
                email=email,
                phone=phone,
                first_name=first_name,
                last_name=last_name,
                role="free",
                storage_quota=plan["storage_quota"],
                trial_start=trial_start,
                trial_end=trial_end,
                subscription_status="active",
                email_verified=False,
                confirmation_token=confirmation_token,
                phone_verified=False,
                phone_verification_code_hash=hash_secret(phone_verification_code),
                phone_code_expires=phone_code_expires,
                mfa_enabled=False,
                recovery_salt=recovery_salt,
                encrypted_private_key_recovery=encrypted_private_key_recovery,
            )

            audit_event("register_success", username=username, email=email)
            # Dispatch the email and SMS after the DB commit so we never
            # advertise a link or code that the caller cannot subsequently use.
            self.send_confirmation_email(email, username, confirmation_token)
            self.send_sms_verification(phone, phone_verification_code, username)
            return True
        except Exception as e:
            audit_event("register_failure", username=username, reason=type(e).__name__)
            return False

    def send_confirmation_email(self, email: str, username: str, token: str) -> bool:
        """Email the account-confirmation link to a freshly registered user.

        The link targets :func:`views.auth.confirm_email`. When SMTP is not
        configured, or the send fails, the link is logged at WARNING so an
        operator can still verify the account from the server logs; this keeps
        local and bare-VPS deployments usable before mail credentials exist.

        Args:
            email: The recipient address.
            username: The account username (used for the greeting).
            token: The single-use confirmation token stored on the account.

        Returns:
            True if the mail server accepted the message, False otherwise.
        """
        confirm_url = external_url(f"/confirm/{token}")
        body = (
            f"Hi {username},\n\n"
            f"Confirm your QuantumVault email address by visiting:\n"
            f"{confirm_url}\n\n"
            f"If you did not create this account, you can ignore this message."
        )

        if not mail_is_configured():
            audit_event("confirmation_email_unconfigured", username=username)
            current_app.logger.warning(
                "Mail is not configured; confirmation link for %s: %s",
                username,
                confirm_url,
            )
            return False

        sent = send_transactional_email(
            "Confirm your QuantumVault account", [email], body
        )
        audit_event("confirmation_email", username=username, sent=sent)
        if not sent:
            current_app.logger.warning(
                "Confirmation email failed; link for %s: %s", username, confirm_url
            )
        return sent

    # ------------------------------------------------------------------
    # SRP login
    # ------------------------------------------------------------------
    def srp_hello(self, username: str, client_a_hex: str) -> Optional[Tuple[str, str]]:
        """Begin an SRP-6a login and return the salt and server challenge B."""
        user_data = self.user_db.get_user(username)
        if not user_data or not user_data.get('srp_salt') or not user_data.get('srp_verifier'):
            audit_event("srp_hello_unknown_user", username=username)
            return None
        server_b_hex = srp6a.hello(
            self.srp_store,
            username=username,
            client_a_hex=client_a_hex,
            salt_hex=user_data['srp_salt'],
            verifier_hex=user_data['srp_verifier'],
        )
        if server_b_hex is None:
            audit_event("srp_hello_invalid_A", username=username)
            return None
        audit_event("srp_hello_success", username=username)
        return user_data['srp_salt'], server_b_hex

    def srp_verify(self, username: str, client_m1_hex: str) -> Optional[Tuple[UserModel, str]]:
        """Complete an SRP-6a login and return the authenticated user and proof."""
        server_m2_hex = srp6a.verify(self.srp_store, username, client_m1_hex)
        if server_m2_hex is None:
            audit_event("srp_verify_failure", username=username)
            return None

        user_data = self.user_db.get_user(username)
        if not user_data:
            return None

        audit_event("srp_verify_success", username=username)
        user = UserModel(
            id=user_data["id"],
            username=user_data["username"],
            role=user_data["role"],
            email=user_data["email"],
            phone=user_data["phone"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            storage_quota=user_data["storage_quota"],
            trial_start=user_data["trial_start"],
            trial_end=user_data["trial_end"],
            subscription_status=user_data["subscription_status"],
            email_verified=user_data["email_verified"],
            mfa_enabled=user_data["mfa_enabled"]
        )
        return user, server_m2_hex

    # ------------------------------------------------------------------
    # SMS provider
    # ------------------------------------------------------------------
    def send_sms_verification(self, phone: str, code: str, username: str = "") -> bool:
        """Send a verification code via SMS."""
        if not configuration.username or not configuration.password:
            return False
        try:
            api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
            message = f"Your QuantumVault verification code is: {code}"
            if username:
                message += f" https://quantumvault.pro/verify_phone?username={username}"

            sms_message = SmsMessage(source="QuantumVault", body=message, to=phone)
            sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])
            api_instance.sms_send_post(sms_messages)
            return True
        except (ApiException, Exception) as e:
            audit_event("sms_send_failure", reason=str(e))
            return False

    # ------------------------------------------------------------------
    # Phone verification
    # ------------------------------------------------------------------
    def verify_phone_code(self, username: str, code: str) -> bool:
        """Verify a phone verification code for a user.

        The stored value is the peppered hash; the supplied code is
        hashed in the same way and the two digests are compared in
        constant time.
        """
        user_data = self.user_db.get_user(username)
        if not user_data:
            audit_event("phone_verify_unknown_user", username=username)
            return False

        stored_hash = user_data.get("phone_verification_code_hash") or user_data.get("phone_verification_code")
        expires_at = user_data.get("phone_code_expires")

        if not verify_secret(code, stored_hash):
            audit_event("phone_verify_bad_code", username=username)
            return False

        if not self._is_code_valid(expires_at):
            audit_event("phone_verify_expired", username=username)
            return False

        try:
            self.user_db.update_user_phone_status(
                username=username,
                phone_verified=True,
                phone_verification_code_hash=None,
                phone_code_expires=None
            )
            audit_event("phone_verify_success", username=username)
            return True
        except Exception as e:
            audit_event("phone_verify_db_error", username=username, reason=type(e).__name__)
            return False

    def _is_code_valid(self, expires_at) -> bool:
        """Return True if a verification code has not yet expired."""
        if not expires_at:
            return False
        try:
            if isinstance(expires_at, str):
                expires_dt = datetime.fromisoformat(expires_at)
            else:
                expires_dt = expires_at

            if expires_dt.tzinfo is None:
                expires_dt = pytz.utc.localize(expires_dt)

            return _now_utc() <= expires_dt
        except (ValueError, TypeError):
            return False

    # ------------------------------------------------------------------
    # MFA
    # ------------------------------------------------------------------
    def verify_mfa_code(self, username: str, code: str) -> bool:
        """Verify a multi-factor authentication code for a user."""
        user_data = self.user_db.get_user(username)
        if not user_data:
            audit_event("mfa_unknown_user", username=username)
            return False

        stored_hash = user_data.get("mfa_code_hash") or user_data.get("mfa_code")
        if verify_secret(code, stored_hash) and self._is_code_valid(user_data.get("mfa_code_expires")):
            try:
                self.user_db.update_user_mfa_status(
                    username=username,
                    mfa_code_hash=None,
                    mfa_code_expires=None
                )
                audit_event("mfa_success", username=username)
                return True
            except Exception as e:
                audit_event("mfa_db_error", username=username, reason=type(e).__name__)
                return False

        audit_event("mfa_failure", username=username)
        return False

    def send_mfa_code(self, username: str) -> bool:
        """Generate, store, and send an MFA code to the user's phone."""
        user_data = self.user_db.get_user(username)
        if not user_data or not user_data.get("phone_verified"):
            audit_event("mfa_send_unverified", username=username)
            return False

        mfa_code = new_one_time_code(6)
        expires_at = _now_utc() + timedelta(minutes=10)

        try:
            self.user_db.update_user_mfa_status(
                username=username,
                mfa_code_hash=hash_secret(mfa_code),
                mfa_code_expires=expires_at
            )
            ok = self.send_sms_verification(user_data["phone"], mfa_code)
            audit_event("mfa_send", username=username, sent=ok)
            return ok
        except Exception as e:
            audit_event("mfa_send_error", username=username, reason=type(e).__name__)
            return False

    def toggle_mfa(self, username: str, enable: bool) -> None:
        """Enable or disable MFA for a user."""
        try:
            self.user_db.update_user_mfa_status(
                username=username,
                mfa_enabled=enable
            )
            audit_event("mfa_toggle", username=username, enabled=enable)
        except Exception as e:
            audit_event("mfa_toggle_error", username=username, reason=type(e).__name__)
            raise
