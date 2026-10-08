# controllers

*Community 3 | 8 files | cohesion 0.47*

## Definition

This community groups 8 file(s) rooted at `controllers` with dominant language py (cohesion 0.47). Central symbols: `ChannelMode`, `ChannelStatus`, `ContactController`, `ContactDB`, `ContactModel`, `PlanForm`, `SecureChannelConfig`, `SecureChannelManager`. Core file: `tests/test_secure_channel.py` (67 symbols). Documented purpose: Local development entry point.  This script exists for the ``make run`` workflow: the Werkzeug dev server with SSL on the loopback port. It is the only place in.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 2 | yes |
| `controllers/contact.py` | py | presentation | 4 | no |
| `controllers/secure_channel.py` | py | presentation | 37 | yes |
| `models/contact.py` | py | presentation | 9 | no |
| `models/superadmin_audit.py` | py | business_logic | 5 | yes |
| `scripts/test_bloque1.py` | py | testing | 8 | yes |
| `tests/test_secure_channel.py` | py | testing | 67 | yes |
| `views/admin.py` | py | presentation | 19 | no |

## Key Symbols

- `main` (function, `app.py:21`) `def main()`
- `_is_production_like` (function, `app.py:58`) `def _is_production_like()` - Return True if the runtime looks like a public-facing deployment.
- `ContactController` (class, `controllers/contact.py:4`) `class ContactController` - Handles logic related to contact messages.
- `__init__` (method, `controllers/contact.py:6`) `def __init__(self, db_path)` - Initialize the ContactController with the database path.
- `create_contact` (method, `controllers/contact.py:14`) `def create_contact(self, user_id, subject, message)` - Create a new contact message.
- `get_user_contacts` (method, `controllers/contact.py:36`) `def get_user_contacts(self, user_id)` - Retrieve all contact messages for a user.
- `ChannelMode` (class, `controllers/secure_channel.py:65`) `class ChannelMode(Enum)` - Selectable disposable channel mode.
- `parse` (method, `controllers/secure_channel.py:74`) `def parse(cls, raw)` - Parse free-form input into a mode, defaulting to disabled.
- `is_cloudflare_url` (method, `controllers/secure_channel.py:82`) `def is_cloudflare_url(value)` - Return whether value is a quick-tunnel HTTPS URL.
- `is_onion_url` (method, `controllers/secure_channel.py:89`) `def is_onion_url(value)` - Return whether value is a v3 onion HTTP address.
- `_as_port` (method, `controllers/secure_channel.py:96`) `def _as_port(value, default)` - Coerce input to a TCP port, falling back on default.
- `_as_scheme` (method, `controllers/secure_channel.py:107`) `def _as_scheme(value, default)` - Coerce input to an origin scheme, accepting http or https only.
- `SecureChannelConfig` (class, `controllers/secure_channel.py:116`) `class SecureChannelConfig` - Immutable secure channel configuration from env and mapping.
- `configured` (method, `controllers/secure_channel.py:129`) `def configured(self)` - Return whether a disposible channel mode is selected.
- `from_mapping` (method, `controllers/secure_channel.py:134`) `def from_mapping(cls, mapping, env)` - Resolve configuration with environment, mapping, then default order.
- `read` (method, `controllers/secure_channel.py:142`) `def read(key)`
- `ChannelStatus` (class, `controllers/secure_channel.py:174`) `class ChannelStatus` - Point-in-time view of disposable channel state.
- `active` (method, `controllers/secure_channel.py:184`) `def active(self)` - Return whether any backend address is currently published.
- `_default_launcher` (method, `controllers/secure_channel.py:193`) `def _default_launcher(cmd, log_path)` - Spawn a backend daemon detached from the web worker.
- `_default_killer` (method, `controllers/secure_channel.py:207`) `def _default_killer(pid)` - Terminate one tracked backend process group.
- `SecureChannelManager` (class, `controllers/secure_channel.py:220`) `class SecureChannelManager` - Supervise disposable Cloudflare and Tor backends.
- `__init__` (method, `controllers/secure_channel.py:223`) `def __init__(self, state_dir, local_port, local_scheme, cloudflared_bin, tor_bin` - Bind the manager to a state directory and backend binaries.
- `origin_url` (method, `controllers/secure_channel.py:247`) `def origin_url(self)` - Return the loopback origin URL both backends forward to.
- `from_config` (method, `controllers/secure_channel.py:252`) `def from_config(cls, config, launcher, killer)` - Build a manager sharing binary paths and ports with config.
- `status` (method, `controllers/secure_channel.py:270`) `def status(self)` - Return live status, pruning dead pids without side effects.
- `start` (method, `controllers/secure_channel.py:281`) `def start(self, mode)` - Start backends for mode, replacing any running channel.
- `stop` (method, `controllers/secure_channel.py:301`) `def stop(self)` - Terminate tracked backends and remove persisted state.
- `rotate` (method, `controllers/secure_channel.py:314`) `def rotate(self)` - Dispose current addresses and start the same mode again.
- `audit_details` (method, `controllers/secure_channel.py:321`) `def audit_details(self, action, mode, cloud_url, onion_url)` - Return an audit-safe detail string without full addresses.
- `_status_for` (method, `controllers/secure_channel.py:337`) `def _status_for(self, mode, cloud_url, onion_url, pids)` - Build a status after validating backend address shapes.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 12
- Cross-boundary resolved imports (EXTRACTED): 10

