# Cover Facade and Two-Step Gate (QV-FACADE-1)

An operator-configurable disguise for a QuantumVault instance. When enabled, an
anonymous visitor never sees QuantumVault: the public pages are replaced by an
innocuous cover application selected from five built-in templates, or a custom
Jinja template the operator uploads. The real login is reached only through a
two-step gate. Step one is a secret phrase typed into the cover's form field; a
correct phrase reveals the ordinary login page. Step two is the existing
zero-knowledge SRP-6a login, where the account's real or duress credentials open
the real or the decoy content.

The feature exists because, for a user under surveillance or coercion, the most
dangerous signal is the mere presence of an encryption tool. A cover that looks
like a commonplace website removes that signal: an adversary who opens the site,
or who forces the user to open it, sees a search engine, not a vault.

## Threat model

The feature defends against an adversary who:

1. browses to the instance URL to learn what it is, or
2. coerces the user into opening the site ("show me what this is"), or
3. scans for well-known paths (`/login`, `/register`) to fingerprint the stack.

The guarantee is **concealment of the application's identity** to an
unauthenticated observer, plus a **duress path** that surfaces decoy content
under coercion. It is an obfuscation layer, not the cryptographic root of trust:
the zero-knowledge guarantees of SRP-6a, the hybrid post-quantum key exchange,
and the deniable vault stand on their own and do not depend on the facade. It
does **not** defend against an adversary who already holds valid gate and
account credentials, nor against traffic analysis of an instance whose URL is
already known to be QuantumVault.

## How the two steps compose with the deniable vault

The facade adds the outer door; the existing deniable vault (QV-DENIABLE-1)
provides the inner rooms. Together they deliver the full experience the user
asks for:

1. **Outer door (this contract).** The cover hides the app. A secret phrase in
   the search box is the first factor. A **real** phrase issues a ticket and
   marks the session `real`; a **duress** phrase issues a ticket and marks the
   session `duress`, and can raise a silent, generically named alert. Either
   phrase reveals the same ordinary login page, so an onlooker cannot tell which
   was used.
2. **Inner rooms (QV-DENIABLE-1).** After SRP-6a authentication the browser
   opens the deniable vault. Which slot decrypts is decided **client-side** by
   the passphrase the user types; the server never learns it. The session mode
   from step one (`qv_gate_mode`) is exposed to the front-end so the decoy slot
   can be preselected under duress, but the *content* selection remains in the
   browser.

This split is deliberate. Moving decoy-vs-real content selection to the server
would create a server-side record that a duress login occurred, which a seized
server could disclose. Keeping content selection client-side preserves the
zero-knowledge property: the silent alert is the only optional server-side
signal, and it is opt-in and generically named.

### The deniable passphrase is required

Enabling the facade means the deployment expects an outer cover plus an inner
deniable vault, so a second, independent (deniable) passphrase is required.
When the facade is enabled, the account page marks the second passphrase as
required and explains why. The check is a client-side UX guard: the server
exposes only the instance-level facade flag (`facade_enabled`) and never learns
whether a passphrase has been set, because the container is opaque and content
selection happens in the browser. A misspoken or coerced entry of the deniable
passphrase opens only the notes saved under it and reveals nothing about the
first set.

## No evidence: how concealment stays invisible

For concealment to hold, an unauthenticated observer must find nothing that
distinguishes a QuantumVault instance in facade mode from the cover application
it imitates. The design removes every such signal:

1. **Single endpoint, constant work.** Every submitted phrase reaches one
   handler that always performs the same Argon2id verification work, whether the
   phrase is a miss, the real phrase, or the duress phrase. A wrong phrase
   returns plausible cover results; there is no error, no redirect difference an
   observer can time into an oracle.
2. **Hidden pages.** With `QV_FACADE_HIDE_LOGIN=1` the human-facing pages
   (`/`, `/login`, `/register`, `/recover` by default) return the cover to any
   visitor without a valid ticket, so path scanning reveals only the cover.
