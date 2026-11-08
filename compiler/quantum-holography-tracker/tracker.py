"""Build the tracker page from an input folder.

The page is one HTML file. Its parts come from three inputs:

    words/REPORT.html or words/REPORT.md   the report, with its hero and status section
    words/STATUS.md                        whether the words are settled, and their date
    cards/TERMS.json                       the term cards
    words/OPENING.md                       optional: the title, the subject, the breakthroughs,
                                           the decisive obstructions and the open problems
    cards/OPENING-TERMS.json               optional: cards for the opening (they win on a shared id)
    words/LABELS.json                      optional: the writer's names for the page's labels

and from the chrome in content/quantum-holography-tracker/page.json. Mathematics written in
TeX is rendered to MathML here, so the page needs no renderer. Every term with a card is
linked wherever it appears; the card opens on hover, tap or keyboard focus.
"""
import base64
import datetime as dt
import hashlib
import html
import io
import json
import re
import shutil
import subprocess
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

HERE = Path(__file__).resolve().parent
STATE_ALIASES = {'stabilizing': 'stabilising', 'open': 'remains', 'remaining': 'remains',
                 'what remains': 'remains', 'established': 'established'}
HEADING = re.compile(r'^h[1-6]$')
# Text inside these elements is never linked to a card.
NO_WIRE = {'a', 'code', 'pre', 'math', 'script', 'style', 'summary', 'button', 'h1', 'dfn',
           'kbd', 'samp', 'svg', 'textarea', 'select', 'option', 'label', 'annotation', 'title'}
# Text inside these elements is never read as TeX.
NO_TEX = {'math', 'code', 'pre', 'script', 'style', 'annotation', 'svg', 'textarea', 'title'}
TEX = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]', re.S)
HTMLISH = re.compile(r'<\s*(p|div|span|em|strong|b|i|math|ul|ol|li|a|br|sup|sub|dfn|table|section)\b', re.I)
CARD_ID = re.compile(r'^[a-z0-9][a-z0-9-]*$')
KEEP_DATA = {'data-term', 'data-state', 'data-card'}
# The opening's parts, recognised by their headings (or by data-role).
OPENING = (
    ('subject', re.compile(r'^(?:the )?subject$')),
    ('breakthroughs', re.compile(r'^(?:the )?(?:main |central )?breakthroughs?$')),
    ('obstructions', re.compile(r'^(?:the )?(?:decisive )?(?:obstructions|no-go results)$')),
    ('open-problems', re.compile(r'^(?:the )?open (?:problems|questions)$')),
)
OBSTRUCTIONS = dict(OPENING)['obstructions']
# The labelled lines of a breakthrough or obstruction, as the writer may name them.
# "Checked" and "Builds on" are optional: a check the writer records, and the items or
# sections an item builds on (drawn as arrows in the map of results).
LINE_KEYS = (
    ('achieved', re.compile(r'^(?:achieved|result|rules out)$')),
    ('why', re.compile(r'^why it matters$')),
    ('domain', re.compile(r'^(?:domain(?: and hypotheses)?|hypotheses|status|holds on)$')),
    ('proved', re.compile(r'^(?:proved in|source|sources|proof)$')),
    ('checked', re.compile(r'^(?:checked|checked by|checked in|independently checked|verified|verified by)$')),
    ('builds', re.compile(r'^(?:builds on|uses|depends on|relies on|extends|requires)$')),
    ('read', re.compile(r'^read (?:more|on)$')),
)
LINE_NAMES = {'achieved': 'Achieved', 'why': 'Why it matters', 'domain': 'Domain and hypotheses',
              'proved': 'Proved in', 'checked': 'Checked', 'builds': 'Builds on', 'read': 'Read more'}
# A status is shown only when the writer's own label states it: "Proved in" (or "Proof")
# gives Proved, a "Checked" line gives Checked, and an open problem is Open.
PROVED_LABEL = re.compile(r'^(?:proved in|proof)$')
# Section references in a "Proved in" line: §10.1, §§80.2–80.4, §§10.1 and 10.5, §§1–6.
# (The patterns write § as \u00a7 and the en dash as \u2013, which the regular expression reads.)
SECTION_RUN = re.compile(r'(\u00a7\u00a7?)\s*((?:\d+(?:\.\d+)*)(?:\s*[\u2013-]\s*\d+(?:\.\d+)*)?'
                         r'(?:\s*(?:,|and|&)\s*(?:\d+(?:\.\d+)*)(?:\s*[\u2013-]\s*\d+(?:\.\d+)*)?)*)')
SECTION_PIECE = re.compile(r'\d+(?:\.\d+)*(?:\s*[\u2013-]\s*\d+(?:\.\d+)*)?')
RANK = re.compile(r'^\s*(\d{1,2})[.)]\s+')
PUNCT_AFTER_MATH = re.compile(r'^[,.;:!?)\]\u2019\u201d]+')


def parse(markup):
    return BeautifulSoup(markup, 'html.parser')


def text_of(node):
    clone = parse(str(node))
    for note in clone.find_all('annotation'):
        note.decompose()
    return ' '.join(clone.get_text(' ').split())


def slugify(text, fallback='section'):
    value = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:64].strip('-')
    return value or fallback


def pandoc(markdown, warnings, mathml=False):
    """Markdown to an HTML fragment. TeX stays in <span class="math"> unless mathml is set."""
    command = ['pandoc', '--from=markdown+tex_math_single_backslash', '--to=html5', '--wrap=none']
    # MathJax mode keeps each formula's TeX intact inside its span; the build renders it.
    command.append('--mathml' if mathml else '--mathjax')
    result = subprocess.run(command, input=markdown, text=True, capture_output=True)
    if result.returncode != 0:
        raise SystemExit('pandoc failed:\n' + result.stderr)
    for line in result.stderr.splitlines():
        if line.strip():
            warnings.append('pandoc: ' + line.strip())
    return result.stdout


class TexRenderer:
    """Collect TeX from many places, render it in one pandoc run, then put it back."""

    def __init__(self):
        self.items, self.out, self.failed = [], [], []

    def add(self, tex, display):
        self.items.append((re.sub(r'\n\s*\n', '\n', tex.strip()), display))
        return len(self.items) - 1

    def collect(self, root, where):
        jobs = []
        # Pandoc marks math it could not convert as <span class="math inline|display">.
        for span in root.find_all('span', class_='math'):
            if span.find('math') is not None:
                continue
            source = span.get_text().strip()
            display = 'display' in (span.get('class') or [])
            for left, right in (('$$', '$$'), ('\\[', '\\]'), ('\\(', '\\)'), ('$', '$')):
                if source.startswith(left) and source.endswith(right) and len(source) > len(left) + len(right):
                    source = source[len(left):-len(right)]
                    display = display or left in ('$$', '\\[')
                    break
            placeholder = NavigableString('')
            span.replace_with(placeholder)
            jobs.append((placeholder, [(self.add(source, display), where)]))
        for text in list(root.find_all(string=True)):
            if isinstance(text, Comment) or ('\\(' not in text and '\\[' not in text):
                continue
            if any(isinstance(p, Tag) and p.name in NO_TEX for p in text.parents):
                continue
            pieces, last = [], 0
            for match in TEX.finditer(str(text)):
                pieces.append(str(text)[last:match.start()])
                display = match.group(2) is not None
                pieces.append((self.add(match.group(2) if display else match.group(1), display), where))
                last = match.end()
            if len(pieces) > 1:
                pieces.append(str(text)[last:])
                jobs.append((text, pieces))
        return jobs

    def run(self, warnings):
        """Render with Temml; formulas Temml rejects go to pandoc; the rest are reported."""
        if not self.items:
            return
        rendered = [None] * len(self.items)
        script = HERE / 'tex2mathml.cjs'
        node = shutil.which('node')
        if node and script.exists():
            payload = json.dumps([{'tex': tex, 'display': display} for tex, display in self.items])
            result = subprocess.run([node, str(script)], input=payload, text=True, capture_output=True)
            if result.returncode == 0:
                for i, row in enumerate(json.loads(result.stdout)):
                    if 'html' in row:
                        rendered[i] = row['html']
                    else:
                        warnings.append('temml: ' + row['error'][:160])
            else:
                warnings.append('temml did not run: ' + result.stderr.strip()[:200])
        else:
            warnings.append('node or the TeX renderer is missing; pandoc renders all TeX')
        rest = [i for i, value in enumerate(rendered) if value is None]
        if rest:
            blocks = []
            for i in rest:
                tex, display = self.items[i]
                blocks.append(f'::: {{#qhm{i}}}\n' + ('\\[' if display else '\\(') + tex +
                              ('\\]' if display else '\\)') + '\n:::\n')
            out = parse(pandoc('\n'.join(blocks), warnings, mathml=True))
            for i in rest:
                div = out.find(id=f'qhm{i}')
                math = div.find('math') if div else None
                if math is not None:
                    rendered[i] = str(math)
        for i, (tex, display) in enumerate(self.items):
            if rendered[i] is None:
                self.failed.append(tex)
                rendered[i] = f'<code class="tex">{html.escape(tex)}</code>'
        self.out = rendered

    def apply(self, jobs):
        for text, pieces in jobs:
            nodes = []
            for piece in pieces:
                if isinstance(piece, tuple):
                    nodes.extend(list(parse(self.out[piece[0]]).contents))
                elif piece:
                    nodes.append(NavigableString(piece))
            text.replace_with(*nodes)


def parse_status(path, digests):
    text = path.read_text(encoding='utf-8') if path.exists() else ''
    line = re.search(r'^\s*(?:status|state)\s*:\s*(.+)$', text, re.I | re.M)
    value = line.group(1).strip() if line else (text.strip().splitlines() or [''])[0]
    lowered = value.lower()
    if re.match(r'settled\b', lowered):
        state = 'settled'
    elif re.match(r'draft\b', lowered):
        state = 'draft'
    else:
        state = (lowered.split() or ['missing'])[0]
    date = None
    dated = re.search(r'^\s*date\s*:\s*(\d{4}-\d{2}-\d{2})', text, re.I | re.M) or \
        re.search(r'\b(\d{4}-\d{2}-\d{2})\b', text)
    if dated:
        date = dt.date.fromisoformat(dated.group(1))
    else:
        worded = re.search(r'\b(\d{1,2}) (January|February|March|April|May|June|July|August|'
                           r'September|October|November|December) (\d{4})\b', text)
        if worded:
            date = dt.datetime.strptime(' '.join(worded.groups()), '%d %B %Y').date()
    hashes = sorted(set(re.findall(r'\b[0-9a-f]{12,64}\b', text)))
    matched = sorted({name for h in hashes for name, digest in digests.items() if digest.startswith(h)})
    return {'path': str(path), 'state': state, 'value': value, 'date': date,
            'hashes': hashes, 'hash_matches': matched, 'digests': digests}


def long_date(day):
    return f'{day.day} {day.strftime("%B %Y")}'


class Cards:
    """The term cards, with each field as parsed HTML."""

    def __init__(self, rows, renderer, warnings, problems):
        self.rows, self.by_id, self.order = rows, {}, []
        self.fields = {}
        markdown_jobs = []
        for index, row in enumerate(rows):
            ident = str(row.get('id', '')).strip()
            if not CARD_ID.match(ident):
                problems.append(('card id is not a lowercase slug', ident or f'#{index}'))
            if ident in self.by_id:
                problems.append(('duplicate card id', ident))
                continue
            self.by_id[ident] = row
            self.order.append(ident)
            for field in ('definition', 'motivation', 'context'):
                value = row.get(field) or ''
                if not isinstance(value, str):
                    problems.append((f'{field} is not a string', ident))
                    value = ''
                if value.strip() and not HTMLISH.search(value):
                    markdown_jobs.append((ident, field, value))
                else:
                    self.fields[(ident, field)] = value
        if markdown_jobs:
            blocks = [f'::: {{#qhf{i}}}\n{value}\n:::\n' for i, (_, _, value) in enumerate(markdown_jobs)]
            out = parse(pandoc('\n'.join(blocks), warnings))
            for i, (ident, field, _) in enumerate(markdown_jobs):
                div = out.find(id=f'qhf{i}')
                self.fields[(ident, field)] = div.decode_contents() if div else ''
        self.trees, self.tex_jobs = {}, []
        for key, value in self.fields.items():
            tree = parse(value)
            self.tex_jobs += renderer.collect(tree, f'card {key[0]} {key[1]}')
            self.trees[key] = tree

    def name(self, ident):
        return str(self.by_id[ident].get('display_name') or ident)

    def names(self, ident):
        row = self.by_id[ident]
        values = [row.get('display_name') or ''] + list(row.get('aliases') or [])
        return [v for v in values if isinstance(v, str) and v.strip()]


