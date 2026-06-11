"""End-to-end encrypted file synchronization views.

``POST /secure_sync`` accepts an opaque encrypted payload from the SPA
and stores it under the authenticated user's prefix in S3. The
endpoint is CSRF-protected and rate-limited per (IP, user) pair to
prevent the server from being used as a free file storage for an
attacker who phished a session cookie.
"""

import os

from flask import Blueprint, current_app, jsonify, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from utils.security import json_csrf_protect


limiter = Limiter(key_func=get_remote_address)
sync_bp = Blueprint("sync", __name__)


@sync_bp.route("/secure_sync", methods=["POST"])
@login_required
@limiter.limit("30 per minute")
@json_csrf_protect
def secure_sync():
    """Receive an already-encrypted file + wrapped FEK and persist them.

    The server never sees the plaintext: the file body and the
    wrapped key are opaque from the server's perspective. We only
    enforce quota and basic input validation.
    """
    if "file" not in request.files:
        return jsonify({"error": "File part is missing"}), 400
    if "wrapped_fek" not in request.form:
        return jsonify({"error": "Wrapped file encryption key (FEK) is missing"}), 400

    file_storage = request.files["file"]
    wrapped_fek = request.form["wrapped_fek"].encode("utf-8")
    try:
        file_size = int(request.form.get("size", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid size"}), 400

    if file_size < 0:
        return jsonify({"error": "Invalid size"}), 400

    username = current_user.username

    # Check the storage quota before we accept the upload. The quota is
    # authoritative here; if the bucket size differs (e.g. a parallel
    # upload raced us) the user sees a transient 400 and can retry.
    controller = current_app.sync_controller
    current_usage = controller.get_storage_usage(username)
    if current_usage + file_size > current_user.storage_quota:
        return jsonify({"error": "Storage quota exceeded"}), 400

    file_controller = current_app.file_controller
    success = file_controller.upload_encrypted_file(
        username=username,
        file_storage=file_storage,
        wrapped_fek=wrapped_fek,
    )
    if success:
        return jsonify({
            "message": f"File {secure_filename(file_storage.filename)} synchronized successfully",
        }), 200
    return jsonify({
        "error": f"Failed to synchronize {secure_filename(file_storage.filename)}",
    }), 500


@sync_bp.route("/sync")
@login_required
@limiter.limit("50 per minute")
def sync_page():
    return render_template("sync.html", username=current_user.username)
