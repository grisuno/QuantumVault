# `quantumvault/static/js/account.js`

> Source: [quantumvault/static/js/account.js:1](../../quantumvault/static/js/account.js#L1) | language `js` | coverage 10.0% | [API index](../index.md)

Account settings controller: secure notes (QV-DENIABLE-1).

Loaded as an external ES module to comply with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts. All container building and opening happens in qv-deniable.js, in the browser. The server returns and accepts an opaque container plus the non-secret structural parameters; it never sees a passphrase or any note text, and it never reports whether a second set of notes exists.

## Contents

- **Functions:** [`setStatus`](#setstatus), [`csrfToken`](#csrftoken), [`apiRequest`](#apirequest), [`loadState`](#loadstate), [`collectSlots`](#collectslots), [`handleConfigure`](#handleconfigure), [`handleOpen`](#handleopen), [`handleReset`](#handlereset), [`init`](#init)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_quantumvault_static_js_account_js__apiRequest(["apiRequest"])
    n_quantumvault_static_js_account_js__csrfToken(["csrfToken"])
    n_quantumvault_static_js_account_js__loadState(["loadState"])
    n_quantumvault_static_js_account_js__handleConfigure(["handleConfigure"])
    n_quantumvault_static_js_account_js__collectSlots(["collectSlots"])
    n_quantumvault_static_js_account_js__setStatus(["setStatus"])
    n_quantumvault_static_js_account_js__handleOpen(["handleOpen"])
    n_quantumvault_static_js_account_js__handleReset(["handleReset"])
    n_quantumvault_static_js_account_js__init(["init"])
    n_quantumvault_static_js_qv_deniable_js__buildDeniableVault["qv-deniable.buildDeniableVault"]
    n_quantumvault_static_js_qv_deniable_js__openDeniableVault["qv-deniable.openDeniableVault"]
    n_quantumvault_static_js_account_js__apiRequest --> n_quantumvault_static_js_account_js__csrfToken
    n_quantumvault_static_js_account_js__loadState --> n_quantumvault_static_js_account_js__apiRequest
    n_quantumvault_static_js_account_js__handleConfigure --> n_quantumvault_static_js_account_js__apiRequest
    n_quantumvault_static_js_account_js__handleConfigure --> n_quantumvault_static_js_account_js__collectSlots
    n_quantumvault_static_js_account_js__handleConfigure --> n_quantumvault_static_js_account_js__setStatus
    n_quantumvault_static_js_account_js__handleOpen --> n_quantumvault_static_js_account_js__setStatus
    n_quantumvault_static_js_account_js__handleReset --> n_quantumvault_static_js_account_js__apiRequest
    n_quantumvault_static_js_account_js__handleReset --> n_quantumvault_static_js_account_js__loadState
    n_quantumvault_static_js_account_js__handleReset --> n_quantumvault_static_js_account_js__setStatus
    n_quantumvault_static_js_account_js__init --> n_quantumvault_static_js_account_js__loadState
    n_quantumvault_static_js_account_js__init --> n_quantumvault_static_js_account_js__setStatus
    n_quantumvault_static_js_account_js__handleConfigure -.-> n_quantumvault_static_js_qv_deniable_js__buildDeniableVault
    n_quantumvault_static_js_account_js__handleOpen -.-> n_quantumvault_static_js_qv_deniable_js__openDeniableVault
```

## Functions

<a id="setstatus"></a>

### `setStatus`

`function` | [quantumvault/static/js/account.js:20](../../quantumvault/static/js/account.js#L20)

```javascript
function setStatus(message, kind)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `message` |  |  |  |
| `kind` |  |  |  |

*Called by:* [`handleConfigure`](#handleconfigure), [`handleOpen`](#handleopen), [`handleReset`](#handlereset), [`init`](#init)

---

<a id="csrftoken"></a>

### `csrfToken`

`function` | [quantumvault/static/js/account.js:31](../../quantumvault/static/js/account.js#L31)

```javascript
function csrfToken()
```

*Called by:* [`apiRequest`](#apirequest)

---

<a id="apirequest"></a>

### `apiRequest`

`function` `async` | [quantumvault/static/js/account.js:36](../../quantumvault/static/js/account.js#L36)

```javascript
async function apiRequest(method, body)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `method` |  |  |  |
| `body` |  |  |  |

*Calls:* [`csrfToken`](#csrftoken)

*Called by:* [`handleConfigure`](#handleconfigure), [`handleReset`](#handlereset), [`loadState`](#loadstate)

---

<a id="loadstate"></a>

### `loadState`

`function` `async` | [quantumvault/static/js/account.js:54](../../quantumvault/static/js/account.js#L54)

```javascript
async function loadState()
```

*Calls:* [`apiRequest`](#apirequest)

*Called by:* [`handleReset`](#handlereset), [`init`](#init)

---

<a id="collectslots"></a>

### `collectSlots`

`function` | [quantumvault/static/js/account.js:60](../../quantumvault/static/js/account.js#L60)

```javascript
function collectSlots()
```

*Called by:* [`handleConfigure`](#handleconfigure)

---

<a id="handleconfigure"></a>

### `handleConfigure`

`function` `async` | [quantumvault/static/js/account.js:73](../../quantumvault/static/js/account.js#L73)

```javascript
async function handleConfigure(event)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `event` |  |  |  |

*Calls:* [`apiRequest`](#apirequest), [`collectSlots`](#collectslots), [`setStatus`](#setstatus), [`buildDeniableVault`](quantumvault.static.js.qv-deniable.js.md#builddeniablevault)

---

<a id="handleopen"></a>

### `handleOpen`

`function` `async` | [quantumvault/static/js/account.js:103](../../quantumvault/static/js/account.js#L103)

```javascript
async function handleOpen(event)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `event` |  |  |  |

*Calls:* [`setStatus`](#setstatus), [`openDeniableVault`](quantumvault.static.js.qv-deniable.js.md#opendeniablevault)

---

<a id="handlereset"></a>

### `handleReset`

`function` `async` | [quantumvault/static/js/account.js:125](../../quantumvault/static/js/account.js#L125)

```javascript
async function handleReset()
```

*Calls:* [`apiRequest`](#apirequest), [`loadState`](#loadstate), [`setStatus`](#setstatus)

---

<a id="init"></a>

### `init`

`function` `async` | [quantumvault/static/js/account.js:138](../../quantumvault/static/js/account.js#L138)

```javascript
async function init()
```

*Calls:* [`loadState`](#loadstate), [`setStatus`](#setstatus)

---
