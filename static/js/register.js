// Registration page controller (zero-knowledge flow).
//
// This module is loaded as an external ES module so it complies with the
// strict Content-Security-Policy (script-src 'self'), which forbids inline
// scripts and inline event handlers. It reads the profile from the form,
// runs the browser-side crypto in qv-crypto.js, and POSTs only opaque
// zero-knowledge material to the server. The password and the private key
// never leave the browser.

import { buildRegistration } from "./qv-crypto.js";

const MIN_PASSWORD_LENGTH = 8;

// Display the one-time QV-RECOVERY-1 code in a modal and wait for the user
// to acknowledge they have saved it before continuing. The code is shown
// only once: it is never sent to or stored by the server in plaintext.
function showRecoveryCode(recoveryCode) {
  return new Promise((resolve) => {
    const modal = document.getElementById("recovery-code-modal");
    const display = document.getElementById("recovery-code-display");
    const continueButton = document.getElementById("recovery-code-continue");
    if (!modal || !display || !continueButton) {
      alert(
        `Save this account recovery code, it will not be shown again:\n\n${recoveryCode}`,
      );
      resolve();
      return;
    }
    display.textContent = recoveryCode;
    modal.classList.remove("hidden");
    continueButton.addEventListener(
      "click",
      () => {
        modal.classList.add("hidden");
        resolve();
      },
      { once: true },
    );
  });
}

async function handleRegister(event) {
  event.preventDefault();
  const form = event.currentTarget;
  const formData = new FormData(form);
  const data = Object.fromEntries(formData.entries());

  if (!data.username || !data.password) {
    alert("Username and password are required.");
    return;
  }
  if (data.password.length < MIN_PASSWORD_LENGTH) {
    alert(`Password must be at least ${MIN_PASSWORD_LENGTH} characters.`);
    return;
  }

  const submitButton = form.querySelector('button[type="submit"]');
  const originalLabel = submitButton ? submitButton.textContent : null;
  if (submitButton) {
    submitButton.disabled = true;
    submitButton.textContent = "Encrypting...";
  }

  try {
    const profile = {
      email: data.email,
      phone: data.phone,
      first_name: data.first_name,
      last_name: data.last_name,
    };

    // buildRegistration generates the SRP salt+verifier, the hybrid
    // ML-KEM-768 + X25519 keypair, the KDF salt, the password-encrypted
    // private blob, and a QV-RECOVERY-1 recovery code in the browser. The
    // password and the recovery code are used only locally; only the
    // payload (opaque ciphertext and verifiers) is sent to the server.
    const { payload, recoveryCode } = await buildRegistration(
      data.username,
      data.password,
      profile,
    );
    payload.csrf_token = data.csrf_token;

    const response = await fetch(form.action, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": data.csrf_token,
        "X-Requested-With": "XMLHttpRequest",
      },
      credentials: "same-origin",
      body: JSON.stringify(payload),
    });
    const result = await response.json();
    if (!result.success) {
      throw new Error(result.error || "Registration failed");
    }
    await showRecoveryCode(recoveryCode);
    window.location.href = result.redirect || "/login";
  } catch (e) {
    console.error("Registration error:", e);
    alert("Error: " + e.message);
    if (submitButton) {
      submitButton.disabled = false;
      if (originalLabel !== null) submitButton.textContent = originalLabel;
    }
  }
}

function init() {
  const form = document.getElementById("register-form");
  if (form) {
    form.addEventListener("submit", handleRegister);
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
