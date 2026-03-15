// ── Header scroll state ──
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 20);
}, { passive: true });

// ── Mobile menu ──
const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.getElementById('mobileMenu');

hamburger?.addEventListener('click', () => {
  mobileMenu.classList.toggle('open');
});
mobileMenu?.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => mobileMenu.classList.remove('open'));
});

// ── Scroll reveal (general) ──
const revealEls = document.querySelectorAll(
  '.editorial-inner, .product-feature, .pg-card, .ing-item, ' +
  '.testi-card, .ritual-step, .newsletter-text'
);

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const delay = el.dataset.delay || 0;
      setTimeout(() => {
        el.classList.add('reveal', 'visible');
      }, delay);
      revealObserver.unobserve(el);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

revealEls.forEach((el, i) => {
  // Stagger cards in grids
  const parent = el.parentElement;
  const siblings = [...parent.children].filter(c =>
    c.classList.contains('pg-card') ||
    c.classList.contains('ing-item') ||
    c.classList.contains('testi-card')
  );
  const idx = siblings.indexOf(el);
  if (idx >= 0) el.dataset.delay = idx * 100;

  el.classList.add('reveal');
  revealObserver.observe(el);
});

// ── Ritual steps reveal ──
const ritualSteps = document.querySelectorAll('.ritual-step');
const ritualObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      ritualObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });
ritualSteps.forEach(s => ritualObserver.observe(s));

// ── Active nav highlight on scroll ──
const sections = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav a[href^="#"], .nav-left a, .nav-right a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 120) current = sec.id;
  });
  navAnchors.forEach(a => {
    const href = a.getAttribute('href');
    if (href === `#${current}`) {
      a.style.color = 'var(--rose)';
    } else {
      a.style.color = '';
    }
  });
}, { passive: true });
