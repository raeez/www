/* The ids a page serves for its statements equal the ids its script gives them; without the script, its script-only
   controls are hidden; how many marks and terms are served with a description.
     NODE_PATH=<node_modules with jsdom> node served-ids.cjs <served.html> <same page or another build of it> */
const { JSDOM } = require('jsdom');
const fs = require('fs');
const served = new JSDOM(fs.readFileSync(process.argv[2], 'utf8')).window.document;
const client = new JSDOM(fs.readFileSync(process.argv[3], 'utf8'), { runScripts: 'dangerously', pretendToBeVisual: true,
  url: 'https://raeez.com/quantum-holography-tracker.html', beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } }).window.document;
const a = [...served.querySelectorAll('main .statement')].map(s => s.id);
const b = [...client.querySelectorAll('main .statement')].map(s => s.id);
console.log('statements', a.length, b.length, 'served without id', a.filter(x => !x).length, 'identical ids in order', JSON.stringify(a) === JSON.stringify(b));
console.log('no-script: hidden script-only controls', [...served.querySelectorAll('[data-needs-script]')].map(e => e.className + ':' + e.hidden).join(' '));
console.log('served cell descriptions', served.querySelectorAll('.cell-btn[aria-describedby]').length, 'terms', served.querySelectorAll('.term[aria-describedby]').length);
