// QuantumVault zero-knowledge browser crypto.
//
// Single source of truth for all client-side cryptography. The password and
// every private key are generated, used, and stored encrypted in the browser;
// only opaque ciphertext, the SRP salt/verifier, the public key, and the
// password-encrypted private key blob ever reach the server.
//
// Primitives:
//   - Authentication: SRP-6a (RFC 5054 2048-bit group, SHA-256), scheme
//     "QV-SRP-1" mirroring utils/srp6a.py byte-for-byte.
//   - Key wrapping: hybrid KEM = ML-KEM-768 (post-quantum) + X25519 (classical),
//     combined via HKDF-SHA256, sealing keys with AES-256-GCM.
//   - Private-key protection: PBKDF2-SHA256 (600k iterations) derives the master
//     key that encrypts the user's private key blob.
//
// All cryptographic primitives are loaded from the local `vendor/` directory
// instead of a CDN. The vendored bundles are pinned to specific upstream
// versions, served as first-party static assets, and benefit from the
// same SRI / CSP protections as the rest of the application. The version
// comment on each import is the upstream package version that was vendored.

// noble/hashes 1.8.0 — SHA-2, HKDF, utils, browser crypto provider
import { sha256 } from "./vendor/sha2.js";
import { hkdf } from "./vendor/hkdf.js";

// noble/post-quantum 0.4.0 — ML-KEM-768 (FIPS 203)
import { ml_kem768 } from "./vendor/ml_kem.js";

// noble/curves 1.9.7 — X25519, Ed25519
import { x25519 } from "./vendor/ed25519.js";

const N_HEX =
  "AC6BDB41324A9A9BF166DE5E1389582FAF72B6651987EE07FC3192943DB56050" +
  "A37329CBB4A099ED8193E0757767A13DD52312AB4B03310DCD7F48A9DA04FD50" +
  "E8083969EDB767B0CF6095179A163AB3661A05FBD5FAAAE82918A9962F0B93B8" +
  "55F97993EC975EEAA80D740ADBF4FF747359D041D5C33EA71D281E446B14773B" +
  "CA97B43A23FB801676BD207A436C6481F1D2B9078717461A5B9D32E688F87748" +
  "544523B524B0D57D5EA77A2775D2ECFA032CFBDBF52FB3786160279004E57AE6" +
  "AF874E7303CE53299CCC041C7BC308D82A5698F3A8D0C38271AE35F8E9DBFBB6" +
  "94B5C803D89F7AE435DE236D525F54759B65E372FCD68EF20FA7111F9E4AFF73";

const N = BigInt("0x" + N_HEX);
const G = 2n;
const N_BYTE_LENGTH = 256;
const PBKDF2_ITERATIONS = 600000;
const GCM_IV_BYTES = 12;
const HKDF_INFO = "quantumvault-fek-v1";

const textEncoder = new TextEncoder();

// --- Encoding helpers ---

function concatBytes(...arrays) {
  const total = arrays.reduce((sum, a) => sum + a.length, 0);
  const out = new Uint8Array(total);
  let offset = 0;
  for (const a of arrays) {
    out.set(a, offset);
    offset += a.length;
  }
  return out;
}

function hexToBytes(hex) {
  const clean = hex.length % 2 ? "0" + hex : hex;
  const out = new Uint8Array(clean.length / 2);
  for (let i = 0; i < out.length; i++) {
    out[i] = parseInt(clean.substr(i * 2, 2), 16);
  }
  return out;
}

function bytesToHex(bytes) {
  let hex = "";
  for (const b of bytes) hex += b.toString(16).padStart(2, "0");
  return hex;
}

function bytesToBase64(bytes) {
  let binary = "";
  for (const b of bytes) binary += String.fromCharCode(b);
  return btoa(binary);
}

// RFC 4648 Base32 alphabet, no padding. Used for QV-RECOVERY-1 codes:
// 20 random bytes (160 bits) encode to exactly 32 characters with no
// leftover bits, so no padding character is ever needed.
const BASE32_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";

