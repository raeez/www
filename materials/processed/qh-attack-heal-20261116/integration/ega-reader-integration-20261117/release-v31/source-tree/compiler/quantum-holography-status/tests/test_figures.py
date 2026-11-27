"""Tests of figures.py against the figure record contract (FIGURE-RECORD-CONTRACT.md) and the scientific visual
contract: identity, verbatim authored text, the three distinct profile integrals, validity, the authored states of
each model, the meaning of every mark, and named problems. The fixture copies the shapes, formulas, matrices and
rules of the author's records; its reader-facing words are synthetic. Set QH_READER_MANIFEST to an author manifest
to render its real figure records as well."""
import copy
import html
import json
import os
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.dont_write_bytecode = True
import figures as F  # noqa: E402

RECORDS = {r['id']: r for r in json.loads((HERE / 'fixtures' / 'figures-synthetic.json').read_text(encoding='utf-8'))['figures']}
GAUSS, EXP = RECORDS['fig-synthetic-gaussian'], RECORDS['fig-synthetic-expansions']
COH, INF, ADJ = RECORDS['fig-synthetic-cohomology'], RECORDS['fig-synthetic-infinite'], RECORDS['fig-synthetic-adjunction']


class Ctx:
    def rich(self, text, terms=True):
        return html.escape(text, quote=False)


def render(record, ctx=None):
    return F.render(record, ctx or Ctx())


def config(markup):
    return json.loads(html.unescape(re.search(r'data-config="([^"]*)"', markup).group(1)))


def integrate(node, var, env, lo=-40.0, hi=40.0, n=80000):
    h = (hi - lo) / n
    return sum((F.value(node, dict(env, **{var: lo + h * i})) or 0.0) for i in range(n + 1)) * h


def problems_of(record, change):
    bad = copy.deepcopy(record)
    change(bad)
    return render(bad)['problems']


class Formulas(unittest.TestCase):
    def test_typesetting_keeps_every_symbol(self):
        names = ['x', 'a', 'b', 'c', 'hbar']
        self.assertEqual(F.tex(F.parse('a-c^2/b', names)), r'a-\frac{c^{2}}{b}')
        self.assertEqual(F.tex(F.parse('sqrt(2*pi*hbar/b)', names)), r'\sqrt{\frac{2 \pi \hbar}{b}}')
        self.assertEqual(F.tex(F.parse('-c*x/b', names)), r'-\frac{c x}{b}')
        self.assertEqual(F.tex(F.parse('ab>c^2', names)), 'a b > c^{2}')
        self.assertEqual(F.tex(F.parse('z!=w')), r'z \ne w', 'a control word is never glued to the next letter')
        self.assertIn(r'\sum_{n \ge 0}', F.tex(F.parse('sum_(n>=0)(n+1)*w^n/z^(n+2)')))
        self.assertEqual(F.plain_formula(F.parse('|w|<|z|')), '|w| < |z|')

    def test_evaluation(self):
        env = {'a': 2.0, 'b': 1.0, 'c': 0.5, 'x': 1.0, 'hbar': 1.0}
        names = list(env)
        self.assertAlmostEqual(F.value(F.parse('a-c^2/b', names), env), 1.75)
        self.assertAlmostEqual(F.value(F.parse('-c*x/b', names), env), -0.5)
        self.assertIs(F.value(F.parse('b>0 and hbar>0 and a*b>c^2', names), env), True)
        self.assertIs(F.value(F.parse('b>0 and hbar>0 and a*b>c^2', names), dict(env, c=2.0)), False)
        rule = F.parse('i=j and i<N', ('i', 'j', 'N'))
        self.assertIs(F.value(rule, {'i': 2.0, 'j': 2.0, 'N': 3.0}), True)
        self.assertIs(F.value(rule, {'i': 3.0, 'j': 3.0, 'N': 3.0}), False)

    def test_subscripts_are_lowered_and_nothing_else_changes(self):
        self.assertEqual(F.sub_html('ε_FX ∘ F(η_X) = id_FX'),
                         'ε<sub>FX</sub> ∘ F(η<sub>X</sub>) = id<sub>FX</sub>')
        self.assertEqual(F.sub_html('Integrated fixed-x weight Z_y(x)'), 'Integrated fixed-x weight Z<sub>y</sub>(x)')
        svg = F.sub_svg('F(η_X)')
        self.assertEqual(re.sub(r'<[^>]+>', '', svg), 'F(ηX)')
        self.assertIn('dy="4">X</tspan><tspan dy="-4">)</tspan>', svg, 'the baseline returns after a subscript')