## Connections

- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: app.py imports app_factory.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: app.py imports utils/utils.py.
- [INFERRED] shares_context community 3 <-> 4 (strength 0.5): Inferred shared context (language py and layer presentation) with no import path between community 3 (controllers) and community 4 (views: deniable_vault).
- [INFERRED] shares_context community 3 <-> 5 (strength 0.5): Inferred shared context (language py and layer presentation) with no import path between community 3 (controllers) and community 5 (utils).
- [INFERRED] shares_context community 3 <-> 6 (strength 0.5): Inferred shared context (language py) with no import path between community 3 (controllers) and community 6 (tools).
- [INFERRED] shares_context community 3 <-> 7 (strength 0.5): Inferred shared context (language py) with no import path between community 3 (controllers) and community 7 (orphans).

## Risks

- [taint high] `controllers/secure_channel.py` -> `controllers/secure_channel.py` via `subprocess` (0 hops)
- [taint high] `tests/test_secure_channel.py` -> `tests/test_secure_channel.py` via `subprocess` (0 hops)
- [taint high] `tests/test_secure_channel.py` -> `views/admin.py` via `subprocess` (1 hops)
- [taint high] `tests/test_secure_channel.py` -> `controllers/secure_channel.py` via `subprocess` (1 hops)
- [taint high] `tests/test_secure_channel.py` -> `utils/utils.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/superadmin_audit.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `controllers/contact.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/user.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `views/auth.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/plans.py` via `subprocess` (2 hops)
- [taint high] `tests/test_secure_channel.py` -> `models/contact.py` via `subprocess` (3 hops)
- [taint high] `tests/test_secure_channel.py` -> `utils/mailer.py` via `subprocess` (3 hops)
- [taint high] `tests/test_secure_channel.py` -> `utils/security.py` via `subprocess` (3 hops)
- [taint high] `tests/test_secure_channel.py` -> `controllers/auth.py` via `subprocess` (3 hops)
- [taint high] `tests/test_secure_channel.py` -> `utils/__init__.py` via `subprocess` (4 hops)

## Open Questions

- Why do 3 file(s) lack file-level docs (e.g. `controllers/contact.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `controllers/secure_channel.py` still required, or can it be isolated?
- What would break if the most connected file in controllers changed?
- Should controllers be split, given cohesion 0.47?

## Sources

- `app.py`
- `controllers/contact.py`
- `controllers/secure_channel.py`
- `models/contact.py`
- `models/superadmin_audit.py`
- `scripts/test_bloque1.py`
- `tests/test_secure_channel.py`
- `views/admin.py`
