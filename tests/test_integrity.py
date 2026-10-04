"""Contract tests for SRI pins and reproducible builds (QV-SRI-1)."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path

from utils.integrity import (
    SRI_ALGORITHM,
    compute_sri,
    integrity_for,
    manifest_path,
    template_integrity,
)


def test_compute_sri_format() -> None:
    value = compute_sri(b"quantumvault")
    assert value.startswith(SRI_ALGORITHM + "-")
    assert base64.b64decode(value.split("-", 1)[1]) == hashlib.sha384(b"quantumvault").digest()


def test_manifest_exists_and_pins_crypto() -> None:
    path = manifest_path()
    assert path.exists()
    manifest = json.loads(path.read_text(encoding="utf-8"))
    assert manifest["algorithm"] == SRI_ALGORITHM
    assert "js/qv-padding.js" in manifest["assets"]
    assert (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
        in manifest["cdn"]
    )


def test_manifest_hashes_match_files() -> None:
    manifest = json.loads(manifest_path().read_text(encoding="utf-8"))
    root = Path(__file__).resolve().parent.parent / "static"
    for relative in ("js/qv-crypto.js", "js/qv-padding.js", "js/messages.js", "js/upload.js"):
        assert compute_sri((root / relative).read_bytes()) == manifest["assets"][relative]


def test_template_integrity_resolves_both_forms() -> None:
    assert template_integrity("/static/js/qv-crypto.js") == integrity_for("js/qv-crypto.js")
    url = "https://cdn.jsdelivr.net/npm/marked/marked.min.js"
    assert template_integrity(url) == integrity_for(url)
    assert template_integrity("/static/js/does-not-exist.js") == ""


def test_jinja_global_registered(app) -> None:
    assert app.jinja_env.globals["sri_integrity"] is template_integrity


def test_verify_build_passes_on_clean_tree() -> None:
    import tools.verify_build as verify

    failures: list[str] = []
    manifest = verify.load_manifest()
    verify.check_local_hashes(manifest, failures)
    verify.check_template_references(manifest, failures)
    verify.check_bucket_parity(failures)
    assert failures == []
