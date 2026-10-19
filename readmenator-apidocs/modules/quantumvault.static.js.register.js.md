# `quantumvault/static/js/register.js`

> Source: [quantumvault/static/js/register.js:1](../../quantumvault/static/js/register.js#L1) | language `js` | coverage 50.0% | [API index](../index.md)

Registration page controller (zero-knowledge flow).

This module is loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts and inline event handlers. It reads the profile from the form, runs the browser-side crypto in qv-crypto.js, and POSTs only opaque zero-knowledge material to the server. The password and the private key never leave the browser.

## Contents

- **Functions:** [`showRecoveryCode`](#showrecoverycode), [`handleRegister`](#handleregister), [`init`](#init)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_quantumvault_static_js_register_js__handleRegister(["handleRegister"])
    n_quantumvault_static_js_register_js__showRecoveryCode(["showRecoveryCode"])
    n_quantumvault_static_js_qv_crypto_js__buildRegistration["qv-crypto.buildRegistration"]
    n_quantumvault_static_js_register_js__handleRegister --> n_quantumvault_static_js_register_js__showRecoveryCode
    n_quantumvault_static_js_register_js__handleRegister -.-> n_quantumvault_static_js_qv_crypto_js__buildRegistration
```

## Functions

<a id="showrecoverycode"></a>

### `showRecoveryCode`

`function` | [quantumvault/static/js/register.js:17](../../quantumvault/static/js/register.js#L17)

```javascript
function showRecoveryCode(recoveryCode)
```

Display the one-time QV-RECOVERY-1 code in a modal and wait for the user to acknowledge they have saved it before continuing.

The code is shown only once: it is never sent to or stored by the server in plaintext.

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `recoveryCode` |  |  |  |

*Called by:* [`handleRegister`](#handleregister)

---

<a id="handleregister"></a>

### `handleRegister`

`function` `async` | [quantumvault/static/js/register.js:42](../../quantumvault/static/js/register.js#L42)

```javascript
async function handleRegister(event)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `event` |  |  |  |

*Calls:* [`buildRegistration`](quantumvault.static.js.qv-crypto.js.md#buildregistration), [`showRecoveryCode`](#showrecoverycode)

---

<a id="init"></a>

### `init`

`function` | [quantumvault/static/js/register.js:110](../../quantumvault/static/js/register.js#L110)

```javascript
function init()
```

---
