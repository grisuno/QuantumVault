# Index

| File | Purpose | Subsystem | Symbols | Used by |
|------|---------|-----------|---------|---------|
| `__init__.py` | - | root | 0 | 0 |
| `app.py` | Local development entry point. | root | 2 | 1 |
| `app_factory.py` | Application factory for QuantumVault. | root | 8 | 6 |
| `client.go` | - | root | 1 | 0 |
| `client.py` | - | root | 0 | 0 |
| `controllers/__init__.py` | - | controllers | 0 | 0 |
| `controllers/auth.py` | Zero-knowledge authentication controller for QuantumVault. | controllers | 14 | 1 |
| `controllers/contact.py` | ContactController: Handles logic related to contact messages. | controllers | 4 | 2 |
| `controllers/deniable_vault.py` | QV-DENIABLE-1 deniable vault: configuration, validation, orchestration. | controllers | 22 | 2 |
| `controllers/facade.py` | QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control. | controllers | 26 | 5 |
| `controllers/file.py` | Encrypted file persistence layer. | controllers | 9 | 2 |
| `controllers/message.py` | Server-side controller for end-to-end encrypted messages. | controllers | 4 | 2 |
| `controllers/secure_channel.py` | QV-TUNNEL disposable secure channels over Cloudflare and Tor. | controllers | 37 | 2 |
| `controllers/sync.py` | controllers/sync.py | controllers | 3 | 1 |
| `enc_dec.go` | - | root | 4 | 0 |
| `enc_dec.py` | Offline admin tool for ML-KEM-512 key-wrap encryption (QuantumVault). | root | 5 | 0 |
| `install.sh` | Script para instalar prerrequisitos y compilar el proyecto postcuantum Fecha: 26 de junio de... | root | 0 | 0 |
| `make.sh` | - | root | 0 | 0 |
| `models/__init__.py` | - | models | 0 | 0 |
| `models/contact.py` | ContactModel: Pydantic model for a contact message. | models | 9 | 1 |
| `models/deniable_vault.py` | Opaque storage for QV-DENIABLE-1 deniable vault containers. | models | 6 | 3 |
| `models/message.py` | Persistence layer for end-to-end encrypted messages. | models | 6 | 2 |
| `models/plans.py` | PlanDB: Database operations for subscription plans. | models | 10 | 4 |
| `models/superadmin_audit.py` | Append-only audit log for superadmin actions. | models | 5 | 1 |
| `models/user.py` | UserModel: Pydantic model for a user with Flask-Login support. | models | 27 | 14 |
| `pq_decrypt_password.py` | - | root | 0 | 0 |
| `scripts/doctor.py` | Doctor: verify and repair the QuantumVault operator environment. | scripts | 28 | 0 |
| `scripts/email_tool.py` | Operator email tooling for QuantumVault. | scripts | 6 | 0 |
| `scripts/garage-init.sh` | Bootstrap a fresh Garage deployment for QuantumVault. | scripts | 1 | 0 |
| `scripts/garage-native.sh` | Run Garage (S3-compatible object storage) natively, without Docker. | scripts | 3 | 0 |
| `scripts/makeadmin.py` | Operator tooling to promote QuantumVault users to a privileged role. | scripts | 5 | 0 |
| `scripts/test_bloque1.py` | Bloque 1 test: superadmin_edit_user endpoint. | scripts | 8 | 0 |
| `server.go` | - | root | 2 | 0 |
| `server.py` | - | root | 0 | 0 |
| `static/js/account.js` | Account settings controller: secure notes (QV-DENIABLE-1). | js | 9 | 0 |
| `static/js/coded-text.js` | Decipher animation for elements tagged with the "codedText" class. | js | 3 | 0 |
| `static/js/login.js` | Login page controller (zero-knowledge SRP-6a flow). | js | 2 | 1 |
| `static/js/messages.js` | Messages page controller (zero-knowledge end-to-end messaging). | js | 6 | 0 |
| `static/js/qv-crypto.js` | QuantumVault zero-knowledge browser crypto. | js | 40 | 6 |
| `static/js/qv-deniable.js` | QuantumVault deniable vault (QV-DENIABLE-1) browser crypto. | js | 7 | 1 |
| `static/js/qv-padding.js` | QuantumVault fixed-bucket padding (QV-PAD-1), browser mirror of utils/padding.py. | js | 5 | 1 |
| `static/js/recover.js` | Account recovery page controller (QV-RECOVERY-1 flow). | js | 3 | 0 |
| `static/js/register.js` | Registration page controller (zero-knowledge flow). | js | 3 | 1 |
| `static/js/upload.js` | Upload page controller (zero-knowledge file storage). | js | 6 | 0 |
| `templates/terms.py` | terms: Render the About page. | misc | 1 | 0 |
| `test.sh` | - | root | 0 | 0 |
| `tests/__init__.py` | - | tests | 0 | 0 |
| `tests/conftest.py` | Shared pytest fixtures for the QuantumVault test suite. | tests | 8 | 0 |
| `tests/test_account_facade.py` | Behaviour contract: the decoy site requires a deniable passphrase. | tests | 6 | 0 |
| `tests/test_auth_phone.py` | Regression tests for the phone-verification page and resend route. | tests | 3 | 0 |
| `tests/test_cover.py` | Specification tests for the QV-FACADE-2 configurable cover templates. | tests | 52 | 0 |
| `tests/test_deniable_vault.py` | Specification tests for the QV-DENIABLE-1 deniable vault feature. | tests | 55 | 0 |
| `tests/test_doctor.py` | Behaviour contracts for scripts/doctor.py. | tests | 12 | 0 |
| `tests/test_facade.py` | Specification tests for the QV-FACADE-1 cover facade and two-step gate. | tests | 52 | 0 |
| `tests/test_integrity.py` | Contract tests for SRI pins and reproducible builds (QV-SRI-1). | tests | 6 | 0 |
| `tests/test_padding.py` | Contract tests for fixed-bucket padding (QV-PAD-1) and its enforcement. | tests | 24 | 0 |
| `tests/test_secure_channel.py` | Behaviour contracts for QV-TUNNEL disposable secure channels. | tests | 67 | 0 |
| `tests/test_security.py` | Tests for utils/security.py: audit log redaction and JSON CSRF protection. | tests | 8 | 0 |
| `tests/test_srp.py` | Pure-Python SRP-6a (QV-SRP-1) roundtrip test. | tests | 6 | 0 |
| `tests/test_utils.py` | Contract tests for shared utility helpers. | tests | 3 | 0 |
| `tools/generate_sri.py` | Generate the SRI manifest for first-party assets and pinned CDN URLs. | tools | 5 | 0 |
| `tools/mutation_test.py` | Mutation testing harness for the QuantumVault facade and cover contracts. | tools | 8 | 0 |
| `tools/verify_build.py` | Verify reproducible builds and the fixed code contracts (QV-SRI-1). | tools | 11 | 1 |
| `utils/__init__.py` | - | utils | 0 | 3 |
| `utils/cache.py` | /home/grisun0/src/postcuantum/v1/utils/cache.py | utils | 5 | 0 |
| `utils/integrity.py` | Subresource Integrity manifest helpers (QV-SRI-1). | utils | 8 | 4 |
| `utils/mailer.py` | Transactional email helpers for QuantumVault. | utils | 3 | 4 |
| `utils/padding.py` | Fixed-bucket padding for metadata-size concealment (QV-PAD-1). | utils | 13 | 5 |
| `utils/plans.py` | SubscriptionPlans: Define los planes de suscripción disponibles. | utils | 3 | 0 |
| `utils/scheduler.py` | Background scheduler for trial expiration and inbox cleanup. | utils | 5 | 0 |
| `utils/security.py` | Centralized security primitives for QuantumVault. | utils | 10 | 8 |
| `utils/srp6a.py` | Zero-knowledge SRP-6a authentication primitives for QuantumVault. | utils | 14 | 0 |
| `utils/utils.py` | utils/utils.py | utils | 8 | 14 |
| `views/__init__.py` | - | views | 0 | 0 |
| `views/about.py` | about: Render the About page. | views | 1 | 1 |
| `views/account.py` | Account settings page and the deniable vault JSON API (QV-DENIABLE-1). | views | 5 | 1 |
| `views/admin.py` | UserEditForm: Form for editing user details. | views | 19 | 3 |
| `views/auth.py` | Authentication and account-management views. | views | 29 | 5 |
| `views/facade.py` | Cover facade HTTP integration: before-request cover and the gate endpoint. | views | 6 | 1 |
| `views/faq.py` | faq: Render the About page. | views | 2 | 1 |
| `views/file.py` | UploadForm: Formulario para la subida de archivos cifrados. | views | 3 | 1 |
| `views/message.py` | MessageForm: Form for sending messages. | views | 3 | 1 |
| `views/privacy.py` | privacy: Render the About page. | views | 1 | 1 |
| `views/subscription.py` | SubscriptionForm: Formulario para seleccionar un plan de suscripción. | views | 4 | 1 |
| `views/sync.py` | End-to-end encrypted file synchronization views. | views | 2 | 1 |
| `views/terms.py` | terms: Render the About page. | views | 1 | 1 |
| `views/views.py` | Top-level non-API views: home page, account preferences, etc. | views | 2 | 1 |
| `wsgi.py` | WSGI entry point for production deployments. | root | 0 | 0 |
