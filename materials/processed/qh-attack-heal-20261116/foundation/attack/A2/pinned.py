# Static check of the pinned first bar link (status.css:126-131, <=900px) against status.js keepInSight()
# (js:388-395): after keepInSight centres the current link, how much of it lies under the pinned first link?
import base64, io, re, sys
from fontTools.ttLib import TTFont
html = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'@font-face\{font-family:"QH Garamond";font-weight:400;font-style:normal;[^}]*?base64,([A-Za-z0-9+/=]+)\)', html)
f = TTFont(io.BytesIO(base64.b64decode(m.group(1)))); cmap = f.getBestCmap(); hm = f['hmtx']; upm = f['head'].unitsPerEm
def w(t, size): return sum(hm[cmap[ord(c)]][0] for c in t if ord(c) in cmap) / upm * size
nav = html[html.find('<nav class="nav"'):html.find('</nav>', html.find('<nav class="nav"'))]
labels = [re.sub(r'<[^>]+>', '', x) for x in re.findall(r'<a href="#[^"]+">(.*?)</a>', nav)]
def base(vw): return min(max(17.0, 15.36 + 0.003 * vw), 20.0)
def gutter(vw): return min(max(16.0, 0.04 * vw), 40.0)
for vw in (375, 480, 768):
    sm = base(vw) * 0.88
    home = 0 if vw <= 560 else w('Raeez Lorgat', sm) * 1.02 * 0.995
    inner = vw - 2 * gutter(vw)
    gaps = 18 * (2 if vw <= 560 else 3)
    navw = inner - home - 24 - 34 - gaps
    widths = [w(t, sm) * 0.995 + 20 for t in labels]
    pin = widths[0] + 8   # pinned li plus its 8px shadow
    lefts, x = [], 0.0
    for wd in widths: lefts.append(x); x += wd + 2
    row = x - 2 + 24
    out = []
    for i, (t, wd) in enumerate(zip(labels, widths)):
        if i == 0: continue
        sl = max(0.0, min(lefts[i] - (navw - wd) / 2, row - navw))   # keepInSight centring, clamped to the scroll range
        rel = lefts[i] - sl                                             # link's left edge relative to the nav box
        hidden = max(0.0, min(pin, rel + wd) - rel) if rel < pin else 0.0
        out.append(f'{t} {hidden:.0f}/{wd:.0f}px')
    print(f'{vw}px: nav {navw:.0f}px, row {row:.0f}px, pinned first link {widths[0]:.0f}px (+8 shadow); covered after centring: ' + ', '.join(out))
