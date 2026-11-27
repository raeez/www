const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
const PAGE = fs.readFileSync(process.argv[2], 'utf8');
const vc = new VirtualConsole(); vc.on('jsdomError', e => console.log('JSDOMERR', String(e.message).slice(0, 200)));
vc.on('error', (...a) => console.log('ERR', ...a));
const dom = new JSDOM(PAGE, { url: 'https://raeez.com/q.html', runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc,
  beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
const w = dom.window, d = w.document;
const log = [];
w.addEventListener('hashchange', () => log.push('hashchange ' + w.location.hash));
d.addEventListener('qh:state', e => log.push('qh:state ' + JSON.stringify(e.detail.hash)));
setTimeout(async () => {
  const a = d.querySelector('#atlas-r-beta-hub th .atlas-link');
  a.focus(); a.click();
  await new Promise(r => setTimeout(r, 120));
  const sel = Array.from(d.querySelectorAll('.atlas-claim.is-selected')).map(x => x.id);
  console.log({ hash: w.location.hash, sel, active: d.activeElement && (d.activeElement.className + '#' + d.activeElement.id), log });
  a.click();
  await new Promise(r => setTimeout(r, 120));
  console.log('second click', { hash: w.location.hash, sel: Array.from(d.querySelectorAll('.atlas-claim.is-selected')).map(x => x.id), active: d.activeElement && d.activeElement.className, log });
}, 100);
