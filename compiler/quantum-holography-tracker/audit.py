"""Audits of a built tracker page.

Each audit reads the built page or the build's record of its inputs:

    terms      unwired terms: names marked or emphasised as terms without a card, and
               names that look like mathematical terms but have no card
    cards      cards with empty fields, unknown related ids, pointers instead of
               definitions, shared definitions and definitions too long for a card
    words      pointers to absent statements, attachments, TeX that failed to render,
               and words the page still needs (headlines, state definitions)
    leaks      internal strings in the page's text and attributes
    fetches    anything the page loads from another host, beyond the site's fonts
    listing    whether the page appears in the site's indexes
    weight     page bytes, compressed bytes and what they are made of

A failure in leaks, fetches, listing, robots, cards or words stops a settled build.
"""
import gzip
import re
from collections import Counter, defaultdict

from bs4 import BeautifulSoup, Comment, Tag

FONT_HOSTS = ('use.typekit.net', 'p.typekit.net', 'fonts.googleapis.com', 'fonts.gstatic.com')
INDEXES = ('writing.html', 'feed.xml', 'sitemap.xml', 'llms.txt', 'llms-full.txt', 'robots.txt', 'index.html')

LEAKS = [
    ('session or seat id', r'\b[0-9a-f]{8}-[0-9a-f]{4}(?:-[0-9a-f]{4}){0,3}\b'),
    ('long hexadecimal identifier', r'\b(?=[0-9a-f]*[a-f])(?=[0-9a-f]*[0-9])[0-9a-f]{12,}\b'),
    ('internal path', r'(?:/Users/|~/|\bmathematics-runtime\b|\bcoordination/|\bcentcom\b|\bworktrees?\b)'),
    ('file name', r'\b[\w-]+\.(?:tex|md|py|json|tsv|zip|sh|sty|cls|bib)\b'),
    ('LaTeX label', r'(?<![\w/])(?!https?:|mailto:|data:)[a-z]{2,8}:[a-z][a-z0-9]{1,15}(?::[a-z0-9-]+)?\b'),
    ('label anchor', r'\blabel-[a-z]+-[a-z]'),
    ('question code', r'\b(?:[BDENRTW]\d{2,3}|O-\d{2}|NEW-[A-Z0-9][\w-]*|W1-NEW\d+|H\d{3})\b'),
    ('ledger code', r'\b(?:D-20\d\d-\d\d-\d\d[\w-]*|MC-[A-Z]+-\d+|SC-\d{2,3})\b'),
    ('model or tool name', r'\b(?:Astra|Sol|Codex|GPT(?:-\d+)?|Claude|Opus|Fable|Sonnet|Gemini|ChatGPT|LLM)\b'
                           r'|\bPro\b(?![-‐–])'),
    ('process word', r'\b(?:wave(?![-‐ ]operator)|waves(?![-‐ ]operator)|heal|heals|healed|healing|packet|packets|harvest|harvested|seat|seats|'
                     r'lane|lanes|swarm|stand-in|redispatch|draft)\b'),
]
LEAK_RE = [(name, re.compile(pattern)) for name, pattern in LEAKS]
HARD_LEAKS = {'session or seat id', 'long hexadecimal identifier', 'internal path', 'file name',
              'LaTeX label', 'label anchor', 'question code', 'ledger code', 'model or tool name',
              'process word'}

POSITIONAL = re.compile(r'\b(above|below|preceding|earlier|later|this section|the next section|'
                        r'the examples|the following section|see)\b', re.I)
REFERENCE = re.compile(r'\b(Section|Chapter|Theorem|Proposition|Lemma|Definition|Corollary|Remark|'
                       r'Example|Question)\s+\d', re.I)
HEADS = ('algebra', 'algebras', 'coalgebra', 'coalgebras', 'category', 'categories', 'functor', 'functors',
         'complex', 'complexes', 'module', 'modules', 'space', 'spaces', 'group', 'groups', 'sheaf', 'sheaves',
         'operad', 'operads', 'cohomology', 'homology', 'duality', 'equivalence', 'equivalences', 'morphism',
         'morphisms', 'comparison', 'tensor', 'tensors', 'bracket', 'brackets', 'deformation', 'quantization',
         'representation', 'representations', 'lattice', 'lattices', 'completion', 'extension', 'extensions',
         'marking', 'stratum', 'strata', 'locus', 'fibre', 'fiber', 'adjunction', 'invariant', 'invariants',
         'connection', 'curvature', 'anomaly', 'current', 'currents', 'vacuum', 'product', 'products',
         'coproduct', 'residue', 'residues', 'pole', 'poles', 'action', 'actions', 'operator', 'operators',
         'theorem', 'identity', 'identities', 'resolution', 'transform', 'transpose', 'contraction',
         'homotopy', 'homotopies', 'derivation', 'derivations', 'charge', 'charges', 'kernel', 'kernels',
         'map', 'maps', 'object', 'objects', 'carrier', 'carriers', 'recipient', 'recipients', 'diagram',
         'diagrams', 'centre', 'center', 'unit', 'counit', 'monoid', 'monoids', 'bimodule', 'bimodules')
