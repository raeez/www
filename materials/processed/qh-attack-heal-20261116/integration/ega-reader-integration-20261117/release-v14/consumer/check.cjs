#!/usr/bin/env node
'use strict';
const fs = require('fs');
const path = require('path');
const { JSDOM, VirtualConsole } = require('jsdom');
const [site, output] = process.argv.slice(2);
if (!site || !output) throw new Error('usage: check.cjs <site directory> <report.json>');
const requirements = JSON.parse(fs.readFileSync(path.join(__dirname, 'requirements.json'), 'utf8'));
const indexText = fs.readFileSync(path.join(site, 'reader-index.js'), 'utf8');
const units = JSON.parse(indexText.replace(/^window.QH_READER_INDEX = /, '').replace(/;\n$/, '')).units;
const checks = [];
const check = (name, pass, details) => checks.push({ name, pass: !!pass, ...(details || {}) });
const sleep = ms => new Promise(r => setTimeout(r, ms));
function page(name) {
  let markup = fs.readFileSync(path.join(site, name), 'utf8');
  markup = markup.replace('<script type="application/json" id="reader-pages">', '<script>' + indexText + '</script><script type="application/json" id="reader-pages">');
  const errors = [], leaves = [], scrolls = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => { if (!/Not implemented/.test(String(e && e.message))) errors.push(String(e.message || e)); });
  const dom = new JSDOM(markup, { url: 'https://example.org/' + name, runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc,
    beforeParse(w) { w.Element.prototype.scrollIntoView = function () { scrolls.push(this.id); }; w.scrollTo = function () {};
      w.addEventListener('qh:leave', e => { leaves.push(JSON.parse(JSON.stringify(e.detail))); e.preventDefault(); }, true); }
  });
  return { dom, w: dom.window, d: dom.window.document, errors, leaves, scrolls };
}
async function query(p, title) {
  const q = p.d.getElementById('reader-q');
  if (q.closest('[hidden]')) p.d.querySelector('.reader-search-toggle').click();
  q.value = title; q.dispatchEvent(new p.w.Event('input', { bubbles: true }));
  await sleep(350);
  return [...p.d.querySelectorAll('#reader-results .reader-hit-link')];
}
(async () => {
  requirements.headings.forEach(row => check('shared_heading_title_and_destination', units.filter(u => u.page === row.page && u.id === row.id && u.title === row.title && u.kind === 'heading').length === 1, { id: row.id }));
  let p = page('index.html'); await sleep(120);
  const ev = new p.w.CustomEvent('qh:reader-units', { detail: {} }); p.d.dispatchEvent(ev);
  for (const row of requirements.headings) {
    check('live_local_heading_unit', ev.detail.units.filter(u => u.id === row.id && u.title === row.title && u.kind === 'heading').length === 1, { id: row.id });
    const hits = await query(p, row.title); const hit = hits.find(a => a.getAttribute('href') === '#' + row.id);
    check('local_exact_title_result', !!hit, { id: row.id });
    if (hit) { p.scrolls.length = 0; hit.click(); await sleep(20); check('local_result_navigation', p.scrolls.includes(row.id), { id: row.id }); }
  }
  check('book_no_script_errors', !p.errors.length, { errors: p.errors }); p.w.close(); if (global.gc) global.gc();
  p = page('reference.html'); await sleep(120);
  for (const row of requirements.headings) {
    const hits = await query(p, row.title); check('companion_exact_title_result', hits.some(a => a.getAttribute('href') === row.page + '#' + row.id), { id: row.id });
  }
  for (const row of requirements.links) {
    const links = [...p.d.querySelectorAll('a[href]')].filter(a => a.getAttribute('href') === row.href && a.textContent === row.label);
    check('authored_label_and_href', links.length === 1, { href: row.href });
    const [name, id] = row.href.split('#');
    const markup = fs.readFileSync(path.join(site, name), 'utf8');
    check('link_destination_exists', markup.includes('id="' + id + '"'), { href: row.href });
    if (links.length === 1) { const n = p.leaves.length; links[0].click(); check('existing_cross_page_navigation', p.leaves.length === n + 1 && p.leaves[n].url === new URL(row.href, p.w.location.href).href, { href: row.href }); }
  }
  check('reference_no_script_errors', !p.errors.length, { errors: p.errors }); p.w.close(); if (global.gc) global.gc();
  const result = { status: checks.every(x => x.pass) ? 'PASS' : 'FAIL', check_count: checks.length, failures: checks.filter(x => !x.pass), checks, search_units: units.length, heading_requirements: requirements.headings.length, authored_links: requirements.links.length };
  fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
  console.log(JSON.stringify({ status: result.status, check_count: checks.length, failures: result.failures, search_units: units.length }));
  process.exit(result.failures.length ? 1 : 0);
})();
