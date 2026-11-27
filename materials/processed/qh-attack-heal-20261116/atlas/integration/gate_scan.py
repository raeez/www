"""Gate scans of the atlas: the page audit's FORBIDDEN rules and the external-gate rules, over atlas.css,
atlas.js and the atlas section of built pages (text, attributes and TeX annotations counted apart).

usage: python3 -B gate_scan.py <compiler dir with audit.py> <atlas.css> <atlas.js> <page.html>...
Exit 1 when the atlas's own files or the interface text of a page (outside supplied content) has a hit."""
import html, re, sys

sys.path.insert(0, sys.argv[1])
import audit  # noqa: E402

EXTRA = [
    (r'\b(draft|phase|wave|cycle|swarm|attack|heal|referee|candidate|lane|wip|todo|fixme|tbd|placeholder|provisional)\b', 'process word', re.I),
    (r'\bv\d+(\.\d+)+\b|\bversion\b', 'version word', re.I),
    (r'\b(perhaps|maybe|probably|we believe|it seems|hopefully)\b', 'hedging word', re.I),
    (r'/Users/|~/|centcom|\bmathematics/|\.claude\b|github\.com/|file://', 'closed-source path', re.I),
    (r'\b(?=[0-9a-f]*[a-f])(?=[0-9a-f]*\d)[0-9a-f]{7,}\b', 'hex hash', 0),
    (r'\d\s*%|\bpercent\b', 'percentage', re.I),
    (r'\b(session|model|assistant)\b', 'model or session word', re.I),
]
RULES = [(p, w, f) for p, w, f in audit.FORBIDDEN] + EXTRA
# For attributes, which carry the content owner's ids: the page's rules, paths, hashes and percentages; the
# process and model word lists apply to the atlas's own words only (ids such as a Ward model or a finite
# cycle are mathematics).
ATTR_RULES = [(p, w, f) for p, w, f in RULES if w not in ('process word', 'version word', 'hedging word', 'model or session word')]
GEOMETRY = {'d', 'transform', 'viewbox', 'x', 'y', 'width', 'height', 'rx', 'refx', 'refy', 'markerwidth', 'markerheight',
            'x1', 'x2', 'y1', 'y2', 'cx', 'cy', 'r', 'points', 'markerunits', 'orient', 'focusable', 'tabindex', 'style'}
# Elements whose text is the content owner's (supplied), not the atlas's interface words: the atlas's own list.
import atlas  # noqa: E402  (from the same compiler dir as audit)
SUPPLIED = re.compile(r'class="(?:[^"]* )?(?:' + '|'.join(re.escape(c) for c in atlas.SUPPLIED_CLASSES) + r')(?: [^"]*)?"')


def api_use(why, m, text):
    """In a stylesheet or script: a CSS length in per cent, and the HTML placeholder API (::placeholder, .placeholder)."""
    if why == 'percentage' and m.group(0).endswith('%'):
        return True
    return m.group(0).lower() == 'placeholder' and (text[max(0, m.start() - 2):m.start()] == '::' or text[m.start() - 1:m.start()] == '.')


def scan(label, text, strict=True, source=False, rules=None):
    hits = []
    for pattern, why, flags in rules or RULES:
        for m in re.finditer(pattern, text, flags):
            if source and api_use(why, m, text):
                continue
            hits.append((why, m.group(0), text[max(0, m.start() - 50):m.end() + 30].replace('\n', ' ')))
    print(f'{label}: {len(hits)} hit(s)')
    for why, word, ctx in hits[:12]:
        print(f'    {why}: {word!r} in ...{ctx}...')
    return hits if strict else []


def section(page):
    """The atlas section, to its own closing tag (sections inside it are counted)."""
    m = re.search(r'<section\b[^>]*\sid="atlas"[^>]*>', page)  # the id, wherever it stands in the tag
    a = m.start() if m else -1
    if a < 0:
        return ''
    depth = 0
    for t in re.finditer(r'<(/?)section\b[^>]*>', page[a:]):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return page[a:a + t.end()]
    return page[a:]


def strip_supplied(markup):
    """Removes every element whose class marks supplied content, by matching its tag to its close."""
    out, i = [], 0
    for m in SUPPLIED.finditer(markup):
        start = markup.rfind('<', 0, m.start())
        if start < i:
            continue
        tag = re.match(r'<([a-zA-Z][\w-]*)', markup[start:]).group(1)
        depth, j = 0, start
        for t in re.finditer(r'<(/?)' + tag + r'\b[^>]*>', markup[start:]):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                j = start + t.end()
                break
        out.append(markup[i:start])
        i = j
    out.append(markup[i:])
    return ''.join(out)


def main():
    bad = []
    for path in sys.argv[2:4]:
        bad += scan(path.rsplit('/', 1)[-1] + ' (CSS lengths and the placeholder API excepted)', open(path, encoding='utf-8').read(), source=True)
    for path in sys.argv[4:]:
        sec = section(open(path, encoding='utf-8').read())
        print(f'== {path} (atlas section {len(sec.encode())} bytes)')
        no_tex = re.sub(r'<annotation\b[^>]*>.*?</annotation>', ' ', sec, flags=re.S)
        tex = ' '.join(re.findall(r'<annotation\b[^>]*>(.*?)</annotation>', sec, flags=re.S))
        attrs = ' '.join(html.unescape(v) for k, v in re.findall(r'\s([\w:-]+)="([^"]*)"', no_tex) if k.lower() not in GEOMETRY)
        words = strip_supplied(no_tex)
        iface = html.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'<(svg|math)\b.*?</\1>', ' ', words, flags=re.S)))
        bad += scan(f'  interface text, supplied content removed ({len(iface.split())} words)', iface)
        bad += scan('  attributes (geometry removed; page rules, paths, hashes, percentages)', attrs, rules=ATTR_RULES)
        scan('  attributes, process and model word lists (supplied ids; for the content owner)', attrs, strict=False,
             rules=[r for r in RULES if r not in ATTR_RULES])
        seen = audit.visible_text('<body>' + no_tex)  # the page audit's own reading of visible text
        scan(f'  all visible text, supplied content included ({len(seen.split())} words; content findings, for the content owner)',
             seen, strict=False)
        scan('  TeX annotations (not visible)', html.unescape(tex), strict=False)
    print('RESULT', 'FAIL' if bad else 'PASS')
    sys.exit(1 if bad else 0)


main()
