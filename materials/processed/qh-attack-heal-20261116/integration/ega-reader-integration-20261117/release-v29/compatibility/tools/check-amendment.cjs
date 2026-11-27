#!/usr/bin/env node
'use strict';

const assert = require('node:assert/strict');
const { createHash } = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM, VirtualConsole, requestInterceptor } = require('jsdom');
const { planFor } = require('./build-amendment.cjs');

assert.ok(process.argv.length === 3 ||
  ([5, 6].includes(process.argv.length) && process.argv[3] === '--resume-v29'),
  'usage: check-amendment.cjs AMENDED_PUBLIC [--resume-v29 EXACT_RECEIPT [physical|history]]');
const site = fs.realpathSync(process.argv[2]);
const base = 'https://research.momentum.inc/quantum-holography/';
const report = JSON.parse(fs.readFileSync(site + '-receipt.json', 'utf8'));
const index = fs.readFileSync(path.join(site, 'reader-index.js'));
const pageText = new Map(report.results.map(({ page }) => [page, fs.readFileSync(path.join(site, page), 'utf8')]));
const pin = (text) => ({ sha256: createHash('sha256').update(text).digest('hex'), bytes: Buffer.byteLength(text) });
for (const { page, after } of report.results) assert.deepEqual(pin(pageText.get(page)), after);
assert.deepEqual(pin(index), report.outputIndex);

const checks = [];

function resumeLeading(filename) {
  const proof = JSON.parse(fs.readFileSync(filename, 'utf8'));
  assert.equal(proof.schema, 'qh-v29-runtime-resume/1');
  assert.equal(proof.release, site);
  const original = fs.readFileSync(proof.original.path);
  const failure = fs.readFileSync(proof.failure.path);
  assert.deepEqual(pin(original), { bytes: proof.original.bytes, sha256: proof.original.sha256 });
  assert.deepEqual(pin(failure), { bytes: proof.failure.bytes, sha256: proof.failure.sha256 });
  assert.equal(proof.original.sha256, '9b76e43cf3a79e1c540bd02b06eb3d5404324dbe458480d6966cdd0f40818c80');
  assert.equal(proof.failure.sha256, '7d04ac3ce119eec4c85f624eed9ec862fd91b4852e2d30d8b637737387d16352');
  assert.deepEqual(pin(fs.readFileSync(site + '-receipt.json')), proof.amendment);
  assert.deepEqual(proof.rawFiles, report.inputs.raw);
  for (const [name, expected] of Object.entries(proof.rawFiles)) {
    assert.deepEqual(pin(fs.readFileSync(path.join(proof.raw, name))), expected);
  }
  assert.deepEqual(proof.files, Object.fromEntries(report.results.map(({ page, after }) => [page, after])));
  assert.deepEqual(proof.index, report.outputIndex);
  const first = '  assertAliases();\n';
  const last = '  const unchanged = book.compatibility.find';
  const baseline = original.toString();
  const prefix = baseline.slice(baseline.indexOf(first), baseline.indexOf(last)).trimEnd();
  const replacement = fs.readFileSync(__filename, 'utf8');
  const newPrefix = replacement.slice(replacement.indexOf(first),
    replacement.indexOf('\n}\n\nasync function checkPhysicalBookmarks')).trimEnd();
  assert.ok(prefix.startsWith(first));
  assert.equal(newPrefix, prefix, 'Previously reached runtime code changed');
  return {
    original_checker: proof.original,
    original_failure: proof.failure,
    reached_assertion: 'check-amendment.cjs:316',
    byte_identical_leading_code: pin(prefix),
    raw: proof.rawFiles,
    portable: proof.files,
    index: proof.index,
  };
}
function open(page, suffix) {
  const scrolls = [], scrollTargets = [], departures = [], errors = [];
  const virtualConsole = new VirtualConsole();
  virtualConsole.on('jsdomError', (error) => errors.push(error.message));
  const resources = { interceptors: [requestInterceptor((req) => req.url === base + 'reader-index.js' ?
    new Response(index, { headers: { 'Content-Type': 'application/javascript' } }) : new Response('', { status: 404 }))] };
  const dom = new JSDOM(pageText.get(page), {
    url: new URL(suffix, base).href, runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole, resources,
    beforeParse(window) {
      window.Element.prototype.scrollIntoView = function () { scrolls.push(this.id); scrollTargets.push(this); };
      window.scrollTo = function () {};
      window.addEventListener('qh:leave', (event) => {
        departures.push(JSON.parse(JSON.stringify(event.detail)));
        event.preventDefault();
      }, true);
    }
  });
  return { window: dom.window, doc: dom.window.document, scrolls, scrollTargets, departures, errors };
}

