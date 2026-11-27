#!/usr/bin/env python3
"""Presence of the atlas data in a built page (no browser; agnostic about the atlas markup).

    python3 tools/atlas_presence.py <atlas.json> <page.html> [--json out.json]

The atlas renderer belongs to the atlas lane; this check does not prescribe its markup. For each item of the atlas
(domains, claims, edges, comparisons, reading paths and their stages) it reports where the page carries it:

  shown      its words are in the static markup of section#atlas (text, SVG text, or an accessible name:
             aria-label, title, alt), TeX and MathML set aside; a field counts as shown when at least 90% of its
             four-word runs occur (a field shorter than four words: all of its words, contiguously)
  addressed  not shown, but its id is an attribute value in section#atlas (id, href, data-*)
  embedded   only inside a script element of the page (data drawn by a script at run time; a browser must judge it)
  absent     none of these

Fields per kind: domain label and summary; claim title and statement; edge label and scope (and its source and
target claims must exist); comparison title and overview; reading path title and summary, stage labels.
Fails when section#atlas is missing (the page was built without the atlas), when any item is absent, or when an
edge names a claim the atlas does not have. Exit status 0 when every item is at least embedded.
"""
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fidelity import parse  # noqa: E402

TEX = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]', re.S)
ATTRS = ('aria-label', 'title', 'alt')


def words(text):
    return re.findall(r'\w+', unicodedata.normalize('NFKC', TEX.sub(' ', text or '')).casefold())


def grams(tokens, k):
    return {tuple(tokens[i:i + k]) for i in range(len(tokens) - k + 1)}


def script_words(text):
    """Words of a script: the string values when it is JSON (so escapes do not break runs), else its raw text."""
    try:
        data = json.loads(text)
    except ValueError:
        return words(text)
    out = []

    def rec(v):
        if isinstance(v, str):
            out.extend(words(v))
        elif isinstance(v, dict):
            for x in v.values():
                rec(x)
        elif isinstance(v, list):
            for x in v:
                rec(x)
    rec(data)
    return out


def collect(section):
    """Static tokens of the section (text, SVG text, accessible names), attribute values, and script tokens."""
    stream, values, script = [], set(), []

    def rec(n, in_script):
        for c in n.children:
            if isinstance(c, str):
                if in_script:
                    script.extend(script_words(c))
                else:
                    stream.extend(words(c))
                continue
            if c.tag in ('math', 'style'):
                continue
            for a, v in c.attrs.items():
                if v is None:
                    continue
                if a in ATTRS:
                    stream.extend(words(v))
                if a == 'id' or a == 'href' or a.startswith('data-'):
                    values.update(x.lstrip('#') for x in v.split())
            rec(c, in_script or c.tag == 'script')  # inline markup (a glossary button, emphasis) does not break a run
    rec(section, False)
    return stream, values, script


def present(fields, index):
    """At least 90% of the fields' four-word runs (a field shorter than four words: the whole field) occur."""
    runs = [r for f in fields if f for r in ([tuple(words(f))] if len(words(f)) < 4 else grams(words(f), 4)) if r]
    if not runs:
        return True
    return sum(1 for r in runs if r in index.get(len(r), ())) / len(runs) >= 0.9


def main():
    args = sys.argv[1:]
    out_json = None
    if '--json' in args:
        k = args.index('--json')
        out_json = args[k + 1]
        del args[k:k + 2]
    A = json.loads(Path(args[0]).read_text(encoding='utf-8'))
    root, raw = parse(args[1])
    section = root.first(lambda n: n.tag == 'section' and n.attrs.get('id') == 'atlas')
    if section is None:
        print('FAIL section#atlas missing: the page was built without the atlas')
        return 1
    stream, values, script = collect(section)
    page_scripts = []
    for n in root.walk():
        if n.tag == 'script':
            page_scripts.extend(script_words(''.join(c for c in n.children if isinstance(c, str))))
    index = {k: grams(stream, k) for k in (1, 2, 3, 4)}
    sindex = {k: grams(script + page_scripts, k) for k in (1, 2, 3, 4)}
    claims = {c['id'] for c in A.get('claims', [])}
    kinds = {
        'domains': [(d['id'], [d.get('label'), d.get('summary')]) for d in A.get('domains', [])],
        'claims': [(c['id'], [c.get('title'), c.get('statement')]) for c in A.get('claims', [])],
        'edges': [(e['id'], [e.get('label'), e.get('scope')]) for e in A.get('edges', [])],
        'comparisons': [(k['id'], [k.get('title'), k.get('overview')]) for k in A.get('comparisons', [])],
        'reading paths': [(p['id'], [p.get('title'), p.get('summary')] + [s.get('label') for s in p.get('stages', [])])
                          for p in A.get('readingPaths', [])],
    }
    report, absent = {}, []
    ok = True
    for kind, items in kinds.items():
        tally = Counter()
        for iid, fields in items:
            if present(fields, index):
                where = 'shown'
            elif iid in values:
                where = 'addressed'
            elif present(fields, sindex):
                where = 'embedded'
            else:
                where = 'absent'
                absent.append(f'{kind}: {iid}')
            tally[where] += 1
        report[kind] = dict(tally)
        line = ', '.join(f'{w} {tally[w]}' for w in ('shown', 'addressed', 'embedded', 'absent') if tally[w])
        bad = tally['absent'] > 0
        ok = ok and not bad
        print(('FAIL ' if bad else 'PASS ') + f'{kind}: {len(items)} — {line}')
    dangling = [e['id'] for e in A.get('edges', []) if e.get('source') not in claims or e.get('target') not in claims]
    print(('FAIL ' if dangling else 'PASS ') + f'edges join claims of the atlas — {len(dangling)} dangling' +
          (f': {dangling[:8]}' if dangling else ''))
    ok = ok and not dangling
    if absent:
        print('absent (first 20): ' + '; '.join(absent[:20]))
    print('ALL PASS' if ok else 'ATLAS PRESENCE FAILURES')
    if out_json:
        Path(out_json).write_text(json.dumps({'ok': ok, 'by_kind': report, 'absent': absent, 'dangling_edges': dangling},
                                             indent=1), encoding='utf-8')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
