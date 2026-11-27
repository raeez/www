"""Checks run on every build of the status page.

Failures stop the page from being written to the repository root (unless --allow-draft):
  - a statement or cell with an unknown status, a missing cell, a TeX error;
  - any reference to another host (the page must make no outside request and carry no tracker);
  - an in-page link whose target does not exist;
  - reader-visible words that belong to project management rather than mathematics
    (the golden rule): names of tools or models, record and file names, internal
    identifiers, workflow vocabulary, process stage labels, percentages, raw TeX. The same rules
    apply to the words of formulas (\text{}), to attribute values that a reader hears or sees
    (aria-label, title, alt, placeholder, meta content) and to element ids, which appear in shared
    addresses.
Warnings (reported, not blocking): words that may be workflow residue and need the content owner's
reading, and statements without an id (no link reaches the statement itself).
"""
import html
import re
from collections import Counter

from status import CELL_STATUSES, COLUMNS, STATEMENT_STATUSES, strip_tags

# Reader-visible text must not name tools, models, files or workflow. Each pattern is
# matched case-insensitively against the visible text with mathematics removed.
FORBIDDEN = [
    (r'\b(astra|claude|codex|opus|fable|gpt-?\d|chatgpt|openai|anthropic|sonnet|haiku)\b', 'model or tool name', re.I),
    (r'\b(llm|language model|ai model|agent|subagent|prompt|chatbot)s?\b', 'model or agent vocabulary', re.I),
    (r'\b(adoption|adopted record|inscribe|census|spine|ledger|dossier|frontier engine|worktree|'
     r'commit|pull request|repository|pipeline|todo|backlog|audit|reviewer|checker|attacker|owner|ownership)s?\b',
     'workflow vocabulary', re.I),
    (r'(?<![\w.])(T|N|B|R|P|C)\d{1,3}(?![\w])', 'internal identifier', 0),
    (r'(?<![\w.])E[1-8](?![\w])', 'possible internal identifier (or E_n written without subscript)', 0),
    (r'\bv\d\b|-v\d\b', 'version tag', 0),
    (r'\.(md|json|tex|py|tsv|csv|log)\b', 'file name', 0),
    (r'/Users/|~/[\w.-]|\b(?:engine|prep|chains|frontier|inscribe)/[\w.-]+(?:/|\.\w{1,4}\b)', 'path', 0),
    (r'\b[a-z]{2,5}:(thm|prop|lem|def|cor|qn|eq|sec|rem|op|cc|hyp|mix|p|t):[\w-]+', 'LaTeX label', 0),
    (r'\battack[- ]?heal\w*|\bswarms?\b', 'workflow vocabulary', re.I),
    # Capitalised stage labels fail; the same words in lower case may be mathematics ("the s-wave 1", "phase 0")
    # and are only warned about (WARN).
    (r'(?<![\w-])(Wave|Phase|Session|Lane|Sprint|Round|Cycle)[- ]?[A-Z]?\d+\b', 'process stage label', 0),
    (r'\d+(?:\.\d+)?\s?%|\bper ?cent\b', 'percentage', re.I),
    (r'\b(version|revision)\s+\d+', 'version tag', re.I),
    (r'(?<![\w.])G\d{2,3}(?![\w])', 'internal identifier', 0),
]
PERCENT = FORBIDDEN[11]
WORDS = [FORBIDDEN[0], FORBIDDEN[1], FORBIDDEN[2], FORBIDDEN[9]]  # names and workflow words, for word-like tokens

# Raw TeX delimiters left in reader text mean a formula was not set as mathematics.
RAW_TEX = (r'\\[()\[\]]', 'raw TeX in reader text', 0)
# TeX source in an attribute is read aloud or shown as code.
TEX_IN_ATTRIBUTE = re.compile(r'\\[A-Za-z()\[\]{}]')
# Element ids appear in shared addresses: no tool, workflow or path names and no stage numbers there either;
# identifier shapes are only warned about, since ids also come from mathematics (r3, e2).
ID_FORBIDDEN = WORDS + [(r'(wave|phase|session|lane|sprint|round|cycle)-?\d+|/', 'stage number or path in an id', re.I)]
ID_WARN = [(r'(?<![a-z0-9])[tnbrpcg]\d{1,3}(?![a-z0-9])', 'identifier-like token in an id', re.I)]
# TeX source: names and files only; ~ is a TeX tie and chains/cochains is mathematics.
TEX_FORBIDDEN = [FORBIDDEN[0], FORBIDDEN[6], (r'/Users/|\b(?:engine|prep|frontier|inscribe)/[\w.-]+', 'path', 0)]

