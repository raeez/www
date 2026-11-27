"""Mechanical checks of reader-safe atlas data (EVAL-PLAN Q24; CONTRACT.json atlas_testability_requirements).
Usage: python -I -B qh-atlas-fidelity.py <atlas.json or built page.html> [--html <built page>] [--content <content.json>]
       [--out result.json]
With --content, AT9 compares each page statement's status with the atlas claim of the same id under the stated mapping
(checked to checked, conditional to conditional, 'refuted form' to scoped_negative); other page statuses on shared ids
are listed for the content owner, not failed.
The atlas data follows DESIGN-CONTRACT.json's shape: domains, claims, edges, comparisons, readingPaths. Given a built
page, the data is read from <script type="application/json" id="qh-atlas-data"> and the rendered hooks
([data-claim-id], [data-edge-id], [data-path-id]) are compared with it. Reads only; writes only --out.
The checks decide data and rendering fidelity; they do not judge mathematics, wording or the page image.
"""
import html as htmlmod
import json
import re
import sys
from collections import Counter, defaultdict

src = sys.argv[1]
page = sys.argv[sys.argv.index('--html') + 1] if '--html' in sys.argv else (src if src.endswith('.html') else None)
out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
content_path = sys.argv[sys.argv.index('--content') + 1] if '--content' in sys.argv else None
markup = open(page, encoding='utf-8').read() if page else ''
if src.endswith('.html'):
    m = re.search(r'<script\b[^>]*id="qh-atlas-data"[^>]*>(.*?)</script>', markup, re.S)
    atlas = json.loads(htmlmod.unescape(m.group(1))) if m else None
else:
    atlas = json.load(open(src, encoding='utf-8'))

results = {}


def check(cid, ok, detail):
    results[cid] = {'pass': bool(ok), **detail}
    print(f"{'PASS' if ok else 'FAIL'} {cid} {json.dumps(detail, ensure_ascii=False)[:260]}")


if atlas is None:
    check('AT0-data-present', False, {'problem': 'no qh-atlas-data block and no atlas JSON'})
    sys.exit(1)

STATUS = {'checked', 'conditional', 'scoped_negative', 'remaining'}
PATH_KINDS = {'editorial_orientation', 'source_bound_dependency_path'}
LISTS = {'establishedClaimIds': 'checked', 'conditionalClaimIds': 'conditional', 'scopedNegativeClaimIds': 'scoped_negative', 'remainingClaimIds': 'remaining'}
SAFE_ID = re.compile(r'^[a-z0-9][a-z0-9_-]{0,79}$')

domains = atlas.get('domains') or []
claims = atlas.get('claims') or []
edges = atlas.get('edges') or []
comparisons = atlas.get('comparisons') or []
paths = atlas.get('readingPaths') or []
D = {d.get('id'): d for d in domains}
C = {c.get('id'): c for c in claims}
E = {e.get('id'): e for e in edges}
K = {k.get('id'): k for k in comparisons}
check('AT0-data-present', True, {'domains': len(domains), 'claims': len(claims), 'edges': len(edges), 'comparisons': len(comparisons), 'paths': len(paths)})

# AT1 ids: present, unique, reader-safe
problems = []
for kind, items in (('domain', domains), ('claim', claims), ('edge', edges), ('comparison', comparisons), ('path', paths)):
    ids = [x.get('id') for x in items]
    for i, n in Counter(ids).items():
        if n > 1:
            problems.append(f'{kind} id {i!r} used {n} times')
    for i in ids:
        if not isinstance(i, str) or not SAFE_ID.match(i):
            problems.append(f'{kind} id {i!r} is not reader-safe')
check('AT1-ids', not problems, {'problems': problems[:12], 'count': len(problems)})

