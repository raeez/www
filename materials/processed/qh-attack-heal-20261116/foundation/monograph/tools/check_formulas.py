"""Formula retention: every formula of each chapter's Markdown, inline \\(...\\) and displayed \\[...\\] or $$...$$,
must reach the chapter's article as MathML whose TeX annotation is the same formula (whitespace aside; an authored
\\tag is shown by the page beside its display, so it is compared apart). Figures are excluded.
    python3 check_formulas.py <book.html> <reader-data folder> <out.json> [formula ...]"""
import collections, hashlib, html, json, os, re, sys
book, rd, out = sys.argv[1:4]
watch = sys.argv[4:]
norm = lambda t: ' '.join(t.split())
h = open(book, encoding='utf-8').read()
m = json.load(open(os.path.join(rd, 'manifest.json'), encoding='utf-8'))
rows, found = [], {w: [] for w in watch}
for c in m['chapters']:
    f = os.path.normpath(os.path.join(rd, c['path'])); raw = re.sub(r'<!--.*?-->', '', open(f, encoding='utf-8').read(), flags=re.S)
    raw = re.sub(r'`[^`\n]*`', ' ', raw)
    src = []
    for mm in re.finditer(r'\\\[(.+?)\\\]|\$\$(.+?)\$\$|\\\((.+?)\\\)', raw, re.S):
        tex = mm.group(1) or mm.group(2) or mm.group(3)
        src.append(norm(re.sub(r'\\tag\*?\{[^{}]*\}', '', tex)))
    a = h.index(f'<article class="mg-chapter" id="{c["id"]}"'); b = h.index('</article>', a)
    art = re.sub(r'<figure\b.*?</figure>', ' ', h[a:b], flags=re.S)
    page = [norm(html.unescape(x)) for x in re.findall(r'<annotation encoding="application/x-tex">(.*?)</annotation>', art, re.S)]
    cs, cp = collections.Counter(src), collections.Counter(page)
    missing = list((cs - cp).elements()); extra = list((cp - cs).elements())
    rows.append({'chapter': c['id'], 'file_sha256': hashlib.sha256(open(f, 'rb').read()).hexdigest(), 'formulas_source': len(src),
                 'formulas_page': len(page), 'missing_on_page': missing, 'extra_on_page': extra})
    for w in watch:
        for t in src:
            if w in t:
                found[w].append({'chapter': c['id'], 'formula': t[:200], 'on_page': t in cp})
res = {'book_sha256': hashlib.sha256(open(book, 'rb').read()).hexdigest(),
       'totals': {'formulas_source': sum(r['formulas_source'] for r in rows), 'formulas_page': sum(r['formulas_page'] for r in rows),
                  'missing_on_page': sum(len(r['missing_on_page']) for r in rows), 'extra_on_page': sum(len(r['extra_on_page']) for r in rows)},
       'watched': found, 'chapters': rows}
json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(res['totals']))
for w, hits in found.items():
    print(repr(w), [(x['chapter'], x['on_page']) for x in hits])
for r in rows:
    if r['missing_on_page'] or r['extra_on_page']:
        print(r['chapter'], 'missing', [x[:70] for x in r['missing_on_page'][:3]], 'extra', [x[:70] for x in r['extra_on_page'][:3]])
