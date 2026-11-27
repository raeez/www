"""Figures of the reader: the author's figure records drawn as figures, with their controls.

The reader places a figure with the one-line hook `::: figure <figure-id>` in a chapter and calls
render(record, ctx) for the record of that id in reader-data/manifest.json (FIGURE-RECORD-CONTRACT.md). The
figure's DOM id is the record id verbatim; the element carries data-figure and data-qh-figure (the id),
data-figure-type (the record's type) and data-figure-chapter and data-figure-section (the record's chapter and
section; the reader's own data-chapter and data-section mark its chapters and sections, never a figure). Its title
carries data-block-title, the reader's name for the figure in its search and reminders. Every word and formula a figure shows is the author's record: title,
caption, control labels and display windows, output and domain labels, the validity message, the profiles
with their captions and integrals, and the state labels and series. The atlas lane adds only layout, the
drawing, the controls themselves and the evaluation of the authored formulas. Nothing listed under
prohibited_inferences is drawn; a plotted window is never presented as a whole integral. A record this
component cannot honour fails the build with each problem named, and no guessed figure is ever drawn.

Models drawn (record field `model`, the five the visual contract authorizes): gaussian-elimination,
two-expansions, cohomology-jump, infinite-rank and adjunction-triangles. Labels written with an underscore
subscript (η_X, ε_FX) are set with the subscript lowered; no other change is made to an authored string.
"""
import html
import json
import math
import re
from fractions import Fraction

MODELS = ('gaussian-elimination', 'two-expansions', 'cohomology-jump', 'infinite-rank', 'adjunction-triangles')
TYPES = ('authored_formula', 'authored_finite_states', 'authored_diagram')
STATE_MODELS = ('two-expansions', 'cohomology-jump', 'infinite-rank', 'adjunction-triangles')
CONSTANTS = {'pi': math.pi}
FUNCTIONS = ('sqrt', 'exp')
# The interface words, the only words a figure adds to the author's record; the page may replace any of them
# (ctx.words), as it may the reader's own.
WORDS = {'controls': 'Parameters', 'outputs': 'Values at these parameters', 'equations': 'Equations',
         'equation': 'Equation', 'integral': 'Integral over the real line', 'yes': 'yes', 'no': 'no',
         'hypothesis': 'Hypothesis', 'equivalent': 'Equivalent statement',
         'scale': 'The curves share one vertical scale.'}


# Formulas ---------------------------------------------------------------------------------------------------
# The authored linear syntax: numbers, names, + - * / ^, juxtaposition, f(...), |...|, comparisons, `and`, and
# sum_(condition)term. Parsed once into a tree that is typeset (TeX, symbol for symbol) and evaluated.

TOKEN = re.compile(r'\s*(?:(\d+(?:\.\d+)?)|([A-Za-z]+)|(<=|>=|!=|==|[-+*/^()<>=|_,]))')


class FormulaError(ValueError):
    pass


def tokens(text):
    out, i = [], 0
    while i < len(text):
        if text[i].isspace():
            i += 1
            continue
        m = TOKEN.match(text, i)
        if not m or m.end() == i:
            raise FormulaError(f'cannot read {text[i:]!r}')
        num, name, op = m.groups()
        out.append(('num', num) if num else ('name', name) if name else ('op', op))
        i = m.end()
    return out


class Parser:
    def __init__(self, text, names):
        self.toks = tokens(text)
        self.i = 0
        self.names = set(names) | set(CONSTANTS) | {'hbar'}
        self.in_abs = 0

    def peek(self, kind=None, value=None):
        if self.i >= len(self.toks):
            return None
        t = self.toks[self.i]
        if (kind and t[0] != kind) or (value and t[1] != value):
            return None
        return t

    def take(self, kind=None, value=None):
        t = self.peek(kind, value)
        if not t:
            raise FormulaError(f'expected {value or kind} at token {self.i}')
        self.i += 1
        return t

    def parse(self):
        node = self.conj()
        if self.i != len(self.toks):
            raise FormulaError(f'unread input from token {self.i}')
        return node

    def conj(self):
        node = self.cmp()
        while self.peek('name', 'and'):
            self.i += 1
            node = ['and', node, self.cmp()]
        return node

    def cmp(self):
        left = self.add()
        t = self.peek('op')
        if t and t[1] in ('<', '>', '<=', '>=', '!=', '==', '='):
            self.i += 1
            return ['cmp', '==' if t[1] == '=' else t[1], left, self.add()]
        return left

    def add(self):
        if self.peek('op', '-'):  # a leading minus applies to the whole first term: -c*x/b = -(c x / b)
            self.i += 1
            node = ['neg', self.mul()]
        else:
            node = self.mul()
        while self.peek('op') and self.peek('op')[1] in '+-':
            op = self.take('op')[1]
            node = ['add' if op == '+' else 'sub', node, self.mul()]
        return node

    def starts_atom(self):
        t = self.peek()
        if t is None or (t[0] == 'name' and t[1] == 'and'):
            return False
        return t[0] in ('num', 'name') or (t[0] == 'op' and (t[1] == '(' or (t[1] == '|' and not self.in_abs)))

    def mul(self):
        node = self.unary()
        while True:
            t = self.peek('op')
            if t and t[1] in '*/':
                self.i += 1
                node = ['mul' if t[1] == '*' else 'div', node, self.unary()]
            elif self.starts_atom():
                node = ['mul', node, self.unary()]  # juxtaposition
            else:
                return node

    def unary(self):
        if self.peek('op', '-'):
            self.i += 1
            return ['neg', self.unary()]
        return self.power()

    def power(self):
        base = self.atom()
        if self.peek('op', '^'):
            self.i += 1
            return ['pow', base, self.unary()]
        return base

    def atom(self):
        t = self.peek()
        if t is None:
            raise FormulaError('formula ends early')
        if t[0] == 'num':
            self.i += 1
            return ['num', float(t[1]) if '.' in t[1] else int(t[1])]
        if t[0] == 'op' and t[1] == '(':
            self.i += 1
            node = self.conj()
            self.take('op', ')')
            return ['group', node]
        if t[0] == 'op' and t[1] == '|':
            self.i += 1
            self.in_abs += 1
            node = self.add()
            self.in_abs -= 1
            self.take('op', '|')
            return ['abs', node]
        if t[0] == 'name':
            self.i += 1
            name = t[1]
            if name == 'sum' and self.peek('op', '_'):
                self.i += 1
                self.take('op', '(')
                cond = self.cmp()
                self.take('op', ')')
                return ['sum', cond, self.mul()]
            if name in FUNCTIONS and self.peek('op', '('):
                self.i += 1
                arg = self.conj()
                self.take('op', ')')
                return ['call', name, arg]
            if name in self.names or len(name) == 1:
                return ['var', name]
            node = ['var', name[0]]  # juxtaposed single-letter names, e.g. "ab" in "ab>c^2"
            for ch in name[1:]:
                node = ['mul', node, ['var', ch]]
            return node
        raise FormulaError(f'unexpected {t[1]!r}')


def parse(text, names=()):
    return Parser(str(text), names).parse()


def variables(node):
    if node[0] == 'var':
        return {node[1]}
    out = set()
    for part in node[1:]:
        if isinstance(part, list):
            out |= variables(part)
    return out


PREC = {'and': -1, 'cmp': 0, 'add': 1, 'sub': 1, 'neg': 1, 'mul': 2, 'div': 3, 'pow': 4, 'sum': 1}


def tex(node):
    """The authored formula in TeX, symbol for symbol."""
    k = node[0]
    if k == 'num':
        return str(node[1])
    if k == 'var':
        return {'hbar': r'\hbar', 'pi': r'\pi'}.get(node[1], node[1])
    if k == 'group':
        inner = node[1]
        return tex(inner) if inner[0] in ('var', 'num', 'call', 'abs', 'pow', 'group') else f'\\left({tex(inner)}\\right)'
    if k == 'abs':
        return f'\\lvert {tex(node[1])}\\rvert'
    if k == 'neg':
        return '-' + wrap(node[1], 2)
    if k in ('add', 'sub'):
        return f'{tex(node[1])}{"+" if k == "add" else "-"}{wrap(node[2], 1 if k == "add" else 2)}'
    if k == 'mul':
        return f'{wrap(node[1], 2)} {wrap(node[2], 2)}'
    if k == 'div':
        return f'\\frac{{{tex(unbracket(node[1]))}}}{{{tex(unbracket(node[2]))}}}'
    if k == 'pow':
        return f'{wrap(node[1], 5)}^{{{tex(unbracket(node[2]))}}}'
    if k == 'call':
        if node[1] == 'sqrt':
            return f'\\sqrt{{{tex(unbracket(node[2]))}}}'
        return f'\\{node[1]}\\left({tex(unbracket(node[2]))}\\right)'
    if k == 'cmp':
        op = {'<': '<', '>': '>', '<=': r'\le', '>=': r'\ge', '!=': r'\ne', '==': '='}[node[1]]
        return f'{tex(node[2])} {op} {tex(node[3])}'
    if k == 'and':
        return f'{tex(node[1])},\\ {tex(node[2])}'
    if k == 'sum':
        return f'\\sum_{{{tex(node[1])}}} {tex(node[2])}'
    raise FormulaError(f'cannot typeset {k}')


