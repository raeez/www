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
import importlib.util
import json
import re
from pathlib import Path

SCHEMA = 'qh-reader/v1'
HERE = Path(__file__).resolve().parent

# Lead-in words, longest first, and the kind of block each opens. The reader contract's result kinds are theorem,
# conditional, example, counterexample, heuristic and open; a definition is a term block; the rest are remarks.
LEAD_WORDS = {
    'conditional result': 'conditional', 'conditional theorem': 'conditional', 'conditional proposition': 'conditional',
    'open problem': 'open', 'open question': 'open', 'counterexample': 'counterexample', 'definition': 'definition',
    'definitions': 'definition', 'theorem': 'theorem', 'proposition': 'theorem', 'lemma': 'theorem',
    'corollary': 'theorem', 'conjecture': 'conjecture', 'heuristic': 'heuristic', 'example': 'example',
    'examples': 'example', 'construction': 'construction', 'remark': 'remark', 'remarks': 'remark',
    'notation': 'remark', 'convention': 'remark', 'conventions': 'remark', 'question': 'open', 'problem': 'open',
    'proof': 'proof', 'proof sketch': 'proof', 'sketch of proof': 'proof',
}
LEAD_ALT = '|'.join(sorted((re.escape(w) for w in LEAD_WORDS), key=len, reverse=True))
FIRST_WORD = re.compile(rf'^(?:{LEAD_ALT})\b', re.I)
# A named result ("Recognition theorem.", "Strict three-spectator theorem."): a short phrase ending in one of these words.
LAST_WORD = re.compile(r'\b(theorem|proposition|lemma|corollary|conjecture|counterexample|example|definition|construction)\b', re.I)
NOT_A_NAME = re.compile(r'^(?:the|this|that|these|those|a|an|it|we|our|its|which|what|how|why|here|there)\b', re.I)
RESULT_KINDS = ('theorem', 'conditional', 'conjecture', 'heuristic', 'example', 'counterexample', 'open')
# The status mark each kind of result carries: the same marks and colours as the atlas and the reference volume.
KIND_MARK = {'theorem': 'checked', 'conditional': 'conditional', 'conjecture': 'conjecture', 'heuristic': 'heuristic',
             'counterexample': 'refuted form', 'open': 'open'}
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

INLINE_MATH = re.compile(r'\\\((.+?)\\\)', re.S)
DISPLAY_IN_LINE = re.compile(r'\\\[(.+?)\\\]', re.S)
TAG_RE = re.compile(r'\\tag\*?\{([^{}]*)\}')
ID_LINE = re.compile(r'\{#([A-Za-z][\w:.-]*)\}')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
HEADING_ID = re.compile(r'^(.*?)\s*\{#([A-Za-z][\w:.-]*)\}\s*$')
LIST_RE = re.compile(r'^(\s*)([-*+]|\d{1,3}[.)])\s+(.*)$')
FIGURE_HOOK = re.compile(r':::\s*figure\s+([a-z0-9]+(?:-[a-z0-9]+)*)\s*')
FENCE_OPEN = re.compile(r'(:{3,})\s*(\S.*?)\s*')
FENCE_CLOSE = re.compile(r':{3,}')
TABLE_SEP = re.compile(r'^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)*\|?\s*$')
REF_DEF = re.compile(r'^\s{0,3}\[([^\]]+)\]:\s*<?(\S+?)>?(?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))?\s*$')
ARXIV_RE = re.compile(r'arxiv\.org/(?:abs|html|pdf)/((?:math|hep-th|math-ph|alg-geom|q-alg)/\d{7}|\d{4}\.\d{4,5})(v\d+)?', re.I)
END_MARK = re.compile(r'(?:∎|□|\\qed|\\square\\\)|\\blacksquare\\\))\s*$')


def slugify(text):
    import unicodedata
    text = unicodedata.normalize('NFKD', re.sub(r'\\\(.+?\\\)', ' ', text or ''))
    text = re.sub(r'[^\w\s-]', '', text.encode('ascii', 'ignore').decode()).strip().lower()
    return re.sub(r'[\s_-]+', '-', text)[:64].strip('-') or 'x'


# Blocks ------------------------------------------------------------------------------------------------------

