"""Offline admin tool for ML-KEM-512 key-wrap encryption (QuantumVault).

WARNING
--------
This script is **not** part of the zero-knowledge user trust path. It is an
operator-only CLI used to retroactively wrap/unwrap files that were uploaded
before the browser-based hybrid ML-KEM-768 + X25519 KEM replaced this flow.
Do not call it from any user-facing route. The browser does the encryption for
regular users; the server never sees plaintext passwords or private keys.

The script reads the object-storage endpoint (Garage / S3) from the environment:

    S3_ENDPOINT_URL   - http://localhost:3900 for local Garage
    S3_ACCESS_KEY     - scoped Garage key
    S3_SECRET_KEY     - scoped Garage secret
    S3_REGION         - S3 region name (default: garage)
    S3_BUCKET         - bucket name (default: quantumvault)

When ``S3_ENDPOINT_URL`` is unset, the script falls back to plain AWS S3 using
the ambient AWS credentials chain. The ``--aws-region`` flag overrides
``S3_REGION`` for a single invocation.
"""

import argparse
import os
from io import BytesIO
from oqs import KeyEncapsulation
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import boto3
from botocore.exceptions import ClientError
from pathlib import Path


def derive_aes_key(shared_secret):
    """Derive a 32-byte AES key from an ML-KEM shared secret.

    Args:
        shared_secret: The raw shared secret bytes from ``KeyEncapsulation``.

    Returns:
        A 32-byte AES-256 key suitable for use with :class:`AESGCM`.
    """
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"", iterations=100000)
    return kdf.derive(shared_secret)


def encrypt_file_in_memory(data: bytes, aes_key: bytes) -> tuple[bytes, bytes]:
    """Encrypt ``data`` in memory with AES-256-GCM and return nonce + ciphertext.

    Args:
        data: The plaintext bytes to encrypt.
        aes_key: The 32-byte AES key.

    Returns:
        A tuple ``(nonce, ciphertext)`` where ``nonce`` is 12 random bytes.
    """
    nonce = os.urandom(12)
    aesgcm = AESGCM(aes_key)
    ciphertext = aesgcm.encrypt(nonce, data, None)
    return nonce, ciphertext


def decrypt_file_in_memory(nonce: bytes, ciphertext: bytes, aes_key: bytes) -> bytes:
    """Decrypt ``ciphertext`` in memory with AES-256-GCM and return the plaintext.

    Args:
        nonce: The 12-byte nonce from the encrypt step.
        ciphertext: The encrypted bytes.
        aes_key: The 32-byte AES key.

    Returns:
        The original plaintext bytes.
    """
    aesgcm = AESGCM(aes_key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext


def _build_s3_client(region: str):
    """Build a boto3 S3 client honoring the zero-trust environment convention.

    Args:
        region: The region name (overrides ``S3_REGION`` for this call).

    Returns:
        A configured ``boto3.client('s3')`` instance.
    """
    kwargs: dict = {"region_name": region}
    endpoint_url = os.environ.get("S3_ENDPOINT_URL")
    if endpoint_url:
        kwargs["endpoint_url"] = endpoint_url
        access_key = os.environ.get("S3_ACCESS_KEY")
        secret_key = os.environ.get("S3_SECRET_KEY")
        if access_key:
            kwargs["aws_access_key_id"] = access_key
        if secret_key:
            kwargs["aws_secret_access_key"] = secret_key
    return boto3.client("s3", **kwargs)


def main():
    """Run the offline admin CLI (encrypt or decrypt a single object)."""
    parser = argparse.ArgumentParser(
        description=(
            "Offline admin tool: encrypt/decrypt a single object in S3 with "
            "ML-KEM-512 + AES-256-GCM. Not part of the user trust path."
        )
    )
    parser.add_argument("--mode", choices=["encrypt", "decrypt"], required=True, help="encrypt or decrypt")
    parser.add_argument("--pubkey", help="Public key file (for encryption)")
    parser.add_argument("--seckey", help="Secret key file (for decryption)")
    parser.add_argument("--s3-bucket", default=os.environ.get("S3_BUCKET", "quantumvault"), help="Bucket name")
    parser.add_argument("--s3-key", required=True, help="Object key in the bucket")
    parser.add_argument(
        "--aws-region",
        default=os.environ.get("S3_REGION", "garage"),
        help="S3 region (overrides S3_REGION)",
    )
    parser.add_argument("--username", required=True, help="Owner username (used in key prefix)")
    parser.add_argument("--filename", required=True, help="Filename (used in key prefix)")
    args = parser.parse_args()

    s3_client = _build_s3_client(args.aws_region)
    kem = KeyEncapsulation("ML-KEM-512")

    if args.mode == "encrypt":
        if not args.pubkey:
            raise ValueError("--pubkey is required for encryption")
        with open(args.pubkey, 'rb') as f:
            public_key = f.read()

        ciphertext, shared_secret = kem.encap_secret(public_key)
        aes_key = derive_aes_key(shared_secret)

        try:
            response = s3_client.get_object(Bucket=args.s3_bucket, Key=args.s3_key)
            file_data = response['Body'].read()
        except ClientError as e:
            print(f"Error downloading object from S3: {e}")
            return

        nonce, encrypted_data = encrypt_file_in_memory(file_data, aes_key)

        s3_encrypted_key = f"users/{args.username}/files/encrypted/{args.filename}"
        s3_client.put_object(Bucket=args.s3_bucket, Key=s3_encrypted_key, Body=nonce + encrypted_data)

        s3_ciphertext_key = f"users/{args.username}/files/encrypted/{args.filename}.ciphertext"
        s3_client.put_object(Bucket=args.s3_bucket, Key=s3_ciphertext_key, Body=ciphertext)

        print(f"Encrypted object uploaded to {s3_encrypted_key}")
        print(f"KEM ciphertext uploaded to {s3_ciphertext_key}")

    elif args.mode == "decrypt":
        if not args.seckey:
            raise ValueError("--seckey is required for decryption")
        with open(args.seckey, 'rb') as f:
            secret_key = f.read()
        kem = KeyEncapsulation("ML-KEM-512", secret_key=secret_key)

        s3_ciphertext_key = f"users/{args.username}/files/encrypted/{args.filename}.ciphertext"
        try:
            response = s3_client.get_object(Bucket=args.s3_bucket, Key=s3_ciphertext_key)
            ciphertext = response['Body'].read()
        except ClientError as e:
            print(f"Error downloading KEM ciphertext: {e}")
            return

        shared_secret = kem.decap_secret(ciphertext)
        aes_key = derive_aes_key(shared_secret)

        s3_encrypted_key = f"users/{args.username}/files/encrypted/{args.filename}"
        try:
            response = s3_client.get_object(Bucket=args.s3_bucket, Key=s3_encrypted_key)
            encrypted_data = response['Body'].read()
        except ClientError as e:
            print(f"Error downloading encrypted object: {e}")
            return

        if len(encrypted_data) < 12:
            raise ValueError("Invalid encrypted object")
        nonce, ciphertext_data = encrypted_data[:12], encrypted_data[12:]

        decrypted_data = decrypt_file_in_memory(nonce, ciphertext_data, aes_key)

        s3_decrypted_key = f"users/{args.username}/files/decrypted/{args.filename}"
        s3_client.put_object(Bucket=args.s3_bucket, Key=s3_decrypted_key, Body=decrypted_data)
        print(f"Decrypted object uploaded to {s3_decrypted_key}")


if __name__ == "__main__":
    main()
