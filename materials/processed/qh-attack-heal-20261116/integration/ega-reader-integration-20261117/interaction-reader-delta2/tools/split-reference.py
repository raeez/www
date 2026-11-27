"""The book with its reference in companion pages (reader/DEFERRED-REFERENCE.md), made from one built page:

    python3 -I tools/split-reference.py <book.html> <out dir> [--book-name index.html] [--status <status.js>]
                                         [--keep programme-overview]

- --book-name: the book page's file name in <out dir> (default: the source's), as the pages link to it.
- status.js: a script of the page that runs beside the reader (it carries the reader-mode comment) is moved to
  reference.html, before the reader; --status gives it instead when the page has none.

- out/<book name>: the title page, the contents, the chapters and the kept reference parts. Its reader script is kept;
  the atlas script is dropped; the map (script#reader-pages) is added.
- out/reference.html: every other reference part except the atlas, whole, with #card, the map, status.js (if given)
  and the reader script.
- out/atlas.html: the atlas part, whole, with the map, the atlas script and the reader script.

Every href="#id" whose id lives in another page is written as "<page>#id". Each page's CSP gains 'self' for scripts,
so that the search index (reader-index.js, made afterwards by tools/reader-index.cjs) can be loaded. The tool moves
markup and changes no text. It prints, for each page, its elements, MathML formulae, ids and bytes, and its sha256."""
import hashlib
import html
import json
import os
import re
import sys

READER = '/* The reader of the monograph.'
ATLAS = '/* The research atlas'
STATUS_MARK = 'Beside the monograph reader ([data-reader]) this script keeps'


def sha(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def top_sections(s, start, end):
    """Top-level <section ...> elements of s[start:end] (balanced), as (open start, close end, open tag)."""
    out = []
    depth = 0
    cur = None
    for m in re.finditer(r'<(/?)section\b[^>]*>', s[start:end]):
        if m.group(1):
            depth -= 1
            if depth == 0 and cur:
                out.append((cur[0], start + m.end(), cur[1]))
                cur = None
        else:
            if depth == 0:
                cur = (start + m.start(), m.group(0))
            depth += 1
    return out


def ids_in(t):
    return re.findall(r'\bid="([^"]+)"', t)


def heading_text(sec):
    m = re.search(r'aria-labelledby="([^"]+)"', sec)
    h = re.search(r'<(h[1-6])\b[^>]*\bid="%s"[^>]*>(.*?)</\1>' % re.escape(m.group(1)), sec, re.S) if m else None
    if not h:
        h = re.search(r'<(h[1-6])\b[^>]*>(.*?)</\1>', sec, re.S)
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h.group(2)))).strip() if h else ''


def rewrite(page, own, where):
    """href="#id" for an id of another page becomes "<page>#id"."""
    def fix(m):
        raw = m.group(1)
        idv = html.unescape(raw)
        if idv in own or idv not in where:
            return m.group(0)
        return 'href="%s#%s"' % (where[idv], raw)
    return re.sub(r'href="#([^"]+)"', fix, page)


def csp_self(page):
    return re.sub(r"(script-src)([^;\"]*)", lambda m: m.group(0) if "'self'" in m.group(2) else m.group(1) + " 'self'" + m.group(2), page, count=1)


