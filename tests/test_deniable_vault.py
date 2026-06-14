"""Specification tests for the QV-DENIABLE-1 deniable vault feature.

The feature is split across layers, each tested in isolation and then
end-to-end through the account HTTP API:

* :class:`controllers.deniable_vault.DeniableVaultConfig` and
  :class:`controllers.deniable_vault.EnvelopeValidator` enforce the
  structural invariants that make a stored container indistinguishable to
  the (zero-knowledge) server: an exact slot count and a fixed-length slot
  ciphertext. The server validates *structure only*; it never decrypts.
* :class:`controllers.deniable_vault.DeniableVaultConfig.random_container`
  lets the server mint a well-formed, unopenable container so that every
  account has one. "Has a container" is therefore universal and reveals
  nothing about whether a hidden vault exists.
* :class:`models.deniable_vault.DeniableVaultDB` stores the opaque
  envelope verbatim, one row per user.
* :class:`controllers.deniable_vault.DeniableVaultController` provisions,
  validates, persists, and emits generic audit events that name neither
  the feature nor the contents.
* The ``account`` blueprint exposes the settings page and the
  ``GET/PUT/DELETE /api/account/vault`` endpoints, gated by authentication,
  CSRF, and rate limiting.
"""

from __future__ import annotations

import base64
import copy
import json
from datetime import datetime, timezone

import pytest

from controllers.deniable_vault import (
    DeniableVaultConfig,
    DeniableVaultController,
    EnvelopeValidationError,
    EnvelopeValidator,
)
from models.deniable_vault import DeniableVaultDB
from models.user import UserDB


# ---------------------------------------------------------------------------
# Fixtures and helpers
# ---------------------------------------------------------------------------


@pytest.fixture
def config() -> DeniableVaultConfig:
    """Return the default deniable-vault configuration."""
    return DeniableVaultConfig.from_mapping({})


@pytest.fixture
def validator(config: DeniableVaultConfig) -> EnvelopeValidator:
    """Return a validator bound to the default configuration."""
    return EnvelopeValidator(config)