STOP = set('''a an the this that these those its their our his her of and or but nor for to in on at by with from
into onto over under between among same other another each every any all some no not only also both either
neither first second third one two three several many more most such own full whole new given fixed declared
original independent independently actual specified stated separate further different distinct common
corresponding resulting required necessary natural ordinary usual general specific single double finite
which whose where when how why what who whom is are was were be been being has have had do does did can
could may might must shall should will would than then there here very much less least'''.split())
CAPITAL_STOP = set('''The A An This That These Those It Its In On At By For From To Of And Or But If When Where While
With Without We Our Here There Then Thus Hence However Moreover Finally First Second Third Each Every
Such No Not One Two Three Let Write Take Consider Suppose Assume Choose Define Construct Compare Prove
Show Give Fix Use For After Before Under Over Over Section Theorem Proposition Lemma Definition Corollary
Remark Example Examples Question Questions Part Figure Table Proof Deciding Its Their Both Either Neither
Some Any All Only Also Even Since Because Although Though Unlike Like As Is Are Was Were Be Can Could May
Might Must Should Would Will Do Does Did Every Several Many More Most Other Another Same New Full Whole
January February March April May June July August September October November December Status Terms
Contents Next Read Show Find Introduced Related Why Where What Which Who How Established Working Failing
Stabilising Oscillating Remains None Earlier Later Now Today'''.split())


def visible_text(node):
    clone = BeautifulSoup(str(node), 'html.parser')
    for bad in clone.find_all(['script', 'style', 'annotation']):
        bad.decompose()
    return ' '.join(clone.get_text(' ').split())


def snippet(text, start, end, width=70):
    a = max(0, start - width)
    b = min(len(text), end + width)
    return ('…' if a else '') + text[a:b] + ('…' if b < len(text) else '')


def place_of(node):
    for parent in [node] + list(node.parents):
        if not isinstance(parent, Tag):
            continue
        if parent.get('data-card'):
            return 'card ' + parent['data-card']
        if parent.name == 'section' and parent.get('id') and (
                'chapter' in (parent.get('class') or []) or parent['id'] in ('status', 'terms')):
            return 'section ' + parent['id']
        if parent.name == 'header' and 'hero' in (parent.get('class') or []):
            return 'first screen'
        if parent.name in ('head', 'footer'):
            return parent.name
    return 'page'


def scan_leaks(page):
    found = []
    body = page.body
    for text in body.find_all(string=True):
        if isinstance(text, Comment):
            found.append(('comment', 'HTML comment', str(text)[:80], place_of(text.parent)))
            continue
        parents = [p.name for p in text.parents if isinstance(p, Tag)]
        if 'script' in parents or 'style' in parents:
            continue
        source = str(text)
        kind = 'TeX source' if 'annotation' in parents else ('formula' if 'math' in parents else 'text')
        for name, regex in LEAK_RE:
            if kind != 'text' and name in ('model or tool name', 'process word', 'question code'):
                continue
            for match in regex.finditer(source):
                found.append((name, kind, snippet(source, match.start(), match.end()), place_of(text.parent)))
    for node in page.find_all(True):
        if node.name in ('script', 'style'):
            continue
        for attr, value in node.attrs.items():
            if attr in ('style', 'property', 'encoding', 'xmlns'):
                continue
            values = value if isinstance(value, list) else [value]
            for item in values:
                if attr in ('href',) and str(item).startswith(('https://', 'http://', 'mailto:')):
                    continue
                if attr == 'content' and node.name == 'meta' and node.get('name') == 'viewport':
                    continue
                for name, regex in LEAK_RE:
                    if name in ('process word', 'model or tool name') and attr in ('class',):
                        continue
                    for match in regex.finditer(str(item)):
                        found.append((name, f'attribute {attr}', f'<{node.name} {attr}="{item}">'[:160],
                                      place_of(node)))
    head_text = ' '.join(page.head.get_text(' ').split()) if page.head else ''
    for node in page.head.find_all('meta') if page.head else []:
        head_text += ' ' + node.get('content', '')
    return found


