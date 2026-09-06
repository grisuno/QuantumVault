# Subsystem: js

## static/js/account.js
- Layer: utility
- Doc: Account settings controller: secure notes (QV-DENIABLE-1).  Loaded as an external ES module to comply with the strict Co
- Language: js
- Symbols:
  - `setStatus` (function, line 19)
  - `csrfToken` (function, line 30)
  - `apiRequest` (function, line 36)
  - `loadState` (function, line 54)
  - `collectSlots` (function, line 59)
  - `handleConfigure` (function, line 73)
  - `handleOpen` (function, line 98)
  - `handleReset` (function, line 120)
  - `init` (function, line 133)
- Depends on: `static/js/qv-deniable.js`

## static/js/coded-text.js
- Layer: utility
- Doc: Decipher animation for elements tagged with the "codedText" class.  Extracted from an inline <script> so it complies wit
- Language: js
- Symbols:
  - `randomChar` (function, line 12)
  - `animateElement` (function, line 18)
  - `init` (function, line 49)

## static/js/login.js
- Layer: utility
- Doc: Login page controller (zero-knowledge SRP-6a flow).  Loaded as an external ES module so it complies with the strict Cont
- Language: js
- Symbols:
  - `handleLogin` (function, line 11)
  - `init` (function, line 43)
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/messages.js
- Layer: infrastructure
- Doc: Messages page controller (zero-knowledge end-to-end messaging).  Loaded as an external ES module so it complies with the
- Language: js
- Symbols:
  - `getCsrfToken` (function, line 11)
  - `handleSend` (function, line 17)
  - `collectEnvelopes` (function, line 43)
  - `handleDecryptInbox` (function, line 60)
  - `initEditor` (function, line 87)
  - `init` (function, line 108)
- Depends on: `static/js/qv-crypto.js`

## static/js/qv-crypto.js
- Layer: utility
- Doc: QuantumVault zero-knowledge browser crypto.  Single source of truth for all client-side cryptography. The password and e
- Language: js
- Symbols:
  - `concatBytes` (function, line 52)
  - `hexToBytes` (function, line 63)
  - `bytesToHex` (function, line 72)
  - `bytesToBase64` (function, line 78)
  - `bytesToBase32` (function, line 89)
  - `base64ToBytes` (function, line 107)
  - `bytesToBigInt` (function, line 114)
  - `i2osp` (function, line 121)
  - `mod` (function, line 131)
  - `modPow` (function, line 135)
  - `randomBytes` (function, line 153)
  - `H` (function, line 162)
  - `Hint` (function, line 166)
  - `deriveKeyFromPassphrase` (function, line 178)
  - `deriveMasterKey` (function, line 199)
  - `aesGcmEncrypt` (function, line 203)
  - `aesGcmDecrypt` (function, line 214)
  - `computeK` (function, line 244)
  - `deriveVerifier` (function, line 249)
  - `srpLogin` (function, line 257)
  - `generateIdentity` (function, line 309)
  - `parsePublicKey` (function, line 337)
  - `parsePrivateBlob` (function, line 345)
  - `deriveWrapKey` (function, line 353)
  - `wrapKey` (function, line 365)
  - `unwrapKey` (function, line 389)
  - `generateRecoveryCode` (function, line 411)
  - `normalizeRecoveryCode` (function, line 422)
  - `wrapPrivateKeyForRecovery` (function, line 430)
  - `derivePublicKeyFromPrivateBlob` (function, line 449)
  - `postJson` (function, line 467)
  - `buildRegistration` (function, line 490)
  - `register` (function, line 524)
  - `recoverAccount` (function, line 535)
  - `login` (function, line 586)
  - `encryptAndUpload` (function, line 591)
  - `downloadAndDecrypt` (function, line 620)
  - `fetchPublicKey` (function, line 658)
  - `sendSecureMessage` (function, line 673)
  - `decryptInbox` (function, line 703)
- Depends on: `static/js/login.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

## static/js/qv-deniable.js
- Layer: utility
- Doc: QuantumVault deniable vault (QV-DENIABLE-1) browser crypto.  A deniable vault is an opaque container with a fixed number
- Language: js
- Symbols:
  - `toBytes` (function, line 47)
  - `frame` (function, line 55)
  - `unframe` (function, line 64)
  - `sealSlot` (function, line 82)
  - `openSlot` (function, line 102)
  - `buildDeniableVault` (function, line 125)
  - `openDeniableVault` (function, line 170)
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/account.js`

## static/js/recover.js
- Layer: utility
- Doc: Account recovery page controller (QV-RECOVERY-1 flow).  Loaded as an external ES module so it complies with the strict C
- Language: js
- Symbols:
  - `setStatus` (function, line 14)
  - `handleRecover` (function, line 22)
  - `init` (function, line 79)
- Depends on: `static/js/qv-crypto.js`

## static/js/register.js
- Layer: utility
- Doc: Registration page controller (zero-knowledge flow).  This module is loaded as an external ES module so it complies with 
- Language: js
- Symbols:
  - `showRecoveryCode` (function, line 16)
  - `handleRegister` (function, line 42)
  - `init` (function, line 109)
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/upload.js
- Layer: utility
- Doc: Upload page controller (zero-knowledge file storage).  Loaded as an external ES module so it complies with the strict Co
- Language: js
- Symbols:
  - `getCsrfToken` (function, line 11)
  - `getUsername` (function, line 16)
  - `getPublicKey` (function, line 23)
  - `handleUpload` (function, line 40)
  - `handleDownload` (function, line 74)
  - `init` (function, line 96)
- Depends on: `static/js/qv-crypto.js`
