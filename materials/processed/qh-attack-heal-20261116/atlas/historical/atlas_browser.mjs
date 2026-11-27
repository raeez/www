// Behaviour, layout and print checks of the research atlas in headless Chrome.
//
//   node atlas_browser.mjs <page.html> <out dir> <atlas.json the page was built from> [--quick]
//
// The page is a local build that contains the atlas. Chrome runs headless with its own profile in
// <out dir>/profile (removed at the end) and is driven over the DevTools protocol with Node's
// WebSocket; no package is needed. Every check is recorded in <out dir>/results.json with its
// evidence; screenshots and PDFs go to <out dir>. The exit status is 1 when a check fails.
// Expected values come from the atlas.json, not from the page, so that a wrong page cannot pass.
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const [page, outArg, fixtureArg] = process.argv.slice(2);
const quick = process.argv.includes('--quick');
if (!page || !outArg || !fixtureArg) {
  console.error('usage: node atlas_browser.mjs <page.html> <out dir> <atlas.json> [--quick]');
  process.exit(2);
}
const out = resolve(outArg);
mkdirSync(out, { recursive: true });
const atlas = JSON.parse(readFileSync(fixtureArg, 'utf8'));
const url = pathToFileURL(resolve(page)).href;
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const profile = join(out, 'profile');
rmSync(profile, { recursive: true, force: true });