def scan_fetches(page, markup):
    loads = []
    for node in page.find_all(True):
        for attr in ('src', 'srcset', 'poster', 'data'):
            if node.has_attr(attr):
                loads.append((node.name, attr, node[attr]))
        if node.name == 'link' and node.has_attr('href'):
            loads.append(('link ' + ' '.join(node.get('rel') or []), 'href', node['href']))
        if node.has_attr('style'):
            for url in re.findall(r'url\(([^)]+)\)', node['style']):
                loads.append((node.name, 'style url', url))
    for style in page.find_all('style'):
        css = style.get_text()
        for url in re.findall(r'url\(\s*([^)]+?)\s*\)', css):
            loads.append(('style', 'url', url[:80]))
        for url in re.findall(r'@import\s+([^;]+);', css):
            loads.append(('style', '@import', url))
    for script in page.find_all('script'):
        code = script.get_text()
        for call in re.findall(r'\b(fetch|XMLHttpRequest|sendBeacon|WebSocket|EventSource|importScripts|'
                               r'new Worker|import\()', code):
            loads.append(('script', 'call', call))
    out = []
    for element, attr, value in loads:
        value = str(value).strip('\'" ')
        if value.startswith('data:') or value.startswith('#'):
            continue
        host = re.match(r'https?://([^/]+)', value)
        allowed = bool(host) and host.group(1) in FONT_HOSTS and element.startswith('link')
        out.append({'element': element, 'attribute': attr, 'value': value[:120], 'allowed': allowed})
    return out


def candidates(page, wirer, cards):
    """Names in the report text that look like terms and have no card."""
    main = BeautifulSoup(str(page.find('main')), 'html.parser')
    for node in main.select('#terms, script, style, math, .term, dfn, nav, .tally'):
        node.decompose()
    emphasised = Counter()
    for node in main.find_all(['strong', 'em', 'b', 'i']):
        phrase = ' '.join(node.get_text(' ').split())
        if not phrase or phrase[-1] in '.:;,' or len(phrase.split()) > 5 or len(phrase) < 3:
            continue
        if wirer.ident(phrase) or wirer.ident(phrase.rstrip('s')):
            continue
        emphasised[phrase] += 1
    text = ' '.join(main.get_text(' ').split())
    names = Counter()
    for sentence in re.split(r'(?<=[.!?:;])\s+', text):
        words = sentence.split(' ')
        for i, word in enumerate(words):
            if i == 0:
                continue
            bare = word.strip('()[],.;:!?“”"\'’')
            if not bare or bare in CAPITAL_STOP:
                continue
            if re.fullmatch(r'[A-Z][a-z]+(?:[-–][A-Z][a-z]+)*', bare) or re.fullmatch(r'[A-Z]{2,6}', bare):
                if not wirer.ident(bare):
                    names[bare] += 1
    phrases = Counter()
    head = '|'.join(HEADS)
    for match in re.finditer(r'\b((?:[a-z][a-z-–]+ ){1,2}(?:%s))\b' % head, text):
        words = match.group(1).split()
        while words and words[0] in STOP:
            words = words[1:]
        if len(words) < 2:
            continue
        phrase = ' '.join(words)
        if wirer.ident(phrase):
            continue
        phrases[phrase] += 1
    return {
        'emphasised_without_card': emphasised.most_common(),
        'names_without_card': [(k, v) for k, v in names.most_common() if v >= 2],
        'phrases_without_card': [(k, v) for k, v in phrases.most_common() if v >= 4],
    }


RAW_NOTATION = re.compile(r'(?<![\w\\])(?:[A-Za-z]\w*_[A-Za-z0-9{(]|[A-Za-z)\]]\^[\w{(-]|\\[A-Za-z]{2,}|->|=>|<-)')


def raw_notation(page):
    """Mathematics typed as plain text (x_i, z^n, \\lambda, ->) outside any formula."""
    main = BeautifulSoup(str(page.find('main')), 'html.parser')
    for node in main.select('math, script, style, code'):
        node.decompose()
    found = []
    for text in main.find_all(string=True):
        source = str(text)
        for match in RAW_NOTATION.finditer(source):
            found.append((place_of(text.parent), snippet(source, match.start(), match.end(), 40)))
    return found


