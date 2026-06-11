// Upload page controller (zero-knowledge file storage).
//
// Loaded as an external ES module so it complies with the strict
// Content-Security-Policy (script-src 'self'). The browser derives a fresh
// file key, encrypts the file with AES-256-GCM, and wraps the key to the
// user's hybrid public key. Downloads are decrypted locally after prompting
// for the password. The server never sees plaintext, the file key, or the
// password.

import { encryptAndUpload, downloadAndDecrypt } from "./qv-crypto.js";

function getCsrfToken() {
  const field = document.querySelector("[name=csrf_token]");
  return field ? field.value : "";
}

function getUsername(uploadForm) {
  return uploadForm.dataset.username || "";
}

let cachedPublicKey = null;

async function getPublicKey(username) {
  if (cachedPublicKey) return cachedPublicKey;
  if (!username) throw new Error("Username not valid");
  const response = await fetch(
    `/api/auth/pubkey?username=${encodeURIComponent(username)}`,
    { headers: { "X-CSRFToken": getCsrfToken() }, credentials: "same-origin" },
  );
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(
      error.error || `Error ${response.status} getting public key`,
    );
  }
  cachedPublicKey = (await response.json()).publicKey;
  return cachedPublicKey;
}

async function handleUpload(event, uploadForm, fileInput, submitButton) {
  event.preventDefault();
  submitButton.disabled = true;
  const originalLabel = submitButton.textContent;
  submitButton.textContent = "Encrypting...";

  const files = fileInput.files;
  if (files.length === 0) {
    alert("Please select a file.");
    submitButton.disabled = false;
    submitButton.textContent = originalLabel;
    return;
  }

  try {
    const publicKey = await getPublicKey(getUsername(uploadForm));
    if (!publicKey) throw new Error("Could not retrieve public key.");

    submitButton.textContent = "Uploading...";
    const result = await encryptAndUpload(
      uploadForm.action,
      getCsrfToken(),
      files[0],
      publicKey,
    );
    alert(result.message || "File uploaded successfully!");
    window.location.reload();
  } catch (error) {
    alert(`Error: ${error.message}`);
    submitButton.disabled = false;
    submitButton.textContent = originalLabel;
  }
}

async function handleDownload(event, username) {
  event.preventDefault();
  const link = event.currentTarget;
  const filename = link.dataset.filename;
  const password = prompt("Please enter your password to decrypt the file:");
  if (!password) return;

  try {
    const result = await downloadAndDecrypt(link.href, username, password);
    const downloadUrl = window.URL.createObjectURL(result.blob);
    const anchor = document.createElement("a");
    anchor.style.display = "none";
    anchor.href = downloadUrl;
    anchor.download = result.filename || filename;
    document.body.appendChild(anchor);
    anchor.click();
    window.URL.revokeObjectURL(downloadUrl);
    anchor.remove();
  } catch (error) {
    alert(`Decryption failed: ${error.message}`);
  }
}

function init() {
  const uploadForm = document.getElementById("uploadForm");
  if (uploadForm) {
    const fileInput = document.getElementById("fileInput");
    const submitButton = document.getElementById("submitButton");
    uploadForm.addEventListener("submit", (e) =>
      handleUpload(e, uploadForm, fileInput, submitButton),
    );
  }

  const username = uploadForm ? getUsername(uploadForm) : "";
  document.querySelectorAll(".download-link").forEach((link) => {
    link.addEventListener("click", (e) => handleDownload(e, username));
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
