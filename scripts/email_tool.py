#!/usr/bin/env python
"""Operator email tooling for QuantumVault.

Three subcommands, all runnable from any Linux host or AWS VPS that has the
project checked out and its configuration available (payload.json plus an
optional .env):

    python scripts/email_tool.py test-smtp you@example.com
        Send a real test message through the configured SMTP server to prove
        the transport works from this machine.

    python scripts/email_tool.py link <username>
        Print the account-confirmation URL for a user without sending mail,
        so an operator can verify an account when SMTP is not yet set up.

    python scripts/email_tool.py confirm <username>
        Mark a user's email as verified directly in the database.

Exit code is 0 on success and 1 on failure so the commands compose in scripts.
"""

import argparse
import os
import sys

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from flask import Flask
from flask_mail import Mail

from models.user import UserDB
from utils.mailer import external_url, mail_is_configured, send_transactional_email
from utils.utils import Config, load_payload

USERS_DB_PATH = "instance/users.db"


def _build_mail_app(config: Config) -> Flask:
    """Build a minimal Flask app that only carries the mail configuration.

    Intentionally avoids the full application factory (object storage, Redis,
    security headers) so this tool runs on a bare host with nothing but SMTP
    reachable.
    """
    app = Flask(__name__)
    app.config.update(
        MAIL_SERVER=config.MAIL_SERVER,
        MAIL_PORT=config.MAIL_PORT,
        MAIL_USE_TLS=config.MAIL_USE_TLS,
        MAIL_USE_SSL=config.MAIL_USE_SSL,
        MAIL_USERNAME=config.MAIL_USERNAME,
        MAIL_PASSWORD=config.MAIL_PASSWORD,
        MAIL_DEFAULT_SENDER=config.MAIL_DEFAULT_SENDER,
        SERVER_NAME=config.SERVER_NAME,
        PREFERRED_URL_SCHEME=config.PREFERRED_URL_SCHEME,
    )
    app.config["MAIL"] = Mail(app)
    return app


def cmd_test_smtp(args: argparse.Namespace) -> int:
    """Send a test email through the configured SMTP server."""
    config = Config(load_payload())
    app = _build_mail_app(config)
    with app.app_context():
        if not mail_is_configured():
            print(
                "MAIL_USERNAME / MAIL_PASSWORD are empty. Set them in .env or the "
                "environment before sending. See .env.example for AWS SES and "
                "Gmail instructions."
            )
            return 1
        print(
            f"Sending test email via {config.MAIL_SERVER}:{config.MAIL_PORT} "
            f"(TLS={config.MAIL_USE_TLS}, SSL={config.MAIL_USE_SSL}) to {args.recipient} ..."
        )
        ok = send_transactional_email(
            subject="QuantumVault SMTP test",
            recipients=[args.recipient],
            body="This is a QuantumVault SMTP connectivity test. If you received it, mail works.",
        )
    if ok:
        print("OK: the mail server accepted the message.")
        return 0
    print("FAIL: delivery failed. Check the server, port, TLS/SSL, and credentials.")
    return 1


def cmd_link(args: argparse.Namespace) -> int:
    """Print the confirmation URL for a user without sending email."""
    config = Config(load_payload())
    user = UserDB(USERS_DB_PATH).get_user(args.username)
    if not user:
        print(f"FAIL: no user named {args.username!r}.")
        return 1
    if user.get("email_verified"):
        print(f"User {args.username!r} is already verified.")
        return 0
    token = user.get("confirmation_token")
    if not token:
        print(
            f"FAIL: user {args.username!r} has no confirmation token. "
            f"Use 'confirm' to verify directly."
        )
        return 1
    app = _build_mail_app(config)
    with app.app_context():
        print(external_url(f"/confirm/{token}"))
    return 0


def cmd_confirm(args: argparse.Namespace) -> int:
    """Mark a user's email as verified directly in the database."""
    user_db = UserDB(USERS_DB_PATH)
    user = user_db.get_user(args.username)
    if not user:
        print(f"FAIL: no user named {args.username!r}.")
        return 1
    if user.get("email_verified"):
        print(f"User {args.username!r} is already verified.")
        return 0
    try:
        user_db.update_user(username=args.username, email_verified=True)
    except Exception as exc:
        print(f"FAIL: could not update user: {type(exc).__name__}: {exc}")
        return 1
    print(f"OK: {args.username!r} is now verified.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser for the three subcommands."""
    parser = argparse.ArgumentParser(description="QuantumVault email operator tooling.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_test = sub.add_parser("test-smtp", help="Send a test email to verify SMTP works.")
    p_test.add_argument("recipient", help="Destination email address.")
    p_test.set_defaults(func=cmd_test_smtp)

    p_link = sub.add_parser("link", help="Print a user's confirmation URL.")
    p_link.add_argument("username", help="The account username.")
    p_link.set_defaults(func=cmd_link)

    p_confirm = sub.add_parser("confirm", help="Verify a user's email directly.")
    p_confirm.add_argument("username", help="The account username.")
    p_confirm.set_defaults(func=cmd_confirm)

    return parser


def main() -> int:
    """Parse arguments and dispatch to the selected subcommand."""
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
