"""Each split page names its own public address as canonical (run after the split, before the search index).

    python3 -I set_canonical.py <site folder>

The book page's canonical link, as the build writes it from page.json (for example
https://momentum-sez.github.io/quantum-holography/index.html), gives the site's address. Then:
- index.html names the site's address itself (…/quantum-holography/), the address a reader is given;
- reference.html and atlas.html name their own files (…/reference.html, …/atlas.html); the splitter copies the book's
  head, and with it the book's canonical, into both.
Only the <link rel="canonical"> tag changes; each page must hold exactly one. Idempotent. Prints each page's address."""
import re
import sys
from pathlib import Path

site = Path(sys.argv[1])
TAG = re.compile(r'<link rel="canonical" href="([^"]+)">')
book = (site / 'index.html').read_text(encoding='utf-8')
found = TAG.findall(book)
if len(found) != 1:
    sys.exit(f'index.html holds {len(found)} canonical links')
base = re.sub(r'(?:index\.html)?$', '', found[0])
if not base.endswith('/'):
    sys.exit(f'cannot read the site address from {found[0]!r}')
for name, url in (('index.html', base), ('reference.html', base + 'reference.html'), ('atlas.html', base + 'atlas.html')):
    p = site / name
    t = p.read_text(encoding='utf-8')
    if len(TAG.findall(t)) != 1:
        sys.exit(f'{name} holds {len(TAG.findall(t))} canonical links')
    before = TAG.search(t).group(1)
    p.write_text(TAG.sub(f'<link rel="canonical" href="{url}">', t, count=1), encoding='utf-8')
    print(f'{name:15s} {before} -> {url}')
