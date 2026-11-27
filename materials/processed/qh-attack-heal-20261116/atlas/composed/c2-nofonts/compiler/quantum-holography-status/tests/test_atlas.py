"""Tests of the research atlas renderer (atlas.py): validation, reader safety, markup hooks and geometry.

    python3 -B -m unittest discover -s compiler/quantum-holography-status/tests -p 'test_atlas.py' -v

The fixture tests/fixtures/atlas-synthetic.json is synthetic: it exercises the renderer and is never
content of the page. Most tests use a small stand-in for the page's AtlasContext; the last one builds
the whole page through status.Build when status.py provides the atlas mount (AtlasContext), with its
temporary files under $ATLAS_TEST_TMP when that is set.
"""
import copy
import html
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent
sys.path.insert(0, str(SRC))
sys.dont_write_bytecode = True
import atlas  # noqa: E402

FIXTURE = json.loads((HERE / 'fixtures' / 'atlas-synthetic.json').read_text(encoding='utf-8'))
PAGE_HOOKS = set('grid card card-inner term filter row rows row-name statement statement-head statement-title status-chip question '
                 'question-ask known fold failure claim-text open-group col-def gloss theme nav find mark tally math-display '
                 'math-long'.split())
SHARED_HOOKS = {'term', 'math-display', 'math-long'}  # made by the page's own text renderer, shared on purpose


class Ctx:
    """The parts of the page's AtlasContext that the renderer uses."""

    def __init__(self, statements=('hyperbolic-siegel-weil',), anchors=(), labels=None):
        self._statements = set(statements)
        self.anchors = frozenset(anchors)
        self.labels = labels or {}
        self.status_labels = {}

    def rich(self, text, terms=True):
        return html.escape(text or '', quote=False)

    def mark(self, status, label=None):
        return ''

    def anchor_for(self, statement_id):
        return '#s-' + statement_id if statement_id in self._statements else None

    @staticmethod
    def ident(text):
        return text


def errors(data, ctx=None):
    return atlas.validate(data, ctx or Ctx()).errors


def mutated(fn):
    data = copy.deepcopy(FIXTURE)
    fn(data)
    return data


def claim(data, cid):
    return next(c for c in data['claims'] if c['id'] == cid)


class Valid(unittest.TestCase):
    def test_fixture_is_valid_and_renders(self):
        self.assertEqual(errors(FIXTURE), [])
        out = atlas.render(FIXTURE, Ctx())
        self.assertEqual(out['problems'], [])
        for k in ('html', 'css', 'js', 'title', 'kicker', 'nav_label'):
            self.assertTrue(out[k], k)

    def test_invalid_data_renders_nothing(self):
        out = atlas.render(mutated(lambda d: d.update(schema='other')), Ctx())
        self.assertEqual(out['html'], '')
        self.assertTrue(out['problems'])

    def test_comparison_ids_may_be_omitted_and_are_then_derived(self):
        data = mutated(lambda d: claim(d, 'alpha-base').pop('comparisonIds'))
        a = atlas.validate(data, Ctx())
        self.assertEqual(a.errors, [])
        self.assertEqual(a.claim['alpha-base']['comparisonIds'], ['k-alpha'])

    def test_page_labels_replace_interface_words(self):
        out = atlas.render(FIXTURE, Ctx(labels={'atlas': 'Map', 'nav_atlas': 'Map', 'atlas_kicker': 'K', 'atlas_intro': 'Intro words.'}))
        self.assertEqual((out['title'], out['nav_label'], out['kicker']), ('Map', 'Map', 'K'))
        self.assertIn('Intro words.', out['html'])

    def test_ids_already_on_the_page_are_refused(self):
        out = atlas.render(FIXTURE, Ctx(anchors={'atlas-index'}))
        self.assertEqual(out['html'], '')
        self.assertIn('atlas-index', out['problems'][0])