# AT2 enumerations and required fields
problems = []
for c in claims:
    st = (c.get('status') or {})
    if st.get('code') not in STATUS:
        problems.append(f"claim {c.get('id')}: status code {st.get('code')!r}")
    if not (st.get('label') or '').strip():
        problems.append(f"claim {c.get('id')}: no status label")
    for f in ('domainId', 'title', 'statement'):
        if not (c.get(f) or '').strip():
            problems.append(f"claim {c.get('id')}: no {f}")
for p in paths:
    if p.get('kind') not in PATH_KINDS:
        problems.append(f"path {p.get('id')}: kind {p.get('kind')!r}")
for e in edges:
    for f in ('source', 'target', 'relation', 'label'):
        if not (e.get(f) or '').strip():
            problems.append(f"edge {e.get('id')}: no {f}")
check('AT2-fields-and-enums', not problems, {'problems': problems[:12], 'count': len(problems)})

# AT3 referential integrity
problems = []
for c in claims:
    if c.get('domainId') not in D:
        problems.append(f"claim {c.get('id')}: unknown domain {c.get('domainId')!r}")
    for k in c.get('comparisonIds') or []:
        if k not in K:
            problems.append(f"claim {c.get('id')}: unknown comparison {k!r}")
for e in edges:
    for end in ('source', 'target'):
        if e.get(end) not in C:
            problems.append(f"edge {e.get('id')}: unknown {end} {e.get(end)!r}")
    if e.get('source') == e.get('target'):
        problems.append(f"edge {e.get('id')}: loop on {e.get('source')!r}")
for k in comparisons:
    if k.get('domainId') not in D:
        problems.append(f"comparison {k.get('id')}: unknown domain {k.get('domainId')!r}")
    for lst in LISTS:
        for cid in k.get(lst) or []:
            if cid not in C:
                problems.append(f"comparison {k.get('id')}.{lst}: unknown claim {cid!r}")
for p in paths:
    for s in p.get('stages') or []:
        for cid in s.get('claimIds') or []:
            if cid not in C:
                problems.append(f"path {p.get('id')}: unknown claim {cid!r}")
check('AT3-references', not problems, {'problems': problems[:12], 'count': len(problems)})

# AT4 comparisons and claims agree both ways, and list membership matches the claim's status code
problems = []
member = defaultdict(set)
for k in comparisons:
    for lst, code in LISTS.items():
        for cid in k.get(lst) or []:
            member[cid].add(k.get('id'))
            if cid in C and (C[cid].get('status') or {}).get('code') != code:
                problems.append(f"comparison {k.get('id')}: {cid} listed as {code} but its status is {(C[cid].get('status') or {}).get('code')}")
for c in claims:
    declared = set(c.get('comparisonIds') or [])
    if declared != member[c.get('id')]:
        problems.append(f"claim {c.get('id')}: comparisonIds {sorted(declared)} but listed in {sorted(member[c.get('id')])}")
check('AT4-comparison-agreement', not problems, {'problems': problems[:12], 'count': len(problems)})

# AT5 edges: no duplicates; one label per relation (a free label cannot restate a relation differently)
problems = []
for key, n in Counter((e.get('source'), e.get('target'), e.get('relation')) for e in edges).items():
    if n > 1:
        problems.append(f'edge {key} appears {n} times')
labels = defaultdict(set)
for e in edges:
    labels[e.get('relation')].add(e.get('label'))
multi = {r: sorted(l) for r, l in labels.items() if len(l) > 1}
check('AT5-edge-uniqueness', not problems, {'problems': problems[:12], 'relations': {r: len(l) for r, l in labels.items()}})
check('AT5b-one-label-per-relation', not multi, {'relations_with_several_labels': dict(list(multi.items())[:6])})

# AT6 a dependency path is connected by data edges between consecutive stages; editorial paths say so
problems = []
adj = set((e.get('source'), e.get('target')) for e in edges)
for p in paths:
    stages = p.get('stages') or []
    if p.get('kind') == 'source_bound_dependency_path':
        for a, b in zip(stages, stages[1:]):
            if not any((x, y) in adj or (y, x) in adj for x in a.get('claimIds') or [] for y in b.get('claimIds') or []):
                problems.append(f"path {p.get('id')}: no edge between stage '{a.get('label')}' and stage '{b.get('label')}'")
