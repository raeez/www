const { JSDOM } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html',
  beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
const w = dom.window, d = w.document;
const log = [];
w.addEventListener('popstate', e => log.push('popstate ' + JSON.stringify(e.state) + ' ' + w.location.hash));
w.addEventListener('hashchange', () => log.push('hashchange ' + w.location.hash));
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  await sleep(30);
  const boxes = d.querySelectorAll('main .math-display, main .math-long');
  const inDetails = [...boxes].filter(b => b.closest('details')).length;
  console.log('math boxes', boxes.length, 'inside details', inDetails);
  d.querySelector('.nav a[href="#examples"]').click(); await sleep(20);
  w.location.hash = 's-' + 'x-nope'; await sleep(20);
  w.history.pushState({ a: 1 }, '', '#results'); await sleep(20);
  w.history.back(); await sleep(50);
  w.history.back(); await sleep(50);
  w.history.forward(); await sleep(50);
  console.log(log.join('\n'));
  console.log('history.length', w.history.length, 'final', w.location.href);
})();