class Negative(unittest.TestCase):
    """Every rule, with the message that names it."""

    def expect(self, data, fragment, ctx=None):
        found = errors(data, ctx)
        self.assertTrue(any(fragment in e for e in found), f'{fragment!r} not in {found}')

    def test_unknown_keys_at_every_level(self):
        self.expect(mutated(lambda d: d.update(sourcePaths=['x'])), "unknown key 'sourcePaths'")
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(binding='x')), "unknown key 'binding'")
        self.expect(mutated(lambda d: d['edges'][0].update(origin='x')), "unknown key 'origin'")
        self.expect(mutated(lambda d: d['readingPaths'][0]['stages'][0].update(note='x')), "unknown key 'note'")
        self.expect(mutated(lambda d: claim(d, 'alpha-base')['status'].update(hash='x')), "unknown key 'hash'")

    def test_missing_keys_and_schema(self):
        self.expect(mutated(lambda d: claim(d, 'alpha-base').pop('statement')), "missing key 'statement'")
        self.expect(mutated(lambda d: d.pop('edges')), "missing key 'edges'")
        self.expect(mutated(lambda d: d.update(schema='programme-scientific-atlas-public/v2')), 'atlas.schema')

    def test_types_are_checked_before_use(self):
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(hypotheses='abc')), 'a list of non-empty strings is required')
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(status='checked')), 'status: an object is required')
        self.expect(mutated(lambda d: d.update(claims={'a': 1})), 'atlas.claims: a list is required')
        self.expect(mutated(lambda d: d['edges'][0].update(source=['alpha-base'])), "no claim with id ['alpha-base']")
        self.expect(mutated(lambda d: d.update(domains=[1])), 'domains[0]: an object is required')
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(title=7)), 'title: a string is required')

    def test_ids(self):
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(id='Alpha Base')), 'is not a lower-case id')
        self.expect(mutated(lambda d: d['claims'].append(copy.deepcopy(claim(d, 'alpha-base')))), "duplicate id 'alpha-base'")
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(id='t12')), "part 't12' of the form of an internal identifier")
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(id='claim-e2')), "part 'e2'")
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(id='da39a3ee5e6b4b0d3255bfef95601890afd80709')), 'hash-like token')

    def test_reader_safety_of_every_string(self):
        for value, why in (('claude_session', 'model or tool name'), ('claim_audit', 'workflow vocabulary'),
                           ('owner_note', 'workflow vocabulary'), ('see notes/plan.md', 'file name'),
                           ('from /Users/someone/x', 'path'), ('by thm:main-result', 'label of the form name:part'),
                           ('50% of cases', 'percentage'), ('https://example.org', 'address of another host'),
                           ('commit 3f9a2c1b', 'hash-like token'), ('the v2 statement', 'version tag')):
            self.expect(mutated(lambda d, v=value: claim(d, 'alpha-base').update(statement='Synthetic ' + v)), why)
        self.expect(mutated(lambda d: d['edges'][0].update(scope='from the ledger')), 'workflow vocabulary')
        self.expect(mutated(lambda d: d['domains'][0].update(id='claude_session')), 'model or tool name')
        self.assertEqual(errors(mutated(lambda d: claim(d, 'alpha-base').update(statement='As in arXiv:2408.07117, \\(50\\%\\).'))), [])

    def test_references(self):
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(domainId='nowhere')), "no domain with id 'nowhere'")
        self.expect(mutated(lambda d: d['edges'][0].update(target='nobody')), "no claim with id 'nobody'")
        self.expect(mutated(lambda d: d['edges'][0].update(target=d['edges'][0]['source'])), 'a claim related to itself')
        self.expect(mutated(lambda d: d['edges'].append(dict(d['edges'][0], id='e-again'))), "a second 'uses' edge")
        self.expect(mutated(lambda d: claim(d, 'beta-linked').update(statementRef='no-such-statement')),
                    "no statement on the page with id 'no-such-statement'")

    def test_typed_vocabulary(self):
        self.expect(mutated(lambda d: d['edges'][1].update(label='uses')), "relation 'uses' is labelled both")
        self.expect(mutated(lambda d: claim(d, 'alpha-lift')['status'].update(label='Another label')), "status 'checked' is labelled both")
        self.expect(mutated(lambda d: claim(d, 'alpha-base')['status'].update(code='proved')), "'proved' is not one of")
        self.expect(mutated(lambda d: d['edges'][0].update(relation='Uses')), 'is not a relation code')

    def test_conditional_claims_name_their_hypotheses(self):
        self.expect(mutated(lambda d: claim(d, 'alpha-conditional').update(hypotheses=[])), 'must list the hypotheses')

    def test_titles_are_unique(self):
        self.expect(mutated(lambda d: claim(d, 'beta-remaining').update(title=claim(d, 'gamma-b')['title'])), 'have the same title')

    def test_comparisons(self):
        self.expect(mutated(lambda d: d['comparisons'][0]['remainingClaimIds'].append('alpha-base')), "is in both establishedClaimIds")
        self.expect(mutated(lambda d: d['comparisons'][0].update(establishedClaimIds=['alpha-base', 'alpha-lift', 'alpha-remaining'],
                                                                 remainingClaimIds=[])), "has status 'remaining', not 'checked'")
        self.expect(mutated(lambda d: d['comparisons'][1].update(establishedClaimIds=[], conditionalClaimIds=[], remainingClaimIds=[])),
                    'lists no claim')
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(comparisonIds=[])), "disagree on whether the claim is in it")
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(comparisonIds=['k-alpha', 'k-none'])), "no comparison with id 'k-none'")

    def test_paths_joined_by_recorded_relations(self):
        self.expect(mutated(lambda d: d['readingPaths'][1]['stages'][1].update(claimIds=['beta-isolated'])),
                    "claim 'beta-isolated' is joined to no claim of stage 1")
        self.expect(mutated(lambda d: d['readingPaths'][1]['stages'][2]['claimIds'].append('beta-isolated')),
                    "claim 'beta-isolated' is joined to no claim of stage 2")
        self.expect(mutated(lambda d: d['readingPaths'][1].update(stages=d['readingPaths'][1]['stages'][:1])), 'needs at least two stages')
        self.expect(mutated(lambda d: d['readingPaths'][1]['stages'][1].update(claimIds=[])), 'needs a claim')
        self.expect(mutated(lambda d: d['readingPaths'][0].update(kind='dependency')), "'dependency' is not one of")
        self.assertEqual(errors(mutated(lambda d: d['readingPaths'][0]['stages'][1].update(claimIds=[]))), [],
                         'an editorial stage may hold no claim')