function bytesToBase32(bytes) {
  let bits = 0;
  let value = 0;
  let output = "";
  for (const byte of bytes) {
    value = (value << 8) | byte;
    bits += 8;
    while (bits >= 5) {
      output += BASE32_ALPHABET[(value >>> (bits - 5)) & 0x1f];
      bits -= 5;
    }
  }
  if (bits > 0) {
    output += BASE32_ALPHABET[(value << (5 - bits)) & 0x1f];
  }
  return output;
}

function base64ToBytes(b64) {
  const binary = atob(b64);
  const out = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) out[i] = binary.charCodeAt(i);
  return out;
}

function bytesToBigInt(bytes) {
  let result = 0n;
  for (const b of bytes) result = (result << 8n) | BigInt(b);
  return result;
}

// Encode an integer as a big-endian byte string padded to the length of N.
function i2osp(value) {
  const out = new Uint8Array(N_BYTE_LENGTH);
  let v = value;
  for (let i = N_BYTE_LENGTH - 1; i >= 0; i--) {
    out[i] = Number(v & 0xffn);
    v >>= 8n;
  }
  return out;
}

function mod(a, m) {
  return ((a % m) + m) % m;
}

function modPow(base, exponent, modulus) {
  let result = 1n;
  let b = mod(base, modulus);
  let e = exponent;
  while (e > 0n) {
    if (e & 1n) result = (result * b) % modulus;
    e >>= 1n;
    b = (b * b) % modulus;
  }
  return result;
}

function randomBytes(length) {
  const out = new Uint8Array(length);
  crypto.getRandomValues(out);
  return out;
}

function H(...arrays) {
  return sha256(concatBytes(...arrays));
}

function Hint(...arrays) {
  return bytesToBigInt(H(...arrays));
}

// --- WebCrypto symmetric primitives ---

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

