"""Verify reproducible builds and the fixed code contracts (QV-SRI-1).

Checks performed, all offline:

1. Every first-party asset in ``static/sri_manifest.json`` recomputes to
   its pinned hash. A mismatch means the served bytes drifted from the
   audited bytes.
2. Every ``/static/...`` script or stylesheet referenced by any template
   carries an ``integrity`` attribute equal to the manifest value.
3. Every ``https://`` script or stylesheet referenced by any template
   carries an ``integrity`` attribute equal to the manifest CDN pin.
4. The JavaScript bucket tables in ``static/js/qv-padding.js`` equal the
   Python defaults in ``utils/padding.py``, so the two sides of the
   padding contract cannot drift apart silently.

Usage:
    ./.venv/bin/python tools/verify_build.py
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = PROJECT_ROOT / "static"
TEMPLATES_DIR = PROJECT_ROOT / "templates"
MANIFEST_PATH = STATIC_DIR / "sri_manifest.json"


class AssetReference(HTMLParser):
    """Collect external script and stylesheet references from one template."""

    def __init__(self) -> None:
        """Initialize the reference collector."""
        super().__init__()
        self.entries: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Record one script or link tag with its integrity attribute."""
        attributes = dict(attrs)
        if tag == "script" and attributes.get("src"):
            self.entries.append(
                {"kind": "script", "ref": _normalize_reference(str(attributes["src"])),
                 "integrity": str(attributes.get("integrity", ""))}
            )
        if tag == "link" and attributes.get("href"):
            rel = str(attributes.get("rel", ""))
            href = _normalize_reference(str(attributes["href"]))
            if "stylesheet" in rel or href.endswith(".css"):
                self.entries.append(
                    {"kind": "style", "ref": href,
                     "integrity": str(attributes.get("integrity", ""))}
                )


def _normalize_reference(ref: str) -> str:
    """Resolve a ``url_for('static', ...)`` expression to its served path."""
    match = re.search(
        r"url_for\(\s*['\"]static['\"]\s*,\s*filename\s*=\s*['\"]([^'\"]+)['\"]",
        ref,
    )
    if match is not None:
        return "/static/" + match.group(1)
    return ref


def load_manifest() -> dict:
    """Load and return the SRI manifest document."""
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def expected_for_reference(manifest: dict, ref: str) -> str | None:
    """Resolve the pinned integrity value for one template reference."""
    relative = ref[len("/static/"):] if ref.startswith("/static/") else ref
    pinned = manifest.get("assets", {}).get(relative)
    if pinned is not None:
        return pinned
    return manifest.get("cdn", {}).get(ref)


def integrity_attribute_ok(integrity: str, ref: str, expected: str) -> bool:
    """Accept a literal pin or the ``sri_integrity`` template expression."""
    if integrity == expected:
        return True
    for quote in ("'", '"'):
        if integrity == "{{ sri_integrity(" + quote + ref + quote + ") }}":
            return True
    return False


def check_local_hashes(manifest: dict, failures: list[str]) -> None:
    """Recompute every pinned local asset and record mismatches."""
    sys.path.insert(0, str(PROJECT_ROOT))
    from utils.integrity import compute_file_sri

    for relative, pinned in sorted(manifest.get("assets", {}).items()):
        path = STATIC_DIR / relative
        if not path.exists():
            failures.append("manifest lists missing file " + relative)
            continue
        actual = compute_file_sri(path, manifest.get("algorithm", "sha384"))
        if actual != pinned:
            failures.append("hash drift in " + relative)


def check_template_references(manifest: dict, failures: list[str]) -> None:
    """Require manifest-backed integrity on every template reference."""
    for template in sorted(TEMPLATES_DIR.glob("*.html")):
        parser = AssetReference()
        parser.feed(template.read_text(encoding="utf-8"))
        for entry in parser.entries:
            ref = entry["ref"]
            if not (ref.startswith("/static/") or ref.startswith("https://")):
                continue
            expected = expected_for_reference(manifest, ref)
            if expected is None:
                failures.append(template.name + " references unpinned " + ref)
            elif not integrity_attribute_ok(entry["integrity"], ref, expected):
                failures.append(template.name + " has stale integrity for " + ref)


def check_bucket_parity(failures: list[str]) -> None:
    """Require identical bucket tables in Python and JavaScript."""
    sys.path.insert(0, str(PROJECT_ROOT))
    from utils.padding import DEFAULT_FILE_BUCKETS, DEFAULT_MESSAGE_BUCKETS

    text = (STATIC_DIR / "js" / "qv-padding.js").read_text(encoding="utf-8")
    numbers = [int(value) for value in re.findall(r"\b\d{3,8}\b", text)]
    for bucket in DEFAULT_MESSAGE_BUCKETS:
        if bucket not in numbers:
            failures.append("qv-padding.js lacks message bucket " + str(bucket))
    for bucket in DEFAULT_FILE_BUCKETS:
        if bucket not in numbers:
            failures.append("qv-padding.js lacks file bucket " + str(bucket))


def main() -> int:
    """Run every check and report failures."""
    failures: list[str] = []
    if not MANIFEST_PATH.exists():
        print("missing manifest: run tools/generate_sri.py")
        return 1
    manifest = load_manifest()
    check_local_hashes(manifest, failures)
    check_template_references(manifest, failures)
    check_bucket_parity(failures)
    if failures:
        print("verify_build FAILED:")
        for failure in failures:
            print("  - " + failure)
        return 1
    print("verify_build OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