def card_audit(build):
    cards = build.cards
    rows = []
    by_text = defaultdict(list)
    for ident in cards.order:
        row = cards.by_id[ident]
        issues = []
        if not str(row.get('display_name') or '').strip():
            issues.append('no display_name')
        for field in ('definition', 'motivation', 'context'):
            tree = cards.trees.get((ident, field))
            if tree is None or not visible_text(tree):
                issues.append(f'empty {field}')
        related = row.get('related')
        if not isinstance(related, list) or not related:
            issues.append('no related terms')
        else:
            unknown = [r for r in related if r not in cards.by_id]
            if unknown:
                issues.append('related ids without a card: ' + ', '.join(map(str, unknown)))
        definition = cards.trees.get((ident, 'definition'))
        text = visible_text(definition) if definition is not None else ''
        words = len(text.split())
        if words > 180:
            issues.append(f'definition of {words} words (long for a card)')
        names = [n.casefold() for n in cards.names(ident)]
        if text and not any(n in text.casefold() for n in names):
            issues.append('definition does not name its term')
        for field in ('definition', 'motivation', 'context'):
            tree = cards.trees.get((ident, field))
            if tree is None:
                continue
            body = visible_text(tree)
            for match in POSITIONAL.finditer(body):
                issues.append(f'{field} depends on page position: “{snippet(body, match.start(), match.end(), 40)}”')
                break
            for match in REFERENCE.finditer(body):
                issues.append(f'{field} cites a numbered item: “{snippet(body, match.start(), match.end(), 40)}”')
                break
            for name, regex in LEAK_RE:
                for match in regex.finditer(body):
                    issues.append(f'{field} carries a {name}: “{match.group(0)}”')
                    break
        for pointer in build.pointers:
            if pointer['where'] == f'card {ident}':
                issues.append(f'points to an absent statement: “{pointer["text"]}”')
        if text:
            by_text[' '.join(text.split()).casefold()].append(ident)
        rows.append({'id': ident, 'display_name': cards.name(ident), 'words': words, 'issues': issues})
    shared = [ids for ids in by_text.values() if len(ids) > 1]
    for ids in shared:
        for row in rows:
            if row['id'] in ids:
                row['issues'].append('shares its definition with ' + ', '.join(i for i in ids if i != row['id']))
    return rows, shared


def weight(markup, page, compare=None):
    data = markup.encode('utf-8')
    total = len(data)
    packed = len(gzip.compress(data, 9))

    def size(pattern):
        return sum(len(m.encode('utf-8')) for m in re.findall(pattern, markup, re.S))

    font = sum(len(m) for m in re.findall(r'base64,([A-Za-z0-9+/=]+)', markup))
    parts = {
        'style (with the embedded math font)': size(r'<style>.*?</style>'),
        'embedded math font': font,
        'script': size(r'<script>.*?</script>'),
        'MathML': size(r'<math\b.*?</math>'),
        'TeX source inside MathML': size(r'<annotation\b.*?</annotation>'),
        'term cards (glossary)': size(r'<section[^>]*\bid="terms".*?</section>\s*</main>'),
        'status section': size(r'<section[^>]*\bid="status".*?</div></section>\s*<section'),
        'term links': size(r'<a class="term[^"]*"[^>]*>'),
    }
    report = {'bytes': total, 'gzip_bytes': packed, 'parts': parts}
    if compare:
        report['compare'] = compare
    return report


def listing(root, slug):
    hits = []
    for name in INDEXES:
        path = root / name
        if path.exists() and slug in path.read_text(encoding='utf-8', errors='replace'):
            hits.append(name)
    return hits


