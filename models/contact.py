from pydantic import BaseModel
from typing import Optional
import sqlite3
from datetime import datetime
import pytz
from flask import flash

class ContactModel(BaseModel):
    """Pydantic model for a contact message.

    Attributes:
        id: Unique contact ID.
        user_id: ID of the user who sent the message.
        subject: Subject of the contact message.
        message: Content of the contact message.
        created_at: Timestamp when the message was created.
        status: Status of the message (e.g. 'pending', 'resolved').
    """
    id: Optional[int] = None
    user_id: int
    subject: str
    message: str
    created_at: datetime
    status: str = "pending"

class ContactDB:
    """Database operations for contact messages."""

    def __init__(self, db_path: str):
        """Initialize the ContactDB with the database path.

        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        """Initialize the contacts table with all required fields."""
        with sqlite3.connect(self.db_path) as db:
            db.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                subject TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at DATETIME NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                FOREIGN KEY (user_id) REFERENCES users (id)
            )''')
            db.commit()

    def create_contact(self, user_id: int, subject: str, message: str) -> bool:
        """Create a new contact message.

        Args:
            user_id: ID of the user sending the message.
            subject: Subject of the message.
            message: Content of the message.

        Returns:
            True on success, False if validation fails or the DB write fails.
        """
        if not subject or not message:
            flash("Subject and message are required.")
            return False
        if len(subject) > 100:
            flash("Subject must not exceed 100 characters.")
            return False
        if len(message) > 1000:
            flash("Message must not exceed 1000 characters.")
            return False

        created_at = datetime.now(pytz.utc)
        try:
            with sqlite3.connect(self.db_path) as db:
                db.execute(
                    "INSERT INTO contacts (user_id, subject, message, created_at, status) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (user_id, subject, message, created_at, "pending"),
                )
                db.commit()
                return True
        except sqlite3.Error:
            from flask import current_app
            if current_app:
                current_app.logger.exception("create_contact: db error")
            return False

    def get_user_contacts(self, user_id: int) -> list[dict]:
        """Retrieve all contact messages for a user.

        Args:
            user_id: ID of the user.

        Returns:
            List of contact message dictionaries, newest first. On DB
            error, returns an empty list and logs the failure.
        """
        try:
            with sqlite3.connect(self.db_path) as db:
                cursor = db.execute(
                    "SELECT id, user_id, subject, message, created_at, status "
                    "FROM contacts WHERE user_id = ? "
                    "ORDER BY created_at DESC",
                    (user_id,),
                )
                rows = cursor.fetchall()
                return [self._convert_row_to_dict(row) for row in rows]
        except sqlite3.Error:
            from flask import current_app
            if current_app:
                current_app.logger.exception("get_user_contacts: db error")
            return []

    def _convert_row_to_dict(self, row) -> dict:
        """Convert an SQLite row to a dictionary.

        Args:
            row: SQLite row.

        Returns:
            Contact data as a dictionary.
        """
        if not row:
            return {}
        try:
            created_at = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f%z') if row[4] else None
        except (ValueError, TypeError):
            created_at = None
        return {
            "id": row[0],
            "user_id": row[1],
            "subject": row[2],
            "message": row[3],
            "created_at": created_at,
            "status": row[5],
        }

    def get_all_contacts(self, page: int = 1, per_page: int = 10) -> tuple[list[dict], int]:
        """Retrieve all contact messages with pagination.

        Args:
            page: 1-based page number.
            per_page: Number of contacts per page.

        Returns:
            ``(rows, total_count)``. ``rows`` may be empty on DB error.
        """
        try:
            with sqlite3.connect(self.db_path) as db:
                total_contacts = db.execute("SELECT COUNT(*) FROM contacts").fetchone()[0]
                offset = (page - 1) * per_page
                cursor = db.execute(
                    "SELECT c.id, c.user_id, c.subject, c.message, c.created_at, c.status, u.username "
                    "FROM contacts c JOIN users u ON c.user_id = u.id "
                    "ORDER BY c.created_at DESC "
                    "LIMIT ? OFFSET ?",
                    (per_page, offset),
                )
                rows = cursor.fetchall()
                return [self._convert_row_to_dict_with_username(row) for row in rows], total_contacts
        except sqlite3.Error:
            from flask import current_app
            if current_app:
                current_app.logger.exception("get_all_contacts: db error")
            return [], 0

    def _convert_row_to_dict_with_username(self, row) -> dict:
        """Convert an SQLite row to a dictionary, including username."""
        if not row:
            return {}
        try:
            created_at = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f%z') if row[4] else None
        except (ValueError, TypeError):
            created_at = None
        return {
            "id": row[0],
            "user_id": row[1],
            "subject": row[2],
            "message": row[3],
            "created_at": created_at,
            "status": row[5],
            "username": row[6],
        }
