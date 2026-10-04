# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `app_factory.py` (score: 48.80)
- `utils/utils.py` (score: 32.80)
- `models/user.py` (score: 30.70)
- `views/auth.py` (score: 24.90)
- `views/admin.py` (score: 21.90)
- `utils/security.py` (score: 19.00)
- `static/js/qv-crypto.js` (score: 18.00)
- `controllers/facade.py` (score: 14.60)
- `controllers/auth.py` (score: 13.40)
- `controllers/message.py` (score: 12.40)

## Hotspots (complexity + centrality)

- `static/js/qv-crypto.js` -- complexity: 0.6, centrality: 1.0, combined: 0.8
- `tests/test_secure_channel.py` -- complexity: 1.0, centrality: 0.1, combined: 0.5
- `tests/test_deniable_vault.py` -- complexity: 0.8, centrality: 0.1, combined: 0.4
- `tests/test_facade.py` -- complexity: 0.8, centrality: 0.0, combined: 0.3
- `tests/test_cover.py` -- complexity: 0.8, centrality: 0.0, combined: 0.3
- `controllers/secure_channel.py` -- complexity: 0.6, centrality: 0.1, combined: 0.3
- `views/auth.py` -- complexity: 0.4, centrality: 0.1, combined: 0.3
- `views/admin.py` -- complexity: 0.3, centrality: 0.2, combined: 0.2
- `models/user.py` -- complexity: 0.4, centrality: 0.1, combined: 0.2
- `static/js/account.js` -- complexity: 0.1, centrality: 0.3, combined: 0.2

## Dependency Cycles

Circular dependencies. Refactor to break the cycle.

- `static/js/qv-crypto.js` -> `static/js/register.js` -> `static/js/qv-crypto.js`
- `static/js/qv-crypto.js` -> `static/js/login.js` -> `static/js/qv-crypto.js`

## Layer Violations

- `scripts/test_bloque1.py` (testing) -> `models/user.py` (presentation): testing must not import presentation
- `scripts/test_bloque1.py` (testing) -> `views/admin.py` (presentation): testing must not import presentation
- `tests/conftest.py` (testing) -> `app_factory.py` (presentation): testing must not import presentation
- `tests/conftest.py` (testing) -> `utils/security.py` (presentation): testing must not import presentation
- `tests/test_account_facade.py` (testing) -> `app_factory.py` (presentation): testing must not import presentation
- `tests/test_account_facade.py` (testing) -> `controllers/facade.py` (presentation): testing must not import presentation
- `tests/test_account_facade.py` (testing) -> `models/user.py` (presentation): testing must not import presentation
- `tests/test_cover.py` (testing) -> `app_factory.py` (presentation): testing must not import presentation
- `tests/test_cover.py` (testing) -> `controllers/facade.py` (presentation): testing must not import presentation
- `tests/test_deniable_vault.py` (testing) -> `controllers/deniable_vault.py` (presentation): testing must not import presentation

## Dataflow Issues (INFERRED, review each lead)

- `tests/test_secure_channel.py:141` `test_env_template_documents_channel_keys` [UNCHECKED_ALLOC] `text`: Result of allocator stored in `text` is never checked against NULL.
- `tests/test_secure_channel.py:687` `test_superadmin_channel_section_is_readable` [UNCHECKED_ALLOC] `text`: Result of allocator stored in `text` is never checked against NULL.
- `tests/test_secure_channel.py:777` `test_s3_probe_detects_live_endpoint` [UNCHECKED_ALLOC] `server`: Result of allocator stored in `server` is never checked against NULL.
