#!/usr/bin/env python3
"""Static DOM contract check (no browser): the markup status.py writes, before status.js runs.

    python3 tools/contract_static.py <page.html> [--candidate]

Asserts each selector of the status.py <-> status.js contract (CONTRACT.json) with its minimum count, using a
small CSS selector engine over the parsed HTML (tag, #id, .class, [attr], [attr=v], [attr^=v], [attr*=v],
:not(compound), :first-child; descendant, '>' and '+' combinators; selector lists). Hooks that status.js creates
at run time cannot be checked here and are listed as such. --candidate adds the foundation lane's structures
and its attribute checks. Exit status 0 when every check passes.
"""
import re
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from fidelity import Node, parse  # noqa: E402

RUNTIME_ONLY = ['.find[role="search"] #find-q (search, built by status.js)',
                '.row-actions.known-actions (question-section toolbar, added by status.js)',
                '#card content (.card-term, .card-more), written by status.js']

HOOKS = [
    ('html', 1), ('button.theme', 1), ('#main', 1), ('a.skip[href="#main"]', 1),
    ('#card[role="dialog"][hidden] > .card-inner', 1),
    ('button.term[data-term][aria-controls="card"][aria-expanded]', 100),
    ('.gloss[id^="term-"] > dt + dd', 144), ('#terms h2', 1), ('table.grid', 1),
    ('table.grid thead button.col-head[data-col][aria-controls="card"]', 8),
    ('.col-def[id^="col-"] > dt + dd', 8),
    ('table.grid td.cell[data-status] > button.cell-btn[data-row][aria-controls="card"] + .cell-note[hidden]', 160),
    ('table.grid tbody th a[href^="#row-"]', 20), ('details.row[id^="row-"] > summary', 20),
    ('details.row .row-name', 20), ('.rows .statement[data-status]', 100), ('.row-tools', 1),
    ('.filter[data-filter][aria-pressed]', 3), ('[data-expand="all"]', 1), ('[data-expand="none"]', 1),
    ('main section.section .questions', 2), ('.tally a[data-filter]', 3), ('main > .tally', 1),
    ('.nav a[href^="#"]', 6), ('main .statement[data-status] .statement-head .status-chip .mark', 281),
    ('main .statement .statement-title', 200), ('main .question[id^="q-"] h3', 34),
    ('main .question .question-num .question-num-label', 34),
    ('main .question > .statement, main .question > .question-ask > .statement', 34),
    ('main .failure[id] .claim-text', 11), ('main .failure > .statement', 11), ('main .open-group[id] h3', 4),
    ('main .col-def dt', 8), ('#essay-title', 1), ('main .essay > p:not(.essay-byline)', 20), ('main .essay-lead', 1),
    ('main .gloss dt', 144), ('.math-display, .math-long', 50), ('section#results, section#examples, section#open', 3),
]

NEW_HOOKS = [
    ('main > .overview > nav.contents[aria-labelledby="contents-label"] ol > li > a[href^="#"]', 9),
    ('main > .overview > header.cover#programme + .lead + nav.contents', 1),
    ('main > .overview + nav.tally', 1),
    ('main > section.questions-section.wide', 2),
    ('.question.compare > .question-ask > .question-ask-label + .statement', 34),
    ('.question-known > ul.statements.known-list > li.fold-item > details.known.fold > summary.fold-head', 105),
    ('details.known.fold > article.statement[data-status][id^="s-"]', 105),
    ('.statement[id] > .statement-head > .statement-context > a[href^="#"]', 135),
    ('.question.compare > .question-ask > .question-ask-label[data-label]', 34),
    ('.bar > .bar-inner > a.nav-top[href="#programme"] + nav.nav', 1),
    ('main > .overview > nav.contents#contents', 1),
    ('.grid-block > .grid-wrap[role="region"]:not([tabindex])', 1),
    ('.q-index-head > .q-index-label[id]', 2),
    ('.bar button.find-open[data-find-open]', 1),
    ('.grid-legend .legend-key a[href="#status"]', 1),
    ('.cell-note > .cell-note-head + .cell-note-text', 160),
    ('.cell-note > .cell-note-meaning', 160),
    ('button.col-head > .col-head-text', 8),
    ('section#terms.terms-section > nav.gloss-index a[href^="#term-"]', 2),
    ('table.grid thead th:first-child + th > button.col-head:not([tabindex])', 1),
    ('table.grid button.col-head[tabindex="-1"]', 7),
    ('table.grid button.cell-btn[tabindex="-1"]', 160),
    ('table.grid tbody th > a.row-link[tabindex="-1"]', 20),
    ('.math-display > math[style*="--fw:"]', 1),
    ('main section.section > header.section-head > p.kicker > span.part-num', 9),
    ('main > .overview > nav.contents ol > li > a > span.contents-num + span.contents-title', 9),
    ('details.known.fold > summary.fold-head > span.fold-status', 105),
    ('.question-known > p.known-head > span.known-key > svg.mark', 1),
]

TOKEN = re.compile(r'\s*([>+])\s*|\s+')
SIMPLE = re.compile(r'(#[\w-]+)|(\.[\w-]+)|(\[[^\]]+\])|(:not\((?:[^()]|\([^()]*\))*\))|(:first-child)|([\w-]+|\*)')


def split_list(sel):
    out, depth, cur = [], 0, ''
    for ch in sel:
        depth += ch == '('
        depth -= ch == ')'
        if ch == ',' and depth == 0:
            out.append(cur.strip())
            cur = ''
        else:
            cur += ch
    out.append(cur.strip())
    return out