class Element(unittest.TestCase):
    def test_identity_hooks_and_reader_vocabulary(self):
        for r in RECORDS.values():
            out = render(r)
            self.assertEqual(out['problems'], [], r['id'])
            tag = re.match(r'<figure [^>]*>', out['html']).group(0)
            for attr in (f'id="{r["id"]}"', f'data-figure="{r["id"]}"', f'data-qh-figure="{r["id"]}"',
                         f'data-figure-type="{r["type"]}"', f'data-figure-model="{r["model"]}"', f'data-figure-chapter="{r["chapter_id"]}"'):
                self.assertIn(attr, tag)
            # the reader's own vocabulary marks chapters and sections; a figure never carries it
            self.assertNotRegex(tag, r'\sdata-(?:chapter|section)=')
            # the order the foundation checks: the id before data-figure
            self.assertRegex(out['html'], rf'<figure\b[^>]*\bid="{re.escape(r["id"])}"[^>]*\bdata-figure\b')
            self.assertIn('class="qh-fig-title" data-block-title>', out['html'], 'the reader names a figure by its title')
            self.assertNotIn('id="fig-fig-', out['html'], 'no second prefix')

    def test_no_id_is_used_twice_on_a_page_of_every_figure(self):
        page = ''.join(render(r)['html'] for r in RECORDS.values())
        ids = re.findall(r'\sid="([^"]+)"', page)
        self.assertEqual(len(ids), len(set(ids)), sorted({i for i in ids if ids.count(i) > 1}))
        for ref in set(re.findall(r'url\(#([^)]+)\)', page)):
            self.assertIn(ref, ids, 'every arrowhead names a marker of its own drawing')

    def test_equation_links(self):
        self.assertIn('href="#eq-synthetic-one">(1.1)</a>', render(GAUSS)['html'], 'a printed number links as itself')
        self.assertIn('href="#eq-synthetic-complex">Equation</a>', render(COH)['html'], 'an unnumbered display links by the interface word')
        self.assertIn('href="#eq-synthetic-complex">Gleichung</a>', render(COH, type('C', (Ctx,), {'words': {'equation': 'Gleichung'}})())['html'],
                      'the page may replace an interface word')

    def test_marks_keep_their_meaning(self):
        css = (HERE.parent / 'figures.css').read_text(encoding='utf-8')
        self.assertNotIn('stroke-dasharray', css, 'dashes are reserved for open comparisons')
        page = ''.join(render(r)['html'] for r in RECORDS.values())
        self.assertNotIn('qh-fig-band', page, 'no band without an authored label')
        self.assertNotIn('qh-fig-area', page, 'no filled area: a window is not the whole mass')


