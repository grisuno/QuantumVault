"""Transactional email helpers for QuantumVault.

Centralizes how outbound transactional mail is addressed and delivered so the
registration flow and the background scheduler share a single implementation
instead of each rebuilding absolute URLs and calling Flask-Mail directly.

The public host used for links is taken from ``SERVER_NAME`` and
``PREFERRED_URL_SCHEME`` so the same code produces correct links from a
background thread (no request context) and from a request handler.
"""

from typing import Sequence

from flask import current_app
from flask_mail import Message

DEFAULT_SENDER = "noreply@quantumvault.pro"
DEFAULT_HOST = "quantumvault.pro"
DEFAULT_SCHEME = "https"


def external_url(path: str) -> str:
    """Build an absolute URL for a root-relative path using the public host.

    Args:
        path: A path such as ``/confirm/<token>``. A leading slash is added
            if missing.

    Returns:
        The absolute URL, for example ``https://www.quantumvault.pro/confirm/x``.
    """
    host = current_app.config.get("SERVER_NAME") or DEFAULT_HOST
    scheme = current_app.config.get("PREFERRED_URL_SCHEME", DEFAULT_SCHEME)
    normalized = path if path.startswith("/") else f"/{path}"
    return f"{scheme}://{host}{normalized}"


def mail_is_configured() -> bool:
    """Return True when SMTP credentials are present so a send can succeed.

    A send is only attempted when both a username and password are set,
    which lets callers fall back to logging a link in local or bare-VPS
    deployments that have no mail account yet.
    """
    return bool(
        current_app.config.get("MAIL_USERNAME")
        and current_app.config.get("MAIL_PASSWORD")
    )


def send_transactional_email(
    subject: str, recipients: Sequence[str], body: str
) -> bool:
    """Send a plain-text transactional email through the configured server.

    This never raises: a failure is logged and reported through the boolean
    return so callers (registration, scheduler) degrade gracefully instead of
    aborting the surrounding operation.

    Args:
        subject: The email subject line.
        recipients: One or more destination addresses.
        body: The plain-text message body.

    Returns:
        True if Flask-Mail accepted the message, False otherwise.
    """
    mail = current_app.config.get("MAIL")
    if mail is None:
        current_app.logger.error(
            "send_transactional_email: the Mail extension is not initialised"
        )
        return False

    sender = current_app.config.get("MAIL_DEFAULT_SENDER") or DEFAULT_SENDER
    try:
        mail.send(
            Message(
                subject=subject,
                sender=sender,
                recipients=list(recipients),
                body=body,
            )
        )
        return True
    except Exception:
        current_app.logger.exception("send_transactional_email: delivery failed")
        return False
