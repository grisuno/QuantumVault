"""Centralized security primitives for QuantumVault.

Single source of truth for:

- The structured audit log used by every security-relevant event
  (registration, login, MFA, lockouts, contact, role changes, etc.).
- A JSON-CSRF decorator that protects ``/api/*`` POST/PUT/DELETE routes
  against cross-origin forgery via the ``X-CSRF-Token`` header (the
  same token already issued by ``/api/csrf-token``).
- Small helpers for constant-time comparison and secret hashing of
  short-lived codes (phone verification, MFA, recovery codes).

Keeping these in one module makes the threat model auditable: if a
new endpoint is added and it touches the audit logger, the call site
becomes trivially visible during a security review.
"""

from __future__ import annotations

import functools
import hashlib
import hmac
import json
import logging
import os
import secrets
import time
import uuid
from typing import Any, Callable, Optional

from flask import current_app, g, jsonify, request
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError


# ---------------------------------------------------------------------------
# Structured audit logger
# ---------------------------------------------------------------------------

_AUDIT_LOGGER_NAME = "quantumvault.audit"
_audit_logger: Optional[logging.Logger] = None


def _get_audit_logger() -> logging.Logger:
    """Return the process-wide audit logger, configured on first use.

    The audit logger writes single-line JSON records to stdout. Every
    security-relevant event (login success/failure, registration, MFA,
    contact message, role change, account lockout, CSRF rejection) must
    call :func:`audit_event` so that incident response has a single
    stream to correlate against.
    """
    global _audit_logger
    if _audit_logger is not None:
        return _audit_logger

    logger = logging.getLogger(_AUDIT_LOGGER_NAME)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(message)s")
        )
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    _audit_logger = logger
    return logger


def _correlation_id() -> str:
    """Return the per-request correlation id, generating one if missing.

    The id is stored on Flask's ``g`` so a single request emits multiple
    audit events that share the same key, which is what an operator needs
    when reconstructing a session.
    """
    cid = getattr(g, "correlation_id", None)
    if not cid:
        cid = uuid.uuid4().hex
        g.correlation_id = cid
    return cid


def audit_event(event: str, **fields: Any) -> None:
    """Emit a structured audit record.

    Args:
        event: A short, snake_case event name, e.g. ``login_success`` or
            ``mfa_failure``.
        **fields: Additional structured fields to record. The keys
            ``ts`` (unix epoch in milliseconds), ``event``, ``cid``
            (correlation id), and ``ip`` are added automatically.
    """
    record = {
        "ts": int(time.time() * 1000),
        "event": event,
        "cid": _correlation_id(),
        "ip": request.remote_addr if request else None,
        "ua": (request.headers.get("User-Agent") if request else None),
    }
    record.update(fields)
    try:
        _get_audit_logger().info(json.dumps(record, default=str, sort_keys=True))
    except Exception:
        # The audit log must never crash the request path.
        current_app.logger.exception("audit_event emit failed")


# ---------------------------------------------------------------------------
# Constant-time compare + secret hashing helpers
# ---------------------------------------------------------------------------

def constant_time_compare(a: Optional[str], b: Optional[str]) -> bool:
    """Return True if the two strings match in constant time.

    A regular ``==`` leaks length and content-prefix information via
    short-circuit evaluation. This wraps :func:`hmac.compare_digest`
    which compares the whole input even when lengths differ.
    """
    if a is None or b is None:
        return False
    return hmac.compare_digest(a.encode("utf-8"), b.encode("utf-8"))


def hash_secret(secret: str) -> str:
    """Hash a short-lived secret (phone code, MFA, recovery code) for storage.

    Uses SHA-256 with a server-side pepper. The pepper is read from the
    ``QV_SECRET_PEPPER`` environment variable and falls back to a value
    derived from ``SECRET_KEY`` so the hash is non-deterministic across
    reinstalls but stable for a given deployment.

    The goal is to avoid storing plaintext codes in the database: a DB
    dump no longer hands an attacker ready-to-use codes. Phone codes
    are 6 digits and MFA codes are 6 digits, so a peppered SHA-256 is
    more than sufficient: an attacker with the DB but without the
    pepper must precompute a 10^6-entry rainbow table per deployment.
    """
    pepper = os.environ.get(
        "QV_SECRET_PEPPER",
        current_app.config.get("SECRET_KEY", "qv-fallback-pepper") if current_app else "qv-fallback-pepper",
    )
    return hashlib.sha256(f"{pepper}:{secret}".encode("utf-8")).hexdigest()


def verify_secret(secret: str, expected_hash: str) -> bool:
    """Verify a short-lived secret against its stored hash."""
    if not expected_hash:
        return False
    return constant_time_compare(hash_secret(secret), expected_hash)


def new_one_time_code(length: int = 6) -> str:
    """Return a cryptographically random numeric verification code."""
    return "".join(str(secrets.randbelow(10)) for _ in range(length))


# ---------------------------------------------------------------------------
# JSON CSRF protection
# ---------------------------------------------------------------------------

def _extract_csrf_token() -> str:
    """Return the CSRF token from the request header or body.

    Mirrors Flask-WTF's own lookup order so a client that sets either
    ``X-CSRFToken`` or ``X-CSRF-Token`` (the two spellings Flask-WTF accepts
    in ``WTF_CSRF_HEADERS``), or a ``csrf_token`` form/JSON field, is handled
    uniformly. The browser crypto in ``static/js/qv-crypto.js`` sends the
    ``X-CSRFToken`` header.
    """
    for header_name in ("X-CSRFToken", "X-CSRF-Token"):
        value = request.headers.get(header_name)
        if value:
            return value
    if request.is_json:
        body = request.get_json(silent=True) or {}
        token = body.get("csrf_token")
        if token:
            return token
    return request.form.get("csrf_token", "")


def json_csrf_protect(view: Callable) -> Callable:
    """Decorator: require a valid CSRF token on JSON state-changing requests.

    The token is the one Flask-WTF issues through ``form.hidden_tag()`` or
    ``/api/csrf-token``. It is a *signed* value, so it is validated with
    :func:`flask_wtf.csrf.validate_csrf`, which unsigns it and compares it to
    the raw token held in the session; a direct string comparison against the
    session value never matches and must not be used. A missing or invalid
    token is rejected with HTTP 403 and recorded in the audit log.

    GET, HEAD and OPTIONS pass through unchanged because they are not
    state-changing. Use this on every ``/api/`` route that mutates state.
    """
    @functools.wraps(view)
    def wrapper(*args, **kwargs):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return view(*args, **kwargs)

        try:
            validate_csrf(_extract_csrf_token())
        except ValidationError:
            audit_event("csrf_rejection", method=request.method, path=request.path)
            return jsonify({"error": "CSRF token missing or invalid."}), 403

        return view(*args, **kwargs)

    return wrapper
