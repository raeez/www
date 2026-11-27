(function () {
  'use strict';
  var root = document.documentElement;
  var doc = document;
  /* Beside the monograph reader ([data-reader]) this script keeps what only it serves: the term and scope cards, the
     example table's keys, the filters, the disclosures and their history, and print. The place shown, the address, the
     search, the notices and the reading place are the reader's. */
  var READER = !!doc.querySelector('[data-reader]');
  function all(selector, context) { return Array.prototype.slice.call((context || doc).querySelectorAll(selector)); }
  function media(query) { return !!(window.matchMedia && window.matchMedia(query).matches); }
  function smooth() { return media('(prefers-reduced-motion: reduce)') ? 'auto' : 'smooth'; }
  function plainClick(event) { return !(event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey); }

  /* A component mounted in [data-atlas-mount] keeps its own state. The page's listeners ignore events that start
     inside it, and the page's filters, Open all, search, anchors, table keys, print opening and formula focus leave it
     alone; only the glossary card of a .term[data-term] is shared. The component asks the page to show one of the
     page's anchors with a qh:navigate event, hears the reader's search and filters in qh:state events, may claim an
     address the page does not have by cancelling qh:unknown-anchor, and reports new page content with
     qh:content-changed. These events are handled near the end of this script. */
  var ISOLATED = '[data-atlas-mount]';
  var mounts = all(ISOLATED); /* found again when the page reports new content */
  var isolating = mounts.length > 0;
  function shared(el) {
    if (!isolating || !el) return true;
    for (var i = 0; i < mounts.length; i++) if (mounts[i].contains(el)) return false;
    return true;
  }
  function own(selector, context) { return all(selector, context).filter(shared); }
  function list(collection) { return Array.prototype.slice.call(collection).filter(shared); }
  function byClass(name, context) { return context ? list(context.getElementsByClassName(name)) : []; }
  function byTag(name, context) { return context ? list(context.getElementsByTagName(name)) : []; }
  function origin(event) { /* the element an event started on, inside an open shadow root too */
    var path = event.composedPath ? event.composedPath() : [];
    return path[0] && path[0].nodeType === 1 ? path[0] : event.target;
  }

  /* Storage on this device can be refused (private windows, blocked site data); nothing on the page depends on it. */
  function stored(key) { try { return window.localStorage.getItem(key); } catch (e) { return null; } }
  function keep(key, value) {
    try { if (value === null) window.localStorage.removeItem(key); else window.localStorage.setItem(key, value); } catch (e) { /* refused */ }
  }

  /* The page's script hooks, found in one pass: a served search mount, controls served hidden until the script runs,
     and controls that open the search. */
  var main = doc.getElementById('main') || doc.querySelector('main');
  var hooks = list(doc.getElementsByTagName('*')).filter(function (el) {
    return el.hasAttribute('data-find') || el.hasAttribute('data-needs-script') || el.hasAttribute('data-find-open');
  });
  function hooked(attr) { return hooks.filter(function (el) { return el.hasAttribute(attr); }); }

  /* Elements after which reading text takes a space (textOf, used from start-up on). */
  var BLOCK = /^(p|div|li|dt|dd|h[1-6]|article|ul|ol|dl|summary|section|header)$/;

  /* Interface words: these defaults, or data-label-* attributes on a [data-find] element served with the page. */
  var mount = hooked('data-find')[0] || null;
  function word(name, fallback) {
    var v = mount && mount.getAttribute('data-label-' + name);
    return v || fallback;
  }
  function fill(text, values) {
    return text.replace(/\{(\w+)\}/g, function (m, k) { return Object.prototype.hasOwnProperty.call(values, k) ? values[k] : m; });
  }
  var WORDS = {
    search: word('search', 'Search this page'),
    placeholder: word('placeholder', 'Search statements, questions, examples and terms'),
    placeholderShort: word('placeholder-short', 'Search this page'),
    hint: word('hint', 'Press / to search; the down arrow moves through the results.'),
    part: word('part', 'Part'),
    status: word('status', 'Status'),
    clear: word('clear', 'Clear'),
    none: word('none', 'Nothing on this page matches.'),
    one: word('one', '1 match'),
    many: word('many', '{n} matches'),
    more: word('more', 'Show {k} more'),
    short: word('short', 'Type at least two letters or digits, or one symbol.'),
    formula: word('formula', 'in a formula'),
    witness: word('witness', 'counterexample: {status}'),
    shown: word('shown', 'Showing {shown} of {total} statements, in {rows} of {all} examples.'),
    allShown: word('all-shown', 'Showing all {total} statements of the examples.'),
    showAll: word('show-all', 'Show all'),
    rowEmpty: word('row-empty', 'No statement of this example has the status chosen above.'),
    rowShowAll: word('row-show-all', 'Show all statements'),
    unknown: word('unknown', 'Nothing on this page has the address {address}.'),
    unknownAsk: word('unknown-ask', 'The address asks for {values}, which this page does not have; the page is shown without it.'),
    searchFor: word('search-for', 'Search for “{words}”'),
    lensOn: word('lens-on', 'Marked {n} of the {all} marks in the table.'),
    lensOff: word('lens-off', 'No status is marked in the table.'),
    lensHelp: word('lens-help', 'Select a status to mark its cells in the table.'),
    gridKeys: word('grid-keys', 'Arrow keys move between the marks and headings of the table; Home and End go to the ends of a row; Tab leaves the table.'),
    resume: word('resume', 'You were reading {title}.'),
    resumeGo: word('resume-go', 'Continue reading'),
    close: word('close', 'Close')
  };

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
      keep('qh-theme', next);
    });
  }
  /* Controls that only work with the script may be served hidden; they are shown here. */
  hooked('data-needs-script').forEach(function (el) { if (el.hidden) el.hidden = false; });

  /* The address carries the reader's search and filters (?q=, ?in=, ?status=, ?show=) so a view can be shared, and
     its hash names an element of the page; other parameters are kept as they are. history.state.qh records, for each
     entry, which disclosures were open and where focus was when the reader left it, so that Back restores both. */
  function readParams() {
    try { return new URLSearchParams(location.search); } catch (e) { return null; }
  }
  function listParam(params, name) {
    var v = params && params.get(name);
    return v ? v.split(',').map(function (s) { return s.trim(); }).filter(Boolean) : [];
  }
  function entryState(patch) {
    var s = history.state;
    if (s != null && typeof s !== 'object') return s; /* a state this script did not write is left alone */
    s = Object.assign({}, s);
    if (patch) s.qh = Object.assign({}, s.qh && typeof s.qh === 'object' ? s.qh : {}, patch);
    return s;
  }
  function qhOf(state) { return state && typeof state === 'object' && state.qh && typeof state.qh === 'object' ? state.qh : {}; }
  function replaceAddress(url, patch) {
    try { history.replaceState(entryState(patch), '', url); } catch (e) { /* the address cannot be changed here (some file views) */ }
  }
  function pushAddress(url) {
    try { history.pushState(null, '', url); } catch (e) { /* as above */ }
  }
  function writeParams(changes) {
    var params = readParams();
    if (!params) return;
    Object.keys(changes).forEach(function (k) {
      if (changes[k]) params.set(k, changes[k]); else params.delete(k);
    });
    var search = params.toString();
    replaceAddress(location.pathname + (search ? '?' + search : '') + location.hash);
  }
  function setHash(id, push) {
    var url = location.pathname + location.search + (id ? '#' + id : '');
    if (push) pushAddress(url); else replaceAddress(url);
  }
  function hashId() {
    var raw = location.hash.slice(1);
    if (!raw) return '';
    try { return decodeURIComponent(raw); } catch (e) { return raw; }
  }

  /* Where focus was, in a form that finds the same element again: its id, its place in the search results, or its
     place among the controls of the nearest element with an id (or of the page), counting only controls outside the
     parts whose controls come and go (the search, the notices, the card). */
  var FOCUSABLE = 'a[href], button, input, select, textarea, summary, [tabindex]';
  var CHANGING = '.find, .qh-notice, #card';
  function steady(host) { return all(FOCUSABLE, host).filter(function (el) { return !el.closest(CHANGING); }); }
  function locator(el) {
    if (!el || el.nodeType !== 1 || el === doc.body || el === root) return null;
    if (el.matches('.find-link[data-hit]')) return { hit: +el.getAttribute('data-hit'), limit: limit };
    if (el.id) return { id: el.id };
    if (el.closest(CHANGING)) return null;
    var host = (el.parentElement && el.parentElement.closest('[id]')) || doc.body;
    var n = steady(host).indexOf(el);
    return n < 0 ? null : { within: host === doc.body ? '' : host.id, n: n };
  }
  function located(at) {
    if (!at || typeof at !== 'object') return null;
    if (typeof at.hit === 'number') return results ? all('.find-link', results)[at.hit] || null : null;
    if (typeof at.id === 'string') return doc.getElementById(at.id);
    if (typeof at.within !== 'string' || typeof at.n !== 'number') return null;
    var host = at.within ? doc.getElementById(at.within) : doc.body;
    return host ? steady(host)[at.n] || null : null;
  }

  /* Every statement has an address. One without its own id is given 's-' and the words of its title, by the rule the
     page's builder uses for ids, so that a link made now keeps working if the builder later writes that id itself.
     Paragraphs of the lead and the essay are named by their first words, the explanations of the status key by their
     status, a section's introduction by its section, and a column's line in a row by the row and the column. */
  function ident(text) {
    var t = text.normalize('NFKD').replace(/[^\x00-\x7f]/g, '').replace(/[^A-Za-z0-9_\s-]/g, '').trim().toLowerCase();
    return t.replace(/[\s_-]+/g, '-').slice(0, 60) || 'x';
  }
  function sourceText(el) { /* the words as written, formulae by their TeX */
    var out = '';
    (function walk(n) {
      if (n.nodeType === 3) { out += n.nodeValue; return; }
      if (n.nodeType !== 1) return;
      if (n.localName === 'math') { var a = n.querySelector('annotation'); out += a ? a.textContent : ''; return; }
      for (var c = n.firstChild; c; c = c.nextSibling) walk(c);
    })(el);
    return out;
  }
  var given = {};
  function give(el, base) {
    if (el.id) return el.id;
    var id = base;
    for (var n = 2; doc.getElementById(id); n++) id = base + '-' + n;
    el.id = id;
    given[id] = true;
    return id;
  }
  function firstWords(el, n) { return sourceText(el).split(/\s+/).filter(Boolean).slice(0, n).join(' '); }
  var leads = byClass('lead', main).filter(function (l) { return l.parentNode === main; });
  var essays = byClass('essay', main);
  function paragraphs(holders, skip) {
    return [].concat.apply([], holders.map(function (h) { return Array.prototype.filter.call(h.children, function (c) {
      return c.localName === 'p' && !(skip && c.classList.contains(skip)); }); }));
  }
  byClass('statement', main).filter(function (st) { return !st.id; })
    .concat(paragraphs(leads), byClass('essay-lead', main), paragraphs(essays, 'essay-byline'), byClass('key-item', main),
            byClass('section-intro', main).filter(function (x) { return x.parentNode.matches && x.parentNode.matches('section.section'); }))
    .forEach(function (el) {
    var c = el.classList;
    if (c.contains('statement')) {
      var from = el.querySelector('.statement-title') || el.querySelector('.statement-text') || el;
      give(el, 's-' + ident(sourceText(from).slice(0, 400)));
    } else if (c.contains('key-item')) {
      var m = el.querySelector('.mark');
      var st = m && /(?:^|\s)mark-([\w-]+)/.exec(m.getAttribute('class') || '');
      if (st) give(el, 'status-' + st[1]);
    } else if (c.contains('section-intro')) {
      give(el, el.parentNode.id + '-intro');
    } else {
      var section = el.closest('section.section');
      give(el, (section ? section.id : 'programme') + '-' + ident(firstWords(el, 8)).slice(0, 48));
    }
  });
  var grid = byClass('grid', doc)[0] || null;
  var columnIds = grid ? all('thead .col-head[data-col]', grid).map(function (b) { return b.getAttribute('data-col'); }) : [];
  var disclosures = byTag('details', main);
  var rows = disclosures.filter(function (d) { return d.classList.contains('row'); });
  var sections = main ? Array.prototype.filter.call(main.children, function (el) { return el.matches('section.section'); }) : [];
  rows.forEach(function (d) {
    var lines = d.id ? all('.cell-lines > .cell-line', d) : [];
    if (lines.length && lines.length === columnIds.length) lines.forEach(function (li, i) { give(li, d.id + '-' + columnIds[i]); });
  });

  /* What a mark in the table and a term mean is read with them by assistive technology: each trigger is described
     by its scope or its definition, and a row name written in TeX is read as text. */
  byClass('term', main).concat(byClass('cell-btn', main), byClass('col-head', main)).forEach(function (t) {
    if (t.localName === 'a' && !t.hasAttribute('role')) t.setAttribute('role', 'button'); /* it opens a card, not a page */
    if (!t.hasAttribute('aria-haspopup')) { t.setAttribute('aria-haspopup', 'dialog'); t.setAttribute('aria-controls', 'card'); t.setAttribute('aria-expanded', 'false'); }
    var label = t.getAttribute('aria-label') || '';
    if (/\\[()[\]]/.test(label)) t.setAttribute('aria-label', label = label.replace(/\\[()[\]]/g, ''));
    var td = t.classList.contains('cell-btn') ? t.closest('td') : null;
    var note = td && td.querySelector('.cell-note');
    /* A mark's name that still holds TeX is said with the row's full name as the page shows it. */
    if (note && /\\[A-Za-z]/.test(label)) {
      var rowEl = t.getAttribute('data-row') ? doc.getElementById(t.getAttribute('data-row')) : null;
      var named = (rowEl && rowEl.querySelector('.row-name')) || td.parentNode.cells[0];
      var where = note.querySelector('.cell-note-where');
      var said = note.querySelector('.cell-note-head > span:not(.cell-note-where)');
      if (named && named !== td && where && said) t.setAttribute('aria-label', textOf(named) + ', ' + textOf(where) + ': ' + textOf(said));
    }
    if (t.hasAttribute('aria-describedby')) return;
    if (note) {
      /* described by its scope, without the status and column its name already says */
      var base = (t.getAttribute('data-row') || 'cell') + '-' + (columnIds[td.cellIndex - 1] || td.cellIndex) + '-scope';
      var scope = note.querySelector('.cell-note-text') ||
                  Array.prototype.filter.call(note.children, function (c) { return c.localName === 'p' && !c.classList.contains('cell-note-head'); })[0];
      t.setAttribute('aria-describedby', give(scope || note, base));
    } else if (t.classList.contains('term') && t.hasAttribute('data-term')) {
      var entry = doc.getElementById(t.getAttribute('data-term'));
      var dd = entry && entry.querySelector('dd');
      if (dd) t.setAttribute('aria-describedby', give(dd, entry.id + '-def'));
    }
  });

  /* Reaching an element: every closed details around it opens, and a statement the Show filter hides is shown. */
  var showDespiteFilter = null;
  var refilter = null;
  function openAround(el) {
    var opened = [];
    for (var d = el; d; d = d.parentElement) {
      if (d.localName === 'details' && !d.open) { d.open = true; opened.push(d); }
    }
    var hidden = el.closest && el.closest('.statement[hidden]');
    if (hidden && showDespiteFilter) showDespiteFilter(hidden);
    return opened;
  }
  function focusQuietly(el) {
    if (!el.matches('a[href], button, input, summary, [tabindex]')) {
      el.setAttribute('tabindex', '-1');
      el.addEventListener('blur', function off() { el.removeAttribute('tabindex'); el.removeEventListener('blur', off); });
    }
    try { el.focus({ preventScroll: true }); } catch (e) { el.focus(); }
  }
  /* The element a link or a search result led to carries data-revealed until the next one. */
  var revealed = null;
  function markRevealed(el) {
    if (revealed && revealed !== el) revealed.removeAttribute('data-revealed');
    revealed = el;
    el.setAttribute('data-revealed', '');
  }

  /* One floating card serves terms, grid cells and column heads. */
  var card = doc.getElementById('card');
  var cardInner = card ? card.querySelector('.card-inner') : null;
  var owner = null;
  var addressedCellNote = '';
  var pinned = false;
  var hideTimer = null;
  var hoverCapable = media('(hover: hover) and (pointer: fine)');

  function place(target) {
    var r = target.getBoundingClientRect();
    var narrow = window.innerWidth <= 640;
    card.classList.toggle('sheet', narrow && !hoverCapable);
    if (narrow && !hoverCapable) {
      card.style.left = '';
      card.style.top = '';
      /* On a narrow touch screen the card is a sheet at the bottom; the page moves so that its trigger stays above it. */
      requestAnimationFrame(function () {
        var sheet = card.getBoundingClientRect();
        var t = target.getBoundingClientRect();
        if (sheet.height && t.bottom > sheet.top - 8 && window.scrollBy) {
          window.scrollBy({ top: t.bottom - sheet.top + 16, behavior: smooth() });
        }
      });
      return;
    }
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

  /* The card's content is copied from the page (definitions, scopes), formulae included. */
  function copyInto(target, from) {
    for (var c = from.firstChild; c; c = c.nextSibling) target.appendChild(c.cloneNode(true));
    all('[id]', target).forEach(function (n) { n.removeAttribute('id'); });
    return target;
  }
  function element(tag, className, text) {
    var el = doc.createElement(tag);
    if (className) el.className = className;
    if (text) el.textContent = text;
    return el;
  }
  function cardLink(href, content) {
    var a = element('a', 'card-more');
    a.href = href;
    if (typeof content === 'string') a.textContent = content; else a.appendChild(content);
    return a;
  }
  function contentFor(el) {
    var frag = doc.createDocumentFragment();
    if (el.classList.contains('term')) {
      var entry = doc.getElementById(el.getAttribute('data-term'));
      if (!entry) return null;
      frag.appendChild(copyInto(element('p', 'card-term'), entry.querySelector('dt')));
      frag.appendChild(copyInto(element('div'), entry.querySelector('dd')));
      var termsHead = doc.querySelector('#terms h2');
      frag.appendChild(cardLink('#' + entry.id, termsHead ? termsHead.textContent : 'Terms'));
      return frag;
    }
    if (el.classList.contains('cell-btn')) {
      var note = el.parentNode.querySelector('.cell-note');
      if (!note) return null;
      copyInto(frag, note);
      var row = el.getAttribute('data-row');
      var rowLink = doc.querySelector('.grid tbody th a[href="#' + row + '"]');
      if (rowLink) frag.appendChild(cardLink('#' + row, inlineCopy(rowLink)));
      return frag;
    }
    if (el.classList.contains('col-head')) {
      var def = doc.getElementById('col-' + el.getAttribute('data-col'));
      if (!def) return null;
      frag.appendChild(copyInto(element('p', 'card-term'), def.querySelector('dt')));
      frag.appendChild(copyInto(element('div'), def.querySelector('dd')));
      return frag;
    }
    return null;
  }

  function show(el, pin) {
    if (!card) return;
    clearTimeout(hideTimer);
    var content = contentFor(el);
    if (content === null) return;
    addressedCellNote = '';
    if (owner && owner !== el) owner.setAttribute('aria-expanded', 'false');
    owner = el;
    pinned = !!pin;
    cardInner.textContent = '';
    cardInner.appendChild(content);
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
    addressedCellNote = '';
    if (owner) owner.setAttribute('aria-expanded', 'false');
    owner = null;
    pinned = false;
  }

  function hideSoon() {
    if (pinned) return;
    clearTimeout(hideTimer);
    hideTimer = setTimeout(hide, 160);
  }

  /* The next control in reading order after an element, skipping what a closed details or [hidden] conceals and the
     controls a keyboard reader reaches with the arrow keys instead (the table's). */
  var TABBABLE = 'a[href], button:not([disabled]), input:not([disabled]), summary, [tabindex]:not([tabindex="-1"])';
  function reachable(el) {
    if (el.closest('[hidden], #card')) return false;
    for (var child = el, p = el.parentElement; p; child = p, p = p.parentElement) {
      if (p.localName === 'details' && !p.open && !(child.localName === 'summary' && child.parentNode === p)) return false;
    }
    return true;
  }
  /* A reader address can name a paragraph in the source of a table card. Its visible destination is the same card. */
  if (READER && card) {
    doc.addEventListener('qh:reveal', function (event) {
      var target = event.target;
      var note = target.closest && target.closest('.grid td .cell-note[hidden]');
      var trigger = note && note.parentElement.querySelector('button.cell-btn[data-row]');
      if (!trigger || !reachable(trigger)) return;
      var options = event.detail || {};
      if (options.scroll !== false && trigger.scrollIntoView) trigger.scrollIntoView({ block: 'nearest', behavior: 'auto' });
      show(trigger, true);
      addressedCellNote = target.id;
      if (options.focus !== false) focusQuietly(trigger);
      event.preventDefault();
    });
    doc.addEventListener('qh:state', function () {
      if (addressedCellNote && hashId() !== addressedCellNote) hide();
    });
  }
  function nextAfter(el) {
    var list = all(TABBABLE);
    for (var i = 0; i < list.length; i++) {
      if (el.compareDocumentPosition(list[i]) & Node.DOCUMENT_POSITION_FOLLOWING && !el.contains(list[i]) &&
          list[i].tabIndex >= 0 && reachable(list[i])) return list[i];
    }
    return null;
  }

  var triggers = '.term, .cell-btn, .col-head';
  function triggerOf(node) {
    var el = node && node.closest ? node.closest(triggers) : null;
    if (!el) return null;
    return shared(el) || el.matches('.term[data-term]') ? el : null;
  }
  doc.addEventListener('click', function (event) {
    var el = triggerOf(event.target);
    if (el && el.localName === 'a' && !plainClick(event)) return; /* a term served as a link, opened as a link */
    if (el) {
      event.preventDefault();
      if (owner === el && pinned) { hide(); return; }
      show(el, true);
      return;
    }
    if (card && !card.hidden) {
      var link = event.target.closest('a[href]');
      // A search result can open this card before its handled click bubbles here.
      if (addressedCellNote && event.defaultPrevented && link && link.getAttribute('href') === '#' + addressedCellNote) return;
      /* A link in the card leads elsewhere on the page; the card closes behind it. */
      if (!event.target.closest('#card') || event.target.closest('#card a[href]')) hide();
    }
  });
  doc.addEventListener('keydown', function (event) {
    if (event.key !== ' ' || event.defaultPrevented || event.target.localName !== 'a') return;
    if (triggerOf(event.target) === event.target) { event.preventDefault(); event.target.click(); } /* Space, as on a button */
  });
  if (hoverCapable) {
    /* A card opens when the pointer moves onto its trigger, never when the page scrolls a trigger under a resting
       pointer (the browser then reports the pointer over it, and may report a move, at the same place on the screen). */
    var pointerAt = null;
    doc.addEventListener('mousemove', function (event) {
      var at = event.screenX + ',' + event.screenY;
      if (at === pointerAt) return;
      pointerAt = at;
      var el = triggerOf(event.target);
      if (!el || pinned) return;
      if (owner === el && card && !card.hidden) { clearTimeout(hideTimer); return; }
      show(el, false);
    }, { passive: true });
    doc.addEventListener('mouseover', function (event) {
      /* Over the card, or back over the trigger of the card that is shown: the card stays. */
      var t = event.target;
      if (t.closest && t.closest('#card')) { clearTimeout(hideTimer); return; }
      if (card && !card.hidden && owner && triggerOf(t) === owner) clearTimeout(hideTimer);
    });
    doc.addEventListener('mouseout', function (event) {
      var el = triggerOf(event.target) || (event.target.closest && event.target.closest('#card'));
      if (el && !(event.relatedTarget && el.contains(event.relatedTarget))) hideSoon();
    });
  }
  var returning = false; /* focus handed back to a trigger after Escape does not reopen its card */
  doc.addEventListener('focusin', function (event) {
    var t = event.target;
    /* A pinned card belongs to its trigger: focus that moves anywhere else closes it. */
    if (card && !card.hidden && pinned && t !== owner && !card.contains(t)) hide();
    var el = triggerOf(t);
    if (el && !pinned && !returning) show(el, false);
  });
  doc.addEventListener('focusout', function (event) {
    if (triggerOf(event.target) && !(event.relatedTarget && event.relatedTarget.closest && event.relatedTarget.closest('#card'))) hideSoon();
  });
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
      if (event.defaultPrevented) return; /* the search, or a component, used this Escape */
      var back = owner;
      var fromCard = card.contains(event.target) || event.target === owner;
      hide();
      if (fromCard && back && doc.activeElement !== back) { returning = true; back.focus(); returning = false; }
      return;
    }
    /* Tab from an opened trigger enters the card's links; leaving the last one continues after the trigger. */
    if (event.key !== 'Tab' || !card || card.hidden || !owner || !pinned) return;
    var inCard = all('a[href], button', card);
    if (!inCard.length) { hide(); return; }
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

  /* The table of examples is one stop for the Tab key. Inside it the arrow keys move between its marks and headings,
     Home and End go to the ends of a row, and Control with Home or End to the first and last control of the table. */
  if (grid) {
    var gridControls = all('thead button, tbody th a[href], tbody td button', grid);
    var gridStop = gridControls[0] || null;
    gridControls.forEach(function (c) { c.tabIndex = c === gridStop ? 0 : -1; });
    var gridWrap = grid.closest('.grid-wrap');
    /* The table scrolls with the control in focus, so its scroll box need not be a stop of its own. */
    if (gridWrap && gridStop && gridWrap.getAttribute('tabindex') === '0') gridWrap.tabIndex = -1;
    /* What the keys do inside the table is the description of its region (the served hint says it on screen). */
    if (gridStop) {
      var keysHost = gridWrap || grid;
      var gridKeys = doc.getElementById('grid-keys');
      var caption = grid.caption;
      if (!gridKeys && caption && caption.classList.contains('visually-hidden')) {
        /* read when a screen reader enters the table */
        gridKeys = element('span', 'grid-keys', WORDS.gridKeys);
        gridKeys.id = 'grid-keys';
        caption.appendChild(doc.createTextNode(' '));
        caption.appendChild(gridKeys);
      }
      if (!gridKeys) {
        gridKeys = element('p', 'visually-hidden grid-keys', WORDS.gridKeys);
        gridKeys.id = 'grid-keys';
        keysHost.parentNode.insertBefore(gridKeys, keysHost.nextSibling);
      }
      var described = (keysHost.getAttribute('aria-describedby') || '').split(/\s+/).filter(Boolean);
      if (described.indexOf('grid-keys') < 0) keysHost.setAttribute('aria-describedby', described.concat('grid-keys').join(' '));
    }
    grid.addEventListener('focusin', function (event) {
      var c = event.target;
      if (c === gridStop || gridControls.indexOf(c) < 0) return;
      if (gridStop) gridStop.tabIndex = -1;
      c.tabIndex = 0;
      gridStop = c;
    });
    grid.addEventListener('keydown', function (event) {
      if (event.altKey || event.metaKey || event.shiftKey) return;
      var ends = event.key === 'Home' || event.key === 'End';
      if (event.ctrlKey && !ends) return;
      var step = { ArrowLeft: [0, -1], ArrowRight: [0, 1], ArrowUp: [-1, 0], ArrowDown: [1, 0] }[event.key];
      if (!step && !ends) return;
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
      if (event.ctrlKey) {
        target = event.key === 'Home' ? gridControls[0] : gridControls[gridControls.length - 1];
      } else if (step) {
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

    /* Reading the table. The mark in focus or under the pointer lights its row and its column (data-cross: row, col,
       or both where they meet). Each entry of the legend becomes a switch that also counts the marks of its status: it
       marks those cells (data-lit) and quietens the others, so a status can be followed across every family and part
       of the theory; several can be on at once. Without the script the legend stays a plain list. */
    var crossed = [];
    var cross = function (cell) {
      crossed.forEach(function (c) { c.removeAttribute('data-cross'); });
      crossed = [];
      if (!cell || !grid.contains(cell)) return;
      var tr = cell.parentNode;
      var head = tr.parentNode && tr.parentNode.localName === 'thead';
      var ci = cell.cellIndex;
      if (!head) Array.prototype.forEach.call(tr.cells, function (c) { c.setAttribute('data-cross', 'row'); crossed.push(c); });
      if (ci > 0) Array.prototype.forEach.call(grid.rows, function (row) {
        var c = row.cells[ci];
        if (!c) return;
        c.setAttribute('data-cross', row === tr && !head ? 'both' : 'col');
        if (crossed.indexOf(c) < 0) crossed.push(c);
      });
    };
    grid.addEventListener('focusin', function (event) { cross(event.target.closest('th, td')); });
    grid.addEventListener('focusout', function (event) { if (!(event.relatedTarget && grid.contains(event.relatedTarget))) cross(null); });
    if (hoverCapable) {
      grid.addEventListener('mouseover', function (event) { cross(event.target.closest('th, td')); });
      grid.addEventListener('mouseleave', function () { var a = doc.activeElement; cross(a && grid.contains(a) ? a.closest('th, td') : null); });
    }
    var marked = all('td.cell[data-status]', grid);
    var legendList = (grid.closest('.grid-block') || doc).querySelector('.legend');
    var lensNews = legendList ? liveRegion(legendList.parentNode) : null;
    var lenses = [];
    var applyLens = function () {
      var on = lenses.filter(function (b) { return b.getAttribute('aria-pressed') === 'true'; }).map(function (b) { return b.getAttribute('data-lens'); });
      var n = 0;
      marked.forEach(function (c) {
        if (on.indexOf(c.getAttribute('data-status')) >= 0) { c.setAttribute('data-lit', ''); n++; } else c.removeAttribute('data-lit');
      });
      if (on.length) grid.setAttribute('data-lens', on.join(' ')); else grid.removeAttribute('data-lens');
      if (lensNews) lensNews.textContent = on.length ? fill(WORDS.lensOn, { n: n, all: marked.length }) : WORDS.lensOff;
    };
    var lensHelp = null;
    if (legendList) all('li', legendList).forEach(function (li) {
      var m = li.querySelector('.mark');
      var slug = m && /(?:^|\s)mark-([\w-]+)/.exec(m.getAttribute('class') || '');
      /* The status this mark stands for, as the cells of the table write it. */
      var st = null;
      if (slug) marked.some(function (c) {
        var s = c.getAttribute('data-status');
        if (s.replace(/\s+/g, '-') !== slug[1]) return false;
        st = s;
        return true;
      });
      var count = st ? marked.filter(function (c) { return c.getAttribute('data-status') === st; }).length : 0;
      if (!count) return;
      if (!lensHelp) {
        lensHelp = element('p', 'lens-help', WORDS.lensHelp);
        lensHelp.id = 'lens-help';
        legendList.parentNode.insertBefore(lensHelp, legendList);
      }
      var b = element('button', 'lens');
      b.type = 'button';
      b.setAttribute('aria-pressed', 'false');
      b.setAttribute('data-lens', st);
      b.setAttribute('aria-describedby', 'lens-help');
      while (li.firstChild) b.appendChild(li.firstChild);
      b.appendChild(doc.createTextNode(' '));
      b.appendChild(element('span', 'count', String(count)));
      li.appendChild(b);
      lenses.push(b);
      b.addEventListener('click', function () {
        b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
        applyLens();
      });
    });
  }

  /* A row opened by the reader becomes the page address, so it can be shared. Moving from one row to another replaces
     the address; opening a row from any other address keeps that address in the history. */
  rows.forEach(function (d) {
    var summary = d.querySelector('summary');
    if (!summary || !d.id) return;
    summary.addEventListener('click', function () {
      var current = hashId();
      var at = current && doc.getElementById(current);
      if (!d.open) {
        if (!current || (at && at.matches('details.row'))) setHash(d.id, false);
        else { leave(summary); setHash(d.id, true); }
      } else if (current === d.id) setHash('', false);
    });
  });

  /* Open all and Close all act within their own section: the examples' rows, or a section's 'proved toward it' lists. */
  function expandables(scope) { return own('details.row, details.known', scope); }
  function bindExpand(b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('data-expand') === 'all';
      var scope = b.closest('section') || doc;
      expandables(scope).forEach(function (d) { d.open = open; });
    });
  }
  var buttons = byTag('button', doc);
  var expandButtons = buttons.filter(function (b) { return b.hasAttribute('data-expand'); });
  expandButtons.forEach(bindExpand);
  var openWord = (expandButtons.filter(function (b) { return b.getAttribute('data-expand') === 'all'; })[0] || {}).textContent;
  var closeWord = (expandButtons.filter(function (b) { return b.getAttribute('data-expand') === 'none'; })[0] || {}).textContent;
  if (openWord && closeWord) {
    sections.filter(shared).forEach(function (section) {
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

  /* Status filter for the statements of the rows. What it leaves out is said where the reader looks: a line under the
     chips counts what is shown, and a row left without statements says so; both offer to show everything again.
     Rows the filter opened or closed return to the reader's own state when it is turned off. A statement reached by a
     link or a search result is shown although the filter hides its status, without changing the filter. */
  var filters = buttons.filter(function (b) { return b.classList.contains('filter') && b.hasAttribute('data-filter') && !b.closest('.find'); });
  var rowStatements = [].concat.apply([], rows.map(function (d) { return all('.statement', d); }));
  var filterTools = filters.length ? (filters[0].closest('.row-tools') || filters[0].parentNode) : null;
  var filterNews = filterTools ? liveRegion(filterTools) : null;
  var rowsBeforeFilter = null;
  var rowsSetByFilter = null; /* what the filter last made of each row, to tell the reader's own changes from it */
  function shownStatuses() {
    return filters.filter(function (f) { return f.getAttribute('aria-pressed') === 'true'; })
                  .map(function (f) { return f.getAttribute('data-filter'); });
  }
  function showAllButton(label, focusAfter, keepOpen) {
    var b = element('button', 'link-btn', label);
    b.type = 'button';
    b.setAttribute('data-show-all', '');
    b.addEventListener('click', function () {
      var to = focusAfter();
      setFilters([]);
      if (keepOpen) keepOpen.open = true; /* the row whose statements were asked for stays open to show them */
      if (to) to.focus();
    });
    return b;
  }
  var filterNote = null;
  if (filterTools) {
    /* The live region announces the count; on screen it stands beside the button that undoes the filter. */
    filterNote = element('p', 'filter-note');
    filterNote.id = 'examples-filter-note';
    filterNote.hidden = true;
    var noteText = element('span');
    noteText.setAttribute('aria-hidden', 'true');
    filterNote.appendChild(noteText);
    filterNote.appendChild(doc.createTextNode(' '));
    filterNote.appendChild(showAllButton(WORDS.showAll, function () { return filters[0]; }));
    filterTools.appendChild(filterNote);
  }
  function rowNote(d) {
    var note = d.querySelector('.filter-empty');
    if (note) return note;
    var body = d.querySelector('.row-body');
    if (!body) return null;
    note = element('p', 'filter-empty');
    note.hidden = true;
    note.appendChild(doc.createTextNode(WORDS.rowEmpty + ' '));
    note.appendChild(showAllButton(WORDS.rowShowAll, function () { return d.querySelector('summary'); }, d));
    body.insertBefore(note, body.querySelector('.statements'));
    return note;
  }
  function visibleIn(d) { return !!d.querySelector('.statement:not([hidden])'); }
  function describeFilter() {
    var on = shownStatuses();
    var shown = rowStatements.filter(function (s) { return !s.hidden; }).length;
    var inRows = 0;
    rows.forEach(function (d) {
      var any = visibleIn(d);
      if (any) inRows++;
      var empty = on.length > 0 && !any;
      if (empty) d.setAttribute('data-filter-empty', ''); else d.removeAttribute('data-filter-empty');
      var note = empty ? rowNote(d) : d.querySelector('.filter-empty');
      if (note) note.hidden = !empty;
    });
    var counted = fill(WORDS.shown, { shown: shown, total: rowStatements.length, rows: inRows, all: rows.length });
    if (filterNews) filterNews.textContent = on.length ? counted : fill(WORDS.allShown, { total: rowStatements.length });
    if (filterNote) {
      filterNote.hidden = !on.length;
      filterNote.firstChild.textContent = on.length ? counted : '';
    }
  }
  function applyFilter(record) {
    var on = shownStatuses();
    rowStatements.forEach(function (s) {
      s.hidden = on.length > 0 && on.indexOf(s.getAttribute('data-status')) < 0;
      s.removeAttribute('data-filter-exempt');
    });
    if (on.length) {
      if (!rowsBeforeFilter) rowsBeforeFilter = rows.map(function (d) { return d.open; });
      rows.forEach(function (d) { d.open = visibleIn(d); });
      rowsSetByFilter = rows.map(function (d) { return d.open; });
    } else if (rowsBeforeFilter) {
      rows.forEach(function (d, i) { d.open = rowsBeforeFilter[i]; });
      rowsBeforeFilter = null;
      rowsSetByFilter = null;
    }
    describeFilter();
    /* Focus inside a statement the filter has just hidden moves to its row. */
    var a = doc.activeElement;
    var lost = a && a.closest && a.closest('.statement[hidden]');
    var row = lost && lost.closest('details.row');
    if (row && row.querySelector('summary')) row.querySelector('summary').focus();
    if (record !== false) writeParams({ show: on.join(',') });
    announce();
  }
  function setFilters(list) {
    filters.forEach(function (f) { f.setAttribute('aria-pressed', list.indexOf(f.getAttribute('data-filter')) >= 0 ? 'true' : 'false'); });
    applyFilter();
  }
  showDespiteFilter = filters.length ? function (s) {
    if (!shownStatuses().length) return;
    s.hidden = false;
    s.setAttribute('data-filter-exempt', '');
    describeFilter();
  } : null;
  refilter = filters.length ? function () {
    var on = shownStatuses();
    var changed = false;
    rowStatements.forEach(function (s) {
      if (!s.hasAttribute('data-filter-exempt')) return;
      s.removeAttribute('data-filter-exempt');
      s.hidden = on.length > 0 && on.indexOf(s.getAttribute('data-status')) < 0;
      changed = true;
    });
    if (changed) describeFilter();
  } : null;
  /* A row the reader opens or closes while the filter is on (by its heading, a link, or Back) is the reader's own
     state from then on, and stays so when the filter is turned off. Printing opens rows for the paper only. */
  rows.forEach(function (d, i) {
    d.addEventListener('toggle', function () {
      if (!rowsSetByFilter || printed) return;
      if (d.open !== rowsSetByFilter[i]) { rowsBeforeFilter[i] = d.open; rowsSetByFilter[i] = d.open; }
    });
  });
  filters.forEach(function (f) {
    f.addEventListener('click', function () {
      f.setAttribute('aria-pressed', f.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      applyFilter();
    });
  });
  var tallyLinks = [].concat.apply([], byClass('tally', doc).map(function (t) { return all('a[data-filter]', t); }));

  /* A box that scrolls sideways (a wide formula, the bar on a narrow screen) names the edges where it hides more:
     data-edge holds start, end, both or nothing, so that the CSS fades exactly those edges, in either theme. */
  function edgesOf(el) {
    var max = el.scrollWidth - el.clientWidth;
    var e = [];
    if (max > 1 && el.scrollLeft > 1) e.push('start');
    if (max > 1 && el.scrollLeft < max - 1) e.push('end');
    if (e.length) el.setAttribute('data-edge', e.join(' ')); else el.removeAttribute('data-edge');
  }
  var watchedEdges = [];
  function watchEdges(el, on) {
    var at = watchedEdges.indexOf(el);
    if (on && at < 0) { watchedEdges.push(el); el.addEventListener('scroll', onEdgeScroll, { passive: true }); }
    if (!on && at >= 0) { watchedEdges.splice(at, 1); el.removeEventListener('scroll', onEdgeScroll); }
    if (on) edgesOf(el); else el.removeAttribute('data-edge');
  }
  function onEdgeScroll(event) { edgesOf(event.currentTarget); }

  /* Mark the section in view in the bar; on a narrow screen the bar scrolls to keep that link in sight. */
  var nav = doc.querySelector('.nav');
  /* The bar is measured when it scrolls or the window changes, never at start-up: the served fade fits its start. */
  if (nav) {
    nav.addEventListener('scroll', onEdgeScroll, { passive: true });
    window.addEventListener('resize', function () { edgesOf(nav); });
  }
  var navLinks = all('.nav a');
  var byId = {};
  navLinks.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
  function keepInSight(a) {
    if (!nav || nav.scrollWidth <= nav.clientWidth + 1) return;
    var n = nav.getBoundingClientRect();
    var l = a.getBoundingClientRect();
    if (l.left >= n.left + 4 && l.right <= n.right - 28) return;
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
  if ('IntersectionObserver' in window && navLinks.length) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting && byId[e.target.id]) setCurrent(e.target.id); });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(byId).forEach(function (id) { var s = doc.getElementById(id); if (s) observer.observe(s); });
  }

  /* Printing shows every disclosure (rows, related lists, column definitions); afterwards each is as the reader left it.
     A second print request before the first ends keeps the state saved by the first. */
  var printed = null;
  var beforePrint = null;
  window.addEventListener('beforeprint', function () {
    if (printed) { printed.forEach(function (d) { d.open = true; }); return; }
    printed = disclosures.slice();
    beforePrint = printed.map(function (d) { return d.open; });
    printed.forEach(function (d) { d.open = true; });
  });
  window.addEventListener('afterprint', function () {
    if (beforePrint) printed.forEach(function (d, i) { d.open = beforePrint[i]; });
    printed = null;
    beforePrint = null;
  });

  /* Search of the whole page: every part named in the bar, and the programme before them (cover, lead, status key);
     in each, its statements, questions, rows and each row's scope for every column, counterexamples, open problems,
     essay, terms, column definitions and introductions.
     Matching ignores case and accents and every word must occur. A short word must begin a word of the page ('ring' does
     not find 'pairing'); a longer word may sit inside one ('algebra' finds 'coalgebra'). "Quoted words" match as a
     phrase, also before the closing quote is typed. A Greek letter's name finds the letter. Words written with TeX
     (a backslash, _, ^ or braces) are looked for in the formulae, with or without braces. Results are grouped by part,
     the part with the best match first, and the best matches first within a part. */
  var programme = doc.getElementById('programme');
  /* The parts: sections of the page, and a component's section where it offers searchable text. */
  var partSections = sections.filter(function (s) { return s.id && (shared(s) || s.querySelector('[data-qh-unit][id]')); });
  var SCOPES = (programme ? ['programme'] : []).concat(partSections.map(function (s) { return s.id; })
    .filter(function (id) { return byId[id] && id !== 'programme'; }));
  function scopeLabel(id) {
    if (byId[id]) return byId[id].textContent.trim();
    var h = doc.querySelector('#' + id + ' h2');
    return h ? h.textContent.trim() : id;
  }
  function scopeOf(el) {
    if (!main || !main.contains(el)) return null;
    var s = el.closest('section.section');
    if (s && SCOPES.indexOf(s.id) >= 0) return s.id;
    /* Anything else belongs to the last part that begins before it, or to the programme. */
    var scope = programme ? 'programme' : null;
    for (var i = 0; i < partSections.length; i++) {
      var p = partSections[i];
      if (SCOPES.indexOf(p.id) < 0) continue;
      if (p.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING) scope = p.id; else break;
    }
    return scope;
  }

  function fold(s) {
    return (s || '').normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase()
      .replace(/[‘’ʼ]/g, '\'').replace(/[“”„‟«»]/g, '"').replace(/[‐-―−]/g, '-');
  }
  /* TeX compared without braces or spaces, with \geq, \leq and \neq as \ge, \le and \ne. */
  function texNorm(s) {
    return fold(s).replace(/\\(geq|leq|neq)(?![a-z])/g, function (m, c) { return '\\' + c.slice(0, 2); }).replace(/[{}\s]/g, '');
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
  var GREEK = { alpha: 'α', beta: 'β', gamma: 'γ', delta: 'δ', epsilon: 'ε', varepsilon: 'ε', zeta: 'ζ', eta: 'η', theta: 'θ',
                vartheta: 'θ', iota: 'ι', kappa: 'κ', varkappa: 'κ', lambda: 'λ', mu: 'μ', nu: 'ν', xi: 'ξ', pi: 'π', varpi: 'π',
                rho: 'ρ', varrho: 'ρ', sigma: 'σς', varsigma: 'ς', tau: 'τ', upsilon: 'υ', phi: 'φ', varphi: 'φ', chi: 'χ',
                psi: 'ψ', omega: 'ω' };
  var TEXY = /[\\_^{}]/;
  var LETTERLIKE = /[℀-⅏]|\ud835[\udc00-\udfff]/; /* ℂ, ℤ, 𝔰 ...: folding would turn them into plain letters */
  function parseQuery(q) {
    var out = [];
    String(q || '').replace(/>=/g, '≥').replace(/<=/g, '≤').replace(/[“”„‟«»]/g, '"')
      /* A TeX command typed apart from a one-letter or braced argument is one formula word: \mathbb C as \mathbb{C}. */
      .replace(/(\\[A-Za-z]+)\s+(?=\{|[A-Za-z0-9](?![A-Za-z0-9]))/g, '$1')
      .replace(/"([^"]+)(?:"|$)|(\S+)/g, function (_, phrase, w) {
        var raw = phrase ? phrase.replace(/\s+/g, ' ').trim() : w.replace(/^["'.,;:!?()[\]]+|["'.,;:!?()[\]]+$/g, '');
        if (!raw) return '';
        var f = fold(raw);
        var kind = TEXY.test(raw) ? 'tex' : LETTERLIKE.test(raw) ? 'letterlike' :
                   (!phrase && Object.prototype.hasOwnProperty.call(GREEK, f)) ? 'greek' : 'text';
        /* TeX written into words (W_3-modules) is also looked for as the page's words show it (W3-modules). */
        var plain = kind === 'tex' ? fold(raw.replace(/\\[A-Za-z]+/g, '').replace(/[_^{}$]/g, '')) : '';
        out.push({ w: f, raw: raw.toLowerCase(), tex: texNorm(raw), kind: kind, plain: /[a-z]{3}/.test(plain) && plain !== f ? plain : '',
                   strict: kind === 'text' && /^[0-9a-z][0-9a-z '-]*$/.test(f) && f.replace(/[^0-9a-z]/g, '').length <= 5 });
        return '';
      });
    return out;
  }
  var WORDCHAR = /[0-9a-zµÀ-ɏͰ-ϿЀ-ӿ]/;
  function isWordChar(c) { return !!c && WORDCHAR.test(c); }
  /* How a word occurs in a field: 3 as a whole word, 2 at the start of a word, 1 inside a word, 0 not at all. */
  function grade(field, w, strict) {
    if (!field || !w) return 0;
    var lead = isWordChar(w.charAt(0));
    var tail = isWordChar(w.charAt(w.length - 1));
    var best = 0;
    for (var at = field.indexOf(w); at >= 0; at = field.indexOf(w, at + 1)) {
      var start = !lead || !isWordChar(field.charAt(at - 1));
      if (strict && !start) continue;
      var end = !tail || !isWordChar(field.charAt(at + w.length));
      var g = start && end ? 3 : start ? 2 : 1;
      if (g > best) { best = g; if (g === 3) break; }
    }
    return best;
  }

  /* Reader-visible text of an element, formulae given by their symbols (or left out), without marks or chips. */
  function textOf(el, skip, noMath) {
    if (!el) return '';
    var out = [];
    (function walk(n) {
      if (n.nodeType === 3) { out.push(n.nodeValue); return; }
      if (n.nodeType !== 1) return;
      if (skip && n.matches(skip)) return;
      var tag = n.localName;
      if (tag === 'svg' || tag === 'annotation' || tag === 'script' || tag === 'style' || (noMath && tag === 'math')) return;
      for (var c = n.firstChild; c; c = c.nextSibling) walk(c);
      if (BLOCK.test(tag)) out.push(' ');
    })(el);
    return out.join('').replace(/\s+/g, ' ').trim();
  }
  function texOf(el, skip) {
    if (!el) return '';
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

  /* The search units, built in idle moments after the page has loaded, or at once when a search begins first. */
  var units = null;
  var pending = null;
  var building = [];
  function labelsOf(el) {
    return el ? all('.status-chip, .statement-notes .note-label, .statement-hyp-label, .added-chip', el)
      .map(function (n) { return textOf(n); }).join(' ') : '';
  }
  function add(el, o) {
    if (!el || (!shared(el) && !o.offered)) return;
    var scope = scopeOf(el);
    if (!scope) return;
    var chip = o.statusEl ? o.statusEl.querySelector('.status-chip') : null;
    var statusLabel = o.statusLabel || (chip ? textOf(chip) : '');
    var title = o.title || '';
    var context = o.context || '';
    var labels = o.labels !== undefined ? o.labels : labelsOf(o.statusEl);
    var body = o.body !== undefined ? o.body : textOf(el, o.skip);
    var tex = texOf(el, o.skip) + ' ' + (o.quiet ? '' : texOf(o.titleEl)); /* a borrowed title's formulae are not the unit's */
    building.push({
      el: el, scope: scope, titleEl: o.titleEl || null, contextEl: o.contextEl || null, contextLead: o.contextLead || '',
      title: title, context: context, skip: o.skip || null, quiet: !!o.quiet,
      status: o.status || (o.statusEl ? o.statusEl.getAttribute('data-status') : null),
      statusLabel: statusLabel, mark: o.mark || (chip ? chip.querySelector('.mark') : null),
      ft: o.quiet ? '' : fold(title), fc: fold(context),
      fb: fold(body + ' \u0001 ' + statusLabel + ' ' + labels),
      fl: fold(statusLabel + ' ' + labels),
      raw: (textOf(o.titleEl) + ' ' + context + ' ' + body).toLowerCase(),
      ro: (textOf(o.titleEl) + ' ' + body).toLowerCase(),
      ttex: o.quiet ? '' : texNorm(texOf(o.titleEl)),
      tex: texNorm(tex)
    });
  }
  function questionHead(q) {
    var n = q.querySelector('.question-num');
    return n ? textOf(n, '.question-num-label') + '. ' : '';
  }
  function heading(section) {
    var h = section && section.querySelector('h2');
    return h ? (h.querySelector('.anchor') || h) : null;
  }
  function jobs() {
    var list = [];
    var HEAD = '.statement-head, .statement-notes .note-label, .statement-hyp-label, .added-chip';
    /* A question's own statement: a direct child, or inside .question-ask on a comparison card. */
    var ASKED = ':scope > .statement, :scope > .question-ask > .statement';
    var cover = main && main.querySelector(':scope > .cover');
    var coverTitle = cover && cover.querySelector('h1');
    if (cover) list.push(function () { add(cover, { titleEl: coverTitle, title: textOf(coverTitle), skip: 'h1, .kicker, .as-of' }); });
    paragraphs(leads).forEach(function (p) {
      list.push(function () { add(p, { titleEl: coverTitle, title: textOf(coverTitle), quiet: true }); });
    });
    byClass('key-item', main).forEach(function (item) {
      list.push(function () {
        var dt = item.querySelector('dt');
        var h = heading(item.closest('section'));
        add(item, { titleEl: dt, title: textOf(dt), contextEl: h, context: textOf(h), skip: 'dt', mark: dt && dt.querySelector('.mark') });
      });
    });
    [].concat.apply([], byClass('changes', main).map(function (c) { return all('li', c); })).forEach(function (li) {
      list.push(function () { var t = li.querySelector('.change-link span'); add(li, { titleEl: t, title: textOf(t), skip: '.change-link' }); });
    });
    byClass('section-intro', main).filter(function (x) { return x.parentNode.matches && x.parentNode.matches('section.section'); })
      .forEach(function (intro) {
      list.push(function () { var h = heading(intro.parentNode); add(intro, { titleEl: h, title: textOf(h) }); });
    });
    byClass('statement', main).forEach(function (s) {
      list.push(function () {
        var question = s.closest('.question');
        if (question && question.querySelector(ASKED) === s) return; /* indexed with its question */
        if (s.closest('.failure')) return; /* indexed with its claim */
        var titleEl = s.querySelector('.statement-title');
        var o = { titleEl: titleEl, title: textOf(titleEl), skip: HEAD, statusEl: s };
        var row = s.closest('details.row');
        var group = s.closest('.open-group');
        if (question) { var qh = question.querySelector('h3'); o.contextEl = qh && (qh.querySelector('.anchor') || qh); o.contextLead = questionHead(question); o.context = o.contextLead + textOf(qh); }
        else if (row) { o.contextEl = row.querySelector('.row-name'); o.context = textOf(o.contextEl); }
        else if (group) { var gh = group.querySelector('h3'); o.contextEl = gh && (gh.querySelector('.anchor') || gh); o.context = textOf(gh); }
        add(s, o);
      });
    });
    byClass('question', main).forEach(function (q) {
      list.push(function () {
        var asked = q.querySelector(ASKED);
        var h = q.querySelector('h3');
        /* The question's own statement title is searched with it; related statements are indexed on their own. */
        add(q, { titleEl: h && (h.querySelector('.anchor') || h), title: questionHead(q) + textOf(h), statusEl: asked,
                 skip: 'h3, .question-num, .known, .question-known, .question-why-label, .question-ask-label, .status-chip, ' +
                       '.statement-notes .note-label, .statement-hyp-label, .added-chip' });
      });
    });
    rows.forEach(function (d) {
      list.push(function () {
        var name = d.querySelector('.row-name');
        add(d, { titleEl: name, title: textOf(name), labels: '',
                 skip: '.row-num, .row-name, .row-marks, .row-count, .statements, .cell-lines, .filter-empty' });
        /* Each column's scope in the row: found by the row, the column, its status or the words of the scope. */
        all('.cell-lines > .cell-line', d).forEach(function (li) {
          var col = li.querySelector('.cell-col');
          /* Its cell's status is said and searchable by its words; it is not a statement's status, so the Status chips
             and the tally, which count statements, leave it out. */
          add(li, { titleEl: name, title: textOf(name), quiet: true, contextEl: col, context: textOf(name) + ' ' + textOf(col),
                    skip: '.cell-col, .cell-st', labels: '',
                    statusLabel: textOf(li.querySelector('.cell-st')), mark: li.querySelector('.mark') });
        });
      });
    });
    byClass('failure', main).forEach(function (f) {
      list.push(function () {
        var claim = f.querySelector('.claim-text');
        var witness = f.querySelector('.statement');
        var tag = f.querySelector('.claim-tag');
        var wchip = witness && witness.querySelector('.status-chip');
        /* A false claim is shown as false, and its witness's status as the counterexample's. */
        add(f, { titleEl: claim, title: textOf(claim), statusEl: witness, mark: tag && tag.querySelector('.mark'),
                 statusLabel: textOf(tag) + (wchip ? ' · ' + fill(WORDS.witness, { status: textOf(wchip) }) : ''),
                 skip: '.claim, .status-chip, .added-chip, .statement-notes .note-label' });
      });
    });
    byClass('open-group', main).forEach(function (g) {
      list.push(function () { var h = g.querySelector('h3'); add(g, { titleEl: h && (h.querySelector('.anchor') || h), title: textOf(h), skip: 'h3, .statements' }); });
    });
    byClass('col-def', main).forEach(function (c) {
      list.push(function () {
        var dt = c.querySelector('dt');
        var defs = c.closest('details');
        var sum = defs && defs.querySelector('summary');
        add(c, { titleEl: dt, title: textOf(dt), contextEl: sum, context: textOf(sum), skip: 'dt' });
      });
    });
    var essayTitle = doc.getElementById('essay-title');
    if (essayTitle) list.push(function () { add(essayTitle, { titleEl: essayTitle, title: textOf(essayTitle), skip: 'h3' }); });
    byClass('essay-lead', main).concat(paragraphs(essays, 'essay-byline')).forEach(function (p) {
      list.push(function () { add(p, { titleEl: essayTitle, title: textOf(essayTitle), quiet: true }); });
    });
    byClass('gloss', main).forEach(function (g) {
      list.push(function () { var dt = g.querySelector('dt'); add(g, { titleEl: dt, title: textOf(dt), skip: 'dt' }); });
    });
    /* A component's own text is searched only where it offers it: an element with an id and data-qh-unit, titled by
       its [data-qh-unit-title] descendant. */
    (isolating ? all(ISOLATED + ' [data-qh-unit][id]') : []).forEach(function (el) {
      list.push(function () {
        var t = el.querySelector('[data-qh-unit-title]');
        /* A unit may give its status (one of the page's status values) and its place in the component. */
        var st = el.getAttribute('data-qh-unit-status');
        var key = st ? statusKey(st) : null;
        add(el, { titleEl: t, title: textOf(t), skip: '[data-qh-unit-title]', offered: true, status: key ? st : null,
                  statusLabel: key ? key.label : '', mark: key ? key.mark : null, context: el.getAttribute('data-qh-unit-place') || '' });
      });
    });
    /* Text in a part that none of the units above holds (a part of another shape, whatever its markup: paragraphs,
       lists, divs, definition lists, tables): each stretch of it belongs to its nearest block (a table's row, for a
       table), and each such block becomes a unit with its own words, titled by the nearest heading before it, so that
       nothing a reader can read lies outside the search. */
    list.push(function () {
      var held = typeof Set === 'function' ? new Set(building.map(function (u) { return u.el; })) : null;
      if (!held) return;
      var isHeld = function (el) { for (var n = el; n && n !== main; n = n.parentElement) if (held.has(n)) return true; return false; };
      var CHROME = '.find, .qh-notice, #card, nav, .row-tools, .grid-block, .tally, .section-head, .kicker, .essay-byline, ' +
                   '.visually-hidden, [hidden], [aria-hidden="true"], button, annotation, svg, script, style';
      var BLOCKS = 'p, li, dd, dt, h3, h4, h5, h6, blockquote, figcaption, pre, summary, td, th, caption, div, article, aside, header, footer';
      partSections.forEach(function (sec) {
        if (!shared(sec)) return;
        var heads = all('h2, h3, h4', sec);
        var blocks = [];
        var words = [];
        var walker = doc.createTreeWalker(sec, 4);
        for (var t = walker.nextNode(); t; t = walker.nextNode()) {
          var el = t.parentElement;
          if (!el || !/\S/.test(t.nodeValue) || el.closest(CHROME) || isHeld(el)) continue;
          var row = el.closest('tr');
          var b = row && sec.contains(row) ? row : el.closest(BLOCKS);
          if (!b || !sec.contains(b) || b === sec) continue;
          var k = blocks.indexOf(b);
          if (k < 0) { k = blocks.length; blocks.push(b); words.push(''); }
          words[k] += t.nodeValue + (el.closest('td, th') && !t.nextSibling ? ' ' : '');
        }
        blocks.forEach(function (b, k) {
          var own = words[k].replace(/\s+/g, ' ').trim();
          if (!/[A-Za-z\u00C0-\u024F]{3}/.test(own) || own.split(' ').length < 2) return;
          var head = null;
          heads.forEach(function (h) { if (h !== b && !h.contains(b) && (h.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING)) head = h; });
          give(b, sec.id + '-' + ident(own.split(' ').slice(0, 8).join(' ')).slice(0, 48));
          add(b, { titleEl: head, title: head ? textOf(head) : '', body: own });
        });
      });
    });
    return list;
  }
  /* The status key's words and mark for a status value. */
  function statusKey(st) {
    var cls = 'mark-' + st.replace(/\s+/g, '-');
    var items = byClass('key-item', main);
    for (var i = 0; i < items.length; i++) {
      var m = items[i].querySelector('.mark');
      if (m && m.classList.contains(cls)) return { label: textOf(items[i].querySelector('dt')), mark: m };
    }
    return null;
  }
  function index() {
    if (units) return units;
    if (!pending) { building = []; pending = jobs(); }
    while (pending.length) pending.shift()();
    units = building;
    pending = null;
    return units;
  }
  function indexWhenIdle() {
    if (units || READER) return;
    if (!pending) { building = []; pending = jobs(); }
    /* Where idle callbacks are missing, slices of about 8 ms with the page free in between. */
    var idle = window.requestIdleCallback || function (fn) {
      return setTimeout(function () {
        var start = Date.now();
        fn({ timeRemaining: function () { return Math.max(0, 8 - (Date.now() - start)); } });
      }, 30);
    };
    idle(function slice(deadline) {
      if (units || !pending) return;
      while (pending.length && deadline.timeRemaining() > 2) pending.shift()();
      if (pending.length) idle(slice); else { units = building; pending = null; }
    });
  }

  /* The search words as marks: where each occurs in a text, by the same rule as the matching. */
  function marksOf(terms) {
    var m = [];
    terms.forEach(function (t) {
      if (t.kind === 'text' || t.kind === 'tex') {
        m.push({ w: t.w, strict: t.strict });
        if (t.plain) m.push({ w: t.plain, strict: false });
      } else if (t.kind === 'greek') {
        m.push({ w: t.w, strict: true, whole: true });
        GREEK[t.w].split('').forEach(function (c) { m.push({ w: c, strict: false }); });
      }
    });
    return m;
  }
  function rangesIn(s, marks) {
    var m = foldMap(s);
    var ranges = [];
    marks.forEach(function (k) {
      var lead = isWordChar(k.w.charAt(0));
      for (var at = m.text.indexOf(k.w); at >= 0; at = m.text.indexOf(k.w, at + 1)) {
        if (k.strict && lead && isWordChar(m.text.charAt(at - 1))) continue;
        if (k.whole && isWordChar(m.text.charAt(at + k.w.length))) continue;
        ranges.push([m.from[at], m.to[at + k.w.length - 1]]);
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
  /* Wrap the occurrences of the search words in an element's text (outside formulae) in <mark>. */
  function highlight(node, marks) {
    if (!marks.length) return node;
    var texts = [];
    (function walk(n) {
      if (n.nodeType === 3) { texts.push(n); return; }
      if (n.nodeType !== 1 || n.localName === 'math' || n.localName === 'svg') return;
      for (var c = n.firstChild; c; c = c.nextSibling) walk(c);
    })(node);
    texts.forEach(function (t) {
      var s = t.nodeValue;
      var ranges = rangesIn(s, marks);
      if (!ranges.length) return;
      var frag = doc.createDocumentFragment();
      var pos = 0;
      ranges.forEach(function (r) {
        if (r[0] > pos) frag.appendChild(doc.createTextNode(s.slice(pos, r[0])));
        frag.appendChild(element('mark', null, s.slice(r[0], r[1])));
        pos = r[1];
      });
      if (pos < s.length) frag.appendChild(doc.createTextNode(s.slice(pos)));
      t.parentNode.replaceChild(frag, t);
    });
    return node;
  }
  /* The words around the first match, cut from the page itself so that formulae keep their form: a formula is copied
     whole, never cut, and set inline. */
  function pieces(el, skip) {
    var out = [];
    (function walk(n) {
      if (n.nodeType === 3) { out.push({ text: n.nodeValue }); return; }
      if (n.nodeType !== 1) return;
      if (skip && n.matches(skip)) return;
      var tag = n.localName;
      if (tag === 'math') { out.push({ math: n, text: textOf(n) }); return; }
      if (tag === 'svg' || tag === 'annotation' || tag === 'script' || tag === 'style') return;
      for (var c = n.firstChild; c; c = c.nextSibling) walk(c);
      if (BLOCK.test(tag)) out.push({ text: ' ' });
    })(el);
    return out;
  }
  function mathCopy(m) {
    var wide = m.getAttribute('display') === 'block' || !!(m.parentNode && m.parentNode.closest && m.parentNode.closest('.math-display, .math-long'));
    var c = m.cloneNode(true);
    c.removeAttribute('display');
    c.classList.remove('tml-display');
    all('[id]', c).forEach(function (n) { n.removeAttribute('id'); });
    if (!wide) return c;
    /* A display formula keeps the page's rule that a wide formula scrolls inside its own box. */
    var box = element('span', 'math-long');
    box.appendChild(c);
    return box;
  }
  function snippetOf(u, marks) {
    var ps = pieces(u.el, u.skip);
    var flat = '';
    ps.forEach(function (p) {
      var t = p.text.replace(/\s+/g, ' ');
      if (t.charAt(0) === ' ' && (!flat || flat.charAt(flat.length - 1) === ' ')) t = t.slice(1);
      p.s = flat.length;
      flat += t;
      p.e = flat.length;
      p.t = t;
    });
    if (!flat.trim()) return null;
    var first = -1;
    if (marks.length) {
      var m = foldMap(flat);
      marks.forEach(function (k) {
        var lead = isWordChar(k.w.charAt(0));
        for (var at = m.text.indexOf(k.w); at >= 0; at = m.text.indexOf(k.w, at + 1)) {
          if (k.strict && lead && isWordChar(m.text.charAt(at - 1))) continue;
          if (k.whole && isWordChar(m.text.charAt(at + k.w.length))) continue;
          if (first < 0 || m.from[at] < first) first = m.from[at];
          break;
        }
      });
    }
    var start = first > 70 ? flat.lastIndexOf(' ', first - 60) + 1 : 0;
    var end = Math.min(flat.length, start + 220);
    if (end < flat.length) { var sp = flat.lastIndexOf(' ', end); if (sp > start + 120) end = sp; }
    var span = element('span', 'find-snippet');
    if (start > 0) span.appendChild(doc.createTextNode('…'));
    ps.forEach(function (p) {
      if (p.e <= start || p.s >= end || p.s === p.e) return;
      if (p.math) { span.appendChild(mathCopy(p.math)); return; }
      span.appendChild(doc.createTextNode(p.t.slice(Math.max(0, start - p.s), Math.min(p.t.length, end - p.s))));
    });
    if (end < flat.length) span.appendChild(doc.createTextNode('…'));
    return highlight(span, marks);
  }
  /* The search words in the element a result led to, drawn with the CSS Highlight API (the text itself is unchanged).
     Returns the first range, or null. */
  var canHighlight = !!(window.CSS && CSS.highlights && typeof window.Highlight === 'function');
  function markWords(el, marks) {
    if (!canHighlight) return null;
    var first = null;
    try {
      CSS.highlights.delete('qh-find');
      if (!el || !marks || !marks.length) return null;
      var h = new Highlight();
      (function walk(n) {
        if (n.nodeType === 3) {
          rangesIn(n.nodeValue, marks).forEach(function (r) {
            var range = doc.createRange();
            range.setStart(n, r[0]);
            range.setEnd(n, r[1]);
            h.add(range);
            if (!first) first = range;
          });
          return;
        }
        if (n.nodeType !== 1 || n.localName === 'math' || n.localName === 'svg') return;
        for (var c = n.firstChild; c; c = c.nextSibling) walk(c);
      })(el);
      if (first) CSS.highlights.set('qh-find', h);
    } catch (e) { first = null; /* no highlight: the result is still reached */ }
    return first;
  }

  var find = null;
  var input = null;
  var facets = null;
  var countLine = null;
  var news = null;
  var results = null;
  var clearButton = null;
  var limit = 40;
  var STEP = 100;
  var hits = [];
  var state = { q: '', scopes: [], statuses: [] };
  var addressTimer = null;
  var pendingAddress = null;
  var newsTimer = null;
  var returnTo = null; /* where '/' was pressed, for Escape */
  function flushAddress() {
    if (!pendingAddress) return;
    clearTimeout(addressTimer);
    var snapshot = pendingAddress;
    pendingAddress = null;
    writeParams(snapshot);
  }

  function chip(attr, value, content) {
    var b = element('button', 'filter');
    b.type = 'button';
    b.setAttribute(attr, value);
    b.setAttribute('aria-pressed', 'false');
    if (typeof content === 'string') b.appendChild(element('span', null, content));
    else content.forEach(function (n) { b.appendChild(n); });
    return b;
  }
  /* Each group of chips is one stop for the Tab key; inside it the arrow keys, Home and End move between the chips. */
  function group(label, buttons) {
    var g = element('div', 'filters');
    g.setAttribute('role', 'toolbar');
    g.setAttribute('aria-label', label);
    g.appendChild(element('span', 'filters-label', label));
    buttons.forEach(function (b, i) { b.tabIndex = i ? -1 : 0; g.appendChild(b); });
    g.addEventListener('keydown', function (event) {
      var i = buttons.indexOf(event.target);
      if (i < 0 || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
      var to = { ArrowRight: i + 1, ArrowDown: i + 1, ArrowLeft: i - 1, ArrowUp: i - 1, Home: 0, End: buttons.length - 1 }[event.key];
      if (to === undefined) return;
      event.preventDefault();
      buttons[(to + buttons.length) % buttons.length].focus();
    });
    g.addEventListener('focusin', function (event) {
      if (buttons.indexOf(event.target) < 0) return;
      buttons.forEach(function (b) { b.tabIndex = b === event.target ? 0 : -1; });
    });
    return g;
  }

  var statusValues = [];
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
    var label = element('label', 'visually-hidden', WORDS.search);
    label.htmlFor = 'find-q';
    var field = element('div', 'find-field');
    input = element('input', 'find-input');
    input.type = 'search';
    input.id = 'find-q';
    input.setAttribute('autocomplete', 'off');
    input.setAttribute('spellcheck', 'false');
    input.setAttribute('enterkeyhint', 'search');
    input.setAttribute('aria-controls', 'find-results');
    if (hoverCapable) input.setAttribute('aria-describedby', 'find-hint'); /* the hint is for a keyboard and a pointer */
    input.placeholder = WORDS.placeholder;
    clearButton = element('button', 'link-btn find-clear', WORDS.clear);
    clearButton.type = 'button';
    clearButton.hidden = true;
    field.appendChild(input);
    field.appendChild(clearButton);
    var hint = element('p', 'find-hint', WORDS.hint);
    hint.id = 'find-hint';

    facets = element('div', 'find-facets');
    facets.hidden = true;
    facets.appendChild(group(WORDS.part, SCOPES.map(function (id) { return chip('data-scope', id, scopeLabel(id)); })));
    var facetSources = filters.slice();
    tallyLinks.forEach(function (a) {
      var st = a.getAttribute('data-filter');
      if (!facetSources.some(function (f) { return f.getAttribute('data-filter') === st; })) facetSources.push(a);
    });
    statusValues = facetSources.map(function (f) { return f.getAttribute('data-filter'); });
    var statusChips = facetSources.map(function (f) {
      return chip('data-status-facet', f.getAttribute('data-filter'),
                  Array.prototype.slice.call(f.childNodes).filter(function (n) { return !(n.nodeType === 1 && n.matches('.count')); })
                    .map(function (n) { return n.cloneNode(true); }));
    });
    if (statusChips.length) facets.appendChild(group(WORDS.status, statusChips));

    /* The count is shown at once; it is announced once typing pauses, and only when it changes. */
    countLine = element('p', 'find-count');
    news = liveRegion(find);
    results = element('div', 'find-results');
    results.id = 'find-results';
    results.hidden = true;

    [label, field, hint, facets, countLine, results].forEach(function (n) { find.insertBefore(n, news); });

    var timer = null;
    input.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () { state.q = input.value; limit = 40; run(true); }, 90);
    });
    input.addEventListener('focus', function () { facets.hidden = false; index(); });
    input.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowDown' || event.key === 'Enter') {
        /* Enter (the phone's Search key) runs the search and moves to the first result; the list stays in view. */
        if (event.key === 'Enter' && state.q !== input.value) { clearTimeout(timer); state.q = input.value; limit = 40; run(true); }
        var first = results.querySelector('.find-link');
        if (first) { event.preventDefault(); first.focus(); }
      } else if (event.key === 'Escape') {
        event.preventDefault();
        if (active()) { clearAll(); return; }
        /* An empty search hands focus back to where '/' was pressed. */
        var back = returnTo;
        returnTo = null;
        if (back && back.isConnected && reachable(back)) back.focus(); else input.blur();
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
      if (more) {
        /* The next results come a hundred at a time, so that a broad search never builds the whole list at once. */
        var had = all('.find-link', results).length;
        limit = had + STEP;
        run(false);
        var links = all('.find-link', results);
        if (links[had]) links[had].focus();
        return;
      }
      var a = event.target.closest('.find-link');
      if (!a || !plainClick(event)) return;
      event.preventDefault();
      go(hits[+a.getAttribute('data-hit')], a);
    });
    results.addEventListener('keydown', function (event) {
      var links = all('.find-link', results);
      var more = results.querySelector('.find-more');
      var i = links.indexOf(event.target);
      if (i < 0 && event.target !== more) return;
      var to = null;
      if (event.target === more) { if (event.key === 'ArrowUp') to = links[links.length - 1]; else if (event.key === 'Escape') to = input; }
      else if (event.key === 'ArrowDown') to = links[i + 1] || more;
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
  function tell(text) {
    clearTimeout(newsTimer);
    newsTimer = setTimeout(function () { if (news.textContent !== text) news.textContent = text; }, 700);
  }
  /* Each Part chip counts the matches in its part, so the reader sees where they are before choosing one. */
  function countParts(perScope) {
    all('.filter[data-scope]', facets).forEach(function (b) {
      var c = b.querySelector('.count');
      if (!c) { b.appendChild(doc.createTextNode(' ')); c = b.appendChild(element('span', 'count')); }
      var n = perScope ? perScope[b.getAttribute('data-scope')] || 0 : null;
      c.textContent = n === null ? '' : String(n);
      if (n === 0) b.setAttribute('data-none', ''); else b.removeAttribute('data-none');
    });
  }
  /* How strongly a unit holds a search term (0: not at all); its title counts most and its context least. */
  function weigh(u, t) {
    if (t.kind === 'tex') {
      var tt = function (f) { return Math.max(grade(f, t.w, false), t.plain ? grade(f, t.plain, false) : 0); };
      return Math.max(tt(u.ft) * 4 + tt(u.fb) + tt(u.fc) / 2, u.ttex.indexOf(t.tex) >= 0 ? 4 : u.tex.indexOf(t.tex) >= 0 ? 1 : 0);
    }
    if (t.kind === 'letterlike') {
      if (u.raw === undefined) u.raw = (textOf(u.titleEl) + ' ' + u.context + ' ' + textOf(u.el, u.skip)).toLowerCase();
      return u.raw.indexOf(t.raw) >= 0 ? 1 : 0;
    }
    if (t.kind === 'greek') {
      /* The letter first; the name counts only as a whole word ('mu' is not the start of 'multiple'). */
      var inTitle = 0;
      var inBody = 0;
      GREEK[t.w].split('').forEach(function (c) { if (u.ft.indexOf(c) >= 0) inTitle = 13; if (u.fb.indexOf(c) >= 0) inBody = 4; });
      return Math.max(inTitle, inBody, grade(u.ft, t.w, true) === 3 ? 12 : 0, grade(u.fb, t.w, true) === 3 ? 3 : 0);
    }
    var gt = grade(u.ft, t.w, t.strict);
    var gb = grade(u.fb, t.w, t.strict);
    var gc = grade(u.fc, t.w, t.strict);
    return gt || gb || gc ? gt * 4 + gb + gc / 2 : 0;
  }
  /* Words typed in the order they are written, as one phrase: a pattern for them side by side, or null for one word or a
     query with a formula, a Greek name or a symbol in it. */
  function phraseOf(terms) {
    if (terms.length < 2 || terms.some(function (t) { return t.kind !== 'text'; })) return null;
    return new RegExp(terms.map(function (t) { return t.w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('[\\s,;:]+'), 'g');
  }
  function together(field, re) {
    if (!field || !re) return false;
    re.lastIndex = 0;
    for (var m = re.exec(field); m; m = re.exec(field)) {
      if (!isWordChar(field.charAt(m.index - 1))) return true;
      re.lastIndex = m.index + 1;
    }
    return false;
  }
  /* Whether a term is in the unit's own words (its title, its text, its formulae), not only in its place. */
  function ownHas(u, t) {
    if (t.kind === 'tex') return u.tex.indexOf(t.tex) >= 0 || !!(grade(u.ft, t.w, false) || grade(u.fb, t.w, false)) ||
      !!(t.plain && (grade(u.ft, t.plain, false) || grade(u.fb, t.plain, false)));
    if (t.kind === 'letterlike') return u.ro.indexOf(t.raw) >= 0;
    if (t.kind === 'greek') return GREEK[t.w].split('').some(function (c) { return u.ft.indexOf(c) >= 0 || u.fb.indexOf(c) >= 0; }) ||
      grade(u.ft, t.w, true) === 3 || grade(u.fb, t.w, true) === 3;
    return !!(grade(u.ft, t.w, t.strict) || grade(u.fb, t.w, t.strict));
  }
  /* Whether a term shows in the words of a result (else it was found only in a formula). */
  function inWords(u, t, plain) {
    if (t.kind === 'letterlike') return plain.toLowerCase().indexOf(t.raw) >= 0;
    var p = fold(plain);
    if (t.kind === 'greek') return GREEK[t.w].split('').some(function (c) { return p.indexOf(c) >= 0; }) || grade(p, t.w, true) === 3;
    if (t.plain && (grade(p, t.plain, false) > 0 || (!u.quiet && grade(fold(textOf(u.titleEl, null, true)), t.plain, false) > 0))) return true;
    return grade(p, t.w, t.strict) > 0 || (!u.quiet && grade(fold(textOf(u.titleEl, null, true)), t.w, t.strict) > 0) ||
           grade(u.fc, t.w, t.strict) > 0 || grade(u.fl, t.w, t.strict) > 0;
  }

  function run(record) {
    var terms = parseQuery(state.q);
    var faceted = state.scopes.length > 0 || state.statuses.length > 0;
    /* Typed text with fewer than two letters or digits (or one symbol) searches nothing, and says so. */
    var typed = terms.map(function (t) { return t.kind === 'text' ? t.w : t.raw; }).join('').replace(/[^\p{L}\p{N}\p{S}]/gu, '');
    var tooShort = !!state.q.trim() && !faceted && !/[^\x00-\x7f]/.test(typed) && typed.length < 2;
    var on = active() && !tooShort;
    clearButton.hidden = !active();
    if (record) {
      clearTimeout(addressTimer);
      pendingAddress = { q: state.q.trim(), 'in': state.scopes.join(','), status: state.statuses.join(',') };
      addressTimer = setTimeout(flushAddress, 350);
    }
    results.textContent = '';
    hits = [];
    markWords(null);
    if (!on) {
      results.hidden = true;
      countLine.textContent = tooShort ? WORDS.short : '';
      tell(countLine.textContent);
      countParts(null);
      announce();
      return;
    }
    var perScope = {};
    var exact = fold(state.q.replace(/["“”„‟«»]/g, '')).replace(/\s+/g, ' ').trim();
    /* Results that hold every word in their own title or text come before those found only through their place (a row,
       a question, a column); among them, those that hold the words side by side, in the order typed, come first, in a
       title before in the text; the part with the best result leads the list. */
    var phrase = phraseOf(terms);
    index().forEach(function (u, i) {
      if (state.statuses.length && state.statuses.indexOf(u.status) < 0) return;
      var score = 0;
      for (var k = 0; k < terms.length; k++) {
        var w = weigh(u, terms[k]);
        if (!w) return;
        score += w;
      }
      perScope[u.scope] = (perScope[u.scope] || 0) + 1;
      if (state.scopes.length && state.scopes.indexOf(u.scope) < 0) return;
      if (exact && u.ft === exact) score += 30;
      var own = terms.every(function (t) { return ownHas(u, t); }) ? 1 : 0;
      var tier = !phrase || !own ? 0 : together(u.ft, phrase) ? 2 : together(u.fb, phrase) ? 1 : 0;
      hits.push({ unit: u, score: score, own: own, tier: tier, order: i });
    });
    var best = {};
    var rank = function (h) { return h.own * 4e6 + h.tier * 1e6 + h.score; };
    hits.forEach(function (h) { best[h.unit.scope] = Math.max(best[h.unit.scope] || 0, rank(h)); });
    hits.sort(function (a, b) {
      return best[b.unit.scope] - best[a.unit.scope] || SCOPES.indexOf(a.unit.scope) - SCOPES.indexOf(b.unit.scope) ||
             b.own - a.own || b.tier - a.tier || b.score - a.score || a.order - b.order;
    });
    countParts(perScope);
    countLine.textContent = hits.length === 0 ? WORDS.none : hits.length === 1 ? WORDS.one : WORDS.many.replace('{n}', hits.length);
    tell(countLine.textContent);
    results.hidden = hits.length === 0;
    var marks = marksOf(terms);
    var shown = hits.slice(0, limit);
    var inPart = {};
    hits.forEach(function (h) { inPart[h.unit.scope] = (inPart[h.unit.scope] || 0) + 1; });
    var current = null;
    var list = null;
    shown.forEach(function (h, n) {
      var u = h.unit;
      if (u.scope !== current) {
        current = u.scope;
        var g = element('div', 'find-group');
        g.appendChild(element('p', 'find-group-head', scopeLabel(u.scope) + ' · ' + inPart[u.scope]));
        list = element('ol', 'find-list');
        list.setAttribute('aria-label', scopeLabel(u.scope));
        g.appendChild(list);
        results.appendChild(g);
      }
      var li = element('li', 'find-hit');
      var a = element('a', 'find-link');
      var anchor = u.el.id ? u.el : u.el.parentNode.closest('[id]');
      a.href = '#' + (anchor ? anchor.id : '');
      a.setAttribute('data-hit', String(n));
      /* A term found only in a formula is named, since no highlighted word can show it. */
      var plain = textOf(u.el, u.skip, true);
      var inFormula = terms.some(function (t) { return !inWords(u, t, plain); });
      var parts = [];
      if (u.statusLabel) parts.push(element('span', null, u.statusLabel));
      if (u.contextEl || u.context) {
        var c = u.contextEl ? inlineCopy(u.contextEl) : element('span', null, u.context);
        if (u.contextLead) c.insertBefore(doc.createTextNode(u.contextLead), c.firstChild);
        parts.push(c);
      }
      if (inFormula) parts.push(element('span', 'find-formula', WORDS.formula));
      var ids = 'find-hit-' + n;
      if (parts.length) {
        var w = element('span', 'find-where');
        w.id = ids + '-where';
        if (u.mark) w.appendChild(u.mark.cloneNode(true));
        var inner = element('span');
        parts.forEach(function (p, k) { if (k) inner.appendChild(doc.createTextNode(' · ')); inner.appendChild(p); });
        w.appendChild(highlight(inner, marks));
        a.appendChild(w);
      }
      var t = inlineCopy(u.titleEl);
      t.className = 'find-title';
      t.id = ids + '-title';
      if (!u.titleEl) t.textContent = u.title || scopeLabel(u.scope);
      a.appendChild(u.quiet ? t : highlight(t, marks));
      var snip = u.el === u.titleEl ? null : snippetOf(u, marks);
      if (snip) { snip.id = ids + '-text'; a.appendChild(snip); a.setAttribute('aria-describedby', snip.id); }
      /* The result is named by its title and its place; the words around the match describe it. */
      a.setAttribute('aria-labelledby', t.id + (parts.length ? ' ' + ids + '-where' : ''));
      li.appendChild(a);
      list.appendChild(li);
    });
    if (hits.length > shown.length) {
      var more = element('button', 'link-btn find-more', fill(WORDS.more, { k: Math.min(STEP, hits.length - shown.length), n: hits.length }));
      more.type = 'button';
      results.appendChild(more);
    }
    announce();
  }
  function go(h, link) {
    if (!h) return;
    flushAddress(); /* the entry being left keeps the search that led away from it */
    returnTo = null;
    leave(link || null);
    navigateTo(h.unit.el, marksOf(parseQuery(state.q)));
  }
  /* Going to an element of the page: the address names it (a new history entry, unless it already does), then every
     disclosure around it opens, so that what opens belongs to the new entry; the view moves to it (to its first
     highlighted word when that lies far down a long element) and focus moves to it. */
  function navigateTo(el, marks) {
    var anchor = el.id ? el : (el.parentNode && el.parentNode.closest('[id]'));
    if (anchor) {
      if (location.hash === '#' + anchor.id) setHash(anchor.id, false);
      else if (anchor === el) location.hash = el.id;
      else setHash(anchor.id, true);
    }
    if (!shared(el)) {
      /* A component's own element: the component shows it (qh:reveal); the page only scrolls to it if it does not. */
      var shown = true;
      try { shown = !el.dispatchEvent(new CustomEvent('qh:reveal', { bubbles: true, cancelable: true, detail: { id: el.id } })); } catch (e) { shown = false; }
      if (!shown) requestAnimationFrame(function () { el.scrollIntoView({ block: 'start', behavior: smooth() }); focusQuietly(el); });
      return;
    }
    openAround(el);
    markRevealed(el);
    var first = markWords(el, marks);
    requestAnimationFrame(function () {
      var to = el;
      var block = 'start';
      if (first && first.getBoundingClientRect) {
        var r = first.getBoundingClientRect();
        var box = el.getBoundingClientRect();
        if (r.top - box.top > window.innerHeight * 0.6 && first.startContainer.parentElement) { to = first.startContainer.parentElement; block = 'center'; }
      }
      to.scrollIntoView({ block: block, behavior: smooth() });
      focusQuietly(el);
    });
  }

  function focusSearch(fromKey) {
    if (!input) return;
    var a = doc.activeElement;
    if (fromKey && a && a !== input && a !== doc.body && a !== main && !(find && find.contains(a))) returnTo = a;
    facets.hidden = false;
    try { input.focus({ preventScroll: true }); } catch (e) { input.focus(); }
    find.scrollIntoView({ block: 'start', behavior: smooth() });
  }

  if (!READER) build();
  if (input) {
    doc.addEventListener('keydown', function (event) {
      var altGraph = event.getModifierState && event.getModifierState('AltGraph');
      if (event.key !== '/' || event.metaKey || ((event.ctrlKey || event.altKey) && !altGraph) || event.defaultPrevented) return;
      var t = origin(event);
      if (t && (t.isContentEditable || /^(input|textarea|select)$/i.test(t.localName))) return;
      if (!shared(event.target)) return;
      event.preventDefault();
      focusSearch(true);
    });
    hooked('data-find-open').forEach(function (b) { b.addEventListener('click', function (event) { event.preventDefault(); focusSearch(); }); });
    window.addEventListener('load', indexWhenIdle);
    /* The placeholder names what can be searched; a field too narrow to show it whole (a phone) gets the short one.
       Measured once the page has loaded and when the window changes, never at start-up. */
    var fitPlaceholder = function () {
      var room = input.clientWidth;
      if (!room) return;
      var cs = window.getComputedStyle(input);
      room -= (parseFloat(cs.paddingLeft) || 0) + (parseFloat(cs.paddingRight) || 0);
      var em = parseFloat(cs.fontSize) || 16;
      input.placeholder = WORDS.placeholder.length * em * 0.5 <= room ? WORDS.placeholder : WORDS.placeholderShort;
    };
    var fitTimer = null;
    window.addEventListener('load', fitPlaceholder);
    window.addEventListener('resize', function () { clearTimeout(fitTimer); fitTimer = setTimeout(fitPlaceholder, 150); });
  }

  /* The tally counts every statement on the page, so its links list every statement of that status on the page, as a
     new entry in the history (Back returns to the page as it was). Without the search (or with a modifier key) the
     link keeps its own target. */
  tallyLinks.forEach(function (a) {
    a.addEventListener('click', function (event) {
      if (!plainClick(event)) return;
      if (!input) { setFilters([a.getAttribute('data-filter')]); return; }
      event.preventDefault();
      flushAddress();
      leave(a);
      var params = readParams() || new URLSearchParams();
      var pageParts = SCOPES.filter(function (id) { var s = doc.getElementById(id); return !s || shared(s); });
      var scopes = pageParts.length < SCOPES.length ? pageParts : [];
      params.delete('q');
      if (scopes.length) params.set('in', scopes.join(',')); else params.delete('in');
      params.set('status', a.getAttribute('data-filter'));
      pushAddress(location.pathname + '?' + params.toString());
      setState({ q: '', scopes: scopes, statuses: [a.getAttribute('data-filter')] }, false);
      focusSearch();
    });
  });

  /* A formula that is wider than its box scrolls inside it; such a box takes keyboard focus so it can be scrolled
     with the arrow keys. Boxes inside links, buttons and summaries are left alone (they cannot hold a focus stop).
     Each box is measured when it comes near the screen, so that start-up does not lay out the whole page. */
  function measure(box) {
    if (box.closest('a, button, summary, .find, #card')) return;
    var wide = box.scrollWidth > box.clientWidth + 1;
    if (wide && !box.hasAttribute('tabindex')) { box.setAttribute('tabindex', '0'); box.setAttribute('data-scroll-focus', ''); }
    else if (!wide && box.hasAttribute('data-scroll-focus')) { box.removeAttribute('tabindex'); box.removeAttribute('data-scroll-focus'); }
    watchEdges(box, wide);
  }
  var boxes = byClass('math-display', main).concat(byClass('math-long', main));
  var nearBoxes = null;
  if ('IntersectionObserver' in window) {
    nearBoxes = new Set();
    var watcher = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { nearBoxes.add(e.target); measure(e.target); } else nearBoxes.delete(e.target);
      });
    }, { rootMargin: '400px 0px' });
    boxes.forEach(function (b) { watcher.observe(b); });
  }
  function measureNear() { (nearBoxes ? Array.from(nearBoxes) : boxes).forEach(measure); }
  var measureTimer = null;
  function measureSoon() { clearTimeout(measureTimer); measureTimer = setTimeout(measureNear, 150); }
  window.addEventListener('resize', measureSoon);
  if (!nearBoxes) { doc.addEventListener('toggle', measureSoon, true); requestAnimationFrame(measureNear); }
  try { if (doc.fonts && doc.fonts.ready) doc.fonts.ready.then(measureNear); } catch (e) { /* no font loading API */ }

  /* Disclosures of each history entry: which are open is kept in that entry's state while the reader stays, and is
     restored when the reader comes back to it (Back, Forward, reload). */
  function disclosureKey(d) { /* its id, else the first id inside it, else its place under the nearest id */
    if (d.id) return d.id;
    var inner = d.querySelector('[id]');
    if (inner) return 'in:' + inner.id;
    var host = d.parentElement && d.parentElement.closest('[id]');
    return host ? host.id + ':' + (d.className || 'details') : null;
  }
  function openList() { return disclosures.filter(function (d) { return d.open; }).map(disclosureKey).filter(Boolean); }
  function restoreOpen(list) {
    if (!Array.isArray(list)) return;
    var want = {};
    list.forEach(function (k) { want[k] = true; });
    disclosures.forEach(function (d) { var k = disclosureKey(d); if (k) d.open = !!want[k]; });
  }
  var openTimer = null;
  doc.addEventListener('toggle', function (event) {
    var d = event.target;
    if (!d || d.localName !== 'details' || !shared(d)) return;
    clearTimeout(openTimer);
    openTimer = setTimeout(function () { if (!printed) replaceAddress(location.href, { open: openList() }); }, 120);
  }, true);
  /* Before the reader leaves an entry: its open disclosures, and the control that focus should return to. */
  function leave(from) {
    clearTimeout(openTimer);
    var patch = { open: openList() };
    var at = locator(from);
    if (at) patch.back = at;
    replaceAddress(location.href, patch);
  }

  /* The reader's place, kept on this device: the part at the top of the screen when scrolling stops. A later visit
     that names no address offers to continue there. */
  var PLACE = 'qh-place';
  var PLACES = '.statement[id], .question[id], .failure[id], .open-group[id], .gloss[id], .col-def[id], .cell-line[id], ' +
               '.key-item[id], details.row[id], section.section[id], #programme';
  function placeNow() {
    if (!main || typeof doc.elementFromPoint !== 'function') return null;
    var bar = doc.querySelector('.bar');
    var y = Math.max(0, bar ? bar.getBoundingClientRect().bottom : 0) + 24;
    var el = doc.elementFromPoint(window.innerWidth / 2, y);
    var unit = el && el.closest ? el.closest(PLACES) : null;
    return unit && shared(unit) && main.contains(unit) ? unit : null;
  }
  function savePlace() {
    if (READER) return;
    var u = placeNow();
    if (u) keep(PLACE, JSON.stringify({ id: u.id, title: placeTitle(u), at: Date.now() }));
  }
  var placeTimer = null;
  window.addEventListener('scroll', function () { clearTimeout(placeTimer); placeTimer = setTimeout(savePlace, 700); }, { passive: true });
  window.addEventListener('pagehide', function () { flushAddress(); savePlace(); });
  function placeTitle(el) {
    if (el.matches('.cell-line')) {
      var row = el.closest('details.row');
      return textOf(row && row.querySelector('.row-name')) + ', ' + textOf(el.querySelector('.cell-col'));
    }
    var t = el.querySelector('.statement-title, h3, .claim-text, dt, .row-name, h2');
    var s = textOf(t || el);
    return s.length > 90 ? s.slice(0, 88) + '…' : s;
  }
  function navigationType() {
    try { var n = performance.getEntriesByType('navigation')[0]; return n ? n.type : 'navigate'; } catch (e) { return 'navigate'; }
  }
  function offerPlace() {
    var raw = stored(PLACE);
    if (!raw) return;
    var at = null;
    try { at = JSON.parse(raw); } catch (e) { at = null; }
    var el = at && typeof at.id === 'string' && at.id !== 'programme' ? doc.getElementById(at.id) : null;
    if (!el || !shared(el) || !main.contains(el)) return;
    if (typeof at.title === 'string' && at.title !== placeTitle(el)) return; /* the address names something else now */
    notice('resume', fill(WORDS.resume, { title: '“' + placeTitle(el) + '”' }), [
      [WORDS.resumeGo, function () { dismiss(); leave(null); navigateTo(el, null); }]
    ], function () { keep(PLACE, null); });
  }

  /* Notices at the top of the page: an address the page does not have, and the place a reader stopped. The notice
     area is a live region present from the start and empty when there is nothing to say, so that its words are
     announced when they appear. */
  var noticeBox = null;
  var noticeKind = null;
  if (main && !READER) {
    noticeBox = element('div', 'qh-notice');
    noticeBox.setAttribute('role', 'status');
    main.insertBefore(noticeBox, main.firstChild);
  }
  function notice(kind, text, actions, onClose) {
    if (!noticeBox) return;
    dismiss();
    noticeKind = kind;
    noticeBox.setAttribute('data-notice', kind);
    var p = element('p');
    p.appendChild(element('span', null, text));
    actions.concat([[WORDS.close, function () { dismiss(); if (onClose) onClose(); }]]).forEach(function (pair) {
      var b = element('button', 'link-btn', pair[0]);
      b.type = 'button';
      b.addEventListener('click', pair[1]);
      p.appendChild(doc.createTextNode(' '));
      p.appendChild(b);
    });
    noticeBox.appendChild(p);
  }
  function dismiss() {
    if (!noticeBox || !noticeKind) return;
    var hadFocus = noticeBox.contains(doc.activeElement);
    noticeBox.textContent = '';
    noticeBox.removeAttribute('data-notice');
    noticeKind = null;
    if (hadFocus && main) focusQuietly(main);
  }
  function unknownAddress(id, readable, arrival) {
    var claim = null;
    try { claim = new CustomEvent('qh:unknown-anchor', { cancelable: true, detail: { id: id } }); } catch (e) { claim = null; }
    if (claim && !doc.dispatchEvent(claim)) return; /* a component has this address */
    var words = readable ? id.replace(/^(s|q|f|row|open|col|term|defn)-/, '').replace(/-h$/, '').replace(/-\d+$/, '')
      .replace(/[-_]+/g, ' ').trim() : '';
    var actions = [];
    if (input && /[a-z]{2}/i.test(words)) {
      actions.push([fill(WORDS.searchFor, { words: words }), function () {
        dismiss();
        setState({ q: words, scopes: [], statuses: [] }, true);
        focusSearch();
      }]);
    }
    notice('unknown', fill(WORDS.unknown, { address: '#' + id }), actions);
    /* Reached during a visit (a link, an edited address), the notice is brought into view with focus on its words;
       Back returns to where the reader was. */
    var said = !arrival && noticeKind === 'unknown' ? noticeBox.querySelector('p > span') : null;
    if (said) {
      focusQuietly(said);
      try { said.scrollIntoView({ block: 'center' }); } catch (e) { said.scrollIntoView(); }
    }
  }

  /* The state of the page, for a component that follows it. */
  function announce() {
    try {
      doc.dispatchEvent(new CustomEvent('qh:state', { detail: {
        q: state ? state.q.trim() : '', scopes: state ? state.scopes.slice() : [], statuses: state ? state.statuses.slice() : [],
        show: shownStatuses(), hash: hashId()
      } }));
    } catch (e) { /* no CustomEvent */ }
  }
  doc.addEventListener('qh:navigate', function (event) {
    if (READER) return;
    var id = event.detail && event.detail.id;
    var el = typeof id === 'string' && id ? doc.getElementById(id) : null;
    if (!el || !shared(el)) return; /* not an anchor of the page */
    event.preventDefault();
    flushAddress();
    leave(event.target);
    navigateTo(el, null);
  });
  doc.addEventListener('qh:content-changed', function () {
    mounts = all(ISOLATED);
    isolating = mounts.length > 0;
    units = null;
    pending = null;
    if (input && active()) run(false); else indexWhenIdle();
  });

  /* A link inside the page: the entry it leaves keeps the reader's search, open disclosures and focus; a link to the
     address already shown (which the browser does not treat as a change) still opens what conceals its target. */
  doc.addEventListener('click', function (event) {
    if (!plainClick(event)) return;
    var a = event.target.closest && event.target.closest('a[href^="#"]');
    if (!a) return;
    flushAddress();
    if (!shared(a) || triggerOf(a)) return; /* a term served as a link opens its card instead */
    var raw = a.getAttribute('href').slice(1);
    if (!raw) return;
    var id = raw;
    try { id = decodeURIComponent(raw); } catch (e) { id = raw; }
    if (id === hashId()) {
      var t = doc.getElementById(id);
      if (t) { openAround(t); markRevealed(t); }
      return;
    }
    leave(a.closest('#card') && owner ? owner : a);
  }, true);

  /* Arrival, and Back and Forward: the address, then the disclosures of the entry, then its target and focus. */
  function same(a, b) { return a.slice().sort().join(',') === b.slice().sort().join(','); }
  function fromURL(arrival) {
    var params = readParams();
    var known = filters.map(function (f) { return f.getAttribute('data-filter'); });
    var asked = { show: listParam(params, 'show'), 'in': listParam(params, 'in'), status: listParam(params, 'status') };
    var allowed = { show: known, 'in': SCOPES, status: input ? statusValues : [] };
    var kept = {};
    var dropped = [];
    Object.keys(asked).forEach(function (k) {
      kept[k] = asked[k].filter(function (v) { return allowed[k].indexOf(v) >= 0; });
      asked[k].forEach(function (v) { if (allowed[k].indexOf(v) < 0) dropped.push('“' + v + '”'); });
    });
    if (filters.length && !same(kept.show, shownStatuses())) {
      filters.forEach(function (f) { f.setAttribute('aria-pressed', kept.show.indexOf(f.getAttribute('data-filter')) >= 0 ? 'true' : 'false'); });
      applyFilter(false);
    }
    /* Values the page does not have are named once and dropped from the address, so that it shows what the page shows. */
    if (arrival && dropped.length) {
      writeParams({ show: kept.show.join(','), 'in': kept['in'].join(','), status: kept.status.join(',') });
      notice('ask', fill(WORDS.unknownAsk, { values: dropped.join(', ') }), []);
    }
    if (input) {
      var next = { q: (params && params.get('q')) || '', scopes: kept['in'], statuses: kept.status };
      if (next.q === state.q.trim() && same(next.scopes, state.scopes) && same(next.statuses, state.statuses)) return;
      setState(next);
      if (arrival && !location.hash && active()) requestAnimationFrame(function () { find.scrollIntoView({ block: 'start' }); });
    }
  }
  /* The address the search gives to a block of a part of another shape exists once the search's units are built: such
     an address (a part's id, then words) is looked up again after building them, before it is called unknown. */
  function findAddress(id) {
    var el = doc.getElementById(id);
    if (el || !input || !partSections.some(function (s) { return id.indexOf(s.id + '-') === 0; })) return el;
    index();
    return doc.getElementById(id);
  }
  function openTarget(arrival) {
    if (noticeKind === 'unknown' || (!arrival && noticeKind)) dismiss();
    var raw = location.hash.slice(1);
    if (!raw) { announce(); return; }
    var id = raw;
    var readable = true;
    try { id = decodeURIComponent(raw); } catch (e) { readable = false; }
    if ((id === 'find-q' || id === 'find-results') && input) { focusSearch(); announce(); return; }
    var target = readable ? findAddress(id) : null;
    if (target && !shared(target)) { announce(); return; } /* the component's own address */
    var opened = target ? openAround(target) : [];
    if (!target || target.closest('[hidden]')) { unknownAddress(id, readable, arrival); announce(); return; }
    markRevealed(target);
    if (opened.length || (arrival && given[target.id])) requestAnimationFrame(function () { target.scrollIntoView(); });
    announce();
  }
  window.addEventListener('popstate', function (event) {
    if (READER) {
      var kept = qhOf(event.state);
      if (refilter) refilter();
      if (kept.open) restoreOpen(kept.open);
      return;
    }
    /* A search typed just before Back belongs to the entry that was left, not to this one. */
    clearTimeout(addressTimer);
    pendingAddress = null;
    if (noticeKind && noticeKind !== 'unknown') dismiss();
    if (refilter) refilter();
    var qh = qhOf(event.state);
    fromURL(false);
    if (qh.open) restoreOpen(qh.open);
    /* The element the address names is shown here, not only on hashchange, which may come after the next frame. */
    var id = hashId();
    var to = id && id !== 'find-q' && id !== 'find-results' ? findAddress(id) : null;
    if (to && !shared(to)) to = null;
    if (to) openAround(to);
    var back = qh.back;
    if (back) {
      var want = back.all ? Infinity : typeof back.limit === 'number' ? back.limit : 0;
      if (want > limit && input && active()) { limit = want; run(false); }
      requestAnimationFrame(function () {
        var el = located(back);
        if (el && el.isConnected && reachable(el)) focusQuietly(el);
      });
    } else if (to) {
      /* An entry that keeps no place to return to (one reached by Forward, a link the browser follows, or an address
         typed in) puts focus on the element its address names. */
      requestAnimationFrame(function () { if (to.isConnected && reachable(to)) focusQuietly(to); });
    }
  });
  window.addEventListener('hashchange', function () { if (!READER) openTarget(false); });

  var arrivalState = qhOf(history.state);
  try {
    fromURL(true);
  } finally {
    if (arrivalState.open && navigationType() !== 'navigate') restoreOpen(arrivalState.open);
    if (!READER) {
      openTarget(true);
      if (!location.hash && !active() && !shownStatuses().length && navigationType() === 'navigate') offerPlace();
    }
  }
})();
