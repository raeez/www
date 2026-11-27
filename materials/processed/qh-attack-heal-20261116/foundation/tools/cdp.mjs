// Minimal Chrome DevTools Protocol driver for local verification of the status page.
// No packages: Node's global WebSocket and child_process only. Writes only under the
// lane output directory (profile in tmp/, screenshots and PDFs where the scenario says).
//
//   node tools/run.mjs <scenario.mjs> [args...]
//
// A scenario module exports `default async function (b, args)` where `b` is the browser
// helper returned by launch(). Every page records console errors and exceptions.
import { spawn } from 'node:child_process';
import { mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const LANE = resolve(HERE, '..');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

export async function launch(tag = 'cdp') {
  const profile = resolve(LANE, 'tmp', `chrome-${tag}-${process.pid}`);
  mkdirSync(profile, { recursive: true });
  const proc = spawn(CHROME, [
    '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
    '--hide-scrollbars', '--mute-audio', '--disable-extensions', '--disable-background-networking',
    `--user-data-dir=${profile}`, '--remote-debugging-port=0', 'about:blank',
  ], { stdio: ['ignore', 'ignore', 'pipe'] });
  const wsUrl = await new Promise((ok, fail) => {
    let buf = '';
    const t = setTimeout(() => fail(new Error('Chrome did not report a DevTools endpoint')), 20000);
    proc.stderr.on('data', (d) => {
      buf += d;
      const m = buf.match(/DevTools listening on (ws:\/\/\S+)/);
      if (m) { clearTimeout(t); ok(m[1]); }
    });
    proc.on('exit', (c) => fail(new Error('Chrome exited ' + c)));
  });
  const ws = new WebSocket(wsUrl);
  await new Promise((ok, fail) => { ws.onopen = ok; ws.onerror = fail; });
  let nextId = 1;
  const pending = new Map();
  const listeners = new Set();
  ws.onmessage = (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending.has(msg.id)) {
      const { ok, fail } = pending.get(msg.id);
      pending.delete(msg.id);
      if (msg.error) fail(new Error(JSON.stringify(msg.error))); else ok(msg.result);
    } else if (msg.method) {
      for (const l of listeners) l(msg);
    }
  };
  function send(method, params = {}, sessionId) {
    const id = nextId++;
    ws.send(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }));
    return new Promise((ok, fail) => pending.set(id, { ok, fail }));
  }

  async function page(opts = {}) {
    const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
    const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
    const s = (m, p) => send(m, p, sessionId);
    const log = [];
    const waiters = [];
    const on = (msg) => {
      if (msg.sessionId !== sessionId) return;
      if (msg.method === 'Runtime.exceptionThrown') {
        const d = msg.params.exceptionDetails;
        log.push({ kind: 'exception', text: (d.exception && d.exception.description) || d.text });
      } else if (msg.method === 'Runtime.consoleAPICalled' && ['error', 'warning', 'assert'].includes(msg.params.type)) {
        log.push({ kind: 'console.' + msg.params.type, text: msg.params.args.map((a) => a.value ?? a.description).join(' ') });
      } else if (msg.method === 'Log.entryAdded' && ['error', 'warning'].includes(msg.params.entry.level)) {
        log.push({ kind: 'log.' + msg.params.entry.level, text: msg.params.entry.text, url: msg.params.entry.url });
      }
      for (const w of waiters.slice()) if (w.method === msg.method) { waiters.splice(waiters.indexOf(w), 1); w.ok(msg.params); }
    };
    listeners.add(on);
    const waitFor = (method, ms = 30000) => new Promise((ok, fail) => {
      const w = { method, ok };
      waiters.push(w);
      setTimeout(() => { const i = waiters.indexOf(w); if (i >= 0) { waiters.splice(i, 1); fail(new Error('timeout ' + method)); } }, ms);
    });
    await s('Page.enable');
    await s('Runtime.enable');
    await s('Log.enable');
    const api = {
      log, s,
      async setView({ width = 1400, height = 900, mobile = false, scheme = 'light', reduced = 'no-preference', media = '', touch = false } = {}) {
        await s('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile });
        await s('Emulation.setEmulatedMedia', { media, features: [
          { name: 'prefers-color-scheme', value: scheme },
          { name: 'prefers-reduced-motion', value: reduced },
        ] });
        await s('Emulation.setTouchEmulationEnabled', touch ? { enabled: true, maxTouchPoints: 5 } : { enabled: false });
      },
      async goto(url, settle = 350) {
        const loaded = waitFor('Page.loadEventFired');
        await s('Page.navigate', { url });
        await loaded;
        await new Promise((r) => setTimeout(r, settle));
      },
      async eval(expr) {
        const r = await s('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true, userGesture: true });
        if (r.exceptionDetails) throw new Error('eval: ' + ((r.exceptionDetails.exception && r.exceptionDetails.exception.description) || r.exceptionDetails.text));
        return r.result.value;
      },
      async key(key, { shift = false, code, text } = {}) {
        const map = { Tab: [9, 'Tab'], Enter: [13, 'Enter'], Escape: [27, 'Escape'], ArrowDown: [40, 'ArrowDown'], ArrowUp: [38, 'ArrowUp'],
          ArrowLeft: [37, 'ArrowLeft'], ArrowRight: [39, 'ArrowRight'], Home: [36, 'Home'], End: [35, 'End'], ' ': [32, 'Space'], '/': [191, 'Slash'] };
        const [vk, c] = map[key] || [0, code || key];
        const mods = shift ? 8 : 0;
        const t = text ?? (key === 'Enter' ? '\r' : key.length === 1 ? key : undefined);
        await s('Input.dispatchKeyEvent', { type: t ? 'keyDown' : 'rawKeyDown', key, code: c, windowsVirtualKeyCode: vk, modifiers: mods, ...(t ? { text: t } : {}) });
        await s('Input.dispatchKeyEvent', { type: 'keyUp', key, code: c, windowsVirtualKeyCode: vk, modifiers: mods });
        await new Promise((r) => setTimeout(r, 40));
      },
      async screenshot(path, { full = false } = {}) {
        let params = { format: 'png' };
        if (full) {
          const m = await s('Page.getLayoutMetrics');
          const h = Math.min(Math.ceil(m.cssContentSize.height), 16000);
          params = { format: 'png', captureBeyondViewport: true, clip: { x: 0, y: 0, width: m.cssLayoutViewport.clientWidth, height: h, scale: 1 } };
        }
        const { data } = await s('Page.captureScreenshot', params);
        mkdirSync(dirname(path), { recursive: true });
        writeFileSync(path, Buffer.from(data, 'base64'));
        return path;
      },
      async pdf(path, { paper = 'A4', css = true } = {}) {
        const sizes = { A4: [8.27, 11.69], Letter: [8.5, 11] };
        const [w, h] = sizes[paper];
        const { data } = await s('Page.printToPDF', { paperWidth: w, paperHeight: h, preferCSSPageSize: css, printBackground: false,
          displayHeaderFooter: false, marginTop: 0, marginBottom: 0, marginLeft: 0, marginRight: 0, generateDocumentOutline: true });
        mkdirSync(dirname(path), { recursive: true });
        writeFileSync(path, Buffer.from(data, 'base64'));
        return path;
      },
      async close() { listeners.delete(on); await send('Target.closeTarget', { targetId }); },
    };
    await api.setView(opts);
    return api;
  }

  async function close() {
    try { await send('Browser.close'); } catch (e) { /* already closing */ }
    await new Promise((r) => { proc.once('exit', r); setTimeout(r, 3000); });
    try { proc.kill('SIGKILL'); } catch (e) { /* gone */ }
    try { rmSync(profile, { recursive: true, force: true }); } catch (e) { /* keep */ }
  }
  return { page, close, send };
}

export const fileUrl = (p) => pathToFileURL(resolve(p)).href;
