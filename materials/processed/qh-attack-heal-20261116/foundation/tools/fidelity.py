#!/usr/bin/env python3
"""Fidelity of a candidate status page against the baseline build (static HTML, before scripts).

    python3 tools/fidelity.py baseline/preview.html preview.html [--json out.json] [--relabel <old page.json> <new page.json>]

--relabel: the status labels changed by a ruling (page.json status_labels, selected by the stored code) are mapped from the
old page.json to the new one in the baseline's units before E6 compares rows and the status key, so that a ruled relabelling
is not read as a loss; every other word must still match.

Checks (EVALUATION-PLAN.md E4-E7, E17):
  E4 every id of the baseline exists in the candidate;
  E5 every anchored statement keeps its data-status; the status multiset of all statements is equal;
     every grid cell keeps its (row, column) status;
  E6 every research unit keeps its text: statements (status, title, text, notes), question cards
     (title, why), rows (name, summary, lines by column), grid cell notes, column definitions,
     counterexample claims, open-problem groups, glossary entries, status key, lead, essay;
     the count of <math> elements is equal;
  E7 the Content-Security-Policy, title and description are unchanged.
Exit status 0 when every check passes.
"""
import hashlib
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}


class Node:
    __slots__ = ('tag', 'attrs', 'children', 'parent')

    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.children, self.parent = tag, dict(attrs), [], parent

    def cls(self):
        return self.attrs.get('class', '').split()

    def walk(self):
        yield self
        for c in self.children:
            if isinstance(c, Node):
                yield from c.walk()

    def find_all(self, pred):
        return [n for n in self.walk() if pred(n)]

    def first(self, pred):
        for n in self.walk():
            if pred(n):
                return n
        return None

    def text(self, skip=None):
        out = []

        def rec(n):
            for c in n.children:
                if isinstance(c, str):
                    out.append(c)
                elif c.tag in ('svg', 'script', 'style'):
                    continue
                elif skip and skip(c):
                    continue
                else:
                    rec(c)
                    out.append(' ')
        rec(self)
        return re.sub(r'\s+', ' ', ''.join(out)).strip()

    def ancestors(self):
        p = self.parent
        while p is not None:
            yield p
            p = p.parent


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('#root', {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def parse(path):
    t = Tree()
    raw = open(path, encoding='utf-8').read()
    t.feed(raw)
    return t.root, raw


def has(c):
    return lambda n: c in n.cls()


def statement_tuple(n):
    title = n.first(has('statement-title'))
    text = n.first(has('statement-text'))
    notes = n.first(has('statement-notes'))
    return (n.attrs.get('data-status', ''), title.text() if title else '', text.text() if text else '',
            notes.text() if notes else '')


def units(root, raw):
    u = {}
    u['ids'] = set(re.findall(r'\sid="([^"]+)"', raw))
    stmts = root.find_all(lambda n: n.tag == 'article' and 'statement' in n.cls())
    u['statements'] = Counter(statement_tuple(s) for s in stmts)
    u['statement_status'] = Counter(s.attrs.get('data-status', '') for s in stmts)
    u['anchored_status'] = {s.attrs['id']: s.attrs.get('data-status', '') for s in stmts if s.attrs.get('id')}
    u['anchored_text'] = {s.attrs['id']: statement_tuple(s) for s in stmts if s.attrs.get('id')}
    # Questions.
    q = {}
    for n in root.find_all(lambda n: 'question' in n.cls() and n.attrs.get('id', '').startswith('q-')):
        h3 = n.first(lambda x: x.tag == 'h3')
        why = n.first(has('question-why'))
        known = n.find_all(lambda x: x.tag == 'article' and 'statement' in x.cls())
        q[n.attrs['id']] = (h3.text() if h3 else '', why.text(skip=has('question-why-label')) if why else '', len(known))
    u['questions'] = q
    # Rows (the detail under the grid).
    rows = {}
    for n in root.find_all(lambda n: n.attrs.get('id', '').startswith('row-')):
        name = n.first(has('row-name'))
        summ = n.first(has('row-summary'))
        lines = n.find_all(has('cell-line'))
        rows[n.attrs['id']] = (name.text() if name else '', summ.text() if summ else '',
                               tuple(sorted(l.text() for l in lines)),
                               len(n.find_all(lambda x: x.tag == 'article' and 'statement' in x.cls())))
    u['rows'] = rows
    # Grid cells.
    grid = root.first(lambda n: n.tag == 'table' and 'grid' in n.cls())
    cells = {}
    if grid is not None:
        cols = [b.attrs.get('data-col') for b in grid.find_all(has('col-head'))]
        for td in grid.find_all(lambda n: n.tag == 'td' and 'cell' in n.cls()):
            btn = td.first(has('cell-btn'))
            tr = td.parent
            tds = [c for c in tr.children if isinstance(c, Node) and c.tag == 'td']
            col = cols[tds.index(td)] if tds.index(td) < len(cols) else '?'
            note = td.first(has('cell-note'))
            paras = [p for p in (note.children if note else []) if isinstance(p, Node) and p.tag == 'p']
            # The note is the paragraph after the head (the baseline has no class on it; a candidate may add
            # a paragraph giving the status's meaning after it).
            body = [p for p in paras if not ({'cell-note-head', 'cell-note-meaning'} & set(p.cls()))]
            cells[(btn.attrs.get('data-row') if btn else '?', col)] = (td.attrs.get('data-status', ''),
                                                                      body[0].text() if body else '')
    u['cells'] = cells
    u['col_defs'] = {n.attrs['id']: n.text() for n in root.find_all(has('col-def')) if n.attrs.get('id')}
    u['failures'] = {n.attrs['id']: (n.first(has('claim-text')).text() if n.first(has('claim-text')) else '')
                     for n in root.find_all(has('failure')) if n.attrs.get('id')}
    groups = {}
    for n in root.find_all(has('open-group')):
        h3 = n.first(lambda x: x.tag == 'h3')
        intro = n.first(has('group-intro'))
        groups[n.attrs.get('id', '')] = (h3.text() if h3 else '', intro.text() if intro else '')
    u['open_groups'] = groups
    u['glossary'] = {n.attrs['id']: n.text() for n in root.find_all(has('gloss')) if n.attrs.get('id')}
    u['key'] = Counter(n.text() for n in root.find_all(has('key-item')))
    lead = root.first(lambda n: 'lead' in n.cls() and n.tag == 'div')
    u['lead'] = tuple(p.text() for p in (lead.find_all(lambda x: x.tag == 'p') if lead else []))
    essay = root.first(lambda n: n.tag == 'article' and 'essay' in n.cls())
    u['essay'] = tuple(p.text() for p in (essay.find_all(lambda x: x.tag in ('p', 'h3')) if essay else []))
    el = root.first(has('essay-lead'))
    u['essay_lead'] = el.text() if el else ''
    for kind in ('intro',):
        u['section_intros'] = Counter(n.text() for n in root.find_all(has('section-intro')))
    u['math'] = raw.count('<math')
    u['tex'] = Counter(re.findall(r'<annotation encoding="application/x-tex">(.*?)</annotation>', raw, re.S))
    m = re.search(r'Content-Security-Policy" content="([^"]*)"', raw)
    u['csp'] = m.group(1) if m else ''
    m = re.search(r'<title>(.*?)</title>', raw)
    u['title'] = m.group(1) if m else ''
    m = re.search(r'<meta name="description" content="([^"]*)"', raw)
    u['description'] = m.group(1) if m else ''
    return u


def compare(a, b):
    report = []

    def check(name, ok, detail=''):
        report.append({'check': name, 'pass': bool(ok), 'detail': detail})

    missing = sorted(a['ids'] - b['ids'])
    check('E4 ids preserved', not missing, f'{len(missing)} missing: {missing[:20]}')
    added = sorted(b['ids'] - a['ids'])
    report.append({'check': 'info: ids added', 'pass': True, 'detail': f'{len(added)}: {added[:30]}'})
    changed = {k: (v, b['anchored_status'].get(k)) for k, v in a['anchored_status'].items() if b['anchored_status'].get(k) != v}
    check('E5 anchored statement status', not changed, json.dumps(changed)[:400])
    check('E5 status multiset', a['statement_status'] == b['statement_status'],
          f"{dict(a['statement_status'])} vs {dict(b['statement_status'])}")
    cell_diff = {f'{k[0]}/{k[1]}': (v[0], b['cells'].get(k, ('MISSING',))[0]) for k, v in a['cells'].items()
                 if b['cells'].get(k, ('MISSING',))[0] != v[0]}
    check('E5 grid cell status', not cell_diff and len(a['cells']) == len(b['cells']),
          f"{len(a['cells'])} vs {len(b['cells'])} cells; diffs {json.dumps(cell_diff)[:300]}")
    lost = a['statements'] - b['statements']
    check('E6 statements (status, title, text, notes) multiset', not lost,
          f'{sum(lost.values())} baseline statements without an identical candidate: ' +
          json.dumps([list(x)[:2] + [x[2][:80]] for x in list(lost)[:5]]))
    text_changed = [k for k, v in a['anchored_text'].items() if b['anchored_text'].get(k) != v]
    check('E6 anchored statement text', not text_changed, str(text_changed[:10]))
    for key in ('questions', 'rows', 'col_defs', 'failures', 'open_groups', 'glossary'):
        diff = [k for k, v in a[key].items() if b[key].get(k) != v]
        check(f'E6 {key}', not diff and len(a[key]) <= len(b[key]),
              f'{len(a[key])} vs {len(b[key])}; differing: {diff[:8]}' +
              (f' e.g. {a[key][diff[0]]!r:.200} -> {b[key].get(diff[0])!r:.200}' if diff else ''))
    cell_note_diff = [f'{k[0]}/{k[1]}' for k, v in a['cells'].items() if b['cells'].get(k, (None, None))[1] != v[1]]
    check('E6 grid cell notes', not cell_note_diff, str(cell_note_diff[:8]))
    check('E6 status key', not (a['key'] - b['key']), str(list(a['key'] - b['key'])[:3]))
    for key in ('lead', 'essay', 'essay_lead'):
        check(f'E6 {key}', a[key] == b[key], '' if a[key] == b[key] else f'{str(a[key])[:160]} -> {str(b[key])[:160]}')
    check('E6 section intros', not (a['section_intros'] - b['section_intros']), str(list(a['section_intros'] - b['section_intros'])[:2])[:300])
    lost_tex = a['tex'] - b['tex']
    check('E6 every baseline formula present (TeX multiset inclusion)', not lost_tex,
          f"{sum(lost_tex.values())} lost: {list(lost_tex)[:5]}")
    report.append({'check': 'info: formula elements', 'pass': True,
                   'detail': f"{a['math']} -> {b['math']} (extra: {dict(list((b['tex'] - a['tex']).items())[:6])})"})
    for key in ('csp', 'title', 'description'):
        check(f'E7 {key}', a[key] == b[key], '' if a[key] == b[key] else f'{a[key][:120]} -> {b[key][:120]}')
    return report


def relabel(u, old, new):
    """Map the old status labels to the new ones (longest first) in the units that show status labels: row lines, key."""
    pairs = sorted(((old[k], new[k]) for k in old if k in new and old[k] != new[k]), key=lambda p: -len(p[0]))

    def m(t):
        for a, b in pairs:
            t = t.replace(a, b)
        return t
    u['rows'] = {k: (v[0], v[1], tuple(sorted(m(x) for x in v[2])), v[3]) for k, v in u['rows'].items()}
    u['key'] = Counter({m(k): n for k, n in u['key'].items()})
    return pairs


def main():
    base, cand = sys.argv[1], sys.argv[2]
    ra, rawa = parse(base)
    rb, rawb = parse(cand)
    ua = units(ra, rawa)
    if '--relabel' in sys.argv:
        k = sys.argv.index('--relabel')
        old = json.load(open(sys.argv[k + 1], encoding='utf-8'))['status_labels']
        new = json.load(open(sys.argv[k + 2], encoding='utf-8'))['status_labels']
        print('info relabelled by the ruling: ' + '; '.join(f'{a} -> {b}' for a, b in relabel(ua, old, new)))
    report = compare(ua, units(rb, rawb))
    ok = all(r['pass'] for r in report)
    for r in report:
        print(('PASS ' if r['pass'] else 'FAIL ') + r['check'] + (f' — {r["detail"]}' if r['detail'] and (not r['pass'] or r['check'].startswith('info')) else ''))
    print('candidate sha256', hashlib.sha256(rawb.encode()).hexdigest())
    print('ALL PASS' if ok else 'FIDELITY FAILURES')
    if '--json' in sys.argv:
        json.dump(report, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