async function aesGcmEncrypt(keyBytes, plaintext) {
  const key = await crypto.subtle.importKey("raw", keyBytes, "AES-GCM", false, [
    "encrypt",
  ]);
  const iv = randomBytes(GCM_IV_BYTES);
  const ciphertext = new Uint8Array(
    await crypto.subtle.encrypt({ name: "AES-GCM", iv }, key, plaintext),
  );
  return concatBytes(iv, ciphertext);
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

// --- SRP-6a (QV-SRP-1), mirrors utils/srp6a.py ---

function computeK() {
  return Hint(i2osp(N), i2osp(G));
}

// Derive x = H(salt | H(I | ":" | P)) and the verifier v = g^x mod N.
function deriveVerifier(username, password, saltHex) {
  const inner = H(textEncoder.encode(`${username}:${password}`));
  const x = Hint(hexToBytes(saltHex), inner);
  return bytesToHex(i2osp(modPow(G, x, N)));
}

// Run a full SRP-6a login against the server, verifying the server proof M2.
async function srpLogin(username, password, csrfToken) {
  const a = bytesToBigInt(randomBytes(32));
  const A = modPow(G, a, N);

  const helloResponse = await postJson(
    "/api/srp/hello",
    { username, A: bytesToHex(i2osp(A)) },
    csrfToken,
  );
  if (!helloResponse.success) {
    throw new Error(helloResponse.error || "Authentication failed.");
  }

  const saltHex = helloResponse.salt;
  const B = BigInt("0x" + helloResponse.B);
  if (mod(B, N) === 0n) throw new Error("Invalid server challenge.");

  const k = computeK();
  const u = Hint(i2osp(A), i2osp(B));
  if (u === 0n) throw new Error("Invalid scrambling parameter.");

  const inner = H(textEncoder.encode(`${username}:${password}`));
  const x = Hint(hexToBytes(saltHex), inner);

  const S = modPow(mod(B - (k * modPow(G, x, N)) % N, N), a + u * x, N);
  const K = H(i2osp(S));

  const hN = H(i2osp(N));
  const hG = H(i2osp(G));
  const hXor = hN.map((byte, idx) => byte ^ hG[idx]);
  const hIdentity = H(textEncoder.encode(username));

  const M1 = H(hXor, hIdentity, hexToBytes(saltHex), i2osp(A), i2osp(B), K);

  const verifyResponse = await postJson(
    "/api/srp/verify",
    { username, M1: bytesToHex(M1) },
    csrfToken,
  );
  if (!verifyResponse.success) {
    throw new Error(verifyResponse.error || "Authentication failed.");
  }

  const expectedM2 = H(i2osp(A), M1, K);
  if (bytesToHex(expectedM2) !== verifyResponse.M2) {
    throw new Error("Server identity could not be verified.");
  }
  return verifyResponse;
}

// --- Hybrid identity and key wrapping ---

// Generate the user's hybrid (ML-KEM-768 + X25519) key pair.
function generateIdentity() {
  const kem = ml_kem768.keygen();
  // x25519.keygen() returns { secretKey, publicKey }; we use both below.
  const x = x25519.keygen();
  const xSecret = x.secretKey;
  const xPublic = x.publicKey;

  const publicKeyB64 = bytesToBase64(
    textEncoder.encode(
      JSON.stringify({
        v: 1,
        mlkem: bytesToBase64(kem.publicKey),
        x: bytesToBase64(xPublic),
      }),
    ),
  );

  const privateBlob = textEncoder.encode(
    JSON.stringify({
      v: 1,
      mlkem: bytesToBase64(kem.secretKey),
      x: bytesToBase64(xSecret),
    }),
  );

  return { publicKeyB64, privateBlob };
}

function parsePublicKey(publicKeyB64) {
  const parsed = JSON.parse(new TextDecoder().decode(base64ToBytes(publicKeyB64)));
  return {
    mlkem: base64ToBytes(parsed.mlkem),
    x: base64ToBytes(parsed.x),
  };
}

function parsePrivateBlob(privateBlob) {
  const parsed = JSON.parse(new TextDecoder().decode(privateBlob));
  return {
    mlkem: base64ToBytes(parsed.mlkem),
    x: base64ToBytes(parsed.x),
  };
}

function deriveWrapKey(sharedSecretPq, sharedSecretClassic) {
  return hkdf(
    sha256,
    concatBytes(sharedSecretPq, sharedSecretClassic),
    new Uint8Array(0),
    textEncoder.encode(HKDF_INFO),
    32,
  );
}

// Seal a file encryption key to a recipient's hybrid public key.
async function wrapKey(publicKeyB64, fekBytes) {
  const pub = parsePublicKey(publicKeyB64);
  const encapsulation = ml_kem768.encapsulate(pub.mlkem);
  const ephemeral = x25519.keygen();
  const ephemeralSecret = ephemeral.secretKey;
  const ephemeralPublic = ephemeral.publicKey;
  const classicShared = x25519.getSharedSecret(ephemeralSecret, pub.x);

  const wrapKeyBytes = deriveWrapKey(encapsulation.sharedSecret, classicShared);
  const sealed = await aesGcmEncrypt(wrapKeyBytes, fekBytes);

  return bytesToBase64(
    textEncoder.encode(
      JSON.stringify({
        v: 1,
        kem: bytesToBase64(encapsulation.cipherText),
        e: bytesToBase64(ephemeralPublic),
        sealed: bytesToBase64(sealed),
      }),
    ),
  );
}

// Recover a file encryption key using the recipient's hybrid private blob.
async function unwrapKey(privateBlob, wrappedFekB64) {
  const priv = parsePrivateBlob(privateBlob);
  const parsed = JSON.parse(
    new TextDecoder().decode(base64ToBytes(wrappedFekB64)),
  );
  const pqShared = ml_kem768.decapsulate(base64ToBytes(parsed.kem), priv.mlkem);
  const classicShared = x25519.getSharedSecret(priv.x, base64ToBytes(parsed.e));

  const wrapKeyBytes = deriveWrapKey(pqShared, classicShared);
  return aesGcmDecrypt(wrapKeyBytes, base64ToBytes(parsed.sealed));
}

// --- Account recovery (QV-RECOVERY-1) ---
//
// A high-entropy recovery code independently re-wraps the same hybrid
// privateBlob that the password wraps. It does not change the user's
// keypair, so messages and files encrypted before a recovery reset stay
// decryptable afterwards. The server stores only the recovery-code-wrapped
// blob and its salt; it never sees the recovery code itself.

// Generate a QV-RECOVERY-1 code: 20 random bytes (160 bits) Base32-encoded
// (RFC 4648, no padding) and grouped as XXXX-XXXX-... for readability.
export function generateRecoveryCode() {
  const raw = bytesToBase32(randomBytes(20));
  const groups = [];
  for (let i = 0; i < raw.length; i += 4) {
    groups.push(raw.slice(i, i + 4));
  }
  return groups.join("-");
}

// Normalize a user-entered recovery code: strip surrounding whitespace,
// remove group separators, and uppercase, so "abcd-efgh" and "ABCDEFGH"
// derive the same key.
function normalizeRecoveryCode(recoveryCode) {
  return recoveryCode.trim().toUpperCase().replace(/[^A-Z2-7]/g, "");
}

// Re-wrap an existing privateBlob under a key derived from a recovery code,
// using the same PBKDF2-SHA256 + AES-256-GCM scheme as the password path,
// with its own independent salt.
export async function wrapPrivateKeyForRecovery(privateBlob, recoveryCode) {
  const recoverySalt = bytesToHex(randomBytes(16));
  const recoveryKey = await deriveMasterKey(
    normalizeRecoveryCode(recoveryCode),
    recoverySalt,
  );
  const encryptedPrivateKeyRecovery = bytesToBase64(
    await aesGcmEncrypt(recoveryKey, privateBlob),
  );
  return { recoverySalt, encryptedPrivateKeyRecovery };
}

// Reconstruct the public key (the same {v, mlkem, x} structure produced by
// generateIdentity) from a decrypted privateBlob. The noble ML-KEM-768
// secretKey is encoded as [innerSK(1152) | publicKey(1184) | H(pk)(32) |
// z(32)], so the public key is recoverable directly; the X25519 public key
// is derived from its secret via x25519.getPublicKey. Used as a
// proof-of-possession when resetting credentials with a recovery code: the
// server accepts the reset only if this matches the stored public_key.
export function derivePublicKeyFromPrivateBlob(privateBlob) {
  const priv = parsePrivateBlob(privateBlob);
  const mlkemPublicKey = priv.mlkem.slice(1152, 1152 + 1184);
  const xPublicKey = x25519.getPublicKey(priv.x);

  return bytesToBase64(
    textEncoder.encode(
      JSON.stringify({
        v: 1,
        mlkem: bytesToBase64(mlkemPublicKey),
        x: bytesToBase64(xPublicKey),
      }),
    ),
  );
}

// --- Network helpers ---

async function postJson(url, body, csrfToken) {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
      "X-Requested-With": "XMLHttpRequest",
    },
    credentials: "same-origin",
    body: JSON.stringify(body),
  });
  return response.json();
}