def parse_complex(sel):
    """'a > b c + d' -> [(None, 'a'), ('>', 'b'), (' ', 'c'), ('+', 'd')]."""
    parts, comb, i, depth, cur = [], None, 0, 0, ''
    while i < len(sel):
        ch = sel[i]
        if ch in '([':
            depth += 1
        if ch in ')]':
            depth -= 1
        if depth == 0 and (ch in ' >+'):
            if cur:
                parts.append((comb, cur))
                cur, comb = '', ' '
            j = i
            while j < len(sel) and sel[j] in ' >+':
                if sel[j] in '>+':
                    comb = sel[j]
                j += 1
            i = j
            continue
        cur += ch
        i += 1
    if cur:
        parts.append((comb, cur))
    return parts


def elements(n):
    return [k for k in n.children if isinstance(k, Node)]


def match_compound(n, comp):
    if not isinstance(n, Node) or n.tag.startswith('#'):
        return False
    for m in SIMPLE.finditer(comp):
        idp, cls, attr, neg, first, tag = m.groups()
        if tag and tag != '*' and n.tag != tag:
            return False
        if idp and n.attrs.get('id') != idp[1:]:
            return False
        if cls and cls[1:] not in n.cls():
            return False
        if first:
            sib = elements(n.parent) if n.parent else []
            if not sib or sib[0] is not n:
                return False
        if attr:
            a = re.match(r'\[([\w-]+)(?:([\^*]?=)"([^"]*)")?\]', attr)
            name, op, val = a.groups()
            if name not in n.attrs:
                return False
            v = n.attrs.get(name) or ''
            if op == '=' and v != val:
                return False
            if op == '^=' and not v.startswith(val):
                return False
            if op == '*=' and val not in v:
                return False
        if neg and match_compound(n, neg[5:-1]):
            return False
    return True


def matches(n, parts):
    comb, comp = parts[-1]
    if not match_compound(n, comp):
        return False
    if len(parts) == 1:
        return True
    rest = parts[:-1]
    if comb == '>':
        return n.parent is not None and matches(n.parent, rest)
    if comb == '+':
        sib = elements(n.parent) if n.parent else []
        k = sib.index(n)
        return k > 0 and matches(sib[k - 1], rest)
    p = n.parent
    while p is not None:
        if matches(p, rest):
            return True
        p = p.parent
    return False


def count(root, selector):
    lists = [parse_complex(s) for s in split_list(selector)]
    return sum(1 for n in root.walk() if any(matches(n, parts) for parts in lists))


def main():
    path = sys.argv[1]
    root, raw = parse(path)
    candidate = '--candidate' in sys.argv
    ok = True
    for sel, minimum in HOOKS + (NEW_HOOKS if candidate else []):
        n = count(root, sel)
        good = n >= minimum
        ok &= good
        print(('PASS ' if good else 'FAIL ') + f'{n:>5} >= {minimum:<4} {sel}')
    if candidate:
        checks = [
            ('no attribute carries TeX delimiters', not re.search(r'="[^"]*\\[(\[]', raw)),
            ('no TeX annotation inside a family link of the table',
             not re.search(r'<a class="row-link"[^>]*>(?:(?!</a>).)*<annotation', raw, re.S)),
            ('no context line on a statement without an anchor', ' class="statement-context"' not in ''.join(
                re.findall(r'<article class="statement[^"]*" data-status="[^"]*">(?:(?!</article>).)*', raw, re.S))),
            ('the question part label has no text node (search skips it; CSS draws it)',
             not re.search(r'<p class="question-ask-label"[^>]*>[^<]+</p>', raw)),
            ('no glossary term inside a column definition',
             not re.search(r'<div class="col-def"[^>]*>(?:(?!</div>).)*class="term"', raw, re.S)),
            ('every section head carries the part number of its contents entry',
             re.findall(r'<section id="([^"]+)"[^>]*><header class="section-head"><p class="kicker"><span class="part-num">([^<]*)</span>', raw)
             == re.findall(r'<li><a href="#([^"]+)"><span class="contents-num">([^<]*)</span>', raw)),
            ('a related statement shows its status text unless it is checked (then the text is read, not shown)',
             all((hidden == ' visually-hidden') == (st == 'checked') for hidden, st in re.findall(
                 r'<span class="fold-status( visually-hidden)?">[^<]*</span>(?:(?!<article).)*<article class="statement[^"]*" data-status="([^"]+)"',
                 raw, re.S))),
            ('a card names the checked mark in its related-statements head exactly when a related statement is checked',
             all(('data-status="checked"' in cd) == ('class="known-key"' in cd)
                 for cd in re.findall(r'<div class="question-known">(.*?)</ul></div>', raw, re.S))),
            ('every hidden separator leaves its spaces outside, so the text reads with spaces (kickers, date line, notes)',
             not re.search(r'<span class="sep" aria-hidden="true">\s|<span class="sep" aria-hidden="true">[^<]*\s</span>', raw)),
            ('one id per element name (no duplicate ids)', len(re.findall(r'\sid="([^"]+)"', raw)) == len(set(re.findall(r'\sid="([^"]+)"', raw)))),
        ]
        for name, good in checks:
            ok &= bool(good)
            print(('PASS ' if good else 'FAIL ') + name)
    for r in RUNTIME_ONLY:
        print('NOT CHECKED (created at run time) ' + r)
    print('ALL PASS' if ok else 'CONTRACT FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