async function scenario(name, page, suffix, check) {
  const session = open(page, suffix);
  try {
    const evidence = await check(session);
    assert.deepEqual(session.errors, [], `${name} produced runtime errors`);
    checks.push({ name, ...evidence });
  } finally {
    session.window.close();
    await new Promise((resolve) => setImmediate(resolve));
    if (global.gc) global.gc();
  }
}

function query(session) {
  return new URL(session.window.location.href).searchParams.get('q');
}

function assertSearch(session, words) {
  assert.equal(query(session), words);
  assert.equal(session.doc.getElementById('reader-q').value, words);
  assert.equal(session.doc.getElementById('reader-search').hidden, false);
}

function assertDeparture(session, file, words, id) {
  assert.equal(session.departures.length, 1);
  const { url, how } = session.departures[0];
  const dest = new URL(url, session.window.location.href);
  assert.equal(dest.origin, new URL(base).origin);
  assert.equal(dest.pathname, new URL(file, base).pathname);
  assert.equal(dest.searchParams.get('q'), words);
  assert.equal(dest.hash, '#' + id);
  assert.equal(how, 'replace');
  return { destination: dest.href };
}

const passage = 'ch04-irregular-collision';
const claim = 'atlas-c-horizontal-occupied-deletion-all-slots';
const conflict = 'ch05-ordered-cuts-give-a-finite-geometric-bar-construction-p13';
const predecessor = (doc) => doc.querySelector('.reader-notice[data-notice="predecessor"]');
const stableV16 = 'ch18-passage-afaa1cd3efc8e7012cca';
const oldCommonTail = 'ch18-passage-257007e06254976b6e04';
const commonTailEnclosure = 'problem-physical-adjunction';
const currentCommonTail = 'ch18-passage-1d16563940e431537022';
const commonTailTheorem = 'ch06-common-tail-completeness';
const revisedV16 = 'ch18-passage-2bc5ee4a0eae303e0289';
const noteScope = 'row-w-algebras-object-scope';
const gridNotes = [
  ['examples-passage-3f8121a5894569b871ca-5', 'object', 'Algebra and geometry: Partial'],
  ['examples-passage-3f8121a5894569b871ca-6', 'dual', 'Koszul dual: Partial'],
  ['examples-passage-3f8121a5894569b871ca-7', 'modules', 'Module comparison: Partial'],
  ['examples-passage-f707aa7427949e68b1db-3', 'fusion', 'Fusion and exchange: Published'],
  ['examples-passage-3f8121a5894569b871ca-8', 'bulk', 'Bulk operations: Partial'],
  ['examples-passage-f707aa7427949e68b1db-4', 'lines', 'Lines and endpoints: Published']
].map(([id, column, label]) => ({ id, column, label: 'W-algebras and quantum Drinfeld–Sokolov reduction, ' + label }));
const { id: noteMeaning, label: noteLabel } = gridNotes[0];
const reviewedV18RawIndex = '2c3f4047c91253dbc8af787b2b56f00668a2f8c5207d14fccebbd3aca137b741';

