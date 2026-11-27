const { JSDOM } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html',
  beforeParse(w) {
    w.Element.prototype.scrollIntoView = function () {};
    w.__s = {};
    for (const P of [w.Document.prototype, w.Element.prototype]) {
      const Q = P.querySelectorAll;
      P.querySelectorAll = function (s) { const t = w.performance.now(); try { return Q.call(this, s); } finally {
        const k = (this.nodeType === 9 ? 'doc ' : this.localName + ' ') + s; const r = w.__s[k] = w.__s[k] || [0, 0]; r[0]++; r[1] += w.performance.now() - t; } };
    }
  } });
const rows = Object.entries(dom.window.__s).sort((a, b) => b[1][1] - a[1][1]).slice(0, 18);
rows.forEach(([k, [n, ms]]) => console.log(ms.toFixed(1).padStart(7), String(n).padStart(4), k.slice(0, 150)));
