/**
 * main.js — Entry point: initialises all interactive modules
 */

import { initNav } from './nav.js';
import { initReveal } from './reveal.js';
import { initPetals } from './petals.js';

document.addEventListener('DOMContentLoaded', () => {
  initNav();
  initReveal();
  initPetals();
  loadInformation();
});

async function loadInformation() {
  const grid = document.getElementById('infoGrid');
  if (!grid) return;

  try {
    const res = await fetch('information.json');
    if (!res.ok) throw new Error('fetch failed');
    const { posts } = await res.json();

    grid.innerHTML = posts.map(post => `
      <article class="info-card reveal">
        <div class="info-card__image">
          <img src="${escHtml(post.image)}" alt="${escHtml(post.title)}" loading="lazy"
               onerror="this.style.display='none'">
        </div>
        <div class="info-card__body">
          <div class="info-card__meta">
            <span class="info-card__date">${escHtml(post.date)}</span>
            ${post.category ? `<span class="info-card__category">${escHtml(post.category)}</span>` : ''}
          </div>
          <h3 class="info-card__title">${escHtml(post.title)}</h3>
          <p class="info-card__excerpt">${escHtml(post.excerpt)}</p>
          <a href="${escHtml(post.link)}" class="info-card__link">続きを読む →</a>
        </div>
      </article>
    `).join('');

    /* re-trigger reveal observer for newly inserted cards */
    if (typeof window.__revealObserver === 'function') {
      window.__revealObserver();
    } else {
      grid.querySelectorAll('.reveal').forEach(el => el.classList.add('is-visible'));
    }
  } catch {
    grid.innerHTML = '<p class="information__loading">情報を読み込めませんでした。</p>';
  }
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
