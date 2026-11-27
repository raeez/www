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
# The classes the foundation mount reserves for the page script (status.py ATLAS_RESERVED_CLASSES), and 'mark'.
# Classes the page binds for its own script, as the foundation mount reserves them, plus the page's formula boxes and
# marks, which the atlas keeps out of (it renames the boxes and draws its own marks). The glossary button .term is
# the one class shared with the page: the interaction script opens the page's card from a .term[data-term].
PAGE_HOOKS = set('grid card card-inner filter filters row rows row-name statement statement-head statement-title status-chip '
                 'question question-ask questions known fold failure claim-text open-group col-def gloss theme nav find tally '
                 'math-display math-long cell-btn col-head'.split())


class Ctx:
    """The parts of the page's AtlasContext that the renderer uses."""

    def __init__(self, statements=('hyperbolic-siegel-weil',), anchors=('q-d-native-interface',), labels=None):
        self._statements = set(statements)
        self.anchors = frozenset(anchors)
        self.labels = labels or {}
        # Like page.json: the page's label for the statement status that matches the atlas's scoped negative.
        self.status_labels = {'refuted form': 'Refuted as first posed'}

    def rich(self, text, terms=True):
        """Like the page renderer: TeX in the page's formula boxes, and a glossary button when terms are on."""
        out = html.escape(text or '', quote=False)
        out = re.sub(r'\\\[(.+?)\\\]', lambda m: f'<span class="math-display"><math>{m.group(1)}</math></span>', out, flags=re.S)
        out = re.sub(r'\\\((.+?)\\\)', lambda m: (f'<span class="math-inline math-long"><math>{m.group(1)}</math></span>'
                                                  if len(m.group(1)) > 36 else f'<span class="math-inline"><math>{m.group(1)}</math></span>'), out)
        if terms:
            out = out.replace('weak module', '<button type="button" class="term" data-term="term-weak-module">weak module</button>')
        return out

    def mark(self, status, label=None):
        """Like the page's mark(): the page's svg with its colour class, a title and a name when labelled."""
        cls = status.replace(' ', '-')
        title = f'<title>{html.escape(label)}</title>' if label else ''
        attrs = f' role="img" aria-label="{html.escape(label)}"' if label else ' aria-hidden="true"'
        return (f'<svg class="mark mark-{cls}" viewBox="0 0 16 16" width="16" height="16"{attrs} focusable="false">'
                f'{title}<circle data-page-mark="{cls}" cx="8" cy="8" r="5"/></svg>')

    def anchor_for(self, statement_id):
        return '#s-' + statement_id if statement_id in self._statements else None

    def section_anchor(self, section_id):
        return '#' + section_id if section_id in self.anchors else None

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
    def test_source_label_links_to_the_book_section(self):
        data = mutated(lambda d: claim(d, 'alpha-base').update(
            sourceLabel='Current products', sectionRef='ch12-current-products'))
        context = Ctx(anchors=('q-d-native-interface', 'ch12-current-products'))
        self.assertEqual(errors(data, context), [])
        self.assertEqual(atlas.validate(data, context).claim['alpha-base']['sectionRef'],
                         '#ch12-current-products')
        self.assertTrue(any('sectionRef' in message for message in errors(data, Ctx())))

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

    def test_derived_ids_cannot_collide(self):
        data = mutated(lambda d: (d['claims'].append(dict(copy.deepcopy(claim(d, 'beta-isolated')), id='beta-isolated-h',
                                                         title='Synthetic claim with a suffix in its id')),
                                  d['domains'].append({'id': 'alpha-h', 'label': 'Synthetic domain alpha h', 'summary': 'Synthetic summary.'})))
        out = atlas.render(data, Ctx())
        self.assertEqual(out['problems'], [])
        ids = re.findall(r'\sid="([^"]+)"', out['html'])
        self.assertEqual(len(ids), len(set(ids)), 'no duplicate id')

    def test_more_relation_types_than_line_styles_are_drawn_plain_and_said_so(self):
        def many(d):
            for i in range(9):
                d['edges'].append({'id': f'e-extra-{i}', 'source': 'gamma-b', 'target': 'gamma-neg', 'relation': f'kind{i}',
                                   'label': f'synthetic relation {i}', 'scope': ''})
        out = atlas.render(mutated(many), Ctx())
        self.assertEqual(out['problems'], [])
        styles = set(re.findall(r'<path class="atlas-edge (rk-\d)"', out['html']))
        self.assertEqual(styles, {'rk-8'}, 'one plain style for every line when the types outnumber the styles')
        self.assertIn('drawn in one style', out['html'])
        names = re.search(r'<details class="atlas-more atlas-rel-all">.*?<ul class="atlas-rel-names">(.*?)</ul></details>', out['html'], re.S)
        self.assertTrue(names, 'the relation names stay readable in the key, in a disclosure')
        for i in range(9):
            self.assertIn(f'synthetic relation {i}', names.group(1))

    def test_question_links_conventions_and_notes(self):
        data = mutated(lambda d: (d['domains'][0].update(conventions=['Synthetic convention.'], relatedQuestionIds=['d-native-interface']),
                                  d['readingPaths'][0].update(note='Synthetic editorial note.')))
        out = atlas.render(data, Ctx())
        self.assertEqual(out['problems'], [])
        self.assertIn('href="#q-d-native-interface"', out['html'])
        self.assertIn('Synthetic convention.', out['html'])
        self.assertIn('Synthetic editorial note.', out['html'])
        self.assertTrue(any("no question on the page with id 'nowhere'" in e
                            for e in errors(mutated(lambda d: d['comparisons'][0].update(questionId='nowhere')))))

    def test_an_unknown_field_fails_the_build_and_is_named(self):
        out = atlas.render(mutated(lambda d: claim(d, 'alpha-base').update(familyId='synthetic-family')), Ctx())
        self.assertTrue(any("unknown key 'familyId'" in p for p in out['problems']), 'a field of a new payload is never dropped silently')
        self.assertNotIn('synthetic-family', out['html'], 'and nothing of it is shown')

    def test_a_reader_finding_fails_the_build_but_still_draws_the_atlas(self):
        out = atlas.render(mutated(lambda d: claim(d, 'alpha-base').update(statement='Synthetic statement with C1 outside TeX.')), Ctx())
        self.assertTrue(out['html'], 'a draft build can still show the atlas')
        self.assertTrue(any('internal identifier' in p for p in out['problems']), 'the build fails')
        out = atlas.render(mutated(lambda d: d['edges'][0].update(target='nobody')), Ctx())
        self.assertEqual(out['html'], '', 'a structural error draws nothing')

    def test_interface_words_meet_the_reader_rules(self):
        out = atlas.render(FIXTURE, Ctx(labels={'atlas_intro': 'Read the ledger first.'}))
        self.assertEqual(out['html'], '')
        self.assertTrue(any('label intro' in p and 'workflow vocabulary' in p for p in out['problems']), out['problems'])

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
        self.assertEqual(errors(mutated(lambda d: claim(d, 'alpha-base').update(statement='The map dbar:L_P and Xi:RHom are notation.'))), [],
                         'mathematical notation with a colon is not a label')
        self.assertEqual(errors(mutated(lambda d: claim(d, 'beta-isolated').update(id='native-displayed-r3-transport'))), [],
                         'ordinary slug parts such as r3 are accepted in ids')

    def test_references(self):
        self.expect(mutated(lambda d: claim(d, 'alpha-base').update(domainId='nowhere')), "no domain with id 'nowhere'")
        self.expect(mutated(lambda d: d['edges'][0].update(target='nobody')), "no claim with id 'nobody'")
        self.expect(mutated(lambda d: d['edges'][0].update(target=d['edges'][0]['source'])), 'a claim related to itself')
        self.expect(mutated(lambda d: d['edges'].append(dict(d['edges'][0], id='e-again'))), "a second 'uses' edge")
        self.expect(mutated(lambda d: claim(d, 'beta-linked').update(statementRef='no-such-statement')),
                    "no statement on the page with id 'no-such-statement'")

    def test_typed_vocabulary(self):
        self.expect(mutated(lambda d: claim(d, 'alpha-base')['status'].update(code='proved')), "'proved' is not one of")
        self.expect(mutated(lambda d: d['edges'][0].update(relation='uses!')), 'is not a relation code')
        self.assertEqual(errors(mutated(lambda d: (d['edges'][1].update(label='another wording'),
                                                  claim(d, 'alpha-lift')['status'].update(label='Another label'),
                                                  d['edges'][2].update(relation='checked construction input')))), [],
                         'each claim and each edge keeps its own label; relation codes may be words')

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

    def test_status_words_by_code_and_hypotheses_as_supplied(self):
        for c in FIXTURE['claims']:
            art = re.search(rf'<article class="atlas-claim [^"]*" id="atlas-c-{c["id"]}".*?</article>', self.html, re.S).group(0)
            self.assertIn(f'<span class="atlas-chip-group">{atlas.LABELS["group_" + c["status"]["code"]]}</span>', art,
                          'the status word chosen by the stored code')
            self.assertEqual(art.count('<li>'), len(c['hypotheses']), 'one plain list item per hypothesis')
            if not c['hypotheses']:
                self.assertIn('None listed.', art)

    def test_stage_heading_comes_before_its_joins_and_the_rail_has_no_arrow(self):
        for stage in re.findall(r'<li class="atlas-stage".*?</li>(?=<li class="atlas-stage"|</ol>)', self.html, re.S):
            if 'atlas-join' in stage:
                self.assertLess(stage.find('atlas-stage-h'), stage.find('atlas-join'))
        self.assertNotIn('.atlas-stage + .atlas-stage::after', self.out['css'])
        self.assertIn('Stage 4 is joined to stage 3 by', self.html)

    def test_the_four_statuses_are_said_to_be_the_page_statuses(self):
        self.assertIn('The four statuses are those of the whole page', self.html)
        self.assertIn('at least one of which is not established', self.html)

    def test_editorial_and_joined_paths_are_labelled_by_what_is_checked(self):
        self.assertIn('Editorial order', self.html)
        self.assertIn('Joined by recorded relations', self.html)
        self.assertNotRegex(re.sub(r'<[^>]+>', ' ', self.html), r'(?i)\b(dependency|proof order)\b')

    def test_namespace_and_attribute_quoting(self):
        classes = set()
        for value in re.findall(r'class="([^"]*)"', self.html):
            classes.update(value.split())
        self.assertEqual(classes & PAGE_HOOKS, set(), 'no class the page reserves for its script')
        for tag in re.findall(r'<[a-z]+[^>]*\bclass="term"[^>]*>', self.html):
            self.assertRegex(tag, r'^<button type="button" class="term" data-term="term-[\w-]+"', 'a shared .term is a glossary button')
        self.assertIn('atlas-math-display', classes, 'display formulae keep their box, in the atlas name')
        self.assertIn('atlas-math-long', classes, 'long inline formulae keep their box, in the atlas name')
        self.assertEqual(re.findall(r"\s[\w-]+='", self.html), [])

    def test_search_units_are_offered_to_the_page(self):
        for kind, prefix in (('claims', 'atlas-c-'), ('domains', 'atlas-d-'), ('comparisons', 'atlas-k-'), ('readingPaths', 'atlas-p-')):
            for item in FIXTURE[kind]:
                unit = re.search(rf'<(?:article|details) [^>]*id="{prefix}{item["id"]}"[^>]*>', self.html).group(0)
                self.assertIn('data-qh-unit', unit, item['id'])
        self.assertEqual(self.html.count('data-qh-unit-title'), sum(len(FIXTURE[k]) for k in ('claims', 'domains', 'comparisons', 'readingPaths')))

    def test_script_and_styles_make_no_request(self):
        for name in ('css', 'js'):
            text = self.out[name]
            self.assertNotRegex(text, r'\b(fetch|XMLHttpRequest|sendBeacon|WebSocket|EventSource|importScripts)\s*\(')
            self.assertNotIn('</script', text)
            self.assertEqual([u for u in re.findall(r'url\(\s*([^)]*)\)', text) if not u.strip('\'" ').startswith('#')], [])
        writes = re.findall(r'pushState|replaceState|location\.(?:hash|href)\s*=(?!=)|location\.(?:assign|replace)\(', self.out['js'])
        self.assertEqual(writes, [], 'the atlas never writes the address')
        self.assertNotRegex(self.out['js'] + self.out['css'], r'\.(py|json|md)\b', 'no file name in the shipped script or styles')

    def test_shipped_script_and_styles_carry_no_forbidden_word(self):
        import audit
        for name in ('css', 'js'):
            text = self.out[name]
            for t in (text, re.sub(r'[_-]', ' ', text)):
                hits = [m.group(0) for pattern, why, flags in audit.FORBIDDEN for m in re.finditer(pattern, t, flags)
                        # a CSS length or gradient stop in per cent is not a reader-visible percentage
                        if not (name == 'css' and why == 'percentage' and m.group(0).rstrip().endswith('%'))]
                self.assertEqual(hits, [], name)

    def test_the_map_keeps_its_own_size_on_screen(self):
        css = self.out['css']
        self.assertIn('.atlas-map-inner { width: calc(var(--map-w) * 1px);', css)
        w = re.search(r'<svg class="atlas-map-svg" viewBox="0 0 (\d+) \d+" width="\1"', self.html).group(1)
        self.assertIn(f'style="--map-w:{w}"', self.html)
        self.assertIn('.atlas-node text { font-family: var(--font-ui); font-size: 13px;', css)

    def test_a_long_domain_runs_over_several_columns(self):
        def long(d):
            for i in range(60):
                d['claims'].append({'id': f'gamma-extra-{i}', 'domainId': 'gamma', 'title': f'Synthetic extra claim {i}',
                                    'statement': 'Synthetic statement.', 'status': {'code': 'remaining', 'label': 'Synthetic remaining label'},
                                    'hypotheses': []})
        out = atlas.render(mutated(long), Ctx())
        self.assertEqual(out['problems'], [])
        xs = {float(x) for x in re.findall(r'data-claim-ref="gamma-[^"]*" transform="translate\(([\d.]+) ', out['html'])}
        self.assertGreater(len(xs), 1, 'the gamma lane has several columns')
        h = int(re.search(r'viewBox="0 0 \d+ (\d+)"', out['html']).group(1))
        self.assertLess(h, 63 * 26, 'the map is shorter than one column of 63 claims')
        self.assertIn('class="atlas-index atlas-index-long"', out['html'], 'a long index scrolls in its own box')
        self.assertNotIn('atlas-index-long"', self.html, 'a short index does not')

    def test_the_map_and_key_come_first(self):
        main = self.html[self.html.find('<div class="atlas-main">'):]
        self.assertTrue(main.startswith('<div class="atlas-main"><section class="atlas-part atlas-overview" id="atlas-overview"'))
        self.assertLess(main.find('class="atlas-key"'), main.find('id="atlas-map"'), 'the legend comes before the figure')
        self.assertLess(main.find('id="atlas-map"'), main.find('id="atlas-domains"'))

    def test_every_supplied_text_sits_in_a_supplied_class(self):
        # Every string of the content owner gets a sentinel word; with the elements of atlas.SUPPLIED_CLASSES taken
        # out, no sentinel may be left in the text or in any attribute (so the gate scans and the count scans can
        # tell the content owner's words from the atlas's own).
        def mark_all(d):
            S = ' Zqxs'
            for x in d['domains']:
                x['label'] += S; x['summary'] += S
                x['conventions'] = [c + S for c in x.get('conventions', ['Synthetic convention.'])]
            for c in d['claims']:
                c['title'] += S; c['statement'] += S; c['hypotheses'] = [h + S for h in c['hypotheses']]
                c['status']['label'] += S
                c['sourceLabel'] = (c.get('sourceLabel') or 'Synthetic source') + S
            for e in d['edges']:
                e['label'] += S; e['scope'] = (e.get('scope') or 'synthetic scope') + S
            for k in d['comparisons']:
                k['title'] += S; k['overview'] += S
            for p in d['readingPaths']:
                p['title'] += S; p['summary'] += S; p['note'] = (p.get('note') or 'Synthetic note.') + S
                for st in p['stages']:
                    st['label'] += S; st['description'] += S
        out = atlas.render(mutated(mark_all), Ctx())
        self.assertEqual(out['problems'], [])
        h = out['html']
        self.assertIn('Zqxs', h)
        rest = h
        for cls_ in atlas.SUPPLIED_CLASSES:
            while True:
                m = re.search(r'<([a-z][\w-]*)\b[^>]*\bclass="(?:[^"]* )?' + re.escape(cls_) + r'(?: [^"]*)?"[^>]*>', rest)
                if not m:
                    break
                tag, depth, end = m.group(1), 0, len(rest)
                for t in re.finditer(r'<(/?)' + tag + r'\b[^>]*>', rest[m.start():]):
                    depth += -1 if t.group(1) else 1
                    if depth == 0:
                        end = m.start() + t.end()
                        break
                rest = rest[:m.start()] + rest[end:]
        rest = re.sub(r'<template\b.*?</template>', '', rest, flags=re.S)
        left = [rest[max(0, i - 160):i + 10] for i in [m.start() for m in re.finditer('Zqxs', rest)]]
        self.assertEqual(left, [], 'supplied text outside atlas.SUPPLIED_CLASSES')

    def test_the_reader_tests_know_every_supplied_class(self):
        cjs = (HERE / 'atlas.test.cjs').read_text(encoding='utf-8')
        block = re.search(r'const SUPPLIED = (.*?);\n', cjs, re.S).group(1)
        missing = [c for c in atlas.SUPPLIED_CLASSES if '.' + c not in block]
        self.assertEqual(missing, [], 'atlas.test.cjs SUPPLIED lacks these classes of atlas.SUPPLIED_CLASSES')

    def test_conventions_come_first_and_each_claim_links_to_them(self):
        self.assertIn('id="atlas-d-alpha--conv"', self.html)
        card = re.search(r'<article class="atlas-domain" id="atlas-d-alpha".*?</article>', self.html, re.S).group(0)
        self.assertLess(card.find('atlas-conventions'), card.find('atlas-groups'), 'conventions before the claims they govern')
        claim_ = re.search(r'<article class="atlas-claim[^"]*" id="atlas-c-alpha-base".*?</article>', self.html, re.S).group(0)
        self.assertIn('href="#atlas-d-alpha--conv"', claim_)
        beta = re.search(r'<article class="atlas-claim[^"]*" id="atlas-c-beta-isolated".*?</article>', self.html, re.S).group(0)
        self.assertNotIn('--conv', beta, 'a domain without conventions gets no link')

    def test_status_words_follow_the_stored_code_never_the_record_label(self):
        # The status-language ruling: the visible word is chosen by the stored code; per-record labels are display
        # aliases and appear nowhere on the page.
        for c in FIXTURE['claims']:
            self.assertNotIn(html.escape(c['status']['label']), self.html, c['id'])
        words = {atlas.LABELS['group_' + k] for k in atlas.CODES}
        self.assertEqual(words, {'Established', 'Conditional', 'Remaining', 'Scoped negative'})
        chips = re.findall(r'<span class="atlas-chip-group">([^<]*)</span>', self.html)
        self.assertTrue(chips and set(chips) <= words)
        cells = re.findall(r'<td class="atlas-col-status">.*?<span>([^<]*)</span></td>', self.html)
        self.assertTrue(cells and set(cells) <= words)

    def test_the_key_shows_the_page_mark_of_every_status(self):
        for code, legacy in atlas.PAGE_STATUS.items():
            item = re.search(rf'<div class="atlas-key-item" data-key-status="{code}">.*?</div>', self.html, re.S).group(0)
            self.assertIn(f'class="mark mark-{legacy.replace(" ", "-")}"', item, code)
        self.assertEqual(atlas.PAGE_STATUS, {'checked': 'checked', 'conditional': 'conditional', 'remaining': 'open',
                                             'scoped_negative': 'refuted form'}, 'the ruling\'s aliases')
        self.assertIn('--as-negative: var(--st-refuted-form)', self.out['css'])
        self.assertIn('--as-remaining: var(--st-open)', self.out['css'])

    def test_one_mark_system_the_pages(self):
        # C5: every status mark in the atlas is the page's mark for the status's page alias, drawn by the page
        # (ctx.mark); no mark of the atlas's own remains, and the key needs no sentence to translate between two.
        self.assertNotIn('atlas-mark', self.html)
        self.assertNotRegex(self.html, r'class="am[ -"]')
        self.assertNotIn('atlas-mark', self.out['css'])
        self.assertNotRegex(self.out['css'], r'\.am-')
        self.assertNotIn('key_page', atlas.LABELS)
        self.assertEqual(atlas.LABELS['key_separate'], 'The four statuses are those of the whole page.', 'no translation between two systems')
        self.assertNotIn('squares', self.html)
        code = {c['id']: c['status']['code'] for c in FIXTURE['claims']}
        slug = {k: v.replace(' ', '-') for k, v in atlas.PAGE_STATUS.items()}
        links = re.findall(r'<a class="atlas-link" href="#atlas-c-([^"]+)">(.*?)</a>', self.html, re.S)
        marked = [(cid, body) for cid, body in links if '<svg' in body]
        self.assertTrue(marked)
        for cid, body in marked:
            self.assertIn(f'<svg class="mark mark-{slug[code[cid]]}"', body, cid)
        for cid, body in re.findall(r'<a class="atlas-node [^"]*"[^>]*data-claim-ref="([^"]+)"[^>]*>(.*?)</a>', self.html, re.S):
            self.assertIn(f'<g class="atlas-node-mark mark-{slug[code[cid]]}" transform="translate(-19 -6) scale(.75)">'
                          f'<circle data-page-mark="{slug[code[cid]]}"', body, cid)
            self.assertNotIn('<title>', body, 'the map node is named by its link, not by its mark')
        for k, body in re.findall(r'<span class="atlas-chip ac-([a-z-]+)">(.*?)</span></span>', self.html, re.S):
            self.assertIn(f'class="mark mark-{slug[k.replace("-", "_")]}"', body, k)
        for k, cell in re.findall(r'<tr id="[^"]+" data-claim-ref="([^"]+)">.*?<td class="atlas-col-status">(.*?)</td>', self.html, re.S):
            self.assertIn(f'class="mark mark-{slug[code[k]]}"', cell, k)
        # a labelled mark (a list not grouped by status) is named by its status word, as the page names its marks
        labelled = re.findall(r'<svg class="mark mark-[a-z-]+" [^>]*role="img" aria-label="([^"]+)"', self.html)
        self.assertTrue(set(labelled) <= {atlas.LABELS['group_' + k] for k in atlas.CODES})

    def test_without_a_page_no_mark_is_drawn_and_the_word_stands(self):
        class Plain(Ctx):
            pass
        Plain.mark = property(lambda self: (_ for _ in ()).throw(AttributeError('mark')))
        out = atlas.render(copy.deepcopy(FIXTURE), Plain())
        self.assertNotIn('<svg class="mark', out['html'])
        self.assertIn(atlas.LABELS['group_checked'], out['html'])
        self.assertEqual([p for p in out['problems'] if 'no mark' in p], [])

    def test_the_locator_is_the_whole_map_in_small_and_only_places(self):
        # A2: in the pane and hidden until the script selects a claim: one band per domain and one dot per claim, each
        # at its claim's place in the map (the same layout); a ring and a number the script places; a link to the map.
        # Nothing on it is a line, so it implies no relation.
        loc = re.search(r'<div class="atlas-locator" hidden>.*?<p class="atlas-locator-caption">.*?</p></div>', self.html, re.S).group(0)
        self.assertGreater(self.html.index('<div class="atlas-locator"'), self.html.index('class="atlas-part atlas-claims-full"'), 'in the pane')
        self.assertEqual(len(re.findall(r'<rect class="atlas-locator-track', loc)), len(FIXTURE['domains']))
        self.assertEqual(re.findall(r'data-domain-ref="([^"]+)"', loc), [d['id'] for d in FIXTURE['domains']])
        dots = {i: (float(x), float(y)) for i, x, y in re.findall(r'<circle data-claim-ref="([^"]+)" cx="([^"]+)" cy="([^"]+)"', loc)}
        nodes = {i: (float(x), float(y)) for i, x, y in
                 re.findall(r'<a class="atlas-node [^"]*" href="#atlas-c-[^"]+" tabindex="-1" data-claim-ref="([^"]+)" transform="translate\(([-\d.]+) ([-\d.]+)\)"', self.html)}
        self.assertEqual(len(dots), len(FIXTURE['claims']))
        self.assertEqual(dots, nodes, 'every dot at the place of its pill in the map')
        self.assertIn('viewBox="0 0 ' + re.search(r'<svg class="atlas-map-svg" viewBox="0 0 ([\d.]+ [\d.]+)"', self.html).group(1) + '"', loc)
        self.assertNotRegex(loc, r'<(path|line|polyline|marker)\b', 'no relation is drawn or implied')
        self.assertIn('<a class="atlas-locator-link" href="#atlas-map">', loc)
        for k in ('locator', 'locator_link', 'locator_caption'):
            self.assertIn(html.escape(atlas.LABELS[k]), loc, k)

    def test_the_pane_has_a_column_of_its_own_on_a_wide_screen_and_its_head_stays_at_its_top(self):
        # A6: on a wide screen nothing lies over the atlas: the pane takes a column of its own while it is shown and
        # the atlas reflows; its head, with Close, stays at its top at every width; print leaves the locator out; the
        # index in a narrow column writes the domain under the claim rather than squeezing it.
        css = self.out['css']
        wide = css[css.index('@media (min-width: 1000px) {'):]
        wide = wide[:wide.index('\n}\n')]
        self.assertIn('.atlas-js.has-pane { display: grid; grid-template-columns: minmax(0, 1.618fr) minmax(0, 1fr);', wide)
        self.assertNotIn('position: fixed', wide, 'nothing lies over the atlas on a wide screen')
        self.assertIn('position: sticky', wide)
        self.assertRegex(css, r'\.atlas-js \.atlas-pane-head \{ position: sticky; top: 0;')
        self.assertIn('.atlas-locator', css[css.index('@media print'):], 'print leaves the locator out')
        self.assertRegex(css, r'@container atlas-main \(max-width: 44rem\) \{\s*\.atlas-table \.atlas-col-domain \{ display: none; \}')

    def test_an_alias_the_page_cannot_show_fails_the_build(self):
        class NoMarks(Ctx):
            def mark(self, status, label=None):
                return ''
        out = atlas.render(copy.deepcopy(FIXTURE), NoMarks())
        self.assertTrue(any("has no mark for its status 'refuted form'" in p for p in out['problems']), 'never dropped silently')
        self.assertTrue(out['html'], 'a reader finding: a draft still draws')

    def test_every_claim_is_offered_to_the_page_search_with_its_page_status(self):
        tags = re.findall(r'<article class="atlas-claim[^"]*"[^>]*>', self.html)
        self.assertTrue(tags)
        for tag in tags:
            code = re.search(r'data-status-code="([a-z_]+)"', tag).group(1)
            self.assertIn(f'data-qh-unit-status="{atlas.PAGE_STATUS[code]}"', tag)

    def test_the_atlas_keeps_its_scale_long_parts_folded_and_the_map_a_screen_tall(self):
        # Native QA C1/C2: at 955 claims in 12 domains the map was 8,192 px tall and the comparisons, paths and domain
        # lists ran open. Comparisons and paths are folded disclosures (their anchors on the details), each domain's
        # conventions, claims and comparisons are folded under its summary, and the map is at most MAP_ROWS rows tall.
        for item in FIXTURE['comparisons']:
            self.assertRegex(self.html, rf'<details class="atlas-fold atlas-comparison" id="atlas-k-{item["id"]}"')
        for item in FIXTURE['readingPaths']:
            self.assertRegex(self.html, rf'<details class="atlas-fold atlas-path [^"]*" id="atlas-p-{item["id"]}"')
        self.assertEqual(self.html.count('<details class="atlas-fold atlas-domain-fold">'), len(FIXTURE['domains']))
        self.assertNotRegex(self.html, r'<details class="atlas-fold[^"]*"[^>]* open', 'every fold starts closed')
        def wide(d):
            for i in range(12):
                d['domains'].append({'id': f'extra-{i}', 'label': f'Synthetic extra domain {i}', 'summary': 'Synthetic.'})
            for i in range(300):
                d['claims'].append({'id': f'extra-claim-{i}', 'domainId': 'gamma', 'title': f'Synthetic wide claim {i}',
                                    'statement': 'Synthetic statement.', 'status': {'code': 'checked', 'label': 'Synthetic label'},
                                    'hypotheses': []})
        out = atlas.render(mutated(wide), Ctx())
        self.assertEqual(out['problems'], [])
        h = int(re.search(r'<svg class="atlas-map-svg" viewBox="0 0 \d+ (\d+)"', out['html']).group(1))
        self.assertLessEqual(h, 18 * 2 + (atlas.MAP_ROWS - 1) * 26 + 18, 'the map keeps a screen height when it cannot fit the width')

    def test_a_hypothesis_list_repeated_in_one_comparison_is_named_once(self):
        def same(d):
            hyps = ['Synthetic shared hypothesis one.', 'Synthetic shared hypothesis two.']
            k = d['comparisons'][0]
            ids = [cid for b in ('conditionalClaimIds', 'scopedNegativeClaimIds') for cid in (k.get(b) or [])]
            for cid in ids:
                claim(d, cid)['hypotheses'] = list(hyps)
            return ids
        data = copy.deepcopy(FIXTURE); ids = same(data)
        if len(ids) < 2:
            self.skipTest('the fixture comparison lists fewer than two conditional or negative claims')
        out = atlas.render(data, Ctx())
        fold = re.search(rf'<details class="atlas-fold atlas-comparison" id="atlas-k-{data["comparisons"][0]["id"]}".*?</details>', out['html'], re.S).group(0)
        self.assertEqual(fold.count('Synthetic shared hypothesis one.'), 1, 'shown once in the comparison')
        self.assertIn('Same hypotheses as No.', fold)
        self.assertGreaterEqual(out['html'].count('Synthetic shared hypothesis one.'), len(ids), 'every claim still lists them in full')

    def test_native_qa_map_and_layout_faults_are_closed(self):
        css = self.out['css']
        # C11: the pill rule touches only the pill, so a status mark keeps its own fill
        self.assertNotRegex(css, r'\.atlas-node rect\b', 'no rule reaches the mark inside a node')
        nodes = re.findall(r'<a class="atlas-node[^"]*"[^>]*>(.*?)</a>', self.html, re.S)
        self.assertTrue(nodes and all(n.startswith('<rect class="atlas-pill"') for n in nodes))
        # C13: one-column grids may shrink below their widest word or formula
        for sel in ('.atlas-claimlist {', '.atlas-groups {', '.atlas-hyps {', '.atlas-rels, .atlas-join-list {', '.atlas-tools {'):
            rule = css[css.index(sel):css.index('}', css.index(sel))]
            self.assertIn('grid-template-columns: minmax(0, 1fr)', rule, sel)
        # C16: the map box is one tab stop that says how to use it, with a polite live region
        self.assertIn('aria-describedby="atlas-map-keys"', self.html)
        self.assertIn('aria-live="polite" data-atlas-map-say', self.html)
        # C7: running text in an open fold keeps the reading measure
        self.assertIn('.atlas-fold-body > .atlas-overview', css)

    def test_a_stage_that_names_its_one_claim_names_it_once(self):
        def same(d):
            p = d['readingPaths'][0]
            st = p['stages'][0]
            st['claimIds'] = st['claimIds'][:1]
            st['label'] = claim(d, st['claimIds'][0])['title']
            return p['id'], st['claimIds'][0]
        data = copy.deepcopy(FIXTURE); pid, cid = same(data)
        out = atlas.render(data, Ctx())
        stage = re.search(rf'id="atlas-p-{pid}".*?<li class="atlas-stage" data-stage="0">(.*?)</li>', out['html'], re.S).group(1)
        self.assertIn(f'href="#atlas-c-{cid}"', stage.split('</h5>')[0], 'the stage heading is the link to its claim')
        self.assertNotIn('atlas-claimlist', stage, 'and the title is not repeated in a list')

    def test_a_scoped_negative_claim_lists_its_scope(self):
        neg = next(c['id'] for c in FIXTURE['claims'] if c['status']['code'] == 'scoped_negative')
        out = atlas.render(mutated(lambda d: claim(d, neg).update(hypotheses=[])), Ctx())
        self.assertTrue(any('a scoped negative claim must list the hypotheses of its scope' in p for p in out['problems']))
        self.assertTrue(out['html'], 'a reader finding: the build fails, a draft still draws')

    def test_glossary_buttons_in_the_text_and_never_inside_a_link(self):
        self.assertIn('class="term" data-term="term-weak-module"', self.html, 'a statement keeps its glossary button')
        for inner in re.findall(r'<a\b[^>]*>(.*?)</a>', self.html, flags=re.S):
            self.assertNotIn('<button', inner, 'no button inside a link')

    def test_interface_words_travel_in_the_template(self):
        tpl = re.search(r'<template class="atlas-wordlist">(.*?)</template>', self.html, re.S).group(1)
        for k, v in atlas.LABELS.items():
            if k.startswith('js_'):
                self.assertIn(f'<span data-word="{k[3:].replace("_", "-")}">{html.escape(v)}</span>', tpl)
        for name in set(re.findall(r"word\('([^']+)'\)", self.out['js'])):
            self.assertIn(f'data-word="{name}"', tpl, name)

    def test_no_count_presented_as_progress(self):
        # A space at every element boundary, as a reader or a screen reader meets the text; the index table
        # (its numbers stand under the 'No.' heading), the drawings and the inert words are left out.
        h = re.sub(r'<(table|template|svg)\b.*?</\1>', ' ', self.html, flags=re.S)
        text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h)))
        for rule in (r'%', r'\b\d+\s+of\s+\d+\b', r'(?i)\b(progress|completed?|completion|percent)\b',
                     r'(?i)(?<!No\. )\b\d+\s+(established|conditional|scoped|remaining|claims?|theorems?)\b'):
            self.assertNotRegex(text, rule)
        self.assertNotRegex(text, r'^\s*The atlas sets out the claims', 'the introduction does not imply the full set')

    def test_map_lines_start_at_their_source_and_end_at_their_target(self):
        pos = {m.group(1): (float(m.group(2)), float(m.group(3))) for m in re.finditer(
            r'<a class="atlas-node [^"]*" href="#atlas-c-[^"]+" tabindex="-1" data-claim-ref="([^"]+)" transform="translate\(([\d.]+) ([\d.]+)\)"', self.html)}
        self.assertEqual(set(pos), {c['id'] for c in FIXTURE['claims']})
        for m in re.finditer(r'<path class="atlas-edge[^"]*" d="M([\d.]+) ([\d.]+)C[\d. ]+ ([\d.]+) ([\d.]+)" data-edge-id="([^"]+)" '
                             r'data-source="([^"]+)" data-target="([^"]+)"', self.html):
            x0, y0, x1, y1 = map(float, m.group(1, 2, 3, 4))
            (sx, sy), (tx, ty) = pos[m.group(6)], pos[m.group(7)]
            self.assertAlmostEqual(y0, sy, delta=.06, msg=m.group(5))
            self.assertAlmostEqual(abs(x0 - sx), 22, delta=.06, msg=m.group(5))
            self.assertAlmostEqual(y1, ty, delta=.06, msg=m.group(5))
            self.assertAlmostEqual(abs(x1 - tx), 22, delta=.06, msg=m.group(5))

    def test_every_claim_reference_carries_its_number(self):
        for m in re.finditer(r'<a class="atlas-link" href="#atlas-c-([^"]+)">(.*?)</a>', self.html, re.S):
            if 'atlas-col-claim' in self.html[max(0, m.start() - 60):m.start()]:
                continue  # the index row has its number in its own column
            self.assertRegex(m.group(2), r'^<span class="atlas-num"><span class="atlas-vh">No\. </span>\d+</span>', m.group(1))


