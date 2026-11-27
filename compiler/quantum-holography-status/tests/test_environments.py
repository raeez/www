"""Mathematical declarations in the Markdown used by the native book."""
import json
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from monograph import Book, Diagram, Form, lead_in, parse_blocks, status_mark_of
from status import Build, mark
from audit import _Attributes, environment_errors


class Elements(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.ids = {}
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, attrs['id']
            self.ids[attrs['id']] = attrs


class Environments(unittest.TestCase):
    def setUp(self):
        compiler = Path(__file__).resolve().parents[2]
        folder = compiler.parent / 'content/quantum-holography-status'
        page = json.loads((folder / 'page.json').read_text(encoding='utf-8'))
        self.book = Book(Build(folder, page), folder / 'reader-data/manifest.json', mark, page['reader'])
        self.book.current = 'ch01'
        self.book.pending_refs = []

    def render(self, source, envs=True):
        return self.book.render(parse_blocks(source.splitlines()), envs=envs)

    def test_front_search_targets_survive_insertions_and_preserve_authored_ids(self):
        def targets(book, before, words):
            blocks = [{'t': 'h', 'id': 'opening-contours'}, *before, {'t': 'p', 'text': words},
                      {'t': 'math', 'tex': 'x^2'}, {'t': 'math', 'tex': 'y', 'id': 'eq-authored'},
                      {'t': 'p', 'text': 'Definition context.', 'passage_id': 'authored-definition'}]
            book.address_front_passages(blocks, 'introduction')
            tail = blocks[-4:]
            assert 'front_text_id' not in tail[3]
            return [tail[0]['front_text_id'], tail[1]['id'], tail[2]['id'], tail[3]['passage_id']]

        first = targets(self.book, [], 'Fix a contour.')
        other = Book(self.book.b, self.book.path, mark, self.book.L)
        later = targets(other, [{'t': 'p', 'text': 'A preceding example.'}], 'Fix a [contour](definition-use:use-contour).')
        self.assertEqual(first, later)
        self.assertEqual(first[2:], ['eq-authored', 'authored-definition'])
        self.assertRegex(first[0], r'^opening-contours-text-[a-f0-9]+$')
        self.assertRegex(first[1], r'^opening-contours-equation-[a-f0-9]+$')

    def test_diagram_preserves_edge_kind_and_status_with_a_single_coincident_label(self):
        rec = {'id': 'fig-example', 'title': 'Two objects', 'caption': 'The maps between them.',
               'nodes': [{'id': 'a', 'label': 'A'}, {'id': 'b', 'label': 'B'}],
               'edges': [{'id': ident, 'source': 'a', 'target': 'b', 'kind': kind, 'status': status}
                         for ident, kind, status in [('map', 'mathematical_map', 'Defined map'),
                                                     ('compare', 'open_comparison', 'Open problem'),
                                                     ('unmarked', 'mathematical_map', '')]]}
        page = Diagram(self.book, rec).render()
        ids = Elements(page).ids
        item = lambda name: page.split(f'id="fig-example--{name}"', 1)[1].split('</li>', 1)[0]
        self.assertEqual(item('map').split('>', 1)[1].count('Defined map'), 1)
        self.assertEqual(ids['fig-example--map']['data-edge-kind'], 'mathematical_map')
        self.assertEqual(ids['fig-example--map']['data-edge-status'], 'Defined map')
        self.assertIn('Open comparison', item('compare'))
        self.assertIn('Open problem</span>', item('compare'))
        self.assertIn(self.book.mark(status_mark_of('Open problem')), item('compare'))
        self.assertNotIn('data-edge-status', ids['fig-example--unmarked'])

    def test_ordered_cut_graph_wraps_after_difference_and_lists_the_complete_equation(self):
        nodes = [{'id': ident, 'label': r'\(' + start + r'\setminus' + union + r'\)'}
                 for ident, start, union in [('cut-u12', 'U_{1,2}=X^3', r'(\Delta_{12}\cup\Delta_{13})'),
                                             ('cut-u21', 'U_{2,1}=X^3', r'(\Delta_{13}\cup\Delta_{23})')]]
        rec = {'id': 'fig-ordered-cut-support', 'title': 'Ordered cuts', 'caption': 'Their domains.',
               'nodes': nodes, 'edges': []}
        diagram = Diagram(self.book, rec)
        diagram.text = lambda value: value
        page = diagram.render()
        for node in nodes:
            first, rest = node['label'].split(r'\setminus')
            self.assertIn(first + r'\setminus\)<br>\(' + rest, page)
            self.assertIn('class="mg-dg-nd-name">' + node['label'] + '</span>', page)
        self.assertEqual(diagram.plot_node_label({'id': 'other', 'label': nodes[0]['label']}), nodes[0]['label'])

    def test_declarations_and_status(self):
        cases = [
            ('**Corollary.** Hence.', 'corollary', 'proved'),
            ('**Lemma 2.1**. Thus.', 'lemma', 'proved'),
            ('**Theorem A.**', 'theorem', 'proved'),
            ('**Proposition B.**', 'proposition', 'proved'),
            ('**Lemma IV.**', 'lemma', 'proved'),
            ('**Recognition theorem.** It follows.', 'theorem', 'proved'),
            ('**Conditional theorem (affine induction).** Assume H.', 'theorem', 'conditional'),
            ('**Conditional unit theorem for inflated coefficients.** Assume H.', 'theorem', 'conditional'),
            ('**Conditional consequence.** Assume H.', 'consequence', 'conditional'),
            ('**Cofree descent lemma.** Therefore.', 'lemma', 'proved'),
            ('**Conjectural comparison proposition.** We expect it.', 'proposition', 'conjecture'),
            ('**Conjecture.** We expect it.', 'conjecture', 'conjecture'),
            ('**Conditional conjecture.** We expect it under H.', 'conjecture', 'conjecture'),
            ('**Open mapping theorem.** It follows.', 'theorem', 'proved'),
            ('**Theorem (conditional expectation).** It follows.', 'theorem', 'proved'),
            ('**Theorem (the open mapping problem).** It follows.', 'theorem', 'proved'),
            ('**Heuristic.** Formally.', 'heuristic', 'heuristic'),
            ('**Heuristic argument.** Formally.', 'heuristic', 'heuristic'),
            ('**Conditional corollary (Weil positivity).** Assume the hypothesis.', 'corollary', 'conditional'),
            ('**Open question.** Which?', 'open-question', 'open'),
            ('**Problem 18.1.** Determine the map.', 'open-problem', 'open'),
            ('**Definition (the conditional law).** Let x be fixed.', 'definition', None),
            ('**Example of a construction.** Take x.', 'example', None),
            ('_Sketch of the proof._ First reduce.', 'proof-sketch', None),
            ('*Proof of Lemma 2.1.* Choose x.', 'proof', None),
        ]
        for text, kind, status in cases:
            with self.subTest(text=text):
                self.assertEqual(lead_in(text)[0], Form(kind, status))
                html = self.render(text)
                elements = Elements(html).ids
                group = next(iter(elements.values()))
                self.assertEqual((group['data-env'], group.get('data-status')), (kind, status))
                self.assertEqual(group['role'], 'group')
                self.assertIn('data-block-title', elements[group['aria-labelledby']])
                self.assertIn('class="mg-env-name"', html)
                self.assertEqual('data-term' in group, kind == 'definition')
                self.assertEqual('data-result' in group, kind not in ('proof', 'proof-sketch', 'definition'))
        for text in ('Theorem 1. It follows.', 'The **lemma.** is cited.', '*Recognition theorem.* applies.',
                     '**By the theorem.**', '**This is a corollary.**', '**Lemma 2.1 implies descent.**',
                     '**Proof of concept.**', '**Sketch of a deformation.**', '**Conditional expectation.**',
                     '**Theorematic.**', '**Conjectures abound.**', '**Unproved theorem.**', '**Lemma** is a word.'):
            with self.subTest(text=text):
                self.assertIsNone(lead_in(text))

    def test_fences_and_literal_code(self):
        source = ''':::: {.lemma .conditional #lem-norm n="3.2" title="A fixed norm"}
First line.

~~~text
:::
**Corollary.**
~~~

::: proof-sketch {#local-sketch}
Second line.
:::
::::'''
        html = self.render(source)
        ids = Elements(html).ids
        self.assertEqual(ids['lem-norm']['data-env'], 'lemma')
        self.assertEqual(ids['lem-norm']['data-kind'], 'lemma')
        self.assertEqual(ids['lem-norm']['data-result-family'], 'conditional')
        self.assertEqual(ids['lem-norm']['data-status'], 'conditional')
        self.assertIn('Conditional lemma 3.2 (A fixed norm).', html)
        self.assertEqual(ids['local-sketch']['data-env'], 'proof-sketch')
        self.assertIn('<code>:::\n**Corollary.**</code>', html)
        self.assertEqual(html.count('data-env='), 2)
        self.assertNotIn('mg-qed', html)
        self.assertEqual(self.book.problems, [])
        copy = self.render(source, envs=False)
        self.assertNotIn('data-env=', copy)
        self.assertNotIn('id=', copy)
        self.assertIn('Conditional lemma 3.2 (A fixed norm).', copy)
        preserved = self.render('::: conditional-theorem {#fixed n="4.3" title="A fixed norm"}\n'
                                '**Theorem 4.3 (A fixed norm).** Assume H.\n:::')
        self.assertEqual(preserved.count('data-env='), 1)
        self.assertIn('data-status="conditional"', preserved)
        self.assertIn('Conditional theorem 4.3 (A fixed norm).', preserved)

    def test_explicit_and_generated_addresses(self):
        html = self.render('**Proposition (ternary diagonal operations).** Claim.\n\n'
                           '*Proof.* Word. ∎\n\n*Proof.* Other. ∎\n\n'
                           '::: conditional-theorem {#fixed n="4.1"}\nA condition.\n:::\n\n'
                           '::: corollary\n**Corollary (descent).** Hence.\n:::')
        ids = Elements(html).ids
        self.assertIn('ch01-proposition-ternary-diagonal-operations', ids)
        self.assertIn('ch01-proof-2', ids)
        self.assertIn('ch01-corollary-descent', ids)
        self.assertEqual(ids['fixed']['data-kind'], 'theorem')
        self.assertEqual(ids['fixed']['data-result-family'], 'conditional')
        self.assertIn('Conditional theorem 4.1.', html)
        self.assertEqual(html.count('Corollary (descent).'), 1)

    def test_proof_extent_and_end_marks(self):
        html = self.render('*Proof.* Choose x.\n\nNext choose y.\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n'
                           '1. First term.\n2. Last term. ∎\n\nhence a new paragraph.\n\n'
                           '**Lemma**\n\nThe statement is here.\n\n'
                           '*Proof sketch.* First step.\n\nFinal step. □\n\nAnother topic.')
        proof, rest = html.split('</ol></div>', 1)
        self.assertIn('Next choose y.', proof)
        self.assertIn('<table', proof)
        self.assertIn('Last term. ∎', proof)
        self.assertTrue(rest.startswith('<p>hence a new paragraph.</p>'))
        self.assertIn('Lemma</span></span> The statement is here.</p></div>', rest)
        self.assertIn('Final step. □</p></div><p>Another topic.', rest)
        self.assertNotIn('mg-qed', html)
        plain = self.render('*Proof.* A short proof.\n\nA different question.')
        self.assertIn('mg-qed', plain)
        self.assertTrue(plain.endswith('</div><p>A different question.</p>'))

    def test_status_words_used_in_diagrams_and_the_result_index(self):
        for label, expected in [('Corollary', 'checked'), ('Proposition', 'checked'), ('Lemma', 'checked'),
                                ('Conditional theorem', 'conditional'), ('Conjectural lemma', 'conjecture'),
                                ('Theorem on an open set', 'checked'), ('Open mapping theorem', 'checked'),
                                ('Open problem equivalent to a vanishing', 'open'), ('Heuristic', 'heuristic'),
                                ('Counterexample', 'refuted form'), ('Defined map', None),
                                ('A reference to the theorem', None), ('The converse is not proved', None)]:
            with self.subTest(label=label):
                self.assertEqual(status_mark_of(label), expected)
        self.book.section_index = {}
        self.render('**Corollary (descent).** The conclusion.')
        self.book.theorems = {'r': {'id': 'r', 'chapter_id': 'ch01', 'title': 'Corollary (descent)',
                                   'kind': 'theorem', 'status': 'Theorem', 'rendered_anchor': 'ch01-corollary-descent'}}
        html = self.book.results_index()
        self.assertIn('data-index-env="corollary" data-status="proved"', html)
        self.assertIn('class="mg-ri-status">Proved corollary<', html)
        self.assertIn('href="#ch01-corollary-descent"', html)
        self.book.theorems['r']['status'] = 'Conditional result'
        self.assertIn('data-status="conditional"', self.book.results_index())
        self.assertTrue(any('disagrees' in message for message in self.book.problems))

    def test_index_and_glossary_use_the_chapters_link_definitions(self):
        self.book.section_index = {}
        self.book.reference_ids = set()
        self.book.refdefs = {'ch01': {'source': '#ref-first'}, 'ch02': {'source': '#ref-second'}}
        self.book.terms = {'term': {'id': 'term', 'chapter_id': 'ch01', 'label': 'Coefficient',
                                    'definition': 'See [the computation][source].'}}
        self.book.theorems = {'result': {'id': 'result', 'chapter_id': 'ch02', 'title': 'A comparison',
                                         'kind': 'theorem', 'status': 'Proved',
                                         'statement_excerpt': 'Use [the computation][source].'}}
        self.assertIn('href="#ref-first"', self.book.glossary())
        self.assertEqual(self.book.current, 'glossary')
        self.assertIn('href="#ref-second"', self.book.results_index())
        self.assertEqual(self.book.current, 'index')

    def test_native_audit_detects_changed_kind_status_and_label(self):
        html = self.render('**Conditional corollary.** Assume the comparison.')
        for before, after in [(None, None), ('data-env="corollary"', 'data-env="theorem"'),
                              ('data-status="conditional"', 'data-status="proved"'),
                              ('data-block-title', 'data-copy-title'), ('data-result', 'data-term')]:
            with self.subTest(before=before):
                parser = _Attributes()
                parser.feed(html.replace(before, after) if before else html)
                self.assertEqual(bool(environment_errors(parser, self.book.environment_forms)), before is not None)

    def test_exact_index_passages_can_share_a_paragraph_and_a_proof(self):
        book = self.book
        words = 'Use the field on the disk.'
        proof = '*Proof.* Take the trace.'
        def choice(ident, target, paragraph):
            return {'id': ident, 'chapter_id': 'ch01', 'source_target': target, 'source_paragraph': paragraph}
        book.terms = {'f': choice('f', 'old-definition', words), 'p': choice('p', 'start-of-proof', proof)}
        book.theorems = {'r': choice('r', 'disk-reading', words), 's': choice('s', 'disk-reading', words)}
        book.definition_uses.by_id['fixture-use'] = {'target': 'old-definition', 'preview': 'The field.'}
        blocks = parse_blocks(['Use [the field](definition-use:fixture-use) on the disk.', '', proof, '', 'Continue outside.'])
        blocks[0]['passage_id'] = 'old-definition'
        book.bind_index_passages('ch01', blocks)
        markup = book.render(blocks)
        ids = Elements(markup).ids
        self.assertIn('<p id="old-definition"><span id="disk-reading">Use ', markup)
        self.assertIn('data-definition-use="fixture-use"', markup)
        self.assertEqual(book.anchor_kind['disk-reading'], 'text')
        self.assertEqual(book.anchor_kind['old-definition'], 'definition')
        self.assertNotIn('data-env', ids['disk-reading'])
        self.assertIn('<p><span id="start-of-proof"><span class="mg-env-label"', markup)
        self.assertIn('Take the trace.</span>', markup)
        self.assertEqual(list(book.environment_forms.values()), [Form('proof')])
        self.assertIn('</div><p>Continue outside.</p>', markup)
        self.assertEqual(book.problems, [])

    def test_stale_or_ambiguous_index_paragraphs_fail_at_the_source(self):
        book = self.book
        book.terms = {}
        book.theorems = {'r': {'id': 'r', 'chapter_id': 'ch01', 'source_target': 'exact-r',
                               'source_paragraph': 'A chosen sentence.'}}
        for source, error in [('Other words.', 'missing index passages'),
                              ('A chosen sentence.\n\nA chosen sentence.', 'ambiguous index passage')]:
            with self.subTest(error=error), self.assertRaisesRegex(ValueError, error):
                book.bind_index_passages('ch01', parse_blocks(source.splitlines()))

    def test_arithmetic_excerpts_link_to_the_real_chapter_destinations(self):
        self.book.load()
        self.book.section_index = {}
        self.book.reference_ids = set()
        term = self.book.terms['term-weil-functional']
        result = self.book.theorems['ch16-theorem-continuous-integer-summation-duality']
        self.book.terms = {term['id']: term}
        self.book.theorems = {result['id']: result}
        for markup, target, key in [(self.book.glossary(), 'ref-ch16-01', 'trace-foundations'),
                                    (self.book.results_index(), 'ref-ch16-02', 'integer-complex')]:
            with self.subTest(target=target):
                self.assertIn('href="#' + target + '"', markup)
                self.assertNotIn('][' + key + ']', markup)
                self.assertIn('{#' + target + '}', self.book.texts['ch16'])


if __name__ == '__main__':
    unittest.main()
