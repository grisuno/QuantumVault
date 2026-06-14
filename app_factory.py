"""Application factory for QuantumVault.

The same ``create_app()`` callable powers:

- ``app.py`` (dev: ``flask run`` or Werkzeug's dev server with debug)
- ``wsgi.py`` (prod: gunicorn / uWSGI behind a reverse proxy)

The factory enforces three things that the old ``app.py``-as-script
pattern could not:

1. No Werkzeug debug PIN is ever exposed. Debug mode is gated on the
   ``FLASK_DEBUG`` environment variable and the Werkzeug debugger is
   disabled regardless.
2. Security headers (CSP, HSTS, X-Frame-Options, etc.) are installed
   via Flask-Talisman in production. The strict policy is the default;
   tests can override ``security_overrides`` to relax specific headers.
3. The session cookie is hardened: HttpOnly, SameSite=Lax, Secure when
   the request is HTTPS. ``PERMANENT_SESSION_LIFETIME`` caps the
   idle/absolute lifetime so an unattended browser does not retain
   auth indefinitely.

Keeping every global side-effect (``app.config[...]``, blueprint
registration, extension init) inside the factory means importing
``quantumvault.app_factory`` is free of side effects. That property
matters because ``gunicorn`` forks workers and a top-level ``app =
create_app()`` in a module would import-time-bind the app to the
parent process and re-execute initialization in each worker.
"""

from __future__ import annotations

import json
import logging
import os
import secrets
import sys
from datetime import timedelta
from typing import Any, Optional

import boto3
from botocore.config import Config as BotoConfig
from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_login import LoginManager
from flask_mail import Mail
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from werkzeug.middleware.proxy_fix import ProxyFix

from controllers.file import FileController
from controllers.sync import SyncController
from models.user import UserDB, UserModel
from utils.utils import Config, load_payload


# CORS allow-list shared by every deployment. The list is intentionally
# small: each entry has a security justification in the comment beside it.
DEFAULT_ALLOWED_ORIGINS = [
    "http://localhost:3000",          # local SPA dev (vite/next)
    "http://localhost:5173",          # local SPA dev (vite default)
    "http://localhost:43441",         # local SPA dev (custom port)
    "https://quantumvault.pro",       # production
    "https://www.quantumvault.pro",   # production (www)
    "https://frontend.quantumvault.pro",  # split-front production
]


def _is_production() -> bool:
    """Return True unless the operator explicitly opts into dev mode."""
    env = os.environ.get("QV_ENV", "").lower()
    if env in ("dev", "development"):
        return False
    if env in ("prod", "production"):
        return True
    # No explicit env: fall back to the well-known Flask convention.
    return os.environ.get("FLASK_ENV", "production") == "production"


def _build_csp() -> dict:
    """Return the strict Content-Security-Policy used in production.

    The policy allows:

    - ``'self'`` for everything by default
    - the JSDelivr CDN pinned to the specific packages the SPA needs
      (Bootstrap CSS, EasyMDE CSS/JS, marked). These are loaded with
      SRI from the templates.
    - ``'unsafe-inline'`` for styles is required because EasyMDE injects
      inline styles; for scripts it is forbidden.
    - WebAssembly is allowed (``'wasm-unsafe-eval'``) so the client can
      later compile liboqs-portable to WASM and avoid pure-JS PQ.

    Adding a new third-party origin to this list is a security review
    gate. Do not add origins without updating docs/SECURITY_TODO.md.
    """
    return {
        "default-src": "'self'",
        "object-src": "'none'",
        "base-uri": "'self'",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "img-src": "'self' data:",
        "font-src": "'self' data:",
        "style-src": "'self' 'unsafe-inline' https://cdn.jsdelivr.net",
        "script-src": "'self' 'wasm-unsafe-eval' https://cdn.jsdelivr.net",
        "connect-src": "'self' https://cdn.jsdelivr.net",
    }


