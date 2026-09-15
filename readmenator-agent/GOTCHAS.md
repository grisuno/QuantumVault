# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `app_factory.py` (score: 46.80)
- `utils/utils.py` (score: 30.80)
- `models/user.py` (score: 30.70)
- `views/auth.py` (score: 24.90)
- `utils/security.py` (score: 19.00)
- `views/admin.py` (score: 17.10)
- `static/js/qv-crypto.js` (score: 16.00)
- `controllers/facade.py` (score: 14.60)
- `controllers/auth.py` (score: 13.40)
- `tests/test_deniable_vault.py` (score: 11.50)

## Hotspots (complexity + centrality)

- `static/js/qv-crypto.js` -- complexity: 0.7, centrality: 1.0, combined: 0.9
- `tests/test_deniable_vault.py` -- complexity: 1.0, centrality: 0.1, combined: 0.4
- `tests/test_facade.py` -- complexity: 0.9, centrality: 0.0, combined: 0.4
- `tests/test_cover.py` -- complexity: 0.9, centrality: 0.0, combined: 0.4
- `views/auth.py` -- complexity: 0.5, centrality: 0.1, combined: 0.3
- `models/user.py` -- complexity: 0.5, centrality: 0.1, combined: 0.3
- `static/js/account.js` -- complexity: 0.2, centrality: 0.3, combined: 0.2
- `controllers/facade.py` -- complexity: 0.5, centrality: 0.1, combined: 0.2
- `app_factory.py` -- complexity: 0.1, centrality: 0.3, combined: 0.2
- `controllers/deniable_vault.py` -- complexity: 0.4, centrality: 0.1, combined: 0.2

## Dependency Cycles

Circular dependencies. Refactor to break the cycle.

- `static/js/qv-crypto.js` -> `static/js/register.js`
- `static/js/qv-crypto.js` -> `static/js/login.js`

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
