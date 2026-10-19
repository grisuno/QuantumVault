# QuantumVault API Reference

> Generated offline by readmenator: 73 modules, 691 documented entities, documentation coverage 76.4% (360/471 public items). Deterministic, zero tokens: signatures from source, docs parsed from Google, NumPy, reST, Javadoc/JSDoc/Doxygen, C# XML, and Rustdoc comments.

Navigate: [Interactive architecture and flows](flows.html) | [Architecture and flows (Mermaid)](architecture.md) | [Class hierarchy](classes.md) | [General index](genindex.md) | [Coverage and warnings](COVERAGE.md) | [`api/index.json`](api/index.json) | [HTML browser](index.html)

Languages: go (3), js (10), py (56), sh (4)

## Modules

### `.`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`__init__`](modules/init__.py.md) |  | 0 | 0 | 0.0% |
| [`app`](modules/app.py.md) | Local development entry point. | 0 | 1 | 50.0% |
| [`client.go`](modules/client.go.md) |  | 0 | 0 | 0.0% |
| [`client`](modules/client.py.md) |  | 0 | 0 | 0.0% |
| [`enc_dec.go`](modules/enc_dec.go.md) |  | 0 | 0 | 0.0% |
| [`enc_dec`](modules/enc_dec.py.md) | Offline admin tool for ML-KEM-512 key-wrap encryption (QuantumVault). | 0 | 4 | 100.0% |
| [`install.sh`](modules/install.sh.md) | install.sh: Script para instalar prerrequisitos y compilar el proyecto postcuantum Fecha: 26 de junio de 2025 Autor: Grok 3 (xAI) | 0 | 0 | 100.0% |
| [`make.sh`](modules/make.sh.md) |  | 0 | 0 | 0.0% |
| [`pq_decrypt_password`](modules/pq_decrypt_password.py.md) |  | 0 | 0 | 0.0% |
| [`server.go`](modules/server.go.md) |  | 0 | 0 | 0.0% |
| [`server`](modules/server.py.md) |  | 0 | 0 | 0.0% |

### `controllers`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`controllers`](modules/controllers.__init__.py.md) |  | 0 | 0 | 0.0% |
| [`controllers.auth`](modules/controllers.auth.py.md) | Zero-knowledge authentication controller for QuantumVault. | 1 | 11 | 100.0% |
| [`controllers.contact`](modules/controllers.contact.py.md) |  | 1 | 3 | 80.0% |
| [`controllers.deniable_vault`](modules/controllers.deniable_vault.py.md) | QV-DENIABLE-1 deniable vault: configuration, validation, orchestration. | 4 | 12 | 100.0% |
| [`controllers.facade`](modules/controllers.facade.py.md) | QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control. | 6 | 14 | 100.0% |
| [`controllers.file`](modules/controllers.file.py.md) | Encrypted file persistence layer. | 1 | 6 | 87.5% |
| [`controllers.message`](modules/controllers.message.py.md) | Server-side controller for end-to-end encrypted messages. | 1 | 3 | 100.0% |
| [`controllers.secure_channel`](modules/controllers.secure_channel.py.md) | QV-TUNNEL disposable secure channels over Cloudflare and Tor. | 4 | 14 | 100.0% |
| [`controllers.sync`](modules/controllers.sync.py.md) | controllers/sync.py | 1 | 2 | 50.0% |

### `models`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`models`](modules/models.__init__.py.md) |  | 0 | 0 | 0.0% |
| [`models.contact`](modules/models.contact.py.md) |  | 2 | 4 | 85.7% |
| [`models.deniable_vault`](modules/models.deniable_vault.py.md) | Opaque storage for QV-DENIABLE-1 deniable vault containers. | 1 | 4 | 100.0% |
| [`models.message`](modules/models.message.py.md) | Persistence layer for end-to-end encrypted messages. | 2 | 4 | 100.0% |
| [`models.plans`](modules/models.plans.py.md) |  | 1 | 7 | 88.9% |
| [`models.superadmin_audit`](modules/models.superadmin_audit.py.md) | Append-only audit log for superadmin actions. | 1 | 3 | 100.0% |
| [`models.user`](modules/models.user.py.md) |  | 2 | 18 | 95.2% |

### `quantumvault`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`quantumvault`](modules/quantumvault.__init__.py.md) | QuantumVault application package. | 0 | 0 | 100.0% |
| [`quantumvault.app_factory`](modules/quantumvault.app_factory.py.md) | Application factory for QuantumVault. | 0 | 1 | 100.0% |
| [`quantumvault.wsgi`](modules/quantumvault.wsgi.py.md) | WSGI entry point for production deployments. | 0 | 1 | 100.0% |

### `quantumvault/static/js`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`quantumvault/static/js/account.js`](modules/quantumvault.static.js.account.js.md) | Account settings controller: secure notes (QV-DENIABLE-1). | 0 | 9 | 10.0% |
| [`quantumvault/static/js/coded-text.js`](modules/quantumvault.static.js.coded-text.js.md) | Decipher animation for elements tagged with the "codedText" class. | 0 | 3 | 25.0% |
| [`quantumvault/static/js/login.js`](modules/quantumvault.static.js.login.js.md) | Login page controller (zero-knowledge SRP-6a flow). | 0 | 2 | 33.3% |
| [`quantumvault/static/js/messages.js`](modules/quantumvault.static.js.messages.js.md) | Messages page controller (zero-knowledge end-to-end messaging). | 0 | 6 | 14.3% |
| [`quantumvault/static/js/qv-crypto.js`](modules/quantumvault.static.js.qv-crypto.js.md) | QuantumVault zero-knowledge browser crypto. | 0 | 40 | 46.3% |
| [`quantumvault/static/js/qv-deniable.js`](modules/quantumvault.static.js.qv-deniable.js.md) | QuantumVault deniable vault (QV-DENIABLE-1) browser crypto. | 0 | 7 | 87.5% |
| [`quantumvault/static/js/qv-padding.js`](modules/quantumvault.static.js.qv-padding.js.md) | QuantumVault fixed-bucket padding (QV-PAD-1), browser mirror of utils/padding.py. | 0 | 5 | 16.7% |
| [`quantumvault/static/js/recover.js`](modules/quantumvault.static.js.recover.js.md) | Account recovery page controller (QV-RECOVERY-1 flow). | 0 | 3 | 25.0% |
| [`quantumvault/static/js/register.js`](modules/quantumvault.static.js.register.js.md) | Registration page controller (zero-knowledge flow). | 0 | 3 | 50.0% |
| [`quantumvault/static/js/upload.js`](modules/quantumvault.static.js.upload.js.md) | Upload page controller (zero-knowledge file storage). | 0 | 6 | 14.3% |

