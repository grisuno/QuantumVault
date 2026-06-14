// Account settings controller: secure notes (QV-DENIABLE-1).
//
// Loaded as an external ES module to comply with the strict
// Content-Security-Policy (script-src 'self'), which forbids inline scripts.
// All container building and opening happens in qv-deniable.js, in the
// browser. The server returns and accepts an opaque container plus the
// non-secret structural parameters; it never sees a passphrase or any note
// text, and it never reports whether a second set of notes exists.

import { buildDeniableVault, openDeniableVault } from "./qv-deniable.js";

const API_URL = "/api/account/vault";

// In-memory state. `parameters` are the structural limits advertised by the
// server; `envelope` is the current container, always present (the server
// mints a random one on first access).
let parameters = null;
let envelope = null;

function setStatus(message, kind) {
  const el = document.getElementById("dv-status");
  if (!el) return;
  el.textContent = message;
  el.className = "mt-3";
  if (message) {
    const variant = kind === "error" ? "danger" : kind === "success" ? "success" : "info";
    el.classList.add("alert", `alert-${variant}`);
  }
}

function csrfToken() {
  const el = document.getElementById("dv-csrf-token");
  return el ? el.value : "";
}

async function apiRequest(method, body) {
  const options = {
    method,
    credentials: "same-origin",
    headers: { "X-CSRFToken": csrfToken() },
  };
  if (body !== undefined) {
    options.headers["Content-Type"] = "application/json";
    options.body = JSON.stringify(body);
  }
  const response = await fetch(API_URL, options);
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.error || `Request failed (${response.status}).`);
  }
  return data;
}

async function loadState() {
  const data = await apiRequest("GET");
  parameters = data.parameters;
  envelope = data.envelope;
}

function collectSlots() {
  const decoyPassphrase = document.getElementById("dv-decoy-passphrase").value;
  const decoyData = document.getElementById("dv-decoy-data").value;
  const hiddenPassphrase = document.getElementById("dv-hidden-passphrase").value;
  const hiddenData = document.getElementById("dv-hidden-data").value;

  const slots = [{ passphrase: decoyPassphrase, data: decoyData }];
  if (hiddenPassphrase) {
    slots.push({ passphrase: hiddenPassphrase, data: hiddenData });
  }
  return slots;
}

async function handleConfigure(event) {
  event.preventDefault();
  const slots = collectSlots();
  if (!slots[0].passphrase) {
    setStatus("A passphrase is required.", "error");
    return;
  }
  if (slots.length > 1 && slots[1].passphrase === slots[0].passphrase) {
    setStatus("The two passphrases must be different.", "error");
    return;
  }

  setStatus("Encrypting and saving...", "info");
  try {
    const built = await buildDeniableVault(parameters, slots);
    await apiRequest("PUT", { envelope: built });
    envelope = built;
    setStatus("Saved.", "success");
    event.currentTarget.reset();
  } catch (e) {
    console.error("Secure notes save failed:", e);
    setStatus(e.message, "error");
  }
}

async function handleOpen(event) {
  event.preventDefault();
  const output = document.getElementById("dv-open-output");
  const passphrase = document.getElementById("dv-open-passphrase").value;
  output.value = "";

  if (!envelope) {
    setStatus("Nothing to open yet.", "error");
    return;
  }

  try {
    const opened = await openDeniableVault(envelope, passphrase);
    output.value = opened.text;
    setStatus("Opened.", "success");
  } catch (e) {
    // A wrong passphrase and an unused slot are deliberately
    // indistinguishable: both simply yield no notes.
    setStatus("No notes were found for that passphrase.", "info");
  }
}

async function handleReset() {
  if (!window.confirm("Reset all notes? This cannot be undone.")) {
    return;
  }
  try {
    await apiRequest("DELETE");
    await loadState();
    setStatus("All notes were reset.", "info");
  } catch (e) {
    setStatus(e.message, "error");
  }
}

async function init() {
  const configureForm = document.getElementById("dv-configure-form");
  const openForm = document.getElementById("dv-open-form");
  const resetButton = document.getElementById("dv-reset-button");

  if (configureForm) configureForm.addEventListener("submit", handleConfigure);
  if (openForm) openForm.addEventListener("submit", handleOpen);
  if (resetButton) resetButton.addEventListener("click", handleReset);

  try {
    await loadState();
  } catch (e) {
    setStatus(`Could not load your notes: ${e.message}`, "error");
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
