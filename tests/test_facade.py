"""Specification tests for the QV-FACADE-1 cover facade and two-step gate.

The feature is specified behaviorally (given/when/then) and tested in isolation
per collaborator, then end-to-end through the HTTP cover flow:

* :class:`controllers.facade.FacadeConfig` resolves every knob from the
  environment, then ``app.config``, then a code default, and never carries a
  gate phrase in the repository.
* :class:`controllers.facade.GatePhraseHasher` hashes and verifies a gate phrase
  with Argon2id, so a low-entropy phrase resists offline attack if the config
  leaks.
* :class:`controllers.facade.GateTicket` mints and verifies a short-lived signed
  ticket keyed by the app secret; expiry, tampering, and a wrong key all verify
  to ``None``.
* :class:`controllers.facade.FacadeGate` classifies a submitted phrase as a
  miss, the real phrase, or the duress phrase, and emits a single generic audit
  event that reveals neither the outcome nor the phrase.
* The ``facade`` blueprint conceals the app: anonymous visitors see the cover on
  the protected pages, a correct phrase reveals the ordinary login, an
  authenticated user bypasses the cover, and a disabled facade changes nothing.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

import pytest

from app_factory import create_app
from controllers.facade import (
    FacadeConfig,
    FacadeGate,
    GateDecision,
    GateOutcome,
    GatePhraseHasher,
    GateTicket,
)
from models.user import UserDB


REAL_PHRASE = "correct horse battery"
DURESS_PHRASE = "under the willow tree"
WRONG_PHRASE = "please let me in now"
SECRET_KEY = "facade-test-secret-key-not-for-production-use"


# ---------------------------------------------------------------------------
# Fixtures and helpers
# ---------------------------------------------------------------------------


@pytest.fixture
def fast_hasher() -> GatePhraseHasher:
    """Return an Argon2id hasher with cheap parameters for fast tests.

    Argon2 embeds its cost parameters in the encoded hash, so verification is
    independent of the verifying hasher's own settings; a cheap hasher can
    therefore produce fixtures without weakening what production verifies.
    """
    return GatePhraseHasher(
        time_cost=1, memory_cost=8, parallelism=1, hash_len=16, salt_len=16
    )


@pytest.fixture
def gate_config(fast_hasher: GatePhraseHasher) -> FacadeConfig:
    """Return an enabled facade config with real and duress phrases set."""
    return FacadeConfig.from_mapping(
        {
            "QV_FACADE_ENABLED": "1",
            "QV_FACADE_GATE_HASH": fast_hasher.hash(REAL_PHRASE),
            "QV_FACADE_DURESS_GATE_HASH": fast_hasher.hash(DURESS_PHRASE),
        }
    )


def _facade_overrides(fast_hasher: GatePhraseHasher, **extra: object) -> dict:
    """Return ``create_app`` config overrides that enable the facade."""
    overrides = {
        "TESTING": True,
        "WTF_CSRF_SSL_STRICT": False,
        "QV_FACADE_ENABLED": "1",
        "QV_FACADE_GATE_HASH": fast_hasher.hash(REAL_PHRASE),
        "QV_FACADE_DURESS_GATE_HASH": fast_hasher.hash(DURESS_PHRASE),
        "QV_FACADE_COVER_BRAND": "Findex",
    }
    overrides.update(extra)
    return overrides


@pytest.fixture
def facade_client(tmp_path, fast_hasher):
    """Return a test client for an app with the facade enabled."""
    application = create_app(
        config_overrides={
            "SQLALCHEMY_DATABASE_PATH": str(tmp_path / "users.db"),
            **_facade_overrides(fast_hasher),
        },
        security_overrides={
            "force_https": False,
            "content_security_policy": None,
            "strict_transport_security": False,
        },
    )
    return application.test_client()


def _make_user(app_or_path, username: str = "alice") -> dict:
    """Create a minimal user row in the given database and return it."""
    user_db = UserDB(app_or_path)
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


def _csrf(client) -> str:
    """Fetch a CSRF token bound to the client's session."""
    return client.get("/api/csrf-token").get_json()["csrf_token"]


# ---------------------------------------------------------------------------
# FacadeConfig
# ---------------------------------------------------------------------------