const results = [];
function check(name, ok, evidence) {
  results.push({ name, ok: !!ok, evidence });
  console.log((ok ? 'PASS ' : 'FAIL ') + name + (ok ? '' : '  ' + JSON.stringify(evidence).slice(0, 400)));
}
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Chrome and the protocol ---------------------------------------------------------------------
const chrome = spawn(CHROME, ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`, '--no-first-run',
  '--no-default-browser-check', '--disable-gpu', '--hide-scrollbars', '--force-color-profile=srgb', '--disable-extensions',
  '--allow-file-access-from-files', 'about:blank'], { stdio: ['ignore', 'ignore', 'ignore'] });
let portFile = join(profile, 'DevToolsActivePort');
for (let i = 0; i < 200 && !existsSync(portFile); i++) await sleep(50);
await sleep(100);
const [port, wsPath] = readFileSync(portFile, 'utf8').trim().split('\n');
const ws = new WebSocket(`ws://127.0.0.1:${port}${wsPath}`);
await new Promise((r, j) => { ws.onopen = r; ws.onerror = j; });
let nextId = 0;
const pending = new Map();
const events = [];
ws.onmessage = (m) => {
  const msg = JSON.parse(m.data);
  if (msg.id && pending.has(msg.id)) {
    const { resolve: ok, reject: no } = pending.get(msg.id);
    pending.delete(msg.id);
    if (msg.error) no(new Error(JSON.stringify(msg.error))); else ok(msg.result);
  } else events.push(msg);
};
function send(method, params = {}, sessionId) {
  const id = ++nextId;
  ws.send(JSON.stringify({ id, method, params, sessionId }));
  return new Promise((ok, no) => pending.set(id, { resolve: ok, reject: no }));
}
const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
const S = (m, p) => send(m, p, sessionId);
await S('Page.enable');
await S('Runtime.enable');
await S('Log.enable');
const problems = [];
function collect() {
  while (events.length) {
    const e = events.shift();
    if (e.method === 'Runtime.exceptionThrown') problems.push({ kind: 'exception', text: e.params.exceptionDetails.exception?.description || e.params.exceptionDetails.text });
    if (e.method === 'Runtime.consoleAPICalled' && ['error', 'warning', 'assert'].includes(e.params.type)) {
      problems.push({ kind: 'console.' + e.params.type, text: e.params.args.map((a) => a.value ?? a.description).join(' ') });
    }
    if (e.method === 'Log.entryAdded' && ['error', 'warning'].includes(e.params.entry.level)) problems.push({ kind: 'log', text: e.params.entry.text, url: e.params.entry.url });
  }
}
async function js(expression) {
  const r = await S('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) throw new Error('page: ' + (r.exceptionDetails.exception?.description || r.exceptionDetails.text) + '\n' + expression.slice(0, 200));
  return r.result.value;
}
async function size(width, height = 900) {
  await S('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });
}
async function media(features) { await S('Emulation.setEmulatedMedia', { media: '', features }); }
async function load(hash = '') {
  const done = new Promise((r) => { const t = setInterval(() => { const i = events.findIndex((e) => e.method === 'Page.loadEventFired'); if (i >= 0) { events.splice(i, 1); clearInterval(t); r(); } }, 20); });
  await S('Page.navigate', { url: url + hash });
  await done;
  await js('new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))');
  await sleep(60);
}
async function center(selector) {
  return js(`(() => { const el = document.querySelector(${JSON.stringify(selector)}); if (!el) return null;
    el.scrollIntoView({ block: 'center', behavior: 'instant' });
    const r = el.getClientRects()[0] || el.getBoundingClientRect();  /* a wrapped link: a point on its first line */
    return { x: r.left + Math.min(r.width / 2, 24), y: r.top + r.height / 2 }; })()`);
}
async function click(selector) {
  const p = await center(selector);
  if (!p) throw new Error('no element ' + selector);
  await sleep(30);
  for (const type of ['mouseMoved', 'mousePressed', 'mouseReleased']) {
    await S('Input.dispatchMouseEvent', { type, x: p.x, y: p.y, button: 'left', clickCount: 1 });
  }
  await sleep(60);
}
const KEYS = { ArrowDown: 40, ArrowUp: 38, Escape: 27, Enter: 13, Tab: 9, Home: 36, End: 35 };
async function press(key, shift = false) {
  const base = { key, code: key, windowsVirtualKeyCode: KEYS[key], modifiers: shift ? 8 : 0 };
  await S('Input.dispatchKeyEvent', { type: 'keyDown', ...base, ...(key === 'Enter' ? { text: '\r' } : {}) });
  await S('Input.dispatchKeyEvent', { type: 'keyUp', ...base });
  await sleep(60);
}
async function shot(name) {
  const { data } = await S('Page.captureScreenshot', { format: 'png' });
  writeFileSync(join(out, name + '.png'), Buffer.from(data, 'base64'));
  return name + '.png';
}
const PANE = `document.querySelector('.atlas-pane')`;
const paneTitle = () => js(`(() => { const t = document.querySelector('.atlas-pane .atlas-pane-title'); return t ? t.textContent.replace(/\\s+/g, ' ').trim() : null; })()`);
const active = () => js(`(() => { const a = document.activeElement; return a ? (a.className || a.localName) + '|' + (a.getAttribute('href') || a.id || '') : null; })()`);

// What the data says ------------------------------------------------------------------------------
const claimById = Object.fromEntries(atlas.claims.map((c) => [c.id, c]));
const inOf = (id) => atlas.edges.filter((e) => e.target === id);
const outOf = (id) => atlas.edges.filter((e) => e.source === id);
const plainTitle = (id) => claimById[id].title.replace(/\\\(|\\\)/g, '').replace(/\s+/g, ' ').trim();
const hub = [...atlas.claims].sort((a, b) => (inOf(b.id).length + outOf(b.id).length) - (inOf(a.id).length + outOf(a.id).length))[0].id;

try {
  await size(1400);
  await load();
  collect();

  // Preflight: the page under test contains the atlas and its script ran.
  const pre = await js(`({ atlas: !!document.getElementById('atlas'), js: !!document.querySelector('.atlas-body.atlas-js'),
    pane: !!document.querySelector('.atlas-pane'), claims: document.querySelectorAll('.atlas-claim').length })`);
  check('preflight: the page has the atlas and atlas.js ran', pre.atlas && pre.js && pre.pane && pre.claims === atlas.claims.length, pre);

  // INV4: every recorded edge is placed once, in the right list of each end, and drawn from its source to its target.
  const placement = await js(`(() => {
    const out = {};
    for (const li of document.querySelectorAll('.atlas-claim .atlas-rel[data-edge]')) {
      const art = li.closest('.atlas-claim'); const dir = li.closest('ul').getAttribute('data-dir');
      (out[li.dataset.edge] = out[li.dataset.edge] || []).push([art.dataset.claim, dir, li.dataset.other]);
    }
    const geo = {};
    const pos = {};
    for (const g of document.querySelectorAll('.atlas-map .atlas-node')) {
      const m = /translate\\(([\\d.]+) ([\\d.]+)\\)/.exec(g.getAttribute('transform')); pos[g.dataset.claim] = [+m[1], +m[2]];
    }
    for (const p of document.querySelectorAll('.atlas-map .atlas-edge')) {
      const a = p.getPointAtLength(0), b = p.getPointAtLength(p.getTotalLength());
      geo[p.dataset.edge] = { s: p.dataset.source, t: p.dataset.target, a: [a.x, a.y], b: [b.x, b.y] };
    }
    return { out, geo, pos };
  })()`);
  const badPlacement = [];
  for (const e of atlas.edges) {
    const got = (placement.out[e.id] || []).map((x) => x.join(' ')).sort().join(' | ');
    const want = [[e.source, 'out', e.target].join(' '), [e.target, 'in', e.source].join(' ')].sort().join(' | ');
    if (got !== want) badPlacement.push({ edge: e.id, got, want });
    const g = placement.geo[e.id];
    const ps = placement.pos[e.source], pt = placement.pos[e.target];
    if (!g || g.s !== e.source || g.t !== e.target || Math.abs(g.a[1] - ps[1]) > 0.6 || Math.abs(Math.abs(g.a[0] - ps[0]) - 19) > 0.6 ||
        Math.abs(g.b[1] - pt[1]) > 0.6 || Math.abs(Math.abs(g.b[0] - pt[0]) - 19) > 0.6) badPlacement.push({ edge: e.id, geometry: g, ps, pt });
  }
  const extra = Object.keys(placement.geo).filter((k) => !atlas.edges.some((e) => e.id === k));
  check('INV4: each edge listed once at each end, drawn from source to target, no other line', !badPlacement.length && !extra.length &&
        Object.keys(placement.geo).length === atlas.edges.length, { badPlacement, extra, drawn: Object.keys(placement.geo).length });

  // RT8/INV5: filters, a count line without numbers.
  await click('#atlas-q');
  await S('Input.insertText', { text: 'lift' });
  await sleep(200);
  const f1 = await js(`({ rows: [...document.querySelectorAll('.atlas-table tbody tr')].filter(r => !r.hidden).map(r => r.dataset.claim),
                          count: document.querySelector('.atlas-count').textContent })`);
  const wantLift = atlas.claims.filter((c) => (c.title + ' ' + c.statement + ' ' + c.hypotheses.join(' ') + ' ' + c.status.label).toLowerCase().includes('lift')).map((c) => c.id);
  check('RT8: word filter shows exactly the claims whose own text has the word', JSON.stringify(f1.rows) === JSON.stringify(wantLift), { f1, wantLift });
  check('INV5: the count line names no number', !/\d/.test(f1.count), f1.count);
  await click('.atlas-clear');
  await click('.atlas-tools .filter[data-atlas-status="conditional"]');
  const f2 = await js(`({ rows: [...document.querySelectorAll('.atlas-table tbody tr')].filter(r => !r.hidden).map(r => r.dataset.claim),
                          count: document.querySelector('.atlas-count').textContent,
                          dim: [...document.querySelectorAll('.atlas-map .atlas-node.is-out')].length })`);
  const wantCond = atlas.claims.filter((c) => c.status.code === 'conditional').map((c) => c.id);
  check('RT8: status filter shows exactly the conditional claims and dims the others in the map',
        JSON.stringify(f2.rows) === JSON.stringify(wantCond) && f2.dim === atlas.claims.length - wantCond.length && !/\d/.test(f2.count), f2);
  await click('.atlas-clear');

  // RT2/RT3: select from the index; the pane shows the claim, its statuses, hypotheses and every relation, in direction.
  await click(`#atlas-r-${hub} th .atlas-link`);
  const sel = await js(`(() => { const p = document.querySelector('.atlas-pane');
    const hood = [...p.querySelectorAll('.atlas-hood-edge')].map(e => ({ id: e.dataset.edge, s: e.dataset.source, t: e.dataset.target,
      a: e.getPointAtLength(0), b: e.getPointAtLength(e.getTotalLength()) })).map(x => ({ ...x, a: [x.a.x, x.a.y], b: [x.b.x, x.b.y] }));
    const pills = [...p.querySelectorAll('.atlas-hood-svg .atlas-node')].map(g => { const m = /translate\\(([\\d.]+) ([\\d.]+)\\)/.exec(g.getAttribute('transform')); return { c: g.dataset.claim, x: +m[1], y: +m[2] }; });
    return { hash: location.hash, state: history.state, hidden: p.hidden, title: p.querySelector('.atlas-pane-title')?.textContent.replace(/\\s+/g,' ').trim(),
      label: p.querySelector('.atlas-status-label')?.textContent.replace(/\\s+/g,' ').trim(), hyps: p.querySelectorAll('.atlas-hyps li').length,
      relIn: [...p.querySelectorAll('.atlas-rel-block[data-dir="in"] .atlas-rel')].map(li => li.dataset.edge),
      relOut: [...p.querySelectorAll('.atlas-rel-block[data-dir="out"] .atlas-rel')].map(li => li.dataset.edge),
      hood, pills, mapOn: [...document.querySelectorAll('.atlas-map .atlas-edge.is-on')].map(e => e.dataset.edge).sort(),
      rowSel: document.querySelector('.atlas-table tr.is-sel')?.dataset.claim,
      focus: document.activeElement?.className,
      ids: [...document.querySelectorAll('[id]')].map(e => e.id).filter((v, i, a) => a.indexOf(v) !== i) }; })()`);
  const wantIn = inOf(hub).map((e) => e.id).sort(), wantOut = outOf(hub).map((e) => e.id).sort();
  check('RT2: the pane shows the selected claim with its supplied status label and hypotheses',
        sel.title === plainTitle(hub) || sel.title.startsWith(plainTitle(hub).slice(0, 40)), { title: sel.title, want: plainTitle(hub) });
  check('RT2: status label and hypotheses as supplied', sel.label.includes(claimById[hub].status.label) && sel.hyps === claimById[hub].hypotheses.length, sel);
  check('RT3: pane lists exactly the relations into and from the claim',
        JSON.stringify([...sel.relIn].sort()) === JSON.stringify(wantIn) && JSON.stringify([...sel.relOut].sort()) === JSON.stringify(wantOut), { sel: [sel.relIn, sel.relOut], wantIn, wantOut });
  const badHood = sel.hood.filter((h) => {
    const e = atlas.edges.find((x) => x.id === h.id);
    if (!e || e.source !== h.s || e.target !== h.t) return true;
    const src = sel.pills.find((p) => p.c === h.s && Math.abs(h.a[0] - (p.x + 19)) < 1 && Math.abs(h.a[1] - p.y) < 9);
    const dst = sel.pills.find((p) => p.c === h.t && Math.abs(h.b[0] - (p.x - 19)) < 1 && Math.abs(h.b[1] - p.y) < 9);
    return !src || !dst;
  });
  check('INV4: the pane diagram draws each relation once, from its source to its target, and no other',
        sel.hood.length === wantIn.length + wantOut.length && !badHood.length, { n: sel.hood.length, badHood });
  check('RT3: the map marks exactly the selected claim\'s relations', JSON.stringify(sel.mapOn) === JSON.stringify([...wantIn, ...wantOut].sort()), sel.mapOn);
  check('RT9: selection is in the address and the history state', sel.hash === '#atlas-c-' + hub && sel.state && sel.state.atlasClaim === hub, { hash: sel.hash, state: sel.state });
  check('RT6: selection moves focus to the pane heading', /atlas-pane-title/.test(sel.focus || ''), sel.focus);
  check('INV6: no duplicate id after the pane is drawn', sel.ids.length === 0, sel.ids);
  check('index row of the selection is marked', sel.rowSel === hub, sel.rowSel);
  await shot('w1400-selected');

  // RT6: Escape in the pane returns focus to the index link of the selection.
  await press('Escape');
  const afterEsc = await active();
  check('RT6: Escape in the pane returns focus to the claim in the index', afterEsc && afterEsc.includes('#atlas-c-' + hub), afterEsc);

  // RT6: arrows in the index; Enter selects.
  await press('ArrowDown');
  const down = await active();
  const order = atlas.claims.map((c) => c.id);
  const next = order[order.indexOf(hub) + 1];
  check('RT6: Down moves to the next claim of the index', down && down.includes('#atlas-c-' + next), { down, next });
  await press('Enter');
  check('RT6: Enter on an index link selects that claim', (await paneTitle()) === plainTitle(next), await paneTitle());

  // RT3/RT9: move to a neighbour from the pane, then back and forward.
  await click(`#atlas-r-${hub} th .atlas-link`);
  const neighbour = outOf(hub)[0]?.target || inOf(hub)[0].source;
  await click(`.atlas-pane .atlas-rel .atlas-link[href="#atlas-c-${neighbour}"]`);
  const n1 = await paneTitle();
  await js('history.back()');
  await sleep(250);
  const n2 = await paneTitle();
  await js('history.forward()');
  await sleep(250);
  const n3 = await paneTitle();
  check('RT9: back and forward move between selections', n1 === plainTitle(neighbour) && n2.startsWith(plainTitle(hub).slice(0, 40)) && n3 === plainTitle(neighbour), { n1, n2, n3 });

  // RT9 with the page's own address rewrite: select A, open an example row, select B, Back gives A.
  const A = order[0], B = order[order.length - 1];
  await click(`#atlas-r-${A} th .atlas-link`);
  await click('details.row > summary');
  const rewritten = await js('location.hash');
  await click(`#atlas-r-${B} th .atlas-link`);
  await js('history.back()');
  await sleep(250);
  const backA = await paneTitle();
  check('RT9: after the page rewrites the address (a row opened), Back still restores the earlier selection',
        rewritten.startsWith('#row-') && backA === plainTitle(A), { rewritten, backA, want: plainTitle(A) });
  await js("document.querySelectorAll('details.row').forEach(d => d.open = false)");

  // A link elsewhere on the page leaves nothing selected; the pane shows its prompt.
  await js("location.hash = 'examples'");
  await sleep(200);
  const cleared = await js(`({ title: !!document.querySelector('.atlas-pane .atlas-pane-title'), prompt: !!document.querySelector('.atlas-pane .atlas-pane-prompt'),
                               on: document.querySelectorAll('.atlas-map .atlas-edge.is-on').length })`);
  check('RT9: an address that is not a claim leaves nothing selected', !cleared.title && cleared.prompt && cleared.on === 0, cleared);

  // Selecting from the map.
  await click(`.atlas-map .atlas-node[data-claim="${order[1]}"]`);
  check('RT3: a mark of the map selects its claim', (await paneTitle()) === plainTitle(order[1]), await paneTitle());

  // Term card inside the pane: Escape closes the card first and focus stays in the pane.
  const termClaim = atlas.claims.find((c) => /weak module/.test(c.statement));
  if (termClaim) {
    await click(`#atlas-r-${termClaim.id} th .atlas-link`);
    const hasTerm = await js(`!!document.querySelector('.atlas-pane .term')`);
    if (hasTerm) {
      await click('.atlas-pane .term');
      const cardOpen = await js(`!document.getElementById('card').hidden`);
      await press('Escape');
      const st = await js(`({ card: document.getElementById('card').hidden, focus: document.activeElement?.className, title: !!document.querySelector('.atlas-pane .atlas-pane-title') })`);
      check('RT6: with the term card open in the pane, Escape closes the card and keeps the selection', cardOpen && st.card && /term/.test(st.focus || '') && st.title, { cardOpen, st });
    } else check('RT6: the pane copy carries the glossary term', false, 'no .term in pane');
  }

  // Relation toggles act on the pane only and say what they hide.
  await click(`#atlas-r-${hub} th .atlas-link`);
  const kinds = [...new Set([...inOf(hub), ...outOf(hub)].map((e) => e.relation))];
  if (kinds.length > 1) {
    await click(`.atlas-pane .atlas-hood-legend .filter[data-atlas-relation="${kinds[0]}"]`);
    const tg = await js(`(() => { const p = document.querySelector('.atlas-pane');
      return { hiddenItems: [...p.querySelectorAll('.atlas-rel[hidden]')].map(li => li.dataset.relation),
               hiddenLines: [...p.querySelectorAll('.atlas-hood-edge.is-hidden')].length,
               note: p.querySelector('.atlas-hidden-note')?.hidden === false ? p.querySelector('.atlas-hidden-note').textContent : null,
               mapOn: document.querySelectorAll('.atlas-map .atlas-edge.is-on').length }; })()`);
    const nKind = [...inOf(hub), ...outOf(hub)].filter((e) => e.relation === kinds[0]).length;
    check('RT3: hiding a relation type hides it in the pane only and names it', tg.hiddenItems.length === nKind && tg.hiddenItems.every((r) => r === kinds[0]) &&
          tg.hiddenLines === nKind && tg.note && tg.mapOn === wantIn.length + wantOut.length, tg);
    await click(`.atlas-pane .atlas-hood-legend .filter[data-atlas-relation="${kinds[0]}"]`);
  }

  // RT5: follow the path joined by recorded relations.
  const dep = atlas.readingPaths.find((p) => p.kind === 'source_bound_dependency_path');
  if (dep) {
    await click(`#atlas-p-${dep.id} .atlas-path-tools .link-btn`);
    const steps = dep.stages.flatMap((s) => s.claimIds);
    const seen = [await paneTitle()];
    for (let i = 1; i < steps.length; i++) {
      await click('.atlas-pane .atlas-pathbar-actions .link-btn:nth-child(2)');
      seen.push(await paneTitle());
    }
    const here = await js(`[...document.querySelectorAll('#atlas-p-${dep.id} .atlas-stage.is-here')].map(s => s.dataset.stage)`);
    const where = await js(`document.querySelector('.atlas-pane .atlas-pathbar-where')?.textContent`);
    check('RT5: Follow walks the path claim by claim in stage order', JSON.stringify(seen.map((t) => t.slice(0, 40))) === JSON.stringify(steps.map((id) => plainTitle(id).slice(0, 40))) &&
          JSON.stringify(here) === JSON.stringify([String(dep.stages.length - 1)]), { seen, here });
    check('INV5: the path position names no total', where && !/\bof\b/.test(where), where);
    await click('.atlas-pane .atlas-pathbar-actions .link-btn:last-child');
    check('RT5: Leave the path removes the path bar', await js(`!document.querySelector('.atlas-pane .atlas-pathbar') || document.querySelector('.atlas-pane .atlas-pathbar').hidden`), null);
    const kindsShown = await js(`[...document.querySelectorAll('.atlas-path')].map(a => [a.dataset.path, a.querySelector('.atlas-kind-tag').textContent])`);
    check('RT5: editorial and joined paths are labelled differently', new Set(kindsShown.map((k) => k[1])).size === new Set(atlas.readingPaths.map((p) => p.kind)).size, kindsShown);
  }

  // INV5 over the whole atlas: no percentage, no "N of M", no number before a status word, in text and labels.
  const scan = await js(`(() => { const a = document.getElementById('atlas');
    const text = a.innerText + ' ' + [...a.querySelectorAll('[aria-label],[title]')].map(e => (e.getAttribute('aria-label') || '') + ' ' + (e.getAttribute('title') || '')).join(' ');
    const bad = [/%/, /\\b\\d+\\s+of\\s+\\d+\\b/i, /\\b(progress|completed?|completion|percent)\\b/i, /\\b\\d+\\s+(established|conditional|scoped|remaining|claims?|theorems?)\\b/i];
    return bad.map(r => (text.match(r) || [null])[0]); })()`);
  check('INV5: no percentage, progress word, "N of M" or count of statuses anywhere in the atlas', scan.every((x) => x === null), scan);

  // Arrival with a claim in the address.
  await load('#atlas-c-' + order[2]);
  check('RT9: arriving with #atlas-c-<id> shows that claim', (await paneTitle()) === plainTitle(order[2]), await paneTitle());
  await shot('w1400-arrival');
  collect();

  // INV11: contrast of atlas text, marks and lines, light and dark.
  const contrast = async (theme) => {
    await media([{ name: 'prefers-color-scheme', value: theme }]);
    await load();
    await click(`#atlas-r-${hub} th .atlas-link`);
    return js(`(() => {
      const parse = s => { const m = s.match(/[\\d.]+/g).map(Number); if (s.startsWith('color(')) return [m[0]*255, m[1]*255, m[2]*255, m[3] ?? 1]; return [m[0], m[1], m[2], m[3] ?? 1]; };
      const lum = c => { const a = c.slice(0,3).map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }); return 0.2126*a[0] + 0.7152*a[1] + 0.0722*a[2]; };
      const over = (f, b) => [0,1,2].map(i => f[i] * f[3] + b[i] * (1 - f[3])).concat(1);
      const bg = el => { const stack = []; for (let n = el; n; n = n.parentElement) { const c = parse(getComputedStyle(n).backgroundColor); if (c[3] > 0) stack.push(c); if (c[3] >= 1) break; }
        let b = parse(getComputedStyle(document.body).backgroundColor); for (let i = stack.length - 1; i >= 0; i--) b = over(stack[i], b); return b; };
      const ratio = (f, b) => { const l1 = lum(f), l2 = lum(b); return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05); };
      const res = [];
      const TEXT = ['.atlas-intro', '.atlas-key-item dd', '.atlas-key-sub', '.atlas-key-h', '.atlas-domain-summary p', '.atlas-link-title', '.atlas-num', '.atlas-group-h span',
        '.atlas-none', '.atlas-table thead th', '.atlas-col-n', '.atlas-col-status span', '.atlas-caption', '.atlas-fig-h', '.atlas-rel-label', '.atlas-rel-self',
        '.atlas-rel-scope', '.atlas-chip-group', '.atlas-stage-n', '.atlas-kind-tag', '.atlas-count', '.atlas-pane-label', '.atlas-pane .atlas-status-label',
        '.atlas-note-label', '.atlas-lane', '.atlas-overview p', '.atlas-path-kind', '.atlas-item-hyps', '.atlas-sub-h', '.atlas-domain-comps', '.atlas-join-back',
        '.atlas-tools .filter span', '.atlas-tools .filters-label', '.atlas-words label', '.atlas-parts a'];
      for (const sel of TEXT) for (const el of [...document.querySelectorAll('#atlas ' + sel)].filter(e => e.getClientRects().length).slice(0, 3)) {
        const r = ratio(over(parse(getComputedStyle(el).color), bg(el)), bg(el)); res.push({ sel, kind: 'text', r: +r.toFixed(2), ok: r >= 4.5 }); }
      for (const el of [...document.querySelectorAll('#atlas svg.am')].filter(e => e.getClientRects().length).slice(0, 40)) {
        const r = ratio(parse(getComputedStyle(el).color), bg(el)); res.push({ sel: 'mark ' + el.getAttribute('class'), kind: 'mark', r: +r.toFixed(2), ok: r >= 3 }); }
      const map = document.querySelector('.atlas-map'); map.classList.remove('is-focus');
      document.querySelectorAll('.atlas-map .is-on, .atlas-map .is-sel').forEach(n => n.classList.remove('is-on', 'is-sel'));
      const scroll = document.querySelector('.atlas-map-scroll');
      for (const p of [...document.querySelectorAll('.atlas-map .atlas-edge')].slice(0, 3)) {
        const cs = getComputedStyle(p); const c = parse(cs.stroke); c[3] = (c[3] ?? 1) * Number(cs.opacity);
        const r = ratio(over(c, bg(scroll)), bg(scroll)); res.push({ sel: 'map line ' + p.getAttribute('class'), kind: 'line', r: +r.toFixed(2), ok: r >= 3 }); }
      for (const p of [...document.querySelectorAll('.atlas-pane .atlas-hood-edge')].slice(0, 3)) {
        const cs = getComputedStyle(p); const c = parse(cs.stroke); c[3] = (c[3] ?? 1) * Number(cs.opacity);
        const pane = document.querySelector('.atlas-pane'); const r = ratio(over(c, bg(pane)), bg(pane)); res.push({ sel: 'pane line', kind: 'line', r: +r.toFixed(2), ok: r >= 3 }); }
      return res; })()`);
  };
  for (const theme of ['light', 'dark']) {
    const res = await contrast(theme);
    const bad = res.filter((r) => !r.ok);
    check(`INV11: contrast of atlas text (4.5:1), marks and lines (3:1), ${theme}`, !bad.length && res.length > 30, { checked: res.length, bad, min: Math.min(...res.map((r) => r.r)) });
  }
  await media([]);

  // RT7/INV9: widths, themes, no page-level horizontal scroll, the pane as a sheet on narrow screens.
  const widths = quick ? [1400, 375] : [1400, 1024, 768, 480, 375];
  for (const theme of ['light', 'dark']) {
    await media([{ name: 'prefers-color-scheme', value: theme }]);
    for (const w of widths) {
      await size(w, w < 600 ? 820 : 900);
      await load();
      const o = await js(`({ sw: document.documentElement.scrollWidth, iw: window.innerWidth,
        wideItems: [...document.querySelectorAll('#atlas *')].filter(e => { const r = e.getBoundingClientRect(); return r.width && r.right > window.innerWidth + 1 && !e.closest('.atlas-map-scroll, .atlas-table-wrap, .math-display, .math-long, .nav'); }).slice(0, 5).map(e => e.className || e.localName) })`);
      check(`INV9: no page-level horizontal scroll at ${w}px (${theme})`, o.sw <= o.iw && !o.wideItems.length, o);
      for (const part of ['atlas-domains', 'atlas-claims', 'atlas-comparisons', 'atlas-paths']) {
        await js(`document.getElementById('${part}').scrollIntoView({ block: 'start', behavior: 'instant' })`);
        await sleep(80);
        await shot(`w${w}-${theme}-${part}`);
      }
      await click(`#atlas-r-${hub} th .atlas-link`);
      const p = await js(`(() => { const p = document.querySelector('.atlas-pane'); const r = p.getBoundingClientRect();
        return { hidden: p.hidden, pos: getComputedStyle(p).position, top: r.top, bottom: r.bottom, h: innerHeight, left: r.left, right: r.right, w: innerWidth }; })()`);
      const okPane = w >= 1000 ? (p.pos === 'sticky' && !p.hidden && p.top >= 0 && p.bottom <= p.h + 1)
                               : (p.pos === 'fixed' && !p.hidden && Math.abs(p.bottom - p.h) < 2 && p.left === 0 && Math.abs(p.right - p.w) < 2);
      check(`RT7: the pane at ${w}px (${theme}) is ${w >= 1000 ? 'beside the atlas' : 'a sheet at the foot of the window'}`, okPane, p);
      await shot(`w${w}-${theme}-pane`);
      if (w < 1000) {
        await press('Escape');
        const closed = await js(`${PANE}.hidden`);
        check(`RT7: Escape closes the sheet at ${w}px (${theme})`, closed, closed);
      }
      collect();
    }
  }
  await media([]);
  await size(1400);

  // INV10: reduced motion.
  await media([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
  await load();
  const rm = await js(`({ scroll: getComputedStyle(document.documentElement).scrollBehavior,
    t: [...document.querySelectorAll('.atlas-map .atlas-edge, .atlas-table td')].slice(0, 5).map(e => getComputedStyle(e).transitionDuration) })`);
  check('INV10: reduced motion: no smooth scrolling and no transitions in the atlas', rm.scroll === 'auto' && rm.t.every((d) => d.split(',').every((x) => parseFloat(x) === 0)), rm);
  await media([]);

  // RT7: print, A4 and Letter; the filtered and selected screen state does not reach paper.
  await load();
  await click('#atlas-q');
  await S('Input.insertText', { text: 'lift' });
  await sleep(200);
  await click(`#atlas-r-${hub} th .atlas-link`);
  await media([{ name: 'prefers-color-scheme', value: 'dark' }]);
  await S('Emulation.setEmulatedMedia', { media: 'print', features: [{ name: 'prefers-color-scheme', value: 'dark' }] });
  const pr = await js(`(() => { const vis = s => [...document.querySelectorAll(s)].filter(e => e.getClientRects().length).length;
    return { full: vis('.atlas-claims-full .atlas-claim'), rows: vis('.atlas-table tbody tr'), pane: vis('.atlas-pane'), tools: vis('.atlas-tools'),
             domains: vis('.atlas-domain'), comparisons: vis('.atlas-comparison'), paths: vis('.atlas-path'), dim: [...document.querySelectorAll('.atlas-map .atlas-node')].filter(n => getComputedStyle(n).opacity !== '1').length,
             bg: getComputedStyle(document.body).backgroundColor }; })()`);
  check('RT7: print shows every claim in full, every index row, the domains, comparisons and paths, and no screen controls',
        pr.full === atlas.claims.length && pr.rows === atlas.claims.length && pr.pane === 0 && pr.tools === 0 && pr.domains === atlas.domains.length &&
        pr.comparisons === atlas.comparisons.length && pr.paths === atlas.readingPaths.length && pr.dim === 0, pr);
  for (const [name, w, h] of [['a4', 8.27, 11.69], ['letter', 8.5, 11]]) {
    const { data } = await S('Page.printToPDF', { paperWidth: w, paperHeight: h, printBackground: false, preferCSSPageSize: false });
    writeFileSync(join(out, `print-${name}.pdf`), Buffer.from(data, 'base64'));
    check(`RT7: print to ${name} produced a PDF`, data.length > 1000, { bytes: Math.round(data.length * 0.75) });
  }
  await S('Emulation.setEmulatedMedia', { media: '', features: [] });
  collect();
  check('INV9: no console error, warning or exception during all checks', problems.length === 0, problems);
} catch (error) {
  check('the browser run completed', false, String(error && error.stack || error));
} finally {
  const exited = new Promise((r) => { if (chrome.exitCode !== null) r(); else chrome.once('exit', r); });
  try { await Promise.race([send('Browser.close'), sleep(2000)]); } catch (e) { /* already closed */ }
  await Promise.race([exited, sleep(3000)]);
  try { chrome.kill(); } catch (e) { /* gone */ }
  rmSync(profile, { recursive: true, force: true, maxRetries: 10, retryDelay: 200 });
}
const failed = results.filter((r) => !r.ok);
writeFileSync(join(out, 'results.json'), JSON.stringify({ page: resolve(page), atlas: resolve(fixtureArg), passed: results.length - failed.length, failed: failed.length, results }, null, 1) + '\n');
console.log(`${results.length - failed.length} passed, ${failed.length} failed`);
process.exit(failed.length ? 1 : 0);