// --- High-level flows used by templates ---

// Build the zero-knowledge registration payload entirely in the browser.
//
// Returns `{ payload, recoveryCode }`: `payload` is the JSON body to POST to
// the registration endpoint (it includes the recovery-code-wrapped private
// key, but never the recovery code itself), and `recoveryCode` is the
// plaintext QV-RECOVERY-1 code to show the user exactly once. The server
// never sees `recoveryCode`.
export async function buildRegistration(username, password, profile) {
  const srpSalt = bytesToHex(randomBytes(16));
  const kdfSalt = bytesToHex(randomBytes(16));
  const srpVerifier = deriveVerifier(username, password, srpSalt);

  const identity = generateIdentity();
  const masterKey = await deriveMasterKey(password, kdfSalt);
  const encryptedPrivateKey = bytesToBase64(
    await aesGcmEncrypt(masterKey, identity.privateBlob),
  );

  const recoveryCode = generateRecoveryCode();
  const { recoverySalt, encryptedPrivateKeyRecovery } =
    await wrapPrivateKeyForRecovery(identity.privateBlob, recoveryCode);

  return {
    payload: {
      username,
      srp_salt: srpSalt,
      srp_verifier: srpVerifier,
      public_key: identity.publicKeyB64,
      encrypted_private_key: encryptedPrivateKey,
      kdf_salt: kdfSalt,
      recovery_salt: recoverySalt,
      encrypted_private_key_recovery: encryptedPrivateKeyRecovery,
      email: profile.email,
      phone: profile.phone,
      first_name: profile.first_name,
      last_name: profile.last_name,
    },
    recoveryCode,
  };
}

