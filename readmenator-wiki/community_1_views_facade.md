# views: facade

*Community 1 | 11 files | cohesion 0.41*

## Definition

This community groups 11 file(s) rooted at `views` with dominant language py (cohesion 0.41). Central symbols: `FacadeConfig`, `FacadeGate`, `GateDecision`, `GateOutcome`, `GatePhraseHasher`, `GateTicket`, `SyncController`, `TestCatalog`. Core file: `tests/test_cover.py` (52 symbols). Documented purpose: Application factory for QuantumVault.  The same ``create_app()`` callable powers:  - ``app.py`` (dev: ``flask run`` or Werkzeug's dev server with debug) - ``wsg.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app_factory.py` | py | presentation | 8 | yes |
| `controllers/facade.py` | py | presentation | 26 | yes |
| `controllers/sync.py` | py | presentation | 3 | yes |
| `tests/test_account_facade.py` | py | testing | 6 | yes |
| `tests/test_cover.py` | py | testing | 52 | yes |
| `tests/test_facade.py` | py | testing | 52 | yes |
| `views/about.py` | py | presentation | 1 | no |
| `views/facade.py` | py | presentation | 6 | yes |
| `views/privacy.py` | py | presentation | 1 | no |
| `views/terms.py` | py | presentation | 1 | no |
| `wsgi.py` | py | utility | 0 | yes |

## Key Symbols

- `_is_production` (function, `app_factory.py:71`) `def _is_production()` - Return True unless the operator explicitly opts into dev mode.
- `_build_csp` (function, `app_factory.py:82`) `def _build_csp()` - Return the strict Content-Security-Policy used in production.
- `_build_talisman_kwargs` (function, `app_factory.py:119`) `def _build_talisman_kwargs()` - Return kwargs to pass to ``Talisman`` based on the runtime env.
- `_configure_secret_key` (function, `app_factory.py:160`) `def _configure_secret_key(app, config)` - Set ``app.config['SECRET_KEY']`` from env, payload.json, or a random value.
- `_configure_session` (function, `app_factory.py:203`) `def _configure_session(app)` - Apply session lifetime and cookie hardening.
- `_configure_logging` (function, `app_factory.py:220`) `def _configure_logging(app)` - Wire up a structured application logger.
- `create_app` (function, `app_factory.py:237`) `def create_app(config_overrides, security_overrides)` - Build and return a fully-configured Flask application.
- `load_user` (function, `app_factory.py:416`) `def load_user(user_id)`
- `GateOutcome` (class, `controllers/facade.py:63`) `class GateOutcome(Enum)` - Classification of a submitted gate phrase.
- `GateDecision` (class, `controllers/facade.py:72`) `class GateDecision` - The outcome of evaluating a phrase plus any issued ticket.
- `_as_bool` (method, `controllers/facade.py:79`) `def _as_bool(value, default)` - Coerce an environment or mapping value to a boolean.
- `_as_int` (method, `controllers/facade.py:88`) `def _as_int(value, default)` - Coerce an environment or mapping value to an integer.
- `_as_text` (method, `controllers/facade.py:98`) `def _as_text(value, default)` - Coerce a value to non-empty text, falling back to ``default``.
- `_as_raw_text` (method, `controllers/facade.py:106`) `def _as_raw_text(value, default)` - Coerce a value to text without substituting an empty default.
- `_as_paths` (method, `controllers/facade.py:111`) `def _as_paths(value, default)` - Parse a comma-separated path list into a tuple of stripped paths.
- `FacadeConfig` (class, `controllers/facade.py:124`) `class FacadeConfig` - Immutable facade configuration resolved from environment and app config.
- `gate_configured` (method, `controllers/facade.py:154`) `def gate_configured(self)` - Return whether the facade is enabled and holds a real gate hash.
- `cover_context` (method, `controllers/facade.py:158`) `def cover_context(self)` - Return the cosmetic cover context, never carrying a gate hash.
- `cover_variables` (method, `controllers/facade.py:166`) `def cover_variables(self)` - Return the sanitizable cover variable payload.
- `from_mapping` (method, `controllers/facade.py:181`) `def from_mapping(cls, mapping, env)` - Resolve configuration with environment, mapping, then default order.
- `read` (method, `controllers/facade.py:189`) `def read(key)`
- `GatePhraseHasher` (class, `controllers/facade.py:262`) `class GatePhraseHasher` - Argon2id hashing and verification for a human-chosen gate phrase.
- `__init__` (method, `controllers/facade.py:265`) `def __init__(self, time_cost, memory_cost, parallelism, hash_len, salt_len)` - Bind the hasher to explicit Argon2id cost parameters.
- `hash` (method, `controllers/facade.py:282`) `def hash(self, phrase)` - Return a salted Argon2id digest of ``phrase``.
- `verify` (method, `controllers/facade.py:286`) `def verify(self, phrase, encoded)` - Return whether ``phrase`` matches ``encoded`` without raising.
- `from_config` (method, `controllers/facade.py:296`) `def from_config(cls, config)` - Build a hasher using the cost parameters of ``config``.
- `GateTicket` (class, `controllers/facade.py:305`) `class GateTicket` - Short-lived signed ticket binding a session to a gate mode.
- `__init__` (method, `controllers/facade.py:308`) `def __init__(self, secret_key, ttl_seconds)` - Bind the ticket signer to the app secret and a lifetime.
- `issue` (method, `controllers/facade.py:316`) `def issue(self, mode)` - Return a signed ticket for ``mode`` or raise for an unknown mode.
- `verify` (method, `controllers/facade.py:322`) `def verify(self, token)` - Return the ticket mode, or ``None`` if expired, tampered, or absent.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 13
- Cross-boundary resolved imports (EXTRACTED): 19

## Connections

- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: app.py imports app_factory.py.
- [EXTRACTED] depends_on community 1 <-> 5 (strength 0.9): Extracted import edge crosses communities: app_factory.py imports controllers/file.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: app_factory.py imports models/user.py.
- [EXTRACTED] depends_on community 1 <-> 6 (strength 0.9): Extracted import edge crosses communities: app_factory.py imports utils/integrity.py.
- [EXTRACTED] depends_on community 1 <-> 4 (strength 0.9): Extracted import edge crosses communities: app_factory.py imports views/account.py.
- [INFERRED] shares_context community 1 <-> 7 (strength 0.5): Inferred shared context (language py) with no import path between community 1 (views: facade) and community 7 (orphans).

## Risks

- [layer strict] `tests/conftest.py` (testing) -> `app_factory.py` (presentation)
- [layer strict] `tests/test_account_facade.py` (testing) -> `app_factory.py` (presentation)
- [layer strict] `tests/test_account_facade.py` (testing) -> `controllers/facade.py` (presentation)
- [layer strict] `tests/test_account_facade.py` (testing) -> `models/user.py` (presentation)
- [layer strict] `tests/test_cover.py` (testing) -> `app_factory.py` (presentation)
- [layer strict] `tests/test_cover.py` (testing) -> `controllers/facade.py` (presentation)
- [layer strict] `tests/test_facade.py` (testing) -> `app_factory.py` (presentation)
- [layer strict] `tests/test_facade.py` (testing) -> `controllers/facade.py` (presentation)
- [layer strict] `tests/test_facade.py` (testing) -> `models/user.py` (presentation)

## Open Questions

- Why do 3 file(s) lack file-level docs (e.g. `views/about.py`)? What purpose do they serve?
- What would break if the most connected file in views: facade changed?
- Should views: facade be split, given cohesion 0.41?

## Sources

- `app_factory.py`
- `controllers/facade.py`
- `controllers/sync.py`
- `tests/test_account_facade.py`
- `tests/test_cover.py`
- `tests/test_facade.py`
- `views/about.py`
- `views/facade.py`
- `views/privacy.py`
- `views/terms.py`
- `wsgi.py`
