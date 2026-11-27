const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const file = process.argv[2];
const html = fs.readFileSync(file, 'utf8');
const vc = new VirtualConsole();
const errors = [];
vc.on('jsdomError', e => errors.push('jsdomError: ' + (e.message || e)));
vc.on('error', e => errors.push('console.error: ' + e));
const t0 = Date.now();
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html', virtualConsole: vc });
const t1 = Date.now();
const d = dom.window.document;
const count = s => d.querySelectorAll(s).length;
console.log(JSON.stringify({
  parseAndRunMs: t1 - t0,
  errors,
  sections: [...d.querySelectorAll('main section.section')].map(s => s.id),
  statements: count('main .statement'), rows: count('details.row'), details: count('main details'),
  questions: count('.question'), failures: count('.failure'), openGroups: count('.open-group'), gloss: count('.gloss'),
  ids: count('[id]'), terms: count('button.term'), cells: count('.cell-btn'), math: count('math'),
  find: !!d.querySelector('.find'), findInput: !!d.getElementById('find-q'),
  navLinks: [...d.querySelectorAll('.nav a')].map(a => a.getAttribute('href')),
  tally: [...d.querySelectorAll('.tally a')].map(a => a.getAttribute('data-filter') + ':' + a.querySelector('.count').textContent),
}, null, 1));