def plural_forms(name):
    forms = {name}
    lower = name.lower()
    irregular = {'um': 'a', 'us': 'i', 'eaf': 'eaves', 'ix': 'ices', 'ex': 'ices'}
    for ending, replacement in irregular.items():
        if lower.endswith(ending) and ending in ('um', 'us', 'eaf'):
            forms.add(name[:-len(ending)] + replacement)
    if re.search(r'[^aeiou]y$', lower):
        forms.add(name[:-1] + 'ies')
    elif re.search(r'(s|x|z|ch|sh)$', lower):
        forms.add(name + 'es')
    else:
        forms.add(name + 's')
    return forms


class Wirer:
    """Find every use of a card's name and link it to the card."""

    def __init__(self, cards, problems):
        self.cards = cards
        self.lookup = {}
        patterns = []
        for ident in cards.order:
            for name in cards.names(ident):
                for form in plural_forms(name.strip()):
                    key = self.key(form)
                    if key in self.lookup and self.lookup[key] != ident:
                        problems.append(('two cards share a name',
                                         f'“{" ".join(form.split())}”: {self.lookup[key]}, {ident}'))
                        continue
                    self.lookup[key] = ident
                    patterns.append(form)
        patterns.sort(key=len, reverse=True)
        body = '|'.join(''.join('[-‐–]' if ch in '-‐–' else re.escape(ch) for ch in p) for p in patterns)
        self.regex = re.compile(r'(?<![\w\-‐–])(' + body + r')(?![\w\-‐–])', re.I) if body else None

    @staticmethod
    def key(text):
        return re.sub(r'[-‐–]', '-', ' '.join(text.split())).casefold()

    def ident(self, text):
        return self.lookup.get(self.key(text))

    def wire(self, root, scope_of, skip=(), first_only=False, seen=None):
        """Link names inside root. scope_of(node) names the scope for 'first use'."""
        if self.regex is None:
            return 0
        seen = set() if seen is None else seen
        count = 0
        for text in list(root.find_all(string=True)):
            if isinstance(text, Comment) or not text.strip():
                continue
            blocked = False
            for parent in text.parents:
                if not isinstance(parent, Tag):
                    continue
                if parent.name in NO_WIRE or parent.has_attr('data-term') or \
                        parent.has_attr('data-no-terms') or \
                        (parent.name in ('em', 'i', 'cite') and looks_like_title(parent.get_text())):
                    blocked = True
                    break
            if blocked:
                continue
            source = str(text)
            matches = list(self.regex.finditer(source))
            if not matches:
                continue
            scope = scope_of(text)
            nodes, last = [], 0
            for match in matches:
                ident = self.ident(match.group(1))
                if ident is None or ident in skip:
                    continue
                again = (scope, ident) in seen
                if again and first_only:
                    continue
                seen.add((scope, ident))
                nodes.append(NavigableString(source[last:match.start()]))
                link = Tag(name='a', attrs={'class': 'term again' if again else 'term',
                                            'href': f'#term-{ident}', 'data-term': ident})
                if again:
                    link['tabindex'] = '-1'
                link.string = match.group(1)
                nodes.append(link)
                last = match.end()
                count += 1
            if nodes:
                nodes.append(NavigableString(source[last:]))
                text.replace_with(*nodes)
        return count


def looks_like_title(text):
    """An italic work title (for example a cited paper): three or more words, every word of four or
    more letters capitalised. Term names inside a cited title are not linked to cards."""
    words = re.findall(r"[A-Za-z][A-Za-z'’-]*", text)
    long_words = [w for w in words if len(w) >= 4]
    return len(words) >= 3 and bool(long_words) and all(w[0].isupper() for w in long_words)


def wrap_display_math(root):
    """Each display formula sits in its own horizontal scroller, so a wide one never widens the page."""
    for math in root.find_all('math', attrs={'display': 'block'}):
        if 'math-wrap' not in (math.parent.get('class') or []):
            math.wrap(Tag(name='span', attrs={'class': 'math-wrap'}))


def keep_punctuation(root):
    """Punctuation after an inline formula stays on the formula's line."""
    for math in root.find_all('math'):
        if math.get('display') == 'block' or (math.parent is not None and 'nobr' in (math.parent.get('class') or [])):
            continue
        after = math.next_sibling
        if not isinstance(after, NavigableString) or isinstance(after, Comment):
            continue
        found = PUNCT_AFTER_MATH.match(str(after))
        if not found:
            continue
        rest = str(after)[found.end():]
        span = Tag(name='span', attrs={'class': 'nobr'})
        math.replace_with(span)
        span.append(math)
        span.append(NavigableString(found.group(0)))
        after.replace_with(NavigableString(rest)) if rest else after.extract()


def subset_math_font(markup, font_path):
    """A subset of the OpenType math font holding the characters the page's MathML uses."""
    from fontTools import subset
    from fontTools.ttLib import TTFont
    chars = set('0123456789+−-=()[]{}|/,.;:!?<>*′″√')
    for match in re.finditer(r'<(mi|mo|mn|mtext|ms)\b[^>]*>(.*?)</\1>', markup, re.S):
        chars.update(html.unescape(re.sub(r'<[^>]+>', '', match.group(2))))
    chars = {c for c in chars if not c.isspace()}
    font = TTFont(str(font_path))
    options = subset.Options()
    options.layout_features = ['*']
    options.flavor = 'woff'
    options.with_zopfli = False
    options.name_IDs = ['*']
    options.notdef_outline = True
    options.glyph_names = False
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=[ord(c) for c in chars])
    subsetter.subset(font)
    buffer = io.BytesIO()
    font.flavor = 'woff'
    font.save(buffer)
    return buffer.getvalue(), len(chars)


GLYPHS = {
    'established': '<circle cx="8" cy="8" r="6" fill="currentColor"/>',
    'working': '<circle cx="8" cy="8" r="5.6" fill="none" stroke="currentColor" stroke-width="1.5"/>'
               '<path d="M8 2.4a5.6 5.6 0 0 1 0 11.2z" fill="currentColor"/>',
    'failing': '<circle cx="8" cy="8" r="5.6" fill="none" stroke="currentColor" stroke-width="1.5"/>'
               '<path d="M4.3 11.7 11.7 4.3" stroke="currentColor" stroke-width="1.5"/>',
    'stabilising': '<circle cx="8" cy="8" r="5.6" fill="none" stroke="currentColor" stroke-width="1.5"/>'
                   '<circle cx="8" cy="8" r="2.4" fill="currentColor"/>',
    'oscillating': '<circle cx="8" cy="8" r="5.6" fill="none" stroke="currentColor" stroke-width="1.5"/>'
                   '<path d="M4.4 8c.9-2.2 2.1-2.2 3 0s2.1 2.2 3.2 0" fill="none" stroke="currentColor" '
                   'stroke-width="1.4" stroke-linecap="round"/>',
    'remains': '<circle cx="8" cy="8" r="5.6" fill="none" stroke="currentColor" stroke-width="1.5"/>',
}


# Status marks. Each status has its own shape as well as its own colour.
GLYPHS.update({
    'proved': '<circle cx="8" cy="8" r="5.2" fill="currentColor"/>',
    'checked': '<circle cx="8" cy="8" r="5.6" fill="none" stroke="currentColor" stroke-width="1.5"/>'
               '<path d="M5.2 8.3 7.2 10.2 10.9 6" fill="none" stroke="currentColor" stroke-width="1.6" '
               'stroke-linecap="round" stroke-linejoin="round"/>',
    'open': '<circle cx="8" cy="8" r="5.2" fill="none" stroke="currentColor" stroke-width="1.5"/>',
    'theorem': '<rect x="3.6" y="3.6" width="8.8" height="8.8" rx="1" fill="currentColor"/>',
})

# Interface icons, drawn inline.
ICONS = {
    'search': '<circle cx="7" cy="7" r="4.6" fill="none" stroke="currentColor" stroke-width="1.5"/>'
              '<path d="m10.4 10.4 3.6 3.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
    'theme': '<circle cx="8" cy="8" r="5.6" fill="none" stroke="currentColor" stroke-width="1.4"/>'
             '<path d="M8 2.4a5.6 5.6 0 0 1 0 11.2z" fill="currentColor"/>',
    'contents': '<path d="M2.5 4.5h11M2.5 8h11M2.5 11.5h7" stroke="currentColor" stroke-width="1.5" '
                'stroke-linecap="round"/>',
    'arrow': '<path d="M3 8h9.2M8.8 4.4 12.4 8l-3.6 3.6" fill="none" stroke="currentColor" stroke-width="1.4" '
             'stroke-linecap="round" stroke-linejoin="round"/>',
}


def icon(name, cls='icon'):
    return (f'<svg class="{cls}" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
            f'{ICONS[name]}</svg>')


def glyph(state):
    return (f'<svg class="glyph" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
            f'<use href="#g-{state}"/></svg>')


def section_runs(text):
    """The section references in a citation, in order: ['10.1', '10.5', '80.2–80.4']."""
    refs = []
    for run in SECTION_RUN.finditer(text):
        for piece in SECTION_PIECE.findall(run.group(2)):
            piece = re.sub(r'\s*[–-]\s*', '–', piece)
            if piece not in refs:
                refs.append(piece)
    return refs


def source_brief(value_html):
    """The works and section numbers a "Proved in" line cites, as [(title html, [refs])].

    A work is an italic or cited title; the section numbers that follow it belong to it.
    The brief drops the line's qualifying words, which the full line keeps; it returns
    an empty list when the line names no section of an italic work.
    """
    tree = parse(value_html)
    works, current = [], None
    for node in tree.descendants:
        if isinstance(node, Tag) and node.name in ('em', 'i', 'cite') and \
                not any(isinstance(p, Tag) and p.name in ('em', 'i', 'cite') for p in node.parents):
            current = {'title': node.decode_contents(), 'refs': []}
            works.append(current)
        elif isinstance(node, NavigableString) and not isinstance(node, Comment):
            if any(isinstance(p, Tag) and p.name in ('em', 'i', 'cite') for p in node.parents):
                continue
            if current is not None:
                current['refs'] += [r for r in section_runs(str(node)) if r not in current['refs']]
    return [(w['title'], w['refs']) for w in works if w['refs']]


def brief_html(works):
    parts = []
    for title, refs in works:
        sign = '§§' if len(refs) > 1 or any('–' in r for r in refs) else '§'
        parts.append(f'<span class="src-work"><cite>{title}</cite> '
                     f'<span class="src-refs">{sign}{", ".join(refs)}</span></span>')
    return '<span class="src-sep">; </span>'.join(parts)


def symbols():
    return ('<svg class="symbols" aria-hidden="true" focusable="false"><defs>' +
            ''.join(f'<symbol id="g-{k}" viewBox="0 0 16 16">{v}</symbol>' for k, v in GLYPHS.items()) +
            '</defs></svg>')


