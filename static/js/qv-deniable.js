// QuantumVault deniable vault (QV-DENIABLE-1) browser crypto.
//
// A deniable vault is an opaque container with a fixed number of slots. Each
// slot is independently encrypted under a key derived from its own passphrase;
// only the slot whose passphrase the user enters will authenticate and
// decrypt. The container is built and opened entirely in the browser. The
// server stores only the opaque envelope and never sees a passphrase or a
// plaintext.
//
// Deniability rests on two invariants enforced here and re-checked on the
// server (controllers/deniable_vault.py):
//
//   1. Every container has exactly `slot_count` slots. A container that hides
//      data is structurally identical to one that does not.
//   2. Every slot's plaintext is padded to the same length before encryption,
//      so every slot's ciphertext is the same length. The byte sizes reveal
//      nothing about which slot, if any, holds real data.
//
// When the user configures no hidden vault, the hidden slot is filled with
// random bytes under a random, discarded key. It is then indistinguishable
// from a slot that holds real data the user is simply declining to open.

import {
  randomBytes,
  bytesToHex,
  hexToBytes,
  bytesToBase64,
  base64ToBytes,
  aesGcmEncrypt,
  aesGcmDecrypt,
  deriveKeyFromPassphrase,
  GCM_NONCE_BYTES,
} from "./qv-crypto.js";

// The KDF identifier written into the envelope. It must be a member of the
// server's allow-list (DENIABLE_VAULT_ALLOWED_KDF); PBKDF2-SHA256 is the
// scheme deriveKeyFromPassphrase implements.
const KDF_ID = "PBKDF2-SHA256";

// Each slot's plaintext begins with a 4-byte big-endian length prefix giving
// the true byte length of the payload that follows. The remainder up to the
// fixed slot size is random filler, discarded on open.
const LENGTH_PREFIX_BYTES = 4;

const textEncoder = new TextEncoder();
const textDecoder = new TextDecoder();

function toBytes(data) {
  if (data instanceof Uint8Array) return data;
  return textEncoder.encode(typeof data === "string" ? data : String(data ?? ""));
}

// Frame a payload as [len(4) | payload | random padding] of exactly
// `paddedLength` bytes. `paddedLength` is shared by every slot so the
// resulting ciphertexts are equal length.
function frame(payloadBytes, paddedLength) {
  const out = randomBytes(paddedLength);
  const view = new DataView(out.buffer, out.byteOffset, out.byteLength);
  view.setUint32(0, payloadBytes.length, false);
  out.set(payloadBytes, LENGTH_PREFIX_BYTES);
  return out;
}

// Reverse frame(): read the length prefix and return the exact payload bytes.
function unframe(plaintextBytes) {
  const view = new DataView(
    plaintextBytes.buffer,
    plaintextBytes.byteOffset,
    plaintextBytes.byteLength,
  );
  const length = view.getUint32(0, false);
  const start = LENGTH_PREFIX_BYTES;
  const end = start + length;
  if (length > plaintextBytes.length - LENGTH_PREFIX_BYTES) {
    throw new Error("Corrupt slot: declared payload length exceeds the slot.");
  }
  return plaintextBytes.slice(start, end);
}

// Encrypt one slot's framed plaintext under a passphrase, returning the
// {salt, nonce, ct} object the envelope stores.
async function sealSlot(passphrase, framedPlaintext, parameters) {
  const saltBytes = randomBytes(parameters.salt_hex_length / 2);
  const saltHex = bytesToHex(saltBytes);
  const key = await deriveKeyFromPassphrase(
    passphrase,
    saltHex,
    parameters.min_kdf_iterations,
  );
  const combined = await aesGcmEncrypt(key, framedPlaintext);
  const nonce = combined.slice(0, GCM_NONCE_BYTES);
  const ciphertext = combined.slice(GCM_NONCE_BYTES);
  return {
    salt: saltHex,
    nonce: bytesToHex(nonce),
    ct: bytesToBase64(ciphertext),
  };
}

// Attempt to open one slot with a passphrase. Returns the payload bytes on
// success or null when the passphrase does not authenticate this slot.
async function openSlot(passphrase, slot, iterations) {
  const key = await deriveKeyFromPassphrase(passphrase, slot.salt, iterations);
  const combined = new Uint8Array([
    ...hexToBytes(slot.nonce),
    ...base64ToBytes(slot.ct),
  ]);
  try {
    const plaintext = await aesGcmDecrypt(key, combined);
    return unframe(plaintext);
  } catch (e) {
    return null;
  }
}

// Build a deniable container from a list of slot specifications.
//
// `slots` is an array of `{ passphrase, data }`; `data` may be a string or a
// Uint8Array. The array is padded out to `parameters.slot_count` entries with
// random, unopenable slots so the container always has the fixed slot count.
// Every slot's plaintext is padded to `parameters.slot_plaintext_bytes`, so
// every container is exactly the same size regardless of how much data it
// holds. Throws if more slots are supplied than allowed, or if any slot's
// data does not fit the fixed slot size.
export async function buildDeniableVault(parameters, slots) {
  if (slots.length > parameters.slot_count) {
    throw new Error(`At most ${parameters.slot_count} entries can be saved.`);
  }

  const paddedLength = parameters.slot_plaintext_bytes;
  const specs = slots.map((slot) => ({
    passphrase: slot.passphrase,
    payload: toBytes(slot.data),
  }));

  for (const spec of specs) {
    if (spec.payload.length + LENGTH_PREFIX_BYTES > paddedLength) {
      throw new Error("That note is too large.");
    }
  }

  // Fill the remaining slots with random, unopenable content so every
  // container has exactly slot_count structurally identical slots. A filler
  // slot is just random bytes of the fixed plaintext length; no passphrase
  // can open it, which is the point.
  while (specs.length < parameters.slot_count) {
    specs.push({ passphrase: bytesToHex(randomBytes(32)), payload: null });
  }

  const sealed = [];
  for (const spec of specs) {
    const framed =
      spec.payload === null
        ? randomBytes(paddedLength)
        : frame(spec.payload, paddedLength);
    sealed.push(await sealSlot(spec.passphrase, framed, parameters));
  }

  return {
    v: parameters.schema_version,
    kdf: KDF_ID,
    iterations: parameters.min_kdf_iterations,
    slots: sealed,
  };
}

// Open a container with a passphrase. Tries every slot; only the slot whose
// passphrase matches will authenticate. Returns `{ index, data, text }` for
// the opened slot, or throws if no slot opens.
export async function openDeniableVault(envelope, passphrase) {
  for (let index = 0; index < envelope.slots.length; index++) {
    const payload = await openSlot(passphrase, envelope.slots[index], envelope.iterations);
    if (payload !== null) {
      return { index, data: payload, text: textDecoder.decode(payload) };
    }
  }
  throw new Error("No slot could be opened with that passphrase.");
}