class Gaussian(unittest.TestCase):
    def setUp(self):
        self.out = render(GAUSS)
        self.html = self.out['html']

    def test_every_authored_word_verbatim_and_nothing_invented(self):
        texts = [GAUSS['title'], GAUSS['caption'], GAUSS['validity']['message']] + list(GAUSS['labels'].values())
        texts += [c['label'] for c in GAUSS['controls'].values()] + [p['label'] for p in GAUSS['profiles']]
        formulas = [F.parse(f, list(GAUSS['parameters'])) for f in GAUSS['outputs'].values()]
        texts += [F.prose_formulas(p['caption'], formulas) for p in GAUSS['profiles']]
        for t in texts:
            self.assertIn(html.escape(t, quote=False), self.html)
        self.assertNotIn(GAUSS['prohibited_inferences'][0], self.html)
        self.assertIn('class="qh-fig-invalid" role="status" aria-live="polite" hidden', self.html)

    def test_all_five_controls_with_their_windows(self):
        cfg = config(self.html)
        self.assertEqual(sorted(cfg['controls']), ['a', 'b', 'c', 'hbar', 'x'])
        self.assertEqual(len(re.findall(r'<li class="qh-fig-control"', self.html)), 5)
        self.assertEqual(cfg['controls']['hbar']['max'], 2)

    def test_three_profiles_three_integrals_no_conflation(self):
        env = {n: float(GAUSS['controls'][n]['initial']) for n in GAUSS['parameters']}
        names = list(GAUSS['parameters'])
        for p in GAUSS['profiles']:
            node = F.parse(p['formula'], names + [p['variable']])
            want = F.value(F.parse(p['integral_over_real_line'], names), env)
            self.assertAlmostEqual(integrate(node, p['variable'], env), want, places=4, msg=p['id'])
        self.assertEqual(len(re.findall(r'<div class="qh-fig-profile"', self.html)), 3)

    def test_each_integral_is_one_equation_under_the_same_label_as_the_others(self):
        # G1/G5: each readout is the integral of the plotted function over the real line, in the chapter's notation
        # (\int_{\mathbb R} ... \,dy), then its authored value, then (when that value depends on the parameters) its
        # number. The density's constant 1 is written once: "... = 1", never "1 = 1"; the parts break only between.
        label = '<p class="qh-fig-label">Integral over the real line</p>'
        panel = {seg.split('"', 1)[0]: seg for seg in self.html.split('<div class="qh-fig-profile" data-profile="')[1:]}
        names = list(GAUSS['parameters'])
        for p in GAUSS['profiles']:
            readout = re.search(r'<div class="qh-fig-integral">(.*?)</div>', panel[p['id']], re.S).group(1)
            self.assertTrue(readout.startswith(label), p['id'])
            f = F.tex(F.parse(p['formula'], names + [p['variable']]))
            self.assertIn(f'<span class="qh-fig-seg">\\(\\int_{{\\mathbb R}}{f}\\,d{p["variable"]}\\)</span>', readout, p['id'])
            self.assertIn(f'<span class="qh-fig-seg">\\(={F.tex(F.parse(p["integral_over_real_line"], names))}\\)</span>', readout, p['id'])
        density = re.search(r'<div class="qh-fig-integral">(.*?)</div>', panel['synthetic-density'], re.S).group(1)
        self.assertEqual(density.count('<span class="qh-fig-seg">'), 2, 'the constant: the integral and its value, once')
        self.assertNotIn('<output', density)
        self.assertNotIn('\\(1\\)', density, 'never a bare 1 standing for itself')
        centred = re.search(r'<div class="qh-fig-integral">(.*?)</div>', panel['synthetic-centred'], re.S).group(1)
        self.assertIn('<span class="qh-fig-seg"><span class="qh-fig-eq">=</span> '
                      '<output class="qh-fig-value" data-value="profile:synthetic-centred">2.507</output></span>', centred)
        # G3: labels of one rank are one element: the parameters' label and each integral's label
        self.assertIn('<p class="qh-fig-label">Parameters</p>', self.html)
        self.assertEqual(self.html.count(label), 3)

    def test_one_stated_vertical_scale_for_every_curve(self):
        # G4: every profile is drawn on one vertical scale whose top covers the largest drawn value; each plot states
        # it with ticks at 0, half the top and the top (the same values on every plot) and a hairline at each nonzero
        # tick, and one note says the curves share the scale. No curve is scaled to its own peak.
        env = {n: float(GAUSS['controls'][n]['initial']) for n in GAUSS['parameters']}
        names = list(GAUSS['parameters'])
        top = F.shared_top(GAUSS, env)
        peaks = {p['id']: max(v for _, v in F.samples(F.parse(p['formula'], names + [p['variable']]), p['variable'], env))
                 for p in GAUSS['profiles']}
        self.assertEqual(top, 1.0)
        self.assertAlmostEqual(peaks['synthetic-centred'], 1.0)
        self.assertLess(peaks['synthetic-density'], .5)
        self.assertEqual(self.html.count('<p class="qh-fig-note qh-fig-scale-note">The curves share one vertical scale.</p>'), 1)
        svgs = {seg.split('"', 1)[0]: seg.split('</svg>', 1)[0] for seg in self.html.split('<div class="qh-fig-profile" data-profile="')[1:]}
        for pid, svg in svgs.items():
            ticks = re.findall(r'data-part="scale-(0|mid|top)"[^>]*>([^<]*)<', svg)
            self.assertEqual(ticks, [('0', '0'), ('mid', '0.5'), ('top', '1')], pid)
            self.assertEqual(svg.count('class="qh-fig-guide"'), 2, pid)
            # the highest point of the curve is the profile's peak on that scale, not the top of the box
            ys = [float(y) for y in re.findall(r'[ML]-?[\d.]+ (-?[\d.]+)', re.search(r'data-part="curve" d="([^"]+)"', svg).group(1))]
            self.assertAlmostEqual(min(ys), F.scale_y(peaks[pid], top), places=1, msg=pid)
        # at the corner of the display windows where the density peaks above 1 (b = 4, hbar = 0.25), the scale's top is 2
        self.assertEqual(F.shared_top(GAUSS, dict(env, b=4.0, hbar=0.25)), 2)
        self.assertEqual([F.nice_top(m) for m in (0.399, 1.0, 1.596, 0.09, 4.2)], [0.5, 1.0, 2, 0.1, 5])

    def test_a_negative_value_is_written_with_the_minus_sign(self):
        # G5: as in the typeset formulas beside it, never a hyphen-minus
        self.assertEqual([F.fmt(v) for v in (-0.5, -0.0, 0.0, 2.507, -1.25)], ['\u22120.5', '0', '0', '2.507', '\u22121.25'])
        mean = re.search(r'data-value="conditional_mean">([^<]*)<', self.html).group(1)
        self.assertEqual(mean, '\u22120.5')
        self.assertNotRegex(re.sub(r'<[^>]+>', ' ', self.html), r'(?<![\w\\])-\d', 'no number with a hyphen-minus in the text')

    def test_the_records_own_formulas_are_typeset_where_a_caption_spells_them(self):
        # G2: "-cx/b" and "ħ/b" in an authored caption are the record's outputs conditional_mean and
        # conditional_variance; they are set as those formulas. Nothing else changes: a single symbol and a formula
        # the record does not have ("1/t") stay as written, and no word is added or removed.
        cap = re.search(r'data-profile="synthetic-density".*?<p class="qh-fig-profile-caption">(.*?)</p>', self.html, re.S).group(1)
        self.assertEqual(cap, 'Synthetic density caption: mean \\(-\\frac{c x}{b}\\) and variance \\(\\frac{\\hbar}{b}\\); a b and 1/t stay as written.')
        back = re.sub(r'\\\(-\\frac\{c x\}\{b\}\\\)', '-cx/b', re.sub(r'\\\(\\frac\{\\hbar\}\{b\}\\\)', '\u0127/b', cap))
        self.assertEqual(back, next(p for p in GAUSS['profiles'] if p['id'] == 'synthetic-density')['caption'])
        self.assertEqual(F.prose_formulas('mean \\(x\\) and -cx/b', []), 'mean \\(x\\) and -cx/b', 'a caption with TeX goes through whole')

    def test_the_host_pages_paragraph_rules_stop_at_the_figure(self):
        # G3: a host's p + p indent, justification and p margins do not reach the figure's own paragraphs.
        css = (HERE.parent / 'figures.css').read_text(encoding='utf-8')
        self.assertIn('figure.qh-fig p, figure.qh-fig p + p { text-indent: 0; text-align: left; }', css)
        for k in ('label', 'invalid', 'profile-label', 'profile-caption', 'note', 'explanation', 'cond', 'matrix', 'homotopy',
                  'col-head', 'equation', 'integral', 'integral-value'):
            self.assertRegex(css, rf'\n\.qh-fig \.qh-fig-{k} \{{[^}}]*margin', k)

    def test_the_mean_carries_its_authored_label_on_the_density_only(self):
        density = re.search(r'data-profile="synthetic-density".*?</div>', self.html, re.S).group(0)
        self.assertIn('data-part="mean"', density)
        self.assertIn('data-part="mean-label"', density)
        self.assertIn('Synthetic mean label', density)
        self.assertEqual(self.html.count('data-part="mean"'), 1)

    def test_decimal_singular_initial_state_and_mean_outside_plot(self):
        record = copy.deepcopy(GAUSS)
        for name, initial in {'a': 0.4, 'b': 0.9, 'c': 0.6}.items():
            record['controls'][name]['initial'] = initial
        self.assertTrue(any('break the validity rule' in message for message in render(record)['problems']))

        for name, initial in {'a': 4, 'b': 0.25, 'c': 0.95, 'x': 2}.items():
            record['controls'][name]['initial'] = initial
        result = render(record)
        self.assertEqual(result['problems'], [])
        for part in ('mean', 'mean-label'):
            self.assertRegex(result['html'], rf'data-part="{part}"[^>]*display="none"')
        self.assertIn('data-value="conditional_mean">−7.6', result['html'])

    def test_named_problems(self):
        self.assertTrue(any('is not one this component draws' in p for p in problems_of(GAUSS, lambda r: r.update(model='composition-domains'))))
        self.assertTrue(any('output normalization has no label' in p for p in problems_of(GAUSS, lambda r: r['labels'].pop('normalization'))))
        self.assertTrue(any('break the validity rule' in p for p in problems_of(GAUSS, lambda r: r['controls']['c'].update(initial=1.9))))
        self.assertTrue(any('equation 1.2 has no anchor' in p for p in problems_of(GAUSS, lambda r: r['equation_anchors'].pop('1.2'))))
        bad = copy.deepcopy(GAUSS)
        bad['equation_anchors'].pop('1.2')
        self.assertEqual(render(bad)['html'], '', 'a record with a problem draws nothing')


