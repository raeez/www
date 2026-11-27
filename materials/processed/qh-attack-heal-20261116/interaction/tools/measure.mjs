// Real-browser cost of the page script on a task-owned page: start-up, first search index, per-keystroke search,
// Open all (details toggles) and resize. Timer, frame and listener callbacks are timed by wrappers installed before
// the page's own script runs. Usage: node measure.mjs <page.html> <profile-dir> [label]
import { launch } from './chrome.mjs';
import { resolve } from 'node:path';

const [, , pageFile, profile, label = ''] = process.argv;
const INSTRUMENT = `(() => {
  const log = window.__qhTimes = [];
  const name = (fn, kind) => kind + ':' + (fn.name || String(fn).replace(/\\s+/g, ' ').slice(0, 70));
  const wrap = (fn, kind) => function () { const t = performance.now(); try { return fn.apply(this, arguments); }
    finally { const d = performance.now() - t; if (d > 0.5) log.push({ what: name(fn, kind), ms: +d.toFixed(2), at: +t.toFixed(1) }); } };
  const st = window.setTimeout; window.setTimeout = function (fn, ms) { return st.call(window, typeof fn === 'function' ? wrap(fn, 'timeout') : fn, ms); };
  const raf = window.requestAnimationFrame; window.requestAnimationFrame = function (fn) { return raf.call(window, wrap(fn, 'frame')); };
  const add = EventTarget.prototype.addEventListener;
  const map = new WeakMap();
  EventTarget.prototype.addEventListener = function (type, fn, opts) {
    if (typeof fn !== 'function') return add.call(this, type, fn, opts);
    let w = map.get(fn); if (!w) { w = wrap(fn, 'on' + type); map.set(fn, w); }
    return add.call(this, type, w, opts);
  };
  window.__qhLong = [];
  try { new PerformanceObserver(l => l.getEntries().forEach(e => window.__qhLong.push({ ms: +e.duration.toFixed(1), at: +e.startTime.toFixed(1) })))
    .observe({ type: 'longtask', buffered: true }); } catch (e) {}
})();`;

const b = await launch(profile);
const p = await b.page();
await p.s('Page.addScriptToEvaluateOnNewDocument', { source: INSTRUMENT });
await p.goto('file://' + resolve(pageFile), { width: 1400, height: 900 });
const sleep = ms => new Promise(r => setTimeout(r, ms));
await sleep(800);
const out = { label, page: pageFile };
out.start = await p.evaluate(`(() => { const n = performance.getEntriesByType('navigation')[0];
  return { domContentLoaded: +n.domContentLoadedEventEnd.toFixed(0), load: +n.loadEventEnd.toFixed(0),
           longTasks: window.__qhLong.slice(), callbacks: window.__qhTimes.splice(0) }; })()`);
const take = async (what, js, wait = 600) => {
  await p.evaluate(`window.__qhTimes.length = 0; window.__qhLong.length = 0; ${js}; true`);
  await sleep(wait);
  out[what] = await p.evaluate(`({ callbacks: window.__qhTimes.splice(0).sort((a, b) => b.ms - a.ms).slice(0, 8),
    total: 0, longTasks: window.__qhLong.splice(0) })`);
  out[what].total = +out[what].callbacks.reduce((s, c) => s + c.ms, 0).toFixed(1);
};
await take('focusSearch', `document.getElementById('find-q').focus()`);
await take('typeQuery', `(async () => { const q = document.getElementById('find-q'); for (const ch of 'fusion') {
  q.value += ch; q.dispatchEvent(new Event('input', { bubbles: true })); await new Promise(r => setTimeout(r, 40)); } })()`, 900);
await take('typeTwoWords', `(async () => { const q = document.getElementById('find-q'); q.value = ''; for (const ch of 'virasoro module') {
  q.value += ch; q.dispatchEvent(new Event('input', { bubbles: true })); await new Promise(r => setTimeout(r, 40)); } })()`, 1200);
await take('openAllRows', `document.querySelector('#examples [data-expand="all"]').click()`, 900);
await take('closeAllRows', `document.querySelector('#examples [data-expand="none"]').click()`, 900);
await take('resize', `window.dispatchEvent(new Event('resize'))`, 900);
out.problems = p.problems;
console.log(JSON.stringify(out, null, 1));
await b.close();
