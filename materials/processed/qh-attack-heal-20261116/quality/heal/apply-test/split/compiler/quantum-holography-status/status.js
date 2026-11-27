(function () {
  'use strict';
  var root = document.documentElement;
  var doc = document;
  function all(selector, context) { return Array.prototype.slice.call((context || doc).querySelectorAll(selector)); }
  function media(query) { return !!(window.matchMedia && window.matchMedia(query).matches); }
  function smooth() { return media('(prefers-reduced-motion: reduce)') ? 'auto' : 'smooth'; }

  /* Theme: follows the system until the reader chooses; the choice is remembered on this device. */
  var themeButton = doc.querySelector('.theme');
  function currentTheme() {
    var set = root.getAttribute('data-theme');
    if (set) return set;
    return media('(prefers-color-scheme: dark)') ? 'dark' : 'light';
  }
  if (themeButton) {
    themeButton.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('qh-theme', next); } catch (e) { /* storage unavailable */ }
    });
  }

  /* The address carries the reader's search and filters (?q=, ?in=, ?status=, ?show=) so a view can be shared. */
  function readParams() {
    try { return new URLSearchParams(location.search); } catch (e) { return null; }
  }
  function listParam(params, name) {
    var v = params && params.get(name);
    return v ? v.split(',').map(function (s) { return s.trim(); }).filter(Boolean) : [];
  }
  var lastSearch = location.search; /* the query part last written or read, to tell a fragment's popstate from a real one */
  function writeParams(changes) {
    try {
      var params = new URLSearchParams(location.search);
      Object.keys(changes).forEach(function (k) {
        if (changes[k]) params.set(k, changes[k]); else params.delete(k);
      });
      var search = params.toString();
      history.replaceState(history.state, '', location.pathname + (search ? '?' + search : '') + location.hash);
      lastSearch = location.search;
    } catch (e) { /* the address cannot be changed here (some file views) */ }
  }
  function setHash(id, push) {
    var url = location.pathname + location.search + (id ? '#' + id : '');
    try { history[push ? 'pushState' : 'replaceState'](history.state, '', url); } catch (e) { /* as above */ }
  }

  /* Reaching an element: every closed details around it opens, a status filter that hides it is lifted. */
  var rowFilterLift = null;
  function openAround(el) {
    var opened = false;
    for (var d = el; d; d = d.parentElement) {
      if (d.localName === 'details' && !d.open) { d.open = true; opened = true; }
    }
    if (el.closest && el.closest('.statement[hidden]') && rowFilterLift) { rowFilterLift(); opened = true; }
    return opened;
  }
  function focusQuietly(el) {
    if (!el.matches('a[href], button, input, summary, [tabindex]')) {
      el.setAttribute('tabindex', '-1');
      el.addEventListener('blur', function off() { el.removeAttribute('tabindex'); el.removeEventListener('blur', off); });
    }
    try { el.focus({ preventScroll: true }); } catch (e) { el.focus(); }
  }
  function reveal(el, focus) {
    openAround(el);
    requestAnimationFrame(function () {
      el.scrollIntoView({ block: 'start', behavior: smooth() });
      if (focus) focusQuietly(el);
    });
  }

  /* One floating card serves terms, grid cells and column heads. */
  var card = doc.getElementById('card');
  var cardInner = card ? card.querySelector('.card-inner') : null;
  var owner = null;
  var pinned = false;
  var hideTimer = null;
  var hoverCapable = media('(hover: hover) and (pointer: fine)');

  function place(target) {
    var r = target.getBoundingClientRect();
    var narrow = window.innerWidth <= 640;
    card.classList.toggle('sheet', narrow && !hoverCapable);
    if (narrow && !hoverCapable) { card.style.left = ''; card.style.top = ''; return; }
    var width = card.offsetWidth;
    var height = card.offsetHeight;
    var left = r.left + window.scrollX + r.width / 2 - width / 2;
    left = Math.max(window.scrollX + 12, Math.min(left, window.scrollX + doc.documentElement.clientWidth - width - 12));
    var below = r.bottom + window.scrollY + 8;
    var above = r.top + window.scrollY - height - 8;
    var top = (r.bottom + height + 16 > window.innerHeight && r.top - height - 16 > 0) ? above : below;
    card.style.left = left + 'px';
    card.style.top = top + 'px';
  }

  function contentFor(el) {
    if (el.classList.contains('term')) {
      var entry = doc.getElementById(el.getAttribute('data-term'));
      if (!entry) return null;
      var dt = entry.querySelector('dt');
      var dd = entry.querySelector('dd');
      return '<p class="card-term">' + dt.innerHTML + '</p><div>' + dd.innerHTML + '</div>' +
             '<a class="card-more" href="#' + entry.id + '">' + (doc.querySelector('#terms h2') ? doc.querySelector('#terms h2').textContent : 'Terms') + '</a>';
    }
    if (el.classList.contains('cell-btn')) {
      var note = el.parentNode.querySelector('.cell-note');
      var row = el.getAttribute('data-row');
      var rowLink = doc.querySelector('.grid tbody th a[href="#' + row + '"]');
      return note.innerHTML + (rowLink ? '<a class="card-more" href="#' + row + '">' + rowLink.innerHTML + '</a>' : '');
    }
    if (el.classList.contains('col-head')) {
      var def = doc.getElementById('col-' + el.getAttribute('data-col'));
      if (!def) return null;
      return '<p class="card-term">' + def.querySelector('dt').innerHTML + '</p><div>' + def.querySelector('dd').innerHTML + '</div>';
    }
    return null;
  }

  function show(el, pin) {
    if (!card) return;
    clearTimeout(hideTimer);
    var markup = contentFor(el);
    if (markup === null) return;
    if (owner && owner !== el) owner.setAttribute('aria-expanded', 'false');
    owner = el;
    pinned = !!pin;
    cardInner.innerHTML = markup;
    /* The card is a non-modal dialog: named by its heading, described by the text under it. */
    var head = cardInner.querySelector('.card-term, .cell-note-head');
    var text = head && head.nextElementSibling;
    if (head) { head.id = 'card-title'; card.setAttribute('aria-labelledby', 'card-title'); } else card.removeAttribute('aria-labelledby');
    if (text && !text.matches('a')) { text.id = 'card-text'; card.setAttribute('aria-describedby', 'card-text'); } else card.removeAttribute('aria-describedby');
    card.hidden = false;
    el.setAttribute('aria-expanded', 'true');
    place(el);
  }

  function hide() {
    if (!card || card.hidden) return;
    card.hidden = true;
    if (owner) owner.setAttribute('aria-expanded', 'false');
    owner = null;
    pinned = false;
  }

  function hideSoon() {
    if (pinned) return;
    clearTimeout(hideTimer);
    hideTimer = setTimeout(hide, 160);
  }

  /* The next control in reading order after an element, skipping what a closed details or [hidden] conceals. */
  var TABBABLE = 'a[href], button:not([disabled]), input:not([disabled]), summary, [tabindex]:not([tabindex="-1"])';
  function reachable(el) {
    if (el.closest('[hidden], #card')) return false;
    for (var child = el, p = el.parentElement; p; child = p, p = p.parentElement) {
      if (p.localName === 'details' && !p.open && !(child.localName === 'summary' && child.parentNode === p)) return false;
    }
    return true;
  }
  function nextAfter(el) {
    var list = all(TABBABLE);
    for (var i = 0; i < list.length; i++) {
      if (el.compareDocumentPosition(list[i]) & Node.DOCUMENT_POSITION_FOLLOWING && !el.contains(list[i]) && reachable(list[i])) return list[i];
    }
    return null;
  }

  var triggers = '.term, .cell-btn, .col-head';
  doc.addEventListener('click', function (event) {
    var el = event.target.closest(triggers);
    if (el) {
      event.preventDefault();
      if (owner === el && pinned) { hide(); return; }
      show(el, true);
      return;
    }
    if (card && !card.hidden) {
      /* A link in the card leads elsewhere on the page; the card closes behind it. */
      if (!event.target.closest('#card') || event.target.closest('#card a[href]')) hide();
    }
  });
  if (hoverCapable) {
    doc.addEventListener('mouseover', function (event) {
      var el = event.target.closest(triggers);
      if (el && !pinned) { show(el, false); return; }
      if (event.target.closest('#card')) clearTimeout(hideTimer);
    });
    doc.addEventListener('mouseout', function (event) {
      var el = event.target.closest(triggers + ', #card');
      if (el && !(event.relatedTarget && el.contains(event.relatedTarget))) hideSoon();
    });
  }
  var returning = false; /* focus handed back to a trigger after Escape does not reopen its card */
  doc.addEventListener('focusin', function (event) {
    var el = event.target.closest(triggers);
    if (el && !pinned && !returning) show(el, false);
  });
  doc.addEventListener('focusout', function (event) {
    var el = event.target.closest && event.target.closest(triggers);
    var to = event.relatedTarget;
    if (!el || (to && to.closest && to.closest('#card'))) return;
    /* A pinned card closes when focus moves from its trigger to another control; a click on plain text leaves it. */
    if (pinned && el === owner) { if (to) hide(); return; }
    hideSoon();
  });
  /* The Close control comes as an inert template, so a script that does not wire it never sees it; this script puts it
     in the card when it wires it (a control emitted hidden is shown instead). */
  var cardClose = card ? card.querySelector('.card-close') : null;
  var closeTemplate = card && !cardClose ? card.querySelector('template.card-close-template') : null;
  if (closeTemplate && closeTemplate.content && closeTemplate.content.querySelector('.card-close')) {
    cardClose = doc.importNode(closeTemplate.content.querySelector('.card-close'), true);
    closeTemplate.parentNode.replaceChild(cardClose, closeTemplate);
  }
  if (cardClose) {
    cardClose.hidden = false;
    cardClose.addEventListener('click', function () {
      var back = owner;
      hide();
      if (back) { returning = true; back.focus(); returning = false; }
    });
  }
  if (card) {
    /* Focus that leaves the card for anywhere but its own trigger closes it. */
    card.addEventListener('focusout', function (event) {
      var to = event.relatedTarget;
      if (to && (card.contains(to) || to === owner)) return;
      hide();
    });
  }
  doc.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && card && !card.hidden) {
      var back = owner;
      /* Focus goes back to the trigger only from inside the card; anywhere else Escape closes the card and focus stays. */
      var fromCard = card.contains(doc.activeElement);
      hide();
      if (back && fromCard) { returning = true; back.focus(); returning = false; }
      return;
    }
    /* Tab from an opened trigger enters the card's links; leaving the last one continues after the trigger. */
    if (event.key !== 'Tab' || !card || card.hidden || !owner || !pinned) return;
    var inCard = all('a[href], button', card);
    if (!inCard.length) return;
    if (event.target === owner && !event.shiftKey) {
      event.preventDefault();
      inCard[0].focus();
    } else if (card.contains(event.target)) {
      var i = inCard.indexOf(event.target);
      if (event.shiftKey && i === 0) {
        event.preventDefault();
        owner.focus();
      } else if (!event.shiftKey && i === inCard.length - 1) {
        event.preventDefault();
        var from = owner;
        var next = nextAfter(from);
        hide();
        (next || from).focus();
      }
    }
  });
  window.addEventListener('resize', function () { if (owner && card && !card.hidden) place(owner); });

  /* The table of examples: arrow keys move between its marks and headings; Home and End go to the ends of a row. */
  var grid = doc.querySelector('.grid');
  if (grid) {
    grid.addEventListener('keydown', function (event) {
      if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
      var step = { ArrowLeft: [0, -1], ArrowRight: [0, 1], ArrowUp: [-1, 0], ArrowDown: [1, 0] }[event.key];
      if (!step && event.key !== 'Home' && event.key !== 'End') return;
      var cell = event.target.closest('th, td');
      if (!cell || !grid.contains(cell)) return;
      var rowsAll = Array.prototype.slice.call(grid.rows);
      var r = rowsAll.indexOf(cell.parentNode);
      var c = cell.cellIndex;
      function control(ri, ci) {
        var tr = rowsAll[ri];
        var td = tr && tr.cells[ci];
        return td ? td.querySelector('button, a[href]') : null;
      }
      var target = null;
      if (step) {
        for (var ri = r + step[0], ci = c + step[1]; ri >= 0 && ri < rowsAll.length && ci >= 0 && ci < rowsAll[ri].cells.length;
             ri += step[0], ci += step[1]) {
          target = control(ri, ci);
          if (target) break;
        }
      } else {
        var cells = rowsAll[r].cells;
        var order = event.key === 'Home' ? Array.prototype.slice.call(cells) : Array.prototype.slice.call(cells).reverse();
        for (var k = 0; k < order.length && !target; k++) target = control(r, order[k].cellIndex);
      }
      if (!target) return;
      event.preventDefault();
      if (pinned) hide();
      target.focus();
    });
  }

  /* A mark focused while the table is scrolled sideways is brought clear of the sticky row header. */
  var gridWrap = doc.querySelector('.grid-wrap');
  function clearRowHeader(el) {
    var cell = el.closest && el.closest('td');
    var head = cell && cell.parentNode.querySelector('th');
    if (!head) return;
    var c = el.getBoundingClientRect();
    var h = head.getBoundingClientRect();
    if (c.left < h.right - 1) {
      gridWrap.scrollLeft -= (h.right - c.left) + 4;
      if (owner === el && card && !card.hidden) place(el);
    }
  }
  if (gridWrap) {
    /* Only focus reached by keyboard is moved: a press on a partly covered mark must not scroll it away mid-click. */
    var pressed = false;
    gridWrap.addEventListener('pointerdown', function () { pressed = true; }, true);
    gridWrap.addEventListener('mousedown', function () { pressed = true; }, true);
    doc.addEventListener('keydown', function () { pressed = false; }, true);
    gridWrap.addEventListener('focusin', function (event) {
      var el = event.target;
      if (pressed) { pressed = false; return; }
      clearRowHeader(el);
      requestAnimationFrame(function () { if (doc.activeElement === el) clearRowHeader(el); });
    });
  }

  /* Rows open when they are the target of a link, and a link into a row opens it. */
  function hashTarget() {
    var raw = location.hash.slice(1);
    if (!raw) return null;
    var id;
    try { id = decodeURIComponent(raw); } catch (e) { id = raw; }
    return doc.getElementById(id);
  }
  function openTarget() {
    var target = hashTarget();
    if (!target) return;
    if (openAround(target)) {
      requestAnimationFrame(function () { target.scrollIntoView(); });
    }
  }
  window.addEventListener('hashchange', openTarget);
  doc.addEventListener('click', function (event) {
    if (event.defaultPrevented || event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    var a = event.target.closest && event.target.closest('a[href^="#"]');
    var href = a && a.getAttribute('href');
    if (!href || href.length < 2 || href !== location.hash) return;
    setTimeout(openTarget, 0);
  });

  var rows = all('details.row');
  /* A row opened by the reader becomes the page address (without a new history entry), so it can be shared. */
  rows.forEach(function (d) {
    var summary = d.querySelector('summary');
    if (!summary || !d.id) return;
    summary.addEventListener('click', function () {
      if (!d.open) setHash(d.id, false);
      else if (location.hash === '#' + d.id) setHash('', false);
    });
  });

  /* Open all and Close all act within their own section: the examples' rows, or a section's 'proved toward it' lists. */
  function expandables(scope) { return all('details.row, details.known', scope); }
  function bindExpand(b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('data-expand') === 'all';
      var scope = b.closest('section') || doc;
      expandables(scope).forEach(function (d) { d.open = open; });
    });
  }
  var expandButtons = all('[data-expand]');
  expandButtons.forEach(bindExpand);
  var openWord = (expandButtons.filter(function (b) { return b.getAttribute('data-expand') === 'all'; })[0] || {}).textContent;
  var closeWord = (expandButtons.filter(function (b) { return b.getAttribute('data-expand') === 'none'; })[0] || {}).textContent;
  if (openWord && closeWord) {
    all('main section.section').forEach(function (section) {
      var list = section.querySelector('.questions');
      if (!list || section.querySelectorAll('details.known').length < 2 || section.querySelector('[data-expand]')) return;
      var tools = doc.createElement('div');
      tools.className = 'row-actions known-actions';
      [['all', openWord], ['none', closeWord]].forEach(function (pair) {
        var b = doc.createElement('button');
        b.type = 'button';
        b.className = 'link-btn';
        b.setAttribute('data-expand', pair[0]);
        b.textContent = pair[1];
        bindExpand(b);
        tools.appendChild(b);
      });
      list.parentNode.insertBefore(tools, list);
    });
  }

  function liveRegion(parent) {
    var p = doc.createElement('p');
    p.className = 'visually-hidden';
    p.setAttribute('role', 'status');
    p.setAttribute('aria-live', 'polite');
    parent.appendChild(p);
    return p;
  }

  /* Status filter for the statements of the rows. */
  var filters = all('.filter[data-filter]').filter(function (f) { return !f.closest('.find'); });
  var rowStatements = all('.rows .statement');
  var filterNews = filters.length ? liveRegion(filters[0].closest('.row-tools') || filters[0].parentNode) : null;
  if (filterNews) filterNews.className = 'filter-count'; /* shown, not only announced */
  var EMPTY_ONE = 'No statement in this example has the selected status.';
  var EMPTY_MANY = 'No statement in this example has any of the selected statuses.';
  function applyFilter(record) {
    var on = filters.filter(function (f) { return f.getAttribute('aria-pressed') === 'true'; })
                    .map(function (f) { return f.getAttribute('data-filter'); });
    var shown = 0;
    rowStatements.forEach(function (s) {
      s.hidden = on.length > 0 && on.indexOf(s.getAttribute('data-status')) < 0;
      if (!s.hidden) shown++;
    });
    rows.forEach(function (d) {
      var any = !!d.querySelector('.statement:not([hidden])');
      if (on.length) d.open = any;
      var empty = on.length > 0 && !any;
      if (empty) d.setAttribute('data-filter-empty', ''); else d.removeAttribute('data-filter-empty');
      var note = d.querySelector('.filter-empty-note');
      var list = d.querySelector('.row-body .statements');
      if (empty && !note && list) {
        note = doc.createElement('p');
        note.className = 'filter-empty-note';
        list.parentNode.insertBefore(note, list);
      }
      if (note) { note.hidden = !empty; note.textContent = empty ? (on.length === 1 ? EMPTY_ONE : EMPTY_MANY) : ''; }
      var mixHere = d.querySelector('summary .row-count .mix');
      if (mixHere) mixHere.hidden = on.length > 0;
      var count = d.querySelector('summary .row-count');
      var words = count && count.firstChild && count.firstChild.nodeType === 3 ? count.firstChild : null;
      if (words) {
        if (!count.hasAttribute('data-count')) count.setAttribute('data-count', words.nodeValue);
        var shownHere = d.querySelectorAll('.statement:not([hidden])').length;
        words.nodeValue = on.length ? shownHere + ' of ' + count.getAttribute('data-count') : count.getAttribute('data-count');
      }
    });
    if (filterNews) {
      var inRows = rows.filter(function (d) { return d.querySelector('.statement:not([hidden])'); }).length;
      filterNews.textContent = on.length
        ? 'Showing ' + shown + ' of ' + rowStatements.length + ' statements, in ' + inRows + ' of ' + rows.length + ' examples.'
        : 'Showing all ' + rowStatements.length + ' statements of the examples.';
    }
    if (filterNews) filterNews.classList.toggle('visually-hidden', !on.length);
    if (record !== false) writeParams({ show: on.join(',') });
  }
  function setFilters(list) {
    filters.forEach(function (f) { f.setAttribute('aria-pressed', list.indexOf(f.getAttribute('data-filter')) >= 0 ? 'true' : 'false'); });
    applyFilter();
  }
  rowFilterLift = filters.length ? function () { setFilters([]); } : null;
  filters.forEach(function (f) {
    f.addEventListener('click', function () {
      f.setAttribute('aria-pressed', f.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      applyFilter();
    });
  });
  var tallyLinks = all('.tally a[data-filter]');

  /* Mark the section in view in the bar; on a narrow screen the bar scrolls to keep that link in sight. */
  var nav = doc.querySelector('.nav');
  var navLinks = all('.nav a');
  var byId = {};
  navLinks.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
  function keepInSight(a) {
    if (!nav || nav.scrollWidth <= nav.clientWidth + 1) return;
    var n = nav.getBoundingClientRect();
    var l = a.getBoundingClientRect();
    if (l.left >= n.left + 28 && l.right <= n.right - 28) return; /* clear of either fade */
    var left = nav.scrollLeft + (l.left - n.left) - (n.width - l.width) / 2;
    try { nav.scrollTo({ left: Math.max(0, left), behavior: smooth() }); } catch (e) { nav.scrollLeft = Math.max(0, left); }
  }
  function setCurrent(id) {
    var a = byId[id];
    if (!a || a.getAttribute('aria-current') === 'true') return;
    navLinks.forEach(function (x) { x.removeAttribute('aria-current'); });
    a.setAttribute('aria-current', 'true');
    keepInSight(a);
  }
  navLinks.forEach(function (a) { a.addEventListener('click', function () { setCurrent(a.getAttribute('href').slice(1)); }); });
  /* Each edge of the bar fades while more of its links lie beyond it; a list that fits, or an edge it has reached, is
     not faded. */
  function markNavOverflow() {
    if (!nav) return;
    nav.classList.toggle('nav-overflow', nav.scrollLeft + nav.clientWidth < nav.scrollWidth - 1);
    nav.classList.toggle('nav-overflow-start', nav.scrollLeft > 1);
  }
  markNavOverflow();
  window.addEventListener('resize', markNavOverflow);
  if (nav) nav.addEventListener('scroll', markNavOverflow, { passive: true });
  try { if (doc.fonts && doc.fonts.ready) doc.fonts.ready.then(markNavOverflow); } catch (e) { /* no font loading API */ }
  if ('IntersectionObserver' in window && navLinks.length) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting && byId[e.target.id]) setCurrent(e.target.id); });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(byId).forEach(function (id) { var s = doc.getElementById(id); if (s) observer.observe(s); });
  }

  /* Printing shows every disclosure (rows, related lists, column definitions); afterwards each is as the reader left it. */
  var printed = null;
  var beforePrint = null;
  window.addEventListener('beforeprint', function () {
    printed = all('main details');
    beforePrint = printed.map(function (d) { return d.open; });
    printed.forEach(function (d) { d.open = true; });
    /* Paper shows every statement, so each row's count is its full count while printing. */
    all('summary .row-count[data-count]').forEach(function (c) {
      c.setAttribute('data-shown', c.firstChild.nodeValue);
      c.firstChild.nodeValue = c.getAttribute('data-count');
    });
  });
  window.addEventListener('afterprint', function () {
    if (beforePrint) printed.forEach(function (d, i) { d.open = beforePrint[i]; });
    printed = null;
    beforePrint = null;
    all('summary .row-count[data-shown]').forEach(function (c) {
      c.firstChild.nodeValue = c.getAttribute('data-shown');
      c.removeAttribute('data-shown');
    });
  });

  /* Search of the whole page: statements, questions, examples, counterexamples, open problems, essay and terms.
     Matching ignores case and accents; every word must occur; "quoted words" match as a phrase; TeX is searched too. */
  var main = doc.getElementById('main') || doc.querySelector('main');
  var mount = doc.querySelector('[data-find]');
  function word(name, fallback) {
    var v = mount && mount.getAttribute('data-label-' + name);
    return v || fallback;
  }
  var WORDS = {
    search: word('search', 'Search this page'),
    placeholder: word('placeholder', 'Search statements, questions, examples and terms'),
    hint: word('hint', doc.querySelector('[data-find-open]')
      ? 'The search button in the bar brings you back here from anywhere on the page; the down arrow moves through the results.'
      : 'The down arrow moves through the results.'),
    part: word('part', 'Part'),
    status: word('status', 'Status'),
    clear: word('clear', 'Clear'),
    none: word('none', 'Nothing on this page matches.'),
    one: word('one', '1 match'),
    many: word('many', '{n} matches'),
    more: word('more', 'Show all {n}')
  };
  var SCOPES = ['programme', 'status', 'results', 'decisive', 'frontier', 'examples', 'failures', 'open', 'essay', 'terms'].filter(function (id) {
    return doc.getElementById(id);
  });
  function scopeLabel(id) {
    if (byId[id]) return byId[id].textContent.trim();
    var h = doc.querySelector('#' + id + ' h2');
    return h ? h.textContent.trim() : id;
  }

  function fold(s) {
    return (s || '').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase()
      .replace(/[\u2018\u2019\u02bc]/g, '\'').replace(/[\u201c\u201d]/g, '"').replace(/[\u2010-\u2015\u2212]/g, '-');
  }
  /* The same folding one character at a time, remembering where each folded character came from. */
  function foldMap(s) {
    var out = '';
    var from = [];
    var to = [];
    for (var i = 0; i < s.length;) {
      var cp = s.codePointAt(i);
      var ch = String.fromCodePoint(cp);
      var f = fold(ch);
      for (var j = 0; j < f.length; j++) { out += f[j]; from.push(i); to.push(i + ch.length); }
      i += ch.length;
    }
    return { text: out, from: from, to: to };
  }
  function parseQuery(q) {
    var out = [];
    (q || '').replace(/"([^"]+)"|(\S+)/g, function (_, phrase, w) {
      var t = fold(phrase ? phrase.replace(/\s+/g, ' ').trim() : w.replace(/^[.,;:!?()[\]]+|[.,;:!?()[\]]+$/g, ''));
      if (t) out.push(t);
      return '';
    });
    return out;
  }

  /* Reader-visible text of an element, formulae given by their symbols, without marks or chips. */
  var BLOCK = /^(p|div|li|dt|dd|h[1-6]|article|ul|ol|dl|summary|section|header)$/;
  function textOf(el, skip) {
    var out = [];
    (function walk(n) {
      if (n.nodeType === 3) { out.push(n.nodeValue); return; }
      if (n.nodeType !== 1) return;
      if (skip && n.matches(skip)) return;
      var tag = n.localName;
      if (tag === 'svg' || tag === 'annotation' || tag === 'script' || tag === 'style') return;
      for (var c = n.firstChild; c; c = c.nextSibling) walk(c);
      if (tag === 'li') out.push('; '); /* list items (hypotheses) stay apart in snippets */
      else if (BLOCK.test(tag)) out.push(' ');
    })(el);
    return out.join('').replace(/\s+/g, ' ').trim();
  }
  function texOf(el, skip) {
    return all('annotation', el).filter(function (a) { return !(skip && a.closest(skip)); })
      .map(function (a) { return a.textContent; }).join(' ');
  }
  /* A copy of a heading for the results: formulae kept, links, buttons and ids removed. */
  function inlineCopy(el) {
    var span = doc.createElement('span');
    if (!el) return span;
    var copy = el.cloneNode(true);
    all('svg, .anchor-sr', copy).forEach(function (n) { n.parentNode.removeChild(n); });
    all('a, button', copy).forEach(function (n) {
      while (n.firstChild) n.parentNode.insertBefore(n.firstChild, n);
      n.parentNode.removeChild(n);
    });
    all('[id]', copy).forEach(function (n) { n.removeAttribute('id'); });
    while (copy.firstChild) span.appendChild(copy.firstChild);
    return span;
  }

  var units = null;
  function sectionOf(el) {
    var s = el.closest('section.section');
    if (!s && el.closest('main > .lead')) return SCOPES.indexOf('programme') >= 0 ? 'programme' : null;
    return s && SCOPES.indexOf(s.id) >= 0 ? s.id : null;
  }
  function index() {
    if (units) return units;
    units = [];
    function add(el, titleEl, title, context, bodySkip, statusEl) {
      var scope = sectionOf(el);
      if (!scope) return;
      var body = textOf(el, bodySkip);
      var status = statusEl ? statusEl.getAttribute('data-status') : null;
      var chip = statusEl ? statusEl.querySelector('.status-chip') : null;
      units.push({
        el: el, scope: scope, titleEl: titleEl, title: title, context: context, body: body, status: status,
        statusLabel: chip ? textOf(chip) : '', mark: chip ? chip.querySelector('.mark') : null,
        hay: fold(title + ' \u0001 ' + context + ' \u0001 ' + body + ' \u0001 ' + texOf(el, bodySkip) + ' ' + (titleEl ? texOf(titleEl) : '')),
        ftitle: fold(title)
      });
    }
    var HEAD = '.statement-head, .statement-notes .note-label, .statement-hypotheses .note-label, .added-chip';
    /* A question's own statement: a direct child, or inside .question-ask on a comparison card. */
    var ASKED = ':scope > .statement, :scope > .question-ask > .statement';
    all('main .statement').forEach(function (s) {
      var question = s.closest('.question');
      if (question && question.querySelector(ASKED) === s) return; /* indexed with its question */
      if (s.closest('.failure')) return; /* indexed with its claim */
      var titleEl = s.querySelector('.statement-title');
      var context = '';
      var row = s.closest('details.row');
      var group = s.closest('.open-group');
      if (question) context = questionTitle(question);
      else if (row) context = textOf(row.querySelector('.row-name'));
      else if (group) context = textOf(group.querySelector('h3'));
      add(s, titleEl, titleEl ? textOf(titleEl) : '', context, HEAD, s);
    });
    all('main .question').forEach(function (q) {
      var asked = q.querySelector(ASKED);
      /* The question's own statement title is searched with it; related statements are indexed on their own. */
      add(q, q.querySelector('h3 .anchor') || q.querySelector('h3'), questionTitle(q), '',
          'h3, .question-num, .known, .question-known, .status-chip, .statement-notes .note-label, .statement-hypotheses .note-label, .added-chip', asked);
    });
    all('main details.row').forEach(function (d) {
      var name = d.querySelector('.row-name');
      add(d, name, textOf(name), '', '.row-num, .row-name, .row-marks, .row-count, .statements', null);
    });
    all('main .failure').forEach(function (f) {
      var claim = f.querySelector('.claim-text');
      var witness = f.querySelector('.statement');
      /* The counterexample's own title stays in the searched text. */
      add(f, claim, textOf(claim), '', '.claim, .status-chip, .added-chip, .statement-notes .note-label, .statement-hypotheses .note-label', witness);
    });
    all('main .open-group').forEach(function (g) {
      var h = g.querySelector('h3');
      add(g, h && (h.querySelector('.anchor') || h), textOf(h), '', 'h3, .statements', null);
    });
    all('main .col-def').forEach(function (c) {
      var dt = c.querySelector('dt');
      add(c, dt, textOf(dt), '', 'dt', null);
    });
    var essayTitle = doc.getElementById('essay-title');
    all('main .essay-lead, main .essay > p:not(.essay-byline)').forEach(function (p) {
      add(p, essayTitle, essayTitle ? textOf(essayTitle) : '', '', null, null);
    });
    all('main .gloss').forEach(function (g) {
      var dt = g.querySelector('dt');
      add(g, dt, textOf(dt), '', 'dt', null);
    });
    /* The cover's lead, the status key, and each section's heading with its introduction where it has one. */
    all('main > .lead p').forEach(function (p) { add(p, null, '', '', null, null); });
    all('#status .key-item').forEach(function (k) { var dt = k.querySelector('dt'); add(k, dt, textOf(dt), '', 'dt', null); });
    all('main section.section').forEach(function (sec) {
      var head = sec.querySelector(':scope > .section-head');
      var h = head && head.querySelector('h2');
      var intro = sec.querySelector(':scope > .section-intro');
      if (intro) add(intro, h, h ? textOf(h) : '', '', null, null);
      else if (head) add(head, h, h ? textOf(h) : '', '', null, null);
    });
    return units;
  }
  function questionTitle(q) {
    var h = q.querySelector('h3');
    var n = q.querySelector('.question-num');
    return (n ? textOf(n, '.question-num-label') + '. ' : '') + (h ? textOf(h) : '');
  }

  /* Wrap the folded occurrences of the search words in an element's text (outside formulae) in <mark>. */
  function highlight(node, words) {
    if (!words.length) return node;
    var texts = [];
    (function walk(n) {
      if (n.nodeType === 3) { texts.push(n); return; }
      if (n.nodeType !== 1 || n.localName === 'math' || n.localName === 'svg') return;
      for (var c = n.firstChild; c; c = c.nextSibling) walk(c);
    })(node);
    texts.forEach(function (t) {
      var s = t.nodeValue;
      var ranges = rangesIn(s, words);
      if (!ranges.length) return;
      var frag = doc.createDocumentFragment();
      var pos = 0;
      ranges.forEach(function (r) {
        if (r[0] > pos) frag.appendChild(doc.createTextNode(s.slice(pos, r[0])));
        var m = doc.createElement('mark');
        m.textContent = s.slice(r[0], r[1]);
        frag.appendChild(m);
        pos = r[1];
      });
      if (pos < s.length) frag.appendChild(doc.createTextNode(s.slice(pos)));
      t.parentNode.replaceChild(frag, t);
    });
    return node;
  }
  function rangesIn(s, words) {
    var m = foldMap(s);
    var ranges = [];
    words.forEach(function (w) {
      for (var at = m.text.indexOf(w); at >= 0; at = m.text.indexOf(w, at + Math.max(1, w.length))) {
        ranges.push([m.from[at], m.to[at + w.length - 1]]);
      }
    });
    ranges.sort(function (a, b) { return a[0] - b[0]; });
    var merged = [];
    ranges.forEach(function (r) {
      var last = merged[merged.length - 1];
      if (last && r[0] <= last[1]) last[1] = Math.max(last[1], r[1]); else merged.push(r.slice());
    });
    return merged;
  }
  function snippet(body, words) {
    var first = -1;
    if (words.length) {
      var m = foldMap(body);
      words.forEach(function (w) {
        var at = m.text.indexOf(w);
        if (at >= 0 && (first < 0 || m.from[at] < first)) first = m.from[at];
      });
    }
    var start = first > 70 ? body.lastIndexOf(' ', first - 60) + 1 : 0;
    var end = Math.min(body.length, start + 220);
    if (end < body.length) { var sp = body.lastIndexOf(' ', end); if (sp > start + 120) end = sp; }
    var span = doc.createElement('span');
    span.className = 'find-snippet';
    span.textContent = (start > 0 ? '\u2026' : '') + body.slice(start, end) + (end < body.length ? '\u2026' : '');
    return highlight(span, words);
  }

  var find = null;
  var input = null;
  var facets = null;
  var countLine = null;
  var results = null;
  var clearButton = null;
  var limit = 40;
  var hits = [];
  var state = { q: '', scopes: [], statuses: [] };
  var addressTimer = null;
  var pendingAddress = null;
  function flushAddress() {
    if (!pendingAddress) return;
    clearTimeout(addressTimer);
    var snapshot = pendingAddress;
    pendingAddress = null;
    writeParams(snapshot);
  }

  function chip(attr, value, content) {
    var b = doc.createElement('button');
    b.type = 'button';
    b.className = 'filter';
    b.setAttribute(attr, value);
    b.setAttribute('aria-pressed', 'false');
    if (typeof content === 'string') { var s = doc.createElement('span'); s.textContent = content; b.appendChild(s); }
    else content.forEach(function (n) { b.appendChild(n); });
    return b;
  }
  function group(label, buttons) {
    var g = doc.createElement('div');
    g.className = 'filters';
    g.setAttribute('role', 'group');
    g.setAttribute('aria-label', label);
    var l = doc.createElement('span');
    l.className = 'filters-label';
    l.textContent = label;
    g.appendChild(l);
    buttons.forEach(function (b) { g.appendChild(b); });
    return g;
  }

  function build() {
    if (!main) return;
    find = mount || doc.createElement('div');
    var served = !!mount;
    find.classList.add('find');
    find.setAttribute('role', 'search');
    if (!served) {
      var after = doc.querySelector('main > .tally') || doc.querySelector('main > .lead') || doc.querySelector('main > .cover');
      if (after) after.parentNode.insertBefore(find, after.nextSibling); else main.insertBefore(find, main.firstChild);
    }
    var label = doc.createElement('label');
    label.className = 'visually-hidden';
    label.htmlFor = 'find-q';
    label.textContent = WORDS.search;
    var field = doc.createElement('div');
    field.className = 'find-field';
    input = doc.createElement('input');
    input.type = 'search';
    input.id = 'find-q';
    input.className = 'find-input';
    input.setAttribute('autocomplete', 'off');
    input.setAttribute('spellcheck', 'false');
    input.setAttribute('enterkeyhint', 'search');
    input.setAttribute('aria-controls', 'find-results');
    input.setAttribute('aria-describedby', 'find-hint');
    input.placeholder = WORDS.placeholder;
    clearButton = doc.createElement('button');
    clearButton.type = 'button';
    clearButton.className = 'link-btn find-clear';
    clearButton.textContent = WORDS.clear;
    clearButton.hidden = true;
    field.appendChild(input);
    field.appendChild(clearButton);
    var hint = doc.createElement('p');
    hint.id = 'find-hint';
    hint.className = 'find-hint';
    hint.textContent = WORDS.hint;

    facets = doc.createElement('div');
    facets.className = 'find-facets';
    facets.hidden = true;
    facets.appendChild(group(WORDS.part, SCOPES.map(function (id) { return chip('data-scope', id, scopeLabel(id)); })));
    var facetSources = filters.slice();
    tallyLinks.forEach(function (a) {
      var st = a.getAttribute('data-filter');
      if (!facetSources.some(function (f) { return f.getAttribute('data-filter') === st; })) facetSources.push(a);
    });
    var statusChips = facetSources.map(function (f) {
      return chip('data-status-facet', f.getAttribute('data-filter'),
                  Array.prototype.slice.call(f.childNodes).filter(function (n) { return !(n.nodeType === 1 && n.matches('.count')); })
                    .map(function (n) { return n.cloneNode(true); }));
    });
    if (statusChips.length) facets.appendChild(group(WORDS.status, statusChips));

    countLine = doc.createElement('p');
    countLine.className = 'find-count';
    countLine.setAttribute('role', 'status');
    countLine.setAttribute('aria-live', 'polite');
    results = doc.createElement('div');
    results.id = 'find-results';
    results.className = 'find-results';
    results.hidden = true;

    [label, field, hint, facets, countLine, results].forEach(function (n) { find.appendChild(n); });
    if (!served) fallbackStyle();

    var timer = null;
    input.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () { state.q = input.value; limit = 40; run(true); }, 90);
    });
    input.addEventListener('focus', function () { facets.hidden = false; index(); });
    input.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowDown') {
        if (input.value !== state.q) { clearTimeout(timer); state.q = input.value; limit = 40; run(true); }
        var first = results.querySelector('.find-link');
        if (first) { event.preventDefault(); first.focus(); }
      } else if (event.key === 'Enter') {
        clearTimeout(timer);
        state.q = input.value;
        run(true);
        if (hits.length) { event.preventDefault(); go(hits[0]); }
      } else if (event.key === 'Escape') {
        event.preventDefault();
        if (active()) clearAll(); else input.blur();
      }
    });
    clearButton.addEventListener('click', function () { clearAll(); input.focus(); });
    facets.addEventListener('click', function (event) {
      var b = event.target.closest('.filter');
      if (!b) return;
      b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      state.scopes = pressed('data-scope');
      state.statuses = pressed('data-status-facet');
      limit = 40;
      run(true);
    });
    results.addEventListener('click', function (event) {
      var more = event.target.closest('.find-more');
      if (more) { limit = Infinity; run(false); var links = all('.find-link', results); if (links[40]) links[40].focus(); return; }
      var a = event.target.closest('.find-link');
      if (!a || event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      go(hits[+a.getAttribute('data-hit')]);
    });
    results.addEventListener('keydown', function (event) {
      var links = all('.find-link', results);
      var i = links.indexOf(event.target);
      if (i < 0) return;
      var to = null;
      if (event.key === 'ArrowDown') to = links[i + 1];
      else if (event.key === 'ArrowUp') to = i === 0 ? input : links[i - 1];
      else if (event.key === 'Home') to = links[0];
      else if (event.key === 'End') to = links[links.length - 1];
      else if (event.key === 'Escape') to = input;
      if (to) { event.preventDefault(); to.focus(); }
    });
  }
  function pressed(attr) {
    return all('.filter[' + attr + ']', facets).filter(function (b) { return b.getAttribute('aria-pressed') === 'true'; })
      .map(function (b) { return b.getAttribute(attr); });
  }
  function active() { return !!(state.q.trim() || state.scopes.length || state.statuses.length); }
  function clearAll() {
    input.value = '';
    state = { q: '', scopes: [], statuses: [] };
    all('.filter', facets).forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
    run(true);
  }
  function setState(next, record) {
    state = next;
    input.value = next.q;
    all('.filter[data-scope]', facets).forEach(function (b) {
      b.setAttribute('aria-pressed', next.scopes.indexOf(b.getAttribute('data-scope')) >= 0 ? 'true' : 'false');
    });
    all('.filter[data-status-facet]', facets).forEach(function (b) {
      b.setAttribute('aria-pressed', next.statuses.indexOf(b.getAttribute('data-status-facet')) >= 0 ? 'true' : 'false');
    });
    if (active()) facets.hidden = false;
    run(!!record);
  }

  function run(record) {
    var words = parseQuery(state.q);
    var on = active() && (words.length === 0 || words.join('').length >= 2 || state.scopes.length || state.statuses.length);
    clearButton.hidden = !active();
    if (record) {
      clearTimeout(addressTimer);
      pendingAddress = { q: state.q.trim(), 'in': state.scopes.join(','), status: state.statuses.join(',') };
      addressTimer = setTimeout(flushAddress, 350);
    }
    results.textContent = '';
    hits = [];
    if (!on) { results.hidden = true; countLine.textContent = ''; return; }
    index().forEach(function (u, i) {
      if (state.scopes.length && state.scopes.indexOf(u.scope) < 0) return;
      if (state.statuses.length && state.statuses.indexOf(u.status) < 0) return;
      for (var k = 0; k < words.length; k++) if (u.hay.indexOf(words[k]) < 0) return;
      var score = 0;
      words.forEach(function (w) { if (u.ftitle.indexOf(w) >= 0) score += 2; });
      hits.push({ unit: u, score: score, order: i });
    });
    hits.sort(function (a, b) {
      return SCOPES.indexOf(a.unit.scope) - SCOPES.indexOf(b.unit.scope) || b.score - a.score || a.order - b.order;
    });
    countLine.textContent = hits.length === 0 ? WORDS.none : hits.length === 1 ? WORDS.one : WORDS.many.replace('{n}', hits.length);
    results.hidden = hits.length === 0;
    var shown = hits.slice(0, limit);
    var current = null;
    var list = null;
    shown.forEach(function (h, n) {
      var u = h.unit;
      if (u.scope !== current) {
        current = u.scope;
        var g = doc.createElement('div');
        g.className = 'find-group';
        var head = doc.createElement('p');
        head.className = 'find-group-head';
        head.textContent = scopeLabel(u.scope) + ' \u00b7 ' + hits.filter(function (x) { return x.unit.scope === u.scope; }).length;
        list = doc.createElement('ol');
        list.className = 'find-list';
        list.setAttribute('aria-label', scopeLabel(u.scope));
        g.appendChild(head);
        g.appendChild(list);
        results.appendChild(g);
      }
      var li = doc.createElement('li');
      li.className = 'find-hit';
      var a = doc.createElement('a');
      a.className = 'find-link';
      var anchor = u.el.id ? u.el : u.el.parentNode.closest('[id]');
      a.href = '#' + (anchor ? anchor.id : '');
      a.setAttribute('data-hit', String(n));
      var where = [u.statusLabel, u.context].filter(Boolean).join(' \u00b7 ');
      if (where) {
        var w = doc.createElement('span');
        w.className = 'find-where';
        if (u.mark) w.appendChild(u.mark.cloneNode(true));
        var wt = doc.createElement('span');
        wt.textContent = where.length > 140 ? where.slice(0, 138) + '\u2026' : where;
        w.appendChild(highlight(wt, words));
        a.appendChild(w);
      }
      var t = inlineCopy(u.titleEl);
      t.className = 'find-title';
      if (!u.titleEl) t.textContent = u.title || scopeLabel(u.scope);
      a.appendChild(highlight(t, words));
      if (u.body) a.appendChild(snippet(u.body, words));
      li.appendChild(a);
      list.appendChild(li);
    });
    if (hits.length > shown.length) {
      var more = doc.createElement('button');
      more.type = 'button';
      more.className = 'link-btn find-more';
      more.textContent = WORDS.more.replace('{n}', hits.length);
      results.appendChild(more);
    }
  }
  function go(h) {
    if (!h) return;
    flushAddress(); /* the entry being left keeps the search that led away from it */
    var el = h.unit.el;
    openAround(el);
    if (el.id) {
      if (location.hash === '#' + el.id) setHash(el.id, false); else location.hash = el.id;
    } else {
      var anchor = el.parentNode.closest('[id]');
      if (anchor) setHash(anchor.id, true);
    }
    reveal(el, true);
  }

  function known(list, allowed) {
    return list.map(function (s) { return s.toLowerCase(); }).filter(function (s, i, a) { return allowed.indexOf(s) >= 0 && a.indexOf(s) === i; });
  }
  function fromAddress(params) {
    var statuses = all('.filter[data-status-facet]', facets || doc).map(function (b) { return b.getAttribute('data-status-facet'); });
    return { q: (params && params.get('q')) || '', scopes: known(listParam(params, 'in'), SCOPES), statuses: known(listParam(params, 'status'), statuses) };
  }
  function fallbackStyle() {
    /* Until the page's stylesheet styles the search (it then sets --find-styled on .find), a minimal style in its own tokens. */
    var styled = '';
    try { styled = getComputedStyle(find).getPropertyValue('--find-styled').trim(); } catch (e) { /* no styles */ }
    if (styled) return;
    var style = doc.createElement('style');
    style.setAttribute('data-find-style', '');
    style.textContent = [
      '.find{max-width:calc(var(--measure) + 2 * var(--gutter));margin:clamp(28px,4vw,44px) auto 0;padding:0 var(--gutter)}',
      '.find-field{display:flex;align-items:center;gap:12px}',
      '.find-input{flex:1;min-width:0;font:inherit;font-size:var(--text-sm);color:var(--ink);background:var(--paper-3);border:1px solid var(--rule);border-radius:var(--radius);padding:8px 12px;-webkit-appearance:none;appearance:none}',
      '.find-input::placeholder{color:var(--ink-4)}',
      '.find-input:focus-visible{outline:2px solid var(--focus);outline-offset:1px}',
      '.find-clear[hidden],.find-facets[hidden],.find-results[hidden]{display:none}',
      '.find-hint{margin:.45em 0 0;font-size:var(--text-xs);color:var(--ink-4)}',
      '.find-facets{display:grid;gap:8px;margin-top:12px}',
      '.find-count{margin:12px 0 0;font-size:var(--text-sm);color:var(--ink-3)}',
      '.find-count:empty{position:absolute;width:1px;height:1px;margin:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}',
      '.find-group{margin-top:16px}',
      '.find-group-head{margin:0 0 4px;font-size:var(--text-xs);letter-spacing:.12em;text-transform:uppercase;color:var(--ink-4)}',
      '.find-list{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule-soft)}',
      '.find-hit{border-bottom:1px solid var(--rule-soft)}',
      '.find-link{display:block;padding:9px 4px;color:inherit;text-decoration:none}',
      '.find-link:hover .find-title{color:var(--accent)}',
      '.find-where{display:flex;align-items:center;gap:6px;font-size:var(--text-xs);color:var(--ink-3)}',
      '.find-where .mark{flex:none;width:12px;height:12px}',
      '.find-title{display:block;font-weight:600}',
      '.find-snippet{display:block;margin-top:2px;font-size:var(--text-sm);color:var(--ink-2)}',
      '.find mark{background:var(--accent-soft);color:inherit;border-radius:2px;padding:0 1px}',
      '.find-more{margin-top:12px}',
      '.known-actions{justify-content:flex-end;margin:0 0 14px}',
      '@media print{.find,.known-actions{display:none}}'
    ].join('\n');
    doc.head.appendChild(style);
  }

  function focusSearch() {
    if (!input) return;
    facets.hidden = false;
    try { input.focus({ preventScroll: true }); } catch (e) { input.focus(); }
    find.scrollIntoView({ block: 'start', behavior: smooth() });
  }

  build();
  if (input) {
    /* The search is reached from anywhere through the opener in the bar; there is no single-character shortcut (WCAG 2.1.4). */
    all('[data-find-open]').forEach(function (b) {
      b.hidden = false;
      b.addEventListener('click', function (event) { event.preventDefault(); focusSearch(); });
    });
    markNavOverflow(); /* the opener takes room from the links */
  }

  /* The tally counts every statement on the page, so its links list every statement of that status on the page.
     Without the search (or with a modifier key) the link keeps its own target. */
  tallyLinks.forEach(function (a) {
    a.addEventListener('click', function (event) {
      if (event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      if (!input) { setFilters([a.getAttribute('data-filter')]); return; }
      event.preventDefault();
      setState({ q: '', scopes: [], statuses: [a.getAttribute('data-filter')] }, true);
      focusSearch();
    });
  });

  /* A formula that is wider than its box scrolls inside it; such a box takes keyboard focus so it can be scrolled
     with the arrow keys. Boxes inside links, buttons and summaries are left alone (they cannot hold a focus stop). */
  function markScrollers() {
    all('.math-display, .math-long', main || doc).forEach(function (box) {
      if (box.closest('a, button, summary, .find, #card')) return;
      var wide = box.scrollWidth > box.clientWidth + 1;
      if (wide && !box.hasAttribute('tabindex')) { box.setAttribute('tabindex', '0'); box.setAttribute('data-scroll-focus', ''); }
      else if (!wide && box.hasAttribute('data-scroll-focus')) { box.removeAttribute('tabindex'); box.removeAttribute('data-scroll-focus'); }
    });
  }
  var scrollerTimer = null;
  function markScrollersSoon() { clearTimeout(scrollerTimer); scrollerTimer = setTimeout(markScrollers, 150); }
  window.addEventListener('resize', markScrollersSoon);
  doc.addEventListener('toggle', markScrollersSoon, true);
  requestAnimationFrame(markScrollers);
  try { if (doc.fonts && doc.fonts.ready) doc.fonts.ready.then(markScrollers); } catch (e) { /* no font loading API */ }

  /* The state in the address on arrival, and again when the reader goes back or forward. */
  function same(a, b) { return a.slice().sort().join(',') === b.slice().sort().join(','); }
  function fromURL(arrival) {
    var params = readParams();
    lastSearch = location.search;
    var rawShow = listParam(params, 'show');
    var show = known(rawShow, filters.map(function (f) { return f.getAttribute('data-filter'); }));
    if (rawShow.join(',') !== show.join(',')) writeParams({ show: show.join(',') });
    var nowShown = filters.filter(function (f) { return f.getAttribute('aria-pressed') === 'true'; })
                          .map(function (f) { return f.getAttribute('data-filter'); });
    if (filters.length && !same(show, nowShown)) {
      filters.forEach(function (f) { f.setAttribute('aria-pressed', show.indexOf(f.getAttribute('data-filter')) >= 0 ? 'true' : 'false'); });
      applyFilter(false);
    }
    if (input) {
      var next = fromAddress(params);
      if (listParam(params, 'in').join(',') !== next.scopes.join(',') || listParam(params, 'status').join(',') !== next.statuses.join(',')) {
        writeParams({ 'in': next.scopes.join(','), status: next.statuses.join(',') });
      }
      if (next.q === state.q.trim() && same(next.scopes, state.scopes) && same(next.statuses, state.statuses)) return;
      setState(next);
      if (arrival && !location.hash && active()) requestAnimationFrame(function () { find.scrollIntoView({ block: 'start' }); });
    }
  }
  /* Fragment navigations fire popstate too: the search and filters follow the address only when its query part
     changed, and a query typed but not yet written is written first, into the entry being left. */
  doc.addEventListener('click', function (event) {
    if (event.target.closest && event.target.closest('a[href^="#"]')) flushAddress();
  }, true);
  window.addEventListener('popstate', function () {
    if (location.search === lastSearch) return;
    clearTimeout(addressTimer);
    pendingAddress = null;
    fromURL(false);
  });
  fromURL(true);
  openTarget();
})();
