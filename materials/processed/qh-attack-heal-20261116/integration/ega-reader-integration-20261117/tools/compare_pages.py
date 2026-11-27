"""Where two releases' pages differ, by part of the page, so a re-capture can be limited to what changed.

    python3 -I compare_pages.py <old site folder> <new site folder> <out.json>

Each page is cut into named parts:
- each inline <style> and <script> element, named by the first comment or the first selector or statement;
- in the body, each element that carries an id and is a chapter, the title page (#front), the contents, a reference
  part, or a figure.
For each page: the parts that changed, the parts added or removed, and whether everything outside them is
byte-identical. Reads both folders; writes only <out.json>."""
import hashlib
import json
import re
import sys

old, new, out = sys.argv[1:4]
PAGES = ['index.html', 'reference.html', 'atlas.html']
BLOCK = re.compile(r'<(style|script)\b[^>]*>(.*?)</\1>', re.S)
PART = re.compile(r'<(article|header|nav|section|figure)\b[^>]*\bid="([^"]+)"[^>]*>', re.S)


def name_of(kind, body):
    m = re.search(r'/\*\s*(.{1,70}?)\s*(?:\*/|\n)', body)
    if m:
        return f'{kind}: {m.group(1)}'
    first = body.strip().split('\n', 1)[0][:70]
    return f'{kind}: {first}'


def end_of(text, start, tag):
    """End offset of the element that opens at start (depth-counted on its own tag name)."""
    depth = 0
    for m in re.finditer(r'<(/?)%s\b[^>]*>' % tag, text[start:]):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return start + m.end()
    return len(text)


def parts(text):
    found = {}
    for m in BLOCK.finditer(text):
        key = name_of(m.group(1), m.group(2))
        while key in found:
            key += "'"
        found[key] = (m.start(), m.end())
    body_at = text.find('<body')
    for m in PART.finditer(text, body_at if body_at >= 0 else 0):
        tag, pid = m.group(1), m.group(2)
        if tag == 'section' and 'data-reference' not in m.group(0) and 'data-section' in m.group(0):
            continue  # sections inside chapters are covered by their chapter
        if tag == 'figure' or tag in ('article', 'header', 'nav') or 'data-reference' in m.group(0):
            key = f'{tag}#{pid}'
            if key not in found:
                found[key] = (m.start(), end_of(text, m.start(), tag))
    return found


def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


report = {}
for page in PAGES:
    a = open(f'{old}/{page}', encoding='utf-8').read()
    b = open(f'{new}/{page}', encoding='utf-8').read()
    pa, pb = parts(a), parts(b)
    changed = sorted(k for k in pa.keys() & pb.keys() if a[slice(*pa[k])] != b[slice(*pb[k])])
    added, removed = sorted(pb.keys() - pa.keys()), sorted(pa.keys() - pb.keys())

    def rest(text, ps, keys):
        spans = sorted(ps[k] for k in keys if k in ps)
        kept, at = [], 0
        for s, e in spans:
            if s >= at:
                kept.append(text[at:s])
                at = e
        kept.append(text[at:])
        return ''.join(kept)

    touched = set(changed) | set(added) | set(removed)
    outside_same = rest(a, pa, touched) == rest(b, pb, touched)
    report[page] = {'identical': a == b, 'changed_parts': changed, 'added_parts': added, 'removed_parts': removed,
                    'everything_else_identical': outside_same, 'old_sha256': hashlib.sha256(a.encode()).hexdigest(),
                    'new_sha256': hashlib.sha256(b.encode()).hexdigest()}
    print(f'{page}: identical {a == b}; changed {len(changed)}, added {len(added)}, removed {len(removed)}; '
          f'everything else identical: {outside_same}')
    for k in changed + ['+ ' + x for x in added] + ['- ' + x for x in removed]:
        print('    ', k[:110])
json.dump(report, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
