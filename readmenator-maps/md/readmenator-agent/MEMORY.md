# Project Memory

> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. Section 7 is written by agents and humans and is preserved across rebuilds.

Generated from 88 files at commit `a556ec57e27f`. Read this first, then `readmenator-wiki/index.md`, then `readmenator . ask "<question>"` for anything specific.

## 1. Purpose and domain

- What it is: From the creators of LazyOwn Redteam Framework comes a free and open-source **Zero-knowledge, zero-trust, end-to-end encrypted messaging and file vault, secured with hybrid post-quantum cryptography.** (`README.md:12`)
- Domain vocabulary (term, files): `server` (37), `user` (33), `key` (30), `path` (30), `not` (29), `its` (28), `file` (27), `page` (26), `get` (25), `one` (25), `which` (24), `client` (23), `browser` (23), `build` (23), `without` (23)
- Subsystem `views: auth`: 14 files, core `views/auth.py`: Authentication and account-management views.
- Subsystem `views: facade`: 11 files, core `controllers/facade.py`: QV-FACADE-1 cover facade: configuration, gate hashing, tickets, gate control.
- Subsystem `static/js`: 9 files, core `static/js/qv-crypto.js`: QuantumVault zero-knowledge browser crypto.
- Subsystem `controllers`: 8 files, core `controllers/secure_channel.py`: QV-TUNNEL disposable secure channels over Cloudflare and Tor.
- Subsystem `views: deniable_vault`: 8 files, core `controllers/deniable_vault.py`: QV-DENIABLE-1 deniable vault: configuration, validation, orchestration.
- Subsystem `utils`: 8 files, core `utils/padding.py`: Fixed-bucket padding for metadata-size concealment (QV-PAD-1).
- Subsystem `tools`: 4 files, core `tools/verify_build.py`: Verify reproducible builds and the fixed code contracts (QV-SRI-1).
- Business rules that the code cannot show live in section 7: record them there.

## 2. Workflow

Detected commands:
- `python -m pytest -q` (tests/ layout)
- `make help` (Makefile)
- `make setup` (Makefile)
- `make venv` (Makefile)
- `make deps` (Makefile)
- `make env` (Makefile)
- `make compose-up` (Makefile)
- `make compose-down` (Makefile)
- `make garage-init` (Makefile)
- `make garage-status` (Makefile)
- `make garage-up` (Makefile)
- `make garage-down` (Makefile)

Session protocol:
1. Start: read this file, then `readmenator . fresh` (exit 1 means run `readmenator . --rebuild`).
2. Orient: `readmenator-wiki/index.md`; for a question use `readmenator . ask "<question>"` (local = entities + sources, `--global` = community reports).
3. Before editing a file: `grep -n '<file>' readmenator-agent/GOTCHAS.md readmenator-agent/SECURITY.md`.
4. After the change: run the tests above, then `readmenator . --rebuild` so the maps, wiki, and this file stay true.
5. End: record decisions, business rules, and gotchas with `readmenator . remember "<note>" --kind decision`.

## 3. Rules and constraints

Declared:
- English only. No emojis. In new code, no comments; use docstrings instead. (`CLAUDE.md:45`)
- Every public class, function, and module has a docstring. (`CLAUDE.md:46`)
- One file per contract. Each module owns exactly one responsibility. (`CLAUDE.md:47`)
- Apply DRY and SOLID. Unify duplication; depend on abstractions at layer (`CLAUDE.md:48`)
- No magic numbers and no hardcoded strings: configuration is centralized. (`CLAUDE.md:50`)
- No absolute system paths. Runtime paths derive from configuration (`CLAUDE.md:53`)
- Type hints everywhere. Immutable records use frozen dataclasses. (`CLAUDE.md:56`)
- Production quality only. No placeholders, no simplifications, no stubs. (`CLAUDE.md:57`)
- Prefer removing code over adding code. Dead code is deleted. (`CLAUDE.md:58`)
- Tests are behaviour contracts, not implementation mirrors. (`CLAUDE.md:59`)
- Never trust user input. Every value crossing a trust boundary is bounded, (`CLAUDE.md:66`)
- Secrets are never stored in plaintext. Passwords only derive keys; only (`CLAUDE.md:68`)
- Verification uses constant-time comparison. Authentication and gate paths (`CLAUDE.md:71`)
- Cover templates are hostile input. Rendering uses a Jinja sandbox with a (`CLAUDE.md:73`)
- The session is a server-side opaque identity behind a signed cookie. The (`CLAUDE.md:77`)
- Every state-changing request validates a CSRF token. (`CLAUDE.md:79`)
- Persistence is atomic and owner-only where the application manages files. (`CLAUDE.md:80`)
- Cryptographic material lengths are validated before use. Envelope tampering (`CLAUDE.md:81`)
- The application refuses to start in production without a stable (`CLAUDE.md:83`)
- Audit records for the facade are generic: a successful entry is (`CLAUDE.md:85`)

