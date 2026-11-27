const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const errs = [];
const vc = new VirtualConsole(); vc.on('jsdomError', e => errs.push(e.message)); vc.on('error', (...a) => errs.push('console.error ' + a.join(' ')));
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html', virtualConsole: vc,
  beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
const w = dom.window, d = w.document;
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  await sleep(100);
  const mount = d.querySelector('[data-atlas-mount]');
  const units = [...mount.querySelectorAll('[data-qh-unit][id]')];
  const unit = units[0];
  const title = unit.querySelector('[data-qh-unit-title]');
  let revealed = null, prevented = null;
  d.addEventListener('qh:reveal', e => { revealed = e.detail.id; setTimeout(() => { prevented = e.defaultPrevented; }, 0); });
  const q = d.getElementById('find-q'); q.focus();
  const words = title.textContent.trim().split(/\s+/).slice(0, 3).join(' ');
  q.value = '"' + words + '"'; q.dispatchEvent(new w.Event('input', { bubbles: true })); await sleep(200);
  const links = [...d.querySelectorAll('#find-results .find-link')];
  const hit = links.find(a => a.getAttribute('href') === '#' + unit.id);
  console.log('atlas section', !!mount, 'offered units', units.length, 'query', JSON.stringify(words), 'hits', links.length, 'unit found', !!hit);
  if (hit) { hit.click(); await sleep(120); }
  console.log('qh:reveal for', revealed, 'handled by the atlas (defaultPrevented)', prevented, 'hash', w.location.hash);
  console.log('Part chip for atlas:', !!d.querySelector('.find .filter[data-scope="atlas"]'));
  console.log('page statements still found:', (() => { q.value = 'fusion'; q.dispatchEvent(new w.Event('input', { bubbles: true })); return 'pending'; })());
  await sleep(200);
  console.log('fusion hits', d.querySelectorAll('#find-results .find-link').length, '| atlas hits among them', [...d.querySelectorAll('#find-results .find-link')].filter(a => mount.contains(d.getElementById(a.getAttribute('href').slice(1)))).length);
  console.log('errors', errs.length, errs.slice(0, 5));
  dom.window.close();
})();
