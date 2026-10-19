# `quantumvault/static/js/login.js`

> Source: [quantumvault/static/js/login.js:1](../../quantumvault/static/js/login.js#L1) | language `js` | coverage 33.3% | [API index](../index.md)

Login page controller (zero-knowledge SRP-6a flow).

Loaded as an external ES module so it complies with the strict Content-Security-Policy (script-src 'self'), which forbids inline scripts and inline event handlers. The password never leaves the browser: the SRP handshake exchanges only A (client public) and M1 (proof) and verifies the server proof M2.

## Contents

- **Functions:** [`handleLogin`](#handlelogin), [`init`](#init)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_quantumvault_static_js_login_js__handleLogin(["handleLogin"])
    n_quantumvault_static_js_qv_crypto_js__login["qv-crypto.login"]
    n_quantumvault_static_js_login_js__handleLogin -.-> n_quantumvault_static_js_qv_crypto_js__login
```

## Functions

<a id="handlelogin"></a>

### `handleLogin`

`function` `async` | [quantumvault/static/js/login.js:11](../../quantumvault/static/js/login.js#L11)

```javascript
async function handleLogin(event)
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `event` |  |  |  |

*Calls:* [`login`](quantumvault.static.js.qv-crypto.js.md#login)

---

<a id="init"></a>

### `init`

`function` | [quantumvault/static/js/login.js:44](../../quantumvault/static/js/login.js#L44)

```javascript
function init()
```

---
