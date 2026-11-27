"""Minimal Chrome DevTools Protocol client over --remote-debugging-pipe (no TCP).
Writes only inside the scratch directory given by the caller."""
import json, os, subprocess, time, base64, select

CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

class Chrome:
    def __init__(self, profile, extra=()):
        r1, w1 = os.pipe()
        r2, w2 = os.pipe()
        # move to high fds so dup2 into 3/4 cannot clobber
        a = os.dup2(r1, 60); b = os.dup2(w2, 61)
        os.close(r1); os.close(w2)
        def pre():
            os.dup2(60, 3); os.dup2(61, 4)
        args = [CH, '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
                '--user-data-dir=' + profile, '--hide-scrollbars', '--remote-debugging-pipe',
                '--disable-extensions', '--disable-background-networking', '--disable-sync',
                '--disable-component-update', '--disable-default-apps', '--mute-audio',
                '--force-device-scale-factor=1'] + list(extra) + ['about:blank']
        self.proc = subprocess.Popen(args, pass_fds=(3, 4, 60, 61), preexec_fn=pre,
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.close(60); os.close(61)
        self.w = w1; self.r = r2
        self.buf = b''
        self.next_id = 0
        self.events = []
        self.session = None

    def _read_msg(self, timeout):
        end = time.time() + timeout
        while b'\0' not in self.buf:
            left = end - time.time()
            if left <= 0:
                return None
            rl, _, _ = select.select([self.r], [], [], left)
            if not rl:
                return None
            chunk = os.read(self.r, 1 << 20)
            if not chunk:
                raise RuntimeError('chrome closed pipe')
            self.buf += chunk
        msg, self.buf = self.buf.split(b'\0', 1)
        return json.loads(msg)

    def send(self, method, params=None, session=True, timeout=60):
        self.next_id += 1
        mid = self.next_id
        m = {'id': mid, 'method': method, 'params': params or {}}
        if session and self.session:
            m['sessionId'] = self.session
        os.write(self.w, json.dumps(m).encode() + b'\0')
        end = time.time() + timeout
        while True:
            msg = self._read_msg(max(0.01, end - time.time()))
            if msg is None:
                raise TimeoutError(method)
            if msg.get('id') == mid:
                if 'error' in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get('result', {})
            self.events.append(msg)

    def wait_event(self, name, timeout=30):
        end = time.time() + timeout
        for i, e in enumerate(self.events):
            if e.get('method') == name:
                self.events.pop(i)
                return e
        while time.time() < end:
            msg = self._read_msg(max(0.01, end - time.time()))
            if msg is None:
                break
            if msg.get('method') == name:
                return msg
            self.events.append(msg)
        raise TimeoutError(name)

    def open_page(self):
        t = self.send('Target.createTarget', {'url': 'about:blank'}, session=False)
        s = self.send('Target.attachToTarget', {'targetId': t['targetId'], 'flatten': True}, session=False)
        self.session = s['sessionId']
        self.target = t['targetId']
        self.send('Page.enable'); self.send('Runtime.enable'); self.send('Log.enable')

    def viewport(self, w, h, mobile=False):
        self.send('Emulation.setDeviceMetricsOverride', {'width': w, 'height': h, 'deviceScaleFactor': 1, 'mobile': mobile})

    def media(self, scheme='light', motion='no-preference', mtype=''):
        self.send('Emulation.setEmulatedMedia', {'media': mtype, 'features': [
            {'name': 'prefers-color-scheme', 'value': scheme},
            {'name': 'prefers-reduced-motion', 'value': motion}]})

    def goto(self, url, settle=1.5):
        self.events = [e for e in self.events if e.get('method') != 'Page.loadEventFired']
        self.send('Page.navigate', {'url': url})
        self.wait_event('Page.loadEventFired', 60)
        time.sleep(settle)

    def js(self, expr, await_promise=False):
        r = self.send('Runtime.evaluate', {'expression': expr, 'returnByValue': True, 'awaitPromise': await_promise})
        if 'exceptionDetails' in r:
            raise RuntimeError('JS: ' + json.dumps(r['exceptionDetails'])[:800])
        return r['result'].get('value')

    def shot(self, path, full=False, clip=None):
        p = {'format': 'png'}
        if full:
            p['captureBeyondViewport'] = True
        if clip:
            p['clip'] = dict(clip, scale=1)
        r = self.send('Page.captureScreenshot', p)
        with open(path, 'wb') as f:
            f.write(base64.b64decode(r['data']))

    def key(self, key, code=None, keycode=0, shift=False, text=None):
        mods = 8 if shift else 0
        base = {'key': key, 'code': code or key, 'windowsVirtualKeyCode': keycode, 'modifiers': mods}
        down = dict(base, type='keyDown' if text is None else 'keyDown')
        if text is not None:
            down['text'] = text
        self.send('Input.dispatchKeyEvent', down)
        self.send('Input.dispatchKeyEvent', dict(base, type='keyUp'))

    def tab(self, shift=False):
        self.key('Tab', 'Tab', 9, shift=shift)

    def click(self, x, y):
        for t in ('mouseMoved', 'mousePressed', 'mouseReleased'):
            p = {'type': t, 'x': x, 'y': y, 'button': 'left', 'clickCount': 1}
            if t == 'mouseMoved':
                p = {'type': t, 'x': x, 'y': y}
            self.send('Input.dispatchMouseEvent', p)

    def console_errors(self):
        out = []
        for e in self.events:
            m = e.get('method')
            if m == 'Runtime.exceptionThrown':
                out.append(('exception', e['params']['exceptionDetails'].get('text'), json.dumps(e['params']['exceptionDetails'])[:300]))
            elif m == 'Runtime.consoleAPICalled' and e['params'].get('type') in ('error', 'warning', 'assert'):
                out.append(('console', e['params'].get('type'), json.dumps(e['params'].get('args'))[:300]))
            elif m == 'Log.entryAdded' and e['params']['entry'].get('level') in ('error', 'warning'):
                out.append(('log', e['params']['entry'].get('level'), e['params']['entry'].get('text')[:300]))
        return out

    def close(self):
        try:
            self.send('Browser.close', session=False, timeout=5)
        except Exception:
            pass
        try:
            self.proc.wait(10)
        except Exception:
            self.proc.kill()
