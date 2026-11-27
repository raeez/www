/* jsdom-only cost of the page script (an upper bound: jsdom is many times slower than a browser and has no layout).
   node jsdom-cost.cjs <page.html> [runs]  -> start-up script time, first focus of the search, per-query search time. */
const { JSDOM } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const runs = +(process.argv[3] || 3);
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  const out = { start: [], firstFocus: [], firstFocusAfterIdle: [], query: {} };
  for (let i = 0; i < runs; i++) {
    let t0;
    const dom = new JSDOM(html.replace('<script>(function () {', '<script>window.__t0=performance.now();(function () {')
                              .replace(/\}\)\(\);\n<\/script>\n<\/body>/, '})();window.__t1=performance.now();\n</script>\n</body>'),
      { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html',
        beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
    const w = dom.window, d = w.document;
    out.start.push(+(w.__t1 - w.__t0).toFixed(1));
    t0 = w.performance.now(); d.getElementById('find-q').focus(); out.firstFocus.push(+(w.performance.now() - t0).toFixed(1));
    const q = d.getElementById('find-q');
    for (const s of ['fusion', 'the', 'virasoro module', '"lattice dual"', '\\mathfrak', 'κ']) {
      q.value = s; q.dispatchEvent(new w.Event('input', { bubbles: true }));
      await sleep(5);
      t0 = w.performance.now(); q.dispatchEvent(new w.KeyboardEvent('keydown', { key: 'Enter', bubbles: true })); /* Enter runs the search at once */
      const ms = w.performance.now() - t0;
      (out.query[s] = out.query[s] || []).push(+ms.toFixed(1));
      await sleep(120);
    }
    dom.window.close();
    /* first focus after the page has had idle time to build the index */
    const dom2 = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html',
      beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
    await sleep(3000);
    t0 = dom2.window.performance.now(); dom2.window.document.getElementById('find-q').focus();
    out.firstFocusAfterIdle.push(+(dom2.window.performance.now() - t0).toFixed(1));
    dom2.window.close();
  }
  console.log(JSON.stringify(out));
})();
