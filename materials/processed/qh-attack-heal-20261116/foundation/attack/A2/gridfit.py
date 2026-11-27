# Static estimate of the table's minimum width against its box (screen), candidate CSS status.css:215-236, 366-380:
# columns >= longest heading word at --text-xs (+8px padding) or the upright heading's line (<=760px), and
# >= .cell-btn min-width (44px above 1100px, 0 at <=1100px, 26px at <=359px); row heading >= min-width
# (11.5em above 1100px, 9em at <=1100px, 0 at <=760px) and its longest word (+24px / +16px padding).
import base64, io, re, sys
from fontTools.ttLib import TTFont
html = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'@font-face\{font-family:"QH Garamond";font-weight:400;font-style:normal;[^}]*?base64,([A-Za-z0-9+/=]+)\)', html)
f = TTFont(io.BytesIO(base64.b64decode(m.group(1)))); cmap = f.getBestCmap(); hm = f['hmtx']; upm = f['head'].unitsPerEm
def w(t, size, ls=0.0): return sum(hm[cmap[ord(c)]][0] for c in t if ord(c) in cmap) / upm * size + ls * size * len(t)
heads = re.findall(r'<span class="col-head-text">([^<]*)</span>', html)
names = [re.sub(r'<[^>]+>', '', x) for x in re.findall(r'<a class="row-link"[^>]*>(.*?)</a>', html, re.S)]
def base(vw): return min(max(17.0, 15.36 + 0.003 * vw), 20.0)
def gutter(vw): return min(max(16.0, 0.04 * vw), 40.0)
for vw in (1400, 1101, 1100, 900, 800, 761, 760, 641, 480, 375, 360, 359, 320):
    b = base(vw); xs, sm = b * 0.78, b * 0.88
    tfs = xs if vw <= 760 else sm          # .grid font-size: --text-xs at <=760px, else --text-sm
    box = min(vw - 2 * gutter(vw), 1216) - 2
    if vw > 760:
        cols = [max(max(w(wd, xs, 0.02) for wd in h.split()) + 8, 44 if vw > 1100 else 0, 17) for h in heads]
        col = sum(cols) / 8
        thmin = (11.5 if vw > 1100 else 9) * tfs
    else:
        col = max(1.15 * xs, 26 if vw <= 359 else 0, 15)
        thmin = 0
    thword = max(w(wd, tfs) for n in names for wd in n.split()) + (24 if vw > 760 else 16)
    need = max(thmin, thword) + 1 + 8 * col
    print(f'{vw:5}px: box {box:6.1f}  table min {need:6.1f}  {"fits" if need <= box else "CLIPPED by " + format(need - box, ".1f") + "px" if vw > 359 else "scrolls (" + format(need - box, ".1f") + "px)"}  (column min {col:.1f}, row-heading min {max(thmin, thword):.1f})')
