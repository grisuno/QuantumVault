"""Persistence layer for end-to-end encrypted messages.

The browser performs all cryptography: it generates a random 32-byte content
encryption key (CEK), encrypts the message with AES-256-GCM, and wraps the
CEK to the recipient's hybrid public key (and to the sender for the outbox
copy). The server stores only opaque ciphertext + wrapped keys; it never
sees plaintext or can derive the message.

The on-disk format is a tiny key-value file per message::

    <sender>|<encrypted_message_b64>|<cek_for_recipient_b64>|<cek_for_sender_b64>|<iso_timestamp>

The actual decryption happens in the browser via
``static/js/qv-crypto.js`` -- the page that lists messages fetches each
opaque record and unwraps the CEK with the recipient's private blob.
"""

from pydantic import BaseModel
from typing import Optional, List
import os
import glob
import base64
from datetime import datetime, timedelta
import uuid


class MessageModel(BaseModel):
    """Pydantic model for a stored message envelope.

    Attributes:
        id (Optional[str]): Message ID.
        sender (str): Sender username.
        message (str): Display text. With ZK messages this is the opaque
            payload returned to the client (the browser decrypts it).
        timestamp (Optional[datetime]): When the message was stored.
    """
    id: Optional[str] = None
    sender: str
    message: str
    timestamp: Optional[datetime] = None


class MessageDB:
    """File-based operations for end-to-end encrypted messages."""

    def __init__(self, base_path: str):
        """Initialize the MessageDB with the base directory for per-user mailboxes.

        Args:
            base_path (str): Filesystem path under which each user has a
                ``messages/`` subdirectory.
        """
        self.base_path = base_path

    def save_message(
        self,
        recipient: str,
        sender: str,
        encrypted_message_b64: str,
        cek_for_recipient: str,
        cek_for_sender: str,
        message_id: str,
    ) -> None:
        """Persist an opaque message envelope for the recipient.

        Args:
            recipient (str): Recipient username.
            sender (str): Sender username.
            encrypted_message_b64 (str): AES-256-GCM(CEK, plaintext) as base64
                (IV prepended by the browser).
            cek_for_recipient (str): Hybrid-wrapped CEK to the recipient's
                public key (base64-encoded JSON from qv-crypto).
            cek_for_sender (str): Hybrid-wrapped CEK to the sender's public
                key (so the outbox copy is readable).
            message_id (str): Unique message ID.
        """
        user_dir = os.path.join(self.base_path, recipient, "messages")
        os.makedirs(user_dir, exist_ok=True)

        timestamp = datetime.utcnow().isoformat()
        message_path = os.path.join(user_dir, f"{message_id}.msg")
        with open(message_path, "w") as f:
            f.write(
                f"{sender}:{encrypted_message_b64}:{cek_for_recipient}:{cek_for_sender}:{timestamp}"
            )

    def get_messages(
        self, recipient: str, page: int = 1, per_page: int = 10
    ) -> tuple[list[MessageModel], int]:
        """Return opaque message envelopes for the recipient.

        The browser unwraps the CEK with the user's private blob. This
        method never derives any key material.

        Args:
            recipient (str): Username whose mailbox to read.
            page (int): 1-indexed page number.
            per_page (int): Messages per page.

        Returns:
            A tuple ``(messages, total_pages)`` where each message is
            opaque; the ``message`` field carries the JSON envelope
            ``{encrypted_message_b64, cek_for_recipient, cek_for_sender}``
            so the browser can decrypt it.
        """
        import json
        user_dir = os.path.join(self.base_path, recipient, "messages")
        if not os.path.exists(user_dir):
            return [], 0

        message_files = glob.glob(os.path.join(user_dir, "*.msg"))
        message_files_with_ts: list[tuple[str, datetime]] = []
        for message_file in message_files:
            try:
                with open(message_file, "r") as f:
                    parts = f.read().strip().split(":", 4)
                if len(parts) == 5:
                    ts = datetime.fromisoformat(parts[4])
                else:
                    ts = datetime.fromtimestamp(os.path.getmtime(message_file))
                message_files_with_ts.append((message_file, ts))
            except Exception:
                continue

        message_files = [
            f for f, _ in sorted(message_files_with_ts, key=lambda x: x[1], reverse=True)
        ]

        total_pages = max(1, (len(message_files) + per_page - 1) // per_page)
        start = (page - 1) * per_page
        end = start + per_page
        selected_files = message_files[start:end]

        messages: list[MessageModel] = []
        for message_file in selected_files:
            message_id = os.path.splitext(os.path.basename(message_file))[0]
            try:
                with open(message_file, "r") as f:
                    raw = f.read().strip()
                parts = raw.split(":", 4)
                if len(parts) == 5:
                    sender, enc_msg, cek_r, cek_s, ts_iso = parts
                    ts = datetime.fromisoformat(ts_iso)
                else:
                    continue
                envelope = json.dumps(
                    {
                        "encrypted_message_b64": enc_msg,
                        "cek_for_recipient": cek_r,
                        "cek_for_sender": cek_s,
                    }
                )
                messages.append(
                    MessageModel(
                        id=message_id,
                        sender=sender,
                        message=envelope,
                        timestamp=ts,
                    )
                )
            except Exception as e:
                messages.append(
                    MessageModel(
                        id=message_id,
                        sender="System",
                        message=f"Error reading message: {e}",
                        timestamp=None,
                    )
                )
        return messages, total_pages

    def delete_old_messages(self, recipient: str, days: int = 7) -> None:
        """Delete messages older than ``days`` days from the recipient's mailbox.

        Args:
            recipient (str): Username whose mailbox to prune.
            days (int): Age threshold in days; older messages are removed.
        """
        user_dir = os.path.join(self.base_path, recipient, "messages")
        if not os.path.exists(user_dir):
            return
        cutoff = datetime.utcnow() - timedelta(days=days)
        for message_file in glob.glob(os.path.join(user_dir, "*.msg")):
            try:
                with open(message_file, "r") as f:
                    parts = f.read().strip().split(":", 4)
                if len(parts) != 5:
                    continue
                timestamp = datetime.fromisoformat(parts[4])
                if timestamp < cutoff:
                    os.remove(message_file)
            except Exception:
                from flask import current_app
                if current_app:
                    current_app.logger.exception("delete_old_messages: unexpected error")
