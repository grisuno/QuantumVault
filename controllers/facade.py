"""QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.

The facade hides QuantumVault behind an innocuous cover application. A
secret phrase typed into the cover's search field is the first gate: a
correct phrase issues a short-lived signed ticket and marks the session
``real`` or ``duress``; either way the ordinary login page is revealed,
so an onlooker cannot tell which phrase was used.

This module is the server-side core. It never stores a phrase, never
echoes one into the audit log, and performs the same Argon2id work for a
miss, the real phrase, and the duress phrase so the response is not an
oracle. The zero-knowledge guarantees of SRP-6a and the deniable vault do
not depend on this layer.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping, Optional, Tuple

from argon2 import PasswordHasher as _Argon2PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

from utils.security import audit_event

_DEFAULT_ENABLED = False
_DEFAULT_GATE_HASH = ""
_DEFAULT_DURESS_GATE_HASH = ""
_DEFAULT_COVER_BRAND = "Findex"
_DEFAULT_COVER_TITLE = "Findex"
_DEFAULT_COVER_TAGLINE = "Search the web"
_DEFAULT_COVER_BODY = "Search the web for pages, images, and answers."
_DEFAULT_COVER_FOOTER = "Findex is a free service."
_DEFAULT_CONTACT_EMAIL = "support@example.org"
_DEFAULT_NEWSLETTER_LABEL = "Search"
_DEFAULT_NEWSLETTER_ACTION = "Search"
_DEFAULT_COVER_TEMPLATE = "search_portal"
_DEFAULT_COVER_CUSTOM_TEMPLATE = ""
_DEFAULT_COVER_DIR = "instance/cover_templates"
_DEFAULT_GATE_FIELD = "q"
_DEFAULT_TICKET_TTL_SECONDS = 120
_DEFAULT_MIN_PHRASE_LENGTH = 8
_DEFAULT_MAX_PHRASE_LENGTH = 256
_DEFAULT_HIDE_LOGIN = True
_DEFAULT_PROTECTED_PATHS = ("/", "/login", "/register", "/recover")
_DEFAULT_DURESS_ALERT = False
_DEFAULT_ARGON2_TIME_COST = 3
_DEFAULT_ARGON2_MEMORY_COST = 65536
_DEFAULT_ARGON2_PARALLELISM = 4
_DEFAULT_ARGON2_HASH_LEN = 32
_DEFAULT_ARGON2_SALT_LEN = 16

_TICKET_SALT = "qv-facade-gate-v1"
_AUDIT_COVER_QUERY = "cover_query"
_AUDIT_DURESS_ALERT = "account_priority_signal"

_TRUTHY = frozenset({"1", "true", "yes", "on"})


class GateOutcome(Enum):
    """Classification of a submitted gate phrase."""

    REAL = "real"
    DURESS = "duress"
    MISS = "miss"


@dataclass(frozen=True)
class GateDecision:
    """The outcome of evaluating a phrase plus any issued ticket."""

    outcome: GateOutcome
    ticket: Optional[str]


def _as_bool(value: Any, default: bool) -> bool:
    """Coerce an environment or mapping value to a boolean."""
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in _TRUTHY


def _as_int(value: Any, default: int) -> int:
    """Coerce an environment or mapping value to an integer."""
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _as_text(value: Any, default: str) -> str:
    """Coerce a value to non-empty text, falling back to ``default``."""
    if value is None:
        return default
    text = str(value).strip()
    return text if text else default


def _as_raw_text(value: Any, default: str) -> str:
    """Coerce a value to text without substituting an empty default."""
    return default if value is None else str(value)


def _as_paths(value: Any, default: Tuple[str, ...]) -> Tuple[str, ...]:
    """Parse a comma-separated path list into a tuple of stripped paths."""
    if value is None:
        return default
    if isinstance(value, str):
        items = [part.strip() for part in value.split(",")]
    else:
        items = [str(part).strip() for part in value]
    paths = tuple(part for part in items if part)
    return paths if paths else default


@dataclass(frozen=True)
class FacadeConfig:
    """Immutable facade configuration resolved from environment and app config."""

    enabled: bool = _DEFAULT_ENABLED
    gate_hash: str = _DEFAULT_GATE_HASH
    duress_gate_hash: str = _DEFAULT_DURESS_GATE_HASH
    cover_brand: str = _DEFAULT_COVER_BRAND
    cover_title: str = _DEFAULT_COVER_TITLE
    cover_tagline: str = _DEFAULT_COVER_TAGLINE
    cover_headline: str = _DEFAULT_COVER_BRAND
    cover_body: str = _DEFAULT_COVER_BODY
    cover_footer: str = _DEFAULT_COVER_FOOTER
    contact_email: str = _DEFAULT_CONTACT_EMAIL
    newsletter_label: str = _DEFAULT_NEWSLETTER_LABEL
    newsletter_action: str = _DEFAULT_NEWSLETTER_ACTION
    cover_template: str = _DEFAULT_COVER_TEMPLATE
    cover_custom_template: str = _DEFAULT_COVER_CUSTOM_TEMPLATE
    cover_dir: str = _DEFAULT_COVER_DIR
    gate_field: str = _DEFAULT_GATE_FIELD
    ticket_ttl_seconds: int = _DEFAULT_TICKET_TTL_SECONDS
    min_phrase_length: int = _DEFAULT_MIN_PHRASE_LENGTH
    max_phrase_length: int = _DEFAULT_MAX_PHRASE_LENGTH
    hide_login: bool = _DEFAULT_HIDE_LOGIN
    protected_paths: Tuple[str, ...] = _DEFAULT_PROTECTED_PATHS
    duress_alert: bool = _DEFAULT_DURESS_ALERT
    argon2_time_cost: int = _DEFAULT_ARGON2_TIME_COST
    argon2_memory_cost: int = _DEFAULT_ARGON2_MEMORY_COST
    argon2_parallelism: int = _DEFAULT_ARGON2_PARALLELISM

    @property
    def gate_configured(self) -> bool:
        """Return whether the facade is enabled and holds a real gate hash."""
        return self.enabled and bool(self.gate_hash)

    def cover_context(self) -> dict:
        """Return the cosmetic cover context, never carrying a gate hash."""
        return {
            "brand": self.cover_brand,
            "title": self.cover_title,
            "tagline": self.cover_tagline,
        }

    def cover_variables(self) -> dict:
        """Return the sanitizable cover variable payload."""
        return {
            "brand": self.cover_brand,
            "title": self.cover_title,
            "tagline": self.cover_tagline,
            "headline": self.cover_headline,
            "body_text": self.cover_body,
            "footer_text": self.cover_footer,
            "contact_email": self.contact_email,
            "newsletter_label": self.newsletter_label,
            "newsletter_action": self.newsletter_action,
        }

    @classmethod
    def from_mapping(
        cls,
        mapping: Mapping[str, Any],
        env: Optional[Mapping[str, str]] = None,
    ) -> "FacadeConfig":
        """Resolve configuration with environment, mapping, then default order."""
        source = os.environ if env is None else env

        def read(key: str) -> Any:
            if key in source:
                return source[key]
            if key in mapping:
                return mapping[key]
            return None

        defaults = cls()
        return cls(
            enabled=_as_bool(read("QV_FACADE_ENABLED"), defaults.enabled),
            gate_hash=_as_raw_text(read("QV_FACADE_GATE_HASH"), defaults.gate_hash),
            duress_gate_hash=_as_raw_text(
                read("QV_FACADE_DURESS_GATE_HASH"), defaults.duress_gate_hash
            ),
            cover_brand=_as_text(read("QV_FACADE_COVER_BRAND"), defaults.cover_brand),
            cover_title=_as_text(read("QV_FACADE_COVER_TITLE"), defaults.cover_title),
            cover_tagline=_as_text(
                read("QV_FACADE_COVER_TAGLINE"), defaults.cover_tagline
            ),
            cover_headline=_as_text(
                read("QV_FACADE_COVER_HEADLINE"), defaults.cover_headline
            ),
            cover_body=_as_raw_text(
                read("QV_FACADE_COVER_BODY"), defaults.cover_body
            ),
            cover_footer=_as_raw_text(
                read("QV_FACADE_COVER_FOOTER"), defaults.cover_footer
            ),
            contact_email=_as_text(
                read("QV_FACADE_CONTACT_EMAIL"), defaults.contact_email
            ),
            newsletter_label=_as_text(
                read("QV_FACADE_NEWSLETTER_LABEL"), defaults.newsletter_label
            ),
            newsletter_action=_as_text(
                read("QV_FACADE_NEWSLETTER_ACTION"), defaults.newsletter_action
            ),
            cover_template=_as_text(
                read("QV_FACADE_COVER_TEMPLATE"), defaults.cover_template
            ),
            cover_custom_template=_as_raw_text(
                read("QV_FACADE_COVER_CUSTOM_TEMPLATE"), defaults.cover_custom_template
            ),
            cover_dir=_as_text(read("QV_FACADE_COVER_DIR"), defaults.cover_dir),
            gate_field=_as_text(read("QV_FACADE_GATE_FIELD"), defaults.gate_field),
            ticket_ttl_seconds=_as_int(
                read("QV_FACADE_TICKET_TTL_SECONDS"), defaults.ticket_ttl_seconds
            ),
            min_phrase_length=_as_int(
                read("QV_FACADE_MIN_PHRASE_LENGTH"), defaults.min_phrase_length
            ),
            max_phrase_length=_as_int(
                read("QV_FACADE_MAX_PHRASE_LENGTH"), defaults.max_phrase_length
            ),
            hide_login=_as_bool(read("QV_FACADE_HIDE_LOGIN"), defaults.hide_login),
            protected_paths=_as_paths(
                read("QV_FACADE_PROTECTED_PATHS"), defaults.protected_paths
            ),
            duress_alert=_as_bool(
                read("QV_FACADE_DURESS_ALERT"), defaults.duress_alert
            ),
            argon2_time_cost=_as_int(
                read("QV_FACADE_ARGON2_TIME_COST"), defaults.argon2_time_cost
            ),
            argon2_memory_cost=_as_int(
                read("QV_FACADE_ARGON2_MEMORY_COST"), defaults.argon2_memory_cost
            ),
            argon2_parallelism=_as_int(
                read("QV_FACADE_ARGON2_PARALLELISM"), defaults.argon2_parallelism
            ),
        )


class GatePhraseHasher:
    """Argon2id hashing and verification for a human-chosen gate phrase."""

    def __init__(
        self,
        time_cost: int = _DEFAULT_ARGON2_TIME_COST,
        memory_cost: int = _DEFAULT_ARGON2_MEMORY_COST,
        parallelism: int = _DEFAULT_ARGON2_PARALLELISM,
        hash_len: int = _DEFAULT_ARGON2_HASH_LEN,
        salt_len: int = _DEFAULT_ARGON2_SALT_LEN,
    ) -> None:
        """Bind the hasher to explicit Argon2id cost parameters."""
        self._hasher = _Argon2PasswordHasher(
            time_cost=time_cost,
            memory_cost=memory_cost,
            parallelism=parallelism,
            hash_len=hash_len,
            salt_len=salt_len,
        )

    def hash(self, phrase: str) -> str:
        """Return a salted Argon2id digest of ``phrase``."""
        return self._hasher.hash(phrase)

    def verify(self, phrase: str, encoded: str) -> bool:
        """Return whether ``phrase`` matches ``encoded`` without raising."""
        if not encoded or not isinstance(encoded, str):
            return False
        try:
            return self._hasher.verify(encoded, phrase)
        except (VerifyMismatchError, VerificationError, InvalidHashError):
            return False

    @classmethod
    def from_config(cls, config: FacadeConfig) -> "GatePhraseHasher":
        """Build a hasher using the cost parameters of ``config``."""
        return cls(
            time_cost=config.argon2_time_cost,
            memory_cost=config.argon2_memory_cost,
            parallelism=config.argon2_parallelism,
        )


class GateTicket:
    """Short-lived signed ticket binding a session to a gate mode."""

    def __init__(self, secret_key: str, ttl_seconds: int) -> None:
        """Bind the ticket signer to the app secret and a lifetime."""
        self._serializer = URLSafeTimedSerializer(secret_key, salt=_TICKET_SALT)
        self._ttl_seconds = ttl_seconds
        self._allowed_modes = frozenset(
            (GateOutcome.REAL.value, GateOutcome.DURESS.value)
        )

    def issue(self, mode: str) -> str:
        """Return a signed ticket for ``mode`` or raise for an unknown mode."""
        if mode not in self._allowed_modes:
            raise ValueError(f"unknown gate mode: {mode!r}")
        return self._serializer.dumps({"m": mode})

    def verify(self, token: object) -> Optional[str]:
        """Return the ticket mode, or ``None`` if expired, tampered, or absent."""
        if not isinstance(token, str) or not token:
            return None
        try:
            payload = self._serializer.loads(token, max_age=self._ttl_seconds)
        except (BadSignature, SignatureExpired):
            return None
        if not isinstance(payload, dict):
            return None
        mode = payload.get("m")
        return mode if mode in self._allowed_modes else None


class FacadeGate:
    """Evaluate gate phrases and issue tickets with constant observable work."""

    def __init__(
        self,
        config: FacadeConfig,
        hasher: GatePhraseHasher,
        ticket: GateTicket,
    ) -> None:
        """Bind the gate to its configuration and collaborators."""
        self.config = config
        self.hasher = hasher
        self.ticket = ticket

    @classmethod
    def build(cls, config: FacadeConfig, secret_key: str) -> "FacadeGate":
        """Build a gate from configuration and the application secret."""
        return cls(
            config=config,
            hasher=GatePhraseHasher.from_config(config),
            ticket=GateTicket(secret_key, config.ticket_ttl_seconds),
        )

    def evaluate(self, phrase: object) -> GateDecision:
        """Classify a phrase and emit only a generic audit event."""
        audit_event(_AUDIT_COVER_QUERY)
        text = phrase if isinstance(phrase, str) else ""
        within_length = self.config.min_phrase_length <= len(text) <= self.config.max_phrase_length
        candidate = text[: self.config.max_phrase_length]
        real_match = self.hasher.verify(candidate, self.config.gate_hash) and within_length
        duress_match = False
        if self.config.duress_gate_hash:
            duress_match = (
                self.hasher.verify(candidate, self.config.duress_gate_hash) and within_length
            )
        if real_match:
            return GateDecision(
                GateOutcome.REAL, self.ticket.issue(GateOutcome.REAL.value)
            )
        if duress_match:
            if self.config.duress_alert:
                audit_event(_AUDIT_DURESS_ALERT)
            return GateDecision(
                GateOutcome.DURESS, self.ticket.issue(GateOutcome.DURESS.value)
            )
        return GateDecision(GateOutcome.MISS, None)
