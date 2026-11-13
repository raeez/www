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
import html
import io
import json
import re
import subprocess
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEX2MATHML = HERE.parent / 'quantum-holography-tracker' / 'tex2mathml.cjs'

STATEMENT_STATUSES = ['checked', 'pending', 'conditional', 'conjecture', 'heuristic', 'open', 'published']
CELL_STATUSES = ['checked', 'partial', 'pending', 'published', 'open', 'not posed', 'refuted form']
COLUMNS = ['object', 'dual', 'modules', 'fusion', 'bulk', 'lines', 'states', 'dictionary']

# Each status has its own shape as well as its own colour, so that the marks read in
# monochrome, in print and for readers who do not separate the colours.
MARKS = {
    'checked': '<circle cx="8" cy="8" r="5.6" fill="currentColor"/>',
    'pending': '<circle cx="8" cy="8" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/>'
               '<path d="M8 3a5 5 0 0 1 0 10z" fill="currentColor"/>',
    'partial': '<circle cx="8" cy="8" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/>'
               '<path d="M8 8V3a5 5 0 0 1 5 5z" fill="currentColor"/>',
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

    def add(self, tex, display):
        self.jobs.append({'tex': tex, 'display': display})
        return f'\x00M{len(self.jobs) - 1}\x00'

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

    def substitute(self, markup):
        def one(m):
            i = int(m.group(1))
            row = self.out[i]
            if 'html' in row:
                return row['html']
            return f'<code class="tex-error">{html.escape(self.jobs[i]["tex"])}</code>'
        return re.sub(r'\x00M(\d+)\x00', one, markup)


MATH_RE = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]', re.S)
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
        for entry in glossary:
            tid = 'term-' + ident(entry['term'])
            base = tid
            n = 2
            while any(e['id'] == tid for e in self.entries):
                tid = f'{base}-{n}'
                n += 1
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
            return (f'<button type="button" class="term" data-term="{tid}" aria-describedby="card" '
                    f'aria-controls="{tid}">{m.group(1)}</button>')
        return self.regex.sub(one, escaped_text)


