# GraphRAG Community Reports

Entities: 1040 | Relationships: 3532 | Communities: 8 | Themes: 3 | Text units: 874

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

89 files in 8 communities and 3 themes. Highest-impact communities: views: auth (7.0), static/js (6.4), unassigned files (5.2). God nodes: app_factory.py, models/user.py, utils/utils.py, views/auth.py, views/admin.py.

- [views: auth] rating 7.0: `utils/utils.py` ranks 1 by PageRank, 15 importers, 8 symbols: utils/utils.py
- [static/js] rating 6.4: `static/js/qv-crypto.js` ranks 1 by PageRank, 6 importers, 40 symbols: QuantumVault zero-knowledge browser crypto.
- [unassigned files] rating 5.2: `__init__.py` ranks 1 by PageRank, 0 importers, 0 symbols.
- [views: facade] rating 3.3: `app_factory.py` ranks 1 by PageRank, 6 importers, 8 symbols: Application factory for QuantumVault.
- [utils] rating 3.2: `utils/padding.py` ranks 1 by PageRank, 5 importers, 13 symbols: Fixed-bucket padding for metadata-size concealment (QV-PAD-1).
- [views: deniable_vault] rating 3.1: `utils/security.py` ranks 1 by PageRank, 8 importers, 10 symbols: Centralized security primitives for QuantumVault.
- [controllers] rating 2.3: `models/contact.py` ranks 1 by PageRank, 1 importers, 9 symbols: ContactModel: Pydantic model for a contact message.
- [tools] rating 1.2: `utils/integrity.py` ranks 1 by PageRank, 4 importers, 8 symbols: Subresource Integrity manifest helpers (QV-SRI-1).
- Key entities: file:views/auth.py, file:models/user.py, file:static/js/qv-crypto.js, file:static/js/qv-deniable.js, file:scripts/doctor.py, file:enc_dec.go
- Children: t0, t1, t2
- Root rating = highest community rating.

## views: auth + views: facade +2 (`t0`, theme, rating 7.0)

Theme of 4 communities and 41 files: views: auth (14 files, rating 7.0); views: facade (11 files, rating 3.3); views: deniable_vault (8 files, rating 3.1); controllers (8 files, rating 2.3).

- [views: auth] `utils/utils.py` ranks 1 by PageRank, 15 importers, 8 symbols: utils/utils.py
- [views: auth] `models/user.py` ranks 2 by PageRank, 14 importers, 27 symbols: UserModel: Pydantic model for a user with Flask-Login support.
- [views: facade] `app_factory.py` ranks 1 by PageRank, 6 importers, 8 symbols: Application factory for QuantumVault.
- [views: facade] `controllers/facade.py` ranks 2 by PageRank, 5 importers, 26 symbols: QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.
- [views: deniable_vault] `utils/security.py` ranks 1 by PageRank, 8 importers, 10 symbols: Centralized security primitives for QuantumVault.
- [views: deniable_vault] `models/deniable_vault.py` ranks 2 by PageRank, 3 importers, 6 symbols: Opaque storage for QV-DENIABLE-1 deniable vault containers.
- [controllers] `models/contact.py` ranks 1 by PageRank, 1 importers, 9 symbols: ContactModel: Pydantic model for a contact message.
- [controllers] `views/admin.py` ranks 2 by PageRank, 7 importers, 19 symbols: UserEditForm: Form for editing user details.
- Key entities: file:views/auth.py, file:models/user.py, file:tests/test_cover.py, file:tests/test_facade.py, file:tests/test_deniable_vault.py, file:controllers/deniable_vault.py, file:tests/test_secure_channel.py, file:controllers/secure_channel.py
- Children: c0, c1, c4, c3
- Theme rating = highest child community rating.

## static/js + utils +1 (`t2`, theme, rating 6.4)

Theme of 3 communities and 21 files: static/js (9 files, rating 6.4); utils (8 files, rating 3.2); tools (4 files, rating 1.2).