class TestFacadeConfig:
    def test_defaults_keep_the_facade_off(self):
        config = FacadeConfig.from_mapping({})
        assert config.enabled is False
        assert config.gate_configured is False

    def test_defaults_keep_duress_alert_off(self):
        assert FacadeConfig.from_mapping({}).duress_alert is False

    def test_defaults_are_self_consistent(self):
        config = FacadeConfig.from_mapping({})
        assert config.min_phrase_length >= 1
        assert config.min_phrase_length <= config.max_phrase_length
        assert config.ticket_ttl_seconds > 0
        assert config.argon2_memory_cost >= 8 * config.argon2_parallelism
        assert config.protected_paths

    def test_mapping_overrides_defaults(self):
        config = FacadeConfig.from_mapping(
            {"QV_FACADE_ENABLED": "1", "QV_FACADE_TICKET_TTL_SECONDS": "45"}
        )
        assert config.enabled is True
        assert config.ticket_ttl_seconds == 45

    def test_environment_overrides_mapping(self, monkeypatch):
        monkeypatch.setenv("QV_FACADE_TICKET_TTL_SECONDS", "300")
        config = FacadeConfig.from_mapping({"QV_FACADE_TICKET_TTL_SECONDS": "45"})
        assert config.ticket_ttl_seconds == 300

    def test_protected_paths_csv_is_parsed(self):
        config = FacadeConfig.from_mapping(
            {"QV_FACADE_PROTECTED_PATHS": "/, /login , /welcome"}
        )
        assert config.protected_paths == ("/", "/login", "/welcome")

    def test_gate_configured_requires_enabled_and_a_hash(self):
        assert FacadeConfig.from_mapping(
            {"QV_FACADE_GATE_HASH": "x"}
        ).gate_configured is False
        assert FacadeConfig.from_mapping(
            {"QV_FACADE_ENABLED": "1"}
        ).gate_configured is False
        assert FacadeConfig.from_mapping(
            {"QV_FACADE_ENABLED": "1", "QV_FACADE_GATE_HASH": "x"}
        ).gate_configured is True

    def test_cover_context_is_cosmetic_and_json_serializable(self):
        config = FacadeConfig.from_mapping({"QV_FACADE_COVER_BRAND": "Findex"})
        context = config.cover_context()
        assert context["brand"] == "Findex"
        assert "title" in context and "tagline" in context
        json.dumps(context)
        assert "gate_hash" not in context
        assert "duress_gate_hash" not in context


# ---------------------------------------------------------------------------
# GatePhraseHasher
# ---------------------------------------------------------------------------


class TestGatePhraseHasher:
    def test_hash_then_verify_accepts_the_phrase(self, fast_hasher):
        encoded = fast_hasher.hash(REAL_PHRASE)
        assert fast_hasher.verify(REAL_PHRASE, encoded) is True

    def test_verify_rejects_a_wrong_phrase(self, fast_hasher):
        encoded = fast_hasher.hash(REAL_PHRASE)
        assert fast_hasher.verify(WRONG_PHRASE, encoded) is False

    def test_hash_is_salted_so_two_hashes_differ(self, fast_hasher):
        assert fast_hasher.hash(REAL_PHRASE) != fast_hasher.hash(REAL_PHRASE)

    def test_verify_rejects_an_empty_stored_hash(self, fast_hasher):
        assert fast_hasher.verify(REAL_PHRASE, "") is False

    def test_verify_rejects_a_malformed_stored_hash(self, fast_hasher):
        assert fast_hasher.verify(REAL_PHRASE, "not-an-argon2-hash") is False

    def test_verify_rejects_a_non_string_stored_hash(self, fast_hasher):
        assert fast_hasher.verify(REAL_PHRASE, None) is False
        assert fast_hasher.verify(REAL_PHRASE, 123) is False

    def test_from_config_builds_a_working_hasher(self):
        hasher = GatePhraseHasher.from_config(
            FacadeConfig.from_mapping(
                {
                    "QV_FACADE_ARGON2_TIME_COST": "1",
                    "QV_FACADE_ARGON2_MEMORY_COST": "8",
                    "QV_FACADE_ARGON2_PARALLELISM": "1",
                }
            )
        )
        encoded = hasher.hash(REAL_PHRASE)
        assert hasher.verify(REAL_PHRASE, encoded) is True


# ---------------------------------------------------------------------------
# GateTicket
# ---------------------------------------------------------------------------


