#!/usr/bin/env python
"""Operator tooling to promote QuantumVault users to a privileged role.

Two subcommands, runnable from any Linux host that has the project checked
out (no Flask app context required — talks to the SQLite DB directly):

    python scripts/makeadmin.py <username>
        Promote <username> to 'superadmin'. Idempotent: re-running on an
        already-superadmin user is a no-op that still returns exit code 0.

    python scripts/makeadmin.py <username> <role>
        Set <username>'s role to an arbitrary value from the allowed set
        (free, bronze, silver, gold, admin, superadmin). Use this for
        demotions, role audits, or seeding non-superadmin operators.

Exit code is 0 on success and 1 on failure so the commands compose in
scripts. The DB path defaults to ``instance/users.db``; override with the
``QV_USERS_DB`` environment variable when running against a non-default
deployment (e.g. a staging copy).

The script writes through ``UserDB.update_role`` (models/user.py) so the
storage_quota and subscription_status side-effects match what the rest of
the application does. It does NOT touch the KEM / SRP credentials — a
promotion never invalidates a user's existing login.
"""

import argparse
import os
import sys

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from models.user import UserDB

USERS_DB_PATH = os.environ.get("QV_USERS_DB", "instance/users.db")

# Mirrors the docstring of UserModel (models/user.py). Kept here as a
# runtime guard so a typo in a CLI argument fails fast with a clear
# message instead of silently writing a bogus role into the DB.
ALLOWED_ROLES = ("free", "bronze", "silver", "gold", "admin", "superadmin")

# superadmin gets the whole storage quota; we use 1 TiB which matches the
# rest of the app's "unlimited" tier convention. Subscriptions stay
# active so the user is not gated by billing checks.
_SUPERADMIN_STORAGE_QUOTA = 1024 ** 4
_SUPERADMIN_SUBSCRIPTION_STATUS = "active"


def _resolve_db_path() -> str:
    """Return the absolute users.db path, anchored at the project root.

    A bare ``instance/users.db`` only resolves when the script is run
    from the project root. Anchoring at ``_PROJECT_ROOT`` lets an operator
    invoke it from anywhere (cron, CI, a different cwd) without surprises.
    """
    path = USERS_DB_PATH
    if not os.path.isabs(path):
        path = os.path.join(_PROJECT_ROOT, path)
    return path


def _print_user_summary(user: dict) -> None:
    """Print the post-update user record so the operator can eyeball it."""
    print(
        f"  id={user.get('id')} username={user.get('username')!r} "
        f"role={user.get('role')!r} subscription_status="
        f"{user.get('subscription_status')!r} storage_quota="
        f"{user.get('storage_quota')} email_verified="
        f"{bool(user.get('email_verified'))}"
    )


def cmd_promote(args: argparse.Namespace) -> int:
    """Promote ``args.username`` to the requested role (default: superadmin)."""
    if args.role not in ALLOWED_ROLES:
        print(
            f"FAIL: role {args.role!r} is not one of {ALLOWED_ROLES}. "
            f"Refusing to write an unknown role to the database."
        )
        return 1

    db_path = _resolve_db_path()
    if not os.path.exists(db_path):
        print(f"FAIL: database file not found at {db_path}.")
        return 1

    user_db = UserDB(db_path)
    user = user_db.get_user(args.username)
    if not user:
        print(f"FAIL: no user named {args.username!r} in {db_path}.")
        return 1

    if user.get("role") == args.role:
        print(
            f"OK: {args.username!r} is already {args.role!r}. "
            f"No changes written."
        )
        _print_user_summary(user)
        return 0

    previous_role = user.get("role")
    try:
        user_db.update_role(
            username=args.username,
            role=args.role,
            storage_quota=_SUPERADMIN_STORAGE_QUOTA,
            subscription_status=_SUPERADMIN_SUBSCRIPTION_STATUS,
        )
    except Exception as exc:
        print(
            f"FAIL: could not promote {args.username!r}: "
            f"{type(exc).__name__}: {exc}"
        )
        return 1

    refreshed = user_db.get_user(args.username) or user
    print(
        f"OK: {args.username!r} promoted {previous_role!r} -> {args.role!r}."
    )
    _print_user_summary(refreshed)
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser for the makeadmin subcommands."""
    parser = argparse.ArgumentParser(
        description=(
            "QuantumVault operator tooling: promote (or set) a user's role. "
            "By default the target role is 'superadmin'."
        ),
    )
    parser.add_argument(
        "username",
        help="The account username to promote.",
    )
    parser.add_argument(
        "role",
        nargs="?",
        default="superadmin",
        help=(
            "Target role. One of: "
            f"{', '.join(ALLOWED_ROLES)}. "
            "Defaults to 'superadmin'."
        ),
    )
    parser.set_defaults(func=cmd_promote)
    return parser


def main() -> int:
    """Parse arguments and dispatch to the selected subcommand."""
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