class Expansions(unittest.TestCase):
    def setUp(self):
        self.out = render(EXP)
        self.html = self.out['html']

    def test_two_authored_states_initial_chosen_no_truncation(self):
        self.assertEqual(len(re.findall(r'<li class="qh-fig-state"', self.html)), 2)
        self.assertIn('data-state="w-inside-z" aria-current="true"', self.html)
        self.assertNotIn('<input', self.html, 'no truncation control')
        for t in [s['label'] for s in EXP['states']] + list(EXP['labels'].values()):
            self.assertIn(html.escape(t, quote=False), self.html)
        self.assertIn(r'\sum_{n \ge 0}', self.html)

    def test_labels_attached_to_their_marks(self):
        plane = re.search(r'<svg class="qh-fig-svg qh-fig-plane".*?</svg>', self.html, re.S).group(0)
        self.assertIn('data-part="region-label"', plane)
        self.assertIn('>|w| &lt; |z|</text>', plane, 'the region carries its authored condition')
        self.assertIn('Synthetic pole label</text>', plane, 'the pole carries its authored label')
        self.assertEqual(config(self.html)['states'][1], {'id': 'z-inside-w', 'inside': False, 'text': '|z| < |w|', 'at': [14, 26, 'start']})

    def test_states_are_required_and_read(self):
        self.assertTrue(any('initial_state' in p for p in problems_of(EXP, lambda r: r.update(initial_state='nowhere'))))
        self.assertTrue(any('not a comparison of |w| with |z|' in p for p in problems_of(EXP, lambda r: r['states'][0].update(condition='|w|<2'))))


