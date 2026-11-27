// Minimal Chrome DevTools Protocol client over --remote-debugging-pipe (no ports, no network).
import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
export const CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
export function launch(profileDir, extra = []) {
  const args = ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
    `--user-data-dir=${profileDir}`, '--remote-debugging-pipe', '--disable-background-networking',
    '--disable-component-update', '--disable-sync', '--disable-default-apps', '--disable-extensions', '--no-pings',
    '--disable-domain-reliability', '--disable-client-side-phishing-detection', '--host-resolver-rules=MAP * ~NOTFOUND',
    ...extra, 'about:blank'];
  const proc = spawn(CH, args, { stdio: ['ignore', 'ignore', 'ignore', 'pipe', 'pipe'] });
  const out = proc.stdio[3], inp = proc.stdio[4];
  let seq = 0; const pending = new Map(); const listeners = []; let chunks = [];
  inp.on('data', (d) => {
    let start = 0;
    for (let i = 0; i < d.length; i++) {
      if (d[i] !== 0) continue;
      chunks.push(d.subarray(start, i)); start = i + 1;
      const msg = JSON.parse(Buffer.concat(chunks).toString('utf8')); chunks = [];
      if (msg.id && pending.has(msg.id)) { const p = pending.get(msg.id); pending.delete(msg.id); msg.error ? p.rej(new Error(msg.error.message)) : p.res(msg.result); }
      else for (const f of listeners) f(msg);
    }
    if (start < d.length) chunks.push(Buffer.from(d.subarray(start)));
  });
  const send = (method, params = {}, sessionId) => {
    const id = ++seq; const m = { id, method, params }; if (sessionId) m.sessionId = sessionId;
    out.write(JSON.stringify(m) + '\0');
    return new Promise((res, rej) => { pending.set(id, { res, rej });
      setTimeout(() => { if (pending.has(id)) { pending.delete(id); rej(new Error('cdp timeout ' + method)); } }, method === 'Page.printToPDF' ? 240000 : 30000).unref(); });
  };
  const close = async () => { try { await send('Browser.close'); } catch (e) {} setTimeout(() => { try { proc.kill('SIGKILL'); } catch (e) {} }, 1500).unref(); };
  return { proc, send, on: (f) => listeners.push(f), close };
}
export async function page(b) {
  const { targetId } = await b.send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await b.send('Target.attachToTarget', { targetId, flatten: true });
  const s = (m, p) => b.send(m, p, sessionId);
  const log = []; const waiters = [];
  b.on((msg) => {
    if (msg.sessionId !== sessionId) return;
    const p = msg.params || {};
    if (msg.method === 'Runtime.exceptionThrown') log.push({ kind: 'exception', text: (p.exceptionDetails.exception && p.exceptionDetails.exception.description) || p.exceptionDetails.text });
    if (msg.method === 'Runtime.consoleAPICalled' && /error|warn|assert/.test(p.type)) log.push({ kind: 'console.' + p.type, text: p.args.map((a) => a.value ?? a.description).join(' ') });
    if (msg.method === 'Log.entryAdded') log.push({ kind: 'log.' + p.entry.level, source: p.entry.source, text: p.entry.text });
    for (let i = waiters.length - 1; i >= 0; i--) if (waiters[i].m === msg.method) { waiters[i].r(p); waiters.splice(i, 1); }
  });
  const waitFor = (m, ms = 60000) => new Promise((r, j) => { waiters.push({ m, r }); setTimeout(() => j(new Error('timeout ' + m)), ms).unref(); });
  await s('Page.enable'); await s('Runtime.enable'); await s('Log.enable');
  const ev = async (fnSrc, ...args) => {
    const expression = `(${fnSrc})(${args.map((a) => JSON.stringify(a)).join(',')})`;
    const r = await s('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
    if (r.exceptionDetails) throw new Error('eval: ' + ((r.exceptionDetails.exception && r.exceptionDetails.exception.description) || r.exceptionDetails.text));
    return r.result.value;
  };
  const settle = () => ev(`() => (document.fonts ? document.fonts.ready : Promise.resolve()).then(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => setTimeout(r, 250)))))`);
  const go = async (url) => { const w = waitFor('Page.loadEventFired', 120000); await s('Page.navigate', { url }); await w; await settle(); };
  const size = (width, height, mobile = false) => s('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile });
  const media = (m, features) => s('Emulation.setEmulatedMedia', { media: m || '', features });
  const KEYS = { Tab: [9, 'Tab'], Enter: [13, 'Enter', '\r'], Escape: [27, 'Escape'], ArrowRight: [39, 'ArrowRight'], ArrowLeft: [37, 'ArrowLeft'],
    ArrowDown: [40, 'ArrowDown'], ArrowUp: [38, 'ArrowUp'], Home: [36, 'Home'], End: [35, 'End'], ' ': [32, 'Space', ' '], '/': [191, 'Slash', '/'] };
  const key = async (k, shift = false) => {
    const [code, name, text] = KEYS[k]; const modifiers = shift ? 8 : 0;
    await s('Input.dispatchKeyEvent', { type: text ? 'keyDown' : 'rawKeyDown', key: k, code: name, windowsVirtualKeyCode: code, nativeVirtualKeyCode: code, modifiers, text, unmodifiedText: text });
    await s('Input.dispatchKeyEvent', { type: 'keyUp', key: k, code: name, windowsVirtualKeyCode: code, nativeVirtualKeyCode: code, modifiers });
  };
  const shot = async (path) => { const r = await s('Page.captureScreenshot', { format: 'png' }); writeFileSync(path, Buffer.from(r.data, 'base64')); return path; };
  const pdf = async (path, opts) => { const r = await s('Page.printToPDF', Object.assign({ printBackground: false, displayHeaderFooter: false, preferCSSPageSize: true }, opts)); writeFileSync(path, Buffer.from(r.data, 'base64')); return path; };
  return { s, ev, go, size, media, key, shot, pdf, log, settle, waitFor };
}
