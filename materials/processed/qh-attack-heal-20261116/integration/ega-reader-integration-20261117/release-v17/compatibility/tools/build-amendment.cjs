#!/usr/bin/env node
'use strict';

// Derive the public bundle using the reader's own search units and exact source offsets.
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const pages = ['index.html', 'reference.html', 'atlas.html'];
const indexFile = 'reader-index.js';
const prefix = 'window.QH_READER_INDEX = ';
const suffix = ';\n';
const readerSource = 'controls/reader.js';
const referenceSource = 'controls/status.js';
const read = (name) => fs.readFileSync(path.join(root, name), 'utf8');
const sha = (text) => crypto.createHash('sha256').update(text).digest('hex');
const pin = (text) => ({ sha256: sha(text), bytes: Buffer.byteLength(text) });
const own = (object, key) => Object.prototype.hasOwnProperty.call(object, key);
const strictId = /^[A-Za-z0-9_.:-]+$/;
const compared = (unit) => { const { id, ...rest } = unit; return rest; };

function indexOf(text) {
  assert.ok(text.startsWith(prefix) && text.endsWith(suffix), 'reader index wrapper changed');
  return JSON.parse(text.slice(prefix.length, -suffix.length)).units;
}

function scriptRange(html, name) {
  const matches = [...html.matchAll(new RegExp(`<script type="application/json" id="${name}">(.*?)</script>`, 'gs'))];
  assert.ok(matches.length <= 1, `duplicate ${name}`);
  if (!matches.length) return null;
  const match = matches[0];
  const start = match.index + match[0].indexOf('>') + 1;
  return { start, end: start + match[1].length, value: JSON.parse(match[1]) };
}

function between(start, before, after, kind) {
  return { start, end: start + before.length, before, after, kind };
}

function splice(source, edits) {
  let at = 0;
  let result = '';
  const reverse = [];
  for (const edit of edits.sort((a, b) => a.start - b.start || a.end - b.end)) {
    assert.ok(edit.start >= at && source.slice(edit.start, edit.end) === edit.before, 'source edit overlap or drift');
    result += source.slice(at, edit.start);
    reverse.push(between(result.length, edit.after, edit.before, edit.kind));
    result += edit.after;
    at = edit.end;
  }
  return { text: result + source.slice(at), reverse };
}

function inspectPage(html, name, issued) {
  const { JSDOM, VirtualConsole } = require('jsdom');
  const errors = [];
  const console = new VirtualConsole();
  console.on('jsdomError', (error) => {
    if (!/Not implemented/.test(error.message)) errors.push(error.message);
  });
  const dom = new JSDOM(html, {
    url: `https://example.org/${name}`,
    runScripts: 'dangerously',
    pretendToBeVisual: true,
    includeNodeLocations: true,
    virtualConsole: console,
    beforeParse(window) {
      window.Element.prototype.scrollIntoView = function () {};
      window.scrollTo = function () {};
    }
  });
  const { window } = dom;
  const doc = window.document;
  try {
    const event = new window.CustomEvent('qh:reader-units', { detail: {} });
    doc.dispatchEvent(event);
    assert.ok(Array.isArray(event.detail.units), `${name} did not yield live search units`);
    assert.deepEqual(errors, [], `${name} emitted script errors`);
    const units = JSON.parse(JSON.stringify(event.detail.units)).map((unit) => ({ ...unit, page: name }));
    const allIds = new Set();
    const authored = new Set();
    for (const element of doc.querySelectorAll('[id]')) {
      assert.ok(!allIds.has(element.id), `${name} has duplicate #${element.id}`);
      allIds.add(element.id);
      if (dom.nodeLocation(element)?.attrs?.id) authored.add(element.id);
    }
    const addresses = new Map();
    for (const unit of units) {
      let record = addresses.get(unit.id);
      if (!record) {
        const element = doc.getElementById(unit.id);
        assert.ok(element, `${name} search anchor #${unit.id} absent`);
        const rowLink = element.closest('tr')?.cells[0]?.querySelector('a[href^="#row-"]');
        const row = rowLink?.getAttribute('href').slice(1) || '';
        assert.ok(!row || authored.has(row), `${name} has an unbound examples row #${row}`);
        const scopes = row ? [row] : [];
        const containers = [...scopes];
        const reader = element.closest('[data-reader]');
        for (let p = element; p; p = p.parentElement) {
          if (p === reader) break;
          if (!authored.has(p.id)) continue;
          containers.push(p.id);
          if (p.matches('[data-section], [data-chapter], [data-reference]')) scopes.push(p.id);
        }
        if (!scopes.includes(unit.group)) scopes.push(unit.group);
        const hrefs = [...element.querySelectorAll('a[href]')].map((link) => link.getAttribute('href'));
        const runtimeId = name === 'reference.html' && element.matches('#examples .row-tools > .filter-note') ? 'examples-filter-note' : null;
        record = { id: unit.id, issued: issued.has(unit.id), generated: issued.has(unit.id) ||
          (!authored.has(unit.id) && /-p\d+$/.test(unit.id)), row, scopes, containers, hrefs, runtimeId,
          tag: element.localName, end: dom.nodeLocation(element)?.startTag?.endOffset, units: [] };
        addresses.set(unit.id, record);
      }
      record.units.push(unit);
    }
    const inherited = scriptRange(html, 'reader-redirects')?.value || {};
    const inheritedPredecessors = scriptRange(html, 'reader-predecessors')?.value || {};
    return { units, authored, allIds, addresses, inherited, inheritedPredecessors, issued };
  } finally {
    window.close();
  }
}