function assertCellCard(session, id, expectedLabel) {
  const { doc, scrollTargets, window } = session;
  assert.equal(window.location.hash, '#' + id);
  const target = doc.getElementById(id);
  const source = target.closest('.cell-note');
  const trigger = source.parentElement.querySelector('.cell-btn');
  const card = doc.getElementById('card');
  assert.equal(doc.querySelectorAll('[id="' + id + '"]').length, 1);
  assert.equal(source.hidden, true);
  assert.equal(card.hidden, false);
  if (expectedLabel) assert.equal(trigger.getAttribute('aria-label'), expectedLabel);
  assert.equal(trigger.getAttribute('aria-expanded'), 'true');
  assert.equal(card.querySelector('.' + target.classList[0]).textContent, target.textContent);
  assert.ok(scrollTargets.includes(trigger));
  assert.equal(predecessor(doc), null);
  return { trigger, card };
}

async function traverse(window, step) {
  await new Promise((resolve, reject) => {
    const timeout = setTimeout(() => reject(new Error(`${step} did not complete`)), 2000);
    window.addEventListener('popstate', () => { clearTimeout(timeout); resolve(); }, { once: true });
    window.history[step]();
  });
}

function assertAliases() {
  const owners = new Map();
  const sourceIds = new Map();
  const metadata = (markup, id) => {
    const hits = [...markup.matchAll(new RegExp(`<script type="application/json" id="${id}">(.*?)</script>`, 'gs'))];
    assert.ok(hits.length <= 1, `duplicate metadata ${id}`);
    return hits.length ? JSON.parse(hits[0][1]) : {};
  };
  for (const [page, markup] of pageText) {
    const body = markup.replace(/<script\b[^>]*>[\s\S]*?<\/script>|<style\b[^>]*>[\s\S]*?<\/style>/g, '');
    sourceIds.set(page, new Set([...body.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1])));
    const aliases = [...Object.keys(metadata(markup, 'reader-redirects')), ...Object.keys(metadata(markup, 'reader-predecessors'))];
    for (const alias of aliases) {
      assert.ok(!owners.has(alias), `duplicate alias #${alias}`);
      owners.set(alias, page);
    }
  }
  for (const [id] of owners) {
    for (const [page, ids] of sourceIds) assert.ok(!ids.has(id), `alias #${id} shadows ${page}`);
  }
  for (const [, markup] of pageText) {
    for (const { href, ids, aliases = [] } of metadata(markup, 'reader-pages').pages) {
      assert.equal(new Set(aliases).size, aliases.length);
      assert.ok(aliases.every((id) => owners.get(id) === href && !ids.includes(id)));
    }
  }
  const control = { addresses: new Map(), allIds: new Set(['authored', 'target']), authored: new Set(['authored', 'target']),
    inherited: {}, inheritedPredecessors: {}, issued: new Set() };
  assert.throws(() => planFor('index.html', [], { ...control, inherited: { authored: 'target' } }), /would shadow/);
  assert.throws(() => planFor('index.html', [], { ...control, inherited: { saved: 'target' },
    inheritedPredecessors: { saved: { targets: ['target'], ambiguous: false } } }), /would shadow/);
  checks.push({ name: 'alias maps have one owner and cannot shadow current addresses', aliases: owners.size });
}

