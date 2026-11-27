"""The monograph: the programme as a book in parts and chapters, with the former status page kept whole as its
reference volume.

Input, in the content folder beside content.json:
    reader-data/manifest.json   schema qh-reader/v1 (the author's): parts, chapters, routes, terms, theorems, figures
    chapters/*.md               the chapters, at the paths the manifest gives (relative to manifest.json)

The chapter Markdown is the authoritative text and no word of it is rewritten here. This module only sets it:
`##` headings become numbered sections with the author's ids, displays keep their authored \\tag numbers and
{#id} anchors, a paragraph that opens with a lead-in (**Theorem 10.1 (...).**, **Recognition theorem.**, *Proof.*)
becomes a result block whose label is the lead-in exactly as written, `::: figure <id>` places the atlas lane's
figure for that manifest record (the foundation draws no model), and a plain "(1.3)" links to the display tagged 1.3.

The page follows the interaction lane's reader contract (reader-dom/v1): main[data-reader] holds the front matter,
the contents, one article per manifest chapter and the reference sections (every section of the former page, with
its ids unchanged). Without a script it is the whole book in reading order; reader.js shows one place at a time.
"""
import html
from hashlib import sha256
import importlib.util
import json
import re
import shlex
from pathlib import Path
from urllib.parse import urlsplit

from citations import locator_suffix
from definition_uses import DefinitionUses
from typing import NamedTuple, Optional

SCHEMA = 'qh-reader/v1'
HERE = Path(__file__).resolve().parent


def is_primary_page(target):
    """An authored HTTP(S) citation to a positive physical PDF page."""
    try:
        url = urlsplit(target)
        return (url.scheme in ('http', 'https') and bool(url.hostname)
                and not re.search(r'\s', target)
                and re.fullmatch(r'page=[1-9][0-9]*', url.fragment) is not None)
    except ValueError:
        return False


def scholarly_citation(label, target):
    """Keep a printable locator on page links and on ordinary bibliographical text."""
    citation = label + html.escape(locator_suffix(target, label))
    if is_primary_page(target):
        return f'<a class="mg-primary-page" href="{html.escape(target, quote=True)}">{citation}</a>'
    return citation

PROVED_FORMS = ('theorem', 'lemma', 'proposition', 'corollary')
PROOF_FORMS = ('proof', 'proof-sketch')
FORM_WORDS = {
    **{word: word for word in (*PROVED_FORMS, 'definition', 'construction', 'example', 'counterexample', 'remark',
                               'notation', 'convention', 'conjecture', 'heuristic', 'proof', 'result', 'claim')},
    'definitions': 'definition', 'examples': 'example', 'remarks': 'remark', 'conventions': 'convention',
    'open problem': 'open-problem', 'problem': 'open-problem', 'open question': 'open-question', 'question': 'open-question',
    'proof sketch': 'proof-sketch', 'sketch of proof': 'proof-sketch', 'sketch of the proof': 'proof-sketch',
    'sketch': 'proof-sketch', 'consequence': 'consequence',
}
QUALIFIERS = {'conditional': 'conditional', 'conjectural': 'conjecture', 'heuristic': 'heuristic', 'open': 'open'}
DEFAULT_STATUS = {**dict.fromkeys(PROVED_FORMS, 'proved'), 'conjecture': 'conjecture', 'heuristic': 'heuristic',
                  'open-problem': 'open', 'open-question': 'open', 'counterexample': 'refuted-form'}
PROSE_STYLES = {'notation': 'remark', 'convention': 'remark'}
# The structural kind and epistemic status are independent. Existing visual families name the CSS classes.
STATUS_STYLE = {'proved': 'theorem', 'refuted-form': 'counterexample'}
STATUS_ADJECTIVE = {'proved': 'Proved', 'conditional': 'Conditional', 'conjecture': 'Conjectural',
                    'heuristic': 'Heuristic', 'open': 'Open'}
KIND_MARK = {'theorem': 'checked', 'conditional': 'conditional', 'conjecture': 'conjecture', 'heuristic': 'heuristic',
             'counterexample': 'refuted form', 'open': 'open'}
ALL_WORDS = '|'.join(sorted(map(re.escape, FORM_WORDS), key=len, reverse=True))
FORM_PREFIX = re.compile(rf'^(?P<word>{ALL_WORDS})\b', re.I)
NAMED_FORM = re.compile(rf'\s(?P<word>{ALL_WORDS})$', re.I)
NOT_A_NAME = re.compile(r'^(?:the|this|that|these|those|a|an|it|we|our|its|which|what|how|why|here|there)\b', re.I)
NUMBER = r'(?:(?:[A-Z]\.)?\d+(?:\.\d+)*[a-z]?|[A-Z]|[IVXLCDM]+)'
SUBTITLE = re.compile(r'\s*(?:[:(]|[—–]|\s-\s)')
SCOPE_WORD = re.compile(r'\s+(?:for|on|of|in|under|over|with|at)\s+', re.I)


class Form(NamedTuple):
    kind: str
    status: Optional[str] = None

    @property
    def style(self):
        return STATUS_STYLE.get(self.status, self.status) or PROSE_STYLES.get(self.kind, self.kind)

    @property
    def is_result(self):
        return self.kind in (*PROVED_FORMS, 'conjecture', 'heuristic', 'open-problem', 'open-question', 'example',
                             'counterexample', 'result', 'claim', 'consequence') or (
                                 self.kind == 'construction' and self.status is not None)

    def index_label(self, authored):
        """Expand a generic verdict to include the form. Keep a verdict with specific hypotheses verbatim."""
        generic = {'proved', 'checked', 'established', 'conditional', 'conditional result', 'conditional consequence',
                   'conjecture', 'heuristic', 'open', *PROVED_FORMS}
        if self.kind in (*PROVED_FORMS, 'result', 'claim', 'consequence') and self.status in STATUS_ADJECTIVE:
            if not authored or authored.lower() in generic:
                return f'{STATUS_ADJECTIVE[self.status]} {self.kind}'
        return authored or self.kind.replace('-', ' ').capitalize()


def heading_form(label):
    """Read the declaration in a mathematical label. A word in its subtitle or an ordinary sentence is not a status."""
    # Keep TeX delimiters and mathematical parentheses out of the grammar of the declaration.
    text = re.sub(r'\\\(.+?\\\)', 'M', label.strip().rstrip('.:'), flags=re.S)
    head = SUBTITLE.split(text, maxsplit=1)[0].strip()
    if re.match(r'^(?:unproved|unproven|possible|proposed|candidate|purported|not)\b', head, re.I):
        return None
    if re.fullmatch(r'heuristic (?:argument|model|interpretation|calculation)', head, re.I):
        return Form('heuristic', 'heuristic')
    qualifier = None
    first, _, tail = head.partition(' ')
    if first.lower() in QUALIFIERS and tail:
        qualifier, head = QUALIFIERS[first.lower()], tail.strip()
    elif head.lower() == 'conditional':
        return Form('result', 'conditional')
    elif head.lower() == 'open':
        return Form('open-problem', 'open')
    # "Theorem 10.1", "Recognition theorem", "Conditional unit theorem for inflated coefficients".
    if re.match(r'^proof of concept\b|^sketch of (?!proof\b|the proof\b)', head, re.I):
        return None
    word = FORM_PREFIX.match(head)
    if word and (not head[word.end():].strip() or re.fullmatch(NUMBER, head[word.end():].strip()) or
                 SCOPE_WORD.match(head[word.end():])):
        kind = FORM_WORDS[word['word'].lower()]
    else:
        stem = SCOPE_WORD.split(head, maxsplit=1)[0]
        stem = re.sub(rf'\s+{NUMBER}$', '', stem).strip()
        named = NAMED_FORM.search(stem)
        if (not named or NOT_A_NAME.match(stem) or len(stem.split()) > 10 or
                re.search(r'\b(?:the|an?|this|that|these|those|our|their|its)\s*$', stem[:named.start()], re.I)):
            return None
        kind = FORM_WORDS[named['word'].lower()]
    # "Open mapping theorem" names a proved theorem; "Open problem" and "Open question" declare open status.
    if qualifier == 'open' and not word:
        qualifier = None
    if not qualifier:
        qualified = re.search(r'\((conditional|conjectural|heuristic|open)(?:\s+on\b[^()]*)?\)\s*$', text, re.I)
        if qualified:
            qualifier = QUALIFIERS[qualified[1].lower()]
    if kind in ('conjecture', 'heuristic', 'open-problem', 'open-question'):
        return Form(kind, DEFAULT_STATUS[kind])
    return Form(kind, qualifier or DEFAULT_STATUS.get(kind))
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

INLINE_MATH = re.compile(r'\\\((.+?)\\\)', re.S)
DISPLAY_IN_LINE = re.compile(r'\\\[(.+?)\\\]', re.S)
# A supplied supplement's first line, when it is a date ("17 November 2026"), is set as its dateline.
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December')
DATELINE = re.compile(r'^(\d{1,2}) (' + '|'.join(MONTHS) + r') (\d{4})$')
TAG_RE = re.compile(r'\\tag\*?\{([^{}]*)\}')
ID_LINE = re.compile(r'\{#([A-Za-z][\w:.-]*)\}')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
HEADING_ID = re.compile(r'^(.*?)\s*\{#([A-Za-z][\w:.-]*)\}\s*$')
LIST_RE = re.compile(r'^(\s*)([-*+]|\d{1,3}[.)])\s+(.*)$')
FIGURE_HOOK = re.compile(r':::\s*figure\s+([a-z0-9]+(?:-[a-z0-9]+)*)\s*')
FENCE_OPEN = re.compile(r'(:{3,})\s*(\S.*?)\s*')
FENCE_CLOSE = re.compile(r':{3,}')
CODE_FENCE = re.compile(r'(`{3,}|~{3,})(.*)')
TABLE_SEP = re.compile(r'^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)*\|?\s*$')
REF_DEF = re.compile(r'^\s{0,3}\[([^\]]+)\]:\s*<?(\S+?)>?(?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))?\s*$')
END_MARK = re.compile(r'(?:∎|□|\\(?:qedhere|qed|blacksquare|square)(?:\s*\\\))?)\s*$')


def number_ranges(numbers):
    """[1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 15] -> '1–8, 12, 13, 15': a run of three or more consecutive numbers is written as
    a range; every number of the list is shown, and no other."""
    out, run = [], []
    for n in numbers:
        if run and n == run[-1] + 1:
            run.append(n)
            continue
        if run:
            out.append(f'{run[0]}–{run[-1]}' if len(run) >= 3 else ', '.join(map(str, run)))
        run = [n]
    if run:
        out.append(f'{run[0]}–{run[-1]}' if len(run) >= 3 else ', '.join(map(str, run)))
    return ', '.join(out)


def slugify(text):
    import unicodedata
    text = unicodedata.normalize('NFKD', re.sub(r'\\\(.+?\\\)', ' ', text or ''))
    text = re.sub(r'[^\w\s-]', '', text.encode('ascii', 'ignore').decode()).strip().lower()
    return re.sub(r'[\s_-]+', '-', text)[:64].strip('-') or 'x'


# Blocks ------------------------------------------------------------------------------------------------------

def parse_div_spec(spec):
    """Plain and Pandoc-style fences, including a structural class with an explicit status."""
    head, _, options = spec.partition('{')
    words, attrs = head.strip().split(), {}
    try:
        # Preserve TeX backslashes inside quoted titles.
        tokens = shlex.shlex(options.rstrip().removesuffix('}'), posix=True)
        tokens.whitespace_split, tokens.commenters, tokens.escape = True, '', ''
        for token in tokens:
            if token.startswith('.'):
                words.append(token[1:])
            elif token.startswith('#'):
                attrs['id'] = token[1:]
            elif '=' in token:
                key, value = token.split('=', 1)
                attrs[key] = value
    except ValueError as exc:
        raise ValueError(f'Invalid mathematical fence {spec!r}: {exc}') from exc
    if 'id' in attrs and not re.fullmatch(r'[A-Za-z][\w:.-]*', attrs['id']):
        raise ValueError(f'Invalid fence identifier {attrs["id"]!r}')
    if len(words) == 2 and 'conjecture' in words and any(w in PROVED_FORMS for w in words):
        words[words.index('conjecture')] = 'conjectural'
    if len(words) == 2 and words[-1].lower() in QUALIFIERS:
        words.reverse()
    return '-'.join(words).lower(), attrs


def code_end(lines, start, fence):
    closer = re.compile(re.escape(fence[0]) + '{' + str(len(fence)) + ',}')
    return next((i for i in range(start + 1, len(lines)) if closer.fullmatch(lines[i].strip())), len(lines))


