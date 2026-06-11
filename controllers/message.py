"""Server-side controller for end-to-end encrypted messages.

The browser generates the CEK, encrypts the message with AES-256-GCM, and
wraps the CEK with the recipient's and sender's hybrid public keys. The
server stores only opaque material; it cannot derive plaintext or any key.
"""

from typing import List, Tuple
from models.message import MessageModel, MessageDB
from models.user import UserDB
import uuid
from flask import flash


class MessageController:
    """Handles message persistence in the zero-knowledge flow."""

    def __init__(self, users_path: str, users_db_path: str = "instance/users.db"):
        """Initialize the controller.

        Args:
            users_path: Base directory under which each user has a
                ``messages/`` subdirectory.
            users_db_path: Path to the SQLite user database, used to verify
                that a message recipient is a registered account.
        """
        self.message_db = MessageDB(users_path)
        self.users_path = users_path
        self.user_db = UserDB(users_db_path)

    def send_encrypted_message(
        self,
        sender: str,
        recipient: str,
        encrypted_message_b64: str,
        cek_for_recipient: str,
        cek_for_sender: str,
    ) -> bool:
        """Persist an opaque message envelope for the recipient.

        Args:
            sender: Sender's username.
            recipient: Recipient's username.
            encrypted_message_b64: AES-256-GCM ciphertext (base64) of the
                message body, with the IV prepended by the browser.
            cek_for_recipient: Hybrid-wrapped CEK to the recipient's public
                key (base64 JSON from qv-crypto).
            cek_for_sender: Hybrid-wrapped CEK to the sender's public key
                (so the outbox copy is readable).

        Returns:
            True on success, False otherwise.
        """
        if not self.user_db.get_user(recipient):
            flash("Recipient does not exist")
            return False

        try:
            message_id = str(uuid.uuid4())
            self.message_db.save_message(
                recipient=recipient,
                sender=sender,
                encrypted_message_b64=encrypted_message_b64,
                cek_for_recipient=cek_for_recipient,
                cek_for_sender=cek_for_sender,
                message_id=message_id,
            )
            return True
        except Exception as e:
            flash(f"Error sending message: {e}")
            return False

    def get_messages(
        self, username: str, page: int = 1, per_page: int = 10
    ) -> Tuple[List[MessageModel], int]:
        """Return opaque message envelopes for the user.

        The browser unwraps each CEK with the user's private blob; the
        server only returns the opaque envelopes.

        Args:
            username: User whose mailbox to read.
            page: 1-indexed page number.
            per_page: Messages per page.

        Returns:
            A tuple ``(messages, total_pages)`` of opaque messages.
        """
        return self.message_db.get_messages(username, page=page, per_page=per_page)