### `quantumvault/templates`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`quantumvault.templates.terms`](modules/quantumvault.templates.terms.py.md) |  | 0 | 1 | 50.0% |

### `scripts`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`scripts.doctor`](modules/scripts.doctor.py.md) | Doctor: verify and repair the QuantumVault operator environment. | 2 | 26 | 100.0% |
| [`scripts.email_tool`](modules/scripts.email_tool.py.md) | Operator email tooling for QuantumVault. | 0 | 5 | 100.0% |
| [`scripts/garage-init.sh`](modules/scripts.garage-init.sh.md) | Bootstrap a fresh Garage deployment for QuantumVault. | 0 | 1 | 100.0% |
| [`scripts/garage-native.sh`](modules/scripts.garage-native.sh.md) | Run Garage (S3-compatible object storage) natively, without Docker. | 0 | 3 | 50.0% |
| [`scripts.makeadmin`](modules/scripts.makeadmin.py.md) | Operator tooling to promote QuantumVault users to a privileged role. | 0 | 3 | 100.0% |

### `tools`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`tools.generate_sri`](modules/tools.generate_sri.py.md) | Generate the SRI manifest for first-party assets and pinned CDN URLs. | 0 | 5 | 100.0% |
| [`tools.verify_build`](modules/tools.verify_build.py.md) | Verify reproducible builds and the fixed code contracts (QV-SRI-1). | 1 | 9 | 100.0% |

### `utils`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`utils`](modules/utils.__init__.py.md) |  | 0 | 0 | 0.0% |
| [`utils.cache`](modules/utils.cache.py.md) | /home/grisun0/src/postcuantum/v1/utils/cache.py | 1 | 4 | 83.3% |
| [`utils.integrity`](modules/utils.integrity.py.md) | Subresource Integrity manifest helpers (QV-SRI-1). | 0 | 7 | 100.0% |
| [`utils.mailer`](modules/utils.mailer.py.md) | Transactional email helpers for QuantumVault. | 0 | 3 | 100.0% |
| [`utils.padding`](modules/utils.padding.py.md) | Fixed-bucket padding for metadata-size concealment (QV-PAD-1). | 2 | 9 | 100.0% |
| [`utils.plans`](modules/utils.plans.py.md) |  | 1 | 2 | 75.0% |
| [`utils.scheduler`](modules/utils.scheduler.py.md) | Background scheduler for trial expiration and inbox cleanup. | 0 | 1 | 100.0% |
| [`utils.security`](modules/utils.security.py.md) | Centralized security primitives for QuantumVault. | 0 | 6 | 100.0% |
| [`utils.srp6a`](modules/utils.srp6a.py.md) | Zero-knowledge SRP-6a authentication primitives for QuantumVault. | 1 | 10 | 100.0% |
| [`utils.utils`](modules/utils.utils.py.md) | utils/utils.py | 2 | 5 | 87.5% |
| [`utils.version`](modules/utils.version.py.md) | QuantumVault package version. | 0 | 0 | 100.0% |

### `views`

| Module | Summary | Types | Callables | Coverage |
|---|---|---|---|---|
| [`views`](modules/views.__init__.py.md) |  | 0 | 0 | 0.0% |
| [`views.about`](modules/views.about.py.md) |  | 0 | 1 | 50.0% |
| [`views.account`](modules/views.account.py.md) | Account settings page and the deniable vault JSON API (QV-DENIABLE-1). | 0 | 5 | 100.0% |
| [`views.admin`](modules/views.admin.py.md) |  | 2 | 12 | 86.7% |
| [`views.auth`](modules/views.auth.py.md) | Authentication and account-management views. | 5 | 20 | 46.2% |
| [`views.facade`](modules/views.facade.py.md) | Cover facade HTTP integration: before-request cover and the gate endpoint. | 0 | 1 | 100.0% |
| [`views.faq`](modules/views.faq.py.md) |  | 0 | 2 | 66.7% |
| [`views.file`](modules/views.file.py.md) |  | 1 | 2 | 75.0% |
| [`views.message`](modules/views.message.py.md) |  | 1 | 2 | 75.0% |
| [`views.privacy`](modules/views.privacy.py.md) |  | 0 | 1 | 50.0% |
| [`views.subscription`](modules/views.subscription.py.md) |  | 1 | 3 | 60.0% |
| [`views.sync`](modules/views.sync.py.md) | End-to-end encrypted file synchronization views. | 0 | 2 | 66.7% |
| [`views.terms`](modules/views.terms.py.md) |  | 0 | 1 | 50.0% |
| [`views.views`](modules/views.views.py.md) | Top-level non-API views: home page, account preferences, etc. | 1 | 1 | 66.7% |