def unbracket(node):
    return node[1] if node[0] == 'group' else node


def wrap(node, prec):
    inner = tex(node)
    if PREC.get(node[0], 9) < prec and node[0] != 'group':
        return f'\\left({inner}\\right)'
    return inner


def grid_value(node, env):
    """Evaluate decimal controls and literals exactly for validity and window comparisons."""
    def decimal(v):
        return Fraction(str(v))
    return value(node, {n: decimal(v) for n, v in env.items()}, decimal)


def value(node, env, number=float):
    """The authored formula evaluated at the parameters; None where it has no number (a series)."""
    k = node[0]
    if k == 'num':
        return number(node[1])
    if k == 'var':
        return env.get(node[1], CONSTANTS.get(node[1]))
    if k in ('group', 'abs', 'neg'):
        v = value(node[1], env, number)
        if k == 'group':
            return v
        if v is None or isinstance(v, bool):
            return None
        return abs(v) if k == 'abs' else -v
    if k in ('add', 'sub', 'mul', 'div', 'pow'):
        a, b = value(node[1], env, number), value(node[2], env, number)
        if a is None or b is None or isinstance(a, bool) or isinstance(b, bool):
            return None
        try:
            return {'add': lambda: a + b, 'sub': lambda: a - b, 'mul': lambda: a * b,
                    'div': lambda: a / b, 'pow': lambda: a ** b}[k]()
        except (ZeroDivisionError, OverflowError, ValueError):
            return None
    if k == 'call':
        v = value(node[2], env, number)
        if v is None or isinstance(v, bool):
            return None
        if node[1] == 'sqrt':
            return math.sqrt(v) if v >= 0 else None
        if node[1] == 'exp':
            return math.exp(v) if v < 700 else None
    if k == 'cmp':
        a, b = value(node[2], env, number), value(node[3], env, number)
        if a is None or b is None:
            return None
        return {'<': a < b, '>': a > b, '<=': a <= b, '>=': a >= b, '!=': a != b, '==': a == b}[node[1]]
    if k == 'and':
        return value(node[1], env, number) is True and value(node[2], env, number) is True
    return None


def math_inline(t):
    return '\\(' + t + '\\)'


def fmt(v):
    """A value as the figure writes it: at most three decimals, and a negative value with the minus sign (U+2212),
    as in the typeset formulas beside it, never a hyphen."""
    if v is None:
        return ''
    if v != 0 and (abs(v) >= 1000 or abs(v) < 0.001):
        text = f'{v:.3g}'
    else:
        text = f'{v:.3f}'.rstrip('0').rstrip('.')
    text = text.replace('-', '\u2212')
    return '0' if text == '\u22120' else text


# Checks ----------------------------------------------------------------------------------------------------

def check(record):
    """Problems of a record: each names the figure and the field. Any problem fails the build."""
    problems = []
    rid = record.get('id', '?')

    def err(text):
        problems.append(f'figure {rid}: {text}')
    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', str(rid)):
        err('id must be lower-case words joined by hyphens')
    for key in ('title', 'caption', 'chapter_id', 'type'):
        if not isinstance(record.get(key), str) or not record[key].strip():
            err(f'{key} is required')
    model = record.get('model')
    if model not in MODELS:
        err(f'model {model!r} is not one this component draws ({", ".join(MODELS)})')
        return problems
    if record.get('type') not in TYPES:
        err(f'type {record.get("type")!r} is not one this component draws')
    if model in ('cohomology-jump', 'infinite-rank', 'adjunction-triangles'):
        problems += check_finite(record, err)
        return problems + reader_rules(record, err)
    for ref in record.get('equation_refs') or []:
        if ref not in (record.get('equation_anchors') or {}):
            err(f'equation {ref} has no anchor in equation_anchors')
    labels = record.get('labels') or {}
    if model == 'gaussian-elimination':
        params = record.get('parameters') or {}
        controls = record.get('controls') or {}
        names = list(params)
        for name in record.get('permitted_controls') or []:
            c = controls.get(name)
            if name not in params:
                err(f'permitted control {name!r} is not a parameter')
            if not c or not all(k in c for k in ('initial', 'min', 'max', 'step', 'label')):
                err(f'control {name!r} needs initial, min, max, step and label')
            elif not (c['min'] <= c['initial'] <= c['max']) or c['step'] <= 0:
                err(f'control {name!r}: its initial value lies outside its window, or its step is not positive')
        for name in names:
            if name not in controls:
                err(f'parameter {name!r} has no control with an initial value')
        env = {n: float((controls.get(n) or {}).get('initial', 0)) for n in names}
        allowed = set(names) | set(CONSTANTS)
        validity = record.get('validity') or {}
        if not validity.get('rule') or not validity.get('message'):
            err('validity needs a rule and a message')
        else:
            try:
                node = parse(validity['rule'], names)
                if variables(node) - allowed:
                    err(f'validity uses {sorted(variables(node) - allowed)}, which are not parameters')
                elif grid_value(node, env) is not True:
                    err('the initial parameters break the validity rule')
            except FormulaError as e:
                err(f'validity: {e}')
        if 'domain' not in labels:
            err('labels.domain is required')
        for key, formula in (record.get('outputs') or {}).items():
            if key not in labels:
                err(f'output {key} has no label')
            try:
                node = parse(formula, names)
            except FormulaError as e:
                err(f'output {key}: {e}')
                continue
            if variables(node) - allowed:
                err(f'output {key} uses {sorted(variables(node) - allowed)}, which are not parameters')
            elif value(node, env) is None:
                err(f'output {key} has no value at the initial parameters')
        for j, p in enumerate(record.get('profiles') or []):
            for key in ('id', 'label', 'variable', 'formula', 'integral_over_real_line', 'caption'):
                if not p.get(key):
                    err(f'profiles[{j}].{key} is required')
            try:
                f = parse(p.get('formula', ''), names + [p.get('variable', '')])
                i = parse(p.get('integral_over_real_line', ''), names)
                if variables(f) - allowed - {p.get('variable')} or variables(i) - allowed:
                    err(f'profiles[{j}] uses names that are neither parameters nor its variable')
            except FormulaError as e:
                err(f'profiles[{j}]: {e}')
    else:
        states = record.get('states') or []
        ids = [s.get('id') for s in states]
        if len(states) < 2:
            err('two-expansions needs its authored states')
        for j, st in enumerate(states):
            for key in ('id', 'condition', 'series', 'label'):
                if not st.get(key):
                    err(f'states[{j}].{key} is required')
            for key in ('condition', 'series'):
                try:
                    parse(st.get(key, ''))
                except FormulaError as e:
                    err(f'states[{j}].{key}: {e}')
            try:
                inside_disk(st.get('condition', ''))
            except FormulaError as e:
                err(f'states[{j}]: {e}')
        if record.get('initial_state') not in ids:
            err('initial_state must name one of the states')
        for key in ('domain', 'series', 'pole', 'no_value'):
            if key not in labels:
                err(f'labels.{key} is required')
    return problems + reader_rules(record, err)


def strings(record):
    """Every reader-facing string of a record, for the page's reader rules."""
    out = [record.get('title'), record.get('caption'), record.get('domain') if isinstance(record.get('domain'), str) else None]
    out += [str(v) for v in (record.get('labels') or {}).values()]
    out += [c.get('label') for c in (record.get('controls') or {}).values()]
    out += [p.get(k) for p in record.get('profiles') or [] for k in ('label', 'caption')]
    for st in record.get('states') or []:
        out += [st.get(k) for k in ('label', 'homotopy', 'equation', 'meaning', 'explanation') if isinstance(st.get(k), str)]
        out += [n.get('label') for n in st.get('nodes') or []] + [a.get('label') for a in st.get('arrows') or []]
    out += [p.get(k) for p in record.get('properties') or [] for k in ('hypothesis', 'equivalent_statement', 'explanation')]
    out.append((record.get('validity') or {}).get('message'))
    return [t for t in out if t]


