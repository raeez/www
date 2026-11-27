# Third wave: the bar against status.css:108-146 and :746. >1180px: home + nav(9) + find-open + theme;
# 1041-1180px: nav(9) + find-open + theme; <=1040px: nav-top + nav(8, first link not drawn) + find-open + theme,
# end fade on. ul padding 0 24px 0 4px; links 10px side padding, 2px gaps; bar gap 18px; find-open 34px - 10px.
import base64, io, re, sys
from fontTools.ttLib import TTFont
html = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'@font-face\{font-family:"QH Garamond";font-weight:400;font-style:normal;[^}]*?base64,([A-Za-z0-9+/=]+)\)', html)
f = TTFont(io.BytesIO(base64.b64decode(m.group(1)))); cmap = f.getBestCmap(); hm = f['hmtx']; upm = f['head'].unitsPerEm
def w(t, size, ls=0.0): return (sum(hm[cmap[ord(c)]][0] for c in t if ord(c) in cmap) / upm * size + ls * size * len(t)) * 0.995
nav = html[html.find('<nav class="nav"'):html.find('</nav>', html.find('<nav class="nav"'))]
labels = [re.sub(r'<[^>]+>', '', x) for x in re.findall(r'<a href="#[^"]+">(.*?)</a>', nav)]
top = re.search(r'<a class="nav-top" href="#programme">([^<]*)</a>', html).group(1)
def base(vw): return min(max(17.0, 15.36 + 0.003 * vw), 20.0)
def gutter(vw): return min(max(16.0, 0.04 * vw), 40.0)
print('links:', labels, '| nav-top:', top)
for vw in (1400, 1280, 1181, 1180, 1100, 1041, 1040, 1024, 900, 768, 480, 375):
    sm = base(vw) * 0.88
    inner = min(1216, vw) - 2 * gutter(vw)
    links = labels if vw > 1040 else labels[1:]
    row = sum(w(t, sm) + 20 for t in links) + 2 * (len(links) - 1) + 24 + 4
    items = []
    if vw > 1180: items.append(('home', w('Raeez Lorgat', sm, 0.02)))
    if vw <= 1040: items.append(('nav-top', w(top, sm) + 20))
    fixed = sum(x for _, x in items) + (34 - 10) + 34
    gaps = 18 * (len(items) + 2)          # items + nav + find-open + theme -> n-1 gaps
    navw = inner - fixed - gaps
    hidden = max(0.0, row - 24 - navw)
    cue = 'end fade' if vw <= 1040 else 'no cue (mask off)'
    print(f'{vw:5}px: inner {inner:6.1f}  nav {navw:6.1f}  row {row:6.1f}  links beyond the box {hidden:6.1f}px  [{cue}]' + ('  OVERFLOW WITHOUT CUE' if hidden > 0 and vw > 1040 else ''))
