# Disposable Secure Channels (QV-TUNNEL-1)

I run QuantumVault for people who cannot afford to be visible. A
long-lived domain is a long-lived identifier. Disposable channels
exist so an operator can publish the instance, serve high-risk users,
then destroy every public address and publish fresh ones.

## Design

Two backends, one supervisor, no host-wide side effects. The
inspiration is LazyOwn operator practice: a `cloudflared` quick
tunnel for reachability and a Tor onion service for anonymity. LazyOwn
runs both with interactive prompts, a shared system `torrc`, and sudo.
I kept the idea and removed the privilege: both backends run as
unprivileged child processes of the web worker, each confined to a
disposable directory under `QV_CHANNEL_STATE_DIR`.

Modes are `disabled`, `cloudflared`, `tor`, and `hybrid`. Hybrid runs
both at once. Rotation disposes both addresses together, so no single
address accumulates reputation.

## Security properties

- Loopback only. Both backends forward to `127.0.0.1` and the
  configured local port. No `0.0.0.0` listener is ever created.
- Closed URL allow-lists. Cloudflare output must match
  `https://<label>.trycloudflare.com` exactly. Onion hostnames must
  be v3 (`http://<56 base32>.onion`). Anything else aborts the start
  with `RuntimeError` and no state is persisted.
- No secrets in config. Quick tunnels need no account token and none
  is accepted. Tor uses a fresh data directory per start. No system
  `torrc` is touched and sudo is never required.
- Atomic owner-only state. The supervisor writes `state.json` through
  a temp file plus rename with mode `0600`. Pids of dead backends are
  pruned on read, so a crashed tunnel never reports as live.
- Redacted audit. The superadmin audit log records the mode plus
  truncated SHA-256 fingerprints of the addresses, never the
  addresses themselves. A stolen database does not hand over the
  current `.onion` or tunnel URL.

## Operation

Activation lives only in the superadmin panel. Three POST endpoints
sit under the existing per-boot superadmin token path, behind login,
the superadmin role, a 5 per minute limiter, and CSRF:

- `channel-start` with `mode` in `cloudflared`, `tor`, `hybrid`.
  Any other value is rejected.
- `channel-stop` disposes backends and removes state.
- `channel-rotate` republishes fresh addresses in the same mode.

The panel shows the live mode and both addresses when active, with
rotate and dispose buttons. When idle it shows a mode selector
defaulting to hybrid, plus a diagnostics table: each backend binary,
its configured and resolved path, a found/missing badge, the
loopback origin, the state directory, and the last backend log
lines. A start failure flashes the concrete reason (for example a
missing binary) and points at `make doctor-fix`.

Before first use, run `make doctor` on the server. It reports every
missing piece (system binaries, Python modules, Redis and Garage
reachability, channel backends) in plain English. `make doctor-fix`
installs what it can unattended: requirements, Debian packages,
cloudflared from the official Cloudflare release, and the garage
binary with checksum verification. It also pins the installed
cloudflared path into `.env` as `QV_CHANNEL_CLOUDFLARED_BIN` so the
panel finds it regardless of `PATH`. Anything left over (usually a
password-gated `sudo apt-get install` or a stopped Garage) is
printed as the exact command to run or the instruction to contact
the server administrator.

The origin scheme matters. The dev server speaks HTTPS on its
loopback port, while gunicorn behind a proxy usually speaks plain
HTTP. `QV_CHANNEL_LOCAL_SCHEME` must match reality: with `https`
the tunnel passes `--no-tls-verify` so the self-signed listener
stays reachable; with `http` it connects plainly. A mismatch
surfaces as Bad Gateway on an otherwise healthy tunnel URL.

The panel also probes the Garage S3 endpoint once per view before
building the encrypted-file inventory. When the object store is
down, every per-user listing would fail with retries, so the panel
skips the fan-out and renders an empty inventory instead of filling
the logs. The inventory returns on its own once Garage is back;
nothing needs to be restarted.

## Configuration

| Key | Default | Meaning |
| --- | --- | --- |
| `QV_CHANNEL_MODE` | `disabled` | Default mode selected at boot |
| `QV_CHANNEL_LOCAL_PORT` | `4443` | Loopback port both backends forward to |
| `QV_CHANNEL_LOCAL_SCHEME` | `http` | Origin scheme (`http` or `https`); use `https` for the TLS dev server |
| `QV_CHANNEL_CLOUDFLARED_BIN` | `cloudflared` | Backend binary name or absolute path |
| `QV_CHANNEL_TOR_BIN` | `tor` | Backend binary name or absolute path |
| `QV_CHANNEL_STATE_DIR` | `instance/secure_channels` | Disposable state and logs |
| `QV_CHANNEL_START_TIMEOUT` | `45` | Seconds to wait for URL or hostname |
| `QV_CHANNEL_TOR_SOCKS_PORT` | `0` | Reserved, stays disabled |

Binary resolution never trusts `PATH` alone for absolute candidates:
a path with a slash must exist as a file, otherwise start raises
instead of executing something unexpected.

## Failure modes

- Missing binary raises `RuntimeError` before any process spawns. The
  panel now shows which backend binary is missing and its configured
  path, and the failure flash carries the reason. If `cloudflared`
  is not on `PATH`, point `QV_CHANNEL_CLOUDFLARED_BIN` at its
  absolute path or use `tor` mode, which needs only the system `tor`.
- Bad Gateway on the tunnel URL means the tunnel is up but the
  origin refused the backend connection. The usual cause is a
  scheme mismatch: the dev server speaks HTTPS while the tunnel
  forwards plain HTTP. Set `QV_CHANNEL_LOCAL_SCHEME=https` (the
  tunnel then passes `--no-tls-verify` for the self-signed
  listener), restart the app, and rotate the channel. Behind
  gunicorn plain HTTP, leave the default `http`.
- No URL within the timeout raises `RuntimeError` with no state kept.
- Malformed persisted state reads as absent, never crashes status.
- `stop` always removes state and scratch dirs even when pids are
  already dead.
- `rotate` with no active channel raises `ValueError`.

## Verification

Behaviour contracts live in `tests/test_secure_channel.py` and
`tests/test_doctor.py`. The mutation harness reports zero survivors
for `controllers/secure_channel.py` and `controllers/facade.py`:

```bash
./.venv/bin/python -B tools/mutation_test.py \
  --targets controllers/secure_channel.py controllers/facade.py \
  --tests tests/test_secure_channel.py tests/test_facade.py
```
