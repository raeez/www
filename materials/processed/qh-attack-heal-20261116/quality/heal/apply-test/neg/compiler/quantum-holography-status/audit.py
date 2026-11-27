"""Checks run on every build of the status page.

Failures stop the page from being written to the repository root (unless --allow-draft):
  - a statement or cell with an unknown status, a missing cell, a TeX error;
  - any reference to another host (the page must make no outside request and carry no tracker);
  - an in-page link whose target does not exist;
  - reader-visible words that belong to project management rather than mathematics
    (the golden rule): names of tools or models, record and file names, internal
    identifiers, workflow vocabulary.
"""
import html
import re

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
    (r'/Users/|~/|\bengine/|\bprep/|\bchains/', 'path', 0),
    (r'\b[a-z]{2,5}:(thm|prop|lem|def|cor|qn|eq|sec|rem|op|cc|hyp|mix|p|t):[\w-]+', 'LaTeX label', 0),
]

ALLOWED_HOSTS_IN_HREF = ()  # no other host at all


def visible_text(markup):
    body = markup[markup.find('<body'):]
    body = re.sub(r'<script\b.*?</script>', ' ', body, flags=re.S)
    body = re.sub(r'<style\b.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<math\b.*?</math>', ' ', body, flags=re.S)
    body = re.sub(r'<svg\b.*?</svg>', ' ', body, flags=re.S)
    return re.sub(r'\s+', ' ', strip_tags(body))


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
    dup = {i for i in re.findall(r'\sid="([^"]+)"', markup) if list(re.findall(r'\sid="([^"]+)"', markup)).count(i) > 1}
    for i in sorted(dup):
        failures.append(f'duplicate id {i}')

    # The golden rule, on what a reader sees.
    text = visible_text(markup)
    flagged = []
    for pattern, why, flags in FORBIDDEN:
        for m in re.finditer(pattern, text, flags=flags):
            ctx = text[max(0, m.start() - 50): m.end() + 50]
            flagged.append(f'{why}: "{m.group(0)}" in …{ctx}…')
    failures.extend(flagged)

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
