"""Opaque storage for QV-DENIABLE-1 deniable vault containers.

The server is zero-knowledge: it stores one opaque, client-encrypted
container per user and never derives, decrypts, or inspects the
plaintext. A container is the JSON envelope produced by the browser
(see ``static/js/qv-deniable.js``); from the database's point of view it
is just text.

The table is deliberately minimal. It carries only what the server must
hold to serve the container back and to bound storage:

* ``username`` (primary key) links the row to the owning account.
* ``envelope`` is the opaque container text.
* ``updated_at`` records when the row last changed, for operator
  housekeeping. No per-slot metadata is stored, because storing anything
  that distinguished one slot from another would undermine the
  deniability guarantee the feature exists to provide.

It lives in the same SQLite file as ``users`` so an operator backup or
restore captures identity and vault state together.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from typing import Any, Dict, Optional


class DeniableVaultDB:
    """Persistence for per-user opaque deniable vault containers."""

    def __init__(self, db_path: str) -> None:
        """Initialize the store and ensure its table exists.

        Args:
            db_path: Path to the SQLite database file, shared with
                :class:`models.user.UserDB`.
        """
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        """Create the ``deniable_vaults`` table on first use."""
        with sqlite3.connect(self.db_path) as db:
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS deniable_vaults (
                    username TEXT PRIMARY KEY,
                    envelope TEXT NOT NULL,
                    updated_at DATETIME NOT NULL
                )
                """
            )
            db.commit()

    def upsert(self, username: str, envelope: str) -> None:
        """Insert or replace the container for ``username``.

        The whole container is replaced atomically: a deniable vault has
        no partial state, so a replace is always a full rewrite of the
        opaque envelope.

        Args:
            username: The owning account's username.
            envelope: The opaque container text to store verbatim.
        """
        now = datetime.now(timezone.utc)
        with sqlite3.connect(self.db_path) as db:
            db.execute(
                """
                INSERT INTO deniable_vaults (username, envelope, updated_at)
                VALUES (?, ?, ?)
                ON CONFLICT(username)
                DO UPDATE SET envelope = excluded.envelope,
                              updated_at = excluded.updated_at
                """,
                (username, envelope, now),
            )
            db.commit()

    def get(self, username: str) -> Optional[Dict[str, Any]]:
        """Return the stored container for ``username``, or ``None``.

        Args:
            username: The account to look up.

        Returns:
            A dict with ``username``, ``envelope``, and ``updated_at``,
            or ``None`` when the account has no container.
        """
        with sqlite3.connect(self.db_path) as db:
            db.row_factory = sqlite3.Row
            row = db.execute(
                "SELECT username, envelope, updated_at "
                "FROM deniable_vaults WHERE username = ?",
                (username,),
            ).fetchone()
        return dict(row) if row else None

    def exists(self, username: str) -> bool:
        """Return True if ``username`` has a stored container."""
        with sqlite3.connect(self.db_path) as db:
            row = db.execute(
                "SELECT 1 FROM deniable_vaults WHERE username = ?",
                (username,),
            ).fetchone()
        return row is not None
