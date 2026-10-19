# `utils.mailer`

> Source: [utils/mailer.py:1](../../utils/mailer.py#L1) | language `py` | coverage 100.0% | [API index](../index.md)

Transactional email helpers for QuantumVault.

Centralizes how outbound transactional mail is addressed and delivered so the
registration flow and the background scheduler share a single implementation
instead of each rebuilding absolute URLs and calling Flask-Mail directly.

The public host used for links is taken from ``SERVER_NAME`` and
``PREFERRED_URL_SCHEME`` so the same code produces correct links from a
background thread (no request context) and from a request handler.

## Contents

- **Functions:** [`external_url`](#external_url), [`mail_is_configured`](#mail_is_configured), [`send_transactional_email`](#send_transactional_email)
- **Constants:** [`DEFAULT_SENDER`](#default_sender), [`DEFAULT_HOST`](#default_host), [`DEFAULT_SCHEME`](#default_scheme)

## Functions

<a id="external_url"></a>

### `external_url`

`function` | [utils/mailer.py:22](../../utils/mailer.py#L22)

```python
def external_url(path: str) -> str
```

Build an absolute URL for a root-relative path using the public host.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `path` | `str` |  | A path such as ``/confirm/<token>``. A leading slash is added if missing. |

**Returns:** `str` - The absolute URL, for example ``https://www.quantumvault.pro/confirm/x``.

*Called by:* [`AuthController.send_confirmation_email`](controllers.auth.py.md#authcontroller-send_confirmation_email), [`cmd_link`](scripts.email_tool.py.md#cmd_link), [`init_scheduler`](utils.scheduler.py.md#init_scheduler)

---

<a id="mail_is_configured"></a>

### `mail_is_configured`

`function` | [utils/mailer.py:38](../../utils/mailer.py#L38)

```python
def mail_is_configured() -> bool
```

Return True when SMTP credentials are present so a send can succeed.

A send is only attempted when both a username and password are set,
which lets callers fall back to logging a link in local or bare-VPS
deployments that have no mail account yet.

**Returns:** `bool`

*Called by:* [`AuthController.send_confirmation_email`](controllers.auth.py.md#authcontroller-send_confirmation_email), [`cmd_test_smtp`](scripts.email_tool.py.md#cmd_test_smtp), [`reset_with_recovery`](views.auth.py.md#reset_with_recovery)

---

<a id="send_transactional_email"></a>

### `send_transactional_email`

`function` | [utils/mailer.py:51](../../utils/mailer.py#L51)

```python
def send_transactional_email(subject: str, recipients: Sequence[str], body: str) -> bool
```

Send a plain-text transactional email through the configured server.

This never raises: a failure is logged and reported through the boolean
return so callers (registration, scheduler) degrade gracefully instead of
aborting the surrounding operation.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `subject` | `str` |  | The email subject line. |
| `recipients` | `Sequence[str]` |  | One or more destination addresses. |
| `body` | `str` |  | The plain-text message body. |

**Returns:** `bool` - True if Flask-Mail accepted the message, False otherwise.

*Called by:* [`AuthController.send_confirmation_email`](controllers.auth.py.md#authcontroller-send_confirmation_email), [`cmd_test_smtp`](scripts.email_tool.py.md#cmd_test_smtp), [`init_scheduler`](utils.scheduler.py.md#init_scheduler), [`reset_with_recovery`](views.auth.py.md#reset_with_recovery)

---

## Constants

<a id="default_sender"></a>

### `DEFAULT_SENDER`

`constant` | [utils/mailer.py:17](../../utils/mailer.py#L17)

```python
DEFAULT_SENDER = 'noreply@quantumvault.pro'
```

---

<a id="default_host"></a>

### `DEFAULT_HOST`

`constant` | [utils/mailer.py:18](../../utils/mailer.py#L18)

```python
DEFAULT_HOST = 'quantumvault.pro'
```

---

<a id="default_scheme"></a>

### `DEFAULT_SCHEME`

`constant` | [utils/mailer.py:19](../../utils/mailer.py#L19)

```python
DEFAULT_SCHEME = 'https'
```

---
