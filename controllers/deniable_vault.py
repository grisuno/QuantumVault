"""QV-DENIABLE-1 deniable vault: configuration, validation, orchestration.

This module is the server-side core of the deniable vault feature. It is
strictly zero-knowledge: it validates the *structure* of the opaque
container the browser produces, stores it, and serves it back. It never
decrypts a slot, never sees a passphrase, and never learns which slot
holds the decoy and which holds the hidden data.

Deniability requires that activation leaves no evidence. Two mechanisms
provide that:

* Every account always has exactly one container of a fixed shape. The
  server can mint a well-formed *random* container itself, because the
  blob is opaque and AES-GCM ciphertext is indistinguishable from random.
  An unactivated account therefore looks identical to an activated one:
  "has a container" is universal and so reveals nothing. Activation only
  overwrites the random blob with one whose slots a passphrase can open.
* Every container has the same byte size. Each slot's plaintext is padded
  to a fixed length, so every slot's ciphertext is the same length and
  every container is the same size, whether or not it hides data.

Three collaborators, each with a single responsibility:

* :class:`DeniableVaultConfig` is the immutable set of structural limits,
  sourced from the environment with safe defaults. Nothing about the
  envelope shape is hard-coded at a call site.
* :class:`EnvelopeValidator` enforces those limits, including the fixed
  slot count and the fixed ciphertext length.
* :class:`DeniableVaultController` wires the validator to
  :class:`models.deniable_vault.DeniableVaultDB`, provisions random
  containers on demand, and emits audit events that name neither the
  feature nor the contents.
"""

from __future__ import annotations

import binascii
import base64
import json
import os
import secrets
from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Optional

from models.deniable_vault import DeniableVaultDB
from utils.security import audit_event


# Structural defaults. These are named constants, not call-site magic
# numbers, and every one is overridable via the environment through
# :meth:`DeniableVaultConfig.from_mapping`.
#
# The salt/nonce lengths are expressed in hex characters because the
# envelope encodes them as hex: 32 hex chars == 16 bytes of salt, 24 hex
# chars == 12 bytes of AES-GCM nonce, matching the browser crypto.
_DEFAULT_SCHEMA_VERSION = 1
_DEFAULT_SLOT_COUNT = 2
_DEFAULT_SALT_HEX_LENGTH = 32
_DEFAULT_NONCE_HEX_LENGTH = 24
_DEFAULT_MIN_KDF_ITERATIONS = 600_000
_DEFAULT_MAX_KDF_ITERATIONS = 10_000_000
_DEFAULT_ALLOWED_KDF = ("PBKDF2-SHA256",)
# Each slot's plaintext is padded to exactly this many bytes before
# encryption, so every container is the same size regardless of how much
# data it holds. 64 KiB comfortably fits secrets, keys, and notes.
_DEFAULT_SLOT_PLAINTEXT_BYTES = 65_536
# AES-256-GCM appends a 128-bit authentication tag to the ciphertext.
_GCM_TAG_BYTES = 16
# Upper sanity bound on the whole canonical envelope, UTF-8 encoded.
_DEFAULT_MAX_ENVELOPE_BYTES = 4_000_000

_HEX_DIGITS = frozenset("0123456789abcdefABCDEF")

# The only keys an envelope and a slot may carry. Strict key sets remove
# any place to smuggle a "this is the real slot" marker, which is what
# keeps the container deniable.
_ENVELOPE_KEYS = frozenset({"v", "kdf", "iterations", "slots"})
_SLOT_KEYS = frozenset({"salt", "nonce", "ct"})


