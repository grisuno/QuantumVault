// Account recovery page controller (QV-RECOVERY-1 flow).
//
// Loaded as an external ES module so it complies with the strict
// Content-Security-Policy (script-src 'self'), which forbids inline
// scripts and inline event handlers. recoverAccount() in qv-crypto.js
// fetches the account's recovery bundle, decrypts the private key blob
// entirely in the browser using a key derived from the recovery code,
// and re-wraps it under the new password. The recovery code and the new
// password never leave the browser.

import { recoverAccount } from "./qv-crypto.js";

const MIN_PASSWORD_LENGTH = 8;

function setStatus(el, message, isError) {
  if (!el) return;
  el.textContent = message;
  el.classList.toggle("status-error", isError);
  el.classList.toggle("status-info", !isError && Boolean(message));
}

async function handleRecover(event) {
  event.preventDefault();
  const form = event.currentTarget;
  const submitButton = form.querySelector('button[type="submit"]');
  const statusEl = document.getElementById("recover-status");

  const username = document.getElementById("username").value.trim();
  const recoveryCode = document.getElementById("recovery_code").value.trim();
  const newPassword = document.getElementById("new_password").value;
  const confirmPassword = document.getElementById("confirm_password").value;
  const csrfToken = document.querySelector("[name=csrf_token]").value;

  if (!username || !recoveryCode || !newPassword || !confirmPassword) {
    setStatus(statusEl, "All fields are required.", true);
    return;
  }
  if (newPassword.length < MIN_PASSWORD_LENGTH) {
    setStatus(
      statusEl,
      `Password must be at least ${MIN_PASSWORD_LENGTH} characters.`,
      true,
    );
    return;
  }
  if (newPassword !== confirmPassword) {
    setStatus(statusEl, "Passwords do not match.", true);
    return;
  }

  const originalLabel = submitButton ? submitButton.textContent : null;
  if (submitButton) {
    submitButton.disabled = true;
    submitButton.textContent = "Recovering...";
  }
  setStatus(statusEl, "", false);

  try {
    const result = await recoverAccount(
      csrfToken,
      username,
      recoveryCode,
      newPassword,
    );
    if (!result.success) {
      throw new Error(result.error || "Account recovery failed.");
    }
    setStatus(statusEl, "Password reset. Redirecting to sign in...", false);
    window.location.href = result.redirect || "/login";
  } catch (e) {
    console.error("Recovery error:", e);
    setStatus(statusEl, e.message, true);
    if (submitButton) {
      submitButton.disabled = false;
      if (originalLabel !== null) submitButton.textContent = originalLabel;
    }
  }
}

function init() {
  const form = document.getElementById("recover-form");
  if (form) {
    form.addEventListener("submit", handleRecover);
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
