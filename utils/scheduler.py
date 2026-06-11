"""Background scheduler for trial expiration and inbox cleanup.

Runs two recurring jobs:

- ``check_trial_expiration`` (every 24h): flips ``subscription_status``
  to ``inactive`` once the free trial has elapsed, and emails the
  user with a renewal link.
- ``cleanup_old_messages`` (every 24h): drops inbox messages older
  than 7 days for inactive free users.

Both jobs run in APScheduler's BackgroundScheduler, so they execute
on a separate thread from the Flask request workers. Any exception
inside a job is logged but does not crash the scheduler process.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Optional

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_mail import Mail

from models.message import MessageDB
from models.user import UserDB
from utils.mailer import external_url, send_transactional_email


def _now_utc() -> datetime:
    """Timezone-aware UTC ``now`` (avoids the deprecated ``datetime.utcnow()``)."""
    return datetime.now(timezone.utc)


def init_scheduler(app: Flask, mail: Mail) -> None:
    """Start the background scheduler with the production job schedule.

    The jobs run in a daemon thread, so they do not block the Flask
    request loop. They are added idempotently: re-importing the module
    does not register duplicates because :class:`BackgroundScheduler`
    is local to this call.
    """
    # Ensure the transactional mailer can resolve the Mail extension from
    # config even if the scheduler is started before app_factory wires it.
    app.config.setdefault("MAIL", mail)

    scheduler = BackgroundScheduler(daemon=True)
    user_db = UserDB("instance/users.db")
    message_db = MessageDB("users")
    logger = logging.getLogger("quantumvault.scheduler")

    def _is_trial_elapsed(user: dict) -> bool:
        """Return True if the user is on a free plan and the trial has ended."""
        if user.get("role") != "free":
            return False
        if user.get("subscription_status") != "active":
            return False
        trial_end = user.get("trial_end")
        if not trial_end:
            return False
        if isinstance(trial_end, str):
            try:
                trial_end = datetime.fromisoformat(trial_end)
            except ValueError:
                return False
        if trial_end.tzinfo is None:
            trial_end = pytz.utc.localize(trial_end)
        return _now_utc() > trial_end

    def check_trial_expiration() -> None:
        with app.app_context():
            try:
                users = user_db.get_all_users()
            except Exception:
                logger.exception("check_trial_expiration: get_all_users failed")
                return
            for user in users:
                if not _is_trial_elapsed(user):
                    continue
                try:
                    user_db.update_role(
                        username=user["username"],
                        role="free",
                        storage_quota=user["storage_quota"],
                        subscription_status="inactive",
                    )
                except Exception:
                    logger.exception(
                        "trial expiration: update_role failed for %s", user.get("username")
                    )
                    continue

                # The mail body uses an absolute URL built without
                # ``url_for`` (which needs a request context the
                # background thread does not have). The link is
                # constructed from the public host configured in
                # ``app.config['SERVER_NAME']``.
                if not user.get("email"):
                    continue
                renew_url = external_url("/subscribe")
                sent = send_transactional_email(
                    subject="Your QuantumVault trial has expired",
                    recipients=[user["email"]],
                    body=(
                        f"Hi {user.get('first_name') or 'there'},\n\n"
                        f"Your 14-day QuantumVault trial has expired. "
                        f"Renew at {renew_url} to keep using the service.\n\n"
                        f"Thanks for using QuantumVault."
                    ),
                )
                if not sent:
                    logger.warning(
                        "trial expiration: email send failed for %s", user["email"]
                    )

    def cleanup_old_messages() -> None:
        with app.app_context():
            try:
                users = user_db.get_all_users()
            except Exception:
                logger.exception("cleanup_old_messages: get_all_users failed")
                return
            for user in users:
                if user.get("role") == "free" and user.get("subscription_status") == "inactive":
                    try:
                        message_db.delete_old_messages(user["username"], days=7)
                    except Exception:
                        logger.exception(
                            "cleanup_old_messages: failed for %s", user["username"]
                        )

    scheduler.add_job(check_trial_expiration, "interval", hours=24, id="trial_expiration")
    scheduler.add_job(cleanup_old_messages, "interval", hours=24, id="inbox_cleanup")
    scheduler.start()