function getPage(html, name, issued = new Set()) {
  // Dispose of the full DOM between assets, even as the historical catalog grows.
  const result = execFileSync(process.execPath, ['--max-old-space-size=4096', __filename, '--inspect-page', name], {
    input: JSON.stringify({ html, issued: [...issued] }), encoding: 'utf8', maxBuffer: 64 * 1024 * 1024
  });
  const page = JSON.parse(result);
  page.authored = new Set(page.authored);
  page.allIds = new Set(page.allIds);
  page.addresses = new Map(page.addresses.map(([id, record]) => [id, { ...record, units: [] }]));
  for (const unit of page.units) page.addresses.get(unit.id).units.push(unit);
  page.issued = issued;
  return page;
}

function inspectChild(name) {
  assert.ok(pages.includes(name));
  const input = JSON.parse(fs.readFileSync(0, 'utf8'));
  const { units, authored, allIds, addresses, inherited, inheritedPredecessors } =
    inspectPage(input.html, name, new Set(input.issued));
  process.stdout.write(JSON.stringify({ units, authored: [...authored], allIds: [...allIds],
    addresses: [...addresses].map(([id, { units: ignored, ...record }]) => [id, record]), inherited, inheritedPredecessors }));
}

function identity(record) {
  return JSON.stringify([record.row, record.tag, record.hrefs, record.units.map(({ group, kind, text, tex, title, ttex }) =>
    [group, kind, text, tex, title, ttex])]);
}

function rewrittenIdentity(record) {
  const [unit] = record.units;
  if (record.tag !== 'p' || record.units.length !== 1 || unit.kind !== 'text' || unit.tex.length < 20) return '';
  const sentences = unit.text.split(/(?<=[.!?])\s+/);
  if (sentences.length < 3) return '';
  const tail = sentences.slice(-2).join(' ');
  if (tail.length < 150 || tail.length < unit.text.length * 0.6) return '';
  return JSON.stringify([record.scopes[0], record.row, record.hrefs, unit.group, unit.tex, unit.ttex, tail]);
}

