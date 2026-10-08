# Subsystem: js

## static/js/account.js
- Doc: Account settings controller: secure notes (QV-DENIABLE-1).
- Layer: utility
- Language: js
- Symbols:
  - `setStatus` (function, line 19)
  - `csrfToken` (function, line 30)
  - `apiRequest` (function, line 36)
  - `loadState` (function, line 54)
  - `collectSlots` (function, line 59)
  - `handleConfigure` (function, line 73)
  - `handleOpen` (function, line 103)
  - `handleReset` (function, line 125)
  - `init` (function, line 138)
- Depends on: `static/js/qv-deniable.js`

## static/js/coded-text.js
- Doc: Decipher animation for elements tagged with the "codedText" class.
- Layer: utility
- Language: js
- Symbols:
  - `randomChar` (function, line 12)
  - `animateElement` (function, line 18)
  - `init` (function, line 49)

## static/js/login.js
- Doc: Login page controller (zero-knowledge SRP-6a flow).
- Layer: utility
- Language: js
- Symbols:
  - `handleLogin` (function, line 11)
  - `init` (function, line 43)
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/messages.js
- Doc: Messages page controller (zero-knowledge end-to-end messaging).
- Layer: infrastructure
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
- Doc: QuantumVault zero-knowledge browser crypto.
- Layer: utility
- Language: js
- Symbols:
  - `concatBytes` (function, line 58)
  - `hexToBytes` (function, line 69)
  - `bytesToHex` (function, line 78)
  - `bytesToBase64` (function, line 84)
  - `bytesToBase32` (function, line 95)
  - `base64ToBytes` (function, line 113)
  - `bytesToBigInt` (function, line 120)
  - `i2osp` (function, line 127)
  - `mod` (function, line 137)
  - `modPow` (function, line 141)
  - `randomBytes` (function, line 159)
  - `H` (function, line 168)
  - `Hint` (function, line 172)
  - `deriveKeyFromPassphrase` (function, line 184)
  - `deriveMasterKey` (function, line 205)
  - `aesGcmEncrypt` (function, line 209)
  - `aesGcmDecrypt` (function, line 220)
  - `computeK` (function, line 250)
  - `deriveVerifier` (function, line 255)
  - `srpLogin` (function, line 263)
  - `generateIdentity` (function, line 315)
  - `parsePublicKey` (function, line 343)
  - `parsePrivateBlob` (function, line 351)
  - `deriveWrapKey` (function, line 359)
  - `wrapKey` (function, line 371)
  - `unwrapKey` (function, line 395)
  - `generateRecoveryCode` (function, line 417)
  - `normalizeRecoveryCode` (function, line 428)
  - `wrapPrivateKeyForRecovery` (function, line 436)
  - `derivePublicKeyFromPrivateBlob` (function, line 455)
  - `postJson` (function, line 473)
  - `buildRegistration` (function, line 496)
  - `register` (function, line 530)
  - `recoverAccount` (function, line 541)
  - `login` (function, line 592)
  - `encryptAndUpload` (function, line 599)
  - `downloadAndDecrypt` (function, line 629)
  - `fetchPublicKey` (function, line 668)
  - `sendSecureMessage` (function, line 683)
  - `decryptInbox` (function, line 714)
- Depends on: `static/js/login.js`, `static/js/qv-padding.js`, `static/js/register.js`
- Imported by: `static/js/login.js`, `static/js/messages.js`, `static/js/qv-deniable.js`, `static/js/recover.js`, `static/js/register.js`, `static/js/upload.js`

## static/js/qv-deniable.js
- Doc: QuantumVault deniable vault (QV-DENIABLE-1) browser crypto.
- Layer: utility
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

## static/js/qv-padding.js
- Doc: QuantumVault fixed-bucket padding (QV-PAD-1), browser mirror of utils/padding.py.
- Layer: utility
- Language: js
- Symbols:
  - `tableFor` (function, line 15)
  - `bucketFor` (function, line 20)
  - `randomPad` (function, line 33)
  - `padFramed` (function, line 42)
  - `unframeFramed` (function, line 54)
- Depends on: `utils/padding.py`
- Imported by: `static/js/qv-crypto.js`

## static/js/recover.js
- Doc: Account recovery page controller (QV-RECOVERY-1 flow).
- Layer: utility
- Language: js
- Symbols:
  - `setStatus` (function, line 14)
  - `handleRecover` (function, line 22)
  - `init` (function, line 79)
- Depends on: `static/js/qv-crypto.js`

## static/js/register.js
- Doc: Registration page controller (zero-knowledge flow).
- Layer: utility
- Language: js
- Symbols:
  - `showRecoveryCode` (function, line 16)
  - `handleRegister` (function, line 42)
  - `init` (function, line 109)
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/upload.js
- Doc: Upload page controller (zero-knowledge file storage).
- Layer: utility
- Language: js
- Symbols:
  - `getCsrfToken` (function, line 11)
  - `getUsername` (function, line 16)
  - `getPublicKey` (function, line 23)
  - `handleUpload` (function, line 40)
  - `handleDownload` (function, line 74)
  - `init` (function, line 96)
- Depends on: `static/js/qv-crypto.js`