def run(build, markup, root, compare=None):
    page = BeautifulSoup(markup, 'html.parser')
    failures, notes = [], []
    robots = page.find('meta', attrs={'name': 'robots'})
    robots_ok = bool(robots and 'noindex' in robots.get('content', '') and 'nofollow' in robots.get('content', ''))
    if not robots_ok:
        failures.append('robots: the page lacks <meta name="robots" content="noindex, nofollow">')
    listed = listing(root, build.page['slug'])
    for name in listed:
        failures.append(f'listing: the page is named in {name}')
    fetches = scan_fetches(page, markup)
    for item in fetches:
        if not item['allowed']:
            failures.append(f'fetch: {item["element"]} {item["attribute"]} {item["value"]}')
    leaks = scan_leaks(page)
    leak_counts = Counter(name for name, _, _, _ in leaks)
    for name, count in leak_counts.items():
        if name in HARD_LEAKS or name == 'comment':
            failures.append(f'leak: {count} × {name}')
    ids = Counter(node['id'] for node in page.find_all(id=True))
    duplicate_ids = [k for k, v in ids.items() if v > 1]
    for k in duplicate_ids:
        failures.append(f'html: duplicate id {k}')
    broken = sorted({a['href'][1:] for a in page.find_all('a', href=True)
                     if a['href'].startswith('#') and len(a['href']) > 1 and a['href'][1:] not in ids})
    for k in broken:
        failures.append(f'html: in-page link to a missing id #{k}')
    card_rows, shared = card_audit(build)
    empty = Counter()
    for row in card_rows:
        for issue in row['issues']:
            if issue.startswith('empty ') or issue == 'no related terms' or issue == 'no display_name':
                empty[issue] += 1
            if issue.startswith('related ids without a card'):
                failures.append(f'cards: {row["id"]} {issue}')
    for issue, count in empty.items():
        failures.append(f'cards: {count} × {issue}')
    for problem, detail in build.problems:
        failures.append(f'input: {problem}: {detail}')
    for ident, text, where in build.unknown_terms:
        failures.append(f'terms: marked as a term without a card: “{text}” ({ident}, {where})')
    for text, where in build.uncarded_dfn:
        failures.append(f'terms: defined in the report without a card: “{text}” ({where})')
    if build.pointers:
        failures.append(f'words: {len(build.pointers)} pointers to statements the page does not contain')
    if build.attachments:
        failures.append(f'words: {len(build.attachments)} links to attached documents the page does not carry')
    if build.renderer.failed:
        failures.append(f'math: {len(build.renderer.failed)} TeX formulas failed to render')
    for item in build.missing_words:
        failures.append(f'words: missing {item}')
    long_titles = [i for i in build.board_items if i['words'] > 24]
    if long_titles:
        notes.append(f'{len(long_titles)} status items have titles over 24 words')
    long_bodies = [i for i in build.board_items if i.get('body_words', 0) > 45]
    if long_bodies:
        notes.append(f'{len(long_bodies)} status items have text over 45 words under their title')
    notation = raw_notation(page)
    if notation:
        notes.append(f'{len(notation)} places write mathematics as plain text outside a formula')
    status = build.status
    if status['state'] != 'settled':
        failures.append(f'status: the words are “{status["value"] or status["state"]}”, not settled')
    if status['date'] is None:
        failures.append('status: STATUS.md gives no date')
    found = candidates(page, build.wirer, build.cards)
    def shown(path):
        try:
            return str(path.resolve().relative_to(root))
        except ValueError:
            return str(path)

    return {
        'input': shown(build.folder),
        'report': shown(build.report_path),
        'status': {k: (str(v) if k == 'date' else v) for k, v in status.items()},
        'failures': failures,
        'notes': notes + build.warnings,
        'robots': robots_ok,
        'listed_in': listed,
        'fetches': fetches,
        'leaks': {'counts': dict(leak_counts), 'items': leaks},
        'cards': {'count': len(card_rows), 'rows': card_rows, 'shared_definitions': shared,
                  'issue_counts': dict(Counter(i.split(':')[0].split(' (')[0] if not i.startswith('definition of')
                                               else 'definition long for a card'
                                               for row in card_rows for i in row['issues']))},
        'terms': {'wired_links': build.wired, 'cards': len(build.cards.order),
                  'unknown_marked': build.unknown_terms, 'uncarded_definitions': build.uncarded_dfn,
                  **found},
        'words': {'pointers': build.pointers, 'attachments': build.attachments,
                  'external_links': build.external_links, 'relative_links': build.relative_links,
                  'tex_failures': build.renderer.failed, 'missing': build.missing_words},
        'status_board': {'counts': build.board_counts, 'long_titles': len(long_titles),
                         'long_bodies': len(long_bodies), 'items': len(build.board_items)},
        'raw_notation': notation,
        'weight': weight(markup, page, compare),
        'math_font': {'bytes': build.font_bytes, 'characters': getattr(build, 'font_chars', 0)},
    }


