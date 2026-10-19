# `controllers.sync`

> Source: [controllers/sync.py:1](../../controllers/sync.py#L1) | language `py` | coverage 50.0% | [API index](../index.md)

controllers/sync.py

## Contents

- **Classes:** [`SyncController`](#synccontroller)

## Classes

<a id="synccontroller"></a>

### `SyncController`

`class` | [controllers/sync.py:7](../../controllers/sync.py#L7)

```python
class SyncController
```

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#synccontroller-__init__) | constructor |  |
| [`get_storage_usage`](#synccontroller-get_storage_usage) | method | Calcula el uso de almacenamiento del usuario en S3. |

<a id="synccontroller-__init__"></a>

#### `SyncController.__init__`

`constructor` | [controllers/sync.py:8](../../controllers/sync.py#L8)

```python
def __init__(self, users_path: str, s3_bucket: str, s3_client, file_controller)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `users_path` | `str` |  |  |
| `s3_bucket` | `str` |  |  |
| `s3_client` |  |  |  |
| `file_controller` |  |  |  |

*Called by:* [`create_app`](app_factory.py.md#create_app)

<a id="synccontroller-get_storage_usage"></a>

#### `SyncController.get_storage_usage`

`method` | [controllers/sync.py:14](../../controllers/sync.py#L14)

```python
def get_storage_usage(self, username: str) -> int
```

Calcula el uso de almacenamiento del usuario en S3.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `username` | `str` |  |  |

**Returns:** `int`

---
