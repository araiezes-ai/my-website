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
});
