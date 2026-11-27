"""Builds small content variants with a given builder and checks what the reader would get (no browser).
Usage: python -I -B qh-builder-fixtures.py <builder script> <work folder> [--out result.json]
Each fixture copies content/quantum-holography-status (content.json, essay.md, page.json), changes one thing, builds
with --no-fonts into <work folder>/<fixture>/, and checks the built page or the build's refusal.
Writes only under <work folder> and --out.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

builder, work = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
SRC = Path('content/quantum-holography-status')
PY = sys.executable


def variant(name, change):
    d = work / name / 'input'
    shutil.rmtree(work / name, ignore_errors=True)
    d.mkdir(parents=True)
    for f in ('content.json', 'essay.md', 'page.json'):
        shutil.copyfile(SRC / f, d / f)
    c = json.loads((d / 'content.json').read_text(encoding='utf-8'))
    essay = (d / 'essay.md').read_text(encoding='utf-8')
    c, essay = change(c, essay)
    (d / 'content.json').write_text(json.dumps(c, ensure_ascii=False), encoding='utf-8')
    (d / 'essay.md').write_text(essay, encoding='utf-8')
    page = work / name / 'page.html'
    r = subprocess.run([PY, '-B', str(builder), '--no-fonts', '--allow-draft', '--input', str(d), '--output', str(page),
                        '--audit-dir', str(work / name / 'audit')], capture_output=True, text=True)
    report = (work / name / 'audit' / 'audit.txt').read_text(encoding='utf-8') if (work / name / 'audit' / 'audit.txt').exists() else r.stdout + r.stderr
    html = page.read_text(encoding='utf-8') if page.exists() else ''
    return report, html


def essay_change(c, essay):
    essay = essay.rstrip() + ('\n\n\\(c=26\\)\n\nThe *-algebra structure on a C* algebra is unique.\n\n'
                              'See [the notes](https://example.org/notes.pdf) for details.\n')
    return c, essay


def names_change(c, essay):
    c['rows'][5]['name'] = '\\(\\mathfrak{sl}_2\\)-modules and \\(\\widehat{\\mathfrak g}\\) at level \\(k\\)'
    return c, essay


def ids_order(first_explicit):
    def change(c, essay):
        a = {'term': 'Weak module', 'forms': ['weak modulus'], 'definition': 'A test entry without an id.'}
        b = {'id': 'weak-module', 'term': 'Weak module (completed)', 'forms': ['completed weak modulus'], 'definition': 'A test entry with an id.'}
        c['glossary'] = c['glossary'] + ([b, a] if first_explicit else [a, b])
        return c, essay
    return change


def ids_duplicate(c, essay):
    c['glossary'] = c['glossary'] + [{'id': 'x-term', 'term': 'Test one', 'forms': [], 'definition': 'One.'},
                                     {'id': 'x-term', 'term': 'Test two', 'forms': [], 'definition': 'Two.'}]
    return c, essay


def open_h(c, essay):
    c['open'][0]['id'] = 'h'
    return c, essay


def names_scripts(c, essay):
    c['rows'][1]['name'] = 'Lattices of type \\(E_8\\) and \\(C_2\\)'
    c['rows'][2]['name'] = 'Sigma models on \\(T^2\\) and the projective line \\(P^1\\)'
    return c, essay


def columns_tex(c, essay):
    c['columns'][1]['name'] = 'Modules over \\(\\mathfrak{g}\\)'
    c['columns'][2]['short'] = '\\(\\hbar\\)-bulk'
    return c, essay


def essay_title_tex(c, essay):
    lines = essay.split('\n')
    lines[0] = '# Ordered composition at \\(c=26\\)'
    return c, '\n'.join(lines)


def glossary_anchor_taken(c, essay):
    c['glossary'] = c['glossary'] + [{'id': 'strong-cut-coalgebra', 'term': 'Test entry', 'forms': [],
                                      'definition': 'An entry whose id is another entry\'s natural anchor.'}]
    return c, essay


def mathrm_digits(c, essay):
    c['principal'][0]['text'] = c['principal'][0]['text'] + ' Compare \\(\\mathrm{T15}\\).'
    return c, essay


def title_angles(c, essay):
    c['title'] = 'Bounds \\(a<b\\) and \\(c>d\\)'
    return c, essay


def open_and_glossary_ids(c, essay):
    c['open'][0]['id'] = 'growth-of-the-programme'
    c['glossary'][0]['id'] = 'consecutive-cut'
    return c, essay


SCOPED_NEGATIVE = {'id': 'scoped-negative-fixture', 'status': 'refuted form', 'title': 'A scoped negative result (fixture)',
                   'text': 'In this fixture the comparison fails for \\(k\\neq 0\\).',
                   'hypotheses': ['the level \\(k\\) is generic', 'the module has finite length']}


def refuted_form(c, essay):
    c['rows'][0]['statements'] = c['rows'][0]['statements'] + [dict(SCOPED_NEGATIVE)]
    c['principal'] = c['principal'] + [dict(SCOPED_NEGATIVE, id='scoped-negative-principal')]
    return c, essay


def refuted_inexact(c, essay):
    c['rows'][0]['statements'] = c['rows'][0]['statements'] + [dict(SCOPED_NEGATIVE, status='refuted')]
    return c, essay


def hypotheses_malformed(c, essay):
    c['rows'][0]['statements'] = c['rows'][0]['statements'] + [dict(SCOPED_NEGATIVE, hypotheses='the level is generic')]
    return c, essay


def refuted_unscoped(c, essay):
    s = dict(SCOPED_NEGATIVE)
    s.pop('hypotheses')
    c['rows'][0]['statements'] = c['rows'][0]['statements'] + [s]
    return c, essay


def refuted_principal_only(c, essay):
    c['principal'] = c['principal'] + [dict(SCOPED_NEGATIVE, id='scoped-negative-principal')]
    return c, essay


def short_label(c, essay):
    c['rows'][0]['short'] = 'Heisenberg'
    return c, essay


results = {}


def check(name, ok, observed):
    results[name] = {'pass': ok, 'observed': observed}
    print(f"{'PASS' if ok else 'FAIL'} {name} {json.dumps(observed, ensure_ascii=False)[:300]}")


rep, html = variant('essay', essay_change)
essay_html = html[html.find('id="essay"'):html.find('id="terms"')]
paras = re.findall(r'<p(?: class="[^"]*")?>(.*?)</p>', essay_html, flags=re.S)
short = [p for p in paras if 'c=26' in p or ('<math' in p and '26' in p and len(re.sub(r'<[^>]+>', '', p)) < 40)]
star = [p for p in paras if 'C*' in p or 'C</em>' in p or '-algebra structure' in p]
link = [p for p in paras if 'the notes' in p]
check('A2-A2-01 essay short display formula is mathematics',
      'PASS' in rep and bool(short) and '<math' in short[0] and '\\(' not in short[0],
      {'audit_pass': 'PASS' in rep, 'paragraph': short[0][:160] if short else None})
check('A2-A2-11 essay asterisks and links stay as written',
      bool(star) and '<em>' not in star[0] and bool(link) and 'https://example.org/notes.pdf' in link[0],
      {'asterisk_paragraph': star[0][:120] if star else None, 'link_paragraph': link[0][:120] if link else None})

rep, html = variant('names', names_change)
labels = re.findall(r'aria-label="([^"]*)"', html)
row_labels = [l for l in labels if 'at level' in l]
titles = [t for t in re.findall(r'title="([^"]*)"', html) if 'at level' in t]
check('A2-A2-02 TeX-command names build and are spoken without TeX',
      'PASS' in rep and len(row_labels) == 8 and all('\\' not in l for l in row_labels + titles),
      {'audit_pass': 'PASS' in rep, 'labels': len(row_labels), 'sample': row_labels[:1], 'title': titles[:1]})

anchors = {}
for first in (False, True):
    rep, html = variant(f'ids-order-{"explicit-first" if first else "explicit-last"}', ids_order(first))
    m = re.search(r'<div class="gloss" id="([^"]+)"><dt>Weak module \(completed\)</dt>', html)
    anchors[first] = m.group(1) if m else None
check('A2-A2-03 an explicit glossary id keeps its anchor in either order',
      anchors[False] == anchors[True] == 'term-weak-module', {'explicit_last': anchors[False], 'explicit_first': anchors[True]})

rep, html = variant('ids-duplicate', ids_duplicate)
check('A2-A2-03 two equal explicit glossary ids fail the build with a named problem',
      'FAIL' in rep and 'two entries have the id anchor term-x-term' in rep, {'fails': 'FAIL' in rep, 'named': 'term-x-term' in rep})

rep, html = variant('open-h', open_h)
check('A2-A2-03 an open-group id that takes the section heading anchor fails with a named problem',
      'FAIL' in rep and 'anchor open-h is already used' in rep, {'fails': 'FAIL' in rep, 'named': 'open-h is already used' in rep})

# Cycle 3 (R3-F): A3-F-01 scripts in names, A3-F-07 TeX in column names and the essay title, A3-F-08 an explicit id
# that takes another entry's anchor, A3-F-05 letters and digits in \\mathrm{}, A3-F-09 angle brackets in the title.
rep, html = variant('names-scripts', names_scripts)
labels = [l for l in re.findall(r'aria-label="([^"]*)"', html) if 'Lattices of type' in l or 'Sigma models on' in l]
spoken = ' | '.join(labels)
check('A3-F-01 names with scripts build and keep the script relation in their text form',
      'PASS' in rep and all(t in spoken for t in ('E_8', 'C_2', 'T^2', 'P^1')) and '\\' not in spoken,
      {'audit_pass': 'PASS' in rep, 'labels': len(labels), 'sample': labels[:2]})

rep, html = variant('columns-tex', columns_tex)
heads = re.findall(r'<button type="button" class="col-head" data-col="(?:dual|modules)"[^>]*>(.*?)</button>', html, flags=re.S)
dts = re.findall(r'<div class="col-def" id="col-dual"><dt>(.*?)</dt>', html, flags=re.S)
check('A3-F-07 TeX in a column name and a short label is set as mathematics',
      'PASS' in rep and len(heads) == 2 and all('<math' in h and '\\(' not in h for h in heads)
      and bool(dts) and '<math' in dts[0],
      {'audit_pass': 'PASS' in rep, 'heads_with_math': sum('<math' in h for h in heads), 'dt': dts[0][:80] if dts else None})

rep, html = variant('essay-title-tex', essay_title_tex)
t = re.search(r'<h3 id="essay-title" class="essay-title">(.*?)</h3>', html, flags=re.S)
check('A3-F-07 TeX in the essay title is set as mathematics',
      'PASS' in rep and bool(t) and '<math' in t.group(1) and '\\(' not in t.group(1),
      {'audit_pass': 'PASS' in rep, 'title': t.group(1)[:80] if t else None})

rep, html = variant('glossary-anchor-taken', glossary_anchor_taken)
check('A3-F-08 an explicit id that takes another entry\'s anchor fails with a named problem',
      'FAIL' in rep and 'term-strong-cut-coalgebra of the term "Strong cut coalgebra" is taken' in rep,
      {'fails': 'FAIL' in rep, 'named': 'is taken by another' in rep})

rep, html = variant('mathrm-digits', mathrm_digits)
check('A3-F-05 a \\mathrm group whose digits the renderer drops fails with a named problem',
      'FAIL' in rep and '\\mathrm{T15} would lose digits' in rep and '\\mathrm{M}_{24}' in rep,
      {'fails': 'FAIL' in rep, 'named': '\\mathrm{T15} would lose digits' in rep})

rep, html = variant('title-angles', title_angles)
head_title = re.search(r'<title>(.*?)</title>', html, flags=re.S)
og = re.search(r'<meta property="og:title" content="([^"]*)"', html)
import html as _h
check('A3-F-09 the head title keeps text between angle brackets',
      'PASS' in rep and bool(head_title) and 'a<b' in _h.unescape(head_title.group(1)) and 'c>d' in _h.unescape(head_title.group(1)),
      {'audit_pass': 'PASS' in rep, 'title': _h.unescape(head_title.group(1)) if head_title else None,
       'og_title': _h.unescape(og.group(1)) if og else None})

# R3-F A4-F-05: a row with a short label; the grid shows the short label, the marks keep the full name.
rep, html = variant('short-label', short_label)
head = re.search(r'<th scope="row"[^>]*>(.*?)</th>', html, flags=re.S)
marks = [l for l in re.findall(r'aria-label="([^"]*)"', html) if l.startswith('Heisenberg, free fields')]
check('A4-F-05 a row with a short label builds; the marks keep the full name (qh-static Q07 runs on this page)',
      'PASS' in rep and bool(head) and len(marks) == 8,
      {'audit_pass': 'PASS' in rep, 'header': re.sub(r'<[^>]+>', '', head.group(1))[:60] if head else None, 'marks_full_name': len(marks)})

# C19 and A3-F-12: explicit open-group and glossary ids give their anchors (qh-static Q09 and Q10 run on this page).
rep, html = variant('open-id', open_and_glossary_ids)
check('C19 explicit open-group and glossary ids give their anchors (qh-static runs on this page)',
      'PASS' in rep and 'id="open-growth-of-the-programme"' in html and 'id="term-consecutive-cut"' in html,
      {'audit_pass': 'PASS' in rep, 'open_anchor': 'id="open-growth-of-the-programme"' in html,
       'term_anchor': 'id="term-consecutive-cut"' in html})

# The status contract: 'refuted form' (atlas scoped_negative) is a statement status with hypotheses, never coerced.
rep, html = variant('refuted-form', refuted_form)
arts = re.findall(r'<article class="statement st-refuted-form" data-status="refuted form" id="s-scoped-negative-[a-z]+">(.*?)</article>', html, flags=re.S)
REFUTED_LABEL = json.loads((SRC / 'page.json').read_text(encoding='utf-8'))['status_labels']['refuted form']  # the label in use
chips = [a for a in arts if REFUTED_LABEL in a and 'mark-refuted-form' in a]
# Hypotheses list under either class name (statement-hypotheses, or statement-hyp in the foundation's markup).
hyps = [len(re.findall(r'<li>', re.split(r'class="statement-hyp(?:otheses)?"', a, maxsplit=1)[1].split('</ul>', 1)[0]))
        if re.search(r'class="statement-hyp(?:otheses)?"', a) else 0 for a in arts]
# A tally pill for the status; its count is checked where the pill shows one.
pill = re.search(r'<a href="#examples" data-filter="refuted form">(.*?)</a>', html, flags=re.S)
count = re.search(r'<span class="count">(\d+)</span>', pill.group(1)) if pill else None
open_tally = re.search(r'<a href="#examples" data-filter="open">(?:(?!</a>).)*?<span class="count">(\d+)</span>', html, flags=re.S)
base_html = (work / 'essay' / 'page.html').read_text(encoding='utf-8')  # same statements as the content, other essay
base_open = re.search(r'<a href="#examples" data-filter="open">(?:(?!</a>).)*?<span class="count">(\d+)</span>', base_html, flags=re.S)
# Statements drawn as open (the open count must not change when 'refuted form' statements are added).
open_cards = len(re.findall(r'<article class="statement st-open[ "]', html))
base_open_cards = len(re.findall(r'<article class="statement st-open[ "]', base_html))
filt = re.search(r'<button type="button" class="filter" data-filter="refuted form" aria-pressed="false">.*?<span>' + re.escape(REFUTED_LABEL) + r'</span></button>', html, flags=re.S)
check("status contract: 'refuted form' statements build, keep their status, chip, mark and hypotheses, and are counted and filterable",
      'PASS' in rep and len(arts) == 2 and len(chips) == 2 and hyps == [2, 2] and '<math' in re.split(r'class="statement-hyp(?:otheses)?"', arts[0], maxsplit=1)[1]
      and bool(pill) and (count is None or count.group(1) == '2') and bool(filt)
      and open_cards == base_open_cards and (not open_tally or not base_open or open_tally.group(1) == base_open.group(1)),
      {'audit_pass': 'PASS' in rep, 'articles': len(arts), 'chips': len(chips), 'hypotheses': hyps,
       'tally_pill': bool(pill), 'tally_count': count.group(1) if count else None, 'filter': bool(filt), 'open_tally': open_tally.group(1) if open_tally else None,
       'open_tally_without_fixture': base_open.group(1) if base_open else None, 'open_cards': open_cards,
       'open_cards_without_fixture': base_open_cards})

rep, html = variant('refuted-inexact', refuted_inexact)
draft = re.search(r'<article class="statement st-([a-z-]+)" data-status="refuted" id="s-scoped-negative-fixture">', html)
check("status contract: an inexact status ('refuted') fails the build and is never shown as open",
      'FAIL' in rep and "unknown statement status 'refuted'" in rep and bool(draft) and draft.group(1) == 'unknown',
      {'fails': 'FAIL' in rep, 'named': "unknown statement status 'refuted'" in rep, 'draft_class': draft.group(1) if draft else None})

rep, html = variant('hypotheses-malformed', hypotheses_malformed)
check('status contract: hypotheses that are not a list of texts fail the build with a named problem',
      'FAIL' in rep and 'hypotheses must be a list of non-empty texts' in rep,
      {'fails': 'FAIL' in rep, 'named': 'hypotheses must be a list of non-empty texts' in rep})

rep, html = variant('refuted-unscoped', refuted_unscoped)
check("status contract: a 'refuted form' statement without hypotheses fails the build (explicit scope is mandatory)",
      'FAIL' in rep and "states no hypotheses: a scoped negative result must give its scope" in rep,
      {'fails': 'FAIL' in rep, 'named': 'states no hypotheses' in rep})

rep, html = variant('refuted-principal-only', refuted_principal_only)
row_filter = re.search(r'<button type="button" class="filter" data-filter="refuted form"', html)
pill = re.search(r'<a href="#examples" data-filter="refuted form">(.*?)</a>', html, flags=re.S)
count = re.search(r'<span class="count">(\d+)</span>', pill.group(1)) if pill else None
check("A7-V-04 a status used only outside the example rows has a tally pill but no row filter",
      'PASS' in rep and not row_filter and bool(pill) and (count is None or count.group(1) == '1'),
      {'audit_pass': 'PASS' in rep, 'row_filter': bool(row_filter), 'pill': bool(pill), 'count': count.group(1) if count else None})

ok = all(r['pass'] for r in results.values())
print('ALL PASS' if ok else 'NOT ALL PASS')
if out:
    Path(out).write_text(json.dumps({'builder': str(builder), 'results': results, 'all_pass': ok}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