export async function register(formAction, csrfToken, username, password, profile) {
  const { payload } = await buildRegistration(username, password, profile);
  return postJson(formAction, payload, csrfToken);
}

// Reset SRP credentials and the password-encrypted private key using a
// QV-RECOVERY-1 recovery code, without ever exposing the user's keypair to
// the server. Fetches the recovery-wrapped privateBlob, decrypts it locally
// with a key derived from the recovery code, proves possession of the
// resulting keypair by reconstructing its public key, and re-wraps the same
// privateBlob under the new password.
export async function recoverAccount(csrfToken, username, recoveryCode, newPassword) {
  const bundleResponse = await fetch(
    `/api/auth/recovery-bundle?username=${encodeURIComponent(username)}`,
    { credentials: "same-origin" },
  );
  if (!bundleResponse.ok) {
    const error = await bundleResponse.json().catch(() => ({}));
    throw new Error(error.error || "No recovery code is configured for this account.");
  }
  const bundle = await bundleResponse.json();

  const recoveryKey = await deriveMasterKey(
    normalizeRecoveryCode(recoveryCode),
    bundle.recovery_salt,
  );

  let privateBlob;
  try {
    privateBlob = await aesGcmDecrypt(
      recoveryKey,
      base64ToBytes(bundle.encrypted_private_key_recovery),
    );
  } catch (e) {
    throw new Error("Invalid recovery code.");
  }

  const publicKeyProof = derivePublicKeyFromPrivateBlob(privateBlob);

  const srpSalt = bytesToHex(randomBytes(16));
  const srpVerifier = deriveVerifier(username, newPassword, srpSalt);

  const kdfSalt = bytesToHex(randomBytes(16));
  const masterKey = await deriveMasterKey(newPassword, kdfSalt);
  const encryptedPrivateKey = bytesToBase64(
    await aesGcmEncrypt(masterKey, privateBlob),
  );

  return postJson(
    "/api/auth/reset-with-recovery",
    {
      username,
      public_key_proof: publicKeyProof,
      srp_salt: srpSalt,
      srp_verifier: srpVerifier,
      kdf_salt: kdfSalt,
      encrypted_private_key: encryptedPrivateKey,
    },
    csrfToken,
  );
}

export async function login(csrfToken, username, password) {
  return srpLogin(username, password, csrfToken);
}

// Generate a fresh file key, encrypt the file, wrap the key, and upload.
export async function encryptAndUpload(uploadUrl, csrfToken, file, publicKeyB64) {
  const fek = randomBytes(32);
  const fileBytes = new Uint8Array(await file.arrayBuffer());
  const encryptedFile = await aesGcmEncrypt(fek, fileBytes);
  const wrappedFek = await wrapKey(publicKeyB64, fek);

  const form = new FormData();
  form.append("csrf_token", csrfToken);
  form.append("wrapped_fek", wrappedFek);
  form.append(
    "file",
    new Blob([encryptedFile], { type: "application/octet-stream" }),
    file.name,
  );

  const response = await fetch(uploadUrl, {
    method: "POST",
    headers: { "X-CSRFToken": csrfToken },
    credentials: "same-origin",
    body: form,
  });
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.error || "Upload failed.");
  }
  return response.json();
}

