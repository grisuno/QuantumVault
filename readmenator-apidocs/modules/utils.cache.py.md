# `utils.cache`

> Source: [utils/cache.py:1](../../utils/cache.py#L1) | language `py` | coverage 83.3% | [API index](../index.md)

/home/grisun0/src/postcuantum/v1/utils/cache.py

## Contents

- **Classes:** [`Cache`](#cache)

## Classes

<a id="cache"></a>

### `Cache`

`class` | [utils/cache.py:6](../../utils/cache.py#L6)

```python
class Cache
```

Redis-based caching layer.

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#cache-__init__) | constructor |  |
| [`get`](#cache-get) | method | Retrieve a value from the cache. |
| [`set`](#cache-set) | method | Store a value in the cache with an optional TTL (seconds). |
| [`delete`](#cache-delete) | method | Delete a key from the cache. |

<a id="cache-__init__"></a>

#### `Cache.__init__`

`constructor` | [utils/cache.py:8](../../utils/cache.py#L8)

```python
def __init__(self)
```

<a id="cache-get"></a>

#### `Cache.get`

`method` | [utils/cache.py:11](../../utils/cache.py#L11)

```python
def get(self, key: str) -> Optional[Any]
```

Retrieve a value from the cache.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `key` | `str` |  |  |

**Returns:** `Optional[Any]`

<a id="cache-set"></a>

#### `Cache.set`

`method` | [utils/cache.py:16](../../utils/cache.py#L16)

```python
def set(self, key: str, value: Any, ttl: int = 3600) -> None
```

Store a value in the cache with an optional TTL (seconds).

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `key` | `str` |  |  |
| `value` | `Any` |  |  |
| `ttl` | `int` | `3600` |  |

<a id="cache-delete"></a>

#### `Cache.delete`

`method` | [utils/cache.py:20](../../utils/cache.py#L20)

```python
def delete(self, key: str) -> None
```

Delete a key from the cache.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `key` | `str` |  |  |

---