Measured baseline:
- Security findings at medium or above: 0 (see `readmenator-agent/SECURITY.md`); do not add new ones.
- Dependency cycles: 2; layer violations: 24 (see `readmenator-agent/GOTCHAS.md`).

## 4. Style norms

Declared:
- none declared in instruction files (add them to AGENTS.md or record them in section 7)

Measured baseline:
- py: 70 files, 718 symbols; docstrings on 63% of symbols; functions snake_case (100%); types PascalCase (100%); median file 130 lines, max 786.
- js: 10 files, 84 symbols; docstrings on 30% of symbols; functions camelCase (82%); median file 121 lines, max 749.
- sh: 5 files, 4 symbols; docstrings on 50% of symbols; functions snake_case (100%); median file 127 lines, max 289.
- go: 3 files, 7 symbols; docstrings on 0% of symbols; functions camelCase (57%); median file 102 lines, max 335.
- Tests: 16 files under scripts, tests, tools; follow the existing naming (e.g. `test_bloque1.py`).

## 5. Minimum deliverables

Declared:
- The behaviour is specified before it is implemented: the contract, inputs, (`CLAUDE.md:11`)
- Tests exist for the new behaviour and for the failure modes, written before (`CLAUDE.md:14`)
- Every test passes locally with `./.venv/bin/python -m pytest -q`. (`CLAUDE.md:16`)
- The mutation harness reports zero surviving mutants for the changed (`CLAUDE.md:17`)
- No security regression is introduced; every trust boundary still validates (`CLAUDE.md:19`)
- No dead code, duplicated logic, or spaghetti control flow is introduced. (`CLAUDE.md:21`)
- Duplicated logic found along the way is unified, even when it predates the (`CLAUDE.md:22`)
- Tests, README.md, docs/, and this file are updated to reflect the change. (`CLAUDE.md:24`)

Measured baseline:
- Tests pass: `python -m pytest -q`.
- Docstring coverage stays at or above 59%.
- No new security findings at medium or above (current: 0).
- No new dependency cycles (current: 2).
- Files stay under 300 lines where possible (`readmenator . lint`).
- Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.

## 6. Risks to respect

- God nodes (changes ripple widely): `app_factory.py`, `models/user.py`, `utils/utils.py`, `views/auth.py`, `views/admin.py`
- Hotspots (complex and central): `static/js/qv-crypto.js`, `tests/test_secure_channel.py`, `tests/test_deniable_vault.py`, `tests/test_facade.py`, `tests/test_cover.py`
- Cycle: `static/js/qv-crypto.js` -> `static/js/register.js` -> `static/js/qv-crypto.js`
- Cycle: `static/js/qv-crypto.js` -> `static/js/login.js` -> `static/js/qv-crypto.js`
- Full blast radius: `readmenator-agent/GOTCHAS.md`; findings: `readmenator-agent/SECURITY.md`.

## 7. Session log (preserved across rebuilds)

Append with `readmenator . remember "<note>" --kind <kind>` (kinds: business, decision, rule, workflow, style, deliverable, gotcha, todo, note) or the MCP tool `readmenator.remember`. Record business rules, decisions and their reasons, workflow changes, and anything the next session must not rediscover.

<!-- readmenator:memory:notes:begin -->
<!-- readmenator:memory:notes:end -->
