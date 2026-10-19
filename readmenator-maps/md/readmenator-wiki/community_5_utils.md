# utils

*Community 5 | 8 files | cohesion 0.47*

## Definition

This community groups 8 file(s) rooted at `utils` with dominant language py (cohesion 0.47). Central symbols: `FileController`, `MessageController`, `MessageDB`, `MessageModel`, `PaddingConfig`, `PaddingError`, `_FakeS3`, `_FakeUpload`. Core file: `tests/test_padding.py` (24 symbols). Documented purpose: Encrypted file persistence layer.  The server is intentionally blind to plaintext: it only ever stores opaque ciphertext plus an opaque "wrapped file encryption.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `controllers/file.py` | py | presentation | 9 | yes |
| `controllers/message.py` | py | presentation | 4 | yes |
| `models/message.py` | py | presentation | 6 | yes |
| `tests/test_padding.py` | py | testing | 24 | yes |
| `tests/test_srp.py` | py | testing | 6 | yes |
| `utils/__init__.py` | py | utility | 0 | no |
| `utils/padding.py` | py | utility | 13 | yes |
| `utils/scheduler.py` | py | presentation | 5 | yes |

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
- `MessageModel` (class, `models/message.py:27`) `class MessageModel(BaseModel)` - Pydantic model for a stored message envelope.
- `MessageDB` (class, `models/message.py:43`) `class MessageDB` - File-based operations for end-to-end encrypted messages.
- `__init__` (method, `models/message.py:46`) `def __init__(self, base_path)` - Initialize the MessageDB with the base directory for per-user mailboxes.
- `save_message` (method, `models/message.py:55`) `def save_message(self, recipient, sender, encrypted_message_b64, cek_for_recipie` - Persist an opaque message envelope for the recipient.
- `get_messages` (method, `models/message.py:87`) `def get_messages(self, recipient, page, per_page)` - Return opaque message envelopes for the recipient.
- `delete_old_messages` (method, `models/message.py:172`) `def delete_old_messages(self, recipient, days)` - Delete messages older than ``days`` days from the recipient's mailbox.
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

- Internal resolved imports (EXTRACTED): 9
- Cross-boundary resolved imports (EXTRACTED): 10

## Connections

- [EXTRACTED] depends_on community 1 <-> 5 (strength 0.9): Extracted import edge crosses communities: app_factory.py imports controllers/file.py.
- [EXTRACTED] depends_on community 0 <-> 5 (strength 0.9): Extracted import edge crosses communities: controllers/auth.py imports utils/__init__.py.
- [EXTRACTED] depends_on community 2 <-> 5 (strength 0.9): Extracted import edge crosses communities: static/js/qv-padding.js imports utils/padding.py.
- [EXTRACTED] depends_on community 6 <-> 5 (strength 0.9): Extracted import edge crosses communities: tools/verify_build.py imports utils/padding.py.
- [INFERRED] shares_context community 3 <-> 5 (strength 0.5): Inferred shared context (language py and layer presentation) with no import path between community 3 (controllers) and community 5 (utils).
- [INFERRED] shares_context community 4 <-> 5 (strength 0.5): Inferred shared context (language py and layer presentation) with no import path between community 4 (views: deniable_vault) and community 5 (utils).

## Risks

- [taint high] `tests/test_secure_channel.py` -> `utils/__init__.py` via `subprocess` (4 hops)
- [layer strict] `tests/test_padding.py` (testing) -> `controllers/file.py` (presentation)
- [layer strict] `tests/test_padding.py` (testing) -> `controllers/message.py` (presentation)

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `utils/__init__.py`)? What purpose do they serve?
- What would break if the most connected file in utils changed?
- Should utils be split, given cohesion 0.47?

## Sources

- `controllers/file.py`
- `controllers/message.py`
- `models/message.py`
- `tests/test_padding.py`
- `tests/test_srp.py`
- `utils/__init__.py`
- `utils/padding.py`
- `utils/scheduler.py`
