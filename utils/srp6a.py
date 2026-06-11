"""Zero-knowledge SRP-6a authentication primitives for QuantumVault.

This module implements the server side of a Secure Remote Password (SRP-6a)
handshake using the RFC 5054 2048-bit group with SHA-256. The user's password
never reaches the server: registration stores only ``salt`` and the password
verifier ``v = g**x mod N``; authentication is a challenge/response that proves
knowledge of the password without transmitting it.

The serialization scheme ("QV-SRP-1") is implemented identically in the browser
module ``static/js/qv-crypto.js`` so both ends agree byte-for-byte:

    - Every group element hashed (N, g, A, B, S) is encoded as a big-endian
      integer left-padded to the byte length of N (256 bytes) via :func:`i2osp`.
    - ``H`` is SHA-256 over the concatenation of byte strings.
    - ``salt`` travels as a hex string; its raw bytes are used inside hashes.

Public functions perform the SRP math; :class:`SRPSessionStore` persists the
ephemeral per-login server state in Redis with a short time-to-live.
"""

import hashlib
import hmac
import json
import secrets
from typing import Optional, Tuple

import redis

N_HEX = (
    "AC6BDB41324A9A9BF166DE5E1389582FAF72B6651987EE07FC3192943DB56050"
    "A37329CBB4A099ED8193E0757767A13DD52312AB4B03310DCD7F48A9DA04FD50"
    "E8083969EDB767B0CF6095179A163AB3661A05FBD5FAAAE82918A9962F0B93B8"
    "55F97993EC975EEAA80D740ADBF4FF747359D041D5C33EA71D281E446B14773B"
    "CA97B43A23FB801676BD207A436C6481F1D2B9078717461A5B9D32E688F87748"
    "544523B524B0D57D5EA77A2775D2ECFA032CFBDBF52FB3786160279004E57AE6"
    "AF874E7303CE53299CCC041C7BC308D82A5698F3A8D0C38271AE35F8E9DBFBB6"
    "94B5C803D89F7AE435DE236D525F54759B65E372FCD68EF20FA7111F9E4AFF73"
)
N = int(N_HEX, 16)
g = 2
N_BYTE_LENGTH = (N.bit_length() + 7) // 8

SESSION_TTL_SECONDS = 60
EPHEMERAL_PRIVATE_BITS = 256


def i2osp(value: int) -> bytes:
    """Encode an integer as a big-endian byte string padded to the length of N.

    Args:
        value: Non-negative integer to encode (a group element).

    Returns:
        The big-endian representation left-padded with zero bytes to
        ``N_BYTE_LENGTH``.
    """
    return value.to_bytes(N_BYTE_LENGTH, byteorder="big")


def _hash(*chunks: bytes) -> bytes:
    """Return the SHA-256 digest of the concatenated byte chunks."""
    digest = hashlib.sha256()
    for chunk in chunks:
        digest.update(chunk)
    return digest.digest()


def _hash_int(*chunks: bytes) -> int:
    """Return the SHA-256 digest of the concatenated chunks as an integer."""
    return int.from_bytes(_hash(*chunks), byteorder="big")


def compute_k() -> int:
    """Compute the SRP-6a multiplier parameter ``k = H(N | PAD(g))``."""
    return _hash_int(i2osp(N), i2osp(g))


def compute_u(server_a: int, server_b: int) -> int:
    """Compute the random scrambling parameter ``u = H(PAD(A) | PAD(B))``.

    Args:
        server_a: The client public ephemeral value A.
        server_b: The server public ephemeral value B.

    Returns:
        The scrambling parameter u as an integer.
    """
    return _hash_int(i2osp(server_a), i2osp(server_b))


def generate_server_challenge(verifier: int) -> Tuple[int, int]:
    """Generate the server ephemeral key pair (b, B) for a login challenge.

    Args:
        verifier: The stored password verifier ``v`` for the user.

    Returns:
        A tuple ``(b, B)`` where ``b`` is the secret ephemeral and
        ``B = (k * v + g**b) mod N`` is the public value sent to the client.
    """
    k = compute_k()
    b = secrets.randbits(EPHEMERAL_PRIVATE_BITS)
    server_b = (k * verifier + pow(g, b, N)) % N
    return b, server_b


