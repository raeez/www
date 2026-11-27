# Static estimate of the sticky table heading's height (screen) at the required widths, from the embedded
# font's advances and the candidate CSS (status.css:219-221, 366-378): headings at --text-xs, line-height 1.2,
# padding 10px/10px (wrap, >760px) or upright at <=760px (writing-mode, nowrap, line-height 1.15, padding 10/8).
import base64, io, re, sys
from fontTools.ttLib import TTFont
html = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'@font-face\{font-family:"QH Garamond";font-weight:400;font-style:normal;[^}]*?base64,([A-Za-z0-9+/=]+)\)', html)
f = TTFont(io.BytesIO(base64.b64decode(m.group(1)))); cmap = f.getBestCmap(); hm = f['hmtx']; upm = f['head'].unitsPerEm
def w(t, size, ls=0.02): return sum(hm[cmap[ord(c)]][0] for c in t if ord(c) in cmap) / upm * size + ls * size * len(t)
heads = re.findall(r'<span class="col-head-text">([^<]*)</span>', html)
print('headings:', heads)
def base(vw): return min(max(17.0, 15.36 + 0.003 * vw), 20.0)
def gutter(vw): return min(max(16.0, 0.04 * vw), 40.0)
def lines(text, size, avail):
    words, n, cur = text.split(), 1, 0.0
    for wd in words:
        ww = w(wd, size); sp = w(' ', size)
        if cur and cur + sp + ww > avail: n += 1; cur = ww
        else: cur = cur + (sp if cur else 0) + ww
    return n
for vw in (1400, 1024, 768, 480, 375):
    xs, sm = base(vw) * 0.78, base(vw) * 0.88
    table = min(vw - 2 * gutter(vw), 1216) - 2
    if vw > 760:
        th = min(max(w('Heisenberg, free fields', sm), (11.5 if vw > 1100 else 9) * sm), (15 if vw > 1100 else 12) * sm)
        col = (table - th) / 8 - 8
        n = max(lines(h, xs, col) for h in heads); hh = 20 + n * 1.2 * xs
        mode = f'wrapped, {n} line(s) in {col:.0f}px'
    else:
        hh = max(w(h, xs) for h in heads) + 18; mode = 'upright'
    print(f'{vw}px: heading row ~{hh:5.1f}px ({mode}); sticky band {50}..{50 + hh:.0f}px; scroll-padding-top 66px -> band hidden under it: {max(0, 50 + hh - 66):.0f}px; table row 38px')
