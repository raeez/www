"""The status page of the quantum holography programme, built from one structured content file.

Input folder (default content/quantum-holography-status):
    content.json   the words: lead, status key, principal results, the grid of examples,
                   open problems and the glossary (format in that folder's README.md)
    essay.md       the essay, reproduced whole: a '# Title' line, then paragraphs
    page.json      interface labels and page metadata (the designer's)

The output is one self-contained HTML file: TeX is turned into MathML at build time
(Temml, vendored), the text and math fonts are embedded as subsets, and the page makes
no request to any other host.
"""
import base64
import hashlib
import html
import io
from html.parser import HTMLParser
import json
import re
import subprocess
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEX2MATHML = HERE.parent / 'quantum-holography-tracker' / 'tex2mathml.cjs'

# 'refuted form' is a checked scoped negative result (the atlas's scoped_negative): the statement as first posed fails,
# and the statement says where. It is its own status, never read as open.
STATEMENT_STATUSES = ['checked', 'refuted form', 'pending', 'conditional', 'conjecture', 'heuristic', 'open', 'published']
# Statuses whose statements show their novelty (new, known): results that carry a proof, positive or negative.
NOVELTY_STATUSES = ('checked', 'refuted form', 'pending')
CELL_STATUSES = ['checked', 'partial', 'pending', 'published', 'open', 'not posed', 'refuted form']
COLUMNS = ['object', 'dual', 'modules', 'fusion', 'bulk', 'lines', 'states', 'dictionary']

# Each status has its own shape as well as its own colour, so that the marks read in
# monochrome, in print and for readers who do not separate the colours. No two marks form a series of fills
# (empty, quarter, half, full), which would read as a fraction of a proof: a proposed result is a solid diamond
# (the conjecture's diamond, filled: a proof is claimed), a partly established one a solid triangle. The solid marks
# share the disc's box, and the disc carries the most ink, so a proved result reads as the strongest mark.
MARKS = {
    'checked': '<circle cx="8" cy="8" r="5.6" fill="currentColor"/>',
    'pending': '<path d="M8 2.4 13.6 8 8 13.6 2.4 8z" fill="currentColor"/>',
    'partial': '<path d="M8 2.6 13.3 11.8H2.7z" fill="currentColor" stroke="currentColor" stroke-width="1.2" '
               'stroke-linejoin="round"/>',
    'conditional': '<circle cx="8" cy="8" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/>'
                   '<circle cx="8" cy="8" r="2.2" fill="currentColor"/>',
    'conjecture': '<path d="M8 2.2 13.8 8 8 13.8 2.2 8z" fill="none" stroke="currentColor" stroke-width="1.6" '
                  'stroke-linejoin="round"/>',
    'heuristic': '<circle cx="8" cy="8" r="5" fill="none" stroke="currentColor" stroke-width="1.6" '
                 'stroke-dasharray="2.2 1.9"/>',
    'open': '<circle cx="8" cy="8" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/>',
    'published': '<rect x="3.2" y="3.2" width="9.6" height="9.6" rx="1.2" fill="none" stroke="currentColor" '
                 'stroke-width="1.6"/><path d="M5.8 6.4h4.4M5.8 9.6h4.4" stroke="currentColor" stroke-width="1.4"/>',
    'not posed': '<path d="M5 8h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
    'refuted form': '<path d="M4.6 4.6 11.4 11.4M11.4 4.6 4.6 11.4" stroke="currentColor" stroke-width="1.7" '
                    'stroke-linecap="round"/>',
}

ICONS = {
    'theme': '<circle cx="8" cy="8" r="5.6" fill="none" stroke="currentColor" stroke-width="1.4"/>'
             '<path d="M8 2.4a5.6 5.6 0 0 1 0 11.2z" fill="currentColor"/>',
    'arrow': '<path d="M3 8h9.2M8.8 4.4 12.4 8l-3.6 3.6" fill="none" stroke="currentColor" stroke-width="1.4" '
             'stroke-linecap="round" stroke-linejoin="round"/>',
    'up': '<path d="M8 13V3.6M4.4 7.2 8 3.6l3.6 3.6" fill="none" stroke="currentColor" stroke-width="1.4" '
          'stroke-linecap="round" stroke-linejoin="round"/>',
    'chevron': '<path d="m5 6.5 3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.5" '
               'stroke-linecap="round" stroke-linejoin="round"/>',
    'search': '<circle cx="6.8" cy="6.8" r="4.5" fill="none" stroke="currentColor" stroke-width="1.5"/>'
              '<path d="M10.2 10.2 13.8 13.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>',
}


def slug(cls):
    return cls.replace(' ', '-')


def mark(status, label=None):
    title = f'<title>{html.escape(label)}</title>' if label else ''
    hidden = '' if label else ' aria-hidden="true"'
    role = ' role="img"' if label else ''
    aria = f' aria-label="{html.escape(label)}"' if label else ''
    return (f'<svg class="mark mark-{slug(status)}" viewBox="0 0 16 16" width="16" height="16"'
            f'{hidden}{role}{aria} focusable="false">{title}{MARKS[status]}</svg>')


def icon(name):
    return (f'<svg class="icon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true" '
            f'focusable="false">{ICONS[name]}</svg>')


def ident(text):
    text = unicodedata.normalize('NFKD', text)
    text = re.sub(r'[^\w\s-]', '', text.encode('ascii', 'ignore').decode()).strip().lower()
    return re.sub(r'[\s_-]+', '-', text)[:60] or 'x'


class Math:
    """Collects TeX, renders it once through Temml, and substitutes the MathML."""

    def __init__(self):
        self.jobs = []
        self.errors = []
        self.text_jobs = {}  # TeX -> the one job that gives its text form

    def add(self, tex, display):
        self.jobs.append({'tex': tex, 'display': display})
        return f'\x00M{len(self.jobs) - 1}\x00'

    def add_text(self, tex):
        """A placeholder for the formula's rendered token text (no markup, no TeX), for attributes and titles."""
        if tex not in self.text_jobs:
            self.jobs.append({'tex': tex, 'display': False})
            self.text_jobs[tex] = len(self.jobs) - 1
        return f'\x00T{self.text_jobs[tex]}\x00'

    def render(self):
        if not self.jobs:
            self.out = []
            return
        result = subprocess.run(['node', str(TEX2MATHML)], input=json.dumps(self.jobs),
                                capture_output=True, text=True, check=True)
        self.out = json.loads(result.stdout)
        for job, row in zip(self.jobs, self.out):
            if 'error' in row:
                self.errors.append({'tex': job['tex'], 'error': row['error']})

    def substitute(self, markup, escape_text=True):  # noqa: C901
        def one(m):
            kind, i = m.group(1), int(m.group(2))
            row = self.out[i]
            if kind == 'T':
                text = self.jobs[i]['tex'] if 'html' not in row else math_text(row['html'])
                text = ' '.join(text.split())
                return html.escape(text, quote=True) if escape_text else text
            if 'html' not in row:
                return f'<code class="tex-error">{html.escape(self.jobs[i]["tex"])}</code>'
            out = row['html']
            if self.jobs[i]['display']:
                # The print sheet sets a wide display formula smaller so that it fits the page: the build
                # writes its estimated width (em) as --fw on the formulas that may need it.
                width = mathml_width(out)
                if width > WIDE_FORMULA_EM:
                    out = out.replace('style="display:block math;"', f'style="display:block math;--fw:{width:.1f}"', 1)
            return out
        return re.sub(r'\x00([MT])(\d+)\x00', one, markup)


# Display formulas estimated wider than this (in em) carry --fw for the print sheet. The estimate below,
# compared with Chrome's rendering of the 54 display formulas of the 16 November 2026 content, gives
# rendered/estimated widths from 0.62 to 1.10 (median 0.82); only formulas near or above the page width
# are affected by the print rule.
WIDE_FORMULA_EM = 38.0


class _MathTree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = {'tag': '#', 'attrs': {}, 'kids': [], 'text': ''}
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = {'tag': tag, 'attrs': dict(attrs), 'kids': [], 'text': ''}
        self.stack[-1]['kids'].append(node)
        if tag not in ('mspace', 'none', 'mprescripts'):
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1]['kids'].append({'tag': tag, 'attrs': dict(attrs), 'kids': [], 'text': ''})

    def handle_endtag(self, tag):
        for k in range(len(self.stack) - 1, 0, -1):
            if self.stack[k]['tag'] == tag:
                del self.stack[k:]
                break

    def handle_data(self, data):
        self.stack[-1]['text'] += data


