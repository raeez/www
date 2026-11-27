const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const vc = new VirtualConsole(); vc.on('jsdomError', e => console.log('JSDOMERR', e.message));
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html', virtualConsole: vc,
  beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
const w = dom.window, d = w.document;
setTimeout(() => {
  const rowSt = {}; d.querySelectorAll('.rows .statement').forEach(s => { rowSt[s.dataset.status] = (rowSt[s.dataset.status] || 0) + 1; });
  console.log('row statement statuses', rowSt);
  console.log('Show chips', [...d.querySelectorAll('.row-tools .filter')].map(f => f.dataset.filter));
  const chip = d.querySelector('.row-tools .filter[data-filter="conditional"]');
  if (chip) { chip.click();
    const live = d.querySelector('.row-tools [role=status]');
    console.log('after Conditional: visible statements in rows', d.querySelectorAll('.rows .statement:not([hidden])').length,
      'open rows', d.querySelectorAll('details.row[open]').length, 'filter-empty rows', d.querySelectorAll('details.row[data-filter-empty]').length,
      'live text:', JSON.stringify(live && live.textContent), 'live class:', live && live.className, 'url', w.location.search); }
}, 50);
