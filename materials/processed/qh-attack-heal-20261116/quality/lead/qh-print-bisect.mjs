// Print-loss bisection: prints the page to PDF (given paper) with optional extra CSS and reports whether
// every decisive and frontier question heading and every statement title survives in the PDF text.
// Usage: node qh-print-bisect.mjs --html <preview.html> --out <dir> [--paper Letter|A4] [--variants <json file>]
// Writes only under <dir>. Uses pdftotext from poppler.
import { spawn, execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const args = {};
for (let i = 2; i < process.argv.length; i += 2) args[process.argv[i].replace(/^--/, '')] = process.argv[i + 1];
const HTML = path.resolve(args.html), OUT = path.resolve(args.out);
const PAPERS = { Letter: [8.5, 11], A4: [8.27, 11.69] };
const papers = (args.paper || 'Letter,A4').split(',');
for (const p of papers) if (!PAPERS[p] && /^[\d.]+x[\d.]+$/.test(p)) PAPERS[p] = p.split('x').map(Number);
const variants = args.variants ? JSON.parse(fs.readFileSync(args.variants, 'utf8')) : { none: '' };
fs.mkdirSync(OUT, { recursive: true });
const PROFILE = path.join(OUT, '.chrome-profile');
const sleep = ms => new Promise(r => setTimeout(r, ms));
fs.rmSync(PROFILE, { recursive: true, force: true });
const proc = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', ['--headless=new', '--disable-gpu', '--no-first-run',
  '--no-default-browser-check', '--disable-extensions', '--remote-debugging-port=0', `--user-data-dir=${PROFILE}`, 'about:blank'], { stdio: 'ignore' });
let port, wsPath;
for (let i = 0; i < 100 && !port; i++) { await sleep(100); try { [port, wsPath] = fs.readFileSync(path.join(PROFILE, 'DevToolsActivePort'), 'utf8').trim().split('\n'); } catch { } }
const ws = new WebSocket(`ws://127.0.0.1:${port}${wsPath}`);
await new Promise(r => { ws.onopen = r; });
let id = 0; const pending = new Map(); let loads = 0;
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { const p = pending.get(m.id); pending.delete(m.id); m.error ? p.rej(new Error(JSON.stringify(m.error))) : p.res(m.result); } else if (m.method === 'Page.loadEventFired') loads++; };
const send = (method, params = {}, sessionId) => { const i = ++id; ws.send(JSON.stringify({ id: i, method, params, sessionId })); return new Promise((res, rej) => pending.set(i, { res, rej })); };

// Expected text: every question card title (as the page renders it) and every statement title.
async function expectedTexts(sid) {
  const r = await send('Runtime.evaluate', { returnByValue: true, expression: `(function () {
    function t(el) { var c = el.cloneNode(true); c.querySelectorAll('math, svg').forEach(function (n) { n.replaceWith('\u0000'); });
      var segs = c.textContent.split('\u0000').map(function (x) { return x.replace(/\\s+/g, ''); }); segs.sort(function (a, b) { return b.length - a.length; }); return segs[0] || ''; }
    var out = [];
    document.querySelectorAll('main .question').forEach(function (q) { out.push({ kind: 'question', id: q.id, text: t(q.querySelector('h3')).slice(0, 30) }); });
    document.querySelectorAll('main .statement').forEach(function (s, i) { var h = s.querySelector('.statement-title'); var p = s.querySelector('.statement-text');
      out.push({ kind: 'statement', id: s.id || ('#' + i), text: (h ? t(h) : t(p)).slice(0, 30) }); });
    [['gloss', '.gloss dt'], ['gloss-def', '.gloss dd'], ['key', '.key-item dd'], ['coldef', '.col-def dd'], ['cell-line', '.cell-line .cell-body'],
     ['claim', '.claim-text'], ['open-group', '.open-group h3'], ['why', '.question-why'], ['essay', '.essay > p'], ['row-summary', '.row-summary'],
     ['lead', '.lead p']].forEach(function (pair) {
      document.querySelectorAll('main ' + pair[1]).forEach(function (el, i) { out.push({ kind: pair[0], id: (el.closest('[id]') || {}).id + ':' + i, text: t(el).slice(0, 40) }); });
    });
    return out.filter(function (x) { return x.text.replace(/[^A-Za-z]/g, '').length >= 14; });
  })()` }, sid);
  return r.result.value;
}
const report = {};
for (const [name, css] of Object.entries(variants)) {
  for (const paper of papers) {
    const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
    const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
    await send('Page.enable', {}, sessionId);
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: 'light' }] }, sessionId);
    const before = loads;
    await send('Page.navigate', { url: 'file://' + HTML }, sessionId);
    for (let i = 0; i < 200 && loads === before; i++) await sleep(50);
    await sleep(600);
    if (css) await send('Runtime.evaluate', { expression: `(function(){var s=document.createElement('style');s.textContent=${JSON.stringify(css)};document.head.appendChild(s);return true})()` }, sessionId);
    const expected = await expectedTexts(sessionId);
    const [w, h] = PAPERS[paper];
    const pdf = await send('Page.printToPDF', { paperWidth: w, paperHeight: h, printBackground: false, preferCSSPageSize: false }, sessionId);
    const file = path.join(OUT, `bisect-${name}-${paper}.pdf`);
    fs.writeFileSync(file, Buffer.from(pdf.data, 'base64'));
    const txt = execFileSync('pdftotext', ['-enc', 'UTF-8', file, '-'], { maxBuffer: 64 << 20 }).toString('utf8');
    // Compare ASCII letters only: formula glyphs (mathematical alphanumerics) that the extractor interleaves with
    // nearby words, hyphenation marks, dashes and spaces drop out; ligatures are expanded first.
    const letters = x => x.replace(/ﬀ/g, 'ff').replace(/ﬁ/g, 'fi').replace(/ﬂ/g, 'fl').replace(/ﬃ/g, 'ffi')
      .replace(/ﬄ/g, 'ffl').replace(/[ﬅﬆ]/g, 'st').replace(/[^A-Za-z]/g, '').toLowerCase();
    const flat = letters(txt);
    const missing = expected.filter(x => !flat.includes(letters(x.text).slice(0, 22)));
    const pages = (txt.match(/\f/g) || []).length;
    report[`${name}/${paper}`] = { pages, expected: expected.length, missing: missing.length, missingSample: missing.slice(0, 12) };
    console.log(name, paper, 'pages', pages, 'expected', expected.length, 'missing', missing.length, JSON.stringify(missing.slice(0, 6)));
    await send('Target.closeTarget', { targetId });
  }
}
fs.writeFileSync(path.join(OUT, 'bisect-report.json'), JSON.stringify(report, null, 1) + '\n');
try { await send('Browser.close'); } catch { }
await sleep(300); try { proc.kill('SIGKILL'); } catch { }
fs.rmSync(PROFILE, { recursive: true, force: true });