def _ciphertext(config: DeniableVaultConfig, length: int | None = None) -> str:
    """Return a base64 ciphertext string of the given (or expected) length."""
    if length is None:
        length = config.expected_ct_b64_length()
    # Build a base64 string of exactly ``length`` characters from zero bytes.
    raw = b"\x00" * ((length // 4) * 3)
    encoded = base64.b64encode(raw).decode("ascii")
    return encoded[:length]


def _valid_envelope(config: DeniableVaultConfig) -> dict:
    """Build a structurally valid envelope for ``config``.

    Every slot carries a ciphertext of the fixed expected length so the
    fixed-size invariant holds. The contents are zero bytes; the validator
    never inspects plaintext, only structure.
    """
    slot = {
        "salt": "a" * config.salt_hex_length,
        "nonce": "b" * config.nonce_hex_length,
        "ct": _ciphertext(config),
    }
    return {
        "v": config.schema_version,
        "kdf": sorted(config.allowed_kdf)[0],
        "iterations": config.min_kdf_iterations,
        "slots": [copy.deepcopy(slot) for _ in range(config.slot_count)],
    }


def _make_user(app, username: str = "alice", role: str = "free") -> dict:
    """Create a minimal user row in the test database and return it."""
    user_db = UserDB(app.config["SQLALCHEMY_DATABASE_PATH"])
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
        role=role,
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


def _login(client, app, username: str = "alice", role: str = "free") -> dict:
    """Create and authenticate a user on ``client``'s session."""
    user = _make_user(app, username=username, role=role)
    app.login_manager.session_protection = None
    with client.session_transaction() as sess:
        sess["_user_id"] = str(user["id"])
        sess["_fresh"] = True
    return user


def _csrf(client) -> str:
    """Fetch a CSRF token bound to the client's session."""
    return client.get("/api/csrf-token").get_json()["csrf_token"]


# ---------------------------------------------------------------------------
# DeniableVaultConfig
# ---------------------------------------------------------------------------


class TestDeniableVaultConfig:
    def test_defaults_are_self_consistent(self):
        config = DeniableVaultConfig.from_mapping({})
        assert config.slot_count >= 2
        assert config.min_kdf_iterations <= config.max_kdf_iterations
        assert config.salt_hex_length % 2 == 0
        assert config.nonce_hex_length % 2 == 0
        assert config.slot_plaintext_bytes > 0
        assert config.allowed_kdf

    def test_expected_ct_length_matches_base64_formula(self, config):
        ct_bytes = config.slot_plaintext_bytes + 16
        assert config.expected_ct_b64_length() == ((ct_bytes + 2) // 3) * 4

    def test_mapping_overrides_defaults(self):
        config = DeniableVaultConfig.from_mapping(
            {"DENIABLE_VAULT_SLOT_COUNT": 3, "DENIABLE_VAULT_SLOT_PLAINTEXT_BYTES": 1024}
        )
        assert config.slot_count == 3
        assert config.slot_plaintext_bytes == 1024

    def test_environment_overrides_mapping(self, monkeypatch):
        monkeypatch.setenv("DENIABLE_VAULT_SLOT_COUNT", "4")
        config = DeniableVaultConfig.from_mapping({"DENIABLE_VAULT_SLOT_COUNT": 2})
        assert config.slot_count == 4

    def test_allowed_kdf_csv_is_parsed(self, monkeypatch):
        monkeypatch.setenv("DENIABLE_VAULT_ALLOWED_KDF", "PBKDF2-SHA256, scrypt")
        config = DeniableVaultConfig.from_mapping({})
        assert "PBKDF2-SHA256" in config.allowed_kdf
        assert "scrypt" in config.allowed_kdf

    def test_public_parameters_round_trip_to_json(self, config):
        params = config.public_parameters()
        assert params["slot_count"] == config.slot_count
        assert params["slot_plaintext_bytes"] == config.slot_plaintext_bytes
        assert params["expected_ct_b64_length"] == config.expected_ct_b64_length()
        json.dumps(params)  # must be JSON-serializable for the API


# ---------------------------------------------------------------------------
# EnvelopeValidator
# ---------------------------------------------------------------------------


class TestEnvelopeValidator:
    def test_accepts_a_well_formed_envelope(self, validator, config):
        validator.validate(_valid_envelope(config))

    def test_rejects_non_dict(self, validator):
        for bad in ([], "x", 5, None):
            with pytest.raises(EnvelopeValidationError):
                validator.validate(bad)

    def test_rejects_wrong_schema_version(self, validator, config):
        env = _valid_envelope(config)
        env["v"] = config.schema_version + 1
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_unknown_kdf(self, validator, config):
        env = _valid_envelope(config)
        env["kdf"] = "rot13"
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_iterations_below_minimum(self, validator, config):
        env = _valid_envelope(config)
        env["iterations"] = config.min_kdf_iterations - 1
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_iterations_above_maximum(self, validator, config):
        env = _valid_envelope(config)
        env["iterations"] = config.max_kdf_iterations + 1
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_wrong_slot_count(self, validator, config):
        env = _valid_envelope(config)
        env["slots"] = env["slots"][:-1]
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_bad_salt_length(self, validator, config):
        env = _valid_envelope(config)
        env["slots"][0]["salt"] = "a" * (config.salt_hex_length - 2)
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_non_hex_salt(self, validator, config):
        env = _valid_envelope(config)
        env["slots"][0]["salt"] = "z" * config.salt_hex_length
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_bad_nonce_length(self, validator, config):
        env = _valid_envelope(config)
        env["slots"][0]["nonce"] = "b" * (config.nonce_hex_length + 2)
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_ciphertext_of_wrong_length(self, validator, config):
        env = _valid_envelope(config)
        env["slots"][0]["ct"] = _ciphertext(config, config.expected_ct_b64_length() - 4)
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_unequal_slot_ciphertext_lengths(self, validator, config):
        env = _valid_envelope(config)
        env["slots"][1]["ct"] = _ciphertext(config, config.expected_ct_b64_length() + 4)
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_invalid_base64_ciphertext(self, validator, config):
        env = _valid_envelope(config)
        env["slots"][0]["ct"] = "*" * config.expected_ct_b64_length()
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)

    def test_rejects_missing_slot_keys(self, validator, config):
        env = _valid_envelope(config)
        del env["slots"][0]["nonce"]
        with pytest.raises(EnvelopeValidationError):
            validator.validate(env)


# ---------------------------------------------------------------------------
# Random container provisioning
# ---------------------------------------------------------------------------


class TestRandomContainer:
    def test_random_container_passes_validation(self, config, validator):
        validator.validate(config.random_container())

    def test_random_containers_differ(self, config):
        first = config.random_container()
        second = config.random_container()
        assert first["slots"][0]["ct"] != second["slots"][0]["ct"]

    def test_random_container_has_fixed_shape(self, config):
        container = config.random_container()
        assert len(container["slots"]) == config.slot_count
        lengths = {len(slot["ct"]) for slot in container["slots"]}
        assert lengths == {config.expected_ct_b64_length()}


# ---------------------------------------------------------------------------
# DeniableVaultDB
# ---------------------------------------------------------------------------


class TestDeniableVaultDB:
    def test_upsert_then_get_round_trips_verbatim(self, tmp_path):
        db = DeniableVaultDB(str(tmp_path / "v.db"))
        payload = '{"v":1,"slots":["opaque"]}'
        db.upsert("alice", payload)
        row = db.get("alice")
        assert row is not None
        assert row["envelope"] == payload
        assert row["username"] == "alice"

    def test_upsert_replaces_existing_row(self, tmp_path):
        db = DeniableVaultDB(str(tmp_path / "v.db"))
        db.upsert("alice", "first")
        db.upsert("alice", "second")
        assert db.get("alice")["envelope"] == "second"

    def test_get_missing_returns_none(self, tmp_path):
        db = DeniableVaultDB(str(tmp_path / "v.db"))
        assert db.get("ghost") is None

    def test_exists(self, tmp_path):
        db = DeniableVaultDB(str(tmp_path / "v.db"))
        assert db.exists("alice") is False
        db.upsert("alice", "x")
        assert db.exists("alice") is True


# ---------------------------------------------------------------------------
# DeniableVaultController
# ---------------------------------------------------------------------------


class TestDeniableVaultController:
    def _controller(self, tmp_path) -> DeniableVaultController:
        config = DeniableVaultConfig.from_mapping({})
        db = DeniableVaultDB(str(tmp_path / "v.db"))
        return DeniableVaultController(db=db, config=config)

    def test_load_or_provision_mints_when_absent(self, app, tmp_path):
        controller = self._controller(tmp_path)
        with app.test_request_context("/"):
            assert controller.exists("alice") is False
            envelope = controller.load_or_provision("alice")
            assert controller.exists("alice") is True
        controller.validator.validate(envelope)

    def test_load_or_provision_is_stable(self, app, tmp_path):
        controller = self._controller(tmp_path)
        with app.test_request_context("/"):
            first = controller.load_or_provision("alice")
            second = controller.load_or_provision("alice")
        assert first == second

    def test_save_then_load_round_trips(self, app, tmp_path):
        controller = self._controller(tmp_path)
        env = _valid_envelope(controller.config)
        with app.test_request_context("/"):
            controller.save("alice", env)
            loaded = controller.load_or_provision("alice")
        assert loaded == env

    def test_save_rejects_invalid_envelope(self, app, tmp_path):
        controller = self._controller(tmp_path)
        env = _valid_envelope(controller.config)
        env["slots"] = env["slots"][:-1]
        with app.test_request_context("/"):
            with pytest.raises(EnvelopeValidationError):
                controller.save("alice", env)
            assert controller.exists("alice") is False

    def test_reset_replaces_with_a_valid_random_container(self, app, tmp_path):
        controller = self._controller(tmp_path)
        env = _valid_envelope(controller.config)
        with app.test_request_context("/"):
            controller.save("alice", env)
            reset_env = controller.reset("alice")
            assert controller.load_or_provision("alice") == reset_env
        assert reset_env != env
        controller.validator.validate(reset_env)

    def test_audit_is_generic_and_never_contains_ciphertext(self, app, tmp_path, audit_records):
        controller = self._controller(tmp_path)
        env = _valid_envelope(controller.config)
        secret_ct = env["slots"][0]["ct"]
        with app.test_request_context("/"):
            controller.save("alice", env)
        joined = "\n".join(audit_records)
        assert "account_object_write" in joined
        assert "deniable" not in joined
        assert secret_ct not in joined


# ---------------------------------------------------------------------------
# HTTP API
# ---------------------------------------------------------------------------


class TestDeniableVaultApi:
    def test_settings_page_requires_authentication(self, client):
        response = client.get("/account", follow_redirects=False)
        assert response.status_code in (302, 401)

    def test_get_api_requires_authentication(self, client):
        response = client.get("/api/account/vault")
        assert response.status_code in (302, 401)

    def test_settings_page_renders_for_authenticated_user(self, client, app):
        _login(client, app)
        response = client.get("/account")
        assert response.status_code == 200
        assert b"Account Settings" in response.data
        assert b"dv-configure-form" in response.data

    def test_get_always_returns_an_envelope_and_parameters(self, client, app):
        _login(client, app)
        body = client.get("/api/account/vault").get_json()
        assert body["envelope"] is not None
        assert len(body["envelope"]["slots"]) == body["parameters"]["slot_count"]
        # The API must never advertise whether a hidden vault exists.
        assert "configured" not in body

    def test_put_without_csrf_is_rejected(self, client, app):
        _login(client, app)
        config = DeniableVaultConfig.from_mapping(dict(app.config))
        response = client.put(
            "/api/account/vault", json={"envelope": _valid_envelope(config)}
        )
        assert response.status_code in (400, 403)

    def test_put_get_reset_round_trip(self, client, app):
        _login(client, app)
        config = DeniableVaultConfig.from_mapping(dict(app.config))
        env = _valid_envelope(config)
        token = _csrf(client)

        put = client.put(
            "/api/account/vault",
            json={"envelope": env},
            headers={"X-CSRFToken": token},
        )
        assert put.status_code == 200
        assert put.get_json()["success"] is True

        got = client.get("/api/account/vault").get_json()
        assert got["envelope"] == env

        reset = client.delete("/api/account/vault", headers={"X-CSRFToken": token})
        assert reset.status_code == 200
        assert reset.get_json()["success"] is True

        after = client.get("/api/account/vault").get_json()
        assert after["envelope"] != env
        assert len(after["envelope"]["slots"]) == config.slot_count

    def test_put_rejects_malformed_envelope(self, client, app):
        _login(client, app)
        config = DeniableVaultConfig.from_mapping(dict(app.config))
        env = _valid_envelope(config)
        env["slots"] = env["slots"][:-1]
        token = _csrf(client)
        response = client.put(
            "/api/account/vault",
            json={"envelope": env},
            headers={"X-CSRFToken": token},
        )
        assert response.status_code == 400
        assert response.get_json()["success"] is False

    def test_vault_is_scoped_to_the_authenticated_user(self, client, app):
        _login(client, app, username="alice")
        config = DeniableVaultConfig.from_mapping(dict(app.config))
        env = _valid_envelope(config)
        token = _csrf(client)
        client.put(
            "/api/account/vault",
            json={"envelope": env},
            headers={"X-CSRFToken": token},
        )

        _login(client, app, username="mallory")
        body = client.get("/api/account/vault").get_json()
        # Mallory gets her own freshly provisioned random container, never
        # Alice's saved one.
        assert body["envelope"] != env