class Cohomology(unittest.TestCase):
    def setUp(self):
        self.html = render(COH)['html']

    def test_the_initial_state_is_drawn_from_its_matrix(self):
        svg = re.search(r'<svg class="qh-fig-svg qh-fig-complex".*?</svg>', self.html, re.S).group(0)
        # t = 0: the first arrow ends at 0, there is no contraction, and all four basis vectors survive
        self.assertIn(f'data-part="first" d="{F.first_arrow(False)[0]}"', svg)
        self.assertNotIn('data-part="first-zero" x="226" y="97" text-anchor="middle" display="none"', svg)
        self.assertRegex(svg, r'data-part="h"[^>]*display="none"')
        self.assertEqual(len(re.findall(r'class="qh-fig-basis is-alive"', svg)), 4)
        for t in ('Synthetic degree zero', 'Synthetic degree one', 'u₁ ↦ t v₁', 'u₂ ↦ 0'):
            self.assertIn(t, svg)

    def test_every_state_its_matrix_contraction_dimensions_and_survivors(self):
        self.assertEqual(len(re.findall(r'<li class="qh-fig-state"', self.html)), 3)
        self.assertEqual(self.html.count(r'\begin{pmatrix}'), 3)
        self.assertIn(r'\operatorname{diag}(t,0)=\begin{pmatrix}-1&amp;0\\0&amp;0\end{pmatrix}', self.html)
        rows = re.findall(r'<tr data-state-row="([^"]+)"', self.html)
        self.assertEqual(rows, ['negative', 'zero', 'positive'])
        zero = re.search(r'<tr data-state-row="zero".*?</tr>', self.html, re.S).group(0)
        self.assertEqual(re.findall(r'class="qh-fig-chip">([^<]+)<', zero), ['u₁', 'u₂', 'v₁', 'v₂'])
        for st in COH['states']:
            self.assertIn(st['homotopy'], self.html)
        cfg = config(self.html)
        self.assertEqual([s['h'] for s in cfg['states']], ['Synthetic contraction at minus one', '', 'Synthetic contraction at one'])
        self.assertEqual([s['toV'] for s in cfg['states']], [True, False, True])

    def test_the_records_arithmetic_is_returned_to_the_author_when_it_disagrees(self):
        self.assertTrue(any('disagrees with its matrix' in p for p in problems_of(COH, lambda r: r['states'][0].update(rank=0))))
        self.assertTrue(any('cohomology dimensions disagree' in p for p in problems_of(COH, lambda r: r['states'][1].update(H0_dim=1))))
        self.assertTrue(any('another nonzero entry' in p for p in problems_of(COH, lambda r: r['states'][0].update(differential_matrix=[[-1, 0], [0, 2]]))))
        self.assertTrue(any('must name the first and second basis vectors' in p
                            for p in problems_of(COH, lambda r: r['labels'].update(first_arrow='v₁ ↦ u₁'))))


