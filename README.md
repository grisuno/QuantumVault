
# QuantumVault

<img width="1882" height="979" alt="image" src="https://github.com/user-attachments/assets/0a8b4d20-e00a-45f1-8b62-c0e609abf6a8" />


<img width="1882" height="979" alt="image" src="https://github.com/user-attachments/assets/aa1af1aa-9be4-4d56-a67f-9b1fa3f02287" />


<img width="1882" height="979" alt="image" src="https://github.com/user-attachments/assets/e8f11d33-85ba-4123-b31c-d70a08d7454b" />

**Zero-knowledge, zero-trust, end-to-end encrypted messaging and file vault, secured with hybrid post-quantum cryptography.**

QuantumVault is free and open-source software released under the **GNU Affero General Public License v3.0 (AGPLv3)**.

## Mission

LazyOwn RedTeam released QuantumVault as free software so that journalists, activists, and ordinary people can communicate with hybrid post-quantum end-to-end encryption, free from surveillance, censorship, or any single point of control over their right to private communication and free expression.

We hope you put it to good use.

LazyOwn RedTeam is a security research and offensive security collective. We spend our time finding the gaps that surveillance, censorship, and authoritarian control exploit, and we know how often ordinary people, journalists, activists, and dissidents are left without tools they can actually trust. Rather than keep this technology behind a paywall or a closed SaaS, we are releasing QuantumVault to the public so that anyone, an independent newsroom, an NGO, a community group, or an individual, can deploy their own instance, inspect every line of code, modify it, and run it under their own infrastructure and their own responsibility.


## What QuantumVault Does

- **Deniable Vault (VeriCrypt)**: Plausibly deniable encrypted storage con outer/inner volumes.
- **Encrypt and store files** client-side before they ever leave the user's device, then store them as opaque ciphertext on the server.
- **Exchange end-to-end encrypted messages** sealed with a hybrid post-quantum key exchange so that only the sender and the intended recipient can ever read them.
- **Authenticate without ever sending a password**, using SRP-6a, a zero-knowledge password proof.
- **Recover a forgotten password without a server-side reset**, using a one-time recovery code generated in the browser at registration.
- **Resist quantum and classical attacks alike**, since breaking the hybrid construction requires breaking both the post-quantum and the classical primitive.

### Zero-Knowledge, Zero-Trust by Design

"Zero-knowledge" means the server storing data never has access to plaintext, private keys, or passwords, not as a policy promise, but because the cryptography makes it structurally impossible. "Zero-trust" means operators do not need to be trusted to keep that promise: the source code can be read, the cryptographic primitives verified, and the protections confirmed directly.

The architecture is intentionally hybrid: communications are relayed and encrypted blobs are stored through a central server for convenience and reachability, but that server is reduced to a transport and storage layer. It never holds the keys needed to read what passes through it.

## Cryptography

All cryptographic operations that matter, key generation, encryption, and decryption, happen **in the browser**, using vendored, audit-friendly cryptographic libraries (`static/js/vendor/`, `static/js/qv-crypto.js`).

| Purpose | Primitive |
| --- | --- |
| Post-quantum key encapsulation | **ML-KEM-768** (FIPS 203) |
| Classical key exchange | **X25519** (Curve25519 ECDH) |
| Hybrid key wrapping | ML-KEM-768 + X25519, combined |
| Key derivation | **HKDF-SHA256** |
| Symmetric encryption | **AES-256-GCM** |
| Authentication | **SRP-6a** (zero-knowledge password proof, password never leaves the client) |
| Account recovery | **QV-RECOVERY-1** (160-bit recovery code, independently re-wraps the existing private key blob) |

The hybrid construction means that an attacker would need to break **both** ML-KEM-768 and X25519 to recover a user's keys, today or with a future quantum computer.

### Account recovery (QV-RECOVERY-1)

Because the server never has the password or the private key, a forgotten
password cannot be reset the way a traditional service would. Instead, at
registration the browser generates a 20-byte (160-bit) recovery code,
displayed once as 8 groups of 4 characters (e.g.
`ABCD-EFGH-JKMN-...`), and uses it to independently encrypt the same
private-key blob that the password protects. The recovery code is never
sent to or stored on the server, only the resulting ciphertext and its
salt.