// Download an encrypted file and its key, then decrypt it in the browser.
export async function downloadAndDecrypt(downloadUrl, username, password) {
  const fileResponse = await fetch(downloadUrl, {
    credentials: "same-origin",
  });
  if (!fileResponse.ok) {
    const error = await fileResponse.json().catch(() => ({}));
    throw new Error(error.error || "File not found.");
  }
  const data = await fileResponse.json();

  const keyResponse = await fetch(
    `/api/auth/user-keys?username=${encodeURIComponent(username)}`,
    { credentials: "same-origin" },
  );
  if (!keyResponse.ok) throw new Error("Could not fetch user keys.");
  const keyData = await keyResponse.json();

  const masterKey = await deriveMasterKey(password, keyData.kdf_salt);
  let privateBlob;
  try {
    privateBlob = await aesGcmDecrypt(
      masterKey,
      base64ToBytes(keyData.encrypted_private_key),
    );
  } catch (e) {
    throw new Error("Incorrect password.");
  }

  const fek = await unwrapKey(privateBlob, data.wrapped_fek_b64);
  const plaintext = await aesGcmDecrypt(fek, base64ToBytes(data.encrypted_file_b64));

  return {
    filename: data.filename,
    blob: new Blob([plaintext], { type: "application/octet-stream" }),
  };
}

// Fetch a user's hybrid public key so the browser can wrap content to them.
async function fetchPublicKey(username, csrfToken) {
  const response = await fetch(
    `/api/auth/pubkey?username=${encodeURIComponent(username)}`,
    { headers: { "X-CSRFToken": csrfToken }, credentials: "same-origin" },
  );
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.error || "Failed to fetch the public key.");
  }
  return (await response.json()).publicKey;
}

// Encrypt a message to a recipient (keeping a sender-readable outbox copy)
// and POST the opaque envelope. The plaintext and the CEK never leave the
// browser; the server stores only ciphertext and wrapped keys.
export async function sendSecureMessage(
  csrfToken,
  recipient,
  senderUsername,
  message,
) {
  const cek = randomBytes(32);
  const encryptedMessage = await aesGcmEncrypt(cek, textEncoder.encode(message));

  const recipientPublicKey = await fetchPublicKey(recipient, csrfToken);
  const cekForRecipient = await wrapKey(recipientPublicKey, cek);
  const senderPublicKey = await fetchPublicKey(senderUsername, csrfToken);
  const cekForSender = await wrapKey(senderPublicKey, cek);

  return postJson(
    "/api/secure_message",
    {
      recipient,
      encrypted_message_b64: bytesToBase64(encryptedMessage),
      cek_for_recipient: cekForRecipient,
      cek_for_sender: cekForSender,
    },
    csrfToken,
  );
}

// Decrypt a batch of inbox envelopes with the user's password. The master
// key and private blob are derived once and reused, so this stays cheap even
// for a full mailbox. Returns one result per envelope; a record that cannot
// be decrypted is reported with ``ok: false`` rather than aborting the batch.
export async function decryptInbox(username, password, envelopes) {
  const keyResponse = await fetch(
    `/api/auth/user-keys?username=${encodeURIComponent(username)}`,
    { credentials: "same-origin" },
  );
  if (!keyResponse.ok) throw new Error("Could not fetch user keys.");
  const keyData = await keyResponse.json();

  const masterKey = await deriveMasterKey(password, keyData.kdf_salt);
  let privateBlob;
  try {
    privateBlob = await aesGcmDecrypt(
      masterKey,
      base64ToBytes(keyData.encrypted_private_key),
    );
  } catch (e) {
    throw new Error("Incorrect password.");
  }

  const decoder = new TextDecoder();
  const results = [];
  for (const envelope of envelopes) {
    try {
      const cek = await unwrapKey(privateBlob, envelope.cek_for_recipient);
      const plaintext = await aesGcmDecrypt(
        cek,
        base64ToBytes(envelope.encrypted_message_b64),
      );
      results.push({ ok: true, text: decoder.decode(plaintext) });
    } catch (e) {
      results.push({ ok: false, text: "[Unable to decrypt this message]" });
    }
  }
  return results;
}