class InfiniteRank(unittest.TestCase):
    def setUp(self):
        self.html = render(INF)['html']

    def grid(self, part):
        return re.search(rf'<svg class="qh-fig-svg qh-fig-grid" data-grid="{part}".*?</svg>', self.html, re.S).group(0)

    def test_both_states_in_one_viewport_by_their_rules(self):
        fin, lim = self.grid('finite-truncation'), self.grid('coordinatewise-limit')
        self.assertEqual(re.findall(r'class="qh-fig-cell is-on" data-i="(\d)" data-j="(\d)"', fin), [('0', '0'), ('1', '1'), ('2', '2')])
        self.assertEqual(len(re.findall(r'class="qh-fig-cell is-on"', lim)), 8)
        self.assertEqual(len(re.findall(r'class="qh-fig-cell', fin)), 64)
        self.assertNotIn('qh-fig-continues is-on', fin, 'beyond the viewport D(N) is zero')
        self.assertIn('qh-fig-continues is-on', lim, 'beyond the viewport the identity continues')

    def test_ranks_memberships_and_words(self):
        table = re.search(r'<table class="qh-fig-outputs qh-fig-compare">.*?</table>', self.html, re.S).group(0)
        self.assertIn('data-value="rank:finite-truncation">3</output>', table)
        self.assertIn('<td>infinite</td>', table)
        self.assertEqual(re.findall(r'<td>(yes|no)</td>', table), ['yes', 'no', 'yes', 'yes'])
        for t in list(INF['labels'].values()) + [s['explanation'] for s in INF['states']] + [INF['domain'], INF['controls']['N']['label']]:
            self.assertIn(html.escape(t, quote=False), self.html)

    def test_ranks_must_match_the_outputs(self):
        self.assertTrue(any('finite_rank and outputs.limit_rank' in p for p in problems_of(INF, lambda r: r['states'][1].update(rank='countable'))))


