"""Generate the SRI manifest for first-party assets and pinned CDN URLs.

Regenerating the manifest is the audited step that binds served bytes
to served hashes. The output is deterministic: keys are sorted, the
JSON uses a fixed indent, and the file ends with a single newline, so
two runs over identical inputs produce byte-identical output.

Usage:
    ./.venv/bin/python tools/generate_sri.py
    ./.venv/bin/python tools/generate_sri.py --check
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.integrity import SRI_ALGORITHM, compute_file_sri, compute_sri

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = PROJECT_ROOT / "static"
MANIFEST_PATH = PROJECT_ROOT / "static" / "sri_manifest.json"
LOCAL_SUFFIXES: tuple[str, ...] = (".js", ".css")

PINNED_CDN_URLS: tuple[str, ...] = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
    "https://cdn.jsdelivr.net/npm/easymde/dist/easymde.min.css",
    "https://cdn.jsdelivr.net/npm/easymde/dist/easymde.min.js",
    "https://cdn.jsdelivr.net/npm/marked/marked.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/jsencrypt/3.3.2/jsencrypt.min.js",
)


def collect_local_assets() -> dict[str, str]:
    """Hash every first-party script and stylesheet under ``static/``."""
    assets: dict[str, str] = {}
    for path in sorted(STATIC_DIR.rglob("*")):
        if not path.is_file():
            continue
        if path.name == "sri_manifest.json":
            continue
        if path.suffix.lower() not in LOCAL_SUFFIXES:
            continue
        relative = path.relative_to(STATIC_DIR).as_posix()
        assets[relative] = compute_file_sri(path, SRI_ALGORITHM)
    return assets


def fetch_cdn_assets() -> dict[str, str]:
    """Download every pinned CDN URL and hash its exact bytes."""
    assets: dict[str, str] = {}
    for url in PINNED_CDN_URLS:
        with urllib.request.urlopen(url, timeout=30) as response:
            body = response.read()
        assets[url] = compute_sri(body, SRI_ALGORITHM)
    return assets


def build_manifest(cdn: dict[str, str], local: dict[str, str]) -> dict:
    """Assemble the deterministic manifest document."""
    return {
        "version": 1,
        "algorithm": SRI_ALGORITHM,
        "assets": dict(sorted(local.items())),
        "cdn": dict(sorted(cdn.items())),
    }


def render_manifest(manifest: dict) -> str:
    """Render the manifest deterministically with a trailing newline."""
    return json.dumps(manifest, indent=2, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    """Generate the manifest, or verify it is current with ``--check``."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 when the on-disk manifest differs from a fresh build",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="skip CDN downloads and reuse pinned CDN hashes from disk",
    )
    arguments = parser.parse_args(argv)
    local = collect_local_assets()
    if arguments.offline and MANIFEST_PATH.exists():
        previous = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cdn = dict(previous.get("cdn", {}))
        for url in PINNED_CDN_URLS:
            if url not in cdn:
                raise SystemExit("offline mode lacks a pinned hash for " + url)
    else:
        cdn = fetch_cdn_assets()
    text = render_manifest(build_manifest(cdn, local))
    if arguments.check:
        if not MANIFEST_PATH.exists():
            print("manifest missing: " + str(MANIFEST_PATH))
            return 1
        current = MANIFEST_PATH.read_text(encoding="utf-8")
        if current != text:
            print("manifest is stale: regenerate with tools/generate_sri.py")
            return 1
        print("manifest is current")
        return 0
    MANIFEST_PATH.write_text(text, encoding="utf-8")
    print("wrote " + str(MANIFEST_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
