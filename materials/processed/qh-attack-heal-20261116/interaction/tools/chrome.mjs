// Minimal Chrome DevTools Protocol client for task-owned local pages (no packages; Node with global WebSocket).
// Usage: import { launch } from './chrome.mjs'; const b = await launch(profileDir); const t = await b.page(); ...; await b.close();
import { spawn } from 'node:child_process';
import { readFileSync, existsSync, mkdirSync, rmSync } from 'node:fs';
import { join } from 'node:path';

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const sleep = ms => new Promise(r => setTimeout(r, ms));

export async function launch(profile) {
  if (existsSync(profile)) rmSync(profile, { recursive: true, force: true });
  mkdirSync(profile, { recursive: true });
  const proc = spawn(CHROME, ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`, '--no-first-run',
    '--no-default-browser-check', '--disable-extensions', '--disable-background-networking', '--disable-sync',
    '--allow-file-access-from-files', '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });
  let port = null, path = null;
  for (let i = 0; i < 100 && !port; i++) {
    await sleep(100);
    const f = join(profile, 'DevToolsActivePort');
    if (existsSync(f)) { const [p, ws] = readFileSync(f, 'utf8').trim().split('\n'); if (ws) { port = p; path = ws; } }
  }
  if (!port) { proc.kill(); throw new Error('Chrome did not start'); }
  const ws = new WebSocket(`ws://127.0.0.1:${port}${path}`);
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  let id = 0;
  const pending = new Map();
  const listeners = [];
  ws.onmessage = m => {
    const msg = JSON.parse(m.data);
    if (msg.id && pending.has(msg.id)) {
      const { res, rej } = pending.get(msg.id); pending.delete(msg.id);
      msg.error ? rej(new Error(JSON.stringify(msg.error))) : res(msg.result);
    } else if (msg.method) listeners.forEach(l => l(msg));
  };
  const send = (method, params = {}, sessionId) => new Promise((res, rej) => {
    const n = ++id; pending.set(n, { res, rej });
    ws.send(JSON.stringify(sessionId ? { id: n, method, params, sessionId } : { id: n, method, params }));
  });
  async function page() {
    const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
    const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
    const s = (method, params) => send(method, params, sessionId);
    const problems = [];
    listeners.push(msg => {
      if (msg.sessionId !== sessionId) return;
      if (msg.method === 'Runtime.exceptionThrown') problems.push('exception: ' + (msg.params.exceptionDetails.exception?.description || msg.params.exceptionDetails.text));
      if (msg.method === 'Runtime.consoleAPICalled' && (msg.params.type === 'error' || msg.params.type === 'warning'))
        problems.push(msg.params.type + ': ' + msg.params.args.map(a => a.value ?? a.description).join(' '));
      if (msg.method === 'Log.entryAdded' && (msg.params.entry.level === 'error' || msg.params.entry.level === 'warning'))
        problems.push('log ' + msg.params.entry.level + ': ' + msg.params.entry.text);
    });
    await s('Page.enable'); await s('Runtime.enable'); await s('Log.enable');
    async function evaluate(expression) {
      const r = await s('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
      if (r.exceptionDetails) throw new Error('evaluate: ' + (r.exceptionDetails.exception?.description || r.exceptionDetails.text));
      return r.result.value;
    }
    async function goto(url, { width = 1400, height = 900, dark = false, reduced = false, mobile = false } = {}) {
      await s('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile });
      await s('Emulation.setEmulatedMedia', { media: '', features: [
        { name: 'prefers-color-scheme', value: dark ? 'dark' : 'light' },
        { name: 'prefers-reduced-motion', value: reduced ? 'reduce' : 'no-preference' }] });
      const loaded = new Promise(res => { const l = msg => { if (msg.sessionId === sessionId && msg.method === 'Page.loadEventFired') { listeners.splice(listeners.indexOf(l), 1); res(); } }; listeners.push(l); });
      await s('Page.navigate', { url });
      await loaded;
      await evaluate('document.fonts ? document.fonts.ready.then(() => true) : true');
      await sleep(150);
    }
    async function shot(file, full = false) {
      const { data } = await s('Page.captureScreenshot', { format: 'png', captureBeyondViewport: full });
      const { writeFileSync } = await import('node:fs'); writeFileSync(file, Buffer.from(data, 'base64'));
    }
    async function pdf(file, paper) {
      const sizes = { A4: [8.27, 11.69], Letter: [8.5, 11] };
      const [paperWidth, paperHeight] = sizes[paper];
      await s('Emulation.setEmulatedMedia', { media: 'print' });
      const { data } = await s('Page.printToPDF', { paperWidth, paperHeight, preferCSSPageSize: true, printBackground: false });
      await s('Emulation.setEmulatedMedia', { media: '' });
      const { writeFileSync } = await import('node:fs'); writeFileSync(file, Buffer.from(data, 'base64'));
    }
    async function key(k, code, keyCode, modifiers = 0, text) {
      await s('Input.dispatchKeyEvent', { type: 'keyDown', key: k, code, windowsVirtualKeyCode: keyCode, modifiers, text });
      await s('Input.dispatchKeyEvent', { type: 'keyUp', key: k, code, windowsVirtualKeyCode: keyCode, modifiers });
    }
    return { s, evaluate, goto, shot, pdf, key, problems };
  }
  async function close() { try { await send('Browser.close'); } catch (e) { /* closing */ } ws.close(); await sleep(200); proc.kill(); }
  return { page, close };
}