class Adjunction(unittest.TestCase):
    def setUp(self):
        self.html = render(ADJ)['html']

    def test_two_triangles_their_arrows_and_the_key(self):
        tris = re.findall(r'<svg class="qh-fig-svg qh-fig-triangle".*?</svg>', self.html, re.S)
        self.assertEqual(len(tris), 2)
        for t in tris:
            self.assertEqual(len(re.findall(r'<g class="qh-fig-arrow', t)), 3)
        self.assertEqual(re.findall(r'<g class="qh-fig-arrow( is-unit| is-counit)?">', tris[0]), [' is-unit', ' is-counit', ''])
        self.assertEqual(re.findall(r'<g class="qh-fig-arrow( is-unit| is-counit)?">', tris[1]), [' is-unit', ' is-counit', ''])
        self.assertIn('<span class="qh-fig-sym is-counit">ε</span><sub>FX</sub> ∘ F(<span class="qh-fig-sym is-unit">η</span><sub>X</sub>) = id<sub>FX</sub>', self.html)
        self.assertEqual(re.findall(r'data-key="(\w+)"', self.html), ['F', 'G', 'eta', 'epsilon'])

    def test_criteria_and_domain(self):
        rows = re.search(r'<table class="qh-fig-outputs qh-fig-properties">.*?</table>', self.html, re.S).group(0)
        self.assertEqual(rows.count('<tr>'), 3)
        for p in ADJ['properties']:
            self.assertIn(p['equivalent_statement'], rows)
        self.assertIn(ADJ['domain'], self.html)


class Assets(unittest.TestCase):
    def test_shipped_style_and_script_carry_no_forbidden_word(self):
        try:
            import audit
        except ImportError:
            self.skipTest('audit.py is not beside figures.py')
        a = F.assets()
        for name in ('css', 'js'):
            hits = [m.group(0) for pattern, why, flags in audit.FORBIDDEN for m in re.finditer(pattern, a[name], flags)
                    if not (name == 'css' and why == 'percentage')]
            self.assertEqual(hits, [], name)
        self.assertNotRegex(a['js'], r'pushState|replaceState|location\.(?:hash|href)\s*=(?!=)', 'figures never write the address')


class AuthorManifest(unittest.TestCase):
    def test_the_authors_records_render_without_a_problem(self):
        path = os.environ.get('QH_READER_MANIFEST')
        if not path or not Path(path).exists():
            self.skipTest('QH_READER_MANIFEST is not set')
        seen = []
        for r in json.loads(Path(path).read_text(encoding='utf-8')).get('figures') or []:
            if r.get('model') in F.MODELS:
                out = render(r)
                self.assertEqual(out['problems'], [], r['id'])
                self.assertTrue(out['html'].startswith(f'<figure class="qh-fig" id="{r["id"]}"'))
                seen.append(r['model'])
        self.assertEqual(sorted(set(seen)), sorted(F.MODELS), 'every authorized model has an authored record')


if __name__ == '__main__':
    unittest.main()
