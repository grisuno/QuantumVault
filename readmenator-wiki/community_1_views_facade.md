# views: facade

*Community 1 | 11 files | cohesion 0.41*

## Definition

This community groups 11 file(s) rooted at `views` with dominant language py (cohesion 0.41). Central symbols: `FacadeConfig`, `FacadeGate`, `GateDecision`, `GateOutcome`, `GatePhraseHasher`, `GateTicket`, `SyncController`, `TestCatalog`. Core file: `tests/test_cover.py` (52 symbols). Documented purpose: QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.  The facade hides QuantumVault behind an innocuous cover application. A secret phr.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `controllers/facade.py` | py | presentation | 26 | yes |
| `controllers/sync.py` | py | presentation | 3 | yes |
| `quantumvault/app_factory.py` | py | presentation | 8 | yes |
| `quantumvault/wsgi.py` | py | utility | 1 | yes |
| `tests/test_account_facade.py` | py | testing | 6 | yes |
| `tests/test_cover.py` | py | testing | 52 | yes |
| `tests/test_facade.py` | py | testing | 52 | yes |
| `views/about.py` | py | presentation | 1 | no |
| `views/facade.py` | py | presentation | 6 | yes |
| `views/privacy.py` | py | presentation | 1 | no |
| `views/terms.py` | py | presentation | 1 | no |

## Key Symbols

- `GateOutcome` (class, `controllers/facade.py:63`) `class GateOutcome(Enum)` - Classification of a submitted gate phrase.
- `GateDecision` (class, `controllers/facade.py:72`) `class GateDecision` - The outcome of evaluating a phrase plus any issued ticket.
- `_as_bool` (function, `controllers/facade.py:79`) `def _as_bool(value, default)` - Coerce an environment or mapping value to a boolean.
- `_as_int` (function, `controllers/facade.py:88`) `def _as_int(value, default)` - Coerce an environment or mapping value to an integer.
- `_as_text` (function, `controllers/facade.py:98`) `def _as_text(value, default)` - Coerce a value to non-empty text, falling back to ``default``.
- `_as_raw_text` (function, `controllers/facade.py:106`) `def _as_raw_text(value, default)` - Coerce a value to text without substituting an empty default.
- `_as_paths` (function, `controllers/facade.py:111`) `def _as_paths(value, default)` - Parse a comma-separated path list into a tuple of stripped paths.
- `FacadeConfig` (class, `controllers/facade.py:124`) `class FacadeConfig` - Immutable facade configuration resolved from environment and app config.
- `gate_configured` (method, `controllers/facade.py:154`) `def gate_configured(self)` - Return whether the facade is enabled and holds a real gate hash.
- `cover_context` (method, `controllers/facade.py:158`) `def cover_context(self)` - Return the cosmetic cover context, never carrying a gate hash.
- `cover_variables` (method, `controllers/facade.py:166`) `def cover_variables(self)` - Return the sanitizable cover variable payload.
- `from_mapping` (method, `controllers/facade.py:181`) `def from_mapping(cls, mapping, env)` - Resolve configuration with environment, mapping, then default order.
- `read` (function, `controllers/facade.py:189`) `def read(key)`
- `GatePhraseHasher` (class, `controllers/facade.py:262`) `class GatePhraseHasher` - Argon2id hashing and verification for a human-chosen gate phrase.
- `__init__` (method, `controllers/facade.py:265`) `def __init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)` - Bind the hasher to explicit Argon2id cost parameters.
- `hash` (method, `controllers/facade.py:282`) `def hash(self, phrase)` - Return a salted Argon2id digest of ``phrase``.
- `verify` (method, `controllers/facade.py:286`) `def verify(self, phrase, encoded)` - Return whether ``phrase`` matches ``encoded`` without raising.
- `from_config` (method, `controllers/facade.py:296`) `def from_config(cls, config)` - Build a hasher using the cost parameters of ``config``.
- `GateTicket` (class, `controllers/facade.py:305`) `class GateTicket` - Short-lived signed ticket binding a session to a gate mode.
- `__init__` (method, `controllers/facade.py:308`) `def __init__(self, secret_key, ttl_seconds)` - Bind the ticket signer to the app secret and a lifetime.
- `issue` (method, `controllers/facade.py:316`) `def issue(self, mode)` - Return a signed ticket for ``mode`` or raise for an unknown mode.
- `verify` (method, `controllers/facade.py:322`) `def verify(self, token)` - Return the ticket mode, or ``None`` if expired, tampered, or absent.
- `FacadeGate` (class, `controllers/facade.py:336`) `class FacadeGate` - Evaluate gate phrases and issue tickets with constant observable work.
- `__init__` (method, `controllers/facade.py:339`) `def __init__(self, config, hasher, ticket)` - Bind the gate to its configuration and collaborators.
- `build` (method, `controllers/facade.py:351`) `def build(cls, config, secret_key)` - Build a gate from configuration and the application secret.
- `evaluate` (method, `controllers/facade.py:359`) `def evaluate(self, phrase)` - Classify a phrase and emit only a generic audit event.
- `SyncController` (class, `controllers/sync.py:7`) `class SyncController`
- `__init__` (method, `controllers/sync.py:8`) `def __init__(self, users_path, s3_bucket, s3_client, file_controller)`
- `get_storage_usage` (method, `controllers/sync.py:14`) `def get_storage_usage(self, username)` - Calcula el uso de almacenamiento del usuario en S3.
- `_is_production` (function, `quantumvault/app_factory.py:71`) `def _is_production()` - Return True unless the operator explicitly opts into dev mode.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 13
- Cross-boundary resolved imports (EXTRACTED): 19

