/* Figures of the reader: controls for the author's figure records. The server draws each figure's initial state,
   which is complete without this script and in print. Every value shown is an authored formula evaluated at the
   current parameters, and every state is one the record lists.
   - Gaussian: one range input per permitted control, inside the authored display window. A proposed value that
     breaks the authored validity rule is refused; the authored message is shown and the previous valid values
     stay.
   - Expansions: a choice between the two authored regions.
   - Cohomology jump: a choice between the authored values of t; the drawing, the matrix and the table follow.
   - Infinite rank: the authored control N redraws the finite diagonal beside its limit.
   - Adjunction: the key's unit and counit entries, pressed, pick out the arrows built from them. */
(function () {
  'use strict';
  var doc = document;
  var NS = 'http://www.w3.org/2000/svg';
  function all(sel, root) { return Array.prototype.slice.call((root || doc).querySelectorAll(sel)); }
  var CONST = { pi: Math.PI };

  /* The authored formula evaluated at the parameters, as on the server: null where it has no number. */
  function val(n, env) {
    var k = n[0], a, b;
    if (k === 'num') return +n[1];
    if (k === 'var') return Object.prototype.hasOwnProperty.call(env, n[1]) ? env[n[1]] : (n[1] in CONST ? CONST[n[1]] : null);
    if (k === 'group') return val(n[1], env);
    if (k === 'abs' || k === 'neg') {
      a = val(n[1], env);
      if (a === null || typeof a === 'boolean') return null;
      return k === 'abs' ? Math.abs(a) : -a;
    }
    if (k === 'add' || k === 'sub' || k === 'mul' || k === 'div' || k === 'pow') {
      a = val(n[1], env); b = val(n[2], env);
      if (a === null || b === null || typeof a === 'boolean' || typeof b === 'boolean') return null;
      if (k === 'add') return a + b;
      if (k === 'sub') return a - b;
      if (k === 'mul') return a * b;
      if (k === 'div') return b === 0 ? null : a / b;
      return Math.pow(a, b);
    }
    if (k === 'call') {
      a = val(n[2], env);
      if (a === null || typeof a === 'boolean') return null;
      if (n[1] === 'sqrt') return a >= 0 ? Math.sqrt(a) : null;
      if (n[1] === 'exp') return a < 700 ? Math.exp(a) : null;
      return null;
    }
    if (k === 'cmp') {
      a = val(n[2], env); b = val(n[3], env);
      if (a === null || b === null) return null;
      return { '<': a < b, '>': a > b, '<=': a <= b, '>=': a >= b, '!=': a !== b, '==': a === b }[n[1]];
    }
    if (k === 'and') return val(n[1], env) === true && val(n[2], env) === true;
    return null;
  }
  /* A value as on the server: at most three decimals, a negative value with the minus sign (U+2212). */
  function fmt(v) {
    if (v === null || v === undefined || typeof v === 'boolean' || !isFinite(v)) return '';
    var text = (v !== 0 && (Math.abs(v) >= 1000 || Math.abs(v) < 0.001)) ? v.toPrecision(3)
      : v.toFixed(3).replace(/0+$/, '').replace(/\.$/, '');
    text = text.replace(/-/g, '\u2212');
    return text === '\u22120' ? '0' : text;
  }
  function copy(o) { var r = {}; for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) r[k] = o[k]; return r; }
  function show(el, on) { if (!el) return; if (on) el.removeAttribute('display'); else el.setAttribute('display', 'none'); }

  /* Keep decimal products and ratios exact in grid comparisons, including a*b > c^2. */
  function decimalRatio(node, env) {
    var kind = node[0], a, b;
    if (kind === 'group' || kind === 'neg' || kind === 'abs') {
      a = decimalRatio(node[1], env);
      if (a && (kind === 'neg' || (kind === 'abs' && a[0] < 0n))) return [-a[0], a[1]];
      return a;
    }
    if (kind === 'mul' || kind === 'div' || (kind === 'pow' && node[2][0] === 'num' && node[2][1] === 2)) {
      a = decimalRatio(node[1], env);
      b = kind === 'pow' ? a : decimalRatio(node[2], env);
      if (kind === 'div' && b) {
        if (b[0] === 0n) return null;
        b = b[0] < 0n ? [-b[1], -b[0]] : [b[1], b[0]];
      }
      return a && b ? [a[0] * b[0], a[1] * b[1]] : null;
    }
    if (kind !== 'num' && !(kind === 'var' && Object.prototype.hasOwnProperty.call(env, node[1]))) return null;
    var match = /^(-?\d+)(?:\.(\d+))?(?:e([+-]?\d+))?$/i.exec(String(kind === 'num' ? node[1] : env[node[1]]));
    if (!match) return null;
    var fraction = match[2] || '', places = fraction.length - Number(match[3] || 0);
    var integer = BigInt(match[1] + fraction);
    return places < 0 ? [integer * 10n ** BigInt(-places), 1n] : [integer, 10n ** BigInt(places)];
  }

  function validRule(node, env) {
    if (node[0] === 'and') return validRule(node[1], env) && validRule(node[2], env);
    if (node[0] === 'cmp') {
      var a = decimalRatio(node[2], env), b = decimalRatio(node[3], env);
      if (a && b) {
        var left = a[0] * b[1], right = b[0] * a[1];
        return { '<': left < right, '>': left > right, '<=': left <= right, '>=': left >= right,
                 '!=': left !== right, '==': left === right }[node[1]];
      }
    }
    return val(node, env) === true;
  }

  /* A range input for an authored control, added to its list item after the label and the value. */
  function rangeFor(fig, li, name, c, value) {
    var input = doc.createElement('input');
    input.type = 'range';
    input.id = fig.id + '--' + name;
    input.min = String(c.min); input.max = String(c.max); input.step = String(c.step); input.value = String(value);
    input.setAttribute('aria-valuetext', fmt(value));
    li.appendChild(input);
    return input;
  }

  /* The authored states as buttons: each state's label becomes a button that chooses it. */
  function stateButtons(fig, choose) {
    all('.qh-fig-state[data-state]', fig).forEach(function (li) {
      var id = li.getAttribute('data-state'), label = li.querySelector('.qh-fig-state-label');
      if (!label) return;
      var b = doc.createElement('button');
      b.type = 'button';
      b.className = 'qh-fig-choose';
      while (label.firstChild) b.appendChild(label.firstChild);
      label.appendChild(b);
      b.addEventListener('click', function () { choose(id); });
    });
  }
  function markCurrent(fig, id) {
    all('.qh-fig-state[data-state]', fig).forEach(function (li) {
      var on = li.getAttribute('data-state') === id, b = li.querySelector('button.qh-fig-choose');
      if (on) li.setAttribute('aria-current', 'true'); else li.removeAttribute('aria-current');
      if (b) b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    all('[data-state-row]', fig).forEach(function (tr) {
      if (tr.getAttribute('data-state-row') === id) tr.setAttribute('aria-current', 'true'); else tr.removeAttribute('aria-current');
    });
  }

  function gaussian(fig, cfg) {
    var P = cfg.plot, SPAN = P.span;
    var env = {};
    cfg.names.forEach(function (n) { env[n] = +cfg.controls[n].initial; });
    var note = fig.querySelector('.qh-fig-invalid');
    function wx(t) { return P.x0 + (t + SPAN) / (2 * SPAN) * (P.x1 - P.x0); }
    function wy(v, top) { return P.base - Math.min(v / top, 1.06) * (P.base - P.top); }
    /* The drawn values of a profile, as on the server: 161 points across the window, no number drawn as 0. */
    function samples(p) {
      var out = [], local = copy(env), i, t, v;
      for (i = 0; i <= 160; i++) {
        t = -SPAN + 2 * SPAN * i / 160;
        local[p.variable] = t;
        v = val(p.formula, local);
        out.push([t, (v === null || typeof v === 'boolean') ? 0 : v]);
      }
      return out;
    }
    /* The top of the one vertical scale every curve shares, as on the server: the least of 1, 2, 5 or 10 times a
       power of ten at or above the largest value drawn. */
    function niceTop(m) {
      if (!m || m <= 0 || !isFinite(m)) return 1;
      m *= 1 - 1e-9;
      var e = Math.pow(10, Math.floor(Math.log10(m))), ks = [1, 2, 5, 10];
      for (var i = 0; i < ks.length; i++) if (ks[i] * e >= m) return ks[i] * e;
      return 10 * e;
    }
    function update() {
      all('output[data-value]', fig).forEach(function (o) {
        var key = o.getAttribute('data-value'), v = null;
        if (key.indexOf('profile:') === 0) {
          cfg.profiles.forEach(function (p) { if ('profile:' + p.id === key) v = val(p.integral, env); });
        } else if (Object.prototype.hasOwnProperty.call(cfg.outputs, key)) v = val(cfg.outputs[key], env);
        else if (Object.prototype.hasOwnProperty.call(env, key)) v = env[key];
        o.textContent = fmt(v);
      });
      var mean = cfg.mean ? val(cfg.mean, env) : null;
      var meanVisible = mean !== null && validRule(['cmp', '<=', ['abs', cfg.mean], ['num', SPAN]], env);
      var drawn = cfg.profiles.map(samples), peak = 0;
      drawn.forEach(function (pts) { pts.forEach(function (pt) { if (pt[1] > peak) peak = pt[1]; }); });
      var top = niceTop(peak);
      cfg.profiles.forEach(function (p, k) {
        var box = fig.querySelector('.qh-fig-profile[data-profile="' + p.id + '"] svg');
        if (!box) return;
        var c = box.querySelector('[data-part="curve"]');
        if (c) c.setAttribute('d', 'M' + drawn[k].map(function (pt) { return wx(pt[0]).toFixed(1) + ' ' + wy(pt[1], top).toFixed(1); }).join(' L'));
        var mid = box.querySelector('[data-part="scale-mid"]'), hi = box.querySelector('[data-part="scale-top"]');
        if (mid) mid.textContent = fmt(top / 2);
        if (hi) hi.textContent = fmt(top);
        var m = box.querySelector('[data-part="mean"]'), ml = box.querySelector('[data-part="mean-label"]');
        show(m, meanVisible); show(ml, meanVisible);
        if (m && meanVisible) {
          var x = wx(mean), right = x > P.w / 2;
          m.setAttribute('x1', x.toFixed(1)); m.setAttribute('x2', x.toFixed(1));
          if (ml) { ml.setAttribute('x', (right ? x - 5 : x + 5).toFixed(1)); ml.setAttribute('text-anchor', right ? 'end' : 'start'); }
        }
      });
    }
    all('.qh-fig-control[data-param]', fig).forEach(function (li) {
      var n = li.getAttribute('data-param'), c = cfg.controls[n];
      if (!c) return;
      var input = rangeFor(fig, li, n, c, env[n]);
      input.addEventListener('input', function () {
        var trial = copy(env);
        trial[n] = +input.value;
        if (validRule(cfg.rule, trial)) {
          env = trial;
          if (note) note.hidden = true;
          input.setAttribute('aria-valuetext', fmt(env[n]));
          update();
        } else {
          input.value = String(env[n]); /* refused: the previous valid values stay, and the authored message says why */
          if (note) note.hidden = false;
        }
      });
    });
    fig.classList.add('qh-fig-live');
    update();
  }

  function expansions(fig, cfg) {
    var svg = fig.querySelector('.qh-fig-plane');
    var W = cfg.plane[0], H = cfg.plane[1], cx = cfg.plane[2], cy = cfg.plane[3], r = cfg.plane[4];
    function region(state) {
      var el;
      if (state.inside) {
        el = doc.createElementNS(NS, 'circle');
        el.setAttribute('cx', cx); el.setAttribute('cy', cy); el.setAttribute('r', r);
      } else {
        el = doc.createElementNS(NS, 'path');
        el.setAttribute('fill-rule', 'evenodd');
        el.setAttribute('d', 'M2 2H' + (W - 2) + 'V' + (H - 2) + 'H2Z M' + (cx + r) + ' ' + cy + 'a' + r + ' ' + r + ' 0 1 0 -' + (2 * r) +
                             ' 0a' + r + ' ' + r + ' 0 1 0 ' + (2 * r) + ' 0Z');
      }
      el.setAttribute('class', 'qh-fig-region');
      el.setAttribute('data-part', 'region');
      return el;
    }
    function choose(id) {
      markCurrent(fig, id);
      cfg.states.forEach(function (s) {
        if (s.id !== id || !svg) return;
        var old = svg.querySelector('[data-part="region"]');
        if (old) svg.replaceChild(region(s), old);
        var label = svg.querySelector('[data-part="region-label"]');
        if (label) {
          label.textContent = s.text;
          label.setAttribute('x', s.at[0]); label.setAttribute('y', s.at[1]); label.setAttribute('text-anchor', s.at[2]);
        }
        svg.setAttribute('aria-label', s.text + '; ' + (svg.getAttribute('aria-label') || '').split('; ').slice(1).join('; '));
      });
    }
    stateButtons(fig, choose);
    fig.classList.add('qh-fig-live');
    choose(cfg.initial);
  }

  function cohomology(fig, cfg) {
    var svg = fig.querySelector('.qh-fig-complex');
    function choose(id) {
      markCurrent(fig, id);
      cfg.states.forEach(function (s) {
        if (s.id !== id || !svg) return;
        var first = svg.querySelector('[data-part="first"]');
        if (first) first.setAttribute('d', s.toV ? cfg.paths.v : cfg.paths.zero);
        show(svg.querySelector('[data-part="first-zero"]'), !s.toV);
        var fl = svg.querySelector('[data-part="first-label"]');
        if (fl) fl.setAttribute('x', Math.round(s.toV ? cfg.mids.v : cfg.mids.zero));
        show(svg.querySelector('[data-part="h"]'), !!s.h);
        var hl = svg.querySelector('[data-part="h-label"]');
        if (hl) { hl.textContent = s.h; show(hl, !!s.h); }
        all('.qh-fig-basis[data-basis]', svg).forEach(function (g) {
          g.classList.toggle('is-alive', s.alive.indexOf(g.getAttribute('data-basis')) >= 0);
        });
      });
    }
    stateButtons(fig, choose);
    fig.classList.add('qh-fig-live');
    choose(cfg.initial);
  }

  function infinite(fig, cfg) {
    var env = { N: +cfg.control.initial };
    function update() {
      cfg.grids.forEach(function (g) {
        var svg = fig.querySelector('svg[data-grid="' + g.id + '"]');
        if (!svg) return;
        all('.qh-fig-cell', svg).forEach(function (cell) {
          var e = copy(env);
          e.i = +cell.getAttribute('data-i'); e.j = +cell.getAttribute('data-j');
          var on = val(g.rule, e) === true, t = cell.querySelector('text');
          cell.classList.toggle('is-on', on);
          if (t) t.textContent = on ? '1' : '0';
        });
        var beyond = svg.querySelector('[data-part="beyond"]');
        if (beyond) { var e2 = copy(env); e2.i = cfg.n; e2.j = cfg.n; beyond.classList.toggle('is-on', val(g.rule, e2) === true); }
      });
      var o = fig.querySelector('output[data-value="N"]');
      if (o) o.textContent = fmt(env.N);
      var rank = fig.querySelector('output[data-value="rank:' + cfg.rank.id + '"]');
      if (rank && cfg.rank.formula) rank.textContent = fmt(val(cfg.rank.formula, env));
    }
    var li = fig.querySelector('.qh-fig-control[data-param="N"]');
    if (li) {
      var input = rangeFor(fig, li, 'N', cfg.control, env.N);
      input.addEventListener('input', function () {
        env = { N: +input.value };
        input.setAttribute('aria-valuetext', fmt(env.N));
        update();
      });
    }
    fig.classList.add('qh-fig-live');
    update();
  }

  function adjunction(fig) {
    var keys = all('.qh-fig-key[data-key="eta"], .qh-fig-key[data-key="epsilon"]', fig);
    var pinned = '';
    function emphasise(which) {
      if (which) fig.setAttribute('data-emphasis', which); else fig.removeAttribute('data-emphasis');
    }
    keys.forEach(function (li) {
      var which = li.getAttribute('data-key') === 'eta' ? 'unit' : 'counit';
      var text = li.querySelector('.qh-fig-key-text');
      if (!text) return;
      var b = doc.createElement('button');
      b.type = 'button';
      b.className = 'qh-fig-key-button';
      b.setAttribute('aria-pressed', 'false');
      while (li.firstChild) b.appendChild(li.firstChild);
      li.appendChild(b);
      b.addEventListener('click', function () {
        pinned = pinned === which ? '' : which;
        keys.forEach(function (k) {
          var kb = k.querySelector('button');
          var kw = k.getAttribute('data-key') === 'eta' ? 'unit' : 'counit';
          if (kb) kb.setAttribute('aria-pressed', pinned === kw ? 'true' : 'false');
        });
        emphasise(pinned);
      });
      b.addEventListener('mouseenter', function () { if (!pinned) emphasise(which); });
      b.addEventListener('mouseleave', function () { if (!pinned) emphasise(''); });
    });
    fig.classList.add('qh-fig-live');
  }

  var MODELS = { 'gaussian-elimination': gaussian, 'two-expansions': expansions, 'cohomology-jump': cohomology,
                 'infinite-rank': infinite, 'adjunction-triangles': adjunction };
  all('figure[data-figure][data-config]').forEach(function (fig) {
    var cfg;
    try { cfg = JSON.parse(fig.getAttribute('data-config')); } catch (e) { return; }
    if (fig.classList.contains('qh-fig-live') || !MODELS[cfg.model]) return;
    MODELS[cfg.model](fig, cfg);
  });
})();