class Markup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = atlas.render(FIXTURE, Ctx())
        cls.html = cls.out['html']

    def test_quality_hooks(self):
        h = self.html
        ids = re.findall(r'<article class="atlas-claim [^"]*" id="atlas-c-([^"]+)" data-claim-id="([^"]+)" data-status-code="([^"]+)"', h)
        self.assertEqual(sorted((a, b) for a, b, _ in ids), sorted((c['id'], c['id']) for c in FIXTURE['claims']))
        codes = {a: s for a, _, s in ids}
        for c in FIXTURE['claims']:
            self.assertEqual(codes[c['id']], c['status']['code'])
        for e in FIXTURE['edges']:
            hooks = re.findall(rf'data-edge-id="{e["id"]}" data-source="([^"]+)" data-target="([^"]+)" data-relation="([^"]+)"', h)
            self.assertGreaterEqual(len(hooks), 3, e['id'])  # the source's list, the target's list, the map
            self.assertEqual(set(hooks), {(e['source'], e['target'], e['relation'])})
        drawn = re.findall(r'<path class="atlas-edge[^"]*" d="[^"]+" data-edge-id="([^"]+)"', h)
        self.assertEqual(sorted(drawn), sorted(e['id'] for e in FIXTURE['edges']), 'the map draws each edge once and nothing else')
        self.assertEqual(sorted(re.findall(r'data-path-id="([^"]+)" data-path-kind="([^"]+)"', h)),
                         sorted((p['id'], p['kind']) for p in FIXTURE['readingPaths']))
        self.assertEqual(len(re.findall(r'data-claim-id="', h)), len(FIXTURE['claims']), 'data-claim-id marks the claims only')

    def test_statuses_and_hypotheses_are_shown_as_supplied(self):
        for c in FIXTURE['claims']:
            art = re.search(rf'<article class="atlas-claim [^"]*" id="atlas-c-{c["id"]}".*?</article>', self.html, re.S).group(0)
            self.assertIn(html.escape(c['status']['label'], quote=False), art)
            self.assertEqual(art.count('<li>'), len(c['hypotheses']), 'one plain list item per hypothesis')
            if not c['hypotheses']:
                self.assertIn('None listed.', art)

    def test_editorial_and_joined_paths_are_labelled_by_what_is_checked(self):
        self.assertIn('Editorial order', self.html)
        self.assertIn('Joined by recorded relations', self.html)
        self.assertNotRegex(re.sub(r'<[^>]+>', ' ', self.html), r'(?i)\b(dependency|proof order)\b')

    def test_namespace_and_attribute_quoting(self):
        classes = set()
        for value in re.findall(r'class="([^"]*)"', self.html):
            classes.update(value.split())
        self.assertEqual(classes & PAGE_HOOKS - SHARED_HOOKS, set())
        self.assertEqual(re.findall(r"\s[\w-]+='", self.html), [])

    def test_script_and_styles_make_no_request(self):
        for name in ('css', 'js'):
            text = self.out[name]
            self.assertNotRegex(text, r'\b(fetch|XMLHttpRequest|sendBeacon|WebSocket|EventSource|importScripts)\s*\(')
            self.assertNotIn('</script', text)
            self.assertEqual([u for u in re.findall(r'url\(\s*([^)]*)\)', text) if not u.strip('\'" ').startswith('#')], [])
        writes = re.findall(r'pushState|replaceState|location\.(?:hash|href)\s*=(?!=)|location\.(?:assign|replace)\(', self.out['js'])
        self.assertEqual(writes, [], 'the atlas never writes the address')
        self.assertNotRegex(self.out['js'] + self.out['css'], r'\.(py|json|md)\b', 'no file name in the shipped script or styles')

    def test_interface_words_travel_in_the_template(self):
        tpl = re.search(r'<template class="atlas-words">(.*?)</template>', self.html, re.S).group(1)
        for k, v in atlas.LABELS.items():
            if k.startswith('js_'):
                self.assertIn(f'<span data-word="{k[3:].replace("_", "-")}">{html.escape(v)}</span>', tpl)
        for name in set(re.findall(r"word\('([a-z-]+)'\)", self.out['js'])):
            self.assertIn(f'data-word="{name}"', tpl, name)

    def test_no_count_presented_as_progress(self):
        text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<template.*?</template>', ' ', self.html, flags=re.S)))
        for rule in (r'%', r'\b\d+\s+of\s+\d+\b', r'(?i)\b(progress|completed?|completion|percent)\b'):
            self.assertNotRegex(text, rule)

    def test_map_lines_start_at_their_source_and_end_at_their_target(self):
        pos = {m.group(1): (float(m.group(2)), float(m.group(3))) for m in re.finditer(
            r'<a class="atlas-node [^"]*" href="#atlas-c-[^"]+" tabindex="-1" data-claim-ref="([^"]+)" transform="translate\(([\d.]+) ([\d.]+)\)"', self.html)}
        self.assertEqual(set(pos), {c['id'] for c in FIXTURE['claims']})
        for m in re.finditer(r'<path class="atlas-edge[^"]*" d="M([\d.]+) ([\d.]+)C[\d. ]+ ([\d.]+) ([\d.]+)" data-edge-id="([^"]+)" '
                             r'data-source="([^"]+)" data-target="([^"]+)"', self.html):
            x0, y0, x1, y1 = map(float, m.group(1, 2, 3, 4))
            (sx, sy), (tx, ty) = pos[m.group(6)], pos[m.group(7)]
            self.assertAlmostEqual(y0, sy, delta=.06, msg=m.group(5))
            self.assertAlmostEqual(abs(x0 - sx), 19, delta=.06, msg=m.group(5))
            self.assertAlmostEqual(y1, ty, delta=.06, msg=m.group(5))
            self.assertAlmostEqual(abs(x1 - tx), 19, delta=.06, msg=m.group(5))

    def test_every_claim_reference_carries_its_number(self):
        for m in re.finditer(r'<a class="atlas-link" href="#atlas-c-([^"]+)">(.*?)</a>', self.html, re.S):
            if 'atlas-col-claim' in self.html[max(0, m.start() - 60):m.start()]:
                continue  # the index row has its number in its own column
            self.assertRegex(m.group(2), r'^<span class="atlas-num">\d+</span>', m.group(1))


@unittest.skipUnless(hasattr(__import__('status'), 'AtlasContext'), 'status.py has no atlas mount (AtlasContext) in this tree')
class Mounted(unittest.TestCase):
    def test_whole_page_builds_with_the_atlas_and_passes_the_audit(self):
        import audit
        import status
        root = SRC.parent.parent
        content = root / 'content' / 'quantum-holography-status'
        page = json.loads((content / 'page.json').read_text(encoding='utf-8'))
        with tempfile.TemporaryDirectory(dir=os.environ.get('ATLAS_TEST_TMP')) as tmp:
            folder = Path(tmp)
            for name in ('content.json', 'essay.md'):
                (folder / name).symlink_to(content / name)
            (folder / 'atlas.json').write_text(json.dumps(FIXTURE), encoding='utf-8')
            build = status.Build(folder, page, {}, None, atlas_module=SRC / 'atlas.py')
            markup = build.run()
            result = audit.run(build, markup)
        self.assertEqual(result['failures'], [])
        self.assertEqual(result['math_errors'], 0)
        self.assertEqual(markup.count('data-atlas-mount'), 1)
        self.assertIn('href="#s-hyperbolic-siegel-weil"', markup)


if __name__ == '__main__':
    unittest.main()