class Build:
    def __init__(self, folder, page, math_font=None):
        self.folder = Path(folder)
        self.page = page
        self.labels = dict(page['labels'])
        self.states = [s['id'] for s in page['states']]
        self.state_label = {s['id']: s['label'] for s in page['states']}
        self.hidden_states, self.show_next, self.label_overrides = set(), True, {}
        self.opening, self.ranked, self.ranked_items, self.ranked_issues = {}, {}, [], []
        self.opening_sections, self.opening_doc, self.opening_path = [], None, None
        self.has_board = True
        self.math_font = math_font
        self.warnings, self.problems = [], []
        self.pointers, self.attachments, self.external_links = [], [], []
        self.unknown_terms, self.uncarded_dfn, self.relative_links = [], [], []
        self.defining = {}
        self.missing_words = []
        self.open_part = None
        self.statement_index = {}   # section id -> [{'id', 'kind', 'proof'}]
        self.section_number = {}    # section id -> its number in the contents
        self.id_section = {}        # any id inside a chapter -> the chapter's id
        self.results, self.problems_open, self.result_groups = [], [], []
        self.map_notes = []

    # ---------------------------------------------------------------- inputs
    def read(self):
        words, cards_dir = self.folder / 'words', self.folder / 'cards'
        report_html, report_md = words / 'REPORT.html', words / 'REPORT.md'
        if report_html.exists() and report_md.exists():
            self.warnings.append('both REPORT.html and REPORT.md exist; REPORT.html is used')
        if report_html.exists():
            self.report_path = report_html
            markup = report_html.read_text(encoding='utf-8')
        elif report_md.exists():
            self.report_path = report_md
            markup = pandoc(report_md.read_text(encoding='utf-8'), self.warnings)
        else:
            raise SystemExit(f'no words/REPORT.html or words/REPORT.md in {self.folder}')
        terms_path = cards_dir / 'TERMS.json'
        if not terms_path.exists():
            raise SystemExit(f'no cards/TERMS.json in {self.folder}')
        terms_bytes = terms_path.read_bytes()
        rows = json.loads(terms_bytes)
        if not isinstance(rows, list):
            raise SystemExit('cards/TERMS.json must hold a list of card objects')
        report_bytes = self.report_path.read_bytes()
        digests = {
            self.report_path.name: hashlib.sha256(report_bytes).hexdigest(),
            'TERMS.json': hashlib.sha256(terms_bytes).hexdigest(),
            self.report_path.name + '+TERMS.json': hashlib.sha256(report_bytes + terms_bytes).hexdigest(),
        }
        # The opening: its own words and cards. An opening card replaces a card with the same id.
        opening_html, opening_md = words / 'OPENING.html', words / 'OPENING.md'
        opening_markup = None
        if opening_html.exists():
            self.opening_path = opening_html
            opening_markup = opening_html.read_text(encoding='utf-8')
        elif opening_md.exists():
            self.opening_path = opening_md
            opening_markup = pandoc(opening_md.read_text(encoding='utf-8'), self.warnings)
        if self.opening_path is not None:
            digests[self.opening_path.name] = hashlib.sha256(self.opening_path.read_bytes()).hexdigest()
        opening_cards = cards_dir / 'OPENING-TERMS.json'
        if opening_cards.exists():
            extra_bytes = opening_cards.read_bytes()
            digests['OPENING-TERMS.json'] = hashlib.sha256(extra_bytes).hexdigest()
            extra = json.loads(extra_bytes)
            if not isinstance(extra, list):
                raise SystemExit('cards/OPENING-TERMS.json must hold a list of card objects')
            at = {str(row.get('id', '')).strip(): i for i, row in enumerate(rows) if isinstance(row, dict)}
            rows = list(rows)
            for row in extra:
                ident = str(row.get('id', '')).strip() if isinstance(row, dict) else ''
                if ident in at:
                    rows[at[ident]] = row
                else:
                    at[ident] = len(rows)
                    rows.append(row)
        self.status = parse_status(words / 'STATUS.md', digests)
        self.read_labels(words / 'LABELS.json')
        self.renderer = TexRenderer()
        self.cards = Cards(rows, self.renderer, self.warnings, self.problems)
        self.doc = parse(markup)
        self.report_tex = self.renderer.collect(self.doc, 'report')
        if opening_markup is not None:
            self.opening_doc = parse(opening_markup)
            self.report_tex += self.renderer.collect(self.opening_doc, 'opening')
        self.renderer.run(self.warnings)
        self.renderer.apply(self.report_tex)
        self.renderer.apply(self.cards.tex_jobs)

    # ---------------------------------------------------------- structure
    def structure(self):
        doc = self.doc
        hero = doc.find(attrs={'data-role': 'hero'})
        status = doc.find(attrs={'data-role': 'status'})
        if hero is not None:
            hero.extract()
        if status is not None:
            status.extract()
        if hero is None:
            hero = self.plain_hero(doc)
        if self.opening_doc is not None:
            # The opening replaces the report's title lines and its status board.
            odoc = self.opening_doc
            ohero = odoc.find(attrs={'data-role': 'hero'})
            ohero = ohero.extract() if ohero is not None else self.opening_hero(odoc)
            hero, status, self.has_board = ohero, None, False
            self.take_opening(odoc, rest=True)
        else:
            self.take_opening(doc, rest=False)
        self.hero, self.status_el = hero, status
        for node in doc.find_all(attrs={'data-role': 'eyebrow'}):
            node['class'] = ['eyebrow']
        sections, loose = [], []
        for node in list(doc.contents):
            if isinstance(node, Tag) and node.name == 'section':
                if loose:
                    sections.append(self.wrap(loose))
                    loose = []
                sections.append(node)
            elif isinstance(node, Tag) or (isinstance(node, NavigableString) and node.strip()
                                            and not isinstance(node, Comment)):
                if isinstance(node, Tag) and node.name in ('h1', 'h2') and loose:
                    sections.append(self.wrap(loose))
                    loose = []
                loose.append(node)
        if loose:
            sections.append(self.wrap(loose))
        for section in sections:
            if self.plain_status(section) is not None:
                if self.status_el is None and self.has_board:
                    self.status_el = self.plain_status(section)
                sections.remove(section)
                break
        self.sections = self.opening_sections + sections

    def wrap(self, nodes):
        """Loose report content becomes a section; the section takes its heading's id and label."""
        section = Tag(name='section')
        first = nodes[0] if nodes else None
        if isinstance(first, Tag) and HEADING.match(first.name or ''):
            for attr in ('id', 'data-toc'):
                if first.has_attr(attr):
                    section[attr] = first[attr]
                    del first[attr]
        for node in nodes:
            section.append(node.extract())
        return section

    def plain_hero(self, doc):
        """Without a marked hero: the first <h1> is the title and a short paragraph after it the dek."""
        hero = parse('<header data-role="hero"></header>').header
        title = doc.find('h1')
        if title is None:
            return hero
        follower = title.find_next_sibling(True)
        hero.append(title.extract())
        for role in ('dek', 'state'):
            if follower is None or follower.name != 'p' or len(text_of(follower).split()) > 45:
                break
            following = follower.find_next_sibling(True)
            follower['data-role'] = role
            hero.append(follower.extract())
            follower = following
        return hero

    STATE_WORDS = {'established': 'established', 'working': 'working', 'failing': 'failing',
                   'stabilising': 'stabilising', 'stabilizing': 'stabilising', 'oscillating': 'oscillating',
                   'remains': 'remains', 'what remains': 'remains', 'open': 'remains', 'remaining': 'remains'}

    def state_heading(self, node):
        if not isinstance(node, Tag) or not HEADING.match(node.name or ''):
            return None
        return self.STATE_WORDS.get(text_of(node).strip(' .:').lower())

    def plain_status(self, section):
        """A section whose headings name two or more states is the status section.

        Under each state heading, each list item, sub-heading or paragraph is one item. An item's
        title is its bold lead or its sub-heading; otherwise its whole text is the title. Text
        that begins "Next:" is the item's next step.
        """
        headings = [h for h in section.find_all(HEADING) if self.state_heading(h)]
        if len(headings) < 2:
            return None
        board = parse('<section data-role="status"><ol data-role="board"></ol></section>').section
        out = board.find('ol')
        first = section.find(HEADING)
        if first is not None and first not in headings:
            lead = parse(str(first)).find(HEADING)
            lead.name = 'h2'
            board.insert(0, lead)
            dek = first.find_next_sibling(True)
            if dek is not None and dek.name == 'p' and dek.find_next_sibling(True) in headings:
                copy = parse(str(dek)).p
                copy['data-role'] = 'dek'
                board.insert(1, copy)
        definitions = parse('<dl data-role="states"></dl>').dl
        for heading in headings:
            state = self.state_heading(heading)
            level = int(heading.name[1])
            node = heading.find_next_sibling(True)
            if node is not None and node.name == 'p':
                parts = [c for c in node.contents if not (isinstance(c, NavigableString) and not c.strip())]
                if len(parts) == 1 and isinstance(parts[0], Tag) and parts[0].name in ('em', 'i'):
                    definitions.append(parse(f'<dt data-state="{state}">{text_of(heading)}</dt>'))
                    definitions.append(parse(f'<dd>{parts[0].decode_contents()}</dd>'))
                    node = node.find_next_sibling(True)
            while node is not None and not (HEADING.match(node.name) and int(node.name[1]) <= level):
                following = node.find_next_sibling(True)
                if node.name in ('ul', 'ol'):
                    for li in node.find_all('li', recursive=False):
                        out.append(self.plain_item(state, li.decode_contents()))
                elif HEADING.match(node.name):
                    body, nxt = [], node.find_next_sibling(True)
                    while nxt is not None and not HEADING.match(nxt.name):
                        body.append(str(nxt))
                        nxt = nxt.find_next_sibling(True)
                    out.append(self.plain_item(state, '<strong>' + node.decode_contents() + '</strong>' +
                                               ''.join(body)))
                    following = nxt
                elif node.name == 'p':
                    out.append(self.plain_item(state, node.decode_contents()))
                node = following
        if definitions.find('dt'):
            board.insert(len(board.contents) - 1, definitions)
        return board

    def plain_item(self, state, markup):
        item = parse(f'<li data-state="{state}"></li>').li
        body = parse(markup.strip())
        first = next((c for c in body.contents if not (isinstance(c, NavigableString) and not c.strip())), None)
        if isinstance(first, Tag) and first.name == 'p':
            first = next((c for c in first.contents if not (isinstance(c, NavigableString) and not c.strip())),
                         None)
        if isinstance(first, Tag) and first.name in ('strong', 'b'):
            title = first.decode_contents().strip().rstrip('.:')
            first.decompose()
            rest = body.decode_contents().strip()
        else:
            title, rest = body.decode_contents().strip(), ''
        item.append(parse(f'<h3>{title}</h3>'))
        if rest:
            if not rest.startswith('<p'):
                rest = f'<p>{rest}</p>'
            fragment = parse(rest)
            for para in fragment.find_all('p'):
                inner = para.decode_contents().strip()
                found = re.search(r'(?:^|(?<=[.;]\s))Next:\s*', inner)
                if found:
                    before, after = inner[:found.start()].strip(), inner[found.end():].strip()
                    replacement = (f'<p>{before}</p>' if before else '') + f'<p data-role="next">{after}</p>'
                    para.replace_with(parse(replacement))
            item.append(fragment)
        return item

    # ------------------------------------------------------------ opening
    def read_labels(self, path):
        """words/LABELS.json renames the page's labels and state names; an empty value drops one."""
        if not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
        except ValueError as error:
            self.problems.append(('LABELS.json is not valid JSON', str(error)))
            return
        if not isinstance(data, dict):
            self.problems.append(('LABELS.json must hold one object of {key: text}', type(data).__name__))
            return
        self.label_overrides = data
        for key, value in data.items():
            k = ' '.join(str(key).lower().split())
            k = STATE_ALIASES.get(k, k)
            empty = value is None or value is False or (isinstance(value, str) and not value.strip())
            if not empty and not isinstance(value, str):
                self.problems.append(('LABELS.json value is not text', str(key)))
                continue
            if k in self.state_label:
                if empty:
                    self.hidden_states.add(k)
                else:
                    self.state_label[k] = value.strip()
            elif k == 'next':
                if empty:
                    self.show_next = False
                else:
                    self.labels['next'] = value.strip()
            elif k in self.labels:
                if empty:
                    self.problems.append(('LABELS.json leaves a page label empty', str(key)))
                else:
                    self.labels[k] = value.strip()
            else:
                self.warnings.append(f'LABELS.json: unknown key “{key}” (ignored)')

    def opening_hero(self, doc):
        """The opening's title, and every paragraph before its first section: the subject."""
        hero = parse('<header data-role="hero"></header>').header
        title = doc.find('h1')
        if title is not None:
            follower = title.find_next_sibling(True)
            hero.append(title.extract())
            subject = parse('<section data-role="subject"></section>').section
            while follower is not None and not HEADING.match(follower.name) and follower.name != 'section':
                following = follower.find_next_sibling(True)
                subject.append(follower.extract())
                follower = following
            if subject.find(True) is not None:
                self.opening['subject'] = subject
        return hero

    @staticmethod
    def opening_key(node):
        if not isinstance(node, Tag):
            return None
        role = node.get('data-role')
        if role in dict(OPENING):
            return role
        heading = node if node.name == 'h2' else None
        if node.name == 'section':
            first = node.find(HEADING)
            heading = first if first is not None and first.name == 'h2' else None
        if heading is None:
            return None
        text = text_of(heading).strip(' .:').casefold()
        for key, pattern in OPENING:
            if pattern.match(text):
                return key
        return None

    def take_opening(self, doc, rest):
        """Lift the opening's parts out of doc. With rest, every other part of doc is opening too."""
        nodes = list(doc.contents)
        found, i = [], 0
        while i < len(nodes):
            node = nodes[i]
            key = self.opening_key(node)
            if key is None and not (rest and isinstance(node, Tag) and
                                    (node.name in ('h2', 'section') or node.get('data-role'))):
                i += 1
                continue
            if node.name == 'section' or node.name != 'h2':
                part, i = node.extract(), i + 1
            else:
                group, j = [node], i + 1
                while j < len(nodes):
                    following = nodes[j]
                    if isinstance(following, Tag) and (following.name in ('h1', 'h2', 'section')
                                                       or following.get('data-role')):
                        break
                    group.append(following)
                    j += 1
                part, i = self.wrap(group), j
            found.append((key or 'part', part))
        if found and 'subject' not in self.opening and not rest:
            lead = []
            for node in list(doc.contents):
                if isinstance(node, Tag) and (HEADING.match(node.name) or node.name == 'section'
                                              or node.get('data-role')):
                    break
                lead.append(node)
            if any(isinstance(n, Tag) for n in lead):
                self.opening['subject'] = self.wrap(lead)
        for key, part in found:
            if key in ('breakthroughs', 'obstructions') and key not in self.ranked:
                self.shape_ranked(part, key)
                self.opening[key] = part
            elif key == 'subject' and 'subject' not in self.opening:
                self.opening['subject'] = part
            else:
                if key == 'open-problems' and self.open_part is None:
                    self.open_part = part
                self.opening_sections.append(part)
        subject = self.opening.get('subject')
        if subject is not None:
            for heading in subject.find_all(HEADING):
                heading['data-no-terms'] = ''

    @staticmethod
    def line_label(li):
        node = li
        while True:
            first = next((c for c in node.contents if not (isinstance(c, NavigableString) and not c.strip())), None)
            if isinstance(first, Tag) and first.name == 'p':
                node = first
                continue
            return first if isinstance(first, Tag) and first.name in ('strong', 'b') else None

    def shape_ranked(self, section, key):
        """Breakthroughs and obstructions: each item is a heading and a list of labelled lines.

        A heading followed by a deeper heading, or one named like "Decisive obstructions",
        starts a group; the obstructions group becomes its own band.
        """
        h2 = section.find('h2')
        title = h2.decode_contents() if h2 is not None else ''
        if h2 is not None:
            h2.extract()
        groups = []

        def new_group(kind, heading):
            group = {'kind': kind, 'heading': heading, 'intro': [], 'items': []}
            groups.append(group)
            return group

        group = new_group('obstruction' if key == 'obstructions' else 'breakthrough', None)
        item = None
        children = [c for c in section.contents if isinstance(c, Tag)]
        for index, node in enumerate(children):
            if HEADING.match(node.name):
                following = children[index + 1] if index + 1 < len(children) else None
                text = text_of(node).strip(' .:').casefold()
                deeper = following is not None and HEADING.match(following.name) is not None and \
                    int(following.name[1]) > int(node.name[1])
                if OBSTRUCTIONS.match(text) or deeper or following is None:
                    node['data-no-terms'] = ''
                    group = new_group('obstruction' if OBSTRUCTIONS.match(text) else group['kind'], node)
                    item = None
                    continue
                # A headline is a title, not a use of terms: it links to its own entry.
                node['data-no-terms'] = ''
                item = {'heading': node, 'lists': [], 'extra': []}
                group['items'].append(item)
            elif node.name in ('ul', 'ol'):
                if item is None:
                    item = {'heading': None, 'lists': [], 'extra': []}
                    group['items'].append(item)
                item['lists'].append(node)
            else:
                (item['extra'] if item is not None else group['intro']).append(node)
        for g in groups:
            for it in g['items']:
                for lst in it['lists']:
                    for li in lst.find_all('li', recursive=False):
                        label = self.line_label(li)
                        if label is not None:
                            label['data-no-terms'] = ''
                            # The titles of cited papers are names, not uses of terms.
                            if re.match(r'(?:proved in|sources?)\b', text_of(label).strip().casefold()):
                                for cited in li.find_all(['em', 'i', 'cite']):
                                    cited['data-no-terms'] = ''
        groups = [g for g in groups if g['items'] or g['intro']]
        self.ranked[key] = {'title': title, 'section': section, 'groups': groups}

    def item_lines(self, item):
        """The item's lines as (key, label, value html); key is None for an unrecognised label."""
        lines = []
        for lst in item['lists']:
            for li in lst.find_all('li', recursive=False):
                clone = parse(str(li)).li
                label_tag = self.line_label(clone)
                label = ''
                if label_tag is not None:
                    label = text_of(label_tag).strip().rstrip(':').strip()
                    label_tag.decompose()
                inner = [c for c in clone.contents if not (isinstance(c, NavigableString) and not c.strip())]
                if len(inner) == 1 and isinstance(inner[0], Tag) and inner[0].name == 'p':
                    value = inner[0].decode_contents()
                else:
                    value = clone.decode_contents()
                value = re.sub(r'^\s*:\s*', '', value.strip())
                key = next((k for k, pattern in LINE_KEYS if pattern.match(label.casefold())), None)
                lines.append((key, label, value))
        return lines

    def check_ranked(self):
        """Each breakthrough has its five lines; each Read more resolves to a part of the page."""
        for key, data in self.ranked.items():
            for group in data['groups']:
                for n, item in enumerate(group['items'], 1):
                    head = text_of(item['heading']) if item['heading'] is not None else ''
                    name = f'{group["kind"]} {n}' + (f' “{head[:70]}”' if head else '')
                    lines = self.item_lines(item)
                    keys = [k for k, _, _ in lines]
                    record = {'kind': group['kind'], 'title': head, 'lines': [label for _, label, _ in lines]}
                    self.ranked_items.append(record)
                    if not head:
                        self.ranked_issues.append(f'{name} has no headline')
                    elif len(RANK.sub('', head).split()) > 16:
                        self.warnings.append(f'{name}: headline over 16 words')
                    missing = [LINE_NAMES[k] for k in ('achieved', 'why', 'domain', 'proved', 'read')
                               if k not in keys]
                    if missing:
                        self.ranked_issues.append(f'{name} lacks {", ".join(missing)}')
                    unknown = [label or '(no label)' for k, label, _ in lines if k is None]
                    if unknown:
                        self.ranked_issues.append(f'{name} has lines the page does not recognise: '
                                                  + ', '.join(unknown))
                    for k, label, value in lines:
                        if k != 'read':
                            continue
                        anchors = [a for a in parse(value).find_all('a', href=True)]
                        if not anchors:
                            self.ranked_issues.append(f'{name}: {label} links to no section')
                        for a in anchors:
                            href = a['href'].strip()
                            if not href.startswith('#'):
                                self.ranked_issues.append(f'{name}: {label} links outside the page ({href})')
                                continue
                            target = unquote(href[1:])
                            target = self.renamed.get(target, target)
                            if target not in self.ids:
                                self.ranked_issues.append(f'{name}: {label} points to #{target}, '
                                                          'which the page does not contain')

    # ------------------------------------------------------- result views
    def chip(self, status):
        label = self.labels.get(f'status_{status}', status.capitalize())
        return (f'<span class="chip chip-{status}">{glyph(status)}'
                f'<span class="chip-label">{html.escape(label)}</span></span>')

    def obstruction_word(self):
        """The writer's lead label for an obstruction (for example "Rules out")."""
        for r in self.results:
            if r['kind'] == 'obstruction' and r['lead'] and r['lead'][0]:
                return r['lead'][0]
        return self.labels.get('rules_out', 'Rules out')

    def key_html(self, statuses, obstruction=False):
        """The key: each mark the view uses, drawn exactly as the view draws it."""
        rows = [f'<li>{self.chip(s)}</li>' for s in statuses]
        if obstruction:
            rows.append(f'<li><span class="chip chip-kind">{glyph("failing")}'
                        f'<span class="chip-label">{html.escape(self.obstruction_word())}</span></span></li>')
        if not rows:
            return ''
        return f'<ul class="key" aria-label="{html.escape(self.labels["key"])}">{"".join(rows)}</ul>'

    def num_of(self, target):
        n = self.section_number.get(self.id_section.get(target, ''))
        return f'<span class="num">{n}</span>' if n else ''

    @staticmethod
    def unlinked(markup):
        """Markup without its links (their words stay), for use inside another link."""
        tree = parse(markup)
        for a in tree.find_all('a'):
            if 'hl' in (a.get('class') or []):
                a.decompose()
            else:
                a.unwrap()
        for node in tree.find_all(True):
            for attr in ('id', 'tabindex', 'aria-expanded', 'aria-haspopup', 'aria-controls'):
                if node.has_attr(attr):
                    del node[attr]
        return tree.decode()

    def result_row(self, r):
        """One ranked result: rank, headline and status, the claim as the writer states it, the
        work and sections that hold its proof, the report sections it points to, and the
        remaining lines on demand."""
        rid = r['id']
        if r['kind'] == 'breakthrough':
            mark = f'<span class="rk-n" aria-hidden="true">{html.escape(r["rank"])}</span>'
            spoken = f'<span class="visually-hidden">{html.escape(r["rank"])}. </span>'
        else:
            mark = f'<span class="rk-n rk-n-glyph" aria-hidden="true">{glyph("failing")}</span>'
            spoken = ''
        parts = [f'<li class="rk rk-{r["kind"]}" id="{rid}" aria-labelledby="{rid}-title">{mark}<div class="rk-main">',
                 '<div class="rk-top">']
        if r['head']:
            parts.append(f'<h3 class="rk-head" id="{rid}-title">{spoken}{r["head"]}</h3>')
        if r['status']:
            parts.append('<p class="rk-status">' + ''.join(self.chip(s) for s in r['status']) + '</p>')
        parts.append('</div>')
        if r['lead']:
            label, value = r['lead']
            tag = f'<span class="rk-label">{html.escape(label)}</span> ' if label else ''
            parts.append(f'<p class="rk-claim">{tag}{value}</p>')
        rest = [(k, label, value) for k, label, value in r['lines']
                if (label, value) != r['lead'] and k != 'read']
        if rest or r['extra']:
            summary = ' · '.join(html.escape(label) for _, label, _ in rest if label)
            parts.append(f'<details class="rk-more"><summary><span>{summary or html.escape(self.labels["more"])}'
                         '</span></summary><dl class="rk-lines">')
            for k, label, value in rest:
                cls = f' class="rk-{k}"' if k else ''
                parts.append(f'<div{cls}><dt>{html.escape(label)}</dt><dd>{value}</dd></div>')
            parts.append('</dl>')
            if r['extra']:
                parts.append('<div class="rk-extra">' + ''.join(str(n) for n in r['extra']) + '</div>')
            parts.append('</details>')
        parts.append('</div>')
        side = []
        if r['brief']:
            side.append(f'<p class="rk-src">{r["brief"]}</p>')
        if r['reads']:
            label = next((lab for k, lab, _ in r['lines'] if k == 'read'), self.labels['read'])
            links = ''.join(f'<li><a href="#{t}">{self.num_of(t)}<span class="rk-sec-name">{text}</span></a></li>'
                            for t, text in r['reads'])
            side.append(f'<div class="rk-read"><span class="rk-side-label">{html.escape(label)}</span>'
                        f'<ul class="rk-secs">{links}</ul></div>')
        if side:
            parts.append('<div class="rk-side">' + ''.join(side) + '</div>')
        parts.append('</li>')
        return ''.join(parts)

    def ranked_section(self, record, cover=False):
        ident = record['ident']
        statuses = []
        for r in record['items']:
            statuses += [s for s in r['status'] if s not in statuses]
        key = '' if cover else self.key_html(statuses, obstruction=record['kind'] == 'obstruction')
        tag = 'ol' if record['kind'] == 'breakthrough' else 'ul'
        intro = ''.join(str(n) for n in record['intro'])
        return (f'<section class="ranked ranked-{record["band"]}{" ranked-cover" if cover else ""}" '
                f'id="{ident}" aria-labelledby="{ident}-title"><div class="ranked-head">'
                f'<h2 class="ranked-title" id="{ident}-title">{record["title"]}</h2>{key}</div>'
                + (f'<div class="ranked-intro">{intro}</div>' if intro else '') +
                f'<{tag} class="rk-list">{"".join(self.result_row(r) for r in record["items"])}</{tag}></section>')

    def strip_html(self):
        """Under the breakthroughs: the obstructions, by name, each linked to its entry."""
        out = []
        for g in self.result_groups:
            if g['kind'] != 'obstruction' or not g['items']:
                continue
            links = ''.join(f'<li><a href="#{r["id"]}">{glyph("failing")}<span>{self.unlinked(r["head"])}</span></a></li>'
                            for r in g['items'])
            out.append(f'<div class="strip"><p class="strip-title"><a href="#{g["ident"]}">'
                       f'{html.escape(g["title_text"])}</a></p><ul class="strip-list">{links}</ul></div>')
        return ''.join(out)

    def jump_html(self, cover_group):
        """The first screen's way into the rest of the page, with the size of each part."""
        lab = self.labels
        links = []
        for g in self.result_groups:
            if g is cover_group:
                continue
            links.append((g['ident'], g['title_text'], str(len(g['items']))))
        for entry in self.entries:
            if entry.get('opening') and entry['label']:
                count = str(len(self.problems_open)) if self.open_part is entry['section'] and self.problems_open else ''
                links.append((entry['id'], entry['label'], count))
        if self.results:
            links.append(('map', lab['map'], ''))
        if self.has_board:
            links.append(('status', lab['status'], ''))
        first = next((e for e in self.entries if e['label'] is not None and not e.get('opening')), None)
        if first is not None:
            links.append((first['id'], lab['report'], f'{len(self.section_number)} {lab["sections"]}'))
        links.append(('terms', lab['terms'], str(len(self.cards.order))))
        items = ''.join(f'<li><a href="#{ident}"><span class="jump-name">{html.escape(name)}</span>'
                        + (f'<span class="jump-n">{html.escape(n)}</span>' if n else '') +
                        f'{icon("arrow", "jump-arrow")}</a></li>' for ident, name, n in links)
        return f'<nav class="jump" id="jump" aria-label="{html.escape(lab["on_page"])}"><ul>{items}</ul></nav>'

    def map_html(self):
        """The map of results, one row for each result: in the middle the result and its status;
        to the left the report sections its own links name, with the statements stated there;
        to the right the work and sections its "Proved in" line cites. A hairline joins the
        result to each of them. An open problem has a row of its own. A "Builds on" line, or a
        link in an item's words to another item or section, is listed under the item. Nothing
        is drawn that the words do not state."""
        if not self.results:
            return ''
        lab = self.labels
        items = {r['id']: r for r in self.results}
        problems = {p['id']: p for p in self.problems_open}

        def mark(r):
            if r['kind'] == 'breakthrough':
                return f'<span class="mn-mark mn-rank" aria-hidden="true">{html.escape(r["rank"])}</span>'
            return f'<span class="mn-mark" aria-hidden="true">{glyph("failing")}</span>'

        def statements(sid):
            rows = self.statement_index.get(sid) or []
            if not rows:
                return ''
            chips = ''.join(f'<li><a class="st-chip{" has-proof" if s["proof"] else ""}" href="#{s["id"]}">'
                            f'{glyph("theorem")}<span class="st-kind">{html.escape(s["kind"])}</span>'
                            + (f'<span class="st-proof">{html.escape(lab["proof_here"])}</span>' if s['proof'] else '') +
                            '</a></li>' for s in rows)
            return f'<ul class="mn-stmts">{chips}</ul>'

        def named(ids):
            out = []
            for t in ids:
                if t in items:
                    r = items[t]
                    out.append(f'<a href="#{t}">{mark(r)}<span>{self.unlinked(r["head"])}</span></a>')
                elif t in problems:
                    out.append(f'<a href="#{t}"><span class="mn-mark" aria-hidden="true">{glyph("open")}</span>'
                               f'<span>{self.unlinked(problems[t]["title"])}</span></a>')
                else:
                    sid = self.id_section.get(t)
                    if sid in self.section_number:
                        out.append(f'<a href="#{t}">{self.num_of(t)}<span>{html.escape(self.section_label.get(sid, ""))}</span></a>')
            return out

        def relations(x):
            rows = []
            builds = named(x['builds'])
            if builds:
                rows.append(f'<p class="mn-rel"><span class="mn-rel-label">{html.escape(lab["builds_on"])}</span>'
                            + ''.join(builds) + '</p>')
            refers = named([t for t in x['refers'] if t not in x['builds']])
            if refers:
                rows.append(f'<p class="mn-rel"><span class="mn-rel-label">{html.escape(lab["refers_to"])}</span>'
                            + ''.join(refers) + '</p>')
            return ''.join(rows)

        def proved_in(r):
            line = next((value for k, _, value in r['lines'] if k == 'proved'), None)
            return source_brief(line) if line is not None else []

        rows_html, statuses, last_work = [], [], None
        for g in self.result_groups:
            if not g['items']:
                continue
            rows_html.append(f'<div class="mgroup mgroup-{g["kind"]}"><h3 class="mgroup-title">{html.escape(g["title_text"])}</h3>')
            last_work = None
            for r in g['items']:
                statuses += [s for s in r['status'] if s not in statuses]
                node = f'map-{r["id"]}'
                targets, secs = [], []
                for k, (t, text) in enumerate(r['reads'], 1):
                    sid = self.id_section.get(t)
                    sec_id = self.fresh_id(f'{node}-sec-{k}')
                    targets.append(sec_id)
                    secs.append(f'<li class="mn-sec" id="{sec_id}"><a class="mn-link" href="#{t}">{self.num_of(t)}'
                                f'<span class="mn-title">{html.escape(self.section_label.get(sid, "")) or text}</span></a>'
                                f'{statements(sid)}</li>')
                cites = []
                for title, refs in proved_in(r):
                    key = ' '.join(text_of(parse(title)).split())
                    cite_id = self.fresh_id(f'{node}-cite-{len(cites) + 1}')
                    targets.append(cite_id)
                    sign = '§§' if len(refs) > 1 or any('–' in x for x in refs) else '§'
                    same = key == last_work
                    cites.append(f'<p class="mn-cite{" is-same" if same else ""}" id="{cite_id}">'
                                 f'<cite class="mn-work">{title}</cite>'
                                 f'<span class="src-refs">{sign}{", ".join(refs)}</span></p>')
                    last_work = key
                rows_html.append(
                    f'<div class="mrow">'
                    f'<div class="mres"><div class="mn mn-{r["kind"]}" id="{node}"'
                    + (f' data-to="{" ".join(targets)}"' if targets else '') + '>'
                    f'{mark(r)}<div class="mn-body"><a class="mn-link" href="#{r["id"]}">'
                    f'<span class="mn-title">{self.unlinked(r["head"])}</span></a>'
                    f'<p class="mn-meta">{"".join(self.chip(s) for s in r["status"])}</p>{relations(r)}</div></div></div>'
                    + (f'<ul class="msecs">{"".join(secs)}</ul>' if secs else '<div class="msecs"></div>')
                    + (f'<div class="mcite">{"".join(cites)}</div>' if cites else '<div class="mcite"></div>')
                    + '</div>')
            rows_html.append('</div>')
        if self.problems_open:
            heading = self.open_part.find('h2') if self.open_part is not None else None
            title = text_of(heading).replace('#', '').strip() if heading is not None else lab['map_open']
            rows_html.append(f'<div class="mgroup mgroup-open"><h3 class="mgroup-title">{html.escape(title)}</h3>')
            for p in self.problems_open:
                node = self.fresh_id(f'map-{p["id"]}')
                rows_html.append(f'<div class="mrow"><div class="mres"><div class="mn mn-open" id="{node}">'
                                 f'<span class="mn-mark" aria-hidden="true">{glyph("open")}</span>'
                                 f'<div class="mn-body"><a class="mn-link" href="#{p["id"]}">'
                                 f'<span class="mn-title">{self.unlinked(p["title"])}</span></a>'
                                 f'<p class="mn-meta">{self.chip("open")}</p>{relations(p)}</div></div></div>'
                                 '<div class="msecs"></div><div class="mcite"></div></div>')
            rows_html.append('</div>')
            statuses.append('open')
        proved_label = next((label for r in self.results for k, label, _ in r['lines'] if k == 'proved'), lab['map_works'])
        key = self.key_html(statuses, obstruction=any(r['kind'] == 'obstruction' for r in self.results))
        return (f'<section class="mapsec" id="map" aria-labelledby="map-title"><div class="mapsec-inner">'
                f'<header class="map-head"><h2 id="map-title">{html.escape(lab["map"])}</h2>'
                f'<p class="map-note">{html.escape(lab["map_note"])}</p>{key}</header>'
                f'<div class="map"><div class="mcols" aria-hidden="true"><span class="mcol-res"></span>'
                f'<span class="mcol-secs">{html.escape(lab["map_sections"])}</span>'
                f'<span class="mcol-cite">{html.escape(proved_label)}</span></div>'
                + ''.join(rows_html) +
                '<svg class="map-wires" aria-hidden="true" focusable="false"></svg></div></div></section>')

    def open_problems_view(self):
        """Each open problem gets its status above its title."""
        part = self.open_part
        if part is None:
            return
        part['class'] = list(dict.fromkeys((part.get('class') or []) + ['open-problems']))
        for p in self.problems_open:
            heading = part.find(id=p['id'])
            if heading is None:
                continue
            status = parse(f'<p class="op-status">{self.chip("open")}</p>').p
            heading.insert_before(status)

    def subject_html(self):
        part = self.opening.get('subject')
        if part is None:
            return ''
        heading = part.find(HEADING)
        label = ''
        if heading is not None:
            label = f'<p class="subject-label">{heading.decode_contents()}</p>'
            heading.extract()
        return f'<div class="subject" id="subject">{label}{part.decode_contents()}</div>'

    def assign_ids(self):
        # Ids the page itself uses; a report id that collides is renamed.
        reserved = {'main', 'status', 'status-title', 'terms', 'terms-title', 'terms-other', 'contents',
                    'qh-card', 'qh-card-title', 'top', 'board-filter', 'board-filter-row', 'bar', 'subject',
                    'breakthroughs', 'breakthroughs-title', 'obstructions', 'obstructions-title',
                    'map', 'map-title', 'map-wires', 'finder', 'finder-title', 'finder-input', 'finder-list',
                    'finder-status', 'toast', 'terms-filter', 'terms-filter-count', 'report', 'jump'}
        reserved |= {f'map-{band}-{n}' for band in ('breakthroughs', 'obstructions') for n in range(1, 40)}
        reserved |= {f'{band}-{n}' for band in ('breakthroughs', 'obstructions') for n in range(1, 40)}
        reserved |= {f'status-{s}' for s in self.states} | {f'status-{s}-title' for s in self.states}
        reserved |= {f'terms-{c}' for c in 'abcdefghijklmnopqrstuvwxyz'}
        used = set()

        def claim(base):
            if base.startswith('term-'):
                base = 'defn-' + base[5:]
            candidate, n = base, 2
            while candidate in used or candidate in reserved:
                candidate = f'{base}-{n}'
                n += 1
            used.add(candidate)
            return candidate

        self.renamed = {}
        for section in self.sections:
            for node in [section] + section.find_all(True):
                if node.has_attr('id'):
                    old = node['id']
                    new = claim(old)
                    if new != old:
                        self.renamed[old] = new
                        node['id'] = new
        # Ids made of hexadecimal hashes are internal; give the referenced ones plain names.
        referenced = {unquote(a['href'][1:]) for section in self.sections for a in section.find_all('a', href=True)
                      if a['href'].startswith('#')}
        hashed = re.compile(r'(?:^|-)[0-9a-f]{12,}$')
        counter = 0
        for section in self.sections:
            for node in section.find_all(id=True):
                if hashed.search(node['id']):
                    old = node['id']
                    used.discard(old)
                    if old in referenced or any(k == old for k in self.renamed.values()):
                        counter += 1
                        new = claim(f'passage-{counter}')
                        node['id'] = new
                        self.renamed[old] = new
                        for key, value in list(self.renamed.items()):
                            if value == old:
                                self.renamed[key] = new
                    else:
                        del node['id']
        for section in self.sections:
            if not section.has_attr('id'):
                heading = section.find(HEADING)
                section['id'] = claim(slugify(text_of(heading) if heading else 'section'))
            for heading in section.find_all(HEADING):
                if not heading.has_attr('id'):
                    heading['id'] = claim(slugify(text_of(heading), 'part'))
        # The opening's own parts carry only the ids the page gives them.
        for part in self.opening.values():
            for node in [part] + part.find_all(id=True):
                if node.has_attr('id'):
                    del node['id']
        self.ids = used
        for section in self.sections:
            sid = section['id']
            self.id_section[sid] = sid
            for node in section.find_all(id=True):
                self.id_section.setdefault(node['id'], sid)
        if self.has_board:
            self.ids |= {'status'} | {f'status-{s}' for s in self.states}
        self.ids |= {'terms', 'top'} | ({'subject'} if 'subject' in self.opening else set())
        # The ranked results and their groups have anchors of their own, so the words can link
        # one result to another.
        for _, _, _, ident, item_ids in self.result_idents():
            self.ids.add(ident)
            self.ids |= set(item_ids)

    # -------------------------------------------------------------- contents
    def toc(self):
        """One contents entry per section; below it, the section's main headings.

        A section's label is its data-toc attribute, else its first heading's data-toc,
        else its eyebrow, else its first heading. The entries below it are the headings
        at the section's highest heading level (or the next level down, when the only
        heading at that level gave the label), together with any heading that has data-toc.
        """
        entries = []
        for section in self.sections:
            headings = section.find_all(HEADING)
            first = headings[0] if headings else None
            eyebrow = section.find(class_='eyebrow')
            label_heading = None
            if section.get('data-toc'):
                label = section['data-toc']
                if first is not None and text_of(first) == label:
                    label_heading = first
            elif first is not None and first.get('data-toc'):
                label, label_heading = first['data-toc'], first
            elif eyebrow is not None:
                label = text_of(eyebrow)
            elif first is not None:
                label, label_heading = text_of(first), first
            else:
                label = None
            if section.get('data-toc') and first is not None and label_heading is None and \
                    not first.get('data-toc') and len(headings) and \
                    sum(1 for h in headings if h.name == first.name) == 1:
                label_heading = first
            children = []
            if headings:
                top = min(int(h.name[1]) for h in headings)
                level = [h for h in headings if int(h.name[1]) == top and h is not label_heading]
                if not level:
                    level = [h for h in headings if int(h.name[1]) == top + 1]
                chosen = {id(h) for h in level} | {id(h) for h in headings if h.get('data-toc')}
                for h in headings:
                    if id(h) in chosen and h is not label_heading:
                        children.append((h['id'], h.get('data-toc') or text_of(h)))
            entries.append({'id': section['id'], 'label': label, 'children': children,
                            'section': section, 'label_heading': label_heading,
                            'opening': any(section is s for s in self.opening_sections)})
        self.entries = entries
        self.section_label = {e['id']: e['label'] or '' for e in entries}
        n = 0
        for e in entries:
            if e['label'] is None or e['opening']:
                continue
            n += 1
            self.section_number[e['id']] = n

    # ----------------------------------------------------------------- links
    def links(self, root, where):
        for link in root.find_all('a', href=True):
            href = link['href'].strip()
            if href.startswith('#'):
                target = unquote(href[1:])
                if target.startswith('term-') and target[5:] in self.cards.by_id:
                    ident = target[5:]
                    link['href'] = f'#term-{ident}'
                    link['data-term'] = ident
                    link['class'] = ['term']
                    continue
                if target.startswith('term-'):
                    self.unknown_terms.append((target[5:], text_of(link), where))
                    link.unwrap()
                    continue
                target = self.renamed.get(target, target)
                if target in self.ids:
                    link['href'] = '#' + target
                else:
                    self.pointers.append({'target': target, 'text': text_of(link),
                                          'context': self.sentence(link), 'where': where})
                    link.unwrap()
            elif href.startswith('data:'):
                self.attachments.append({'text': text_of(link), 'context': self.sentence(link),
                                         'where': where})
                link.unwrap()
            elif re.match(r'https?://', href):
                link['rel'] = 'noopener'
                self.external_links.append({'href': href, 'text': text_of(link), 'where': where})
            elif not href.startswith('mailto:'):
                self.relative_links.append({'href': href, 'text': text_of(link), 'where': where})

    @staticmethod
    def sentence(node):
        block = node.find_parent(['p', 'li', 'dd', 'td', 'div']) or node.parent
        text = text_of(block)
        anchor = text_of(node)
        at = text.find(anchor)
        if at < 0:
            return text[:220]
        start = max(text.rfind('. ', 0, at) + 2, 0) if text.rfind('. ', 0, at) >= 0 else 0
        end = text.find('. ', at + len(anchor))
        return text[start:(end + 1 if end >= 0 else len(text))][:320]

    def explicit_terms(self, root, where):
        for node in root.find_all(attrs={'data-term': True}):
            ident = node['data-term']
            if node.name == 'dfn' or (node.name == 'a' and node.get('href', '').startswith('#term-')):
                continue
            if ident in self.cards.by_id:
                link = Tag(name='a', attrs={'class': 'term', 'href': f'#term-{ident}', 'data-term': ident})
                for child in list(node.contents):
                    link.append(child.extract())
                node.replace_with(link)
            else:
                self.unknown_terms.append((ident, text_of(node), where))
                node.unwrap()

    def definitions(self):
        """Each <dfn> naming a card becomes a trigger for it; the first is its defining site."""
        found = []
        for section in self.sections:
            for dfn in section.find_all('dfn'):
                ident = None
                own = dfn.get('id', '')
                if own.startswith('defn-') and own[5:] in self.cards.by_id:
                    ident = own[5:]
                    self.defining.setdefault(ident, (own, section['id']))
                if ident is None:
                    ident = self.wirer.ident(text_of(dfn))
                if ident is None:
                    self.uncarded_dfn.append((text_of(dfn), self.section_label.get(section['id'], '')))
                    continue
                found.append((dfn, ident, section))
        for dfn, ident, section in found:
            if ident not in self.defining:
                anchor = dfn.get('id') or ('defn-' + ident)
                if not dfn.get('id'):
                    if anchor in self.ids:
                        anchor = f'defn-{ident}-site'
                    dfn['id'] = anchor
                    self.ids.add(anchor)
                self.defining[ident] = (anchor, section['id'])
            dfn['class'] = ['term', 'defining']
            dfn['data-term'] = ident
            dfn['tabindex'] = '0'

    # ----------------------------------------------------------------- board
    def board(self):
        lab = self.labels
        items = {s: [] for s in self.states}
        if not self.has_board:
            # The opening replaces the status board.
            self.board_counts = {s: 0 for s in self.states}
            self.board_items = []
            self.board_html = parse('')
            return
        headline = dek = None
        defs = {}
        el = self.status_el
        if el is not None:
            heading = el.find(['h2'])
            if heading is not None:
                headline = heading.decode_contents()
            dek_el = el.find(attrs={'data-role': 'dek'})
            if dek_el is not None:
                dek = dek_el.decode_contents()
            for dt_el in el.select('dl[data-role="states"] dt[data-state]'):
                dd = dt_el.find_next_sibling('dd')
                defs[self.state_id(dt_el['data-state'])] = dd.decode_contents() if dd else ''
            for node in el.find_all(attrs={'data-state': True}):
                if node.name == 'dt' or node.find_parent(attrs={'data-state': True}):
                    continue
                state = self.state_id(node['data-state'])
                if state not in items:
                    self.problems.append(('status item with an unknown state', node['data-state']))
                    continue
                items[state].append(node)
        if headline is None:
            self.missing_words.append('the status section headline (one claim sentence)')
        if not defs:
            self.missing_words.append('one line defining each state (established, working, failing, '
                                      'stabilising, oscillating, remains)')
        self.board_counts = {s: len(items[s]) for s in self.states}
        for state in self.hidden_states:
            if self.board_counts.get(state):
                self.problems.append(('LABELS.json drops a state that still has items', state))
        self.board_items = []
        parts = ['<section id="status" class="board sec" aria-labelledby="status-title">',
                 '<header class="sec-head">']
        if headline:
            parts.append(f'<p class="eyebrow">{html.escape(lab["status"])}</p>')
        parts.append(f'<h2 id="status-title">{headline or html.escape(lab["status"])}</h2>')
        if dek:
            parts.append(f'<p class="dek">{dek}</p>')
        # The search is a small control; its field and its empty result appear only when used.
        parts.append('<div class="board-tools" hidden><button class="filter-toggle" type="button" '
                     f'aria-expanded="false" aria-controls="board-filter-row" title="{html.escape(lab["filter"])}">'
                     '<svg class="glyph" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
                     '<circle cx="6.8" cy="6.8" r="4.6" fill="none" stroke="currentColor" stroke-width="1.5"/>'
                     '<path d="m10.2 10.2 4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'
                     f'</svg><span class="filter-toggle-label">{html.escape(lab["filter"])}</span></button>'
                     '<label class="filter" id="board-filter-row" hidden><span class="visually-hidden">'
                     f'{html.escape(lab["filter"])}</span><input id="board-filter" type="search" '
                     'autocomplete="off" spellcheck="false"></label></div>')
        parts.append('</header>')
        if self.ranked:
            parts.append(self.tally_html())
        parts.append('<div class="states">')
        for state in self.shown_states():
            label = html.escape(self.state_label[state])
            n = len(items[state])
            parts.append(f'<section class="state" id="status-{state}" data-state="{state}" '
                         f'aria-labelledby="status-{state}-title">')
            parts.append(f'<header class="state-head">{glyph(state)}'
                         f'<h3 id="status-{state}-title">{label}</h3>'
                         f'<span class="state-count">{n}</span>'
                         + (f'<p class="state-def">{defs[state]}</p>' if defs.get(state) else '') +
                         '</header>')
            if not n:
                parts.append(f'<p class="state-empty">{html.escape(lab["empty_state"])}</p></section>')
                continue
            parts.append('<ol class="st-list">')
            for node in items[state]:
                parts.append(self.board_item(node, state))
            parts.append('</ol></section>')
        parts.append('</div></section>')
        self.board_html = parse(''.join(parts))

    def shown_states(self):
        return [s for s in self.states if not (s in self.hidden_states and not self.board_counts.get(s))]

    def tally_html(self):
        tally = []
        for s in self.shown_states():
            tally.append(f'<li data-state="{s}"><a href="#status-{s}">{glyph(s)}'
                         f'<span class="t-n">{self.board_counts[s]}</span>'
                         f'<span class="t-l">{html.escape(self.state_label[s])}</span></a></li>')
        return f'<ol class="tally" aria-label="{html.escape(self.labels["status"])}">{"".join(tally)}</ol>'

    def state_id(self, value):
        value = ' '.join(value.lower().split())
        return STATE_ALIASES.get(value, value)

    def board_item(self, node, state):
        node = parse(str(node)).find(True)
        heading = node.find(HEADING)
        if heading is not None:
            title = heading.decode_contents()
            heading.decompose()
        else:
            first = node.find(['strong', 'b'])
            title = first.decode_contents() if first else None
            if first is not None:
                first.decompose()
        if not title:
            self.problems.append(('status item without a title', text_of(node)[:80]))
            title = html.escape(text_of(node)[:80])
        nexts = node.find_all(attrs={'data-role': 'next'})
        for n in nexts:
            n.extract()
        ref = node.get('data-ref')
        body = node.decode_contents().strip()
        title_text = text_of(parse(title))
        self.board_items.append({'state': state, 'title': title_text,
                                 'words': len(title_text.split()),
                                 'body_words': len(text_of(parse(body)).split()) if body else 0})
        detail = []
        if body:
            detail.append(f'<div class="st-text">{body}</div>')
        for n in nexts:
            if not self.show_next or not text_of(n):
                continue
            detail.append(f'<p class="st-next"><span class="st-label">{html.escape(self.labels["next"])}'
                          f'</span> {n.decode_contents()}</p>')
        if ref:
            target = self.renamed.get(ref, ref)
            if target in self.ids:
                detail.append(f'<p class="st-read"><a href="#{target}">{html.escape(self.labels["read"])}'
                              f' <span aria-hidden="true">→</span></a></p>')
            else:
                self.problems.append(('status item points to a missing section', ref))
        if not detail:
            return f'<li class="st-item"><p class="st-title">{glyph(state)}<span>{title}</span></p></li>'
        return (f'<li class="st-item"><details><summary class="st-title">{glyph(state)}<span>{title}'
                f'</span></summary><div class="st-body">{"".join(detail)}</div></details></li>')

    # ------------------------------------------------------------------ cards
    def card_html(self, ident):
        lab = self.labels
        name = html.escape(self.cards.name(ident))
        out = [f'<article class="card-entry" id="term-{ident}" data-card="{ident}" '
               f'aria-labelledby="term-{ident}-title">',
               f'<h3 class="card-title" id="term-{ident}-title">{name}</h3>']
        trees = self.cards.trees
        definition = trees.get((ident, 'definition'))
        if definition is not None and text_of(definition):
            out.append(f'<div class="card-def">{definition.decode()}</div>')
        for field, label, cls in (('motivation', lab['motivation'], 'card-why'),
                                  ('context', lab['context'], 'card-where')):
            tree = trees.get((ident, field))
            if tree is not None and text_of(tree):
                out.append(f'<div class="{cls}"><p class="card-label">{html.escape(label)}</p>'
                           f'{tree.decode()}</div>')
        if ident in self.defining:
            anchor, section = self.defining[ident]
            out.append(f'<p class="card-intro"><span class="card-label">{html.escape(lab["introduced"])}'
                       f'</span> <a href="#{anchor}">{html.escape(self.section_label.get(section, ""))}</a></p>')
        related = [r for r in (self.cards.by_id[ident].get('related') or [])
                   if isinstance(r, str) and r in self.cards.by_id and r != ident]
        if related:
            chips = ''.join(f'<li><a class="term rel" href="#term-{r}" data-term="{r}">'
                            f'{html.escape(self.cards.name(r))}</a></li>' for r in related)
            out.append(f'<div class="card-rel"><p class="card-label">{html.escape(lab["related"])}</p>'
                       f'<ul>{chips}</ul></div>')
        out.append('</article>')
        return ''.join(out)

    def glossary(self):
        lab = self.labels

        def sort_key(ident):
            name = self.cards.name(ident)
            stripped = re.sub(r'^[^A-Za-z0-9]+', '', name)
            return (stripped or name).casefold()

        order = sorted(self.cards.order, key=sort_key)
        letters, entries, current = [], [], None
        for ident in order:
            letter = (sort_key(ident)[:1] or '#').upper()
            if not letter.isalpha():
                letter = '#'
            if letter != current:
                current = letter
                letters.append(letter)
                entries.append(f'<h3 class="letter" id="terms-{letter.lower() if letter != "#" else "other"}">'
                               f'{letter}</h3>')
            entries.append(self.card_html(ident))
        alpha = ''.join(f'<a href="#terms-{l.lower() if l != "#" else "other"}">{l}</a>' for l in letters)
        markup = (f'<section id="terms" class="glossary sec" aria-labelledby="terms-title">'
                  f'<header class="sec-head"><h2 id="terms-title">{html.escape(lab["terms"])}'
                  f'<span class="count">{len(order)}</span></h2>'
                  f'<div class="terms-tools" hidden><label class="terms-filter">{icon("search")}'
                  f'<span class="visually-hidden">{html.escape(lab["filter_terms"])}</span>'
                  f'<input id="terms-filter" type="search" autocomplete="off" spellcheck="false" '
                  f'placeholder="{html.escape(lab["filter_terms"], quote=True)}"></label>'
                  f'<p class="terms-filter-count" id="terms-filter-count" role="status" aria-live="polite"></p></div>'
                  f'</header>'
                  f'<nav class="alpha" aria-label="{html.escape(lab["terms"])}">{alpha}</nav>'
                  f'<div class="card-list">{"".join(entries)}</div></section>')
        return parse(markup)

    # ------------------------------------------------------------------- body
    def statements(self, section):
        for node in section.find_all(class_='statement'):
            kind = node.get('data-kind')
            if kind:
                label = Tag(name='p', attrs={'class': 'statement-kind'})
                label.string = kind
                node.insert(0, label)
        for node in section.find_all(class_='proof'):
            if node.name == 'details':
                continue
            details = Tag(name='details', attrs={'class': 'proof'})
            summary = Tag(name='summary')
            summary.string = node.get('data-summary') or self.labels['proof']
            details.append(summary)
            for child in list(node.contents):
                details.append(child.extract())
            node.replace_with(details)
        for table in section.find_all('table'):
            if table.parent is not None and 'table-wrap' not in (table.parent.get('class') or []):
                wrap = Tag(name='div', attrs={'class': 'table-wrap'})
                table.wrap(wrap)
        wrap_display_math(section)

    def fresh_id(self, base):
        candidate, n = base, 2
        while candidate in self.ids:
            candidate = f'{base}-{n}'
            n += 1
        self.ids.add(candidate)
        return candidate

    def collect_statements(self):
        """Give each statement of the report an anchor and record its kind and whether its proof
        is on the page. The kind is the writer's own (Theorem, Proposition, ...)."""
        for entry in self.entries:
            if entry.get('opening'):
                continue
            section = entry['section']
            rows = []
            for node in section.find_all(class_='statement'):
                if node.find_parent(class_='statement') is not None:
                    continue
                label = node.find('p', class_='statement-kind', recursive=False)
                kind = text_of(label) if label is not None else (node.get('data-kind') or '')
                if not kind:
                    continue
                if not node.has_attr('id'):
                    node['id'] = self.fresh_id(f'{entry["id"]}-{slugify(kind, "statement")}')
                after = node.find_next_sibling(True)
                proof = after is not None and after.name == 'details' and 'proof' in (after.get('class') or [])
                rows.append({'id': node['id'], 'kind': kind, 'proof': proof})
                self.id_section[node['id']] = entry['id']
            self.statement_index[entry['id']] = rows

    def anchors(self, root):
        """Within a link list, the in-page targets in order, as (id, link html)."""
        found = []
        for a in root.find_all('a', href=True):
            href = a['href']
            if not href.startswith('#') or href.startswith('#term-') or 'term' in (a.get('class') or []):
                continue
            target = unquote(href[1:])
            if target in self.ids and target not in [t for t, _ in found]:
                found.append((target, a.decode_contents()))
        return found

    def result_idents(self):
        """Each group of ranked results with its band, its anchor and its items' anchors."""
        out, seen = [], {}
        for key in ('breakthroughs', 'obstructions'):
            data = self.ranked.get(key)
            if not data:
                continue
            for group in data['groups']:
                band = 'breakthroughs' if group['kind'] == 'breakthrough' else 'obstructions'
                seen[band] = seen.get(band, 0) + 1
                ident = band if seen[band] == 1 else f'{band}-group-{seen[band]}'
                out.append((data, group, band, ident,
                            [f'{ident}-{n}' for n in range(1, len(group['items']) + 1)]))
        return out

    def model_results(self):
        """The ranked results, each with the status its own lines state."""
        results = []
        self.result_groups = []
        for data, group, band, ident, item_ids in self.result_idents():
            kind = group['kind']
            heading = group['heading']
            title = heading.decode_contents() if heading is not None else data['title']
            record = {'ident': ident, 'band': band, 'kind': kind, 'title': title,
                      'title_text': text_of(parse(title)), 'intro': group['intro'], 'items': []}
            self.result_groups.append(record)
            for n, item in enumerate(group['items'], 1):
                lines = self.item_lines(item)
                head = item['heading'].decode_contents().strip() if item['heading'] is not None else ''
                rank = None
                found = RANK.match(head)
                if found:
                    rank, head = found.group(1), head[found.end():]
                rid = f'{ident}-{n}'
                status = []
                for k, label, _ in lines:
                    if k == 'proved' and PROVED_LABEL.match(label.casefold()) and 'proved' not in status:
                        status.append('proved')
                    if k == 'checked' and 'checked' not in status:
                        status.append('checked')
                brief = ''
                for k, label, value in lines:
                    if k == 'proved':
                        brief = brief_html(source_brief(value))
                        break
                reads, builds, refers = [], [], []
                for k, label, value in lines:
                    targets = self.anchors(parse(value))
                    if k == 'read':
                        reads += [t for t in targets if t not in reads]
                    elif k == 'builds':
                        builds += [t for t, _ in targets if t not in builds]
                    else:
                        refers += [t for t, _ in targets if t not in refers]
                lead = next(((label, value) for k, label, value in lines if k == 'achieved'), None)
                if lead is None:
                    lead = next(((label, value) for k, label, value in lines if k not in ('read',)), None)
                entry = {'id': rid, 'kind': kind, 'band': band, 'n': n,
                         'rank': (rank or str(n)) if kind == 'breakthrough' else None,
                         'head': head, 'head_text': text_of(parse(head)) if head else '',
                         'lines': lines, 'lead': lead, 'extra': item['extra'],
                         'status': status, 'brief': brief, 'reads': reads,
                         'builds': builds, 'refers': refers}
                record['items'].append(entry)
                results.append(entry)
        self.results = results
        # Open problems: each heading in the open problems section, with what its words link to.
        part = self.open_part
        if part is not None:
            heads = [h for h in part.find_all(HEADING) if h.name != 'h2' and h.has_attr('id')]
            top = min((int(h.name[1]) for h in heads), default=3)
            heads = [h for h in heads if int(h.name[1]) == top]
            for h in heads:
                builds, refers = [], []
                node = h.find_next_sibling(True)
                while node is not None and not (HEADING.match(node.name) and int(node.name[1]) <= top):
                    text = text_of(node)
                    targets = [t for t, _ in self.anchors(node)]
                    if re.match(r'^(?:builds on|uses|depends on|relies on|extends|requires)\s*:', text, re.I):
                        builds += [t for t in targets if t not in builds]
                    else:
                        refers += [t for t in targets if t not in refers]
                    node = node.find_next_sibling(True)
                self.problems_open.append({'id': h['id'], 'title': h.decode_contents(),
                                           'title_text': text_of(h), 'builds': builds, 'refers': refers,
                                           'status': ['open']})
        declared = sum(len(r['builds']) for r in self.results + self.problems_open)
        if self.results and not declared:
            self.map_notes.append('map: no result or open problem has a "Builds on" line, so the map draws '
                                  'no arrows between results; a "Builds on" line linking other items draws them')

    def strip_internal_attributes(self, root):
        for node in root.find_all(True):
            for attr in list(node.attrs):
                if attr.startswith('data-') and attr not in KEEP_DATA:
                    del node[attr]

    def section_heads(self):
        n = 0
        for entry in self.entries:
            section = entry['section']
            section['class'] = list(dict.fromkeys((section.get('class') or []) + ['sec', 'chapter']))
            if section.has_attr('data-toc'):
                del section['data-toc']
            if entry['label'] is None:
                section['class'] = section['class'] + ['lead']
                continue
            if entry.get('opening'):
                section['class'] = section['class'] + ['opening']
                continue
            n += 1
            eyebrow = section.find(class_='eyebrow')
            label = text_of(eyebrow) if eyebrow is not None else entry['label']
            if eyebrow is not None:
                eyebrow.decompose()
            heading = section.find(HEADING)
            if heading is not None and text_of(heading) == label:
                label = ''
            head = parse(f'<p class="eyebrow" data-no-terms><span class="num">{n}</span>'
                         f'{html.escape(label)}</p>').p
            section.insert(0, head)

    # ------------------------------------------------------------------ build
    def run(self):
        self.read()
        self.structure()
        self.assign_ids()
        self.toc()
        self.wirer = Wirer(self.cards, self.problems)
        self.definitions()
        for entry in self.entries:
            section = entry['section']
            self.links(section, entry['label'])
            self.explicit_terms(section, entry['label'])
            self.statements(section)
        self.collect_statements()
        self.links(self.hero, 'hero')
        self.check_ranked()
        for key, part in self.opening.items():
            self.links(part, key)
            self.explicit_terms(part, key)
            self.statements(part)
        self.board()
        self.links(self.board_html, 'status')
        self.explicit_terms(self.board_html, 'status')
        for key, tree in self.cards.trees.items():
            self.links(tree, f'card {key[0]}')
            self.explicit_terms(tree, f'card {key[0]}')

        def body_scope(node):
            for parent in node.parents:
                if isinstance(parent, Tag) and parent.name == 'section' and \
                        'chapter' in (parent.get('class') or []):
                    return parent.get('id')
            return 'top'

        self.section_heads()
        self.wired = 0
        for section in self.sections:
            self.wired += self.wirer.wire(section, body_scope)
        self.wired += self.wirer.wire(self.hero, lambda node: 'hero')
        if 'subject' in self.opening:
            self.wired += self.wirer.wire(self.opening['subject'], lambda node: 'subject')
        for data in self.ranked.values():
            for group in data['groups']:
                for root in group['intro']:
                    self.wired += self.wirer.wire(root, lambda node, g=group: id(g), first_only=True)
                for item in group['items']:
                    seen = set()
                    roots = ([item['heading']] if item['heading'] is not None else []) + item['lists'] + item['extra']
                    for root in roots:
                        self.wired += self.wirer.wire(root, lambda node, it=item: id(it), first_only=True, seen=seen)
        for item in self.board_html.find_all('li', class_='st-item'):
            self.wired += self.wirer.wire(item, lambda node, item=item: id(item), first_only=True)
        for ident in self.cards.order:
            seen = set()
            for field in ('definition', 'motivation', 'context'):
                tree = self.cards.trees.get((ident, field))
                if tree is not None:
                    self.wirer.wire(tree, lambda node: ident, skip={ident}, first_only=True, seen=seen)
        for section in self.sections:
            self.strip_internal_attributes(section)
        self.strip_internal_attributes(self.board_html)
        for tree in self.cards.trees.values():
            self.strip_internal_attributes(tree)
            wrap_display_math(tree)
        wrap_display_math(self.board_html)
        wrap_display_math(self.hero)
        for part in self.opening.values():
            self.strip_internal_attributes(part)
            wrap_display_math(part)
        for root in [self.hero, self.board_html, *self.opening.values(), *self.sections, *self.cards.trees.values()]:
            keep_punctuation(root)
        self.model_results()
        self.open_problems_view()
        self.warnings += self.map_notes
        self.glossary_html = self.glossary()
        return self.assemble()

    def hero_html(self):
        """The title lines of the first screen (the cover adds the ranked results beneath)."""
        hero = self.hero
        title = hero.find('h1')
        if title is None:
            self.problems.append(('the report has no title', 'h1'))
        eyebrow = hero.find(attrs={'data-role': 'eyebrow'})
        dek = hero.find(attrs={'data-role': 'dek'})
        state = hero.find(attrs={'data-role': 'state'})
        if self.opening_doc is not None:
            if 'subject' not in self.opening:
                self.missing_words.append('the subject paragraphs under the opening\'s title')
        else:
            if dek is None:
                self.missing_words.append('the one-line description under the title (data-role="dek")')
            if state is None:
                self.missing_words.append('the one-line current state under the title (data-role="state")')
        self.title_text = text_of(title) if title is not None else self.page['slug']
        self.dek_text = text_of(dek) if dek is not None else ''
        if not self.dek_text and 'subject' in self.opening:
            first = self.opening['subject'].find('p')
            self.dek_text = text_of(first) if first is not None else ''
        # The text of linked words is joined with spaces; punctuation closes up to its word.
        self.dek_text = re.sub(r'\s+([.,;:!?)])', r'\1', self.dek_text)
        date = self.status['date']
        parts = ['<div class="hero">']
        top = []
        if eyebrow is not None:
            top.append(f'<span class="hero-eyebrow">{eyebrow.decode_contents()}</span>')
        if date:
            top.append(f'<time class="hero-date" datetime="{date.isoformat()}">{long_date(date)}</time>')
        if top:
            parts.append('<p class="hero-top">' + '<span class="hero-sep" aria-hidden="true"> · </span>'.join(top) + '</p>')
        parts.append(f'<h1 class="title">{title.decode_contents() if title is not None else ""}</h1>')
        if dek is not None:
            parts.append(f'<p class="hero-dek">{dek.decode_contents()}</p>')
        if state is not None:
            parts.append(f'<p class="hero-state">{state.decode_contents()}</p>')
        parts.append(self.subject_html())
        if self.has_board and not self.ranked:
            parts.append(self.tally_html())
        parts.append('</div>')
        return ''.join(parts)

    def cover_html(self):
        """The first screen: the title, the subject, then the breakthroughs in rank order with
        their status, and the obstructions by name."""
        hero = self.hero_html()
        cover_group = next((g for g in self.result_groups if g['kind'] == 'breakthrough' and g['items']), None)
        self.cover_group = cover_group
        ranked = self.ranked_section(cover_group, cover=True) if cover_group is not None else ''
        strip = self.strip_html() if cover_group is not None else ''
        jump = self.jump_html(cover_group)
        return f'<header class="cover" id="top">{hero}{ranked}{strip}{jump}</header>'

    def toc_html(self):
        lab = self.labels
        rows = []
        marks = defaultdict(list)
        for r in self.results:
            for t, _ in r['reads']:
                sid = self.id_section.get(t)
                if sid and r not in marks[sid]:
                    marks[sid].append(r)
        for g in self.result_groups:
            rows.append(f'<li class="toc-opening"><a href="#{g["ident"]}">{html.escape(g["title_text"])}</a></li>')
        for entry in self.entries:
            if entry.get('opening') and entry['label']:
                rows.append(f'<li class="toc-opening"><a href="#{entry["id"]}">{html.escape(entry["label"])}</a></li>')
        if self.results:
            rows.append(f'<li class="toc-opening"><a href="#map">{html.escape(lab["map"])}</a></li>')
        if self.has_board:
            rows.append(f'<li><a href="#status">{html.escape(lab["status"])}</a></li>')
        first = True
        for entry in self.entries:
            if entry['label'] is None or entry.get('opening'):
                continue
            n = self.section_number[entry['id']]
            sub = ''
            if entry['children']:
                sub = '<ol class="sub">' + ''.join(
                    f'<li><a href="#{cid}">{html.escape(label)}</a></li>' for cid, label in entry['children']) + '</ol>'
            mk = ''
            for r in marks.get(entry['id'], []):
                if r['kind'] == 'breakthrough':
                    mk += f'<span class="mk mk-b" aria-hidden="true">{html.escape(r["rank"])}</span>'
                else:
                    mk += f'<span class="mk mk-o" aria-hidden="true">{glyph("failing")}</span>'
                mk += f'<span class="visually-hidden">, {html.escape(r["head_text"])}</span>'
            count = len(self.statement_index.get(entry['id']) or [])
            if count:
                mk += '<span class="mk-st" aria-hidden="true">' + '<i></i>' * min(count, 4) + '</span>'
            cls = ' class="toc-first"' if first else ''
            first = False
            rows.append(f'<li data-section="{entry["id"]}"{cls}><a href="#{entry["id"]}"><span class="num">{n}'
                        f'</span><span class="toc-text">{html.escape(entry["label"])}</span>'
                        + (f'<span class="toc-marks">{mk}</span>' if mk else '') + f'</a>{sub}</li>')
        rows.append(f'<li class="toc-terms"><a href="#terms">{html.escape(lab["terms"])}'
                    f'<span class="toc-count">{len(self.cards.order)}</span></a></li>')
        return (f'<nav class="toc" id="contents" aria-label="{html.escape(lab["contents"])}">'
                f'<p class="toc-label">{html.escape(lab["contents"])}</p><ol>{"".join(rows)}</ol></nav>')

    def heading_anchors(self):
        """Every heading in the report, and every statement, carries a link to itself."""
        label = html.escape(self.labels['anchor'], quote=True)
        for section in self.sections:
            for heading in section.find_all(['h2', 'h3', 'h4']):
                if heading.has_attr('id') and not heading.find('a', class_='hl'):
                    heading.append(parse(f'<a class="hl" href="#{heading["id"]}" aria-label="{label}">#</a>').a)
            for statement in section.find_all(class_='statement'):
                kind = statement.find('p', class_='statement-kind', recursive=False)
                if statement.has_attr('id') and kind is not None and not kind.find('a', class_='hl'):
                    kind.append(parse(f'<a class="hl" href="#{statement["id"]}" aria-label="{label}">#</a>').a)

    def finder_html(self):
        lab = self.labels
        return (f'<div class="finder" id="finder" role="dialog" aria-modal="true" aria-labelledby="finder-title" hidden>'
                f'<div class="finder-panel"><h2 class="visually-hidden" id="finder-title">{html.escape(lab["search"])}</h2>'
                f'<div class="finder-field">{icon("search")}'
                f'<input id="finder-input" type="search" role="combobox" aria-expanded="true" aria-controls="finder-list" '
                f'aria-autocomplete="list" autocomplete="off" spellcheck="false" '
                f'placeholder="{html.escape(lab["search_placeholder"], quote=True)}" '
                f'aria-label="{html.escape(lab["search"], quote=True)}">'
                f'<button class="finder-close" type="button" aria-label="{html.escape(lab["close"], quote=True)}">'
                f'<kbd>Esc</kbd></button></div>'
                f'<div class="finder-body"><ul id="finder-list" role="listbox" aria-label="{html.escape(lab["search"], quote=True)}"></ul>'
                f'<p class="finder-status" id="finder-status" role="status" aria-live="polite"></p></div></div></div>')

    def assemble(self):
        page, lab = self.page, self.labels
        self.heading_anchors()
        cover = self.cover_html()
        others = ''.join(self.ranked_section(g) for g in self.result_groups
                         if g is not self.cover_group and g['items'])
        opening = others + ''.join(s.decode() for s in self.opening_sections)
        body = ''.join(section.decode() for section in self.sections
                       if not any(section is s for s in self.opening_sections))
        board = self.board_html.decode() if self.has_board else ''
        figure = self.map_html()
        css = (HERE / 'tracker.css').read_text(encoding='utf-8')
        js = (HERE / 'tracker.js').read_text(encoding='utf-8')
        keys = ('close', 'back', 'show_all', 'show_fewer', 'no_match', 'search_none', 'search_results',
                'search_sections', 'search_statements', 'search_terms', 'copied', 'theme', 'terms_shown')
        config = json.dumps({k: lab[k] for k in keys}, ensure_ascii=False)
        fontface = ''
        self.font_bytes = 0
        if self.math_font is not None:
            woff, count = subset_math_font(cover + opening + figure + body + str(self.glossary_html) + board,
                                           self.math_font)
            self.font_bytes = len(woff)
            self.font_chars = count
            fontface = ('@font-face{font-family:"QH Garamond Math";src:url(data:font/woff;base64,' +
                        base64.b64encode(woff).decode('ascii') + ') format("woff");font-display:swap}\n')
        description = html.escape(self.dek_text or self.title_text, quote=True)
        title = html.escape(self.title_text)
        home = html.escape(page['home'], quote=True)
        theme = ("<script>try{var t=localStorage.getItem('qh-theme');"
                 "if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>")
        doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="color-scheme" content="light dark">
