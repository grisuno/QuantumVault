from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, current_app as app
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .auth import role_required
import os
import base64

file_bp = Blueprint('file', __name__)
limiter = Limiter(key_func=get_remote_address)

class UploadForm(FlaskForm):
    """Formulario para la subida de archivos cifrados."""
    file = FileField('Archivo Cifrado', validators=[DataRequired()])
    wrapped_fek = HiddenField('Clave de Archivo Envuelta', validators=[DataRequired()])
    submit = SubmitField('Subir Archivo Seguro')

@file_bp.route('/upload', methods=['GET', 'POST'])
@login_required
@role_required('free', 'bronze', 'silver', 'gold', 'admin', 'superadmin')
@limiter.limit("20 per minute")
def upload():
    """Maneja la subida de archivos cifrados desde el cliente."""
    controller = app.file_controller
    form = UploadForm() # Still needed for rendering the template

    if request.method == 'POST':
        if current_user.subscription_status != "active" and current_user.role == "free":
            return jsonify({"error": "Tu período de prueba ha expirado. Por favor, actualiza a un plan de pago."}), 403

        file = request.files.get('file')
        wrapped_fek_b64 = request.form.get('wrapped_fek')

        if not file or not wrapped_fek_b64:
            return jsonify({"error": "Falta el archivo o la clave cifrada."}), 400

        wrapped_fek_bytes = base64.b64decode(wrapped_fek_b64)

        if controller.upload_encrypted_file(current_user.username, file, wrapped_fek_bytes):
            return jsonify({"message": f'Archivo {file.filename} subido de forma segura.'}), 200
        else:
            # The controller uses flash, but for a fetch request, a JSON response is better.
            return jsonify({"error": "Error al subir el archivo."}), 500

    # GET request
    files = controller.list_encrypted_files(current_user.username)
    return render_template('upload.html', form=form, files=files, username=current_user.username)

@file_bp.route('/download/<path:filename>')
@login_required
@role_required('free', 'bronze', 'silver', 'gold', 'admin', 'superadmin')
@limiter.limit("20 per minute")
def download(filename: str):
    """Provide the encrypted file and its key for client-side decryption.

    The filename comes from the URL and is used to look up a key under
    the authenticated user's S3 prefix. The server never lets the
    filename escape that prefix: any ``/``, ``\\``, ``..`` or control
    character is rejected before the S3 key is constructed, so a
    crafted ``filename`` like ``../admin/files/x`` cannot exfiltrate
    another user's ciphertext.
    """
    if not filename or filename != os.path.basename(filename):
        return jsonify({"error": "Invalid filename."}), 400
    if any(ord(c) < 0x20 or ord(c) == 0x7f for c in filename):
        return jsonify({"error": "Invalid filename."}), 400
    if current_user.subscription_status != "active" and current_user.role == "free":
        return jsonify({"error": "Trial expired."}), 403

    controller = app.file_controller
    encrypted_file, wrapped_fek, error = controller.get_encrypted_file_and_key(current_user.username, filename)
    if error:
        return jsonify({"error": error}), 404

    return jsonify({
        "filename": filename,
        "encrypted_file_b64": base64.b64encode(encrypted_file).decode("utf-8"),
        "wrapped_fek_b64": base64.b64encode(wrapped_fek).decode("utf-8"),
    })
