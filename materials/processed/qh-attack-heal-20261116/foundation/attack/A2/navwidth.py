# Static estimate of the bar's link row against the nav box, from the embedded font's advance widths.
# Calibrated against widths measured on the baseline before the browser restriction (A2 run1/run2).
import base64, io, json, re, sys
from fontTools.ttLib import TTFont
def face(html):
    for m in re.finditer(r'@font-face\{font-family:"QH Garamond";font-weight:400;font-style:normal;[^}]*?base64,([A-Za-z0-9+/=]+)\)', html):
        return TTFont(io.BytesIO(base64.b64decode(m.group(1))))
def width(font, text, size, spacing_em=0.0):
    cmap = font.getBestCmap(); hmtx = font['hmtx']; upm = font['head'].unitsPerEm
    adv = sum(hmtx[cmap[ord(ch)]][0] for ch in text if ord(ch) in cmap)
    return adv / upm * size + spacing_em * size * len(text)
def links(html):
    nav = html[html.find('<nav class="nav"'):html.find('</nav>', html.find('<nav class="nav"'))]
    return [re.sub(r'<[^>]+>', '', x) for x in re.findall(r'<a href="#[^"]+">(.*?)</a>', nav)]
def base_px(vw): return min(max(17.0, 0.96 * 16 + 0.003 * vw), 20.0)
def gutter(vw): return min(max(16.0, 0.04 * vw), 40.0)
base = open(sys.argv[1], encoding='utf-8').read(); cand = open(sys.argv[2], encoding='utf-8').read()
fb, fc = face(base), face(cand)
lb, lc = links(base), links(cand)
print('baseline links:', lb); print('candidate links:', lc)
# calibration: baseline link widths measured at 1400 (A2 run1) = text + 20px padding
meas1400 = {'Programme': 97, 'Results': 69, 'Decisive questions': 141, 'Frontier': 74, 'Examples': 82, 'Counterexamples': 136, 'Open': 58, 'Essay': 55, 'Terms': 61}
sm1400 = base_px(1400) * 0.88
est = {t: width(fb, t, sm1400) + 20 for t in meas1400}
print('calibration at 1400 (measured vs estimated):', {t: (meas1400[t], round(est[t], 1)) for t in meas1400})
ratio = sum(meas1400.values()) / sum(est.values()); print('measured/estimated total ratio %.3f' % ratio)
for vw in (1100, 1060, 1024, 1000, 960, 920, 901):
    sm = base_px(vw) * 0.88
    def row(font, labels): return sum(width(font, t, sm) * ratio + 20 for t in labels) + 2 * (len(labels) - 1) + 24
    home = width(fb, 'Raeez Lorgat', sm, 0.02) * ratio
    inner = min(1216, vw) - 2 * gutter(vw)
    nav_b = inner - home - 34 - 2 * 18
    nav_c = inner - home - (34 - 10) - 34 - 3 * 18
    ub, uc = row(fb, lb), row(fc, lc)
    print(f'{vw}px: baseline nav {nav_b:6.1f} ul {ub:6.1f} links hidden {max(0, ub - 24 - nav_b):5.1f} | candidate nav {nav_c:6.1f} ul {uc:6.1f} links hidden {max(0, uc - 24 - nav_c):5.1f}  (mask {"off" if vw >= 900 else "on"}, pinned first link {"no" if vw > 900 else "yes"})')
