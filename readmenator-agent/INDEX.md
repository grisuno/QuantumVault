# Index

| File | Purpose | Subsystem | Symbols |
|------|---------|-----------|---------|
| `__init__.py` | - | root | 0 |
| `app.py` | Local development entry point.  This script exists for the ``make run`` workflow | root | 2 |
| `app_factory.py` | Application factory for QuantumVault.  The same ``create_app()`` callable powers | root | 8 |
| `client.go` | - | root | 1 |
| `client.py` | - | root | 0 |
| `controllers/__init__.py` | - | controllers | 0 |
| `controllers/auth.py` | Zero-knowledge authentication controller for QuantumVault.  Registration accepts | controllers | 14 |
| `controllers/contact.py` | - | controllers | 4 |
| `controllers/deniable_vault.py` | QV-DENIABLE-1 deniable vault: configuration, validation, orchestration.  This mo | controllers | 22 |
| `controllers/facade.py` | QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.  T | controllers | 26 |
| `controllers/file.py` | Encrypted file persistence layer.  The server is intentionally blind to plaintex | controllers | 9 |
| `controllers/message.py` | Server-side controller for end-to-end encrypted messages.  The browser generates | controllers | 4 |
| `controllers/sync.py` | controllers/sync.py | controllers | 3 |
| `enc_dec.go` | - | root | 4 |
| `enc_dec.py` | Offline admin tool for ML-KEM-512 key-wrap encryption (QuantumVault).  WARNING - | root | 5 |
| `install.sh` | install.sh: Script para instalar prerrequisitos y compilar el proyecto postcuant | root | 0 |
| `make.sh` | - | root | 0 |
| `models/__init__.py` | - | models | 0 |
| `models/contact.py` | - | models | 9 |
| `models/deniable_vault.py` | Opaque storage for QV-DENIABLE-1 deniable vault containers.  The server is zero- | models | 6 |
| `models/message.py` | Persistence layer for end-to-end encrypted messages.  The browser performs all c | models | 6 |
| `models/plans.py` | - | models | 10 |
| `models/superadmin_audit.py` | Append-only audit log for superadmin actions.  Why a separate table: every privi | models | 5 |
| `models/user.py` | - | models | 27 |
| `pq_decrypt_password.py` | - | root | 0 |
| `scripts/doctor.py` | Doctor: import every project module and report the first error.  Used by `make d | scripts | 0 |
| `scripts/email_tool.py` | Operator email tooling for QuantumVault.  Three subcommands, all runnable from a | scripts | 6 |
| `scripts/garage-init.sh` | Bootstrap a fresh Garage deployment for QuantumVault.  What this does: 1. Waits  | scripts | 1 |
| `scripts/garage-native.sh` | Run Garage (S3-compatible object storage) natively, without Docker.  Idempotent: | scripts | 3 |
| `scripts/makeadmin.py` | Operator tooling to promote QuantumVault users to a privileged role.  Two subcom | scripts | 5 |
| `scripts/test_bloque1.py` | Bloque 1 test: superadmin_edit_user endpoint.  Renders the user-edit form via Fl | scripts | 8 |
| `server.go` | - | root | 2 |
| `server.py` | - | root | 0 |
| `static/js/account.js` | Account settings controller: secure notes (QV-DENIABLE-1).  Loaded as an externa | js | 9 |
| `static/js/coded-text.js` | Decipher animation for elements tagged with the "codedText" class.  Extracted fr | js | 3 |
| `static/js/login.js` | Login page controller (zero-knowledge SRP-6a flow).  Loaded as an external ES mo | js | 2 |
| `static/js/messages.js` | Messages page controller (zero-knowledge end-to-end messaging).  Loaded as an ex | js | 6 |
| `static/js/qv-crypto.js` | QuantumVault zero-knowledge browser crypto.  Single source of truth for all clie | js | 40 |
| `static/js/qv-deniable.js` | QuantumVault deniable vault (QV-DENIABLE-1) browser crypto.  A deniable vault is | js | 7 |
| `static/js/recover.js` | Account recovery page controller (QV-RECOVERY-1 flow).  Loaded as an external ES | js | 3 |
| `static/js/register.js` | Registration page controller (zero-knowledge flow).  This module is loaded as an | js | 3 |
| `static/js/upload.js` | Upload page controller (zero-knowledge file storage).  Loaded as an external ES  | js | 6 |
| `templates/terms.py` | - | misc | 1 |
| `test.sh` | - | root | 0 |
| `tests/__init__.py` | - | tests | 0 |
| `tests/conftest.py` | Shared pytest fixtures for the QuantumVault test suite.  Builds the Flask app vi | tests | 7 |
| `tests/test_account_facade.py` | Behaviour contract: the decoy site requires a deniable passphrase.  When the cov | tests | 6 |
| `tests/test_auth_phone.py` | Regression tests for the phone-verification page and resend route.  The verify-p | tests | 3 |
| `tests/test_cover.py` | Specification tests for the QV-FACADE-2 configurable cover templates.  Behaviour | tests | 52 |
| `tests/test_deniable_vault.py` | Specification tests for the QV-DENIABLE-1 deniable vault feature.  The feature i | tests | 55 |
| `tests/test_facade.py` | Specification tests for the QV-FACADE-1 cover facade and two-step gate.  The fea | tests | 52 |
| `tests/test_security.py` | Tests for utils/security.py: audit log redaction and JSON CSRF protection. | tests | 8 |
| `tests/test_srp.py` | Pure-Python SRP-6a (QV-SRP-1) roundtrip test.  Mirrors the client-side math in ` | tests | 6 |
| `tests/test_utils.py` | Contract tests for shared utility helpers. | tests | 3 |
| `tools/mutation_test.py` | Mutation testing harness for the QuantumVault facade and cover contracts.  Each  | misc | 8 |
| `utils/__init__.py` | - | utils | 0 |
| `utils/cache.py` | /home/grisun0/src/postcuantum/v1/utils/cache.py | utils | 5 |
| `utils/mailer.py` | Transactional email helpers for QuantumVault.  Centralizes how outbound transact | utils | 3 |
| `utils/plans.py` | - | utils | 3 |
| `utils/scheduler.py` | Background scheduler for trial expiration and inbox cleanup.  Runs two recurring | utils | 5 |
| `utils/security.py` | Centralized security primitives for QuantumVault.  Single source of truth for:   | utils | 10 |
| `utils/srp6a.py` | Zero-knowledge SRP-6a authentication primitives for QuantumVault.  This module i | utils | 14 |
| `utils/utils.py` | utils/utils.py | utils | 8 |
| `views/__init__.py` | - | views | 0 |
| `views/about.py` | - | views | 1 |
| `views/account.py` | Account settings page and the deniable vault JSON API (QV-DENIABLE-1).  The sett | views | 5 |
| `views/admin.py` | - | views | 11 |
| `views/auth.py` | Authentication and account-management views.  Routes:  - ``GET  /register``      | views | 29 |
| `views/facade.py` | Cover facade HTTP integration: before-request cover and the gate endpoint.  When | views | 6 |
| `views/faq.py` | - | views | 2 |
| `views/file.py` | - | views | 3 |
| `views/message.py` | - | views | 3 |
| `views/privacy.py` | - | views | 1 |
| `views/subscription.py` | - | views | 4 |
| `views/sync.py` | End-to-end encrypted file synchronization views.  ``POST /secure_sync`` accepts  | views | 2 |
| `views/terms.py` | - | views | 1 |
| `views/views.py` | Top-level non-API views: home page, account preferences, etc. | views | 2 |
| `wsgi.py` | WSGI entry point for production deployments.  Run with gunicorn (or any WSGI ser | root | 0 |
