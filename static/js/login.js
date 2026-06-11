// Login page controller (zero-knowledge SRP-6a flow).
//
// Loaded as an external ES module so it complies with the strict
// Content-Security-Policy (script-src 'self'), which forbids inline scripts
// and inline event handlers. The password never leaves the browser: the SRP
// handshake exchanges only A (client public) and M1 (proof) and verifies the
// server proof M2.

import { login } from "./qv-crypto.js";

async function handleLogin(event) {
  event.preventDefault();
  const form = event.currentTarget;
  const submitButton = form.querySelector('button[type="submit"]');

  try {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const csrfToken = document.querySelector("[name=csrf_token]").value;

    if (!username || !password) {
      alert("Username and password are required.");
      return;
    }

    if (submitButton) {
      submitButton.disabled = true;
    }

    const result = await login(csrfToken, username, password);

    if (result.mfa_required) {
      window.location.href = result.redirect || "/verify_mfa";
    } else {
      window.location.href = result.redirect || "/";
    }
  } catch (e) {
    console.error("Login error:", e);
    alert("Error: " + e.message);
    if (submitButton) submitButton.disabled = false;
  }
}

function init() {
  const form = document.getElementById("login-form");
  if (form) {
    form.addEventListener("submit", handleLogin);
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
