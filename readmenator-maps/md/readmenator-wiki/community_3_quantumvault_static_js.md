# quantumvault/static/js

*Community 3 | 9 files | cohesion 0.89*

## Definition

This community groups 9 file(s) rooted at `quantumvault/static/js` with dominant language js (cohesion 0.89). Central symbols: `H`, `Hint`, `aesGcmDecrypt`, `aesGcmEncrypt`, `apiRequest`, `base64ToBytes`, `bucketFor`, `buildDeniableVault`. Core file: `quantumvault/static/js/qv-crypto.js` (40 symbols). Documented purpose: Account settings controller: secure notes (QV-DENIABLE-1).  Loaded as an external ES module to comply with the strict Content-Security-Policy (script-src 'self'.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `quantumvault/static/js/account.js` | js | utility | 9 | yes |
| `quantumvault/static/js/login.js` | js | utility | 2 | yes |
| `quantumvault/static/js/messages.js` | js | infrastructure | 6 | yes |
| `quantumvault/static/js/qv-crypto.js` | js | utility | 40 | yes |
| `quantumvault/static/js/qv-deniable.js` | js | utility | 7 | yes |
| `quantumvault/static/js/qv-padding.js` | js | utility | 5 | yes |
| `quantumvault/static/js/recover.js` | js | utility | 3 | yes |
| `quantumvault/static/js/register.js` | js | utility | 3 | yes |
| `quantumvault/static/js/upload.js` | js | utility | 6 | yes |

## Key Symbols

- `setStatus` (function, `quantumvault/static/js/account.js:20`)
- `csrfToken` (function, `quantumvault/static/js/account.js:31`)
- `apiRequest` (function, `quantumvault/static/js/account.js:36`)
- `loadState` (function, `quantumvault/static/js/account.js:54`)
- `collectSlots` (function, `quantumvault/static/js/account.js:60`)
- `handleConfigure` (function, `quantumvault/static/js/account.js:73`)
- `handleOpen` (function, `quantumvault/static/js/account.js:103`)
- `handleReset` (function, `quantumvault/static/js/account.js:125`)
- `init` (function, `quantumvault/static/js/account.js:138`)
- `handleLogin` (function, `quantumvault/static/js/login.js:11`)
- `init` (function, `quantumvault/static/js/login.js:44`)
- `getCsrfToken` (function, `quantumvault/static/js/messages.js:12`)
- `handleSend` (function, `quantumvault/static/js/messages.js:17`)
- `collectEnvelopes` (function, `quantumvault/static/js/messages.js:44`)
- `handleDecryptInbox` (function, `quantumvault/static/js/messages.js:60`)
- `initEditor` (function, `quantumvault/static/js/messages.js:88`)
- `init` (function, `quantumvault/static/js/messages.js:109`)
- `concatBytes` (function, `quantumvault/static/js/qv-crypto.js:59`)
- `hexToBytes` (function, `quantumvault/static/js/qv-crypto.js:70`)
- `bytesToHex` (function, `quantumvault/static/js/qv-crypto.js:79`)
- `bytesToBase64` (function, `quantumvault/static/js/qv-crypto.js:85`)
- `bytesToBase32` (function, `quantumvault/static/js/qv-crypto.js:96`)
- `base64ToBytes` (function, `quantumvault/static/js/qv-crypto.js:114`)
- `bytesToBigInt` (function, `quantumvault/static/js/qv-crypto.js:121`)
- `i2osp` (function, `quantumvault/static/js/qv-crypto.js:128`) - Encode an integer as a big-endian byte string padded to the length of N.
- `mod` (function, `quantumvault/static/js/qv-crypto.js:138`)
- `modPow` (function, `quantumvault/static/js/qv-crypto.js:142`)
- `randomBytes` (function, `quantumvault/static/js/qv-crypto.js:160`)
- `H` (function, `quantumvault/static/js/qv-crypto.js:169`)
- `Hint` (function, `quantumvault/static/js/qv-crypto.js:173`)

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 10
- Cross-boundary resolved imports (EXTRACTED): 1

## Connections

- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: quantumvault/static/js/qv-padding.js imports utils/padding.py.
- [INFERRED] shares_context community 3 <-> 6 (strength 0.5): Inferred shared context (layer utility) with no import path between community 3 (quantumvault/static/js) and community 6 (quantumvault).
- [INFERRED] shares_context community 3 <-> 7 (strength 0.5): Inferred shared context (layer utility) with no import path between community 3 (quantumvault/static/js) and community 7 (orphans).

## Risks

- [cycle] `quantumvault/static/js/qv-crypto.js` -> `quantumvault/static/js/register.js` -> `quantumvault/static/js/qv-crypto.js`
- [cycle] `quantumvault/static/js/qv-crypto.js` -> `quantumvault/static/js/login.js` -> `quantumvault/static/js/qv-crypto.js`

## Open Questions

- Can the cycle `quantumvault/static/js/qv-crypto.js` -> `quantumvault/static/js/register.js` be broken with an interface?
- What would break if the most connected file in quantumvault/static/js changed?
- Should quantumvault/static/js be split, given cohesion 0.89?

## Sources

- `quantumvault/static/js/account.js`
- `quantumvault/static/js/login.js`
- `quantumvault/static/js/messages.js`
- `quantumvault/static/js/qv-crypto.js`
- `quantumvault/static/js/qv-deniable.js`
- `quantumvault/static/js/qv-padding.js`
- `quantumvault/static/js/recover.js`
- `quantumvault/static/js/register.js`
- `quantumvault/static/js/upload.js`