def reader_rules(record, err):
    try:
        import audit
    except ImportError:
        return []
    for t in strings(record):
        for pattern, why, flags in audit.FORBIDDEN:
            m = re.search(pattern, t, flags)
            if m:
                err(f'{why} {m.group(0)!r} in {t[:60]!r}')
    return []


def problems_so_far(record):
    """True when a state of a cohomology record lacks the fields the basis check reads."""
    return any(not isinstance((st.get('surviving_basis') or {}).get(k), list) for st in record.get('states') or [] for k in ('H0', 'H1'))


def check_finite(record, err):
    """The finite-state models: every field the drawing reads, and the record's own arithmetic (returned to the
    author when it disagrees, never corrected here)."""
    model = record['model']
    labels = record.get('labels') or {}
    states = record.get('states') or []
    ids = [s.get('id') for s in states]
    if len(states) < 2 or len(set(ids)) != len(ids):
        err('the states must be at least two, with distinct ids')
    if record.get('initial_state') not in ids:
        err('initial_state must name one of the states')
    need = {'cohomology-jump': ('degree_zero', 'degree_one', 'first_arrow', 'second_arrow', 'H0', 'H1', 'Euler_characteristic', 'homotopy'),
            'infinite-rank': ('finite', 'limit', 'rank', 'tensor_membership', 'completion_membership', 'viewport', 'convergence'),
            'adjunction-triangles': ('F', 'G', 'eta', 'epsilon', 'left_triangle', 'right_triangle')}[model]
    for key in need:
        if key not in labels:
            err(f'labels.{key} is required')
    for j, st in enumerate(states):
        if not st.get('label'):
            err(f'states[{j}].label is required')
        if model == 'cohomology-jump':
            m = st.get('differential_matrix')
            if not (isinstance(m, list) and len(m) == 2 and all(isinstance(r, list) and len(r) == 2 for r in m)):
                err(f'states[{j}].differential_matrix must be 2 by 2')
                continue
            det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
            rank = 2 if det else (1 if any(v for r in m for v in r) else 0)
            for key in ('rank', 'H0_dim', 'H1_dim', 'Euler_characteristic', 'homotopy', 'surviving_basis'):
                if key not in st:
                    err(f'states[{j}].{key} is required')
            if st.get('rank') != rank:
                err(f'states[{j}]: rank {st.get("rank")} disagrees with its matrix (rank {rank})')
            if st.get('H0_dim') != 2 - rank or st.get('H1_dim') != 2 - rank:
                err(f'states[{j}]: the cohomology dimensions disagree with the rank')
            if st.get('Euler_characteristic') != (st.get('H0_dim') or 0) - (st.get('H1_dim') or 0):
                err(f'states[{j}]: the Euler characteristic is not dim H0 - dim H1')
            sb = st.get('surviving_basis') or {}
            if len(sb.get('H0') or []) != st.get('H0_dim') or len(sb.get('H1') or []) != st.get('H1_dim'):
                err(f'states[{j}]: the surviving basis disagrees with the dimensions')
            if m[0][1] or m[1][0] or m[1][1]:
                err(f'states[{j}]: the drawing shows diag(t,0); this matrix has another nonzero entry')
        elif model == 'infinite-rank':
            for key in ('entry_rule', 'rank', 'explanation'):
                if not st.get(key):
                    err(f'states[{j}].{key} is required')
            for key in ('algebraic_tensor_member', 'completion_member'):
                if not isinstance(st.get(key), bool):
                    err(f'states[{j}].{key} must be true or false')
            try:
                parse(st.get('entry_rule', ''), ('i', 'j', 'N'))
            except FormulaError as e:
                err(f'states[{j}].entry_rule: {e}')
        else:
            nodes = {n.get('id') for n in st.get('nodes') or []}
            if len(st.get('nodes') or []) != 3 or not all(n.get('label') for n in st.get('nodes') or []):
                err(f'states[{j}] needs its three labelled nodes')
            for a in st.get('arrows') or []:
                if a.get('from') not in nodes or a.get('to') not in nodes or not a.get('label'):
                    err(f'states[{j}]: an arrow needs a label and endpoints among its nodes')
            for key in ('equation', 'meaning'):
                if not st.get(key):
                    err(f'states[{j}].{key} is required')
    if model == 'cohomology-jump' and not problems_so_far(record):
        us, vs = basis_names(record)
        if len(us) != 2 or len(vs) != 2:
            err('each degree needs two basis vectors, named in the states\' surviving bases')
        elif not (labels.get('first_arrow', '').startswith(us[0]) and vs[0] in labels.get('first_arrow', '')
                  and labels.get('second_arrow', '').startswith(us[1])):
            err('labels.first_arrow and labels.second_arrow must name the first and second basis vectors')
    if model == 'infinite-rank':
        outs = record.get('outputs') or {}
        ranks = sorted(str(st.get('rank')) for st in states)
        if ranks != sorted([str(outs.get('finite_rank')), str(outs.get('limit_rank'))]):
            err('the states\' ranks must be outputs.finite_rank and outputs.limit_rank, one each')
        c = (record.get('controls') or {}).get('N') or {}
        if not all(k in c for k in ('initial', 'min', 'max', 'step', 'label')):
            err('controls.N needs initial, min, max, step and label')
        if not isinstance((record.get('outputs') or {}).get('viewport_size'), int):
            err('outputs.viewport_size must be a whole number')
    if model == 'adjunction-triangles':
        for j, p in enumerate(record.get('properties') or []):
            for key in ('hypothesis', 'equivalent_statement', 'explanation'):
                if not p.get(key):
                    err(f'properties[{j}].{key} is required')
    return []


# Drawing ---------------------------------------------------------------------------------------------------
# Every mark a figure draws has its meaning in the figure. A curve is an authored function over a finite window of
# its variable; no area is filled, so a window never reads as a whole integral. A solid arrow is a defined map and
# carries its authored label. A ring marks a basis vector the record lists as surviving in cohomology, and the
# same ring marks that vector's name in the table. A cell holds the matrix entry its authored rule gives. Dashes
# are kept for open comparisons and are not used here. The script redraws with the same geometry.

PANEL_W, PANEL_H, PAD, SPAN = 300, 150, 18, 4.0
# A profile plot: the vertical scale on the left (its line at SCALE_X, labelled ticks at 0, half the top and the top),
# the variable's axis along the base, and the window of the variable from WIN_X0 to WIN_X1.
SCALE_X, WIN_X0, WIN_X1, AXIS_X1 = 34, 42, 278, 288
BASE_Y, TOP_Y = PANEL_H - PAD, 26
SUB = re.compile(r'_([A-Za-z0-9′\']+)')
CMP_TEXT = {'<': '<', '>': '>', '<=': '≤', '>=': '≥', '!=': '≠', '==': '='}


def esc(t):
    return html.escape(str(t), quote=False)


def attr(t):
    return html.escape(str(t), quote=True)


def sub_html(text):
    """An authored label with its underscore subscripts lowered (eta_X, id_FX, Z_y(x)); every character kept."""
    out, i = [], 0
    for m in SUB.finditer(text):
        out.append(esc(text[i:m.start()]))
        out.append(f'<sub>{esc(m.group(1))}</sub>')
        i = m.end()
    out.append(esc(text[i:]))
    return ''.join(out)


def sub_svg(text):
    """The same for SVG text: a lowered tspan, and the baseline restored for what follows it."""
    out, i, low = [], 0, False
    for m in SUB.finditer(text):
        before = text[i:m.start()]
        if before:
            out.append(f'<tspan dy="-4">{esc(before)}</tspan>' if low else esc(before))
            low = False
        out.append(f'<tspan class="qh-fig-sub" dy="{0 if low else 4}">{esc(m.group(1))}</tspan>')
        low = True
        i = m.end()
    if text[i:]:
        out.append(f'<tspan dy="-4">{esc(text[i:])}</tspan>' if low else esc(text[i:]))
    return ''.join(out)