def mathml_width(markup):
    """An estimate of a MathML formula's rendered width in em, from its tree: glyph counts for tokens,
    the wider part of fractions and stacked scripts, scripts at reduced size, spacing around operators."""
    def w(n, scale=1.0):
        tag, text, kids = n['tag'], n['text'].strip(), n['kids']
        if tag in ('annotation', 'annotation-xml'):
            return 0.0
        if tag == 'mtext':
            return 0.48 * len(n['text']) * scale
        if tag in ('mi', 'mn', 'ms'):
            if tag == 'mi' and len(text) > 1:
                return 0.5 * len(text) * scale
            return sum(0.55 if ch.isascii() and ch.islower() else 0.62 for ch in text) * scale
        if tag == 'mo':
            big = n['attrs'].get('largeop') == 'true' or (text and text in '∑∫∏⨁⋃⋂∮')
            space = 0.3 if text in (',', ';') else 0.0 if n['attrs'].get('form') in ('prefix', 'postfix') or text in '()[]{}|' else 0.5
            return (len(text) * (1.0 if big else 0.62) + space) * scale
        if tag == 'mspace':
            m = re.match(r'([\d.]+)em', n['attrs'].get('width', ''))
            return (float(m.group(1)) if m else 0.3) * scale
        if tag == 'mfrac' and len(kids) >= 2:
            return max(w(kids[0], scale * 0.9), w(kids[1], scale * 0.9)) + 0.3 * scale
        if tag in ('msub', 'msup') and len(kids) >= 2:
            return w(kids[0], scale) + 0.72 * w(kids[1], scale)
        if tag == 'msubsup' and len(kids) >= 3:
            return w(kids[0], scale) + 0.72 * max(w(kids[1], scale), w(kids[2], scale))
        if tag in ('munder', 'mover', 'munderover') and kids:
            return max([w(kids[0], scale)] + [0.72 * w(k, scale) for k in kids[1:]])
        if tag == 'msqrt':
            return sum(w(k, scale) for k in kids) + 0.9 * scale
        if tag == 'mroot' and len(kids) >= 2:
            return w(kids[0], scale) + 0.9 * scale + 0.5 * w(kids[1], scale)
        if tag == 'mtable':
            return max([w(k, scale) for k in kids] or [0.0])
        if tag == 'mtr':
            return sum(w(k, scale) for k in kids) + 0.8 * scale * max(len(kids) - 1, 0)
        if tag == 'semantics':
            return w(kids[0], scale) if kids else 0.0
        return sum(w(k, scale) for k in kids)
    tree = _MathTree()
    tree.feed(markup)
    return w(tree.root)


MATH_RE = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]', re.S)


class _MathText(HTMLParser):
    """Reads Temml's MathML into text that keeps the structure a reader needs: base_sub, base^sup,
    (num)/(den), √x. The TeX annotation is skipped; invisible parts are dropped."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = [['root', []]]
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if self.skip or tag in ('annotation', 'annotation-xml', 'mphantom'):
            self.skip += 1
            return
        self.stack.append([tag, []])

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1
            return
        if len(self.stack) > 1:
            name, parts = self.stack.pop()
            self.stack[-1][1].append(_math_join(name, parts))

    def handle_data(self, data):
        if not self.skip:
            self.stack[-1][1].append(data)


def _math_group(s):
    s = s.strip()
    return s if len(s) <= 1 else f'({s})'


def _math_join(name, parts):
    kids = [p for p in parts if p.strip()]
    if name == 'msub' and len(kids) == 2:
        return f'{kids[0]}_{_math_group(kids[1])}'
    if name == 'msup' and len(kids) == 2:
        return f'{kids[0]}^{_math_group(kids[1])}'
    if name == 'msubsup' and len(kids) == 3:
        return f'{kids[0]}_{_math_group(kids[1])}^{_math_group(kids[2])}'
    if name == 'mfrac' and len(kids) == 2:
        return f'{_math_group(kids[0])}/{_math_group(kids[1])}'
    if name == 'msqrt':
        return '√' + _math_group(''.join(kids))
    if name == 'mroot' and len(kids) == 2:
        return f'{_math_group(kids[1])}√{_math_group(kids[0])}'
    if name == 'mspace':
        return ' '
    return ''.join(parts)


def math_text(markup):
    """Plain text of rendered MathML, for attributes and titles: C_2, T^2, q^(1/2), p/q; never TeX."""
    parser = _MathText()
    parser.feed(markup)
    parser.close()
    return ''.join(parser.stack[0][1])
LINK_RE = re.compile(r'\[([^\[\]]+)\]\((https?://[^\s)]+)\)')
ARXIV_RE = re.compile(r'arxiv\.org/(?:abs|html|pdf)/((?:math|hep-th|math-ph|alg-geom|q-alg)/\d{7}|\d{4}\.\d{4,5})(v\d+)?', re.I)


def unlink(text):
    """[label](url) -> label, followed by its arXiv number when the address has one.

    The page makes no reference to another host, so citations are given as text."""
    def one(m):
        label, url = m.group(1), m.group(2)
        a = ARXIV_RE.search(url)
        if a and a.group(1) not in label:
            return f'{label} (arXiv:{a.group(1)}{a.group(2) or ""})'
        return label
    return LINK_RE.sub(one, text or '')
EMPH_RE = re.compile(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])')


class Terms:
    """Attaches glossary definitions to the first use of each term in a block of text."""

    def __init__(self, glossary):
        self.by_form = {}
        self.entries = []
        self.problems = []
        # An entry's own id is its anchor and is reserved first; anchors derived from terms avoid it.
        explicit = ['term-' + ident(e['id']) for e in glossary if (e.get('id') or '').strip()]
        for dup in sorted({t for t in explicit if explicit.count(t) > 1}):
            self.problems.append(f'glossary: two entries have the id anchor {dup}')
        taken = set(explicit)
        for entry in glossary:
            if (entry.get('id') or '').strip():
                tid = 'term-' + ident(entry['id'])
            else:
                tid = base = 'term-' + ident(entry['term'])
                if base in explicit:
                    self.problems.append(f'glossary: the anchor {base} of the term "{entry["term"]}" is taken by another '
                                         f'entry\'s id; give one of them a different id')
                n = 2
                while tid in taken:
                    tid = f'{base}-{n}'
                    n += 1
                taken.add(tid)
            entry = dict(entry, id=tid)
            self.entries.append(entry)
            forms = set(entry.get('forms') or []) | {entry['term']}
            for form in forms:
                form = form.strip()
                if len(form) >= 3:
                    self.by_form.setdefault(form.lower(), tid)
        forms = sorted(self.by_form, key=len, reverse=True)
        self.regex = None
        if forms:
            alternatives = '|'.join(re.escape(html.escape(f, quote=False)) for f in forms)
            self.regex = re.compile(r'(?<![\w>-])(' + alternatives + r')(?![\w-])', re.I)
        self.used = {}

    def link(self, escaped_text, seen):
        if not self.regex:
            return escaped_text

        def one(m):
            tid = self.by_form.get(html.unescape(m.group(1)).lower())
            if not tid or tid in seen:
                return m.group(0)
            seen.add(tid)
            self.used[tid] = self.used.get(tid, 0) + 1
            return (f'<button type="button" class="term" data-term="{tid}" aria-haspopup="dialog" '
                    f'aria-expanded="false" aria-controls="card">{m.group(1)}</button>')
        return self.regex.sub(one, escaped_text)


# Classes that status.js or the page layout bind; the atlas uses its own (atlas-*) classes.
# The classes that ctx.rich() and ctx.mark() emit (term, math-inline, math-long, math-display, nobr, mark) are not reserved:
# status.js handles them correctly anywhere on the page.
ATLAS_RESERVED_CLASSES = frozenset({
    'grid', 'card', 'card-inner', 'filter', 'filters', 'row', 'rows', 'row-name', 'statement', 'statement-head',
    'statement-title', 'status-chip', 'question', 'question-ask', 'questions', 'known', 'fold', 'failure', 'claim-text',
    'open-group', 'col-def', 'gloss', 'theme', 'nav', 'find', 'tally', 'cell-btn', 'col-head'})


class AtlasContext:
    """What the atlas renderer may use from the page: its text renderer, its status marks, its labels
    and the anchors of the statements already on the page. The renderer receives nothing else."""

    def __init__(self, build):
        self._build = build
        self.labels = build.page['labels']
        self.status_labels = build.page['status_labels']

    def rich(self, text, terms=True):
        """Plain text with TeX and *emphasis* to HTML, through the page's own renderer."""
        return self._build.rich(text, terms=terms)

    def mark(self, status, label=None):
        return mark(status, label) if status in MARKS else ''

    @property
    def anchors(self):
        return frozenset(self._build.anchors)

    def anchor_for(self, statement_id):
        """'#s-…' when a statement with this content id is on the page, else None."""
        sid = 's-' + ident(statement_id or '')
        return '#' + sid if statement_id and sid in self._build.anchors else None

    @staticmethod
    def claim_anchor(claim_id):
        """The id the atlas gives the element of a claim ('atlas-claim-…'); a statement of the page whose content names
        this claim (atlasClaimId) links to it when the atlas draws it."""
        return 'atlas-claim-' + ident(claim_id or '')

    def question_anchor(self, question_id):
        """'#q-…' when a question card with this content id is on the page, else None."""
        qid = 'q-' + ident(question_id or '')
        return '#' + qid if question_id and qid in self._build.anchors else None

    ident = staticmethod(ident)


