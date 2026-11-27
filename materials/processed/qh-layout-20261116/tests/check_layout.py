#!/usr/bin/env python3
"""Focused checks of the layout build against the unmodified baseline build.

    python3 -I check_layout.py <baseline.html> <new.html> <content.json>

1. Every formula of the baseline appears in the new page the same number of times (MathML multiset).
2. Every statement card of the baseline appears unchanged in the new page, except that a question
   whose own title differs from its card title now shows that title; the shown title must be the
   content's own title, byte for byte.
3. All 22 decisive questions are present in content order, each with an index link.
4. Every element and attribute status.js selects is still present, in the same numbers.
5. No baseline id is lost.
"""
import collections
import html
import json
import re
import sys

base = open(sys.argv[1], encoding='utf-8').read()
new = open(sys.argv[2], encoding='utf-8').read()
content = json.load(open(sys.argv[3], encoding='utf-8'))
fails = []

def body(m):
    return m[m.find('<body'):]

b, n = body(base), body(new)

# 1. Formulas.
mb = collections.Counter(re.findall(r'<math\b.*?</math>', b, re.S))
mn = collections.Counter(re.findall(r'<math\b.*?</math>', n, re.S))
missing = mb - mn
if missing:
    fails.append(f'{sum(missing.values())} formula occurrence(s) of the baseline missing')
print(f'formulas: baseline {sum(mb.values())}, new {sum(mn.values())}, extra in new {sum((mn - mb).values())}')

# 2. Statement cards.
art = lambda s: re.findall(r'<article class="statement.*?</article>', s, re.S)
ab, an = collections.Counter(art(b)), collections.Counter(art(n))
lost = ab - an
gained = an - ab
titled = {}
for key in ('decisive', 'frontier'):
    for q in (content.get(key) or {}).get('questions', []):
        qs = q.get('question') or {}
        if qs.get('title') and qs['title'].strip() != (q.get('title') or '').strip():
            titled[qs.get('id')] = qs['title']
explained = 0
for a in list(lost.elements()):
    sid = re.search(r'id="s-([^"]+)"', a)
    cand = [g for g in gained if sid and f'id="s-{sid.group(1)}"' in g]
    if len(cand) != 1:
        fails.append(f'statement lost without counterpart: {a[:120]}')
        continue
    g = cand[0]
    m = re.search(r'<h4 class="statement-title">(.*?)</h4>', g, re.S)
    stripped = g.replace(m.group(0), '') if m else g
    raw = next((t for i, t in titled.items() if sid.group(1) == re.sub(r'[\s_-]+', '-', i.lower())), None)
    if stripped != a or not m or raw is None or html.unescape(re.sub(r'<[^>]+>', '', m.group(1))) != raw:
        fails.append(f'statement changed beyond its own title: s-{sid.group(1)}')
    else:
        explained += 1
print(f'statements: baseline {sum(ab.values())}, new {sum(an.values())}, unchanged {sum((ab & an).values())}, '
      f'now titled {explained} (content questions with a distinct own title: {len(titled)})')
if explained != len(titled):
    fails.append('not every distinct question title is shown exactly once')

# 3. Decisive questions.
qs = content['decisive']['questions']
ids = re.findall(r'<div class="question compare[^"]*" id="(q-[^"]+)"', n)
want = ['q-' + re.sub(r'[\s_-]+', '-', q['id'].lower()) for q in qs]
if len(qs) != 22 or ids != want:
    fails.append(f'decisive questions: {len(ids)} cards, expected 22 in content order')
sec = n[n.find('<section id="decisive"'):n.find('</section>', n.find('<section id="decisive"'))]
links = re.findall(r'<nav class="q-index".*?</nav>', sec, re.S)
idx = re.findall(r'href="#(q-[^"]+)"', links[0]) if links else []
if idx != want:
    fails.append('decisive index does not link every question in order')
for q in qs:
    if html.escape(q['title'], quote=False) not in sec:
        fails.append(f'decisive title missing: {q["title"]}')
print(f'decisive: {len(ids)} cards, {len(idx)} index links')

# 4. Hooks of status.js.
hooks = {
    '.theme': r'<button[^>]*class="theme"', '#card .card-inner': r'id="card"[^>]*><div class="card-inner"',
    '.term[data-term]': r'class="term" data-term="', '.cell-btn[data-row]': r'class="cell-btn" data-row="',
    '.cell-note': r'class="cell-note"', '.col-head[data-col]': r'class="col-head" data-col="',
    '#col-*': r'id="col-', 'details.row': r'<details class="row"', '[data-expand]': r'data-expand="',
    '.filter[data-filter]': r'class="filter" data-filter="', '.tally a[data-filter]': r'<a href="#examples" data-filter="',
    '.rows .statement[data-status]': None, '.nav a': None, '#terms h2': r'<section id="terms"',
}
for name, pat in hooks.items():
    if pat is None:
        continue
    cb, cn = len(re.findall(pat, b)), len(re.findall(pat, n))
    if cb != cn or cb == 0:
        fails.append(f'hook {name}: baseline {cb}, new {cn}')
rows = lambda s: s[s.find('<div class="rows">'):s.find('</section>', s.find('<div class="rows">'))]
rb, rn = len(re.findall(r'data-status="', rows(b))), len(re.findall(r'data-status="', rows(n)))
if rb != rn:
    fails.append(f'row statements: baseline {rb}, new {rn}')
navb = re.findall(r'<nav class="nav".*?</nav>', b, re.S)[0]
navn = re.findall(r'<nav class="nav".*?</nav>', n, re.S)[0]
if navb != navn:
    fails.append('bar navigation changed')
print(f'hooks: {len(hooks)} checked')

# 5. Ids.
idb, idn = set(re.findall(r'\sid="([^"]+)"', b)), set(re.findall(r'\sid="([^"]+)"', n))
if idb - idn:
    fails.append(f'ids lost: {sorted(idb - idn)[:10]}')
print(f'ids: baseline {len(idb)}, new {len(idn)}, added {len(idn - idb)}')

for f in fails:
    print('FAIL', f)
print('PASS' if not fails else f'{len(fails)} failure(s)')
sys.exit(1 if fails else 0)