async function leadingScenarios() {
  assertAliases();
  const words = 'irregular collision';
  let afterLoad;
  await scenario('chapter address keeps the query at startup', 'index.html', '?q=irregular+collision#' + passage, (session) => {
    assertSearch(session, words);
    assert.ok(session.scrolls.includes(passage));
    afterLoad = session.window.location.href;
    return { destination: afterLoad };
  });
  await scenario('fresh reload keeps the query and heading', 'index.html', afterLoad, (session) => {
    assertSearch(session, words);
    assert.equal(session.window.location.hash, '#' + passage);
  });
  await scenario('remote claim keeps its query on ownership redirect', 'index.html', '?q=obstruction#' + claim,
    (session) => assertDeparture(session, 'atlas.html', 'obstruction', claim));
  await scenario('companion sends its query back to the book', 'reference.html', 'reference.html?q=irregular+collision#' + passage,
    (session) => assertDeparture(session, 'index.html', words, passage));
  await scenario('a historical companion address retains its query on the owner redirect', 'index.html', '?q=Koszul#examples-p133',
    (session) => assertDeparture(session, 'reference.html', 'Koszul', 'examples-p133'));
  const bracket = String.raw`[a_\lambda b]+[b_\lambda a]`;
  const encodedBracket = '?q=' + encodeURIComponent(bracket);
  await scenario('a shared bracket query preserves its literal brackets, plus and TeX on startup', 'index.html',
    encodedBracket + '#' + passage, (session) => {
      assertSearch(session, bracket);
      assert.equal(session.window.location.hash, '#' + passage);
      assert.ok(session.window.location.href.includes('%2B'));
    });
  await scenario('a bracket query crosses to an older companion fragment intact', 'index.html', encodedBracket + '#examples-p133',
    (session) => assertDeparture(session, 'reference.html', bracket, 'examples-p133'));
  if (report.inputs.historic.matchIssuedEnclosures) {
    const reference = report.results.find(({ page }) => page === 'reference.html');
    const detailId = 'examples-passage-8d9e778d816d13729c70-15';
    const detail = reference.compatibility.find(({ id }) => id === detailId);
    assert.equal(detail.role, 'retained');
    assert.ok(detail.origins.some((origin) => origin.edition === 'v17' && origin.enclosure?.[1] === 's-critical-translation-cone-cohomology'));
    await scenario('a repeated label keeps its v17 address inside its authored statement', 'reference.html',
      'reference.html#' + detailId, (session) => {
        const target = session.doc.getElementById(detailId);
        assert.ok(target.closest('#s-critical-translation-cone-cohomology'));
        assert.equal(target.closest('details').open, true);
        assert.match(target.textContent, /Hypotheses/);
        assert.ok(session.scrolls.includes(detailId));
        assert.equal(predecessor(session.doc), null);
        return { address: detailId };
      });
    const note = reference.compatibility.find(({ id }) => id === noteMeaning);
    assert.equal(note.role, 'retained');
    assert.ok(note.origins.some((origin) => origin.edition === 'v17' && origin.enclosure?.[0] === 'cell'));
    const knownCells = gridNotes.filter(({ id, column }) => reference.compatibility.some((record) =>
      record.id === id && record.role === 'retained' && record.origins.some((origin) => origin.edition === 'v17' &&
        origin.enclosure?.[0] === 'cell' && origin.enclosure[1] === 'row-w-algebras' && origin.enclosure[2] === column)));
    if (report.inputs.raw['reader-index.js'].sha256 === reviewedV18RawIndex) assert.deepEqual(knownCells, gridNotes);
    await scenario('repeated v17 card labels open their separately authored cells', 'reference.html', 'reference.html#examples', (session) => {
      for (const { id, label } of knownCells) {
        const navigate = new session.window.CustomEvent('qh:navigate', { detail: { id }, cancelable: true });
        assert.equal(session.doc.dispatchEvent(navigate), false);
        const { trigger } = assertCellCard(session, id, label);
        assert.equal(session.doc.activeElement, trigger);
      }
      return { addresses: knownCells.map(({ id }) => id) };
    });
    await scenario('a shared bracket query crosses to the retained table card address', 'index.html', encodedBracket + '#' + noteMeaning,
      (session) => assertDeparture(session, 'reference.html', bracket, noteMeaning));
    await scenario('a shared table note opens its visible cell card and preserves URL and query', 'reference.html',
      'reference.html' + encodedBracket + '#' + noteMeaning, (session) => {
        assertSearch(session, bracket);
        assertCellCard(session, noteMeaning, noteLabel);
        return { address: noteMeaning };
      });
    const phrase = 'higher and non-principal comparisons open';
    await scenario('a table search hit shows its card and restores search and keyboard focus through Back and Forward', 'reference.html',
      'reference.html?q=' + encodeURIComponent(phrase) + '#examples', async (session) => {
        const { doc, window } = session;
        assertSearch(session, phrase);
        const hit = doc.querySelector(`.reader-hit-link[href="#${noteScope}"]`);
        assert.ok(hit, 'the actual cell scope is a search result');
        hit.click();
        const { trigger, card } = assertCellCard(session, noteScope, noteLabel);
        assert.equal(doc.activeElement, trigger);
        await traverse(window, 'back');
        assertSearch(session, phrase);
        assert.equal(window.location.hash, '#examples');
        assert.equal(doc.activeElement.getAttribute('href'), '#' + noteScope);
        assert.equal(card.hidden, true);
        await traverse(window, 'forward');
        assertCellCard(session, noteScope, noteLabel);
        assert.equal(doc.activeElement, trigger);
        trigger.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'Tab', bubbles: true, cancelable: true }));
        assert.ok(card.contains(doc.activeElement));
        doc.activeElement.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'Escape', bubbles: true, cancelable: true }));
        assert.equal(card.hidden, true);
        assert.equal(doc.activeElement, trigger);
        return { address: noteScope, cell: noteLabel };
      });
  } else if (report.results.find(({ page }) => page === 'reference.html').after.sha256 ===
    '045755e54c2e0d5bef8b4b3742837611d82f92b4670c5beed8256cabd6e79cfa') {
    await scenario('the dated v17 control reaches a hidden table template without opening its card', 'reference.html',
      'reference.html' + encodedBracket + '#' + noteMeaning, (session) => {
        assertSearch(session, bracket);
        assert.equal(session.doc.getElementById(noteMeaning).closest('.cell-note').hidden, true);
        assert.equal(session.doc.getElementById('card').hidden, true);
        assert.ok(session.scrolls.includes(noteMeaning));
        return { address: noteMeaning };
      });
  }
  await scenario('actual atlas address keeps the query', 'atlas.html', 'atlas.html?q=obstruction#' + claim, (session) => {
    assertSearch(session, 'obstruction');
    assert.equal(session.window.location.hash, '#' + claim);
  });
  const title = 'An irregular collision can detect a hidden extension';
  await scenario('a companion lazily loads a heading hit from the amended search index', 'reference.html',
    'reference.html?q=' + encodeURIComponent(title), async (session) => {
      const href = 'index.html#' + passage;
      let hit;
      for (let turn = 0; turn < 30 && !hit; turn++) {
        hit = session.doc.querySelector(`.reader-hit-link[href="${href}"]`);
        if (!hit) await new Promise((resolve) => setTimeout(resolve, 30));
      }
      assert.ok(hit);
      hit.click();
      assert.equal(session.departures[0].how, 'assign');
      assert.equal(new URL(session.departures[0].url, session.window.location.href).href, base + href);
      assert.equal(session.window.history.state.reader.q, title);
    });

  const book = report.results.find((record) => record.page === 'index.html');
  const history = report.inputs.historic.editions.map(({ edition }) => edition);
  if (history.includes('v17')) {
    const issued = report.results.flatMap(({ page, compatibility }) => compatibility
      .filter(({ origins }) => origins.some((origin) => origin.edition === 'v17')).map((record) => ({ page, ...record })));
    const firstEdition = (origins) => history.find((edition) => origins.some((origin) => origin.edition === edition));
    const retained = issued.find(({ role, origins }) => role === 'retained' && firstEdition(origins) === 'v17');
    assert.ok(retained, 'expected a retained locator whose earliest published origin is v17');
    const pathPrefix = (page) => page === 'index.html' ? '' : page;
    await scenario('a bookmark first issued in v17 retains its exact fragment', retained.page,
      pathPrefix(retained.page) + '#' + retained.id, (session) => {
        assert.equal(session.window.location.hash, '#' + retained.id);
        assert.deepEqual(retained.targets, [retained.id]);
        assert.equal(predecessor(session.doc), null);
        assert.ok(session.scrolls.includes(retained.id));
        return { address: retained.id, first_edition: firstEdition(retained.origins),
          observed_editions: retained.origins.map(({ edition }) => edition) };
      });
    const changed = issued.find(({ role, origins }) => role === 'changed' && origins.some((origin) => origin.match === 'advanced_with_source')) ||
      issued.find(({ role }) => role === 'changed');
    if (changed) {
      await scenario('a revised v17 bookmark gives an explicit current locator', changed.page,
        pathPrefix(changed.page) + '#' + changed.id, (session) => {
          assert.equal(session.window.location.hash, '#' + changed.id);
          const notice = predecessor(session.doc);
          assert.match(notice.querySelector('.reader-notice-text').textContent, /changed passage/);
          const chooser = notice.querySelector('a[href]');
          assert.equal(chooser.hash, '#' + changed.targets[0]);
          chooser.click();
          assert.ok(session.scrolls.includes(changed.targets[0]));
          return { from: changed.id, to: changed.targets[0] };
        });
    }
  }
}