def parse_div_spec(spec):
    """'{.theorem #thm-x title="..."}', 'theorem {#thm-x}' or 'transition' -> (class, attrs)."""
    cls, attrs = '', {}
    m = re.match(r'^([A-Za-z][\w-]*)?\s*(\{(.*)\})?\s*$', spec.strip())
    body = ''
    if m:
        cls = (m.group(1) or '').lower()
        body = m.group(3) or ''
    else:
        body = spec.strip('{} ')
    for part in re.finditer(r'\.([\w-]+)|#([\w:.-]+)|([\w-]+)="([^"]*)"', body):
        if part.group(1) and not cls:
            cls = part.group(1).lower()
        elif part.group(2):
            attrs['id'] = part.group(2)
        elif part.group(3):
            attrs[part.group(3)] = part.group(4)
    return cls, attrs


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
        if s.startswith('```') or s.startswith('~~~'):
            flush()
            fence, j, buf = s[:3], i + 1, []
            while j < n and not lines[j].strip().startswith(fence):
                buf.append(lines[j])
                j += 1
            blocks.append({'t': 'code', 'text': '\n'.join(buf)})
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
    """(kind, label markdown, rest) when a paragraph opens with a lead-in, else None. The label is the author's
    bold or italic run exactly as written."""
    m = re.match(r'^(\*\*|__)(?=\S)(.+?)(?<=\S)\1', text, re.S) or re.match(r'^(\*|_)(?=\S)([^*_]+?)(?<=\S)\1', text)
    if not m:
        return None
    inner, after = m.group(2), text[m.end():]
    bare = inner.strip()
    # A lead-in ends its run with a full stop or colon, or is followed by one: "**Theorem 6.3.**", "**Example**."
    punct_after = re.match(r'^\s*[.:]', after)
    if not (bare.endswith(('.', ':')) or punct_after or re.search(r'\)\s*[.:]?$', bare)):
        return None
    core = re.sub(r'[.:]+$', '', bare).strip()
    kind = None
    if FIRST_WORD.match(core):
        kind = LEAD_WORDS[FIRST_WORD.match(core).group(0).lower()]
    else:
        stem = re.sub(r'\s*\((?:[^()]|\([^()]*\))*\)\s*$', '', core).strip()
        stem = re.sub(r'\s+\d+(?:\.\d+)*[a-z]?$', '', stem)
        lw = LAST_WORD.search(stem)
        if lw and len(stem.split()) <= 9 and not NOT_A_NAME.match(stem):
            kind = LEAD_WORDS[lw.group(1).lower()]
    if not kind:
        return None
    # A qualifier in the name governs the status: "Conditional full-unit theorem." is a conditional result, never a
    # theorem's mark.
    if kind in ('theorem', 'example', 'construction') or kind == 'remark':
        if re.search(r'\bconditional\b', core, re.I):
            kind = 'conditional'
        elif re.search(r'\bconjectur', core, re.I):
            kind = 'conjecture'
        elif re.search(r'\bheuristic', core, re.I):
            kind = 'heuristic'
        elif re.search(r'\bopen (?:problem|question)\b', core, re.I):
            kind = 'open'
    if m.group(1) in ('*', '_') and kind != 'proof':
        return None
    if punct_after:
        after = after[punct_after.end():]
        inner = inner + punct_after.group(0).strip()
    return kind, inner, after.lstrip()


# The book ------------------------------------------------------------------------------------------------------

