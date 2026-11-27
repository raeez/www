/* The reader of the monograph.

   Without this script the page is the whole book in reading order, and its contents links work. With it, the page
   shows one place at a time: the title page with the contents, one chapter, or one part of the reference (the
   glossary, the atlas). The places not shown carry hidden="until-found", so the browser's own find still reaches them,
   and the reader follows it there. The script adds a reading bar (where the reader is, the previous and next chapter,
   the contents and the search), the contents as a panel, a reminder for each cross-reference that keeps the reader's
   place, and a search over the chapters and the reference in which the chapters come first.

   Every change of place is an entry in the browser's history, and the entry being left keeps where the reader was and
   which control had focus, so that Back and Forward return to both. A search that led to a result is kept in the entry
   it was made in: Back reopens it with focus on the result chosen.

   It reads the page as served: [data-reader] on the main element, [data-reader-front], [data-reader-toc],
   article[data-chapter] chapters, section[data-section] sections, environments ([data-env], [data-result], div[data-term]),
   figure[data-figure] figures and diagrams, [data-reference] parts and a[href] cross-references (a[data-ref] names one
   explicitly). A component may give its own elements data-chapter or data-section values; only an article is a chapter
   and only a section element a section. Components such as the atlas keep their own state and
   speak to the page through events: qh:navigate (asks the page to show a place), qh:unknown-anchor (claims an
   address), qh:content-changed (new words to search); the page tells them of a change of place with qh:chapter and
   qh:state, and asks one to show a place of its own with qh:reveal.

   It adds no words of its own beyond the interface words below, which the page may replace (data-label-<key> on
   [data-reader]), and no styles: what it shows is marked by classes and attributes, and two measures are given as
   custom properties (--reader-bar-h on the root, --peek-x and --peek-y on the reminder). Nothing is sent anywhere; the
   reader's place is kept on this device only. */
