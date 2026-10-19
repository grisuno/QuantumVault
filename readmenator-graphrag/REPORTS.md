# GraphRAG Community Reports

Entities: 1044 | Relationships: 3544 | Communities: 8 | Themes: 4 | Text units: 877

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

90 files in 8 communities and 4 themes. Highest-impact communities: views: auth (7.0), quantumvault/static/js (6.0), unassigned files (4.7). God nodes: quantumvault/app_factory.py, models/user.py, utils/utils.py, views/auth.py, views/admin.py.

- [views: auth] rating 7.0: `utils/utils.py` ranks 1 by PageRank, 15 importers, 8 symbols: utils/utils.py
- [quantumvault/static/js] rating 6.0: `quantumvault/static/js/qv-crypto.js` ranks 1 by PageRank, 6 importers, 40 symbols: QuantumVault zero-knowledge browser crypto.
- [unassigned files] rating 4.7: `__init__.py` ranks 1 by PageRank, 0 importers, 0 symbols.
- [utils] rating 3.7: `utils/padding.py` ranks 1 by PageRank, 5 importers, 13 symbols: Fixed-bucket padding for metadata-size concealment (QV-PAD-1).
- [views: facade] rating 3.0: `quantumvault/app_factory.py` ranks 1 by PageRank, 6 importers, 8 symbols: Application factory for QuantumVault.
- [views: deniable_vault] rating 2.9: `utils/security.py` ranks 1 by PageRank, 8 importers, 10 symbols: Centralized security primitives for QuantumVault.
- [controllers] rating 2.2: `models/contact.py` ranks 1 by PageRank, 1 importers, 9 symbols: ContactModel: Pydantic model for a contact message.
- [quantumvault] rating 0.5: `utils/version.py` ranks 1 by PageRank, 1 importers, 0 symbols: QuantumVault package version.
- Key entities: file:views/auth.py, file:models/user.py, file:quantumvault/static/js/qv-crypto.js, file:quantumvault/static/js/qv-deniable.js, file:scripts/doctor.py, file:enc_dec.go
- Children: t0, t1, t2, t3
- Root rating = highest community rating.

## views: auth + views: facade +2 (`t0`, theme, rating 7.0)

Theme of 4 communities and 43 files: views: auth (16 files, rating 7.0); views: facade (11 files, rating 3.0); views: deniable_vault (8 files, rating 2.9); controllers (8 files, rating 2.2).

- [views: auth] `utils/utils.py` ranks 1 by PageRank, 15 importers, 8 symbols: utils/utils.py
- [views: auth] `models/user.py` ranks 2 by PageRank, 14 importers, 27 symbols: UserModel: Pydantic model for a user with Flask-Login support.
- [views: facade] `quantumvault/app_factory.py` ranks 1 by PageRank, 6 importers, 8 symbols: Application factory for QuantumVault.
- [views: facade] `controllers/facade.py` ranks 2 by PageRank, 5 importers, 26 symbols: QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.
- [views: deniable_vault] `utils/security.py` ranks 1 by PageRank, 8 importers, 10 symbols: Centralized security primitives for QuantumVault.
- [views: deniable_vault] `models/deniable_vault.py` ranks 2 by PageRank, 3 importers, 6 symbols: Opaque storage for QV-DENIABLE-1 deniable vault containers.
- [controllers] `models/contact.py` ranks 1 by PageRank, 1 importers, 9 symbols: ContactModel: Pydantic model for a contact message.
- [controllers] `views/admin.py` ranks 2 by PageRank, 7 importers, 19 symbols: UserEditForm: Form for editing user details.
- Key entities: file:views/auth.py, file:models/user.py, file:tests/test_cover.py, file:tests/test_facade.py, file:tests/test_deniable_vault.py, file:controllers/deniable_vault.py, file:tests/test_secure_channel.py, file:controllers/secure_channel.py
- Children: c0, c1, c5, c4
- Theme rating = highest child community rating.

## quantumvault/static/js + utils (`t2`, theme, rating 6.0)

Theme of 2 communities and 19 files: quantumvault/static/js (9 files, rating 6.0); utils (10 files, rating 3.7).

