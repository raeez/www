import json, re, sys, unicodedata
import fitz
S = sys.argv[1]
keys = json.load(open(S + '/run4.json'))['steps']['statementKeys']
def norm(t):
    t = unicodedata.normalize('NFKC', t)
    t = t.replace('­', '').replace('‐', '-').replace('‑', '-')
    t = re.sub(r'-\s*\n\s*', '', t)          # soft line-end hyphenation
    t = re.sub(r'\s+', ' ', t)
    return t.strip()
out = {}
for name in ('print-a4.pdf', 'print-letter.pdf', 'print-a4-dark.pdf'):
    doc = fitz.open(S + '/' + name)
    W, H = doc[0].rect.width, doc[0].rect.height
    minx, maxx = 1e9, -1e9; beyond = []; inmargin = []; texts = []
    for pno, page in enumerate(doc):
        d = page.get_text('dict')
        for blk in d['blocks']:
            for line in blk.get('lines', []):
                for sp in line['spans']:
                    if not sp['text'].strip(): continue
                    x0, y0, x1, y1 = sp['bbox']
                    minx = min(minx, x0); maxx = max(maxx, x1)
                    if x1 > W + 0.5 or x0 < -0.5: beyond.append((pno + 1, round(x0, 1), round(x1, 1), sp['text'][:40], sp['font']))
        texts.append(page.get_text('text'))
    full = norm('\n'.join(texts))
    # margins actually used by body text: robust percentiles of span x-extents
    xs0 = []; xs1 = []
    for page in doc:
        for blk in page.get_text('dict')['blocks']:
            for line in blk.get('lines', []):
                for sp in line['spans']:
                    if sp['text'].strip(): xs0.append(sp['bbox'][0]); xs1.append(sp['bbox'][2])
    xs0.sort(); xs1.sort()
    q = lambda a, f: a[int(f * (len(a) - 1))]
    res = {'pages': len(doc), 'paper_pt': [round(W, 1), round(H, 1)], 'text_min_x0': round(minx, 1), 'text_max_x1': round(maxx, 1),
           'x0_p01': round(q(xs0, .01), 1), 'x1_p99': round(q(xs1, .99), 1), 'spans_beyond_paper': len(beyond), 'beyond_sample': beyond[:12]}
    # status chips (uppercase via text-transform)
    up = {k: len(re.findall(re.escape(v), full)) for k, v in {'checked': 'PROVED AND INDEPENDENTLY CHECKED', 'open': 'OPEN PROBLEM', 'conditional': 'CONDITIONAL', 'published': 'PUBLISHED'}.items()}
    res['uppercase_chip_counts'] = up
    # statement titles / first words present
    missing = []
    for k in keys:
        probe = k['title'] if len(k['title']) >= 12 else (k['text'] if len(k['text']) >= 12 else k['title'])
        p = norm(probe)
        if len(p) < 6: continue
        p = p[:60]
        if p not in full and p.replace("'", '’') not in full: missing.append({'id': k['id'], 'probe': p})
    res['statements_probed'] = len(keys); res['statements_missing_text'] = len(missing); res['missing_sample'] = missing[:10]
    ctrl = ['Open all', 'Close all', 'Search this page', 'Skip to the page', 'Switch between light and dark', 'Select a mark for its scope', 'Press / to search', 'Search statements, questions']
    res['control_labels_in_pdf'] = {c: full.count(c) for c in ctrl if full.count(c)}
    # page numbers: a bare number centred near the bottom of each page
    pn = 0
    for i, page in enumerate(doc):
        for blk in page.get_text('dict')['blocks']:
            for line in blk.get('lines', []):
                t = ''.join(s['text'] for s in line['spans']).strip()
                if t == str(i + 1) and line['bbox'][1] > H - 60: pn += 1
    res['pages_with_bottom_number'] = pn
    out[name] = res
json.dump(out, open(S + '/pdfcheck.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False)[:6000])
