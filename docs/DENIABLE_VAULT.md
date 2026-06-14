# Deniable Vault (QV-DENIABLE-1)

A self-service feature, available to every authenticated role (free through
superadmin), that lets a user store notes behind a passphrase, with optional
plausible deniability: a second, independent passphrase reveals a different set
of notes. Under coercion the user can disclose one passphrase; the existence of
the other cannot be proven. It is the production implementation of the
proof-of-concept deniable container, adapted to QuantumVault's zero-knowledge
architecture.

It is reached from the **Account Settings** page (a normal, universal part of
every account), not from a dedicated menu item, and it is presented as ordinary
"secure notes". Advertising it as a deniable vault would defeat the purpose:
deniability only protects the user if its presence is not obvious.

## Threat model

The feature defends against an adversary who can either:

1. read the server's database (a dump, a backup, a subpoena), or
2. coerce the user into revealing a passphrase ("rubber-hose" disclosure).

The guarantee is **plausible deniability**: neither adversary can *prove* that a
second (hidden) set of notes exists. It does **not** defend against an adversary
who controls the user's browser while it is in use, nor does it recover data if
a passphrase is forgotten.

## No evidence: how activation stays invisible

For the guarantee to hold there must be no signal — anywhere — that
distinguishes a user who activated a hidden set of notes from one who did not.
The design removes every such signal:

1. **Universal containers.** Every account has exactly one container. The
   server mints a well-formed *random* one on first access
   (`DeniableVaultConfig.random_container`), because the blob is opaque and
   AES-GCM ciphertext is indistinguishable from random. "Has a container" is
   therefore true for everyone and proves nothing. Activation only overwrites
   the random blob with one a passphrase can open.
2. **Fixed size.** Every slot's plaintext is padded to a fixed length
   (`slot_plaintext_bytes`), so every slot's ciphertext — and therefore every
   container — is exactly the same size, whether or not it hides data.
3. **No status.** The API never returns a "configured" flag, and the UI never
   shows one. Opening with a wrong passphrase and opening an unused slot are
   indistinguishable: both simply return no notes.
4. **No admin view.** There is no operator count or per-user indicator of
   deniable-vault usage.
5. **Generic audit.** Provisioning, activation, and reset all emit the same
   neutral `account_object_write` event with only the username — never the
   feature name, the slot, or any ciphertext.
6. **No repository hint.** The structural parameters are not written to
   `payload.json`; defaults live in code and are overridable only via the
   environment.

## Cryptography and "post-quantum"

All key derivation, encryption, and decryption happen in the browser. The
server never receives a passphrase or any plaintext, and it stores only opaque
ciphertext (never plaintext, and never in `payload.json`).

- **KDF:** PBKDF2-SHA256, iteration count advertised by the server
  (`min_kdf_iterations`, default 600,000), with a per-slot 16-byte random salt.
- **Cipher:** AES-256-GCM with a per-slot 12-byte random nonce.

This construction is **post-quantum secure by design**: it uses no public-key
cryptography. A deniable vault is unlocked by a passphrase, not by a keypair, so
there is no ML-KEM/X25519 key exchange to attack. AES-256 and SHA-256 retain
128-bit security against Grover's algorithm, which is the post-quantum bar.
Adding ML-KEM here would be cryptographically meaningless — it solves key
exchange, a problem this feature does not have. The data is therefore stored
encrypted post-quantumly in the database, satisfying the at-rest requirement
without a public-key layer.

## Envelope schema

The opaque container the browser produces and the server stores verbatim:

```json
{
  "v": 1,
  "kdf": "PBKDF2-SHA256",
  "iterations": 600000,
  "slots": [
    { "salt": "<32 hex>", "nonce": "<24 hex>", "ct": "<base64, fixed length>" },
    { "salt": "<32 hex>", "nonce": "<24 hex>", "ct": "<base64, fixed length>" }
  ]
}
```

The server validates this structure only; it never decodes a `ct`. Every `ct`
must be exactly `expected_ct_b64_length` characters, so all containers are the
same size.

## Components

| Layer    | File                                   | Responsibility                                       |
| -------- | -------------------------------------- | ---------------------------------------------------- |
| Model    | `models/deniable_vault.py`             | Opaque per-user container storage                    |
| Config   | `controllers/deniable_vault.py`        | `DeniableVaultConfig` limits + random container mint |
| Validate | `controllers/deniable_vault.py`        | `EnvelopeValidator` structure-only checks            |
| Control  | `controllers/deniable_vault.py`        | `DeniableVaultController` provision/validate/store    |
| View     | `views/account.py`                     | Settings page + `GET/PUT/DELETE /api/account/vault`  |
| Browser  | `static/js/qv-deniable.js`             | Build and open containers                            |
| Browser  | `static/js/account.js`                 | Settings page controller                             |
| Template | `templates/account.html`               | Account settings UI (secure notes)                   |

## Configuration

All structural limits are configuration, not call-site constants. Defaults live
in code (`controllers/deniable_vault.py`); each can be overridden per-host via
the matching environment variable. They are intentionally absent from
`payload.json`.

| Environment variable                    | Default         | Meaning                              |
| --------------------------------------- | --------------- | ------------------------------------ |
| `DENIABLE_VAULT_SCHEMA_VERSION`         | `1`             | Required envelope `v`                |
| `DENIABLE_VAULT_SLOT_COUNT`             | `2`             | Exact number of slots               |
| `DENIABLE_VAULT_SALT_HEX_LENGTH`        | `32`            | Per-slot salt length, hex chars     |
| `DENIABLE_VAULT_NONCE_HEX_LENGTH`       | `24`            | Per-slot nonce length, hex chars    |
| `DENIABLE_VAULT_MIN_KDF_ITERATIONS`     | `600000`        | Minimum accepted PBKDF2 iterations  |
| `DENIABLE_VAULT_MAX_KDF_ITERATIONS`     | `10000000`      | Maximum accepted PBKDF2 iterations  |
| `DENIABLE_VAULT_ALLOWED_KDF`            | `PBKDF2-SHA256` | Comma-separated KDF allow-list      |
| `DENIABLE_VAULT_SLOT_PLAINTEXT_BYTES`   | `65536`         | Fixed per-slot plaintext size       |
| `DENIABLE_VAULT_MAX_ENVELOPE_BYTES`     | `4000000`       | Upper bound on canonical envelope   |

## Tests

- `tests/test_deniable_vault.py`: config resolution, validator invariants,
  random-container provisioning, storage round-trip, controller behavior, audit
  redaction, and the HTTP API (auth gating, CSRF, validation, per-user
  scoping).
- `scripts/verify_deniable_crypto.mjs`: browser crypto round-trip and the
  fixed-size invariants. Run all browser-crypto specs with `make verify-crypto`.
