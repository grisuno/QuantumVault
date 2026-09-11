# QuantumVault Engineering Contract

This file is the binding contract for all work in this repository. It is read by
every contributor and every agent before changing code. It supersedes
convenience, speed, and personal preference.

## Definition of Done

A change is done only when every item below is true.

1. The behaviour is specified before it is implemented: the contract, inputs,
   outputs, and failure modes are written down first (in this file, in
   `docs/`, or in the test that encodes them).
2. Tests exist for the new behaviour and for the failure modes, written before
   or with the implementation.
3. Every test passes locally with `./.venv/bin/python -m pytest -q`.
4. The mutation harness reports zero surviving mutants for the changed
   contracts when the change touches the facade or cover modules.
5. No security regression is introduced; every trust boundary still validates
   input.
6. No dead code, duplicated logic, or spaghetti control flow is introduced.
7. Duplicated logic found along the way is unified, even when it predates the
   task.
8. Tests, README.md, docs/, and this file are updated to reflect the change.

## Methodology

The workflow is spec-driven development plus test-driven development plus
behaviour-driven development, followed by mutation testing.

1. Specify. Capture the contract and the edge cases in this file, in `docs/`,
   or in the test that encodes them.
2. Red. Write a failing test that describes the required behaviour.
3. Green. Implement the smallest change that satisfies the contract.
4. Refactor. Remove duplication and improve structure without changing
   behaviour.
5. Mutate. Run `make mutate` (or `./.venv/bin/python -B tools/mutation_test.py`).
   A surviving mutant means a missing test and must be fixed by strengthening
   the test, never by weakening or excluding the mutant, unless the mutant is
   provably equivalent, in which case the equivalent construct must be removed
   from the source.

## Code rules

- English only. No emojis. In new code, no comments; use docstrings instead.
- Every public class, function, and module has a docstring.
- One file per contract. Each module owns exactly one responsibility.
- Apply DRY and SOLID. Unify duplication; depend on abstractions at layer
  boundaries.
- No magic numbers and no hardcoded strings: configuration is centralized.
  New facade and cover settings live in their `Config` records and are
  overridable through the environment.
- No absolute system paths. Runtime paths derive from configuration
  (`SQLALCHEMY_DATABASE_PATH`, `QV_UPLOAD_FOLDER`, `QV_FACADE_COVER_DIR`),
  never from a hard-coded location.
- Type hints everywhere. Immutable records use frozen dataclasses.
- Production quality only. No placeholders, no simplifications, no stubs.
- Prefer removing code over adding code. Dead code is deleted.
- Tests are behaviour contracts, not implementation mirrors.

## Security invariants

These invariants must never be violated. Fixing a violation is never out of
scope.

1. Never trust user input. Every value crossing a trust boundary is bounded,
   canonicalized, and stripped of control and spoofing characters.
2. Secrets are never stored in plaintext. Passwords only derive keys; only
   Argon2id-hashed or wrapped material is persisted. Gate phrases are stored
   as Argon2id hashes in the environment, never in the repository.
3. Verification uses constant-time comparison. Authentication and gate paths
   perform the same work regardless of which credential is supplied.
4. Cover templates are hostile input. Rendering uses a Jinja sandbox with a
   closed variable allow-list and autoescaping; imports, includes, extends,
   macros, attribute traversal, scripts, event handlers, external form
   actions, and embeds are rejected before rendering.
5. The session is a server-side opaque identity behind a signed cookie. The
   facade ticket carries only `real` or `duress`, never an account identity.
6. Every state-changing request validates a CSRF token.
7. Persistence is atomic and owner-only where the application manages files.
8. Cryptographic material lengths are validated before use. Envelope tampering
   and version downgrade raise typed errors.
9. The application refuses to start in production without a stable
   `FLASK_SECRET_KEY`; the server never exposes a Werkzeug debug PIN.
10. Audit records for the facade are generic: a successful entry is
    indistinguishable from a miss, and no phrase is ever logged.

## Facade and cover contract (QV-FACADE-1, QV-FACADE-2)

- The facade is enabled only when both `enabled` and a gate hash are present;
  otherwise the instance fails open to the ordinary application.
- Anonymous visitors to the protected paths see the cover; an authenticated
  user bypasses it; a valid ticket reveals the ordinary login.
- The cover is chosen from five built-in templates or a validated custom
  template. Every cover variable is sanitized and bounded; the contact email
  is validated.
- A correct real phrase issues a `real` ticket; a correct duress phrase issues
  a `duress` ticket, optionally emitting a single generically named audit
  event. A miss issues nothing.
- When the facade is enabled, the account page requires a second (deniable)
  passphrase for the deniable vault. The server exposes only the instance-level
  facade flag and never learns whether a passphrase is set, because selection
  stays client-side.
- The zero-knowledge guarantees of SRP-6a, the hybrid post-quantum key
  exchange, and the deniable vault stand on their own and do not depend on the
  facade.

## Layering

`views` (HTTP) depend on `controllers` and `models`; `controllers` depend on
`models` and `utils`; `models` depend on `utils`. No lower layer may import a
higher layer. Cross-cutting security primitives live in `utils/security.py`.

## Commands

- Run tests: `./.venv/bin/python -m pytest -q`
- Run mutation testing: `make mutate` or
  `./.venv/bin/python -B tools/mutation_test.py`
- List mutants without running:
  `./.venv/bin/python -B tools/mutation_test.py --list`
