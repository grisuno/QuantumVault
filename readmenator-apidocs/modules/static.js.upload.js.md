# `static/js/upload.js`

> Source: [static/js/upload.js:1](../../static/js/upload.js#L1) | language `js` | coverage 14.3% | [API index](../index.md)

Upload page controller (zero-knowledge file storage).

Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'). The browser derives a fresh file key, encrypts the file with AES-256-GCM, and wraps the key to the user's hybrid public key. Downloads are decrypted locally after prompting for the password. The server never sees plaintext, the file key, or the password.

## Contents

- **Functions:** [`getCsrfToken`](#getcsrftoken), [`getUsername`](#getusername), [`getPublicKey`](#getpublickey), [`handleUpload`](#handleupload), [`handleDownload`](#handledownload), [`init`](#init)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_static_js_upload_js__getPublicKey(["getPublicKey"])
    n_static_js_upload_js__getCsrfToken(["getCsrfToken"])
    n_static_js_upload_js__handleUpload(["handleUpload"])
    n_static_js_upload_js__getUsername(["getUsername"])
    n_static_js_upload_js__init(["init"])
    n_static_js_upload_js__handleDownload(["handleDownload"])
    n_static_js_qv_crypto_js__encryptAndUpload["qv-crypto.encryptAndUpload"]
    n_static_js_qv_crypto_js__downloadAndDecrypt["qv-crypto.downloadAndDecrypt"]
    n_static_js_upload_js__getPublicKey --> n_static_js_upload_js__getCsrfToken
    n_static_js_upload_js__handleUpload --> n_static_js_upload_js__getCsrfToken
    n_static_js_upload_js__handleUpload --> n_static_js_upload_js__getPublicKey
    n_static_js_upload_js__handleUpload --> n_static_js_upload_js__getUsername
    n_static_js_upload_js__init --> n_static_js_upload_js__getUsername
    n_static_js_upload_js__init --> n_static_js_upload_js__handleDownload
    n_static_js_upload_js__init --> n_static_js_upload_js__handleUpload
    n_static_js_upload_js__handleUpload -.-> n_static_js_qv_crypto_js__encryptAndUpload
    n_static_js_upload_js__handleDownload -.-> n_static_js_qv_crypto_js__downloadAndDecrypt
```

## Functions

<a id="getcsrftoken"></a>

### `getCsrfToken`

`function` | [static/js/upload.js:12](../../static/js/upload.js#L12)

```javascript
function getCsrfToken()
```

*Called by:* [`getPublicKey`](#getpublickey), [`handleUpload`](#handleupload)

---

<a id="getusername"></a>

### `getUsername`

`function` | [static/js/upload.js:17](../../static/js/upload.js#L17)

```javascript
function getUsername(uploadForm)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `uploadForm` |  |  |  |

*Called by:* [`handleUpload`](#handleupload), [`init`](#init)

---

<a id="getpublickey"></a>

### `getPublicKey`

`function` `async` | [static/js/upload.js:23](../../static/js/upload.js#L23)

```javascript
async function getPublicKey(username)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `username` |  |  |  |

*Calls:* [`getCsrfToken`](#getcsrftoken)

*Called by:* [`handleUpload`](#handleupload)

---

<a id="handleupload"></a>

### `handleUpload`

`function` `async` | [static/js/upload.js:40](../../static/js/upload.js#L40)

```javascript
async function handleUpload(event, uploadForm, fileInput, submitButton)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `event` |  |  |  |
| `uploadForm` |  |  |  |
| `fileInput` |  |  |  |
| `submitButton` |  |  |  |

*Calls:* [`encryptAndUpload`](static.js.qv-crypto.js.md#encryptandupload), [`getCsrfToken`](#getcsrftoken), [`getPublicKey`](#getpublickey), [`getUsername`](#getusername)

*Called by:* [`init`](#init)

---

<a id="handledownload"></a>

### `handleDownload`

`function` `async` | [static/js/upload.js:74](../../static/js/upload.js#L74)

```javascript
async function handleDownload(event, username)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `event` |  |  |  |
| `username` |  |  |  |

*Calls:* [`downloadAndDecrypt`](static.js.qv-crypto.js.md#downloadanddecrypt)

*Called by:* [`init`](#init)

---

<a id="init"></a>

### `init`

`function` | [static/js/upload.js:97](../../static/js/upload.js#L97)

```javascript
function init()
```

*Calls:* [`getUsername`](#getusername), [`handleDownload`](#handledownload), [`handleUpload`](#handleupload)

---