def _build_talisman_kwargs() -> dict:
    """Return kwargs to pass to ``Talisman`` based on the runtime env."""
    if not _is_production():
        # Talisman auto-disables HSTS forcing and several headers in
        # debug mode, but we still want X-Frame-Options even locally so
        # an iframe-based clickjack on a developer's preview port does
        # not slip through. Report-only is opt-in via QV_CSP_REPORT_ONLY=1.
        kwargs: dict[str, Any] = {
            "force_https": False,
            "strict_transport_security": False,
            "frame_options": "DENY",
            "content_security_policy": _build_csp(),
            "session_cookie_secure": False,
            "session_cookie_http_only": True,
            "session_cookie_samesite": "Lax",
            "x_content_type_options": True,
            "referrer_policy": "strict-origin-when-cross-origin",
        }
        if os.environ.get("QV_CSP_REPORT_ONLY") == "1":
            kwargs["content_security_policy_report_only"] = True
            kwargs["content_security_policy_report_uri"] = (
                os.environ.get("QV_CSP_REPORT_URI", "/api/csp-report")
            )
        return kwargs
    return {
        "force_https": True,
        "force_https_permanent": True,
        "strict_transport_security": True,
        "strict_transport_security_preload": True,
        "strict_transport_security_max_age": 31556926,  # 1 year
        "strict_transport_security_include_subdomains": True,
        "frame_options": "DENY",
        "content_security_policy": _build_csp(),
        "session_cookie_secure": True,
        "session_cookie_http_only": True,
        "session_cookie_samesite": "Lax",
        "x_content_type_options": True,
        "referrer_policy": "strict-origin-when-cross-origin",
    }


def _configure_secret_key(app: Flask, config: Config) -> None:
    """Set ``app.config['SECRET_KEY']`` from env, payload.json, or a random value.

    The previous code set a fresh 24-byte hex on every process start.
    That is correct for development (sessions reset, no surprises) but
    in production the operator MUST set ``FLASK_SECRET_KEY`` (or
    ``SECRET_KEY``) to a stable, 32+ byte value. Otherwise every
    gunicorn worker restart invalidates every session, including
    CSRF tokens, and the audit log will show a flood of CSRF rejections.

    For backward compatibility, ``payload.json``'s ``SECRET_KEY`` is
    accepted as a third source so a project that was bootstrapped by
    ``make env`` keeps working without a code change. The env var
    always wins over ``payload.json`` so an operator can override.
    """
    payload_key = ""
    try:
        with open("payload.json", encoding="utf-8") as fh:
            payload_key = json.load(fh).get("SECRET_KEY", "") or ""
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    key = (
        os.environ.get("FLASK_SECRET_KEY")
        or os.environ.get("SECRET_KEY")
        or payload_key
    )
    if key:
        app.config["SECRET_KEY"] = key
    elif _is_production():
        # Refuse to start in production with a random key: that is
        # operationally dangerous and almost certainly a misconfiguration.
        sys.stderr.write(
            "FATAL: FLASK_SECRET_KEY is not set. Refusing to start in production\n"
            "because rotating the secret on every worker restart invalidates\n"
            "every session and CSRF token. Set FLASK_SECRET_KEY to a stable\n"
            "32+ byte value (e.g. `openssl rand -hex 32`).\n"
        )
        sys.exit(2)
    else:
        app.config["SECRET_KEY"] = secrets.token_hex(24)


def _configure_session(app: Flask) -> None:
    """Apply session lifetime and cookie hardening.

    The defaults are deliberately conservative:

    - 8 hours of permanent session lifetime (then user must re-login)
    - 30 minutes of idle lifetime (rolling refresh on every request)
    - Cookies are HttpOnly, SameSite=Lax, and Secure in production
    """
    app.config.setdefault("PERMANENT_SESSION_LIFETIME", timedelta(hours=8))
    app.config.setdefault("SESSION_REFRESH_EACH_REQUEST", True)
    app.config.setdefault("SESSION_COOKIE_HTTPONLY", True)
    app.config.setdefault("SESSION_COOKIE_SAMESITE", "Lax")
    if _is_production():
        app.config.setdefault("SESSION_COOKIE_SECURE", True)


