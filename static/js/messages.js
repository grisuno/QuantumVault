// Messages page controller (zero-knowledge end-to-end messaging).
//
// Loaded as an external ES module so it complies with the strict
// Content-Security-Policy (script-src 'self'). Sending encrypts the message
// to the recipient's hybrid public key in the browser; receiving decrypts the
// opaque envelopes locally after prompting for the password. Decrypted text is
// rendered with textContent (never innerHTML) so a malicious sender cannot
// inject HTML/script into the recipient's page.

import { sendSecureMessage, decryptInbox } from "./qv-crypto.js";

function getCsrfToken() {
  const field = document.querySelector("[name=csrf_token]");
  return field ? field.value : "";
}

async function handleSend(event) {
  event.preventDefault();
  const form = event.currentTarget;
  const username = form.dataset.username || "";

  try {
    const message = document.getElementById("message").value;
    const recipient = document.getElementById("recipient").value;
    if (!message || !recipient) {
      alert("Recipient and message are required.");
      return;
    }

    const result = await sendSecureMessage(
      getCsrfToken(),
      recipient,
      username,
      message,
    );
    if (!result.success) throw new Error(result.error || "Messaging failed");
    window.location.href = result.redirect || "/";
  } catch (e) {
    console.error("Messaging error:", e);
    alert("Error: " + e.message);
  }
}

function collectEnvelopes() {
  const nodes = Array.from(document.querySelectorAll(".quantum"));
  const items = [];
  for (const node of nodes) {
    try {
      const envelope = JSON.parse(node.textContent);
      if (envelope && envelope.encrypted_message_b64) {
        items.push({ node, envelope });
      }
    } catch (e) {
      // Not an encrypted envelope (e.g. a system notice); leave it untouched.
    }
  }
  return items;
}

async function handleDecryptInbox(form) {
  const username = form.dataset.username || "";
  const items = collectEnvelopes();
  if (items.length === 0) {
    alert("There are no encrypted messages to decrypt.");
    return;
  }

  const password = prompt("Enter your password to decrypt your messages:");
  if (!password) return;

  try {
    const results = await decryptInbox(
      username,
      password,
      items.map((item) => item.envelope),
    );
    results.forEach((result, index) => {
      // textContent, not innerHTML: decrypted message bodies are untrusted
      // sender input and must never be parsed as HTML.
      items[index].node.textContent = result.text;
    });
  } catch (e) {
    console.error("Inbox decryption error:", e);
    alert("Error: " + e.message);
  }
}

function initEditor() {
  const textarea = document.getElementById("message");
  if (!textarea || typeof window.EasyMDE === "undefined") return;

  const editor = new window.EasyMDE({
    element: textarea,
    status: false,
    toolbar: [
      "bold", "italic", "strikethrough", "|",
      "heading", "heading-smaller", "heading-bigger", "|",
      "quote", "unordered-list", "ordered-list", "horizontal-rule", "|",
      "link", "image", "table", "code", "|",
      "undo", "redo", "clean-block", "|",
      "preview", "side-by-side", "fullscreen", "guide",
    ],
  });
  editor.codemirror.on("change", () => {
    textarea.value = editor.value();
  });
}

function init() {
  const form = document.getElementById("messageForm");
  if (form) {
    form.addEventListener("submit", handleSend);
  }
  const decryptButton = document.getElementById("decryptInboxButton");
  if (decryptButton && form) {
    decryptButton.addEventListener("click", () => handleDecryptInbox(form));
  }
  initEditor();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