def text_report(result, limit=25):
    lines = []
    add = lines.append
    w = result['weight']
    add(f'Input: {result["input"]}')
    st = result['status']
    add(f'Words: {st["value"] or st["state"]} · date {st["date"]} · hashes in STATUS.md matching inputs: '
        f'{", ".join(st["hash_matches"]) or "none"}')
    add('')
    add(f'PAGE WEIGHT  {w["bytes"]:,} bytes · {w["gzip_bytes"]:,} bytes compressed (gzip -9)')
    for name, value in w['parts'].items():
        add(f'  {name:<40} {value:>12,}')
    if w.get('compare'):
        c = w['compare']
        add(f'  base page {c["path_name"]}: {c["bytes"]:,} bytes · {c["gzip_bytes"]:,} compressed')
    add('')
    add(f'ROBOTS  noindex, nofollow: {"yes" if result["robots"] else "NO"}')
    add(f'LISTING  named in: {", ".join(result["listed_in"]) or "none of " + ", ".join(INDEXES)}')
    add('')
    fetches = result['fetches']
    add(f'EXTERNAL FETCHES  {len(fetches)} ({sum(1 for f in fetches if not f["allowed"])} not allowed)')
    for f in fetches:
        add(f'  {"ok " if f["allowed"] else "NO "} {f["element"]} {f["attribute"]} {f["value"]}')
    add('')
    leaks = result['leaks']
    add(f'INTERNAL STRINGS  {len(leaks["items"])}')
    for name, count in sorted(leaks['counts'].items(), key=lambda kv: -kv[1]):
        add(f'  {count:>6} × {name}')
        shown = [i for i in leaks['items'] if i[0] == name][:6]
        for _, kind, text, where in shown:
            add(f'           {where} ({kind}): {text}')
    add('')
    t = result['terms']
    add(f'TERMS  {t["cards"]} cards · {t["wired_links"]:,} term links in the page')
    add(f'  marked as a term, no card: {len(t["unknown_marked"])}')
    for ident, text, where in t['unknown_marked'][:limit]:
        add(f'    “{text}” → {ident} ({where})')
    add(f'  defined in the report (<dfn>), no card: {len(t["uncarded_definitions"])}')
    for text, where in t['uncarded_definitions'][:limit]:
        add(f'    “{text}” ({where})')
    add(f'  emphasised (bold or italic) in the report, no card: {len(t["emphasised_without_card"])} distinct')
    add('    ' + '; '.join(f'{k} ({v})' for k, v in t['emphasised_without_card'][:limit]))
    add(f'  capitalised names and acronyms used twice or more, no card: {len(t["names_without_card"])} distinct')
    add('    ' + '; '.join(f'{k} ({v})' for k, v in t['names_without_card'][:limit]))
    add(f'  technical phrases used four times or more, no card: {len(t["phrases_without_card"])} distinct')
    add('    ' + '; '.join(f'{k} ({v})' for k, v in t['phrases_without_card'][:limit]))
    add('')
    c = result['cards']
    add(f'CARDS  {c["count"]}')
    for issue, count in sorted(c['issue_counts'].items(), key=lambda kv: -kv[1]):
        add(f'  {count:>5} × {issue}')
    add(f'  shared definitions: {len(c["shared_definitions"])} groups covering '
        f'{sum(len(g) for g in c["shared_definitions"])} cards')
    add('')
    wd = result['words']
    add(f'WORDS THE PAGE STILL NEEDS')
    add(f'  pointers to statements the page does not contain: {len(wd["pointers"])}')
    for p in wd['pointers'][:8]:
        add(f'    {p["where"]}: “{p["text"]}”')
    add(f'  links to attached documents the page does not carry: {len(wd["attachments"])}')
    for p in wd['attachments'][:limit]:
        add(f'    {p["where"]}: “{p["text"]}”')
    add(f'  TeX formulas that failed to render: {len(wd["tex_failures"])}')
    for item in wd['missing']:
        add(f'  missing: {item}')
    add(f'  external links (kept): {len(wd["external_links"])}')
    add(f'  mathematics written as plain text outside a formula: {len(result["raw_notation"])}')
    for where, text in result['raw_notation'][:6]:
        add(f'    {where}: {text}')
    sb = result['status_board']
    add('')
    add('STATUS BOARD  ' + ' · '.join(f'{k} {v}' for k, v in sb['counts'].items()) +
        f' · titles over 24 words: {sb["long_titles"]} · text over 45 words: {sb["long_bodies"]}')
    mf = result['math_font']
    add(f'MATH FONT  {mf["bytes"]:,} bytes for {mf["characters"]} characters')
    add('')
    add(f'FAILURES  {len(result["failures"])}')
    for f in result['failures'][:60]:
        add(f'  {f}')
    if len(result['failures']) > 60:
        add(f'  … and {len(result["failures"]) - 60} more (see audit.json)')
    if result['notes']:
        add('')
        add('NOTES')
        for n in result['notes'][:30]:
            add(f'  {n}')
    return '\n'.join(lines) + '\n'
