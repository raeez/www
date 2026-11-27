#!/usr/bin/env python3
"""Atlas mount test (EVALUATION-PLAN.md E16). Run from the repository root:

    /tmp/qh-tracker-build-20261116-venv/bin/python -B materials/processed/qh-attack-heal-20261116/foundation/tests/atlas/atlas_test.py

Builds the page three ways with no fonts, through status.Build directly (the production build script is
unchanged): (1) the real input folder, no atlas.json -> no atlas section; (2) the fixture folder with
atlas.json and the stub renderer -> one atlas section, the first after the overview and before #results, a nav item,
the renderer's css and js, statement links resolved, audit clean; (3) atlas.json with a missing renderer
-> a build failure. Writes the fixture page to tests/atlas/out/ for inspection.
"""
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
PAGE = json.loads((ROOT / 'content' / 'quantum-holography-status' / 'page.json').read_text(encoding='utf-8'))
results = []


def check(name, ok, detail=''):
    results.append((name, bool(ok), detail))


# 1. No atlas data.
b = status.Build(ROOT / 'content' / 'quantum-holography-status', PAGE, {}, None, atlas_module=HERE / 'stub_atlas.py')
m = b.run()
a = audit.run(b, m)
check('no atlas.json: no atlas section', 'data-atlas-mount' not in m and 'id="atlas"' not in m)
check('no atlas.json: no nav item', 'href="#atlas"' not in m)
check('no atlas.json: audit clean', not a['failures'], a['failures'][:3])

# 2. Fixture data with the stub renderer.
b = status.Build(HERE / 'input', PAGE, {}, None, atlas_module=HERE / 'stub_atlas.py')
m = b.run()
a = audit.run(b, m)
out = HERE / 'out'
out.mkdir(exist_ok=True)
(out / 'atlas-fixture.html').write_text(m, encoding='utf-8')
main = m[m.find('<main'):m.find('</main>')]
order = [x for x in re.findall(r'<(?:section|header|aside) id="([^"]+)"', main)]
check('fixture: one atlas section', m.count('data-atlas-mount') == 1)
sections = [x for x in order if x not in ('programme', 'changes')]
check('fixture: atlas the first section after the overview, then #results',
      sections[:2] == ['atlas', 'results'], order)
atlas_part = m[m.find('<section id="atlas"'):m.find('</section>', m.find('<section id="atlas"'))]
check('fixture: a scoped_negative claim carries the refuted-form mark (never open)',
      re.search(r'data-claim="fixture-scoped-negative-claim"><svg class="mark mark-refuted-form"', atlas_part) is not None)
nav = m[m.find('<nav class="nav"'):m.find('</nav>', m.find('<nav class="nav"'))]
check('fixture: nav item after Programme', re.search(r'href="#programme".*?href="#atlas"', nav) is not None)
check('fixture: renderer css embedded before the print sheet',
      '.atlas-fixture{border-top' in m and m.find('.atlas-fixture{border-top') < m.find('Print. Embedded after status.css'))
check('fixture: renderer js in its own script after the page script', re.search(r'</script>\n<script>window.__atlasFixtureRan = true;', m) is not None)
check('fixture: statement link resolved through ctx.anchor_for', 'href="#s-hyperbolic-siegel-weil"' in main)
check('fixture: unknown claim left unlinked', 'data-claim="fixture-claim-two">' in main and 'href="#s-fixture-claim-two"' not in main)
check('fixture: TeX in atlas text rendered as MathML', re.search(r'Placeholder summary B with (<span class="nobr">)?<span class="math-inline"><math', main) is not None)
check('fixture: audit clean', not a['failures'], a['failures'][:3])

# 2b. An atlas status code the page does not know is refused (a build problem), not drawn as open.
unk = HERE / 'input-unknown-code'
unk.mkdir(exist_ok=True)
for name in ('content.json', 'essay.md'):
    (unk / name).write_text((ROOT / 'content' / 'quantum-holography-status' / name).read_text(encoding='utf-8'), encoding='utf-8')
fx = json.loads((HERE / 'input' / 'atlas.json').read_text(encoding='utf-8'))
fx['claims'][0]['status'] = {'code': 'not_a_status', 'label': 'Placeholder unknown'}
(unk / 'atlas.json').write_text(json.dumps(fx, ensure_ascii=False), encoding='utf-8')
b = status.Build(unk, PAGE, {}, None, atlas_module=HERE / 'stub_atlas.py')
a = audit.run(b, b.run())
check('fixture: an unknown atlas status code is a build failure', any('unknown status code' in f for f in a['failures']), a['failures'][:2])

# 3. Data without a renderer.
b = status.Build(HERE / 'input', PAGE, {}, None, atlas_module=HERE / 'missing_atlas.py')
m = b.run()
a = audit.run(b, m)
check('atlas.json without renderer: build failure', any('no atlas renderer' in f for f in a['failures']), a['failures'][:2])

# 4. Hardening: assets that would close their element, and page classes in the atlas markup.
b = status.Build(HERE / 'input', PAGE, {}, None, atlas_module=HERE / 'stub_atlas_bad_assets.py')
a = audit.run(b, b.run())
check('atlas js with a closing script tag: build failure', any('closing </script' in f for f in a['failures']), a['failures'][:2])
b = status.Build(HERE / 'input', PAGE, {}, None, atlas_module=HERE / 'stub_atlas_bad_class.py')
a = audit.run(b, b.run())
check('atlas markup with a reserved page class: build failure', any('classes that the page script binds: statement' in f for f in a['failures']), a['failures'][:2])

# 5. Text through ctx.rich() (a glossary term, a long formula, display math) and a question link are accepted.
b = status.Build(HERE / 'input', PAGE, {}, None, atlas_module=HERE / 'stub_atlas_rich.py')
m = b.run()
a = audit.run(b, m)
sec = m[m.find('data-atlas-mount'):m.find('</section>', m.find('data-atlas-mount'))]
check('ctx.rich output with a term, a long formula and display math: no build failure', not a['failures'], a['failures'][:3])
check('the atlas section holds the term button, the long formula and the display formula',
      'class="term"' in sec and 'math-long' in sec and 'class="math-display"' in sec)
check('ctx.question_anchor resolves a question card', 'href="#q-d-native-interface"' in sec)

ok = all(r[1] for r in results)
for name, passed, detail in results:
    print(('PASS ' if passed else 'FAIL ') + name + ('' if passed else f' — {detail}'))
print('ALL PASS' if ok else 'ATLAS MOUNT FAILURES')
sys.exit(0 if ok else 1)
