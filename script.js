/* ============================================================
   ValléE DeS RoseS — Main Script
   - Header scroll state
   - Mobile nav toggle
   - Hero slideshow
   - Information JSON loader
   - Scroll reveal animations
   ============================================================ */

// ── Header scroll ──
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 10);
}, { passive: true });

// ── Mobile nav ──
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');

hamburger?.addEventListener('click', () => {
  const open = mobileNav.classList.toggle('open');
  hamburger.classList.toggle('open', open);
  hamburger.setAttribute('aria-label', open ? 'メニューを閉じる' : 'メニューを開く');
});

// Close mobile nav on link click
mobileNav?.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    mobileNav.classList.remove('open');
    hamburger.classList.remove('open');
  });
});

// ── Hero Slideshow ──
// 画像は images/ フォルダに配置してください:
//   images/hero-1.jpg  (ピンクバラ + グラス)
//   images/hero-2.jpg  (ドライローズ + キャンドル)
//   images/hero-3.jpg  (ピオニー + バラ)
//   images/hero-4.jpg  (白木 + ピンクバラ)
//   images/hero-5.jpg  (グラス + バラ クローズアップ)

const HERO_IMAGES = [
  { src: 'images/hero-1.jpg', alt: 'ピンクのバラとグラス' },
  { src: 'images/hero-2.jpg', alt: 'ドライローズとキャンドル' },
  { src: 'images/hero-3.jpg', alt: 'ピオニーとバラ' },
  { src: 'images/hero-4.jpg', alt: '白い木板とピンクバラ' },
  { src: 'images/hero-5.jpg', alt: 'グラスとバラのクローズアップ' },
];

const SLIDE_INTERVAL = 4500; // ms

function initSlider() {
  const wrap = document.querySelector('.hero-img-wrap');
  if (!wrap) return;

  // Check if any hero images actually exist before building slider
  const firstImg = new Image();
  firstImg.onload = () => buildSlider(wrap);
  firstImg.onerror = () => { /* keep placeholder */ };
  firstImg.src = HERO_IMAGES[0].src;
}

function buildSlider(wrap) {
  // Remove placeholder
  const placeholder = wrap.querySelector('.hero-placeholder');
  if (placeholder) placeholder.remove();

  // Build slides
  HERO_IMAGES.forEach((item, i) => {
    const slide = document.createElement('div');
    slide.className = 'hero-slide' + (i === 0 ? ' active' : '');
    const img = document.createElement('img');
    img.src = item.src;
    img.alt = item.alt;
    img.loading = i === 0 ? 'eager' : 'lazy';
    slide.appendChild(img);
    wrap.appendChild(slide);
  });

  // Build dots
  const dotsWrap = document.createElement('div');
  dotsWrap.className = 'hero-dots';
  HERO_IMAGES.forEach((_, i) => {
    const dot = document.createElement('button');
    dot.className = 'hero-dot' + (i === 0 ? ' active' : '');
    dot.setAttribute('aria-label', `スライド ${i + 1}`);
    dot.addEventListener('click', () => goToSlide(i));
    dotsWrap.appendChild(dot);
  });
  wrap.appendChild(dotsWrap);

  // Autoplay
  let current = 0;
  let timer = setInterval(() => goToSlide((current + 1) % HERO_IMAGES.length), SLIDE_INTERVAL);

  function goToSlide(idx) {
    const slides = wrap.querySelectorAll('.hero-slide');
    const dots = wrap.querySelectorAll('.hero-dot');
    slides[current].classList.remove('active');
    dots[current].classList.remove('active');
    current = idx;
    slides[current].classList.add('active');
    dots[current].classList.add('active');
    clearInterval(timer);
    timer = setInterval(() => goToSlide((current + 1) % HERO_IMAGES.length), SLIDE_INTERVAL);
  }
}

// ── Information JSON Loader ──
async function loadInformation() {
  const grid = document.getElementById('infoGrid');
  if (!grid) return;

  try {
    const res = await fetch('information.json');
    if (!res.ok) throw new Error('fetch failed');
    const data = await res.json();
    renderInfo(grid, data.posts);
  } catch (err) {
    grid.innerHTML = '<p style="text-align:center;color:#a09090;padding:2rem;font-size:0.85rem;">情報の読み込みに失敗しました。</p>';
    console.warn('information.json の読み込みエラー:', err);
  }
}

function renderInfo(grid, posts) {
  if (!posts || posts.length === 0) {
    grid.innerHTML = '<p style="text-align:center;color:#a09090;padding:2rem;">現在お知らせはありません。</p>';
    return;
  }

  grid.innerHTML = posts.map(post => `
    <article class="info-card reveal">
      <a href="${escHtml(post.link || '#')}" class="info-card-img">
        <div class="info-card-img-placeholder"></div>
        ${post.image ? `<img src="${escHtml(post.image)}" alt="${escHtml(post.title)}" loading="lazy" />` : ''}
      </a>
      <div class="info-card-body">
        <span class="info-card-date">${escHtml(post.date)}</span>
        <h3 class="info-card-title">
          <a href="${escHtml(post.link || '#')}">${escHtml(post.title)}</a>
        </h3>
        <p class="info-card-excerpt">${escHtml(post.excerpt)}</p>
        <a href="${escHtml(post.link || '#')}" class="info-card-link">こちら</a>
      </div>
    </article>
  `).join('');

  // Trigger reveal on newly rendered cards
  grid.querySelectorAll('.reveal').forEach((el, i) => {
    el.style.transitionDelay = `${i * 0.12}s`;
    revealObserver.observe(el);
  });
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ── Scroll Reveal ──
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

function initReveal() {
  document.querySelectorAll('.menu-card, .quote-content, .ig-card, .footer-inner').forEach((el, i) => {
    el.classList.add('reveal');
    el.style.transitionDelay = `${(i % 4) * 0.08}s`;
    revealObserver.observe(el);
  });
}

// ── Init ──
document.addEventListener('DOMContentLoaded', () => {
  initSlider();
  loadInformation();
  initReveal();
});