def parse_blocks(lines):  # noqa: C901 (one pass over the lines, one branch per block form)
    blocks = []
    para = []
    state = {'attached': False}
    after_display = False

    def flush():
        if para:
            blocks.append({'t': 'p', 'text': ' '.join(x.strip() for x in para), 'attached': state['attached']})
        para.clear()
        state['attached'] = False

    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            flush()
            after_display = False
            i += 1
            continue
        m = FIGURE_HOOK.fullmatch(s)
        if m:
            flush()
            blocks.append({'t': 'figure', 'id': m.group(1)})
            after_display = False
            i += 1
            continue
        m = FENCE_OPEN.fullmatch(s)
        if m and not FENCE_CLOSE.fullmatch(s):
            flush()
            depth, j, inner = 1, i + 1, []
            while j < n:
                t = lines[j].strip()
                code = CODE_FENCE.fullmatch(t)
                if code:
                    end = code_end(lines, j, code[1])
                    inner.extend(lines[j:end + 1])
                    j = end + 1
                    continue
                if FENCE_CLOSE.fullmatch(t):
                    depth -= 1
                    if depth == 0:
                        break
                elif FENCE_OPEN.fullmatch(t) and not FIGURE_HOOK.fullmatch(t):
                    depth += 1
                inner.append(lines[j])
                j += 1
            cls, attrs = parse_div_spec(m.group(2))
            blocks.append({'t': 'div', 'cls': cls, 'attrs': attrs, 'blocks': parse_blocks(inner),
                           'closed': j < n})
            i = j + 1
            after_display = False
            continue
        code = CODE_FENCE.fullmatch(s)
        if code:
            flush()
            j = code_end(lines, i, code[1])
            blocks.append({'t': 'code', 'text': '\n'.join(lines[i + 1:j])})
            after_display = False
            i = j + 1
            continue
        m = HEADING_RE.match(line)
        if m and not line.startswith(' ' * 4):
            flush()
            text = m.group(2).rstrip('#').strip()
            hid = None
            mh = HEADING_ID.match(text)
            if mh:
                text, hid = mh.group(1).strip(), mh.group(2)
            blocks.append({'t': 'h', 'level': len(m.group(1)), 'text': text, 'id': hid})
            after_display = False
            i += 1
            continue
        if s.startswith('\\[') or s.startswith('$$'):
            flush()
            closer = '\\]' if s.startswith('\\[') else '$$'
            first = s[2:]
            if closer in first:
                k = first.index(closer)
                tex, rest, j = first[:k], first[k + 2:].strip(), i
            else:
                buf, j, rest = [first], i + 1, ''
                while j < n and closer not in lines[j]:
                    buf.append(lines[j])
                    j += 1
                if j < n:
                    k = lines[j].index(closer)
                    buf.append(lines[j][:k])
                    rest = lines[j][k + 2:].strip()
                tex = '\n'.join(buf)
            i = j + 1
            did = None
            mid = ID_LINE.fullmatch(rest) if rest else None
            if mid:
                did, rest = mid.group(1), ''
            elif not rest and i < n and ID_LINE.fullmatch(lines[i].strip()):
                did = ID_LINE.fullmatch(lines[i].strip()).group(1)
                i += 1
            tag = None
            mt = TAG_RE.search(tex)
            if mt:
                tag = mt.group(1).strip()
                tex = TAG_RE.sub('', tex)
            blocks.append({'t': 'math', 'tex': tex.strip(), 'tag': tag, 'id': did})
            after_display = True
            if rest:
                para.append(rest)
                state['attached'] = True
            continue
        if s.startswith('>'):
            flush()
            buf, j = [], i
            while j < n and lines[j].strip().startswith('>'):
                buf.append(re.sub(r'^\s*>\s?', '', lines[j]))
                j += 1
            blocks.append({'t': 'quote', 'blocks': parse_blocks(buf)})
            i = j
            continue
        if re.fullmatch(r'(?:\*\s*){3,}|(?:-\s*){3,}|(?:_\s*){3,}', s):
            flush()
            blocks.append({'t': 'hr'})
            i += 1
            continue
        if '|' in s and i + 1 < n and TABLE_SEP.match(lines[i + 1]) and not para:
            def cells(row):
                row = row.strip()
                row = row[1:] if row.startswith('|') else row
                row = row[:-1] if row.endswith('|') and not row.endswith('\\|') else row
                return [c.strip() for c in re.split(r'(?<!\\)\|', row)]
            head = cells(line)
            align = []
            for c in cells(lines[i + 1]):
                align.append('center' if c.startswith(':') and c.endswith(':') else 'right' if c.endswith(':') else '')
            rows, j = [], i + 2
            while j < n and lines[j].strip() and '|' in lines[j]:
                rows.append(cells(lines[j]))
                j += 1
            blocks.append({'t': 'table', 'head': head, 'align': align, 'rows': rows})
            i = j
            continue
        m = LIST_RE.match(line)
        if m:
            flush()
            indent = len(m.group(1))
            ordered = m.group(2)[0].isdigit()
            items, j = [], i
            start = int(re.match(r'\d+', m.group(2)).group(0)) if ordered else 1
            while j < n:
                mm = LIST_RE.match(lines[j])
                if mm and len(mm.group(1)) == indent and mm.group(2)[0].isdigit() == ordered:
                    width = len(mm.group(1)) + len(mm.group(2)) + 1
                    item = [mm.group(3)]
                    j += 1
                    while j < n:
                        t = lines[j]
                        if not t.strip():
                            nxt = lines[j + 1] if j + 1 < n else ''
                            if nxt.strip() and (len(nxt) - len(nxt.lstrip())) > indent:
                                item.append('')
                                j += 1
                                continue
                            break
                        lead = len(t) - len(t.lstrip())
                        if lead > indent and not (LIST_RE.match(t) and lead == indent):
                            item.append(t[min(lead, width):])
                            j += 1
                            continue
                        if LIST_RE.match(t) or HEADING_RE.match(t) or t.strip().startswith(('\\[', '$$', ':::')):
                            break
                        item.append(t)  # a lazy continuation line
                        j += 1
                    items.append(parse_blocks(item))
                    continue
                break
            blocks.append({'t': 'list', 'ordered': ordered, 'start': start, 'items': items})
            i = j
            after_display = False
            continue
        if not para:
            state['attached'] = after_display
        para.append(line)
        after_display = False
        i += 1
    flush()
    return split_inline_displays(blocks)


def split_inline_displays(blocks):
    """A paragraph with \\[...\\] inside a line: the text before, the display, and the text after (attached)."""
    out = []
    for b in blocks:
        if b['t'] != 'p' or '\\[' not in b['text']:
            out.append(b)
            continue
        pos, attached = 0, b['attached']
        for m in DISPLAY_IN_LINE.finditer(b['text']):
            before = b['text'][pos:m.start()].strip()
            if before:
                out.append({'t': 'p', 'text': before, 'attached': attached})
            tex = m.group(1)
            tag = None
            mt = TAG_RE.search(tex)
            if mt:
                tag, tex = mt.group(1).strip(), TAG_RE.sub('', tex)
            out.append({'t': 'math', 'tex': tex.strip(), 'tag': tag, 'id': None})
            pos, attached = m.end(), True
        after = b['text'][pos:].strip()
        if after:
            out.append({'t': 'p', 'text': after, 'attached': True})
    return out


def lead_in(text):
    """(form, label markdown, rest) when a paragraph opens with a lead-in, else None. The label is the author's
    bold or italic run exactly as written."""
    m = re.match(r'^(\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)\1(?=[\s.:,;!?)]|$)', text, re.S)
    if not m:
        return None
    inner, after = m.group(2), text[m.end():]
    bare = inner.strip()
    # A lead-in ends its run with a full stop or colon, or is followed by one: "**Theorem 6.3.**", "**Example**."
    punct_after = re.match(r'^\s*[.:]', after)
    if after.strip() and not (bare.endswith(('.', ':')) or punct_after or re.search(r'\)\s*[.:]?$', bare)):
        return None
    form = heading_form(bare)
    if not form:
        return None
    if m.group(1) in ('*', '_') and form.kind not in PROOF_FORMS:
        return None
    if punct_after:
        after = after[punct_after.end():]
        inner = inner + punct_after.group(0).strip()
    return form, inner, after.lstrip()


def ends_proof(block):
    if block['t'] == 'list':
        return bool(block['items'] and block['items'][-1] and ends_proof(block['items'][-1][-1]))
    if block['t'] == 'quote':
        return bool(block['blocks'] and ends_proof(block['blocks'][-1]))
    return bool(END_MARK.search(block.get('text', '') if block['t'] == 'p' else block.get('tex', '')))


# The book ------------------------------------------------------------------------------------------------------

