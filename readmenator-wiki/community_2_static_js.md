# static/js

*Community 2 | 9 files | cohesion 0.89*

## Definition

This community groups 9 file(s) rooted at `static/js` with dominant language js (cohesion 0.89). Central symbols: `H`, `Hint`, `aesGcmDecrypt`, `aesGcmEncrypt`, `apiRequest`, `base64ToBytes`, `bucketFor`, `buildDeniableVault`. Core file: `static/js/qv-crypto.js` (40 symbols). Documented purpose: Account settings controller: secure notes (QV-DENIABLE-1).  Loaded as an external ES module to comply with the strict Content-Security-Policy (script-src 'self'.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `static/js/account.js` | js | utility | 9 | yes |
| `static/js/login.js` | js | utility | 2 | yes |
| `static/js/messages.js` | js | infrastructure | 6 | yes |
| `static/js/qv-crypto.js` | js | utility | 40 | yes |
| `static/js/qv-deniable.js` | js | utility | 7 | yes |
| `static/js/qv-padding.js` | js | utility | 5 | yes |
| `static/js/recover.js` | js | utility | 3 | yes |
| `static/js/register.js` | js | utility | 3 | yes |
| `static/js/upload.js` | js | utility | 6 | yes |

## Key Symbols

- `setStatus` (function, `static/js/account.js:19`)
- `csrfToken` (function, `static/js/account.js:30`)
- `apiRequest` (function, `static/js/account.js:36`)
- `loadState` (function, `static/js/account.js:54`)
- `collectSlots` (function, `static/js/account.js:59`)
- `handleConfigure` (function, `static/js/account.js:73`)
- `handleOpen` (function, `static/js/account.js:103`)
- `handleReset` (function, `static/js/account.js:125`)
- `init` (function, `static/js/account.js:138`)
- `handleLogin` (function, `static/js/login.js:11`)
- `init` (function, `static/js/login.js:43`)
- `getCsrfToken` (function, `static/js/messages.js:11`)
- `handleSend` (function, `static/js/messages.js:17`)
- `collectEnvelopes` (function, `static/js/messages.js:43`)
- `handleDecryptInbox` (function, `static/js/messages.js:60`)
- `initEditor` (function, `static/js/messages.js:87`)
- `init` (function, `static/js/messages.js:108`)
- `concatBytes` (function, `static/js/qv-crypto.js:58`) - -- Encoding helpers ---
- `hexToBytes` (function, `static/js/qv-crypto.js:69`)
- `bytesToHex` (function, `static/js/qv-crypto.js:78`)
- `bytesToBase64` (function, `static/js/qv-crypto.js:84`)
- `bytesToBase32` (function, `static/js/qv-crypto.js:95`)
- `base64ToBytes` (function, `static/js/qv-crypto.js:113`)
- `bytesToBigInt` (function, `static/js/qv-crypto.js:120`)
- `i2osp` (function, `static/js/qv-crypto.js:127`)
- `mod` (function, `static/js/qv-crypto.js:137`)
- `modPow` (function, `static/js/qv-crypto.js:141`)
- `randomBytes` (function, `static/js/qv-crypto.js:159`)
- `H` (function, `static/js/qv-crypto.js:168`)
- `Hint` (function, `static/js/qv-crypto.js:172`)

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 10
- Cross-boundary resolved imports (EXTRACTED): 1

## Connections

- [EXTRACTED] depends_on community 2 <-> 5 (strength 0.9): Extracted import edge crosses communities: static/js/qv-padding.js imports utils/padding.py.
- [INFERRED] shares_context community 2 <-> 6 (strength 0.5): Inferred shared context (layer utility) with no import path between community 2 (static/js) and community 6 (tools).
- [INFERRED] shares_context community 2 <-> 7 (strength 0.5): Inferred shared context (layer utility) with no import path between community 2 (static/js) and community 7 (orphans).

## Risks

- [cycle] `static/js/qv-crypto.js` -> `static/js/register.js` -> `static/js/qv-crypto.js`
- [cycle] `static/js/qv-crypto.js` -> `static/js/login.js` -> `static/js/qv-crypto.js`

## Open Questions

- Can the cycle `static/js/qv-crypto.js` -> `static/js/register.js` be broken with an interface?
- What would break if the most connected file in static/js changed?
- Should static/js be split, given cohesion 0.89?

## Sources

- `static/js/account.js`
- `static/js/login.js`
- `static/js/messages.js`
- `static/js/qv-crypto.js`
- `static/js/qv-deniable.js`
- `static/js/qv-padding.js`
- `static/js/recover.js`
- `static/js/register.js`
- `static/js/upload.js`