- [static/js] `static/js/qv-crypto.js` ranks 1 by PageRank, 6 importers, 40 symbols: QuantumVault zero-knowledge browser crypto.
- [static/js] `static/js/login.js` ranks 2 by PageRank, 1 importers, 2 symbols: Login page controller (zero-knowledge SRP-6a flow).
- [utils] `utils/padding.py` ranks 1 by PageRank, 5 importers, 13 symbols: Fixed-bucket padding for metadata-size concealment (QV-PAD-1).
- [utils] `utils/__init__.py` ranks 2 by PageRank, 3 importers, 0 symbols.
- [tools] `utils/integrity.py` ranks 1 by PageRank, 4 importers, 8 symbols: Subresource Integrity manifest helpers (QV-SRI-1).
- [tools] `tools/verify_build.py` ranks 2 by PageRank, 1 importers, 11 symbols: Verify reproducible builds and the fixed code contracts (QV-SRI-1).
- Key entities: file:static/js/qv-crypto.js, file:static/js/qv-deniable.js, file:tests/test_padding.py, file:utils/padding.py, file:tools/verify_build.py, file:utils/integrity.py
- Children: c2, c5, c6
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 5.2)

Theme of 1 communities and 27 files: unassigned files (27 files, rating 5.2).

- [unassigned files] `__init__.py` ranks 1 by PageRank, 0 importers, 0 symbols.
- [unassigned files] `client.go` ranks 2 by PageRank, 0 importers, 1 symbols.
- Key entities: file:scripts/doctor.py, file:enc_dec.go
- Children: c7
- Theme rating = highest child community rating.

## views: auth (`c0`, community, rating 7.0)

14 files under views (py 14), mostly presentation. Core file utils/utils.py (PageRank 0.0770, imported by 15 files): utils/utils.py Key abstractions: Payload, Config, database_path, as_bool, sanitize_path, load_payload. Depends on views: deniable_vault (2), utils (2), controllers (1). Used by views: facade (10), controllers (7), utils (5).

- `utils/utils.py` ranks 1 by PageRank, 15 importers, 8 symbols: utils/utils.py
- `models/user.py` ranks 2 by PageRank, 14 importers, 27 symbols: UserModel: Pydantic model for a user with Flask-Login support.
- `views/auth.py` ranks 3 by PageRank, 5 importers, 29 symbols: Authentication and account-management views.
- Hotspot `views/auth.py`: 29 symbols, 28 connections (score 0.25).
- Hotspot `models/user.py`: 27 symbols, 21 connections (score 0.22).
- 1 layer violations, e.g. test_utils.py (testing) -> utils.py (presentation).
- Taint: 6 paths reach this group via subprocess.
- Key entities: file:views/auth.py, file:models/user.py, file:controllers/auth.py, file:utils/utils.py, sym:models/user.py::get_user@454, file:models/plans.py, file:scripts/email_tool.py, sym:views/auth.py::role_required@71
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 23.

## static/js (`c2`, community, rating 6.4)

9 files under static/js (js 9), mostly utility. Core file static/js/qv-crypto.js (PageRank 0.0797, imported by 6 files): QuantumVault zero-knowledge browser crypto. Key abstractions: concatBytes, hexToBytes, bytesToHex, bytesToBase64, bytesToBase32, base64ToBytes. Depends on utils (1).

- `static/js/qv-crypto.js` ranks 1 by PageRank, 6 importers, 40 symbols: QuantumVault zero-knowledge browser crypto.
- `static/js/login.js` ranks 2 by PageRank, 1 importers, 2 symbols: Login page controller (zero-knowledge SRP-6a flow).
- `static/js/qv-padding.js` ranks 3 by PageRank, 1 importers, 5 symbols: QuantumVault fixed-bucket padding (QV-PAD-1), browser mirror of utils/padding.py.
- Hotspot `static/js/qv-crypto.js`: 40 symbols, 215 connections (score 0.84).
- Hotspot `static/js/account.js`: 9 symbols, 59 connections (score 0.22).
- Dependency cycle: qv-crypto.js -> register.js -> qv-crypto.js.
- Surprising bridge: contact.py <-> account.js (9 hops across communities).
- Key entities: file:static/js/qv-crypto.js, file:static/js/qv-deniable.js, file:static/js/account.js, file:static/js/messages.js, file:static/js/upload.js, file:static/js/qv-padding.js, file:static/js/register.js, file:static/js/recover.js
- Rating 6.4/10 = 7 x PageRank share 0.91 + 3 x risk 0.00. Internal imports: 10.

## unassigned files (`c7`, community, rating 5.2)

27 files under root (py 18, sh 5, go 3, js 1), mostly utility. Core file __init__.py (PageRank 0.0061, imported by 0 files). Key abstractions: main, deriveAESKey, encryptFile, decryptFile, main, derive_aes_key.

