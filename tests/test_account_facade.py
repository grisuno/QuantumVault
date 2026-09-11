"""Behaviour contract: the decoy site requires a deniable passphrase.

When the cover facade is enabled, the account page must ask for a deniable
(second) passphrase and mark the field required. The server exposes only
the instance-level facade flag; it never learns whether a passphrase is set.
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from app_factory import create_app
from controllers.facade import GatePhraseHasher
from models.user import UserDB

REAL_PHRASE = "correct horse battery"
SECRET_KEY = "account-facade-test-secret-key"


@pytest.fixture
def fast_hasher() -> GatePhraseHasher:
    return GatePhraseHasher(time_cost=1, memory_cost=8, parallelism=1, hash_len=16, salt_len=16)


def _make_user(db_path: str, username: str = "alice") -> dict:
    user_db = UserDB(db_path)
    user_db.create_user(
        username=username,
        srp_salt="00",
        srp_verifier="00",
        public_key="pk",
        encrypted_private_key="epk",
        kdf_salt="00",
        email=f"{username}@example.test",
        phone="",
        first_name="Test",
        last_name="User",
        role="free",
        storage_quota=10 * 1024 * 1024,
        trial_start=datetime.now(timezone.utc),
        trial_end=datetime.now(timezone.utc),
        subscription_status="active",
        email_verified=True,
        confirmation_token=None,
        phone_verified=False,
        phone_verification_code_hash=None,
        phone_code_expires=None,
        mfa_enabled=False,
    )
    return user_db.get_user(username)


def _authenticated_client(application, db_path: str):
    application.login_manager.session_protection = None
    user = _make_user(db_path)
    client = application.test_client()
    with client.session_transaction() as sess:
        sess["_user_id"] = str(user["id"])
        sess["_fresh"] = True
    return client


def _build(tmp_path, fast_hasher, *, facade_enabled: bool):
    overrides = {
        "TESTING": True,
        "WTF_CSRF_SSL_STRICT": False,
        "SQLALCHEMY_DATABASE_PATH": str(tmp_path / "users.db"),
    }
    if facade_enabled:
        overrides.update(
            {
                "QV_FACADE_ENABLED": "1",
                "QV_FACADE_GATE_HASH": fast_hasher.hash(REAL_PHRASE),
            }
        )
    return create_app(
        config_overrides=overrides,
        security_overrides={
            "force_https": False,
            "content_security_policy": None,
            "strict_transport_security": False,
        },
    )


def test_facade_enabled_requires_a_deniable_passphrase(tmp_path, fast_hasher):
    db_path = str(tmp_path / "users.db")
    app = _build(tmp_path, fast_hasher, facade_enabled=True)
    client = _authenticated_client(app, db_path)
    response = client.get("/account")
    assert response.status_code == 200
    assert b"dv-facade-required-notice" in response.data
    assert b'data-dv-require-hidden="1"' in response.data
    assert b"(required)" in response.data


def test_facade_disabled_keeps_it_optional(tmp_path, fast_hasher):
    db_path = str(tmp_path / "users.db")
    app = _build(tmp_path, fast_hasher, facade_enabled=False)
    client = _authenticated_client(app, db_path)
    response = client.get("/account")
    assert response.status_code == 200
    assert b"dv-facade-required-notice" not in response.data
    assert b'data-dv-require-hidden="0"' in response.data
    assert b"(optional)" in response.data
