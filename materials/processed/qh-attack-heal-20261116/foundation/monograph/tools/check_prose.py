"""Prose retention: every word of each chapter's Markdown, outside formulas, link targets, ids and hooks, must reach
the chapter's article on the page. Also displays and \\tag numbers, source against page.
    python3 check_prose.py <book.html> <reader-data folder> <out.json>"""
import difflib, hashlib, html, json, os, re, sys, datetime
book, rd, out = sys.argv[1:4]
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def words(t): return re.findall(r"[A-Za-z][A-Za-z'’-]*", t)
h = open(book, encoding='utf-8').read()
m = json.load(open(os.path.join(rd, 'manifest.json'), encoding='utf-8'))
rows = []
for c in m['chapters']:
    f = os.path.normpath(os.path.join(rd, c['path'])); raw = open(f, encoding='utf-8').read()
    src = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
    src = '\n'.join(l for l in src.splitlines() if not re.match(r'^\s{0,3}\[[^\]]+\]:\s', l))
    src = re.sub(r'\\\[.*?\\\]|\$\$.*?\$\$|\\\(.*?\\\)', ' ', src, flags=re.S)
    src = re.sub(r'\]\([^)]*\)', ']', src); src = re.sub(r'\]\[[^\]]*\]', ']', src)
    src = re.sub(r'\{#[^}]*\}', ' ', src); src = re.sub(r'^:::.*$', ' ', src, flags=re.M)
    src = re.sub(r'^#\s.*$', ' ', src, count=1, flags=re.M)
    sw = words(src)
    a = h.index(f'<article class="mg-chapter" id="{c["id"]}"'); b = h.index('</article>', a); art = h[a:b]
    art2 = re.sub(r'<figure\b.*?</figure>', ' ', art, flags=re.S)
    t = re.sub(r'<math\b.*?</math>', ' ', art2, flags=re.S)
    for pat in (r'<header class="mg-ch-head">.*?</header>', r'<aside\b.*?</aside>', r'<nav class="mg-ch-end".*?</nav>'):
        t = re.sub(pat, ' ', t, flags=re.S)
    for pat in (r'<span class="mg-sec-no">.*?</span>', r'<span class="mg-tag"[^>]*>.*?</span>', r'<span class="mg-qed"[^>]*>.*?</span>'):
        t = re.sub(pat, ' ', t)
    hw = words(html.unescape(re.sub(r'<[^>]+>', ' ', t)))
    ops = difflib.SequenceMatcher(None, sw, hw, autojunk=False).get_opcodes()
    lost = [' '.join(sw[i1:i2]) for op, i1, i2, j1, j2 in ops if op in ('delete', 'replace')]
    added = [' '.join(hw[j1:j2]) for op, i1, i2, j1, j2 in ops if op in ('insert', 'replace')]
    ds = len(re.findall(r'\\\[', raw)) + len(re.findall(r'^\s*\$\$', raw, flags=re.M)) // 2
    dp = len(re.findall(r'<div class="math-display">|<span class="math-display">', art2))
    ts, tp = re.findall(r'\\tag\*?\{([^{}]*)\}', raw), re.findall(r'data-tag="([^"]+)"', art)
    rows.append({'chapter': c['id'], 'file': os.path.basename(f), 'file_sha256': sha(f), 'prose_words': len(sw),
                 'source_words_not_on_page': lost, 'page_words_not_in_source': added, 'displays': [ds, dp], 'tags': [len(ts), len(tp)],
                 'tags_equal': ts == tp})
res = {'made_utc': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'), 'book_sha256': sha(book),
       'totals': {'chapters': len(rows), 'prose_words': sum(r['prose_words'] for r in rows),
                  'source_words_not_on_page': sum(len(r['source_words_not_on_page']) for r in rows),
                  'displays_equal': all(r['displays'][0] == r['displays'][1] for r in rows), 'tags_equal': all(r['tags_equal'] for r in rows)},
       'chapters': rows}
json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(res['totals']))
for r in rows:
    extra = [x for x in r['page_words_not_in_source'] if not re.fullmatch(r'(arXiv( (math|hep-th|v))*\s*)+', x)]
    if r['source_words_not_on_page'] or extra:
        print(r['chapter'], 'lost', r['source_words_not_on_page'][:5], 'added (other than arXiv numbers)', extra[:5])
