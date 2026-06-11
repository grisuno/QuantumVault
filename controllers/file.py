"""Encrypted file persistence layer.

The server is intentionally blind to plaintext: it only ever stores
opaque ciphertext plus an opaque "wrapped file encryption key"
(``wrapped_fek``) produced by the browser. Every filename that flows
through this controller is normalized via :func:`safe_filename` so
the S3 key the user ends up with cannot contain path separators or
control characters.
"""

import os
from typing import List, Optional, Tuple

from flask import current_app, flash
from werkzeug.utils import secure_filename

import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Catch both API-level errors (ClientError) and transport/connection errors
# (BotoCoreError, e.g. EndpointConnectionError when object storage is down)
# so a storage outage degrades gracefully instead of crashing the request.
S3_ERRORS = (BotoCoreError, ClientError)


def _log_s3_error(operation: str, error: Exception) -> None:
    """Log a failed S3 operation without raising further."""
    current_app.logger.error("%s: %s", operation, error)


def safe_filename(name: Optional[str]) -> str:
    """Return a filename safe to embed in an S3 key.

    Applies :func:`werkzeug.utils.secure_filename` to strip any path
    components and control characters, then rejects any residual
    shell-meta characters and NUL bytes. Returns an empty string
    for empty/None input.
    """
    if not name:
        return ""
    sanitized = secure_filename(name)
    bad = set(";|`'\"<>$\\&\0\n\r\t")
    for ch in bad:
        if ch in sanitized:
            return ""
    return sanitized


class FileController:
    """Persistence for end-to-end encrypted files and their wrapped FEKs."""

    def __init__(self, users_path: str, s3_bucket: str, s3_client) -> None:
        self.users_path = users_path
        self.s3_bucket = s3_bucket
        self.s3_client = s3_client

    def _key(self, username: str, filename: str, suffix: str = "") -> str:
        """Build the S3 key for a user's encrypted file or FEK.

        The username is the server's truth (it came from the
        authenticated session), so it does not need additional
        validation. The filename is expected to have been normalized
        via :func:`safe_filename` by the caller.
        """
        if not filename:
            raise ValueError("filename must be a non-empty safe string")
        return f"users/{username}/files/encrypted/{filename}{suffix}"

    def get_storage_usage(self, username: str) -> int:
        """Sum the bytes used by ``username``'s encrypted files in S3."""
        prefix = f"users/{username}/files/encrypted/"
        total = 0
        try:
            paginator = self.s3_client.get_paginator("list_objects_v2")
            for page in paginator.paginate(Bucket=self.s3_bucket, Prefix=prefix):
                for obj in page.get("Contents", []):
                    total += obj["Size"]
        except S3_ERRORS as e:
            _log_s3_error("get_storage_usage", e)
            return 0
        return total

    def upload_encrypted_file(self, username: str, file_storage, wrapped_fek: bytes) -> bool:
        """Persist an already-encrypted file and its wrapped FEK to S3."""
        filename = safe_filename(getattr(file_storage, "filename", None))
        if not filename:
            flash("Invalid filename.")
            return False

        try:
            self.s3_client.put_object(
                Bucket=self.s3_bucket,
                Key=self._key(username, filename),
                Body=file_storage.read(),
            )
            self.s3_client.put_object(
                Bucket=self.s3_bucket,
                Key=self._key(username, filename, suffix=".fek"),
                Body=wrapped_fek,
            )
            flash(f"File {filename} uploaded securely.")
            return True
        except S3_ERRORS as e:
            _log_s3_error("upload_encrypted_file", e)
            return False

    def get_encrypted_file_and_key(
        self, username: str, filename: str
    ) -> Tuple[Optional[bytes], Optional[bytes], Optional[str]]:
        """Fetch a user's encrypted file and its wrapped FEK from S3.

        Returns:
            A 3-tuple of ``(ciphertext, wrapped_fek, error)``. On success
            ``error`` is ``None``; on failure it contains a human-readable
            reason and the byte values are ``None``.
        """
        filename = safe_filename(filename)
        if not filename:
            return None, None, "Invalid filename."

        try:
            file_obj = self.s3_client.get_object(
                Bucket=self.s3_bucket,
                Key=self._key(username, filename),
            )
            ciphertext = file_obj["Body"].read()
            fek_obj = self.s3_client.get_object(
                Bucket=self.s3_bucket,
                Key=self._key(username, filename, suffix=".fek"),
            )
            wrapped_fek = fek_obj["Body"].read()
            return ciphertext, wrapped_fek, None
        except S3_ERRORS as e:
            _log_s3_error("get_encrypted_file_and_key", e)
            return None, None, "Encrypted file storage is unavailable."

    def list_encrypted_files(self, username: str) -> List[str]:
        """List the encrypted files that belong to ``username``."""
        prefix = f"users/{username}/files/encrypted/"
        try:
            paginator = self.s3_client.get_paginator("list_objects_v2")
            result: List[str] = []
            for page in paginator.paginate(Bucket=self.s3_bucket, Prefix=prefix):
                for obj in page.get("Contents", []):
                    if obj["Key"].endswith(".fek"):
                        continue
                    result.append(os.path.basename(obj["Key"]))
            return result
        except S3_ERRORS as e:
            _log_s3_error("list_encrypted_files", e)
            return []
