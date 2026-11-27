const { JSDOM } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html',
  beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
const w = dom.window, d = w.document;
setTimeout(() => {
  const det = [...d.querySelectorAll('main details')];
  const before = det.filter(x => x.open).length;
  w.dispatchEvent(new w.Event('beforeprint'));
  w.dispatchEvent(new w.Event('beforeprint'));   /* a second print dialog before the first afterprint */
  w.dispatchEvent(new w.Event('afterprint'));
  console.log('open before', before, 'open after restore', det.filter(x => x.open).length, 'of', det.length);
}, 50);