- `__init__.py` ranks 1 by PageRank, 0 importers, 0 symbols.
- `client.go` ranks 2 by PageRank, 0 importers, 1 symbols.
- `client.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `scripts/doctor.py`: 28 symbols, 13 connections (score 0.20).
- Hotspot `utils/srp6a.py`: 14 symbols, 6 connections (score 0.10).
- Taint: 3 paths reach this group via subprocess, urllib.request.
- Key entities: file:scripts/doctor.py, file:enc_dec.go, file:utils/srp6a.py, file:enc_dec.py, file:tests/test_doctor.py, file:tools/mutation_test.py, file:client.go, sym:scripts/doctor.py::collect_report@449
- Rating 5.2/10 = 7 x PageRank share 0.74 + 3 x risk 0.00. Internal imports: 0.

## views: facade (`c1`, community, rating 3.3)

11 files under views (py 11), mostly presentation. Core file app_factory.py (PageRank 0.0231, imported by 6 files): Application factory for QuantumVault. Key abstractions: create_app, load_user, GateOutcome, GateDecision, FacadeConfig, GatePhraseHasher. Depends on views: auth (10), views: deniable_vault (3), controllers (1). Used by views: deniable_vault (2), controllers (1).

- `app_factory.py` ranks 1 by PageRank, 6 importers, 8 symbols: Application factory for QuantumVault.
- `controllers/facade.py` ranks 2 by PageRank, 5 importers, 26 symbols: QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.
- `controllers/sync.py` ranks 3 by PageRank, 1 importers, 3 symbols: controllers/sync.py
- Hotspot `tests/test_facade.py`: 52 symbols, 10 connections (score 0.34).
- Hotspot `tests/test_cover.py`: 52 symbols, 7 connections (score 0.33).
- 8 layer violations, e.g. test_account_facade.py (testing) -> app_factory.py (presentation).
- Surprising bridge: facade.py <-> account.js (8 hops across communities).
- Key entities: file:tests/test_cover.py, file:tests/test_facade.py, file:app_factory.py, file:controllers/facade.py, sym:tests/test_cover.py::store@52, sym:app_factory.py::create_app@237, sym:controllers/facade.py::evaluate@359, file:views/facade.py
- Rating 3.3/10 = 7 x PageRank share 0.47 + 3 x risk 0.00. Internal imports: 13.

## utils (`c5`, community, rating 3.2)

8 files under utils (py 8), mostly presentation. Core file utils/padding.py (PageRank 0.0411, imported by 5 files): Fixed-bucket padding for metadata-size concealment (QV-PAD-1). Key abstractions: PaddingError, PaddingConfig, buckets_for, max_plaintext_bytes, config_from_env, cached_tables. Depends on views: auth (5). Used by views: auth (2), views: facade (1), static/js (1).

- `utils/padding.py` ranks 1 by PageRank, 5 importers, 13 symbols: Fixed-bucket padding for metadata-size concealment (QV-PAD-1).
- `utils/__init__.py` ranks 2 by PageRank, 3 importers, 0 symbols.
- `controllers/message.py` ranks 3 by PageRank, 2 importers, 4 symbols: Server-side controller for end-to-end encrypted messages.
- Hotspot `tests/test_padding.py`: 24 symbols, 11 connections (score 0.17).
- Hotspot `utils/padding.py`: 13 symbols, 12 connections (score 0.11).
- 2 layer violations, e.g. test_padding.py (testing) -> file.py (presentation).
- Taint: 1 paths reach this group via subprocess.
- Key entities: file:tests/test_padding.py, file:utils/padding.py, file:controllers/file.py, file:models/message.py, file:controllers/message.py, file:utils/scheduler.py, file:tests/test_srp.py, sym:utils/padding.py::pad@169
- Rating 3.2/10 = 7 x PageRank share 0.46 + 3 x risk 0.00. Internal imports: 9.

## views: deniable_vault (`c4`, community, rating 3.1)

8 files under tests (py 8), mostly presentation. Core file utils/security.py (PageRank 0.0429, imported by 8 files): Centralized security primitives for QuantumVault. Key abstractions: audit_event, constant_time_compare, hash_secret, verify_secret, new_one_time_code, json_csrf_protect. Depends on views: auth (3), views: facade (2). Used by views: facade (3), views: auth (2).

- `utils/security.py` ranks 1 by PageRank, 8 importers, 10 symbols: Centralized security primitives for QuantumVault.
- `models/deniable_vault.py` ranks 2 by PageRank, 3 importers, 6 symbols: Opaque storage for QV-DENIABLE-1 deniable vault containers.
- `controllers/deniable_vault.py` ranks 3 by PageRank, 2 importers, 22 symbols: QV-DENIABLE-1 deniable vault: configuration, validation, orchestration.
- Hotspot `tests/test_deniable_vault.py`: 55 symbols, 12 connections (score 0.36).
- Hotspot `controllers/deniable_vault.py`: 22 symbols, 14 connections (score 0.17).
- 5 layer violations, e.g. conftest.py (testing) -> app_factory.py (presentation).
- Taint: 1 paths reach this group via subprocess.
- Surprising bridge: deniable_vault.py <-> account.js (8 hops across communities).
- Key entities: file:tests/test_deniable_vault.py, file:controllers/deniable_vault.py, file:utils/security.py, sym:controllers/deniable_vault.py::validate@285, sym:utils/security.py::audit_event@86, file:tests/conftest.py, sym:tests/test_deniable_vault.py::_valid_envelope@71, file:models/deniable_vault.py
- Rating 3.1/10 = 7 x PageRank share 0.44 + 3 x risk 0.00. Internal imports: 10.

## controllers (`c3`, community, rating 2.3)

8 files under controllers (py 8), mostly presentation. Core file models/contact.py (PageRank 0.0147, imported by 1 files): ContactModel: Pydantic model for a contact message. Key abstractions: ContactModel, ContactDB, create_contact, get_user_contacts, get_all_contacts, UserEditForm. Depends on views: auth (7), views: facade (1). Used by views: auth (1), views: facade (1).

- `models/contact.py` ranks 1 by PageRank, 1 importers, 9 symbols: ContactModel: Pydantic model for a contact message.
- `views/admin.py` ranks 2 by PageRank, 7 importers, 19 symbols: UserEditForm: Form for editing user details.
- `controllers/contact.py` ranks 3 by PageRank, 2 importers, 4 symbols: ContactController: Handles logic related to contact messages.
- Hotspot `tests/test_secure_channel.py`: 67 symbols, 25 connections (score 0.47).
- Hotspot `controllers/secure_channel.py`: 37 symbols, 17 connections (score 0.27).
- 8 layer violations, e.g. test_bloque1.py (testing) -> user.py (presentation).
- Taint: 7 paths reach this group via subprocess.
- Dataflow: 3 INFERRED issues (first: UNCHECKED_ALLOC in test_env_template_documents_channel_keys).
- Key entities: file:tests/test_secure_channel.py, file:controllers/secure_channel.py, file:views/admin.py, sym:controllers/secure_channel.py::SecureChannelManager@220, file:models/contact.py, file:scripts/test_bloque1.py, file:models/superadmin_audit.py, sym:controllers/secure_channel.py::_status_for@337
- Rating 2.3/10 = 7 x PageRank share 0.33 + 3 x risk 0.00. Internal imports: 12.

## tools (`c6`, community, rating 1.2)

4 files under tools (py 4), mostly utility. Core file utils/integrity.py (PageRank 0.0185, imported by 4 files): Subresource Integrity manifest helpers (QV-SRI-1). Key abstractions: manifest_path, compute_sri, compute_file_sri, load_manifest, integrity_for, clear_manifest_cache. Depends on utils (1). Used by views: facade (1).

- `utils/integrity.py` ranks 1 by PageRank, 4 importers, 8 symbols: Subresource Integrity manifest helpers (QV-SRI-1).
- `tools/verify_build.py` ranks 2 by PageRank, 1 importers, 11 symbols: Verify reproducible builds and the fixed code contracts (QV-SRI-1).
- `tests/test_integrity.py` ranks 3 by PageRank, 0 importers, 6 symbols: Contract tests for SRI pins and reproducible builds (QV-SRI-1).
- Hotspot `tools/verify_build.py`: 11 symbols, 11 connections (score 0.10).
- Hotspot `utils/integrity.py`: 8 symbols, 11 connections (score 0.08).
- Taint: 2 paths reach this group via urllib.request.
- Key entities: file:tools/verify_build.py, file:utils/integrity.py, file:tools/generate_sri.py, file:tests/test_integrity.py, sym:tools/verify_build.py::check_template_references@110, sym:tools/generate_sri.py::main@81, sym:tools/verify_build.py::main@141, sym:utils/integrity.py::compute_sri@30
- Rating 1.2/10 = 7 x PageRank share 0.18 + 3 x risk 0.00. Internal imports: 4.