async function checkPhysicalBookmarks(book) {
  const unchanged = book.compatibility.find((record) => record.id === stableV16);
  assert.equal(unchanged.role, 'retained');
  assert.deepEqual(unchanged.targets, [stableV16]);
  assert.ok(unchanged.origins.some(({ edition, match, identity }) => edition === 'v16' && match === 'exact' &&
    identity === '0b7cec6c98147ccdec2ae3d1ad565d99cb1508fc0c68f33440d9602ac783ba7a'));
  await scenario('an unchanged v16 passage keeps its original content address', 'index.html', '#' + stableV16, (session) => {
    assert.equal(session.window.location.hash, '#' + stableV16);
    assert.ok(session.scrolls.includes(stableV16));
    const paragraph = session.doc.getElementById(stableV16);
    assert.ok(session.doc.getElementById(commonTailEnclosure).contains(paragraph));
    assert.match(paragraph.textContent, /^The algebraic unit is known for every simple complex Lie algebra/);
    assert.equal(predecessor(session.doc), null);
    return { address: stableV16 };
  });
  const changedCommonTail = book.compatibility.find(({ id }) => id === oldCommonTail);
  assert.equal(changedCommonTail.role, 'changed');
  assert.deepEqual(changedCommonTail.targets, [commonTailEnclosure]);
  assert.ok(changedCommonTail.origins.some(({ edition, match, identity }) => edition === 'v16' && match === 'changed' &&
    identity === '91f8734687506edd18e409b05c31bb12bb8d3570bd7697228e2201158fe11791'));
  await scenario('the changed v16 common-tail address opens its current statement', 'index.html', '#' + oldCommonTail, (session) => {
    const { window, doc } = session;
    assert.equal(window.location.hash, '#' + oldCommonTail);
    assert.equal(doc.getElementById(oldCommonTail), null);
    const notice = predecessor(doc);
    assert.ok(notice && !notice.hidden);
    assert.match(notice.querySelector('.reader-notice-text').textContent, /changed passage/);
    const choices = [...notice.querySelectorAll('a[href]')];
    assert.deepEqual(choices.map(a => a.hash), ['#' + commonTailEnclosure]);
    choices[0].click();
    assert.equal(window.location.hash, '#' + commonTailEnclosure);
    assert.ok(session.scrolls.includes(commonTailEnclosure));
    const enclosure = doc.getElementById(commonTailEnclosure);
    const paragraph = doc.getElementById(currentCommonTail);
    assert.ok(enclosure.contains(paragraph));
    assert.match(paragraph.textContent, /common annihilating tail in sufficiently low cohomological degrees makes the smooth-vector completion unit invertible/);
    const theoremLink = paragraph.querySelector('a[href="#' + commonTailTheorem + '"]');
    assert.ok(theoremLink);
    theoremLink.click();
    const preview = doc.getElementById('reader-peek');
    if (!preview.hidden) preview.querySelector('.reader-peek-go').click();
    assert.equal(window.location.hash, '#' + commonTailTheorem);
    assert.ok(session.scrolls.includes(commonTailTheorem));
    const theorem = doc.getElementById(commonTailTheorem);
    assert.equal(theorem.closest('article[data-chapter]').id, 'ch06');
    const statements = [];
    for (let element = theorem.nextElementSibling; element && !element.matches('h1,h2,h3,h4'); element = element.nextElementSibling)
      statements.push(element.textContent);
    assert.match(statements.join(' '), /the actual unit is an equivalence/);
    return { from: oldCommonTail, notice: 'changed passage', to: commonTailEnclosure,
      statement: currentCommonTail, theorem: commonTailTheorem, clicks_work: true };
  });
}

