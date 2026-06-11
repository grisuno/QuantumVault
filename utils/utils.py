# utils/utils.py
import json
from typing import TypedDict, Union
import re
import os
from werkzeug.utils import secure_filename

_TRUTHY = frozenset({"1", "true", "yes", "on"})


def as_bool(value: Union[str, bool, int, None], default: bool = False) -> bool:
    """Coerce an environment or payload value into a real boolean.

    Strings such as ``"True"`` and ``"False"`` are both truthy when passed
    straight to Flask, which silently enables flags that were meant to be
    disabled. This normalizes them so ``MAIL_USE_TLS="False"`` disables TLS.

    Args:
        value: The raw value from ``os.environ`` or ``payload.json``.
        default: The value to return when ``value`` is ``None``.

    Returns:
        The coerced boolean.
    """
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    return str(value).strip().lower() in _TRUTHY

def sanitize_path(path: str) -> str:
    """
    Sanitiza una ruta de archivo para prevenir LFI y path traversal.
    - Elimina caracteres peligrosos
    - Normaliza la ruta
    - Asegura que no contenga '..' o rutas absolutas
    """
    if not path:
        return ""

    # Eliminar caracteres no permitidos
    path = re.sub(r'[^\w\-_\.\/]', '', path)

    # Dividir en partes y sanitizar cada una
    parts = []
    for part in path.split('/'):
        if part in ('', '.', '..'):
            continue
        safe_part = secure_filename(part)
        if safe_part:  # Solo añadir si no está vacío
            parts.append(safe_part)

    # Reunir con separadores seguros
    sanitized = "/".join(parts)

    # Asegurar que no empiece con separador
    if sanitized.startswith('/'):
        sanitized = sanitized[1:]

    return sanitized

class Payload(TypedDict, total=False):
    """Non-secret application configuration loaded from ``payload.json``."""

    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_DATABASE_PATH: str
    SQLALCHEMY_TRACK_MODIFICATIONS: str
    MAX_CONTENT_LENGTH: int
    storage_uri: str
    cert: str
    key: str
    port: int
    host: str
    debug: str
    MAIL_SERVER: str
    MAIL_PORT: int
    MAIL_USE_TLS: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_DEFAULT_SENDER: str
    SERVER_NAME: str
    PREFERRED_URL_SCHEME: str


class Config:
    """Application configuration sourced from ``payload.json`` and the environment.

    Non-secret defaults come from ``payload.json``; secrets and infrastructure
    endpoints (mail credentials, object storage, Redis) are overlaid from
    environment variables so that no credential is committed to the repository.

    Every attribute is declared on the class so static analyzers see the
    full shape; :meth:`__init__` populates them from the loaded payload.
    """

    # Non-secret knobs read from payload.json
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_DATABASE_PATH: str
    SQLALCHEMY_TRACK_MODIFICATIONS: str
    MAX_CONTENT_LENGTH: int
    cert: str
    key: str
    port: int
    host: str
    debug: str
    SERVER_NAME: str
    PREFERRED_URL_SCHEME: str

    # Mail transport, overlaid from env so the SMTP endpoint can be set on
    # any host without editing payload.json.
    MAIL_SERVER: str
    MAIL_PORT: int
    MAIL_USE_TLS: bool
    MAIL_USE_SSL: bool

    # Secret/infra values overlaid from env at __init__ time
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_DEFAULT_SENDER: str
    storage_uri: str
    s3_endpoint_url: str
    s3_access_key: str
    s3_secret_key: str
    s3_bucket: str
    s3_region: str

    def __init__(self, config_dict: Payload):
        for key, value in config_dict.items():
            setattr(self, key, value)

        self.MAIL_SERVER = os.environ.get('MAIL_SERVER', config_dict.get('MAIL_SERVER', 'localhost'))
        self.MAIL_PORT = int(os.environ.get('MAIL_PORT', config_dict.get('MAIL_PORT', 587)) or 587)
        self.MAIL_USE_TLS = as_bool(os.environ.get('MAIL_USE_TLS', config_dict.get('MAIL_USE_TLS')), True)
        self.MAIL_USE_SSL = as_bool(os.environ.get('MAIL_USE_SSL', config_dict.get('MAIL_USE_SSL')), False)
        self.MAIL_USERNAME = os.environ.get('MAIL_USERNAME', config_dict.get('MAIL_USERNAME', ''))
        self.MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', config_dict.get('MAIL_PASSWORD', ''))
        self.MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', config_dict.get('MAIL_DEFAULT_SENDER', ''))

        self.storage_uri = os.environ.get('STORAGE_URI', config_dict.get('storage_uri', 'redis://localhost:6379'))

        self.s3_endpoint_url = os.environ.get('S3_ENDPOINT_URL', '')
        self.s3_access_key = os.environ.get('S3_ACCESS_KEY', '')
        self.s3_secret_key = os.environ.get('S3_SECRET_KEY', '')
        self.s3_bucket = os.environ.get('S3_BUCKET', 'quantumvault')
        self.s3_region = os.environ.get('S3_REGION', 'garage')

    def __getitem__(self, key: str):
        return getattr(self, key, None)

def load_payload() -> Payload:
    """Load non-secret application configuration from ``payload.json``.

    A local ``.env`` file is loaded first (when ``python-dotenv`` is available)
    so environment-based secrets are populated before :class:`Config` reads them.

    Returns:
        The parsed configuration dictionary.
    """
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    with open('payload.json', 'r') as file:
        config = json.load(file)
    return config
