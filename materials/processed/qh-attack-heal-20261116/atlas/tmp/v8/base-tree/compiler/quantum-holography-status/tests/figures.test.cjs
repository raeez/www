/* Reader tests of figures.js in jsdom: node figures.test.cjs <preview.html>. jsdom is read from NODE_PATH. */
'use strict';
const fs = require('fs');
const assert = require('assert');
const { JSDOM } = require('jsdom');
const PAGE = fs.readFileSync(process.argv[2], 'utf8');
function load() { return new JSDOM(PAGE, { runScripts: 'dangerously', pretendToBeVisual: true }).window; }
function input(w, el, v) { el.value = String(v); el.dispatchEvent(new w.Event('input', { bubbles: true })); }
const tests = [];
function test(name, fn) { tests.push({ name, fn }); }

test('Gaussian: every permitted control is a range input inside its authored window', () => {
  const w = load(), fig = w.document.querySelector('figure[data-figure-model="gaussian-elimination"]');
  if (!fig) return 'SKIP';
  const cfg = JSON.parse(fig.getAttribute('data-config'));
  const inputs = fig.querySelectorAll('input[type="range"]');
  assert.equal(inputs.length, Object.keys(cfg.controls).length);
  for (const i of inputs) {
    const n = i.id.split('--').pop(), c = cfg.controls[n];
    assert.equal(+i.min, c.min); assert.equal(+i.max, c.max); assert.equal(+i.step, c.step); assert.equal(+i.value, c.initial);
    assert.ok(fig.querySelector(`label[for="${i.id}"]`), 'each control keeps its authored label');
  }
});

test('Gaussian: a value inside the validity rule updates every authored value', () => {
  const w = load(), fig = w.document.querySelector('figure[data-figure-model="gaussian-elimination"]');
  if (!fig) return 'SKIP';
  const a = fig.querySelector('input[id$="--a"]');
  input(w, a, 3);
  const k = fig.querySelector('output[data-value="effective_stiffness"]');
  if (k) assert.equal(k.textContent, '2.75', 'a - c^2/b at a=3, b=1, c=0.5');
  assert.equal(fig.querySelector('output[data-value="a"]').textContent, '3');
  assert.ok(fig.querySelector('.qh-fig-invalid').hidden);
});

test('Gaussian: a value outside the rule is refused, the authored message shows, the previous values stay', () => {
  const w = load(), fig = w.document.querySelector('figure[data-figure-model="gaussian-elimination"]');
  if (!fig) return 'SKIP';
  const c = fig.querySelector('input[id$="--c"]');
  const before = Array.from(fig.querySelectorAll('output[data-value]')).map(o => o.textContent);
  input(w, c, 1.9);  /* a=2, b=1: ab = 2 < 3.61 */
  assert.equal(+c.value, 0.5, 'the control returns to the previous valid value');
  assert.equal(fig.querySelector('.qh-fig-invalid').hidden, false, 'the authored message is shown');
  assert.deepEqual(Array.from(fig.querySelectorAll('output[data-value]')).map(o => o.textContent), before, 'no value changed');
});

test('Gaussian: the three profiles keep their own integrals; a constant one is written once', () => {
  const w = load(), fig = w.document.querySelector('figure[data-figure-model="gaussian-elimination"]');
  if (!fig) return 'SKIP';
  const cfg = JSON.parse(fig.getAttribute('data-config'));
  const dens = cfg.profiles.find(p => p.density), other = cfg.profiles.find(p => !p.density);
  const read = id => fig.querySelector(`.qh-fig-profile[data-profile="${id}"] .qh-fig-integral-value`);
  if (dens) {
    assert.equal(read(dens.id).querySelector('output'), null, 'the constant has no readout of its own');
    assert.equal(read(dens.id).textContent.includes('='), false, 'never "1 = 1"');
  }
  const before = other && read(other.id).querySelector('output').textContent;
  input(w, fig.querySelector('input[id$="--b"]'), 2);
  if (dens) assert.equal(read(dens.id).querySelector('output'), null, 'a density integrates to one at every b');
  if (other) assert.notEqual(read(other.id).querySelector('output').textContent, before, 'the other integrals follow b');
  assert.equal(fig.querySelectorAll('.qh-fig-area').length, 0, 'no filled area');
});

test('Expansions: the choice moves between the two authored states only, and redraws the region', () => {
  const w = load(), fig = w.document.querySelector('figure[data-figure-model="two-expansions"]');
  if (!fig) return 'SKIP';
  const buttons = fig.querySelectorAll('button.qh-fig-choose');
  assert.equal(buttons.length, 2);
  assert.equal(fig.querySelectorAll('input').length, 0, 'no truncation control');
  buttons[1].click();
  const states = fig.querySelectorAll('.qh-fig-state');
  assert.equal(states[1].getAttribute('aria-current'), 'true');
  assert.equal(states[0].hasAttribute('aria-current'), false);
  const region = fig.querySelector('[data-part="region"]');
  assert.equal(region.localName, 'path', 'the exterior region');
  buttons[0].click();
  assert.equal(fig.querySelector('[data-part="region"]').localName, 'circle', 'the disk again');
});

