"""The repaired page, read from its markup: G4, G1/G5, A2 and A6 as they stand in the built page."""
import re
import sys

s = open(sys.argv[1], encoding='utf-8').read()
g = re.search(r'<figure class="qh-fig" id="fig-gaussian-reduction".*?</figure>', s, re.S).group(0)
pids = ('conditional-density', 'centred-fluctuation', 'original-weight')
ticks = [re.findall(r'data-part="scale-(?:0|mid|top)"[^>]*>([^<]*)<', g.split('data-profile="%s"' % p)[1].split('</svg>')[0]) for p in pids]
print('  G4: scale note', g.count('qh-fig-scale-note">The curves share one vertical scale.</p>'), 'time(s); ticks per plot:', ticks)
TEX = '\\('
for pid in pids:
    seg = g.split('data-profile="%s"' % pid)[1].split('<div class="qh-fig-profile"')[0]
    ro = re.search(r'<p class="qh-fig-integral-value">(.*?)</p>', seg, re.S).group(1)
    print('  G1/G5 readout %s: %d parts, %d typeset formulas, no TeX left: %s, number %s'
          % (pid, ro.count('qh-fig-seg'), ro.count('<math'), TEX not in ro, re.findall(r'<output[^>]*>([^<]*)<', ro)))
print('  G5: conditional mean', re.findall(r'data-value="conditional_mean">([^<]*)<', g))
a = s[re.search(r'<section\b[^>]*\sid="atlas"', s).start():]
loc = re.search(r'<div class="atlas-locator" hidden>.*?<p class="atlas-locator-caption">.*?</p></div>', a, re.S).group(0)
print('  A2: locator in the pane, hidden until a claim is selected:', len(re.findall(r'<rect class="atlas-locator-track', loc)),
      'domain bands,', len(re.findall(r'<circle data-claim-ref=', loc)), 'dots, no line on it:',
      not re.search(r'<(path|line|polyline|marker)\b', loc))
print("  A6: the pane's column on a wide screen:",
      '.atlas-js.has-pane { display: grid; grid-template-columns: minmax(0, 1.618fr) minmax(0, 1fr);' in s,
      '| head with Close sticky at every width:', '.atlas-js .atlas-pane-head { position: sticky; top: 0;' in s,
      '| no overlay at wide widths:', 'right: clamp(12px, 2vw, 32px)' not in s)
