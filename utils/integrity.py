"""Subresource Integrity manifest helpers (QV-SRI-1).

The manifest at ``static/sri_manifest.json`` pins the exact bytes of
every first-party script and stylesheet plus every pinned CDN URL. It
is generated with ``tools/generate_sri.py`` and checked with
``tools/verify_build.py``. Templates read values through
:func:`integrity_for` so the served HTML always carries the hash of the
audited bytes, and a compromised static file or a swapped CDN payload
fails closed in the browser instead of executing.
"""

from __future__ import annotations

import base64
import functools
import hashlib
import json
from pathlib import Path
from typing import Optional

SRI_ALGORITHM: str = "sha384"
MANIFEST_RELATIVE_PATH: str = "static/sri_manifest.json"


def manifest_path() -> Path:
    """Return the manifest path resolved from this file, never hardcoded."""
    return Path(__file__).resolve().parent.parent / MANIFEST_RELATIVE_PATH


def compute_sri(data: bytes, algorithm: str = SRI_ALGORITHM) -> str:
    """Return the SRI string ``<algorithm>-<base64 digest>`` for ``data``."""
    digest = hashlib.new(algorithm, data).digest()
    return algorithm + "-" + base64.b64encode(digest).decode("ascii")


def compute_file_sri(path: Path, algorithm: str = SRI_ALGORITHM) -> str:
    """Return the SRI string for the bytes stored at ``path``."""
    return compute_sri(path.read_bytes(), algorithm)


@functools.lru_cache(maxsize=1)
def _cached_manifest_text() -> str:
    """Return the raw manifest text, cached for the process lifetime."""
    return manifest_path().read_text(encoding="utf-8")


def load_manifest() -> dict:
    """Return the parsed SRI manifest, or an empty mapping when absent."""
    try:
        return json.loads(_cached_manifest_text())
    except (FileNotFoundError, ValueError):
        return {}


def integrity_for(key: str) -> Optional[str]:
    """Return the pinned integrity string for one manifest key.

    Args:
        key: Either a first-party asset path such as ``js/qv-crypto.js``
            or a full CDN URL.

    Returns:
        The pinned ``sha384-...`` value, or ``None`` when unpinned.
    """
    manifest = load_manifest()
    assets = manifest.get("assets", {})
    if key in assets:
        return assets[key]
    return manifest.get("cdn", {}).get(key)


def clear_manifest_cache() -> None:
    """Drop the cached manifest text so tests see a regenerated file."""
    _cached_manifest_text.cache_clear()


def template_integrity(key: str) -> str:
    """Return the integrity string for a template asset reference.

    Accepts the same reference the template already uses: a ``/static/``
    path is normalized to its manifest key, and a full CDN URL resolves
    to the CDN pin. Returns an empty string when unpinned so a missing
    entry fails closed in ``verify_build`` instead of rendering ``None``.
    """
    normalized = key
    if normalized.startswith("/static/"):
        normalized = normalized[len("/static/"):]
    found = integrity_for(normalized)
    if found is not None:
        return found
    return integrity_for(key) or ""