3. **Cosmetic-only cover.** The cover's brand, title, and tagline are
   configuration, so each deployment can imitate a different commonplace site.
   Nothing in the cover names QuantumVault.
4. **Generic audit.** Every gate evaluation emits the same neutral `cover_query`
   event with no outcome field and no phrase, so a successful entry is
   indistinguishable in the log from a miss. The optional duress alert is a
   separate, generically named, opt-in event.
5. **No repository hint.** Gate phrases are never stored in the repository or in
   `payload.json`; the operator supplies an Argon2id hash via the environment.
6. **Fail-open on misconfiguration.** If facade mode is enabled but no gate hash
   is configured, the instance serves the normal app (still SRP-protected) and
   logs a warning, rather than locking every user — including the operator — out
   behind a door that can never open.

## Gate phrase storage and verification

A gate phrase is a human-chosen secret and may have low entropy, so it is
verified with **Argon2id**, not the fast peppered SHA-256 used for one-time
numeric codes. The operator generates the hash once and stores it in the
environment; the plaintext phrase never touches the server's disk.

```bash
python -m controllers.facade > /dev/null  # prints usage
python -c "from controllers.facade import GatePhraseHasher; \
import getpass; print(GatePhraseHasher.from_config(\
__import__('controllers.facade', fromlist=['FacadeConfig']).FacadeConfig()\
).hash(getpass.getpass('phrase: ')))"
```

The self-contained operator tool is simpler to invoke directly:

```bash
python controllers/facade.py    # reads the phrase from a no-echo prompt, prints the Argon2id hash
```

Set the printed value as `QV_FACADE_GATE_HASH` (and, optionally, a second phrase
as `QV_FACADE_DURESS_GATE_HASH`).

## Ticket protocol

A correct phrase issues a short-lived, signed ticket, stored in the session and
verified when the visitor reaches a protected page:

- **Signing:** `itsdangerous.URLSafeTimedSerializer` keyed by the app
  `SECRET_KEY`, with a fixed salt namespace. No new dependency: `itsdangerous`
  ships with Flask.
- **Payload:** only `{"m": "real" | "duress"}`. No username, no timestamp beyond
  the signer's own, nothing that identifies the account.
- **Expiry:** enforced by `max_age = QV_FACADE_TICKET_TTL_SECONDS` (default 120).
  An expired, tampered, or wrong-key ticket verifies to `None` and the visitor
  falls back to the cover.

## Components

| Layer    | File                        | Responsibility                                             |
| -------- | --------------------------- | ---------------------------------------------------------- |
| Config   | `controllers/facade.py`     | `FacadeConfig` limits and cosmetic cover parameters        |
| Hashing  | `controllers/facade.py`     | `GatePhraseHasher` Argon2id hash/verify of the gate phrase |
| Ticket   | `controllers/facade.py`     | `GateTicket` issue/verify of the signed, expiring ticket   |
| Control  | `controllers/facade.py`     | `FacadeGate` evaluate a phrase, emit generic audit         |
| Cover    | `controllers/cover.py`      | Five built-in templates, sanitization, sandboxed rendering |
| Store    | `controllers/cover.py`      | `CustomCoverStore` validated operator template uploads     |
| View     | `views/facade.py`           | Before-request cover gate, `POST /gate`, session mode      |

Cover rendering is sandboxed and self-contained; there is no separate
`templates/facade.html` file, because the cover source lives in the
catalog and the custom store so every cover is validated the same way.

## Configuration

All settings are configuration, not call-site constants. Defaults live in code
(`controllers/facade.py`) and are overridable per host via the matching
environment variable. Resolution order for every field is: environment variable,
then `app.config`, then the module default. Gate phrase hashes are intentionally
absent from `payload.json`.