def compute_proofs(
    username: str,
    salt_hex: str,
    verifier: int,
    server_a: int,
    server_b: int,
    server_b_secret: int,
) -> Tuple[bytes, bytes]:
    """Compute the expected client proof M1 and the server proof M2.

    Args:
        username: The user identity I.
        salt_hex: The user salt as a hex string.
        verifier: The stored password verifier v.
        server_a: The client public ephemeral A.
        server_b: The server public ephemeral B.
        server_b_secret: The server secret ephemeral b.

    Returns:
        A tuple ``(expected_m1, m2)`` of raw digest bytes.
    """
    salt_bytes = bytes.fromhex(salt_hex)
    u = compute_u(server_a, server_b)
    shared = pow(server_a * pow(verifier, u, N) % N, server_b_secret, N)
    session_key = _hash(i2osp(shared))

    h_n = _hash(i2osp(N))
    h_g = _hash(i2osp(g))
    h_xor = bytes(a ^ b for a, b in zip(h_n, h_g))
    h_identity = _hash(username.encode("utf-8"))

    expected_m1 = _hash(
        h_xor,
        h_identity,
        salt_bytes,
        i2osp(server_a),
        i2osp(server_b),
        session_key,
    )
    m2 = _hash(i2osp(server_a), expected_m1, session_key)
    return expected_m1, m2


class SRPSessionStore:
    """Redis-backed store for the ephemeral state of an in-flight SRP login.

    Each ``hello`` step persists the values needed to verify the subsequent
    ``verify`` step. Entries expire after :data:`SESSION_TTL_SECONDS` so an
    abandoned handshake cannot be resumed later.
    """

    def __init__(self, storage_uri: str):
        """Initialize the store from a Redis connection URI.

        Args:
            storage_uri: A ``redis://`` connection string (the same one used by
                the rate limiter).
        """
        self._redis = redis.Redis.from_url(storage_uri)

    @staticmethod
    def _key(username: str) -> str:
        """Return the Redis key for a username's pending SRP session."""
        return f"srp:session:{username}"

    def save(
        self,
        username: str,
        salt_hex: str,
        verifier_hex: str,
        server_a_hex: str,
        server_b_hex: str,
        server_b_secret_hex: str,
    ) -> None:
        """Persist the ephemeral SRP challenge state for a username.

        Args:
            username: The user identity.
            salt_hex: The user salt as a hex string.
            verifier_hex: The stored verifier as a hex string.
            server_a_hex: The client public ephemeral A as a hex string.
            server_b_hex: The server public ephemeral B as a hex string.
            server_b_secret_hex: The server secret ephemeral b as a hex string.
        """
        payload = json.dumps(
            {
                "salt": salt_hex,
                "verifier": verifier_hex,
                "A": server_a_hex,
                "B": server_b_hex,
                "b": server_b_secret_hex,
            }
        )
        self._redis.setex(self._key(username), SESSION_TTL_SECONDS, payload)

    def load(self, username: str) -> Optional[dict]:
        """Load and consume the ephemeral SRP state for a username.

        The entry is deleted on read so each challenge is single-use.

        Args:
            username: The user identity.

        Returns:
            The stored session dictionary, or ``None`` if no valid session
            exists (expired, missing, or already consumed).
        """
        key = self._key(username)
        pipeline = self._redis.pipeline()
        pipeline.get(key)
        pipeline.delete(key)
        raw, _ = pipeline.execute()
        if not raw:
            return None
        return json.loads(raw)


def hello(
    store: SRPSessionStore,
    username: str,
    client_a_hex: str,
    salt_hex: str,
    verifier_hex: str,
) -> Optional[str]:
    """Process the SRP ``hello`` step and return the server challenge B.

    Args:
        store: The ephemeral session store.
        username: The user identity.
        client_a_hex: The client public ephemeral A as a hex string.
        salt_hex: The stored user salt as a hex string.
        verifier_hex: The stored verifier as a hex string.

    Returns:
        The server public ephemeral B as a hex string, or ``None`` if the
        client value A is invalid (``A mod N == 0``).
    """
    server_a = int(client_a_hex, 16)
    if server_a % N == 0:
        return None
    verifier = int(verifier_hex, 16)
    server_b_secret, server_b = generate_server_challenge(verifier)
    store.save(
        username=username,
        salt_hex=salt_hex,
        verifier_hex=verifier_hex,
        server_a_hex=format(server_a, "x"),
        server_b_hex=format(server_b, "x"),
        server_b_secret_hex=format(server_b_secret, "x"),
    )
    return format(server_b, "x")


def verify(
    store: SRPSessionStore,
    username: str,
    client_m1_hex: str,
) -> Optional[str]:
    """Process the SRP ``verify`` step and return the server proof M2.

    Args:
        store: The ephemeral session store.
        username: The user identity.
        client_m1_hex: The client proof M1 as a hex string.

    Returns:
        The server proof M2 as a hex string on success, or ``None`` if no
        pending session exists or the client proof is invalid.
    """
    session = store.load(username)
    if not session:
        return None

    expected_m1, m2 = compute_proofs(
        username=username,
        salt_hex=session["salt"],
        verifier=int(session["verifier"], 16),
        server_a=int(session["A"], 16),
        server_b=int(session["B"], 16),
        server_b_secret=int(session["b"], 16),
    )

    client_m1 = bytes.fromhex(client_m1_hex)
    if not hmac.compare_digest(expected_m1, client_m1):
        return None
    return m2.hex()
