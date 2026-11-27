"""Each split page names itself in its <head>: canonical address, <title> and og:title. Run it after the split and
before the search index. The splitter copies the book's head, with the book's address and title, into the companion
pages.

    python3 -I set_page_metadata.py <site folder>

- Canonical: index.html names the site's address (…/quantum-holography/), read from the book's canonical link as the
  build writes it from page.json; reference.html and atlas.html name their own files.
- Title and og:title: the book keeps its own. A companion page is named first, then the book:
  - atlas.html by the book's contents link to it ("Atlas"), the name the reader's bar and search scopes also give it;
  - reference.html as "Reference", its share of the contents group "Atlas and reference".
  The book's title, its author suffix and its og:title are read from index.html, not restated here.
Only these three tags in each head change; the atlas's SVG <title> elements in the body are untouched. Each head must
hold exactly one of each. Idempotent. Prints each page's values."""
import html
import re
import sys
from pathlib import Path

site = Path(sys.argv[1])
CANON = re.compile(r'<link rel="canonical" href="([^"]+)">')
TITLE = re.compile(r'<title>(.*?)</title>', re.S)
OG = re.compile(r'<meta property="og:title" content="([^"]*)">')


def split_head(text, name):
    i = text.find('</head>')
    if i < 0:
        sys.exit(f'{name} has no </head>')
    return text[:i], text[i:]


def one(rx, head, name, what):
    found = rx.findall(head)
    if len(found) != 1:
        sys.exit(f'{name}: its head holds {len(found)} {what}')
    return found[0]


def words(fragment):
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', fragment)).split())


book_head, book_body = split_head((site / 'index.html').read_text(encoding='utf-8'), 'index.html')
canon = one(CANON, book_head, 'index.html', 'canonical links')
base = re.sub(r'(?:index\.html)?$', '', canon)
if not (base.startswith('https://') and base.endswith('/')):
    sys.exit(f'cannot read the site address from {canon!r}')
book_og = html.unescape(one(OG, book_head, 'index.html', 'og:title tags'))
book_title = html.unescape(one(TITLE, book_head, 'index.html', 'titles'))
if not book_title.startswith(book_og):
    sys.exit('the book title does not begin with its og:title')
suffix = book_title[len(book_og):]  # ' — <author>'

contents = re.search(r'<nav\b[^>]*\bid="contents"[^>]*>(.*?)</nav>', book_body, re.S)
if not contents:
    sys.exit('index.html has no contents')
atlas_links = [words(m.group(1)) for m in re.finditer(r'<a\b[^>]*\shref="atlas\.html#atlas"[^>]*>(.*?)</a>', contents.group(1), re.S)]
if len(atlas_links) != 1 or not atlas_links[0]:
    sys.exit(f'the contents link to the atlas: {atlas_links}')

pages = (('index.html', base, None),
         ('reference.html', base + 'reference.html', 'Reference'),
         ('atlas.html', base + 'atlas.html', atlas_links[0]))
for name, url, page_name in pages:
    p = site / name
    head, body = split_head(p.read_text(encoding='utf-8'), name)
    one(CANON, head, name, 'canonical links')
    head = CANON.sub(lambda m: f'<link rel="canonical" href="{url}">', head, count=1)
    if page_name:
        og = f'{page_name} — {book_og}'
        one(TITLE, head, name, 'titles')
        one(OG, head, name, 'og:title tags')
        head = TITLE.sub(lambda m: f'<title>{html.escape(og + suffix, quote=False)}</title>', head, count=1)
        head = OG.sub(lambda m: f'<meta property="og:title" content="{html.escape(og)}">', head, count=1)
    p.write_text(head + body, encoding='utf-8')
    print(f'{name:15s} {url} | title: {html.unescape(one(TITLE, head, name, "titles"))} | og:title: {html.unescape(one(OG, head, name, "og:title tags"))}')