async function checkRemainingScenarios(book) {
  const stableRow = report.results.find((record) => record.page === 'reference.html').compatibility
    .find(({ role, origins }) => role === 'retained' && origins.some((origin) => origin.edition === 'v16' &&
      origin.scope === 'row-heisenberg' && origin.priorLabel.startsWith('A proof establishes the conclusion')));
  assert.ok(stableRow, 'expected a repeated label in an unchanged v16 example row');
  await scenario('a repeated label in an unchanged example row keeps its v16 address', 'reference.html', 'reference.html#' + stableRow.id, (session) => {
    assert.equal(session.window.location.hash, '#' + stableRow.id);
    const target = session.doc.getElementById(stableRow.id);
    assert.match(target.textContent, /proof establishes the conclusion/);
    if (report.inputs.historic.runtime && target.closest('.cell-note[hidden]')) assertCellCard(session, stableRow.id);
    else assert.ok(session.scrolls.includes(stableRow.id));
    assert.equal(predecessor(session.doc), null);
    return { address: stableRow.id };
  });
  if (report.inputs.raw['index.html'].sha256 !== '08f89babf71198ac8804417540df3fd586327ae63d1df8937a7412531da699e1') {
    const revised = book.compatibility.find((record) => record.id === revisedV16);
    assert.equal(revised.role, 'changed');
    assert.ok(revised.origins.some((origin) => origin.edition === 'v16' && origin.match === 'advanced_with_source'));
    await scenario('a materially revised v16 passage offers its actual successor', 'index.html', '#' + revisedV16, (session) => {
      assert.equal(session.window.location.hash, '#' + revisedV16);
      const notice = predecessor(session.doc);
      assert.match(notice.querySelector('.reader-notice-text').textContent, /changed passage/);
      const link = notice.querySelector('a[href]');
      assert.equal(link.hash, '#' + revised.targets[0]);
      assert.match(session.doc.getElementById(revised.targets[0]).textContent, /prescribed unflipped rational exchange orders/);
      link.click();
      assert.ok(session.scrolls.includes(revised.targets[0]));
      return { from: revisedV16, to: revised.targets[0] };
    });
  }
  const contested = book.compatibility.find((record) => record.id === conflict);
  assert.equal(contested.role, 'ambiguous');
  assert.equal(contested.origins.length, 2);
  const olderAdjunction = contested.origins.find((item) => item.edition === 'v14');
  assert.match(olderAdjunction.priorLabel, /There are two adjunction conventions/);
  assert.ok(['exact', 'retained_rewrite'].includes(olderAdjunction.match));
  assert.match(contested.origins.find((item) => item.edition === 'v15').priorLabel, /One can see the inverse explicitly/);
  await scenario('search and the historic v14/v15 choice can be shared together', 'index.html', '?q=connected+bar#' + conflict, (session) => {
    assertSearch(session, 'connected bar');
    assert.equal(session.window.location.hash, '#' + conflict);
    assert.deepEqual([...predecessor(session.doc).querySelectorAll('a[href]')].map((a) => a.hash),
      contested.targets.map((target) => '#' + target));
  });
  await scenario('conflicting historic address offers an explicit choice and survives Back', 'index.html', '#' + conflict, async (session) => {
    const { doc, window } = session;
    assert.equal(window.location.hash, '#' + conflict);
    const notice = predecessor(doc);
    assert.ok(notice);
    assert.match(notice.querySelector('.reader-notice-text').textContent, /can refer to different passages/);
    const actions = [...notice.querySelectorAll('a[href]')];
    assert.deepEqual(actions.map((link) => link.getAttribute('href')), contested.targets.map((target) => '#' + target));
    assert.ok(actions.every((link) => doc.getElementById(link.hash.slice(1))));
    assert.match(doc.getElementById(olderAdjunction.target).textContent, /(?:two adjunction conventions|strict dg representatives the twisting-cochain)/);
    const chosen = actions.find((link) => link.textContent.includes('One can see the inverse')) || actions[0];
    const target = chosen.hash;
    chosen.click();
    assert.equal(window.location.hash, target);
    assert.ok(session.scrolls.includes(target.slice(1)));
    await traverse(window, 'back');
    assert.equal(window.location.hash, '#' + conflict);
    assert.ok(predecessor(doc));
    return { locators: contested.targets };
  });

  for (const edition of ['v14', 'v15']) {
    const matches = book.compatibility.filter(({ role, origins }) => role === 'exact' && origins.every((origin) => origin.edition === edition));
    const retained = matches.find(({ origins }) => origins[0].priorLabel.length >= 65) || matches[0];
    assert.ok(retained, `expected an exact ${edition}-only predecessor`);
    await scenario(`a uniquely identifiable ${edition} passage follows its durable address`, 'index.html', '#' + retained.id, (session) => {
      assert.equal(session.window.location.hash, '#' + retained.targets[0]);
      assert.ok(session.scrolls.includes(retained.targets[0]));
      assert.equal(predecessor(session.doc), null);
      return { from: retained.id, to: retained.targets[0] };
    });
  }

  const revised = report.results.find(({ page }) => page === 'reference.html').compatibility
    .find(({ role, id }) => role === 'changed' && !id.startsWith('orientation-'));
  assert.ok(revised, 'expected a changed historical reference passage');
  await scenario('changed reference passage offers its authored locator', 'reference.html', 'reference.html#' + revised.id, (session) => {
    assert.equal(session.window.location.hash, '#' + revised.id);
    const notice = predecessor(session.doc);
    assert.ok(notice);
    assert.match(notice.querySelector('.reader-notice-text').textContent, /changed passage/);
    assert.deepEqual([...notice.querySelectorAll('a[href]')].map((a) => a.hash), revised.targets.map((target) => '#' + target));
    return { from: revised.id, locators: revised.targets };
  });

  await scenario('the authored chapter cross-reference still reveals its heading', 'index.html', '#ch18', (session) => {
    const link = [...session.doc.querySelectorAll('#ch18 a[href]')].find((a) => a.getAttribute('href') === '#' + passage);
    assert.ok(link);
    link.click();
    const preview = session.doc.getElementById('reader-peek');
    if (!preview.hidden) preview.querySelector('.reader-peek-go').click();
    assert.equal(session.window.location.hash, '#' + passage);
    assert.ok(session.scrolls.includes(passage));
  });

}

async function main() {
  const resume = process.argv[4] ? resumeLeading(process.argv[4]) : null;
  const segment = process.argv[5] || 'all';
  assert.ok(['all', 'physical', 'history'].includes(segment));
  if (!resume) await leadingScenarios();
  const book = report.results.find((record) => record.page === 'index.html');
  if (segment !== 'history') await checkPhysicalBookmarks(book);
  if (segment !== 'physical') await checkRemainingScenarios(book);
  process.stdout.write(JSON.stringify({ status: 'PASS', files: Object.fromEntries(report.results.map(({ page, after }) => [page, after])),
    index: report.outputIndex, checks, ...(resume ? { continuation: resume, segment } : {}) }, null, 2) + '\n');
}

main().catch((error) => { console.error(error.stack); process.exitCode = 1; });
