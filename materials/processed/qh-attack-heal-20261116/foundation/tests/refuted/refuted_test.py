#!/usr/bin/env python3
"""Statement status 'refuted form' (a checked scoped negative result; the atlas's scoped_negative). Run from the
repository root:

    /tmp/qh-tracker-build-20261116-venv/bin/python -B materials/processed/qh-attack-heal-20261116/foundation/tests/refuted/refuted_test.py

Builds a fixture copy of the content (written to tests/refuted/input/, never to content/) in which one family
statement (with hypotheses and novelty) and one related statement of a decisive question carry the status
'refuted form'. Checks that the status is kept (never read as open) in the article, its chip, its mark and colour,
its hypotheses and novelty, the related line (status words visible), the overview's status line, the family
filters, the build audit, the completeness check and the static contract; and that a misspelt status still fails
the audit. The fixture statements are placeholders for the renderer, not programme content."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'compiler' / 'quantum-holography-status'))
import audit  # noqa: E402
import status  # noqa: E402

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent.parent / 'tools'
src = ROOT / 'content' / 'quantum-holography-status'
PAGE = json.loads((src / 'page.json').read_text(encoding='utf-8'))
results = []


def check(name, ok, detail=''):
    results.append((name, bool(ok), detail))


def fixture(folder, row_status, known_status, drop_key=False):
    c = json.loads((src / 'content.json').read_text(encoding='utf-8'))
    if drop_key:
        c['status_key'] = [k for k in c['status_key'] if k.get('status') != 'refuted form']
    c['rows'][0]['statements'].append({
        'status': row_status, 'id': 'fixture-scoped-negative', 'title': 'The comparison as first posed',
        'text': 'The comparison map is not an equivalence on the whole category; it is one on the stated subcategory.',
        'hypotheses': ['Coefficients in a field of characteristic zero.', 'Inputs of finite length.'],
        'novelty': 'new', 'antecedents': '', 'cite': '', 'source': []})
    c['decisive']['questions'][0]['known'].append({
        'status': known_status, 'id': 'fixture-scoped-negative-related', 'title': 'The first-posed form fails',
        'text': 'The first-posed form of the comparison fails on the completed inputs.', 'source': []})
    folder.mkdir(exist_ok=True)
    (folder / 'content.json').write_text(json.dumps(c, ensure_ascii=False), encoding='utf-8')
    (folder / 'essay.md').write_text((src / 'essay.md').read_text(encoding='utf-8'), encoding='utf-8')
    (folder / 'page.json').write_text(json.dumps(PAGE, ensure_ascii=False), encoding='utf-8')
    b = status.Build(folder, PAGE, {}, None)
    m = b.run()
    return b, m, audit.run(b, m)


label = PAGE['status_labels']['refuted form']
b, m, a = fixture(HERE / 'input', 'refuted form', 'refuted form')
out = HERE / 'out'
out.mkdir(exist_ok=True)
(out / 'refuted-fixture.html').write_text(m, encoding='utf-8')
check('statement status list holds refuted form', 'refuted form' in status.STATEMENT_STATUSES)
check('build: no problems', not b.problems, b.problems[:3])
check('audit clean', not a['failures'], a['failures'][:3])
art = re.search(r'<article class="([^"]*)" data-status="([^"]*)" id="s-fixture-scoped-negative">(.*?)</article>', m, re.S)
check('family statement keeps the status (article)', art and art.group(2) == 'refuted form' and 'st-refuted-form' in art.group(1).split(),
      art.group(1, 2) if art else 'missing')
body = art.group(3) if art else ''
check('its chip names the status, with the cross mark',
      f'<span class="status-chip chip-refuted-form"><svg class="mark mark-refuted-form"' in body and f'<span>{label}</span>' in body)
check('its hypotheses are listed before the text', body.find('class="statement-hyp"') >= 0 and
      body.find('class="statement-hyp"') < body.find('class="statement-text"') and body.count('<li>') == 2)
check('its novelty is shown', PAGE['novelty_labels']['new'] in body)
rel = re.search(r'<summary class="fold-head">(?:(?!</summary>).)*</summary><article class="[^"]*" data-status="refuted form" '
                r'id="s-fixture-scoped-negative-related">', m, re.S)
check('related statement keeps the status, its words visible on the line',
      rel and f'<span class="fold-status">{label}</span>' in rel.group(0) and 'mark-refuted-form' in rel.group(0))
check('overview status line lists it', f'data-filter="refuted form"' in m[m.find('<nav class="tally"'):m.find('</nav>', m.find('<nav class="tally"'))])
check('family filters offer it', re.search(r'<button[^>]*class="filter[^"]*"[^>]*data-filter="refuted form"', m) is not None
      or re.search(r'data-filter="refuted form"[^>]*class="filter', m) is not None)
css = (ROOT / 'compiler' / 'quantum-holography-status' / 'status.css').read_text(encoding='utf-8')
check('stylesheet colours the status', '.st-refuted-form { --st: var(--st-refuted-form); }' in css)
r = subprocess.run([sys.executable, '-I', '-B', str(TOOLS / 'completeness.py'), str(HERE / 'input'), str(out / 'refuted-fixture.html')],
                   capture_output=True, text=True, cwd=ROOT)
check('completeness on the fixture', r.returncode == 0, [x for x in r.stdout.splitlines() if x.startswith('FAIL')][:3])
r = subprocess.run([sys.executable, '-I', '-B', str(TOOLS / 'contract_static.py'), str(out / 'refuted-fixture.html'), '--candidate'],
                   capture_output=True, text=True, cwd=ROOT)
check('static contract on the fixture', r.returncode == 0, [x for x in r.stdout.splitlines() if x.startswith('FAIL')][:3])

# A misspelt status is still refused, and the page it writes shows the value as it is, never as open.
b2, m2, a2 = fixture(HERE / 'input-misspelt', 'refuted', 'refuted form')
check('a misspelt status fails the audit (not read as open silently)',
      any('refuted' in f and 'status' in f for f in a2['failures']) or any("'refuted'" in p for p in b2.problems),
      (a2['failures'] + b2.problems)[:3])
bad = re.search(r'<article class="([^"]*)" data-status="([^"]*)" id="s-fixture-scoped-negative">(.*?)</div>', m2, re.S)
check('the misspelt value is shown as itself, without a mark (not as open)',
      bad and bad.group(2) == 'refuted' and 'st-unknown' in bad.group(1).split() and '<span>refuted</span>' in bad.group(3)
      and 'mark-open' not in bad.group(3) and PAGE['status_labels']['open'] not in bad.group(3), bad.group(1, 2) if bad else 'missing')

# A statement status used on the page but absent from the content's key fails the build (the key explains every status).
b3, m3, a3 = fixture(HERE / 'input-nokey', 'refuted form', 'refuted form', drop_key=True)
check('a status without a key entry fails the build', any('status_key' in p and 'refuted form' in p for p in b3.problems), b3.problems[:3])
check('the same rule holds for the table: a cell status without a key entry fails the build (no page wording of its own)',
      any(p.startswith("status key: the table uses 'refuted form'") for p in b3.problems), b3.problems[:3])

# A status held only outside the families: listed in the overview's status line, not offered as a family filter.
b4, m4, a4 = fixture(HERE / 'input-related-only', 'checked', 'refuted form')
tally4 = m4[m4.find('<nav class="tally"'):m4.find('</nav>', m4.find('<nav class="tally"'))]
tools4 = m4[m4.find('<div class="row-tools">'):m4.find('<div class="row-actions">')]
check('a status only in related statements: in the status line, not a family filter',
      'data-filter="refuted form"' in tally4 and 'data-filter="refuted form"' not in tools4 and not a4['failures'], a4['failures'][:2])

for name, ok, detail in results:
    print(('PASS ' if ok else 'FAIL ') + name + (f' — {detail}' if (detail and not ok) else ''))
print('ALL PASS' if all(r[1] for r in results) else 'FAILURES')
sys.exit(0 if all(r[1] for r in results) else 1)
