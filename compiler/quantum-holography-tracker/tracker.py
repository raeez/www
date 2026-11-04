"""Build the tracker page from an input folder.

The page is one HTML file. Its parts come from three inputs:

    words/REPORT.html or words/REPORT.md   the report, with its hero and status section
    words/STATUS.md                        whether the words are settled, and their date
    cards/TERMS.json                       the term cards

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
        body = '|'.join(re.escape(p).replace(r'\-', '[-‐–]').replace('–', '[-‐–]') for p in patterns)
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
                        parent.has_attr('data-no-terms'):
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


def wrap_display_math(root):
    """Each display formula sits in its own horizontal scroller, so a wide one never widens the page."""
    for math in root.find_all('math', attrs={'display': 'block'}):
        if 'math-wrap' not in (math.parent.get('class') or []):
            math.wrap(Tag(name='span', attrs={'class': 'math-wrap'}))


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


def glyph(state):
    return (f'<svg class="glyph" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
            f'<use href="#g-{state}"/></svg>')


def symbols():
    return ('<svg class="symbols" aria-hidden="true" focusable="false"><defs>' +
            ''.join(f'<symbol id="g-{k}" viewBox="0 0 16 16">{v}</symbol>' for k, v in GLYPHS.items()) +
            '</defs></svg>')


class Build:
    def __init__(self, folder, page, math_font=None):
        self.folder = Path(folder)
        self.page = page
        self.labels = page['labels']
        self.states = [s['id'] for s in page['states']]
        self.state_label = {s['id']: s['label'] for s in page['states']}
        self.math_font = math_font
        self.warnings, self.problems = [], []
        self.pointers, self.attachments, self.external_links = [], [], []
        self.unknown_terms, self.uncarded_dfn, self.relative_links = [], [], []
        self.defining = {}
        self.missing_words = []

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
        self.status = parse_status(words / 'STATUS.md', digests)
        self.renderer = TexRenderer()
        self.cards = Cards(rows, self.renderer, self.warnings, self.problems)
        self.doc = parse(markup)
        self.report_tex = self.renderer.collect(self.doc, 'report')
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
        if self.status_el is None:
            for section in sections:
                board = self.plain_status(section)
                if board is not None:
                    self.status_el = board
                    sections.remove(section)
                    break
        self.sections = sections

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

    def assign_ids(self):
        # Ids the page itself uses; a report id that collides is renamed.
        reserved = {'main', 'status', 'status-title', 'terms', 'terms-title', 'terms-other', 'contents',
                    'qh-card', 'qh-card-title', 'top', 'board-filter', 'bar'}
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
        self.ids = used

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
                            'section': section, 'label_heading': label_heading})
        self.entries = entries
        self.section_label = {e['id']: e['label'] or '' for e in entries}

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
        self.board_items = []
        parts = ['<section id="status" class="board sec" aria-labelledby="status-title">',
                 '<header class="sec-head">']
        if headline:
            parts.append(f'<p class="eyebrow">{html.escape(lab["status"])}</p>')
        parts.append(f'<h2 id="status-title">{headline or html.escape(lab["status"])}</h2>')
        if dek:
            parts.append(f'<p class="dek">{dek}</p>')
        parts.append('</header>')
        parts.append('<div class="board-tools" hidden><label class="filter"><span>'
                     f'{html.escape(lab["filter"])}</span><input id="board-filter" type="search" '
                     'autocomplete="off" spellcheck="false"></label>'
                     f'<p class="filter-none" hidden>{html.escape(lab["no_match"])}</p></div>')
        parts.append('<div class="states">')
        for state in self.states:
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
                  f'<span class="count">{len(order)}</span></h2></header>'
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
            n += 1
            eyebrow = section.find(class_='eyebrow')
            label = text_of(eyebrow) if eyebrow is not None else entry['label']
            if eyebrow is not None:
                eyebrow.decompose()
            heading = section.find(HEADING)
            if heading is not None and text_of(heading) == label:
                label = ''
            head = parse(f'<p class="eyebrow"><span class="num">{n}</span>{html.escape(label)}</p>').p
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
        self.links(self.hero, 'hero')
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
        self.glossary_html = self.glossary()
        return self.assemble()

    def hero_html(self):
        hero = self.hero
        title = hero.find('h1')
        if title is None:
            self.problems.append(('the report has no title', 'h1'))
        eyebrow = hero.find(attrs={'data-role': 'eyebrow'})
        dek = hero.find(attrs={'data-role': 'dek'})
        state = hero.find(attrs={'data-role': 'state'})
        if dek is None:
            self.missing_words.append('the one-line description under the title (data-role="dek")')
        if state is None:
            self.missing_words.append('the one-line current state under the title (data-role="state")')
        self.title_text = text_of(title) if title is not None else self.page['slug']
        self.dek_text = text_of(dek) if dek is not None else ''
        tally = []
        for s in self.states:
            tally.append(f'<li data-state="{s}"><a href="#status-{s}">{glyph(s)}'
                         f'<span class="t-n">{self.board_counts[s]}</span>'
                         f'<span class="t-l">{html.escape(self.state_label[s])}</span></a></li>')
        date = self.status['date']
        parts = ['<header class="hero" id="top">']
        if eyebrow is not None:
            parts.append(f'<p class="eyebrow hero-eyebrow">{eyebrow.decode_contents()}</p>')
        parts.append(f'<h1 class="title">{title.decode_contents() if title is not None else ""}</h1>')
        if dek is not None:
            parts.append(f'<p class="hero-dek">{dek.decode_contents()}</p>')
        if state is not None:
            parts.append(f'<p class="hero-state">{state.decode_contents()}</p>')
        parts.append(f'<ol class="tally" aria-label="{html.escape(self.labels["status"])}">{"".join(tally)}</ol>')
        if date:
            parts.append(f'<p class="hero-date"><time datetime="{date.isoformat()}">{long_date(date)}</time></p>')
        parts.append('</header>')
        return ''.join(parts)

    def toc_html(self):
        lab = self.labels
        rows = [f'<li><a href="#status">{html.escape(lab["status"])}</a></li>']
        n = 0
        for entry in self.entries:
            if entry['label'] is None:
                continue
            n += 1
            sub = ''
            if entry['children']:
                sub = '<ol class="sub">' + ''.join(
                    f'<li><a href="#{cid}">{html.escape(label)}</a></li>' for cid, label in entry['children']) + '</ol>'
            rows.append(f'<li data-section="{entry["id"]}"><a href="#{entry["id"]}"><span class="num">{n}'
                        f'</span>{html.escape(entry["label"])}</a>{sub}</li>')
        rows.append(f'<li><a href="#terms">{html.escape(lab["terms"])}</a></li>')
        return (f'<nav class="toc" id="contents" aria-label="{html.escape(lab["contents"])}">'
                f'<p class="toc-label">{html.escape(lab["contents"])}</p><ol>{"".join(rows)}</ol></nav>')

    def assemble(self):
        page, lab = self.page, self.labels
        hero = self.hero_html()
        body = ''.join(section.decode() for section in self.sections)
        css = (HERE / 'tracker.css').read_text(encoding='utf-8')
        js = (HERE / 'tracker.js').read_text(encoding='utf-8')
        config = json.dumps({k: lab[k] for k in ('close', 'back', 'show_all', 'show_fewer', 'no_match')},
                            ensure_ascii=False)
        fontface = ''
        self.font_bytes = 0
        if self.math_font is not None:
            woff, count = subset_math_font(hero + body + str(self.glossary_html) + str(self.board_html),
                                           self.math_font)
            self.font_bytes = len(woff)
            self.font_chars = count
            fontface = ('@font-face{font-family:"QH Garamond Math";src:url(data:font/woff;base64,' +
                        base64.b64encode(woff).decode('ascii') + ') format("woff");font-display:swap}\n')
        date = self.status['date']
        description = html.escape(self.dek_text or self.title_text, quote=True)
        title = html.escape(self.title_text)
        home = html.escape(page['home'], quote=True)
        doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>{title} — {html.escape(page["author"])}</title>
<meta name="description" content="{description}">
<meta name="author" content="{html.escape(page["author"])}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<link rel="icon" href="data:,">
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
<div class="bar" id="bar"><a class="home" href="{home}">{html.escape(page["home_label"])}</a><span class="bar-title" aria-hidden="true">{title}</span><button class="toc-button" type="button" aria-controls="contents" aria-expanded="false">{html.escape(lab["contents"])}</button></div>
<div class="frame">
{self.toc_html()}
<main id="main">
{hero}
{self.board_html.decode()}
{body}
{self.glossary_html.decode()}
</main>
</div>
<footer class="foot">
<p class="author-byline"><strong>{html.escape(page["author"])}</strong></p>
<p class="foot-links"><a href="{home}">raeez.com</a> · <a href="mailto:raeez@momentum.inc">raeez@momentum.inc</a></p>
</footer>
<div class="popcard" id="qh-card" role="dialog" aria-modal="false" aria-labelledby="qh-card-title" hidden>
<div class="pc-head"><button class="pc-back" type="button" hidden><span aria-hidden="true">←</span> <span class="pc-back-name"></span></button><p class="pc-title" id="qh-card-title" tabindex="-1"></p><button class="pc-close" type="button" aria-label="{html.escape(lab["close"])}"><span aria-hidden="true">×</span></button></div>
<div class="pc-body"></div>
</div>
<script>
window.QH_LABELS={config};
{js}</script>
</body>
</html>
'''
        # The HTML serialiser lowercases attribute names; SVG needs viewBox.
        return doc.replace(' viewbox="', ' viewBox="')