# Possible workflow residue in reader text: reported for the content owner, not blocking.
WARN = [
    (r'\badopted\b', 'possible workflow vocabulary (adopted)', re.I),
    (r'\bdrafts?\b', 'possible process vocabulary (draft)', re.I),
    (r'\b(saved|stored|recorded)\s+(?:[\w-]+\s+){0,3}(certificates?|computations?|arithmetic|matrix|matrices)\b|\breplayed\b',
     'reference to a stored artefact the reader cannot inspect', re.I),
    (r'(?<![\w\\])[A-Za-z]_(?:\{[^}]*\}|[A-Za-z0-9])', 'possible formula outside TeX delimiters', 0),
    (r'(?<![\w-])(wave|phase|session|lane|sprint|round|cycle)[- ]?\d+\b', 'possible process stage label', 0),
]
READER_ATTRIBUTES = re.compile(r'\s(aria-label|title|alt|placeholder|aria-description|aria-roledescription|aria-placeholder|aria-valuetext)="([^"]*)"')
DATA_BLOCK = re.compile(r'<script\b[^>]*type="application/(?:ld\+)?json"[^>]*>(.*?)</script>', re.S)
HASH = (r'(?<![\w-])[0-9a-f]{32,}(?![\w-])', 'hash', re.I)

ALLOWED_HOSTS_IN_HREF = ()  # no other host at all


def visible_text(markup, spaced=False):
    """The reader-visible body text with formulas removed. With spaced=True every tag boundary becomes a
    space, so that words in adjacent elements (a status chip and a title) do not fuse."""
    body = markup[markup.find('<body'):]
    body = re.sub(r'<script\b.*?</script>', ' ', body, flags=re.S)
    body = re.sub(r'<style\b.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<math\b.*?</math>', ' ', body, flags=re.S)
    body = re.sub(r'<svg\b.*?</svg>', ' ', body, flags=re.S)
    if spaced:
        return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', body)).replace('\u00ad', ''))
    return re.sub(r'\s+', ' ', strip_tags(body).replace('\u00ad', ''))


def scan(text, patterns, label=''):
    found = []
    for pattern, why, flags in patterns:
        for m in re.finditer(pattern, text, flags=flags):
            ctx = text[max(0, m.start() - 50): m.end() + 50]
            found.append(f'{why}{label}: "{m.group(0)}" in …{ctx}…')
    return found


