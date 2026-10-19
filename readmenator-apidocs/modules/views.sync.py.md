# `views.sync`

> Source: [views/sync.py:1](../../views/sync.py#L1) | language `py` | coverage 66.7% | [API index](../index.md)

End-to-end encrypted file synchronization views.

``POST /secure_sync`` accepts an opaque encrypted payload from the SPA
and stores it under the authenticated user's prefix in S3. The
endpoint is CSRF-protected and rate-limited per (IP, user) pair to
prevent the server from being used as a free file storage for an
attacker who phished a session cookie.

## Contents

- **Functions:** [`secure_sync`](#secure_sync), [`sync_page`](#sync_page)

## Functions

<a id="secure_sync"></a>

### `secure_sync`

`function` | [views/sync.py:29](../../views/sync.py#L29)

Decorators: `@sync_bp.route('/secure_sync', methods=['POST'])`, `@login_required`, `@limiter.limit('30 per minute')`, `@json_csrf_protect`

```python
def secure_sync()
```

Receive an already-encrypted file + wrapped FEK and persist them.

The server never sees the plaintext: the file body and the
wrapped key are opaque from the server's perspective. We only
enforce quota and basic input validation.

---

<a id="sync_page"></a>

### `sync_page`

`function` | [views/sync.py:79](../../views/sync.py#L79)

Decorators: `@sync_bp.route('/sync')`, `@login_required`, `@limiter.limit('50 per minute')`

```python
def sync_page()
```

---