test('Expansions: the chosen region carries its own condition', () => {
  const w = load(), fig = w.document.querySelector('figure[data-figure-model="two-expansions"]');
  if (!fig) return 'SKIP';
  const cfg = JSON.parse(fig.getAttribute('data-config'));
  fig.querySelectorAll('button.qh-fig-choose')[1].click();
  assert.equal(fig.querySelector('[data-part="region-label"]').textContent, cfg.states[1].text);
  assert.equal(fig.querySelector('[data-part="region-label"]').getAttribute('text-anchor'), cfg.states[1].at[2]);
  fig.querySelectorAll('button.qh-fig-choose')[0].click();
  assert.equal(+fig.querySelector('[data-part="region-label"]').getAttribute('x'), cfg.states[0].at[0], 'back inside the disk');
});

test('Cohomology: each value of t redraws the complex from its own matrix, contraction and survivors', () => {
  const w = load(), fig = w.document.querySelector('figure[data-figure-model="cohomology-jump"]');
  if (!fig) return 'SKIP';
  const cfg = JSON.parse(fig.getAttribute('data-config'));
  const buttons = Array.from(fig.querySelectorAll('button.qh-fig-choose'));
  assert.equal(buttons.length, cfg.states.length);
  cfg.states.forEach((s, k) => {
    buttons[k].click();
    const svg = fig.querySelector('.qh-fig-complex');
    assert.equal(svg.querySelector('[data-part="first"]').getAttribute('d'), s.toV ? cfg.paths.v : cfg.paths.zero, s.id);
    assert.equal(svg.querySelector('[data-part="first-zero"]').hasAttribute('display'), s.toV, 'the 0 target only where the entry is zero');
    assert.equal(svg.querySelector('[data-part="h"]').hasAttribute('display'), !s.h, 'the contraction only where the state gives one');
    assert.equal(svg.querySelector('[data-part="h-label"]').textContent, s.h);
    const alive = Array.from(svg.querySelectorAll('.qh-fig-basis.is-alive')).map(g => g.getAttribute('data-basis')).sort();
    assert.deepEqual(alive, s.alive.slice().sort());
    assert.equal(fig.querySelector('tr[aria-current="true"]').getAttribute('data-state-row'), s.id);
    assert.equal(fig.querySelector('.qh-fig-state[aria-current="true"]').getAttribute('data-state'), s.id);
    assert.equal(buttons[k].getAttribute('aria-pressed'), 'true');
  });
});

test('Infinite rank: N redraws the finite diagonal and its rank; the limit does not move', () => {
  const w = load(), fig = w.document.querySelector('figure[data-figure-model="infinite-rank"]');
  if (!fig) return 'SKIP';
  const cfg = JSON.parse(fig.getAttribute('data-config'));
  const input = fig.querySelector('input[type="range"][id$="--N"]');
  assert.equal(+input.min, cfg.control.min); assert.equal(+input.max, cfg.control.max); assert.equal(+input.value, cfg.control.initial);
  const fin = fig.querySelector('svg[data-grid="' + cfg.grids[0].id + '"]'), lim = fig.querySelector('svg[data-grid="' + cfg.grids[1].id + '"]');
  const limBefore = lim.innerHTML;
  input.value = '5'; input.dispatchEvent(new w.Event('input', { bubbles: true }));
  const on = Array.from(fin.querySelectorAll('.qh-fig-cell.is-on')).map(c => c.getAttribute('data-i') + c.getAttribute('data-j'));
  assert.deepEqual(on, ['00', '11', '22', '33', '44']);
  assert.equal(fin.querySelector('.qh-fig-cell[data-i="4"][data-j="4"] text').textContent, '1');
  assert.equal(fin.querySelector('.qh-fig-cell[data-i="5"][data-j="5"] text').textContent, '0');
  assert.equal(fig.querySelector('output[data-value="rank:' + cfg.rank.id + '"]').textContent, '5');
  assert.equal(fig.querySelector('output[data-value="N"]').textContent, '5');
  assert.equal(lim.innerHTML, limBefore, 'the limit is the same at every N');
  assert.equal(fin.querySelector('[data-part="beyond"]').classList.contains('is-on'), false);
});

test('Adjunction: the unit and counit keys pick out the arrows built from them', () => {
  const w = load(), fig = w.document.querySelector('figure[data-figure-model="adjunction-triangles"]');
  if (!fig) return 'SKIP';
  const unit = fig.querySelector('.qh-fig-key[data-key="eta"] button'), counit = fig.querySelector('.qh-fig-key[data-key="epsilon"] button');
  assert.ok(unit && counit, 'the two keys are buttons');
  unit.click();
  assert.equal(fig.getAttribute('data-emphasis'), 'unit'); assert.equal(unit.getAttribute('aria-pressed'), 'true');
  counit.click();
  assert.equal(fig.getAttribute('data-emphasis'), 'counit'); assert.equal(unit.getAttribute('aria-pressed'), 'false');
  counit.click();
  assert.equal(fig.hasAttribute('data-emphasis'), false, 'pressed again, the emphasis is released');
  assert.equal(fig.querySelectorAll('.qh-fig-arrow.is-unit').length, 2);
  assert.equal(fig.querySelectorAll('.qh-fig-arrow.is-counit').length, 2);
});

let failed = 0, skipped = 0;
for (const t of tests) {
  try { const r = t.fn(); if (r === 'SKIP') { skipped++; console.log('SKIP ' + t.name); } else console.log('PASS ' + t.name); }
  catch (e) { failed++; console.log('FAIL ' + t.name + '\n      ' + String(e && e.message || e).split('\n').slice(0, 4).join('\n      ')); }
}
console.log(failed ? failed + ' failed' : 'all passed' + (skipped ? '; ' + skipped + ' skipped' : ''));
process.exit(failed ? 1 : 0);
