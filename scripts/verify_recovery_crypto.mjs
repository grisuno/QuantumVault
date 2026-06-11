// Verification script for the QV-RECOVERY-1 scheme added to
// static/js/qv-crypto.js.
//
// Confirms, against the real vendored ML-KEM-768 / X25519 modules:
//   1. The noble ML-KEM-768 secretKey layout is
//      [innerSK(1152) | publicKey(1184) | H(pk)(32) | z(32)] = 2400 bytes,
//      so derivePublicKeyFromPrivateBlob's slice offsets (1152, 1184) are
//      correct.
//   2. buildRegistration -> wrapPrivateKeyForRecovery -> decrypt ->
//      derivePublicKeyFromPrivateBlob reproduces the original public_key
//      byte-for-byte.
//
// Run with:  node scripts/verify_recovery_crypto.mjs

import { ml_kem768 } from "../static/js/vendor/ml_kem.js";
import { x25519 } from "../static/js/vendor/ed25519.js";
import {
  buildRegistration,
  wrapPrivateKeyForRecovery,
  derivePublicKeyFromPrivateBlob,
} from "../static/js/qv-crypto.js";

let failures = 0;

function check(label, condition) {
  const status = condition ? "PASS" : "FAIL";
  console.log(`[${status}] ${label}`);
  if (!condition) failures++;
}

// --- 1. Raw offset check against the vendored ML-KEM-768 module ---

const kem = ml_kem768.keygen();
check("ML-KEM-768 secretKey is 2400 bytes", kem.secretKey.length === 2400);
check("ML-KEM-768 publicKey is 1184 bytes", kem.publicKey.length === 1184);

const slicedPublicKey = kem.secretKey.slice(1152, 1152 + 1184);
check(
  "secretKey[1152:2336] equals publicKey (offset verification)",
  Buffer.from(slicedPublicKey).equals(Buffer.from(kem.publicKey)),
);

const xKeys = x25519.keygen();
const derivedXPublic = x25519.getPublicKey(xKeys.secretKey);
check(
  "x25519.getPublicKey(secretKey) equals keygen().publicKey",
  Buffer.from(derivedXPublic).equals(Buffer.from(xKeys.publicKey)),
);

// --- 2. Full integration: buildRegistration -> recovery rewrap -> decrypt ---

const PBKDF2_ITERATIONS = 600000;
const GCM_IV_BYTES = 12;
const textEncoder = new TextEncoder();

function hexToBytes(hex) {
  const out = new Uint8Array(hex.length / 2);
  for (let i = 0; i < out.length; i++) {
    out[i] = parseInt(hex.substr(i * 2, 2), 16);
  }
  return out;
}

function base64ToBytes(b64) {
  const binary = atob(b64);
  const out = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) out[i] = binary.charCodeAt(i);
  return out;
}

function normalizeRecoveryCode(recoveryCode) {
  return recoveryCode.trim().toUpperCase().replace(/[^A-Z2-7]/g, "");
}

async function deriveMasterKey(password, kdfSaltHex) {
  const baseKey = await crypto.subtle.importKey(
    "raw",
    textEncoder.encode(password),
    "PBKDF2",
    false,
    ["deriveBits"],
  );
  const bits = await crypto.subtle.deriveBits(
    {
      name: "PBKDF2",
      salt: hexToBytes(kdfSaltHex),
      iterations: PBKDF2_ITERATIONS,
      hash: "SHA-256",
    },
    baseKey,
    256,
  );
  return new Uint8Array(bits);
}

async function aesGcmDecrypt(keyBytes, ivAndCiphertext) {
  const key = await crypto.subtle.importKey("raw", keyBytes, "AES-GCM", false, [
    "decrypt",
  ]);
  const iv = ivAndCiphertext.slice(0, GCM_IV_BYTES);
  const ciphertext = ivAndCiphertext.slice(GCM_IV_BYTES);
  return new Uint8Array(
    await crypto.subtle.decrypt({ name: "AES-GCM", iv }, key, ciphertext),
  );
}

const profile = {
  email: "alice@example.test",
  phone: "",
  first_name: "Alice",
  last_name: "Example",
};

const { payload, recoveryCode } = await buildRegistration(
  "alice",
  "correct horse battery staple",
  profile,
);

check("recoveryCode has 8 groups of 4 chars", /^([A-Z2-7]{4}-){7}[A-Z2-7]{4}$/.test(recoveryCode));
check("payload includes recovery_salt", typeof payload.recovery_salt === "string" && payload.recovery_salt.length === 32);
check("payload includes encrypted_private_key_recovery", typeof payload.encrypted_private_key_recovery === "string");

const recoveryKey = await deriveMasterKey(
  normalizeRecoveryCode(recoveryCode),
  payload.recovery_salt,
);
const recoveredPrivateBlob = await aesGcmDecrypt(
  recoveryKey,
  base64ToBytes(payload.encrypted_private_key_recovery),
);

const reconstructedPublicKey = derivePublicKeyFromPrivateBlob(recoveredPrivateBlob);
check(
  "derivePublicKeyFromPrivateBlob(recovered blob) equals payload.public_key",
  reconstructedPublicKey === payload.public_key,
);

// A second, independent recovery wrap of the same blob (e.g. rotation)
// must also round-trip correctly.
const rewrapped = await wrapPrivateKeyForRecovery(recoveredPrivateBlob, recoveryCode);
const rewrappedKey = await deriveMasterKey(normalizeRecoveryCode(recoveryCode), rewrapped.recoverySalt);
const rewrappedBlob = await aesGcmDecrypt(
  rewrappedKey,
  base64ToBytes(rewrapped.encryptedPrivateKeyRecovery),
);
check(
  "re-wrapped recovery blob decrypts to the same privateBlob",
  Buffer.from(rewrappedBlob).equals(Buffer.from(recoveredPrivateBlob)),
);

console.log("");
if (failures > 0) {
  console.error(`${failures} check(s) FAILED`);
  process.exit(1);
} else {
  console.log("All checks passed.");
}
