#!/usr/bin/env node
/* The search index of a book whose reference lives in companion pages: each built page loaded with its own scripts,
   the reader asked for its search units (qh:reader-units), each unit addressed in its page.

       NODE_PATH=<jsdom> node --max-old-space-size=8192 tools/reader-index.cjs <out reader-index.js> <page.html>...

   The page names written are the files' base names, as the pages link to one another. Reads the pages and writes only
   <out>. Prints the units per page and part, and the sha256 of the output. */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { JSDOM, VirtualConsole } = require('jsdom');
const [out, ...pages] = process.argv.slice(2);
if (!out || !pages.length) { console.error('usage: reader-index.cjs <out reader-index.js> <page.html>...'); process.exit(2); }
(async () => {
  const units = [];
  for (const file of pages) {
    const name = path.basename(file);
    const errors = [];
    const vc = new VirtualConsole();
    vc.on('jsdomError', e => { if (!/Not implemented/.test(String(e && e.message))) errors.push(String(e && e.message || e)); });
    const dom = new JSDOM(fs.readFileSync(file, 'utf8'), {
      url: 'https://example.org/' + name,
      runScripts: 'dangerously',
      pretendToBeVisual: true,
      virtualConsole: vc,
      beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; w.scrollTo = function () {}; }
    });
    await new Promise(r => setTimeout(r, 80));
    const ev = new dom.window.CustomEvent('qh:reader-units', { detail: {} });
    dom.window.document.dispatchEvent(ev);
    const got = ev.detail.units;
    if (!Array.isArray(got)) { console.error(`${name}: the reader did not answer (is reader.js in the page?)`); process.exit(1); }
    if (errors.length) { console.error(`${name}: script errors: ${errors.slice(0, 3).join(' | ')}`); process.exit(1); }
    const per = {};
    JSON.parse(JSON.stringify(got)).forEach(x => { x.page = name; units.push(x); per[x.group] = (per[x.group] || 0) + 1; });
    console.log(name, Object.entries(per).map(([g, n]) => `${g} ${n}`).join(', '));
    dom.window.close();
    if (global.gc) global.gc();
  }
  const text = 'window.QH_READER_INDEX = ' + JSON.stringify({ units }) + ';\n';
  fs.writeFileSync(out, text);
  console.log(`${units.length} units, ${text.length} bytes, sha256 ${crypto.createHash('sha256').update(text).digest('hex')} ${out}`);
})();
