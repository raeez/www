# Drawing ---------------------------------------------------------------------------------------------------
# Every mark a figure draws has its meaning in the figure. A curve is an authored function over a finite window of
# its variable; no area is filled, so a window never reads as a whole integral. A solid arrow is a defined map and
# carries its authored label. A ring marks a basis vector the record lists as surviving in cohomology, and the
# same ring marks that vector's name in the table. A cell holds the matrix entry its authored rule gives. Dashes
# are kept for open comparisons and are not used here. The script redraws with the same geometry.

PANEL_W, PANEL_H, PAD, SPAN = 300, 150, 18, 4.0
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
    return PAD + (t + SPAN) / (2 * SPAN) * (PANEL_W - 2 * PAD)


def profile_path(node, var, env, scale):
    pts = []
    for i in range(161):
        t = -SPAN + 2 * SPAN * i / 160
        v = value(node, dict(env, **{var: t}))
        v = 0.0 if v is None or isinstance(v, bool) else v
        pts.append((window_x(t), PANEL_H - PAD - min(v / scale, 1.06) * (PANEL_H - 2 * PAD - 8)))
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)


def is_density(p):
    return str(p.get('integral_over_real_line')).strip() == '1'


def profile_scale(p, node, env):
    """Unnormalized weights share the vertical scale 0..1, so their peaks compare; a density uses its own peak."""
    if not is_density(p):
        return 1.0
    peak = max((value(node, dict(env, **{p['variable']: t / 40})) or 0) for t in range(-160, 161))
    return peak or 1.0


def mean_mark(x, label):
    """The conditional mean on the density, as a line with its authored label attached at its head."""
    right = x > PANEL_W / 2
    return (f'<line class="qh-fig-mean" data-part="mean" x1="{x:.1f}" y1="{PAD - 4}" x2="{x:.1f}" y2="{PANEL_H - PAD}"/>'
            f'<text class="qh-fig-mark-label" data-part="mean-label" x="{x - 5 if right else x + 5:.1f}" y="{PAD - 7}" '
            f'text-anchor="{"end" if right else "start"}">{sub_svg(label)}</text>')


def profile_svg(record, p, env):
    names = list(record['parameters'])
    node = parse(p['formula'], names + [p['variable']])
    base = PANEL_H - PAD
    outs, labels = record.get('outputs') or {}, record.get('labels') or {}
    marks = ''
    if is_density(p) and p['variable'] == 'y' and 'conditional_mean' in outs and labels.get('conditional_mean'):
        mean = value(parse(outs['conditional_mean'], names), env)
        marks = mean_mark(window_x(max(-SPAN, min(SPAN, mean))), labels['conditional_mean'])
    return (f'<svg class="qh-fig-svg" viewBox="0 0 {PANEL_W} {PANEL_H}" aria-hidden="true" focusable="false">'
            f'<path class="qh-fig-curve" data-part="curve" d="{profile_path(node, p["variable"], env, profile_scale(p, node, env))}"/>'
            f'{marks}<path class="qh-fig-axis" d="M{PAD - 6} {base}H{PANEL_W - PAD + 6}"/>'
            f'<path class="qh-fig-axis" d="M{PANEL_W / 2:.1f} {base}v4"/>'
            f'<path class="qh-fig-more" d="M{PAD - 6} {base}l5 -3v6zM{PANEL_W - PAD + 6} {base}l-5 -3v6z"/>'
            f'<text class="qh-fig-tick" x="{PANEL_W / 2:.1f}" y="{PANEL_H - 2}" text-anchor="middle">0</text>'
            f'<text class="qh-fig-tick qh-fig-var" x="{PANEL_W - PAD}" y="{PANEL_H - 2}" text-anchor="end">{esc(p["variable"])}</text></svg>')


# The two expansions: the w-plane at a fixed z

PLANE = (360, 232, 150, 120, 76)  # width, height, centre x, centre y, radius |z|


def region_shape(inside):
    W, H, cx, cy, r = PLANE
    if inside:
        return f'<circle class="qh-fig-region" data-part="region" cx="{cx}" cy="{cy}" r="{r}"/>'
    return (f'<path class="qh-fig-region" data-part="region" fill-rule="evenodd" '
            f'd="M2 2H{W - 2}V{H - 2}H2Z M{cx + r} {cy}a{r} {r} 0 1 0 -{2 * r} 0a{r} {r} 0 1 0 {2 * r} 0Z"/>')


def region_label_at(inside):
    W, H, cx, cy, r = PLANE
    return (cx - 34, cy + 40, 'middle') if inside else (14, 26, 'start')


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
    config = {'model': record['model'], 'names': names, 'controls': controls, 'outputs': outputs,
              'rule': parse(record['validity']['rule'], names), 'profiles': profiles,
              'mean': outputs.get('conditional_mean'), 'window': [PANEL_W, PANEL_H, PAD, SPAN]}
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
    panels = ''.join(
        f'<div class="qh-fig-profile" data-profile="{attr(p["id"])}">'
        f'<p class="qh-fig-profile-label">{rich_label(p["label"], rich)}</p>{profile_svg(record, p, env)}'
        f'<p class="qh-fig-integral"><span class="qh-fig-label">{esc(words["integral"])}</span> '
        f'{rich(math_inline(tex(parse(p["integral_over_real_line"], names))))} '
        f'<span class="qh-fig-eq">=</span> <output class="qh-fig-value" data-value="profile:{attr(p["id"])}">'
        f'{fmt(value(parse(p["integral_over_real_line"], names), env))}</output></p>'
        f'<p class="qh-fig-profile-caption">{rich_label(p["caption"], rich)}</p></div>'
        for p in record.get('profiles') or [])
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
              'states': [{'id': s['id'], 'inside': inside_disk(s['condition']),
                          'text': plain_formula(parse(s['condition']))} for s in states]}
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
                     f'<figcaption class="qh-fig-caption">{rich_label(record["caption"], rich)}</figcaption></figure>'),
            'problems': []}


def assets():
    """The stylesheet and script the reader includes once on a page that places a figure."""
    from pathlib import Path
    here = Path(__file__).resolve().parent
    return {'css': (here / 'figures.css').read_text(encoding='utf-8'), 'js': (here / 'figures.js').read_text(encoding='utf-8')}