class Build:
    def __init__(self, folder, page, text_fonts=None, math_font=None, atlas_module=None):
        self.folder = Path(folder)
        self.page = page
        self.text_fonts = text_fonts or {}
        self.math_font = math_font
        self.atlas_module = Path(atlas_module) if atlas_module else HERE / 'atlas.py'
        self.math = Math()
        self.problems = []
        self.warnings = []
        self.anchors = set()
        self.links = []
        self.atlas_assets = {'css': '', 'js': ''}
        # The monograph (monograph.py): when the input folder holds the author's reader-data/manifest.json, the page is
        # the book, and every section built below is kept whole, with its ids, as the book's reference sections.
        manifest = self.folder / 'reader-data' / 'manifest.json'
        self.reader_manifest = manifest if manifest.exists() else None
        self.book = None

    # Text -------------------------------------------------------------------------------

    def rich(self, text, seen=None, terms=True, markup=True):
        """Plain text with TeX and *emphasis* to HTML; glossary terms attached once per block.
        With markup=False only TeX is converted: asterisks and [links](...) stay as written."""
        if text is None:
            return ''
        text = unlink(text) if markup else text
        seen = set() if seen is None else seen
        parts = []
        pos = 0
        for m in MATH_RE.finditer(text):
            parts.append(self.plain(text[pos:m.start()], seen, terms, markup))
            pos = m.end()
            if m.group(1) is not None:
                tex = m.group(1).strip()
                # Punctuation that follows a formula stays on its line.
                trail = re.match(r'[.,;:!?)\]]+', text[pos:])
                punct = html.escape(trail.group(0), quote=False) if trail else ''
                if trail:
                    pos += len(trail.group(0))
                if len(tex) > 36:
                    parts.append('<span class="math-inline math-long">' + self.math.add(tex, False) + punct + '</span>')
                elif punct:
                    parts.append('<span class="nobr"><span class="math-inline">' + self.math.add(tex, False) +
                                 '</span>' + punct + '</span>')
                else:
                    parts.append('<span class="math-inline">' + self.math.add(tex, False) + '</span>')
            else:
                parts.append('<span class="math-display">' + self.math.add(m.group(2).strip(), True) + '</span>')
        parts.append(self.plain(text[pos:], seen, terms, markup))
        return ''.join(parts)

    def text_form(self, text):
        """Text for attributes and titles: each formula becomes its rendered token text after the TeX run
        (never TeX source), and emphasis marks are dropped. The caller escapes the result."""
        out, pos = [], 0
        text = unlink(text or '')
        for m in MATH_RE.finditer(text):
            out.append(EMPH_RE.sub(r'\1', text[pos:m.start()]))
            out.append(self.math.add_text((m.group(1) or m.group(2)).strip()))
            pos = m.end()
        out.append(EMPH_RE.sub(r'\1', text[pos:]))
        return ''.join(out)

    def plain(self, text, seen, terms, markup=True):
        if '\\(' in text or '\\)' in text or '\\[' in text or '\\]' in text:
            self.problems.append('unbalanced TeX delimiters in: ' + text[:120])
        escaped = html.escape(text, quote=False)
        if markup:
            escaped = EMPH_RE.sub(r'<em>\1</em>', escaped)
        if terms:
            escaped = self.term_links.link(escaped, seen)
        return escaped

    # Pieces -----------------------------------------------------------------------------

    def status_label(self, status):
        return self.page['status_labels'][status]

    def part_number(self, n):
        return self.page['labels'].get('part', '§{n}').format(n=n)

    def statement_id(self, s):
        sid = (s.get('id') or '').strip()
        return 's-' + ident(sid) if sid else ''

    def statement(self, s, where, heading='h4', title_override=None, chip=True, context=None):
        """One statement. `context` is (href, label HTML) of the question, family of examples or group
        that holds it; that line is shown only when the statement is the target of the address, so a
        reader who arrives by a link sees where the statement stands. A statement may carry a list of
        hypotheses (optional field 'hypotheses'), shown as a labelled list before its text."""
        raw = s.get('status')
        status = raw if raw in STATEMENT_STATUSES else None
        if status is None:
            # Shown as the value it carries, without a mark, never as another status; the build fails on it.
            self.problems.append(f'{where}: unknown statement status {raw!r}')
        seen = set()
        label = self.status_label(status) if status else str(raw or '?')
        title = (s.get('title') or '') if title_override is None else title_override
        sid = self.statement_id(s)
        if sid:
            self.anchors.add(sid)
        id_attr = f' id="{sid}"' if sid else ''
        claim = (s.get('atlasClaimId') or '').strip()
        if claim:
            id_attr += f' data-atlas-claim="{html.escape(claim)}"'
        added = ' added' if s.get('added') else ''
        cls = slug(status) if status else 'unknown'
        out = [f'<article class="statement st-{cls}{added}" data-status="{html.escape(status or str(raw or ""))}"{id_attr}>']
        out.append('<div class="statement-head">')
        out.append(f'<span class="status-chip chip-{cls}">{mark(status) if status else ""}<span>{html.escape(label)}</span></span>')
        if s.get('added') and chip:
            out.append(f'<span class="added-chip">{html.escape(self.page["labels"]["added"])}</span>')
        if title:
            out.append(f'<{heading} class="statement-title">{self.rich(title, seen, terms=False)}</{heading}>')
        if context and sid:
            out.append(f'<p class="statement-context"><a href="{context[0]}">{context[1]}</a></p>')
        out.append('</div>')
        summary = (s.get('summary') or '').strip()
        if summary:
            out.append(f'<p class="statement-summary">{self.rich(summary, seen)}</p>')
        given = s.get('hypotheses')
        if given is not None and (not isinstance(given, list) or not all(isinstance(h, str) and h.strip() for h in given)):
            self.problems.append(f'{where}: hypotheses must be a list of non-empty texts')
        hypotheses = [h for h in given if isinstance(h, str) and h.strip()] if isinstance(given, list) else []
        if hypotheses:
            out.append(f'<div class="statement-hyp"><p class="statement-hyp-label">{html.escape(self.page["labels"]["hypotheses"])}</p>'
                       f'<ul>{"".join(f"<li>{self.rich(h, seen)}</li>" for h in hypotheses)}</ul></div>')
        out.append(f'<div class="statement-text">{self.paragraphs(s.get("text", ""), seen)}</div>')
        notes = []
        novelty = (s.get('novelty') or '').strip()
        antecedents = (s.get('antecedents') or '').strip()
        cite = (s.get('cite') or '').strip()
        if status in NOVELTY_STATUSES and novelty:
            notes.append(f'<span class="note-novelty">{html.escape(self.page["novelty_labels"].get(novelty, novelty))}</span>')
        if antecedents:
            notes.append(f'<span class="note-label">{html.escape(self.page["labels"]["antecedents"])}</span> '
                         f'{self.rich(antecedents, seen, terms=False)}')
        if cite:
            notes.append(f'<span class="note-label">{html.escape(self.page["labels"]["cite"])}</span> '
                         f'{self.rich(cite, seen, terms=False)}')
        if notes:
            out.append('<p class="statement-notes">' + ' <span class="sep" aria-hidden="true">·</span> '.join(notes) + '</p>')
        if claim:
            out.append(f'\x00ACLAIM:{ident(claim)}\x00')  # a link to the claim, filled in once the atlas is drawn
        out.append('</article>')
        if not (s.get('text') or '').strip():
            self.problems.append(f'{where}: empty statement text')
        return ''.join(out)

    def paragraphs(self, text, seen=None):
        blocks = [b.strip() for b in re.split(r'\n\s*\n', text or '') if b.strip()]
        if len(blocks) <= 1:
            return f'<p>{self.rich(text.strip() if text else "", seen)}</p>'
        return ''.join(f'<p>{self.rich(b, seen)}</p>' for b in blocks)

    def section(self, sid, title, body, cls='', kicker=None, added=False, attrs=''):
        self.anchors.add(sid)
        # Every section head carries its part number, in the order of the contents (filled in by run(), once the
        # built sections are known). The kicker's words follow the number where they place the section; words that
        # only repeat the heading ('Essay' over 'Essay', 'Remaining comparisons' over 'The remaining comparisons')
        # are not drawn.
        words = lambda t: {w.rstrip('s') for w in re.findall(r'[a-z]+', (t or '').lower())}  # noqa: E731
        if kicker and words(kicker) <= words(title):
            kicker = None
        role = f' <span class="sep" aria-hidden="true">·</span> {html.escape(kicker)}' if kicker else ''
        k = f'<p class="kicker"><span class="part-num">\x00PART:{sid}\x00</span>{role}</p>'
        chip = (f'<p class="section-added"><span class="added-chip">{html.escape(self.page["labels"]["added_section"])}'
                f'</span></p>') if added else ''
        return (f'<section id="{sid}" class="section {cls}" aria-labelledby="{sid}-h"{attrs}>'
                f'<header class="section-head">{k}<h2 id="{sid}-h"><a class="anchor" href="#{sid}">'
                f'{html.escape(title)}</a></h2>{chip}</header>{body}</section>')

    def atlas(self):
        """The atlas mount. The atlas is rendered by a separate module (default atlas.py beside this file)
        from atlas.json in the input folder, a reader-safe projection supplied with the content. With no
        atlas.json there is no atlas section and no navigation item. The module's render(data, ctx)
        returns a dict: 'html' (the section body), optional 'title', 'kicker', 'nav_label', 'css', 'js'
        and 'problems' (a list of strings, each a build failure). It is called after every other section
        is built, so ctx.anchor_for() knows every statement anchor on the page."""
        data_path = self.folder / 'atlas.json'
        if not data_path.exists():
            if (self.content or {}).get('scientific_atlas'):
                self.problems.append('scientific_atlas names an atlas, but there is no atlas.json in the content folder')
            return '', None
        if not self.atlas_module.exists():
            self.problems.append(f'atlas.json is present but there is no atlas renderer ({self.atlas_module.name})')
            return '', None
        import importlib.util
        spec = importlib.util.spec_from_file_location('qh_status_atlas', self.atlas_module)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        data = json.loads(data_path.read_text(encoding='utf-8'))
        pointer = (self.content or {}).get('scientific_atlas') or {}
        if pointer:
            if pointer.get('path', 'atlas.json') != 'atlas.json':
                self.problems.append(f'scientific_atlas: path {pointer.get("path")!r}; the atlas is read from atlas.json in the content folder')
            for key in ('schema', 'asOf'):
                if pointer.get(key) and data.get(key) != pointer.get(key):
                    self.problems.append(f'scientific_atlas: {key} {pointer.get(key)!r} but atlas.json has {data.get(key)!r}')
        result = module.render(data, AtlasContext(self)) or {}
        for problem in result.get('problems') or []:
            self.problems.append(f'atlas: {problem}')
        body = result.get('html') or ''
        if not body.strip():
            return '', None
        css, js = result.get('css') or '', result.get('js') or ''
        if re.search(r'</(script|style)', css + js, re.I):
            self.problems.append('atlas: its css or js contains a closing </script or </style')
        used = {c for m in re.finditer(r'\bclass="([^"]*)"', body) for c in m.group(1).split()}
        clash = sorted(used & ATLAS_RESERVED_CLASSES)
        if clash:
            self.problems.append('atlas: markup uses classes that the page script binds: ' + ', '.join(clash))
        L = self.page['labels']
        self.atlas_assets = {'css': css, 'js': js}
        nav_label = result.get('nav_label') or L.get('nav_atlas') or 'Atlas'
        title = result.get('title') or L.get('atlas') or nav_label
        kicker = result.get('kicker') or L.get('atlas_kicker')
        return self.section('atlas', title, body, cls='wide atlas', kicker=kicker, attrs=' data-atlas-mount'), nav_label

    # Sections ---------------------------------------------------------------------------

    def cover(self, c):
        L = self.page['labels']
        lead = ''.join(f'<p>{self.rich(p)}</p>' for p in c.get('lead', []))
        counts = self.counts(c)
        # The statuses on the page, each opening its statements (status.js); not counted, so that the overview
        # draws no theorem-count inference. It is the overview's one-line legend of the statement marks.
        stats = ''.join(
            f'<li><a href="#examples" data-filter="{st}">{mark(st)}'
            f'<span class="count-label">{html.escape(self.status_label(st))}</span></a></li>'
            for st, n in counts if n)
        self.anchors.add('programme')
        # The overview: the cover, the lead and the contents (placed once every section is built, see run()).
        # On a wide screen the contents stands in the right margin beside the cover and the lead. The tally stays a
        # direct child of main: status.js places the search after it.
        return (f'<div class="overview"><header class="cover" id="programme">'
                f'<p class="kicker">{html.escape(L["kicker"])}</p>'
                f'<h1>{self.rich(c["title"], terms=False)}</h1>'
                f'<p class="subtitle">{self.rich(c.get("subtitle", ""), terms=False)}</p>'
                f'<p class="as-of">{html.escape(L["as_of"])} {self.as_of_html(c)}'
                + (f' <span class="sep" aria-hidden="true">·</span>&nbsp;<a href="#changes">{html.escape(L["changes_link"])}</a>'
                   if (c.get('changes') or {}).get('items') else '') +
                f' <span class="sep" aria-hidden="true">·</span>&nbsp;<a href="#contents">{html.escape(L["contents"])}</a>'
                '</p>'
                f'</header>'
                f'<div class="lead prose">{lead}</div>'
                '\x00CONTENTS\x00</div>'
                f'<nav class="tally" aria-label="{html.escape(L["tally"])}"><p class="tally-label">'
                f'{html.escape(L["tally"])}</p><ul>{stats}</ul></nav>')

    def contents(self, c, parts):
        """The page's parts in page order, each with its heading (as the section shows it) and what it
        holds, counted from the content: the overview's entry points to every section. `parts` maps a
        section id to its heading for the sections that were built."""
        L = self.page['labels']

        def many(n, one, more):
            return L[one] if n == 1 else L[more].format(n=n)

        def questions(key):
            return [q.get('question') or {} for q in (c.get(key) or {}).get('questions', [])]

        opened = [s for g in c.get('open', []) for s in g.get('statements', [])]
        # What each part holds, by number: no status counts (the page draws no closure or tally inference).
        holds = {
            'atlas': ('', ''),
            'results': (many(len(c.get('principal', [])), 'statements_one', 'statements_many'), ''),
            'decisive': (many(len(questions('decisive')), 'questions_one', 'questions_many'), ''),
            'frontier': (many(len(questions('frontier')), 'comparisons_one', 'comparisons_many'), ''),
            'examples': (L['contents_examples'].format(rows=len(c.get('rows', [])), cols=len(c.get('columns', []))), ''),
            'failures': (many(len((c.get('failures') or {}).get('items', [])), 'counterexamples_one', 'counterexamples_many'), ''),
            'open': (L['contents_open'].format(n=len(opened), g=len(c.get('open', []))), ''),
            'essay': (L['essay'], ''),
            'terms': (many(len(self.term_links.entries), 'definitions_one', 'definitions_many'), ''),
            'orientation': (many(len((c.get('orientation') or {}).get('programmeFamilies') or []), 'groups_one', 'groups_many'), ''),
        }
        items = []
        # The numeral track fits the longest number label (a worded template such as 'Part {n}' too), the same on every line.
        track = max((len(self.part_number(i + 1)) for i in range(len(parts))), default=0)
        for i, (sid, heading) in enumerate(parts.items()):
            count, mix = holds.get(sid, ('', ''))
            items.append(f'<li><a href="#{sid}"><span class="contents-num">{html.escape(self.part_number(i + 1))}</span>'
                         f'<span class="contents-title">{heading}</span>'
                         f'<span class="contents-holds">{html.escape(count)}{mix}</span></a></li>')
        return (f'<nav class="contents" id="contents" aria-labelledby="contents-label" style="--contents-num:{track}ch"><p class="contents-label" id="contents-label">'
                f'{html.escape(L["contents"])}</p><ol>{"".join(items)}</ol></nav>')

    def as_of_html(self, c):
        """The date of the content, with the time of its evidence boundary when the content gives one (as_of_utc)."""
        day = c.get('as_of') or ''
        when = c.get('as_of_utc') or ''
        m = re.fullmatch(r'(\d{4}-\d{2}-\d{2})T(\d{2}):(\d{2})(?::\d{2}(?:\.\d+)?)?Z', when)
        if when and not m:
            self.problems.append(f'as_of_utc {when!r} is not a UTC time (YYYY-MM-DDTHH:MMZ)')
        if m and m.group(1) != day:
            self.problems.append(f'as_of {day!r} and as_of_utc {when!r} name different days')
        shown = long_date(day) + (f', {m.group(2)}:{m.group(3)} UTC' if m else '')
        return f'<time datetime="{html.escape(when if m else day)}">{html.escape(shown)}</time>'

    def orientation(self, c):
        """How the programme fits together: the content's explanation, its families of examples in groups (each
        group links its families in the table), and the content's guidance for reading the page."""
        o = c.get('orientation') or {}
        if not o:
            return ''
        L = self.page['labels']
        rows = {r.get('id'): r for r in c.get('rows', [])}
        text = ''.join(f'<p>{self.rich(p)}</p>' for p in o.get('explanation') or [] if (p or '').strip())
        groups = []
        for i, g in enumerate(o.get('programmeFamilies') or []):
            gid = 'pf-' + ident(g.get('id') or g.get('title') or str(i))
            self.anchors.add(gid)
            links = []
            for fid in g.get('familyIds') or []:
                r = rows.get(fid)
                if r is None:
                    self.problems.append(f'orientation {g.get("id")!r}: no family {fid!r} in the table')
                    continue
                rid = 'row-' + ident(r.get('id') or r['name'])
                links.append(f'<li><a href="#{rid}">{self.rich(r["name"], terms=False)}</a></li>')
            groups.append(f'<div class="pf" id="{gid}"><h3><a class="anchor" href="#{gid}">{self.rich(g.get("title", ""), terms=False)}</a></h3>'
                          f'<div class="pf-text prose">{self.paragraphs(g.get("text", ""))}</div>'
                          f'<p class="pf-label">{html.escape(L["orientation_families"])}</p><ul class="pf-families">{"".join(links)}</ul></div>')
        guide = ''.join(f'<div class="guide-item"><dt>{self.rich(x.get("title", ""), terms=False)}</dt>'
                        f'<dd>{self.rich(x.get("text", ""))}</dd></div>' for x in o.get('readerGuidance') or [])
        body = (f'<div class="orientation-text prose">{text}</div>' if text else '') + \
               (f'<div class="pfs">{"".join(groups)}</div>' if groups else '') + \
               (f'<div class="guidance"><h3 class="guidance-title">{html.escape(L["orientation_guidance"])}</h3><dl class="guide">{guide}</dl></div>'
                if guide else '')
        return self.section('orientation', o.get('title') or L['orientation'], body, cls='wide orientation',
                            kicker=L.get('orientation_kicker'))

    def counts(self, c):
        tally = {s: 0 for s in STATEMENT_STATUSES}
        for s in self.all_statements(c):
            if s.get('status') in tally:
                tally[s['status']] += 1
        return [(s, tally[s]) for s in STATEMENT_STATUSES]

    @staticmethod
    def all_statements(c):
        yield from c.get('principal', [])
        for key in ('decisive', 'frontier'):
            for q in (c.get(key) or {}).get('questions', []):
                if q.get('question'):
                    yield q['question']
                yield from q.get('known', [])
        for r in c.get('rows', []):
            yield from r.get('statements', [])
        for f in (c.get('failures') or {}).get('items', []):
            if f.get('witness'):
                yield f['witness']
        for g in c.get('open', []):
            yield from g.get('statements', [])

    def key(self, c, compact=False):
        used_cells = {cell.get('status') for r in c.get('rows', []) for cell in (r.get('cells') or {}).values()}
        if compact:
            items = ''.join(f'<li>{mark(st)}<span>{html.escape(self.status_label(st))}</span></li>'
                            for st in CELL_STATUSES if st in used_cells)
            return f'<ul class="legend" aria-label="{html.escape(self.page["labels"]["legend"])}">{items}</ul>'
        items = []
        explained = set()
        for k in c.get('status_key', []):
            st = k.get('status')
            if st not in MARKS:
                self.problems.append(f'status key: unknown status {st!r}')
                continue
            explained.add(st)
            items.append(f'<div class="key-item"><dt>{mark(st)}<span>{html.escape(self.status_label(st))}'
                         f'</span></dt><dd>{self.rich(k.get("explanation", ""))}</dd></div>')
        # Every status the page shows has its entry in the content's key, which names and explains it in the
        # content owner's words; the page adds no wording of its own for a status (the labels are page.json's,
        # selected by the stored code).
        for st in STATEMENT_STATUSES:
            if st not in explained and any(s.get('status') == st for s in self.all_statements(c)):
                self.problems.append(f'status key: statements use {st!r}, which has no entry in content.json status_key')
        for st in CELL_STATUSES:
            if st in used_cells and st not in explained:
                self.problems.append(f'status key: the table uses {st!r}, which has no entry in content.json status_key')
        extra = ''
        return f'<dl class="key">{"".join(items)}</dl>{extra}'

    def changes(self, c):
        ch = c.get('changes') or {}
        items = ch.get('items') or []
        if not items:
            return ''
        L = self.page['labels']
        refs = {}
        for st in self.all_statements(c):
            if st.get('id'):
                refs[st['id']] = st
        lis = []
        for i, it in enumerate(items):
            ref = (it.get('ref') or '').strip()
            target = refs.get(ref)
            if not target:
                self.problems.append(f'changes item {i}: no statement with id {ref!r}')
            title = self.rich((target or {}).get('title') or '', terms=False)
            status = (target or {}).get('status')
            head = (f'<a class="change-link" href="#s-{ident(ref)}">{mark(status) if status in STATEMENT_STATUSES else ""}<span>{title}</span></a>'
                    if target else '')
            lis.append(f'<li>{head}<p>{self.rich(it.get("text", ""))}</p></li>')
        since = ch.get('since') or ''
        label = L['changes_since'].format(date=long_date(since)) if since else L['changes']
        self.anchors.add('changes')
        intro = f'<p class="changes-intro">{self.rich(ch["intro"])}</p>' if ch.get('intro') else ''
        return (f'<aside class="changes" id="changes" aria-labelledby="changes-h">'
                f'<p class="kicker">{html.escape(L["changes_kicker"])}</p>'
                f'<h2 id="changes-h" class="changes-title">{html.escape(label)}</h2>'
                f'{intro}<ol class="change-list">{"".join(lis)}</ol></aside>')

    def fold(self, s, where, chip=True, context=None):
        """A related statement reduced to one line, its status and its title, that opens to the whole
        statement. The statement inside keeps its own markup and anchor; while it is inside the fold its
        heading is drawn by the line above it."""
        status = s.get('status') if s.get('status') in STATEMENT_STATUSES else None
        shown = self.status_label(status) if status else str(s.get('status') or '?')  # an invalid value as itself
        added = (f'<span class="added-chip">{html.escape(self.page["labels"]["added"])}</span>'
                 if s.get('added') and chip else '')
        # The status text is visible for every status but 'checked', the common case, whose mark shows it (the key
        # and the legend name the mark) and whose text stays in the line's accessible name; so the conditional and
        # open items stand out in a list of related statements.
        quiet = ' visually-hidden' if status == 'checked' else ''
        return (f'<li class="fold-item"><details class="known fold">'
                f'<summary class="fold-head">{mark(status) if status else ""}<span class="fold-title">{self.rich(s.get("title") or "", terms=False)}'
                f'</span><span class="fold-status{quiet}">{html.escape(shown)}</span>{added}{icon("chevron")}'
                f'</summary>{self.statement(s, where, chip=chip, context=context)}</details></li>')

    def frontier(self, c, key='frontier'):
        """Question cards, the same in every question section: the number and title, then the question
        (its statement, then why it matters) and, beside it on a wide screen, the related statements as
        a list of lines, each opening to its statement. The list shows every related statement's status
        and title at once; the texts open one at a time, or all at once with Open all."""
        fr = c.get(key) or {}
        questions = fr.get('questions') or []
        if not questions:
            return ''
        L = self.page['labels']
        out = []
        index = []
        # Numbers restart in each question section, so the number's label names the section's kind of item.
        qlabel = L.get(f'{key}_question') or L.get('question', 'Question')
        # The index marks each question's own status only where the section's questions differ in status.
        mixed_status = len({(q.get('question') or {}).get('status') for q in questions}) > 1
        all_added = all(st.get('added') for q in questions for st in [q.get('question') or {}] + (q.get('known') or []))
        for i, q in enumerate(questions):
            qid = 'q-' + ident(q.get('id') or q.get('title') or str(i))
            self.anchors.add(qid)
            question = q.get('question') or {}
            card_title = (q.get('title') or '').strip()
            own_title = (question.get('title') or '').strip()
            # The question's own title is shown only where it says more than the card's title.
            override = '' if not own_title or own_title == card_title else None
            body = (self.statement(question, f'{key} {i} question', title_override=override, chip=not all_added)
                    if question else '')
            why = (f'<div class="question-why prose"><p class="question-why-label">{html.escape(L["why"])}</p>'
                   f'{self.paragraphs(q["why"])}</div>') if q.get('why') else ''
            known = q.get('known') or []
            n = len(known)
            count = L['statements_one'] if n == 1 else L['statements_many'].format(n=n)
            kn = ''
            if known:
                where = (f'#{qid}', f'{html.escape(qlabel)} {i + 1} · {self.rich(card_title, terms=False)}')
                items = ''.join(self.fold(s, f'{key} {i} known {j}', chip=not all_added, context=where)
                                for j, s in enumerate(known))
                # The checked items show only their mark (fold()); the head names that mark once, in words.
                known_key = (f'<span class="known-key" aria-hidden="true">{mark("checked")}<span>{html.escape(self.status_label("checked"))}</span></span>'
                             if any(st.get('status') == 'checked' for st in known) else '')
                kn = (f'<div class="question-known"><p class="known-head"><span class="known-label">'
                      f'{html.escape(L["known"])}</span><span class="row-count">{html.escape(count)}</span>{known_key}</p>'
                      f'<ul class="statements known-list" role="list">{items}</ul></div>')
            title_html = self.rich(card_title, terms=False)
            head = (f'<header class="question-head"><p class="question-num"><span class="question-num-label">'
                    f'{html.escape(qlabel)}</span> {i + 1}</p>'
                    f'<h3><a class="anchor" href="#{qid}">{title_html}</a></h3></header>')
            # The label is drawn from its data attribute by the style sheet, so that the page search does not find
            # 'question' in every card; it is still read by assistive technology and printed.
            ask = f'<p class="question-ask-label" data-label="{html.escape(L["question_label"])}"></p>' if body else ''
            cls = 'question compare' + ('' if len(known) > 2 else ' few-known' if known else ' no-known')
            out.append(f'<div class="{cls}" id="{qid}">{head}<div class="question-ask">{ask}{body}{why}</div>{kn}</div>')
            # The question's own status leads its index entry, apart from the counts of its related statements.
            asked = question.get('status') if question.get('status') in STATEMENT_STATUSES else None
            own = mark(asked, self.status_label(asked)) if asked and mixed_status else ''
            index.append(f'<li><a href="#{qid}"><span class="q-index-num">{i + 1}</span>'
                         f'<span class="q-index-title">{own}{self.rich(card_title, terms=False)}</span></a></li>')
        intro = f'<div class="section-intro prose">{self.paragraphs(fr["intro"])}</div>' if fr.get('intro') else ''
        index_label = L.get(f'{key}_index') or L.get('question_index', 'The questions')
        # Named by its label and its section's heading, so the two question indexes differ as landmarks.
        nav = (f'<nav class="q-index" aria-labelledby="{key}-index-label {key}-h"><p class="q-index-head">'
               f'<span class="q-index-label" id="{key}-index-label">{html.escape(index_label)}</span></p>'
               f'<ol>{"".join(index)}</ol></nav>') if len(questions) > 1 else ''
        return self.section(key, fr.get('heading') or L[key], intro + nav + f'<div class="questions compare">{"".join(out)}</div>',
                            cls=f'wide questions-section {key}', kicker=L[f'{key}_kicker'], added=all_added)

    def failures(self, c):
        fa = c.get('failures') or {}
        items = fa.get('items') or []
        if not items:
            return ''
        L = self.page['labels']
        out = []
        all_added = all((it.get('witness') or {}).get('added') for it in items)
        for i, it in enumerate(items):
            fid = 'f-' + ident(it.get('id') or str(i))
            self.anchors.add(fid)
            w = it.get('witness') or {}
            witness = self.statement(w, f'failure {i} witness', chip=not all_added) if w else ''
            if not w:
                self.problems.append(f'failure {i}: no witness')
            out.append(f'<div class="failure" id="{fid}"><p class="claim">'
                       f'<span class="claim-tag">{mark("refuted form")}<span>{html.escape(L["false"])}</span></span>'
                       f'<span class="claim-text">{self.rich(claim_text(it.get("claim", "")), terms=False)}</span></p>{witness}</div>')
        intro = f'<div class="section-intro prose">{self.paragraphs(fa["intro"])}</div>' if fa.get('intro') else ''
        return self.section('failures', fa.get('heading') or L['failures'], intro + f'<div class="failures">{"".join(out)}</div>',
                            kicker=L['failures_kicker'], added=all_added)

    def principal(self, c):
        L = self.page['labels']
        body = ''.join(self.statement(s, f'principal {i}', heading='h3') for i, s in enumerate(c.get('principal', [])))
        return self.section('results', L['principal'], f'<div class="statements principal">{body}</div>',
                            kicker=L['principal_kicker'])

    def grid(self, c):
        L = self.page['labels']
        columns = {col['id']: col for col in c.get('columns', [])}
        # What each status means, as the content's key gives it, repeated in each cell's card so that a mark can be
        # read where it is used.
        meaning = {k.get('status'): self.rich(k.get('explanation', ''), terms=False)
                   for k in c.get('status_key', []) if k.get('status') in MARKS and k.get('explanation')}
        order = [cid for cid in COLUMNS if cid in columns] or COLUMNS
        for cid in COLUMNS:
            if cid not in columns:
                self.problems.append(f'columns: missing column {cid}')
        # The table is one stop in the tab order (its first column heading); the arrow keys, Home and End move
        # inside it (status.js), so its other controls take tabindex -1.
        out_of_tab = ' tabindex="-1"'
        head = ''.join(
            f'<th scope="col"><button type="button" class="col-head" data-col="{cid}"{"" if k == 0 else out_of_tab} '
            f'aria-describedby="col-{cid}" aria-haspopup="dialog" aria-expanded="false" aria-controls="card"><span class="col-head-text">'
            f'{self.rich(columns.get(cid, {}).get("short") or columns.get(cid, {}).get("name", cid), terms=False)}</span>'
            f'</button></th>' for k, cid in enumerate(order))
        rows = []
        for r in c.get('rows', []):
            rid = 'row-' + ident(r.get('id') or r['name'])
            cells = []
            for cid in order:
                cell = (r.get('cells') or {}).get(cid)
                if not cell:
                    self.problems.append(f'row {r.get("id")}: missing cell {cid}')
                    cells.append('<td></td>')
                    continue
                st = cell.get('status')
                if st not in CELL_STATUSES:
                    self.problems.append(f'row {r.get("id")}, {cid}: unknown cell status {st!r}')
                    st = 'not posed'
                colname = columns.get(cid, {}).get('name', cid)
                note = cell.get('note') or ''
                label = f'{self.text_form(r["name"])}, {self.text_form(colname)}: {self.status_label(st)}'
                note_html = self.rich(note, terms=False)
                cells.append(
                    f'<td class="cell cell-{slug(st)}" data-status="{st}">'
                    f'<button type="button" class="cell-btn" data-row="{rid}" aria-label="{html.escape(label)}" tabindex="-1" '
                    f'aria-haspopup="dialog" aria-expanded="false" aria-controls="card">'
                    f'{mark(st)}</button>'
                    f'<div class="cell-note" hidden><p class="cell-note-head">{mark(st)}<span>'
                    f'{html.escape(self.status_label(st))}</span> <span class="cell-note-where">'
                    f'{self.rich(colname, terms=False)}</span></p><p class="cell-note-text">{note_html}</p>'
                    + (f'<p class="cell-note-meaning">{meaning[st]}</p>' if meaning.get(st) else '') +
                    '</div></td>')
            short = r.get('short') or self.page.get('row_short', {}).get(r.get('id')) or r['name']
            rows.append(f'<tr><th scope="row"><a class="row-link" href="#{rid}" tabindex="-1" title="{html.escape(self.text_form(r["name"]))}">'
                        f'{self.rich(short, terms=False)}</a></th>'
                        f'{"".join(cells)}</tr>')
        col_notes = ''.join(
            f'<div class="col-def" id="col-{cid}"><dt>{self.rich(columns[cid]["name"], terms=False)}</dt>'
            f'<dd>{self.rich(columns[cid].get("explanation", ""), terms=False)}</dd></div>' for cid in order if cid in columns)
        table = (f'<div class="grid-wrap" role="region" aria-label="{html.escape(L["grid"])}">'
                 f'<table class="grid"><caption class="visually-hidden">{html.escape(L["grid_caption"])}</caption>'
                 f'<thead><tr><th scope="col" class="corner">{html.escape(L["grid_corner"])}</th>{head}</tr></thead>'
                 f'<tbody>{"".join(rows)}</tbody></table></div>')
        legend = (f'<div class="grid-legend">{self.key(c, compact=True)}'
                  f'<p class="legend-key"><a href="#status">{html.escape(L["key"])}</a></p></div>')
        return (f'<div class="grid-block">{table}<p class="grid-hint">{html.escape(L["grid_hint"])}</p>'
                f'<div class="grid-aside">{legend}<details class="col-defs"><summary>{html.escape(L["columns"])}'
                f'{icon("chevron")}</summary><dl>{col_notes}</dl></details></div></div>')

    def rows(self, c):
        L = self.page['labels']
        columns = {col['id']: col for col in c.get('columns', [])}
        out = []
        for i, r in enumerate(c.get('rows', [])):
            rid = 'row-' + ident(r.get('id') or r['name'])
            self.anchors.add(rid)
            statements = r.get('statements', [])
            where = (f'#{rid}', self.rich(r['name'], terms=False))
            body = ''.join(self.statement(s, f'row {r.get("id")} statement {j}', context=where) for j, s in enumerate(statements))
            cells = []
            for cid in COLUMNS:
                cell = (r.get('cells') or {}).get(cid)
                if not cell:
                    continue
                st = cell.get('status') if cell.get('status') in CELL_STATUSES else 'not posed'
                note = (cell.get('note') or '').strip()
                note_html = f'<span class="cell-text">{self.rich(note, terms=False)}</span>' if note else ''
                cells.append(f'<li class="cell-line cell-{slug(st)}">{mark(st)}<span class="cell-col">'
                             f'{self.rich(columns.get(cid, {}).get("name", cid), terms=False)}</span>'
                             f'<span class="cell-body"><span class="cell-st">{html.escape(self.status_label(st))}</span>'
                             f'{note_html}</span></li>')
            marks = ''.join(mark(((r.get('cells') or {}).get(cid) or {}).get('status', 'not posed')
                                 if ((r.get('cells') or {}).get(cid) or {}).get('status') in CELL_STATUSES
                                 else 'not posed') for cid in COLUMNS)
            n = len(statements)
            count = L['statements_one'] if n == 1 else L['statements_many'].format(n=n)
            out.append(
                f'<details class="row" id="{rid}"><summary><span class="row-num">{i + 1}</span>'
                f'<span class="row-name">{self.rich(r["name"], terms=False)}</span>'
                f'<span class="row-marks" aria-hidden="true">{marks}</span>'
                f'<span class="row-count">{html.escape(count)}</span>{icon("chevron")}</summary>'
                f'<div class="row-body"><p class="row-summary">{self.rich(r.get("summary", ""))}</p>'
                f'<ul class="cell-lines" aria-label="{html.escape(L["by_column"])}">{"".join(cells)}</ul>'
                f'<div class="statements">{body}</div></div></details>')
        in_families = {s.get('status') for r in c.get('rows', []) for s in r.get('statements', [])}
        filters = ''.join(
            f'<button type="button" class="filter" data-filter="{st}" aria-pressed="false">{mark(st)}'
            f'<span>{html.escape(self.status_label(st))}</span></button>'
            for st in STATEMENT_STATUSES if st in in_families)
        toolbar = (f'<div class="row-tools"><div class="filters" role="group" aria-label="{html.escape(L["filter"])}">'
                   f'<span class="filters-label">{html.escape(L["filter"])}</span>{filters}</div>'
                   f'<div class="row-actions"><button type="button" class="link-btn" data-expand="all">{html.escape(L["expand"])}</button>'
                   f'<button type="button" class="link-btn" data-expand="none">{html.escape(L["collapse"])}</button></div></div>')
        return self.section('examples', L['examples'],
                            f'<p class="section-intro prose">{html.escape(L["examples_intro"])}</p>' +
                            self.grid(c) + toolbar + f'<div class="rows" style="--marks:{len(COLUMNS)}">{"".join(out)}</div>',
                            cls='wide', kicker=L['examples_kicker'])

    def open_problems(self, c):
        L = self.page['labels']
        groups = []
        used = {'open', 'open-h'}  # the section's own anchors
        for i, g in enumerate(c.get('open', [])):
            gid = 'open-' + ident(g.get('id') or g.get('heading', str(i)))
            if gid in used:
                self.problems.append(f'open group {i}: anchor {gid} is already used on the page')
            used.add(gid)
            self.anchors.add(gid)
            where = (f'#{gid}', self.rich(g.get('heading', ''), terms=False))
            body = ''.join(self.statement(s, f'open {i}.{j}', context=where) for j, s in enumerate(g.get('statements', [])))
            intro = f'<div class="prose group-intro">{self.paragraphs(g["intro"])}</div>' if g.get('intro') else ''
            groups.append(f'<div class="open-group" id="{gid}"><h3><a class="anchor" href="#{gid}">'
                          f'{self.rich(g.get("heading", ""), terms=False)}</a></h3>{intro}<div class="statements">{body}</div></div>')
        return self.section('open', L['open'], ''.join(groups), kicker=L['open_kicker'])

    def author_html(self):
        name = html.escape(self.page['author'])
        if self.page['home_label'] == self.page['author']:
            href = html.escape(self.page['home'], quote=True)
            return f'<a href="{href}" rel="author">{name}</a>'
        return name

    def essay(self, text, lead):
        L = self.page['labels']
        lines = text.strip().split('\n')
        title = lines[0].lstrip('#').strip() if lines and lines[0].startswith('#') else L['essay']
        body = '\n'.join(lines[1:] if lines and lines[0].startswith('#') else lines)
        paras = []
        for block in re.split(r'\n\s*\n', body.strip()):
            block = ' '.join(block.split())
            if not block:
                continue
            if len(block) <= 32 and '=' in block and not MATH_RE.search(block):
                paras.append(f'<p class="essay-display">{html.escape(block, quote=False)}</p>')
            else:
                paras.append(f'<p>{self.rich(block, terms=False, markup=False)}</p>')
        lead_html = f'<p class="essay-lead">{self.rich(lead)}</p>' if (lead or '').strip() else ''
        self.essay_title = title
        return self.section('essay', L['essay'],
                            f'{lead_html}<article class="essay prose" aria-labelledby="essay-title">'
                            f'<h3 id="essay-title" class="essay-title">{self.rich(title, terms=False, markup=False)}</h3>'
                            f'<p class="essay-byline">{self.author_html()}</p>'
                            f'{"".join(paras)}</article>', kicker=L['essay_kicker'])

    def glossary(self):
        L = self.page['labels']
        items = []
        letters = {}
        for e in sorted(self.term_links.entries, key=lambda e: e['term'].lower()):
            self.anchors.add(e['id'])
            items.append(f'<div class="gloss" id="{e["id"]}"><dt>{self.rich(e["term"], terms=False)}</dt>'
                         f'<dd>{self.rich(e.get("definition", ""), terms=False)}</dd></div>')
            # The first letter of the term as read (accents and TeX delimiters set aside) links to its first term.
            first = next((ch for ch in unicodedata.normalize('NFKD', self.math_free(e['term'])) if ch.isalnum()), '#')
            letters.setdefault(first.upper(), e['id'])
        if not items:
            return ''
        index = ''.join(f'<li><a href="#{tid}">{html.escape(letter)}</a></li>' for letter, tid in letters.items())
        nav = (f'<nav class="gloss-index" aria-label="{html.escape(L["terms_index"])}"><ol>{index}</ol></nav>'
               if len(letters) > 1 else '')
        return self.section('terms', L['terms'], f'<p class="section-intro prose">{html.escape(L["terms_intro"])}</p>'
                            f'{nav}<dl class="glossary">{"".join(items)}</dl>', cls='wide terms-section',
                            kicker=L['terms_kicker'])

    # Page -------------------------------------------------------------------------------

    def run(self):
        c = json.loads((self.folder / 'content.json').read_text(encoding='utf-8'))
        self.content = c
        essay_path = self.folder / 'essay.md'
        essay_text = essay_path.read_text(encoding='utf-8') if essay_path.exists() else ''
        if not essay_path.exists():
            self.warnings.append('essay.md not found in the input folder; the page has no essay')
        self.term_links = Terms(c.get('glossary', []))
        self.problems.extend(self.term_links.problems)
        L = self.page['labels']

        cover = self.cover(c)
        orientation = self.orientation(c)
        changes = self.changes(c)
        key = self.section('status', L['key'], self.key(c), cls='key-section', kicker=L['key_kicker'])
        principal = self.principal(c)
        decisive = self.frontier(c, 'decisive')
        frontier = self.frontier(c)
        examples = self.rows(c)
        failures = self.failures(c)
        open_ = self.open_problems(c)
        essay = self.essay(essay_text, c.get('essay_lead', '')) if essay_text else ''
        terms = self.glossary()
        atlas, atlas_nav = self.atlas()

        # The contents, after the lead: every built section in page order, by the heading it shows.
        # Page order: the established results, the key to the marks, the examples (the programme across its
        # families and parts), then what remains (the decisive questions, the remaining comparisons, the open
        # problems), the natural statements that fail, the essay and the glossary. The lead names the table before
        # the questions; the key comes just before the table, on screen and on paper; the atlas, when present, leads.
        parts = {}
        if orientation:
            parts['orientation'] = self.rich((c.get('orientation') or {}).get('title') or L['orientation'], terms=False)
        if atlas:
            parts['atlas'] = html.escape(atlas_nav)
        parts['results'] = html.escape(L['principal'])
        parts['status'] = html.escape(L['key'])
        parts['examples'] = html.escape(L['examples'])
        for sid, built, heading in (('decisive', decisive, (c.get('decisive') or {}).get('heading')),
                                    ('frontier', frontier, (c.get('frontier') or {}).get('heading'))):
            if built:
                parts[sid] = self.rich(heading or L.get(sid, sid), terms=False)
        parts['open'] = html.escape(L['open'])
        if failures:
            parts['failures'] = self.rich((c.get('failures') or {}).get('heading') or L['failures'], terms=False)
        if essay:
            parts['essay'] = self.rich(self.essay_title, terms=False, markup=False)  # TeX in the title as mathematics
        if terms:
            parts['terms'] = html.escape(L['terms'])
        cover = cover.replace('\x00CONTENTS\x00', self.contents(c, parts))
        number = {sid: self.part_number(i + 1) for i, sid in enumerate(parts)}

        nav_items = [('programme', L['nav_programme'])]
        if orientation:
            nav_items.append(('orientation', L['nav_orientation']))
        if atlas:
            nav_items.append(('atlas', atlas_nav))
        nav_items.append(('results', L['nav_results']))
        nav_items.append(('examples', L['nav_examples']))
        if decisive:
            nav_items.append(('decisive', L['nav_decisive']))
        if frontier:
            nav_items.append(('frontier', L['nav_frontier']))
        nav_items.append(('open', L['nav_open']))
        if failures:
            nav_items.append(('failures', L['nav_failures']))
        if essay:
            nav_items.append(('essay', L['nav_essay']))
        if terms:
            nav_items.append(('terms', L['nav_terms']))
        nav = ''.join(f'<li><a href="#{a}">{html.escape(t)}</a></li>' for a, t in nav_items)

        body = (f'<a class="skip" href="#main">{html.escape(L["skip"])}</a>'
                f'<div class="bar"><div class="bar-inner">'
                f'<a class="home" href="{html.escape(self.page["home"])}">{html.escape(self.page["home_label"])}</a>'
                f'<a class="nav-top" href="#programme">{html.escape(L["nav_programme"])}</a>'
                f'<nav class="nav" aria-label="{html.escape(L["on_page"])}"><ul>{nav}</ul></nav>'
                f'<button type="button" class="find-open" data-find-open aria-label="{html.escape(L["search_open"])}" '
                f'title="{html.escape(L["search_open"])}">{icon("search")}</button>'
                f'<button type="button" class="theme" aria-label="{html.escape(L["theme"])}" title="{html.escape(L["theme"])}">'
                f'{icon("theme")}</button></div></div>'
                f'<main id="main" tabindex="-1">{cover}{changes}{orientation}{atlas}{principal}{key}{examples}{decisive}{frontier}{open_}{failures}{essay}{terms}</main>'
                f'<footer class="foot"><div class="foot-inner"><p>{self.author_html()} · '
                f'{self.as_of_html(c)}</p>'
                f'<p><a href="{html.escape(self.page["home"])}">{html.escape(self.page["home_label"])}</a> · '
                f'<a href="#programme">{icon("up")}<span>{html.escape(L["top"])}</span></a></p></div></footer>'
                f'<div class="card" id="card" role="dialog" aria-modal="false" hidden><div class="card-inner"></div></div>')
        if self.reader_manifest:
            body = self.monograph_body(c, L, cover, (changes, orientation, atlas, principal, key, examples, decisive,
                                                    frontier, open_, failures, essay, terms), parts)
        atlas_ids = set(re.findall(r'\sid="([^"]+)"', atlas))
        body = re.sub('\x00ACLAIM:([\\w-]+)\x00',
                      lambda m: (f'<p class="statement-notes statement-atlas"><span class="note-label"><a href="#atlas-claim-{m.group(1)}">'
                                 f'{html.escape(L["in_atlas"])}</a></span></p>'
                                 if f'atlas-claim-{m.group(1)}' in atlas_ids else ''), body)
        unnumbered = sorted(set(re.findall('\x00PART:([\\w-]+)\x00', body)) - set(number))
        if unnumbered:
            self.problems.append(f'page: sections missing from the contents, so without a part number: {unnumbered}')
        body = re.sub('\x00PART:([\\w-]+)\x00', lambda m: html.escape(number.get(m.group(1), '')), body)

        meta = self.book.m if self.book else c  # the book's own title and subtitle; the former page keeps its own
        title_form = self.text_form(meta['title'])
        description_form = self.text_form(meta.get('subtitle', ''))
        self.math.render()
        body = self.math.substitute(body)
        # A family's link in the table is copied as text into its cells' cards (status.js reads its
        # textContent), so its formulas carry no TeX annotation there, which would be read twice.
        body = re.sub(r'(<a class="row-link"[^>]*>)(.*?)(</a>)',
                      lambda m: m.group(1) + re.sub(r'<annotation\b[^>]*>.*?</annotation>', '', m.group(2), flags=re.S) + m.group(3),
                      body, flags=re.S)
        for err in self.math.errors:
            self.problems.append('TeX: ' + err['error'][:160] + ' in ' + err['tex'][:80])

        # The print sheet follows the screen sheet (and the atlas's own sheet), so that its rules win at
        # equal specificity. The atlas script runs after the page script, in its own element.
        css = '\n'.join(part for part in ((HERE / 'status.css').read_text(encoding='utf-8'), self.atlas_assets['css'],
                                          (HERE / 'status-print.css').read_text(encoding='utf-8')) if part)
        js = (HERE / 'status.js').read_text(encoding='utf-8')
        if self.atlas_assets['js']:
            js += '\n</script>\n<script>' + self.atlas_assets['js']
        if self.reader_manifest:
            css, js = self.monograph_assets()
        fonts = self.font_faces(body)
        title_text = self.math.substitute(title_form, escape_text=False)
        description = self.math.substitute(description_form, escape_text=False)
        head = (
            '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            "<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'none'; style-src 'unsafe-inline'; "
            "script-src 'unsafe-inline'; font-src data:; img-src data:; base-uri 'none'; form-action 'none'\">\n"
            '<meta name="referrer" content="no-referrer">\n'
            '<meta name="robots" content="noindex, nofollow">\n'
            '<meta name="color-scheme" content="light dark">\n'
            f'<title>{html.escape(title_text)} — {html.escape(self.page["author"])}</title>\n'
            f'<meta name="description" content="{html.escape(description)}">\n'
            f'<meta name="author" content="{html.escape(self.page["author"])}">\n'
            f'<meta property="og:title" content="{html.escape(title_text)}">\n'
            f'<meta property="og:description" content="{html.escape(description)}">\n'
            '<meta property="og:type" content="article">\n'
            f'<link rel="canonical" href="{html.escape(self.page["site"])}/{self.page["slug"]}.html">\n'
            '<link rel="icon" href="data:,">\n'
            "<script>try{var t=localStorage.getItem('qh-theme');if(t==='dark'||t==='light')"
            "document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>\n"
            f'<style>{fonts}\n{css}</style>\n</head>\n')
        return head + f'<body>\n{body}\n<script>{js}</script>\n</body>\n</html>\n'

    # The monograph ------------------------------------------------------------------------------------------

    def monograph_body(self, c, L, cover, sections, parts):
        """The book (monograph.py), followed by the former page, kept whole as the book's reference sections
        (reader-dom/v1: each a [data-reference] place with its ids unchanged)."""
        import monograph
        R = self.page.get('reader') or {}
        self.book = monograph.Book(self, self.reader_manifest, mark, R)
        supplements = self.supplements_supplied()
        # The book's contents is #contents; the former page's own contents gives up that id, so that an old link to
        # #contents lands on the book's contents, which lists every reference section.
        cover = cover.replace('<nav class="contents" id="contents"', '<nav class="contents" id="programme-contents"', 1)
        cover = cover.replace('<h1>', '<h1 id="programme-title">', 1)
        chunks = [f'<section class="mg-ref-overview" id="programme-overview" data-reference '
                  f'aria-labelledby="programme-title">{cover}</section>']
        index = [('programme-overview', self.rich(c['title'], terms=False))]
        for chunk in sections:
            if not chunk:
                continue
            m = re.match(r'<section id="([^"]+)"', chunk)
            if not m:
                self.problems.append('reader: a section of the former page does not open with <section id=...>')
                continue
            chunks.append(chunk.replace('<section ', '<section data-reference ', 1))
            sid = m.group(1)
            if sid in parts:
                index.append((sid, parts[sid]))
            elif sid == 'changes':
                index.append((sid, html.escape(L['changes'])))
        # Supplied supplements (exact author handoffs) follow the part each names; the book sets them (monograph.py).
        placed = set()
        for sup in supplements:
            at = next((k for k, ch in enumerate(chunks) if re.match(r'<section (?:data-reference )?id="%s"' % re.escape(sup['after']), ch)), None)
            if at is None:
                self.problems.append(f'supplement {sup["id"]}: the part it follows, {sup["after"]}, is not on the page')
                continue
            chunks.insert(at + 1, f'\x04SUPPLEMENT:{sup["id"]}\x04')
            k = next((k for k, (sid, _) in enumerate(index) if sid == sup['after']), len(index) - 1)
            index.insert(k + 1, (sup['id'], html.escape(sup['title'])))
            placed.add(sup['id'])
        self.book.supplements = {s['id']: s for s in supplements if s['id'] in placed}
        inner = self.book.assemble(''.join(chunks), index)
        self.problems.extend('reader: ' + p for p in self.book.problems)
        self.warnings.extend('reader: ' + w for w in self.book.warnings)
        words = ''.join(f' data-label-{html.escape(k)}="{html.escape(v)}"' for k, v in (R.get('reader_js') or {}).items())
        bar = (f'<nav class="mg-bar" data-reader-bar aria-label="{html.escape(R.get("bar", "Reading"))}">'
               f'<a class="mg-site" href="{html.escape(self.page["home"])}">{html.escape(self.page["home_label"])}</a>'
               f'<span class="mg-bar-static"><a href="#contents">{html.escape(R.get("contents", "Contents"))}</a>'
               f'<a href="#programme-overview">{html.escape(R.get("reference", "Atlas and reference"))}</a></span></nav>')
        return (f'<a class="skip" href="#main">{html.escape(L["skip"])}</a>{bar}'
                f'<main id="main" tabindex="-1" data-reader{words}>{inner}</main>'
                f'<footer class="foot"><div class="foot-inner"><p>{self.author_html()} · '
                f'{self.book.date_html()}</p>'
                f'<p><a href="{html.escape(self.page["home"])}">{html.escape(self.page["home_label"])}</a> · '
                f'<a href="#front">{icon("up")}<span>{html.escape(L["top"])}</span></a></p></div></footer>'
                f'<div class="card" id="card" role="dialog" aria-modal="false" hidden><div class="card-inner"></div></div>')

    def supplements_supplied(self):
        """The content folder's supplied supplements (supplements/supplements.json): exact author handoffs, each used only
        at the sha256 its record names, so that the page carries exactly the supplied words."""
        reg = self.folder / 'supplements' / 'supplements.json'
        if not reg.exists():
            return []
        out = []
        for s in json.loads(reg.read_text(encoding='utf-8')).get('supplements', []):
            f = self.folder / 'supplements' / s.get('file', '')
            raw = f.read_bytes() if f.is_file() else b''
            if hashlib.sha256(raw).hexdigest() != s.get('sha256'):
                self.problems.append(f'supplement {s.get("id")}: {s.get("file")} is not at its recorded sha256')
                continue
            text = raw.decode('utf-8')
            first = text.lstrip().split('\n', 1)[0]
            if not first.startswith('# ') or not s.get('id') or not s.get('after'):
                self.problems.append(f'supplement {s.get("id")}: needs an id, the part it follows and a "# " title line')
                continue
            out.append(dict(s, text=text, title=first[2:].strip()))
        return out

    def monograph_assets(self):
        """The book's sheets and scripts: the page sheet, the atlas's, the print sheet, then the book's own sheet and the
        figures' (each lane's rules win inside its own markup). The reader script replaces status.js on this page
        (the interaction lane's reader contract, G5) unless page.json's reader.with_status_js asks for both."""
        R = self.page.get('reader') or {}
        figures = self.book.figure_assets()
        css = '\n'.join(part for part in (
            (HERE / 'status.css').read_text(encoding='utf-8'), self.atlas_assets['css'],
            (HERE / 'status-print.css').read_text(encoding='utf-8'),
            (HERE / 'monograph.css').read_text(encoding='utf-8'), figures['css'], self.book.map_css(),
            (HERE / 'front-figure.css').read_text(encoding='utf-8') if self.book.m.get('front_figures') else '') if part)
        scripts = []
        if R.get('with_status_js'):
            scripts.append((HERE / 'status.js').read_text(encoding='utf-8'))
        reader = HERE / 'reader.js'
        if reader.exists():
            scripts.append(reader.read_text(encoding='utf-8'))
        else:
            self.warnings.append('reader: reader.js (interaction lane) not found; the book is served as one long page')
        for part in (self.atlas_assets['js'], figures['js']):
            if part:
                scripts.append(part)
        for part in scripts + [css]:
            if re.search(r'</(script|style)', part, re.I):
                self.problems.append('reader: a sheet or script contains a closing </script or </style')
        return css, '\n</script>\n<script>'.join(scripts)

    def math_free(self, text):
        return MATH_RE.sub(lambda m: m.group(1) or m.group(2) or '', text or '')

    def font_faces(self, body):
        faces = []
        text_chars = set(strip_tags(re.sub(r'<math\b.*?</math>', ' ', body, flags=re.S)))
        text_chars |= set(strip_tags(self.math_free(self.content.get('title', ''))))
        text_chars |= set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,;:!?—–-’‘“”()[]·…')
        self.font_report = {}
        for (family, weight, style), path in self.text_fonts.items():
            data = subset_font(path, text_chars, keep_math=False)
            self.font_report[f'{family} {weight} {style}'] = len(data)
            faces.append(f'@font-face{{font-family:"{family}";font-weight:{weight};font-style:{style};'
                         f'font-display:swap;src:url(data:font/woff;base64,{base64.b64encode(data).decode()}) format("woff")}}')
        if self.math_font:
            chars = set('0123456789+−-=()[]{}|/,.;:!?<>*′″√')
            for m in re.finditer(r'<(mi|mo|mn|mtext|ms)\b[^>]*>(.*?)</\1>', body, re.S):
                chars.update(html.unescape(re.sub(r'<[^>]+>', '', m.group(2))))
            data = subset_font(self.math_font, chars, keep_math=True)
            self.font_report['math'] = len(data)
            faces.append('@font-face{font-family:"QH Garamond Math";font-display:swap;'
                         f'src:url(data:font/woff;base64,{base64.b64encode(data).decode()}) format("woff")}}')
        return '\n'.join(faces)


