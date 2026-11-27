const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const vc = new VirtualConsole(); vc.on('jsdomError', e => console.log('JSDOMERR', e.message));
const t0 = Date.now();
const log = (...a) => console.log(String(Date.now() - t0).padStart(5), ...a);
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html', virtualConsole: vc,
  beforeParse(w) {
    w.Element.prototype.scrollIntoView = function () {};
    const H = w.History.prototype;
    const ps = H.pushState, rs = H.replaceState;
    H.pushState = function (s, t, u) { log('pushState', JSON.stringify(s), u); return ps.call(this, s, t, u); };
    H.replaceState = function (s, t, u) { log('replaceState', JSON.stringify(s).slice(0, 120), u); return rs.call(this, s, t, u); };
    w.addEventListener('popstate', e => log('popstate', JSON.stringify(e.state), w.location.hash));
    w.addEventListener('hashchange', () => log('hashchange', w.location.hash));
  } });
const w = dom.window, d = w.document;
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  await sleep(60);
  log('--- nav click');
  d.querySelector('.nav a[href="#results"]').click(); await sleep(60);
  log('--- tally click');
  d.querySelector('.tally a[data-filter]').click(); await sleep(80);
  log('--- back; length', w.history.length);
  w.history.back(); await sleep(200);
  log('active', d.activeElement.localName, d.activeElement.className);
})();