- [quantumvault/static/js] `quantumvault/static/js/qv-crypto.js` ranks 1 by PageRank, 6 importers, 40 symbols: QuantumVault zero-knowledge browser crypto.
- [quantumvault/static/js] `quantumvault/static/js/login.js` ranks 2 by PageRank, 1 importers, 2 symbols: Login page controller (zero-knowledge SRP-6a flow).
- [utils] `utils/padding.py` ranks 1 by PageRank, 5 importers, 13 symbols: Fixed-bucket padding for metadata-size concealment (QV-PAD-1).
- [utils] `utils/integrity.py` ranks 2 by PageRank, 4 importers, 8 symbols: Subresource Integrity manifest helpers (QV-SRI-1).
- Key entities: file:quantumvault/static/js/qv-crypto.js, file:quantumvault/static/js/qv-deniable.js, file:tests/test_padding.py, file:utils/padding.py
- Children: c3, c2
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 4.7)

Theme of 1 communities and 26 files: unassigned files (26 files, rating 4.7).

- [unassigned files] `__init__.py` ranks 1 by PageRank, 0 importers, 0 symbols.
- [unassigned files] `client.go` ranks 2 by PageRank, 0 importers, 1 symbols.
- Key entities: file:scripts/doctor.py, file:enc_dec.go
- Children: c7
- Theme rating = highest child community rating.

## quantumvault (`t3`, theme, rating 0.5)

Theme of 1 communities and 2 files: quantumvault (2 files, rating 0.5).

- [quantumvault] `utils/version.py` ranks 1 by PageRank, 1 importers, 0 symbols: QuantumVault package version.
- [quantumvault] `quantumvault/__init__.py` ranks 2 by PageRank, 0 importers, 0 symbols: QuantumVault application package.
- Key entities: file:quantumvault/__init__.py, file:utils/version.py
- Children: c6
- Theme rating = highest child community rating.

## views: auth (`c0`, community, rating 7.0)

16 files under views (py 16), mostly presentation. Core file utils/utils.py (PageRank 0.0761, imported by 15 files): utils/utils.py Key abstractions: Payload, Config, database_path, as_bool, sanitize_path, load_payload. Depends on utils (2), views: deniable_vault (2), controllers (1). Used by views: facade (10), controllers (7), utils (4).

- `utils/utils.py` ranks 1 by PageRank, 15 importers, 8 symbols: utils/utils.py
- `models/user.py` ranks 2 by PageRank, 14 importers, 27 symbols: UserModel: Pydantic model for a user with Flask-Login support.
- `views/auth.py` ranks 3 by PageRank, 5 importers, 29 symbols: Authentication and account-management views.
- Hotspot `views/auth.py`: 29 symbols, 28 connections (score 0.25).
- Hotspot `models/user.py`: 27 symbols, 21 connections (score 0.22).
- 1 layer violations, e.g. test_utils.py (testing) -> utils.py (presentation).
- Taint: 6 paths reach this group via subprocess.
- Key entities: file:views/auth.py, file:models/user.py, file:controllers/auth.py, file:utils/utils.py, file:models/message.py, sym:models/user.py::get_user@454, file:models/plans.py, file:scripts/email_tool.py
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 26.

## quantumvault/static/js (`c3`, community, rating 6.0)

9 files under quantumvault/static/js (js 9), mostly utility. Core file quantumvault/static/js/qv-crypto.js (PageRank 0.0788, imported by 6 files): QuantumVault zero-knowledge browser crypto. Key abstractions: concatBytes, hexToBytes, bytesToHex, bytesToBase64, bytesToBase32, base64ToBytes. Depends on utils (1).

- `quantumvault/static/js/qv-crypto.js` ranks 1 by PageRank, 6 importers, 40 symbols: QuantumVault zero-knowledge browser crypto.
- `quantumvault/static/js/login.js` ranks 2 by PageRank, 1 importers, 2 symbols: Login page controller (zero-knowledge SRP-6a flow).
- `quantumvault/static/js/qv-padding.js` ranks 3 by PageRank, 1 importers, 5 symbols: QuantumVault fixed-bucket padding (QV-PAD-1), browser mirror of utils/padding.py.
- Hotspot `quantumvault/static/js/qv-crypto.js`: 40 symbols, 215 connections (score 0.84).
- Hotspot `quantumvault/static/js/account.js`: 9 symbols, 59 connections (score 0.22).
- Dependency cycle: qv-crypto.js -> register.js -> qv-crypto.js.
- Surprising bridge: contact.py <-> account.js (9 hops across communities).
- Key entities: file:quantumvault/static/js/qv-crypto.js, file:quantumvault/static/js/qv-deniable.js, file:quantumvault/static/js/account.js, file:quantumvault/static/js/messages.js, file:quantumvault/static/js/upload.js, file:quantumvault/static/js/qv-padding.js, file:quantumvault/static/js/register.js, file:quantumvault/static/js/recover.js
- Rating 6.0/10 = 7 x PageRank share 0.85 + 3 x risk 0.00. Internal imports: 10.

