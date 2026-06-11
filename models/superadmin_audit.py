"""Append-only audit log for superadmin actions.

Why a separate table: every privileged action (MFA reset, confirmation
token re-issue, account suspension) needs an immutable record of who
did what to which user, from which IP, and when. Mixing this into the
``users`` table is wrong on two counts:

1. The audit row is written by the superadmin, not the affected user.
   Adding ``last_reset_by`` / ``last_reset_at`` columns to ``users``
   would let an attacker who pwns the DB forge the trail.

2. Audit history is monotonic: an entry must never be UPDATEd or
   DELETEd. SQLite has no row-level immutability, but a dedicated
   table with no application code path that writes UPDATEs is the
   closest we can get.

The table lives in ``instance/users.db`` (same file as ``users``) to
keep operator backup / restore symmetric: one file = one snapshot of
identity state. Storage is bounded by the operational tempo of the
superadmin role, not user activity, so growth is negligible.

Rows are never pruned by the application. If a future retention policy
is needed it should be a documented operator script, not a silent
DELETE in the request path.
"""

import sqlite3
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


class SuperadminAuditDB:
    """Database operations for the superadmin audit log."""

    def __init__(self, db_path: str):
        """Initialize the audit log and ensure its table exists.

        Args:
            db_path: Path to the SQLite database file (shared with
                ``UserDB`` so the two are backed up together).
        """
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        """Create the audit table on first use; no-op if it already exists."""
        with sqlite3.connect(self.db_path) as db:
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS superadmin_audit (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ts DATETIME NOT NULL,
                    actor TEXT NOT NULL,
                    action TEXT NOT NULL,
                    target_user TEXT,
                    ip TEXT,
                    details TEXT
                )
                """
            )
            # Operational queries are always "list recent", "find by
            # target" or "find by actor". Indexes keep them cheap
            # without bloating writes (audit's write rate is the
            # superadmin's hand speed, not the request rate).
            db.execute(
                "CREATE INDEX IF NOT EXISTS idx_audit_ts "
                "ON superadmin_audit(ts DESC)"
            )
            db.execute(
                "CREATE INDEX IF NOT EXISTS idx_audit_target "
                "ON superadmin_audit(target_user, ts DESC)"
            )
            db.commit()

    def record(
        self,
        actor: str,
        action: str,
        target_user: Optional[str] = None,
        ip: Optional[str] = None,
        details: Optional[str] = None,
    ) -> int:
        """Append one audit row and return its id.

        The timestamp is generated server-side in UTC so two operators
        in different timezones can correlate a single incident. The
        return value is the new row's primary key, useful for tests
        and for linking related log lines in the response.

        Args:
            actor: Username of the superadmin performing the action.
            action: Short verb-noun identifier (e.g. ``reset_mfa``,
                ``resend_confirmation``, ``toggle_suspend``).
            target_user: Username the action was applied to, or None
                for global actions (none today, kept for future use).
            ip: Remote address that issued the request. ``None`` when
                the request did not carry one (e.g. background job).
            details: Free-text context, kept short. Use it for the
                state transition (e.g. ``active->inactive``) not for
                payloads that should never leave the audit log.

        Returns:
            The new row's ``id``.
        """
        ts = datetime.now(timezone.utc)
        with sqlite3.connect(self.db_path) as db:
            cur = db.execute(
                """
                INSERT INTO superadmin_audit
                    (ts, actor, action, target_user, ip, details)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (ts, actor, action, target_user, ip, details),
            )
            db.commit()
            new_id = cur.lastrowid
            return int(new_id) if new_id is not None else 0

    def recent(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Return the most recent ``limit`` audit rows, newest first.

        Args:
            limit: Maximum rows to return. Capped at 500 to bound
                template rendering cost on a noisy superadmin.

        Returns:
            List of dicts with keys ``id``, ``ts``, ``actor``,
            ``action``, ``target_user``, ``ip``, ``details``.
        """
        limit = max(1, min(int(limit), 500))
        with sqlite3.connect(self.db_path) as db:
            db.row_factory = sqlite3.Row
            rows = db.execute(
                "SELECT id, ts, actor, action, target_user, ip, details "
                "FROM superadmin_audit ORDER BY id DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [dict(r) for r in rows]