class TestGateTicket:
    def test_issue_then_verify_round_trips_the_mode(self):
        ticket = GateTicket(SECRET_KEY, ttl_seconds=120)
        token = ticket.issue(GateOutcome.REAL.value)
        assert ticket.verify(token) == GateOutcome.REAL.value

    def test_issue_rejects_an_unknown_mode(self):
        ticket = GateTicket(SECRET_KEY, ttl_seconds=120)
        with pytest.raises(ValueError):
            ticket.issue("administrator")

    def test_verify_rejects_an_expired_ticket(self):
        issuer = GateTicket(SECRET_KEY, ttl_seconds=120)
        token = issuer.issue(GateOutcome.DURESS.value)
        expired = GateTicket(SECRET_KEY, ttl_seconds=-1)
        assert expired.verify(token) is None

    def test_verify_rejects_a_ticket_signed_with_another_key(self):
        token = GateTicket(SECRET_KEY, ttl_seconds=120).issue(GateOutcome.REAL.value)
        other = GateTicket("a-different-secret-key", ttl_seconds=120)
        assert other.verify(token) is None

    def test_verify_rejects_garbage_and_none(self):
        ticket = GateTicket(SECRET_KEY, ttl_seconds=120)
        assert ticket.verify("garbage") is None
        assert ticket.verify(None) is None

    def test_verify_rejects_a_non_string_token(self):
        ticket = GateTicket(SECRET_KEY, ttl_seconds=120)
        assert ticket.verify(123) is None
        assert ticket.verify(b"bytes") is None


# ---------------------------------------------------------------------------
# FacadeGate
# ---------------------------------------------------------------------------


class TestFacadeGate:
    def _gate(self, config: FacadeConfig) -> FacadeGate:
        return FacadeGate.build(config, SECRET_KEY)

    def test_real_phrase_yields_a_real_ticket(self, app, gate_config):
        gate = self._gate(gate_config)
        with app.test_request_context("/"):
            decision = gate.evaluate(REAL_PHRASE)
        assert isinstance(decision, GateDecision)
        assert decision.outcome is GateOutcome.REAL
        assert gate.ticket.verify(decision.ticket) == GateOutcome.REAL.value

    def test_duress_phrase_yields_a_duress_ticket(self, app, gate_config):
        gate = self._gate(gate_config)
        with app.test_request_context("/"):
            decision = gate.evaluate(DURESS_PHRASE)
        assert decision.outcome is GateOutcome.DURESS
        assert gate.ticket.verify(decision.ticket) == GateOutcome.DURESS.value

    def test_wrong_phrase_is_a_miss_with_no_ticket(self, app, gate_config):
        gate = self._gate(gate_config)
        with app.test_request_context("/"):
            decision = gate.evaluate(WRONG_PHRASE)
        assert decision.outcome is GateOutcome.MISS
        assert decision.ticket is None

    def test_miss_without_a_duress_hash(self, app, fast_hasher):
        config = FacadeConfig.from_mapping(
            {
                "QV_FACADE_ENABLED": "1",
                "QV_FACADE_GATE_HASH": fast_hasher.hash(REAL_PHRASE),
            }
        )
        gate = self._gate(config)
        with app.test_request_context("/"):
            assert gate.evaluate(WRONG_PHRASE).outcome is GateOutcome.MISS

    def test_minimum_length_phrase_is_accepted(self, app, fast_hasher):
        phrase = "abcdefgh"
        config = FacadeConfig.from_mapping(
            {
                "QV_FACADE_ENABLED": "1",
                "QV_FACADE_GATE_HASH": fast_hasher.hash(phrase),
            }
        )
        gate = self._gate(config)
        with app.test_request_context("/"):
            assert gate.evaluate(phrase).outcome is GateOutcome.REAL

    def test_maximum_length_phrase_is_accepted(self, app, fast_hasher):
        phrase = "a" * 256
        config = FacadeConfig.from_mapping(
            {
                "QV_FACADE_ENABLED": "1",
                "QV_FACADE_GATE_HASH": fast_hasher.hash(phrase),
            }
        )
        gate = self._gate(config)
        with app.test_request_context("/"):
            assert gate.evaluate(phrase).outcome is GateOutcome.REAL

    def test_too_short_phrase_is_a_miss(self, app, gate_config):
        gate = self._gate(gate_config)
        with app.test_request_context("/"):
            decision = gate.evaluate("a")
        assert decision.outcome is GateOutcome.MISS

    def test_too_long_phrase_is_a_miss(self, app, gate_config):
        gate = self._gate(gate_config)
        with app.test_request_context("/"):
            decision = gate.evaluate("z" * (gate_config.max_phrase_length + 1))
        assert decision.outcome is GateOutcome.MISS

    def test_audit_is_generic_and_never_contains_the_phrase(
        self, app, gate_config, audit_records
    ):
        gate = self._gate(gate_config)
        with app.test_request_context("/"):
            gate.evaluate(REAL_PHRASE)
        joined = "\n".join(audit_records)
        assert "cover_query" in joined
        for forbidden in ("facade", "gate", "duress", "vault", REAL_PHRASE):
            assert forbidden not in joined

    def test_duress_alert_is_opt_in_and_generically_named(
        self, app, fast_hasher, audit_records
    ):
        config = FacadeConfig.from_mapping(
            {
                "QV_FACADE_ENABLED": "1",
                "QV_FACADE_GATE_HASH": fast_hasher.hash(REAL_PHRASE),
                "QV_FACADE_DURESS_GATE_HASH": fast_hasher.hash(DURESS_PHRASE),
                "QV_FACADE_DURESS_ALERT": "1",
            }
        )
        gate = self._gate(config)
        with app.test_request_context("/"):
            gate.evaluate(DURESS_PHRASE)
        joined = "\n".join(audit_records)
        assert "account_priority_signal" in joined
        assert "duress" not in joined