## Connections

- [EXTRACTED] depends_on community 4 <-> 1 (strength 0.9): Extracted import edge crosses communities: app.py imports quantumvault/app_factory.py.
- [EXTRACTED] depends_on community 1 <-> 5 (strength 0.9): Extracted import edge crosses communities: controllers/facade.py imports utils/security.py.
- [EXTRACTED] depends_on community 1 <-> 2 (strength 0.9): Extracted import edge crosses communities: quantumvault/app_factory.py imports controllers/file.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: quantumvault/app_factory.py imports models/user.py.
- [INFERRED] shares_context community 1 <-> 6 (strength 0.5): Inferred shared context (language py) with no import path between community 1 (views: facade) and community 6 (quantumvault).
- [INFERRED] shares_context community 1 <-> 7 (strength 0.5): Inferred shared context (language py) with no import path between community 1 (views: facade) and community 7 (orphans).

## Risks

- [layer strict] `tests/conftest.py` (testing) -> `quantumvault/app_factory.py` (presentation)
- [layer strict] `tests/test_account_facade.py` (testing) -> `quantumvault/app_factory.py` (presentation)
- [layer strict] `tests/test_account_facade.py` (testing) -> `controllers/facade.py` (presentation)
- [layer strict] `tests/test_account_facade.py` (testing) -> `models/user.py` (presentation)
- [layer strict] `tests/test_cover.py` (testing) -> `quantumvault/app_factory.py` (presentation)
- [layer strict] `tests/test_cover.py` (testing) -> `controllers/facade.py` (presentation)
- [layer strict] `tests/test_facade.py` (testing) -> `quantumvault/app_factory.py` (presentation)
- [layer strict] `tests/test_facade.py` (testing) -> `controllers/facade.py` (presentation)
- [layer strict] `tests/test_facade.py` (testing) -> `models/user.py` (presentation)

## Open Questions

- Why do 3 file(s) lack file-level docs (e.g. `views/about.py`)? What purpose do they serve?
- What would break if the most connected file in views: facade changed?
- Should views: facade be split, given cohesion 0.41?

## Sources

- `controllers/facade.py`
- `controllers/sync.py`
- `quantumvault/app_factory.py`
- `quantumvault/wsgi.py`
- `tests/test_account_facade.py`
- `tests/test_cover.py`
- `tests/test_facade.py`
- `views/about.py`
- `views/facade.py`
- `views/privacy.py`
- `views/terms.py`
