# tools

*Community 6 | 4 files | cohesion 0.67*

## Definition

This community groups 4 file(s) rooted at `tools` with dominant language py (cohesion 0.67). Central symbols: `AssetReference`, `__init__`, `_cached_manifest_text`, `_normalize_reference`, `build_manifest`, `check_bucket_parity`, `check_local_hashes`, `check_template_references`. Core file: `tools/verify_build.py` (11 symbols). Documented purpose: Contract tests for SRI pins and reproducible builds (QV-SRI-1)..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `tests/test_integrity.py` | py | testing | 6 | yes |
| `tools/generate_sri.py` | py | utility | 5 | yes |
| `tools/verify_build.py` | py | utility | 11 | yes |
| `utils/integrity.py` | py | utility | 8 | yes |

## Key Symbols

- `test_compute_sri_format` (function, `tests/test_integrity.py:19`) `def test_compute_sri_format()`
- `test_manifest_exists_and_pins_crypto` (function, `tests/test_integrity.py:25`) `def test_manifest_exists_and_pins_crypto()`
- `test_manifest_hashes_match_files` (function, `tests/test_integrity.py:37`) `def test_manifest_hashes_match_files()`
- `test_template_integrity_resolves_both_forms` (function, `tests/test_integrity.py:44`) `def test_template_integrity_resolves_both_forms()`
- `test_jinja_global_registered` (function, `tests/test_integrity.py:51`) `def test_jinja_global_registered(app)`
- `test_verify_build_passes_on_clean_tree` (function, `tests/test_integrity.py:55`) `def test_verify_build_passes_on_clean_tree()`
- `collect_local_assets` (function, `tools/generate_sri.py:41`) `def collect_local_assets()` - Hash every first-party script and stylesheet under ``static/``.
- `fetch_cdn_assets` (function, `tools/generate_sri.py:56`) `def fetch_cdn_assets()` - Download every pinned CDN URL and hash its exact bytes.
- `build_manifest` (function, `tools/generate_sri.py:66`) `def build_manifest(cdn, local)` - Assemble the deterministic manifest document.
- `render_manifest` (function, `tools/generate_sri.py:76`) `def render_manifest(manifest)` - Render the manifest deterministically with a trailing newline.
- `main` (function, `tools/generate_sri.py:81`) `def main(argv)` - Generate the manifest, or verify it is current with ``--check``.
- `AssetReference` (class, `tools/verify_build.py:34`) `class AssetReference(HTMLParser)` - Collect external script and stylesheet references from one template.
- `__init__` (method, `tools/verify_build.py:37`) `def __init__(self)` - Initialize the reference collector.
- `handle_starttag` (method, `tools/verify_build.py:42`) `def handle_starttag(self, tag, attrs)` - Record one script or link tag with its integrity attribute.
- `_normalize_reference` (method, `tools/verify_build.py:60`) `def _normalize_reference(ref)` - Resolve a ``url_for('static', ...)`` expression to its served path.
- `load_manifest` (method, `tools/verify_build.py:71`) `def load_manifest()` - Load and return the SRI manifest document.
- `expected_for_reference` (method, `tools/verify_build.py:76`) `def expected_for_reference(manifest, ref)` - Resolve the pinned integrity value for one template reference.
- `integrity_attribute_ok` (method, `tools/verify_build.py:85`) `def integrity_attribute_ok(integrity, ref, expected)` - Accept a literal pin or the ``sri_integrity`` template expression.
- `check_local_hashes` (method, `tools/verify_build.py:95`) `def check_local_hashes(manifest, failures)` - Recompute every pinned local asset and record mismatches.
- `check_template_references` (method, `tools/verify_build.py:110`) `def check_template_references(manifest, failures)` - Require manifest-backed integrity on every template reference.
- `check_bucket_parity` (method, `tools/verify_build.py:126`) `def check_bucket_parity(failures)` - Require identical bucket tables in Python and JavaScript.
- `main` (method, `tools/verify_build.py:141`) `def main()` - Run every check and report failures.
- `manifest_path` (function, `utils/integrity.py:25`) `def manifest_path()` - Return the manifest path resolved from this file, never hardcoded.
- `compute_sri` (function, `utils/integrity.py:30`) `def compute_sri(data, algorithm)` - Return the SRI string ``<algorithm>-<base64 digest>`` for ``data``.
- `compute_file_sri` (function, `utils/integrity.py:36`) `def compute_file_sri(path, algorithm)` - Return the SRI string for the bytes stored at ``path``.
- `_cached_manifest_text` (function, `utils/integrity.py:42`) `def _cached_manifest_text()` - Return the raw manifest text, cached for the process lifetime.
- `load_manifest` (function, `utils/integrity.py:47`) `def load_manifest()` - Return the parsed SRI manifest, or an empty mapping when absent.
- `integrity_for` (function, `utils/integrity.py:55`) `def integrity_for(key)` - Return the pinned integrity string for one manifest key.
- `clear_manifest_cache` (function, `utils/integrity.py:72`) `def clear_manifest_cache()` - Drop the cached manifest text so tests see a regenerated file.
- `template_integrity` (function, `utils/integrity.py:77`) `def template_integrity(key)` - Return the integrity string for a template asset reference.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 4
- Cross-boundary resolved imports (EXTRACTED): 2

## Connections

- [EXTRACTED] depends_on community 1 <-> 6 (strength 0.9): Extracted import edge crosses communities: app_factory.py imports utils/integrity.py.
- [EXTRACTED] depends_on community 6 <-> 5 (strength 0.9): Extracted import edge crosses communities: tools/verify_build.py imports utils/padding.py.
- [INFERRED] shares_context community 0 <-> 6 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (views: auth) and community 6 (tools).
- [INFERRED] shares_context community 2 <-> 6 (strength 0.5): Inferred shared context (layer utility) with no import path between community 2 (static/js) and community 6 (tools).
- [INFERRED] shares_context community 3 <-> 6 (strength 0.5): Inferred shared context (language py) with no import path between community 3 (controllers) and community 6 (tools).

## Risks

- [taint medium] `tools/generate_sri.py` -> `tools/generate_sri.py` via `urllib.request` (0 hops)
- [taint medium] `tools/generate_sri.py` -> `utils/integrity.py` via `urllib.request` (1 hops)

## Open Questions

- Is the dangerous import `urllib.request` in `tools/generate_sri.py` still required, or can it be isolated?
- What would break if the most connected file in tools changed?
- Should tools be split, given cohesion 0.67?

## Sources

- `tests/test_integrity.py`
- `tools/generate_sri.py`
- `tools/verify_build.py`
- `utils/integrity.py`
