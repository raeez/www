#!/usr/bin/env node
'use strict';

const assert = require('node:assert/strict');
const { createHash } = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM, VirtualConsole, requestInterceptor } = require('jsdom');

assert.equal(process.argv.length, 3, 'usage: check-amendment.cjs AMENDED_PUBLIC');
const site = fs.realpathSync(process.argv[2]);
const base = 'https://research.momentum.inc/quantum-holography/';
const report = JSON.parse(fs.readFileSync(site + '-receipt.json', 'utf8'));
const index = fs.readFileSync(path.join(site, 'reader-index.js'));
const pageText = new Map(report.results.map(({ page }) => [page, fs.readFileSync(path.join(site, page), 'utf8')]));
const pin = (text) => ({ sha256: createHash('sha256').update(text).digest('hex'), bytes: Buffer.byteLength(text) });
for (const { page, after } of report.results) assert.deepEqual(pin(pageText.get(page)), after);
assert.deepEqual(pin(index), report.outputIndex);

const checks = [];
function open(page, suffix) {
  const scrolls = [], departures = [], errors = [];
  const virtualConsole = new VirtualConsole();
  virtualConsole.on('jsdomError', (error) => errors.push(error.message));
  const resources = { interceptors: [requestInterceptor((req) => req.url === base + 'reader-index.js' ?
    new Response(index, { headers: { 'Content-Type': 'application/javascript' } }) : new Response('', { status: 404 }))] };
  const dom = new JSDOM(pageText.get(page), {
    url: new URL(suffix, base).href, runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole, resources,
    beforeParse(window) {
      window.Element.prototype.scrollIntoView = function () { scrolls.push(this.id); };
      window.scrollTo = function () {};
      window.addEventListener('qh:leave', (event) => {
        departures.push(JSON.parse(JSON.stringify(event.detail)));
        event.preventDefault();
      }, true);
    }
  });
  return { window: dom.window, doc: dom.window.document, scrolls, departures, errors };
}

async function scenario(name, page, suffix, check) {
  const session = open(page, suffix);
  try {
    const evidence = await check(session);
    assert.deepEqual(session.errors, [], `${name} produced runtime errors`);
    checks.push({ name, ...evidence });
  } finally {
    session.window.close();
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

async function main() {
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
  const contested = book.compatibility.find((record) => record.id === conflict);
  assert.equal(contested.role, 'ambiguous');
  assert.equal(contested.origins.length, 2);
  const olderAdjunction = contested.origins.find((item) => item.edition === 'v14');
  assert.match(olderAdjunction.priorLabel, /There are two adjunction conventions/);
  assert.ok(['exact', 'retained_rewrite'].includes(olderAdjunction.match));
  assert.match(contested.origins.find((item) => item.edition === 'v15').priorLabel, /One can see the inverse explicitly/);
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
    await new Promise((resolve, reject) => {
      const timeout = setTimeout(() => reject(new Error('Back did not complete')), 2000);
      window.addEventListener('popstate', () => { clearTimeout(timeout); resolve(); }, { once: true });
      window.history.back();
    });
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

  process.stdout.write(JSON.stringify({ status: 'PASS', files: Object.fromEntries(report.results.map(({ page, after }) => [page, after])),
    index: report.outputIndex, checks }, null, 2) + '\n');
}

main().catch((error) => { console.error(error.stack); process.exitCode = 1; });
