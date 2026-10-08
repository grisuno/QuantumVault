# views: deniable_vault

*Community 4 | 8 files | cohesion 0.50*

## Definition

This community groups 8 file(s) rooted at `tests` with dominant language py (cohesion 0.50). Central symbols: `DeniableVaultConfig`, `DeniableVaultController`, `DeniableVaultDB`, `EnvelopeValidationError`, `EnvelopeValidator`, `TestDeniableVaultApi`, `TestDeniableVaultConfig`, `TestDeniableVaultController`. Core file: `tests/test_deniable_vault.py` (55 symbols). Documented purpose: QV-DENIABLE-1 deniable vault: configuration, validation, orchestration.  This module is the server-side core of the deniable vault feature. It is strictly zero-.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `controllers/deniable_vault.py` | py | presentation | 22 | yes |
| `models/deniable_vault.py` | py | business_logic | 6 | yes |
| `tests/conftest.py` | py | testing | 8 | yes |
| `tests/test_deniable_vault.py` | py | testing | 55 | yes |
| `tests/test_security.py` | py | testing | 8 | yes |
| `utils/security.py` | py | presentation | 10 | yes |
| `views/account.py` | py | presentation | 5 | yes |
| `views/sync.py` | py | presentation | 2 | yes |

## Key Symbols

- `_base64_length` (function, `controllers/deniable_vault.py:81`) `def _base64_length(byte_length)` - Return the length of the standard base64 encoding of ``byte_length`` bytes.
- `canonical_json` (function, `controllers/deniable_vault.py:86`) `def canonical_json(envelope)` - Serialize an envelope deterministically for storage and sizing.
- `EnvelopeValidationError` (class, `controllers/deniable_vault.py:104`) `class EnvelopeValidationError(ValueError)` - Raised when an envelope violates a structural invariant.
- `_coerce_int` (method, `controllers/deniable_vault.py:108`) `def _coerce_int(value, default)` - Return ``value`` coerced to int, falling back to ``default``.
- `_coerce_kdf` (method, `controllers/deniable_vault.py:118`) `def _coerce_kdf(value, default)` - Return an allow-list of KDF identifiers from a value.
- `DeniableVaultConfig` (class, `controllers/deniable_vault.py:134`) `class DeniableVaultConfig` - Immutable structural limits for a deniable vault container.
- `from_mapping` (method, `controllers/deniable_vault.py:148`) `def from_mapping(cls, mapping, env)` - Build a config from a mapping, with environment overrides.
- `read` (method, `controllers/deniable_vault.py:171`) `def read(key)`
- `expected_ct_b64_length` (method, `controllers/deniable_vault.py:213`) `def expected_ct_b64_length(self)` - Return the exact base64 length every slot ciphertext must have.
- `random_container` (method, `controllers/deniable_vault.py:222`) `def random_container(self)` - Return a well-formed container filled with random, unopenable data.
- `public_parameters` (method, `controllers/deniable_vault.py:250`) `def public_parameters(self)` - Return the parameters the browser needs to build a container.
- `EnvelopeValidator` (class, `controllers/deniable_vault.py:272`) `class EnvelopeValidator` - Validate the structure of an opaque deniable vault envelope.
- `__init__` (method, `controllers/deniable_vault.py:281`) `def __init__(self, config)` - Bind the validator to a configuration.
- `validate` (method, `controllers/deniable_vault.py:285`) `def validate(self, envelope)` - Validate ``envelope``, raising on the first violation.
- `_validate_slot` (method, `controllers/deniable_vault.py:339`) `def _validate_slot(self, index, slot)` - Validate a single slot.
- `_validate_hex` (method, `controllers/deniable_vault.py:376`) `def _validate_hex(value, expected_length, index, field)` - Validate that ``value`` is hex of exactly ``expected_length``.
- `DeniableVaultController` (class, `controllers/deniable_vault.py:393`) `class DeniableVaultController` - Coordinate validation, provisioning, persistence, and auditing.
- `__init__` (method, `controllers/deniable_vault.py:401`) `def __init__(self, db, config, validator)` - Initialize the controller.
- `load_or_provision` (method, `controllers/deniable_vault.py:419`) `def load_or_provision(self, username)` - Return ``username``'s container, minting a random one if absent.
- `save` (method, `controllers/deniable_vault.py:441`) `def save(self, username, envelope)` - Validate and persist a container for ``username``.
- `reset` (method, `controllers/deniable_vault.py:456`) `def reset(self, username)` - Overwrite ``username``'s container with a fresh random one.
- `exists` (method, `controllers/deniable_vault.py:474`) `def exists(self, username)` - Return True if ``username`` already has a stored container.
- `DeniableVaultDB` (class, `models/deniable_vault.py:30`) `class DeniableVaultDB` - Persistence for per-user opaque deniable vault containers.
- `__init__` (method, `models/deniable_vault.py:33`) `def __init__(self, db_path)` - Initialize the store and ensure its table exists.
- `_init_db` (method, `models/deniable_vault.py:43`) `def _init_db(self)` - Create the ``deniable_vaults`` table on first use.
- `upsert` (method, `models/deniable_vault.py:57`) `def upsert(self, username, envelope)` - Insert or replace the container for ``username``.
- `get` (method, `models/deniable_vault.py:82`) `def get(self, username)` - Return the stored container for ``username``, or ``None``.
- `exists` (method, `models/deniable_vault.py:101`) `def exists(self, username)` - Return True if ``username`` has a stored container.
- `_hermetic_env` (function, `tests/conftest.py:26`) `def _hermetic_env(monkeypatch)` - Keep the suite hermetic against the operator's local ``.env`` file.
- `_push_request_context` (function, `tests/conftest.py:58`) `def _push_request_context()` - Neutralize pytest-flask's autouse request-context push.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 10
- Cross-boundary resolved imports (EXTRACTED): 10

## Connections

- [EXTRACTED] depends_on community 1 <-> 4 (strength 0.9): Extracted import edge crosses communities: app_factory.py imports views/account.py.
- [EXTRACTED] depends_on community 0 <-> 4 (strength 0.9): Extracted import edge crosses communities: controllers/auth.py imports utils/security.py.
- [INFERRED] shares_context community 3 <-> 4 (strength 0.5): Inferred shared context (language py and layer presentation) with no import path between community 3 (controllers) and community 4 (views: deniable_vault).
- [INFERRED] shares_context community 4 <-> 5 (strength 0.5): Inferred shared context (language py and layer presentation) with no import path between community 4 (views: deniable_vault) and community 5 (utils).

## Risks

- [taint high] `tests/test_secure_channel.py` -> `utils/security.py` via `subprocess` (3 hops)
- [layer strict] `tests/conftest.py` (testing) -> `app_factory.py` (presentation)
- [layer strict] `tests/conftest.py` (testing) -> `utils/security.py` (presentation)
- [layer strict] `tests/test_deniable_vault.py` (testing) -> `controllers/deniable_vault.py` (presentation)
- [layer strict] `tests/test_deniable_vault.py` (testing) -> `models/user.py` (presentation)
- [layer strict] `tests/test_security.py` (testing) -> `utils/security.py` (presentation)

## Open Questions

- What would break if the most connected file in views: deniable_vault changed?
- Should views: deniable_vault be split, given cohesion 0.50?

## Sources

- `controllers/deniable_vault.py`
- `models/deniable_vault.py`
- `tests/conftest.py`
- `tests/test_deniable_vault.py`
- `tests/test_security.py`
- `utils/security.py`
- `views/account.py`
- `views/sync.py`
