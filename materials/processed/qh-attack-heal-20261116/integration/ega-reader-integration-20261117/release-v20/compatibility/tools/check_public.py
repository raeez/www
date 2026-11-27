"""The public files of a release: what each holds that must not be published, and whether every local link resolves.

    python3 -I check_public.py <site folder> <out.json>

For index.html, reference.html, atlas.html and reader-index.js: sha256 and bytes; every hit of a private-path,
account, custody or model/tool-attribution pattern, with its context; and, across the three pages, every local href and
src: '#id' in the same page, 'page.html#id' in that page, a bare file name present in the folder. External addresses are
counted separately. The reader's page map (script#reader-pages) is checked too: each id it lists exists in its page.
Reads the folder; writes only <out.json>."""
import hashlib
import html
import json
import os
import re
import sys

site, out = sys.argv[1:3]
PAGES = ['index.html', 'reference.html', 'atlas.html']
FILES = PAGES + ['reader-index.js']
PATTERNS = [r'/Users/', r'/private/', r'/tmp/', r'\bfile://', r'127\.0\.0\.1', r'\blocalhost\b', r'raeez@', r'@mass\.build',
            r'\.claude\b', r'\bcentcom\b', r'Co-Authored-By', r'Generated with', r'\bclaude-[a-z]', r'\bClaude\b', r'\bOpus\b',
            r'\bSonnet\b', r'\bFable\b', r'\bAstra\b', r'\bGPT-?\d', r'\bCodex\b', r'\banthropic\b', r'\bopenai\b', r'\bworktree',
            r'materials/processed', r'qh-attack-heal', r'\bTODO\b', r'\bFIXME\b']
RX = re.compile('|'.join(PATTERNS), re.I)
res = {'files': {}, 'links': {}}
text = {}
for f in FILES:
    p = os.path.join(site, f)
    raw = open(p, 'rb').read()
    t = raw.decode('utf-8')
    text[f] = t
    hits = []
    for m in RX.finditer(t):
        hits.append({'match': m.group(0), 'at': m.start(), 'context': t[max(0, m.start() - 60):m.end() + 60].replace('\n', ' ')})
    res['files'][f] = {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw), 'private_or_attribution_hits': hits}
ids = {f: set(re.findall(r'\sid="([^"]+)"', text[f])) for f in PAGES}
bad, checked, external = [], 0, 0
for f in PAGES:
    body = re.sub(r'<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>', ' ', text[f], flags=re.S)
    for m in re.finditer(r'\s(href|src)="([^"]*)"', body):
        u = html.unescape(m.group(2))
        if re.match(r'(https?:|mailto:|data:)', u):
            external += u.startswith(('http:', 'https:', 'mailto:'))
            continue
        checked += 1
        page, _, frag = u.partition('#')
        target = page or f
        if target not in os.listdir(site):
            bad.append({'page': f, 'link': u, 'why': 'no such file'})
            continue
        if frag and target in ids and frag not in ids[target]:
            bad.append({'page': f, 'link': u, 'why': 'no such id in ' + target})
    mp = re.search(r'<script type="application/json" id="reader-pages">(.*?)</script>', text[f], re.S)
    if mp:
        pm = json.loads(mp.group(1).replace('<\\/', '</'))
        for pg in pm.get('pages', []):
            missing = [i for i in pg.get('ids', []) if i not in ids.get(pg['href'], set())]
            if missing:
                bad.append({'page': f, 'link': 'reader-pages map: ' + pg['href'], 'why': f'{len(missing)} ids missing, e.g. {missing[:3]}'})
            checked += len(pg.get('ids', []))
res['links'] = {'local_links_checked': checked, 'bad_local_links': bad, 'external_addresses': external}
json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for f, d in res['files'].items():
    print(f'{f:16s} {d["sha256"]} {d["bytes"]:>9d} bytes  hits: {len(d["private_or_attribution_hits"])}')
    for h in d['private_or_attribution_hits'][:6]:
        print('     ', repr(h['match']), '…' + h['context'][:140] + '…')
print(f'local links and map ids checked {checked}; bad {len(bad)}; external addresses {external}')
for b in bad[:10]:
    print('  BAD', b)
