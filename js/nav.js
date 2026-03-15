/**
 * nav.js — Sticky navigation with transparency-to-frosted-glass transition
 * and mobile hamburger menu
 */

export function initNav() {
  const nav = document.getElementById('nav');
  const hamburger = document.getElementById('navHamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileMenuClose = document.getElementById('mobileMenuClose');
  const mobileLinks = mobileMenu ? mobileMenu.querySelectorAll('.mobile-menu__link, .mobile-menu__link') : [];

  if (!nav) return;

  // --- Scroll behaviour ---
  const SCROLL_THRESHOLD = 80;

  function updateNav() {
    if (window.scrollY > SCROLL_THRESHOLD) {
      nav.classList.add('nav--scrolled');
      nav.classList.remove('nav--transparent');
    } else {
      nav.classList.remove('nav--scrolled');
      nav.classList.add('nav--transparent');
    }
  }

  // Initialise on load
  updateNav();
  window.addEventListener('scroll', updateNav, { passive: true });

  // --- Mobile menu ---
  function openMenu() {
    mobileMenu.classList.add('is-open');
    hamburger.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    mobileMenu.classList.remove('is-open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if (hamburger) {
    hamburger.addEventListener('click', openMenu);
  }

  if (mobileMenuClose) {
    mobileMenuClose.addEventListener('click', closeMenu);
  }

  // Close menu when a link is clicked
  mobileLinks.forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileMenu.classList.contains('is-open')) {
      closeMenu();
    }
  });

  // Close on backdrop click
  mobileMenu.addEventListener('click', (e) => {
    if (e.target === mobileMenu) closeMenu();
  });
}
