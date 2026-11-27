#!/usr/bin/env node
/* Each mutation takes one behaviour out of a copy of reader.js or status.js and runs the test that guards it; the test
   must fail on the copy (and passes on the live file). Writes only the copies, under the directory given.

       NODE_PATH=<jsdom> node tools/reader-mutations.cjs <worktree> <scratch dir> */
'use strict';
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');
const [root, scratch] = process.argv.slice(2);
if (!root || !scratch) { console.error('usage: reader-mutations.cjs <worktree> <scratch dir>'); process.exit(2); }
const dir = path.join(root, 'compiler/quantum-holography-status');
const tests = path.join(dir, 'tests/reader.test.cjs');
const live = { reader: fs.readFileSync(path.join(dir, 'reader.js'), 'utf8'), status: fs.readFileSync(path.join(dir, 'status.js'), 'utf8') };
const M = [
  { file: 'reader', name: 'chapters matched as any [data-chapter] (the code that failed on the built book)', test: 'hooks: a figure that carries',
    from: "var chapters = all(CHAPTER, main).filter(function (c) { return !!c.id && !(c.parentNode && c.parentNode.closest && c.parentNode.closest(CHAPTER)); });",
    to: "var chapters = all('[data-chapter]', main).filter(function (c) { return !!c.id; });" },
  { file: 'reader', name: 'the reference listed before the chapters', test: 'search: the chapters come first',
    from: "function groupOrder() { return places.map(function (p) { return p.id; }); }",
    to: "function groupOrder() { return places.map(function (p) { return p.id; }).reverse(); }" },
  { file: 'reader', name: 'every group shown whole', test: 'search: the chapters come first',
    from: "if (searchState.scope === 'all') return 3;", to: "if (searchState.scope === 'all') return 1000;" },
  { file: 'reader', name: 'focus not kept in the entry left', test: 'history: Back returns to the chapter and to the control',
    from: "    patch.focus = f || null;", to: "    patch.focus = null;" },
  { file: 'reader', name: 'closed rows not opened on arrival', test: 'reference: an address inside a closed row',
    from: "  function arrive(t, o) {\n    openAround(t);", to: "  function arrive(t, o) {" },
  { file: 'reader', name: 'cross-references navigate instead of reminding', test: 'reminder: a cross-reference opens the definition',
    from: "    if (r) return true;\n    if (a.closest('nav,", to: "    if (r) return false;\n    return false;\n    if (a.closest('nav," },
  { file: 'reader', name: 'the search query not kept for Back', test: 'search: a result opens its place as a history entry',
    from: "var keepState = { q: searchState.q, scope: searchState.scope, panel: 1, hit: id, focus: null };",
    to: "var keepState = { panel: 0, focus: null };" },
  { file: 'reader', name: 'places simply shown (no hidden until found)', test: 'start: a bare visit shows the title page',
    from: "if (p.getAttribute('hidden') !== UNTIL) p.setAttribute('hidden', UNTIL);", to: "p.removeAttribute('hidden');" },
  { file: 'status', name: 'status page search built beside the reader', test: 'reference: with the status page script beside the reader',
    from: "  if (!READER) build();", to: "  build();" },
  { file: 'status', name: 'status page notices beside the reader', test: 'reference: with the status page script beside the reader',
    from: "  if (main && !READER) {\n    noticeBox", to: "  if (main) {\n    noticeBox" },
  { file: 'status', name: 'status page answers Back itself beside the reader', test: 'reference: with the status page script, Back and Forward',
    from: "    if (READER) {\n      var kept = qhOf(event.state);\n      if (refilter) refilter();\n      if (kept.open) restoreOpen(kept.open);\n      return;\n    }",
    to: "    if (READER) {\n      return;\n    }" }
];
fs.mkdirSync(scratch, { recursive: true });
let bad = 0;
for (const [i, m] of M.entries()) {
  const src = live[m.file];
  if (src.split(m.from).length !== 2) { console.log(`SKIP ${m.name}: the text to change is not found once`); bad++; continue; }
  const copy = path.join(scratch, `${m.file}-m${i + 1}.js`);
  fs.writeFileSync(copy, src.replace(m.from, m.to));
  const env = Object.assign({}, process.env, m.file === 'reader' ? { READER_JS: copy } : { STATUS_JS: copy });
  const r = spawnSync(process.execPath, ['--expose-gc', tests, m.test], { env, encoding: 'utf8', timeout: 300000 });
  const failed = r.status !== 0 && /FAIL /.test(r.stdout);
  if (!failed) bad++;
  console.log(`${failed ? 'caught' : 'MISSED'}  ${m.name}  [${m.test}]`);
}
console.log(`\n${M.length - bad} of ${M.length} mutations caught`);
process.exit(bad ? 1 : 0);
