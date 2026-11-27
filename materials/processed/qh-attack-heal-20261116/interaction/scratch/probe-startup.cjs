/* Where the start-up script spends its time (jsdom, upper bound): wraps document.querySelectorAll and Element.closest. */
const { JSDOM } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8')
  .replace('<script>(function () {', '<script>window.__t0=performance.now();(function () {')
  .replace(/\}\)\(\);\n<\/script>\n<\/body>/, '})();window.__t1=performance.now();\n</script>\n</body>');
const res = [];
for (let i = 0; i < 3; i++) {
  const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html',
    beforeParse(w) {
      w.Element.prototype.scrollIntoView = function () {};
      w.__q = { closest: 0, closestMs: 0, qsa: 0, qsaMs: 0 };
      const C = w.Element.prototype.closest, Q = w.Document.prototype.querySelectorAll, QE = w.Element.prototype.querySelectorAll;
      w.Element.prototype.closest = function (s) { const t = w.performance.now(); try { return C.call(this, s); } finally { w.__q.closest++; w.__q.closestMs += w.performance.now() - t; } };
      w.Document.prototype.querySelectorAll = function (s) { const t = w.performance.now(); try { return Q.call(this, s); } finally { w.__q.qsa++; w.__q.qsaMs += w.performance.now() - t; } };
      w.Element.prototype.querySelectorAll = function (s) { const t = w.performance.now(); try { return QE.call(this, s); } finally { w.__q.qsa++; w.__q.qsaMs += w.performance.now() - t; } };
    } });
  const w = dom.window;
  res.push({ startMs: +(w.__t1 - w.__t0).toFixed(1), closest: w.__q.closest, closestMs: +w.__q.closestMs.toFixed(1), qsa: w.__q.qsa, qsaMs: +w.__q.qsaMs.toFixed(1) });
  dom.window.close();
}
console.log(JSON.stringify(res));
