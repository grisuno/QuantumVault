# Subsystem: tools

## tools/generate_sri.py
- Doc: Generate the SRI manifest for first-party assets and pinned CDN URLs.
- Layer: utility
- Language: py
- Symbols:
  - `collect_local_assets` (function, line 41) `def collect_local_assets()`
  - `fetch_cdn_assets` (function, line 56) `def fetch_cdn_assets()`
  - `build_manifest` (function, line 66) `def build_manifest(cdn, local)`
  - `render_manifest` (function, line 76) `def render_manifest(manifest)`
  - `main` (function, line 81) `def main(argv)`
- Depends on: `utils/integrity.py`

## tools/mutation_test.py
- Doc: Mutation testing harness for the QuantumVault facade and cover contracts.
- Layer: testing
- Language: py
- Symbols:
  - `Mutation` (class, line 56) `class Mutation`
  - `_is_equivalent_bool` (function, line 67) `def _is_equivalent_bool(tokens, index)`
  - `discover_mutations` (function, line 79) `def discover_mutations(path, source)`
  - `apply_mutation` (function, line 109) `def apply_mutation(source, mutation)`
  - `collect` (function, line 121) `def collect(targets, limit)`
  - `purge_bytecode` (function, line 133) `def purge_bytecode()`
  - `run_suite` (function, line 142) `def run_suite(python, tests)`
  - `main` (function, line 157) `def main(argv)`

## tools/verify_build.py
- Doc: Verify reproducible builds and the fixed code contracts (QV-SRI-1).
- Layer: utility
- Language: py
- Symbols:
  - `AssetReference` (class, line 34) `class AssetReference(HTMLParser)`
  - `_normalize_reference` (function, line 60) `def _normalize_reference(ref)`
  - `load_manifest` (function, line 71) `def load_manifest()`
  - `expected_for_reference` (function, line 76) `def expected_for_reference(manifest, ref)`
  - `integrity_attribute_ok` (function, line 85) `def integrity_attribute_ok(integrity, ref, expected)`
  - `check_local_hashes` (function, line 95) `def check_local_hashes(manifest, failures)`
  - `check_template_references` (function, line 110) `def check_template_references(manifest, failures)`
  - `check_bucket_parity` (function, line 126) `def check_bucket_parity(failures)`
  - `main` (function, line 141) `def main()`
  - `__init__` (method, line 37) `def __init__(self)`
  - `handle_starttag` (method, line 42) `def handle_starttag(self, tag, attrs)`
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`
