"""Pure-Python SRP-6a (QV-SRP-1) roundtrip test.

Mirrors the client-side math in ``static/js/qv-crypto.js`` (``deriveVerifier``
and ``srpLogin``) using only :mod:`utils.srp6a`, so this test exercises the
exact server primitives without needing Redis, Flask, or a browser.
"""

from __future__ import annotations

import hashlib
import secrets

from utils import srp6a


def _h(*chunks: bytes) -> bytes:
    digest = hashlib.sha256()
    for chunk in chunks:
        digest.update(chunk)
    return digest.digest()


def _hint(*chunks: bytes) -> int:
    return int.from_bytes(_h(*chunks), byteorder="big")


def _client_derive_verifier(username: str, password: str, salt_hex: str) -> int:
    """Mirror ``deriveVerifier`` in qv-crypto.js: v = g^x mod N."""
    inner = _h(f"{username}:{password}".encode("utf-8"))
    x = _hint(bytes.fromhex(salt_hex), inner)
    return pow(srp6a.g, x, srp6a.N)


def _client_compute_proof(
    username: str,
    password: str,
    salt_hex: str,
    server_a_secret: int,
    server_a: int,
    server_b: int,
) -> tuple[bytes, bytes]:
    """Mirror ``srpLogin`` in qv-crypto.js: derive M1 and the expected M2."""
    k = srp6a.compute_k()
    u = srp6a.compute_u(server_a, server_b)
    assert u != 0

    inner = _h(f"{username}:{password}".encode("utf-8"))
    x = _hint(bytes.fromhex(salt_hex), inner)

    shared = pow(
        (server_b - (k * pow(srp6a.g, x, srp6a.N)) % srp6a.N) % srp6a.N,
        server_a_secret + u * x,
        srp6a.N,
    )
    session_key = _h(srp6a.i2osp(shared))

    h_n = _h(srp6a.i2osp(srp6a.N))
    h_g = _h(srp6a.i2osp(srp6a.g))
    h_xor = bytes(a ^ b for a, b in zip(h_n, h_g))
    h_identity = _h(username.encode("utf-8"))

    m1 = _h(
        h_xor,
        h_identity,
        bytes.fromhex(salt_hex),
        srp6a.i2osp(server_a),
        srp6a.i2osp(server_b),
        session_key,
    )
    m2 = _h(srp6a.i2osp(server_a), m1, session_key)
    return m1, m2


def test_srp6a_full_roundtrip_matches_server_proofs():
    username = "alice"
    password = "correct horse battery staple"
    salt_hex = secrets.token_hex(16)

    verifier = _client_derive_verifier(username, password, salt_hex)

    server_a_secret = secrets.randbits(srp6a.EPHEMERAL_PRIVATE_BITS)
    server_a = pow(srp6a.g, server_a_secret, srp6a.N)

    server_b_secret, server_b = srp6a.generate_server_challenge(verifier)
    assert server_b % srp6a.N != 0

    client_m1, client_m2 = _client_compute_proof(
        username, password, salt_hex, server_a_secret, server_a, server_b
    )

    expected_m1, server_m2 = srp6a.compute_proofs(
        username=username,
        salt_hex=salt_hex,
        verifier=verifier,
        server_a=server_a,
        server_b=server_b,
        server_b_secret=server_b_secret,
    )

    assert client_m1 == expected_m1
    assert client_m2 == server_m2


def test_srp6a_wrong_password_produces_mismatched_proof():
    username = "alice"
    password = "correct horse battery staple"
    wrong_password = "incorrect horse battery staple"
    salt_hex = secrets.token_hex(16)

    verifier = _client_derive_verifier(username, password, salt_hex)

    server_a_secret = secrets.randbits(srp6a.EPHEMERAL_PRIVATE_BITS)
    server_a = pow(srp6a.g, server_a_secret, srp6a.N)

    server_b_secret, server_b = srp6a.generate_server_challenge(verifier)

    client_m1, _ = _client_compute_proof(
        username, wrong_password, salt_hex, server_a_secret, server_a, server_b
    )

    expected_m1, _ = srp6a.compute_proofs(
        username=username,
        salt_hex=salt_hex,
        verifier=verifier,
        server_a=server_a,
        server_b=server_b,
        server_b_secret=server_b_secret,
    )

    assert client_m1 != expected_m1