class Build:
    def __init__(self, folder, page, text_fonts=None, math_font=None):
        self.folder = Path(folder)
        self.page = page
        self.text_fonts = text_fonts or {}
        self.math_font = math_font
        self.math = Math()
        self.problems = []
        self.warnings = []
        self.anchors = set()
        self.links = []

    # Text -------------------------------------------------------------------------------

    def rich(self, text, seen=None, terms=True):
        """Plain text with TeX and *emphasis* to HTML; glossary terms attached once per block."""
        if text is None:
            return ''
        text = unlink(text)
        seen = set() if seen is None else seen
        parts = []
        pos = 0
        for m in MATH_RE.finditer(text):
            parts.append(self.plain(text[pos:m.start()], seen, terms))
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
        parts.append(self.plain(text[pos:], seen, terms))
        return ''.join(parts)

    def plain(self, text, seen, terms):
        if '\\(' in text or '\\)' in text or '\\[' in text or '\\]' in text:
            self.problems.append('unbalanced TeX delimiters in: ' + text[:120])
        escaped = html.escape(text, quote=False)
        escaped = EMPH_RE.sub(r'<em>\1</em>', escaped)
        if terms:
            escaped = self.term_links.link(escaped, seen)
        return escaped

    # Pieces -----------------------------------------------------------------------------

    def status_label(self, status):
        return self.page['status_labels'][status]

    def statement_id(self, s):
        sid = (s.get('id') or '').strip()
        return 's-' + ident(sid) if sid else ''

    def statement(self, s, where, heading='h4', title_override=None, chip=True):
        status = s.get('status')
        if status not in STATEMENT_STATUSES:
            self.problems.append(f'{where}: unknown statement status {status!r}')
            status = 'open'
        seen = set()
        label = self.status_label(status)
        title = (s.get('title') or '') if title_override is None else title_override
        sid = self.statement_id(s)
        if sid:
            self.anchors.add(sid)
        id_attr = f' id="{sid}"' if sid else ''
        added = ' added' if s.get('added') else ''
        out = [f'<article class="statement st-{slug(status)}{added}" data-status="{status}"{id_attr}>']
        out.append('<div class="statement-head">')
        out.append(f'<span class="status-chip chip-{slug(status)}">{mark(status)}<span>{html.escape(label)}</span></span>')
        if s.get('added') and chip:
            out.append(f'<span class="added-chip">{html.escape(self.page["labels"]["added"])}</span>')
        if title:
            out.append(f'<{heading} class="statement-title">{self.rich(title, seen, terms=False)}</{heading}>')
        out.append('</div>')
        out.append(f'<div class="statement-text">{self.paragraphs(s.get("text", ""), seen)}</div>')
        notes = []
        novelty = (s.get('novelty') or '').strip()
        antecedents = (s.get('antecedents') or '').strip()
        cite = (s.get('cite') or '').strip()
        if status in ('checked', 'pending') and novelty:
            notes.append(f'<span class="note-novelty">{html.escape(self.page["novelty_labels"].get(novelty, novelty))}</span>')
        if antecedents:
            notes.append(f'<span class="note-label">{html.escape(self.page["labels"]["antecedents"])}</span> '
                         f'{self.rich(antecedents, seen, terms=False)}')
        if cite:
            notes.append(f'<span class="note-label">{html.escape(self.page["labels"]["cite"])}</span> '
                         f'{self.rich(cite, seen, terms=False)}')
        if notes:
            out.append('<p class="statement-notes">' + ' <span class="sep" aria-hidden="true">·</span> '.join(notes) + '</p>')
        out.append('</article>')
        if not (s.get('text') or '').strip():
            self.problems.append(f'{where}: empty statement text')
        return ''.join(out)

    def paragraphs(self, text, seen=None):
        blocks = [b.strip() for b in re.split(r'\n\s*\n', text or '') if b.strip()]
        if len(blocks) <= 1:
            return f'<p>{self.rich(text.strip() if text else "", seen)}</p>'
        return ''.join(f'<p>{self.rich(b, seen)}</p>' for b in blocks)

    def section(self, sid, title, body, cls='', kicker=None, added=False):
        self.anchors.add(sid)
        k = f'<p class="kicker">{html.escape(kicker)}</p>' if kicker else ''
        chip = (f'<p class="section-added"><span class="added-chip">{html.escape(self.page["labels"]["added_section"])}'
                f'</span></p>') if added else ''
        return (f'<section id="{sid}" class="section {cls}" aria-labelledby="{sid}-h">'
                f'<header class="section-head">{k}<h2 id="{sid}-h"><a class="anchor" href="#{sid}">'
                f'{html.escape(title)}</a></h2>{chip}</header>{body}</section>')

    # Sections ---------------------------------------------------------------------------

    def cover(self, c):
        L = self.page['labels']
        lead = ''.join(f'<p>{self.rich(p)}</p>' for p in c.get('lead', []))
        counts = self.counts(c)
        stats = ''.join(
            f'<li><a href="#examples" data-filter="{st}">{mark(st)}<span class="count">{n}</span>'
            f'<span class="count-label">{html.escape(self.status_label(st))}</span></a></li>'
            for st, n in counts if n)
        self.anchors.add('programme')
        return (f'<header class="cover" id="programme">'
                f'<p class="kicker">{html.escape(L["kicker"])}</p>'
                f'<h1>{self.rich(c["title"], terms=False)}</h1>'
                f'<p class="subtitle">{self.rich(c.get("subtitle", ""), terms=False)}</p>'
                f'<p class="as-of">{html.escape(L["as_of"])} <time datetime="{html.escape(c["as_of"])}">'
                f'{html.escape(long_date(c["as_of"]))}</time>'
                + (f'<span class="sep" aria-hidden="true"> · </span><a href="#changes">{html.escape(L["changes_link"])}</a>'
                   if (c.get('changes') or {}).get('items') else '') +
                '</p>'
                f'</header>'
                f'<div class="lead prose">{lead}</div>'
                f'<nav class="tally" aria-label="{html.escape(L["tally"])}"><p class="tally-label">'
                f'{html.escape(L["tally"])}</p><ul>{stats}</ul></nav>')

    def counts(self, c):
        tally = {s: 0 for s in STATEMENT_STATUSES}
        for s in self.all_statements(c):
            if s.get('status') in tally:
                tally[s['status']] += 1
        return [(s, tally[s]) for s in STATEMENT_STATUSES]

    @staticmethod
    def all_statements(c):
        yield from c.get('principal', [])
        for q in (c.get('frontier') or {}).get('questions', []):
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
        cells = []
        for st in CELL_STATUSES:
            if st in used_cells and st not in explained:
                gloss = self.page['cell_glosses'].get(st)
                if gloss:
                    cells.append(f'<div class="key-item"><dt>{mark(st)}<span>{html.escape(self.status_label(st))}'
                                 f'</span></dt><dd>{html.escape(gloss)}</dd></div>')
        extra = ''
        if cells:
            extra = (f'<p class="key-sub">{html.escape(self.page["labels"]["key_cells"])}</p>'
                     f'<dl class="key">{"".join(cells)}</dl>')
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
            status = (target or {}).get('status', 'open')
            head = (f'<a class="change-link" href="#s-{ident(ref)}">{mark(status)}<span>{title}</span></a>'
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

    def frontier(self, c):
        fr = c.get('frontier') or {}
        questions = fr.get('questions') or []
        if not questions:
            return ''
        L = self.page['labels']
        out = []
        all_added = all(st.get('added') for q in questions for st in [q.get('question') or {}] + (q.get('known') or []))
        for i, q in enumerate(questions):
            qid = 'q-' + ident(q.get('id') or q.get('title') or str(i))
            self.anchors.add(qid)
            question = q.get('question') or {}
            body = self.statement(question, f'frontier {i} question', title_override='', chip=not all_added) if question else ''
            why = (f'<div class="question-why prose"><p class="question-why-label">{html.escape(L["why"])}</p>'
                   f'{self.paragraphs(q["why"])}</div>') if q.get('why') else ''
            known = q.get('known') or []
            kn = ''
            if known:
                inner = ''.join(self.statement(s, f'frontier {i} known {j}', chip=not all_added) for j, s in enumerate(known))
                n = len(known)
                count = L['statements_one'] if n == 1 else L['statements_many'].format(n=n)
                kn = (f'<details class="known"><summary><span>{html.escape(L["known"])}</span>'
                      f'<span class="row-count">{html.escape(count)}</span>{icon("chevron")}</summary>'
                      f'<div class="statements">{inner}</div></details>')
            out.append(f'<div class="question" id="{qid}"><p class="question-num">{i + 1}</p>'
                       f'<h3><a class="anchor" href="#{qid}">{self.rich(q.get("title", ""), terms=False)}</a></h3>'
                       f'{body}{why}{kn}</div>')
        intro = f'<div class="section-intro prose">{self.paragraphs(fr["intro"])}</div>' if fr.get('intro') else ''
        return self.section('frontier', fr.get('heading') or L['frontier'], intro + f'<div class="questions">{"".join(out)}</div>',
                            kicker=L['frontier_kicker'], added=all_added)

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
        order = [cid for cid in COLUMNS if cid in columns] or COLUMNS
        for cid in COLUMNS:
            if cid not in columns:
                self.problems.append(f'columns: missing column {cid}')
        head = ''.join(
            f'<th scope="col"><button type="button" class="col-head" data-col="{cid}" '
            f'aria-describedby="col-{cid}">{html.escape(columns.get(cid, {}).get("short") or columns.get(cid, {}).get("name", cid))}'
            f'</button></th>' for cid in order)
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
                label = f'{r["name"]}, {colname}: {self.status_label(st)}'
                note_html = self.rich(note, terms=False)
                cells.append(
                    f'<td class="cell cell-{slug(st)}" data-status="{st}">'
                    f'<button type="button" class="cell-btn" data-row="{rid}" aria-label="{html.escape(label)}">'
                    f'{mark(st)}</button>'
                    f'<div class="cell-note" hidden><p class="cell-note-head">{mark(st)}<span>'
                    f'{html.escape(self.status_label(st))}</span> <span class="cell-note-where">'
                    f'{html.escape(colname)}</span></p><p>{note_html}</p></div></td>')
            short = r.get('short') or self.page.get('row_short', {}).get(r.get('id')) or r['name']
            rows.append(f'<tr><th scope="row"><a href="#{rid}" title="{html.escape(self.math_free(r["name"]))}">'
                        f'{self.rich(short, terms=False)}</a></th>'
                        f'{"".join(cells)}</tr>')
        col_notes = ''.join(
            f'<div class="col-def" id="col-{cid}"><dt>{html.escape(columns[cid]["name"])}</dt>'
            f'<dd>{self.rich(columns[cid].get("explanation", ""))}</dd></div>' for cid in order if cid in columns)
        table = (f'<div class="grid-wrap" tabindex="0" role="region" aria-label="{html.escape(L["grid"])}">'
                 f'<table class="grid"><caption class="visually-hidden">{html.escape(L["grid_caption"])}</caption>'
                 f'<thead><tr><th scope="col" class="corner">{html.escape(L["grid_corner"])}</th>{head}</tr></thead>'
                 f'<tbody>{"".join(rows)}</tbody></table></div>')
        legend = f'<div class="grid-legend">{self.key(c, compact=True)}</div>'
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
            body = ''.join(self.statement(s, f'row {r.get("id")} statement {j}') for j, s in enumerate(statements))
            cells = []
            for cid in COLUMNS:
                cell = (r.get('cells') or {}).get(cid)
                if not cell:
                    continue
                st = cell.get('status') if cell.get('status') in CELL_STATUSES else 'not posed'
                note = (cell.get('note') or '').strip()
                note_html = f'<span class="cell-text">{self.rich(note, terms=False)}</span>' if note else ''
                cells.append(f'<li class="cell-line cell-{slug(st)}">{mark(st)}<span class="cell-col">'
                             f'{html.escape(columns.get(cid, {}).get("name", cid))}</span>'
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
        filters = ''.join(
            f'<button type="button" class="filter" data-filter="{st}" aria-pressed="false">{mark(st)}'
            f'<span>{html.escape(self.status_label(st))}</span></button>'
            for st, n in self.counts(c) if n)
        toolbar = (f'<div class="row-tools"><div class="filters" role="group" aria-label="{html.escape(L["filter"])}">'
                   f'<span class="filters-label">{html.escape(L["filter"])}</span>{filters}</div>'
                   f'<div class="row-actions"><button type="button" class="link-btn" data-expand="all">{html.escape(L["expand"])}</button>'
                   f'<button type="button" class="link-btn" data-expand="none">{html.escape(L["collapse"])}</button></div></div>')
        return self.section('examples', L['examples'],
                            f'<p class="section-intro prose">{html.escape(L["examples_intro"])}</p>' +
                            self.grid(c) + toolbar + f'<div class="rows">{"".join(out)}</div>',
                            cls='wide', kicker=L['examples_kicker'])

    def open_problems(self, c):
        L = self.page['labels']
        groups = []
        for i, g in enumerate(c.get('open', [])):
            gid = 'open-' + ident(g.get('heading', str(i)))
            self.anchors.add(gid)
            body = ''.join(self.statement(s, f'open {i}.{j}') for j, s in enumerate(g.get('statements', [])))
            intro = f'<div class="prose group-intro">{self.paragraphs(g["intro"])}</div>' if g.get('intro') else ''
            groups.append(f'<div class="open-group" id="{gid}"><h3><a class="anchor" href="#{gid}">'
                          f'{self.rich(g.get("heading", ""), terms=False)}</a></h3>{intro}<div class="statements">{body}</div></div>')
        return self.section('open', L['open'], ''.join(groups), kicker=L['open_kicker'])

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
            esc = html.escape(block, quote=False)
            if len(block) <= 32 and '=' in block:
                paras.append(f'<p class="essay-display">{esc}</p>')
            else:
                paras.append(f'<p>{esc}</p>')
        lead_html = f'<p class="essay-lead">{self.rich(lead)}</p>' if (lead or '').strip() else ''
        self.essay_title = title
        return self.section('essay', L['essay'],
                            f'{lead_html}<article class="essay prose" aria-labelledby="essay-title">'
                            f'<h3 id="essay-title" class="essay-title">{html.escape(title)}</h3>'
                            f'<p class="essay-byline">{html.escape(self.page["author"])}</p>'
                            f'{"".join(paras)}</article>', kicker=L['essay_kicker'])

    def glossary(self):
        L = self.page['labels']
        items = []
        for e in sorted(self.term_links.entries, key=lambda e: e['term'].lower()):
            self.anchors.add(e['id'])
            items.append(f'<div class="gloss" id="{e["id"]}"><dt>{self.rich(e["term"], terms=False)}</dt>'
                         f'<dd>{self.rich(e.get("definition", ""), terms=False)}</dd></div>')
        if not items:
            return ''
        return self.section('terms', L['terms'], f'<p class="section-intro prose">{html.escape(L["terms_intro"])}</p>'
                            f'<dl class="glossary">{"".join(items)}</dl>', kicker=L['terms_kicker'])

    # Page -------------------------------------------------------------------------------

    def run(self):
        c = json.loads((self.folder / 'content.json').read_text(encoding='utf-8'))
        self.content = c
        essay_path = self.folder / 'essay.md'
        essay_text = essay_path.read_text(encoding='utf-8') if essay_path.exists() else ''
        self.term_links = Terms(c.get('glossary', []))
        L = self.page['labels']

        cover = self.cover(c)
        changes = self.changes(c)
        key = self.section('status', L['key'], self.key(c), cls='key-section', kicker=L['key_kicker'])
        principal = self.principal(c)
        frontier = self.frontier(c)
        examples = self.rows(c)
        failures = self.failures(c)
        open_ = self.open_problems(c)
        essay = self.essay(essay_text, c.get('essay_lead', '')) if essay_text else ''
        terms = self.glossary()

        nav_items = [('programme', L['nav_programme']), ('results', L['nav_results'])]
        if frontier:
            nav_items.append(('frontier', L['nav_frontier']))
        nav_items.append(('examples', L['nav_examples']))
        if failures:
            nav_items.append(('failures', L['nav_failures']))
        nav_items.append(('open', L['nav_open']))
        if essay:
            nav_items.append(('essay', L['nav_essay']))
        if terms:
            nav_items.append(('terms', L['nav_terms']))
        nav = ''.join(f'<li><a href="#{a}">{html.escape(t)}</a></li>' for a, t in nav_items)

        body = (f'<a class="skip" href="#main">{html.escape(L["skip"])}</a>'
                f'<div class="bar"><div class="bar-inner">'
                f'<a class="home" href="{html.escape(self.page["home"])}">{html.escape(self.page["home_label"])}</a>'
                f'<nav class="nav" aria-label="{html.escape(L["on_page"])}"><ul>{nav}</ul></nav>'
                f'<button type="button" class="theme" aria-label="{html.escape(L["theme"])}" title="{html.escape(L["theme"])}">'
                f'{icon("theme")}</button></div></div>'
                f'<main id="main" tabindex="-1">{cover}{changes}{key}{principal}{frontier}{examples}{failures}{open_}{essay}{terms}</main>'
                f'<footer class="foot"><div class="foot-inner"><p>{html.escape(self.page["author"])} · '
                f'<time datetime="{html.escape(c["as_of"])}">{html.escape(long_date(c["as_of"]))}</time></p>'
                f'<p><a href="{html.escape(self.page["home"])}">{html.escape(self.page["home_label"])}</a> · '
                f'<a href="#programme">{icon("up")}<span>{html.escape(L["top"])}</span></a></p></div></footer>'
                f'<div class="card" id="card" role="tooltip" hidden><div class="card-inner"></div></div>')

        self.math.render()
        body = self.math.substitute(body)
        for err in self.math.errors:
            self.problems.append('TeX: ' + err['error'][:160] + ' in ' + err['tex'][:80])

        css = (HERE / 'status.css').read_text(encoding='utf-8')
        js = (HERE / 'status.js').read_text(encoding='utf-8')
        fonts = self.font_faces(body)
        title_text = strip_tags(self.math_free(c['title']))
        description = strip_tags(self.math_free(c.get('subtitle', '')))
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
    font = TTFont(str(path))
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