function advancedIdentity(record) {
  const [unit] = record.units;
  if (record.tag !== 'p' || record.units.length !== 1 || unit.kind !== 'text' ||
      !record.hrefs.some((href) => /^(?:index\.html|reference\.html|atlas\.html)?#[\w:.-]+$/.test(href))) return '';
  const sentences = unit.text.split(/(?<=[.!?])\s+/);
  if (sentences.length < 3) return '';
  const lead = sentences.slice(0, 2).join(' ');
  return lead.length >= 150 ? JSON.stringify([record.scopes[0], record.row, record.hrefs, unit.group, lead]) : '';
}

function groupBy(records, key) {
  const groups = new Map();
  for (const record of records) {
    const value = key(record);
    if (!groups.has(value)) groups.set(value, []);
    groups.get(value).push(record);
  }
  return groups;
}

function planFor(name, historic, current) {
  const newIdentities = groupBy(current.addresses.values(), identity);
  const newScopes = groupBy(current.addresses.values(), (record) => record.scopes[0]);
  const newRewrites = groupBy(current.addresses.values(), rewrittenIdentity);
  const advances = groupBy(current.addresses.values(), advancedIdentity);
  const reserved = new Set([...current.allIds, ...Object.keys(current.inherited), ...Object.keys(current.inheritedPredecessors)]);
  const issued = new Set();
  for (const { page } of historic) {
    for (const id of page.allIds) reserved.add(id);
    for (const id of Object.keys(page.inherited)) reserved.add(id);
    for (const id of Object.keys(page.inheritedPredecessors)) reserved.add(id);
    for (const id of page.issued) issued.add(id);
  }

  const anchors = new Map();
  for (const { edition, page } of historic) {
    const oldIdentities = groupBy(page.addresses.values(), identity);
    const oldRewrites = groupBy(page.addresses.values(), rewrittenIdentity);
    const oldAdvances = groupBy(page.addresses.values(), advancedIdentity);
    const ordered = new Map();
    if (page.issued.size) {
      for (const [scope, former] of groupBy(page.addresses.values(), (record) => record.scopes[0])) {
        const now = newScopes.get(scope);
        if (!now || now.length !== former.length || !former.every((record, i) => identity(record) === identity(now[i]))) continue;
        former.forEach((record, i) => { if (record.issued) ordered.set(record.id, now[i]); });
      }
    }
    for (const id of page.authored) {
      if (id.startsWith('reader-') || id === 'card' || page.issued.has(id)) continue;
      assert.ok(current.authored.has(id) || own(current.inherited, id), `${name} lost authored ${edition} address #${id}`);
    }
    for (const prior of page.addresses.values()) {
      if (!prior.generated && current.allIds.has(prior.id)) continue;
      const key = identity(prior);
      const scope = prior.scopes[0];
      const possible = newIdentities.get(key) || [];
      const nearby = possible.filter((record) => record.scopes[0] === scope);
      const oldNearby = oldIdentities.get(key).filter((record) => record.scopes[0] === scope);
      const substantial = prior.units.some((unit) => (unit.text || unit.tex || '').length >= 120);
      const match = ordered.get(prior.id) || (nearby.length === 1 && oldNearby.length === 1 ? nearby[0] :
        substantial && possible.length === 1 && oldIdentities.get(key).length === 1 ? possible[0] : null);
      const rewriteKey = rewrittenIdentity(prior);
      const rewrites = rewriteKey ? newRewrites.get(rewriteKey) || [] : [];
      const rewrite = !match && rewrites.length === 1 && oldRewrites.get(rewriteKey).length === 1 ? rewrites[0] : null;
      const advanceKey = prior.issued && advancedIdentity(prior);
      const renewed = advanceKey ? advances.get(advanceKey) || [] : [];
      const advance = !match && !rewrite && renewed.length === 1 && oldAdvances.get(advanceKey).length === 1 ? renewed[0] : null;
      const fallback = [...prior.containers, ...prior.scopes].find((id) => current.authored.has(id));
      assert.ok(match || rewrite || advance || fallback, `${name} found no surviving locator for ${edition} #${prior.id}`);
      if (!anchors.has(prior.id)) anchors.set(prior.id, []);
      const priorLabel = Array.from(prior.units[0].title || prior.units[0].text).slice(0, 130).join('');
      anchors.get(prior.id).push({ edition, record: match || rewrite || advance, fallback, priorLabel, scope,
        match: match ? 'exact' : rewrite ? 'retained_rewrite' : advance ? 'advanced_with_source' :
          possible.length || rewrites.length || renewed.length ? 'ambiguous' : 'changed',
        identity: sha(JSON.stringify([scope, key])) });
    }
  }
  const retained = new Map();
  for (const [id, origins] of anchors) {
    if (!issued.has(id) || current.allIds.has(id) || !origins.every((origin) => origin.match === 'exact')) continue;
    const record = origins[0].record;
    if (record.generated && origins.every((origin) => origin.record.id === record.id) && !retained.has(record.id)) {
      retained.set(record.id, id);
    }
  }
  const finalId = new Map();
  const annotations = [];
  for (const record of current.addresses.values()) {
    if (!record.generated) {
      finalId.set(record.id, record.id);
      continue;
    }
    if (record.runtimeId) {
      assert.ok(!current.allIds.has(record.runtimeId), `${name} runtime address already exists: #${record.runtimeId}`);
      reserved.add(record.runtimeId);
      finalId.set(record.id, record.runtimeId);
      continue;
    }
    assert.ok(Number.isInteger(record.end), `${name} generated address is missing a source tag: #${record.id}`);
    const group = record.units[0].group;
    const digest = sha(JSON.stringify([record.scopes, identity(record)])).slice(0, 20);
    const base = `${group}-passage-${digest}`;
    let id = retained.get(record.id);
    if (!id) {
      id = base;
      let sequence = 2;
      while (reserved.has(id)) id = `${base}-${sequence++}`;
    }
    reserved.add(id);
    assert.match(id, strictId);
    finalId.set(record.id, id);
    annotations.push({ provisional: record.id, id, offset: record.end - 1 });
  }
  const published = new Set([...current.authored, ...finalId.values()]);
  const redirects = {};
  const predecessors = {};
  const currentLocator = (id) => finalId.get(id) || id;
  const addRedirect = (from, to) => {
    assert.match(from, strictId);
    assert.ok(published.has(to), `${name} redirect target is not an emitted address: #${to}`);
    if (from === to) return;
    assert.ok(!published.has(from), `${name} redirect would shadow #${from}`);
    assert.ok(!own(redirects, from) || redirects[from] === to, `${name} has conflicting redirects for #${from}`);
    assert.ok(!own(predecessors, from), `${name} redirect would shadow predecessor #${from}`);
    redirects[from] = to;
  };
  const addPredecessor = (id, targets, ambiguous) => {
    assert.match(id, strictId);
    assert.ok(!published.has(id) && !own(redirects, id), `${name} predecessor would shadow #${id}`);
    assert.ok(targets.length && targets.every((target) => published.has(target)), `${name} predecessor #${id} lacks a live target`);
    predecessors[id] = { targets: [...new Set(targets)], ambiguous: !!ambiguous };
  };
  for (const [id, target] of Object.entries(current.inherited)) {
    if (!anchors.has(id)) addRedirect(id, currentLocator(target));
  }
  for (const [id, prior] of Object.entries(current.inheritedPredecessors)) {
    if (!anchors.has(id)) addPredecessor(id, prior.targets.map(currentLocator), prior.ambiguous);
  }
  const compatibility = [];
  for (const [id, records] of anchors) {
    const origins = records.map(({ record, fallback, ...origin }) => ({ ...origin, target: record ? finalId.get(record.id) : fallback }));
    const targets = [...new Set(origins.map((origin) => origin.target))];
    const exact = targets.length === 1 && origins.every((origin) => origin.match === 'exact');
    const ambiguous = targets.length > 1 || origins.some((origin) => origin.match === 'ambiguous') ||
      new Set(origins.map((origin) => origin.identity)).size > 1;
    if (exact) {
      addRedirect(id, targets[0]);
    } else {
      addPredecessor(id, targets, ambiguous);
    }
    const role = exact ? (id === targets[0] ? 'retained' : 'exact') : ambiguous ? 'ambiguous' : 'changed';
    compatibility.push({ id, targets, role, origins });
  }
  const durableAddresses = [...finalId].filter(([provisional, id]) =>
    current.addresses.get(provisional).generated || issued.has(id)).map(([, id]) => id);
  return { annotations, redirects, predecessors, published, finalId, compatibility, durableAddresses };
}

function jsonScript(data) {
  return JSON.stringify(data).replace(/</g, '\\u003c');
}

function replaceSource(name, original, oldSource, newSource, kind) {
  const after = newSource.trim();
  const before = original.includes(after) ? after : oldSource.trim();
  const bodyAt = original.indexOf(before);
  assert.ok(bodyAt >= 0 && original.indexOf(before, bodyAt + before.length) < 0,
    `${name} does not have exactly one ${kind} script`);
  const tagAt = original.lastIndexOf('<script>', bodyAt);
  const tagEnd = original.indexOf('</script>', bodyAt);
  assert.equal(original.slice(tagAt + '<script>'.length, tagEnd).trim(), before);
  return { edit: before === after ? null : between(bodyAt, before, after, kind), tagAt };
}

function amend(name, original, sources, plan, companionIds) {
  const { edit, tagAt } = replaceSource(name, original, ...sources.reader, 'embedded_reader_source');
  const edits = edit ? [edit] : [];
  if (name === 'reference.html') {
    const referenceEdit = replaceSource(name, original, ...sources.reference, 'embedded_reference_source').edit;
    if (referenceEdit) edits.push(referenceEdit);
  }
  for (const { offset, id } of plan.annotations) {
    assert.equal(original[offset], '>', `${name} has a mislocated source tag for #${id}`);
    edits.push(between(offset, '', ` id="${id}"`, 'passage_address'));
  }
  for (const [id, data] of [['reader-redirects', plan.redirects], ['reader-predecessors', plan.predecessors]]) {
    const previous = scriptRange(original, id);
    const json = jsonScript(data);
    if (previous && original.slice(previous.start, previous.end) !== json) {
      edits.push(between(previous.start, original.slice(previous.start, previous.end), json, id));
    } else if (!previous && Object.keys(data).length) {
      edits.push(between(tagAt, '', `<script type="application/json" id="${id}">${json}</script>\n`, id));
    }
  }
  const pg = scriptRange(original, 'reader-pages');
  assert.ok(pg, `${name} has no companion page map`);
  for (const entry of pg.value.pages) {
    const companion = companionIds.get(entry.href);
    assert.ok(companion, `unknown companion: ${entry.href}`);
    entry.ids = [...new Set([...entry.ids.filter((id) => companion.published.has(id)), ...companion.annotated])];
    if (companion.aliases.length) entry.aliases = companion.aliases;
    else delete entry.aliases;
  }
  const pageMap = jsonScript(pg.value);
  if (pageMap !== original.slice(pg.start, pg.end)) {
    edits.push(between(pg.start, original.slice(pg.start, pg.end), pageMap, 'companion_address_metadata'));
  }
  const result = splice(original, edits);
  assert.equal(splice(result.text, result.reverse).text, original, `${name} consumer-only reverse readback failed`);
  return { text: result.text, changes: groupBy(edits, (edit) => edit.kind) };
}

function loadHistory(catalogPath, catalog) {
  assert.equal(catalog.schema, 'reader-public-history/1');
  assert.equal(new Set(catalog.editions.map(({ edition }) => edition)).size, catalog.editions.length, 'duplicate publication label');
  return catalog.editions.map((entry) => {
    assert.match(entry.commit, /^[0-9a-f]{40}$/);
    const assets = new Map([...pages, indexFile].map((name) => {
      const data = execFileSync('git', ['--no-optional-locks', '-C', catalog.repository, 'show',
        `${entry.commit}:${catalog.publicPath}/${name}`], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
      assert.deepEqual(pin(data), entry.pins[name], `published ${entry.edition} ${name} does not match its pin`);
      return [name, data];
    }));
    const index = indexOf(assets.get(indexFile));
    const issued = new Map(pages.map((page) => [page, new Set()]));
    if (entry.rawIndex) {
      const { path: relative, ...expected } = entry.rawIndex;
      const data = fs.readFileSync(path.resolve(path.dirname(catalogPath), relative), 'utf8');
      assert.deepEqual(pin(data), expected, `raw index pin drift for ${entry.edition}`);
      const raw = indexOf(data);
      assert.deepEqual(raw.map(compared), index.map(compared), `${entry.edition} raw and published units differ beyond their IDs`);
      index.forEach((unit, i) => { if (unit.id !== raw[i].id) issued.get(unit.page).add(unit.id); });
    }
    if (entry.receipt) {
      assert.ok(!entry.rawIndex, `choose one address inventory for ${entry.edition}`);
      const { path: relative, ...expected } = entry.receipt;
      const data = fs.readFileSync(path.resolve(path.dirname(catalogPath), relative), 'utf8');
      assert.deepEqual(pin(data), expected, `address receipt pin drift for ${entry.edition}`);
      const prior = JSON.parse(data);
      assert.equal(prior.status, 'PASS');
      assert.deepEqual(prior.outputIndex, entry.pins[indexFile]);
      assert.deepEqual(prior.results.map(({ page }) => page), pages);
      for (const { page, after, durableAddresses } of prior.results) {
        assert.deepEqual(after, entry.pins[page]);
        assert.equal(new Set(durableAddresses).size, durableAddresses.length);
        const available = new Set(index.filter((unit) => unit.page === page).map((unit) => unit.id));
        for (const id of durableAddresses) {
          assert.ok(available.has(id), `issued ${entry.edition} locator #${id} is missing from its published index`);
          issued.get(page).add(id);
        }
      }
    }
    return { edition: entry.edition, assets, index, issued };
  });
}

function main() {
  assert.ok([4, 5].includes(process.argv.length), 'usage: build-amendment.cjs RAW_PUBLIC OUTPUT [HISTORY_CATALOG]');
  const input = fs.realpathSync(process.argv[2]);
  const requestedSite = path.resolve(process.argv[3]);
  const site = path.join(fs.realpathSync(path.dirname(requestedSite)), path.basename(requestedSite));
  const relation = path.relative(input, site);
  assert.ok(relation === '..' || relation.startsWith('..' + path.sep) || path.isAbsolute(relation),
    'output must be outside the raw input directory');
  assert.ok(!fs.existsSync(site), `output already exists: ${site}`);
  const receipt = site + '-receipt.json';
  assert.ok(!fs.existsSync(receipt), `receipt already exists: ${receipt}`);
  const catalogPath = path.resolve(process.argv[4] || path.join(root, 'history.json'));
  const catalog = JSON.parse(fs.readFileSync(catalogPath, 'utf8'));
  for (const [name, expected] of Object.entries(catalog.controls)) assert.deepEqual(pin(read(name)), expected, `reader control ${name} differs from release`);
  const oldReader = read('baseline/reader.js');
  const nextReader = read(readerSource);
  const oldReference = read('baseline/status.js');
  const nextReference = read(referenceSource);
  assert.notEqual(oldReader, nextReader);
  const historic = loadHistory(catalogPath, catalog);
  const raw = new Map([...pages, indexFile].map((name) => [name, fs.readFileSync(path.join(input, name), 'utf8')]));
  const rawIndex = indexOf(raw.get(indexFile));
  const plans = new Map();
  const candidates = new Map();
  for (const name of pages) {
    const predecessors = historic.map(({ edition, assets, index, issued }) => {
      const page = getPage(assets.get(name), name, issued.get(name));
      assert.deepEqual(page.units, index.filter((unit) => unit.page === name), `${name} published ${edition} index drift`);
      if (global.gc) global.gc();
      return { edition, page };
    });
    const current = getPage(raw.get(name), name);
    assert.deepEqual(current.units, rawIndex.filter((unit) => unit.page === name), `${name} raw index drift`);
    const plan = planFor(name, predecessors, current);
    plans.set(name, plan);
    process.stderr.write(`${name} planned ${plan.annotations.length} addresses and ${plan.compatibility.length} historic locators\n`);
    if (global.gc) global.gc();
  }
  const aliasOwners = new Map();
  for (const [page, plan] of plans) {
    for (const id of [...Object.keys(plan.redirects), ...Object.keys(plan.predecessors)]) {
      assert.ok(!aliasOwners.has(id), `alias #${id} is duplicated across ${aliasOwners.get(id)} and ${page}`);
      for (const [other, destination] of plans) {
        assert.ok(!destination.published.has(id), `alias ${page}#${id} shadows an address in ${other}`);
      }
      aliasOwners.set(id, page);
    }
  }
  const companionIds = new Map([...plans].map(([name, plan]) => [name, {
    annotated: plan.annotations.map(({ id }) => id), aliases: [...Object.keys(plan.redirects), ...Object.keys(plan.predecessors)],
    published: plan.published
  }]));
  const outputIndex = [];
  const results = [];
  for (const name of pages) {
    const plan = plans.get(name);
    const original = raw.get(name);
    const output = amend(name, original, { reader: [oldReader, nextReader], reference: [oldReference, nextReference] }, plan, companionIds);
    const live = getPage(output.text, name);
    const before = rawIndex.filter((unit) => unit.page === name);
    assert.deepEqual(live.units.map(compared), before.map(compared), `${name} search content or order changed`);
    for (let i = 0; i < before.length; i++) assert.equal(live.units[i].id, plan.finalId.get(before[i].id), `${name} search anchor ` + i);
    const servedPredecessors = scriptRange(output.text, 'reader-predecessors')?.value || {};
    for (const id of [...Object.keys(live.inherited), ...Object.keys(servedPredecessors)]) {
      assert.ok(!live.allIds.has(id), `${name} alias #${id} is shadowed by a runtime address`);
    }
    for (const record of plan.compatibility) {
      assert.ok(record.targets.every((target) => live.allIds.has(target)), `${name} historic #${record.id} has an absent locator`);
      if (record.role === 'retained') assert.ok(live.allIds.has(record.id));
      else if (record.role === 'exact') assert.equal(live.inherited[record.id], record.targets[0]);
      else assert.deepEqual(servedPredecessors[record.id], { targets: record.targets, ambiguous: record.role === 'ambiguous' });
    }
    outputIndex.push(...live.units);
    candidates.set(name, output.text);
    const changes = Object.fromEntries([...output.changes].map(([kind, records]) => [kind, records.length]));
    const roles = Object.fromEntries([...groupBy(plan.compatibility, (record) => record.role)].map(([role, records]) => [role, records.length]));
    results.push({ page: name, before: pin(original), after: pin(output.text), changes, roles,
      durableAddresses: plan.durableAddresses, compatibility: plan.compatibility, reverseExact: true });
    if (global.gc) global.gc();
  }
  const indexText = prefix + JSON.stringify({ units: outputIndex }) + suffix;
  candidates.set(indexFile, indexText);
  fs.mkdirSync(site);
  for (const [file, text] of candidates) fs.writeFileSync(path.join(site, file), text, { flag: 'wx' });
  const report = { schema: 'reader-address-amendment/3', status: 'PASS',
    inputs: { historic: catalog, raw: Object.fromEntries([...raw].map(([name, text]) => [name, pin(text)])) },
    readerAfter: pin(nextReader), referenceAfter: pin(nextReference), outputIndex: pin(indexText), searchUnits: outputIndex.length,
    identityRule: 'Unique equal word and formula projections, link targets, element type and unit kind and group, with the authored example row when present. Short unchanged text must also have the same authored scope. Repeated issued labels retain their locations if every ordered source unit in the same authored scope agrees. A rewritten paragraph can link to its retained referent through a notice when the original scope and full formulas and two substantial concluding sentences agree uniquely, or for an issued passage when two substantial opening sentences and authored link targets agree uniquely.',
    addressRule: 'Uniquely matched previous durable addresses are retained. A single exact destination under a different address gets a redirect. Changed or ambiguous addresses give explicit predecessor locators. New passages have content-derived addresses.',
    results };
  fs.writeFileSync(receipt, JSON.stringify(report, null, 2) + '\n', { flag: 'wx' });
  process.stdout.write(JSON.stringify({ status: 'PASS', site, receipt, searchUnits: report.searchUnits,
    pages: results.map((r) => ({ page: r.page, sha256: r.after.sha256, changes: r.changes,
      historicAddresses: r.roles })) }, null, 2) + '\n');
}

if (require.main === module) {
  if (process.argv[2] === '--inspect-page') inspectChild(process.argv[3]);
  else main();
}
module.exports = { planFor };
