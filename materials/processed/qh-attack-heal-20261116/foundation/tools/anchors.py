#!/usr/bin/env python3
"""Stable anchors of a reference page kept by a candidate page (no browser).

    python3 tools/anchors.py <reference.html> <candidate.html> [--json out.json]

Every id of the reference page is an address a reader may hold (#s-, #q-, #row-, #f-, #open-, #term-, #col- and
the section ids). Fails when any reference id is missing from the candidate, or when a reference statement anchor
(s-*) no longer names a statement. Reports, without failing, the ids the candidate adds and the anchored statements
whose status differs (a content decision for the content owner, listed so that it is seen).
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fidelity import parse  # noqa: E402


def kind(i):
    m = re.match(r'(s|q|row|f|open|term|col)-', i)
    return m.group(1) + '-' if m else 'other'


def info(path):
    root, raw = parse(path)
    ids = re.findall(r'\sid="([^"]+)"', raw)
    stmts = {n.attrs['id']: n.attrs.get('data-status') for n in root.walk()
             if n.tag == 'article' and 'statement' in n.cls() and n.attrs.get('id')}
    return ids, stmts


def main():
    args = sys.argv[1:]
    out_json = None
    if '--json' in args:
        k = args.index('--json')
        out_json = args[k + 1]
        del args[k:k + 2]
    ref_ids, ref_st = info(args[0])
    cand_ids, cand_st = info(args[1])
    ref, cand = set(ref_ids), set(cand_ids)
    missing = sorted(ref - cand)
    not_statement = sorted(i for i in ref_st if i in cand and i not in cand_st)
    added = sorted(cand - ref)
    changed = sorted((i, ref_st[i], cand_st[i]) for i in ref_st if i in cand_st and ref_st[i] != cand_st[i])
    by = Counter(kind(i) for i in ref)
    kept = Counter(kind(i) for i in ref & cand)
    print('reference anchors by kind: ' + ', '.join(f'{k} {kept[k]}/{by[k]}' for k in sorted(by)))
    ok = not missing and not not_statement
    print(('PASS' if not missing else 'FAIL') + f' every reference anchor present — {len(ref)} in the reference, {len(missing)} missing'
          + (f': {missing[:20]}' if missing else ''))
    print(('PASS' if not not_statement else 'FAIL') + f' every reference statement anchor still names a statement'
          + (f' — {len(not_statement)} do not: {not_statement[:20]}' if not_statement else f' — {len(ref_st)} checked'))
    print(f'INFO ids added by the candidate: {len(added)}' + (f' (first: {added[:12]})' if added else ''))
    print(f'INFO anchored statements whose status differs: {len(changed)}' + (f' (first: {changed[:8]})' if changed else ''))
    print('ALL PASS' if ok else 'ANCHOR FAILURES')
    if out_json:
        Path(out_json).write_text(json.dumps({'ok': ok, 'missing': missing, 'not_statement': not_statement,
                                              'added': added, 'status_changed': changed}, indent=1), encoding='utf-8')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
