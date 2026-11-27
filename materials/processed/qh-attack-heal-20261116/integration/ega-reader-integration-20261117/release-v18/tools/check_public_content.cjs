'use strict';
// The compatibility amendment may add addresses and notice metadata.
// Every scientific passage, expression and authored destination must survive.
const { JSDOM } = require('jsdom');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const [raw, amended] = process.argv.slice(2);
const h = x => crypto.createHash('sha256').update(x).digest('hex');
const norm = t => t.replace(/\s+/g,' ').trim();
function facts(file) {
  const dom = new JSDOM(fs.readFileSync(file,'utf8'));
  const doc = dom.window.document;
  const roots = [...doc.querySelectorAll('.mg-front-intro, article[data-chapter], article[data-claim-id], [data-reference]')];
  const rows = roots.map(r => {
    const node = r.cloneNode(true);
    node.querySelectorAll('script,style,template').forEach(e=>e.remove());
    const formulas = Array.from(node.querySelectorAll('math'), e=>e.outerHTML);
    const ids = [...node.querySelectorAll('h2[id], h3[id], h4[id], [data-claim-id]')].map(e=>e.id);
    return [r.id || r.className, h(norm(node.textContent)), h(formulas.join('\n')), formulas.length,ids];
  });
  dom.window.close();
  return rows;
}
const records = {};
for (const file of ['index.html','reference.html','atlas.html']) {
  const before=facts(path.join(raw,file));
  const after=facts(path.join(amended,file));
  assert.ok(before.length, 'no scientific roots in ' + file);
  assert.deepEqual(after,before,'a reader passage, formula or authored heading changed in ' + file);
  records[file] = {matched_roots:before.length, matched_formula_occurrences:before.reduce((v,r)=>v+r[3],0),
    exact_corpus_digest:h(JSON.stringify(before))};
}
console.log(JSON.stringify({status:'PASS',records},null,2));