<title>{title} — {html.escape(page["author"])}</title>
<meta name="description" content="{description}">
<meta name="author" content="{html.escape(page["author"])}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<link rel="icon" href="data:,">
{theme}
<link rel="stylesheet" href="https://use.typekit.net/zlu2quo.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..800;1,400..800&amp;display=swap">
<style>
{fontface}{css}</style>
</head>
<body>
<a class="skip" href="#main">{html.escape(lab["skip"])}</a>
{symbols()}
<div class="bar" id="bar"><a class="home" href="{home}">{html.escape(page["home_label"])}</a><span class="bar-title" aria-hidden="true">{title}</span><div class="tools"><button class="tool find-button" type="button" aria-haspopup="dialog" aria-controls="finder">{icon("search")}<span class="tool-label">{html.escape(lab["search"])}</span><kbd class="tool-kbd" aria-hidden="true">/</kbd></button><button class="tool theme-toggle" type="button" aria-pressed="false" aria-label="{html.escape(lab["theme"], quote=True)}">{icon("theme")}</button><button class="toc-button" type="button" aria-controls="contents" aria-expanded="false">{icon("contents")}<span>{html.escape(lab["contents"])}</span></button></div><div class="progress" aria-hidden="true"><span></span></div></div>
<main id="main">
{cover}
{figure}
<div class="frame">
{self.toc_html()}
<div class="content">
{opening}
{board}
{body}
{self.glossary_html.decode()}
</div>
</div>
</main>
<footer class="foot">
<p class="author-byline"><strong>{html.escape(page["author"])}</strong></p>
<p class="foot-links"><a href="{home}">raeez.com</a> · <a href="mailto:raeez@momentum.inc">raeez@momentum.inc</a></p>
</footer>
<div class="popcard" id="qh-card" role="dialog" aria-modal="false" aria-labelledby="qh-card-title" hidden>
<div class="pc-head"><button class="pc-back" type="button" hidden><span aria-hidden="true">←</span> <span class="pc-back-name"></span></button><p class="pc-title" id="qh-card-title" tabindex="-1"></p><button class="pc-close" type="button" aria-label="{html.escape(lab["close"])}"><span aria-hidden="true">×</span></button></div>
<div class="pc-body"></div>
</div>
{self.finder_html()}
<p class="toast" id="toast" role="status" aria-live="polite" hidden></p>
<script>
window.QH_LABELS={config};
{js}</script>
</body>
</html>
'''
        # The HTML serialiser lowercases attribute names; SVG needs viewBox.
        return doc.replace(' viewbox="', ' viewBox="')