check('AT6-dependency-paths-connected', not problems, {'problems': problems[:12], 'dependency_paths': sum(p.get('kind') == 'source_bound_dependency_path' for p in paths)})

# AT7 public safety of every reader value (keys that must not appear; patterns that must not appear in values)
FORBIDDEN_KEYS = re.compile(r'^(source|sources|path|file|hash|sha\d*|commit|session|account|owner|binding|manifest)$', re.I)
PATTERNS = [
    (r'\b(astra|claude|codex|opus|fable|gpt-?\d|chatgpt|openai|anthropic|sonnet|haiku)\b', 'model or tool name', re.I),
    (r'\b(llm|language model|agent|subagent|prompt|chatbot)s?\b', 'agent vocabulary', re.I),
    (r'\b(adoption|inscribe|census|ledger|dossier|worktree|commit|pull request|repository|pipeline|audit|reviewer|attacker)s?\b|\battack[- ]?heal\w*|\bswarms?\b', 'workflow vocabulary', re.I),
    (r'(?<![\w-])(Wave|Phase|Session|Lane|Sprint|Round|Cycle)[- ]?[A-Z]?\d+\b|\bwave-?\d+\b', 'process stage label', 0),
    (r'/Users/|~/[\w.-]|\b(?:engine|prep|chains|frontier|inscribe)/[\w.-]+', 'path', 0),
    (r'\.(md|json|tex|py|tsv|csv|log)\b', 'file name', 0),
    (r'(?<![\w-])[0-9a-f]{32,}(?![\w-])', 'hash', re.I),
    (r'\d+(?:\.\d+)?\s?%|\bper ?cent\b', 'percentage', re.I),
    (r'\b(v\d+|version\s+\d+|draft|frozen\d*|snapshot)\b', 'version or process word', re.I),
]
problems = []


def walk(node, where):
    if isinstance(node, dict):
        for k, v in node.items():
            # an edge's source and target are its endpoints (claim ids), not private tracing fields
            endpoint = k in ('source', 'target') and re.fullmatch(r'atlas\.edges\[\d+\]', where)
            if FORBIDDEN_KEYS.match(k) and not endpoint:
                problems.append(f'{where}.{k}: private field')
            walk(v, f'{where}.{k}')
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f'{where}[{i}]')
    elif isinstance(node, str):
        text = re.sub(r'\\\(.+?\\\)|\\\[.+?\\\]', ' ', node, flags=re.S)
        for pat, why, flags in PATTERNS:
            m = re.search(pat, text, flags)
            if m:
                problems.append(f'{where}: {why} "{m.group(0)}"')


walk(atlas, 'atlas')
check('AT7-public-safety', not problems, {'problems': problems[:12], 'count': len(problems)})

