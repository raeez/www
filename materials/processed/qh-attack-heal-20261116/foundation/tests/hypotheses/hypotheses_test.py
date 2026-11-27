#!/usr/bin/env python3
"""Hypotheses slot test. Run from the repository root:

    /tmp/qh-tracker-build-20261116-venv/bin/python -B materials/processed/qh-attack-heal-20261116/foundation/tests/hypotheses/hypotheses_test.py

Builds a fixture copy of the content (written to tests/hypotheses/input/, never to content/) in which one
principal statement and one related statement carry a placeholder 'hypotheses' list, and checks that each
renders as a labelled list before the statement text, that the build and audit stay clean, and that a
statement without the field renders no list."""
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'compiler' / 'quantum-holography-status'))
import audit  # noqa: E402
import status  # noqa: E402

HERE = Path(__file__).resolve().parent
src = ROOT / 'content' / 'quantum-holography-status'
c = json.loads((src / 'content.json').read_text(encoding='utf-8'))
c['principal'][0]['hypotheses'] = ['Placeholder hypothesis A.', 'Placeholder hypothesis with \\(x^2\\).']
known = c['decisive']['questions'][0]['known'][0]
known['hypotheses'] = ['Placeholder hypothesis C.']
inp = HERE / 'input'
inp.mkdir(exist_ok=True)
(inp / 'content.json').write_text(json.dumps(c, ensure_ascii=False), encoding='utf-8')
(inp / 'essay.md').write_text((src / 'essay.md').read_text(encoding='utf-8'), encoding='utf-8')
page = json.loads((src / 'page.json').read_text(encoding='utf-8'))
b = status.Build(inp, page, {}, None)
m = b.run()
a = audit.run(b, m)
ok = True


def check(name, cond, detail=''):
    global ok
    ok &= bool(cond)
    print(('PASS ' if cond else 'FAIL ') + name + ('' if cond else f' — {detail}'))


blocks = re.findall(r'<div class="statement-hyp">(.*?)</div><div class="statement-text">', m, re.S)
check('two statements carry a hypotheses list', len(blocks) == 2, len(blocks))
check('the label comes from page.json', all(f'>{page["labels"]["hypotheses"]}<' in x for x in blocks))
check('list items: 2 and 1', sorted(x.count('<li>') for x in blocks) == [1, 2], [x.count('<li>') for x in blocks])
check('TeX in a hypothesis is MathML', any('<math' in x for x in blocks))
check('the related statement keeps its anchor', f'id="s-{status.ident(known["id"])}"' in m)
check('audit clean', not a['failures'], a['failures'][:3])
print('ALL PASS' if ok else 'HYPOTHESES FAILURES')
sys.exit(0 if ok else 1)