def rich_label(text, rich):
    """An authored label through the page's renderer, its underscore subscripts lowered. A label that carries TeX
    of its own goes through whole."""
    if not SUB.search(text) or any(d in text for d in ('\\(', '\\[', '$')):
        return rich(text)
    out, i = [], 0
    for m in SUB.finditer(text):
        if m.start() > i:
            out.append(rich(text[i:m.start()]))
        out.append(f'<sub>{esc(m.group(1))}</sub>')
        i = m.end()
    if i < len(text):
        out.append(rich(text[i:]))
    return ''.join(out)


def tint(markup, symbols):
    """Marks each occurrence of a symbol (eta, epsilon) with the class its arrows carry, so that a symbol in an
    equation or the key and the arrows built from it share one colour."""
    for sym, cls in symbols.items():
        if sym:
            markup = markup.replace(sym, f'<span class="{cls}">{sym}</span>')
    return markup


def marker(mid, cls='qh-fig-head-mark'):
    return (f'<marker id="{mid}" viewBox="0 0 8 8" refX="7.4" refY="4" markerWidth="7" markerHeight="7" '
            f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0.6 7.6 4 0 7.4z" class="{cls}"/></marker>')


def plain_formula(node):
    """A short authored formula as text for a drawing, symbol for symbol: |w|<|z| is set |w| < |z|."""
    k = node[0]
    if k == 'var':
        return node[1]
    if k == 'num':
        return str(node[1])
    if k == 'abs':
        return f'|{plain_formula(node[1])}|'
    if k == 'group':
        return f'({plain_formula(node[1])})'
    if k == 'neg':
        return '−' + plain_formula(node[1])
    if k == 'cmp':
        return f'{plain_formula(node[2])} {CMP_TEXT[node[1]]} {plain_formula(node[3])}'
    if k in ('add', 'sub'):
        return f'{plain_formula(node[1])} {"+" if k == "add" else chr(0x2212)} {plain_formula(node[2])}'
    if k == 'mul':
        return plain_formula(node[1]) + plain_formula(node[2])
    raise FormulaError(f'cannot set {k} in a drawing')


def inside_disk(condition):
    """True for |w| < |z| (w inside the circle of radius |z|), False for |z| < |w|, read from the authored
    condition; any other condition is returned to the author."""
    n = parse(condition)
    if n[0] == 'cmp' and n[1] in ('<', '>') and n[2][0] == 'abs' and n[3][0] == 'abs':
        a, b = n[2][1], n[3][1]
        if a == ['var', 'w'] and b == ['var', 'z']:
            return n[1] == '<'
        if a == ['var', 'z'] and b == ['var', 'w']:
            return n[1] == '>'
    raise FormulaError(f'the condition {condition!r} is not a comparison of |w| with |z|')


def output_tex(text):
    """An authored output written as a function name and arguments, diag(t,0), set as an operator name."""
    m = re.fullmatch(r'([A-Za-z]+)\((.*)\)', text.strip())
    return f'\\operatorname{{{m.group(1)}}}({m.group(2)})' if m else text


# The Gaussian profiles

def window_x(t):
    return WIN_X0 + (t + SPAN) / (2 * SPAN) * (WIN_X1 - WIN_X0)


def scale_y(v, top):
    """The height of a value on the shared vertical scale from 0 (the base) to top."""
    return BASE_Y - min(v / top, 1.06) * (BASE_Y - TOP_Y)


def samples(node, var, env):
    """The drawn values of a profile: 161 points across the window, a value without a number drawn as 0."""
    out = []
    for i in range(161):
        t = -SPAN + 2 * SPAN * i / 160
        v = value(node, dict(env, **{var: t}))
        out.append((t, 0.0 if v is None or isinstance(v, bool) else v))
    return out


def profile_path(node, var, env, top):
    return 'M' + ' L'.join(f'{window_x(t):.1f} {scale_y(v, top):.1f}' for t, v in samples(node, var, env))


def is_density(p):
    return str(p.get('integral_over_real_line')).strip() == '1'


def nice_top(m):
    """The top of the shared vertical scale: the least of 1, 2, 5 or 10 times a power of ten at or above the largest
    drawn value (a peak of exactly 1 gives the scale 0 to 1)."""
    if not m or m <= 0 or not math.isfinite(m):
        return 1.0
    m *= 1 - 1e-9
    e = 10 ** math.floor(math.log10(m))
    return next(k * e for k in (1, 2, 5, 10) if k * e >= m)


def shared_top(record, env):
    """One vertical scale for every profile of the figure at these parameters: its top covers the largest value
    drawn in any of them, so heights compare across the plots and every curve keeps its true height."""
    names = list(record['parameters'])
    peak = 0.0
    for p in record.get('profiles') or []:
        node = parse(p['formula'], names + [p['variable']])
        peak = max([peak] + [v for _, v in samples(node, p['variable'], env)])
    return nice_top(peak)


def scale_marks(top):
    """The stated scale of a profile plot: its line, ticks at 0, half the top and the top with their values, and a
    hairline across the plot at the two nonzero ticks. The script rewrites the two values when the top changes."""
    out = [f'<path class="qh-fig-axis" d="M{SCALE_X} {BASE_Y}V{TOP_Y - 4}"/>']
    for part, v in (('scale-0', 0.0), ('scale-mid', top / 2), ('scale-top', top)):
        y = scale_y(v, top)
        if v:
            out.append(f'<path class="qh-fig-guide" d="M{SCALE_X} {y:.1f}H{WIN_X1}"/>')
        out.append(f'<path class="qh-fig-axis" d="M{SCALE_X - 4} {y:.1f}H{SCALE_X}"/>'
                   f'<text class="qh-fig-tick qh-fig-scale-tick" data-part="{part}" x="{SCALE_X - 7}" y="{y + 4.5:.1f}" '
                   f'text-anchor="end">{fmt(v)}</text>')
    return ''.join(out)


def mean_mark(mean, label):
    """The conditional mean on the density, as a line with its authored label attached at its head."""
    visible = mean is not None and -SPAN <= mean <= SPAN
    display = '' if visible else ' display="none"'
    x = window_x(mean if visible else 0)
    right = x > PANEL_W / 2
    return (f'<line class="qh-fig-mean" data-part="mean"{display} x1="{x:.1f}" y1="{PAD - 4}" x2="{x:.1f}" y2="{PANEL_H - PAD}"/>'
            f'<text class="qh-fig-mark-label" data-part="mean-label"{display} x="{x - 5 if right else x + 5:.1f}" y="{PAD - 7}" '
            f'text-anchor="{"end" if right else "start"}">{sub_svg(label)}</text>')


def profile_svg(record, p, env, top):
    """One profile on the figure's shared vertical scale (top), stated on the plot by its labelled ticks; the
    variable's axis runs to the right of the window, where the real line continues."""
    names = list(record['parameters'])
    node = parse(p['formula'], names + [p['variable']])
    outs, labels = record.get('outputs') or {}, record.get('labels') or {}
    marks = ''
    if is_density(p) and p['variable'] == 'y' and 'conditional_mean' in outs and labels.get('conditional_mean'):
        mean = grid_value(parse(outs['conditional_mean'], names), env)
        marks = mean_mark(mean, labels['conditional_mean'])
    zero = window_x(0)
    return (f'<svg class="qh-fig-svg" viewBox="0 0 {PANEL_W} {PANEL_H}" aria-hidden="true" focusable="false">'
            f'{scale_marks(top)}'
            f'<path class="qh-fig-curve" data-part="curve" d="{profile_path(node, p["variable"], env, top)}"/>'
            f'{marks}<path class="qh-fig-axis" d="M{SCALE_X} {BASE_Y}H{AXIS_X1}"/>'
            f'<path class="qh-fig-axis" d="M{zero:.1f} {BASE_Y}v4"/>'
            f'<path class="qh-fig-more" d="M{AXIS_X1} {BASE_Y}l-5 -3v6z"/>'
            f'<text class="qh-fig-tick" x="{zero:.1f}" y="{PANEL_H - 1}" text-anchor="middle">0</text>'
            f'<text class="qh-fig-tick qh-fig-var" x="{WIN_X1}" y="{PANEL_H - 1}" text-anchor="end">{esc(p["variable"])}</text></svg>')


# The two expansions: the w-plane at a fixed z

PLANE = (360, 232, 150, 120, 76)  # width, height, centre x, centre y, radius |z|


def region_shape(inside):
    W, H, cx, cy, r = PLANE
    if inside:
        return f'<circle class="qh-fig-region" data-part="region" cx="{cx}" cy="{cy}" r="{r}"/>'
    return (f'<path class="qh-fig-region" data-part="region" fill-rule="evenodd" '
            f'd="M2 2H{W - 2}V{H - 2}H2Z M{cx + r} {cy}a{r} {r} 0 1 0 -{2 * r} 0a{r} {r} 0 1 0 {2 * r} 0Z"/>')


def region_label_at(inside):
    """Where the chosen region's condition is written: inside the disk, in its upper left quadrant, clear of the
    axes and the circle; outside it, in the upper left corner."""
    W, H, cx, cy, r = PLANE
    return (cx - 38, cy - 16, 'middle') if inside else (14, 26, 'start')


def plane_svg(state, labels):
    """The chosen region with its authored condition written in it, the circle between the two conditions, and
    the collision pole w = z on that circle with its authored label; no value is drawn at the pole."""
    W, H, cx, cy, r = PLANE
    inside = inside_disk(state['condition'])
    lx, ly, anchor = region_label_at(inside)
    px, py = cx + r * math.cos(-1.0), cy + r * math.sin(-1.0)
    cond = plain_formula(parse(state['condition']))
    return (f'<svg class="qh-fig-svg qh-fig-plane" viewBox="0 0 {W} {H}" role="img" aria-label="{attr(cond + "; " + labels["pole"])}">'
            f'{region_shape(inside)}'
            f'<circle class="qh-fig-boundary" cx="{cx}" cy="{cy}" r="{r}"/>'
            f'<path class="qh-fig-axis" d="M{cx - r - 30} {cy}H{cx + r + 30}M{cx} {cy + r + 20}V{cy - r - 20}"/>'
            f'<circle class="qh-fig-origin" cx="{cx}" cy="{cy}" r="2.4"/>'
            f'<text class="qh-fig-tick" x="{cx - 6}" y="{cy + 15}" text-anchor="end">0</text>'
            f'<text class="qh-fig-region-label" data-part="region-label" x="{lx}" y="{ly}" text-anchor="{anchor}">{esc(cond)}</text>'
            f'<g class="qh-fig-pole" transform="translate({px:.1f} {py:.1f})"><circle r="6.5"/>'
            f'<path d="M-3.4 -3.4L3.4 3.4M3.4 -3.4L-3.4 3.4"/></g>'
            f'<text class="qh-fig-mark-label qh-fig-pole-text" x="{px + 12:.1f}" y="{py - 8:.1f}">{sub_svg(labels["pole"])}</text></svg>')


# The cohomology jump: the complex on its authored basis

CJ = {'W': 460, 'H': 232, 'x0': 110, 'x1': 350, 'y1': 92, 'y2': 192, 'zero': 226}


def basis_names(record):
    """The basis of each degree, read from the states' surviving bases (at the jump every basis vector survives)."""
    h0 = sorted({n for st in record['states'] for n in (st.get('surviving_basis') or {}).get('H0') or []})
    h1 = sorted({n for st in record['states'] for n in (st.get('surviving_basis') or {}).get('H1') or []})
    return h0, h1


def first_arrow(to_v):
    """The first summand's arrow: to v1 where the matrix entry is nonzero, to 0 where it is zero."""
    c = CJ
    end = c['x1'] - 24 if to_v else c['zero'] - 14
    return f'M{c["x0"] + 22} {c["y1"]}H{end}', (c['x0'] + 22 + end) / 2


def complex_svg(record, st):
    c, labels, rid = CJ, record['labels'], record['id']
    us, vs = basis_names(record)
    alive = set(st['surviving_basis']['H0']) | set(st['surviving_basis']['H1'])
    to_v = st['differential_matrix'][0][0] != 0
    d1, mid1 = first_arrow(to_v)
    hide_zero = ' display="none"' if to_v else ''
    hide_h = '' if to_v else ' display="none"'
    h_text = st['homotopy'] if to_v else ''

    def node(name, x, y):
        return (f'<g class="qh-fig-basis{" is-alive" if name in alive else ""}" data-basis="{attr(name)}" transform="translate({x} {y})">'
                f'<circle class="qh-fig-ring" r="17"/><text class="qh-fig-node-text" y="5" text-anchor="middle">{esc(name)}</text></g>')
    name = '; '.join([labels['degree_zero'], labels['degree_one'], labels['first_arrow'], labels['second_arrow']])
    zero_end = c['zero'] - 14
    return (f'<svg class="qh-fig-svg qh-fig-complex" viewBox="0 0 {c["W"]} {c["H"]}" role="img" aria-label="{attr(name)}">'
            f'<defs>{marker(rid + "--arrow")}{marker(rid + "--arrow-h", "qh-fig-head-h")}</defs>'
            f'<text class="qh-fig-col-label" x="{c["x0"]}" y="24" text-anchor="middle">{esc(labels["degree_zero"])}</text>'
            f'<text class="qh-fig-col-label" x="{c["x1"]}" y="24" text-anchor="middle">{esc(labels["degree_one"])}</text>'
            f'<path class="qh-fig-map" data-part="first" d="{d1}" marker-end="url(#{rid}--arrow)"/>'
            f'<text class="qh-fig-zero" data-part="first-zero" x="{c["zero"]}" y="{c["y1"] + 5}" text-anchor="middle"{hide_zero}>0</text>'
            f'<text class="qh-fig-map-label" data-part="first-label" x="{mid1:.0f}" y="{c["y1"] - 12}" text-anchor="middle">{esc(labels["first_arrow"])}</text>'
            f'<path class="qh-fig-map" d="M{c["x0"] + 22} {c["y2"]}H{zero_end}" marker-end="url(#{rid}--arrow)"/>'
            f'<text class="qh-fig-zero" x="{c["zero"]}" y="{c["y2"] + 5}" text-anchor="middle">0</text>'
            f'<text class="qh-fig-map-label" x="{(c["x0"] + 22 + zero_end) / 2:.0f}" y="{c["y2"] - 12}" text-anchor="middle">{esc(labels["second_arrow"])}</text>'
            f'<path class="qh-fig-homotopy-arc" data-part="h" d="M{c["x1"] - 12} {c["y1"] + 16}C{c["x1"] - 50} {c["y1"] + 58} '
            f'{c["x0"] + 50} {c["y1"] + 58} {c["x0"] + 14} {c["y1"] + 17}" marker-end="url(#{rid}--arrow-h)"{hide_h}/>'
            f'<text class="qh-fig-h-label" data-part="h-label" x="{(c["x0"] + c["x1"]) / 2:.0f}" y="{c["y1"] + 64}" text-anchor="middle"{hide_h}>{esc(h_text)}</text>'
            + node(us[0], c['x0'], c['y1']) + node(us[1], c['x0'], c['y2'])
            + node(vs[0], c['x1'], c['y1']) + node(vs[1], c['x1'], c['y2']) + '</svg>')


def matrix_tex(m):
    return r'\begin{pmatrix}' + r'\\'.join('&'.join(str(v) for v in row) for row in m) + r'\end{pmatrix}'


def state_items(states, initial, inner):
    """The authored states as a list; the script turns each label into a button. Without the script every state is
    shown in full, the initial one marked current."""
    return ''.join(
        f'<li class="qh-fig-state" data-state="{attr(st["id"])}"' + (' aria-current="true"' if st['id'] == initial else '') + '>'
        f'<p class="qh-fig-state-label">{esc(st["label"])}</p>{inner(st)}</li>' for st in states)


def render_cohomology(record, rich, words):
    """The two-term complex on its authored basis for the chosen value of t: the first summand's arrow goes to v1
    where the state's matrix entry is nonzero and to 0 where it is zero; the contraction, where the state gives one,
    is drawn back from v1 to u1 with the state's own formula; the vectors the state lists as surviving are ringed.
    Beside it, the state's matrix and contraction text; under it, the dimensions and Euler characteristic of every
    state, with the surviving vectors named."""
    labels, states, initial = record['labels'], record['states'], record['initial_state']
    cur = next(st for st in states if st['id'] == initial)
    differential = output_tex((record.get('outputs') or {}).get('differential', ''))

    def inner(st):
        tex_src = '\\(' + (differential + '=' if differential else '') + matrix_tex(st['differential_matrix']) + '\\)'
        return (f'<div class="qh-fig-per-state"><p class="qh-fig-matrix">{rich(tex_src)}</p>'
                f'<p class="qh-fig-homotopy"><span class="qh-fig-label">{esc(labels["homotopy"])}</span>'
                f'<span class="qh-fig-homotopy-text">{esc(st["homotopy"])}</span></p></div>')

    def chips(names):
        return ''.join(f'<span class="qh-fig-chip">{esc(n)}</span>' for n in names)
    rows = ''.join(
        f'<tr data-state-row="{attr(st["id"])}"' + (' aria-current="true"' if st['id'] == initial else '') + '>'
        f'<th scope="row">{esc(st["label"])}</th>'
        f'<td><span class="qh-fig-dim">{st["H0_dim"]}</span>{chips(st["surviving_basis"]["H0"])}</td>'
        f'<td><span class="qh-fig-dim">{st["H1_dim"]}</span>{chips(st["surviving_basis"]["H1"])}</td>'
        f'<td class="qh-fig-num">{st["Euler_characteristic"]}</td></tr>' for st in states)
    table = (f'<table class="qh-fig-outputs qh-fig-dims"><thead><tr><td></td>'
             f'<th scope="col">{esc(labels["H0"])}</th><th scope="col">{esc(labels["H1"])}</th>'
             f'<th scope="col" class="qh-fig-num">{esc(labels["Euler_characteristic"])}</th></tr></thead><tbody>{rows}</tbody></table>')
    body = (f'<div class="qh-fig-body"><div class="qh-fig-side"><p class="qh-fig-domain">{esc(record["domain"])}</p>'
            f'<ol class="qh-fig-states qh-fig-states-compact">{state_items(states, initial, inner)}</ol></div>'
            f'<div class="qh-fig-stage">{complex_svg(record, cur)}{table}</div></div>')
    us, vs = basis_names(record)
    first_mid = {True: first_arrow(True)[1], False: first_arrow(False)[1]}
    config = {'model': 'cohomology-jump', 'initial': initial,
              'paths': {'v': first_arrow(True)[0], 'zero': first_arrow(False)[0]}, 'mids': {'v': first_mid[True], 'zero': first_mid[False]},
              'states': [{'id': st['id'], 'toV': st['differential_matrix'][0][0] != 0,
                          'alive': st['surviving_basis']['H0'] + st['surviving_basis']['H1'],
                          'h': st['homotopy'] if st['differential_matrix'][0][0] != 0 else ''} for st in states]}
    return body, config


# The infinite rank: the finite diagonal and its coordinatewise limit, each in the same finite viewport

GRID = {'cell': 24, 'left': 30, 'top': 28}


def grid_svg(part, rule, env, n, name):
    """A viewport of rows and columns 0 to n-1. Each cell holds the entry the state's authored rule gives (1 or 0);
    the bracket opens on the left only and the mark at the lower right says the matrix continues; that mark carries
    the accent where the rule gives 1 on the diagonal beyond the viewport."""
    g = GRID
    size = n * g['cell']
    W, H = g['left'] + size + 22, g['top'] + size + 24
    out = []
    for k in range(n):
        out.append(f'<text class="qh-fig-tick" x="{g["left"] + k * g["cell"] + g["cell"] / 2:.0f}" y="{g["top"] - 8}" text-anchor="middle">{k}</text>'
                   f'<text class="qh-fig-tick" x="{g["left"] - 9}" y="{g["top"] + k * g["cell"] + g["cell"] / 2 + 4:.0f}" text-anchor="end">{k}</text>')
    for i in range(n):
        for j in range(n):
            on = value(rule, dict(env, i=i, j=j)) is True
            x, y = g['left'] + j * g['cell'], g['top'] + i * g['cell']
            out.append(f'<g class="qh-fig-cell{" is-on" if on else ""}" data-i="{i}" data-j="{j}">'
                       f'<rect x="{x + 1.5}" y="{y + 1.5}" width="{g["cell"] - 3}" height="{g["cell"] - 3}" rx="2.5"/>'
                       f'<text x="{x + g["cell"] / 2:.0f}" y="{y + g["cell"] / 2 + 4.5:.1f}" text-anchor="middle">{1 if on else 0}</text></g>')
    beyond = value(rule, dict(env, i=n, j=n)) is True
    b = g['left'] - 3
    out.append(f'<path class="qh-fig-bracket" d="M{b + 4} {g["top"]}H{b}V{g["top"] + size}H{b + 4}"/>'
               f'<text class="qh-fig-continues{" is-on" if beyond else ""}" data-part="beyond" x="{g["left"] + size + 3}" '
               f'y="{g["top"] + size + 15}">⋱</text>'
               f'<text class="qh-fig-tick qh-fig-var" x="{g["left"] + size + 6}" y="{g["top"] - 8}">j</text>'
               f'<text class="qh-fig-tick qh-fig-var" x="{g["left"] - 9}" y="{g["top"] + size + 16}" text-anchor="end">i</text>')
    return (f'<svg class="qh-fig-svg qh-fig-grid" data-grid="{attr(part)}" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="{attr(name)}">' + ''.join(out) + '</svg>')


def rank_value(st, env):
    """The state's authored rank evaluated at the control (N), or its authored word where it has no number."""
    try:
        v = value(parse(st['rank'], ('N',)), env)
    except FormulaError:
        v = None
    return fmt(v) if isinstance(v, float) else esc(st['rank'])


def infinite_pair(record):
    by_rank = {st['rank']: st for st in record['states']}
    outs = record['outputs']
    return by_rank[outs['finite_rank']], by_rank[outs['limit_rank']]


def render_infinite(record, rich, words):
    """The finite diagonal D(N), with the authored control N, beside its coordinatewise limit, both in the same
    authored viewport; under them the authored convergence statement and a table of the two states' ranks and
    memberships. A state is shown with the label its rank names in the record (finite_rank or limit_rank)."""
    labels, outs, rid = record['labels'], record['outputs'], record['id']
    n = outs['viewport_size']
    ctl = record['controls']['N']
    env = {'N': float(ctl['initial'])}
    fin, lim = infinite_pair(record)
    rules = {st['id']: parse(st['entry_rule'], ('i', 'j', 'N')) for st in (fin, lim)}

    def column(st, key, control=''):
        return (f'<div class="qh-fig-col" data-state="{attr(st["id"])}">'
                f'<p class="qh-fig-col-head">{esc(labels[key])}</p>{control}'
                f'{grid_svg(st["id"], rules[st["id"]], env, n, labels[key] + ". " + labels["viewport"])}'
                f'<p class="qh-fig-explanation">{esc(st["explanation"])}</p></div>')
    control = (f'<div class="qh-fig-control" data-param="N">'
               f'<label class="qh-fig-control-label" for="{rid}--N">{esc(ctl["label"])}</label>'
               f'<output class="qh-fig-value" data-value="N">{fmt(env["N"])}</output></div>')

    def yes(b):
        return words['yes'] if b else words['no']
    table = (f'<table class="qh-fig-outputs qh-fig-compare"><thead><tr><td></td>'
             f'<th scope="col">{esc(labels["finite"])}</th><th scope="col">{esc(labels["limit"])}</th></tr></thead><tbody>'
             f'<tr><th scope="row">{esc(labels["rank"])}</th>'
             f'<td><output class="qh-fig-value" data-value="rank:{attr(fin["id"])}">{rank_value(fin, env)}</output></td>'
             f'<td>{rank_value(lim, env)}</td></tr>'
             f'<tr><th scope="row">{esc(labels["tensor_membership"])}</th><td>{yes(fin["algebraic_tensor_member"])}</td>'
             f'<td>{yes(lim["algebraic_tensor_member"])}</td></tr>'
             f'<tr><th scope="row">{esc(labels["completion_membership"])}</th><td>{yes(fin["completion_member"])}</td>'
             f'<td>{yes(lim["completion_member"])}</td></tr></tbody></table>')
    body = (f'<div class="qh-fig-body qh-fig-body-single"><p class="qh-fig-domain">{esc(record["domain"])}</p>'
            f'<div class="qh-fig-pair">{column(fin, "finite", control)}{column(lim, "limit")}</div>'
            f'<p class="qh-fig-note">{esc(labels["viewport"])}</p>'
            f'<p class="qh-fig-convergence">{esc(labels["convergence"])}</p>{table}</div>')
    try:
        fin_rank = parse(fin['rank'], ('N',))
    except FormulaError:
        fin_rank = None
    config = {'model': 'infinite-rank', 'n': n, 'control': ctl,
              'grids': [{'id': st['id'], 'rule': rules[st['id']]} for st in (fin, lim)],
              'rank': {'id': fin['id'], 'formula': fin_rank}}
    return body, config


# The adjunction triangles

def clearance(half_w, ux, uy, half_h=11.0):
    """How far along the direction (ux, uy) a label box of these half sizes reaches from its centre."""
    tx = half_w / abs(ux) if abs(ux) > 1e-9 else float('inf')
    ty = half_h / abs(uy) if abs(uy) > 1e-9 else float('inf')
    return min(tx, ty)


def greek(text):
    return next((ch for ch in text if 'Ͱ' <= ch <= 'Ͽ'), '')


def triangle_svg(rid, st, eta, eps):
    """A triangle identity as a commutative triangle: the start at the lower left, the middle object at the top, the
    end at the lower right, every arrow with its authored label set beside it, outside the triangle. Arrows built
    from the unit carry the unit's colour and arrows built from the counit the counit's, as in the key."""
    W, H = 300, 196
    order = [nd['id'] for nd in st['nodes']]
    names = {nd['id']: nd['label'] for nd in st['nodes']}
    pos = {order[0]: (44, 156), order[1]: (150, 40), order[2]: (256, 156)}
    cx, cy = 150, 117
    half = {k: 4.6 * len(names[k]) + 9 for k in order}
    marks = {'': rid + '--' + st['id'] + '--arrow', 'is-unit': rid + '--' + st['id'] + '--unit',
             'is-counit': rid + '--' + st['id'] + '--counit'}
    parts = []
    for a in st['arrows']:
        (x1, y1), (x2, y2) = pos[a['from']], pos[a['to']]
        d = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / d, (y2 - y1) / d
        s1, s2 = clearance(half[a['from']], ux, uy), clearance(half[a['to']], ux, uy) + 3
        ax, ay, bx, by = x1 + ux * s1, y1 + uy * s1, x2 - ux * s2, y2 - uy * s2
        mx, my = (ax + bx) / 2, (ay + by) / 2
        nx, ny = -uy, ux
        if (mx + nx - cx) ** 2 + (my + ny - cy) ** 2 < (mx - cx) ** 2 + (my - cy) ** 2:
            nx, ny = -nx, -ny
        lx, ly = mx + nx * 13, my + ny * 13 + (4 if ny >= 0 else 0) + (10 if ny > 0.9 else 0)
        anchor = 'middle' if abs(nx) < 0.3 else ('start' if nx > 0 else 'end')
        cls = 'is-unit' if eta and eta in a['label'] else ('is-counit' if eps and eps in a['label'] else '')
        parts.append(f'<g class="qh-fig-arrow{" " + cls if cls else ""}">'
                     f'<path class="qh-fig-map" d="M{ax:.1f} {ay:.1f}L{bx:.1f} {by:.1f}" marker-end="url(#{marks[cls]})"/>'
                     f'<text class="qh-fig-map-label" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}">{sub_svg(a["label"])}</text></g>')
    nodes = ''.join(f'<text class="qh-fig-node-text" x="{pos[k][0]}" y="{pos[k][1] + 5}" text-anchor="middle">{sub_svg(names[k])}</text>'
                    for k in order)
    defs = (marker(marks['']) + marker(marks['is-unit'], 'qh-fig-head-mark is-unit') +
            marker(marks['is-counit'], 'qh-fig-head-mark is-counit'))
    return (f'<svg class="qh-fig-svg qh-fig-triangle" viewBox="0 0 {W} {H}" role="img" aria-label="{attr(st["equation"])}">'
            f'<defs>{defs}</defs>{"".join(parts)}{nodes}</svg>')


def render_adjunction(record, rich, words):
    """The key to the adjunction's data (its two functors, unit and counit, in the record's words), the record's
    domain sentence, the two triangle identities side by side, each with its authored equation and meaning, and
    the authored criteria comparing invertibility of the unit or counit with full faithfulness and equivalence."""
    labels, states, rid = record['labels'], record['states'], record['id']
    eta, eps = greek(labels['eta']), greek(labels['epsilon'])
    symbols = {eta: 'qh-fig-sym is-unit', eps: 'qh-fig-sym is-counit'}
    keys = []
    for key, cls in (('F', ''), ('G', ''), ('eta', 'is-unit'), ('epsilon', 'is-counit')):
        swatch = '<span class="qh-fig-swatch" aria-hidden="true"></span>' if cls else ''
        keys.append(f'<li class="qh-fig-key{" " + cls if cls else ""}" data-key="{key}">{swatch}'
                    f'<span class="qh-fig-key-text">{tint(sub_html(labels[key]), symbols)}</span></li>')
    triangles = ''.join(
        f'<li class="qh-fig-col" data-state="{attr(st["id"])}"><p class="qh-fig-col-head">{esc(st["label"])}</p>'
        f'{triangle_svg(rid, st, eta, eps)}<p class="qh-fig-equation">{tint(sub_html(st["equation"]), symbols)}</p>'
        f'<p class="qh-fig-explanation">{esc(st["meaning"])}</p></li>' for st in states)
    props = ''.join(
        f'<tr><td>{tint(sub_html(p["hypothesis"]), symbols)}</td><td><span class="qh-fig-strong">{sub_html(p["equivalent_statement"])}</span>'
        f'<span class="qh-fig-explanation">{sub_html(p["explanation"])}</span></td></tr>' for p in record.get('properties') or [])
    table = (f'<table class="qh-fig-outputs qh-fig-properties"><thead><tr><th scope="col">{esc(words["hypothesis"])}</th>'
             f'<th scope="col">{esc(words["equivalent"])}</th></tr></thead><tbody>{props}</tbody></table>') if props else ''
    body = (f'<div class="qh-fig-body qh-fig-body-single"><ul class="qh-fig-legend">{"".join(keys)}</ul>'
            f'<p class="qh-fig-domain">{esc(record["domain"])}</p>'
            f'<ol class="qh-fig-pair qh-fig-triangles">{triangles}</ol>{table}</div>')
    return body, {'model': 'adjunction-triangles', 'initial': record['initial_state'], 'states': [st['id'] for st in states]}


FINITE_RENDERERS = {'cohomology-jump': render_cohomology, 'infinite-rank': render_infinite,
                    'adjunction-triangles': render_adjunction}


# Rendering -------------------------------------------------------------------------------------------------

def head_html(record, rich, words):
    """The title (marked data-block-title, the reader's name for the figure in its search and reminders) and the
    links to the chapter's equations: a printed number links as (1.3); an anchor of an unnumbered display links
    under the interface word for an equation."""
    anchors = record.get('equation_anchors') or {}
    refs = record.get('equation_refs') or []
    links = [f'<a href="#{attr(anchors[e])}">({esc(e)})</a>' for e in refs]
    links += [f'<a href="#{attr(a)}">{esc(words["equation"])}</a>' for k, a in anchors.items() if k not in refs]
    label = f'<span class="qh-fig-label">{esc(words["equations"])}</span> ' if refs else ''
    side = f'<p class="qh-fig-refs">{label}{" ".join(links)}</p>' if links else ''
    return f'<div class="qh-fig-head"><p class="qh-fig-title" data-block-title>{rich(record["title"])}</p>{side}</div>'


def plain_formula_prose(node):
    """An authored formula as the author spells it in a sentence: -c*x/b as -cx/b, hbar/b as ħ/b."""
    k = node[0]
    if k == 'var':
        return {'hbar': '\u0127', 'pi': '\u03c0'}.get(node[1], node[1])
    if k == 'num':
        return str(node[1])
    if k == 'neg':
        return '-' + plain_formula_prose(node[1])
    if k == 'mul':
        return plain_formula_prose(node[1]) + plain_formula_prose(node[2])
    if k == 'div':
        return plain_formula_prose(node[1]) + '/' + plain_formula_prose(node[2])
    if k == 'pow':
        return plain_formula_prose(node[1]) + '^' + plain_formula_prose(node[2])
    if k == 'group':
        return '(' + plain_formula_prose(node[1]) + ')'
    if k in ('add', 'sub'):
        return plain_formula_prose(node[1]) + ('+' if k == 'add' else '-') + plain_formula_prose(node[2])
    if k == 'call':
        return node[1] + '(' + plain_formula_prose(node[2]) + ')'
    raise FormulaError(f'cannot spell {k}')


def prose_formulas(text, formulas):
    """An authored sentence with each of the record's own formulas that it spells in plain text (the caption's
    -cx/b and ħ/b) set as that formula, typeset like the figure's equations. Only the record's formulas are matched,
    whole and at least three characters long; every other character of the sentence stays as written."""
    if any(d in text for d in ('\\(', '\\[', '$')):
        return text
    forms = {}
    for node in formulas:
        try:
            spelled = plain_formula_prose(node)
        except FormulaError:
            continue
        if len(spelled) >= 3:
            forms.setdefault(spelled, tex(node))
    if not forms:
        return text
    pattern = re.compile(r'(?<![\w/^])(' + '|'.join(re.escape(f) for f in sorted(forms, key=len, reverse=True)) + r')(?![\w/^])')
    return pattern.sub(lambda m: '\\(' + forms[m.group(1)] + '\\)', text)


def caption_text(record):
    """The figure caption as authored; for the Gaussian figure, its own output formulas typeset where it spells them."""
    if record.get('model') != 'gaussian-elimination':
        return record['caption']
    names = list(record.get('parameters') or {})
    return prose_formulas(record['caption'], [parse(f, names) for f in (record.get('outputs') or {}).values()])


def render_gaussian(record, rich, words):
    rid, labels = record['id'], record.get('labels') or {}
    names = list(record['parameters'])
    controls = record['controls']
    env = {n: float(controls[n]['initial']) for n in names}
    outputs = {k: parse(f, names) for k, f in record['outputs'].items()}
    profiles = [{'id': p['id'], 'variable': p['variable'], 'formula': parse(p['formula'], names + [p['variable']]),
                 'integral': parse(p['integral_over_real_line'], names), 'density': is_density(p),
                 'mean': is_density(p) and p['variable'] == 'y'}
                for p in record.get('profiles') or []]
    top = shared_top(record, env)
    config = {'model': record['model'], 'names': names, 'controls': controls, 'outputs': outputs,
              'rule': parse(record['validity']['rule'], names), 'profiles': profiles,
              'mean': outputs.get('conditional_mean'),
              'plot': {'w': PANEL_W, 'span': SPAN, 'x0': WIN_X0, 'x1': WIN_X1, 'base': BASE_Y, 'top': TOP_Y}}
    ctrl = ''.join(
        f'<li class="qh-fig-control" data-param="{attr(n)}">'
        f'<label class="qh-fig-control-label" for="{rid}--{attr(n)}">{rich_label(controls[n]["label"], rich)}</label>'
        f'<output class="qh-fig-value" data-value="{attr(n)}">{fmt(env[n])}</output></li>'
        for n in record.get('permitted_controls') or names)
    rows = ''.join(
        f'<tr data-output="{attr(k)}"><th scope="row">{rich_label(labels[k], rich)}</th>'
        f'<td class="qh-fig-formula">{rich(math_inline(tex(node)))}</td>'
        f'<td class="qh-fig-num"><output class="qh-fig-value" data-value="{attr(k)}">{fmt(value(node, env))}</output></td></tr>'
        for k, node in outputs.items())
    formulas = list(outputs.values())

    def integral(p):
        """The integral over the real line of the plotted function, as one equation in the chapter's notation: the
        authored function integrated in its variable, then the authored value of the integral, then (when that value
        depends on the parameters) its number at these parameters. A constant value (the density's 1) is written once.
        The three parts are kept whole and the line breaks between them."""
        node = parse(p['integral_over_real_line'], names)
        f = parse(p['formula'], names + [p['variable']])
        parts = [rich(math_inline(r'\int_{\mathbb R}' + tex(f) + r'\,d' + tex(['var', p['variable']]))),
                 rich(math_inline('=' + tex(node)))]
        if variables(node):
            parts.append(f'<span class="qh-fig-eq">=</span> <output class="qh-fig-value" data-value="profile:{attr(p["id"])}">'
                         f'{fmt(value(node, env))}</output>')
        return (f'<div class="qh-fig-integral"><p class="qh-fig-label">{esc(words["integral"])}</p>'
                f'<p class="qh-fig-integral-value">' + ' '.join(f'<span class="qh-fig-seg">{x}</span>' for x in parts) +
                '</p></div>')
    panels = ''.join(
        f'<div class="qh-fig-profile" data-profile="{attr(p["id"])}">'
        f'<p class="qh-fig-profile-label">{rich_label(p["label"], rich)}</p>{profile_svg(record, p, env, top)}'
        f'{integral(p)}<p class="qh-fig-profile-caption">{rich_label(prose_formulas(p["caption"], formulas), rich)}</p></div>'
        for p in record.get('profiles') or [])
    panels = f'<p class="qh-fig-note qh-fig-scale-note">{esc(words["scale"])}</p>' + panels
    body = (f'<div class="qh-fig-body"><div class="qh-fig-side">'
            f'<p class="qh-fig-label">{esc(words["controls"])}</p><ul class="qh-fig-controls">{ctrl}</ul>'
            f'<p class="qh-fig-domain">{rich_label(labels["domain"], rich)}</p>'
            f'<p class="qh-fig-invalid" role="status" aria-live="polite" hidden>{rich_label(record["validity"]["message"], rich)}</p>'
            f'</div><div class="qh-fig-stage"><div class="qh-fig-profiles">{panels}</div>'
            f'<table class="qh-fig-outputs"><caption class="qh-fig-label">{esc(words["outputs"])}</caption><tbody>{rows}</tbody></table>'
            f'</div></div>')
    return body, config


def render_expansions(record, rich, words):
    labels, states = record['labels'], record['states']
    first = next(s for s in states if s['id'] == record['initial_state'])
    config = {'model': record['model'], 'initial': record['initial_state'], 'plane': list(PLANE),
              'states': [{'id': s['id'], 'inside': inside_disk(s['condition']), 'text': plain_formula(parse(s['condition'])),
                          'at': list(region_label_at(inside_disk(s['condition'])))} for s in states]}
    items = ''.join(
        f'<li class="qh-fig-state" data-state="{attr(s["id"])}"' + (' aria-current="true"' if s is first else '') + '>'
        f'<p class="qh-fig-state-label">{rich_label(s["label"], rich)}</p>'
        f'<p class="qh-fig-cond">{rich(math_inline(tex(parse(s["condition"]))))}</p>'
        f'<div class="qh-fig-series"><p class="qh-fig-label">{rich_label(labels["series"], rich)}</p>'
        f'{rich(chr(92) + "[" + tex(parse(s["series"])) + chr(92) + "]")}</div></li>'
        for s in states)
    body = (f'<div class="qh-fig-body"><div class="qh-fig-side">'
            f'<p class="qh-fig-label">{rich_label(labels["domain"], rich)}</p><ol class="qh-fig-states">{items}</ol></div>'
            f'<div class="qh-fig-stage">{plane_svg(first, labels)}'
            f'<p class="qh-fig-note">{rich_label(labels["no_value"], rich)}</p></div></div>')
    return body, config


RENDERERS = {'gaussian-elimination': render_gaussian, 'two-expansions': render_expansions}
RENDERERS.update(FINITE_RENDERERS)


def render(record, ctx):
    """One figure, for the reader to place where the chapter's hook stands. A record with any problem renders
    nothing and fails the build with each problem named. ctx gives rich(text) (the page's renderer) and may give
    words, a dict replacing any interface word of WORDS."""
    problems = check(record)
    if problems:
        return {'html': '', 'problems': problems}
    rid = record['id']
    rich = (lambda t: ctx.rich(t, terms=False)) if hasattr(ctx, 'rich') else esc
    words = dict(WORDS, **(getattr(ctx, 'words', None) or {}))
    body, config = RENDERERS[record['model']](record, rich, words)
    cfg = html.escape(json.dumps(config, separators=(',', ':'), ensure_ascii=False), quote=True)
    return {'html': (f'<figure class="qh-fig" id="{rid}" data-figure="{rid}" data-qh-figure="{rid}" '
                     f'data-figure-type="{attr(record["type"])}" data-figure-model="{attr(record["model"])}" '
                     f'data-figure-chapter="{attr(record.get("chapter_id", ""))}" data-figure-section="{attr(record.get("section_id", ""))}" '
                     f'data-config="{cfg}">{head_html(record, rich, words)}{body}'
                     f'<figcaption class="qh-fig-caption">{rich_label(caption_text(record), rich)}</figcaption></figure>'),
            'problems': []}


def assets():
    """The stylesheet and script the reader includes once on a page that places a figure."""
    from pathlib import Path
    here = Path(__file__).resolve().parent
    return {'css': (here / 'figures.css').read_text(encoding='utf-8'), 'js': (here / 'figures.js').read_text(encoding='utf-8')}