class Book:
    def __init__(self, build, manifest_path, mark, labels=None):
        self.b = build
        self.path = Path(manifest_path)
        self.mark = mark
        self.definition_uses = DefinitionUses(self.path.parent)
        self.L = labels or {}
        self.problems = []
        self.warnings = []
        self.m = json.loads(self.path.read_text(encoding='utf-8'))
        if self.m.get('schema') != SCHEMA:
            self.problems.append(f'reader manifest: schema {self.m.get("schema")!r}, expected {SCHEMA}')
        self.parts = self.m.get('parts', [])
        self.chapters = self.m.get('chapters', [])
        self.by_id = {c['id']: c for c in self.chapters}
        self.part_of = {}
        for p in self.parts:
            for cid in p.get('chapter_ids', []):
                self.part_of[cid] = p
        self.part_no = {p['id']: i + 1 for i, p in enumerate(self.parts)}
        self.figures = {f['id']: f for f in self.m.get('figures', []) if f.get('id')}
        # Static diagrams (the author's nodes, edges and words; drawn here) share the figure hook and its id space.
        self.diagrams = {d['id']: d for d in self.m.get('diagrams', []) or [] if isinstance(d, dict) and d.get('id')}
        for ident in set(self.figures) & set(self.diagrams):
            self.problems.append(f'reader manifest: {ident} is both a figure and a diagram record')
        # Authored figures (manifest authored_figures: id, chapter_id, section_id, file): markup written by the author
        # in the book's drawing vocabulary, kept beside the manifest and placed by the same hook as the other figures.
        self.authored = {a['id']: a for a in self.m.get('authored_figures', []) or [] if isinstance(a, dict) and a.get('id')}
        for ident in set(self.authored) & (set(self.figures) | set(self.diagrams)):
            self.problems.append(f'reader manifest: {ident} is an authored figure and also a figure or diagram record')
        self.terms = {t['id']: t for t in self.m.get('terms', []) if isinstance(t, dict) and t.get('id')}
        self.theorems = {t['id']: t for t in self.m.get('theorems', []) if isinstance(t, dict) and t.get('id')}
        self.order = [c['id'] for c in self.chapters]
        missing = [cid for p in self.parts for cid in p.get('chapter_ids', []) if cid not in self.by_id]
        if missing:
            self.problems.append(f'reader manifest: parts name chapters it does not have: {missing}')
        for c in self.chapters:
            for q in c.get('prerequisites', []):
                if q not in self.by_id:
                    self.problems.append(f'reader manifest: {c["id"]} names an unknown prerequisite {q}')
        self.figmod = self.load_figures()
        self.used_ids = set()
        self.tags = {}         # authored equation number -> anchor id
        self.anchor_kind = {}  # id -> data-ref kind (chapter, section, result, definition, figure, equation)
        self.environment_forms = {}  # chapter declarations at their actual anchors, also used by the index of results
        self.index_targets = {}  # explicit source destinations expected in each chapter
        self.texts = {}
        self.blocks = {}
        self.missing_chapters = []
        self.figures_placed = []
        self.refdefs = {}      # chapter id -> {label: target}, from Markdown reference definitions (never shown)
        self.local_links = []  # (chapter id, target): links to working files, shown as their words only
        self.chapter_files = {Path(c['path']).name: c['id'] for c in self.chapters if c.get('path')}
        self.supplements = {}  # id -> supplied supplement (status.py: the content folder's supplements/), placed by assemble()

    # Loading -------------------------------------------------------------------------------------------------

    def load_figures(self):
        path = HERE / 'figures.py'
        if not path.exists():
            if self.figures:
                self.warnings.append('figures.py (atlas lane) not found: figure hooks are left out')
            return None
        spec = importlib.util.spec_from_file_location('qh_figures', path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def figure_assets(self):
        if not self.figmod or not any(f in self.figures for f in self.figures_placed):
            return {'css': '', 'js': ''}
        try:
            got = self.figmod.assets()
            return {'css': got.get('css', ''), 'js': got.get('js', '')}
        except (OSError, AttributeError) as e:
            self.warnings.append(f'figure assets not available ({type(e).__name__}: {e}); figures are served unstyled')
            return {'css': '', 'js': ''}

    def load(self):
        for c in self.chapters:
            f = (self.path.parent / c['path']).resolve()
            if not f.exists():
                self.missing_chapters.append(c['id'])
                continue
            text = f.read_text(encoding='utf-8')
            text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
            defs, kept, in_display = {}, [], False
            for line in text.splitlines():
                t = line.strip()
                # A line of a displayed formula is mathematics, never a reference definition.
                if not in_display and (t.startswith('\\[') or t.startswith('$$')):
                    closer = '\\]' if t.startswith('\\[') else '$$'
                    in_display = closer not in t[2:]
                    kept.append(line)
                    continue
                if in_display:
                    in_display = ('\\]' not in t) and not (t.endswith('$$') or t == '$$')
                    kept.append(line)
                    continue
                d = REF_DEF.match(line)
                if d:
                    defs[d.group(1).strip().lower()] = d.group(2)
                else:
                    kept.append(line)
            self.refdefs[c['id']] = defs
            text = '\n'.join(kept)
            self.texts[c['id']] = text
            annotated = self.definition_uses.mark(c['id'], text)
            blocks = parse_blocks(annotated.splitlines())
            self.definition_uses.anchor_passages(c['id'], self.walk(blocks))
            self.bind_index_passages(c['id'], blocks)
            if blocks and blocks[0]['t'] == 'h' and blocks[0]['level'] == 1:
                title = blocks.pop(0)['text']
                plain = re.sub(r'^\d+\.\s*', '', title).strip()
                if plain != c['title'].strip():
                    self.warnings.append(f'{c["id"]}: the chapter file\'s title "{title}" differs from the manifest title '
                                         f'"{c["title"]}"; the manifest title is shown')
            self.blocks[c['id']] = blocks
        if self.missing_chapters:
            self.warnings.append('chapters not yet supplied: ' + ', '.join(self.missing_chapters))
        # A first pass gives every anchor its id, so that references resolve in any order.
        for cid in self.order:
            self.used_ids.add(cid)
            self.anchor_kind[cid] = 'chapter'
            self.used_ids.add(cid + '-h')
        for cid in self.order:
            for b in self.walk(self.blocks.get(cid, [])):
                if b['t'] == 'math' and b.get('tag'):
                    if b['tag'] in self.tags:
                        self.problems.append(f'{cid}: equation number ({b["tag"]}) is used twice')
                    if not b.get('id'):
                        b['id'] = self.unique('eq-' + slugify(b['tag'].replace('.', '-')))
                    self.claim(b['id'], cid)
                    self.tags[b['tag']] = b['id']
                    self.anchor_kind[b['id']] = 'equation'
                elif b['t'] == 'math' and b.get('id'):
                    self.claim(b['id'], cid)
                    self.anchor_kind[b['id']] = 'equation'
                elif b['t'] == 'figure':
                    self.claim(b['id'], cid)
                    self.anchor_kind[b['id']] = 'figure'

    def bind_index_passages(self, chapter, blocks):
        """Bind the author's exact parser paragraphs, including paragraphs containing marked definition uses."""
        wanted = {}
        for record in (*self.terms.values(), *self.theorems.values()):
            if record.get('chapter_id') != chapter:
                continue
            target = record.get('source_target')
            paragraph = record.get('source_paragraph')
            if target is not None and not re.fullmatch(r'[A-Za-z][\w:.-]*', target):
                raise ValueError(f'{chapter}: invalid index destination {target!r}')
            if target:
                self.index_targets.setdefault(chapter, set()).add(target)
            if paragraph is not None:
                if not target or not paragraph:
                    raise ValueError(f'{chapter}: incomplete source paragraph for {record["id"]}')
                wanted.setdefault(paragraph, set()).add(target)
        if not wanted:
            return
        found = set()
        for block in self.walk(blocks):
            if block['t'] != 'p':
                continue
            plain = re.sub(r'\[([^\[\]\n]+)\]\(definition-use:[a-z0-9-]+\)', r'\1', block['text'])
            if plain in wanted:
                if plain in found:
                    raise ValueError(f'{chapter}: ambiguous index passage {sorted(wanted[plain])}')
                found.add(plain)
                block['source_ids'] = sorted(wanted[plain] - {block.get('passage_id')})
        missing = [sorted(ids) for paragraph, ids in wanted.items() if paragraph not in found]
        if missing:
            raise ValueError(f'{chapter}: missing index passages {missing}')

    def walk(self, blocks):
        for b in blocks:
            yield b
            if b['t'] in ('div', 'quote'):
                yield from self.walk(b['blocks'])
            elif b['t'] == 'list':
                for item in b['items']:
                    yield from self.walk(item)

    def claim(self, ident, where):
        if ident in self.used_ids and self.anchor_kind.get(ident) != 'pending':
            self.problems.append(f'{where}: the id "{ident}" is used twice')
        self.used_ids.add(ident)

    def unique(self, base):
        ident, k = base, 2
        while ident in self.used_ids:
            ident = f'{base}-{k}'
            k += 1
        self.used_ids.add(ident)
        self.anchor_kind[ident] = 'pending'
        return ident

    # Text ------------------------------------------------------------------------------------------------------

    def inline(self, text):
        """Inline Markdown to HTML: TeX through the page's one Temml run, **bold**, *italic*, `code`, [links](...),
        and plain (n.m) equation references linked to their displays."""
        slots = []

        def keep(markup):
            slots.append(markup)
            return f'\x01{len(slots) - 1}\x01'

        text = re.sub(r'`([^`]+)`', lambda m: keep('<code>' + html.escape(m.group(1)) + '</code>'), text)
        out, pos = [], 0
        for m in INLINE_MATH.finditer(text):
            out.append(text[pos:m.start()])
            pos = m.end()
            tex = m.group(1).strip()
            # Punctuation after a formula stays on its line; a bracket that closes a link's words does not move.
            trail = re.match(r'[.,;:!?)]+', text[pos:])
            punct = html.escape(trail.group(0), quote=False) if trail else ''
            if trail:
                pos += len(trail.group(0))
            ph = self.b.math.add(tex, False)
            if len(tex) > 36:
                out.append(keep(f'<span class="math-inline math-long">{ph}{punct}</span>'))
            elif punct:
                out.append(keep(f'<span class="nobr"><span class="math-inline">{ph}</span>{punct}</span>'))
            else:
                out.append(keep(f'<span class="math-inline">{ph}</span>'))
        out.append(text[pos:])
        text = ''.join(out)
        text = DISPLAY_IN_LINE.sub(lambda m: keep('<span class="math-display">' + self.b.math.add(m.group(1).strip(), True)
                                                  + '</span>'), text)
        if '\\(' in text or '\\)' in text:
            self.problems.append('unbalanced TeX delimiters in: ' + text[:100])
        esc = html.escape(text, quote=False)
        defs = self.refdefs.get(self.current, {})

        def ref(m):
            label, key = m.group(1), (m.group(2) or m.group(1)).strip().lower()
            if key not in defs:
                return m.group(0)
            return keep(self.link(self.emphasis(label), defs[key]))
        if defs:
            esc = re.sub(r'\[([^\[\]]+)\]\[([^\[\]]*)\]', ref, esc)
            esc = re.sub(r'\[([^\[\]]+)\](?![\(\[:])()', ref, esc)
        esc = re.sub(r'\[([^\[\]]+)\]\(([^)\s]+)\)', lambda m: keep(self.link(self.emphasis(m.group(1)), m.group(2))), esc)
        esc = self.emphasis(esc)
        esc = re.sub(r'\((\d+\.\d+[a-z]?)\)', self.eqref, esc)
        while '\x01' in esc:
            esc = re.sub('\x01(\\d+)\x01', lambda m: slots[int(m.group(1))], esc)
        return esc

    @staticmethod
    def emphasis(esc):
        esc = re.sub(r'\*\*(?=\S)(.+?)(?<=\S)\*\*', r'<strong>\1</strong>', esc)
        esc = re.sub(r'__(?=\S)(.+?)(?<=\S)__', r'<strong>\1</strong>', esc)
        esc = re.sub(r'(?<![\w*\\])\*(?=[^\s*])([^*\n]+?)(?<=[^\s*\\])\*(?![\w*])', r'<em>\1</em>', esc)
        return re.sub(r'(?<![\w_])_(?=[^\s_])([^_\n]+?)(?<=[^\s_])_(?![\w_])', r'<em>\1</em>', esc)

    def eqref(self, m):
        tag = m.group(1)
        target = self.tags.get(tag)
        if not target:
            return m.group(0)
        return f'(<a href="#{target}" data-ref="equation" class="mg-eqref">{html.escape(tag)}</a>)'

    def link(self, label, target):
        """label: already escaped and emphasised; its formulas are slots that inline() restores.
        Keep the scholarly identifier and PDF page in the text, including when a primary page
        is directly addressable. Locally resolved chapters and fragments use the book's own links."""
        t = html.unescape(target).strip()
        if t.startswith('definition-use:'):
            use = t.split(':', 1)[1]
            self.pending_refs.append((self.definition_uses.by_id[use]['target'], self.current))
            return self.definition_uses.link(use, label)
        if t.startswith('<') and t.endswith('>'):
            t = t[1:-1].strip()
        if t in ("celestial-current-product.pdf", "celestial-residue.pdf", "interacting-theories.pdf",
                 "critical-points-and-sphere-insertions.pdf", "chiral-yangians.pdf"):
            return f'<a href="{t}" type="application/pdf" download>{label}</a>'
        public_file = re.fullmatch(r'(?:(?:https://research\.momentum\.inc/quantum-holography/)|(?:\.\.?/)*(?:quantum-holography/)?)(?:index|reference|atlas)\.html#([\w:.-]+)', t)
        if public_file:
            t = '#' + public_file.group(1)
        chapter_file = re.fullmatch(r'(?:\.\.?/)*(?:chapters/)?([\w-]+\.md)(?:#([\w:.-]+))?', t)
        if chapter_file and chapter_file.group(1) in self.chapter_files:
            t = '#' + (chapter_file.group(2) or self.chapter_files[chapter_file.group(1)])
        if t.startswith('#'):
            ident = t[1:]
            self.pending_refs.append((ident, self.current))
            return f'<a href="#{html.escape(ident)}" data-ref="\x02{html.escape(ident)}\x02">{label}</a>'
        if re.match(r'https?://', t):
            return scholarly_citation(label, t)
        self.local_links.append((self.current, t))
        return label

    # Blocks -----------------------------------------------------------------------------------------------------

    def display(self, b):
        ph = self.b.math.add(b['tex'], True)
        ident = f' id="{html.escape(b["id"])}"' if b.get('id') else ''
        if b.get('tag'):
            return (f'<div class="mg-display has-tag"{ident} data-tag="{html.escape(b["tag"])}">'
                    f'<div class="math-display">{ph}</div>'
                    f'<span class="mg-tag" aria-label="Equation {html.escape(b["tag"])}">({html.escape(b["tag"])})</span></div>')
        return f'<div class="mg-display"{ident}><div class="math-display">{ph}</div></div>'

    def index_text(self, ids, text):
        # The enclosing paragraph keeps its historical reader-generated address and numbering.
        for ident in reversed(ids):
            self.claim(ident, self.current)
            self.anchor_kind[ident] = 'text'
            text = f'<span id="{html.escape(ident, quote=True)}">{text}</span>'
        return text

    def para(self, b, cls=''):
        classes = ' '.join(x for x in (cls, 'mg-cont' if b.get('attached') else '') if x)
        attr = f' class="{classes}"' if classes else ''
        if b.get('passage_id'):
            ident = b['passage_id']
            self.claim(ident, self.current)
            self.anchor_kind[ident] = 'definition'
            attr += f' id="{html.escape(ident, quote=True)}"'
        elif b.get('front_text_id'):
            attr += f' id="{b["front_text_id"]}"'
        return f'<p{attr}>{self.index_text(b.get("source_ids", ()), self.inline(b["text"]))}</p>'

    def render(self, blocks, section_no=None, envs=True):  # noqa: C901
        """envs=False sets a copy (the glossary or the index of results): its lead-ins stay bold
        words, so that no second result block, anchor or tag is made for a statement the chapter already carries."""
        out = []
        i = 0
        while i < len(blocks):
            b = blocks[i]
            t = b['t']
            if t == 'p':
                lead = lead_in(b['text']) if envs else None
                if lead:
                    form, label, rest = lead
                    proof = form.kind in PROOF_FORMS
                    span = [b]
                    j = i + 1
                    implicit_end = None
                    while j < len(blocks) and not (proof and ends_proof(span[-1])):
                        nb = blocks[j]
                        if nb['t'] == 'p':
                            if lead_in(nb['text']):
                                break
                            continues = (not rest and len(span) == 1) or nb.get('attached') or re.match(r'^[a-z(,;]', nb['text'])
                        else:
                            continues = nb['t'] in ('math', 'list')
                        if not continues:
                            if not proof or nb['t'] not in ('p', 'table', 'quote', 'code'):
                                break
                            if implicit_end is None:
                                implicit_end = j
                        span.append(nb)
                        j += 1
                    # An authored end mark delimits even a long proof. Without one, a new independent
                    # paragraph belongs to the exposition; a fenced proof supplies its own exact boundary.
                    if implicit_end is not None and not ends_proof(span[-1]):
                        j = implicit_end
                        span = blocks[i:j]
                    body = ([dict(b, text=rest, source_ids=())] if rest else []) + span[1:]
                    out.append(self.environment(form, label, body, lead_ids=b.get('source_ids', ()), run_in=bool(rest)))
                    i = j
                    continue
                out.append(self.para(b))
            elif t == 'math':
                out.append(self.display(b if envs else dict(b, id=None)))
            elif t == 'h':
                level = min(6, b['level'] + 1)
                if not envs:
                    out.append(f'<h{level} class="mg-h{b["level"]}">{self.inline(b["text"])}</h{level}>')
                    i += 1
                    continue
                ident = b.get('id') or self.unique(f'{self.current}-{slugify(b["text"])}')
                if b.get('id'):
                    self.claim(ident, self.current)
                self.anchor_kind[ident] = 'section'
                out.append(f'<h{level} class="mg-h{b["level"]}" id="{html.escape(ident)}">{self.inline(b["text"])}</h{level}>')
            elif t == 'list':
                tag = 'ol' if b['ordered'] else 'ul'
                start = f' start="{b["start"]}"' if b['ordered'] and b['start'] != 1 else ''
                items = []
                for item in b['items']:
                    if len(item) == 1 and item[0]['t'] == 'p' and not (envs and lead_in(item[0]['text'])):
                        items.append(f'<li>{self.index_text(item[0].get("source_ids", ()), self.inline(item[0]["text"]))}</li>')
                    else:
                        items.append('<li>' + self.render(item, envs=envs) + '</li>')
                out.append(f'<{tag} class="mg-list"{start}>{"".join(items)}</{tag}>')
            elif t == 'quote':
                out.append(f'<blockquote class="mg-quote">{self.render(b["blocks"], envs=envs)}</blockquote>')
            elif t == 'table':
                head = ''.join(f'<th scope="col"{self.align(b, k)}>{self.inline(c)}</th>' for k, c in enumerate(b['head']))
                rows = ''.join('<tr>' + ''.join(f'<td{self.align(b, k)}>{self.inline(c)}</td>' for k, c in enumerate(r))
                               + '</tr>' for r in b['rows'])
                out.append(f'<div class="mg-table-wrap"><table class="mg-table"><thead><tr>{head}</tr></thead>'
                           f'<tbody>{rows}</tbody></table></div>')
            elif t == 'hr':
                out.append('<hr class="mg-rule">')
            elif t == 'code':
                out.append(f'<pre class="mg-code"><code>{html.escape(b["text"])}</code></pre>')
            elif t == 'figure':
                out.append(self.figure(b['id']))
            elif t == 'front-figure':
                self.claim(b['id'], 'front')
                self.anchor_kind[b['id']] = 'figure'
                out.append(self.authored_markup(b['file']))
            elif t == 'div':
                out.append(self.div(b, envs))
            i += 1
        return ''.join(out)

    def align(self, b, k):
        a = b['align'][k] if k < len(b['align']) else ''
        return f' style="text-align:{a}"' if a else ''

    def environment(self, form, label_md, body_blocks, ident=None, envs=True, *, lead_ids=(), run_in=False):
        label = self.inline(label_md)
        if not envs:
            head = f'<strong>{label}</strong>'
        elif ident:
            self.claim(ident, self.current)
        else:
            label_text = re.sub(r'\s+', ' ', re.sub(r'\*|_', '', label_md)).strip().rstrip('.:')
            ident = self.unique(f'{self.current}-{slugify(label_text)}')
        if envs:
            self.claim(ident + '-h', self.current)
            self.environment_forms[ident] = form
            self.anchor_kind[ident] = 'definition' if form.kind == 'definition' else 'result'
            mark = KIND_MARK.get(form.style)
            qualifier = 'Open ' if form.status == 'open' and re.match(r'^(?:problem|question)\b', label_md, re.I) else ''
            head = (f'<span class="mg-env-label" id="{ident}-h" data-block-title>{self.mark(mark) if mark else ""}'
                    f'{qualifier}<span class="mg-env-name">{label}</span></span>')
        inner = self.render(body_blocks, envs=envs)
        # The label runs into the first paragraph, as in a printed book; a statement that opens with a display or a
        # list has its label on a line of its own.
        if not run_in:
            head = self.index_text(lead_ids, head)
        if inner.startswith(('<p>', '<p class="mg-cont">')) or (lead_ids and run_in and inner.startswith('<p ')):
            first, end, remainder = inner.partition('</p>')
            opening, _, first = first.partition('>')
            opening = '<p' if opening == '<p class="mg-cont"' else opening
            inner = opening + '>' + self.index_text(lead_ids if run_in else (), head + ' ' + first) + end + remainder
        else:
            inner = f'<p class="mg-env-alone">{self.index_text(lead_ids if run_in else (), head)}</p>' + inner
        if not envs:
            return inner
        if form.kind == 'proof' and body_blocks and not ends_proof(body_blocks[-1]):
            qed = '<span class="mg-qed" aria-hidden="true">∎</span>'
            inner = inner[:-4] + qed + '</p>' if inner.endswith('</p>') else inner + f'<p class="mg-qed-line">{qed}</p>'
        style = form.style if form.is_result else PROSE_STYLES.get(form.kind, form.kind)
        css = 'mg-proof' if form.kind in PROOF_FORMS else f'mg-env mg-env-{style}'
        attributes = f'data-env="{form.kind}" data-kind="{form.kind}"'
        if form.status:
            attributes += f' data-status="{form.status}"'
        if form.kind == 'definition':
            attributes += ' data-term'
        if form.is_result:
            attributes += f' data-result data-result-family="{form.style}"'
        return f'<div class="{css}" id="{ident}" {attributes} role="group" aria-labelledby="{ident}-h">{inner}</div>'

    def div(self, b, envs=True):
        cls, attrs = b['cls'], b['attrs']
        if not b.get('closed', True):
            self.problems.append(f'{self.current}: a ::: block ({cls or "unnamed"}) is never closed')
        if cls == 'transition':
            return f'<div class="mg-transition">{self.render(b["blocks"], envs=envs)}</div>'
        word = cls.replace('-', ' ')
        form = heading_form(word)
        if form:
            status = attrs.get('status', attrs.get('data-status'))
            if status:
                qualifier = {'conjecture': 'conjectural'}.get(status, status)
                qualified = heading_form(f'{qualifier} {word}')
                if status == 'proved' and form.kind in ('result', 'claim', 'consequence'):
                    form, word = Form(form.kind, status), 'proved ' + word
                elif status != form.status and (qualifier not in QUALIFIERS or not qualified or
                                              qualified.kind != form.kind or qualified.status != QUALIFIERS[qualifier]):
                    self.problems.append(f'{self.current}: {cls} fence has incompatible status {status!r}')
                elif status != form.status:
                    word, form = qualifier + ' ' + word, qualified
            title = attrs.get('title')
            number = attrs.get('n')
            name = self.L.get('kind_' + word.replace(' ', '_')) or word.capitalize()
            if word == 'conditional':
                name = self.L.get('kind_conditional', 'Conditional result')
            if word == 'open':
                name = self.L.get('kind_open', 'Open problem')
            label = name + (f' {number}' if number else '') + (f' ({title})' if title else '') + '.'
            blocks = b['blocks']
            lead = lead_in(blocks[0]['text']) if blocks and blocks[0]['t'] == 'p' else None
            unqualified = re.sub(r'^(?:conditional|conjectural|heuristic|open|proved)\s+', '', label, flags=re.I)
            lead_ids, run_in = (), False
            if lead and lead[0].kind == form.kind and (not (title or number) or
                    lead[1].lower() in (label.lower(), unqualified.lower())):
                authored, authored_label, rest = lead
                if form.status == authored.status or form.status == DEFAULT_STATUS.get(form.kind):
                    form, label = authored, authored_label
                elif authored.status == DEFAULT_STATUS.get(form.kind):
                    # An explicit qualified fence may enclose the original, unqualified run-in heading.
                    label = STATUS_ADJECTIVE[form.status] + ' ' + authored_label[0].lower() + authored_label[1:]
                else:
                    self.problems.append(f'{self.current}: {cls} fence conflicts with its label {authored_label!r}')
                lead_ids, run_in = blocks[0].get('source_ids', ()), bool(rest)
                blocks = ([dict(blocks[0], text=rest, source_ids=())] if rest else []) + blocks[1:]
            return self.environment(form, label, blocks, attrs.get('id'), envs, lead_ids=lead_ids, run_in=run_in)
        self.problems.append(f'{self.current}: unknown ::: block "{cls}"')
        return self.render(b['blocks'], envs=envs)

    def authored_markup(self, name):
        """An authored figure file as it is served: its markup as written, with the TeX between \\( and \\) typeset by
        the page like the formulas of the text. A file without such TeX is served byte for byte."""
        if Path(name).name != name or Path(name).suffix != '.html':
            raise ValueError(f'Invalid authored figure file {name!r}')
        text = (self.path.parent / name).read_text(encoding='utf-8')
        return INLINE_MATH.sub(
            lambda m: '<span class="math-inline">' + self.b.math.add(m.group(1).strip(), False) + '</span>', text)

    def figure(self, fid):
        if fid in self.authored:
            rec = self.authored[fid]
            if rec.get('chapter_id') and rec['chapter_id'] != self.current:
                self.problems.append(f'{self.current}: figure {fid} belongs to {rec["chapter_id"]} in the manifest')
            try:
                markup = self.authored_markup(rec.get('file') or '')
            except (OSError, ValueError) as e:
                self.problems.append(f'figure {fid}: its authored file cannot be read ({e})')
                return ''
            if not re.search(rf'<figure\b[^>]*\bid="{re.escape(fid)}"[^>]*\bdata-figure\b', markup):
                self.problems.append(f'figure {fid}: the authored file is not figure[data-figure][id="{fid}"]')
            self.figures_placed.append(fid)
            return f'<div class="mg-figure">{markup}</div>'
        if fid in self.diagrams:
            markup = Diagram(self, self.diagrams[fid]).render()
            if markup:
                self.figures_placed.append(fid)
            return f'<div class="mg-figure">{markup}</div>' if markup else ''
        rec = self.figures.get(fid)
        if rec is None:
            self.problems.append(f'{self.current}: "::: figure {fid}" names no figure record in the manifest')
            return ''
        if rec.get('chapter_id') and rec['chapter_id'] != self.current:
            self.problems.append(f'{self.current}: figure {fid} belongs to {rec["chapter_id"]} in the manifest')
        if self.figmod is None:
            return ''
        got = self.figmod.render(rec, FigureContext(self))
        for p in got.get('problems', []):
            self.problems.append(f'figure {fid}: {p}')
        markup = got.get('html', '')
        if markup:
            self.figures_placed.append(fid)
            if not re.search(rf'<figure\b[^>]*\bid="{re.escape(fid)}"[^>]*\bdata-figure\b', markup):
                self.problems.append(f'figure {fid}: the rendered element is not figure[data-figure][id="{fid}"]')
        return f'<div class="mg-figure">{markup}</div>' if markup else ''

    # Pieces of the book ------------------------------------------------------------------------------------------

    def chapter_label(self, c):
        return self.L.get('chapter_n', 'Chapter {n}').replace('{n}', str(c['number']))

    def part_label(self, p):
        return self.L.get('part_n', 'Part {n}').replace('{n}', ROMAN[self.part_no[p['id']] - 1])

    def chapter_download(self, c, anchor):
        item = c.get('downloads', {}).get(anchor)
        if not item:
            return ''
        link = self.link(html.escape(item['label']), item['file'])
        return f'<nav aria-label="Downloads">{link}</nav>'

    def chapter(self, c):
        cid = c['id']
        self.current = cid
        p = self.part_of.get(cid)
        blocks = self.blocks.get(cid)
        L = self.L
        total = len(self.chapters)
        number = c['number']
        kicker = ''
        if p:
            kicker = (f'<p class="mg-ch-kicker" data-chapter-kicker><a class="mg-ch-part" href="#{p["id"]}-title">'
                      f'<span class="mg-ch-partno">{html.escape(self.part_label(p))}</span> '
                      f'<span class="mg-ch-partname">{html.escape(p["title"])}</span></a>'
                      f'<span class="mg-ch-pos">{html.escape(L.get("chapter_of", "Chapter {n} of {total}").replace("{n}", str(number)).replace("{total}", str(total)))}</span></p>')
        head = (f'<header class="mg-ch-head">{kicker}'
                f'<div class="mg-ch-titleblock"><p class="mg-ch-no" aria-hidden="true">{number}</p>'
                f'<h2 class="mg-ch-title" id="{cid}-h">{html.escape(c["title"])}</h2></div></header>')
        prereq_items = ''.join(
            f'<li><a href="#{q}" data-ref="chapter"><span class="mg-pre-no">{self.by_id[q]["number"]}</span> '
            f'<span class="mg-pre-title">{html.escape(self.by_id[q]["title"])}</span></a></li>'
            for q in c.get('prerequisites', []) if q in self.by_id)
        prereq = (f'<div class="mg-aside-block mg-aside-pre"><p class="mg-aside-h" id="{cid}-pre-h">{html.escape(L.get("draws_on", "Draws on"))}</p>'
                  f'<ul class="mg-pre" data-prerequisites aria-labelledby="{cid}-pre-h">{prereq_items}</ul></div>'
                  if prereq_items else '<ul class="mg-pre" data-prerequisites hidden></ul>')
        later = [d for d in self.chapters if cid in d.get('prerequisites', [])]
        if later:
            prereq += (f'<div class="mg-aside-block mg-aside-post"><p class="mg-aside-h">{html.escape(L.get("used_in", "Used later in"))}</p>'
                       '<p class="mg-post">' + ', '.join(
                           f'<a href="#{d["id"]}" data-ref="chapter" title="{html.escape(d["title"])}">{d["number"]}</a>' for d in later)
                       + '</p></div>')
        terms = ''
        if c.get('key_terms'):
            terms = (f'<div class="mg-aside-block mg-aside-terms"><p class="mg-aside-h">{html.escape(L.get("key_terms", "Terms"))}</p>'
                     '<ul class="mg-terms">' + ''.join(f'<li>{html.escape(t)}</li>' for t in c['key_terms']) + '</ul></div>')
        self.opening_html = ''
        if blocks is None:
            body = ''
            sections_toc = ''
        else:
            opening, sections = self.split_sections(blocks)
            body_parts = []
            if opening:
                html_open = self.render(opening)
                html_open = re.sub(r'^<p>', '<p class="mg-lead">', html_open, count=1)
                self.opening_html = f'<div class="mg-ch-open">{html_open}</div>'
            toc_items = []
            for k, (h, sblocks) in enumerate(sections, 1):
                sid = h.get('id') or self.unique(f'{cid}-{slugify(h["text"])}')
                if h.get('id'):
                    self.claim(sid, cid)
                self.anchor_kind[sid] = 'section'
                no = f'{number}.{k}'
                title = self.inline(h['text'])
                toc_items.append(f'<li><a href="#{sid}" data-ref="section"><span class="mg-sec-no">{no}</span> '
                                 f'<span class="mg-sec-title">{title}</span></a></li>')
                self.section_index.setdefault(cid, []).append((sid, no, title))
                body_parts.append(f'<section class="mg-sec" id="{sid}" data-section aria-labelledby="{sid}-h">'
                                  f'<h3 class="mg-sec-head" id="{sid}-h"><span class="mg-sec-no">{no}</span> '
                                  f'<span class="mg-sec-title">{title}</span></h3>{self.render(sblocks)}{self.chapter_download(c,sid)}</section>')
            body = ''.join(body_parts)
            sections_toc = (f'<div class="mg-aside-block mg-aside-toc"><p class="mg-aside-h">{html.escape(L.get("in_chapter", "In this chapter"))}</p>'
                            f'<ol class="mg-ch-toc">{"".join(toc_items)}</ol></div>') if toc_items else ''
        aside = (f'<aside class="mg-ch-aside" aria-label="{html.escape(L.get("aside", "This chapter in the book"))}">'
                 f'<div class="mg-aside-block mg-aside-map">{self.locator(cid)}</div>{prereq}{terms}{sections_toc}</aside>')
        end = self.chapter_download(c,cid) + self.chapter_end(c)
        article = (f'<article class="mg-chapter" id="{cid}" data-chapter data-part="{p["id"] if p else ""}" data-number="{number}" '
                   f'aria-labelledby="{cid}-h">{head}<div class="mg-ch-frame">{self.opening_html}{aside}<div class="mg-ch-text">{body}</div></div>'
                   f'{end}</article>')
        if targets := self.index_targets.get(cid):
            missing = targets - set(re.findall(r'(?<![\w-])id="([^"]+)"', article))
            if missing:
                self.problems.append(f'{cid}: index destinations absent from this chapter: {sorted(missing)}')
        return article

    def split_sections(self, blocks):
        opening, sections = [], []
        for b in blocks:
            if b['t'] == 'h' and b['level'] == 2:
                sections.append((b, []))
            elif sections:
                sections[-1][1].append(b)
            else:
                opening.append(b)
        return opening, sections

    def chapter_end(self, c):
        k = self.order.index(c['id'])
        L = self.L
        links = []
        if k > 0:
            q = self.by_id[self.order[k - 1]]
            links.append(f'<a class="mg-end-prev" rel="prev" href="#{q["id"]}"><span class="mg-end-dir">'
                         f'{html.escape(L.get("previous", "Previous"))}</span><span class="mg-end-ch">'
                         f'<span class="mg-end-no">{q["number"]}</span> <span class="mg-end-title">{html.escape(q["title"])}</span></span></a>')
        if k + 1 < len(self.order):
            q = self.by_id[self.order[k + 1]]
            summary = f'<span class="mg-end-summary">{self.b.rich(q["summary"], terms=False)}</span>' if q.get('summary') else ''
            links.append(f'<a class="mg-end-next" rel="next" href="#{q["id"]}"><span class="mg-end-dir">'
                         f'{html.escape(L.get("next", "Next"))}</span><span class="mg-end-ch">'
                         f'<span class="mg-end-no">{q["number"]}</span> <span class="mg-end-title">{html.escape(q["title"])}</span></span>'
                         f'{summary}</a>')
        else:
            links.append(f'<a class="mg-end-next mg-end-ref" href="#contents"><span class="mg-end-dir">'
                         f'{html.escape(L.get("contents", "Contents"))}</span></a>')
        return (f'<nav class="mg-ch-end" data-chapter-end aria-label="{html.escape(L.get("chapters", "Chapters"))}">'
                f'{"".join(links)}</nav>')

    # The map of the book: one grid of columns, a node per chapter and a gap between parts, shared by the front
    # matter's map and each chapter's locator. Arcs join a chapter to each earlier chapter it draws on.

    def columns(self):
        cols = []
        for pi, p in enumerate(self.parts):
            if pi:
                cols.append(('gap', p['id']))
            for cid in p.get('chapter_ids', []):
                if cid in self.by_id:
                    cols.append(('node', cid))
        widths = [1.0 if k == 'node' else 0.55 for k, _ in cols]
        total = sum(widths)
        centre, colno, acc = {}, {}, 0.0
        for n, ((k, cid), w) in enumerate(zip(cols, widths), 1):
            if k == 'node':
                centre[cid] = (acc + w / 2) / total
                colno[cid] = n
            acc += w
        template = ' '.join(f'{w:g}fr' for w in widths)
        return cols, template, centre, colno

    def arcs(self, current=None):
        _, _, centre, _ = self.columns()
        paths = []
        for c in self.chapters:
            for q in c.get('prerequisites', []):
                if q not in centre or c['id'] not in centre:
                    continue
                x1, x2 = centre[q] * 1000, centre[c['id']] * 1000
                span = abs(x2 - x1) / 1000
                h = 10 + 86 * span ** 0.75  # apex height, of 100
                ctrl = 100 - h / 0.75
                cls = 'mg-arc'
                if current:
                    if c['id'] == current:
                        cls += ' is-in'
                    elif q == current:
                        cls += ' is-out'
                    else:
                        continue  # the locator draws only this chapter's own arcs
                paths.append(f'<path class="{cls}" data-from="{q}" data-to="{c["id"]}" '
                             f'd="M{x1:.1f} 100C{x1:.1f} {ctrl:.1f} {x2:.1f} {ctrl:.1f} {x2:.1f} 100"/>')
        return ''.join(paths)

    def reduced_prerequisites(self):
        """Each chapter's direct prerequisites: the ones not reached through another of its prerequisites. The same
        reading order as the manifest's full lists, each relation drawn once."""
        pre = {c['id']: {q for q in c.get('prerequisites', []) if q in self.by_id} for c in self.chapters}
        memo = {}

        def reach(c, path=()):
            if c in memo:
                return memo[c]
            out = set()
            for q in pre[c]:
                if q not in path:
                    out |= {q} | reach(q, path + (c,))
            memo[c] = out
            return out
        return {c: {q for q in ps if not any(q in reach(o) for o in ps if o != q)} for c, ps in pre.items()}

    def book_map(self):
        """The book as one labelled figure: a column per part, a box per chapter with its number and title, and a line
        from a chapter to each later chapter that draws on it directly. Lines run down a column or through the gutters
        between columns, and a line that skips a part runs along the foot of the figure, so that no line crosses a box.
        Positions are fractions of the figure's width and multiples of the type size, so the lines meet the boxes at
        every width; below a width where the titles fit, the figure gives way to the contents, which lists the same."""
        L = self.L
        red = self.reduced_prerequisites()
        parts = [p for p in self.parts if any(cid in self.by_id for cid in p.get('chapter_ids', []))]
        col, row = {}, {}
        for i, p in enumerate(parts):
            for r, cid in enumerate([x for x in p['chapter_ids'] if x in self.by_id]):
                col[cid], row[cid] = i, r
        nrows = max(row.values()) + 1
        M_, B_, G_ = .06, 1.0, .26
        units = 2 * M_ + len(parts) * B_ + (len(parts) - 1) * G_
        U = 1000 / units

        # Each box is as tall as its title needs where the map is narrowest (the sheet shows the map from 52 body sizes
        # wide: a box is then about fifteen characters of its type wide), wrapped at words without hyphenation; each row
        # is as tall as its tallest box. Every length here is in tenths of the body size, the font size of the plot, the
        # boxes and the arrowheads alike (only a box's words are set smaller): a line of the box's words (0.833 x 1.22)
        # is about 10.2, the box's padding and rule about 7.5.
        def lines(title, cap=15):
            n, cur = 1, 0
            for w in title.split():
                if cur == 0:
                    cur = len(w)
                elif cur + 1 + len(w) <= cap:
                    cur += 1 + len(w)
                else:
                    n, cur = n + 1, len(w)
            return n
        hbox = {cid: round(lines(self.by_id[cid]['title']) * 10.2 + 7.5) for cid in col}
        rows_h = [max(hbox[cid] for cid in col if row[cid] == r) for r in range(nrows)]
        GAP = 11
        row_top = [sum(rows_h[:r]) + GAP * r for r in range(nrows)]

        def left(i):
            return (M_ + i * (B_ + G_)) * U

        def right(i):
            return left(i) + B_ * U

        def cx(i):
            return left(i) + B_ * U / 2

        def top(cid):
            return row_top[row[cid]]

        def mid(cid):
            return top(cid) + hbox[cid] / 2

        def bot(cid):
            return top(cid) + hbox[cid]


        def gap_y(k):  # the middle of the gap under row k
            return row_top[k] + rows_h[k] + GAP / 2
        edges = [(q, c['id']) for c in self.chapters for q in sorted(red.get(c['id'], ()), key=lambda x: self.by_id[x]['number'])]
        plan = []
        for a_, c_ in edges:
            i, r, j, s_ = col[a_], row[a_], col[c_], row[c_]
            if i == j and s_ == r + 1:
                plan.append(('down', a_, c_, None))
            elif i == j:
                plan.append(('skip', a_, c_, i - 1))
            elif j == i + 1:
                plan.append(('next', a_, c_, i))
            else:
                plan.append(('long', a_, c_, j - 1))
        ins, outs = {}, {}
        for kind, a_, c_, gk in plan:
            if kind != 'down':
                ins.setdefault(c_, []).append(a_)
            if kind in ('skip', 'next', 'long'):
                outs.setdefault(a_, []).append(c_)
        lanes = {}
        for kind, a_, c_, gk in plan:
            straight = (kind == 'next' and row[a_] == row[c_] and len(ins[c_]) == 1 and len(outs[a_]) == 1)
            if kind == 'long':
                lanes.setdefault(col[a_], []).append((a_, c_))  # the gutter to the right of the source
            if gk is not None and not straight:
                lanes.setdefault(gk, []).append((a_, c_))

        def lane_x(gk, a_, c_):
            items = lanes[gk]
            k, n = items.index((a_, c_)), len(items)
            g0 = right(gk) if gk >= 0 else 0.0
            g1 = left(gk + 1)
            return g0 + (g1 - g0) * (k + 1) / (n + 1)

        def spread(lst, x, base):
            n, k = len(lst), lst.index(x)
            return base + (k - (n - 1) / 2) * 8

        longs = [e for e in plan if e[0] == 'long']
        crossing = {}
        for kind, a_, c_, gk in longs:
            s_, r_ = row[c_], row[a_]
            k = s_ if s_ < r_ else s_ - 1  # the gap beside the target's row, on the source's side
            k = min(max(k, 0), nrows - 2)
            crossing.setdefault(k, []).append((a_, c_))
        H = row_top[-1] + rows_h[-1] + 10
        paths, tips = [], []
        for kind, a_, c_, gk in plan:
            i, j = col[a_], col[c_]
            if kind == 'down':
                x = cx(i)
                d = f'M{x:.1f} {bot(a_):.1f}V{top(c_):.1f}'
                tips.append(('down', x, top(c_), a_, c_))
            else:
                yin = spread(ins[c_], a_, mid(c_))
                if kind == 'long':
                    # Out of the source's right side, along its gutter to the gap between rows beside the target, across
                    # the columns between them in that gap (where no box stands), then up or down the target's gutter.
                    yout = spread(outs[a_], c_, mid(a_))
                    k = next(k for k, es in crossing.items() if (a_, c_) in es)
                    yg = gap_y(k) + (crossing[k].index((a_, c_)) - (len(crossing[k]) - 1) / 2) * 4
                    d = (f'M{right(i):.1f} {yout:.1f}H{lane_x(i, a_, c_):.1f}V{yg:.1f}H{lane_x(gk, a_, c_):.1f}'
                         f'V{yin:.1f}H{left(j):.1f}')
                elif kind == 'skip':
                    yout = spread(outs[a_], c_, mid(a_))
                    d = f'M{left(i):.1f} {yout:.1f}H{lane_x(gk, a_, c_):.1f}V{yin:.1f}H{left(j):.1f}'
                elif (a_, c_) in lanes.get(gk, []):
                    yout = spread(outs[a_], c_, mid(a_))
                    d = f'M{right(i):.1f} {yout:.1f}H{lane_x(gk, a_, c_):.1f}V{yin:.1f}H{left(j):.1f}'
                else:
                    yin = min(mid(a_), mid(c_)) + abs(mid(a_) - mid(c_)) / 2 if hbox[a_] != hbox[c_] else mid(a_)
                    yin = max(top(c_) + 6, min(yin, bot(c_) - 6))
                    d = f'M{right(i):.1f} {max(top(a_) + 6, min(yin, bot(a_) - 6)):.1f}H{left(j):.1f}'
                tips.append(('right', left(j), yin, a_, c_))
            paths.append(f'<path class="mg-bm-edge" data-from="{a_}" data-to="{c_}" d="{d}"/>')
        tip_html = ''.join(f'<span class="mg-bm-tip is-{k}" data-from="{a_}" data-to="{c_}" style="left:{x / 10:.2f}%;top:{y / 10:.2f}em"></span>'
                           for k, x, y, a_, c_ in tips)
        boxes = []
        for c in self.chapters:
            if c['id'] not in col:
                continue
            i, r = col[c['id']], row[c['id']]
            boxes.append(f'<a class="mg-bm-box" href="#{c["id"]}" data-ch="{c["id"]}" style="left:{left(i) / 10:.2f}%;'
                         f'width:{B_ * U / 10:.2f}%;top:{top(c["id"]) / 10:.2f}em;min-height:{hbox[c["id"]] / 10:.2f}em">'
                         f'<span class="mg-bm-no">{c["number"]}</span> <span class="mg-bm-title">{html.escape(c["title"])}</span></a>')
        template = ' '.join([f'{M_:g}fr'] + [f'{B_:g}fr {G_:g}fr' if i < len(parts) - 1 else f'{B_:g}fr' for i in range(len(parts))] + [f'{M_:g}fr'])
        heads = ''.join(f'<li class="mg-bm-part" style="grid-column:{2 + 2 * i}">'
                        f'<a href="#{p["id"]}-title"><span class="mg-bm-partno">{html.escape(self.part_label(p))}</span> '
                        f'<span class="mg-bm-parttitle">{html.escape(p["title"])}</span></a></li>' for i, p in enumerate(parts))
        self.map_edges = edges
        return (f'<figure class="mg-bookmap" aria-labelledby="mg-map-h mg-map-cap">'
                f'<p class="mg-map-h" id="mg-map-h">{html.escape(L.get("map_title", "The chapters and their reading prerequisites"))}</p>'
                f'<div class="mg-bm-stage"><ol class="mg-bm-parts" style="grid-template-columns:{template}">{heads}</ol>'
                f'<div class="mg-bm-plot" style="height:{H / 10:.1f}em">'
                f'<svg class="mg-bm-svg" viewBox="0 0 1000 {H}" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
                f'{"".join(paths)}</svg>{tip_html}{"".join(boxes)}</div></div>'
                f'<figcaption class="mg-map-cap" id="mg-map-cap">{html.escape(L.get("map_caption", ""))}</figcaption></figure>')

    def parts_glance(self):
        """The five parts at a glance, each with its chapters' numbers, linked to the part in the contents."""
        L = self.L
        items = []
        for p in self.parts:
            chs = [self.by_id[cid]['number'] for cid in p.get('chapter_ids', []) if cid in self.by_id]
            if not chs:
                continue
            span = (L.get('chapters_range', 'Chapters {first}–{last}').replace('{first}', str(chs[0])).replace('{last}', str(chs[-1]))
                    if len(chs) > 1 else L.get('chapter_n', 'Chapter {n}').replace('{n}', str(chs[0])))
            items.append(f'<li><a href="#{p["id"]}-title"><span class="mg-glance-no">{ROMAN[self.part_no[p["id"]] - 1]}</span> '
                         f'<span class="mg-glance-title">{html.escape(p["title"])}</span></a> <span class="mg-glance-ch">{html.escape(span)}</span></li>')
        return (f'<div class="mg-rail-block"><p class="mg-rail-h" id="mg-glance-h">{html.escape(L.get("parts", "Parts"))}</p>'
                f'<ol class="mg-glance" aria-labelledby="mg-glance-h">{"".join(items)}</ol></div>')

    def routes(self):
        L = self.L
        items = []
        for r in self.m.get('routes', []) or []:
            chs = [cid for cid in r.get('chapter_ids', []) if cid in self.by_id]
            unknown = [cid for cid in r.get('chapter_ids', []) if cid not in self.by_id]
            if unknown:
                self.problems.append(f'reader manifest: route {r.get("id")} names unknown chapters {unknown}')
            nums = number_ranges([self.by_id[cid]['number'] for cid in chs])
            items.append(f'<li class="mg-route"><a class="mg-route-name" href="#{chs[0] if chs else "contents"}" '
                         f'data-route="{html.escape(r["id"])}" data-route-chapters="{" ".join(chs)}">{html.escape(r["title"])}</a> '
                         f'<span class="mg-route-list">{html.escape(L.get("route_chapters", "Chapters {list}").replace("{list}", nums))}</span></li>')
        if not items:
            return ''
        return (f'<div class="mg-routes"><p class="mg-routes-h" id="mg-routes-h">{html.escape(L.get("routes", "Routes through the book"))}</p>'
                f'<ol class="mg-route-list-all" aria-labelledby="mg-routes-h">{"".join(items)}</ol></div>')

    def address_front_passages(self, blocks, section):
        """Keep a passage address when an earlier paragraph is inserted or its definition links change."""
        for block in self.walk(blocks):
            kind = block['t']
            if kind == 'h':
                section = block.get('id') or section
                continue
            if kind == 'p' and not block.get('passage_id') and not lead_in(block['text']):
                field, address_kind = 'front_text_id', 'text'
                words = re.sub(r'\[([^\[\]\n]+)\]\(definition-use:[a-z0-9-]+\)', r'\1', block['text'])
            elif kind == 'math' and not block.get('id'):
                field, address_kind = 'id', 'equation'
                words = block['tex']
            else:
                continue
            key = sha256(' '.join(words.split()).encode('utf-8')).hexdigest()[:12]
            ident = self.unique(f'{section}-{address_kind}-{key}')
            block[field] = ident
            self.anchor_kind[ident] = address_kind

    def introduction(self):
        text = self.m.get('introduction')
        if not text:
            return ''
        f = (self.path.parent / text).resolve() if isinstance(text, str) and text.endswith('.md') else None
        if f is not None and f.exists():
            text = f.read_text(encoding='utf-8')
        text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
        self.current = 'front'
        blocks = parse_blocks(self.definition_uses.mark('opening', text).splitlines())
        self.address_front_passages(blocks, 'opening-question')
        placements = self.m.get('front_figures', [])
        if placements:
            by_paragraph = {}
            for item in placements:
                name = item['file']
                if Path(name).name != name or Path(name).suffix != '.html':
                    raise ValueError(f'Invalid front figure file {name!r}')
                by_paragraph.setdefault(item['after_paragraph'], []).append(item)
            placed, paragraph = [], 0
            for block in blocks:
                placed.append(block)
                if block['t'] == 'p':
                    paragraph += 1
                    for item in by_paragraph.pop(paragraph, []):
                        placed.append({'t': 'front-figure', 'id': item['id'], 'file': item['file']})
            if by_paragraph:
                raise ValueError(f'No source paragraph at front figure placements {sorted(by_paragraph)}.')
            blocks = placed
        out = self.render(blocks)
        out = re.sub(r'^<p( id="[^"]*")?>', r'<p class="mg-lead"\1>', out, count=1)
        destination = ' id="opening-question" role="region" aria-label="The opening question"' if self.m.get('expanded_introduction') else ''
        return f'<div class="mg-front-intro"{destination}>{out}</div>'

    def section_title(self, sid):
        for cid, items in self.section_index.items():
            for s_id, no, title in items:
                if s_id == sid:
                    return cid, no, title
        return None

    def where_link(self, chapter_id, section_id):
        """'Chapter 4, 4.2 Title' linked to the section (or the chapter when the section is a subsection)."""
        c = self.by_id.get(chapter_id)
        st = self.section_title(section_id) if section_id else None
        if st:
            return (f'<a href="#{html.escape(section_id)}" data-ref="section">{html.escape(self.chapter_label(c))}, '
                    f'<span class="mg-sec-no">{st[1]}</span> {st[2]}</a>')
        target = section_id if section_id else (c['id'] if c else '')
        self.pending_refs.append((target, 'glossary/index'))
        kind = self.anchor_kind.get(target, 'section')
        return f'<a href="#{html.escape(target)}" data-ref="{kind}">{html.escape(self.chapter_label(c)) if c else html.escape(target)}</a>'

    def excerpt(self, text, chapter):
        # A copied passage uses the link definitions of its own Markdown file.
        place, self.current = self.current, chapter
        try:
            return self.render(parse_blocks(text.splitlines()), envs=False)
        finally:
            self.current = place

    def glossary(self):
        """The author's glossary records (verbatim definitions), alphabetically, each linked to the section where the
        chapter gives it. The entry carries the term's id (data-term); the chapter remains the definition's context."""
        L = self.L
        terms = sorted(self.terms.values(), key=lambda t: (t.get('label') or t.get('term') or '').lower())
        if not terms:
            return ''
        entries = []
        self.current = 'glossary'
        for t in terms:
            text = re.sub(r'\{#[A-Za-z][\w:.-]*\}', '', t.get('definition') or '')
            body = self.excerpt(text, t.get('chapter_id'))
            label = self.b.rich(t.get('label') or t.get('term'), terms=False)
            where = t.get('definition_ref') or t.get('section_id')
            if target := t.get('source_target'):
                self.pending_refs.append((target, 'glossary'))
                label = f'<a href="#{html.escape(target)}" data-ref="{self.anchor_kind.get(target, "text")}">{label}</a>'
                where = t.get('section_id')
            if t['id'] in self.reference_ids:
                # The former page already has this id; its old addresses keep it, and neither id is renamed here.
                self.warnings.append(f'glossary: term id {t["id"]} is already an anchor of the former page; the entry is '
                                     f'shown without that id until the author gives the term a distinct id')
                ident = f'glossary-entry-{t["id"]}'
                self.claim(ident, 'glossary')
                id_attr = f' data-term-id="{html.escape(t["id"])}"'
            else:
                ident = t['id']
                self.claim(ident, 'glossary')
                self.anchor_kind[ident] = 'definition'
                id_attr = f' id="{html.escape(ident)}"'
            entries.append(f'<div class="mg-gl-entry"{id_attr} data-term role="group" aria-labelledby="{html.escape(ident)}-h">'
                           f'<p class="mg-gl-head"><dfn class="mg-gl-term" id="{html.escape(ident)}-h" data-block-title>{label}</dfn> '
                           f'<span class="mg-gl-where">{html.escape(L.get("defined_in", "Defined in"))} '
                           f'{self.where_link(t.get("chapter_id"), where)}</span></p>'
                           f'<div class="mg-gl-def">{body}</div></div>')
        return (f'<section class="mg-glossary" id="glossary" data-reference aria-labelledby="glossary-h">'
                f'<h2 class="mg-ref-h" id="glossary-h">{html.escape(L.get("glossary", "Glossary"))}</h2>'
                f'<p class="mg-ref-note">{html.escape(L.get("glossary_note", ""))}</p>{"".join(entries)}</section>')

    def results_index(self):
        """The author's result records by chapter: each title linked to its block in the chapter, its section, its
        status, and its statement as the record gives it (without repeating the title)."""
        L = self.L
        recs = list(self.theorems.values())
        if not recs:
            return ''
        self.current = 'index'
        out, last = [], None
        for t in sorted(recs, key=lambda t: self.order.index(t['chapter_id']) if t.get('chapter_id') in self.order else 99):
            c = self.by_id.get(t.get('chapter_id'))
            if t.get('chapter_id') != last and c:
                last = t['chapter_id']
                out.append(f'<h3 class="mg-ri-ch"><span class="mg-ri-no">{c["number"]}</span> '
                           f'<a href="#{c["id"]}" data-ref="chapter">{html.escape(c["title"])}</a></h3>')
            text = t.get('statement_excerpt') or ''
            lead = re.match(r'^\s*\*\*(.+?)\*\*\s*', text, re.S)
            if lead and re.sub(r'[\W_]+', '', lead.group(1)).lower() == re.sub(r'[\W_]+', '', t.get('title', '')).lower():
                text = text[lead.end():]
            body = self.excerpt(text, t.get('chapter_id'))
            declaration_id = t.get('rendered_anchor') or t['id']
            anchor = t.get('source_target') or declaration_id
            stated = heading_form(t.get('title', ''))
            recorded = heading_form((t.get('kind') or '').replace('-', ' '))
            declaration = self.environment_forms.get(declaration_id)
            form = declaration or stated or recorded or Form('result')
            status_word = t.get('status') or ''
            status = status_of(status_word) or form.status or (recorded and recorded.status)
            if declaration and declaration.status and status and declaration.status != status:
                self.problems.append(f'Index entry {t["id"]}: {status_word!r} disagrees with the '
                                     f'{declaration.status} declaration at #{anchor}')
                if declaration.status != 'proved':
                    status = declaration.status
                status_word = ''
            indexed = Form(form.kind, status)
            status_word = indexed.index_label(status_word)
            mark = KIND_MARK.get(indexed.style)
            mk = self.mark(mark) if mark else ''
            status_attr = f' data-status="{status}"' if status else ''
            self.pending_refs.append((anchor, 'index'))
            out.append(f'<div class="mg-ri-entry mg-ri-{indexed.style}" id="index-{html.escape(t["id"])}" '
                       f'data-kind="{indexed.kind}" data-index-env="{indexed.kind}"{status_attr}>'
                       f'<p class="mg-ri-head">{mk}<a class="mg-ri-title" href="#{html.escape(anchor)}" data-ref="{self.anchor_kind.get(anchor, "result")}">{self.b.rich(t.get("title", ""), terms=False)}</a> '
                       f'<span class="mg-ri-status">{html.escape(status_word)}</span> '
                       f'<span class="mg-ri-where">{self.where_link(t.get("chapter_id"), t.get("context_ref") or t.get("section_id"))}</span></p>'
                       f'<div class="mg-ri-statement">{body}</div></div>')
        return (f'<section class="mg-results-index" id="results-index" data-reference aria-labelledby="results-index-h">'
                f'<h2 class="mg-ref-h" id="results-index-h">{html.escape(L.get("results_index", "Index of results"))}</h2>'
                f'<p class="mg-ref-note">{html.escape(L.get("results_index_note", ""))}</p>{"".join(out)}</section>')

    def locator(self, current):
        """The book's map in miniature at the head of a chapter: this chapter, the chapters it draws on and the later
        chapters that draw on it. A picture only (its links are in the chapter's own list)."""
        cols, template, centre, colno = self.columns()
        c = self.by_id[current]
        pre = set(c.get('prerequisites', []))
        post = {d['id'] for d in self.chapters if current in d.get('prerequisites', [])}
        cells = []
        for d in self.chapters:
            if d['id'] not in colno:
                continue
            state = 'is-here' if d['id'] == current else 'is-pre' if d['id'] in pre else 'is-post' if d['id'] in post else ''
            cells.append(f'<span class="mg-dot {state}" style="grid-column:{colno[d["id"]]}"><span>{d["number"]}</span></span>')
        L = self.L
        key = (f'<p class="mg-locator-key"><span class="mg-key mg-key-here">{html.escape(L.get("locator_here", "This chapter"))}</span>'
               f'<span class="mg-key mg-key-pre">{html.escape(L.get("locator_pre", "Read before it"))}</span>'
               f'<span class="mg-key mg-key-post">{html.escape(L.get("locator_post", "Later chapters that use it"))}</span>'
               f'<span class="mg-key-note">{html.escape(L.get("locator_note", ""))}</span></p>')
        return (f'<div class="mg-locator" aria-hidden="true"><div class="mg-locator-plot" style="grid-template-columns:{template}">'
                f'<svg class="mg-map-arcs" viewBox="0 0 1000 100" preserveAspectRatio="none" focusable="false">{self.arcs(current)}</svg>'
                f'<span class="mg-dots" style="grid-template-columns:{template}">{"".join(cells)}</span></div>{key}</div>')

    def map_css(self):
        """Hover and focus on a chapter of the map light the lines that join it and the chapters at their other ends; a
        route's name lights the route's chapters. Generated, since each rule names one chapter."""
        rules = []
        edges = getattr(self, 'map_edges', [])
        for c in self.chapters:
            cid = c['id']
            near = [a for a, b in edges if b == cid] + [b for a, b in edges if a == cid]
            on = f'.mg-bookmap:has(.mg-bm-box[data-ch="{cid}"]:is(:hover,:focus-visible))'
            rules.append(f'{on} :is(.mg-bm-edge,.mg-bm-tip):not([data-from="{cid}"],[data-to="{cid}"]){{opacity:.18}}')
            rules.append(f'{on} .mg-bm-edge:is([data-from="{cid}"],[data-to="{cid}"]){{stroke:var(--accent);stroke-width:2.2}}')
            rules.append(f'{on} .mg-bm-tip:is([data-from="{cid}"],[data-to="{cid}"]){{color:var(--accent)}}')
            if near:
                sel = ','.join('[data-ch="' + x + '"]' for x in near)
                rules.append(f'{on} .mg-bm-box:is({sel}){{border-color:var(--accent)}}')
        for r in self.m.get('routes', []) or []:
            chs = ','.join(f'[data-ch="{x}"]' for x in r.get('chapter_ids', []))
            if chs:
                on = f'.mg-front:has(.mg-route-name[data-route="{r["id"]}"]:is(:hover,:focus-visible))'
                rules.append(f'{on} .mg-bm-box:not({chs}){{opacity:.28}}')
                rules.append(f'{on} :is(.mg-bm-edge,.mg-bm-tip){{opacity:.25}}')
        return '@supports selector(:has(*)){' + ''.join(rules) + '}'

    def date_html(self):
        """The book's date: the content's day alone (the reference volume's cover keeps the exact evidence boundary)."""
        from status import long_date
        day = (self.b.content or {}).get('as_of') or ''
        return f'<time datetime="{html.escape(day)}">{html.escape(long_date(day))}</time>' if day else ''

    def expanded_introduction(self):
        spec = self.m['expanded_introduction']
        text = (self.path.parent / spec['file']).read_text(encoding='utf-8')
        blocks = parse_blocks(self.definition_uses.mark('expanded-introduction', text).splitlines())
        headings = [b for b in blocks if b['t'] == 'h']
        for h in headings:
            if not h['id'] or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*', h['id']):
                raise ValueError('An introduction heading needs a stable fragment identifier.')
            self.claim(h['id'], 'front')
            self.anchor_kind[h['id']] = 'section'
        for ident in ('introduction', 'opening-question'):
            self.claim(ident, 'front')
            self.anchor_kind[ident] = 'section'
        self.address_front_passages(blocks, 'introduction')
        sections, body = [], []
        for block in blocks:
            if block['t'] == 'h':
                sections.append(self.render(body))
                body = []
                level = min(6, block['level'] + 1)
                sections.append(f'<h{level} class="mg-sec-head" id="{block["id"]}">{self.inline(block["text"])}</h{level}>')
            else:
                body.append(block)
        sections.append(self.render(body))
        items = ''.join(f'<li><a href="#{h["id"]}">{self.inline(h["text"])}</a></li>' for h in headings if h['level'] == 2)
        chapter = self.by_id.get('ch19')
        chapter_link = f'<a href="#ch19">{html.escape(chapter["title"])}</a>' if chapter else ''
        pdf = '<a href="introduction.pdf" type="application/pdf">Download PDF</a>' if spec.get('pdf') else ''
        navigation = (
                '<nav class="mg-introduction-nav" aria-label="Introduction navigation">'
                f'<a href="#opening-question">The opening question</a><a href="#contents">Book contents</a>{chapter_link}{pdf}</nav>'
                '<details class="mg-introduction-contents"><summary>Sections of the introduction</summary>'
                f'<nav aria-label="Sections of the introduction"><ol>{items}</ol></nav></details>')
        body_html = ''.join(sections)
        entry, end_paragraph, remaining = body_html.partition('</p>')
        body_html = entry + end_paragraph + navigation + remaining
        return ('<section class="mg-front-abstract mg-introduction" id="book-abstract" aria-labelledby="book-abstract-h">'
                '<h2 class="mg-introduction-title" id="book-abstract-h"><span id="introduction">Introduction</span></h2>'
                f'<div class="mg-introduction-text">{body_html}</div></section>')

    def front(self):
        m, L = self.m, self.L
        abstract = ''
        if m.get('expanded_introduction'):
            self.current = 'front'
            abstract = self.expanded_introduction()
        elif m.get('abstract'):
            self.current = 'front'
            body = self.render(parse_blocks(m['abstract'].splitlines()), envs=False)
            abstract = (f'<section class="mg-front-abstract" id="book-abstract" aria-labelledby="book-abstract-h">'
                        f'<h2 class="mg-map-h" id="book-abstract-h">Abstract</h2>{body}</section>')
        audience = f'<p class="mg-front-audience">{self.b.rich(m["audience"], terms=False)}</p>' if m.get('audience') else ''
        sub = f'<p class="mg-front-subtitle">{self.b.rich(m["subtitle"], terms=False)}</p>' if m.get('subtitle') else ''
        day = self.date_html()
        date = f" · {day}" if day else ""
        byline = f'<p class="mg-front-byline">{self.b.author_html()}{date}</p>'
        kinds = [('theorem', 'Theorem'), ('conditional', 'Conditional result'), ('conjecture', 'Conjecture'),
                 ('heuristic', 'Heuristic'), ('counterexample', 'Counterexample'), ('open', 'Open problem')]
        key = ''.join(f'<li class="mg-mark-{k}">{self.mark(KIND_MARK[k])}<span>{html.escape(L.get("kind_" + k, word))}</span></li>'
                      for k, word in kinds)
        marks = (f'<div class="mg-marks"><p class="mg-marks-h" id="mg-marks-h">{html.escape(L.get("marks", "Marks of the results"))}</p>'
                 f'<ul class="mg-marks-list" aria-labelledby="mg-marks-h">{key}</ul>'
                 f'<p class="mg-marks-note">{html.escape(L.get("marks_note", ""))}</p></div>')
        rail = (f'<aside class="mg-front-rail" aria-label="{html.escape(L.get("front_rail", "The book at a glance"))}">'
                f'{self.parts_glance()}{self.routes()}</aside>')
        return (f'<header class="mg-front" id="front" data-reader-front><div class="mg-front-frame"><div class="mg-front-main">'
                f'<div class="mg-front-title-block"><h1 class="mg-front-title">{self.b.rich(m["title"], terms=False)}</h1>'
                f'{sub}{audience}{byline}</div>{abstract}{self.introduction()}</div>{rail}</div>{self.book_map()}{marks}</header>')

    def supplement(self, sup):
        """A supplied document (an exact author handoff, used only at its recorded sha256) as a reference part of its
        own, under the reference's section head: its title as the heading, its first line as the dateline when that is a
        date, its sections unnumbered with ids from their titles, its formulae typeset as in the chapters. Every word is
        the file's. No lead-in becomes a result (envs=False), so nothing is numbered, anchored or reworded; the part takes
        no part number, so the reference's numbered parts keep theirs."""
        sid = sup['id']
        self.current = sid
        for ident in (sid, sid + '-h'):
            self.claim(ident, sid)
        self.anchor_kind[sid] = 'section'
        blocks = parse_blocks(sup['text'].splitlines())
        if blocks and blocks[0]['t'] == 'h' and blocks[0]['level'] == 1:
            blocks.pop(0)
        date = ''
        if blocks and blocks[0]['t'] == 'p':
            m = DATELINE.match(blocks[0]['text'].strip())
            if m:
                blocks.pop(0)
                iso = f'{m.group(3)}-{MONTHS.index(m.group(2)) + 1:02d}-{int(m.group(1)):02d}'
                date = f'<p class="mg-supp-date"><time datetime="{iso}">{html.escape(m.group(0))}</time></p>'
        opening, sections = self.split_sections(blocks)
        out = [self.render(opening, envs=False)] if opening else []
        for h, sblocks in sections:
            ident = self.unique(f'{sid}-{slugify(h["text"])}')
            self.claim(ident + '-h', sid)
            self.anchor_kind[ident] = 'section'
            out.append(f'<section class="mg-supp-sec" id="{ident}" aria-labelledby="{ident}-h">'
                       f'<h3 class="mg-sec-head" id="{ident}-h">{self.inline(h["text"])}</h3>'
                       f'{self.render(sblocks, envs=False)}</section>')
        kicker = f'<p class="kicker">{html.escape(sup["kicker"])}</p>' if sup.get('kicker') else ''
        return (f'<section data-reference id="{sid}" class="section mg-supplement" aria-labelledby="{sid}-h">'
                f'<header class="section-head">{kicker}<h2 id="{sid}-h"><a class="anchor" href="#{sid}">'
                f'{html.escape(sup["title"])}</a></h2>{date}</header>'
                f'<div class="mg-supp-text">{"".join(out)}</div></section>')

    def contents(self, reference):
        L = self.L
        parts = []
        for p in self.parts:
            chs = []
            for cid in p.get('chapter_ids', []):
                c = self.by_id.get(cid)
                if not c:
                    continue
                summary = f'<p class="mg-toc-summary">{self.b.rich(c["summary"], terms=False)}</p>' if c.get('summary') else ''
                pre = c.get('prerequisites', [])
                uses = (f'<p class="mg-toc-uses"><span class="mg-toc-uses-h">{html.escape(L.get("draws_on", "Draws on"))}</span> '
                        + ', '.join(f'<a href="#{q}" data-ref="chapter">{self.by_id[q]["number"]}</a>' for q in pre if q in self.by_id)
                        + '</p>') if pre else ''
                secs = self.section_index.get(cid, [])
                sec_html = ('<ol class="mg-toc-sections">' + ''.join(
                    f'<li><a href="#{sid}"><span class="mg-sec-no">{no}</span> {title}</a></li>' for sid, no, title in secs)
                    + '</ol>') if secs else ''
                state = ' data-unwritten' if cid in self.missing_chapters else ''
                chs.append(f'<li class="mg-toc-ch"{state}><a class="mg-toc-link" href="#{cid}" data-chapter-link>'
                           f'<span class="mg-toc-no">{c["number"]}</span> <span class="mg-toc-title">{html.escape(c["title"])}</span></a>'
                           f'{summary}{uses}{sec_html}</li>')
            parts.append(f'<li class="mg-toc-part" data-part="{p["id"]}"><p class="mg-toc-part-head">'
                         f'<span class="mg-toc-part-no">{html.escape(self.part_label(p))}</span> '
                         f'<span class="mg-toc-part-title" id="{p["id"]}-title">{html.escape(p["title"])}</span></p>'
                         + (f'<p class="mg-toc-part-summary">{self.b.rich(p["summary"], terms=False)}</p>' if p.get('summary') else '')
                         + f'<ol class="mg-toc-chapters">{"".join(chs)}</ol></li>')
        ref = ''
        if reference:
            links = []
            for sid, title in reference:
                local = f'<a href="#{sid}">{title}</a>'
                if sid == 'programme-overview':
                    # The slashless book mount redirects to its directory with the fragment intact.
                    # It stays a remote PDF action even when the reader prints that returned page.
                    site = html.escape(self.b.page['site'].rstrip('/'))
                    local += (f'<noscript><a class="mg-print-overview" href="{site}#programme-overview">'
                              f'{title}</a></noscript>')
                links.append(f'<li>{local}</li>')
            ref = (f'<div class="mg-toc-ref"><p class="mg-toc-part-head"><span class="mg-toc-part-title" id="reference-title">'
                   f'{html.escape(L.get("reference", "Atlas and reference"))}</span></p>'
                   f'<p class="mg-toc-ref-note">{html.escape(L.get("reference_note", ""))}</p>'
                   '<ul class="mg-toc-ref-list">' + ''.join(links) + '</ul></div>')
        return (f'<nav class="mg-toc" id="contents" data-reader-toc aria-labelledby="contents-h">'
                f'<h2 class="mg-toc-h" id="contents-h">{html.escape(L.get("contents", "Contents"))}</h2>'
                '<p class="mg-introduction-nav mg-toc-opening"><a href="#introduction">Introduction</a><a href="#opening-question">The opening question</a></p>'
                f'<ol class="mg-toc-parts">{"".join(parts)}</ol>{ref}</nav>')

    def assemble(self, reference_html, reference_index):
        """The main element's content: front, contents, chapters, then the reference sections as served by status.py."""
        self.section_index = {}
        self.pending_refs = []
        self.pending_defs = []
        self.current = 'front'
        self.load()
        # Each supplied supplement is set where status.py placed its mark, after the chapters' ids are claimed.
        reference_html = re.sub('\x04SUPPLEMENT:([^\x04]+)\x04', lambda m: self.supplement(self.supplements[m.group(1)]),
                                reference_html)
        self.reference_ids = set(re.findall(r'\sid="([^"]+)"', reference_html))
        chapters = ''.join(self.chapter(c) for c in self.chapters)
        glossary = self.glossary()
        index = self.results_index()
        if glossary:
            reference_index = [('glossary', html.escape(self.L.get('glossary', 'Glossary')))] + list(reference_index)
        if index:
            reference_index = [('results-index', html.escape(self.L.get('results_index', 'Index of results')))] + list(reference_index)
        self.current = 'front'
        front = self.front()
        toc = self.contents(reference_index)
        body = front + toc + chapters + index + glossary + reference_html
        known = set(re.findall(r'\sid="([^"]+)"', body))

        def kind_of(m):
            ident = html.unescape(m.group(1))
            return self.anchor_kind.get(ident) if self.anchor_kind.get(ident) not in (None, 'pending') else (
                'chapter' if ident in self.by_id else 'section')
        for ident, where in self.pending_refs:
            if ident not in known:
                self.problems.append(f'{where}: link to #{ident}, which the page does not have')
        body = re.sub('\x02([^\x02]*)\x02', kind_of, body)
        # A diagram node's definition link: kept when its section is on the page; otherwise the node's name stands alone
        # until the author's anchor pass gives that section its id.
        missing_defs = sorted({(t, rid) for t, _, rid, _ in self.pending_defs if t not in known})
        for t, rid in missing_defs:
            body = re.sub(r'<a href="#' + re.escape(html.escape(t)) + r'" data-ref="\x03[^\x03]*\x03">(.*?)</a>', r'\1', body)
        body = re.sub('\x03([^\x03]*)\x03', lambda m: 'section', body)
        if missing_defs:
            self.warnings.append('diagram definition links waiting for their section ids (shown as names until the '
                                 'anchor pass): ' + ', '.join(f'{rid}: {t}' for t, rid in missing_defs))
        for ident, kind in self.anchor_kind.items():
            if kind == 'figure' and ident not in known and self.figmod is not None:
                self.problems.append(f'figure {ident} is placed but not rendered')
        if self.local_links:
            by = {}
            for cid, t in self.local_links:
                by.setdefault(cid, []).append(t)
            self.warnings.append('links to working files are shown as their words only (the author\'s source keeps the '
                                 'address): ' + '; '.join(f'{cid}: {len(ts)}' for cid, ts in sorted(by.items())))
        return body


EDGE_KINDS = ('mathematical_map', 'functor', 'construction', 'open_comparison', 'reading_relation', 'equivalence')


def status_of(word):
    """The epistemic meaning of an authored status, including a structural label such as 'Corollary'."""
    w = (word or '').strip().lower()
    form = heading_form(w)
    if form and form.status:
        return form.status
    if re.match(r'^(?:proved|established|checked)\b', w):
        return 'proved'
    if re.match(r'^(?:counterexample|obstruction|refuted|scoped negative)\b', w):
        return 'refuted-form'
    if re.match(r'^open (?:problem|question|comparison)\b', w):
        return 'open'
    if re.match(r'^conjecture\b', w):
        return 'conjecture'
    if re.match(r'^conditional (?:on|upon|comparison|implication)\b', w):
        return 'conditional'
    first = w.split(' ', 1)[0]
    return QUALIFIERS.get(first) if first in ('conjectural', 'heuristic') else None


def status_mark_of(word):
    status = status_of(word)
    return KIND_MARK.get(STATUS_STYLE.get(status, status))


class Diagram:
    """One authored diagram record (manifest diagrams[], the author's PROGRAMME-DIAGRAM-CONTRACT) drawn as a figure.
    The author supplies every node, edge, label, status, hypothesis and caption; the drawing places them on a layered
    grid (layers follow the edges' direction) without adding, merging or reversing any edge.

    Node labels are page text at reading size, set over the edges, so no estimate of a formula's width is needed. Each
    edge runs between the centres of its nodes, behind them, with its arrowhead (none for an undirected comparison)
    and its number at its middle; a construction, drawn as a double line, also carries its literal label there. The
    figure's chapter and section are data-figure-chapter and data-figure-section, outside the reader's own selectors. Under the drawing, as written:
    the legend, the record's hypotheses, relations, equations and formulas, the witness, what is not asserted, and a
    numbered list of the edges (ends, words, kind, status, hypotheses) and of the nodes (with their descriptions and
    links to their definitions). The lists are also the diagram for a screen reader and on paper. Two orientations are
    served (layers left to right; top to bottom for a narrow column or a long chain); the sheet shows the one that fits."""

    CELL_W, CELL_H = 240, 124

    def __init__(self, book, rec):
        self.book, self.rec = book, rec
        self.problems = book.problems
        self.where = f'diagram {rec.get("id")}'

    def text(self, value):
        return self.book.b.rich(value, terms=False) if isinstance(value, str) else ''

    def plot_node_label(self, node):
        label = node['label']
        # Keep both excluded diagonals together in the two ordered-cut opens.
        # The list uses the complete author-supplied formula for each node.
        if self.rec['id'] == 'fig-ordered-cut-support' and node['id'] in ('cut-u12', 'cut-u21'):
            formula = INLINE_MATH.fullmatch(label)
            if formula:
                left, operator, right = formula.group(1).partition(r'\setminus')
                if operator and left and right:
                    return self.text(r'\(' + left + operator + r'\)') + '<br>' + self.text(r'\(' + right + r'\)')
        return self.text(label)

    def check(self):
        rec, ok = self.rec, True
        for key in ('title', 'caption', 'nodes', 'edges'):
            if key not in rec:
                self.problems.append(f'{self.where}: the record has no {key}')
                ok = False
        nodes = rec.get('nodes') or []
        ids = [n.get('id') for n in nodes]
        if len(set(ids)) != len(ids) or not all(ids):
            self.problems.append(f'{self.where}: node ids are missing or repeated')
            ok = False
        for n in nodes:
            if not n.get('label'):
                self.problems.append(f'{self.where}: node {n.get("id")} has no label')
                ok = False
        for e in rec.get('edges') or []:
            if e.get('source') not in ids or e.get('target') not in ids:
                self.problems.append(f'{self.where}: edge {e.get("id")} joins a node the record does not have')
                ok = False
            if e.get('kind') not in EDGE_KINDS:
                self.problems.append(f'{self.where}: edge {e.get("id")} has kind {e.get("kind")!r}, not one of {EDGE_KINDS}')
                ok = False
            if e.get('direction') not in (None, 'directed', 'undirected'):
                self.problems.append(f'{self.where}: edge {e.get("id")} has direction {e.get("direction")!r}')
                ok = False
        for h in rec.get('highlighted_node_ids') or []:
            if h not in ids:
                self.problems.append(f'{self.where}: highlighted node {h} is not a node of the record')
                ok = False
        known = {'id', 'chapter_id', 'section_id', 'type', 'title', 'caption', 'nodes', 'edges', 'context_key',
                 'highlighted_node_ids', 'legend', 'node_identity_rule', 'hypotheses', 'relations', 'equations', 'formulas',
                 'prohibitions', 'witness', 'status'}
        for key in rec:
            if key not in known:
                self.problems.append(f'{self.where}: field {key!r} is not one the reader can show (returned to the author)')
        if rec.get('chapter_id') and rec['chapter_id'] != self.book.current:
            self.problems.append(f'{self.where}: placed in {self.book.current}, but the record names {rec["chapter_id"]}')
        return ok

    def layers(self):
        nodes = [n['id'] for n in self.rec['nodes']]
        edges = [(e['source'], e['target']) for e in self.rec['edges'] if e['source'] != e['target']]
        # Break any cycle at its back edges (depth-first, in the record's node order), for placement only.
        out = {n: [t for s, t in edges if s == n] for n in nodes}
        state, back = {}, set()

        def visit(n):
            state[n] = 1
            for t in out[n]:
                if state.get(t) == 1:
                    back.add((n, t))
                elif not state.get(t):
                    visit(t)
            state[n] = 2
        for n in nodes:
            if not state.get(n):
                visit(n)
        forward = [(s, t) for s, t in edges if (s, t) not in back]
        layer = {n: 0 for n in nodes}
        for _ in range(len(nodes)):
            changed = False
            for s, t in forward:
                if layer[t] < layer[s] + 1:
                    layer[t] = layer[s] + 1
                    changed = True
            if not changed:
                break
        count = max(layer.values()) + 1 if layer else 0
        order = [[n for n in nodes if layer[n] == k] for k in range(count)]
        pos = {n: i for col in order for i, n in enumerate(col)}
        neighbours = {n: [t for s, t in forward if s == n] + [s for s, t in forward if t == n] for n in nodes}
        for _ in range(4):  # barycentre sweeps: fewer crossings, the same edges
            for col in order:
                col.sort(key=lambda n: (sum(pos[m] for m in neighbours[n]) / len(neighbours[n]) if neighbours[n] else pos[n], pos[n]))
                for i, n in enumerate(col):
                    pos[n] = i
        return order

    def label_height(self):
        """The tallest node box, estimated from its words (formulas counted by their visible symbols), so that the rows
        leave room for it: about eighteen characters to a line of the node's measure."""
        import math
        longest = 0
        for n in self.rec['nodes']:
            text = re.sub(r'\\[a-zA-Z]+|[{}^_\\()]', '', (n.get('label') or '') + ' ' + (n.get('formula') or ''))
            longest = max(longest, len(text.strip()))
        return math.ceil(longest / 18) * 21 + 14

    def geometry(self, order, vertical):
        rows = max((len(c) for c in order), default=1)
        box = self.label_height()
        W, H = (200, max(150, box + 56)) if vertical else (self.CELL_W, max(self.CELL_H, box + 40))
        width = (rows if vertical else len(order)) * W
        height = (len(order) if vertical else rows) * H
        centre = {}
        for k, col in enumerate(order):
            pad = (rows - len(col)) / 2
            for i, n in enumerate(col):
                a, b = k + .5, i + pad + .5
                centre[n] = (b * W, a * H) if vertical else (a * W, b * H)
        return width, height, centre

    def drawing(self, order, vertical):
        import math
        rec = self.rec
        width, height, centre = self.geometry(order, vertical)
        pairs = {}
        for e in rec['edges']:
            pairs.setdefault(frozenset((e['source'], e['target'])), []).append(e['id'])
        paths, badges = [], []
        for n, e in enumerate(rec['edges'], 1):
            p0, p2 = centre[e['source']], centre[e['target']]
            dx, dy = p2[0] - p0[0], p2[1] - p0[1]
            length = math.hypot(dx, dy) or 1
            ux, uy = dx / length, dy / length
            px, py = -uy, ux
            bend = 0.0
            group = pairs[frozenset((e['source'], e['target']))]
            if len(group) > 1:
                # Edges between the same two nodes bow apart, each to its own side.
                bend = (group.index(e['id']) - (len(group) - 1) / 2) * 112
                if e['source'] > e['target']:
                    bend = -bend
            if not bend:
                # An edge that would pass over another node bows out to clear it.
                for m, (cx, cy) in centre.items():
                    if m in (e['source'], e['target']):
                        continue
                    t = (cx - p0[0]) * ux + (cy - p0[1]) * uy
                    if 0 < t < length and abs((cx - p0[0]) * px + (cy - p0[1]) * py) < 40:
                        bend = 120
                        break
            c = ((p0[0] + p2[0]) / 2 + px * bend, (p0[1] + p2[1]) / 2 + py * bend)

            def at(t):
                return ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p2[0],
                        (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p2[1])

            def tangent(t):
                return math.atan2(2 * (1 - t) * (c[1] - p0[1]) + 2 * t * (p2[1] - c[1]),
                                  2 * (1 - t) * (c[0] - p0[0]) + 2 * t * (p2[0] - c[0]))
            d = (f'M{p0[0]:.1f} {p0[1]:.1f}Q{c[0]:.1f} {c[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}' if bend
                 else f'M{p0[0]:.1f} {p0[1]:.1f}L{p2[0]:.1f} {p2[1]:.1f}')
            kind = e['kind']
            head = ''
            if e.get('direction') != 'undirected':
                hx, hy = at(.6)
                ang = tangent(.6)
                size = 7.5
                tip = (hx + math.cos(ang) * size, hy + math.sin(ang) * size)
                wing = [(hx - math.cos(ang) * size + math.cos(ang + k * math.pi / 2) * size * .62,
                         hy - math.sin(ang) * size + math.sin(ang + k * math.pi / 2) * size * .62) for k in (1, -1)]
                if kind == 'functor':  # an open chevron: a functor between categories
                    head = (f'<path class="mg-dg-head is-{kind}" d="M{wing[0][0]:.1f} {wing[0][1]:.1f}L{tip[0]:.1f} {tip[1]:.1f}'
                            f'L{wing[1][0]:.1f} {wing[1][1]:.1f}"/>')
                else:
                    head = (f'<path class="mg-dg-head is-{kind}" d="M{tip[0]:.1f} {tip[1]:.1f}L{wing[0][0]:.1f} {wing[0][1]:.1f}'
                            f'L{wing[1][0]:.1f} {wing[1][1]:.1f}Z"/>')
            rail = f'<path class="mg-dg-rail" d="{d}"/>' if kind == 'construction' else ''
            paths.append(f'<path class="mg-dg-edge is-{kind}" data-edge="{html.escape(e["id"])}" d="{d}"/>{rail}{head}')
            bx, by = at(.4)
            words = f'<span class="mg-dg-badge-words">{self.text(e.get("label"))}</span>' if kind == 'construction' and e.get('label') else ''
            badges.append(f'<span class="mg-dg-badge is-{kind}" style="left:{100 * bx / width:.2f}%;top:{100 * by / height:.2f}%">'
                          f'{n}{words}</span>')
        nodes = []
        hl = set(rec.get('highlighted_node_ids') or [])
        for nd in rec['nodes']:
            x, y = centre[nd['id']]
            formula = f'<span class="mg-dg-node-formula">{self.text(nd["formula"])}</span>' if nd.get('formula') else ''
            cls = 'mg-dg-node' + (' is-highlighted' if nd['id'] in hl else '')
            nodes.append(f'<span class="{cls}" style="left:{100 * x / width:.2f}%;top:{100 * y / height:.2f}%" '
                         f'data-node="{html.escape(nd["id"])}">{self.plot_node_label(nd)}{formula}</span>')
        variant = 'is-vertical' if vertical else 'is-horizontal'
        return (f'<div class="mg-dg-plot {variant}" aria-hidden="true" style="aspect-ratio:{width} / {height};--dg-w:{width}px;'
                f'--dg-min:{round(width * .78)}px">'
                f'<svg class="mg-dg-svg" viewBox="0 0 {width} {height}" focusable="false">{"".join(paths)}</svg>'
                f'{"".join(badges)}{"".join(nodes)}</div>')

    def definition_link(self, nd):
        ref = nd.get('definition_ref')
        target = ref.get('section_id') if isinstance(ref, dict) else ref if isinstance(ref, str) else None
        if not target:
            return None
        self.book.pending_defs.append((target, self.book.current, self.rec['id'], nd['id']))
        return target

    def render(self):
        if not self.check():
            return ''
        rec, L, rid = self.rec, self.book.L, self.rec['id']
        order = self.layers()
        tall = len(order) > 5
        kind_words = {'mathematical_map': L.get('edge_map', 'Defined map'), 'functor': L.get('edge_functor', 'Functor'),
                      'construction': L.get('edge_construction', 'Construction'),
                      'open_comparison': L.get('edge_open', 'Open comparison'),
                      'reading_relation': L.get('edge_reading', 'Reading relation'),
                      'equivalence': L.get('edge_equivalence', 'Equivalence')}
        kinds = []
        for e in rec['edges']:
            if e['kind'] not in kinds:
                kinds.append(e['kind'])
        authored = {g.get('kind'): g.get('text') for g in rec.get('legend') or [] if isinstance(g, dict)}
        legend = ''.join(f'<li class="mg-dg-key is-{k}"><span class="mg-dg-sample" aria-hidden="true"></span>'
                         f'<span>{self.text(authored[k]) if authored.get(k) else html.escape(kind_words[k])}</span></li>' for k in kinds)
        for k, t in authored.items():
            if k not in kinds and t:
                legend += f'<li class="mg-dg-key"><span>{self.text(t)}</span></li>'
        blocks = []
        if rec.get('status'):
            st = rec['status']
            mark = status_mark_of(st)
            blocks.append(f'<p class="mg-dg-recstatus">{self.book.mark(mark) if mark else ""}{self.text(st)}</p>')
        if rec.get('hypotheses'):
            hyp = rec['hypotheses'] if isinstance(rec['hypotheses'], list) else [rec['hypotheses']]
            blocks.append(f'<div class="mg-dg-block"><p class="mg-dg-h">{html.escape(L.get("hypotheses", "Hypotheses"))}</p>'
                          '<ul class="mg-dg-ul">' + ''.join(f'<li>{self.text(h)}</li>' for h in hyp) + '</ul></div>')
        for key, word in (('equations', L.get('equations', 'Equations')), ('formulas', L.get('formulas', 'Formulas'))):
            if rec.get(key):
                vals = rec[key] if isinstance(rec[key], list) else [rec[key]]
                blocks.append(f'<div class="mg-dg-block"><p class="mg-dg-h">{html.escape(word)}</p>'
                              '<ul class="mg-dg-ul mg-dg-eqs">' + ''.join(f'<li>{self.text(v)}</li>' for v in vals) + '</ul></div>')
        if rec.get('relations'):
            items = []
            for r in rec['relations']:
                r = r if isinstance(r, dict) else {'text': r}
                st = r.get('status') or ''
                mark = status_mark_of(st)
                items.append(f'<li><span class="mg-dg-rel-status">{self.book.mark(mark) if mark else ""}{html.escape(st)}</span> '
                             f'{self.text(r.get("text"))}</li>')
            blocks.append(f'<div class="mg-dg-block"><p class="mg-dg-h">{html.escape(L.get("relations", "Relations"))}</p>'
                          f'<ul class="mg-dg-ul mg-dg-rels">{"".join(items)}</ul></div>')
        if rec.get('witness'):
            w = rec['witness']
            if isinstance(w, dict):
                parts = ''.join(f'<li>{self.text(w[k])}</li>' for k in ('coordinates', 'conclusion') if w.get(k))
                extra = [k for k in w if k not in ('coordinates', 'conclusion')]
                if extra:
                    self.problems.append(f'{self.where}: witness field(s) {extra} are not shown (returned to the author)')
            else:
                parts = f'<li>{self.text(w)}</li>'
            blocks.append(f'<div class="mg-dg-block"><p class="mg-dg-h">{html.escape(L.get("witness", "Witness"))}</p>'
                          f'<ul class="mg-dg-ul">{parts}</ul></div>')
        if rec.get('prohibitions'):
            pro = rec['prohibitions'] if isinstance(rec['prohibitions'], list) else [rec['prohibitions']]
            blocks.append(f'<div class="mg-dg-block mg-dg-not"><p class="mg-dg-h">{html.escape(L.get("not_asserted", "Not asserted"))}</p>'
                          '<ul class="mg-dg-ul">' + ''.join(f'<li>{self.text(x)}</li>' for x in pro) + '</ul></div>')
        label_of = {n['id']: self.text(n['label']) for n in rec['nodes']}
        edges = []
        for n, e in enumerate(rec['edges'], 1):
            st = e.get('status') or ''
            kind_label = kind_words[e['kind']]
            mark = status_mark_of(st)
            kind_and_status = f'<span class="mg-dg-kind">{html.escape(kind_label)}</span>'
            if st:
                status_classes = 'mg-dg-status'
                if st.strip().casefold() == kind_label.strip().casefold():
                    status_classes = 'mg-dg-kind mg-dg-status'
                    kind_and_status = ''
                kind_and_status += (f'<span class="{status_classes}">{self.book.mark(mark) if mark else ""}'
                                    f'{html.escape(st)}</span>')
            status_attr = f' data-edge-status="{html.escape(st)}"' if st else ''
            arrow = '—' if e.get('direction') == 'undirected' else '→'
            between = L.get('compared_with', 'compared with') if e.get('direction') == 'undirected' else L.get('to', 'to')
            hyp = e.get('hypotheses')
            hyp = hyp if isinstance(hyp, list) else [hyp] if hyp else []
            hyp_html = (f'<span class="mg-dg-hyp"><span class="mg-dg-hyp-h">{html.escape(L.get("hypotheses", "Hypotheses"))}</span> '
                        + ' '.join(self.text(h) for h in hyp) + '</span>') if hyp else ''
            edges.append(f'<li class="mg-dg-item is-{e["kind"]}" id="{html.escape(rid)}--{html.escape(e["id"])}" '
                         f'data-edge-kind="{html.escape(e["kind"])}"{status_attr}>'
                         f'<span class="mg-dg-n">{n}</span><span class="mg-dg-what">'
                         f'<span class="mg-dg-ends">{label_of[e["source"]]} <span class="mg-dg-arrow" role="img" '
                         f'aria-label="{html.escape(between)}">{arrow}</span> {label_of[e["target"]]}</span>'
                         + (f' <span class="mg-dg-label">{self.text(e["label"])}</span>' if e.get('label') else '')
                         + f' {kind_and_status}{hyp_html}</span></li>')
        nodes = []
        for nd in rec['nodes']:
            target = self.definition_link(nd)
            name = label_of[nd['id']]
            name = (f'<a href="#{html.escape(target)}" data-ref="\x03{html.escape(target)}\x03">{name}</a>' if target else name)
            desc = f'<span class="mg-dg-desc">{self.text(nd["description"])}</span>' if nd.get('description') else ''
            formula = f'<span class="mg-dg-desc">{self.text(nd["formula"])}</span>' if nd.get('formula') else ''
            status = f'<span class="mg-dg-status">{html.escape(nd["status"])}</span>' if nd.get('status') else ''
            hl = ' is-highlighted' if nd['id'] in (rec.get('highlighted_node_ids') or []) else ''
            nodes.append(f'<li class="mg-dg-nd{hl}" id="{html.escape(rid)}--{html.escape(nd["id"])}">'
                         f'<span class="mg-dg-nd-name">{name}</span>{formula}{desc}{status}</li>')
        lists = (f'<ol class="mg-dg-list" aria-label="{html.escape(L.get("edges", "Arrows of the diagram"))}">{"".join(edges)}</ol>'
                 f'<ul class="mg-dg-nodes" aria-label="{html.escape(L.get("nodes", "Objects of the diagram"))}">{"".join(nodes)}</ul>')
        if rec.get('context_key'):
            # A recurring guide: its full lists fold under the drawing (opened for print); its caption and legend stay.
            lists = (f'<details class="mg-dg-more"><summary>{html.escape(L.get("guide_more", "The questions and their links"))}</summary>'
                     f'{lists}</details>')
        # The context key is the author's identifier for the recurring guide; the drawing uses it and the page does not
        # serve it (it carries a version tag).
        attrs = ' data-context-guide' if rec.get('context_key') else ''
        return (f'<figure class="mg-diagram" id="{html.escape(rid)}" data-figure="{html.escape(rid)}" data-qh-figure="{html.escape(rid)}" '
                f'data-figure-type="'
                f'{html.escape(rec.get("type", "authored_diagram"))}" data-figure-chapter="{html.escape(rec.get("chapter_id", ""))}" '
                f'data-figure-section="{html.escape(rec.get("section_id", ""))}"{attrs}>'
                f'<p class="mg-dg-title" data-block-title>{self.text(rec["title"])}</p>'
                f'<ul class="mg-dg-legend">{legend}</ul>'
                f'<div class="mg-dg-stage k{min(len(order), 6)}{" is-tall" if tall else ""}">'
                f'{"" if tall else self.drawing(order, False)}{self.drawing(order, True)}</div>'
                f'<figcaption class="mg-dg-caption">{self.text(rec["caption"])}</figcaption>'
                f'{"".join(blocks)}{lists}</figure>')


class FigureContext:
    """What the atlas lane's figures.render receives: the page's TeX and text rendering, and the anchors of the
    chapter's tagged equations."""

    def __init__(self, book):
        self.book = book
        # The author's approved interface words for the figures (manifest figure_words), read by figures.render.
        self.words = dict(book.m.get('figure_words') or {})

    def rich(self, text, terms=False, **kw):
        return self.book.b.rich(text, terms=False)

    def equation_anchor(self, tag):
        return self.book.tags.get(tag)

    def anchor_for(self, ident):
        return ident if ident in self.book.used_ids else None

    def mark(self, status, label=None):
        return self.book.mark(status, label)