## unassigned files (`c7`, community, rating 4.7)

26 files under root (py 17, sh 5, go 3, js 1), mostly utility. Core file __init__.py (PageRank 0.0060, imported by 0 files). Key abstractions: main, deriveAESKey, encryptFile, decryptFile, main, derive_aes_key.

- `__init__.py` ranks 1 by PageRank, 0 importers, 0 symbols.
- `client.go` ranks 2 by PageRank, 0 importers, 1 symbols.
- `client.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `scripts/doctor.py`: 28 symbols, 13 connections (score 0.20).
- Hotspot `utils/srp6a.py`: 14 symbols, 6 connections (score 0.10).
- Taint: 3 paths reach this group via subprocess, urllib.request.
- Key entities: file:scripts/doctor.py, file:enc_dec.go, file:utils/srp6a.py, file:enc_dec.py, file:tests/test_doctor.py, file:tools/mutation_test.py, file:client.go, sym:scripts/doctor.py::collect_report@449
- Rating 4.7/10 = 7 x PageRank share 0.67 + 3 x risk 0.00. Internal imports: 0.

## utils (`c2`, community, rating 3.7)

10 files under tests (py 10), mostly utility. Core file utils/padding.py (PageRank 0.0407, imported by 5 files): Fixed-bucket padding for metadata-size concealment (QV-PAD-1). Key abstractions: PaddingError, PaddingConfig, buckets_for, max_plaintext_bytes, config_from_env, cached_tables. Depends on views: auth (4). Used by views: auth (2), views: facade (2), quantumvault/static/js (1).

- `utils/padding.py` ranks 1 by PageRank, 5 importers, 13 symbols: Fixed-bucket padding for metadata-size concealment (QV-PAD-1).
- `utils/integrity.py` ranks 2 by PageRank, 4 importers, 8 symbols: Subresource Integrity manifest helpers (QV-SRI-1).
- `utils/__init__.py` ranks 3 by PageRank, 3 importers, 0 symbols.
- Hotspot `tests/test_padding.py`: 24 symbols, 11 connections (score 0.17).
- Hotspot `utils/padding.py`: 13 symbols, 12 connections (score 0.11).
- 2 layer violations, e.g. test_padding.py (testing) -> file.py (presentation).
- Taint: 3 paths reach this group via subprocess, urllib.request.
- Key entities: file:tests/test_padding.py, file:utils/padding.py, file:utils/integrity.py, file:tools/verify_build.py, file:controllers/file.py, file:controllers/message.py, file:tools/generate_sri.py, file:tests/test_integrity.py
- Rating 3.7/10 = 7 x PageRank share 0.53 + 3 x risk 0.00. Internal imports: 12.

## views: facade (`c1`, community, rating 3.0)

11 files under views (py 11), mostly presentation. Core file quantumvault/app_factory.py (PageRank 0.0228, imported by 6 files): Application factory for QuantumVault. Key abstractions: create_app, load_user, GateOutcome, GateDecision, FacadeConfig, GatePhraseHasher. Depends on views: auth (10), views: deniable_vault (3), utils (2). Used by views: deniable_vault (2), controllers (1).

- `quantumvault/app_factory.py` ranks 1 by PageRank, 6 importers, 8 symbols: Application factory for QuantumVault.
- `controllers/facade.py` ranks 2 by PageRank, 5 importers, 26 symbols: QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.
- `controllers/sync.py` ranks 3 by PageRank, 1 importers, 3 symbols: controllers/sync.py
- Hotspot `tests/test_facade.py`: 52 symbols, 10 connections (score 0.34).
- Hotspot `tests/test_cover.py`: 52 symbols, 7 connections (score 0.33).
- 8 layer violations, e.g. test_account_facade.py (testing) -> app_factory.py (presentation).
- Surprising bridge: facade.py <-> account.js (8 hops across communities).
- Key entities: file:tests/test_cover.py, file:tests/test_facade.py, file:quantumvault/app_factory.py, file:controllers/facade.py, sym:tests/test_cover.py::store@52, sym:quantumvault/app_factory.py::create_app@237, sym:controllers/facade.py::evaluate@359, file:views/facade.py
- Rating 3.0/10 = 7 x PageRank share 0.43 + 3 x risk 0.00. Internal imports: 13.

## views: deniable_vault (`c5`, community, rating 2.9)

8 files under tests (py 8), mostly presentation. Core file utils/security.py (PageRank 0.0425, imported by 8 files): Centralized security primitives for QuantumVault. Key abstractions: audit_event, constant_time_compare, hash_secret, verify_secret, new_one_time_code, json_csrf_protect. Depends on views: auth (3), views: facade (2). Used by views: facade (3), views: auth (2).

- `utils/security.py` ranks 1 by PageRank, 8 importers, 10 symbols: Centralized security primitives for QuantumVault.
- `models/deniable_vault.py` ranks 2 by PageRank, 3 importers, 6 symbols: Opaque storage for QV-DENIABLE-1 deniable vault containers.
- `controllers/deniable_vault.py` ranks 3 by PageRank, 2 importers, 22 symbols: QV-DENIABLE-1 deniable vault: configuration, validation, orchestration.
- Hotspot `tests/test_deniable_vault.py`: 55 symbols, 12 connections (score 0.36).
- Hotspot `controllers/deniable_vault.py`: 22 symbols, 14 connections (score 0.17).
- 5 layer violations, e.g. conftest.py (testing) -> app_factory.py (presentation).
- Taint: 1 paths reach this group via subprocess.
- Surprising bridge: deniable_vault.py <-> account.js (8 hops across communities).
- Key entities: file:tests/test_deniable_vault.py, file:controllers/deniable_vault.py, file:utils/security.py, sym:controllers/deniable_vault.py::validate@285, sym:utils/security.py::audit_event@86, sym:tests/test_deniable_vault.py::_valid_envelope@71, file:tests/conftest.py, file:models/deniable_vault.py
- Rating 2.9/10 = 7 x PageRank share 0.41 + 3 x risk 0.00. Internal imports: 10.

## controllers (`c4`, community, rating 2.2)

8 files under controllers (py 8), mostly presentation. Core file models/contact.py (PageRank 0.0145, imported by 1 files): ContactModel: Pydantic model for a contact message. Key abstractions: ContactModel, ContactDB, create_contact, get_user_contacts, get_all_contacts, UserEditForm. Depends on views: auth (7), views: facade (1). Used by views: auth (1), views: facade (1).

- `models/contact.py` ranks 1 by PageRank, 1 importers, 9 symbols: ContactModel: Pydantic model for a contact message.
- `views/admin.py` ranks 2 by PageRank, 7 importers, 19 symbols: UserEditForm: Form for editing user details.
- `controllers/contact.py` ranks 3 by PageRank, 2 importers, 4 symbols: ContactController: Handles logic related to contact messages.
- Hotspot `tests/test_secure_channel.py`: 67 symbols, 25 connections (score 0.47).
- Hotspot `controllers/secure_channel.py`: 37 symbols, 17 connections (score 0.27).
- 8 layer violations, e.g. test_bloque1.py (testing) -> user.py (presentation).
- Taint: 7 paths reach this group via subprocess.
- Dataflow: 3 INFERRED issues (first: UNCHECKED_ALLOC in test_env_template_documents_channel_keys).
- Key entities: file:tests/test_secure_channel.py, file:controllers/secure_channel.py, file:views/admin.py, sym:controllers/secure_channel.py::SecureChannelManager@220, file:models/contact.py, file:scripts/test_bloque1.py, file:models/superadmin_audit.py, sym:controllers/secure_channel.py::_status_for@337
- Rating 2.2/10 = 7 x PageRank share 0.31 + 3 x risk 0.00. Internal imports: 12.

## quantumvault (`c6`, community, rating 0.5)

2 files under quantumvault (py 2), mostly utility. Core file utils/version.py (PageRank 0.0111, imported by 1 files): QuantumVault package version.

- `utils/version.py` ranks 1 by PageRank, 1 importers, 0 symbols: QuantumVault package version.
- `quantumvault/__init__.py` ranks 2 by PageRank, 0 importers, 0 symbols: QuantumVault application package.
- Hotspot `quantumvault/__init__.py`: 0 symbols, 2 connections (score 0.01).
- Hotspot `utils/version.py`: 0 symbols, 1 connections (score 0.00).
- Key entities: file:quantumvault/__init__.py, file:utils/version.py
- Rating 0.5/10 = 7 x PageRank share 0.07 + 3 x risk 0.00. Internal imports: 1.
