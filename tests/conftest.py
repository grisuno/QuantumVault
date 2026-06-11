"""Shared pytest fixtures for the QuantumVault test suite.

Builds the Flask app via :func:`app_factory.create_app` in a mode safe for
automated tests: development settings (so a missing ``FLASK_SECRET_KEY``
does not abort startup), CSP/HTTPS-redirect disabled, an in-memory rate
limiter, and a temporary SQLite database path so the suite never touches
``instance/users.db``.
"""

from __future__ import annotations

import logging
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

os.environ.setdefault("QV_ENV", "dev")
os.environ.setdefault("STORAGE_URI", "memory://")
os.environ.setdefault("FLASK_SECRET_KEY", "test-only-secret-key-do-not-use-in-prod")

from app_factory import create_app  # noqa: E402


@pytest.fixture
def app(tmp_path):
    """Return a QuantumVault Flask app configured for testing."""
    db_path = tmp_path / "users.db"
    application = create_app(
        config_overrides={
            "TESTING": True,
            "SQLALCHEMY_DATABASE_PATH": str(db_path),
        },
        security_overrides={
            "force_https": False,
            "content_security_policy": None,
            "strict_transport_security": False,
        },
    )
    return application


@pytest.fixture
def client(app):
    """Return a Flask test client for the test app."""
    return app.test_client()


class _ListLogHandler(logging.Handler):
    """Collect emitted log messages in a list for assertions."""

    def __init__(self):
        super().__init__()
        self.messages: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.messages.append(record.getMessage())


@pytest.fixture
def audit_records():
    """Yield a list that is appended with each ``audit_event`` JSON line.

    The audit logger has ``propagate = False`` (by design, so it never
    mixes into the application log), so ``caplog`` cannot see it. This
    fixture attaches a temporary handler directly to the audit logger
    instead.
    """
    from utils.security import _get_audit_logger

    logger = _get_audit_logger()
    handler = _ListLogHandler()
    logger.addHandler(handler)
    try:
        yield handler.messages
    finally:
        logger.removeHandler(handler)
