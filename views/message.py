from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, abort
from flask_login import login_required, current_user
from controllers.message import MessageController
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .auth import role_required
import os

message_bp = Blueprint('message', __name__)
limiter = Limiter(key_func=get_remote_address)

USER_KEYS_BASE_DIR = os.path.abspath('users')
# The browser performs the hybrid KEM wrap, so the server never needs the
# legacy server RSA private key. Keep USER_KEYS_BASE_DIR for admin tooling.

class MessageForm(FlaskForm):
    """Form for sending messages."""
    recipient = StringField('Recipient', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

@message_bp.route('/messages', methods=['GET', 'POST'])
@login_required
@role_required('free', 'bronze', 'silver', 'gold', 'admin', 'superadmin')
@limiter.limit("50 per minute")
def messages():
    """Render the messages page; the browser handles all crypto.

    Sending happens via the JSON API in /api/secure_message below.
    """
    controller = MessageController('users')
    form = MessageForm()

    # Get pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = 10
    messages, total_pages = controller.get_messages(current_user.username, page, per_page)

    return render_template('messages.html', form=form, messages=messages, page=page, total_pages=total_pages, username=current_user.username)


@message_bp.route('/api/secure_message', methods=['POST'])
@login_required
@role_required('free', 'bronze', 'silver', 'gold', 'admin', 'superadmin')
@limiter.limit("50 per minute")
def api_secure_message():
    """Accept an opaque end-to-end encrypted message envelope.

    The browser already generated the CEK, encrypted the message body with
    AES-256-GCM, and wrapped the CEK to the recipient's and sender's
    hybrid public keys. The server stores only the opaque material.
    """
    data = request.get_json() or {}
    recipient = data.get("recipient")
    encrypted_message_b64 = data.get("encrypted_message_b64")
    cek_for_recipient = data.get("cek_for_recipient")
    cek_for_sender = data.get("cek_for_sender")

    if not (recipient and encrypted_message_b64 and cek_for_recipient and cek_for_sender):
        return jsonify({"success": False, "error": "Missing envelope fields."}), 400

    controller = MessageController('users')
    if controller.send_encrypted_message(
        sender=current_user.username,
        recipient=recipient,
        encrypted_message_b64=encrypted_message_b64,
        cek_for_recipient=cek_for_recipient,
        cek_for_sender=cek_for_sender,
    ):
        return jsonify({"success": True, "redirect": url_for("message.messages")})
    return jsonify({"success": False, "error": "Failed to send message."}), 400



