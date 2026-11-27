'use strict';
const fs = require('fs');
const { JSDOM, VirtualConsole } = require('jsdom');
const errors = [];
const vc = new VirtualConsole();
vc.on('jsdomError', e => errors.push(String(e && e.message || e).slice(0, 300)));
vc.on('error', e => errors.push(String(e).slice(0, 300)));
const dom = new JSDOM(fs.readFileSync(process.argv[2], 'utf8'), { runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc, url: 'https://example.invalid/book.html' });
const w = dom.window, d = w.document;
setTimeout(() => {
  const figs = Array.from(d.querySelectorAll('figure.qh-fig'));
  console.log('figures:', figs.length, '| live:', figs.filter(f => f.classList.contains('qh-fig-live')).length);
  console.log('reader on:', !!d.querySelector('main[data-reader][data-reader-on]'));
  console.log('elements with data-chapter and an id:', d.querySelectorAll('[data-chapter][id]').length, '| of them figures:', d.querySelectorAll('figure[data-chapter]').length);
  console.log('figures with data-section:', d.querySelectorAll('figure[data-section]').length, '| titles for the reader:', d.querySelectorAll('figure.qh-fig [data-block-title]').length);
  const coh = d.getElementById('fig-cohomology-jump');
  const b = coh && coh.querySelectorAll('button.qh-fig-choose');
  if (b && b.length) { b[0].click(); console.log('cohomology t=-1 chosen:', coh.querySelector('tr[aria-current="true"]').getAttribute('data-state-row'), '| h shown:', !coh.querySelector('[data-part="h"]').hasAttribute('display')); }
  const inf = d.getElementById('fig-infinite-rank'), inp = inf && inf.querySelector('input[type="range"]');
  if (inp) { inp.value = '6'; inp.dispatchEvent(new w.Event('input', { bubbles: true })); console.log('infinite N=6 on-cells (finite):', inf.querySelectorAll('svg[data-grid="finite-truncation"] .qh-fig-cell.is-on').length); }
  const links = Array.from(d.querySelectorAll('figure.qh-fig a[href^="#"]')).map(a => a.getAttribute('href'));
  console.log('figure links:', links.join(' '), '| unresolved:', links.filter(h => !d.getElementById(decodeURIComponent(h.slice(1)))).join(' ') || 'none');
  console.log('script errors:', errors.length ? errors.slice(0, 5) : 'none');
  process.exit(0);
}, 1500);