# AT8 rendering fidelity (only with a built page): drawn claims, edges and paths equal the data; a text equivalent exists
if markup:
    def attrs(tag_attr):
        return re.findall(r'<[^>]*\b' + tag_attr + r'="([^"]*)"[^>]*>', markup)
    drawn_edges = re.findall(r'<([a-z]+)\b[^>]*\bdata-edge-id="([^"]*)"[^>]*>', markup)
    problems = []
    for tag, eid in drawn_edges:
        if eid not in E:
            problems.append(f'drawn edge {eid!r} is not in the data')
    for m in re.finditer(r'<[^>]*\bdata-edge-id="([^"]*)"[^>]*>', markup):
        el = m.group(0)
        e = E.get(m.group(1))
        if not e:
            continue
        for attr, key in (('data-source', 'source'), ('data-target', 'target'), ('data-relation', 'relation')):
            v = re.search(attr + r'="([^"]*)"', el)
            if not v or v.group(1) != e.get(key):
                problems.append(f'edge {m.group(1)}: {attr} {v.group(1) if v else None!r} != {e.get(key)!r}')
    claim_hooks = re.findall(r'<[^>]*\bdata-claim-id="([^"]*)"[^>]*>', markup)
    for cid in set(claim_hooks):
        if cid not in C:
            problems.append(f'drawn claim {cid!r} is not in the data')
    for m in re.finditer(r'<[^>]*\bdata-claim-id="([^"]*)"[^>]*\bdata-status-code="([^"]*)"', markup):
        if m.group(1) in C and (C[m.group(1)].get('status') or {}).get('code') != m.group(2):
            problems.append(f'claim {m.group(1)}: drawn status {m.group(2)} != data')
    for m in re.finditer(r'<[^>]*\bdata-path-id="([^"]*)"[^>]*\bdata-path-kind="([^"]*)"', markup):
        p = {x.get('id'): x for x in paths}.get(m.group(1))
        if not p:
            problems.append(f'drawn path {m.group(1)!r} is not in the data')
        elif p.get('kind') != m.group(2):
            problems.append(f'path {m.group(1)}: drawn kind {m.group(2)} != {p.get("kind")}')
    outside_svg = re.sub(r'<svg\b.*?</svg>', ' ', markup, flags=re.S)
    text_edges = set(re.findall(r'<[^>]*\bdata-edge-id="([^"]*)"', outside_svg))
    missing_text = [eid for eid in E if eid not in text_edges]
    check('AT8-rendering-fidelity', not problems, {'problems': problems[:12], 'count': len(problems), 'drawn_edges': len(drawn_edges), 'claims_drawn': len(set(claim_hooks))})
    check('AT8b-text-equivalent', not missing_text, {'edges_without_text_equivalent': missing_text[:12], 'count': len(missing_text)})
    editorial = [p for p in paths if p.get('kind') == 'editorial_orientation']
    marked = re.findall(r'data-path-kind="editorial_orientation"', markup)
    check('AT8c-editorial-paths-marked', len(marked) >= len(editorial), {'editorial_paths': len(editorial), 'marked_in_page': len(marked)})

if content_path:
    page_content = json.load(open(content_path, encoding='utf-8'))

    def page_statements(c):
        yield from c.get('principal', [])
        for key in ('decisive', 'frontier'):
            for q in (c.get(key) or {}).get('questions', []):
                if q.get('question'):
                    yield q['question']
                yield from q.get('known', [])
        for r in c.get('rows', []):
            yield from r.get('statements', [])
        for f in (c.get('failures') or {}).get('items', []):
            if f.get('witness'):
                yield f['witness']
        for g in c.get('open', []):
            yield from g.get('statements', [])

    MAPPING = {'checked': 'checked', 'conditional': 'conditional', 'refuted form': 'scoped_negative'}
    by_id = {cl.get('id'): cl for cl in (atlas or {}).get('claims', []) if cl.get('id')}
    mismatches, outside, shared = [], [], 0
    for s in page_statements(page_content):
        sid = (s.get('id') or '').strip()
        if sid and sid in by_id:
            shared += 1
            code = (by_id[sid].get('status') or {}).get('code')
            want = MAPPING.get(s.get('status'))
            row = {'id': sid, 'page': s.get('status'), 'atlas': code}
            if want is None:
                outside.append(row)
            elif code != want:
                mismatches.append(row)
    check('AT9-page-atlas-status', not mismatches,
          {'shared_ids': shared, 'mismatches': mismatches[:12], 'count': len(mismatches), 'outside_mapping': outside[:12],
           'outside_count': len(outside)})

ok = all(r['pass'] for r in results.values())
print('ALL PASS' if ok else 'NOT ALL PASS')
if out:
    json.dump({'source': src, 'page': page, 'results': results, 'all_pass': ok}, open(out, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
