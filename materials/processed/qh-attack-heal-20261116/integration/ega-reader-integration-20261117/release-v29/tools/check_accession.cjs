'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

function matchingRecord(object, id, records = []) {
  if (!object || typeof object !== 'object') return records;
  if (object.id === id) records.push(object);
  for (const child of Object.values(object)) matchingRecord(child, id, records);
  return records;
}

function uniqueAddress(doc, id) {
  const found = [...doc.querySelectorAll('[id]')].filter((node) => node.id === id);
  assert.equal(found.length, 1, 'expected one rendered address #' + id);
  return found[0];
}

function sourceMath(item) {
  return [...item.matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g)]
    .map((match) => (match[1] ?? match[2]).trim());
}

module.exports = function checkAccession({ source, book, reference, atlas, units, formulae, prose, containsMath }) {
  const expected = JSON.parse(fs.readFileSync(path.join(__dirname, '../verification/ACCESSION-CHECKS.json')));
  const claims = JSON.parse(fs.readFileSync(path.join(source, 'atlas.json'))).claims;
  const statements = JSON.parse(fs.readFileSync(path.join(source, 'content.json')));
  const pages = { 'index.html': book, 'reference.html': reference, 'atlas.html': atlas };
  const routes = [];
  function route(page, id, title) {
    assert.ok(title && title.length > 5, id);
    const matches = units.filter((unit) => unit.page === page && unit.id === id);
    assert.ok(matches.some((unit) => unit.title === title), 'missing search candidate for ' + page + '#' + id);
    return { page, id, title };
  }
  for (const { id, file } of expected.headings) {
    const marker = ' {#' + id + '}';
    const authored = fs.readFileSync(path.join(source, file), 'utf8').split('\n').filter((line) => /^#{1,6}\s/.test(line) &&
      line.trimEnd().endsWith(marker));
    assert.equal(authored.length, 1, file + '#' + id);
    const heading = uniqueAddress(book, id);
    assert.match(heading.localName, /^h[1-6]$/);
    routes.push({ ...route('index.html', id, prose(heading).trim()), type: 'chapter-heading' });
  }
  for (const id of expected.claims) {
    const authored = claims.filter((claim) => claim.id === id);
    assert.equal(authored.length, 1, id);
    const item = authored[0];
    const card = uniqueAddress(atlas, 'atlas-c-' + id);
    assert.equal(card.dataset.claimId, id);
    assert.equal(card.dataset.statusCode, item.status.code);
    assert.ok(prose(card).includes(item.status.label), 'missing reviewed grade for ' + id);
    const rendered = new Set(formulae(card));
    for (const tex of sourceMath([item.statement, ...item.hypotheses].join('\n'))) {
      assert.ok(rendered.has(tex), 'atlas omitted reviewed formula for ' + id + ': ' + tex);
    }
    const qualification = card.querySelector('.atlas-note-source');
    const pill = card.querySelector('.atlas-chip');
    const searchGrade = Boolean(qualification && prose(qualification).includes(item.status.label) &&
      !(pill && prose(pill).includes(item.status.label)));
    routes.push({ ...route('atlas.html', card.id, item.title), type: 'atlas-claim', claim: id,
      grade: item.status, searchGrade });
  }
  for (const id of expected.reference) {
    const authored = matchingRecord(statements, id);
    assert.equal(authored.length, 1, id);
    const card = uniqueAddress(reference, 's-' + id);
    assert.equal(card.dataset.status, authored[0].status);
    const title = prose(card.querySelector('.statement-title')).trim();
    routes.push({ ...route('reference.html', card.id, title), type: 'reference-statement', grade: authored[0].status });
  }
  for (const { page, id, math, text } of expected.probes) {
    const section = uniqueAddress(pages[page], id);
    containsMath(section, math);
    const rendered = prose(section);
    for (const phrase of text) assert.ok(rendered.includes(phrase), 'missing reviewed scope in ' + id + ': ' + phrase);
  }
  assert.ok(routes.length && expected.probes.length);
  return { routes, scientificProbes: expected.probes.map(({ page, id }) => ({ page, id })) };
};