class Book:
    def __init__(self, build, manifest_path, mark, labels=None):
        self.b = build
        self.path = Path(manifest_path)
        self.mark = mark
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
        self.texts = {}
        self.blocks = {}
        self.missing_chapters = []
        self.figures_placed = []
        self.refdefs = {}      # chapter id -> {label: target}, from Markdown reference definitions (never shown)
        self.local_links = []  # (chapter id, target): links to working files, shown as their words only
        self.chapter_files = {Path(c['path']).name: c['id'] for c in self.chapters if c.get('path')}

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
            defs, kept = {}, []
            for line in text.splitlines():
                d = REF_DEF.match(line)
                if d:
                    defs[d.group(1).strip().lower()] = d.group(2)
                else:
                    kept.append(line)
            self.refdefs[c['id']] = defs
            text = '\n'.join(kept)
            self.texts[c['id']] = text
            blocks = parse_blocks(text.splitlines())
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
            trail = re.match(r'[.,;:!?)\]]+', text[pos:])
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
        An anchor or a chapter's file becomes a link in the book. A web address follows the page's rule that it makes
        no reference to another host: the citation is its words, with its arXiv number. Anything else (a working
        file) is shown as its words only, and listed for the author."""
        t = html.unescape(target).strip()
        if t.startswith('<') and t.endswith('>'):
            t = t[1:-1].strip()
        chapter_file = re.fullmatch(r'(?:\./)?([\w-]+\.md)(?:#([\w:.-]+))?', t)
        if chapter_file and chapter_file.group(1) in self.chapter_files:
            t = '#' + (chapter_file.group(2) or self.chapter_files[chapter_file.group(1)])
        if t.startswith('#'):
            ident = t[1:]
            self.pending_refs.append((ident, self.current))
            return f'<a href="#{html.escape(ident)}" data-ref="\x02{html.escape(ident)}\x02">{label}</a>'
        if re.match(r'https?://', t):
            a = ARXIV_RE.search(t)
            if a and a.group(1) not in label:
                return f'{label} (arXiv:{a.group(1)}{a.group(2) or ""})'
            return label
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

    def para(self, b, cls=''):
        classes = ' '.join(x for x in (cls, 'mg-cont' if b.get('attached') else '') if x)
        attr = f' class="{classes}"' if classes else ''
        return f'<p{attr}>{self.inline(b["text"])}</p>'

    def render(self, blocks, section_no=None):  # noqa: C901
        out = []
        i = 0
        while i < len(blocks):
            b = blocks[i]
            t = b['t']
            if t == 'p':
                lead = lead_in(b['text'])
                if lead:
                    span = [b]
                    j = i + 1
                    kind = lead[0]
                    while j < len(blocks):
                        nb = blocks[j]
                        if nb['t'] == 'math' or nb['t'] == 'list':
                            span.append(nb)
                            j += 1
                            continue
                        if nb['t'] == 'p' and not lead_in(nb['text']) and (
                                nb.get('attached') or re.match(r'^[a-z(,;]', nb['text'])):
                            span.append(nb)
                            j += 1
                            continue
                        break
                    if kind == 'proof' and not END_MARK.search(span[-1].get('text', '') if span[-1]['t'] == 'p' else ''):
                        # A proof runs to its end mark when one follows before the next heading or lead-in.
                        k = j
                        while k < len(blocks) and blocks[k]['t'] in ('p', 'math', 'list') and not (
                                blocks[k]['t'] == 'p' and lead_in(blocks[k]['text'])):
                            if blocks[k]['t'] == 'p' and END_MARK.search(blocks[k]['text']):
                                span.extend(blocks[j:k + 1])
                                j = k + 1
                                break
                            k += 1
                    out.append(self.environment(lead, span))
                    i = j
                    continue
                out.append(self.para(b))
            elif t == 'math':
                out.append(self.display(b))
            elif t == 'h':
                level = min(6, b['level'] + 1)
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
                    if len(item) == 1 and item[0]['t'] == 'p':
                        items.append(f'<li>{self.inline(item[0]["text"])}</li>')
                    else:
                        items.append('<li>' + self.render(item) + '</li>')
                out.append(f'<{tag} class="mg-list"{start}>{"".join(items)}</{tag}>')
            elif t == 'quote':
                out.append(f'<blockquote class="mg-quote">{self.render(b["blocks"])}</blockquote>')
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
            elif t == 'div':
                out.append(self.div(b))
            i += 1
        return ''.join(out)

    def align(self, b, k):
        a = b['align'][k] if k < len(b['align']) else ''
        return f' style="text-align:{a}"' if a else ''

    def environment(self, lead, span, attrs=None):
        kind, label_md, rest = lead
        attrs = attrs or {}
        label = self.inline(label_md)
        label_text = re.sub(r'\s+', ' ', re.sub(r'\*|_', '', label_md)).strip().rstrip('.:')
        ident = attrs.get('id')
        if ident:
            self.claim(ident, self.current)
        else:
            ident = self.unique(f'{self.current}-{slugify(label_text)}')
        first = dict(span[0], text=rest)
        body_blocks = ([first] if rest.strip() else []) + span[1:]
        inner = self.render(body_blocks)
        mark_status = KIND_MARK.get(kind)
        mark_svg = self.mark(mark_status) if mark_status else ''
        head = (f'<span class="mg-env-label" id="{ident}-h" data-block-title>{mark_svg}'
                f'<span class="mg-env-name">{label}</span></span>')
        # The label runs into the first paragraph, as in a printed book; a statement that opens with a display or a
        # list has its label on a line of its own.
        if inner.startswith('<p>') or inner.startswith('<p class="mg-cont">'):
            inner = re.sub(r'^<p( class="mg-cont")?>', '<p>' + head + ' ', inner, count=1)
        else:
            inner = f'<p class="mg-env-alone">{head}</p>' + inner
        if kind == 'proof':
            if not END_MARK.search(re.sub(r'<[^>]+>', '', inner[-200:])):
                inner = re.sub(r'(</p>)$', '<span class="mg-qed" aria-hidden="true">∎</span>\\1', inner) \
                    if inner.endswith('</p>') else inner + '<p class="mg-qed-line"><span class="mg-qed" aria-hidden="true">∎</span></p>'
            self.anchor_kind[ident] = 'result'
            return f'<div class="mg-proof" id="{ident}" role="group" aria-labelledby="{ident}-h">{inner}</div>'
        if kind == 'definition':
            self.anchor_kind[ident] = 'definition'
            return (f'<div class="mg-env mg-env-definition" id="{ident}" data-term role="group" '
                    f'aria-labelledby="{ident}-h">{inner}</div>')
        if kind in RESULT_KINDS:
            self.anchor_kind[ident] = 'result'
            return (f'<div class="mg-env mg-env-{kind}" id="{ident}" data-result data-kind="{kind}" role="group" '
                    f'aria-labelledby="{ident}-h">{inner}</div>')
        self.anchor_kind[ident] = 'result'
        return f'<div class="mg-env mg-env-{kind}" id="{ident}" role="group" aria-labelledby="{ident}-h">{inner}</div>'

    def div(self, b):
        cls, attrs = b['cls'], b['attrs']
        if not b.get('closed', True):
            self.problems.append(f'{self.current}: a ::: block ({cls or "unnamed"}) is never closed')
        if cls == 'transition':
            return f'<div class="mg-transition">{self.render(b["blocks"])}</div>'
        word = cls.replace('-', ' ')
        if word in LEAD_WORDS:
            kind = LEAD_WORDS[word]
            title = attrs.get('title')
            number = attrs.get('n')
            name = self.L.get('kind_' + kind) or word.capitalize()
            label = name + (f' {number}' if number else '') + (f' ({title})' if title else '') + '.'
            blocks = b['blocks']
            if blocks and blocks[0]['t'] == 'p':
                return self.environment((kind, label, blocks[0]['text']), blocks, attrs)
            return self.environment((kind, label, ''), [{'t': 'p', 'text': ''}] + blocks, attrs)
        self.problems.append(f'{self.current}: unknown ::: block "{cls}"')
        return self.render(b['blocks'])

    def figure(self, fid):
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
                f'<h2 class="mg-ch-title" id="{cid}-h"><span class="mg-ch-no">{number}</span>'
                f'<span class="mg-ch-name">{html.escape(c["title"])}</span></h2></header>')
        prereq_items = ''.join(
            f'<li><a href="#{q}" data-ref="chapter"><span class="mg-pre-no">{self.by_id[q]["number"]}</span>'
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
                toc_items.append(f'<li><a href="#{sid}" data-ref="section"><span class="mg-sec-no">{no}</span>'
                                 f'<span class="mg-sec-title">{title}</span></a></li>')
                self.section_index.setdefault(cid, []).append((sid, no, title))
                body_parts.append(f'<section class="mg-sec" id="{sid}" data-section aria-labelledby="{sid}-h">'
                                  f'<h3 class="mg-sec-head" id="{sid}-h"><span class="mg-sec-no">{no}</span>'
                                  f'<span class="mg-sec-title">{title}</span></h3>{self.render(sblocks)}</section>')
            body = ''.join(body_parts)
            sections_toc = (f'<div class="mg-aside-block mg-aside-toc"><p class="mg-aside-h">{html.escape(L.get("in_chapter", "In this chapter"))}</p>'
                            f'<ol class="mg-ch-toc">{"".join(toc_items)}</ol></div>') if toc_items else ''
        aside = (f'<aside class="mg-ch-aside" aria-label="{html.escape(L.get("aside", "This chapter in the book"))}">'
                 f'<div class="mg-aside-block mg-aside-map">{self.locator(cid)}</div>{prereq}{terms}{sections_toc}</aside>')
        end = self.chapter_end(c)
        return (f'<article class="mg-chapter" id="{cid}" data-chapter data-part="{p["id"] if p else ""}" data-number="{number}" '
                f'aria-labelledby="{cid}-h">{head}<div class="mg-ch-frame">{self.opening_html}{aside}<div class="mg-ch-text">{body}</div></div>'
                f'{end}</article>')

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
                         f'<span class="mg-end-no">{q["number"]}</span><span class="mg-end-title">{html.escape(q["title"])}</span></span></a>')
        if k + 1 < len(self.order):
            q = self.by_id[self.order[k + 1]]
            summary = f'<span class="mg-end-summary">{self.b.rich(q["summary"], terms=False)}</span>' if q.get('summary') else ''
            links.append(f'<a class="mg-end-next" rel="next" href="#{q["id"]}"><span class="mg-end-dir">'
                         f'{html.escape(L.get("next", "Next"))}</span><span class="mg-end-ch">'
                         f'<span class="mg-end-no">{q["number"]}</span><span class="mg-end-title">{html.escape(q["title"])}</span></span>'
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
                        cls += ' is-quiet'
                paths.append(f'<path class="{cls}" data-from="{q}" data-to="{c["id"]}" '
                             f'd="M{x1:.1f} 100C{x1:.1f} {ctrl:.1f} {x2:.1f} {ctrl:.1f} {x2:.1f} 100"/>')
        return ''.join(paths)

    def book_map(self):
        cols, template, centre, colno = self.columns()
        L = self.L
        nodes = []
        for c in self.chapters:
            if c['id'] not in colno:
                continue
            p = self.part_of.get(c['id'])
            nodes.append(f'<li class="mg-node-cell" style="grid-column:{colno[c["id"]]}">'
                         f'<a class="mg-node" href="#{c["id"]}" data-ch="{c["id"]}" data-part="{p["id"] if p else ""}" '
                         f'title="{html.escape(str(c["number"]) + " · " + c["title"])}">'
                         f'<span class="mg-node-no" aria-hidden="true">{c["number"]}</span>'
                         f'<span class="visually-hidden">{html.escape(self.chapter_label(c) + ": " + c["title"])}</span></a></li>')
        parts = []
        for p in self.parts:
            ids = [cid for cid in p.get('chapter_ids', []) if cid in colno]
            if not ids:
                continue
            parts.append(f'<li class="mg-band" style="grid-column:{colno[ids[0]]} / {colno[ids[-1]] + 1}">'
                         f'<a href="#{p["id"]}-title"><span class="mg-band-no">{ROMAN[self.part_no[p["id"]] - 1]}</span>'
                         f'<span class="mg-band-title">{html.escape(p["title"])}</span></a></li>')
        routes = []
        for r in self.m.get('routes', []) or []:
            chs = [cid for cid in r.get('chapter_ids', []) if cid in colno]
            unknown = [cid for cid in r.get('chapter_ids', []) if cid not in colno]
            if unknown:
                self.problems.append(f'reader manifest: route {r.get("id")} names unknown chapters {unknown}')
            cells = ''.join(f'<span class="mg-route-cell" style="grid-column:{colno[cid]}" data-ch="{cid}"></span>' for cid in chs)
            nums = ', '.join(str(self.by_id[cid]['number']) for cid in chs)
            routes.append(f'<li class="mg-route" data-route-row="{html.escape(r["id"])}">'
                          f'<a class="mg-route-name" href="#{chs[0] if chs else "contents"}" data-route="{html.escape(r["id"])}" '
                          f'data-route-chapters="{" ".join(chs)}">{html.escape(r["title"])}</a>'
                          f'<span class="mg-route-list">{html.escape(L.get("route_chapters", "Chapters {list}").replace("{list}", nums))}</span>'
                          f'<span class="mg-route-cells" aria-hidden="true" style="grid-template-columns:{template}">{cells}</span></li>')
        routes_html = ''
        if routes:
            routes_html = (f'<div class="mg-routes"><p class="mg-routes-h" id="mg-routes-h">{html.escape(L.get("routes", "Routes through the book"))}</p>'
                           f'<ol class="mg-route-list-all" aria-labelledby="mg-routes-h">{"".join(routes)}</ol></div>')
        return (f'<figure class="mg-map" aria-labelledby="mg-map-h mg-map-cap">'
                f'<p class="mg-map-h" id="mg-map-h">{html.escape(L.get("map_title", "The chapters and their reading prerequisites"))}</p>'
                f'<div class="mg-map-plot" style="grid-template-columns:{template}">'
                f'<svg class="mg-map-arcs" viewBox="0 0 1000 100" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
                f'{self.arcs()}</svg>'
                f'<ol class="mg-nodes" style="grid-template-columns:{template}">{"".join(nodes)}</ol>'
                f'<ol class="mg-bands" style="grid-template-columns:{template}">{"".join(parts)}</ol></div>'
                f'{routes_html}'
                f'<figcaption class="mg-map-cap" id="mg-map-cap">{html.escape(L.get("map_caption", ""))}</figcaption></figure>')

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
        """Hover and focus on a chapter of the map light its arcs and the chapters they join; a route's name lights the
        route. Generated, since each rule names one chapter."""
        rules = []
        for c in self.chapters:
            cid = c['id']
            near = c.get('prerequisites', []) + [d['id'] for d in self.chapters if cid in d.get('prerequisites', [])]
            sel_near = ','.join(f'[data-ch="{x}"]' for x in near) or '[data-ch="none"]'
            on = f'.mg-map:has(.mg-node[data-ch="{cid}"]:is(:hover,:focus-visible))'
            rules.append(f'{on} .mg-arc:is([data-from="{cid}"],[data-to="{cid}"]){{stroke:var(--accent);stroke-opacity:1;stroke-width:1.8}}')
            rules.append(f'{on} .mg-node:is({sel_near}){{border-color:var(--accent);color:var(--ink)}}')
        for r in self.m.get('routes', []) or []:
            chs = ','.join(f'[data-ch="{x}"]' for x in r.get('chapter_ids', []))
            if chs:
                on = f'.mg-map:has(.mg-route-name[data-route="{r["id"]}"]:is(:hover,:focus-visible))'
                rules.append(f'{on} .mg-node:not({chs}){{opacity:.3}}')
        return '@supports selector(:has(*)){' + ''.join(rules) + '}'

    def front(self):
        m, L = self.m, self.L
        audience = f'<p class="mg-front-audience">{self.b.rich(m["audience"], terms=False)}</p>' if m.get('audience') else ''
        sub = f'<p class="mg-front-subtitle">{self.b.rich(m["subtitle"], terms=False)}</p>' if m.get('subtitle') else ''
        byline = f'<p class="mg-front-byline">{html.escape(self.b.page["author"])} · {self.b.as_of_html(self.b.content)}</p>'
        kinds = [('theorem', 'Theorem'), ('conditional', 'Conditional result'), ('conjecture', 'Conjecture'),
                 ('heuristic', 'Heuristic'), ('counterexample', 'Counterexample'), ('open', 'Open problem')]
        key = ''.join(f'<li class="mg-mark-{k}">{self.mark(KIND_MARK[k])}<span>{html.escape(L.get("kind_" + k, word))}</span></li>'
                      for k, word in kinds)
        marks = (f'<div class="mg-marks"><p class="mg-marks-h" id="mg-marks-h">{html.escape(L.get("marks", "Marks of the results"))}</p>'
                 f'<ul class="mg-marks-list" aria-labelledby="mg-marks-h">{key}</ul>'
                 f'<p class="mg-marks-note">{html.escape(L.get("marks_note", ""))}</p></div>')
        return (f'<header class="mg-front" id="front" data-reader-front>'
                f'<div class="mg-front-title-block"><h1 class="mg-front-title">{self.b.rich(m["title"], terms=False)}</h1>'
                f'{sub}{audience}{byline}</div>{self.book_map()}{marks}</header>')

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
                           f'<span class="mg-toc-no">{c["number"]}</span><span class="mg-toc-title">{html.escape(c["title"])}</span></a>'
                           f'{summary}{uses}{sec_html}</li>')
            parts.append(f'<li class="mg-toc-part" data-part="{p["id"]}"><p class="mg-toc-part-head">'
                         f'<span class="mg-toc-part-no">{html.escape(self.part_label(p))}</span> '
                         f'<span class="mg-toc-part-title" id="{p["id"]}-title">{html.escape(p["title"])}</span></p>'
                         + (f'<p class="mg-toc-part-summary">{self.b.rich(p["summary"], terms=False)}</p>' if p.get('summary') else '')
                         + f'<ol class="mg-toc-chapters">{"".join(chs)}</ol></li>')
        ref = ''
        if reference:
            ref = (f'<div class="mg-toc-ref"><p class="mg-toc-part-head"><span class="mg-toc-part-title" id="reference-title">'
                   f'{html.escape(L.get("reference", "Atlas and reference"))}</span></p>'
                   f'<p class="mg-toc-ref-note">{html.escape(L.get("reference_note", ""))}</p>'
                   '<ul class="mg-toc-ref-list">' + ''.join(
                       f'<li><a href="#{sid}">{title}</a></li>' for sid, title in reference) + '</ul></div>')
        return (f'<nav class="mg-toc" id="contents" data-reader-toc aria-labelledby="contents-h">'
                f'<h2 class="mg-toc-h" id="contents-h">{html.escape(L.get("contents", "Contents"))}</h2>'
                f'<ol class="mg-toc-parts">{"".join(parts)}</ol>{ref}</nav>')

    def assemble(self, reference_html, reference_index):
        """The main element's content: front, contents, chapters, then the reference sections as served by status.py."""
        self.section_index = {}
        self.pending_refs = []
        self.current = 'front'
        self.load()
        chapters = ''.join(self.chapter(c) for c in self.chapters)
        self.current = 'front'
        front = self.front()
        toc = self.contents(reference_index)
        body = front + toc + chapters + reference_html
        known = set(re.findall(r'\sid="([^"]+)"', body))

        def kind_of(m):
            ident = html.unescape(m.group(1))
            return self.anchor_kind.get(ident) if self.anchor_kind.get(ident) not in (None, 'pending') else (
                'chapter' if ident in self.by_id else 'section')
        for ident, where in self.pending_refs:
            if ident not in known:
                self.problems.append(f'{where}: link to #{ident}, which the page does not have')
        body = re.sub('\x02([^\x02]*)\x02', kind_of, body)
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