def subset_font(path, chars, keep_math):
    import logging
    logging.getLogger('fontTools.subset').setLevel(logging.ERROR)
    from fontTools import subset
    from fontTools.ttLib import TTFont
    chars = {c for c in chars if not c.isspace()} | {' ', ' '}
    font = TTFont(str(path), recalcTimestamp=False)  # keep the source font's date: the page is byte-reproducible
    options = subset.Options()
    options.layout_features = ['*']
    options.flavor = 'woff'
    options.name_IDs = ['*']
    options.notdef_outline = True
    options.glyph_names = False
    options.hinting = False
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=[ord(c) for c in chars])
    subsetter.subset(font)
    buffer = io.BytesIO()
    font.flavor = 'woff'
    font.save(buffer)
    return buffer.getvalue()


def claim_text(text):
    """A false claim is labelled by the page; a leading 'False:' in the text is dropped."""
    text = re.sub(r'^\s*false\s*[:.]\s*', '', text or '', flags=re.I)
    return text[:1].upper() + text[1:]


def strip_tags(markup):
    return html.unescape(re.sub(r'<[^>]+>', '', markup or ''))


MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']


def long_date(day):
    m = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})', day or '')
    if not m:
        return day or ''
    return f'{int(m.group(3))} {MONTHS[int(m.group(2)) - 1]} {m.group(1)}'
