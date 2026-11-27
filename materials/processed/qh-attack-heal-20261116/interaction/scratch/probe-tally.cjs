const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const vc = new VirtualConsole(); vc.on('jsdomError', e => console.log('JSDOMERR', e.message));
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html', virtualConsole: vc,
  beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
const w = dom.window, d = w.document;
const sleep = ms => new Promise(r => setTimeout(r, ms));
const desc = el => el ? el.localName + (el.id ? '#' + el.id : '') + '.' + el.className : String(el);
(async () => {
  await sleep(60);
  d.querySelector('.nav a[href="#results"]').click(); await sleep(60);
  const tally = d.querySelector('.tally a[data-filter]');
  w.addEventListener('popstate', e => console.log('popstate state', JSON.stringify(e.state)));
  d.addEventListener('focusin', e => console.log('focusin', desc(e.target)));
  tally.click(); await sleep(80);
  console.log('after tally: url', w.location.href, 'state', JSON.stringify(w.history.state));
  w.history.back(); await sleep(200);
  console.log('after back: active', desc(d.activeElement), 'url', w.location.href);
})();
