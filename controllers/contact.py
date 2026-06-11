from models.contact import ContactDB, ContactModel
from flask import flash

class ContactController:
    """Handles logic related to contact messages."""
    def __init__(self, db_path: str):
        """Initialize the ContactController with the database path.

        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.contact_db = ContactDB(db_path)

    def create_contact(self, user_id: int, subject: str, message: str) -> bool:
        """Create a new contact message.

        Args:
            user_id (int): ID of the user sending the message.
            subject (str): Subject of the message.
            message (str): Content of the message.

        Returns:
            bool: True if the message was created successfully, False otherwise.
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
        return self.contact_db.create_contact(user_id, subject, message)

    def get_user_contacts(self, user_id: int) -> list[ContactModel]:
        """Retrieve all contact messages for a user.

        Args:
            user_id (int): ID of the user.

        Returns:
            list[ContactModel]: List of contact messages.
        """
        contacts = self.contact_db.get_user_contacts(user_id)
        return [ContactModel(**contact) for contact in contacts]
