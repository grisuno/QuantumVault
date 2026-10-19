# utils

*Community 2 | 10 files | cohesion 0.57*

## Definition

This community groups 10 file(s) rooted at `tests` with dominant language py (cohesion 0.57). Central symbols: `AssetReference`, `FileController`, `MessageController`, `PaddingConfig`, `PaddingError`, `_FakeS3`, `_FakeUpload`, `__init__`. Core file: `tests/test_padding.py` (24 symbols). Documented purpose: Encrypted file persistence layer.  The server is intentionally blind to plaintext: it only ever stores opaque ciphertext plus an opaque "wrapped file encryption.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `controllers/file.py` | py | presentation | 9 | yes |
| `controllers/message.py` | py | presentation | 4 | yes |
| `tests/test_integrity.py` | py | testing | 6 | yes |
| `tests/test_padding.py` | py | testing | 24 | yes |
| `tests/test_srp.py` | py | testing | 6 | yes |
| `tools/generate_sri.py` | py | utility | 5 | yes |
| `tools/verify_build.py` | py | utility | 11 | yes |
| `utils/__init__.py` | py | utility | 0 | no |
| `utils/integrity.py` | py | utility | 8 | yes |
| `utils/padding.py` | py | utility | 13 | yes |

## Key Symbols

- `_log_s3_error` (function, `controllers/file.py:28`) `def _log_s3_error(operation, error)` - Log a failed S3 operation without raising further.
- `safe_filename` (function, `controllers/file.py:33`) `def safe_filename(name)` - Return a filename safe to embed in an S3 key.
- `FileController` (class, `controllers/file.py:51`) `class FileController` - Persistence for end-to-end encrypted files and their wrapped FEKs.
- `__init__` (method, `controllers/file.py:54`) `def __init__(self, users_path, s3_bucket, s3_client)`
- `_key` (method, `controllers/file.py:59`) `def _key(self, username, filename, suffix)` - Build the S3 key for a user's encrypted file or FEK.
- `get_storage_usage` (method, `controllers/file.py:71`) `def get_storage_usage(self, username)` - Sum the bytes used by ``username``'s encrypted files in S3.
- `upload_encrypted_file` (method, `controllers/file.py:85`) `def upload_encrypted_file(self, username, file_storage, wrapped_fek)` - Persist an already-encrypted file and its wrapped FEK to S3.
- `get_encrypted_file_and_key` (method, `controllers/file.py:118`) `def get_encrypted_file_and_key(self, username, filename)` - Fetch a user's encrypted file and its wrapped FEK from S3.
- `list_encrypted_files` (method, `controllers/file.py:148`) `def list_encrypted_files(self, username)` - List the encrypted files that belong to ``username``.
- `MessageController` (class, `controllers/message.py:19`) `class MessageController` - Handles message persistence in the zero-knowledge flow.
- `__init__` (method, `controllers/message.py:22`) `def __init__(self, users_path, users_db_path)` - Initialize the controller.
- `send_encrypted_message` (method, `controllers/message.py:36`) `def send_encrypted_message(self, sender, recipient, encrypted_message_b64, cek_f` - Persist an opaque message envelope for the recipient.
- `get_messages` (method, `controllers/message.py:90`) `def get_messages(self, username, page, per_page)` - Return opaque message envelopes for the user.
- `test_compute_sri_format` (function, `tests/test_integrity.py:19`) `def test_compute_sri_format()`
- `test_manifest_exists_and_pins_crypto` (function, `tests/test_integrity.py:25`) `def test_manifest_exists_and_pins_crypto()`
- `test_manifest_hashes_match_files` (function, `tests/test_integrity.py:37`) `def test_manifest_hashes_match_files()`
- `test_template_integrity_resolves_both_forms` (function, `tests/test_integrity.py:44`) `def test_template_integrity_resolves_both_forms()`
- `test_jinja_global_registered` (function, `tests/test_integrity.py:51`) `def test_jinja_global_registered(app)`
- `test_verify_build_passes_on_clean_tree` (function, `tests/test_integrity.py:55`) `def test_verify_build_passes_on_clean_tree()`
- `test_pad_roundtrip_message_sizes` (function, `tests/test_padding.py:26`) `def test_pad_roundtrip_message_sizes()`
- `test_pad_roundtrip_file_kind` (function, `tests/test_padding.py:33`) `def test_pad_roundtrip_file_kind()`
- `test_bucket_boundaries` (function, `tests/test_padding.py:38`) `def test_bucket_boundaries()`
- `test_pad_output_length_is_bucketed` (function, `tests/test_padding.py:44`) `def test_pad_output_length_is_bucketed()`
- `test_pad_uses_fresh_randomness` (function, `tests/test_padding.py:49`) `def test_pad_uses_fresh_randomness()`
- `test_pad_rejects_oversize` (function, `tests/test_padding.py:56`) `def test_pad_rejects_oversize()`
- `test_unpad_rejects_non_bucket_length` (function, `tests/test_padding.py:61`) `def test_unpad_rejects_non_bucket_length()`
- `test_unpad_rejects_corrupt_prefix` (function, `tests/test_padding.py:66`) `def test_unpad_rejects_corrupt_prefix()`
- `test_unpad_rejects_wrong_kind` (function, `tests/test_padding.py:74`) `def test_unpad_rejects_wrong_kind()`
- `test_wire_lengths` (function, `tests/test_padding.py:80`) `def test_wire_lengths()`
- `test_config_from_env_override` (function, `tests/test_padding.py:87`) `def test_config_from_env_override(monkeypatch)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 12
- Cross-boundary resolved imports (EXTRACTED): 9

## Connections

- [EXTRACTED] depends_on community 0 <-> 2 (strength 0.9): Extracted import edge crosses communities: controllers/auth.py imports utils/__init__.py.
- [EXTRACTED] depends_on community 1 <-> 2 (strength 0.9): Extracted import edge crosses communities: quantumvault/app_factory.py imports controllers/file.py.
- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: quantumvault/static/js/qv-padding.js imports utils/padding.py.
- [INFERRED] shares_context community 2 <-> 4 (strength 0.5): Inferred shared context (language py) with no import path between community 2 (utils) and community 4 (controllers).
- [INFERRED] shares_context community 2 <-> 5 (strength 0.5): Inferred shared context (language py) with no import path between community 2 (utils) and community 5 (views: deniable_vault).
- [INFERRED] shares_context community 2 <-> 6 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (utils) and community 6 (quantumvault).
- [INFERRED] shares_context community 2 <-> 7 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 2 (utils) and community 7 (orphans).

## Risks

- [taint high] `tests/test_secure_channel.py` -> `utils/__init__.py` via `subprocess` (4 hops)
- [taint medium] `tools/generate_sri.py` -> `tools/generate_sri.py` via `urllib.request` (0 hops)
- [taint medium] `tools/generate_sri.py` -> `utils/integrity.py` via `urllib.request` (1 hops)
- [layer strict] `tests/test_padding.py` (testing) -> `controllers/file.py` (presentation)
- [layer strict] `tests/test_padding.py` (testing) -> `controllers/message.py` (presentation)

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `utils/__init__.py`)? What purpose do they serve?
- Is the dangerous import `urllib.request` in `tools/generate_sri.py` still required, or can it be isolated?
- What would break if the most connected file in utils changed?
- Should utils be split, given cohesion 0.57?

## Sources

- `controllers/file.py`
- `controllers/message.py`
- `tests/test_integrity.py`
- `tests/test_padding.py`
- `tests/test_srp.py`
- `tools/generate_sri.py`
- `tools/verify_build.py`
- `utils/__init__.py`
- `utils/integrity.py`
- `utils/padding.py`