@unittest.skipUnless(hasattr(__import__('status'), 'AtlasContext'), 'status.py has no atlas mount (AtlasContext) in this tree')
class Mounted(unittest.TestCase):
    def test_whole_page_builds_with_the_atlas_and_passes_the_audit(self):
        import audit
        import status
        root = SRC.parent.parent
        content = root / 'content' / 'quantum-holography-status'
        page = json.loads((content / 'page.json').read_text(encoding='utf-8'))
        # A content that names its atlas (content.json scientific_atlas) gets the synthetic atlas under that name.
        pointer = json.loads((content / 'content.json').read_text(encoding='utf-8')).get('scientific_atlas') or {}
        fixture = dict(FIXTURE, **{k: pointer[k] for k in ('schema', 'asOf') if k in pointer})

        def run(with_atlas):
            with tempfile.TemporaryDirectory(dir=os.environ.get('ATLAS_TEST_TMP')) as tmp:
                folder = Path(tmp)
                for name in ('content.json', 'essay.md'):
                    (folder / name).symlink_to(content / name)
                if with_atlas:
                    (folder / 'atlas.json').write_text(json.dumps(fixture), encoding='utf-8')
                build = status.Build(folder, page, {}, None, atlas_module=SRC / 'atlas.py')
                markup = build.run()
                return markup, audit.run(build, markup)
        _, alone = run(False)
        markup, result = run(True)
        # The atlas adds no failure to the page's own audit (the page's content may carry findings of its own, and a
        # content that names an atlas fails without one).
        self.assertEqual([f for f in result['failures'] if f not in alone['failures']], [])
        self.assertEqual(result['math_errors'], 0)
        self.assertEqual(len(re.findall(r'<section [^>]*\bdata-atlas-mount[ >]', markup)), 1, 'one mounted atlas section')
        nav = re.search(r'<nav class="nav".*?</nav>', markup, re.S).group(0)
        page_names = {html.unescape(t) for t in re.findall(r'<a href="#[^"]+">([^<]+)</a>', nav)} - {'Atlas'}
        parts = re.search(r'<nav class="atlas-parts".*?</nav>', markup, re.S).group(0)
        self.assertEqual({html.unescape(t) for t in re.findall(r'<a href="#[^"]+">([^<]+)</a>', parts)} & page_names, set(),
                         'no atlas part shares a name with a section of the page')
        self.assertIn('href="#s-hyperbolic-siegel-weil"', markup)


if __name__ == '__main__':
    unittest.main()
