/**
 * petals.js — Floating rose petal animation for the hero section
 * Creates SVG petal elements that drift down with CSS keyframe animations
 */

const PETAL_SVG = `<svg viewBox="0 0 40 60" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <path d="M20 2 C20 2 2 18 2 34 C2 47 10 56 20 58 C30 56 38 47 38 34 C38 18 20 2 20 2Z"
    fill="currentColor" opacity="0.85"/>
  <path d="M20 12 C20 12 8 24 8 34 C8 43 13 52 20 54 C27 52 32 43 32 34 C32 24 20 12 20 12Z"
    fill="white" opacity="0.25"/>
</svg>`;

const PETAL_COLORS = [
  '#E8A5B0',
  '#F5D5D9',
  '#C4627A',
  '#D4899A',
  '#EDB8C0',
];

export function initPetals() {
  const container = document.getElementById('petalsContainer');
  if (!container) return;

  // Skip on reduced-motion preference
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const PETAL_COUNT = 10;

  for (let i = 0; i < PETAL_COUNT; i++) {
    createPetal(container, i);
  }
}

function createPetal(container, index) {
  const petal = document.createElement('div');
  petal.className = 'petal';
  petal.innerHTML = PETAL_SVG;

  // Random properties
  const size = 14 + Math.random() * 20;          // 14–34px
  const leftPercent = 5 + Math.random() * 90;    // 5–95%
  const duration = 12 + Math.random() * 18;      // 12–30s
  const delay = -(Math.random() * duration);     // stagger start times
  const color = PETAL_COLORS[index % PETAL_COLORS.length];
  const opacity = 0.3 + Math.random() * 0.5;     // 0.3–0.8

  petal.style.cssText = `
    left: ${leftPercent}%;
    top: -60px;
    width: ${size}px;
    height: ${size * 1.5}px;
    color: ${color};
    opacity: ${opacity};
    animation-duration: ${duration}s;
    animation-delay: ${delay}s;
  `;

  container.appendChild(petal);
}
