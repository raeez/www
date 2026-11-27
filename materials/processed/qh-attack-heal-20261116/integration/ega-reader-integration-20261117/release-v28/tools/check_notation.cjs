'use strict';

const assert = require('node:assert/strict');
const {execFileSync} = require('node:child_process');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');

const [pagePath, manifestPath] = process.argv.slice(2);
const binding = JSON.parse(execFileSync(process.env.PYTHON || 'python3',
  ['-B', path.join(__dirname, 'source_reading.py'), manifestPath], {encoding:'utf8'}));
const raw = fs.readFileSync(pagePath);
const page = new JSDOM(raw.toString('utf8'));
const doc = page.window.document;
const normalize = text => text.replace(/\s+/gu, ' ').trim();
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const fragment = text => JSDOM.fragment(text);

function visible(node) {
  const copy = node.cloneNode(true);
  copy.querySelectorAll('math').forEach(m => m.replaceWith('⟨math⟩'));
  copy.querySelectorAll('script,style,template,[aria-hidden="true"]').forEach(n => n.remove());
  return normalize(copy.textContent);
}
function math(node) {
  return [...node.querySelectorAll('math')].map(m => {
    const annotation = m.querySelector('semantics > annotation[encoding="application/x-tex"]');
    assert.ok(annotation && m.querySelector('semantics > :not(annotation)'), 'missing visible MathML or TeX equivalent');
    assert.equal(m.querySelector('merror'), null, 'invalid mathematical notation');
    return {tex:annotation.textContent.trim(), display:m.getAttribute('display') === 'block'};
  });
}
function signature(node) {
  const links = [...node.querySelectorAll('a[href]')].map(a => {
    const href = a.getAttribute('href');
    // The three split pages keep the authored fragment IDs and supply the target filename.
    return [href.replace(/^(?:index|reference|atlas)\.html#/, '#'), visible(a)];
  });
  return {text:visible(node), math:math(node), links};
}
const front = doc.querySelector('.mg-front-intro');
assert.ok(front);
assert.equal(visible(doc.querySelector('.mg-front-title')), normalize(binding.title));
assert.equal(visible(doc.querySelector('.mg-front-subtitle')), normalize(binding.subtitle));
const placements = new Map(binding.front_figures.map(entry => [entry.id,entry.after_paragraph]));
let paragraph = 0;
const reading = [];
for (const block of front.children) {
  if (placements.has(block.id)) {
    assert.equal(paragraph, placements.get(block.id), 'illustration differs from its authored location');
    assert.equal(block.localName, 'figure');
    math(block);
    placements.delete(block.id);
  } else {
    if (block.localName === 'p') paragraph++;
    reading.push(block);
  }
}
assert.equal(placements.size, 0, 'a declared front figure is missing');
const expected = [...fragment(binding.reference).children];
assert.deepEqual(reading.map(signature), expected.map(signature), 'visible reading or its mathematical notation differs from its source');
const files = new Map([[path.basename(pagePath),doc]]);
const destinations = [];
for (const block of reading) for (const a of block.querySelectorAll('a[href]')) {
  const href = a.getAttribute('href');
  const [file,id] = href.split('#');
  if (id === undefined) continue;
  const target = file || path.basename(pagePath);
  if (!files.has(target)) {
    assert.ok(['index.html','reference.html','atlas.html'].includes(target), 'unknown local reading destination: ' + href);
    files.set(target,new JSDOM(fs.readFileSync(path.join(path.dirname(pagePath),target),'utf8')).window.document);
  }
  assert.ok(files.get(target).getElementById(decodeURIComponent(id)), 'broken authored reading destination: ' + href);
  destinations.push(href);
}
const chapterChecks = [];
for (const chapter of binding.chapters) {
  const article = doc.getElementById(chapter.id);
  assert.ok(article && article.matches('article[data-chapter]'), chapter.id);
  assert.equal(visible(article.querySelector('.mg-ch-title')), chapter.title);
  if (chapter.first_html) {
    const first = [...article.querySelectorAll('.mg-ch-open p')].find(p => !p.closest('figure'));
    assert.ok(first, 'no expected chapter opening in ' + chapter.id);
    assert.deepEqual(signature(first), signature(fragment(chapter.first_html).firstElementChild), 'authored opening in ' + chapter.id);
  }
  const forms = math(article);
  if (chapter.has_math) assert.ok(forms.length, 'authored chapter mathematics missing in ' + chapter.id);
  chapterChecks.push({id:chapter.id,title:chapter.title,formulas:forms.length});
}
assert.equal(doc.querySelectorAll('article[data-chapter]').length,binding.chapters.length);
const forms = reading.flatMap(math);
const report = {status:'PASS',file:path.resolve(pagePath),reader_sha256:sha(raw),
  introduction_sha256:sha(Buffer.from(binding.introduction)),accepted_opening_blocks:reading.length,
  opening_math_occurrences:forms.length,opening_displays:forms.filter(m=>m.display).length,
  opening_formula_in_lead:!!front.querySelector('.mg-lead math'),placed_front_figures:binding.front_figures,
  checked_opening_destinations:destinations,chapters:chapterChecks};
for (const document of files.values()) document.defaultView.close();
console.log(JSON.stringify(report,null,2));
