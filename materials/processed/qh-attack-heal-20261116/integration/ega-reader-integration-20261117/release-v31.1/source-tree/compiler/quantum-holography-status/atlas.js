/* The research atlas: the script for the atlas mount ([data-atlas-mount]) of the page.

   It reads only the atlas markup: the claims, the relations recorded with each claim, the map, the
   index and the words of the interface. It adds filters above the index, turns the part with every
   claim in full into a pane that shows the claim the address names, highlights that claim's recorded
   relations in the map and in a small diagram, and lets the reader follow a reading path.

   The address is the selection. A link to a claim (#atlas-c-<id>) is an ordinary in-page link: the
   browser makes the history entry, and this script follows the address on hashchange and on the page's
   qh:state event, so Back and Forward move between selections. It never writes the address or the
   history. A link to a part of the page outside the atlas is passed to the page as a qh:navigate
   event, so that the page opens and focuses it. Nothing is stored and no request is made. */
(function () {
  'use strict';
  var doc = document;
  var mount = doc.querySelector('[data-atlas-mount]');
  var body = mount && mount.querySelector('.atlas-body');
  var full = mount && mount.querySelector('.atlas-claims-full');
  if (!body || !full) return;
  var SVG = 'http://www.w3.org/2000/svg';
  var CLAIM = /^atlas-c-(.+)$/;

  function all(selector, context) { return Array.prototype.slice.call((context || doc).querySelectorAll(selector)); }
  function media(query) { return !!(window.matchMedia && window.matchMedia(query).matches); }
  function smooth() { return media('(prefers-reduced-motion: reduce)') ? 'auto' : 'smooth'; }
  function wide() { return media('(min-width: 1000px)'); }
  function plainClick(event) { return !(event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey); }
  var template = body.querySelector('template.atlas-wordlist');
  function word(name) {
    var n = template && template.content && template.content.querySelector('[data-word="' + name + '"]');
    return n ? n.textContent : '';
  }
  function fill(text, values) { return text.replace(/\{(\w+)\}/g, function (_, k) { return values[k] == null ? '' : String(values[k]); }); }
  function el(tag, cls, text) {
    var n = doc.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function svg(tag, attrs) {
    var n = doc.createElementNS(SVG, tag);
    Object.keys(attrs || {}).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    return n;
  }
  function decode(raw) { try { return decodeURIComponent(raw); } catch (e) { return raw; } }
  function fold(s) {
    return (s || '').normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase()
      .replace(/[‘’ʼ]/g, '\'').replace(/[“”]/g, '"').replace(/[‐-―−]/g, '-');
  }
  function words(q) {
    var out = [];
    (q || '').replace(/"([^"]+)"|(\S+)/g, function (_, phrase, w) {
      var t = fold(phrase ? phrase.replace(/\s+/g, ' ').trim() : w);
      if (t) out.push(t);
      return '';
    });
    return out;
  }
  /* The words a reader sees in an element: formulae by their symbols, no TeX source, no marks. */
  function textOf(node, skip) {
    var out = [];
    (function walk(n) {
      if (n.nodeType === 3) { out.push(n.nodeValue); return; }
      if (n.nodeType !== 1 || (skip && n.matches(skip))) return;
      var tag = n.localName;
      if (tag === 'svg' || tag === 'annotation' || tag === 'script' || tag === 'style' || tag === 'template') return;
      for (var c = n.firstChild; c; c = c.nextSibling) walk(c);
      out.push(' ');
    })(node);
    return out.join('').replace(/\s+/g, ' ').trim();
  }
  function texOf(node, skip) {
    return all('annotation', node).filter(function (a) { return !(skip && a.closest(skip)); })
      .map(function (a) { return a.textContent; }).join(' ');
  }

  /* The claims and their relations, read from the markup. */
  var claims = {};
  var order = [];
  /* The filter reads a claim's title, statement, hypotheses and source statement, and nothing else. */
  var TIP_RELATIONS = 6; /* relations named in the map tip; the pane lists every one */
  var SEARCHED = '.atlas-claim-title, .atlas-statement, .atlas-hyps, .atlas-note-source';
  function hayOf(article) {
    return fold(all(SEARCHED, article).map(function (n) { return textOf(n, '.atlas-note-label') + ' ' + texOf(n); }).join(' '));
  }
  all('.atlas-claim[data-claim-id]', full).forEach(function (article) {
    var id = article.getAttribute('data-claim-id');
    claims[id] = {
      id: id, article: article, title: article.querySelector('.atlas-claim-title'),
      domain: article.getAttribute('data-domain-id'), status: article.getAttribute('data-status-code'),
      number: article.getAttribute('data-number') || '',
      row: doc.getElementById('atlas-r-' + id), node: body.querySelector('.atlas-map .atlas-node[data-claim-ref="' + id + '"]'),
      into: [], out: [], filtered: false, hay: hayOf(article)
    };
    order.push(id);
  });
  if (!order.length) return;
  var edges = {};
  all('.atlas-rels[data-dir="out"] > .atlas-rel[data-edge-id]', full).forEach(function (li) {
    var lab = li.querySelector('.atlas-rel-label');
    var e = { id: li.getAttribute('data-edge-id'), source: li.getAttribute('data-source'), target: li.getAttribute('data-target'),
              relation: li.getAttribute('data-relation'), label: lab ? lab.textContent.replace(/\s+/g, ' ').trim() : '', path: null };
    if (!claims[e.source] || !claims[e.target]) return;
    edges[e.id] = e;
    claims[e.source].out.push(e);
    claims[e.target].into.push(e);
  });
  all('.atlas-map .atlas-edge[data-edge-id]', body).forEach(function (p) { var e = edges[p.getAttribute('data-edge-id')]; if (e) e.path = p; });
  var relations = {};
  all('[data-key-relation]', body).forEach(function (n) {
    relations[n.getAttribute('data-key-relation')] = { label: n.textContent.replace(/\s+/g, ' ').trim(),
                                                       style: n.getAttribute('data-key-style') || '0',
                                                       swatch: n.querySelector('.atlas-swatch') };
  });
  var hiddenRelations = {};  /* relation codes the reader has hidden in the pane */
  var map = body.querySelector('.atlas-map');
  body.classList.add('atlas-js');

  /* The pane: the part with every claim in full shows the claim the address names. */
  var head = el('div', 'atlas-pane-head');
  var paneLabel = el('p', 'atlas-pane-label', word('pane'));
  var paneSay = el('p', 'atlas-vh');  /* announces the claim reached by Previous or Next */
  paneSay.setAttribute('aria-live', 'polite');
  paneLabel.id = 'atlas-pane-label';
  head.appendChild(paneLabel);
  head.appendChild(paneSay);
  var closeButton = el('button', 'link-btn atlas-pane-close', word('close'));
  closeButton.type = 'button';
  head.appendChild(closeButton);
  var emptyLine = el('p', 'atlas-pane-empty', word('empty'));
  var pathBar = el('div', 'atlas-pathbar');
  pathBar.hidden = true;
  var heading = full.querySelector(':scope > .atlas-part-head');
  var after = heading ? heading.nextSibling : full.firstChild;
  [head, emptyLine, pathBar].forEach(function (n) { full.insertBefore(n, after); });
  full.setAttribute('aria-labelledby', 'atlas-pane-label');
  /* The locator at the top of the pane: the whole atlas in small, from the map's own layout. */
  var locator = full.querySelector('.atlas-locator');
  var locRing = locator && locator.querySelector('.atlas-locator-ring');
  var locNo = locator && locator.querySelector('.atlas-locator-no');
  var locBox = (function () {
    var s = locator && locator.querySelector('svg');
    var v = s ? (s.getAttribute('viewBox') || '').split(/[\s,]+/).map(Number) : [];
    return v.length === 4 && v[2] > 0 && v[3] > 0 ? { w: v[2], h: v[3] } : null;
  })();
  var current = null;
  var origin = null;      /* the control that selected the claim shown, for Escape and Close */
  var activation = null;  /* a claim link the reader has just activated */

  /* Filters above the index: words, domains and statuses. The count line names no number, so that a
     filtered list is never read as a count of results. */
  var index = doc.getElementById('atlas-index');
  var state = { q: '', domains: [], statuses: [] };
  var countLine = null;
  var input = null;
  function chip(attr, value, nodes) {
    var b = el('button', 'atlas-chip-btn');
    b.type = 'button';
    b.setAttribute(attr, value);
    b.setAttribute('aria-pressed', 'false');
    nodes.forEach(function (n) { b.appendChild(n); });
    return b;
  }
  function chipGroup(label, buttons) {
    var g = el('div', 'atlas-chips');
    g.setAttribute('role', 'group');
    g.setAttribute('aria-label', label);
    g.appendChild(el('span', 'atlas-chips-label', label));
    buttons.forEach(function (b) { g.appendChild(b); });
    return g;
  }
  if (index) {
    var tools = el('div', 'atlas-tools');
    tools.setAttribute('role', 'search');
    tools.setAttribute('aria-label', word('filter'));
    var line = el('div', 'atlas-words');
    var label = el('label', null, word('words'));
    label.htmlFor = 'atlas-q';
    input = el('input');
    input.type = 'search';
    input.id = 'atlas-q';
    input.placeholder = word('field-hint');
    input.setAttribute('autocomplete', 'off');
    input.setAttribute('spellcheck', 'false');
    input.setAttribute('aria-controls', 'atlas-index');
    var clear = el('button', 'link-btn atlas-clear', word('clear'));
    clear.type = 'button';
    line.appendChild(label);
    line.appendChild(input);
    line.appendChild(clear);
    tools.appendChild(line);
    tools.appendChild(el('p', 'atlas-filter-note', word('filter-note')));
    var seenDomains = [];
    order.forEach(function (id) { if (seenDomains.indexOf(claims[id].domain) < 0) seenDomains.push(claims[id].domain); });
    var domainChips = seenDomains.map(function (d) {
      var name = body.querySelector('#atlas-d-' + d + ' .atlas-domain-h');
      return chip('data-atlas-domain', d, [el('span', null, name ? textOf(name) : d)]);
    });
    if (domainChips.length > 1) tools.appendChild(chipGroup(word('domain'), domainChips));
    var statusChips = all('.atlas-key-item[data-key-status]', body).filter(function (item) {
      var code = item.getAttribute('data-key-status');
      return order.some(function (id) { return claims[id].status === code; });
    }).map(function (item) {
      return chip('data-atlas-status', item.getAttribute('data-key-status'),
                  Array.prototype.slice.call(item.querySelector('dt').childNodes).map(function (n) { return n.cloneNode(true); }));
    });
    if (statusChips.length > 1) tools.appendChild(chipGroup(word('status'), statusChips));
    countLine = el('p', 'atlas-count');
    countLine.setAttribute('role', 'status');
    countLine.setAttribute('aria-live', 'polite');
    tools.appendChild(countLine);
    index.insertBefore(tools, index.firstChild);

    var timer = null;
    input.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () { state.q = input.value; applyFilter(); }, 80);
    });
    input.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && input.value) { event.preventDefault(); input.value = ''; state.q = ''; applyFilter(); }
      else if (event.key === 'ArrowDown') {
        var first = indexLinks()[0];
        if (first) { event.preventDefault(); first.focus(); }
      }
    });
    clear.addEventListener('click', function () {
      input.value = '';
      state = { q: '', domains: [], statuses: [] };
      all('.atlas-chip-btn', tools).forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
      applyFilter();
      input.focus();
    });
    tools.addEventListener('click', function (event) {
      var b = event.target.closest('.atlas-chip-btn');
      if (!b) return;
      b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      state.domains = pressed(tools, 'data-atlas-domain');
      state.statuses = pressed(tools, 'data-atlas-status');
      applyFilter();
    });
  }
  function pressed(scope, attr) {
    return all('.atlas-chip-btn[' + attr + ']', scope).filter(function (b) { return b.getAttribute('aria-pressed') === 'true'; })
      .map(function (b) { return b.getAttribute(attr); });
  }
  function applyFilter() {
    var ws = words(state.q);
    var any = ws.length || state.domains.length || state.statuses.length;
    var shown = 0;
    order.forEach(function (id) {
      var c = claims[id];
      var on = !(state.domains.length && state.domains.indexOf(c.domain) < 0) &&
               !(state.statuses.length && state.statuses.indexOf(c.status) < 0) &&
               ws.every(function (w) { return c.hay.indexOf(w) >= 0; });
      c.filtered = !on;
      if (on) shown++;
      if (c.row) c.row.hidden = !on;
      if (c.node) c.node.classList.toggle('is-out', !!any && !on);
    });
    Object.keys(edges).forEach(function (k) {
      var e = edges[k];
      if (e.path) e.path.classList.toggle('is-out', !!any && (claims[e.source].filtered || claims[e.target].filtered));
    });
    if (countLine) countLine.textContent = !any ? word('count-all') : shown ? word('count-some') : word('count-none');
  }
  applyFilter();

  function indexLinks() {
    return all('tbody tr', index || body).filter(function (tr) { return !tr.hidden; })
      .map(function (tr) { return tr.querySelector('th .atlas-link'); }).filter(Boolean);
  }
  if (index) {
    /* Up and Down move between the claims of the index; Home and End go to the first and the last. */
    index.addEventListener('keydown', function (event) {
      if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
      var link = event.target.closest && event.target.closest('tbody th .atlas-link');
      if (!link) return;
      var links = indexLinks();
      var i = links.indexOf(link);
      var to = null;
      if (event.key === 'ArrowDown') to = links[i + 1];
      else if (event.key === 'ArrowUp') to = i === 0 ? input : links[i - 1];
      else if (event.key === 'Home') to = links[0];
      else if (event.key === 'End') to = links[links.length - 1];
      if (to) { event.preventDefault(); to.focus(); }
    });
  }

  /* The selection in the map and the index: every recorded relation of the selected claim. */
  function highlight() {
    if (map) {
      map.classList.toggle('is-focus', !!current);
      all('.atlas-node', map).forEach(function (n) { n.classList.remove('is-sel', 'is-on'); });
      Object.keys(edges).forEach(function (k) {
        var p = edges[k].path;
        if (!p) return;
        p.classList.remove('is-on');
        p.setAttribute('marker-end', 'url(#atlas-arrow)');
      });
    }
    order.forEach(function (id) {
      var r = claims[id].row;
      if (!r) return;
      r.classList.remove('is-sel');
      var a = r.querySelector('th .atlas-link');
      if (a) a.removeAttribute('aria-current');
    });
    if (!current) return;
    var c = claims[current];
    if (c.row) {
      c.row.classList.add('is-sel');
      var a = c.row.querySelector('th .atlas-link');
      if (a) a.setAttribute('aria-current', 'true');
    }
    if (c.node) c.node.classList.add('is-sel', 'is-on');
    c.into.concat(c.out).forEach(function (e) {
      if (e.path) {
        e.path.classList.add('is-on');
        e.path.setAttribute('marker-end', 'url(#atlas-arrow-on)');
        e.path.parentNode.appendChild(e.path);  /* drawn last, so above the other lines */
      }
      var other = claims[e.source === current ? e.target : e.source];
      if (other.node) other.node.classList.add('is-on');
    });
    /* The selected mark and row are brought into view inside their own boxes (the map and a long index scroll
       in boxes of their own); only those boxes move, never the page. */
    keepInBox(c.node, map && map.querySelector('.atlas-map-scroll'), 'x');
    keepInBox(c.row, body.querySelector('.atlas-index-long .atlas-table-wrap'), 'y');
  }
  function keepInBox(item, box, axis) {
    if (!item || !box || !item.getBoundingClientRect) return;
    var x = axis === 'x';
    if ((x ? box.scrollWidth - box.clientWidth : box.scrollHeight - box.clientHeight) <= 1) return;
    var r = item.getBoundingClientRect(), b = box.getBoundingClientRect();
    var lo = x ? r.left : r.top, hi = x ? r.right : r.bottom, blo = x ? b.left : b.top, bhi = x ? b.right : b.bottom;
    if (hi - lo <= 0 || (lo >= blo && hi <= bhi)) return;
    var by = (lo + hi) / 2 - (blo + bhi) / 2;
    if (x) box.scrollLeft += by; else box.scrollTop += by;
  }

  /* The diagram of the selected claim: on the left the claims with a relation into it, on the right the
     claims it has a relation to; one line for each recorded relation and no other. Its marks are links. */
  function pill(c, x, y, self) {
    var a = svg('a', { 'class': 'atlas-node' + (self ? ' is-self' : ''), href: '#atlas-c-' + c.id, tabindex: '-1',
                       'data-claim-ref': c.id, transform: 'translate(' + x + ' ' + y + ')' });
    if (c.node) Array.prototype.slice.call(c.node.childNodes).forEach(function (n) { a.appendChild(n.cloneNode(true)); });
    return a;
  }
  function kindClass(relation) {
    var info = relations[relation];
    return 'rk-' + (info ? info.style : '0');
  }
  function svgText(x, y, text) {
    var t = svg('text', { x: String(x), y: String(y), 'class': 'atlas-hood-side', 'text-anchor': 'middle' });
    t.textContent = text;
    return t;
  }
  function neighbourhood(c) {
    var wrap = el('div', 'atlas-hood');
    wrap.appendChild(el('p', 'atlas-sub-h', word('relations')));
    var mine = c.into.concat(c.out);
    if (!mine.length) {
      wrap.appendChild(el('p', 'atlas-none', word('relations-none')));
      return wrap;
    }
    var kinds = [];
    mine.forEach(function (e) { if (kinds.indexOf(e.relation) < 0) kinds.push(e.relation); });
    if (kinds.length > 1) {
      var legend = el('div', 'atlas-hood-legend');
      legend.setAttribute('role', 'group');
      legend.setAttribute('aria-label', word('show'));
      legend.appendChild(el('span', 'atlas-chips-label', word('show')));
      kinds.forEach(function (r) {
        var info = relations[r] || { label: r, style: '0' };
        var b = el('button', 'atlas-chip-btn');
        b.type = 'button';
        b.setAttribute('data-atlas-relation', r);
        b.setAttribute('aria-pressed', hiddenRelations[r] ? 'false' : 'true');
        var sw = svg('svg', { 'class': 'atlas-swatch ' + kindClass(r), viewBox: '0 0 28 8', width: '28', height: '8',
                              'aria-hidden': 'true', focusable: 'false' });
        sw.appendChild(svg('path', { d: 'M1 4H27' }));
        b.appendChild(sw);
        b.appendChild(el('span', null, info.label));
        legend.appendChild(b);
      });
      wrap.appendChild(legend);
      var note = el('p', 'atlas-hidden-note');
      note.hidden = true;
      wrap.appendChild(note);
    }
    var left = [];
    var right = [];
    c.into.forEach(function (e) { if (left.indexOf(e.source) < 0) left.push(e.source); });
    c.out.forEach(function (e) { if (right.indexOf(e.target) < 0) right.push(e.target); });
    /* A claim with many relations: the drawing keeps the first twelve claims on each side and says so; the lists
       below it keep every relation. */
    var CAP = 12;
    if (left.length > CAP || right.length > CAP) {
      left = left.slice(0, CAP);
      right = right.slice(0, CAP);
      wrap.appendChild(el('p', 'atlas-hidden-note', word('hood-cap')));
    }
    var W = 320, row = 30, top = 26, lx = 46, cx = 160, rx = 274, half = 19;
    var rows = Math.max(left.length, right.length, 1);
    var H = top + rows * row + 4;
    var cy = top + ((rows - 1) * row) / 2 + 9;
    var s = svg('svg', { 'class': 'atlas-hood-svg', viewBox: '0 0 ' + W + ' ' + H, width: String(W), height: String(H),
                         'aria-hidden': 'true', focusable: 'false' });
    var defs = svg('defs');
    [['atlas-hood-arrow', 'atlas-arrow'], ['atlas-hood-arrow-on', 'atlas-arrow-on']].forEach(function (m) {
      var marker = svg('marker', { id: m[0], 'class': m[1], viewBox: '0 0 8 8', refX: '7.5', refY: '4', markerWidth: '7',
                                   markerHeight: '7', markerUnits: 'userSpaceOnUse', orient: 'auto' });
      marker.appendChild(svg('path', { d: 'M0 0.6 7.6 4 0 7.4z' }));
      defs.appendChild(marker);
    });
    s.appendChild(defs);
    if (left.length) s.appendChild(svgText(lx, 12, word('side-in')));
    if (right.length) s.appendChild(svgText(rx, 12, word('side-out')));
    var y = {};
    function place(list, key) {
      var start = top + ((rows - list.length) * row) / 2 + 9;
      list.forEach(function (id, i) { y[key + id] = start + i * row; });
    }
    place(left, 'L');
    place(right, 'R');
    var lines = svg('g');
    var nodes = svg('g');
    function curve(x0, y0, x1, y1, e) {
      var bend = (x1 - x0) / 2;
      lines.appendChild(svg('path', {
        'class': 'atlas-hood-edge ' + kindClass(e.relation), 'data-edge-id': e.id, 'data-source': e.source, 'data-target': e.target,
        'data-relation': e.relation, 'marker-end': 'url(#atlas-hood-arrow)',
        d: 'M' + x0 + ' ' + y0 + 'C' + (x0 + bend) + ' ' + y0 + ' ' + (x1 - bend) + ' ' + y1 + ' ' + x1 + ' ' + y1
      }));
    }
    c.into.forEach(function (e, i) {
      if (left.indexOf(e.source) < 0) return;
      var dy = c.into.filter(function (f, j) { return j < i && f.source === e.source; }).length * 4;
      curve(lx + half, y['L' + e.source] + dy, cx - half, cy + dy, e);
    });
    c.out.forEach(function (e, i) {
      if (right.indexOf(e.target) < 0) return;
      var dy = c.out.filter(function (f, j) { return j < i && f.target === e.target; }).length * 4;
      curve(cx + half, cy + dy, rx - half, y['R' + e.target] + dy, e);
    });
    left.forEach(function (id) { nodes.appendChild(pill(claims[id], lx, y['L' + id], false)); });
    right.forEach(function (id) { nodes.appendChild(pill(claims[id], rx, y['R' + id], false)); });
    nodes.appendChild(pill(c, cx, cy, true));
    s.appendChild(lines);
    s.appendChild(nodes);
    wrap.appendChild(s);
    return wrap;
  }

  /* Hiding a relation in the pane hides it in the pane's diagram and lists only, and says so. */
  function applyRelationFilter() {
    if (!current) return;
    var article = claims[current].article;
    all('.atlas-rel[data-relation]', article).forEach(function (li) { li.hidden = !!hiddenRelations[li.getAttribute('data-relation')]; });
    all('.atlas-hood-edge', article).forEach(function (p) { p.classList.toggle('is-hidden', !!hiddenRelations[p.getAttribute('data-relation')]); });
    var note = article.querySelector('.atlas-hidden-note');
    if (note) {
      var names = Object.keys(hiddenRelations).filter(function (r) { return relations[r]; }).map(function (r) { return relations[r].label; });
      note.hidden = !names.length;
      note.textContent = names.length ? word('hidden') + ' ' + names.join(', ') : '';
    }
  }
  function markScrollers(scope) {
    /* A formula wider than its box scrolls in it; such a box takes focus so that keys can scroll it. */
    all('.atlas-math-display, .atlas-math-long', scope || body).forEach(function (box) {
      if (box.closest('a, button')) return;
      if (box.scrollWidth > box.clientWidth + 1) box.setAttribute('tabindex', '0');
      else box.removeAttribute('tabindex');
    });
  }

  /* Selection follows the address. */
  function select(id) {
    var c = claims[id];
    if (current && claims[current]) {
      var was = claims[current].article;
      was.classList.remove('is-selected');
      all('.atlas-hood', was).forEach(function (n) { n.parentNode.removeChild(n); });
      all('.atlas-rel[hidden]', was).forEach(function (li) { li.hidden = false; });
    }
    current = id;
    /* Only the claim shown is unhidden, so that no focus (the page's Tab past the glossary card) can land in a claim
       the pane does not show; print shows them all. */
    order.forEach(function (k) { claims[k].article.hidden = k !== id; });
    full.classList.toggle('has-selection', !!c);
    layout();
    locate(c);
    emptyLine.hidden = !!c;
    if (c) {
      c.article.classList.add('is-selected');
      var first = c.article.querySelector(':scope > .atlas-rel-block');
      c.article.insertBefore(neighbourhood(c), first);
      if (path) {
        var here = path.steps[path.at] && path.steps[path.at].claim === id;
        if (!here) for (var i = 0; i < path.steps.length; i++) if (path.steps[i].claim === id) { path.at = i; break; }
      }
      applyRelationFilter();
    }
    renderPathBar();
    markStage();
    highlight();
    markScrollers(full);
  }
  /* On a wide screen the pane has a column of its own while it is shown: a claim is selected and the reader has not
     closed it. It covers nothing; the atlas reflows into the other column and the reader's place is kept. */
  function layout(anchor) {
    var open = !!current && !full.classList.contains('is-closed');
    if (open === body.classList.contains('has-pane')) return;
    var keep = wide() ? placeKeeper(open, anchor) : null;
    body.classList.toggle('has-pane', open);
    if (keep) keep();
  }
  function closePane(anchor) { full.classList.add('is-closed'); layout(anchor); }
  /* The locator marks the claim shown at its place in the whole atlas: its dot, a ring, and its number with its status
     mark as on its pill in the map; and the band of its domain. Nothing else changes on it. */
  function locate(c) {
    if (!locator) return;
    locator.hidden = !c;
    if (!c || !locBox) return;
    all('.atlas-locator-track', locator).forEach(function (r) { r.classList.toggle('is-here', r.getAttribute('data-domain-ref') === c.domain); });
    all('circle[data-claim-ref]', locator).forEach(function (d) { d.classList.toggle('is-here', d.getAttribute('data-claim-ref') === c.id); });
    var dot = locator.querySelector('circle[data-claim-ref="' + c.id + '"]');
    if (!dot || !locRing || !locNo) return;
    var x = +dot.getAttribute('cx'), y = +dot.getAttribute('cy');
    locRing.setAttribute('cx', String(x));
    locRing.setAttribute('cy', String(y));
    locNo.textContent = '';
    var mark = c.article.querySelector('.atlas-chip .mark');
    if (mark) locNo.appendChild(mark.cloneNode(true));
    locNo.appendChild(doc.createTextNode(c.number));
    locNo.style.left = (100 * x / locBox.w).toFixed(2) + '%';
    locNo.style.top = (100 * y / locBox.h).toFixed(2) + '%';
    locNo.classList.toggle('is-west', x / locBox.w > 0.72);
  }
  /* When the pane opens or closes its column, the atlas column reflows; the place the reader is at is put back where it
     was on the screen. The place is chosen by direction, and only among elements in view that move with the page (none
     inside a fixed or sticky box, none inside the pane, which is what changes):
     an anchor given by the caller (the control focus returns to when the reader closes the pane), when in view;
     opening: the element the reader acted on in the atlas column, else the focused element in the atlas column;
     closing (a link or Back has taken the reader out of the atlas): the element the address names outside the atlas,
     else the focused element outside the atlas;
     and else the first part of the atlas in view. */
  function placeKeeper(opening, anchor) {
    var main = body.querySelector('.atlas-main');
    if (!main) return null;
    var vh = window.innerHeight || doc.documentElement.clientHeight || 0;
    function moves(n) {
      for (var p = n; p && p !== doc.body && p !== doc.documentElement; p = p.parentElement) {
        var pos = window.getComputedStyle ? window.getComputedStyle(p).position : '';
        if (pos === 'fixed' || pos === 'sticky') return false;
      }
      return true;
    }
    function usable(n) {
      if (!n || !n.isConnected || n === doc.body || n === doc.documentElement || full.contains(n) || !n.getBoundingClientRect) return false;
      var r = n.getBoundingClientRect();
      if ((!r.width && !r.height) || r.bottom <= 0 || r.top >= vh) return false;
      return moves(n);
    }
    var a = null;
    var from = activation && activation.from;
    var focused = doc.activeElement;
    if (usable(anchor)) a = anchor;
    else if (opening) {
      if (usable(from) && main.contains(from)) a = from;
      else if (usable(focused) && main.contains(focused)) a = focused;
    } else {
      var id = decode(location.hash.slice(1));
      var target = id ? doc.getElementById(id) : null;
      if (usable(target) && !mount.contains(target)) a = target;
      else if (usable(focused) && !mount.contains(focused)) a = focused;
    }
    if (!a) a = all(':scope > .atlas-part', main).filter(usable)[0] || null;
    if (!a) return null;
    var before = a.getBoundingClientRect().top;
    return function () {
      var r = a.getBoundingClientRect();
      if (!r.width && !r.height) return; /* hidden by the change itself: nothing to keep */
      var by = r.top - before;
      if (Math.abs(by) <= 1) return;
      try { window.scrollBy({ top: by, left: 0, behavior: 'instant' }); } catch (e) { window.scrollBy(0, by); }
    };
  }
  function addressClaim() {
    var m = CLAIM.exec(decode(location.hash.slice(1)));
    return m && claims[m[1]] ? m[1] : null;
  }
  function insideAtlas() {
    var id = decode(location.hash.slice(1));
    var target = id ? doc.getElementById(id) : null;
    return !!(target && mount.contains(target));
  }
  function focusTitle() {
    var t = current && claims[current].title;
    if (!t) return;
    t.setAttribute('tabindex', '-1');
    try { t.focus({ preventScroll: true }); } catch (e) { t.focus(); }
  }
  var lastAddress = null;
  /* Comparisons, reading paths and the claims of each domain are folded (details.atlas-fold). An address, a link or
     a search result that leads inside a fold opens it; a target that was hidden in a closed fold is then scrolled to. */
  function unfold(target) {
    var hidden = false;
    for (var n = target; n && n !== mount; n = n.parentElement) {
      if (n.localName === 'details' && !n.open) {
        if (n !== target) hidden = true;
        n.open = true;
      }
    }
    return hidden;
  }
  function unfoldAddress(arrival) {
    var hid = decode(location.hash.slice(1));
    var target = hid ? doc.getElementById(hid) : null;
    if (!target || !mount.contains(target) || full.contains(target)) return;
    if (unfold(target) || arrival) target.scrollIntoView({ block: 'start', behavior: 'auto' });
  }
  function sync(arrival) {
    var address = location.hash;
    var changed = address !== lastAddress;
    lastAddress = address;
    if (changed) unfoldAddress(arrival);
    var id = addressClaim();
    if (id) {
      var was = current;
      var inPane = full.contains(doc.activeElement);
      var mine = activation && activation.id === id && Date.now() - activation.t < 2000;
      /* A sheet the reader closed stays closed until the address changes or the reader selects a claim:
         the page's own state announcements (search, filters) do not reopen it. */
      if (changed || mine) full.classList.remove('is-closed');
      if (id !== current) select(id); else layout();
      var stepRole = mine && activation.step;
      if (mine) origin = activation.from;
      activation = null;
      if (stepRole) focusStep(stepRole); /* Previous and Next keep the keyboard on the path bar */
      else if (mine || (id !== was && inPane)) focusTitle(); /* Back or Forward inside the pane: focus follows the claim */
      else if (arrival && wide()) (claims[id].row || map || body).scrollIntoView({ block: 'center', behavior: 'auto' });
    } else if (current && !insideAtlas()) {
      /* The address has left the atlas: nothing is selected. Another part of the atlas keeps the pane. */
      var hadFocus = full.contains(doc.activeElement);
      select(null);
      if (hadFocus) back();
    }
  }
  window.addEventListener('hashchange', function () { sync(false); });
  doc.addEventListener('qh:state', function () { sync(false); });
  /* A result of the page's search inside the atlas: the page has set the address and asks the atlas to show it. A claim
     is shown in the pane, with focus on its heading; other parts of the atlas are left to the page to scroll to. */
  mount.addEventListener('qh:reveal', function (event) {
    var id = event.detail && event.detail.id;
    var m = typeof id === 'string' ? CLAIM.exec(id) : null;
    if (!m || !claims[m[1]]) {
      /* Another atlas unit (a comparison, a path, a domain): opened in place, then left to the page to scroll to. */
      var unit = typeof id === 'string' ? doc.getElementById(id) : null;
      if (unit && mount.contains(unit)) unfold(unit);
      return;
    }
    event.preventDefault();
    full.classList.remove('is-closed');
    if (current !== m[1]) select(m[1]); else layout();
    lastAddress = location.hash;
    if (wide()) (claims[m[1]].row || map || body).scrollIntoView({ block: 'center', behavior: smooth() });
    focusTitle();
  });

  /* Links inside the atlas. A claim link is followed by the browser and selects through the address; a link
     to the page outside the atlas goes through the page's qh:navigate, which opens and focuses its target. */
  mount.addEventListener('click', function (event) {
    if (event.defaultPrevented || !plainClick(event)) return;
    var a = event.target.closest && event.target.closest('a[href^="#"]');
    if (!a || !mount.contains(a)) return;
    var id = decode(a.getAttribute('href').slice(1));
    var target = id ? doc.getElementById(id) : null;
    if (!target) return;
    if (!mount.contains(target)) {
      var ask;
      try { ask = new CustomEvent('qh:navigate', { bubbles: true, cancelable: true, detail: { id: id } }); } catch (e) { ask = null; }
      if (ask && !a.dispatchEvent(ask)) event.preventDefault(); /* the page has shown it */
      if (!wide()) closePane();
      return;
    }
    var m = CLAIM.exec(id);
    if (m && claims[m[1]]) {
      activation = { id: m[1], from: full.contains(a) ? origin : a, t: Date.now() };
      if (a.hasAttribute('data-step') && path) { path.at = +a.getAttribute('data-step'); activation.step = a.getAttribute('data-step-role'); }
      if (a.hasAttribute('data-follow')) startPath(a.getAttribute('data-follow'));
      if (location.hash === '#' + id) { event.preventDefault(); sync(false); } /* the address already names it */
      return;
    }
    if (full.contains(a) && !wide()) closePane(); /* the sheet makes way for the part it links to */
    /* The locator returns to the map: after the browser has followed the link, the map takes the keyboard with its
       cursor on the claim shown, whose pill is already in view in the map's box and highlighted. */
    if (a.classList.contains('atlas-locator-link') && current && mapBox && moveCursor) {
      var shown = current;
      setTimeout(function () {
        try { mapBox.focus({ preventScroll: true }); } catch (e) { mapBox.focus(); }
        if (claims[shown] && claims[shown].node) moveCursor(shown);
      }, 0);
    }
  });

  full.addEventListener('click', function (event) {
    var b = event.target.closest('.atlas-hood-legend .atlas-chip-btn');
    if (!b) return;
    var r = b.getAttribute('data-atlas-relation');
    var on = b.getAttribute('aria-pressed') !== 'true';
    b.setAttribute('aria-pressed', on ? 'true' : 'false');
    if (on) delete hiddenRelations[r]; else hiddenRelations[r] = true;
    applyRelationFilter();
  });
  /* Pointing at a line or a mark of the diagram, or at a relation in a list, marks the line and the relation. */
  function pair(event, on) {
    if (!current) return;
    var t = event.target.closest && event.target.closest('.atlas-rel[data-edge-id], .atlas-hood-edge[data-edge-id], .atlas-hood-svg .atlas-node[data-claim-ref]');
    if (!t || !claims[current].article.contains(t)) return;
    var ids;
    if (t.hasAttribute('data-edge-id')) ids = [t.getAttribute('data-edge-id')];
    else {
      var other = t.getAttribute('data-claim-ref');
      ids = claims[current].into.concat(claims[current].out)
        .filter(function (e) { return e.source === other || e.target === other; }).map(function (e) { return e.id; });
    }
    ids.forEach(function (k) {
      all('[data-edge-id="' + k + '"]', claims[current].article).forEach(function (n) {
        n.classList.toggle('is-on', on);
        if (n.localName === 'path') n.setAttribute('marker-end', on ? 'url(#atlas-hood-arrow-on)' : 'url(#atlas-hood-arrow)');
      });
    });
  }
  full.addEventListener('mouseover', function (event) { pair(event, true); });
  full.addEventListener('mouseout', function (event) { pair(event, false); });
  full.addEventListener('focusin', function (event) { pair(event, true); });
  full.addEventListener('focusout', function (event) { pair(event, false); });

  function backTarget() {
    /* Focus returns to the control that made the selection, else to the claim in the index, else to the filter. */
    var to = origin && doc.contains(origin) && !full.contains(origin) && !origin.closest('[aria-hidden="true"]') &&
             origin.getClientRects().length ? origin : null;
    if (!to && current && claims[current].row && !claims[current].row.hidden) to = claims[current].row.querySelector('th .atlas-link');
    return to || input;
  }
  function back(to) {
    to = to || backTarget();
    if (to) { try { to.focus({ preventScroll: wide() }); } catch (e) { to.focus(); } }
  }
  /* Close and Escape put the pane away and give its column back; the place of the control focus returns to is kept. */
  function dismiss() { var to = backTarget(); closePane(to); back(to); }
  closeButton.addEventListener('click', dismiss);
  /* On a narrow screen the sheet covers the page: when focus leaves it for the page, it closes, so that focus is
     never on a control hidden under it. Focus that moves into the page's term card keeps it open. */
  full.addEventListener('focusout', function (event) {
    var to = event.relatedTarget;
    if (wide() || !to || full.contains(to)) return;
    var card = doc.getElementById('card');
    if (card && card.contains(to)) return;
    closePane();
  });
  full.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape') return;
    var card = doc.getElementById('card');
    if (card && !card.hidden) return; /* the page's term card closes first, by its own handler */
    event.preventDefault();
    dismiss();
  });

  /* The map: pointing at a mark, or moving the keyboard cursor onto it, names its claim and marks its relations. */
  if (map) {
    var tip = el('div', 'atlas-tip');
    tip.hidden = true;
    tip.setAttribute('aria-hidden', 'true');
    map.appendChild(tip);
    map.addEventListener('mouseover', function (event) {
      var node = event.target.closest('.atlas-node[data-claim-ref]');
      if (node) showTip(node);
    });
    var showTip = function (node) {
      var c = claims[node.getAttribute('data-claim-ref')];
      if (!c) return;
      tip.textContent = '';
      tip.appendChild(el('span', 'atlas-num', c.number));
      var t = el('span');
      t.innerHTML = c.title.innerHTML;
      all('[id]', t).forEach(function (n) { n.removeAttribute('id'); });
      tip.appendChild(doc.createTextNode(' '));
      tip.appendChild(t);
      var rels = c.out.map(function (e) { return { e: e, to: true }; }).concat(c.into.map(function (e) { return { e: e, to: false }; }));
      if (rels.length) {
        var list = el('span', 'atlas-tip-rels');
        rels.slice(0, TIP_RELATIONS).forEach(function (r) {
          var other = claims[r.to ? r.e.target : r.e.source];
          var line = el('span', 'atlas-tip-rel');
          line.textContent = r.to ? word('tip-to') + ' ' + r.e.label + ' ' + word('number') + ' ' + other.number
                                  : word('tip-from') + ' ' + word('number') + ' ' + other.number + ' ' + r.e.label;
          list.appendChild(line);
        });
        if (rels.length > TIP_RELATIONS) list.appendChild(el('span', 'atlas-tip-rel', word('tip-more')));
        tip.appendChild(list);
      }
      tip.hidden = false;
      var r = node.getBoundingClientRect();
      var m = map.getBoundingClientRect();
      var left = Math.max(0, Math.min(r.left - m.left + r.width / 2 - tip.offsetWidth / 2, m.width - tip.offsetWidth));
      tip.style.left = left + 'px';
      tip.style.top = (r.top - m.top - tip.offsetHeight - 8) + 'px';
      c.into.concat(c.out).forEach(function (e) { if (e.path) e.path.classList.add('is-on'); });
    };
    map.addEventListener('mouseout', function (event) {
      var node = event.target.closest('.atlas-node[data-claim-ref]');
      if (!node || (event.relatedTarget && node.contains(event.relatedTarget))) return;
      if (cursor) { showTip(claims[cursor].node); return; }
      tip.hidden = true;
      highlight();
    });

    /* One tab stop: the map box. The arrow keys move a cursor over the marks (up and down a column, across to the
       nearest mark of the next column), Home and End go to the first and last claim, Enter shows the claim in the
       pane, Escape leaves the cursor. The claim under the cursor is named in the tip and announced. */
    var mapBox = map.querySelector('.atlas-map-scroll');
    var mapSay = map.querySelector('[data-atlas-map-say]');
    var at = {};
    order.forEach(function (id) {
      var n = claims[id].node;
      var m = n && /translate\(([-\d.]+)[ ,]+([-\d.]+)\)/.exec(n.getAttribute('transform') || '');
      if (m) at[id] = { x: +m[1], y: +m[2] };
    });
    var placed = order.filter(function (id) { return at[id]; });
    var cursor = null;
    var statusWord = function (c) {
      var k = body.querySelector('.atlas-key-item[data-key-status="' + c.status + '"] dt span');
      return k ? textOf(k) : '';
    };
    var moveCursor = function (id) {
      if (cursor && claims[cursor].node) claims[cursor].node.classList.remove('is-cursor');
      cursor = id;
      if (!id) { tip.hidden = true; highlight(); return; }
      var c = claims[id];
      c.node.classList.add('is-cursor');
      keepInBox(c.node, mapBox, 'x');
      keepInBox(c.node, mapBox, 'y');
      highlight();
      showTip(c.node);
      if (mapSay) mapSay.textContent = word('number') + ' ' + c.number + ': ' + textOf(c.title) + ' (' + statusWord(c) + ')';
    };
    var step = function (dir) {
      if (!cursor) return current && at[current] ? current : placed[0];
      var p = at[cursor], best = null, score = Infinity;
      placed.forEach(function (id) {
        var q = at[id];
        if (id === cursor) return;
        var dx = q.x - p.x, dy = q.y - p.y, d;
        if (dir === 'down' && Math.abs(dx) < 1 && dy > 0) d = dy;
        else if (dir === 'up' && Math.abs(dx) < 1 && dy < 0) d = -dy;
        else if (dir === 'right' && dx > 1) d = dx * 1000 + Math.abs(dy);
        else if (dir === 'left' && dx < -1) d = -dx * 1000 + Math.abs(dy);
        else return;
        if (d < score) { score = d; best = id; }
      });
      if (!best && (dir === 'down' || dir === 'up')) {
        var i = placed.indexOf(cursor) + (dir === 'down' ? 1 : -1);
        best = placed[i] || null; /* past the end of a column, on to the next claim in order */
      }
      return best || cursor;
    };
    if (mapBox) {
      mapBox.addEventListener('keydown', function (event) {
        var k = event.key, to = null;
        if (k === 'ArrowDown') to = step('down');
        else if (k === 'ArrowUp') to = step('up');
        else if (k === 'ArrowRight') to = step('right');
        else if (k === 'ArrowLeft') to = step('left');
        else if (k === 'Home') to = placed[0];
        else if (k === 'End') to = placed[placed.length - 1];
        else if (k === 'Enter' && cursor) {
          event.preventDefault();
          var link = claims[cursor].row && claims[cursor].row.querySelector('th .atlas-link');
          if (link) { link.click(); if (activation) activation.from = mapBox; }
          return;
        } else if (k === 'Escape' && cursor) { event.preventDefault(); moveCursor(null); return; }
        else return;
        event.preventDefault();
        if (to) moveCursor(to);
      });
      mapBox.addEventListener('blur', function () { moveCursor(null); });
      /* The fades at the sides of the map box say which way it scrolls. (Named apart from the table of edges above,
         which highlight() and the filter read.) */
      var mapFades = function () {
        var f = mapBox.parentNode;
        f.classList.toggle('more-left', mapBox.scrollLeft > 2);
        f.classList.toggle('more-right', mapBox.scrollLeft + mapBox.clientWidth < mapBox.scrollWidth - 2);
      };
      mapBox.addEventListener('scroll', mapFades, { passive: true });
      window.addEventListener('resize', mapFades);
      mapFades();
    }
  }

  /* Reading paths: Follow walks through the claims of a path, stage by stage. Every step is a claim link. */
  var path = null;
  var paths = {};
  all('.atlas-path[data-path-id]', body).forEach(function (article) {
    var steps = [];
    all('.atlas-stage', article).forEach(function (stage) {
      var j = +stage.getAttribute('data-stage');
      all(':scope > .atlas-stage-h .atlas-link, :scope > .atlas-claimlist .atlas-link', stage).forEach(function (a) {
        var m = CLAIM.exec(decode(a.getAttribute('href').slice(1)));
        if (m && claims[m[1]]) steps.push({ stage: j, claim: m[1] });
      });
    });
    if (!steps.length) return;
    var pid = article.getAttribute('data-path-id');
    paths[pid] = { id: pid, article: article, steps: steps, title: textOf(article.querySelector('.atlas-path-h')),
                   kind: textOf(article.querySelector('.atlas-kind-tag')) };
    var p = el('p', 'atlas-path-tools');
    var follow = el('a', 'link-btn atlas-follow', word('follow'));
    follow.href = '#atlas-c-' + steps[0].claim;
    follow.setAttribute('data-follow', pid);
    follow.setAttribute('data-step', '0');
    p.appendChild(follow);
    var kind = article.querySelector('.atlas-path-kind');
    if (kind) kind.parentNode.insertBefore(p, kind.nextSibling); else article.appendChild(p);
  });
  function startPath(pid) {
    var p = paths[pid];
    if (!p) return;
    path = { id: pid, article: p.article, steps: p.steps, at: 0, title: p.title, kind: p.kind };
  }
  function stepLink(text, i, role) {
    var a = el('a', 'link-btn atlas-step', text);
    a.href = '#atlas-c-' + path.steps[i].claim;
    a.setAttribute('data-step', String(i));
    if (role) a.setAttribute('data-step-role', role);
    return a;
  }
  function renderPathBar() {
    pathBar.textContent = '';
    pathBar.hidden = !(path && current);
    if (pathBar.hidden) return;
    var step = path.steps[path.at];
    var on = step && step.claim === current;
    var stage = path.article.querySelector('.atlas-stage[data-stage="' + step.stage + '"]');
    var title = el('p');
    title.appendChild(el('strong', null, path.title));
    if (path.kind) { title.appendChild(doc.createTextNode(' ')); title.appendChild(el('span', 'atlas-kind-tag', path.kind)); }
    pathBar.appendChild(title);
    pathBar.appendChild(el('p', 'atlas-pathbar-where', fill(word('position'), { n: step.stage + 1 }) +
                           (stage ? ' · ' + textOf(stage.querySelector('.atlas-stage-label, .atlas-stage-h .atlas-link-title')) : '')));
    var actions = el('p', 'atlas-pathbar-actions');
    if (on) {
      if (path.at > 0) actions.appendChild(stepLink(word('prev'), path.at - 1, 'prev'));
      if (path.at < path.steps.length - 1) actions.appendChild(stepLink(word('next'), path.at + 1, 'next'));
    } else {
      actions.appendChild(stepLink(word('resume'), path.at));
    }
    var leave = el('button', 'link-btn', word('leave'));
    leave.type = 'button';
    leave.addEventListener('click', function () { path = null; renderPathBar(); markStage(); focusTitle(); });
    actions.appendChild(leave);
    pathBar.appendChild(actions);
  }
  /* After Previous or Next, focus stays on the control of the same kind (or the other one at an end of the path), and
     the claim now shown is announced. */
  function focusStep(role) {
    var to = pathBar.querySelector('[data-step-role="' + role + '"]') || pathBar.querySelector('[data-step-role]') ||
             pathBar.querySelector('button');
    if (to) { try { to.focus({ preventScroll: true }); } catch (e) { to.focus(); } }
    if (paneSay && current) paneSay.textContent = textOf(pathBar.querySelector('.atlas-pathbar-where')) + ': ' + textOf(claims[current].title);
  }
  function markStage() {
    all('.atlas-stage.is-here', body).forEach(function (s) { s.classList.remove('is-here'); });
    if (!path || !current) return;
    var step = path.steps[path.at];
    if (step && step.claim === current) {
      var stage = path.article.querySelector('.atlas-stage[data-stage="' + step.stage + '"]');
      if (stage) stage.classList.add('is-here');
    }
  }

  /* Printing opens the atlas's own disclosures (the page leaves the atlas alone) and restores them afterwards. */
  var opened = null;
  window.addEventListener('beforeprint', function () {
    opened = all('details', body).filter(function (d) { return !d.open; });
    opened.forEach(function (d) { d.open = true; });
  });
  window.addEventListener('afterprint', function () {
    if (opened) opened.forEach(function (d) { d.open = false; });
    opened = null;
  });

  /* The pane: a column of its own beside the atlas when the window is wide, a sheet at the foot when narrow. */
  window.addEventListener('resize', function () { markScrollers(body); });

  /* Links to questions of the page take the question's own heading as their text. */
  all('a.atlas-question-link[data-question-ref]', body).forEach(function (a) {
    var q = doc.getElementById(a.getAttribute('data-question-ref'));
    var h = q && q.querySelector('h3');
    if (!h || !textOf(h)) return;
    /* The heading as the page sets it (its formulae included), without its own links, buttons or ids. */
    var copy = h.cloneNode(true);
    all('a, button', copy).forEach(function (n) {
      while (n.firstChild) n.parentNode.insertBefore(n.firstChild, n);
      n.parentNode.removeChild(n);
    });
    all('[id]', copy).forEach(function (n) { n.removeAttribute('id'); });
    a.innerHTML = copy.innerHTML;
  });

  select(null);
  sync(true);
  markScrollers(body);
})();