# ---------------------------------------------------------------------------
# HTTP cover flow
# ---------------------------------------------------------------------------


class TestFacadeHttp:
    def test_anonymous_login_page_is_replaced_by_the_cover(self, facade_client):
        response = facade_client.get("/login")
        assert response.status_code == 200
        assert b"Findex" in response.data
        assert b"QuantumVault" not in response.data

    def test_anonymous_root_is_replaced_by_the_cover(self, facade_client):
        response = facade_client.get("/")
        assert response.status_code == 200
        assert b"Findex" in response.data
        assert b"QuantumVault" not in response.data

    def test_wrong_phrase_keeps_the_cover_and_does_not_redirect(self, facade_client):
        token = _csrf(facade_client)
        response = facade_client.post(
            "/gate", data={"q": WRONG_PHRASE, "csrf_token": token}
        )
        assert response.status_code == 200
        assert b"Findex" in response.data

    def test_real_phrase_reveals_the_login(self, facade_client):
        token = _csrf(facade_client)
        response = facade_client.post(
            "/gate", data={"q": REAL_PHRASE, "csrf_token": token}
        )
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/login")

        revealed = facade_client.get("/login")
        assert revealed.status_code == 200
        assert b"QuantumVault" in revealed.data

        with facade_client.session_transaction() as sess:
            assert sess.get("qv_gate_mode") == "real"

    def test_duress_phrase_marks_the_session(self, facade_client):
        token = _csrf(facade_client)
        response = facade_client.post(
            "/gate", data={"q": DURESS_PHRASE, "csrf_token": token}
        )
        assert response.status_code == 302
        with facade_client.session_transaction() as sess:
            assert sess.get("qv_gate_mode") == "duress"

    def test_authenticated_user_bypasses_the_cover(self, tmp_path, fast_hasher):
        db_path = str(tmp_path / "users.db")
        application = create_app(
            config_overrides={
                "SQLALCHEMY_DATABASE_PATH": db_path,
                **_facade_overrides(fast_hasher),
            },
            security_overrides={
                "force_https": False,
                "content_security_policy": None,
                "strict_transport_security": False,
            },
        )
        application.login_manager.session_protection = None
        user = _make_user(db_path)
        client = application.test_client()
        with client.session_transaction() as sess:
            sess["_user_id"] = str(user["id"])
            sess["_fresh"] = True

        response = client.get("/")
        assert response.status_code == 200
        assert b"QuantumVault" in response.data

    def test_gate_endpoint_is_absent_when_facade_disabled(self, client):
        response = client.post("/gate", data={"q": REAL_PHRASE})
        assert response.status_code == 404

    def test_disabled_facade_serves_the_real_login(self, client):
        response = client.get("/login")
        assert response.status_code == 200
        assert b"Findex" not in response.data

    def test_enabled_without_a_hash_fails_open_to_the_real_app(
        self, tmp_path
    ):
        application = create_app(
            config_overrides={
                "SQLALCHEMY_DATABASE_PATH": str(tmp_path / "users.db"),
                "TESTING": True,
                "WTF_CSRF_SSL_STRICT": False,
                "QV_FACADE_ENABLED": "1",
                "QV_FACADE_GATE_HASH": "",
            },
            security_overrides={
                "force_https": False,
                "content_security_policy": None,
                "strict_transport_security": False,
            },
        )
        response = application.test_client().get("/login")
        assert response.status_code == 200
        assert b"QuantumVault" in response.data
