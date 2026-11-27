// Does content-visibility on the page's sections shorten the start-up long task, with and without the script's
// eager formula measurement? Usage: node cv-experiment.mjs <page.html> <profile-dir>
import { launch } from './chrome.mjs';
import { resolve } from 'node:path';

const [, , pageFile, profile] = process.argv;
const sleep = ms => new Promise(r => setTimeout(r, ms));
const CV = `document.addEventListener('DOMContentLoaded', () => {}, { once: true });
  (function () { var s = document.createElement('style');
  s.textContent = 'main > .section, main > .changes { content-visibility: auto; contain-intrinsic-size: auto 1600px; }';
  (document.head || document.documentElement).appendChild(s); })();`;
const LONG = `window.__long = []; try { new PerformanceObserver(l => l.getEntries().forEach(e => window.__long.push(+e.duration.toFixed(1))))
  .observe({ type: 'longtask', buffered: true }); } catch (e) {}`;
const NO_MEASURE = `(function () { var raf = window.requestAnimationFrame, first = true;
  window.requestAnimationFrame = function (fn) { if (first && fn.name === 'markScrollers') { first = false; return 0; } return raf.call(window, fn); }; })();`;

const runs = [['plain', [LONG]], ['content-visibility', [LONG, CV]], ['content-visibility, no first formula pass', [LONG, CV, NO_MEASURE]],
              ['plain, no first formula pass', [LONG, NO_MEASURE]]];
const b = await launch(profile);
const out = {};
for (const [name, scripts] of runs) {
  const samples = [];
  for (let i = 0; i < 3; i++) {
    const p = await b.page();
    for (const source of scripts) await p.s('Page.addScriptToEvaluateOnNewDocument', { source });
    await p.goto('file://' + resolve(pageFile), { width: 1400, height: 900 });
    await sleep(500);
    samples.push(await p.evaluate(`({ long: window.__long, dcl: +performance.getEntriesByType('navigation')[0].domContentLoadedEventEnd.toFixed(0),
      fcp: +((performance.getEntriesByName('first-contentful-paint')[0] || {}).startTime || 0).toFixed(0) })`));
    await p.s('Page.close').catch(() => {});
  }
  out[name] = samples;
}
console.log(JSON.stringify(out, null, 1));
await b.close();
