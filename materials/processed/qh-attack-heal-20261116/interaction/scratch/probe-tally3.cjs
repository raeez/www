const { JSDOM, VirtualConsole } = require('jsdom');
const fs = require('fs');
let html = fs.readFileSync(process.argv[2], 'utf8');
const inject = (a, b) => { if (!html.includes(a)) console.log('MISSING', a.slice(0, 60)); html = html.replace(a, b); };
inject('function leave(from) {', 'function leave(from) { console.log("LEAVE", from && (from.className || from.localName));');
inject("      if (!input) { setFilters([a.getAttribute('data-filter')]); return; }", "      console.log('TALLY HANDLER', !!input); if (!input) { setFilters([a.getAttribute('data-filter')]); return; }");
inject("    var a = event.target.closest && event.target.closest('a[href^=\"#\"]');", "    var a = event.target.closest && event.target.closest('a[href^=\"#\"]'); console.log('CAPTURE', a && a.getAttribute('href'), event.eventPhase);");
const vc = new VirtualConsole(); vc.on('jsdomError', e => console.log('JSDOMERR', e.message)); vc.on('log', (...a) => console.log('PAGE', ...a));
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, url: 'https://raeez.com/quantum-holography-tracker.html', virtualConsole: vc,
  beforeParse(w) { w.Element.prototype.scrollIntoView = function () {}; } });
const w = dom.window, d = w.document;
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  await sleep(60);
  const tally = d.querySelector('.tally a[data-filter]');
  console.log('tally href', tally.getAttribute('href'), 'outer', tally.outerHTML.slice(0, 120));
  tally.click(); await sleep(150);
  console.log('url', w.location.href, 'state', JSON.stringify(w.history.state));
})();
