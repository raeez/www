const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const vc = new VirtualConsole(); vc.on('jsdomError', e => console.log('JSDOMERR', e.message));
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html' + process.argv[3], virtualConsole: vc,
  beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
const w = dom.window, d = w.document;
setTimeout(() => {
  const n = [...d.querySelectorAll('.qh-notice')];
  console.log('notices', n.length, n.map(x => x.getAttribute('data-notice') + ' | ' + x.textContent));
  console.log('url', w.location.href);
}, 120);