def counts(page):
    body = page[page.find('<body'):]
    return {'elements': len(re.findall(r'<[a-zA-Z][\w-]*', body)), 'math': len(re.findall(r'<math\b', body)),
            'ids': len(ids_in(body)), 'bytes': len(page.encode('utf-8'))}


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    src, outdir = argv[1], argv[2]
    status = open(argv[argv.index('--status') + 1], encoding='utf-8').read() if '--status' in argv else None
    keep = set(['programme-overview'])
    if '--keep' in argv:
        keep = set(argv[argv.index('--keep') + 1].split(','))
    s = open(src, encoding='utf-8').read()
    book_name = argv[argv.index('--book-name') + 1] if '--book-name' in argv else os.path.basename(src)
    if '/' in book_name or not book_name.endswith('.html'):
        print('--book-name must be a file name ending in .html')
        return 2
    m0 = s.find('<main')
    m1 = s.find('>', m0) + 1
    me = s.rfind('</main>')
    main_open = s[m0:m1]
    secs = [(a, b, tag) for a, b, tag in top_sections(s, m1, me) if 'data-reference' in tag]
    parts = {'reference.html': [], 'atlas.html': []}
    for a, b, tag in secs:
        idm = re.search(r'\bid="([^"]+)"', tag)
        pid = idm.group(1) if idm else ''
        if not pid or pid in keep:
            continue
        page = 'atlas.html' if 'data-atlas-mount' in tag else 'reference.html'
        parts[page].append((a, b, pid))
    moved = sorted([x for v in parts.values() for x in v], key=lambda x: x[0])
    if not moved:
        print('no reference part to move')
        return 1
    # the book page: the reference parts moved out
    book = s
    for a, b, pid in reversed(moved):
        book = book[:a] + book[b:]
    where = {}
    pages = []
    for page in ('reference.html', 'atlas.html'):
        if not parts[page]:
            continue
        ids = []
        meta = []
        for a, b, pid in parts[page]:
            sec = s[a:b]
            ids.extend(ids_in(sec))
            meta.append({'id': pid, 'title': heading_text(sec)})
        for i in ids:
            where[i] = page
        pages.append({'href': page, 'parts': meta, 'ids': ids})
    title_m = re.search(r'<h1\b[^>]*>(.*?)</h1>', s, re.S)
    title = html.unescape(re.sub(r'<[^>]+>', ' ', title_m.group(1))).strip() if title_m else ''
    title = re.sub(r'\s+', ' ', title)
    pmap = {'book': book_name, 'title': title, 'index': 'reader-index.js', 'pages': pages}
    map_script = '<script type="application/json" id="reader-pages">%s</script>' % json.dumps(pmap, ensure_ascii=False).replace('</', '<\\/')
    book_ids = set(ids_in(book[book.find('<body'):]))
    for i in book_ids:
        where.setdefault(i, book_name)

    # scripts after </main>
    def scripts(page_text):
        return [(m.start(), m.end(), m.group(1)) for m in re.finditer(r'<script>(.*?)</script>', page_text, re.S)]
    tail_from = s.rfind('</main>')
    sc = [x for x in scripts(s) if x[0] > tail_from]
    reader = next((x[2] for x in sc if x[2].lstrip().startswith(READER)), None)
    atlas = next((x[2] for x in sc if x[2].lstrip().startswith(ATLAS)), None)
    served_status = next((x[2] for x in sc if STATUS_MARK in x[2][:2000]), None)
    if status is None:
        status = served_status
    if reader is None:
        print('the page has no reader script')
        return 1
    # the book: drop the atlas script, put the map before the reader
    bme = book.rfind('</main>')
    for gone in (atlas, served_status):
        if gone is not None:
            i = book.find('<script>' + gone + '</script>', bme)
            book = book[:i] + book[i + len('<script>' + gone + '</script>'):]
    i = book.find('<script>' + reader + '</script>', bme)
    book = book[:i] + map_script + book[i:]
    book = csp_self(rewrite(book, book_ids, where))

    head = s[:s.find('<body')]
    body_open = re.search(r'<body\b[^>]*>', s).group(0)
    before_main = s[s.find(body_open) + len(body_open):m0]
    after_main = s[me + len('</main>'):]
    foot = re.search(r'<footer\b.*?</footer>', after_main, re.S)
    foot = foot.group(0) if foot else ''
    card = re.search(r'<div class="card" id="card".*?</div></div>', after_main, re.S)
    card = card.group(0) if card else ''
    companion_open = main_open.replace('data-reader', 'data-reader data-reader-book="%s"' % book_name, 1)
    out = {book_name: book}
    for page in ('reference.html', 'atlas.html'):
        if not parts[page]:
            continue
        body = ''.join(s[a:b] for a, b, pid in parts[page])
        own = set(ids_in(body))
        scripts_html = ''
        if page == 'reference.html' and status:
            scripts_html += '<script>%s</script>' % status
        if page == 'atlas.html' and atlas is not None:
            scripts_html += '<script>%s</script>' % atlas
        scripts_html += '<script>%s</script>' % reader
        doc = (head + body_open + before_main + companion_open + body + '</main>' + foot +
               (card if page == 'reference.html' else '') + map_script + scripts_html + '</body></html>\n')
        own |= set(ids_in(before_main + companion_open + foot + (card if page == 'reference.html' else '')))
        out[page] = csp_self(rewrite(doc, own, where))
    os.makedirs(outdir, exist_ok=True)
    total = counts(s)
    print('source  ', sha(s), json.dumps(total))
    for name, text in out.items():
        open(os.path.join(outdir, name), 'w', encoding='utf-8').write(text)
        c = counts(text)
        print('%-8s' % name[:8], sha(text), json.dumps(c), '(%d%% of the source elements)' % round(100 * c['elements'] / max(1, total['elements'])))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
