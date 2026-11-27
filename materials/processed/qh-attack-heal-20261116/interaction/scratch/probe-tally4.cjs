const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const vc = new VirtualConsole(); vc.on('jsdomError', e => console.log('JSDOMERR', e.message));
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html', virtualConsole: vc,
  beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; w.addEventListener('popstate', e => console.log('popstate state', JSON.stringify(e.state), 'history.state', JSON.stringify(w.history.state))); } });
const w = dom.window, d = w.document;
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  await sleep(60);
  w.history.replaceState({ qh: { back: { id: 'x' } } }, '', w.location.href);
  console.log('A state', JSON.stringify(w.history.state));
  w.history.pushState(null, '', '?status=checked');
  console.log('B state', JSON.stringify(w.history.state));
  w.history.back(); await sleep(100);
  console.log('C state', JSON.stringify(w.history.state), w.location.href);
  /* the same through a fragment navigation */
  w.history.replaceState({ qh: { back: { id: 'y' } } }, '', w.location.href);
  w.location.hash = 'results'; await sleep(60);
  w.history.back(); await sleep(100);
  console.log('D state', JSON.stringify(w.history.state), w.location.href);
})();
