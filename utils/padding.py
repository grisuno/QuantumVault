"""Fixed-bucket padding for metadata-size concealment (QV-PAD-1).

An observer who cannot read ciphertext can still read its length. This
module groups every plaintext into fixed buckets so the wire reveals
only a coarse size class instead of an exact byte count.

Wire format for one padded plaintext of bucket ``B``::

    LENGTH_PREFIX || PLAINTEXT || RANDOM_PAD

where ``LENGTH_PREFIX`` is the true plaintext length as a 4-byte
big-endian unsigned integer and ``RANDOM_PAD`` is fresh output from
:mod:`secrets` filling the remainder ``B - prefix - len(plaintext)``.
The padded plaintext is then encrypted with AES-256-GCM, so the stored
and transmitted ciphertext length is ``B + GCM_OVERHEAD_BYTES`` for
every plaintext inside the same bucket.

Cache safety contract: the only value ever cached is the immutable
bucket table itself, keyed by configuration version, never by message
content or message length. Padding bytes are drawn fresh from the
operating-system CSPRNG on every call and are never stored, reused, or
placed in any cache. Reusing pad bytes across envelopes would make
equal-length plaintexts produce related padded inputs, so reuse is
forbidden by construction: there is no API that accepts caller-supplied
pad bytes and no cache entry that holds them.

Bucket lookup always scans the full table so the number of iterations
does not depend on which bucket matched.
"""

from __future__ import annotations

import functools
import os
import secrets
import struct
from dataclasses import dataclass
from typing import Final, Literal

Kind = Literal["message", "file"]

LENGTH_PREFIX_BYTES: Final[int] = 4
GCM_IV_BYTES: Final[int] = 12
GCM_TAG_BYTES: Final[int] = 16
GCM_OVERHEAD_BYTES: Final[int] = GCM_IV_BYTES + GCM_TAG_BYTES

DEFAULT_MESSAGE_BUCKETS: Final[tuple[int, ...]] = (
    512,
    1024,
    2048,
    4096,
    8192,
    16384,
    32768,
    65536,
)
DEFAULT_FILE_BUCKETS: Final[tuple[int, ...]] = (
    65536,
    131072,
    262144,
    524288,
    1048576,
    2097152,
    4194304,
    8388608,
    10485760,
)

MESSAGE_BUCKETS_ENV_VAR: Final[str] = "QV_PAD_MESSAGE_BUCKETS"
FILE_BUCKETS_ENV_VAR: Final[str] = "QV_PAD_FILE_BUCKETS"


class PaddingError(ValueError):
    """Raised when data does not fit any bucket or framing is invalid."""


@dataclass(frozen=True, slots=True)
class PaddingConfig:
    """Immutable bucket tables for the two padded payload kinds."""

    message_buckets: tuple[int, ...] = DEFAULT_MESSAGE_BUCKETS
    file_buckets: tuple[int, ...] = DEFAULT_FILE_BUCKETS

    def buckets_for(self, kind: Kind) -> tuple[int, ...]:
        """Return the bucket table for ``kind``."""
        if kind == "message":
            return self.message_buckets
        return self.file_buckets

    def max_plaintext_bytes(self, kind: Kind) -> int:
        """Return the largest plaintext that fits ``kind``."""
        return max(self.buckets_for(kind)) - LENGTH_PREFIX_BYTES


def _parse_buckets(raw: str | None, fallback: tuple[int, ...]) -> tuple[int, ...]:
    """Parse a comma-separated bucket list, falling back on any error."""
    if not raw:
        return fallback
    try:
        values = tuple(int(part.strip()) for part in raw.split(",") if part.strip())
    except ValueError:
        return fallback
    cleaned = tuple(sorted({value for value in values if value > LENGTH_PREFIX_BYTES}))
    if len(cleaned) < 2:
        return fallback
    return cleaned


def config_from_env() -> PaddingConfig:
    """Build a :class:`PaddingConfig` from the environment.

    ``QV_PAD_MESSAGE_BUCKETS`` and ``QV_PAD_FILE_BUCKETS`` accept
    comma-separated byte sizes. Unset or malformed values resolve to the
    compiled defaults so a misconfigured host fails closed to a known
    table instead of disabling padding.
    """
    return PaddingConfig(
        message_buckets=_parse_buckets(
            os.environ.get(MESSAGE_BUCKETS_ENV_VAR), DEFAULT_MESSAGE_BUCKETS
        ),
        file_buckets=_parse_buckets(
            os.environ.get(FILE_BUCKETS_ENV_VAR), DEFAULT_FILE_BUCKETS
        ),
    )