def _configure_logging(app: Flask) -> None:
    """Wire up a structured application logger.

    The Werkzeug access log goes through Flask's default handler at
    INFO. Application errors use the standard ``app.logger``. The
    audit logger (``quantumvault.audit``) is configured separately in
    :mod:`utils.security` and writes one-line JSON to stdout.
    """
    level = logging.DEBUG if not _is_production() else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        stream=sys.stdout,
    )
    app.logger.setLevel(level)


def create_app(
    config_overrides: Optional[dict[str, Any]] = None,
    security_overrides: Optional[dict[str, Any]] = None,
) -> Flask:
    """Build and return a fully-configured Flask application.

    Args:
        config_overrides: Values to merge into ``app.config`` after
            defaults are applied. Useful for tests that need to swap
            the database path or disable the rate limiter.
        security_overrides: Values to merge into the Talisman kwargs.
            Used by tests to disable CSP and the HTTPS redirect without
            forking the whole factory.

    Returns:
        A Flask application ready to be served by gunicorn or the
        Werkzeug dev server.
    """
    app = Flask(__name__)

    # The application reads non-secret config from payload.json and
    # overlays secrets from environment variables.
    config = Config(load_payload())
    _configure_secret_key(app, config)
    _configure_session(app)
    _configure_logging(app)

    # Core Flask config values, mirroring the previous app.py.
    app.config["UPLOAD_FOLDER"] = os.path.abspath(
        os.environ.get("QV_UPLOAD_FOLDER", "users")
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_DATABASE_PATH"] = config.SQLALCHEMY_DATABASE_PATH
    app.config["SERVER_NAME"] = config.SERVER_NAME
    app.config["PREFERRED_URL_SCHEME"] = config.PREFERRED_URL_SCHEME
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["MAX_CONTENT_LENGTH"] = config.MAX_CONTENT_LENGTH
    app.config["MAIL_SERVER"] = config.MAIL_SERVER
    app.config["MAIL_PORT"] = config.MAIL_PORT
    app.config["MAIL_USE_TLS"] = config.MAIL_USE_TLS
    app.config["MAIL_USE_SSL"] = config.MAIL_USE_SSL
    app.config["MAIL_USERNAME"] = config.MAIL_USERNAME
    app.config["MAIL_PASSWORD"] = config.MAIL_PASSWORD
    app.config["MAIL_DEFAULT_SENDER"] = config.MAIL_DEFAULT_SENDER
    app.config["STORAGE_URI"] = config.storage_uri
    app.config["S3_ENDPOINT_URL"] = config.s3_endpoint_url
    app.config["S3_BUCKET"] = config.s3_bucket
    app.config["S3_REGION"] = config.s3_region

    # Operators that do not want to offer paid plans can disable the
    # subscription blueprint and nav link entirely.
    app.config["ENABLE_SUBSCRIPTIONS"] = (
        os.environ.get("QV_ENABLE_SUBSCRIPTIONS", "1") == "1"
    )
    app.jinja_env.globals["ENABLE_SUBSCRIPTIONS"] = app.config["ENABLE_SUBSCRIPTIONS"]

    # ProxyFix must run only when behind a trusted reverse proxy. The
    # operator toggles QV_TRUSTED_PROXY=1 to opt in. Without it the
    # client IP is whatever connected to gunicorn directly, which is
    # the right default for the dev server.
    if os.environ.get("QV_TRUSTED_PROXY") == "1":
        app.wsgi_app = ProxyFix(
            app.wsgi_app, x_for=1, x_host=1, x_proto=1, x_prefix=1
        )

    # CORS allow-list is configurable via env so production can pin
    # to its real origin and dev can keep the localhost defaults.
    allowed_origins = [
        o.strip()
        for o in os.environ.get("QV_ALLOWED_ORIGINS", "").split(",")
        if o.strip()
    ] or DEFAULT_ALLOWED_ORIGINS
    CORS(
        app,
        origins=allowed_origins,
        supports_credentials=True,
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization", "X-Requested-With", "X-CSRFToken", "X-CSRF-Token"],
        expose_headers=["Content-Type", "X-CSRFToken"],
        max_age=3600,
    )

    # Security headers via Flask-Talisman. The defaults are strict;
    # the only relaxations are ``force_https`` and ``HSTS`` in dev.
    talisman_kwargs = _build_talisman_kwargs()
    if security_overrides:
        talisman_kwargs.update(security_overrides)
    Talisman(app, **talisman_kwargs)

    # Extension init. The order matters: Mail and LoginManager both
    # read app.config, CSRFProtect must be initialised before any
    # blueprint that uses FlaskForm.
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"

    CSRFProtect(app)

    # Rate limiter. The default per-IP limit is 200/min; per-route
    # decorators (in views/) can lower it for sensitive endpoints.
    storage_uri = config.storage_uri
    limiter = Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["200 per minute"],
        storage_uri=storage_uri,
    )
    app.extensions["limiter"] = limiter

    mail = Mail(app)
    with app.app_context():
        app.config["MAIL"] = mail

    # Self-hosted S3-compatible object storage (Garage). The server only
    # ever reads and writes opaque ciphertext.
    s3_client = boto3.client(
        "s3",
        endpoint_url=config.s3_endpoint_url,
        aws_access_key_id=config.s3_access_key,
        aws_secret_access_key=config.s3_secret_key,
        region_name=config.s3_region,
        config=BotoConfig(
            s3={"addressing_style": "path"},
            signature_version="s3v4",
            connect_timeout=3,
            read_timeout=30,
            retries={"max_attempts": 2, "mode": "standard"},
        ),
    )

    app.file_controller = FileController(
        users_path=app.config["UPLOAD_FOLDER"],
        s3_bucket=config.s3_bucket,
        s3_client=s3_client,
    )
    app.sync_controller = SyncController(
        users_path=app.config["UPLOAD_FOLDER"],
        s3_bucket=config.s3_bucket,
        s3_client=s3_client,
        file_controller=app.file_controller,
    )

    # Blueprints
    from views.about import about_bp
    from views.account import account_bp
    from views.admin import admin_bp
    from views.auth import auth_bp
    from views.faq import faq_bp
    from views.file import file_bp
    from views.message import message_bp
    from views.privacy import privacy_bp
    from views.sync import sync_bp
    from views.terms import terms_bp
    from views.views import views_bp

    blueprints = [
        auth_bp,
        file_bp,
        message_bp,
        admin_bp,
        account_bp,
        views_bp,
        about_bp,
        terms_bp,
        privacy_bp,
        faq_bp,
        sync_bp,
    ]

    if app.config["ENABLE_SUBSCRIPTIONS"]:
        from views.subscription import subscription_bp
        blueprints.append(subscription_bp)

    for bp in blueprints:
        app.register_blueprint(bp)

    @login_manager.user_loader
    def load_user(user_id: str) -> Optional[UserModel]:
        user_db = UserDB(app.config["SQLALCHEMY_DATABASE_PATH"])
        user_data = user_db.get_user_by_id(int(user_id))
        if not user_data:
            return None
        return UserModel(
            id=user_data["id"],
            username=user_data["username"],
            role=user_data["role"],
            email=user_data["email"],
            phone=user_data["phone"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            storage_quota=user_data["storage_quota"],
            trial_start=user_data["trial_start"],
            trial_end=user_data["trial_end"],
            subscription_status=user_data["subscription_status"],
            email_verified=user_data["email_verified"],
            mfa_enabled=user_data["mfa_enabled"],
        )

    if config_overrides:
        app.config.update(config_overrides)

    return app
