// Verification script for the QV-DENIABLE-1 browser crypto in
// static/js/qv-deniable.js. It exercises the build/open round-trip against the
// real module and asserts the structural invariants the server also enforces
// (controllers/deniable_vault.py): exactly slot_count slots and equal-length
// slot ciphertexts.
//
// Run with:  node scripts/verify_deniable_crypto.mjs

import {
  buildDeniableVault,
  openDeniableVault,
} from "../static/js/qv-deniable.js";

let failures = 0;

function check(label, condition) {
  const status = condition ? "PASS" : "FAIL";
  console.log(`[${status}] ${label}`);
  if (!condition) failures++;
}

// A smaller slot size than production keeps the script fast while exercising
// the same code paths. The base64 ciphertext length is derived the same way
// the server does: base64(slot_plaintext_bytes + 16-byte GCM tag).
const SLOT_PLAINTEXT_BYTES = 4096;
const expectedCtB64Length = Math.ceil((SLOT_PLAINTEXT_BYTES + 16) / 3) * 4;

// The parameters the server advertises via GET /api/account/vault. Kept here
// in sync with the defaults in controllers/deniable_vault.py.
const parameters = {
  schema_version: 1,
  slot_count: 2,
  salt_hex_length: 32,
  nonce_hex_length: 24,
  min_kdf_iterations: 600000,
  max_kdf_iterations: 10000000,
  allowed_kdf: ["PBKDF2-SHA256"],
  slot_plaintext_bytes: SLOT_PLAINTEXT_BYTES,
  expected_ct_b64_length: expectedCtB64Length,
  max_envelope_bytes: 4000000,
};

const decoyPassphrase = "open sesame";
const decoyData = "Shopping list: milk, bread, batteries.";
const hiddenPassphrase = "correct horse battery staple";
const hiddenData = "Real notes: the keys are behind the third brick.";

// --- 1. Build with both a decoy and a hidden slot ---

const envelope = await buildDeniableVault(parameters, [
  { passphrase: decoyPassphrase, data: decoyData },
  { passphrase: hiddenPassphrase, data: hiddenData },
]);

check("envelope schema version is 1", envelope.v === 1);
check("envelope kdf is PBKDF2-SHA256", envelope.kdf === "PBKDF2-SHA256");
check(
  "envelope iterations meet the minimum",
  envelope.iterations >= parameters.min_kdf_iterations,
);
check("envelope has exactly slot_count slots", envelope.slots.length === parameters.slot_count);

const ctLengths = new Set(envelope.slots.map((slot) => slot.ct.length));
check("all slot ciphertexts are the same length", ctLengths.size === 1);
check(
  "slot ciphertext is the fixed expected length",
  [...ctLengths][0] === expectedCtB64Length,
);

const saltLengths = new Set(envelope.slots.map((slot) => slot.salt.length));
check("all slot salts are the configured length", saltLengths.size === 1 && [...saltLengths][0] === parameters.salt_hex_length);

// --- 2. Each passphrase opens its own slot and nothing else ---

const opened = await openDeniableVault(envelope, decoyPassphrase);
check("decoy passphrase yields the decoy data", opened.text === decoyData);

const openedHidden = await openDeniableVault(envelope, hiddenPassphrase);
check("hidden passphrase yields the hidden data", openedHidden.text === hiddenData);

check(
  "decoy and hidden resolve to different slots",
  opened.index !== openedHidden.index,
);

// --- 3. A wrong passphrase opens nothing ---

let wrongRejected = false;
try {
  await openDeniableVault(envelope, "not the password");
} catch (e) {
  wrongRejected = true;
}
check("wrong passphrase opens no slot", wrongRejected);

// --- 4. A decoy-only container is structurally identical ---
//
// When the user configures no hidden vault, the hidden slot is random and
// unopenable, yet the container has the same shape as one that hides data.

const decoyOnly = await buildDeniableVault(parameters, [
  { passphrase: decoyPassphrase, data: decoyData },
]);
check("decoy-only container still has slot_count slots", decoyOnly.slots.length === parameters.slot_count);
const decoyOnlyCtLengths = new Set(decoyOnly.slots.map((slot) => slot.ct.length));
check("decoy-only container has equal-length slots", decoyOnlyCtLengths.size === 1);

const decoyOnlyOpen = await openDeniableVault(decoyOnly, decoyPassphrase);
check("decoy-only container opens with the decoy passphrase", decoyOnlyOpen.text === decoyData);

// --- 5. A note larger than the fixed slot size is rejected up front ---

let oversizeRejected = false;
try {
  await buildDeniableVault(parameters, [
    { passphrase: decoyPassphrase, data: "x".repeat(SLOT_PLAINTEXT_BYTES + 1) },
  ]);
} catch (e) {
  oversizeRejected = true;
}
check("a note larger than the slot size is rejected", oversizeRejected);

console.log("");
if (failures > 0) {
  console.error(`${failures} check(s) FAILED`);
  process.exit(1);
} else {
  console.log("All checks passed.");
}
