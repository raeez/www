import sys, json, time, base64
sys.path.insert(0, sys.argv[1])
from cdp import Chrome
S = sys.argv[1]; P = sys.argv[2]
URL = 'file://' + P
out = {}
NAVVIS = r'''(() => { const nav = document.querySelector('.nav'); const nr = nav.getBoundingClientRect();
  return [...nav.querySelectorAll('a')].map(a => { const r = a.getBoundingClientRect(); const v = (r.left >= nr.left - 1 && r.right <= nr.right + 1) ? 'visible' : ((r.right > nr.left && r.left < nr.right) ? 'partly' : 'hidden'); return a.textContent + ':' + v + (a.getAttribute('aria-current') ? '*' : ''); }); })()'''
c = Chrome(S + '/chrome')
try:
    c.open_page()
    # 1. 1400: grid header stickiness and lower rows
    c.viewport(1400, 900); c.media('light', 'reduce')
    c.goto(URL, 2.0)
    c.js("(() => { const g = document.querySelector('.grid-wrap'); scrollTo(0, g.getBoundingClientRect().top + scrollY + 420); })()"); time.sleep(0.4)
    out['grid1400_scrolled'] = c.js("(() => { const th = document.querySelector('.grid thead th'); const r = th.getBoundingClientRect(); const lastRow = document.querySelector('.grid tbody tr:last-child').getBoundingClientRect(); return {theadTop: Math.round(r.top), theadBottom: Math.round(r.bottom), barBottom: 51, lastRowTop: Math.round(lastRow.top), lastRowBottom: Math.round(lastRow.bottom), theadVisible: r.bottom > 51 && r.top < innerHeight}; })()")
    c.shot(f'{S}/g1400-lower-rows.png')
    # keyboard: index link 12 -> Enter -> Tab
    c.js("document.querySelectorAll('#decisive .q-index li a')[11].focus()"); time.sleep(0.2)
    c.key('Enter', 'Enter', 13, text='\r'); time.sleep(0.6)
    out['kbd_after_enter'] = c.js("({hash: location.hash, active: document.activeElement.className || document.activeElement.localName, y: Math.round(scrollY)})")
    c.tab(); time.sleep(0.2)
    out['kbd_after_tab'] = c.js("(() => { const a = document.activeElement; const q = a.closest('.question'); return {tag: a.localName, cls: a.className, href: a.getAttribute('href'), inQuestion: q ? q.id : null, text: a.textContent.trim().slice(0,60)}; })()")
    # 2. 1024: grid cut-off
    c.viewport(1024, 768); c.media('light', 'reduce')
    c.goto('about:blank', 0.2); c.goto(URL + '#examples', 2.0)
    c.js("document.querySelector('.grid-wrap').scrollIntoView({block:'start'}); scrollBy(0, -70)"); time.sleep(0.4)
    out['grid1024'] = c.js("(() => { const g = document.querySelector('.grid-wrap'); const ths = [...document.querySelectorAll('.grid thead th')]; return {clientW: g.clientWidth, scrollW: g.scrollWidth, wrapRight: Math.round(g.getBoundingClientRect().right), heads: ths.map(t => [t.textContent, Math.round(t.getBoundingClientRect().left), Math.round(t.getBoundingClientRect().right)])}; })()")
    c.shot(f'{S}/g1024-grid.png')
    # 3. 375: nav visibility by section
    c.viewport(375, 812, mobile=True)
    c.send('Emulation.setTouchEmulationEnabled', {'enabled': True, 'maxTouchPoints': 5})
    c.media('light', 'reduce')
    c.goto('about:blank', 0.2); c.goto(URL, 2.0)
    out['nav375'] = {'top': c.js(NAVVIS)}
    for sec in ['decisive', 'frontier', 'examples', 'failures', 'open']:
        c.js(f"document.getElementById('{sec}').scrollIntoView({{block:'start'}}); scrollBy(0, 400)"); time.sleep(0.9)
        out['nav375'][sec] = c.js(NAVVIS)
    c.shot(f'{S}/n375-in-open.png', clip={'x': 0, 'y': 0, 'width': 375, 'height': 60})
    # 4. 375 dark: grid
    c.media('dark', 'reduce')
    c.goto('about:blank', 0.2); c.goto(URL + '#examples', 2.0)
    c.js("document.querySelector('.grid-wrap').scrollIntoView({block:'start'}); scrollBy(0, -70)"); time.sleep(0.4)
    c.shot(f'{S}/g375-dark.png')
    # 5. A4 print page count
    c.viewport(1400, 900); c.media('light', 'reduce')
    c.goto('about:blank', 0.2); c.goto(URL, 2.0)
    pdf = c.send('Page.printToPDF', {'paperWidth': 8.27, 'paperHeight': 11.69, 'printBackground': False, 'preferCSSPageSize': True}, timeout=240)
    data = base64.b64decode(pdf['data'])
    open(f'{S}/print-a4.pdf', 'wb').write(data)
    out['pdf_a4_bytes'] = len(data)
    out['console'] = c.console_errors()
    json.dump(out, open(S + '/m3.json', 'w'), indent=1)
finally:
    c.close()
print('ok')
