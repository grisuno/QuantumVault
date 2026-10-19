// QuantumVault fixed-bucket padding (QV-PAD-1), browser mirror of utils/padding.py.
//
// Every plaintext is framed as [len(4 BE) | plaintext | fresh random pad]
// up to its bucket before AES-GCM. Buckets must stay identical to the
// server table: an envelope whose ciphertext length is not bucket+GCM
// overhead is rejected by the server. Pad bytes come from
// crypto.getRandomValues on every call and are never cached or reused;
// only the immutable bucket tables below are long-lived.

export const MESSAGE_BUCKETS = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536];
export const FILE_BUCKETS = [
  65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 10485760,
];
export const LENGTH_PREFIX_BYTES = 4;

function tableFor(kind) {
  return kind === "file" ? FILE_BUCKETS : MESSAGE_BUCKETS;
}

export function bucketFor(plaintextLen, kind) {
  const table = tableFor(kind);
  const needed = plaintextLen + LENGTH_PREFIX_BYTES;
  let candidate = 0;
  for (const bucket of table) {
    const fits = needed <= bucket ? 1 : 0;
    if (fits === 1 && (candidate === 0 || bucket < candidate)) {
      candidate = bucket;
    }
  }
  if (candidate === 0) throw new Error("Plaintext exceeds the largest bucket.");
  return candidate;
}

function randomPad(length) {
  const out = new Uint8Array(length);
  for (let offset = 0; offset < length; offset += 65536) {
    crypto.getRandomValues(out.subarray(offset, Math.min(offset + 65536, length)));
  }
  return out;
}

export function padFramed(plaintextBytes, kind) {
  const body = plaintextBytes instanceof Uint8Array ? plaintextBytes : new Uint8Array(0);
  const bucket = bucketFor(body.length, kind);
  const out = new Uint8Array(bucket);
  const filler = randomPad(bucket);
  out.set(filler, 0);
  const view = new DataView(out.buffer, out.byteOffset, out.byteLength);
  view.setUint32(0, body.length, false);
  out.set(body, LENGTH_PREFIX_BYTES);
  return out;
}

export function unframeFramed(paddedBytes, kind) {
  const table = tableFor(kind);
  let allowed = 0;
  for (const bucket of table) {
    if (paddedBytes.length === bucket) allowed = 1;
  }
  if (allowed !== 1) throw new Error("Padded length is not a configured bucket.");
  const view = new DataView(
    paddedBytes.buffer,
    paddedBytes.byteOffset,
    paddedBytes.byteLength,
  );
  const declared = view.getUint32(0, false);
  if (declared > paddedBytes.length - LENGTH_PREFIX_BYTES) {
    throw new Error("Declared length exceeds bucket.");
  }
  return paddedBytes.slice(LENGTH_PREFIX_BYTES, LENGTH_PREFIX_BYTES + declared);
}
