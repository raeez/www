import json, re, sys, html, fitz
S, HTML = sys.argv[1], sys.argv[2]
s = open(HTML, encoding='utf-8').read(); body = s[s.find('<body'):s.rfind('<script>')]
def runs(fragment):
    frag = re.sub(r'<math\b.*?</math>', '\x01', fragment, flags=re.S)
    frag = re.sub(r'<svg\b.*?</svg>', ' ', frag, flags=re.S)
    txt = html.unescape(re.sub(r'<[^>]+>', '', frag))
    parts = [re.sub(r'\s+', ' ', p).strip() for p in txt.split('\x01')]
    return max(parts, key=len) if parts else ''
sq = lambda t: re.sub(r'[^a-z0-9]', '', t.lower())
units = []
def grab(kind, pattern):
    for m in re.finditer(pattern, body, re.S):
        r = runs(m.group(1))
        if len(sq(r)) >= 8: units.append((kind, r))
grab('question title', r'<header class="question-head">.*?<h3><a class="anchor" href="#[^"]+">(.*?)</a></h3>')
grab('why', r'<div class="question-why prose"><p class="question-why-label">[^<]*</p>(.*?)</div>')
grab('row name', r'<span class="row-name">(.*?)</span><span class="row-marks"')
grab('row summary', r'<p class="row-summary">(.*?)</p><ul class="cell-lines"')
grab('cell line', r'<span class="cell-text">(.*?)</span></span></li>')
grab('failure claim', r'<span class="claim-text">(.*?)</span></p>')
grab('open group', r'<div class="open-group" id="[^"]+"><h3><a class="anchor" href="#[^"]+">(.*?)</a></h3>')
grab('group intro', r'<div class="prose group-intro">(.*?)</div>')
grab('glossary term', r'<div class="gloss" id="[^"]+"><dt>(.*?)</dt>')
grab('glossary def', r'<div class="gloss" id="[^"]+"><dt>.*?</dt><dd>(.*?)</dd></div>')
for m in re.finditer(r'<p(?: class="essay-display")?>(.*?)</p>', body[body.find('<article class="essay prose"'):body.find('</article>', body.find('<article class="essay prose"'))], re.S):
    r = runs(m.group(1));  units.append(('essay para', r)) if len(sq(r)) >= 8 else None
grab('col def', r'<div class="col-def" id="[^"]+"><dt>.*?</dt><dd>(.*?)</dd></div>')
grab('key explanation', r'<div class="key-item"><dt>.*?</dt><dd>(.*?)</dd></div>')
grab('lead', r'<div class="lead prose">(.*?)</div>')
res = {}
for name in sys.argv[3:]:
    doc = fitz.open(S + '/' + name)
    full = sq(' '.join(p.get_text('text') for p in doc))
    miss = {}; tot = {}
    for kind, r in units:
        tot[kind] = tot.get(kind, 0) + 1
        probe = sq(r)[:34]
        if probe not in full: miss.setdefault(kind, []).append(r[:70])
    res[name] = {'units': tot, 'missing_counts': {k: len(v) for k, v in miss.items()}, 'missing': miss}
pass
print(json.dumps({k: {'units_total': sum(v['units'].values()), 'missing_counts': v['missing_counts'], 'missing': v['missing']} for k, v in res.items()}, indent=1, ensure_ascii=False)[:5000])