(function () {
  'use strict';
  var doc = document;
  var main = doc.querySelector('[data-reader]');
  if (!main || main.hasAttribute('data-reader-on')) return;
  main.setAttribute('data-reader-on', '');
  var root = doc.documentElement;

  /* ------------------------------------------------------------------ small tools */

  function all(selector, context) { return Array.prototype.slice.call((context || doc).querySelectorAll(selector)); }
  function media(query) { return !!(window.matchMedia && window.matchMedia(query).matches); }
  function plainClick(event) { return !(event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey); }
  function element(tag, className, text) {
    var n = doc.createElement(tag);
    if (className) n.className = className;
    if (text != null) n.textContent = text;
    return n;
  }
  function decode(s) { try { return decodeURIComponent(s); } catch (e) { return s; } }
  function stored(key) { try { return window.localStorage.getItem(key); } catch (e) { return null; } }
  function keep(key, value) {
    try {
      if (value == null) window.localStorage.removeItem(key); else window.localStorage.setItem(key, value);
    } catch (e) { /* storage refused: the place is simply not kept */ }
  }
  function sessionGet(key) { try { return window.sessionStorage.getItem(key); } catch (e) { return null; } }
  function sessionSet(key, value) {
    try {
      if (value == null) window.sessionStorage.removeItem(key); else window.sessionStorage.setItem(key, value);
    } catch (e) { /* refused */ }
  }
  function fire(target, name, detail, cancelable) {
    var event;
    try { event = new CustomEvent(name, { bubbles: true, cancelable: !!cancelable, detail: detail }); } catch (e) { return true; }
    return target.dispatchEvent(event);
  }
  function editable(el) {
    return !!(el && el.closest && el.closest('input, textarea, select, [contenteditable=""], [contenteditable="true"]'));
  }
  function later(fn) { (window.requestAnimationFrame || function (f) { return setTimeout(f, 16); })(fn); }

  /* The interface words. The page may give its own for any key: data-label-<key> on [data-reader]. */
  var WORDS = {
    'reading': 'Reading',
    'front': 'Title page',
    'contents': 'Contents',
    'part': 'Part {n}',
    'chapter': 'Chapter {n}',
    'chapter-of': 'Chapter {n} of {total}',
    'reference': 'Reference',
    'previous': 'Previous',
    'next': 'Next',
    'begin': 'Begin',
    'return': 'Back to the text',
    'previous-chapter': 'Previous chapter: {title}',
    'next-chapter': 'Next chapter: {title}',
    'begin-chapter': 'Begin with chapter {n}: {title}',
    'return-to': 'Back to the text: {title}',
    'search': 'Search',
    'search-label': 'Search the chapters and the reference',
    'search-placeholder': 'Search the book',
    'search-in': 'Search in',
    'all': 'All',
    'chapters': 'Chapters',
    'best': 'Best match',
    'none': 'No results.',
    'one': '1 result.',
    'many': '{n} results.',
    'too-short': 'Type at least two letters or digits.',
    'more-in': '{k} more in {where}',
    'in-formula': 'in a formula',
    'formula-in-source': 'Formula in source',
    'formula-as-tex': 'Formula: {tex}',
    'kind-chapter': 'Chapter',
    'kind-section': 'Section',
    'kind-text': 'Passage',
    'kind-figure': 'Figure',
    'kind-gloss': 'Glossary entry',
    'kind-unit': 'Atlas entry',
    'kind-heading': 'Heading',
    'kind-definition': 'Definition', 'kind-theorem': 'Theorem', 'kind-lemma': 'Lemma',
    'kind-proposition': 'Proposition', 'kind-corollary': 'Corollary', 'kind-result': 'Result',
    'kind-claim': 'Claim', 'kind-consequence': 'Consequence', 'kind-example': 'Example',
    'kind-counterexample': 'Counterexample', 'kind-conjecture': 'Conjecture', 'kind-heuristic': 'Heuristic',
    'kind-open-problem': 'Open problem', 'kind-open-question': 'Open question', 'kind-proof': 'Proof',
    'kind-proof-sketch': 'Proof sketch', 'kind-construction': 'Construction', 'kind-remark': 'Remark',
    'kind-notation': 'Notation', 'kind-convention': 'Convention', 'kind-introduction': 'Introduction',
    'close': 'Close',
    'go-to': 'Go to {where}',
    'define-kind': 'Definition',
    'define-go': 'Read the definition',
    'define-go-here': 'Show the definition on this screen',
    'define-reference': 'Reference',
    'define-equation': 'Equation {n}',
    'define-text': 'Definition in the text',
    'define-return': 'Back to “{term}”',
    'proof-skip': 'Skip to the end of the proof',
    'unknown': 'This book has no place with the address {address}.',
    'changed-address': 'This saved address names a changed passage. Its location is available below.',
    'ambiguous-address': 'This saved address can refer to different passages. Choose from the available locations.',
    'search-for': 'Search for “{words}”',
    'resume': 'You were reading {title}.',
    'resume-go': 'Continue reading',
    'route': '{route} route, step {i} of {n}',
    'theme': 'Switch between light and dark',
    'index-failed': 'The parts of the reference in other pages could not be searched from here.',
    'leave-route': 'Leave this route'
  };
  function word(key) {
    var v = main.getAttribute('data-label-' + key);
    return v != null && v !== '' ? v : WORDS[key];
  }
  function fill(text, values) {
    return String(text).replace(/\{(\w+)\}/g, function (m, k) { return values[k] == null ? '' : String(values[k]); });
  }
  function roman(n) {
    var out = '';
    [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'],
     [5, 'V'], [4, 'IV'], [1, 'I']].forEach(function (p) { while (n >= p[0]) { out += p[1]; n -= p[0]; } });
    return out;
  }

  /* Reader-visible text of an element, formulae given by their symbols (or left out). Parts matching skip inside it are
     left out; the element itself is never skipped. */
  var BLOCK = /^(p|div|li|dt|dd|h[1-6]|article|section|header|footer|aside|nav|ul|ol|dl|table|tr|td|th|figure|figcaption|blockquote|pre|summary|details)$/;
  function textOf(el, skip, noMath) {
    if (!el) return '';
    var out = [];
    (function walk(n, top) {
      if (n.nodeType === 3) { out.push(n.nodeValue); return; }
      if (n.nodeType !== 1) return;
      if (!top && skip && n.matches(skip)) return;
      if (!top && n.hasAttribute('data-reader-skip')) return; /* the reader's own controls are not the book's words */
      var tag = n.localName;
      if (tag === 'svg' || tag === 'annotation' || tag === 'script' || tag === 'style' || tag === 'template' || (noMath && tag === 'math')) return;
      for (var c = n.firstChild; c; c = c.nextSibling) walk(c, false);
      if (BLOCK.test(tag)) out.push(' ');
    })(el, true);
    return out.join('').replace(/\s+/g, ' ').trim();
  }
  /* The TeX of the formulae in an element (from their annotations), leaving out those inside parts matching skip. */
  function texOf(el, skip) {
    if (!el) return '';
    return all('annotation', el).filter(function (a) {
      if (!skip) return true;
      var s = a.parentNode && a.parentNode.closest(skip);
      return !s || s === el || !el.contains(s);
    }).map(function (a) { return a.textContent; }).join(' ');
  }
  /* A copy for showing elsewhere: formulae and links kept, ids, controls and interactive figures removed. */
  function cleanCopy(node, tag) {
    var copy = node.cloneNode(true);
    all('script, style, template, button, input, select, textarea, figure[data-figure], [hidden], .anchor-sr, [data-reader-skip]', copy)
      .forEach(function (n) { if (n.parentNode) n.parentNode.removeChild(n); });
    all('[data-definition-near]', copy).forEach(function (n) { n.removeAttribute('data-definition-near'); });
    copy.removeAttribute('data-definition-near');
    all('[id]', copy).forEach(function (n) { n.removeAttribute('id'); });
    all('[tabindex]', copy).forEach(function (n) { n.removeAttribute('tabindex'); });
    all('[aria-labelledby], [aria-describedby], [aria-controls]', copy).forEach(function (n) {
      n.removeAttribute('aria-labelledby'); n.removeAttribute('aria-describedby'); n.removeAttribute('aria-controls');
    });
    all('details', copy).forEach(function (d) { d.open = true; });
    copy.removeAttribute('id');
    copy.removeAttribute('tabindex');
    copy.removeAttribute('data-current');
    copy.removeAttribute('data-revealed');
    if (tag) {
      var wrap = element(tag, copy.className || null);
      while (copy.firstChild) wrap.appendChild(copy.firstChild);
      return wrap;
    }
    return copy;
  }
  /* Between two parts of a copied heading that touch (a number set as an element, then the title), a space. */
  function spaceParts(node) {
    for (var k = node.firstChild; k && k.nextSibling; k = k.nextSibling) {
      if (k.nodeType === 1 && k.nextSibling.nodeType === 1) node.insertBefore(doc.createTextNode(' '), k.nextSibling);
    }
    return node;
  }
  /* A copy of a title for one line: formulae kept, links and controls unwrapped or removed. */
  function inlineCopy(el) {
    var span = doc.createElement('span');
    if (!el) return span;
    var copy = el.cloneNode(true);
    all('svg, .anchor-sr, button, script, style', copy).forEach(function (n) { if (n.parentNode) n.parentNode.removeChild(n); });
    all('a', copy).forEach(function (n) {
      while (n.firstChild) n.parentNode.insertBefore(n.firstChild, n);
      n.parentNode.removeChild(n);
    });
    all('[id]', copy).forEach(function (n) { n.removeAttribute('id'); });
    while (copy.firstChild) span.appendChild(copy.firstChild);
    return spaceParts(span);
  }

  /* ------------------------------------------------------------------ the book as served */

  var front = main.querySelector('[data-reader-front]');
  var toc = main.querySelector('[data-reader-toc]');
  var CHAPTER = 'article[data-chapter]';
  var SECTION = 'section[data-section]';
  var REFERENCE = 'section[data-reference], div[data-reference], article[data-reference]';
  var chapters = all(CHAPTER, main).filter(function (c) { return !!c.id && !(c.parentNode && c.parentNode.closest && c.parentNode.closest(CHAPTER)); });
  var references = all(REFERENCE, main).filter(function (r) { return !!r.id && !r.closest(CHAPTER) && !(r.parentNode && r.parentNode.closest && r.parentNode.closest(REFERENCE)); });
  function isChapter(el) { return chapters.indexOf(el) >= 0; }
  function isPart(el) { return references.indexOf(el) >= 0; }
  function isSection(el) { return !!el && el.nodeType === 1 && el.matches(SECTION); }
  var places = chapters.concat(references);
  var partIds = [];
  chapters.forEach(function (c) {
    var p = c.getAttribute('data-part');
    if (p && partIds.indexOf(p) < 0) partIds.push(p);
  });
  var bookTitle = front && front.querySelector('h1') ? textOf(front.querySelector('h1')) : '';
  /* The number of chapters in the book, which the page may give when it serves only some of them. */
  var chapterTotal = +(main.getAttribute('data-chapter-count') || 0) || chapters.length;
  var hoverCapable = media('(hover: hover) and (pointer: fine)');
  /* A place not shown waits hidden until found, where the browser can find text in it; elsewhere it is simply hidden. */
  var UNTIL = 'onbeforematch' in doc.documentElement ? 'until-found' : '';

  function chapterHeading(c) { return (c && (doc.getElementById(c.id + '-h') || c.querySelector('h2, h1'))) || null; }
  function sectionHeading(s) {
    if (!s) return null;
    if (/^h[1-6]$/.test(s.localName)) return s;
    var h = doc.getElementById(s.id + '-h');
    if (h && s.contains(h)) return h;
    for (var c = s.firstElementChild; c; c = c.nextElementSibling) if (/^h[2-6]$/.test(c.localName)) return c;
    return s.querySelector('h3, h4, h5, h6');
  }
  function referenceHeading(r) {
    var by = r && r.getAttribute('aria-labelledby');
    return (by && doc.getElementById(by.split(/\s+/)[0])) || (r && r.querySelector('h2, h1')) || null;
  }
  function chapterNumber(c) { return c.getAttribute('data-number') || String(chapters.indexOf(c) + 1); }
  /* A heading's words: the text of its parts with a space where one part ends and the next begins, so that a number
     the page sets as an element of its own ("1.1") stays apart from the title it numbers. */
  function headingText(h) {
    if (!h) return '';
    var out = [];
    for (var k = h.firstChild; k; k = k.nextSibling) {
      if (k.nodeType === 3) out.push(k.nodeValue);
      else if (k.nodeType === 1) out.push(' ' + textOf(k) + ' ');
    }
    return out.join('').replace(/\s+/g, ' ').trim();
  }
  /* A chapter's title without its number: the heading's parts after a first element that holds only the chapter's
     number (the page may set it apart: "1" beside "Boundary observables and reconstruction"). */
  function chapterTitleParts(c) {
    var h = chapterHeading(c);
    if (!h) return { h: null, nodes: [], dropped: false };
    var n = chapterNumber(c);
    var nodes = [];
    var dropped = false;
    for (var k = h.firstChild; k; k = k.nextSibling) {
      if (!dropped && k.nodeType === 1 && !nodes.some(function (x) { return x.nodeType === 1 || x.nodeValue.trim(); })) {
        var tx = textOf(k).replace(/[.:·]$/, '').trim();
        if (tx === n || tx === roman(+n) || tx === fill(word('chapter'), { n: n })) { dropped = true; continue; }
      }
      nodes.push(k);
    }
    return { h: h, nodes: nodes, dropped: dropped };
  }
  function chapterTitle(c) {
    var parts = chapterTitleParts(c);
    if (!parts.h) return '';
    if (!parts.dropped) return headingText(parts.h);
    return parts.nodes.map(function (k) { return k.nodeType === 3 ? k.nodeValue : k.nodeType === 1 ? ' ' + textOf(k) + ' ' : ''; })
      .join('').replace(/\s+/g, ' ').trim();
  }
  /* The element that holds a chapter's name alone, where the heading sets the number apart; else the heading. */
  function chapterNameEl(c) {
    var parts = chapterTitleParts(c);
    var els = parts.nodes.filter(function (k) { return k.nodeType === 1; });
    var words = parts.nodes.filter(function (k) { return k.nodeType === 3 && k.nodeValue.trim(); });
    return parts.dropped && els.length === 1 && !words.length ? els[0] : parts.h;
  }
  function chapterName(c) { return fill(word('chapter'), { n: chapterNumber(c) }) + ', ' + chapterTitle(c); }
  function placeOf(t) {
    if (!t || !main.contains(t)) return null;
    var p = t.closest(CHAPTER + ', ' + REFERENCE);
    while (p && places.indexOf(p) < 0) p = p.parentNode && p.parentNode.closest ? p.parentNode.closest(CHAPTER + ', ' + REFERENCE) : null;
    return p;
  }
  function onFront(t) { return !!t && ((front && front.contains(t)) || (toc && toc.contains(t))); }
  /* Whether an element is a place of the book this script shows (a place, inside one, or the title page). */
  function ours(t) { return !!t && t !== main && main.contains(t) && (!!placeOf(t) || onFront(t)); }
  /* Environments as the chapter renderer marks them: [data-env] with its class (definition, theorem, proof, …); a
     definition may also be served as [data-term] and any other result as [data-result]. */
  var ENV = '[data-env], div[data-term], section[data-term], div[data-result], section[data-result], aside[data-result]';
  var PROOF = '[data-env="proof"], [data-env="proof-sketch"]';
  function envKind(b) {
    return b.getAttribute('data-env') || (b.hasAttribute('data-term') ? 'definition' : 'result');
  }
  function envLabel(kind, status) {
    if (!kind || !WORDS['kind-' + kind]) return '';
    var label = word('kind-' + kind);
    if (status === 'proved') return 'Proved ' + label.toLowerCase();
    if (status === 'conditional') return 'Conditional ' + label.toLowerCase();
    if (status === 'conjecture' && kind !== 'conjecture') return 'Conjectural ' + label.toLowerCase();
    if (status === 'heuristic' && kind !== 'heuristic') return 'Heuristic ' + label.toLowerCase();
    if (status === 'open' && !/^open-/.test(kind)) return 'Open ' + label.toLowerCase();
    return label;
  }
  function envWords(kind, status) {
    return fold(envLabel(kind, status) + ' ' + (status || '').replace(/-/g, ' '));
  }
  /* The sections of a place: section[data-section] where the page wraps them, else its headings with an address. */
  function sectionMarks(place) {
    var wrapped = all(SECTION, place);
    if (wrapped.length) return wrapped;
    var own = isChapter(place) ? chapterHeading(place) : referenceHeading(place);
    return all('h2[id], h3[id], h4[id]', place).filter(function (h) { return h !== own && !h.closest(ENV + ', figure, nav, [data-reader-skip]'); });
  }
  function sectionOf(t) {
    if (!t || !t.closest) return null;
    var w = t.closest(SECTION);
    if (w) return w;
    var place = placeOf(t);
    if (!place || place.querySelector(SECTION)) return null;
    var found = null;
    sectionMarks(place).forEach(function (h) {
      if (h === t || (h.compareDocumentPosition(t) & Node.DOCUMENT_POSITION_FOLLOWING)) found = h;
    });
    return found;
  }
  function blockTitle(b) {
    if (!b) return null;
    var t = b.querySelector('[data-block-title]');
    if (t) return t;
    for (var c = b.firstElementChild; c; c = c.nextElementSibling) if (/^h[2-6]$/.test(c.localName)) return c;
    if (b.localName === 'figure') return null;
    return b.querySelector('dfn');
  }

  /* Old addresses the page maps to new ones: a JSON object {old id: new id} in script#reader-redirects. */
  var redirects = {};
  var predecessors = {};
  (function () {
    function readAddresses(id) {
      var s = doc.getElementById(id);
      if (!s) return {};
      try { return JSON.parse(s.textContent) || {}; } catch (e) { return {}; }
    }
    redirects = readAddresses('reader-redirects');
    predecessors = readAddresses('reader-predecessors');
  })();
  function predecessor(id) {
    return Object.prototype.hasOwnProperty.call(predecessors, id) ? predecessors[id] : null;
  }

  /* The book may keep parts of its reference in companion pages, loaded only when asked for. The map
     (script#reader-pages) names each page, its parts and every address in them; a companion page names the book in
     main[data-reader-book]. */
  var pagesMap = null;
  (function () {
    var s2 = doc.getElementById('reader-pages');
    if (!s2) return;
    try { pagesMap = JSON.parse(s2.textContent); } catch (e) { pagesMap = null; }
    if (!pagesMap || typeof pagesMap !== 'object' || !Array.isArray(pagesMap.pages)) pagesMap = null;
  })();
  var bookHref = main.getAttribute('data-reader-book') || (pagesMap && pagesMap.book) || '';
  var companion = main.hasAttribute('data-reader-book');
  var owners = null;
  function ownerOf(id) {
    if (!pagesMap) return null;
    if (!owners) {
      owners = {};
      pagesMap.pages.forEach(function (pg) {
        if (!pg || typeof pg.href !== 'string') return;
        (pg.parts || []).forEach(function (pt) { if (pt && pt.id) owners[pt.id] = pg.href; });
        (pg.ids || []).forEach(function (x) { owners[x] = pg.href; });
        (pg.aliases || []).forEach(function (x) { owners[x] = pg.href; });
      });
    }
    return Object.prototype.hasOwnProperty.call(owners, id) ? owners[id] : null;
  }
  /* The address in another page for an id this page does not hold: its companion page, or (from a companion page) the
     book. */
  function externalHref(id) {
    if (!id || doc.getElementById(id)) return null;
    var page = ownerOf(id);
    if (page) return page + '#' + encodeURIComponent(id);
    if (companion && bookHref) return bookHref + '#' + encodeURIComponent(id);
    return null;
  }
  function samePage(url) {
    try {
      var u = new URL(url, location.href);
      return u.origin === location.origin && u.pathname === location.pathname;
    } catch (e) { return true; }
  }
  /* A page of the book that is not this one: the book itself or a companion page named in the map. */
  function bookPage(url) {
    if (!pagesMap || samePage(url)) return false;
    var name;
    try { name = new URL(url, location.href).pathname.split('/').pop(); } catch (e) { return false; }
    if (bookHref && name === bookHref.split('/').pop()) return true;
    return pagesMap.pages.some(function (pg) { return pg && typeof pg.href === 'string' && pg.href.split('/').pop() === name; });
  }

  /* Addresses for blocks that have none: the nearest id above, then -p and the block's number under it, given in the
     same order every time, so that an address given here holds on a later visit to the same text. */
  var givenCount = {};
  function give(el) {
    if (el.id) return el.id;
    var host = el.parentNode && el.parentNode.closest ? el.parentNode.closest('[id]') : null;
    var base = host ? host.id : 'block';
    var n = givenCount[base] || 0;
    var id;
    do { n++; id = base + '-p' + n; } while (doc.getElementById(id) || Object.prototype.hasOwnProperty.call(redirects, id) || predecessor(id));
    givenCount[base] = n;
    el.id = id;
    return id;
  }
  function resolve(id) {
    if (!id) return null;
    var t = doc.getElementById(id);
    if (t) return t;
    var m = /^(.+)-p\d+$/.exec(id);
    var host = m ? doc.getElementById(m[1]) : null;
    var place = host ? placeOf(host) || (front && front.contains(host) ? front : null) : null;
    if (!place) return null;
    jobsFor(place).forEach(function (job) { job([]); }); /* the same order as the search index: the same addresses */
    return doc.getElementById(id);
  }

  /* ------------------------------------------------------------------ the reading bar */

  var bar = doc.querySelector('[data-reader-bar]');
  if (!bar) {
    bar = element('nav');
    bar.setAttribute('data-reader-bar', '');
    bar.setAttribute('aria-label', word('reading'));
    main.parentNode.insertBefore(bar, main);
  }
  bar.classList.add('reader-bar');

  var home = null;
  if (front && front.id) {
    home = element('a', 'reader-home', bookTitle || word('front'));
    home.id = 'reader-home';
    home.href = '#' + front.id;
    bar.appendChild(home);
  } else if (companion && bookHref) {
    home = element('a', 'reader-home', (pagesMap && pagesMap.title) || word('front'));
    home.id = 'reader-home';
    home.href = bookHref + '#front';
    bar.appendChild(home);
  }
  var position = element('span', 'reader-position');
  var posPart = position.appendChild(element('span', 'reader-position-part'));
  var posChapter = position.appendChild(element('span', 'reader-position-chapter'));
  var posTitle = position.appendChild(element('span', 'reader-position-title'));
  var posSection = position.appendChild(element('span', 'reader-position-section'));
  var tocButton = null;
  if (toc && toc.id) {
    /* The place, shown where the contents open: the bar's one control for where the reader is and where to go. */
    tocButton = element('button', 'reader-contents-toggle');
    tocButton.id = 'reader-contents-toggle';
    tocButton.type = 'button';
    tocButton.setAttribute('aria-expanded', 'false');
    tocButton.setAttribute('aria-controls', toc.id);
    tocButton.appendChild(element('span', 'reader-contents-word', word('contents')));
    tocButton.appendChild(position);
    bar.appendChild(tocButton);
  } else {
    bar.appendChild(position);
  }
  var routeBox = element('span', 'reader-route');
  routeBox.hidden = true;
  var routeText = routeBox.appendChild(element('span', 'reader-route-text'));
  var routeLeave = routeBox.appendChild(element('button', 'reader-route-leave', word('leave-route')));
  routeLeave.type = 'button';
  bar.appendChild(routeBox);
  /* A step says where it goes: the word ("Previous", "Next", "Begin", "Back to the text") and "Chapter 5 · title";
     its full name is its accessible name. */
  function stepLink(className, rel, arrow) {
    var a = element('a', className);
    a.id = className;
    a.rel = rel;
    a.hidden = true;
    var arrowSpan = element('span', 'reader-step-arrow', arrow);
    arrowSpan.setAttribute('aria-hidden', 'true');
    var label = element('span', 'reader-step-label');
    var title = element('span', 'reader-step-title');
    if (rel === 'prev') { a.appendChild(arrowSpan); a.appendChild(label); a.appendChild(title); }
    else { a.appendChild(label); a.appendChild(title); a.appendChild(arrowSpan); }
    bar.appendChild(a);
    return a;
  }
  var prevLink = stepLink('reader-prev', 'prev', '←');
  var nextLink = stepLink('reader-next', 'next', '→');
  var searchButton = element('button', 'reader-search-toggle', word('search'));
  searchButton.id = 'reader-search-toggle';
  searchButton.type = 'button';
  searchButton.setAttribute('aria-expanded', 'false');
  searchButton.setAttribute('aria-controls', 'reader-search');
  searchButton.setAttribute('aria-keyshortcuts', '/');
  bar.appendChild(searchButton);

  /* Light and dark: the page's own control (.theme), kept in the bar when the page serves none. It follows the system
     until the reader chooses; the choice is remembered on this device (qh-theme) and restored by the page before it is
     drawn. One press switches once, whichever other script of the page also knows the control. */
  var themeButton = null;
  if (!doc.querySelector('.theme')) {
    themeButton = element('button', 'theme reader-theme');
    themeButton.id = 'reader-theme';
    themeButton.type = 'button';
    themeButton.setAttribute('aria-label', word('theme'));
    themeButton.title = word('theme');
    var SVGNS = 'http://www.w3.org/2000/svg';
    var icon = doc.createElementNS(SVGNS, 'svg');
    icon.setAttribute('class', 'icon');
    icon.setAttribute('viewBox', '0 0 16 16');
    icon.setAttribute('width', '16');
    icon.setAttribute('height', '16');
    icon.setAttribute('aria-hidden', 'true');
    icon.setAttribute('focusable', 'false');
    var ring = doc.createElementNS(SVGNS, 'circle');
    ring.setAttribute('cx', '8');
    ring.setAttribute('cy', '8');
    ring.setAttribute('r', '5.6');
    ring.setAttribute('fill', 'none');
    ring.setAttribute('stroke', 'currentColor');
    ring.setAttribute('stroke-width', '1.4');
    icon.appendChild(ring);
    themeButton.appendChild(icon);
    themeButton.addEventListener('click', function (event) {
      event.stopImmediatePropagation();
      var set = root.getAttribute('data-theme');
      var now = set === 'dark' || set === 'light' ? set : media('(prefers-color-scheme: dark)') ? 'dark' : 'light';
      var next = now === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      keep('qh-theme', next);
    });
    bar.appendChild(themeButton);
  }

  function measureBar() {
    var h = bar.offsetHeight;
    if (h) root.style.setProperty('--reader-bar-h', h + 'px');
  }
  function barBottom() {
    var r = bar.getBoundingClientRect();
    return Math.max(0, r.bottom || 0);
  }

  /* ------------------------------------------------------------------ notices */

  /* The notice area: an address the book does not have, and the place a reader stopped. It is present from the start
     and empty when there is nothing to say, so that its words are announced when they appear. */
  var notices = element('div', 'reader-notices');
  notices.setAttribute('role', 'status');
  main.insertBefore(notices, main.firstChild);
  var noticeKind = null;
  var noticeClose = null;
  function notice(kind, text, actions, onClose) {
    dismiss(false);
    noticeKind = kind;
    noticeClose = onClose || null;
    var box = element('div', 'reader-notice');
    box.setAttribute('data-notice', kind);
    var p = element('p', 'reader-notice-text', text);
    p.tabIndex = -1;
    box.appendChild(p);
    var row = element('p', 'reader-notice-actions');
    actions.forEach(function (a) {
      var n;
      if (a.href) {
        n = element('a', 'reader-notice-action', a.text);
        n.href = a.href;
        if (a.content) n.replaceChildren(a.content);
      }
      else {
        n = element('button', 'reader-notice-action', a.text);
        n.type = 'button';
        n.addEventListener('click', a.act);
      }
      row.appendChild(n);
      row.appendChild(doc.createTextNode(' '));
    });
    var close = element('button', 'reader-notice-close', word('close'));
    close.type = 'button';
    close.addEventListener('click', function () {
      var after = noticeClose;
      dismiss(true);
      if (after) after();
    });
    row.appendChild(close);
    box.appendChild(row);
    notices.appendChild(box);
    return p;
  }
  function dismiss(moveFocus, only) {
    if (!noticeKind || (only && only !== noticeKind)) return;
    var hadFocus = notices.contains(doc.activeElement);
    notices.textContent = '';
    noticeKind = null;
    noticeClose = null;
    if (hadFocus && moveFocus) focusQuietly(placeHeading(current) || main);
  }

  /* ------------------------------------------------------------------ places and views */

  var current = null; /* the place shown: a chapter or a reference section; null for the title page */
  var view = '';
  var currentSection = null;
  var lastReading = null; /* the last chapter place read, for the way back from the reference */
  var drawerOpen = false;

  function placeHeading(p) {
    if (!p) return (front && front.querySelector('h1')) || front || toc;
    return isChapter(p) ? chapterHeading(p) : referenceHeading(p);
  }
  /* On a narrow screen a formula kept whole with its punctuation (.nobr) can be wider than its line. Such a group, and
     only such a group, scrolls in place rather than widening the page. */
  function fitFormulas() {
    var scope = current || front;
    if (!scope) return;
    var groups = all('.nobr', scope);
    groups.forEach(function (n) { n.classList.remove('reader-wide'); });
    if (!media('(max-width: 480px)')) return;
    groups.filter(function (n) {
      var block = n.parentElement && n.parentElement.closest(STRUCT + ', .mg-env, .mg-display');
      if (!block) return false;
      var right = block.getBoundingClientRect().right - (parseFloat(getComputedStyle(block).paddingRight) || 0);
      return n.getBoundingClientRect().right > right + 0.5;
    }).forEach(function (n) { n.classList.add('reader-wide'); });
  }
  function show(place) {
    clearReturn();
    later(fitFormulas);
    var target = place && places.indexOf(place) >= 0 ? place : null;
    if (!target && !front && !toc && chapters.length) target = chapters[0];
    else if (!target && !front && !toc && references.length) target = references[0];
    places.forEach(function (p) {
      if (p === target) { p.removeAttribute('hidden'); p.setAttribute('data-current', ''); }
      else {
        if (p.getAttribute('hidden') !== UNTIL) p.setAttribute('hidden', UNTIL);
        p.removeAttribute('data-current');
      }
    });
    if (front) {
      if (target) front.setAttribute('hidden', UNTIL); else front.removeAttribute('hidden');
    }
    if (toc) {
      if (!target) { toc.removeAttribute('hidden'); toc.removeAttribute('data-drawer'); drawerOpen = false; }
      else if (!drawerOpen) toc.setAttribute('hidden', '');
    }
    var was = current;
    current = target;
    view = !target ? 'front' : isChapter(target) ? 'chapter' : 'reference';
    main.setAttribute('data-reader-view', view);
    if (was !== target) {
      currentSection = null;
      if (view === 'chapter') {
        lastReading = target;
        fire(doc, 'qh:chapter', { id: target.id, number: chapterNumber(target), part: target.getAttribute('data-part') || '' });
      }
    }
    updateBar();
    updateToc();
  }

  /* The previous and next chapter: in the book's order, or along a route when one is followed. */
  var route = null;
  function neighbours(c) {
    var seq = chapters;
    if (route) seq = route.list.map(function (id) { return doc.getElementById(id); }).filter(function (x) { return chapters.indexOf(x) >= 0; });
    var i = chapters.indexOf(c);
    var prev = null;
    var next = null;
    seq.forEach(function (x) {
      var j = chapters.indexOf(x);
      if (j < i) prev = x; else if (j > i && !next) next = x;
    });
    return { prev: prev, next: next };
  }
  function setStep(link, target, labelKey, nameKey, href) {
    if (!target) { link.hidden = true; link.removeAttribute('href'); link.removeAttribute('aria-label'); link.removeAttribute('data-step'); return; }
    link.hidden = false;
    link.href = '#' + (href || target.id);
    link.setAttribute('data-step', labelKey);
    link.querySelector('.reader-step-label').textContent = word(labelKey);
    var toChapter = isChapter(target);
    var title = toChapter ? chapterTitle(target) : headingText(placeHeading(target));
    link.querySelector('.reader-step-title').textContent = toChapter ? fill(word('chapter'), { n: chapterNumber(target) }) + ' · ' + title : title;
    link.setAttribute('aria-label', fill(word(nameKey), { title: toChapter ? chapterName(target) : title, n: toChapter ? chapterNumber(target) : '' }));
  }
  function updateBar() {
    var c = view === 'chapter' ? current : null;
    if (c) {
      var pn = partIds.indexOf(c.getAttribute('data-part')) + 1;
      posPart.textContent = pn ? fill(word('part'), { n: roman(pn) }) : '';
      posChapter.textContent = fill(word('chapter-of'), { n: chapterNumber(c), total: chapterTotal });
      posTitle.textContent = chapterTitle(c);
      posSection.textContent = currentSection ? headingText(sectionHeading(currentSection)) : '';
      var n = neighbours(c);
      setStep(prevLink, n.prev, 'previous', 'previous-chapter');
      setStep(nextLink, n.next, 'next', 'next-chapter');
    } else if (view === 'reference') {
      posPart.textContent = '';
      posChapter.textContent = word('reference');
      posTitle.textContent = partLabel(current.id);
      posSection.textContent = '';
      var back = lastReading && lastReading.isConnected ? lastReading : null;
      var backSection = back && lastReadingSection && back.contains(lastReadingSection) ? lastReadingSection : null;
      setStep(prevLink, back, 'return', 'return-to', backSection ? backSection.id : null);
      if (!back && companion && bookHref) {
        /* From a companion page, back to the place last read in the book (kept on this device), else its title page. */
        var kept = null;
        try { kept = JSON.parse(stored(PLACE_KEY) || 'null'); } catch (e) { kept = null; }
        var to = kept && typeof kept.id === 'string' ? kept.id : 'front';
        prevLink.hidden = false;
        prevLink.href = bookHref + '#' + encodeURIComponent(to);
        prevLink.setAttribute('data-step', 'return');
        prevLink.querySelector('.reader-step-label').textContent = word('return');
        prevLink.querySelector('.reader-step-title').textContent = kept && typeof kept.title === 'string' ? kept.title : ((pagesMap && pagesMap.title) || '');
        prevLink.setAttribute('aria-label', fill(word('return-to'), { title: prevLink.querySelector('.reader-step-title').textContent || word('front') }));
      }
      setStep(nextLink, null);
    } else {
      posPart.textContent = '';
      posChapter.textContent = '';
      posTitle.textContent = '';
      posSection.textContent = '';
      setStep(prevLink, null);
      var first = route ? neighbours(null).next : chapters[0];
      setStep(nextLink, first || null, 'begin', 'begin-chapter');
    }
    position.hidden = !posChapter.textContent;
    if (route && view === 'chapter') {
      var at = route.list.indexOf(current.id);
      routeText.textContent = fill(word('route'), { route: route.name, i: at >= 0 ? at + 1 : '–', n: route.list.length });
      routeBox.hidden = false;
    } else routeBox.hidden = true;
  }
  function updateToc() {
    if (!toc) return;
    all('a[href^="#"]', toc).forEach(function (a) {
      var id = decode(a.getAttribute('href').slice(1));
      var t = doc.getElementById(id);
      var li = a.closest('li');
      if (t && current && t === current) {
        a.setAttribute('aria-current', 'page');
        if (li) li.setAttribute('data-current', '');
      } else if (t && currentSection && t === currentSection) {
        a.setAttribute('aria-current', 'location');
        if (li) li.removeAttribute('data-current');
      } else {
        a.removeAttribute('aria-current');
        if (li) li.removeAttribute('data-current');
      }
    });
  }

  /* The section at the top of the reading area, for the bar, the contents and the place kept. */
  var lastReadingSection = null;
  function sectionAtTop() {
    if (view !== 'chapter' || !current) return null;
    var limit = barBottom() + 32;
    var found = null;
    var secs = sectionMarks(current);
    for (var i = 0; i < secs.length; i++) {
      var r = secs[i].getBoundingClientRect();
      if (r.top <= limit) found = secs[i];
      else break;
    }
    return found;
  }
  function trackSection() {
    var s = sectionAtTop();
    if (s === currentSection) return;
    currentSection = s;
    if (view === 'chapter') lastReadingSection = s;
    posSection.textContent = s ? headingText(sectionHeading(s)) : '';
    updateToc();
  }

  /* ------------------------------------------------------------------ addresses and history */

  function hashId() { return decode(location.hash.replace(/^#/, '')); }
  function urlFor(id, q, address) {
    var u;
    try { u = new URL(address || location.href, location.href); } catch (e) { return address || '#' + id; }
    if (q) u.searchParams.set('q', q); else u.searchParams.delete('q');
    u.hash = id ? id : '';
    return u.href.replace(/#$/, '');
  }
  function stateWith(patch, fresh) {
    var base = !fresh && history.state && typeof history.state === 'object' ? history.state : {};
    var out = {};
    var k;
    for (k in base) if (Object.prototype.hasOwnProperty.call(base, k)) out[k] = base[k];
    var r = {};
    var br = !fresh && base.reader && typeof base.reader === 'object' ? base.reader : {};
    for (k in br) if (Object.prototype.hasOwnProperty.call(br, k)) r[k] = br[k];
    for (k in patch) if (Object.prototype.hasOwnProperty.call(patch, k)) r[k] = patch[k];
    out.reader = r;
    return out;
  }
  function replaceEntry(state, url) {
    try { history.replaceState(state, '', url == null ? location.href : url); return true; } catch (e) { return false; }
  }
  function pushEntry(state, url) {
    try { history.pushState(state, '', url); return true; } catch (e) { return false; }
  }
  var FOCUSABLE = 'a[href], button, input, select, textarea, summary, [tabindex]';
  /* Where an element is, in a form that survives the page being shown again: an id, or an id and the number of the
     focusable element under it. */
  function locator(el) {
    if (!el || el === doc.body || el === root || !el.closest) return null;
    if (!main.contains(el) && !bar.contains(el)) return null;
    if (el.id && !el.closest('.reader-results')) return { id: el.id };
    var host = el.parentNode && el.parentNode.closest('[id]');
    if (!host) return null;
    var n = all(FOCUSABLE, host).indexOf(el);
    return n < 0 ? { id: host.id } : { id: host.id, n: n };
  }
  function located(at) {
    if (!at || typeof at.id !== 'string') return null;
    var host = doc.getElementById(at.id);
    if (!host) return null;
    if (typeof at.n !== 'number') return host;
    return all(FOCUSABLE, host)[at.n] || null;
  }
  /* The element at the top of the reading area with an address, and how far below the bar it is. */
  function topAnchor() {
    var y = barBottom() + 8;
    var el = null;
    if (typeof doc.elementFromPoint === 'function') {
      var hit = doc.elementFromPoint(Math.max(1, (window.innerWidth || 0) / 2), y);
      el = hit && hit.closest ? hit.closest('[id]') : null;
      if (el && !(current ? current.contains(el) : onFront(el))) el = null;
    }
    if (!el) el = (view === 'chapter' && (sectionAtTop() || current)) || current || null;
    if (!el || !el.id) return null;
    return { at: el.id, off: Math.round(el.getBoundingClientRect().top) };
  }
  /* The entry being left keeps the place, the scroll and the focus, so that Back returns to all three. */
  function leaveEntry(from, extra) {
    var patch = { id: current ? (currentSection || current).id : '', view: view, y: Math.round(window.pageYOffset || 0) };
    var a = topAnchor();
    if (a) { patch.at = a.at; patch.off = a.off; }
    var f = locator(from || doc.activeElement);
    patch.focus = f || null;
    patch.panel = 0;
    if (extra) for (var k in extra) if (Object.prototype.hasOwnProperty.call(extra, k)) patch[k] = extra[k];
    replaceEntry(stateWith(patch), extra && extra.q ? urlFor(hashId(), extra.q) : null);
  }
  var entryTimer = null;
  function saveEntrySoon() {
    clearTimeout(entryTimer);
    entryTimer = setTimeout(function () {
      var st = history.state && history.state.reader;
      if (!st) return;
      var patch = { y: Math.round(window.pageYOffset || 0) };
      var a = topAnchor();
      if (a) { patch.at = a.at; patch.off = a.off; }
      replaceEntry(stateWith(patch));
    }, 250);
  }

  /* Focus the reader gives itself (a returned reminder, a restored place) is not a reader arriving at a term by keys. */
  var quietFocus = null;
  function focusQuietly(el) {
    if (!el || !el.focus) return;
    var natural = /^(button|input|select|textarea|summary)$/.test(el.localName) || (el.localName === 'a' && el.hasAttribute('href'));
    if (!natural && !el.hasAttribute('tabindex')) el.setAttribute('tabindex', '-1');
    quietFocus = el;
    try { el.focus({ preventScroll: true }); } catch (e) { el.focus(); }
    quietFocus = null;
  }
  var revealed = null;
  function markRevealed(el) {
    if (revealed && revealed !== el) revealed.removeAttribute('data-revealed');
    revealed = el && el !== main ? el : null;
    if (revealed) revealed.setAttribute('data-revealed', '');
  }
  function scrollToEl(el) {
    if (!el || !el.scrollIntoView) return;
    try { el.scrollIntoView({ block: 'start', behavior: 'auto' }); } catch (e) { el.scrollIntoView(true); }
  }
  /* What gets focus when a place is reached: a chapter or a section by its heading, anything else itself. */
  function focusFor(t) {
    if (!t) return placeHeading(null);
    if (isChapter(t)) return chapterHeading(t) || t;
    if (isPart(t)) return referenceHeading(t) || t;
    if (isSection(t)) return sectionHeading(t) || t;
    if (/^h[1-6]$/.test(t.localName)) return t;
    if (t === front) return placeHeading(null);
    if (t === toc) return (toc.getAttribute('aria-labelledby') && doc.getElementById(toc.getAttribute('aria-labelledby'))) || toc;
    return t;
  }
  /* A target inside closed disclosures (a statement in a row of the reference) is shown by opening them. */
  function openAround(t) {
    for (var d = t.parentNode && t.parentNode.closest ? t.parentNode.closest('details') : null; d;
         d = d.parentNode && d.parentNode.closest ? d.parentNode.closest('details') : null) {
      if (!d.open) d.open = true;
    }
    if (t.localName === 'details' && !t.open) t.open = true;
  }
  function revealCellNote(t, options) {
    return t && t.closest('.cell-note[hidden]') &&
      !fire(t, 'qh:reveal', { id: t.id, focus: options.focus !== false, scroll: options.scroll !== false }, true);
  }
  function arrive(t, o) {
    openAround(t);
    markRevealed(t);
    if (revealCellNote(t, o)) return;
    if (o.restore && restorePlace(o.restore, o.focus !== false)) return;
    var inComponent = t.closest && t.closest('[data-atlas-mount]');
    if (inComponent && !fire(t, 'qh:reveal', { id: t.id }, true)) return; /* the component shows it and moves focus */
    scrollToEl(t);
    if (o.focus !== false) focusQuietly(focusFor(t));
    if (o.marks) markWords(t, o.marks);
  }
  function restorePlace(st, withFocus) {
    var done = false;
    var at = st.at ? doc.getElementById(st.at) : null;
    if (at && (current ? current.contains(at) : onFront(at))) {
      window.scrollTo(0, Math.max(0, at.getBoundingClientRect().top + (window.pageYOffset || 0) - (st.off || 0)));
      done = true;
    } else if (typeof st.y === 'number') {
      window.scrollTo(0, st.y);
      done = true;
    }
    if (withFocus) {
      var f = located(st.focus);
      if (f && (ours(f) || bar.contains(f))) { focusQuietly(f); done = true; }
      else if (done) focusQuietly(focusFor(current) || main);
    }
    return done;
  }

  var lastId = null; /* the address last handled, so that a popstate and the hashchange after it count once */
  /* Show the place an address names. Options: push (a new history entry), replace (this entry), from (the control used,
     kept for Back), extra (more to keep in the entry left), focus (false: leave focus), restore (an entry's saved
     place), marks (search words to show), initial (the first address of the visit). */
  function go(id, o) {
    o = o || {};
    var target = resolve(id);
    if (!target && Object.prototype.hasOwnProperty.call(redirects, id) && typeof redirects[id] === 'string') {
      id = redirects[id];
      target = resolve(id);
      if (target && !o.push) o.replace = true;
    }
    if (!target) {
      var older = predecessor(id);
      if (older) { showPredecessor(id, older, o); return true; }
      var away = externalHref(id);
      if (away) {
        leaveFor(o.keepQuery ? urlFor(id, searchState.q, away) : away,
                 o.initial || (o.replace && !o.push) ? 'replace' : 'assign', o.from, o.extra);
        return true;
      }
      unknownAddress(id, o);
      return false;
    }
    if (!ours(target)) return false;
    var place = placeOf(target);
    closePeek(false);
    if (drawerOpen) closeDrawer(false);
    dismiss(false);
    if (o.push) {
      leaveEntry(o.from, o.extra);
      if (!pushEntry(stateWith({ id: id, view: place ? (isChapter(place) ? 'chapter' : 'reference') : 'front' }, true), urlFor(id))) {
        lastId = id;
        location.hash = id;
      }
    } else if (o.replace) {
      replaceEntry(stateWith({ id: id }), urlFor(id, o.keepQuery ? searchState.q : null));
    }
    lastId = id;
    show(place);
    arrive(target, o);
    later(trackSection);
    tellState();
    return true;
  }
  /* Before leaving for another page of the book: components are told (qh:leave, cancelable) and, unless the address is
     replaced, the entry left keeps the place, the focus and the search, so that Back returns to them. */
  function leaveFor(url, how, from, extra) {
    if (how !== 'replace') leaveEntry(from, extra);
    if (!fire(doc, 'qh:leave', { url: url, how: how }, true)) return;
    try { if (how === 'replace') location.replace(url); else location.assign(url); } catch (e) { location.href = url; }
  }
  function tellState() { fire(doc, 'qh:state', { q: searchState.q, view: view, id: current ? current.id : '' }); }

  /* An address the book does not have. A component may claim it (qh:unknown-anchor); else it is named, in view, with a
     search for its words. */
  function unknownAddress(id, o) {
    if (!fire(doc, 'qh:unknown-anchor', { id: id }, true)) return;
    if (o.initial || !current) show(o.initial ? null : current);
    var words = id.replace(/^(ch\d+|p\d+|def|thm|fig|sec|term|gl)-/i, '').replace(/-(h|p\d+)$/, '').replace(/[-_.]+/g, ' ').trim();
    var actions = [];
    if (/[a-z]{2}/i.test(words)) {
      actions.push({ text: fill(word('search-for'), { words: words }), act: function () { dismiss(false); openSearch(null, words); } });
    }
    var p = notice('unknown', fill(word('unknown'), { address: '#' + id }), actions);
    scrollToEl(notices);
    if (!o.initial) focusQuietly(p);
  }

  function showPredecessor(id, older, o) {
    if (o.initial || !current) show(null);
    if (o.push) {
      leaveEntry(o.from, o.extra);
      pushEntry(stateWith({ id: id, view: view }, true), urlFor(id));
    }
    lastId = id;
    var actions = older.targets.map(function (candidate) {
      var t = doc.getElementById(candidate);
      if (!t) return null;
      var heading = /^h[1-6]$/.test(t.localName) ? t :
        isSection(t) ? sectionHeading(t) : isChapter(t) ? chapterHeading(t) : isPart(t) ? referenceHeading(t) : null;
      var label = heading ? headingText(heading) : textOf(t, null, true) || textOf(t);
      if (label.length > 110) label = label.slice(0, 107).replace(/\s+\S*$/, '') + '…';
      var action = { text: fill(word('go-to'), { where: label || candidate }), href: '#' + candidate };
      var source = heading || t;
      if (source.querySelector('math')) {
        var snippet = snippetOf({ el: source, skip: '.anchor-sr, [aria-hidden="true"], [hidden], button' }, [], 110);
        if (snippet) {
          snippet.removeAttribute('class');
          all('[id]', snippet).forEach(function (node) { node.removeAttribute('id'); });
          var content = doc.createDocumentFragment();
          word('go-to').split('{where}').forEach(function (part, i) {
            if (i) content.appendChild(snippet.cloneNode(true));
            content.appendChild(doc.createTextNode(part));
          });
          action.content = content;
        }
      }
      return action;
    }).filter(Boolean);
    var p = notice('predecessor', word(older.ambiguous ? 'ambiguous-address' : 'changed-address'), actions);
    scrollToEl(notices);
    if (!o.initial) focusQuietly(p);
  }

  /* ------------------------------------------------------------------ the contents as a panel */

  function openDrawer() {
    if (!toc) return;
    if (view === 'front') {
      scrollToEl(toc);
      focusQuietly(focusFor(toc));
      return;
    }
    drawerOpen = true;
    toc.removeAttribute('hidden');
    toc.setAttribute('data-drawer', '');
    tocButton.setAttribute('aria-expanded', 'true');
    var here = toc.querySelector('[aria-current="location"]') || toc.querySelector('[aria-current="page"]') || toc.querySelector('a[href]');
    if (here) {
      if (here.scrollIntoView) try { here.scrollIntoView({ block: 'nearest' }); } catch (e) { /* no layout */ }
      focusQuietly(here);
    }
  }
  function closeDrawer(returnFocus) {
    if (!toc || !drawerOpen) return;
    drawerOpen = false;
    toc.removeAttribute('data-drawer');
    if (view !== 'front') toc.setAttribute('hidden', '');
    tocButton.setAttribute('aria-expanded', 'false');
    if (returnFocus) tocButton.focus();
  }
  if (tocButton) {
    tocButton.addEventListener('click', function () { if (drawerOpen) closeDrawer(true); else openDrawer(); });
    toc.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && drawerOpen) { event.preventDefault(); event.stopPropagation(); closeDrawer(true); }
    });
    toc.addEventListener('focusout', function (event) {
      var to = event.relatedTarget;
      if (!drawerOpen || !to || toc.contains(to) || to === tocButton) return;
      closeDrawer(false);
    });
  }

  /* ------------------------------------------------------------------ routes through the book */

  /* A route is served as a link with the chapters it takes, in order: a[data-route][data-route-chapters="ch01 ch03 …"].
     Following it makes the bar's previous and next follow the route until the reader leaves it. */
  var ROUTE_KEY = 'qh-reader-route';
  function routeFrom(a) {
    var list = (a.getAttribute('data-route-chapters') || '').split(/\s+/).filter(function (id) {
      var c = doc.getElementById(id);
      return c && chapters.indexOf(c) >= 0;
    });
    return list.length ? { id: a.getAttribute('data-route'), name: textOf(a), list: list } : null;
  }
  function setRoute(r) {
    route = r;
    sessionSet(ROUTE_KEY, r ? JSON.stringify(r) : null);
    updateBar();
  }
  (function () {
    var raw = sessionGet(ROUTE_KEY);
    if (!raw) return;
    try {
      var r = JSON.parse(raw);
      var link = r && typeof r.id === 'string' ? all('[data-route]', main).filter(function (a) { return a.getAttribute('data-route') === r.id; })[0] : null;
      route = link ? routeFrom(link) : null;
    } catch (e) { route = null; }
  })();
  routeLeave.addEventListener('click', function () {
    setRoute(null);
    focusQuietly(tocButton || nextLink);
  });

  /* ------------------------------------------------------------------ reminders for cross-references */

  var peek = element('div', 'reader-peek');
  peek.id = 'reader-peek';
  peek.setAttribute('role', 'dialog');
  peek.hidden = true;
  var peekHead = peek.appendChild(element('div', 'reader-peek-head'));
  var peekWhere = peekHead.appendChild(element('p', 'reader-peek-where'));
  peekWhere.id = 'reader-peek-where';
  peekWhere.tabIndex = -1;
  var peekClose = peekHead.appendChild(element('button', 'reader-peek-close', '×'));
  peekClose.type = 'button';
  peekClose.setAttribute('aria-label', word('close'));
  var peekBody = peek.appendChild(element('div', 'reader-peek-body'));
  var peekFoot = peek.appendChild(element('p', 'reader-peek-foot'));
  var peekGo = peekFoot.appendChild(element('a', 'reader-peek-go'));
  doc.body.appendChild(peek);
  var peekFrom = null;    /* the cross-reference the reminder belongs to */
  var peekTarget = null;
  var peekPinned = false;
  var hideTimer = null;
  var openTimer = null;

  function whereOf(t) {
    var place = placeOf(t);
    if (!place) return word('front');
    if (isPart(place)) return headingText(referenceHeading(place));
    var where = fill(word('chapter'), { n: chapterNumber(place) });
    var sec = sectionOf(t);
    if (sec && sec !== t && place.contains(sec)) where += ' · ' + headingText(sectionHeading(sec));
    else if (t === place || t === sec) where += ' · ' + (t === place ? chapterTitle(place) : headingText(sectionHeading(sec)));
    return where;
  }
  function firstParagraph(scope) {
    return all('p', scope).filter(function (p) {
      return !p.closest('[data-chapter-kicker], [data-prerequisites], [data-chapter-end], nav, figure, header, .reader-notices, ' + ENV) &&
        textOf(p).length > 0;
    })[0] || null;
  }
  function firstParagraphAfter(h) {
    var place = placeOf(h);
    var list = place ? all('p', place) : [];
    for (var i = 0; i < list.length; i++) {
      if (!(h.compareDocumentPosition(list[i]) & Node.DOCUMENT_POSITION_FOLLOWING)) continue;
      if (list[i].closest('nav, figure, [data-prerequisites], [data-chapter-end]')) continue;
      if (textOf(list[i])) return list[i];
    }
    return null;
  }
  function peekContent(t) {
    var frag = doc.createDocumentFragment();
    if (t.localName === 'figure') {
      var title = blockTitle(t);
      if (title) frag.appendChild(cleanCopy(title, 'p'));
      var cap = t.querySelector('figcaption');
      if (cap) frag.appendChild(cleanCopy(cap, 'div'));
      return frag;
    }
    if (isChapter(t)) {
      var parts = chapterTitleParts(t);
      if (parts.h) {
        var head = element('p', 'reader-peek-title', fill(word('chapter'), { n: chapterNumber(t) }) + ' · ');
        (parts.dropped ? parts.nodes : [parts.h]).forEach(function (k) {
          if (k.nodeType === 3) head.appendChild(doc.createTextNode(k.nodeValue));
          else if (k.nodeType === 1) head.appendChild(inlineCopy(k));
        });
        frag.appendChild(head);
      }
      var tocLink = toc && all('a[data-chapter-link]', toc).find(function (link) {
        return link.hash === '#' + t.id;
      });
      var summary = t.querySelector('[data-chapter-summary]') ||
        (tocLink && tocLink.parentElement.querySelector('.mg-toc-summary')) || firstParagraph(t);
      if (summary) frag.appendChild(cleanCopy(summary, summary.localName === 'p' ? 'p' : 'div'));
      var pre = t.querySelector('[data-prerequisites]');
      if (pre && pre.querySelector('a[href]')) frag.appendChild(cleanCopy(pre));
      return frag;
    }
    if (isSection(t) || isPart(t) || (/^h[2-6]$/.test(t.localName) && placeOf(t) && sectionMarks(placeOf(t)).indexOf(t) >= 0)) {
      var sh = isPart(t) ? referenceHeading(t) : sectionHeading(t);
      if (sh) {
        var shc = spaceParts(cleanCopy(sh, 'p'));
        shc.className = 'reader-peek-title';
        frag.appendChild(shc);
      }
      var fp = /^h[2-6]$/.test(t.localName) ? firstParagraphAfter(t) : firstParagraph(t);
      if (fp) {
        frag.appendChild(cleanCopy(fp, 'p'));
        // A mathematical paragraph can span a display and its continuation.
        for (var part = fp.nextElementSibling; part && part.matches('.mg-display, p.mg-cont'); part = part.nextElementSibling) {
          frag.appendChild(cleanCopy(part, part.localName));
        }
      }
      return frag;
    }
    if (t.localName === 'dt') {
      frag.appendChild(cleanCopy(t, 'p'));
      for (var n = t.nextElementSibling; n && n.localName === 'dd'; n = n.nextElementSibling) frag.appendChild(cleanCopy(n, 'div'));
      return frag;
    }
    if (t.firstElementChild && t.firstElementChild.localName === 'dt') {
      all(':scope > dt, :scope > dd', t).forEach(function (n) { frag.appendChild(cleanCopy(n, n.localName === 'dt' ? 'p' : 'div')); });
      return frag;
    }
    if (/^h[1-6]$/.test(t.localName)) {
      frag.appendChild(cleanCopy(t, 'p'));
      return frag;
    }
    frag.appendChild(cleanCopy(t));
    return frag;
  }
  /* Inline targets (a defined word, a marker) are shown with the block that holds them. */
  var INLINE = /^(a|abbr|b|cite|code|dfn|em|i|mark|q|s|small|span|strong|sub|sup|u|var)$/;
  function peekBlock(t) {
    if (!INLINE.test(t.localName)) return t;
    return t.parentNode && t.parentNode.closest ? t.parentNode.closest(ENV + ', figure, ' + STRUCT + ', ' + DISPLAY + ', ' + SECTION + ', ' + CHAPTER + ', ' + REFERENCE) || t : t;
  }
  /* A link in the text of a chapter or the reference to a place of the book opens a reminder: by its data-ref, or by
     where it stands (in running text, not in a navigation list). data-ref="none" makes it an ordinary link. */
  function isReference(a) {
    if (!main.contains(a) || a.closest('[data-atlas-mount]')) return false;
    var r = a.getAttribute('data-ref');
    if (r === 'none') return false;
    if (r) return true;
    if (a.closest('nav, [data-reader-toc], [data-chapter-end], [data-chapter-kicker], .reader-notices, [data-reader-front], [data-route]')) return false;
    return !!(a.closest(CHAPTER + ', ' + REFERENCE));
  }
  function targetOfLink(a) {
    var href = a.getAttribute('href') || '';
    if (href.charAt(0) !== '#') return null;
    var id = decode(href.slice(1));
    var t = resolve(id);
    if (!t && Object.prototype.hasOwnProperty.call(redirects, id)) t = resolve(redirects[id]);
    return t;
  }
  /* Terms. A phrase the author has linked to its defining passage carries data-ref="definition", the passage as
     data-definition-target and the author's brief statement of the definition as data-definition-preview. On hover or
     keyboard focus the reminder shows that statement with a visible link to the passage; a tap, a click or Enter keeps
     it open. Nothing here generates a definition or guesses a target: a term without the author's preview, or whose
     passage this page cannot show, stays an ordinary link. */
  function isTerm(a) {
    return !!a && a.localName === 'a' && a.getAttribute('data-ref') === 'definition' && !!a.getAttribute('data-definition-preview');
  }
  function selectingIn(node) {
    var s = window.getSelection ? window.getSelection() : null;
    return !!s && !s.isCollapsed && s.rangeCount > 0 && s.getRangeAt(0).intersectsNode(node);
  }
  var termDescribedBy = null; /* the term's own aria-describedby while the reminder describes it */
  var nearTarget = null;      /* a defining passage already on the screen, outlined while its term is shown */
  function definitionTitle(t) {
    var b = t.matches(ENV) ? t : t.closest(ENV);
    if (b && main.contains(b)) {
      var title = blockTitle(b);
      if (title) return textOf(title).replace(/\s*[.:]\s*$/, '');
    }
    if (/^h[1-6]$/.test(t.localName)) return headingText(t);
    var display = t.closest('.mg-display');
    if (display && display.getAttribute('data-tag')) return fill(word('define-equation'), { n: '(' + display.getAttribute('data-tag') + ')' });
    return word('define-text');
  }
  /* The place of a definition in brief, as a chapter and its numbered section ("Chapter 1 · §1.1"); the full place,
     with the section's title, is the link's accessible name. */
  function whereShort(t) {
    var place = placeOf(t);
    if (!place || isPart(place)) return whereOf(t);
    var where = fill(word('chapter'), { n: chapterNumber(place) });
    var sec = sectionOf(t);
    var h = sec && place.contains(sec) ? sectionHeading(sec) : null;
    var m = h && /^(\d+(?:\.\d+)+)\s/.exec(headingText(h));
    return m ? where + ' · §' + m[1] : where;
  }
  function onScreen(t) {
    if (!t.getClientRects().length) return false;
    var r = t.getBoundingClientRect();
    return r.bottom > barBottom() + 8 && r.top < (window.innerHeight || 0) - 8;
  }
  function openDefinition(a, pin) {
    var href = a.getAttribute('href') || '';
    var local = href.charAt(0) === '#';
    var t = local ? targetOfLink(a) : null;
    if (local && (!t || !ours(t))) return false;
    if (t && t.contains(a)) return false; /* the term inside its own definition */
    clearTimeout(hideTimer);
    clearTimeout(openTimer);
    if (peekFrom && peekFrom !== a) releaseTerm();
    peekFrom = a;
    peekTarget = t;
    peekPinned = !!pin;
    peekBody.textContent = '';
    var title = t ? definitionTitle(t) : word('define-kind');
    peekBody.appendChild(element('p', 'reader-define-title', title));
    var text = peekBody.appendChild(element('p', 'reader-define-text', a.getAttribute('data-definition-preview')));
    text.id = 'reader-define-text';
    var where = t ? whereOf(t) : word('define-reference');
    peekWhere.textContent = t ? whereShort(t) : where;
    var near = !!t && onScreen(t);
    peekGo.href = local ? '#' + give(t) : a.getAttribute('href');
    peekGo.textContent = near ? word('define-go-here') : word('define-go');
    peekGo.setAttribute('aria-label', (near ? word('define-go-here') : word('define-go')) + ': ' + title + ', ' + where);
    peek.setAttribute('aria-label', title + ' — ' + where);
    peek.setAttribute('data-kind', 'definition');
    peek.setAttribute('data-term', '');
    if (pin) peek.setAttribute('role', 'dialog'); else peek.removeAttribute('role');
    if (termDescribedBy === null) termDescribedBy = a.getAttribute('aria-describedby') || '';
    a.setAttribute('aria-describedby', ((termDescribedBy ? termDescribedBy + ' ' : '') + text.id).trim());
    if (near) { nearTarget = peekBlock(t); nearTarget.setAttribute('data-definition-near', ''); }
    peek.hidden = false;
    if (pin) a.setAttribute('aria-expanded', 'true');
    placePeek(true);
    /* A long statement scrolls in its own box, reachable by keys. */
    if (peekBody.scrollHeight > peekBody.clientHeight + 1) { peekBody.tabIndex = 0; peekBody.setAttribute('aria-labelledby', text.id); }
    else { peekBody.removeAttribute('tabindex'); peekBody.removeAttribute('aria-labelledby'); }
    if (pin) focusQuietly(peekWhere);
    return true;
  }
  /* The term's own attributes back as they were when its reminder closes or moves to another term. */
  function releaseTerm() {
    if (peekFrom) {
      peekFrom.removeAttribute('aria-expanded');
      if (termDescribedBy !== null) {
        if (termDescribedBy) peekFrom.setAttribute('aria-describedby', termDescribedBy); else peekFrom.removeAttribute('aria-describedby');
      }
    }
    termDescribedBy = null;
    if (nearTarget) nearTarget.removeAttribute('data-definition-near');
    nearTarget = null;
    peek.removeAttribute('data-term');
    peek.setAttribute('role', 'dialog');
    peekBody.removeAttribute('tabindex');
    peekBody.removeAttribute('aria-labelledby');
    peekGo.removeAttribute('aria-label');
    sheetRoom(0);
  }
  /* On a narrow screen the reminder is a sheet at the foot of the screen. The page gains room below its text while the
     sheet is open, so that a term near the end of the page can still be read above it. */
  function sheetRoom(px) {
    if (px) main.style.setProperty('--reader-sheet-room', px + 'px'); else main.style.removeProperty('--reader-sheet-room');
    if (px) main.setAttribute('data-sheet-open', ''); else main.removeAttribute('data-sheet-open');
  }
  /* Back to the reading after a definition was followed: a control beside the defining passage, until the place changes. */
  var returnControl = null;
  function offerReturn(term, block) {
    clearReturn();
    if (!term || !block || !block.parentNode) return;
    var p = element('p', 'reader-return');
    p.setAttribute('data-reader-skip', '');
    var b = p.appendChild(element('button', 'reader-return-button', fill(word('define-return'), { term: textOf(term) })));
    b.type = 'button';
    b.addEventListener('click', function () { clearReturn(); history.back(); });
    block.parentNode.insertBefore(p, block.nextSibling);
    returnControl = p;
  }
  function clearReturn() {
    if (returnControl && returnControl.parentNode) returnControl.parentNode.removeChild(returnControl);
    returnControl = null;
  }
  function openPeek(a, pin, target) {
    if (isTerm(a) && !target) return openDefinition(a, pin);
    var t = target || targetOfLink(a);
    if (!t || !ours(t) || onFront(t)) return false;
    clearTimeout(hideTimer);
    clearTimeout(openTimer);
    if (peekFrom) releaseTerm();
    peekFrom = a;
    peekTarget = t;
    peekPinned = !!pin;
    peekBody.textContent = '';
    peekBody.appendChild(peekContent(peekBlock(t)));
    var where = whereOf(t);
    peekWhere.textContent = where;
    var b = peekBlock(t);
    var name = isChapter(b) ? chapterName(b) : (isSection(b) ? headingText(sectionHeading(b)) : textOf(blockTitle(b))) || textOf(a);
    peek.setAttribute('aria-label', name + (name === where ? '' : ' — ' + where));
    peekGo.href = '#' + give(t);
    peekGo.textContent = fill(word('go-to'), { where: isChapter(t) ? fill(word('chapter'), { n: chapterNumber(t) }) : where });
    peek.setAttribute('data-kind', t.getAttribute('data-ref-kind') || a.getAttribute('data-ref') || '');
    peek.hidden = false;
    if (pin) a.setAttribute('aria-expanded', 'true');
    if (a.localName === 'button') a.setAttribute('aria-controls', 'reader-peek');
    placePeek();
    if (pin) focusQuietly(peekWhere);
    return true;
  }
  function closePeek(returnFocus) {
    clearTimeout(hideTimer);
    clearTimeout(openTimer);
    if (peek.hidden) return;
    var from = peekFrom;
    var hadFocus = peek.contains(doc.activeElement);
    peek.hidden = true;
    releaseTerm();
    peekBody.textContent = '';
    peekFrom = null;
    peekTarget = null;
    peekPinned = false;
    if (from && (returnFocus || hadFocus) && from.isConnected) { quietFocus = from; from.focus(); quietFocus = null; }
  }
  /* Beside the cross-reference on a wide screen: the page's style decides, from the place given here. On a narrow
     screen the page shows the reminder as a sheet and these are not used. */
  function placePeek(opening) {
    if (peek.hidden || !peekFrom) return;
    var rects = peekFrom.getClientRects ? peekFrom.getClientRects() : [];
    var r = rects && rects.length ? rects[0] : peekFrom.getBoundingClientRect();
    var vh = window.innerHeight || 0;
    var below = vh - r.bottom;
    var h = peek.offsetHeight || 0;
    var downward = below >= Math.min(h + 16, 320) || below >= r.top;
    /* A term's definition on a wide screen goes beside the paragraph, level with the term, where it covers no text. */
    if (peek.hasAttribute('data-term') && !media('(max-width: 640px)')) {
      var br = peekBlock(peekFrom).getBoundingClientRect();
      if ((window.innerWidth || 0) - br.right - 24 >= (peek.offsetWidth || 0) + 8) {
        peek.setAttribute('data-placement', 'side');
        peek.style.setProperty('--peek-x', Math.round(br.right + 24) + 'px');
        peek.style.setProperty('--peek-y', Math.round(Math.max(barBottom() + 8, Math.min(r.top - 8, vh - h - 8))) + 'px');
        return;
      }
    }
    peek.setAttribute('data-placement', downward ? 'below' : 'above');
    peek.style.setProperty('--peek-x', Math.round(r.left) + 'px');
    peek.style.setProperty('--peek-y', Math.round(downward ? r.bottom : r.top) + 'px');
    /* A sheet: the term it belongs to is kept readable above it, even at the end of the page. */
    if (opening && peek.hasAttribute('data-term') && media('(max-width: 640px)')) {
      var sheetTop = peek.getBoundingClientRect().top;
      if (r.bottom > sheetTop - 12) {
        sheetRoom(Math.ceil(vh - sheetTop + 24));
        window.scrollBy(0, Math.ceil(r.bottom - sheetTop + 24));
      }
    }
  }
  function hideSoon() {
    if (peekPinned) return;
    clearTimeout(hideTimer);
    /* A term's definition may stand beside the paragraph: the pointer is given time to cross to it. */
    hideTimer = setTimeout(function () { if (!peekPinned) closePeek(false); }, peek.hasAttribute('data-term') ? 700 : 300);
  }
  peekClose.addEventListener('click', function () { closePeek(true); });
  peek.addEventListener('click', function (event) {
    var a = event.target.closest && event.target.closest('a[href]');
    if (!a || !peek.contains(a) || !plainClick(event)) return;
    var from = peekFrom;
    var term = isTerm(from) ? from : null;
    var href = a.getAttribute('href');
    if (href.charAt(0) !== '#') {
      /* A definition in another page of the book: the entry left keeps the place, as for any link to that page. */
      if (!bookPage(a.href)) return;
      event.preventDefault();
      closePeek(false);
      leaveFor(a.href, 'assign', from);
      return;
    }
    event.preventDefault();
    var id = decode(href.slice(1));
    closePeek(false);
    if (go(id, { push: true, from: from }) && term) {
      var t = resolve(id);
      if (t) offerReturn(term, peekBlock(t));
    }
  });
  var TABBABLE = 'a[href], button:not([disabled]), input:not([disabled]), summary, [tabindex]:not([tabindex="-1"])';
  function reachable(el) {
    if (!el || el.hidden || el.closest('[hidden]')) return false;
    return !el.closest('[inert]');
  }
  function nextAfter(el) {
    var list = all(TABBABLE).filter(function (n) { return !peek.contains(n) && reachable(n); });
    for (var i = 0; i < list.length; i++) {
      if (el.compareDocumentPosition(list[i]) & Node.DOCUMENT_POSITION_FOLLOWING && !el.contains(list[i])) return list[i];
    }
    return null;
  }
  peek.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') { event.preventDefault(); event.stopPropagation(); closePeek(true); return; }
    if (event.key !== 'Tab') return;
    var inside = all(TABBABLE, peek).filter(reachable);
    if (!inside.length) return;
    if (!event.shiftKey && event.target === inside[inside.length - 1]) {
      /* Past the end of the reminder, Tab goes on in the text after the cross-reference. */
      var from = peekFrom;
      var after = from ? nextAfter(from) : null;
      event.preventDefault();
      closePeek(false);
      if (after) after.focus(); else if (from) from.focus();
    } else if (event.shiftKey && (event.target === inside[0] || event.target === peekWhere)) {
      event.preventDefault();
      closePeek(true);
    }
  });
  peek.addEventListener('mouseenter', function () { clearTimeout(hideTimer); });
  peek.addEventListener('mouseleave', hideSoon);

  function refLink(node) {
    var a = node && node.closest ? node.closest('a[href^="#"]') : null;
    return a && isReference(a) ? a : null;
  }
  if (hoverCapable) {
    /* A reminder on hover opens only after the pointer has moved over the link and rested, and stays while the pointer
       is on the link or on the reminder. */
    var lastXY = '';
    main.addEventListener('mousemove', function (event) {
      var xy = event.screenX + ',' + event.screenY;
      var moved = xy !== lastXY;
      lastXY = xy;
      var a = refLink(event.target);
      /* Not while a button is held: the reader may be selecting text. */
      if (event.buttons) { clearTimeout(openTimer); return; }
      if (!a || !moved) return;
      if (peekFrom === a && !peek.hidden) { clearTimeout(hideTimer); return; }
      if (peekPinned) return;
      clearTimeout(openTimer);
      openTimer = setTimeout(function () { if (!peekPinned) openPeek(a, false); }, isTerm(a) ? 300 : 380);
    });
    /* Pressing the button begins a selection or a click: a reminder waiting to open on hover does not. */
    main.addEventListener('mousedown', function () { clearTimeout(openTimer); }, true);
    main.addEventListener('mouseout', function (event) {
      var a = refLink(event.target);
      if (!a) return;
      var to = event.relatedTarget;
      if (to && (a.contains(to) || peek.contains(to))) return;
      clearTimeout(openTimer);
      if (peekFrom === a) hideSoon();
    });
  }
  /* A term reached by keys shows its definition at once, described to a screen reader; leaving the term closes what
     only reaching it opened. Focus the reader gives itself, or a click's focus, opens nothing. */
  main.addEventListener('focusin', function (event) {
    var a = event.target;
    if (!isTerm(a) || a === quietFocus || peekPinned) return;
    var keyed = true;
    try { keyed = a.matches(':focus-visible'); } catch (e) { keyed = true; }
    if (!keyed) return;
    clearTimeout(openTimer);
    openPeek(a, false);
  });
  main.addEventListener('focusout', function (event) {
    var a = event.target;
    if (!isTerm(a) || peekFrom !== a || peekPinned) return;
    var to = event.relatedTarget;
    if (to && peek.contains(to)) return;
    closePeek(false);
  });

  /* ------------------------------------------------------------------ search */

  function fold(s) {
    return (s || '').normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase()
      .replace(/[‘’ʼ]/g, '\'').replace(/[“”„‟«»]/g, '"').replace(/[‐-―−]/g, '-');
  }
  /* TeX compared without braces or spaces, with \geq, \leq and \neq as \ge, \le and \ne. */
  function texNorm(s) {
    return fold(s).replace(/\\(geq|leq|neq)(?![a-z])/g, function (m, c) { return '\\' + c.slice(0, 2); }).replace(/[{}\s]/g, '');
  }
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
      .replace(/(\\[A-Za-z]+)\s+(?=\{|[A-Za-z0-9](?![A-Za-z0-9]))/g, '$1')
      .replace(/"([^"]+)(?:"|$)|(\S+)/g, function (_, phrase, w) {
        var raw = phrase ? phrase.replace(/\s+/g, ' ').trim() : w.replace(/^["'.,;:!?()[\]]+|["'.,;:!?()[\]]+$/g, '');
        if (!raw) return '';
        var f = fold(raw);
        var kind = TEXY.test(raw) ? 'tex' : LETTERLIKE.test(raw) ? 'letterlike' :
                   (!phrase && Object.prototype.hasOwnProperty.call(GREEK, f)) ? 'greek' : 'text';
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
  function weigh(u, t) {
    if (t.kind === 'tex') {
      var tt = function (f) { return Math.max(grade(f, t.w, false), t.plain ? grade(f, t.plain, false) : 0); };
      return Math.max(tt(u.ft) * 4 + tt(u.fb) + tt(u.fc) / 2, u.ttex.indexOf(t.tex) >= 0 ? 4 : u.tex.indexOf(t.tex) >= 0 ? 1 : 0);
    }
    if (t.kind === 'letterlike') return u.raw.indexOf(t.raw) >= 0 ? 1 : 0;
    if (t.kind === 'greek') {
      var inTitle = 0;
      var inBody = 0;
      GREEK[t.w].split('').forEach(function (c) { if (u.ft.indexOf(c) >= 0) inTitle = 13; if (u.fb.indexOf(c) >= 0) inBody = 4; });
      return Math.max(inTitle, inBody, grade(u.ft, t.w, true) === 3 ? 12 : 0, grade(u.fb, t.w, true) === 3 ? 3 : 0);
    }
    var gt = Math.max(grade(u.ft, t.w, t.strict), grade(u.classification, t.w, t.strict));
    var gb = grade(u.fb, t.w, t.strict);
    var gc = grade(u.fc, t.w, t.strict);
    return gt || gb || gc ? gt * 4 + gb + gc / 2 : 0;
  }
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
  function ownHas(u, t) {
    if (t.kind === 'tex') return u.tex.indexOf(t.tex) >= 0 || !!(grade(u.ft, t.w, false) || grade(u.fb, t.w, false)) ||
      !!(t.plain && (grade(u.ft, t.plain, false) || grade(u.fb, t.plain, false)));
    if (t.kind === 'letterlike') return u.ro.indexOf(t.raw) >= 0;
    if (t.kind === 'greek') return GREEK[t.w].split('').some(function (c) { return u.ft.indexOf(c) >= 0 || u.fb.indexOf(c) >= 0; }) ||
      grade(u.ft, t.w, true) === 3 || grade(u.fb, t.w, true) === 3;
    return !!(grade(u.ft, t.w, t.strict) || grade(u.fb, t.w, t.strict) || grade(u.classification, t.w, t.strict));
  }
  /* Whether a term shows in the words of a result (else it was found only in a formula). */
  function inWords(u, t, plain) {
    if (t.kind === 'letterlike') return plain.toLowerCase().indexOf(t.raw) >= 0;
    var p = fold(plain + ' ' + u.title + ' ' + u.context + ' ' + u.classification);
    if (t.kind === 'greek') return GREEK[t.w].split('').some(function (c) { return p.indexOf(c) >= 0; }) || grade(p, t.w, true) === 3;
    if (t.plain && grade(p, t.plain, false) > 0) return true;
    return grade(p, t.w, t.strict) > 0;
  }
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
  function pieces(el, skip) {
    var out = [];
    (function walk(n, top) {
      if (n.nodeType === 3) { out.push({ text: n.nodeValue }); return; }
      if (n.nodeType !== 1) return;
      if (!top && skip && n.matches(skip)) return;
      if (!top && n.hasAttribute('data-reader-skip')) return;
      var tag = n.localName;
      if (tag === 'math') { out.push({ math: n, text: textOf(n) }); return; }
      if (tag === 'svg' || tag === 'annotation' || tag === 'script' || tag === 'style' || tag === 'template') return;
      for (var c = n.firstChild; c; c = c.nextSibling) walk(c, false);
      if (BLOCK.test(tag)) out.push({ text: ' ' });
    })(el, true);
    return out;
  }
  function mathCopy(m) {
    var wide = m.getAttribute('display') === 'block' || !!(m.parentNode && m.parentNode.closest && m.parentNode.closest('.math-display, .math-long'));
    var c = m.cloneNode(true);
    c.removeAttribute('display');
    c.classList.remove('tml-display');
    all('[id]', c).forEach(function (n) { n.removeAttribute('id'); });
    if (!wide) return c;
    var box = element('span', 'math-long'); /* a wide formula scrolls inside its own box, as on the page */
    box.appendChild(c);
    return box;
  }
  /* Cross-page results carry the same math as the destination, separate from the search text. */
  var MATH_NS = 'http://www.w3.org/1998/Math/MathML';
  var MATH_TAG = /^(math|semantics|annotation|mi|mn|mo|ms|mtext|mspace|mrow|mfrac|msqrt|mroot|mstyle|merror|mpadded|mphantom|menclose|mfenced|msub|msup|msubsup|munder|mover|munderover|mmultiscripts|mprescripts|none|mtable|mtr|mtd|mlabeledtr)$/;
  var MATH_ATTR = /^(accent|accentunder|align|aria-label|bevelled|class|close|columnalign|columnlines|columnspacing|columnspan|depth|dir|display|displaystyle|encoding|fence|form|frame|framespacing|height|largeop|linethickness|lspace|mathbackground|mathcolor|mathsize|mathvariant|maxsize|minsize|movablelimits|notation|open|rowalign|rowlines|rowspacing|rowspan|rspace|scriptlevel|separator|separators|stretchy|symmetric|voffset|width|style|xmlns)$/;
  function snippetParts(sources, skip) {
    var out = [];
    var hasMath = false;
    sources.forEach(function (source) {
      pieces(source, skip).forEach(function (p) {
        if (p.math) {
          hasMath = true;
          var wide = p.math.getAttribute('display') === 'block' || !!p.math.closest('.math-display, .math-long');
          out.push([p.math.outerHTML, wide]);
        } else if (typeof out[out.length - 1] === 'string') {
          out[out.length - 1] += p.text;
        } else {
          out.push(p.text);
        }
      });
    });
    return hasMath ? out : undefined;
  }
  function readSnippet(parts, text, hasMath) {
    var span = element('span');
    if (!Array.isArray(parts)) {
      span.textContent = hasMath ? word('formula-in-source') : text;
      return span;
    }
    var template = doc.createElement('template');
    parts.forEach(function (p) {
      if (typeof p === 'string') {
        span.appendChild(doc.createTextNode(p));
        return;
      }
      if (!Array.isArray(p) || typeof p[0] !== 'string' || typeof p[1] !== 'boolean') {
        span.appendChild(doc.createTextNode(word('formula-in-source')));
        return;
      }
      template.innerHTML = p[0];
      var math = template.content.firstElementChild;
      if (!math || math.localName !== 'math' || template.content.childNodes.length !== 1 ||
          [math].concat(all('*', math)).some(function (n) {
            return n.namespaceURI !== MATH_NS || !MATH_TAG.test(n.localName) ||
              Array.prototype.some.call(n.attributes, function (a) {
                return !MATH_ATTR.test(a.name) || (a.name === 'style' && !/^[-a-z0-9:; .,%]+$/i.test(a.value));
              });
          })) {
        span.appendChild(doc.createTextNode(word('formula-in-source')));
        return;
      }
      if (p[1]) {
        var box = element('span', 'math-long');
        box.appendChild(math);
        span.appendChild(box);
      } else {
        span.appendChild(math);
      }
    });
    return span;
  }
  function snippetOf(u, marks, maxChars) {
    var ps = pieces(u.bodyEl || u.el, u.skip);
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
    var end = Math.min(flat.length, start + (maxChars || 220));
    if (end < flat.length) { var sp = flat.lastIndexOf(' ', end); if (sp > start + (maxChars ? Math.floor(maxChars / 2) : 120)) end = sp; }
    var span = element('span', 'reader-hit-text');
    if (start > 0) span.appendChild(doc.createTextNode('…'));
    ps.forEach(function (p) {
      if (p.e <= start || p.s >= end || p.s === p.e) return;
      if (p.math) { span.appendChild(mathCopy(p.math)); return; }
      span.appendChild(doc.createTextNode(p.t.slice(Math.max(0, start - p.s), Math.min(p.t.length, end - p.s))));
    });
    if (end < flat.length) span.appendChild(doc.createTextNode('…'));
    return highlight(span, marks);
  }
  /* The search words in the place a result led to, drawn with the CSS Highlight API; the text itself is unchanged. */
  var canHighlight = !!(window.CSS && CSS.highlights && typeof window.Highlight === 'function');
  function markWords(el, marks) {
    if (!canHighlight) return;
    try {
      CSS.highlights.delete('reader-find');
      if (!el || !marks || !marks.length) return;
      var h = new Highlight();
      (function walk(n) {
        if (n.nodeType === 3) {
          rangesIn(n.nodeValue, marks).forEach(function (r) {
            var range = doc.createRange();
            range.setStart(n, r[0]);
            range.setEnd(n, r[1]);
            h.add(range);
          });
          return;
        }
        if (n.nodeType !== 1 || n.localName === 'math' || n.localName === 'svg') return;
        for (var c = n.firstChild; c; c = c.nextSibling) walk(c);
      })(el);
      CSS.highlights.set('reader-find', h);
    } catch (e) { /* no highlight: the place is still reached */ }
  }

  /* The search units. In a chapter: the chapter, each section (by its title), each definition, result and figure, and
     each paragraph, list item, quotation, table row or display formula outside those. In the reference: each unit a
     component offers ([data-qh-unit]), each glossary entry, and otherwise each heading and block, as in a chapter. */
  var KIND = { definition: 6, gloss: 5, result: 5, chapter: 4, section: 4, figure: 3, unit: 2, heading: 2, text: 1 };
  var STRUCT = 'p, li, dd, dt, blockquote, pre, tr, figcaption';
  var DISPLAY = '.math-display, math[display="block"]';
  var NOT_TEXT = 'figure[data-figure], [data-prerequisites], [data-chapter-kicker], [data-chapter-end], ' +
                 'nav, h1, h2, h3, h4, h5, h6, [data-block-title], .reader-notices, script, style, template, [data-reader-skip]';
  /* A block whose only words are links to places of this page (an entry of a chapter's own contents) is navigation,
     like a nav list; the places it links to are found as themselves. */
  function linkOnly(b) {
    var links = all('a[href^="#"]', b);
    if (!links.length) return false;
    if (!links.every(function (a) { return !!doc.getElementById(decode(a.getAttribute('href').slice(1))); })) return false;
    var rest = b.cloneNode(true);
    all('a[href^="#"]', rest).forEach(function (n) { n.parentNode.removeChild(n); });
    return !textOf(rest).replace(/[\s·,;:.–—-]+/g, '');
  }
  function textBlocks(scope, extraSkip) {
    // Reference witnesses keep their own paragraphs and addresses inside the counterexample that cites them.
    var skip = (isPart(scope) ? '' : ENV + ', ') + NOT_TEXT + (extraSkip ? ', ' + extraSkip : '');
    var list = all(STRUCT + ', ' + DISPLAY, scope).filter(function (b) {
      if (b.closest(skip) && b.closest(skip) !== scope && scope.contains(b.closest(skip))) return false;
      if (b.matches(DISPLAY)) return !(b.parentNode && b.parentNode.closest(STRUCT) && scope.contains(b.parentNode.closest(STRUCT))) &&
        !(b.localName === 'math' && b.parentNode && b.parentNode.closest('.math-display'));
      if (b.querySelector(STRUCT)) return false;
      return !!textOf(b) || !!b.querySelector('math');
    });
    return list;
  }
  function addUnit(list, el, o) {
    var titleText = o.titleEl ? headingText(o.titleEl) : (o.title || ''); /* a number set apart stays apart from the words */
    var bodyEl = o.bodyEl || el;
    var body = o.body != null ? o.body : textOf(bodyEl, o.skip);
    var context = o.context || '';
    var record = el.closest(REFERENCE) && el.closest('[data-env], [data-index-env], [data-status]');
    var env = o.env || (record && (record.getAttribute('data-index-env') || record.getAttribute('data-env'))) || undefined;
    var status = o.status || (record && record.getAttribute('data-status')) || (env === 'counterexample' ? 'refuted-form' : undefined);
    list.push({
      env: env, status: status, classification: envWords(env, status),
      el: el, anchor: o.anchor || el, group: o.group, kind: o.kind, titleEl: o.titleEl || null, title: titleText, body: body,
      name: o.name ? fold(o.name) : '', context: context, where: o.where || '', whereEl: o.whereEl || null, skip: o.skip || null, bodyEl: o.bodyEl || null, snippetSources: o.snippetSources || null,
      ft: fold(titleText), fb: fold(body), fc: fold(context), keys: titleKeys(fold(titleText)),
      defs: o.defs || [],
      ro: (titleText + ' ' + body).toLowerCase(), raw: (titleText + ' ' + context + ' ' + body).toLowerCase(),
      ttex: texNorm(texOf(o.titleEl)),
      /* a unit given its words (a chapter or section by its title) holds only those formulae, not its whole place's */
      tex: texNorm((o.tex != null ? o.tex : o.body != null && !o.bodyEl ? '' : texOf(bodyEl, o.skip)) + ' ' + texOf(o.titleEl))
    });
  }
  /* A title compared whole with the query: as written, without its closing stop, after its label ("Theorem 6.3."),
     and its name in brackets ("(Bar–cobar equivalence)"). */
  function titleKeys(ft) {
    var t = ft.replace(/[.:;,\s]+$/, '');
    if (!t) return [];
    var out = [t];
    var m = /^[^:()]*?[:.]\s+(.+)$/.exec(t);
    if (m) out.push(m[1].replace(/[.:;,\s]+$/, ''));
    var b = /\(([^()]+)\)$/.exec(t);
    if (b) out.push(b[1].trim());
    return out;
  }
  /* A paragraph that begins with a bold lead-in is titled by it; its bold and defined words are the terms it
     introduces, so that a search for one of them finds where it is introduced first. */
  function leadOf(b) {
    for (var n = b.firstChild; n; n = n.nextSibling) {
      if (n.nodeType === 3 && !n.nodeValue.trim()) continue;
      return n.nodeType === 1 && /^(strong|b)$/.test(n.localName) ? n : null;
    }
    return null;
  }
  function definedIn(b) {
    return all('strong, b, dfn', b).map(function (n) { return fold(textOf(n)).replace(/[.:;,\s]+$/, ''); }).filter(Boolean);
  }
  /* The address of a block found by the search: its own id; else the id of the element that holds it alone (a
     formula's numbered display, a gloss), so that the author's address is used; else one given here. */
  function anchorFor(b) {
    if (b.id) return b;
    var up = b.parentNode;
    if (up && up.nodeType === 1 && up.id && !isChapter(up) && !isPart(up) && !isSection(up)) {
      var blocks = all(STRUCT + ', ' + DISPLAY, up).filter(function (n) { return n !== b && !b.contains(n) && !n.contains(b); });
      if (!blocks.length) return up;
    }
    give(b);
    return b;
  }
  function sectionContext(b, place) {
    var s = sectionOf(b);
    return s && place.contains(s) ? headingText(sectionHeading(s)) : '';
  }
  function sectionHeadingIn(b, place) {
    var s = sectionOf(b);
    return s && place.contains(s) ? sectionHeading(s) : null;
  }
  function passageUnit(list, b, anchor, ch) {
    if (linkOnly(b)) return;
    var ctx = sectionContext(b, ch);
    var lead = b.localName === 'p' ? leadOf(b) : null;
    addUnit(list, b, { kind: 'text', group: ch.id, context: ctx, where: ctx, whereEl: sectionHeadingIn(b, ch),
                       titleEl: lead, defs: definedIn(b), anchor: anchor });
  }
  function environmentUnits(list, place) {
    all(ENV, place).forEach(function (b) {
      var title = blockTitle(b);
      var proof = b.matches(PROOF);
      // Older unlabelled proof containers remain searchable at their original passage addresses.
      var passages = proof ? textBlocks(b) : [];
      if (proof && !title) {
        passages.forEach(function (p) { passageUnit(list, p, anchorFor(p), place); });
        return;
      }
      give(b);
      var parts = passages.map(function (p) { return { block: p, anchor: anchorFor(p) }; })
        .filter(function (p) { return p.anchor !== b; });
      var kind = envKind(b);
      var dfn = b.querySelector('dfn');
      var ctx = sectionContext(b, place);
      // A long proof has a named entry and its individually addressable paragraphs and equations.
      addUnit(list, b, { kind: kind, env: kind, status: b.getAttribute('data-status'), group: place.id,
                         titleEl: title, bodyEl: parts.length ? title : b, skip: ENV,
                         name: dfn ? textOf(dfn) : '', defs: kind === 'definition' ? definedIn(b) : [],
                         context: ctx, where: ctx, whereEl: sectionHeadingIn(b, place) });
      parts.forEach(function (p) { passageUnit(list, p.block, p.anchor, place); });
    });
  }
  function chapterJob(ch) {
    return function (list) {
      var g = ch.id;
      var kicker = ch.querySelector('[data-chapter-kicker]');
      addUnit(list, ch, { kind: 'chapter', group: g, titleEl: chapterNameEl(ch), body: kicker ? textOf(kicker) : '', anchor: ch });
      sectionMarks(ch).forEach(function (s) {
        give(s);
        addUnit(list, s, { kind: 'section', group: g, titleEl: sectionHeading(s), body: '', context: '' });
      });
      all('h4[id][data-reader-search-heading]', ch).forEach(function (h) {
        addUnit(list, h, { kind: 'heading', group: g, titleEl: h, body: '',
                          context: sectionContext(h, ch), where: sectionContext(h, ch),
                          whereEl: sectionHeadingIn(h, ch) });
      });
      environmentUnits(list, ch);
      all('figure[data-figure]', ch).forEach(function (f) {
        give(f);
        var cap = f.querySelector('figcaption');
        var labels = all('svg text', f).map(function (n) { return n.textContent; }).join(' ');
        addUnit(list, f, { kind: 'figure', group: g, titleEl: blockTitle(f), bodyEl: cap || f,
                           body: textOf(f, 'button, input, select, textarea, [aria-hidden="true"]') + ' ' + labels,
                           context: sectionContext(f, ch), where: sectionContext(f, ch), whereEl: sectionHeadingIn(f, ch) });
      });
      textBlocks(ch).forEach(function (b) {
        var anchor = anchorFor(b); /* every block keeps the address it had, in the same order, results or not */
        passageUnit(list, b, anchor, ch);
      });
    };
  }
  var UNIT = '[data-qh-unit]';
  function referenceJobs(ref) {
    var g = ref.id;
    var offered = all(UNIT, ref);
    if (offered.length) {
      /* A component's units, a few hundred at a time so that a large reference never holds the page for long. */
      var jobsList = [];
      for (var i = 0; i < offered.length; i += 150) {
        (function (slice) {
          jobsList.push(function (list) {
            slice.forEach(function (u) {
              if (!u.id) return;
              var t = u.getAttribute('data-qh-unit-title');
              var head = t ? null : u.querySelector('h2, h3, h4, h5, h6, [data-block-title]');
              addUnit(list, u, { kind: 'unit', status: u.getAttribute('data-qh-unit-status'), group: g, title: t || '', titleEl: head, skip: UNIT,
                                 context: u.getAttribute('data-qh-unit-place') || '', where: u.getAttribute('data-qh-unit-place') || '' });
            });
          });
        })(offered.slice(i, i + 150));
      }
      return jobsList;
    }
    return [function (list) {
      all('.failure[data-env="counterexample"][id]', ref).forEach(function (b) {
        var title = b.querySelector('.claim-text');
        if (title) addUnit(list, b, { kind: 'counterexample', group: g, titleEl: title, bodyEl: title });
      });
      all('dl > dt, dl > div > dt', ref).forEach(function (dt) {
        var host = dt.parentNode.localName === 'div' && dt.parentNode.id ? dt.parentNode : dt;
        give(host);
        var definitions = [];
        for (var n = dt.nextElementSibling; n && n.localName === 'dd'; n = n.nextElementSibling) definitions.push(n);
        addUnit(list, host, { kind: 'gloss', group: g, titleEl: dt, name: textOf(dt), snippetSources: definitions,
                             body: definitions.map(function (d) { return textOf(d); }).join(' '),
                             tex: definitions.map(function (d) { return texOf(d); }).join(' ') });
      });
      all('[data-gloss], div[data-term]', ref).forEach(function (b) {
        give(b);
        var dfn = b.querySelector('dfn, dt');
        addUnit(list, b, { kind: 'gloss', env: 'definition', group: g, titleEl: blockTitle(b) || dfn, name: dfn ? textOf(dfn) : '' });
      });
      var own = referenceHeading(ref);
      all('h2, h3, h4, h5, h6', ref).forEach(function (h) {
        if (h === own || h.closest('[data-gloss], [data-term], dl')) return;
        var host = h.id ? h : h.parentNode.closest('[id]');
        if (!host || !ref.contains(host) && host !== ref) return;
        addUnit(list, host, { kind: 'heading', group: g, titleEl: h, body: '' });
        if (h.matches('.question-head h3')) {
          var card = h.closest('.question');
          var question = card && card.querySelector('.question-ask > .statement[data-env][id]');
          // The question and its card can share one printed title while keeping two addresses.
          if (question && !question.querySelector('.statement-title'))
            addUnit(list, question, { kind: 'heading', group: g, titleEl: h, body: '' });
        }
      });
      textBlocks(ref, 'dl > dt, dl > dd, dl > div > dt, dl > div > dd, [data-gloss], div[data-term], section[data-term]').forEach(function (b) {
        var anchor = anchorFor(b);
        if (linkOnly(b)) return;
        addUnit(list, b, { kind: 'text', group: g, context: '', where: '', anchor: anchor });
      });
    }];
  }
  function introductionJob(list) {
    environmentUnits(list, front);
    all('.mg-front-abstract, .mg-front-intro', front).forEach(function (region) {
      var title = region.getAttribute('aria-label') || word('kind-introduction');
      var headings = all('h2[id], h3[id], h4[id], h5[id], h6[id]', region).filter(function (h) {
        return !h.closest(ENV + ', figure, nav, [data-reader-skip]');
      });
      if (region.id && !headings.length) {
        addUnit(list, region, { kind: 'heading', group: front.id, title: title, body: '' });
      }
      headings.forEach(function (h) {
        addUnit(list, h, { kind: 'heading', group: front.id, titleEl: h, body: '',
                           anchor: h.querySelector('#introduction') || h });
      });
      var next = 0, heading = null;
      textBlocks(region, 'figure, nav, [data-reader-skip]').forEach(function (b) {
        if (linkOnly(b)) return;
        while (next < headings.length && (headings[next].compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING)) {
          heading = headings[next++];
        }
        var where = heading ? headingText(heading) : title;
        var anchor = b.id ? b : b.closest('.mg-display[id]') || b;
        give(anchor);
        addUnit(list, b, { kind: 'text', group: front.id, anchor: anchor, titleEl: b.localName === 'p' ? leadOf(b) : null,
                           defs: definedIn(b), context: where, where: where, whereEl: heading });
      });
      all('figure[id]', region).forEach(function (figure) {
        var caption = figure.querySelector('figcaption');
        if (caption) addUnit(list, figure, { kind: 'figure', group: front.id, titleEl: blockTitle(figure), bodyEl: caption });
      });
    });
  }
  function jobsFor(place) {
    if (place === front) return [introductionJob];
    return isChapter(place) ? [chapterJob(place)] : referenceJobs(place);
  }

  var units = null;
  var pending = null;
  var building = [];
  function jobs() {
    var list = [];
    if (front) list.push(introductionJob);
    places.forEach(function (p) { list = list.concat(jobsFor(p)); });
    return list;
  }
  /* The units are built when they are first asked for (the search opening, or a script asking with qh:reader-units),
     never while the page loads or is read: on a telephone that work would hold back the painting of the page being
     scrolled. */
  function index() {
    if (units) return units;
    if (!pending) { building = []; pending = jobs(); }
    while (pending.length) pending.shift()(building);
    units = building.concat(remoteUnits());
    pending = null;
    return units;
  }
  /* The other pages' places, from the companion index (loaded as a script when the search first opens):
     each unit as the reader built it in its own page, addressed in that page. */
  var remoteLoaded = false;
  var remoteFailed = false;
  var remoteGroups = {};
  function remoteUnits() {
    var data = window.QH_READER_INDEX;
    if (!pagesMap || !data || !Array.isArray(data.units)) return [];
    remoteLoaded = true;
    var out = [];
    data.units.forEach(function (x) {
      if (!x || typeof x.id !== 'string' || typeof x.page !== 'string' || doc.getElementById(x.group || '')) return;
      if (samePage(x.page)) return;
      if (!remoteGroups[x.group]) remoteGroups[x.group] = { kind: x.groupKind, title: x.groupTitle || '', number: x.groupNumber || '' };
      var title = x.title || '';
      var where = x.where || '';
      var body = x.text || '';
      out.push({ el: null, anchor: null, remote: true, href: x.page + '#' + encodeURIComponent(x.id), rid: x.id, group: x.group,
                 env: x.env, status: x.status, classification: envWords(x.env, x.status),
                 kind: x.kind || 'text', titleEl: null, title: title, body: body, name: fold(x.name || ''), context: where, where: where,
                 skip: null, bodyEl: null, bodyParts: x.bodyParts, titleParts: x.titleParts, whereParts: x.whereParts,
                 ft: fold(title), fb: fold(body), fc: fold(where), keys: titleKeys(fold(title)),
                 defs: Array.isArray(x.defs) ? x.defs : [], ro: (title + ' ' + body).toLowerCase(),
                 raw: (title + ' ' + where + ' ' + body).toLowerCase(), ttex: x.ttex || '', tex: x.tex || '' });
    });
    return out;
  }
  function loadIndex() {
    if (!pagesMap || !pagesMap.index || remoteLoaded || remoteFailed || window.QH_READER_INDEX) {
      if (window.QH_READER_INDEX && !remoteLoaded) { units = null; pending = null; }
      return;
    }
    if (doc.querySelector('script[data-reader-index]')) return;
    var sc = doc.createElement('script');
    sc.src = pagesMap.index;
    sc.async = true;
    sc.setAttribute('data-reader-index', '');
    sc.addEventListener('load', function () {
      units = null;
      pending = null;
      if (searchOpen && searchState.q.trim()) run();
    });
    sc.addEventListener('error', function () {
      remoteFailed = true;
      if (searchOpen && searchState.q.trim()) run();
    });
    (doc.head || doc.documentElement).appendChild(sc);
  }
  /* For the index's builder: this page's units as the search uses them (qh:reader-units, answered in its detail). */
  doc.addEventListener('qh:reader-units', function (event) {
    if (!event.detail || typeof event.detail !== 'object') return;
    event.detail.units = index().filter(function (u) { return !u.remote; }).map(function (u) {
      var g = doc.getElementById(u.group);
      var chapter = g && isChapter(g);
      return { id: give(u.anchor), group: u.group, groupKind: g === front ? 'front' : chapter ? 'chapter' : 'reference',
               groupTitle: g === front ? word('kind-introduction') : chapter ? chapterTitle(g) : headingText(referenceHeading(g)),
               groupNumber: chapter ? chapterNumber(g) : '', env: u.env, status: u.status,
               kind: u.kind, title: u.title, name: u.name, where: u.where, text: u.body || '', defs: u.defs, ttex: u.ttex, tex: u.tex,
               bodyParts: /^(chapter|section|heading)$/.test(u.kind) ? undefined :
                 snippetParts(u.snippetSources || [u.bodyEl || u.el], u.skip),
               titleParts: u.titleEl ? snippetParts([inlineCopy(u.titleEl)]) : undefined,
               whereParts: u.whereEl ? snippetParts([inlineCopy(u.whereEl)]) : undefined };
    });
  });
  /* The panel: a field, the scopes (all, the chapters, each part of the reference) with their counts, a line that says
     how many results there are, and the results by place: the chapters in the book's order first, then the reference.
     Each place shows its first few results and offers the rest. */
  var panel = element('div', 'reader-search');
  panel.id = 'reader-search';
  panel.setAttribute('role', 'search');
  panel.hidden = true;
  var fieldRow = panel.appendChild(element('div', 'reader-search-field'));
  var searchLabel = fieldRow.appendChild(element('label', 'reader-search-label', word('search-label')));
  searchLabel.htmlFor = 'reader-q';
  var input = fieldRow.appendChild(element('input', 'reader-search-input'));
  input.type = 'search';
  input.id = 'reader-q';
  input.setAttribute('autocomplete', 'off');
  input.setAttribute('spellcheck', 'false');
  input.setAttribute('enterkeyhint', 'search');
  input.setAttribute('aria-controls', 'reader-results');
  input.setAttribute('aria-describedby', 'reader-search-status');
  input.placeholder = word('search-placeholder');
  var panelClose = fieldRow.appendChild(element('button', 'reader-search-close', word('close')));
  panelClose.type = 'button';
  var scopes = panel.appendChild(element('div', 'reader-search-scopes'));
  scopes.hidden = true;
  scopes.setAttribute('role', 'toolbar');
  scopes.setAttribute('aria-label', word('search-in'));
  var scopeIds = ['all'];
  if (chapters.length || (pagesMap && companion)) scopeIds.push('chapters');
  references.forEach(function (r) { scopeIds.push(r.id); });
  if (pagesMap) pagesMap.pages.forEach(function (pg) { (pg.parts || []).forEach(function (pt) { if (pt && pt.id && scopeIds.indexOf(pt.id) < 0 && !doc.getElementById(pt.id)) scopeIds.push(pt.id); }); });
  var scopeButtons = scopeIds.map(function (s, i) {
    var b = element('button', 'reader-scope');
    b.type = 'button';
    b.setAttribute('data-scope', s);
    b.setAttribute('aria-pressed', s === 'all' ? 'true' : 'false');
    b.tabIndex = i ? -1 : 0;
    b.appendChild(element('span', 'reader-scope-label', s === 'all' ? word('all') : s === 'chapters' ? word('chapters') : partLabel(s)));
    b.appendChild(doc.createTextNode(' '));
    b.appendChild(element('span', 'reader-scope-count'));
    scopes.appendChild(b);
    return b;
  });
  var statusLine = panel.appendChild(element('p', 'reader-search-status'));
  statusLine.id = 'reader-search-status';
  var news = panel.appendChild(element('p', 'reader-search-news'));
  news.setAttribute('role', 'status');
  news.setAttribute('aria-live', 'polite');
  var results = panel.appendChild(element('div', 'reader-results'));
  results.id = 'reader-results';
  results.hidden = true;
  bar.appendChild(panel);

  var searchState = { q: '', scope: 'all' };
  var expanded = {};
  var hits = [];
  var searchOpen = false;
  var returnTo = null;
  var STEP = 100;
  var newsTimer = null;
  var addressTimer = null;

  /* The chapters first, in the book's order (here or in the index), then this page's reference parts, then the other
     pages' parts in the map's order. */
  function groupOrder() {
    var order = chapters.map(function (c) { return c.id; });
    Object.keys(remoteGroups).filter(function (g) { return remoteGroups[g].kind === 'chapter' && order.indexOf(g) < 0; })
      .sort(function (a, b) { return (+remoteGroups[a].number || 0) - (+remoteGroups[b].number || 0); })
      .forEach(function (g) { order.push(g); });
    if (front) order.push(front.id);
    references.forEach(function (r) { if (order.indexOf(r.id) < 0) order.push(r.id); });
    if (pagesMap) pagesMap.pages.forEach(function (pg) { (pg.parts || []).forEach(function (pt) { if (pt && pt.id && order.indexOf(pt.id) < 0) order.push(pt.id); }); });
    Object.keys(remoteGroups).forEach(function (g) { if (order.indexOf(g) < 0) order.push(g); });
    return order;
  }
  function remotePartTitle(g) {
    var t = '';
    if (pagesMap) pagesMap.pages.forEach(function (pg) { (pg.parts || []).forEach(function (pt) { if (pt && pt.id === g && pt.title) t = pt.title; }); });
    return t || (remoteGroups[g] && remoteGroups[g].title) || g;
  }
  function scopeOfGroup(g) {
    var p = doc.getElementById(g);
    if ((p && p === front) || (remoteGroups[g] && remoteGroups[g].kind === 'front')) return 'chapters';
    if (p) return isChapter(p) ? 'chapters' : g;
    return remoteGroups[g] && remoteGroups[g].kind === 'chapter' ? 'chapters' : g;
  }
  /* A part's name in the book's own reference mode: what the page's bar or its contents call it ("Atlas and
     reference", "Atlas"), else its title in the map, else its heading. */
  function partLabel(id) {
    var named = '';
    all('[data-reader-bar] a[href], [data-reader-toc] a[href]').some(function (a) {
      if (/(^| )reader-/.test(a.className) || a.closest('.reader-search')) return false;
      var h = a.getAttribute('href') || '';
      var at = h.indexOf('#');
      if (at < 0 || decode(h.slice(at + 1)) !== id) return false;
      named = textOf(a);
      return !!named;
    });
    if (named) return named;
    var p = doc.getElementById(id);
    return p ? headingText(referenceHeading(p)) : remotePartTitle(id);
  }
  function groupWhere(g) {
    var p = doc.getElementById(g);
    if (p && p === front) return word('kind-introduction');
    if (p) return isChapter(p) ? fill(word('chapter'), { n: chapterNumber(p) }) : partLabel(g);
    var r = remoteGroups[g];
    return r && r.kind === 'chapter' ? fill(word('chapter'), { n: r.number }) : partLabel(g);
  }
  function groupTitle(g) {
    var p = doc.getElementById(g);
    if (p) return isChapter(p) ? chapterTitle(p) : '';
    var r = remoteGroups[g];
    return r && r.kind === 'chapter' ? r.title : '';
  }
  function tell(text) {
    clearTimeout(newsTimer);
    newsTimer = setTimeout(function () { if (news.textContent !== text) news.textContent = text; }, 700);
  }
  function limitFor(g) {
    if (expanded[g]) return expanded[g];
    if (searchState.scope === 'all') return 3;
    if (searchState.scope === 'chapters') return 10;
    return STEP;
  }
  function rankSort(a, b) {
    return b.exact - a.exact || b.own - a.own || b.tier - a.tier || b.kind - a.kind || b.score - a.score || a.order - b.order;
  }
  /* Link names are text. Give them the exact TeX instead of the formula's concatenated leaves.
     The visible MathML stays in the accessibility tree for mathematical navigation. */
  function appendHitPart(link, part, id, remote) {
    part.id = id;
    link.appendChild(part);
    if (!remote || !part.querySelector('math')) return id;
    var text = pieces(part).map(function (p) {
      if (!p.math) return p.text;
      var tex = p.math.querySelector('annotation[encoding="application/x-tex"]');
      return tex ? ' ' + fill(word('formula-as-tex'), { tex: tex.textContent.trim() }) + ' ' :
        ' ' + word('formula-in-source') + ' ';
    }).join('').replace(/\s+/g, ' ').trim();
    var label = element('span', null, text);
    label.id = id + '-label';
    label.hidden = true;
    link.appendChild(label);
    return label.id;
  }
  function hitLink(h, n, marks, terms) {
    var u = h.unit;
    var li = element('li', 'reader-hit');
    var a = element('a', 'reader-hit-link');
    if (u.remote) a.href = u.href; else a.href = '#' + give(u.anchor);
    a.setAttribute('data-hit', String(n));
    if (u.remote && !u.bodyEl) u.bodyEl = readSnippet(u.bodyParts, u.body, !!u.tex);
    var ids = 'reader-hit-' + n;
    var labelled = [];
    var lead = h.best ? groupWhere(u.group) + (groupTitle(u.group) ? ' · ' + groupTitle(u.group) : '') : '';
    var plain = textOf(u.bodyEl || u.el, u.skip, true);
    var inFormula = terms.some(function (t) { return !inWords(u, t, plain); });
    var kindWord = envLabel(u.env, u.status) || (WORDS['kind-' + u.kind] ? word('kind-' + u.kind) : '');
    if (u.env) a.setAttribute('data-hit-env', u.env);
    if (u.status) a.setAttribute('data-hit-status', u.status);
    var whereText = u.where || '';
    var w = element('span', 'reader-hit-where');
    var parts = [];
    if (kindWord) parts.push(element('span', 'reader-hit-kind', kindWord));
    if (lead) parts.push(highlight(element('span', null, lead), marks));
    if (!u.remote && u.whereEl) parts.push(highlight(inlineCopy(u.whereEl), marks));
    else if (whereText) parts.push(highlight(readSnippet(u.whereParts, whereText, false), marks));
    if (inFormula) parts.push(element('span', 'reader-hit-formula', word('in-formula')));
    parts.forEach(function (n, k) { if (k) w.appendChild(doc.createTextNode(' · ')); w.appendChild(n); });
    var whereId = parts.length ? appendHitPart(a, w, ids + '-where', u.remote) : '';
    if (u.titleEl || u.title) {
      var t = u.titleEl ? inlineCopy(u.titleEl) : readSnippet(u.titleParts, u.title, !!u.ttex);
      t.className = 'reader-hit-title';
      labelled.push(appendHitPart(a, highlight(t, marks), ids + '-title', u.remote));
    }
    var snip = null;
    if (u.kind === 'chapter' || u.kind === 'section') {
      /* a chapter or a section is shown with its first paragraph, as written */
      var first = u.remote ? null : isChapter(u.el) ? firstParagraph(u.el) : isSection(u.el) ? firstParagraph(u.el) : /^h[1-6]$/.test(u.el.localName) ? firstParagraphAfter(u.el) : null;
      if (first) snip = snippetOf({ el: first, bodyEl: first, skip: null }, marks);
    } else if (u.kind !== 'heading') snip = snippetOf(u, marks);
    if (snip) {
      var snippetId = appendHitPart(a, snip, ids + '-text', u.remote);
      if (labelled.length) a.setAttribute('aria-describedby', snippetId); else labelled.push(snippetId);
    }
    if (whereId) labelled.push(whereId);
    a.setAttribute('aria-labelledby', labelled.join(' '));
    li.appendChild(a);
    return li;
  }
  function run() {
    var terms = parseQuery(searchState.q);
    var typed = terms.map(function (t) { return t.kind === 'text' ? t.w : t.raw; }).join('').replace(/[^\p{L}\p{N}\p{S}]/gu, '');
    var tooShort = !!searchState.q.trim() && !/[^\x00-\x7f]/.test(typed) && typed.length < 2;
    results.textContent = '';
    hits = [];
    markWords(null);
    scopeButtons.forEach(function (b) {
      b.setAttribute('aria-pressed', b.getAttribute('data-scope') === searchState.scope ? 'true' : 'false');
      b.querySelector('.reader-scope-count').textContent = '';
      b.removeAttribute('data-none');
    });
    if (!searchState.q.trim() || tooShort || !terms.length) {
      scopes.hidden = true; /* no scope to choose before there are results */
      results.hidden = true;
      statusLine.textContent = tooShort ? word('too-short') : '';
      tell(statusLine.textContent);
      return;
    }
    var exact = fold(searchState.q.replace(/["“”„‟«»]/g, '')).replace(/\s+/g, ' ').trim();
    var phrase = phraseOf(terms);
    var perGroup = {};
    var perScope = { all: 0 };
    var best = [];
    index().forEach(function (u, i) {
      var score = 0;
      for (var k = 0; k < terms.length; k++) {
        var w = weigh(u, terms[k]);
        if (!w) return;
        score += w;
      }
      var isExact = exact && (u.keys.indexOf(exact) >= 0 || u.name === exact || u.defs.indexOf(exact) >= 0) ? 1 : 0;
      var own = terms.every(function (t) { return ownHas(u, t); }) ? 1 : 0;
      var tier = !phrase || !own ? 0 : together(u.ft, phrase) ? 2 : together(u.fb, phrase) ? 1 : 0;
      var h = { unit: u, score: score, own: own, tier: tier, exact: isExact, kind: KIND[u.kind] || (u.env ? KIND.result : 0), order: i };
      var sc = scopeOfGroup(u.group);
      perScope.all++;
      perScope[sc] = (perScope[sc] || 0) + 1;
      if (searchState.scope !== 'all' && searchState.scope !== sc) return;
      (perGroup[u.group] = perGroup[u.group] || []).push(h);
      if (isExact) best.push(h);
    });
    /* Only the scopes that hold results are offered, with All and the one pressed; the results come first on a narrow
       screen instead of a row of empty scopes. */
    var tabStop = null;
    scopeButtons.forEach(function (b) {
      var sid = b.getAttribute('data-scope');
      var n = perScope[sid] || 0;
      b.querySelector('.reader-scope-count').textContent = String(n);
      if (!n) b.setAttribute('data-none', '');
      b.hidden = !(n > 0 || sid === 'all' || sid === searchState.scope);
      if (!b.hidden && b.tabIndex === 0) tabStop = b;
    });
    if (!tabStop) {
      tabStop = scopeButtons.filter(function (b) { return !b.hidden && b.getAttribute('aria-pressed') === 'true'; })[0] || scopeButtons[0];
      scopeButtons.forEach(function (b) { b.tabIndex = b === tabStop ? 0 : -1; });
    }
    scopes.hidden = false;
    var total = searchState.scope === 'all' ? perScope.all : perScope[searchState.scope] || 0;
    statusLine.textContent = (total === 0 ? word('none') : total === 1 ? word('one') : fill(word('many'), { n: total })) +
      (remoteFailed ? ' ' + word('index-failed') : '');
    tell(statusLine.textContent);
    results.hidden = total === 0;
    var marks = marksOf(terms);
    var order = groupOrder();
    if (best.length && searchState.scope === 'all' && total > 1) {
      best.sort(function (a, b) { return order.indexOf(a.unit.group) - order.indexOf(b.unit.group) || rankSort(a, b); });
      var bg = element('div', 'reader-group');
      bg.setAttribute('data-group', 'best');
      var bh = bg.appendChild(element('p', 'reader-group-head'));
      bh.id = 'reader-group-best';
      bh.appendChild(element('span', 'reader-group-where', word('best')));
      var bl = bg.appendChild(element('ol', 'reader-hits'));
      bl.setAttribute('aria-labelledby', bh.id);
      best.slice(0, 3).forEach(function (h) {
        var copy = { unit: h.unit, best: true };
        hits.push(copy);
        bl.appendChild(hitLink(copy, hits.length - 1, marks, terms));
      });
      results.appendChild(bg);
    }
    order.forEach(function (g) {
      var list = perGroup[g];
      if (!list) return;
      list.sort(rankSort);
      var limit = limitFor(g);
      var box = element('div', 'reader-group');
      box.setAttribute('data-group', g);
      var head = box.appendChild(element('p', 'reader-group-head'));
      head.id = 'reader-group-' + g;
      head.appendChild(element('span', 'reader-group-where', groupWhere(g)));
      var gt = groupTitle(g);
      if (gt) { head.appendChild(doc.createTextNode(' ')); head.appendChild(element('span', 'reader-group-title', gt)); }
      head.appendChild(doc.createTextNode(' '));
      head.appendChild(element('span', 'reader-group-count', String(list.length)));
      var ol = box.appendChild(element('ol', 'reader-hits'));
      ol.setAttribute('aria-labelledby', head.id);
      list.slice(0, limit).forEach(function (h) {
        hits.push(h);
        ol.appendChild(hitLink(h, hits.length - 1, marks, terms));
      });
      if (list.length > limit) {
        var more = box.appendChild(element('button', 'reader-group-more',
          fill(word('more-in'), { k: Math.min(STEP, list.length - limit), where: groupWhere(g) })));
        more.type = 'button';
        more.setAttribute('data-group', g);
        more.setAttribute('data-shown', String(limit));
      }
      results.appendChild(box);
    });
  }
  /* The query is kept in this entry's address (?q=), so that it can be shared and survives a reload. */
  function recordQuery() {
    clearTimeout(addressTimer);
    addressTimer = setTimeout(function () {
      replaceEntry(stateWith({ q: searchState.q, scope: searchState.scope, panel: searchOpen ? 1 : 0 }),
                   urlFor(hashId(), searchOpen ? searchState.q.trim() : null));
    }, 350);
  }
  function openSearch(from, q, o) {
    o = o || {};
    closePeek(false);
    if (drawerOpen) closeDrawer(false);
    if (!searchOpen) returnTo = from || doc.activeElement;
    searchOpen = true;
    panel.hidden = false;
    searchButton.setAttribute('aria-expanded', 'true');
    bar.setAttribute('data-search-open', '');
    if (typeof q === 'string') {
      input.value = q;
      searchState.q = q;
      if (o.scope && scopeIds.indexOf(o.scope) >= 0) searchState.scope = o.scope;
      expanded = {};
    }
    loadIndex();
    index();
    run();
    if (o.record !== false) recordQuery();
    if (o.focus !== false) { input.focus(); if (input.select && typeof q !== 'string') input.select(); }
  }
  function closeSearch(returnFocus, record) {
    if (!searchOpen) return;
    searchOpen = false;
    panel.hidden = true;
    searchButton.setAttribute('aria-expanded', 'false');
    bar.removeAttribute('data-search-open');
    if (record !== false) {
      clearTimeout(addressTimer);
      var id = hashId();
      // An issued bookmark may carry a query while its notice is behind this panel.
      // Closing the panel makes the notice available without erasing its return address.
      if (predecessor(id)) replaceEntry(stateWith({ panel: 0 }));
      else replaceEntry(stateWith({ panel: 0 }), urlFor(id, null));
    }
    if (returnFocus) {
      var back = returnTo;
      returnTo = null;
      if (back && back.isConnected && reachable(back) && back !== doc.body) focusQuietly(back); else searchButton.focus();
    }
  }
  function openHit(h, link) {
    if (!h) return;
    var u = h.unit;
    if (u.remote) {
      clearTimeout(addressTimer);
      leaveFor(u.href, 'assign', link, { q: searchState.q, scope: searchState.scope, panel: 1, hit: u.rid, focus: null });
      return;
    }
    var id = give(u.anchor);
    var keepState = { q: searchState.q, scope: searchState.scope, panel: 1, hit: id, focus: null };
    clearTimeout(addressTimer);
    closeSearch(false, false);
    returnTo = null;
    go(id, { push: true, from: link, extra: keepState, marks: marksOf(parseQuery(searchState.q)) });
  }
  function focusHit(id) {
    var a = id ? all('.reader-hit-link', results).filter(function (l) {
      var h = l.getAttribute('href') || '';
      return h === '#' + id || decode(h.slice(h.indexOf('#') + 1)) === id;
    })[0] : null;
    if (a) a.focus(); else input.focus();
  }
  searchButton.addEventListener('click', function () { if (searchOpen) closeSearch(true); else openSearch(searchButton); });
  panelClose.addEventListener('click', function () { closeSearch(true); });
  var typingTimer = null;
  input.addEventListener('input', function () {
    clearTimeout(typingTimer);
    typingTimer = setTimeout(function () { searchState.q = input.value; expanded = {}; run(); recordQuery(); }, 90);
  });
  input.addEventListener('keydown', function (event) {
    if (event.key === 'ArrowDown' || event.key === 'Enter') {
      if (event.key === 'Enter' && searchState.q !== input.value) {
        clearTimeout(typingTimer);
        searchState.q = input.value;
        expanded = {};
        run();
        recordQuery();
      }
      var first = results.querySelector('.reader-hit-link');
      if (first) { event.preventDefault(); first.focus(); }
    } else if (event.key === 'Escape') {
      event.preventDefault();
      event.stopPropagation();
      closeSearch(true);
    }
  });
  scopes.addEventListener('click', function (event) {
    var b = event.target.closest('.reader-scope');
    if (!b) return;
    searchState.scope = b.getAttribute('data-scope');
    expanded = {};
    run();
    recordQuery();
  });
  scopes.addEventListener('keydown', function (event) {
    var shown = scopeButtons.filter(function (b) { return !b.hidden; });
    var i = shown.indexOf(event.target);
    if (i < 0 || event.altKey || event.ctrlKey || event.metaKey) return;
    var to = { ArrowRight: i + 1, ArrowDown: i + 1, ArrowLeft: i - 1, ArrowUp: i - 1, Home: 0, End: shown.length - 1 }[event.key];
    if (to === undefined) {
      if (event.key === 'Escape') { event.preventDefault(); event.stopPropagation(); closeSearch(true); }
      return;
    }
    event.preventDefault();
    shown[(to + shown.length) % shown.length].focus();
  });
  scopes.addEventListener('focusin', function (event) {
    if (scopeButtons.indexOf(event.target) < 0) return;
    scopeButtons.forEach(function (b) { b.tabIndex = b === event.target ? 0 : -1; });
  });
  results.addEventListener('click', function (event) {
    var more = event.target.closest('.reader-group-more');
    if (more) {
      var g = more.getAttribute('data-group');
      var had = +more.getAttribute('data-shown');
      expanded[g] = had + STEP;
      run();
      var box = all('.reader-group', results).filter(function (b) { return b.getAttribute('data-group') === g; })[0];
      var links = box ? all('.reader-hit-link', box) : [];
      if (links[had]) links[had].focus();
      return;
    }
    var a = event.target.closest('.reader-hit-link');
    if (!a || !plainClick(event)) return;
    event.preventDefault();
    openHit(hits[+a.getAttribute('data-hit')], a);
  });
  results.addEventListener('keydown', function (event) {
    var stops = all('.reader-hit-link, .reader-group-more', results);
    var i = stops.indexOf(event.target);
    if (i < 0) return;
    var to = null;
    if (event.key === 'ArrowDown') to = stops[i + 1] || null;
    else if (event.key === 'ArrowUp') to = i === 0 ? input : stops[i - 1];
    else if (event.key === 'Home') to = stops[0];
    else if (event.key === 'End') to = stops[stops.length - 1];
    else if (event.key === 'Escape') to = input;
    if (to) { event.preventDefault(); event.stopPropagation(); to.focus(); }
  });

  /* ------------------------------------------------------------------ the reader's place, kept on this device */

  var PLACE_KEY = 'qh-reader-place';
  function placeTitle(el) {
    var place = placeOf(el);
    if (!place || !isChapter(place)) return '';
    var t = fill(word('chapter'), { n: chapterNumber(place) }) + ' · ' + chapterTitle(place);
    if (el !== place && sectionHeading(el) && (isSection(el) || /^h[1-6]$/.test(el.localName))) t += ' · ' + headingText(sectionHeading(el));
    return t;
  }
  function savePlace() {
    if (view !== 'chapter' || !current) return;
    var el = sectionAtTop() || current;
    keep(PLACE_KEY, JSON.stringify({ id: el.id, title: placeTitle(el), at: Date.now() }));
  }
  function offerPlace() {
    var raw = stored(PLACE_KEY);
    if (!raw) return;
    var at = null;
    try { at = JSON.parse(raw); } catch (e) { at = null; }
    var el = at && typeof at.id === 'string' ? doc.getElementById(at.id) : null;
    if (!el || !placeOf(el) || !isChapter(placeOf(el))) return;
    if (typeof at.title === 'string' && at.title !== placeTitle(el)) return; /* the address names something else now */
    notice('resume', fill(word('resume'), { title: '“' + placeTitle(el) + '”' }), [{ text: word('resume-go'), href: '#' + el.id }],
           function () { keep(PLACE_KEY, null); });
  }

  /* ------------------------------------------------------------------ events */

  // Chromium writes a same-document fragment as a named PDF destination, even when its chapter is hidden.
  var paperLinks = null;
  window.addEventListener('beforeprint', function () {
    var canonical = doc.querySelector('link[rel~="canonical"][href]');
    if (paperLinks || !canonical) return;
    var publication = new URL(canonical.href);
    if (publication.protocol !== 'https:') return;
    var bookFile = bookHref || 'index.html';
    var ownFile = companion ? publication.pathname.split('/').pop() : bookFile;
    var printedURL = location.href.split('#')[0];
    paperLinks = [];
    all('a[href]', main).forEach(function (a) {
      var href = a.getAttribute('href');
      var hash = href.indexOf('#');
      if (hash < 0 || hash === href.length - 1 || a.hasAttribute('download') || a.closest('[hidden]')) return;
      var file = href.slice(0, hash);
      if (file && file !== bookFile && !(pagesMap && pagesMap.pages.some(function (p) { return p.href === file; }))) return;
      var fragment = href.slice(hash);
      var id = decode(fragment.slice(1));
      var target = (!file || file === ownFile) && doc.getElementById(id);
      var dest;
      if (target && !target.closest('[hidden]') && target.getClientRects().length &&
          window.getComputedStyle(target).visibility === 'visible') {
        dest = fragment;
      } else {
        file = file || (target ? ownFile : ownerOf(id));
        if (!file) return;
        var online = new URL(file === bookFile ? './' : file, publication).href;
        // Write the empty query literally: Chromium's URL.search setter discards it.
        dest = online + (online === printedURL ? '?' : '') + fragment;
      }
      if (dest !== href) {
        paperLinks.push([a, href, dest]);
        a.setAttribute('href', dest);
      }
    });
  });
  window.addEventListener('afterprint', function () {
    if (!paperLinks) return;
    paperLinks.forEach(function (row) {
      if (row[0].getAttribute('href') === row[2]) row[0].setAttribute('href', row[1]);
    });
    paperLinks = null;
  });

  doc.addEventListener('click', function (event) {
    if (event.defaultPrevented || !plainClick(event)) return;
    var term = event.target.closest && event.target.closest('button.term[data-term]');
    if (term && main.contains(term)) {
      var entry = doc.getElementById(term.getAttribute('data-term'));
      if (entry) {
        event.preventDefault();
        if (peekFrom === term && !peek.hidden) closePeek(true); else openPeek(term, true, entry);
      }
      return;
    }
    var a = event.target.closest && event.target.closest('a[href]');
    if (!a || peek.contains(a) || results.contains(a)) return;
    var href = a.getAttribute('href');
    /* A term, whether its definition is in this page or another: the definition opens and stays (a second press
       closes it). A click that ends a selection of the term's words keeps the selection. */
    if (isTerm(a) && main.contains(a)) {
      if (selectingIn(a)) { event.preventDefault(); return; }
      if (peekFrom === a && !peek.hidden && peekPinned) { event.preventDefault(); closePeek(true); return; }
      if (openPeek(a, true)) { event.preventDefault(); return; }
    }
    if (href.charAt(0) !== '#' && !a.hasAttribute('download') && !a.target && bookPage(a.href)) {
      /* Another page of the book (a component's link included): the entry left keeps the place. */
      event.preventDefault();
      leaveFor(a.href, 'assign', a);
      return;
    }
    if (a.closest('[data-atlas-mount]')) return; /* a component's own links: it follows the address itself */
    if (href.charAt(0) !== '#' || href === '#') return;
    var id = decode(href.slice(1));
    if (isReference(a)) {
      if (peekFrom === a && !peek.hidden && peekPinned) { event.preventDefault(); closePeek(true); return; }
      if (openPeek(a, true)) { event.preventDefault(); return; }
    }
    var t = resolve(id) || (Object.prototype.hasOwnProperty.call(redirects, id) ? resolve(redirects[id]) : null);
    if (!t) {
      if (predecessor(id)) { event.preventDefault(); go(id, { push: true, from: a }); return; }
      var away = externalHref(id);
      if (away) { event.preventDefault(); leaveFor(away, 'assign', a); return; }
      if (!main.contains(a) && !bar.contains(a) && !notices.contains(a)) return;
      event.preventDefault();
      unknownAddress(id, { from: a });
      return;
    }
    if (!ours(t)) return;
    if (a.hasAttribute('data-route')) setRoute(routeFrom(a));
    event.preventDefault();
    go(id, { push: true, from: a });
  });

  doc.addEventListener('keydown', function (event) {
    if (event.defaultPrevented) return;
    if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey && !editable(event.target)) {
      event.preventDefault();
      openSearch(event.target === doc.body ? null : event.target);
      return;
    }
    if (event.key !== 'Escape') return;
    if (!peek.hidden) { event.preventDefault(); closePeek(peekPinned || peek.contains(event.target) || event.target === peekFrom); return; }
    if (searchOpen) { event.preventDefault(); closeSearch(panel.contains(event.target) || event.target === searchButton); return; }
    if (drawerOpen) { event.preventDefault(); closeDrawer(true); }
  });

  function outside(event) {
    var t = event.target;
    if (!t || !t.closest) return;
    if (!peek.hidden && !peek.contains(t) && !(peekFrom && peekFrom.contains(t))) closePeek(false);
    if (searchOpen && !panel.contains(t) && !searchButton.contains(t)) closeSearch(false);
    if (drawerOpen && !toc.contains(t) && !(tocButton && tocButton.contains(t))) closeDrawer(false);
  }
  doc.addEventListener('pointerdown', outside);
  doc.addEventListener('mousedown', outside);

  var scrollFrame = false;
  var placeTimer = null;
  window.addEventListener('scroll', function () {
    if (!scrollFrame) {
      scrollFrame = true;
      later(function () {
        scrollFrame = false;
        trackSection();
        /* A reminder kept open follows its link. One shown on hover closes; a term's definition shown on hover or by
           keys stays while its term is on the screen (reaching a term by keys may itself scroll it into view). */
        if (!peek.hidden) {
          if (peekPinned || (peek.hasAttribute('data-term') && peekFrom && onScreen(peekFrom))) placePeek(); else closePeek(false);
        }
      });
    }
    saveEntrySoon();
    clearTimeout(placeTimer);
    placeTimer = setTimeout(savePlace, 700);
  }, { passive: true });
  window.addEventListener('resize', function () { later(function () { measureBar(); placePeek(); fitFormulas(); }); });
  window.addEventListener('pagehide', function () { savePlace(); });
  /* Back from another page of the book may show this page as it was left (the back-forward cache): its search too. */
  window.addEventListener('pageshow', function (event) {
    if (!event.persisted) return;
    var st = history.state && history.state.reader;
    if (st && st.panel && st.q) { openSearch(null, st.q, { focus: false, record: false, scope: st.scope }); focusHit(st.hit); }
  });

  window.addEventListener('popstate', function (event) {
    var st = event.state && event.state.reader;
    var id = hashId();
    var older = predecessor(id);
    if (older) {
      showPredecessor(id, older, { initial: true });
      var predecessorQuery = new URL(location.href).searchParams.get('q');
      if (predecessorQuery) openSearch(null, predecessorQuery, { focus: false, record: false, scope: st && st.scope });
      else if (searchOpen) closeSearch(false, false);
      return;
    }
    if (!st) {
      /* An address followed by the browser itself (typed, or a component's own link): taken as this entry's place. */
      if (id === lastId && (id ? ours(resolve(id)) : true)) { tellState(); return; }
      if (!id) { lastId = ''; show(null); replaceEntry(stateWith({ id: '', view: 'front' })); tellState(); return; }
      var t0 = resolve(id);
      var same = t0 && placeOf(t0) === current && t0.closest('[data-atlas-mount]');
      if (same) { lastId = id; replaceEntry(stateWith({ id: id, view: view })); tellState(); return; }
      go(id, { replace: true });
      return;
    }
    lastId = id;
    closePeek(false);
    if (drawerOpen) closeDrawer(false);
    dismiss(false);
    var t = id ? resolve(id) : null;
    var place = t && ours(t) ? placeOf(t) : null;
    var samePlace = place === current;
    show(place);
    if (t) markRevealed(t);
    if (st.panel && st.q) {
      if (searchOpen) closeSearch(false, false);
      restorePlace(st, false);
      openSearch(null, st.q, { focus: false, scope: st.scope, record: false });
      focusHit(st.hit);
      revealCellNote(t, { focus: false, scroll: false });
    } else {
      if (searchOpen) closeSearch(false, false);
      if (t && samePlace && t.closest('[data-atlas-mount]')) { /* the component follows the address itself */ }
      else if (!revealCellNote(t, {}) && !restorePlace(st, true)) arrive(t || front || toc || main, {});
    }
    later(trackSection);
    tellState();
  });
  window.addEventListener('hashchange', function () {
    var id = hashId();
    if (id === lastId) return;
    if (!id) { lastId = ''; show(null); tellState(); return; }
    go(id, { replace: true });
  });

  /* The browser's own find reaches a place not shown: the reader follows it there, and the browser scrolls to the match. */
  doc.addEventListener('beforematch', function (event) {
    var p = event.target;
    if (places.indexOf(p) < 0 && p !== front) return;
    if (p === current || (p === front && !current)) return;
    // Browsers also reveal hidden ancestors when following a fragment or traversing history.
    // That navigation already owns the entry and its specific destination inside this place.
    var target = resolve(hashId());
    if (target && p.contains(target)) {
      show(p === front ? null : p);
      return;
    }
    leaveEntry(null);
    var id = p === front ? (front.id || '') : p.id;
    pushEntry(stateWith({ id: id, view: p === front ? 'front' : isChapter(p) ? 'chapter' : 'reference' }, true), urlFor(id));
    lastId = id;
    closePeek(false);
    if (drawerOpen) closeDrawer(false);
    show(p === front ? null : p);
    tellState();
  }, true);

  doc.addEventListener('qh:navigate', function (event) {
    var id = event.detail && event.detail.id;
    if (typeof id !== 'string') return;
    var t = resolve(id) || (Object.prototype.hasOwnProperty.call(redirects, id) ? resolve(redirects[id]) : null);
    if (!t) {
      var away = externalHref(id);
      if (away) { event.preventDefault(); leaveFor(away, 'assign', event.target && event.target.nodeType === 1 ? event.target : null); }
      return;
    }
    if (!ours(t)) return;
    event.preventDefault();
    var from = event.target && event.target.nodeType === 1 ? event.target : null;
    go(id, { push: true, from: from });
  });
  doc.addEventListener('qh:content-changed', function () {
    units = null;
    pending = null;
    if (searchOpen && searchState.q.trim()) run();
  });

  /* ------------------------------------------------------------------ the start */

  /* Proofs. A proof that follows its statement is described by that statement's label, so that a screen reader
     names what it proves; a long proof begins with a way past it, shown to a reader moving by keys. */
  all('[data-env="proof"], [data-env="proof-sketch"]', main).forEach(function (proof) {
    var before = proof.previousElementSibling;
    var title = before && before.matches('[data-result], [data-term]') ? blockTitle(before) : null;
    if (title && title.id && !proof.hasAttribute('aria-describedby')) proof.setAttribute('aria-describedby', title.id);
    /* No address is made for the text after the proof: generated passage addresses keep their published order. */
    if (!proof.nextElementSibling || all(':scope > p, :scope > .mg-display, :scope > ol, :scope > ul', proof).length < 4) return;
    var skip = element('button', 'reader-proof-skip', word('proof-skip'));
    skip.type = 'button';
    skip.setAttribute('data-reader-skip', '');
    skip.addEventListener('click', function () {
      var past = proof.nextElementSibling;
      if (!past) return;
      scrollToEl(past);
      focusQuietly(past);
    });
    proof.insertBefore(skip, proof.firstChild);
  });

  try { if ('scrollRestoration' in history) history.scrollRestoration = 'manual'; } catch (e) { /* kept by the browser */ }
  (function start() {
    var params;
    try { params = new URL(location.href).searchParams; } catch (e) { params = null; }
    var q = params ? params.get('q') : null;
    searchState.q = q || '';
    var id = hashId();
    var st = history.state && history.state.reader;
    // Only Back and Forward revisit a saved position. Reload follows the URL.
    var timing = window.performance;
    var nav = timing && timing.getEntriesByType && timing.getEntriesByType('navigation')[0];
    var traversal = nav ? nav.type === 'back_forward' : timing && timing.navigation && timing.navigation.type === 2;
    var saved = traversal && st && (st.at || typeof st.y === 'number') ? st : null;
    if (st && !traversal) {
      var entry = stateWith({});
      delete entry.reader.at;
      delete entry.reader.off;
      delete entry.reader.y;
      delete entry.reader.focus;
      replaceEntry(entry);
    }
    if (id) {
      if (!go(id, { replace: true, initial: true, focus: false, keepQuery: !!q, restore: saved && saved.id === id ? saved : null })) {
        if (!current && view !== 'front') show(null);
        replaceEntry(stateWith({ id: '', view: view }));
      }
    } else {
      show(null);
      lastId = '';
      replaceEntry(stateWith({ id: '', view: 'front' }));
      if (saved) restorePlace(saved, false);
      else window.scrollTo(0, 0);
      if (!q) offerPlace();
    }
    if (q) {
      openSearch(null, q, { focus: false, record: false, scope: st && st.scope });
      if (st && st.panel && st.hit) focusHit(st.hit);
    }
    later(function () { measureBar(); trackSection(); });
  })();
})();
