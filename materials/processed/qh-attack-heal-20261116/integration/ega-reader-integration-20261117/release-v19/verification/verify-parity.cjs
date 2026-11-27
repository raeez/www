'use strict';

const assert = require('node:assert/strict');
const { execFileSync } = require('node:child_process');
const { createHash } = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');

const sourceIdentity = '3b57dd41a75dbc10438565925bffd4cd814d88075960c2bcfed0205a720bd2c0';
const build = path.join(__dirname, '..', 'builds', sourceIdentity);
const report = JSON.parse(fs.readFileSync(path.join(build, 'release-receipt.json')));
const toolkit = '/tmp/qh-research-reader-0733-20261118/compatibility/tools/build-amendment.cjs';
const control = '/Users/raeez/www-worktrees/2026-11-16-qh-max-integration/materials/processed/qh-attack-heal-20261116/integration/ega-reader-integration-20261117/release-v18/compatibility';
const catalog = JSON.parse(fs.readFileSync(path.join(control, 'current-history.json')));
const v18 = catalog.editions.at(-1);
const indexName = 'reader-index.js';
const pin = (data) => ({ sha256: createHash('sha256').update(data).digest('hex'), bytes: data.length });
const stripId = ({ id, ...unit }) => unit;
const key = ({ page, id }) => page + '#' + id;

function units(bytes) {
  const text = bytes.toString();
  const prefix = 'window.QH_READER_INDEX = ';
  assert.ok(text.startsWith(prefix) && text.endsWith(';\n'));
  return JSON.parse(text.slice(prefix.length, -2)).units;
}

assert.equal(report.status, 'PASS');
assert.deepEqual(report.inputs.historic, catalog);
assert.equal(v18.edition, 'v18');
assert.equal(v18.commit, '85a5c7a9e3a1be8873c33f86f8c105b186e31920');
const rawIndex = fs.readFileSync(path.join(build, 'public', indexName));
const servedIndex = fs.readFileSync(path.join(build, 'release', indexName));
assert.deepEqual(pin(rawIndex), report.inputs.raw[indexName]);
assert.deepEqual(pin(servedIndex), report.outputIndex);
const indexed = units(servedIndex);
assert.equal(indexed.length, report.searchUnits);
assert.deepEqual(indexed.map(stripId), units(rawIndex).map(stripId));

const v18Published = execFileSync('git', ['--no-optional-locks', '-C', catalog.repository, 'show',
  v18.commit + ':' + catalog.publicPath + '/' + indexName], { maxBuffer: 32 * 1024 * 1024 });
assert.deepEqual(pin(v18Published), v18.pins[indexName]);
const v18Raw = fs.readFileSync(path.join(control, v18.rawIndex.path));
assert.deepEqual(pin(v18Raw), { sha256: v18.rawIndex.sha256, bytes: v18.rawIndex.bytes });
const earlier = units(v18Published), earlierRaw = units(v18Raw);
assert.deepEqual(earlier.map(stripId), earlierRaw.map(stripId));
const issued = new Set(earlier.filter((unit, i) => unit.id !== earlierRaw[i].id).map(key));
const replayed = new Set(), live = [], pins = {};
const byRole = {}, counts = {};
let verifiedOlderAliases = 0;
for (const pageResult of report.results) {
  const { page, before, after, reverseExact, compatibility } = pageResult;
  const rawPage = fs.readFileSync(path.join(build, 'public', page));
  const servedPage = fs.readFileSync(path.join(build, 'release', page));
  assert.deepEqual(pin(rawPage), before);
  assert.deepEqual(pin(rawPage), report.inputs.raw[page]);
  assert.deepEqual(pin(servedPage), after);
  assert.equal(reverseExact, true);
  pins[page] = after;
  const inspected = JSON.parse(execFileSync(process.execPath, ['--max-old-space-size=4096', toolkit, '--inspect-page', page], {
    input: JSON.stringify({ html: servedPage.toString(), issued: [] }), maxBuffer: 64 * 1024 * 1024
  }));
  const actual = new Set(inspected.allIds);
  assert.ok(inspected.units.every((unit) => actual.has(unit.id)));
  counts[page] = inspected.units.length;
  live.push(...inspected.units);
  for (const record of compatibility) {
    assert.ok(record.targets.every((id) => actual.has(id)), 'absent locator for ' + page + '#' + record.id);
    if (record.role === 'retained') {
      assert.deepEqual(record.targets, [record.id]);
      assert.ok(actual.has(record.id));
    } else {
      assert.ok(!actual.has(record.id));
      if (record.role === 'exact') assert.equal(inspected.inherited[record.id], record.targets[0]);
      else assert.deepEqual(inspected.inheritedPredecessors[record.id],
        { targets: record.targets, ambiguous: record.role === 'ambiguous' });
    }
    verifiedOlderAliases++;
    if (record.origins.some(({ edition }) => edition === 'v18')) {
      const address = key({ page, id: record.id });
      assert.ok(!replayed.has(address));
      replayed.add(address);
      byRole[record.role] = (byRole[record.role] || 0) + 1;
    }
  }
}
assert.deepEqual(live, indexed);
assert.deepEqual(replayed, issued);
assert.deepEqual(byRole, { retained: 4197, changed: 1 });

console.log(JSON.stringify({ status: 'PASS', sourceIdentity, priorCommit: v18.commit, files: { ...pins, [indexName]: report.outputIndex },
  searchUnits: live.length, searchUnitsByPage: counts, oldSearchUnits: earlier.length,
  historicLocatorsVerified: verifiedOlderAliases, issuedV18Addresses: issued.size,
  issuedV18Roles: byRole }, null, 2));
