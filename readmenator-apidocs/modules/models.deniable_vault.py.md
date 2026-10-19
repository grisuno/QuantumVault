# `models.deniable_vault`

> Source: [models/deniable_vault.py:1](../../models/deniable_vault.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Opaque storage for QV-DENIABLE-1 deniable vault containers.

The server is zero-knowledge: it stores one opaque, client-encrypted
container per user and never derives, decrypts, or inspects the
plaintext. A container is the JSON envelope produced by the browser
(see ``static/js/qv-deniable.js``); from the database's point of view it
is just text.

The table is deliberately minimal. It carries only what the server must
hold to serve the container back and to bound storage:

* ``username`` (primary key) links the row to the owning account.
* ``envelope`` is the opaque container text.
* ``updated_at`` records when the row last changed, for operator
  housekeeping. No per-slot metadata is stored, because storing anything
  that distinguished one slot from another would undermine the
  deniability guarantee the feature exists to provide.

It lives in the same SQLite file as ``users`` so an operator backup or
restore captures identity and vault state together.

## Contents

- **Classes:** [`DeniableVaultDB`](#deniablevaultdb)

## Classes

<a id="deniablevaultdb"></a>

### `DeniableVaultDB`

`class` | [models/deniable_vault.py:30](../../models/deniable_vault.py#L30)

```python
class DeniableVaultDB
```

Persistence for per-user opaque deniable vault containers.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#deniablevaultdb-__init__) | constructor | Initialize the store and ensure its table exists. |
| [`upsert`](#deniablevaultdb-upsert) | method | Insert or replace the container for ``username``. |
| [`get`](#deniablevaultdb-get) | method | Return the stored container for ``username``, or ``None``. |
| [`exists`](#deniablevaultdb-exists) | method | Return True if ``username`` has a stored container. |

<a id="deniablevaultdb-__init__"></a>

#### `DeniableVaultDB.__init__`

`constructor` | [models/deniable_vault.py:33](../../models/deniable_vault.py#L33)

```python
def __init__(self, db_path: str) -> None
```

Initialize the store and ensure its table exists.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `db_path` | `str` |  | Path to the SQLite database file, shared with [`models.user.UserDB`](models.user.py.md#userdb). |

*Called by:* [`get_deniable_vault_controller`](views.account.py.md#get_deniable_vault_controller)

<a id="deniablevaultdb-upsert"></a>

#### `DeniableVaultDB.upsert`

`method` | [models/deniable_vault.py:57](../../models/deniable_vault.py#L57)

```python
def upsert(self, username: str, envelope: str) -> None
```

Insert or replace the container for ``username``.

The whole container is replaced atomically: a deniable vault has
no partial state, so a replace is always a full rewrite of the
opaque envelope.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `username` | `str` |  | The owning account's username. |
| `envelope` | `str` |  | The opaque container text to store verbatim. |

<a id="deniablevaultdb-get"></a>

#### `DeniableVaultDB.get`

`method` | [models/deniable_vault.py:82](../../models/deniable_vault.py#L82)

```python
def get(self, username: str) -> Optional[Dict[str, Any]]
```

Return the stored container for ``username``, or ``None``.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `username` | `str` |  | The account to look up. |

**Returns:** `Optional[Dict[str, Any]]` - A dict with ``username``, ``envelope``, and ``updated_at``,
or ``None`` when the account has no container.

<a id="deniablevaultdb-exists"></a>

#### `DeniableVaultDB.exists`

`method` | [models/deniable_vault.py:101](../../models/deniable_vault.py#L101)

```python
def exists(self, username: str) -> bool
```

Return True if ``username`` has a stored container.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `username` | `str` |  |  |

**Returns:** `bool`

---
