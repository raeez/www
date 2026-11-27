# Third wave D-01: the overview grid at >=1280px (status.css:890-899): columns 1fr | min(measure + 2*gutter, 100%) | 1fr;
# contents in column 3, width 100% up to 22rem, padding-left clamp(8px, 1.5vw, 24px), padding-right 0; links padding-right 4px.
import base64, io, re, sys
from fontTools.ttLib import TTFont
html = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'@font-face\{font-family:"QH Garamond";font-weight:400;font-style:normal;[^}]*?base64,([A-Za-z0-9+/=]+)\)', html)
f = TTFont(io.BytesIO(base64.b64decode(m.group(1)))); cmap = f.getBestCmap(); hm = f['hmtx']; upm = f['head'].unitsPerEm
def w(t, size): return sum(hm[cmap[ord(c)]][0] for c in t if ord(c) in cmap) / upm * size * 0.995
c = html[html.find('<nav class="contents"'):html.find('</nav>', html.find('<nav class="contents"'))]
titles = [re.sub(r'<[^>]+>', '', x) for x in re.findall(r'<span class="contents-title">(.*?)</span>', c, re.S)]
holds = [re.sub(r'<span class="visually-hidden">.*?</span>', '', x) for x in re.findall(r'<span class="contents-holds">(.*?)</span></a>', c, re.S)]
holds = [re.sub(r'<[^>]+>', ' ', x) for x in holds]
def base(vw): return min(max(17.0, 15.36 + 0.003 * vw), 20.0)
def gutter(vw): return min(max(16.0, 0.04 * vw), 40.0)
print('titles:', titles)
for vw in (1280, 1366, 1400, 1424, 1440, 1600, 1920):
    for sb in (0, 15):
        lw = vw - sb
        mid = min(640 + 2 * gutter(lw), lw); side = (lw - mid) / 2
        cw = min(side, 22 * 16); padl = min(max(8.0, 0.015 * vw), 24.0)
        text = cw - padl - 4
        slack = side - cw
        sm = base(vw) * 0.88
        longest = max(w(t, sm) for t in titles)
        wraps = sum(1 for t in titles if w(t, sm) > text)
        print(f'{vw}px (scrollbar {sb:2}px): side column {side:6.1f}  contents box {cw:6.1f}  text width {text:6.1f}  right margin to the window edge {slack + 4:5.1f}px  titles wrapping {wraps}/{len(titles)} (longest {longest:.0f}px)')