@functools.lru_cache(maxsize=4)
def _cached_bucket_table(fingerprint: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return the cached immutable bucket tables for one config version.

    The cache key is the comma-joined bucket lists, so distinct operator
    configurations never share an entry. Only the tables are cached.
    Plaintexts, ciphertexts, lengths of individual payloads, and random
    pad bytes never enter this cache.
    """
    message_raw, _, file_raw = fingerprint.partition(";")
    message = _parse_buckets(message_raw or None, DEFAULT_MESSAGE_BUCKETS)
    file = _parse_buckets(file_raw or None, DEFAULT_FILE_BUCKETS)
    return (message, file)


def cached_tables(config: PaddingConfig) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return the process-wide cached bucket tables for ``config``."""
    fingerprint = ",".join(str(value) for value in config.message_buckets)
    fingerprint += ";" + ",".join(str(value) for value in config.file_buckets)
    return _cached_bucket_table(fingerprint)


def bucket_for(plaintext_len: int, kind: Kind, config: PaddingConfig | None = None) -> int:
    """Return the smallest bucket holding ``plaintext_len`` plus prefix.

    Raises:
        PaddingError: If the payload plus prefix exceeds every bucket.
    """
    cfg = config if config is not None else config_from_env()
    message_table, file_table = cached_tables(cfg)
    table = message_table if kind == "message" else file_table
    needed = plaintext_len + LENGTH_PREFIX_BYTES
    candidate = 0
    for bucket in table:
        fits = 1 if needed <= bucket else 0
        if fits == 1 and (candidate == 0 or bucket < candidate):
            candidate = bucket
    if candidate == 0:
        raise PaddingError("plaintext exceeds the largest bucket")
    return candidate


def pad(plaintext: bytes, kind: Kind, config: PaddingConfig | None = None) -> bytes:
    """Pad ``plaintext`` to its bucket with fresh CSPRNG bytes.

    Raises:
        PaddingError: If the payload does not fit any bucket.
    """
    if not isinstance(plaintext, (bytes, bytearray)):
        raise PaddingError("plaintext must be bytes")
    body = bytes(plaintext)
    bucket = bucket_for(len(body), kind, config)
    pad_len = bucket - LENGTH_PREFIX_BYTES - len(body)
    return struct.pack(">I", len(body)) + body + secrets.token_bytes(pad_len)


def unpad(padded: bytes, kind: Kind, config: PaddingConfig | None = None) -> bytes:
    """Remove bucket framing and return the original plaintext.

    Raises:
        PaddingError: If the length is not a bucket or framing is corrupt.
    """
    if not isinstance(padded, (bytes, bytearray)):
        raise PaddingError("padded payload must be bytes")
    body = bytes(padded)
    cfg = config if config is not None else config_from_env()
    message_table, file_table = cached_tables(cfg)
    table = message_table if kind == "message" else file_table
    allowed = 0
    for bucket in table:
        if len(body) == bucket:
            allowed = 1
    if allowed != 1:
        raise PaddingError("padded length is not a configured bucket")
    if len(body) < LENGTH_PREFIX_BYTES:
        raise PaddingError("padded payload too short")
    (declared,) = struct.unpack(">I", body[:LENGTH_PREFIX_BYTES])
    if declared > len(body) - LENGTH_PREFIX_BYTES:
        raise PaddingError("declared length exceeds bucket")
    return body[LENGTH_PREFIX_BYTES : LENGTH_PREFIX_BYTES + declared]


def wire_ciphertext_len(bucket: int) -> int:
    """Return the AES-256-GCM ciphertext length for one padded bucket."""
    return bucket + GCM_OVERHEAD_BYTES


def is_allowed_ciphertext_len(
    ciphertext_len: int, kind: Kind, config: PaddingConfig | None = None
) -> bool:
    """Return True when ``ciphertext_len`` matches a bucket plus GCM overhead."""
    cfg = config if config is not None else config_from_env()
    message_table, file_table = cached_tables(cfg)
    table = message_table if kind == "message" else file_table
    matched = 0
    for bucket in table:
        if ciphertext_len == bucket + GCM_OVERHEAD_BYTES:
            matched = 1
    return matched == 1
