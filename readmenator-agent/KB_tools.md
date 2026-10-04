# Subsystem: tools

## tools/generate_sri.py
- Layer: utility
- Doc: Generate the SRI manifest for first-party assets and pinned CDN URLs.  Regenerating the manifest is the audited step tha
- Language: py
- Symbols:
  - `collect_local_assets` (function, line 41) `def collect_local_assets()`
  - `fetch_cdn_assets` (function, line 56) `def fetch_cdn_assets()`
  - `build_manifest` (function, line 66) `def build_manifest(cdn, local)`
  - `render_manifest` (function, line 76) `def render_manifest(manifest)`
  - `main` (function, line 81) `def main(argv)`
- Depends on: `utils/integrity.py`

## tools/mutation_test.py
- Layer: testing
- Doc: Mutation testing harness for the QuantumVault facade and cover contracts.  Each discovered token mutation is applied in 
- Language: py
- Symbols:
  - `Mutation` (class, line 56) `class Mutation`
  - `_is_equivalent_bool` (method, line 67) `def _is_equivalent_bool(tokens, index)`
  - `discover_mutations` (method, line 79) `def discover_mutations(path, source)`
  - `apply_mutation` (method, line 109) `def apply_mutation(source, mutation)`
  - `collect` (method, line 121) `def collect(targets, limit)`
  - `purge_bytecode` (method, line 133) `def purge_bytecode()`
  - `run_suite` (method, line 142) `def run_suite(python, tests)`
  - `main` (method, line 157) `def main(argv)`

## tools/verify_build.py
- Layer: presentation
- Doc: Verify reproducible builds and the fixed code contracts (QV-SRI-1).  Checks performed, all offline:  1. Every first-part
- Language: py
- Symbols:
  - `AssetReference` (class, line 34) `class AssetReference(HTMLParser)`
  - `_normalize_reference` (method, line 60) `def _normalize_reference(ref)`
  - `load_manifest` (method, line 71) `def load_manifest()`
  - `expected_for_reference` (method, line 76) `def expected_for_reference(manifest, ref)`
  - `integrity_attribute_ok` (method, line 85) `def integrity_attribute_ok(integrity, ref, expected)`
  - `check_local_hashes` (method, line 95) `def check_local_hashes(manifest, failures)`
  - `check_template_references` (method, line 110) `def check_template_references(manifest, failures)`
  - `check_bucket_parity` (method, line 126) `def check_bucket_parity(failures)`
  - `main` (method, line 141) `def main()`
  - `__init__` (method, line 37) `def __init__(self)`
  - `handle_starttag` (method, line 42) `def handle_starttag(self, tag, attrs)`
- Depends on: `utils/integrity.py`, `utils/padding.py`
- Imported by: `tests/test_integrity.py`
