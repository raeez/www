#!/usr/bin/env python3
"""Full-scale atlas mount test on the frozen 11:20 layout snapshot (read-only, opaque data). Run from the repository root:

    /tmp/qh-tracker-build-20261116-venv/bin/python -B materials/processed/qh-attack-heal-20261116/foundation/tests/atlas-real/real_mount_test.py

Builds the page with the lane's test-only stub renderer (titles and domain summaries through the page's renderer)
against the snapshot, checks placement, scale and the audit, and scans every reader-visible string of the snapshot
(titles, statements, hypotheses, labels, summaries, overviews, notes, descriptions, edge labels and scopes) with the
page audit's FORBIDDEN patterns, so that root and the atlas lane see which atlas text would fail the page audit when
rendered. Writes the built page to tests/atlas-real/out/. The snapshot is never modified."""
import hashlib
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path.cwd()
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'compiler' / 'quantum-holography-status'))
import audit  # noqa: E402
import status  # noqa: E402

HERE = Path(__file__).resolve().parent
SNAP = Path('/tmp/programme-public-content-0835-20261116/layout-snapshot-1120/atlas.json')
assert hashlib.sha256(SNAP.read_bytes()).hexdigest() == '1b6ffa8ee2e0603b9440eb4c2f153e6b5d72f597038c95cbc67cdd41e80c519e'
page = json.loads((ROOT / 'content' / 'quantum-holography-status' / 'page.json').read_text(encoding='utf-8'))
t = time.time()
b = status.Build(HERE / 'input', page, {}, None, atlas_module=HERE.parent / 'atlas' / 'stub_atlas.py')
m = b.run()
a = audit.run(b, m)
dt = time.time() - t
(HERE / 'out' / 'atlas-real-stub.html').write_text(m, encoding='utf-8')
main = m[m.find('<main'):m.find('</main>')]
order = re.findall(r'<(?:section|header|aside) id="([^"]+)"', main)
print(f'build {dt:.1f}s, {len(m):,} bytes, math jobs {len(b.math.jobs)}, TeX errors {len(b.math.errors)}')
print('placement overview -> atlas -> results:', [x for x in order if x not in ('programme', 'changes')][:2] == ['atlas', 'results'])
print('nav and contents entries:', 'href="#atlas"' in m[:m.find('<main')], m.count('href="#atlas"'))
print('audit failures:', len(a['failures']))
for f in a['failures'][:12]:
    print('  ', f[:200])

# Every reader-visible string of the snapshot against the page audit's rules.
A = json.loads(SNAP.read_text(encoding='utf-8'))
fields = []
for d in A['domains']:
    fields += [('domain', d['id'], 'label', d.get('label', '')), ('domain', d['id'], 'summary', d.get('summary', ''))]
for c in A['claims']:
    fields += [('claim', c['id'], 'title', c.get('title', '')), ('claim', c['id'], 'statement', c.get('statement', '')),
               ('claim', c['id'], 'status.label', (c.get('status') or {}).get('label', '')), ('claim', c['id'], 'sourceLabel', c.get('sourceLabel', ''))]
    fields += [('claim', c['id'], 'hypothesis', h) for h in c.get('hypotheses') or []]
for e in A['edges']:
    fields += [('edge', e['id'], 'label', e.get('label', '')), ('edge', e['id'], 'scope', e.get('scope', ''))]
for k in A['comparisons']:
    fields += [('comparison', k['id'], 'title', k.get('title', '')), ('comparison', k['id'], 'overview', k.get('overview', ''))]
for p in A['readingPaths']:
    fields += [('path', p['id'], f, p.get(f, '')) for f in ('title', 'summary', 'note')]
    for s in p.get('stages', []):
        fields += [('path', p['id'], 'stage.label', s.get('label', '')), ('path', p['id'], 'stage.description', s.get('description', ''))]
MATH = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]', re.S)
hits = []
for kind, ident, field, text in fields:
    plain = MATH.sub(' ', text or '')
    for pattern, why, flags in audit.FORBIDDEN:
        for mm in re.finditer(pattern, plain, flags=flags):
            hits.append((why, kind, ident, field, mm.group(0), plain[max(0, mm.start() - 40):mm.end() + 40]))
print(f'reader-visible strings scanned: {len(fields)}; FORBIDDEN hits: {len(hits)}')
from collections import Counter
print('by rule:', dict(Counter(h[0] for h in hits)))
out = HERE / 'out' / 'forbidden-hits.json'
out.write_text(json.dumps([dict(zip(('rule', 'kind', 'id', 'field', 'match', 'context'), h)) for h in hits], ensure_ascii=False, indent=1), encoding='utf-8')
for h in hits[:15]:
    print('  ', h[0], '|', h[1], h[2][:40], h[3], '|', repr(h[4]), '|', h[5][:110])
