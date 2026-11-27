'use strict';
const assert = require('node:assert/strict');
const {createHash} = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');

const site = path.resolve(process.argv[2]);
const source = process.argv[3] || path.resolve(__dirname, '../source-tree/content/quantum-holography-status');
const indexed = fs.readFileSync(path.join(site, 'reader-index.js'), 'utf8');
const units = JSON.parse(indexed.replace(/^window.QH_READER_INDEX = /, '').trimEnd().replace(/;$/, '')).units;
const expected = JSON.parse(fs.readFileSync(path.join(source, 'atlas.json'), 'utf8'));
const hashes = {};
function openPage(name) {
  const raw = fs.readFileSync(path.join(site, name));
  hashes[name] = createHash('sha256').update(raw).digest('hex');
  return new JSDOM(raw.toString()).window.document;
}
function formulae(element) {
  assert.ok(element);
  return Array.from(element.querySelectorAll('math annotation[encoding="application/x-tex"]'), node => node.textContent.trim());
}
function containsMath(element, fragments) {
  const tex = formulae(element).join('\n').replace(/\s/g, '');
  for (const fragment of fragments) {
    assert.ok(tex.includes(fragment), 'Missing typeset expression ' + fragment + ' in ' + element.id);
  }
}
function prose(element) {
  const body = element.cloneNode(true);
  body.querySelectorAll('annotation,script,style,template').forEach(node => node.remove());
  return body.textContent.replace(/\s+/g, ' ');
}
const book = openPage('index.html');
const reference = openPage('reference.html');
const atlas = openPage('atlas.html');
const ids = ['coupled-irregular-four-point-flags', 'w4-marked-quartic-negative-three-halves',
             'k3-straight-products-over-the-marked-field'];
for (const id of ids) {
  const item = expected.claims.find(claim => claim.id === id);
  assert.ok(item, 'Missing reviewed source claim ' + id);
  const card = atlas.querySelector('article[data-claim-id="' + id + '"]');
  assert.ok(card, 'Missing visible atlas claim ' + id);
  assert.equal(card.dataset.statusCode, item.status.code);
  assert.equal(item.status.code, 'checked');
  const published = new Set(formulae(card));
  const authored = [item.statement, ...item.hypotheses].join('\n');
  for (const match of authored.matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g)) {
    const actual = (match[1] ?? match[2]).trim();
    assert.ok(published.has(actual), 'Atlas omitted source mathematics for ' + id + ': ' + actual);
  }
  assert.ok(units.some(unit => unit.id === card.id && unit.page === 'atlas.html' && unit.title === item.title),
            'Claim not retrievable by its published title ' + id);
}
const four = book.getElementById('ch04');
containsMath(four, ['i^!C[1]', '(1,9,31,23)', '(0,4,24,20)', '(1,4,5,2)', '(0,2,4,2)',
                    '(1,5,8,4)', '(0,2,6,4)', '(0,1,3,2)', '(0,0,2,2)']);
assert.match(prose(four), /Stokes/);
const w4 = book.getElementById('ch12');
containsMath(w4, ['-3/2', '6\\gamma', '\\gamma=0']);
assert.match(prose(w4), /homotopy abelian/i);
assert.match(prose(w4), /Hochschild/i);
const k3 = book.getElementById('ch15');
containsMath(k3, ['2w+1', 'E^{m+1}=0', '190']);
assert.match(prose(k3), /Witt index/);
for (const section of [book.getElementById('ch18'), reference.getElementById('frontier-comparisons')]) {
  containsMath(section, ['24053.108799478066244']);
  const visible = prose(section);
  for (const phrase of [/finite grid/i, /positive diagonal/i, /uniformly bounded endpoint norm products/i]) {
    assert.ok(phrase.test(visible), 'Missing finite-grid qualification ' + phrase + ' in ' + section.id);
  }
}
console.log(JSON.stringify({status:'PASS',files:hashes,searchable_reviewed_claims:ids,
  checks:['all eight flag image and target tuples','signed quartic obstruction, vanishing and Hochschild consequence',
          'sharp Witt-index bound and two complex components','positive-width norm bound and finite interpolation']}, null, 2));
