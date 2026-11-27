#!/usr/bin/env python3
"""Fidelity and hygiene checks for a candidate page against the baseline page (checks E2-E5 of EVAL-PLAN.md).

    python3 -I tools/fidelity.py [--same-content] [--js <status.js>] <worktree> <baseline.html> <candidate.html> [<ids-file> ...]

With --same-content the two pages are built from the same content (any content, for instance the final payload, once with
the script of the review baseline and once with the candidate's), and the hashes of BASELINE.json are not checked. --js
names the status.js the candidate page must carry (default: the worktree's compiler/quantum-holography-status/status.js).

E2: content.json, essay.md, page.json and README.md hashes equal BASELINE.json; the statements (status, title, text),
    the table's cell statuses and the tally are identical in both pages.
E3: every static id of the baseline page and of each ids-file exists in the candidate; every in-page href resolves.
E4: the Content-Security-Policy meta is byte-identical; the page carries status.js verbatim; no inline script makes a
    network call or builds code from strings.
E5: no inline script (all are public in the page) has process, version or tool vocabulary or a private path; each script
    is named in the result, status.js by its content.
Prints one line per check and exits 1 when any fails."""
import hashlib
import html as htmllib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class Statements(HTMLParser):
    """Collects each article.statement's status, title text and body text, the cells and the tally."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.items = []
        self.cells = []
        self.tally = []
        self.cur = None
        self.field = None
        self.skip = 0
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get('class') or '').split()
        if tag in ('annotation', 'svg', 'script', 'style'):
            self.skip += 1
        if tag == 'article' and 'statement' in cls:
            self.cur = {'status': a.get('data-status'), 'title': '', 'text': '', 'depth': 0}
            self.items.append(self.cur)
        if self.cur is not None:
            self.cur['depth'] += 1
            if 'statement-title' in cls:
                self.field = ('title', self.cur['depth'])
            elif 'statement-text' in cls:
                self.field = ('text', self.cur['depth'])
        if tag == 'td' and 'cell' in cls:
            self.cells.append(a.get('data-status'))
        if tag == 'a' and a.get('data-filter') and a.get('href') == '#examples':
            self.tally.append(a.get('data-filter'))

    def handle_endtag(self, tag):
        if tag in ('annotation', 'svg', 'script', 'style') and self.skip:
            self.skip -= 1
        if self.cur is not None:
            if self.field and self.field[1] == self.cur['depth']:
                self.field = None
            self.cur['depth'] -= 1
            if tag == 'article' and self.cur['depth'] == 0:
                self.cur = None

    def handle_data(self, data):
        if self.cur is not None and self.field and not self.skip:
            self.cur[self.field[0]] += data


def statements(markup):
    p = Statements()
    p.feed(markup)
    norm = lambda s: re.sub(r'\s+', ' ', s).strip()
    return ([(i['status'], norm(i['title']), norm(i['text'])) for i in p.items], p.cells,
            re.findall(r'data-filter="([^"]+)"><svg[^>]*>.*?</svg><span class="count">(\d+)</span>', markup))


def ids(markup):
    return re.findall(r'\sid="([^"]+)"', markup)


def scripts_of(markup):
    return re.findall(r'<script>(.*?)</script>', markup, re.S)


def prose_of(js):
    """The comments and string literals of a script, with their line numbers (regex literals are skipped)."""
    out, i, n, line, last = [], 0, len(js), 1, ''
    while i < n:
        c = js[i]
        if c == '\n':
            line += 1
        if js.startswith('//', i):
            j = js.find('\n', i)
            j = n if j < 0 else j
            out.append((line, js[i:j]))
            i = j
            continue
        if js.startswith('/*', i):
            j = js.find('*/', i + 2) + 2
            out.append((line, js[i:j]))
            line += js[i:j].count('\n')
            i = j
            continue
        if c in '\'"`':
            j = i + 1
            while j < n and js[j] != c:
                j += 2 if js[j] == '\\' else 1
            out.append((line, js[i:j + 1]))
            line += js[i:j + 1].count('\n')
            i = j + 1
            last = c
            continue
        if c == '/' and (last in '(,=:[!&|?{};+-*%<>~^' or re.search(r'(return|typeof|case)\s*$', js[max(0, i - 8):i])):
            j, cls = i + 1, False
            while j < n and (js[j] != '/' or cls):
                if js[j] == '\\':
                    j += 1
                elif js[j] == '[':
                    cls = True
                elif js[j] == ']':
                    cls = False
                j += 1
            i = j + 1
            last = '/'
            continue
        if not c.isspace():
            last = c
        i += 1
    return out


def main():
    args = sys.argv[1:]
    same = '--same-content' in args
    if same:
        args.remove('--same-content')
    js_path = None
    if '--js' in args:
        i = args.index('--js')
        js_path = Path(args[i + 1])
        del args[i:i + 2]
    tree, base_path, cand_path = Path(args[0]), Path(args[1]), Path(args[2])
    extra_ids = args[3:]
    js_path = js_path or tree / 'compiler/quantum-holography-status/status.js'
    base, cand = base_path.read_text(encoding='utf-8'), cand_path.read_text(encoding='utf-8')
    results = []

    def check(name, ok, detail=''):
        results.append(ok)
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))

    if same:
        print('SKIP E2 hashes: the content is not the review baseline\'s, by design (--same-content)')
    else:
        manifest = json.loads((tree / 'materials/processed/qh-attack-heal-20261116/interaction/BASELINE.json').read_text())
        for f in manifest['files']:
            if f['path'].startswith('content/'):
                h = hashlib.sha256((tree / f['path']).read_bytes()).hexdigest()
                check('E2 hash ' + f['path'], h == f['sha256'], h[:16])

    sb, cb, tb = statements(base)
    sc, cc, tc = statements(cand)
    check('E2 statements identical', sb == sc, f'{len(sb)} baseline, {len(sc)} candidate')
    if sb != sc:
        for x, y in zip(sb, sc):
            if x != y:
                print('   first difference:', x[:2], '|', y[:2])
                break
    check('E2 cell statuses identical', cb == cc, f'{len(cb)} cells')
    check('E2 tally identical', tb == tc, str(tc))

    cand_ids = ids(cand)
    dup = sorted({i for i in cand_ids if cand_ids.count(i) > 1})
    check('E3 no duplicate static id', not dup, ', '.join(dup[:5]))
    cset = set(cand_ids)
    missing = sorted(set(ids(base)) - cset)
    check('E3 baseline ids kept', not missing, f'{len(set(ids(base)))} ids; missing: {", ".join(missing[:8])}')
    for f in extra_ids:
        want = {line.strip() for line in Path(f).read_text().splitlines() if line.strip()}
        lost = sorted(want - cset)
        check('E3 ids kept from ' + Path(f).name, not lost, f'{len(want)} ids; missing: {", ".join(lost[:8])}')
    bare = re.sub(r'<script\b.*?</script>', ' ', cand, flags=re.S)
    broken = sorted({h for h in re.findall(r'href="#([^"]*)"', bare) if h and h not in cset})
    check('E3 in-page links resolve', not broken, ', '.join(broken[:8]))

    csp = lambda m: re.search(r'<meta http-equiv="Content-Security-Policy"[^>]*>', m).group(0)
    check('E4 CSP identical', csp(base) == csp(cand), csp(cand)[60:160])
    own = js_path.read_text(encoding='utf-8').strip()
    scripts = scripts_of(cand)
    names = ['status.js' if x.strip() == own else f'inline script {i + 1}' for i, x in enumerate(scripts)]
    check('E4 the page carries status.js verbatim', 'status.js' in names,
          f'{len(scripts)} inline scripts: ' + ', '.join(f'{n} ({len(x)} chars)' for n, x in zip(names, scripts)))
    for name, js in zip(names, scripts):
        net = re.findall(r'\b(fetch|XMLHttpRequest|sendBeacon|WebSocket|EventSource|importScripts|eval)\s*\(|new\s+Function\s*\(|\bimport\s*\(', js)
        check(f'E4 no network call or string code in {name}', not net, str(net[:5]))

    words = re.compile(r'\b(wave|phase|lane|swarm|attack(er)?s?|heal(ed|ing)?|draft|version|v\d|todo|fixme|hack|astra|claude|codex|'
                       r'opus|fable|gpt|openai|anthropic|llm|agent|prompt|worktree|commit|pipeline|ledger|audit|owner|reviewer|'
                       r'baseline|candidate|foundation|interaction lane|atlas lane|quality lane)\b', re.I)
    for name, js in zip(names, scripts):
        hits = []
        prose = prose_of(js)
        for n, text in prose:
            for m in words.finditer(text):
                hits.append(f'{n}:{m.group(0)}')
        paths = re.findall(r'/Users/|~/|\.claude|materials/|compiler/|content/', js)
        check(f'E5 vocabulary of {name} (comments and strings)', not hits, f'{len(prose)} pieces; ' + ', '.join(hits[:12]))
        check(f'E5 paths in {name}', not paths, ', '.join(paths[:5]))
    print('summary:', 'PASS' if all(results) else f'{results.count(False)} failure(s)')
    return 0 if all(results) else 1


if __name__ == '__main__':
    sys.exit(main())
