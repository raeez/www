import sys, json, time
sys.path.insert(0, sys.argv[1])
from cdp import Chrome
S = sys.argv[1]; P = sys.argv[2]
URL = 'file://' + P
out = {}
c = Chrome(S + '/chrome')
try:
    c.open_page()
    # 1400: search "elliptic cubic" from the top
    c.viewport(1400, 900); c.media('light', 'reduce')
    c.goto(URL, 2.0)
    c.js("(() => { const i = document.getElementById('find-q'); i.focus(); i.value = 'elliptic cubic'; i.dispatchEvent(new Event('input', {bubbles: true})); })()"); time.sleep(0.8)
    out['search_elliptic_cubic'] = c.js("(() => ({count: document.querySelector('.find-count').textContent, groups: [...document.querySelectorAll('.find-group-head')].map(g => g.textContent), hits: [...document.querySelectorAll('.find-link')].slice(0, 12).map(a => [a.getAttribute('href'), (a.querySelector('.find-where')||{}).textContent, (a.querySelector('.find-title')||{}).textContent])}))()")
    # Q9 related statements head at 1400
    c.js("(() => { const q = document.getElementById('q-d-critical-quantization'); q.scrollIntoView({block: 'start'}); })()"); time.sleep(0.4)
    c.shot(f'{S}/r1400-q9-related-open.png')
    out['q9'] = c.js("(() => { const q = document.getElementById('q-d-critical-quantization'); return {knownHead: q.querySelector('.known-head').textContent.replace(/\\s+/g,' ').trim(), knownChips: [...q.querySelectorAll('.question-known .status-chip')].map(e => e.textContent.trim())}; })()")
    # key section location relative to grid and in nav
    out['key'] = c.js("(() => { const k = document.getElementById('status'); const g = document.querySelector('.grid-legend'); return {keyTop: Math.round(k.getBoundingClientRect().top + scrollY), legendTop: Math.round(g.getBoundingClientRect().top + scrollY), inNav: !!document.querySelector('.nav a[href=\"#status\"]'), legendLinks: g.querySelectorAll('a').length, chipLinks: document.querySelectorAll('.status-chip a, a .status-chip').length}; })()")
    # 375 touch: bar while reading open problems
    c.viewport(375, 812, mobile=True)
    c.send('Emulation.setTouchEmulationEnabled', {'enabled': True, 'maxTouchPoints': 5})
    c.media('light', 'reduce')
    c.goto('about:blank', 0.2); c.goto(URL, 2.0)
    c.js("document.getElementById('open').scrollIntoView({block:'start'}); scrollBy(0, 300)"); time.sleep(1.0)
    c.shot(f'{S}/n375-open-section.png')
    out['bar375_open'] = c.js("(() => { const nav = document.querySelector('.nav'); return {scrollLeft: Math.round(nav.scrollLeft), maskImage: getComputedStyle(nav).webkitMaskImage || getComputedStyle(nav).maskImage, findTop: Math.round(document.querySelector('.find').getBoundingClientRect().top + scrollY), scrollY: Math.round(scrollY), searchInBar: !!document.querySelector('.bar input, .bar [data-find-open]')}; })()")
    out['console'] = c.console_errors()
    json.dump(out, open(S + '/m4.json', 'w'), indent=1)
finally:
    c.close()
print('ok')