def _base64_length(byte_length: int) -> int:
    """Return the length of the standard base64 encoding of ``byte_length`` bytes."""
    return ((byte_length + 2) // 3) * 4


def canonical_json(envelope: Mapping[str, Any]) -> str:
    """Serialize an envelope deterministically for storage and sizing.

    Keys are sorted and separators are compact so the same logical
    envelope always serializes to the same bytes. Both the size check in
    :class:`EnvelopeValidator` and the persistence path in
    :class:`DeniableVaultController` use this single function, so the
    bytes that are measured are exactly the bytes that are stored.

    Args:
        envelope: The envelope mapping to serialize.

    Returns:
        The canonical JSON string.
    """
    return json.dumps(envelope, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


class EnvelopeValidationError(ValueError):
    """Raised when an envelope violates a structural invariant."""


def _coerce_int(value: Any, default: int) -> int:
    """Return ``value`` coerced to int, falling back to ``default``."""
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _coerce_kdf(value: Any, default: Iterable[str]) -> frozenset[str]:
    """Return an allow-list of KDF identifiers from a value.

    Accepts a comma-separated string (as found in environment variables)
    or any iterable of strings.
    """
    if value is None:
        return frozenset(default)
    if isinstance(value, str):
        items = [part.strip() for part in value.split(",") if part.strip()]
    else:
        items = [str(part).strip() for part in value if str(part).strip()]
    return frozenset(items) if items else frozenset(default)


@dataclass(frozen=True)
class DeniableVaultConfig:
    """Immutable structural limits for a deniable vault container."""

    schema_version: int = _DEFAULT_SCHEMA_VERSION
    slot_count: int = _DEFAULT_SLOT_COUNT
    salt_hex_length: int = _DEFAULT_SALT_HEX_LENGTH
    nonce_hex_length: int = _DEFAULT_NONCE_HEX_LENGTH
    min_kdf_iterations: int = _DEFAULT_MIN_KDF_ITERATIONS
    max_kdf_iterations: int = _DEFAULT_MAX_KDF_ITERATIONS
    allowed_kdf: frozenset[str] = frozenset(_DEFAULT_ALLOWED_KDF)
    slot_plaintext_bytes: int = _DEFAULT_SLOT_PLAINTEXT_BYTES
    max_envelope_bytes: int = _DEFAULT_MAX_ENVELOPE_BYTES

    @classmethod
    def from_mapping(
        cls,
        mapping: Mapping[str, Any],
        env: Optional[Mapping[str, str]] = None,
    ) -> "DeniableVaultConfig":
        """Build a config from a mapping, with environment overrides.

        Resolution order for every field is: environment variable, then
        ``mapping`` entry (e.g. ``app.config``), then the module default.
        Defaults are intentionally not written to ``payload.json`` so the
        repository carries no per-deployment hint that the feature exists;
        an operator overrides them per-host via the environment.

        Args:
            mapping: A mapping such as ``app.config``.
            env: Environment to read overrides from. Defaults to
                ``os.environ``; injectable for tests.

        Returns:
            The resolved, immutable configuration.
        """
        source = os.environ if env is None else env

        def read(key: str) -> Any:
            if key in source:
                return source[key]
            if key in mapping:
                return mapping[key]
            return None

        defaults = cls()
        return cls(
            schema_version=_coerce_int(
                read("DENIABLE_VAULT_SCHEMA_VERSION"), defaults.schema_version
            ),
            slot_count=_coerce_int(
                read("DENIABLE_VAULT_SLOT_COUNT"), defaults.slot_count
            ),
            salt_hex_length=_coerce_int(
                read("DENIABLE_VAULT_SALT_HEX_LENGTH"), defaults.salt_hex_length
            ),
            nonce_hex_length=_coerce_int(
                read("DENIABLE_VAULT_NONCE_HEX_LENGTH"), defaults.nonce_hex_length
            ),
            min_kdf_iterations=_coerce_int(
                read("DENIABLE_VAULT_MIN_KDF_ITERATIONS"),
                defaults.min_kdf_iterations,
            ),
            max_kdf_iterations=_coerce_int(
                read("DENIABLE_VAULT_MAX_KDF_ITERATIONS"),
                defaults.max_kdf_iterations,
            ),
            allowed_kdf=_coerce_kdf(
                read("DENIABLE_VAULT_ALLOWED_KDF"), defaults.allowed_kdf
            ),
            slot_plaintext_bytes=_coerce_int(
                read("DENIABLE_VAULT_SLOT_PLAINTEXT_BYTES"),
                defaults.slot_plaintext_bytes,
            ),
            max_envelope_bytes=_coerce_int(
                read("DENIABLE_VAULT_MAX_ENVELOPE_BYTES"),
                defaults.max_envelope_bytes,
            ),
        )

    def expected_ct_b64_length(self) -> int:
        """Return the exact base64 length every slot ciphertext must have.

        A slot's ciphertext is the fixed plaintext length plus the GCM
        tag, base64-encoded. Fixing it makes every container byte-for-byte
        the same shape.
        """
        return _base64_length(self.slot_plaintext_bytes + _GCM_TAG_BYTES)

    def random_container(self) -> dict[str, Any]:
        """Return a well-formed container filled with random, unopenable data.

        Used to provision an account that has not activated the feature and
        to reset one. The result is structurally indistinguishable from an
        activated container: random hex salts and nonces, and random
        base64 ciphertext of exactly the expected length. No passphrase can
        open it, which is the correct behavior for an unactivated vault.

        Returns:
            A fresh random envelope dict.
        """
        ct_bytes = self.slot_plaintext_bytes + _GCM_TAG_BYTES
        slots = [
            {
                "salt": secrets.token_hex(self.salt_hex_length // 2),
                "nonce": secrets.token_hex(self.nonce_hex_length // 2),
                "ct": base64.b64encode(os.urandom(ct_bytes)).decode("ascii"),
            }
            for _ in range(self.slot_count)
        ]
        return {
            "v": self.schema_version,
            "kdf": sorted(self.allowed_kdf)[0],
            "iterations": self.min_kdf_iterations,
            "slots": slots,
        }

    def public_parameters(self) -> dict[str, Any]:
        """Return the parameters the browser needs to build a container.

        The browser reads these instead of hard-coding them, so a change
        to the server policy propagates to clients without a code change.
        The values are non-secret: they describe the container shape,
        which is identical for every account.
        """
        return {
            "schema_version": self.schema_version,
            "slot_count": self.slot_count,
            "salt_hex_length": self.salt_hex_length,
            "nonce_hex_length": self.nonce_hex_length,
            "min_kdf_iterations": self.min_kdf_iterations,
            "max_kdf_iterations": self.max_kdf_iterations,
            "allowed_kdf": sorted(self.allowed_kdf),
            "slot_plaintext_bytes": self.slot_plaintext_bytes,
            "expected_ct_b64_length": self.expected_ct_b64_length(),
            "max_envelope_bytes": self.max_envelope_bytes,
        }


class EnvelopeValidator:
    """Validate the structure of an opaque deniable vault envelope.

    The validator never decrypts. It checks only the shape: the schema
    version, the KDF identifier and iteration count, the exact slot count,
    each slot's hex and base64 fields, and the fixed ciphertext length
    that makes every container identical in size.
    """

    def __init__(self, config: DeniableVaultConfig) -> None:
        """Bind the validator to a configuration."""
        self.config = config

    def validate(self, envelope: Any) -> None:
        """Validate ``envelope``, raising on the first violation.

        Args:
            envelope: The decoded JSON envelope to validate.

        Raises:
            EnvelopeValidationError: If any structural invariant is
                violated. The message names the violated invariant and
                never echoes ciphertext.
        """
        config = self.config

        if not isinstance(envelope, Mapping):
            raise EnvelopeValidationError("Envelope must be a JSON object.")
        if set(envelope.keys()) != _ENVELOPE_KEYS:
            raise EnvelopeValidationError(
                f"Envelope must contain exactly the keys {sorted(_ENVELOPE_KEYS)}."
            )

        if envelope["v"] != config.schema_version:
            raise EnvelopeValidationError(
                f"Unsupported schema version; expected {config.schema_version}."
            )

        if envelope["kdf"] not in config.allowed_kdf:
            raise EnvelopeValidationError("Unsupported key-derivation function.")

        iterations = envelope["iterations"]
        if not isinstance(iterations, int) or isinstance(iterations, bool):
            raise EnvelopeValidationError("Iteration count must be an integer.")
        if not config.min_kdf_iterations <= iterations <= config.max_kdf_iterations:
            raise EnvelopeValidationError(
                "Iteration count is outside the permitted range "
                f"[{config.min_kdf_iterations}, {config.max_kdf_iterations}]."
            )

        slots = envelope["slots"]
        if not isinstance(slots, list):
            raise EnvelopeValidationError("Slots must be a list.")
        if len(slots) != config.slot_count:
            raise EnvelopeValidationError(
                f"Container must hold exactly {config.slot_count} slots."
            )

        for index, slot in enumerate(slots):
            self._validate_slot(index, slot)

        serialized = canonical_json(envelope)
        if len(serialized.encode("utf-8")) > config.max_envelope_bytes:
            raise EnvelopeValidationError(
                f"Container exceeds the maximum size of {config.max_envelope_bytes} bytes."
            )

    def _validate_slot(self, index: int, slot: Any) -> None:
        """Validate a single slot.

        Args:
            index: The slot's position, used only in error messages.
            slot: The slot mapping to validate.

        Raises:
            EnvelopeValidationError: If the slot is malformed or its
                ciphertext is not the fixed expected length.
        """
        config = self.config
        if not isinstance(slot, Mapping):
            raise EnvelopeValidationError(f"Slot {index} must be a JSON object.")
        if set(slot.keys()) != _SLOT_KEYS:
            raise EnvelopeValidationError(
                f"Slot {index} must contain exactly the keys {sorted(_SLOT_KEYS)}."
            )

        self._validate_hex(slot["salt"], config.salt_hex_length, index, "salt")
        self._validate_hex(slot["nonce"], config.nonce_hex_length, index, "nonce")

        ciphertext = slot["ct"]
        expected = config.expected_ct_b64_length()
        if not isinstance(ciphertext, str) or len(ciphertext) != expected:
            raise EnvelopeValidationError(
                f"Slot {index} ciphertext must be exactly {expected} base64 "
                "characters; every container must be the same fixed size."
            )
        try:
            base64.b64decode(ciphertext, validate=True)
        except (binascii.Error, ValueError) as exc:
            raise EnvelopeValidationError(
                f"Slot {index} ciphertext is not valid base64."
            ) from exc

    @staticmethod
    def _validate_hex(value: Any, expected_length: int, index: int, field: str) -> None:
        """Validate that ``value`` is hex of exactly ``expected_length``.

        Raises:
            EnvelopeValidationError: If the value is not a hex string of
                the expected length.
        """
        if not isinstance(value, str) or len(value) != expected_length:
            raise EnvelopeValidationError(
                f"Slot {index} {field} must be {expected_length} hex characters."
            )
        if any(char not in _HEX_DIGITS for char in value):
            raise EnvelopeValidationError(
                f"Slot {index} {field} must be hexadecimal."
            )


class DeniableVaultController:
    """Coordinate validation, provisioning, persistence, and auditing."""

    # A single, deliberately generic audit event for every container
    # write. Provisioning, activation, and reset all emit the same event
    # so the log never reveals which write activated a hidden vault.
    _WRITE_EVENT = "account_object_write"

    def __init__(
        self,
        db: DeniableVaultDB,
        config: DeniableVaultConfig,
        validator: Optional[EnvelopeValidator] = None,
    ) -> None:
        """Initialize the controller.

        Args:
            db: The opaque container store.
            config: The structural limits in force.
            validator: The validator to use. Defaults to one bound to
                ``config``; injectable for tests.
        """
        self.db = db
        self.config = config
        self.validator = validator or EnvelopeValidator(config)

    def load_or_provision(self, username: str) -> dict[str, Any]:
        """Return ``username``'s container, minting a random one if absent.

        The mint-on-read behavior is what makes "has a container"
        universal: any account that has ever opened its settings has an
        indistinguishable container, so the mere existence of one is not
        evidence of a hidden vault.

        Args:
            username: The owning account.

        Returns:
            The decoded envelope, always present.
        """
        row = self.db.get(username)
        if row:
            return json.loads(row["envelope"])
        envelope = self.config.random_container()
        self.db.upsert(username, canonical_json(envelope))
        audit_event(self._WRITE_EVENT, username=username)
        return envelope

    def save(self, username: str, envelope: Mapping[str, Any]) -> None:
        """Validate and persist a container for ``username``.

        Args:
            username: The owning account.
            envelope: The decoded JSON envelope from the client.

        Raises:
            EnvelopeValidationError: If the envelope is structurally
                invalid; nothing is persisted in that case.
        """
        self.validator.validate(envelope)
        self.db.upsert(username, canonical_json(envelope))
        audit_event(self._WRITE_EVENT, username=username)

    def reset(self, username: str) -> dict[str, Any]:
        """Overwrite ``username``'s container with a fresh random one.

        Reset replaces rather than deletes: removing the row would leave a
        gap that distinguishes a user who deactivated from one who never
        activated. A random container keeps existence universal.

        Args:
            username: The owning account.

        Returns:
            The new random envelope.
        """
        envelope = self.config.random_container()
        self.db.upsert(username, canonical_json(envelope))
        audit_event(self._WRITE_EVENT, username=username)
        return envelope

    def exists(self, username: str) -> bool:
        """Return True if ``username`` already has a stored container."""
        return self.db.exists(username)