EDGE_KINDS = ('mathematical_map', 'equivalence', 'open_comparison', 'reading_relation')
# The status mark an edge carries, by its authored status word; an edge with no status carries none.
EDGE_STATUS_MARK = {'theorem': 'checked', 'established': 'checked', 'proved': 'checked', 'checked': 'checked',
                    'conditional': 'conditional', 'conjecture': 'conjecture', 'heuristic': 'heuristic',
                    'open': 'open', 'open problem': 'open', 'counterexample': 'refuted form', 'obstruction': 'refuted form',
                    'refuted form': 'refuted form'}


class Diagram:
    """One authored diagram record drawn as a figure. The author supplies every node, edge and word; the drawing places
    them on a layered grid (layers follow the edges' direction) without adding, merging or reversing any edge.

    Node labels are page text at reading size, set over the edges, so that no estimate of a formula's width is needed;
    each edge runs between the centres of its two nodes, behind them, and carries its arrowhead and its number at its
    midpoint. The numbered list under the drawing gives each edge's source, target, words, status and hypotheses as
    written: it is also the diagram for a screen reader and on paper. Two orientations are served (layers left to
    right, and top to bottom for a narrow column); the sheet shows the one that fits."""

    CELL_W, CELL_H = 240, 124

    def __init__(self, book, rec):
        self.book, self.rec = book, rec
        self.problems = book.problems
        self.where = f'diagram {rec.get("id")}'

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
            st = (e.get('status') or '').strip().lower()
            if st and st not in EDGE_STATUS_MARK:
                self.problems.append(f'{self.where}: edge {e.get("id")} has status {e.get("status")!r}, which has no mark')
                ok = False
        for h in rec.get('highlighted_node_ids') or []:
            if h not in ids:
                self.problems.append(f'{self.where}: highlighted node {h} is not a node of the record')
                ok = False
        if rec.get('chapter_id') and rec['chapter_id'] != self.book.current:
            self.problems.append(f'{self.where}: placed in {self.book.current}, but the record names {rec["chapter_id"]}')
        return ok

    def layers(self):
        nodes = [n['id'] for n in self.rec['nodes']]
        edges = [(e['source'], e['target']) for e in self.rec['edges'] if e['source'] != e['target']]
        # Break any cycle at its back edges (depth-first, in the record's node order) for placement only.
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
        for _ in range(4):  # barycentre sweeps: fewer crossings, same edges
            for col in order:
                col.sort(key=lambda n: (sum(pos[m] for m in neighbours[n]) / len(neighbours[n]) if neighbours[n] else pos[n], pos[n]))
                for i, n in enumerate(col):
                    pos[n] = i
        return order

    def geometry(self, order, vertical):
        rows = max((len(c) for c in order), default=1)
        cols = len(order)
        W, H = self.CELL_W, self.CELL_H
        if vertical:
            W, H = 200, 150
        width = (rows if vertical else cols) * W
        height = (cols if vertical else rows) * H
        centre = {}
        for k, col in enumerate(order):
            pad = (rows - len(col)) / 2
            for i, n in enumerate(col):
                a = (k + .5)
                b = (i + pad + .5)
                x, y = (b * W, a * H) if vertical else (a * W, b * H)
                centre[n] = (x, y)
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
            hx, hy = at(.6)
            ang = tangent(.6)
            size = 7.5
            tip = (hx + math.cos(ang) * size, hy + math.sin(ang) * size)
            wing = [(hx - math.cos(ang) * size + math.cos(ang + k * math.pi / 2) * size * .62,
                     hy - math.sin(ang) * size + math.sin(ang + k * math.pi / 2) * size * .62) for k in (1, -1)]
            head = f'M{tip[0]:.1f} {tip[1]:.1f}L{wing[0][0]:.1f} {wing[0][1]:.1f}L{wing[1][0]:.1f} {wing[1][1]:.1f}Z'
            kind = e['kind']
            paths.append(f'<path class="mg-dg-edge is-{kind}" data-edge="{html.escape(e["id"])}" d="{d}"/>'
                         f'<path class="mg-dg-head is-{kind}" d="{head}"/>')
            bx, by = at(.4)
            badges.append(f'<span class="mg-dg-badge is-{kind}" style="left:{100 * bx / width:.2f}%;top:{100 * by / height:.2f}%">{n}</span>')
        nodes = []
        hl = set(rec.get('highlighted_node_ids') or [])
        for nd in rec['nodes']:
            x, y = centre[nd['id']]
            label = self.book.b.rich(nd['label'], terms=False)
            cls = 'mg-dg-node' + (' is-highlighted' if nd['id'] in hl else '')
            style = f'left:{100 * x / width:.2f}%;top:{100 * y / height:.2f}%'
            ref = nd.get('definition_ref')
            if ref:
                self.book.pending_refs.append((ref, self.book.current))
                nodes.append(f'<a class="{cls}" style="{style}" href="#{html.escape(ref)}" data-ref="\x02{html.escape(ref)}\x02" '
                             f'data-node="{html.escape(nd["id"])}">{label}</a>')
            else:
                nodes.append(f'<span class="{cls}" style="{style}" data-node="{html.escape(nd["id"])}">{label}</span>')
        variant = 'is-vertical' if vertical else 'is-horizontal'
        return (f'<div class="mg-dg-plot {variant}" aria-hidden="true" style="aspect-ratio:{width} / {height};--dg-w:{width}px">'
                f'<svg class="mg-dg-svg" viewBox="0 0 {width} {height}" focusable="false">{"".join(paths)}</svg>'
                f'{"".join(badges)}{"".join(nodes)}</div>')

    def render(self):
        if not self.check():
            return ''
        rec = self.rec
        L = self.book.L
        order = self.layers()
        node_label = {n['id']: self.book.b.rich(n['label'], terms=False) for n in rec['nodes']}
        words = {'mathematical_map': L.get('edge_map', 'map'), 'equivalence': L.get('edge_equivalence', 'equivalence'),
                 'open_comparison': L.get('edge_open', 'Open problem'),
                 'reading_relation': L.get('edge_reading', 'reading relation (navigation, not a mathematical map)')}
        items = []
        for n, e in enumerate(rec['edges'], 1):
            st = (e.get('status') or '').strip()
            mark = self.book.mark(EDGE_STATUS_MARK[st.lower()]) if st else ''
            status = f' <span class="mg-dg-status">{mark}{html.escape(st)}</span>' if st else ''
            label = f' <span class="mg-dg-label">{self.book.b.rich(e["label"], terms=False)}</span>' if e.get('label') else ''
            hyp = e.get('hypotheses')
            if isinstance(hyp, list):
                hyp = '; '.join(hyp)
            hyp_html = (f'<span class="mg-dg-hyp"><span class="mg-dg-hyp-h">{html.escape(L.get("hypotheses", "Hypotheses"))}</span> '
                        f'{self.book.b.rich(hyp, terms=False)}</span>') if hyp else ''
            items.append(f'<li class="mg-dg-item is-{e["kind"]}" data-edge="{html.escape(e["id"])}"><span class="mg-dg-n">{n}</span>'
                         f'<span class="mg-dg-what"><span class="mg-dg-ends">{node_label[e["source"]]} '
                         f'<span class="mg-dg-arrow" aria-label="{html.escape(L.get("to", "to"))}">→</span> {node_label[e["target"]]}</span>'
                         f'{label} <span class="mg-dg-kind">{html.escape(words[e["kind"]])}</span>{status}{hyp_html}</span></li>')
        rid = rec['id']
        head = f'<p class="mg-dg-title" data-block-title>{self.book.b.rich(rec["title"], terms=False)}</p>'
        return (f'<figure class="mg-diagram" id="{html.escape(rid)}" data-figure="{html.escape(rid)}" data-figure-type="diagram" '
                f'data-chapter="{html.escape(rec.get("chapter_id", ""))}" data-section="{html.escape(rec.get("section_id", ""))}">'
                f'{head}<div class="mg-dg-stage{" is-tall" if len(order) > 5 else ""}">{self.drawing(order, False) if len(order) <= 5 else ""}{self.drawing(order, True)}</div>'
                f'<ol class="mg-dg-list">{"".join(items)}</ol>'
                f'<figcaption class="mg-dg-caption">{self.book.b.rich(rec["caption"], terms=False)}</figcaption></figure>')


class FigureContext:
    """What the atlas lane's figures.render receives: the page's TeX and text rendering, and the anchors of the
    chapter's tagged equations."""

    def __init__(self, book):
        self.book = book

    def rich(self, text, terms=False, **kw):
        return self.book.b.rich(text, terms=False)

    def equation_anchor(self, tag):
        return self.book.tags.get(tag)

    def anchor_for(self, ident):
        return ident if ident in self.book.used_ids else None

    def mark(self, status, label=None):
        return self.book.mark(status, label)
