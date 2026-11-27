# Third wave: table-layout fixed (status.css:676-683, 750-766). Family column share 21% (>1100), 20% (<=1100),
# 23% (<=900), 38% (<=760); mark columns share the rest equally. Checks per width and text zoom z (fonts x z,
# px sizes unchanged): mark fits its column; longest unbroken heading word and family-name word versus the cell
# (else overflow-wrap:anywhere / hyphens break it: no overflow, but a broken word); upright heading line width
# (<=760px) versus the column; heading-row height (sticky) versus the focused-mark clearance from scroll-margin-top.
import base64, io, re, sys
from fontTools.ttLib import TTFont
html = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'@font-face\{font-family:"QH Garamond";font-weight:400;font-style:normal;[^}]*?base64,([A-Za-z0-9+/=]+)\)', html)
f = TTFont(io.BytesIO(base64.b64decode(m.group(1)))); cmap = f.getBestCmap(); hm = f['hmtx']; upm = f['head'].unitsPerEm
def w(t, size, ls=0.0): return (sum(hm[cmap[ord(c)]][0] for c in t if ord(c) in cmap) / upm * size + ls * size * len(t)) * 0.995
heads = re.findall(r'<span class="col-head-text">([^<]*)</span>', html)
names = [re.sub(r'<[^>]+>', '', x) for x in re.findall(r'<a class="row-link"[^>]*>(.*?)</a>', html, re.S)]
def base(vw): return min(max(17.0, 15.36 + 0.003 * vw), 20.0)
def gutter(vw): return min(max(16.0, 0.04 * vw), 40.0)
def share(vw): return 0.38 if vw <= 760 else 0.23 if vw <= 900 else 0.20 if vw <= 1100 else 0.21
def lines(text, size, avail):
    n, cur = 1, 0.0
    for wd in text.split():
        ww = w(wd, size, 0.02); sp = w(' ', size)
        if ww > avail:                       # broken inside the word (overflow-wrap: anywhere / hyphens)
            extra = int(ww // avail); n += extra if cur == 0 else extra + 1; cur = ww - extra * avail; continue
        if cur and cur + sp + ww > avail: n += 1; cur = ww
        else: cur = cur + (sp if cur else 0) + ww
    return n
for z in (1.0, 2.0):
    print(f'--- text zoom {z:.0f}x')
    for vw in (1400, 1024, 900, 768, 761, 760, 480, 375, 320):
        b = base(vw) * z; xs, sm = b * 0.78, b * 0.88
        tfs = xs if vw <= 760 else sm
        box = min(vw - 2 * gutter(vw), 1216) - 2
        fam = box * share(vw); col = (box - fam) / 8
        mark = 15 if vw <= 760 else 17
        if vw > 760:
            avail = col - 8
            broken = [wd for h in heads for wd in h.split() if w(wd, xs, 0.02) > avail]
            n = max(lines(h, xs, avail) for h in heads); hh = 20 + n * 1.2 * xs
            headnote = f'heading lines {n}, words broken {len(broken)}'
            margin_em = 4.5 * sm      # scroll-margin-top 4.5em at the cell font (--text-sm)
        else:
            upright = 1.15 * xs
            hh = max(w(h, xs, 0.02) for h in heads) + 18
            headnote = f'upright line {upright:.1f}px vs column {col:.1f}px' + (' OVERLAPS' if upright > col else '')
            margin_em = 9.5 * xs
        fam_avail = fam - (16 if vw <= 760 else 24)
        nbroken = sum(1 for nme in names for wd in nme.split() if w(wd, tfs) > fam_avail)
        clear = 66 + margin_em - (50 + hh)
        print(f'{vw:5}px: box {box:6.1f} family {fam:5.1f} col {col:5.1f} mark {mark}px {"ok" if mark <= col else "OVERFLOWS"} | {headnote} | family words broken {nbroken} | heading row {hh:5.1f}px, focused-mark clearance {clear:+5.1f}px')
