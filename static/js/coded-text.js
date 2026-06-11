// Decipher animation for elements tagged with the "codedText" class.
//
// Extracted from an inline <script> so it complies with the strict
// Content-Security-Policy (script-src 'self'), which forbids inline scripts.
// The effect is purely cosmetic: if the GSAP animation library is not
// available it degrades gracefully and leaves the text untouched.

const SCRAMBLE_ALPHABET =
  "abcdefghijklmnopqrstuvwxyz1234567890!@#$^&*()…æ_+-=;[]/~`";
const ANIMATION_DURATION_SECONDS = 3;
const START_DELAY_SECONDS = 0.05;

function randomChar() {
  const char =
    SCRAMBLE_ALPHABET[Math.floor(Math.random() * SCRAMBLE_ALPHABET.length)];
  return Math.random() > 0.5 ? char : char.toUpperCase();
}

function animateElement(element) {
  const originalText = element.innerHTML;
  const originalChars = originalText.split("");
  const revealFromRight = element.classList.contains("fromRight");

  element.textContent = originalChars.map(randomChar).join("");

  const timeline = window.gsap.timeline();
  timeline.to(element, {
    duration: ANIMATION_DURATION_SECONDS,
    ease: "power2.out",
    delay: START_DELAY_SECONDS,
    onUpdate: () => {
      const charsToReveal = Math.floor(
        timeline.progress() * (originalChars.length + 1),
      );
      let currentText = "";
      for (let i = 0; i < originalChars.length; i++) {
        const revealed = revealFromRight
          ? i >= originalChars.length - charsToReveal
          : i < charsToReveal;
        currentText += revealed ? originalChars[i] : randomChar();
      }
      element.textContent = currentText;
    },
    onComplete: () => {
      element.innerHTML = originalText;
    },
  });
}

function init() {
  if (typeof window.gsap === "undefined") return;
  document.querySelectorAll(".codedText").forEach(animateElement);
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