To recover an account, visit `/recover`, enter the username, the
recovery code, and a new password. The browser fetches the stored
ciphertext, decrypts it locally with a key derived from the recovery
code, proves to the server that the decryption succeeded (by
reconstructing the account's public key from the recovered blob), and
then re-wraps the same private key under the new password. The
underlying keypair never changes, so previously stored messages and
files remain decryptable.

**The recovery code is shown exactly once**, in a one-time dialog right
after registration. If it is lost and the password is also forgotten,
the account's encrypted data cannot be recovered by anyone, including
the operator: this is a direct consequence of the zero-knowledge design,
not a missing feature.

## Architecture and Stack

| Layer | Technology |
| --- | --- |
| Web framework | Flask 3 (`app_factory.py`, `wsgi.py`) |
| Authentication / sessions | Flask-Login, SRP-6a session store backed by Redis |
| Forms / CSRF | Flask-WTF, WTForms |
| Security headers | Flask-Talisman |
| Rate limiting | Flask-Limiter |
| Database | SQLite (`instance/users.db`) via SQLAlchemy models (`models/`) |
| Object storage | [Garage](https://garagehq.deuxfleurs.fr/) (self-hosted, S3-compatible) |
| Cache / ephemeral state | Redis |
| Email | Flask-Mail (AWS SES or SMTP) |
| SMS / MFA | ClickSend |
| Production server | Gunicorn |
| Client-side cryptography | Vendored JS: ML-KEM-768, X25519/Ed25519, HKDF, SHA-2/SHA-3, WebCrypto AES-GCM |

## Requirements

- Python 3.10+
- `python3-venv`
- Docker and Docker Compose (recommended), or a manually managed Redis instance and Garage instance
- `openssl` (for local TLS certificates and secret generation)

QuantumVault's server side does not require `liboqs` or any native post-quantum library: all post-quantum and classical cryptography runs client-side in the browser via the vendored JavaScript modules in `static/js/vendor/`. No server-side post-quantum library installation is needed to run the application.

## Quick Start

```bash
git clone https://github.com/grisuno/QuantumVault.git
cd QuantumVault

# One-shot setup: creates the virtualenv, installs Python dependencies,
# generates .env from .env.example, and (if Docker is available) brings
# up Garage + Redis and bootstraps the storage bucket.
make setup

# Start the Flask app in the foreground (dev mode, TLS on the loopback port)
make run
```

By default the app listens on `https://0.0.0.0:4443`.

If `make run` reports missing TLS material, generate a self-signed certificate:

```bash
openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365 -subj '/CN=localhost'
```

### Running Without Docker

If Docker is not available, install dependencies and bring up the dependencies natively:

```bash
make venv         # create the virtualenv
make deps         # install Python dependencies
make env          # create .env from .env.example and generate Garage tokens
make redis-up     # start a local Redis instance
make garage-up    # download, run, and provision Garage natively
make run-local    # start the Flask app
```

### Production

Production deployments use Gunicorn against the WSGI entry point (`wsgi.py`). A reverse proxy in front should terminate TLS and forward to the bound port.

```bash
make serve
```

## Configuration

Configuration lives in `.env` (copy from `.env.example`, generated automatically by `make env`). Key settings:

- **Object storage (Garage / S3)**: `S3_ENDPOINT_URL`, `S3_ACCESS_KEY`, `S3_SECRET_KEY`, `S3_BUCKET`, `S3_REGION`
- **Session store / rate limiting**: `STORAGE_URI` (Redis URL)
- **Mail**: `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USE_SSL`, `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_DEFAULT_SENDER`. Supports AWS SES or any SMTP provider, including Gmail with an App Password. If left empty, the app skips sending mail and logs the confirmation link instead, recoverable with `python scripts/email_tool.py link <username>`.
- **SMS / MFA (ClickSend)**: `CLICKSEND_USERNAME`, `CLICKSEND_API_KEY`. Leave blank to skip SMS in development.
- **Garage admin / RPC**: `GARAGE_ADMIN_TOKEN`, `GARAGE_RPC_SECRET`, `GARAGE_KEY_NAME`, `GARAGE_ADMIN_URL`
- **Flask**: `FLASK_DEBUG`
- **Feature flags**: `QV_ENABLE_SUBSCRIPTIONS` (default `1`) — set to `0` to disable the paid-plans blueprint and nav link for operators who only want the free, self-hosted core.
- **Privacy hardening**: `QV_AUDIT_LOG_IP`, `QV_AUDIT_LOG_UA` (both default `1`), `QV_TRUSTED_PROXY` (default `0`). See "Running for high-risk users (Tor)" below.

### Running for high-risk users (Tor)

QuantumVault's zero-knowledge cryptography already keeps message/file
content, private keys, and passwords away from the server. The settings
below additionally reduce the *operational metadata* an instance retains,
for operators serving journalists, activists, or anyone else whose safety
depends on minimizing what a compromised or subpoenaed server can reveal:

- Set `QV_AUDIT_LOG_IP=0` and `QV_AUDIT_LOG_UA=0` so the structured audit
  log (`utils/security.py` `audit_event`) records `ip` and `ua` as `null`
  instead of the requester's address and User-Agent string. The audit log
  still records timestamps, event names, and correlation IDs, so abuse
  patterns remain visible without storing identifying details.
- Leave `QV_TRUSTED_PROXY` unset (or `0`). This setting is for operators
  who run their own reverse proxy in front of gunicorn and want
  `X-Forwarded-For` honored; behind Tor, the address Tor presents is not a
  meaningful client identifier, so there is nothing to "trust" and the
  default (use the directly-connecting socket address) is correct.
- Serve the instance as a Tor onion service by pointing a `HiddenServicePort`
  in `torrc` at the port gunicorn binds to (see `make serve` /
  `wsgi.py`). No application code changes are needed — Tor handles
  the `.onion` address and end-to-end transport encryption; QuantumVault's
  own TLS/HSTS settings (`_build_talisman_kwargs` in `app_factory.py`) can
  remain as configured for the clearnet listener, if any, or be left at
  their defaults for an onion-only deployment reached over Tor's own
  encrypted circuits.
- Standard web server access logs (nginx/gunicorn) are outside
  QuantumVault's control; disable or rotate them aggressively at the
  reverse-proxy layer if they are not needed, since they can record client
  addresses independently of the application's own audit log.

## Common Make Targets

Run `make help` to list all available targets. The most relevant ones:

| Target | Description |
| --- | --- |
| `make setup` | First-time setup: virtualenv, dependencies, `.env`, and (if Docker is present) Garage + Redis |
| `make run` | Run the Flask app in the foreground, starting Docker Compose or a local Redis/Garage as needed |
| `make run-local` | Run Flask without touching Docker (manage Redis/Garage yourself) |
| `make serve` | Run Gunicorn against the production WSGI module |
| `make stop` | Stop the dev app, Docker Compose stack, and any Redis/Garage started by `make run` |
| `make compose-up` / `make compose-down` | Bring the Garage + Redis Docker Compose stack up or down |
| `make garage-up` / `make garage-down` | Run Garage natively without Docker |
| `make redis-up` / `make redis-down` / `make redis-status` | Manage a native Redis instance |
| `make db-reset` | Wipe the development SQLite database |
| `make backupdb` | Snapshot `instance/users.db` to `backups/` |
| `make doctor` | Import-smoke test of every project module to report missing dependencies |
| `make test` | Run the pytest suite (SRP-6a roundtrip, audit-log redaction, CSRF helper tests) |
| `make audit` | Run the security audit stack: `pip-audit` + `bandit` + secret scanning |
| `make pip-audit` | Check the dependency tree for known vulnerabilities |
| `make bandit` | Static security scan of the Python codebase |
| `make semgrep` | Run Semgrep rules against crypto anti-patterns in the codebase |
| `make upgrade-deps` | Refresh the virtualenv to match `requirements.txt` and regenerate `requirements.lock` |
| `make clean` | Remove caches and build artifacts (keeps `.env` and `instance/users.db`) |

## Self-Hosting and AGPLv3

Because QuantumVault is licensed under AGPLv3, anyone running a modified version of it as a network service must make the corresponding source code available to its users. This keeps every deployment auditable.

Each instance of QuantumVault is operated independently by whoever deploys it. LazyOwn RedTeam provides the software, not a hosted service, and does not control or have visibility into independently operated instances.

## License

QuantumVault is released under the **GNU Affero General Public License v3.0 (AGPLv3)**. See the `LICENSE` file for the full text.

---

**QuantumVault: free software, post-quantum encryption, for a free press and free expression.**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)
