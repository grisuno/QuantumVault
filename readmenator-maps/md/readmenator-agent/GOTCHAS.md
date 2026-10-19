# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `app_factory.py` (score: 48.80, imported by 6 files)
- `models/user.py` (score: 30.70, imported by 14 files)
- `utils/utils.py` (score: 28.80, imported by 14 files)
- `views/auth.py` (score: 24.90, imported by 5 files)
- `views/admin.py` (score: 21.90, imported by 3 files)
- `utils/security.py` (score: 19.00, imported by 8 files)
- `static/js/qv-crypto.js` (score: 18.00, imported by 6 files)
- `controllers/auth.py` (score: 15.40, imported by 1 files)
- `controllers/facade.py` (score: 14.60, imported by 5 files)
- `controllers/message.py` (score: 12.40, imported by 2 files)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `utils/utils.py` -- 14 direct, 30 total dependents
- `utils/padding.py` -- 5 direct, 23 total dependents
- `models/user.py` -- 14 direct, 22 total dependents
- `utils/security.py` -- 8 direct, 22 total dependents
- `utils/__init__.py` -- 3 direct, 17 total dependents
- `utils/mailer.py` -- 4 direct, 17 total dependents
- `models/plans.py` -- 4 direct, 16 total dependents
- `models/contact.py` -- 1 direct, 15 total dependents
- `controllers/auth.py` -- 1 direct, 14 total dependents
- `controllers/contact.py` -- 2 direct, 14 total dependents

## Hotspots (complexity + centrality)

- `static/js/qv-crypto.js` -- complexity: 0.6, centrality: 1.0, combined: 0.8
- `controllers/secure_channel.py` -- complexity: 0.6, centrality: 0.1, combined: 0.3
- `views/auth.py` -- complexity: 0.4, centrality: 0.1, combined: 0.3
- `views/admin.py` -- complexity: 0.3, centrality: 0.2, combined: 0.2
- `models/user.py` -- complexity: 0.4, centrality: 0.1, combined: 0.2
- `static/js/account.js` -- complexity: 0.1, centrality: 0.3, combined: 0.2
- `app_factory.py` -- complexity: 0.1, centrality: 0.3, combined: 0.2
- `scripts/doctor.py` -- complexity: 0.4, centrality: 0.1, combined: 0.2
- `controllers/facade.py` -- complexity: 0.4, centrality: 0.1, combined: 0.2
- `controllers/deniable_vault.py` -- complexity: 0.3, centrality: 0.1, combined: 0.2

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
