# controllers/sync.py
import os
from flask import current_app, flash
import boto3
from botocore.exceptions import ClientError

class SyncController:
    def __init__(self, users_path: str, s3_bucket: str, s3_client, file_controller):
        self.users_path = users_path
        self.s3_bucket = s3_bucket
        self.s3_client = s3_client
        self.file_controller = file_controller

    def get_storage_usage(self, username: str) -> int:
        """Calcula el uso de almacenamiento del usuario en S3."""
        total_size = 0
        prefix = f"users/{username}/files/encrypted/"
        try:
            paginator = self.s3_client.get_paginator('list_objects_v2')
            for page in paginator.paginate(Bucket=self.s3_bucket, Prefix=prefix):
                for obj in page.get('Contents', []):
                    total_size += obj['Size']
        except ClientError as e:
            current_app.logger.error(f"Error al calcular el uso de almacenamiento para {username}: {e}")
            flash(f"Error al calcular el uso de almacenamiento: {e}")
            return 0
        return total_size
