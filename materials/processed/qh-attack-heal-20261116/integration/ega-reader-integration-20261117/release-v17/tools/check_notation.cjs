'use strict';
// Parse the shipped, static MathML without executing the site or loading its search index.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const { JSDOM } = require('jsdom');

const file = path.resolve(process.argv[2]);
const expected = JSON.parse(fs.readFileSync(process.argv[3], 'utf8')).introduction;
const sourceExpressions = Array.from(expected.matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g),
  m => (m[1] ?? m[2]).trim());
const digest = b => crypto.createHash('sha256').update(b).digest('hex');
const bytes = fs.readFileSync(file);
const { document } = new JSDOM(bytes.toString()).window;
const front = document.querySelector('.mg-front-intro');
assert.ok(front, 'published book introduction missing');
const annotations = Array.from(front.querySelectorAll('math annotation[encoding="application/x-tex"]'));
const shipped = annotations.map(a => a.textContent.trim());
assert.deepEqual(shipped, sourceExpressions, 'a front-page mathematical expression was lost or altered');
const displays = Array.from(front.querySelectorAll('math[display="block"]'));
assert.equal(displays.length, 3);
assert.ok(front.querySelector('p.mg-lead math'), 'no typeset expression in the opening sentence');
for (const display of displays) {
  assert.ok(display.querySelector('semantics > :not(annotation)'), 'display has no visible MathML');
  assert.equal(display.querySelector('merror'), null, 'invalid display');
}
const first = displays[0].querySelector('annotation').textContent;
const second = displays[1].querySelector('annotation').textContent;
const third = displays[2].querySelector('annotation').textContent;
assert.ok(first.includes('J_{-1}^2') && first.includes('J_{-2}') && first.includes('sqrt{2}'));
assert.ok(second.includes('J_{-1}^2J_2+J_{-2}J_1^2') && second.includes('\\pm2'));
assert.ok(third.includes('j_*j^*') && third.includes('\\Delta_*L'));
const targets = Array.from(front.querySelectorAll('a[href^="#"]'), a => a.hash.slice(1));
assert.ok(targets.length >= 3);
for (const id of targets) assert.ok(document.getElementById(id), 'broken opening reference ' + id);
const copy = front.cloneNode(true);
copy.querySelectorAll('math').forEach(n => n.remove());
assert.equal(/\\[()[\]]|\\(?:frac|Delta|mathcal)\b/.test(copy.textContent), false);
const chapters = Array.from(document.querySelectorAll('article[data-chapter]'), ch => {
  const formulas = Array.from(ch.querySelectorAll('math'));
  assert.ok(formulas.length > 0, 'empty chapter MathML: ' + ch.id);
  assert.equal(ch.querySelector('merror'), null);
  return { id: ch.id, formulas: formulas.length };
});
assert.equal(chapters.length, 18);
console.log(JSON.stringify({ file, reader_sha256: digest(bytes), introduction_tex_sha256: digest(expected),
  status: 'PASS', typeset_front_expressions: shipped.length, front_displays: displays.length,
  formula_in_lead: true, opening_destinations: targets, chapters }, null, 2));