| Environment variable               | Default    | Meaning                                             |
| ---------------------------------- | ---------- | --------------------------------------------------- |
| `QV_FACADE_ENABLED`                | `0`        | Master switch; `0` keeps the normal app unchanged   |
| `QV_FACADE_GATE_HASH`              | (empty)    | Argon2id hash of the real gate phrase               |
| `QV_FACADE_DURESS_GATE_HASH`       | (empty)    | Argon2id hash of the optional duress gate phrase    |
| `QV_FACADE_COVER_BRAND`            | `Findex`   | Cover brand name (cosmetic)                         |
| `QV_FACADE_COVER_TITLE`            | `Findex`   | Cover HTML title (cosmetic)                         |
| `QV_FACADE_COVER_TAGLINE`          | `Search the web` | Cover tagline (cosmetic)                      |
| `QV_FACADE_COVER_HEADLINE`         | `Findex`   | Cover headline (cosmetic)                           |
| `QV_FACADE_COVER_BODY`             | `Search the web for pages, images, and answers.` | Cover body text (cosmetic) |
| `QV_FACADE_COVER_FOOTER`           | `Findex is a free service.` | Cover footer text (cosmetic)           |
| `QV_FACADE_CONTACT_EMAIL`          | `support@example.org` | Cover contact email, validated          |
| `QV_FACADE_NEWSLETTER_LABEL`       | `Search`   | Cover form label (cosmetic)                         |
| `QV_FACADE_NEWSLETTER_ACTION`      | `Search`   | Cover form button text (cosmetic)                   |
| `QV_FACADE_COVER_TEMPLATE`         | `search_portal` | Built-in template id or `custom`              |
| `QV_FACADE_COVER_CUSTOM_TEMPLATE`  | (empty)    | File name of a custom template in the cover dir     |
| `QV_FACADE_COVER_DIR`              | `instance/cover_templates` | Directory of custom cover templates  |
| `QV_FACADE_GATE_FIELD`             | `q`        | Form field name carrying the gate phrase            |
| `QV_FACADE_TICKET_TTL_SECONDS`     | `120`      | Ticket lifetime in seconds                          |
| `QV_FACADE_MIN_PHRASE_LENGTH`      | `8`        | Phrases shorter than this are treated as a miss     |
| `QV_FACADE_MAX_PHRASE_LENGTH`      | `256`      | Phrases longer than this are treated as a miss      |
| `QV_FACADE_HIDE_LOGIN`             | `1`        | Replace public pages with the cover for anon users  |
| `QV_FACADE_PROTECTED_PATHS`        | `/,/login,/register,/recover` | Comma-separated pages hidden behind the gate |
| `QV_FACADE_DURESS_ALERT`           | `0`        | Emit a silent, generic alert on a duress entry      |
| `QV_FACADE_ARGON2_TIME_COST`       | `3`        | Argon2id time cost                                  |
| `QV_FACADE_ARGON2_MEMORY_COST`     | `65536`    | Argon2id memory cost (KiB)                          |
| `QV_FACADE_ARGON2_PARALLELISM`     | `4`        | Argon2id parallelism                                |

## Tests

- `tests/test_facade.py`: config resolution and env/mapping precedence, Argon2id
  hash/verify, ticket issue/verify/expiry/tamper, gate evaluation for miss, real,
  and duress phrases, audit redaction, fail-open on misconfiguration, and the
  HTTP cover/gate flow (concealment, phrase submission, redirect to the real
  login, authenticated bypass, backward compatibility when disabled).
- `tests/test_cover.py` (QV-FACADE-2): the five-template catalog, variable
  sanitization and bounds, autoescaping and rejection of scripts and forbidden
  Jinja constructs, the custom template store (extension, size, path-traversal,
  and validation), the cover service selection and fail-open fallback, and the
  HTTP flow for a configured template.

## Mutation testing

```
make mutate
```

or directly:

```
./.venv/bin/python -B tools/mutation_test.py
```

The harness mutates comparison, boolean, and keyword tokens in
`controllers/facade.py` and `controllers/cover.py`, runs the suite for each
mutant, and reports killed and survived mutants. A surviving mutant indicates a
gap in the tests. The harness runs with `-B` and purges bytecode caches so a
restored source is always reloaded instead of a stale `.pyc` compiled from a
mutant.

