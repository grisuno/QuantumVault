# `models.superadmin_audit`

> Source: [models/superadmin_audit.py:1](../../models/superadmin_audit.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Append-only audit log for superadmin actions.

Why a separate table: every privileged action (MFA reset, confirmation
token re-issue, account suspension) needs an immutable record of who
did what to which user, from which IP, and when. Mixing this into the
``users`` table is wrong on two counts:

1. The audit row is written by the superadmin, not the affected user.
   Adding ``last_reset_by`` / ``last_reset_at`` columns to ``users``
   would let an attacker who pwns the DB forge the trail.

2. Audit history is monotonic: an entry must never be UPDATEd or
   DELETEd. SQLite has no row-level immutability, but a dedicated
   table with no application code path that writes UPDATEs is the
   closest we can get.

The table lives in ``instance/users.db`` (same file as ``users``) to
keep operator backup / restore symmetric: one file = one snapshot of
identity state. Storage is bounded by the operational tempo of the
superadmin role, not user activity, so growth is negligible.

Rows are never pruned by the application. If a future retention policy
is needed it should be a documented operator script, not a silent
DELETE in the request path.

## Contents

- **Classes:** [`SuperadminAuditDB`](#superadminauditdb)

## Classes

<a id="superadminauditdb"></a>

### `SuperadminAuditDB`

`class` | [models/superadmin_audit.py:32](../../models/superadmin_audit.py#L32)

```python
class SuperadminAuditDB
```

Database operations for the superadmin audit log.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#superadminauditdb-__init__) | constructor | Initialize the audit log and ensure its table exists. |
| [`record`](#superadminauditdb-record) | method | Append one audit row and return its id. |
| [`recent`](#superadminauditdb-recent) | method | Return the most recent ``limit`` audit rows, newest first. |

<a id="superadminauditdb-__init__"></a>

#### `SuperadminAuditDB.__init__`

`constructor` | [models/superadmin_audit.py:35](../../models/superadmin_audit.py#L35)

```python
def __init__(self, db_path: str)
```

Initialize the audit log and ensure its table exists.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `db_path` | `str` |  | Path to the SQLite database file (shared with `[`UserDB`](models.user.py.md#userdb)` so the two are backed up together). |

*Called by:* [`superadmin`](views.admin.py.md#superadmin)

<a id="superadminauditdb-record"></a>

#### `SuperadminAuditDB.record`

`method` | [models/superadmin_audit.py:75](../../models/superadmin_audit.py#L75)

```python
def record(self, actor: str, action: str, target_user: Optional[str] = None, ip: Optional[str] = None, details: Optional[str] = None) -> int
```

Append one audit row and return its id.

The timestamp is generated server-side in UTC so two operators
in different timezones can correlate a single incident. The
return value is the new row's primary key, useful for tests
and for linking related log lines in the response.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `actor` | `str` |  | Username of the superadmin performing the action. |
| `action` | `str` |  | Short verb-noun identifier (e.g. ``reset_mfa``, ``resend_confirmation``, ``toggle_suspend``). |
| `target_user` | `Optional[str]` | `None` | Username the action was applied to, or None for global actions (none today, kept for future use). |
| `ip` | `Optional[str]` | `None` | Remote address that issued the request. ``None`` when the request did not carry one (e.g. background job). |
| `details` | `Optional[str]` | `None` | Free-text context, kept short. Use it for the state transition (e.g. ``active->inactive``) not for payloads that should never leave the audit log. |

**Returns:** `int` - The new row's ``id``.

<a id="superadminauditdb-recent"></a>

#### `SuperadminAuditDB.recent`

`method` | [models/superadmin_audit.py:119](../../models/superadmin_audit.py#L119)

```python
def recent(self, limit: int = 50) -> List[Dict[str, Any]]
```

Return the most recent ``limit`` audit rows, newest first.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `limit` | `int` | `50` | Maximum rows to return. Capped at 500 to bound template rendering cost on a noisy superadmin. |

**Returns:** `List[Dict[str, Any]]` - List of dicts with keys ``id``, ``ts``, ``actor``,
``action``, ``target_user``, ``ip``, ``details``.

*Called by:* [`superadmin`](views.admin.py.md#superadmin)

---
