# Subsystem: js

## static/js/account.js
- Doc: Account settings controller: secure notes (QV-DENIABLE-1).
- Layer: utility
- Language: js
- Symbols:
  - `setStatus` (function, line 20)
  - `csrfToken` (function, line 31)
  - `apiRequest` (function, line 36)
  - `loadState` (function, line 54)
  - `collectSlots` (function, line 60)
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
  - `randomChar` (function, line 13)
  - `animateElement` (function, line 19)
  - `init` (function, line 50)

## static/js/login.js
- Doc: Login page controller (zero-knowledge SRP-6a flow).
- Layer: utility
- Language: js
- Symbols:
  - `handleLogin` (function, line 11)
  - `init` (function, line 44)
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/messages.js
- Doc: Messages page controller (zero-knowledge end-to-end messaging).
- Layer: infrastructure
- Language: js
- Symbols:
  - `getCsrfToken` (function, line 12)
  - `handleSend` (function, line 17)
  - `collectEnvelopes` (function, line 44)
  - `handleDecryptInbox` (function, line 60)
  - `initEditor` (function, line 88)
  - `init` (function, line 109)
- Depends on: `static/js/qv-crypto.js`

## static/js/qv-crypto.js
- Doc: QuantumVault zero-knowledge browser crypto.
- Layer: utility
- Language: js
- Symbols:
  - `concatBytes` (function, line 59)
  - `hexToBytes` (function, line 70)
  - `bytesToHex` (function, line 79)
  - `bytesToBase64` (function, line 85)
  - `bytesToBase32` (function, line 96)
  - `base64ToBytes` (function, line 114)
  - `bytesToBigInt` (function, line 121)
  - `i2osp` (function, line 128)
  - `mod` (function, line 138)
  - `modPow` (function, line 142)
  - `randomBytes` (function, line 160)
  - `H` (function, line 169)
  - `Hint` (function, line 173)
  - `deriveKeyFromPassphrase` (function, line 184)
  - `deriveMasterKey` (function, line 205)
  - `aesGcmEncrypt` (function, line 209)
  - `aesGcmDecrypt` (function, line 220)
  - `computeK` (function, line 251)
  - `deriveVerifier` (function, line 256)
  - `srpLogin` (function, line 263)
  - `generateIdentity` (function, line 316)
  - `parsePublicKey` (function, line 344)
  - `parsePrivateBlob` (function, line 352)
  - `deriveWrapKey` (function, line 360)
  - `wrapKey` (function, line 371)
  - `unwrapKey` (function, line 395)
  - `generateRecoveryCode` (function, line 417)
  - `normalizeRecoveryCode` (function, line 429)
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
  - `toBytes` (function, line 48)
  - `frame` (function, line 56)
  - `unframe` (function, line 65)
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
  - `tableFor` (function, line 16)
  - `bucketFor` (function, line 20)
  - `randomPad` (function, line 34)
  - `padFramed` (function, line 42)
  - `unframeFramed` (function, line 54)
- Depends on: `utils/padding.py`
- Imported by: `static/js/qv-crypto.js`

## static/js/recover.js
- Doc: Account recovery page controller (QV-RECOVERY-1 flow).
- Layer: utility
- Language: js
- Symbols:
  - `setStatus` (function, line 15)
  - `handleRecover` (function, line 22)
  - `init` (function, line 80)
- Depends on: `static/js/qv-crypto.js`

## static/js/register.js
- Doc: Registration page controller (zero-knowledge flow).
- Layer: utility
- Language: js
- Symbols:
  - `showRecoveryCode` (function, line 17)
  - `handleRegister` (function, line 42)
  - `init` (function, line 110)
- Depends on: `static/js/qv-crypto.js`
- Imported by: `static/js/qv-crypto.js`

## static/js/upload.js
- Doc: Upload page controller (zero-knowledge file storage).
- Layer: utility
- Language: js
- Symbols:
  - `getCsrfToken` (function, line 12)
  - `getUsername` (function, line 17)
  - `getPublicKey` (function, line 23)
  - `handleUpload` (function, line 40)
  - `handleDownload` (function, line 74)
  - `init` (function, line 97)
- Depends on: `static/js/qv-crypto.js`