def run(build, markup):
    failures = list(build.problems)
    warnings = list(build.warnings)
    c = build.content

    # Structure.
    rows = c.get('rows', [])
    if len(rows) != 20:
        warnings.append(f'the grid has {len(rows)} rows (the examples grid has 20)')
    for r in rows:
        for cid in COLUMNS:
            if cid not in (r.get('cells') or {}):
                failures.append(f'row {r.get("id")}: no cell for {cid}')
    for s in build.all_statements(c):
        if s.get('status') not in STATEMENT_STATUSES:
            failures.append(f'unknown status {s.get("status")!r}')

    # No other host: no src/href/url() pointing off the page except the site's own home link.
    bare = re.sub(r'<script\b.*?</script>', ' ', markup, flags=re.S)
    for m in re.finditer(r'(?:src|href|action|srcset|poster|data)\s*=\s*"([^"]*)"', bare):
        if re.search(r'rel="canonical"', bare[max(0, m.start() - 40):m.end() + 40]):
            continue  # the page's own address; never requested
        url = html.unescape(m.group(1))
        if re.match(r'^(https?:)?//', url, re.I):
            failures.append(f'outside reference: {url[:100]}')
    for m in re.finditer(r'url\(\s*([^)]*)\)', markup):
        url = m.group(1).strip('\'" ')
        if not url.startswith('data:') and not url.startswith('#'):
            failures.append(f'outside url(): {url[:100]}')
    if re.search(r'<link[^>]+rel="(stylesheet|preconnect|dns-prefetch|preload)"', markup):
        failures.append('a <link> that loads or prefetches another resource')
    if re.search(r'\b(fetch|XMLHttpRequest|sendBeacon|WebSocket|EventSource)\s*\(', markup):
        failures.append('a network call in the page script')

    # In-page links.
    ids = set(re.findall(r'\sid="([^"]+)"', markup))
    for m in re.finditer(r'href="#([^"]*)"', bare):
        if m.group(1) and m.group(1) not in ids:
            failures.append(f'broken in-page link #{m.group(1)}')
    for m in re.finditer(r'(?:data-term|aria-controls|aria-describedby|data-row)="([^"]+)"', markup):
        if m.group(1) not in ids:
            failures.append(f'reference to missing id {m.group(1)}')
    id_counts = Counter(re.findall(r'\sid="([^"]+)"', markup))
    for i in sorted(k for k, n in id_counts.items() if n > 1):
        failures.append(f'duplicate id {i}')

    # The golden rule, on what a reader sees: the text as written and with tag boundaries spaced, the
    # words inside formulas, the attributes read aloud or shown, the metadata, and the ids.
    flagged = []
    for text in (visible_text(markup), visible_text(markup, spaced=True)):
        flagged += scan(text, FORBIDDEN + [RAW_TEX])
    mtext = ' '.join(strip_tags(m) for m in re.findall(r'<mtext\b[^>]*>(.*?)</mtext>', markup, flags=re.S))
    flagged += scan(mtext, [f for f in FORBIDDEN if f is not PERCENT], ' (in a formula)')
    words = ' '.join(re.findall(r'<mi\b[^>]*>([^<]{3,})</mi>', markup))  # \operatorname{...}, \mathrm{...}
    flagged += scan(html.unescape(words), WORDS, ' (in a formula)')
    tex = ' '.join(re.findall(r'<annotation encoding="application/x-tex">(.*?)</annotation>', markup, flags=re.S))
    flagged += scan(html.unescape(tex), TEX_FORBIDDEN, ' (in TeX source)')
    svg_titles = ' '.join(t for svg in re.findall(r'<svg\b.*?</svg>', markup, flags=re.S) for t in re.findall(r'<title>(.*?)</title>', svg, flags=re.S))
    flagged += scan(html.unescape(svg_titles), FORBIDDEN, ' (in an image title)')
    for block in DATA_BLOCK.findall(markup):
        flagged += scan(block, FORBIDDEN + [HASH], ' (in a data block)')
    comments = re.findall(r'/\*.*?\*/', ' '.join(re.findall(r'<(?:style|script)\b[^>]*>(.*?)</(?:style|script)>', markup, flags=re.S)), flags=re.S)
    comments += re.findall(r'<!--.*?-->', markup, flags=re.S)
    flagged += scan(' '.join(comments), WORDS + [FORBIDDEN[6], FORBIDDEN[7], FORBIDDEN[10]], ' (in a comment)')
    bare_markup = re.sub(r'<(script|style)\b.*?</\1>', ' ', markup, flags=re.S)
    for name, value in READER_ATTRIBUTES.findall(bare_markup):
        value = html.unescape(value)
        flagged += scan(value, FORBIDDEN, f' (in {name})')
        if TEX_IN_ATTRIBUTE.search(value):
            flagged.append(f'TeX source in {name}: "{value[:120]}"')
    for m in re.finditer(r'<meta\s+(?:name|property)="(description|author|og:title|og:description)"\s+content="([^"]*)"', markup):
        flagged += scan(html.unescape(m.group(2)), FORBIDDEN, f' (in meta {m.group(1)})')
    title = re.search(r'<title>(.*?)</title>', markup, flags=re.S)
    if title:
        flagged += scan(html.unescape(title.group(1)), FORBIDDEN, ' (in title)')
    for i in id_counts:
        flagged += scan(i, ID_FORBIDDEN, ' (in id)')
    failures.extend(dict.fromkeys(flagged))
    for w in dict.fromkeys(scan(visible_text(markup, spaced=True), WARN) + scan(mtext, [PERCENT], ' (in a formula)')
                           + [x for i in id_counts for x in scan(i, ID_WARN, ' (in id)')]):
        warnings.append(w)
    anchorless = [strip_tags(s.get('title') or '') or (s.get('text') or '')[:80]
                  for s in build.all_statements(c) if not (s.get('id') or '').strip()]
    if anchorless:
        warnings.append(f'{len(anchorless)} statements have no id, so no link reaches the statement itself '
                        f'(listed in audit.json under statements_without_id); first: {anchorless[0][:80]}')

    # Metadata carries no tool credit either.
    head = re.sub(r'<(style|script)\b.*?</\1>', ' ', markup[:markup.find('</head>')], flags=re.S)
    if re.search(r'generator|astra|claude|codex|gpt', head, re.I):
        failures.append('tool or model named in the page head')

    tally = {}
    for s in build.all_statements(c):
        tally[s.get('status')] = tally.get(s.get('status'), 0) + 1
    cells = {}
    for r in rows:
        for cell in (r.get('cells') or {}).values():
            cells[cell.get('status')] = cells.get(cell.get('status'), 0) + 1
    return {
        'failures': failures,
        'warnings': warnings,
        'bytes': len(markup.encode('utf-8')),
        'statements': tally,
        'cells': cells,
        'terms': len(build.term_links.entries),
        'terms_attached': len(build.term_links.used),
        'terms_unused': sorted(e['term'] for e in build.term_links.entries if e['id'] not in build.term_links.used),
        'math': len(build.math.jobs),
        'math_errors': len(build.math.errors),
        'fonts': getattr(build, 'font_report', {}),
        'statements_without_id': anchorless,
    }


def text_report(result):
    lines = [f'bytes: {result["bytes"]:,}', f'statements: {result["statements"]}', f'cells: {result["cells"]}',
             f'terms: {result["terms"]} (attached in text: {result["terms_attached"]})',
             f'math: {result["math"]} (errors: {result["math_errors"]})', f'fonts: {result["fonts"]}']
    if result['terms_unused']:
        lines.append('terms never attached in the text: ' + ', '.join(result['terms_unused']))
    for w in result['warnings']:
        lines.append('WARNING ' + w)
    for f in result['failures']:
        lines.append('FAIL ' + f)
    lines.append('PASS' if not result['failures'] else f'{len(result["failures"])} failure(s)')
    return '\n'.join(lines) + '\n'
