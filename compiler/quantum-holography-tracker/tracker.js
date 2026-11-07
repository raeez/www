(() => {
  'use strict';
  const L = window.QH_LABELS || {};
  const doc = document.documentElement;
  const card = document.getElementById('qh-card');
  const cardTitle = card.querySelector('.pc-title');
  const cardBody = card.querySelector('.pc-body');
  const backButton = card.querySelector('.pc-back');
  const backName = card.querySelector('.pc-back-name');
  const closeButton = card.querySelector('.pc-close');
  const narrow = window.matchMedia('(max-width: 640px)');
  const GAP = 8, EDGE = 12;
  const fold = text => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase();
  const typing = node => node && (node.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(node.tagName));

  /* ------------------------------------------------------------ cards */
  let anchor = null;     // the term in the page that the card belongs to
  let floating = false;  // opened from the search, with no term in the page
  let returnTo = null;   // where focus goes when a floating card closes
  let pinned = false;    // opened by click, tap or Enter: stays until closed
  let byHover = false;   // opened by a resting mouse: closes when the mouse leaves
  let trail = [];        // ids visited inside the card, for Back
  let current = null;
  let openTimer = 0, closeTimer = 0;
  let pointerAt = -1e9;  // when the last pointer press happened
  let cardFormulas = false;
  let restoring = false; // focus is being returned to a term after Escape
  document.addEventListener('pointerdown', () => { pointerAt = performance.now(); }, true);

  const entry = id => document.getElementById('term-' + id);
  const nameOf = id => {
    const e = entry(id);
    return e ? e.querySelector('.card-title').textContent : id;
  };

  function fill(id) {
    const source = entry(id);
    if (!source) return false;
    current = id;
    cardTitle.textContent = nameOf(id);
    const parts = document.createDocumentFragment();
    for (const child of source.children) {
      if (!child.classList.contains('card-title')) parts.append(child.cloneNode(true));
    }
    parts.querySelectorAll('[id]').forEach(node => node.removeAttribute('id'));
    parts.querySelectorAll('.term[data-term="' + CSS.escape(id) + '"]').forEach(node => {
      node.replaceWith(...node.childNodes);
    });
    cardBody.replaceChildren(parts);
    cardBody.scrollTop = 0;
    cardFormulas = true;
    backButton.hidden = trail.length === 0;
    if (trail.length) backName.textContent = nameOf(trail[trail.length - 1]);
    card.setAttribute('aria-label', cardTitle.textContent);
    return true;
  }

  function place() {
    if (card.hidden) return;
    const sheet = narrow.matches;
    card.classList.toggle('sheet', sheet);
    card.classList.toggle('centred', floating && !sheet);
    if (sheet || floating) {
      card.style.left = card.style.top = card.style.maxHeight = '';
      if (sheet && anchor) keepAboveSheet();
      return;
    }
    if (!anchor) return;
    const r = anchor.getBoundingClientRect();
    const vw = doc.clientWidth, vh = window.innerHeight;
    card.style.maxHeight = 'none';
    card.style.left = '0px';
    card.style.top = '0px';
    const natural = card.offsetHeight;
    const width = card.offsetWidth;
    const below = vh - r.bottom - GAP - EDGE;
    const above = r.top - GAP - EDGE;
    const wanted = Math.min(natural, vh * 0.7, 576);
    const downward = below >= wanted || below >= above;
    const room = Math.max(120, Math.floor(downward ? below : above));
    card.style.maxHeight = Math.min(room, vh * 0.7, 576) + 'px';
    const height = card.offsetHeight;
    const left = Math.min(Math.max(EDGE, r.left - 18), vw - width - EDGE);
    const top = downward ? r.bottom + GAP : r.top - GAP - height;
    card.style.left = Math.round(left) + 'px';
    card.style.top = Math.round(top) + 'px';
  }

  // On a phone the card is a sheet at the foot of the screen. Scroll the page so that
  // the term stays in view above the sheet.
  function keepAboveSheet() {
    requestAnimationFrame(() => {
      if (!anchor || card.hidden) return;
      const r = anchor.getBoundingClientRect();
      const sheetTop = card.getBoundingClientRect().top;
      const barBottom = 64;
      let delta = 0;
      if (r.bottom > sheetTop - EDGE) delta = r.bottom - (sheetTop - EDGE) + 8;
      else if (r.top < barBottom) delta = r.top - barBottom - 8;
      if (delta) window.scrollBy({ top: delta, behavior: 'smooth' });
    });
  }

  // A hidden card keeps no layout, so a scroll reset made while it is hidden does not hold:
  // reset once the card is visible, and again after layout, on every open path.
  function toTop() {
    cardBody.scrollTop = 0; card.scrollTop = 0;
    requestAnimationFrame(() => { cardBody.scrollTop = 0; card.scrollTop = 0; });
  }

  function open(term, options = {}) {
    const id = term.dataset.term;
    if (!id) return;
    if (anchor && anchor !== term) anchor.setAttribute('aria-expanded', 'false');
    trail = [];
    if (!fill(id)) return;
    floating = false;
    anchor = term;
    term.setAttribute('aria-expanded', 'true');
    card.hidden = false;
    pinned = Boolean(options.pin);
    byHover = Boolean(options.hover);
    place();
    if (cardFormulas) { cardFormulas = false; measure(cardBody); }
    toTop();
    if (options.focus) cardTitle.focus({ preventScroll: true });
  }

  // A card opened from the search: it belongs to no term in the page.
  function openFloating(id, from) {
    if (anchor) anchor.setAttribute('aria-expanded', 'false');
    trail = [];
    if (!fill(id)) return;
    anchor = null; floating = true; returnTo = from || null;
    card.hidden = false;
    pinned = true; byHover = false;
    place();
    if (cardFormulas) { cardFormulas = false; measure(cardBody); }
    toTop();
    cardTitle.focus({ preventScroll: true });
  }

  function close(restoreFocus) {
    clearTimeout(openTimer);
    clearTimeout(closeTimer);
    if (card.hidden) return;
    card.hidden = true;
    card.classList.remove('sheet', 'centred');
    const was = anchor || (floating ? returnTo : null);
    if (anchor) anchor.setAttribute('aria-expanded', 'false');
    anchor = null; pinned = false; byHover = false; trail = []; current = null; floating = false; returnTo = null;
    if (restoreFocus && was) {
      restoring = true;
      was.focus({ preventScroll: true });
      setTimeout(() => { restoring = false; }, 0);
    }
  }

  function go(id) {
    if (!entry(id) || id === current) return;
    if (current) trail.push(current);
    fill(id);
    pinned = true;
    place();
    toTop();
  }

  backButton.addEventListener('click', () => {
    const id = trail.pop();
    if (id) { fill(id); place(); toTop(); }
  });
  closeButton.addEventListener('click', () => close(true));
  closeButton.setAttribute('aria-label', L.close || 'Close');

  {
    const terms = [...document.querySelectorAll('main [data-term]')];
    const idle = window.requestIdleCallback || (fn => setTimeout(() => fn({ timeRemaining: () => 8 }), 1));
    let at = 0;
    const mark = deadline => {
      do {
        for (const term of terms.slice(at, at + 200)) {
          term.setAttribute('aria-haspopup', 'dialog');
          term.setAttribute('aria-controls', 'qh-card');
          if (!term.hasAttribute('aria-expanded')) term.setAttribute('aria-expanded', 'false');
        }
        at += 200;
      } while (at < terms.length && deadline.timeRemaining() > 2);
      if (at < terms.length) idle(mark);
    };
    idle(mark);
  }

  const pageTerm = target => {
    const term = target.closest && target.closest('[data-term]');
    return term && !card.contains(term) ? term : null;
  };

  document.addEventListener('pointerover', event => {
    if (event.pointerType !== 'mouse') return;
    const term = pageTerm(event.target);
    if (term) {
      clearTimeout(closeTimer);
      if (term === anchor) return;
      clearTimeout(openTimer);
      if (pinned) return;
      openTimer = setTimeout(() => open(term, { hover: true }), 140);
    } else if (card.contains(event.target)) {
      clearTimeout(closeTimer);
    }
  });

  document.addEventListener('pointerout', event => {
    if (event.pointerType !== 'mouse') return;
    const from = pageTerm(event.target) || (card.contains(event.target) ? card : null);
    if (!from) return;
    const to = event.relatedTarget;
    if (to && (card.contains(to) || (anchor && anchor.contains(to)))) return;
    clearTimeout(openTimer);
    if (!pinned && byHover) closeTimer = setTimeout(() => close(false), 280);
  });

  document.addEventListener('click', event => {
    const inside = card.contains(event.target);
    const term = event.target.closest && event.target.closest('[data-term]');
    if (term && inside) {
      event.preventDefault();
      go(term.dataset.term);
      return;
    }
    if (term) {
      event.preventDefault();
      clearTimeout(openTimer);
      if (term === anchor && pinned) { close(false); return; }
      open(term, { pin: true, focus: event.detail === 0 });
      return;
    }
    if (!inside && !card.hidden) close(false);
  });

  // Keyboard focus opens the card; focus that follows a pointer press is left to the click.
  document.addEventListener('focusin', event => {
    const term = pageTerm(event.target);
    if (term) {
      if (!restoring && term !== anchor && performance.now() - pointerAt > 700) open(term);
      return;
    }
    if (!card.contains(event.target) && !pinned) close(false);
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      if (finder && !finder.hidden) return;
      if (document.body.classList.contains('toc-open')) { setDrawer(false, true); return; }
      if (!card.hidden) { event.preventDefault(); close(true); }
      return;
    }
    const term = pageTerm(event.target);
    if (term && (event.key === ' ' || (event.key === 'Enter' && term.tagName !== 'A'))) {
      event.preventDefault();
      open(term, { pin: true, focus: true });
      return;
    }
    if (event.key === 'Tab' && card.contains(document.activeElement) && pinned) {
      const stops = [...card.querySelectorAll('a[href], button:not([hidden])')]
        .filter(node => node.offsetParent !== null);
      if (!stops.length) return;
      const first = stops[0], last = stops[stops.length - 1];
      if (event.shiftKey && (document.activeElement === first || document.activeElement === cardTitle)) {
        event.preventDefault(); last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault(); first.focus();
      }
    }
  });

  let scrollFrame = 0;
  window.addEventListener('scroll', () => {
    if (card.hidden || narrow.matches || floating || scrollFrame) return;
    scrollFrame = requestAnimationFrame(() => {
      scrollFrame = 0;
      if (!anchor) return;
      const r = anchor.getBoundingClientRect();
      if (r.bottom < 0 || r.top > window.innerHeight) { close(false); return; }
      place();
    });
  }, { passive: true });
  window.addEventListener('resize', () => place());

  /* --------------------------------------------------------- contents */
  const toc = document.getElementById('contents');
  const tocButton = document.querySelector('.toc-button');
  function setDrawer(open, restore) {
    document.body.classList.toggle('toc-open', open);
    tocButton.setAttribute('aria-expanded', String(open));
    if (open) {
      const active = toc.querySelector('a.is-active') || toc.querySelector('a');
      active && active.focus({ preventScroll: true });
      active && active.scrollIntoView({ block: 'center' });
    } else if (restore) tocButton.focus({ preventScroll: true });
  }
  tocButton.addEventListener('click', event => {
    event.stopPropagation();
    setDrawer(!document.body.classList.contains('toc-open'));
  });
  toc.addEventListener('click', event => {
    if (event.target.closest('a')) setDrawer(false);
  });
  document.addEventListener('click', event => {
    if (document.body.classList.contains('toc-open') && !toc.contains(event.target) && !tocButton.contains(event.target)) {
      setDrawer(false);
    }
  }, true);

  // The current place: sections are measured on every scroll, headings only inside the current
  // section (the others may not be laid out yet; see content-visibility in the style).
  const target = link => document.getElementById(decodeURIComponent(link.hash.slice(1)));
  const tops = [], subsOf = new Map();
  for (const li of toc.querySelectorAll(':scope > ol > li')) {
    const link = li.querySelector(':scope > a');
    const node = link && link.hash && target(link);
    if (!node) continue;
    tops.push([link, node]);
    subsOf.set(link, [...li.querySelectorAll('.sub a')].map(a => [a, target(a)]).filter(pair => pair[1]));
  }
  // Entries in page order, so the last one passed is the current one.
  tops.sort((a, b) => (a[1].compareDocumentPosition(b[1]) & Node.DOCUMENT_POSITION_FOLLOWING) ? -1 : 1);
  let spyFrame = 0, activeTop = null, activeSub = null;
  function spy() {
    spyFrame = 0;
    const line = 120;
    let topLink = null, subLink = null;
    for (const [link, node] of tops) {
      if (node.getBoundingClientRect().top - line <= 0) topLink = link; else break;
    }
    if (topLink) {
      for (const [link, node] of subsOf.get(topLink)) {
        if (node.getBoundingClientRect().top - line <= 0) subLink = link; else break;
      }
    }
    if (topLink === activeTop && subLink === activeSub) return;
    if (activeTop) { activeTop.classList.remove('is-active'); activeTop.parentElement.classList.remove('is-current'); }
    if (activeSub) activeSub.classList.remove('is-active');
    activeTop = topLink; activeSub = subLink;
    if (topLink) {
      topLink.classList.add('is-active');
      topLink.parentElement.classList.add('is-current');
    }
    if (subLink) subLink.classList.add('is-active');
    follow(subLink || topLink);
  }
  // On the rail, the current entry stays in view as the reader moves through a long contents.
  const rail = window.matchMedia('(min-width: 1180px)');
  let followed = null;
  function follow(link) {
    if (!link || link === followed || !rail.matches || toc.scrollHeight <= toc.clientHeight + 4) return;
    followed = link;
    const top = link.getBoundingClientRect().top - toc.getBoundingClientRect().top + toc.scrollTop;
    const margin = Math.min(120, toc.clientHeight / 4);
    if (top < toc.scrollTop + margin || top > toc.scrollTop + toc.clientHeight - margin) {
      toc.scrollTop = Math.max(0, top - toc.clientHeight / 3);
    }
  }

  // The reading line under the bar, and the bar's title once the page title has gone by.
  const progress = document.querySelector('.progress span');
  let readFrame = 0;
  function reading() {
    readFrame = 0;
    const max = doc.scrollHeight - window.innerHeight;
    if (progress) progress.style.setProperty('--read', max > 0 ? Math.min(1, window.scrollY / max).toFixed(4) : '0');
  }
  window.addEventListener('scroll', () => {
    if (!spyFrame) spyFrame = requestAnimationFrame(spy);
    if (!readFrame) readFrame = requestAnimationFrame(reading);
  }, { passive: true });
  spy();
  reading();

  const title = document.querySelector('.cover .title');
  if (title && 'IntersectionObserver' in window) {
    new IntersectionObserver(([seen]) => {
      document.body.classList.toggle('scrolled', !seen.isIntersecting);
    }, { rootMargin: '-52px 0px 0px 0px' }).observe(title);
  }

  /* ------------------------------------------------------------ theme */
  const themeButton = document.querySelector('.theme-toggle');
  const dark = window.matchMedia('(prefers-color-scheme: dark)');
  const isDark = () => doc.dataset.theme ? doc.dataset.theme === 'dark' : dark.matches;
  const syncTheme = () => themeButton && themeButton.setAttribute('aria-pressed', String(isDark()));
  if (themeButton) {
    themeButton.addEventListener('click', () => {
      const next = isDark() ? 'light' : 'dark';
      doc.setAttribute('data-theme', next);
      try { localStorage.setItem('qh-theme', next); } catch (error) { /* the choice lasts for this visit */ }
      syncTheme();
    });
    if (dark.addEventListener) dark.addEventListener('change', syncTheme);
    syncTheme();
  }

  /* ------------------------------------------------------------ board */
  const board = document.getElementById('status');
  const VISIBLE = 5;
  if (board) {
    for (const state of board.querySelectorAll('.state')) {
      const items = [...state.querySelectorAll('.st-item')];
      if (items.length <= VISIBLE + 1) continue;
      items.slice(VISIBLE).forEach(item => item.classList.add('is-extra'));
      const more = document.createElement('button');
      more.type = 'button';
      more.className = 'st-more';
      const label = () => state.classList.contains('is-all')
        ? (L.show_fewer || 'Show fewer') : (L.show_all || 'Show all') + ' ' + items.length;
      more.textContent = label();
      more.setAttribute('aria-expanded', 'false');
      more.addEventListener('click', () => {
        const all = state.classList.toggle('is-all');
        more.textContent = label();
        more.setAttribute('aria-expanded', String(all));
        if (!all) state.scrollIntoView({ block: 'start' });
      });
      state.append(more);
    }
    const tools = board.querySelector('.board-tools');
    const input = board.querySelector('#board-filter');
    const toggle = board.querySelector('.filter-toggle');
    const row = board.querySelector('#board-filter-row');
    const none = document.createElement('p');
    none.className = 'filter-none';
    none.hidden = true;
    none.setAttribute('role', 'status');
    none.textContent = L.no_match || 'No match';
    const states = board.querySelector('.states');
    if (states) states.before(none);
    if (tools && input) {
      tools.hidden = false;
      const openSearch = show => {
        row.hidden = !show;
        tools.classList.toggle('is-open', show);
        toggle.setAttribute('aria-expanded', String(show));
        if (show) input.focus();
        else if (input.value) { input.value = ''; input.dispatchEvent(new Event('input')); }
      };
      toggle.addEventListener('click', () => openSearch(row.hidden));
      input.addEventListener('keydown', event => {
        if (event.key === 'Escape') { event.stopPropagation(); openSearch(false); toggle.focus(); }
      });
      input.addEventListener('blur', () => { if (!input.value) setTimeout(() => {
        if (document.activeElement !== toggle && !input.value) openSearch(false); }, 150); });
      const rows = [...board.querySelectorAll('.st-item')].map(item => [item, item.textContent.toLocaleLowerCase()]);
      let timer = 0;
      input.addEventListener('input', () => {
        clearTimeout(timer);
        timer = setTimeout(() => {
          const words = input.value.toLocaleLowerCase().split(/\s+/).filter(Boolean);
          board.classList.toggle('is-filtering', words.length > 0);
          let shown = 0;
          for (const [item, text] of rows) {
            const hit = words.every(word => text.includes(word));
            item.hidden = !hit;
            if (hit) shown++;
          }
          for (const state of board.querySelectorAll('.state')) {
            state.classList.toggle('no-match', words.length > 0 && !state.querySelector('.st-item:not([hidden])'));
          }
          none.hidden = !(words.length && shown === 0);
        }, 120);
      });
    }
  }
  for (const li of document.querySelectorAll('.tally li')) {
    if (li.querySelector('.t-n').textContent.trim() === '0') li.setAttribute('data-zero', '');
  }

  /* ------------------------------------------------------- in-page jumps */
  // Parts far from the screen are laid out only when reached, so a jump can land short while
  // the parts around the target take their real height. Settle the target under the bar.
  function settle(node) {
    let tries = 0;
    for (let d = node.closest('details:not([open])'); d; d = d.parentElement.closest('details:not([open])')) d.open = true;
    const step = () => {
      const want = parseFloat(getComputedStyle(node).scrollMarginTop) || 0;
      const top = node.getBoundingClientRect().top;
      if (Math.abs(top - want) <= 3 || tries++ > 8) { spy(); return; }
      window.scrollBy(0, top - want);
      requestAnimationFrame(() => requestAnimationFrame(step));
    };
    requestAnimationFrame(() => requestAnimationFrame(step));
  }
  const jumpTarget = hash => {
    try { return hash.length > 1 ? document.getElementById(decodeURIComponent(hash.slice(1))) : null; }
    catch (error) { return null; }
  };
  document.addEventListener('click', event => {
    const link = event.target.closest && event.target.closest('a[href^="#"]');
    if (!link) return;
    // Terms open their card instead (that handler, registered earlier, prevents the jump).
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey) return;
    const node = jumpTarget(link.hash);
    if (node) settle(node);
  });
  window.addEventListener('hashchange', () => { const node = jumpTarget(location.hash); if (node) settle(node); });
  if (location.hash) {
    const node = jumpTarget(location.hash);
    if (node) window.addEventListener('load', () => settle(node), { once: true });
  }

  /* ---------------------------------------------- links to each part */
  const toast = document.getElementById('toast');
  let toastTimer = 0;
  function say(text) {
    if (!toast) return;
    toast.textContent = text;
    toast.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => { toast.hidden = true; }, 1600);
  }
  document.addEventListener('click', event => {
    const link = event.target.closest && event.target.closest('a.hl');
    if (!link) return;
    const url = location.href.split('#')[0] + link.hash;
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(() => say(L.copied || 'Link copied'), () => {});
      }
    } catch (error) { /* the address bar still shows the link */ }
  });

  /* ------------------------------------------------------------ search */
  const finder = document.getElementById('finder');
  const finderInput = document.getElementById('finder-input');
  const finderList = document.getElementById('finder-list');
  const finderStatus = document.getElementById('finder-status');
  const findButton = document.querySelector('.find-button');
  const GROUPS = [L.search_results || 'Results', L.search_sections || 'Sections',
                  L.search_statements || 'Statements', L.search_terms || 'Terms'];
  const LIMITS = [8, 8, 6, 8];
  let index = null, shown = [], active = -1, lastFocus = null;

  const plain = node => {
    const copy = node.cloneNode(true);
    copy.querySelectorAll('.hl, annotation, .visually-hidden, .statement-kind, .rk-label').forEach(n => n.remove());
    return copy.textContent.replace(/\s+/g, ' ').trim();
  };
  const glyphOf = name => `<svg class="glyph" viewBox="0 0 16 16" aria-hidden="true"><use href="#g-${name}"/></svg>`;

  function buildIndex() {
    const rows = [];
    for (const li of document.querySelectorAll('.rk')) {
      const head = li.querySelector('.rk-head'), claim = li.querySelector('.rk-claim');
      const n = li.querySelector('.rk-n');
      rows.push({ group: 0, id: li.id, title: head ? plain(head) : '', sub: claim ? plain(claim) : '',
                  mark: li.classList.contains('rk-breakthrough') && n ? n.textContent.trim() : glyphOf('failing'), boost: 6 });
    }
    for (const h of document.querySelectorAll('.open-problems h3[id]')) {
      const next = h.nextElementSibling;
      rows.push({ group: 0, id: h.id, title: plain(h), sub: next && next.tagName === 'P' ? plain(next) : '',
                  mark: glyphOf('open'), boost: 4 });
    }
    for (const section of document.querySelectorAll('.content > .chapter:not(.opening)')) {
      const num = section.querySelector(':scope > .eyebrow .num');
      const n = num ? num.textContent.trim() : '';
      const head = section.querySelector('h2');
      const name = head ? plain(head) : '';
      for (const h of section.querySelectorAll('h2[id], h3[id], h4[id]')) {
        const top = h === head;
        rows.push({ group: 1, id: h.id, title: plain(h), sub: top ? '' : name, mark: n, boost: top ? 3 : 0 });
      }
    }
    for (const st of document.querySelectorAll('.content .statement[id]')) {
      const section = st.closest('.chapter');
      const head = section && section.querySelector('h2');
      const kind = st.querySelector(':scope > .statement-kind');
      rows.push({ group: 2, id: st.id, title: (kind ? plain(kind) : '') + (head ? ' · ' + plain(head) : ''),
                  sub: plain(st).slice(0, 260), mark: glyphOf('theorem'), boost: 1 });
    }
    for (const entryNode of document.querySelectorAll('.card-entry')) {
      const name = entryNode.querySelector('.card-title');
      const def = entryNode.querySelector('.card-def');
      rows.push({ group: 3, id: entryNode.dataset.card, title: name ? name.textContent : '',
                  sub: def ? plain(def).slice(0, 220) : '', term: true, mark: '', boost: 0 });
    }
    for (const row of rows) { row.t = fold(row.title); row.s = fold(row.sub); }
    return rows;
  }

  function score(row, words) {
    let total = row.boost;
    for (const word of words) {
      const at = row.t.indexOf(word);
      if (at >= 0) total += at === 0 ? 30 : /[\s(–-]/.test(row.t[at - 1]) ? 18 : 6;
      else {
        const inBody = row.s.indexOf(word);
        if (inBody < 0) return -1;
        total += inBody === 0 || /[\s(–-]/.test(row.s[inBody - 1]) ? 3 : 1;
      }
    }
    if (row.t === words.join(' ')) total += 40;
    return total;
  }

  const escapeHtml = text => text.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
  function highlight(text, words) {
    if (!words.length) return escapeHtml(text);
    const folded = fold(text);
    const marks = [];
    for (const word of words) {
      let at = folded.indexOf(word);
      while (at >= 0 && marks.length < 12) { marks.push([at, at + word.length]); at = folded.indexOf(word, at + word.length); }
    }
    if (!marks.length || folded.length !== text.length) return escapeHtml(text);
    marks.sort((a, b) => a[0] - b[0]);
    let out = '', last = 0;
    for (const [a, b] of marks) {
      if (a < last) continue;
      out += escapeHtml(text.slice(last, a)) + '<mark>' + escapeHtml(text.slice(a, b)) + '</mark>';
      last = b;
    }
    return out + escapeHtml(text.slice(last));
  }

  function render() {
    if (!index) index = buildIndex();
    const words = fold(finderInput.value).split(/\s+/).filter(Boolean);
    const groups = [[], [], [], []];
    if (!words.length) {
      for (const row of index) if (row.group === 0) groups[0].push(row);
    } else {
      const scored = [];
      for (const row of index) {
        const s = score(row, words);
        if (s >= 0) scored.push([s, row]);
      }
      scored.sort((a, b) => b[0] - a[0]);
      for (const [, row] of scored) if (groups[row.group].length < LIMITS[row.group]) groups[row.group].push(row);
    }
    shown = [];
    const html = [];
    groups.forEach((rows, g) => {
      if (!rows.length) return;
      html.push(`<li class="fd-group" role="presentation">${escapeHtml(GROUPS[g])}</li>`);
      for (const row of rows) {
        const i = shown.length;
        shown.push(row);
        html.push(`<li class="fd-item" role="option" id="fd-${i}" data-i="${i}" aria-selected="false">` +
                  `<span class="fd-mark" aria-hidden="true">${row.mark}</span>` +
                  `<span class="fd-title">${highlight(row.title, words)}</span>` +
                  (row.sub ? `<span class="fd-sub">${highlight(row.sub.slice(0, 200), words)}</span>` : '') + '</li>');
      }
    });
    finderList.innerHTML = html.join('');
    finderStatus.textContent = words.length && !shown.length ? (L.search_none || 'Nothing matches') : '';
    select(shown.length ? 0 : -1);
  }

  function select(i) {
    const old = finderList.querySelector('[aria-selected="true"]');
    if (old) old.setAttribute('aria-selected', 'false');
    active = i;
    if (i < 0) { finderInput.removeAttribute('aria-activedescendant'); return; }
    const item = document.getElementById('fd-' + i);
    item.setAttribute('aria-selected', 'true');
    finderInput.setAttribute('aria-activedescendant', item.id);
    item.scrollIntoView({ block: 'nearest' });
  }

  function choose(i) {
    const row = shown[i];
    if (!row) return;
    closeFinder(false);
    if (row.term) { openFloating(row.id, findButton); return; }
    const node = document.getElementById(row.id);
    if (!node) return;
    if (location.hash === '#' + row.id) settle(node);
    else location.hash = row.id;
  }

  function openFinder() {
    if (!finder.hidden) return;
    close(false);
    if (document.body.classList.contains('toc-open')) setDrawer(false);
    lastFocus = document.activeElement;
    finder.hidden = false;
    document.body.classList.add('finder-open');
    finderInput.value = '';
    render();
    finderInput.focus();
  }
  function closeFinder(restore = true) {
    if (finder.hidden) return;
    finder.hidden = true;
    document.body.classList.remove('finder-open');
    if (restore && lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
  }

  if (finder && findButton) {
    findButton.addEventListener('click', event => { event.stopPropagation(); openFinder(); });
    let inputTimer = 0;
    finderInput.addEventListener('input', () => { clearTimeout(inputTimer); inputTimer = setTimeout(render, 60); });
    finderInput.addEventListener('keydown', event => {
      if (event.key === 'ArrowDown') { event.preventDefault(); if (shown.length) select((active + 1) % shown.length); }
      else if (event.key === 'ArrowUp') { event.preventDefault(); if (shown.length) select((active - 1 + shown.length) % shown.length); }
      else if (event.key === 'Enter') { event.preventDefault(); if (active >= 0) choose(active); }
    });
    finderList.addEventListener('pointermove', event => {
      const item = event.target.closest('.fd-item');
      if (item && Number(item.dataset.i) !== active) select(Number(item.dataset.i));
    });
    finderList.addEventListener('click', event => {
      const item = event.target.closest('.fd-item');
      event.stopPropagation();
      if (item) choose(Number(item.dataset.i));
    });
    finder.addEventListener('click', event => {
      event.stopPropagation();
      if (event.target === finder) closeFinder();
    });
    finder.querySelector('.finder-close').addEventListener('click', () => closeFinder());
    finder.addEventListener('keydown', event => {
      if (event.key === 'Escape') { event.preventDefault(); event.stopPropagation(); closeFinder(); }
      if (event.key === 'Tab') {
        const stops = [finderInput, finder.querySelector('.finder-close')];
        const at = stops.indexOf(document.activeElement);
        event.preventDefault();
        stops[(at + (event.shiftKey ? stops.length - 1 : 1)) % stops.length].focus();
      }
    });
    document.addEventListener('keydown', event => {
      if (!finder.hidden || typing(event.target)) return;
      if ((event.key === '/' && !event.metaKey && !event.ctrlKey && !event.altKey) ||
          (event.key.toLowerCase() === 'k' && (event.metaKey || event.ctrlKey))) {
        event.preventDefault();
        openFinder();
      }
    });
  }

  /* -------------------------------------------------------------- map */
  // Hairlines from each result to the report sections and the citations its own lines name.
  // They are drawn under the nodes and stop short of them; a node in focus lights its own lines.
  const map = document.querySelector('.map');
  const wide = window.matchMedia('(min-width: 1000px)');
  const SVGNS = 'http://www.w3.org/2000/svg';
  let wires = [];
  function firstLine(node) {
    const box = node.getBoundingClientRect();
    const size = parseFloat(getComputedStyle(node).fontSize) || 16;
    const line = parseFloat(getComputedStyle(node).lineHeight) || size * 1.3;
    return { box, y: box.top + Math.min(box.height, line) / 2 };
  }
  function drawMap() {
    if (!map) return;
    const svg = map.querySelector('.map-wires');
    svg.replaceChildren();
    wires = [];
    if (!wide.matches) return;
    const frame = map.getBoundingClientRect();
    for (const source of map.querySelectorAll('.mn[data-to]')) {
      const from = firstLine(source.querySelector('.mn-link .mn-title') || source.querySelector('.mn-link'));
      const linkBox = source.querySelector('.mn-link').getBoundingClientRect();
      const meta = source.querySelector('.mn-meta');
      const metaBox = meta && meta.getBoundingClientRect();
      // The status sits on the title's line; a line to the right starts after it.
      const right = metaBox && metaBox.top < linkBox.bottom ? Math.max(linkBox.right, metaBox.right) : linkBox.right;
      const fromBox = { left: source.getBoundingClientRect().left, right };
      for (const id of source.dataset.to.split(' ')) {
        const goal = document.getElementById(id);
        if (!goal) continue;
        const link = goal.querySelector(':scope > .mn-link') || goal.querySelector('.src-refs') || goal;
        const to = firstLine(link);
        const left = to.box.right <= fromBox.left;
        const x1 = (left ? fromBox.left - 12 : fromBox.right + 12) - frame.left;
        const x2 = (left ? to.box.right + 12 : (goal.getBoundingClientRect().left) - 12) - frame.left;
        const y1 = from.y - frame.top, y2 = to.y - frame.top;
        const bend = (x2 - x1) * 0.5;
        const path = document.createElementNS(SVGNS, 'path');
        path.setAttribute('d', `M${x1.toFixed(1)} ${y1.toFixed(1)}C${(x1 + bend).toFixed(1)} ${y1.toFixed(1)} ` +
                               `${(x2 - bend).toFixed(1)} ${y2.toFixed(1)} ${x2.toFixed(1)} ${y2.toFixed(1)}`);
        svg.append(path);
        const dots = [];
        for (const [x, y] of [[x1, y1], [x2, y2]]) {
          const dot = document.createElementNS(SVGNS, 'circle');
          dot.setAttribute('cx', x.toFixed(1)); dot.setAttribute('cy', y.toFixed(1)); dot.setAttribute('r', '2.2');
          svg.append(dot);
          dots.push(dot);
        }
        wires.push({ path, dots, source, goal });
      }
    }
  }
  const NODES = '.mres .mn, .mn-sec, .mn-cite';
  function light(node) {
    if (!map) return;
    map.querySelectorAll('.is-dim, .is-lit').forEach(n => n.classList.remove('is-dim', 'is-lit'));
    if (!node) { map.classList.remove('is-wired'); return; }
    const source = node.matches('.mres .mn') ? node : (wires.find(w => w.goal === node) || {}).source;
    if (!source) { map.classList.remove('is-wired'); return; }
    const lit = new Set([source]);
    for (const wire of wires) if (wire.source === source) lit.add(wire.goal);
    map.classList.add('is-wired');
    for (const n of map.querySelectorAll(NODES)) n.classList.toggle('is-dim', !lit.has(n));
    for (const wire of wires) {
      const on = wire.source === source;
      wire.path.classList.toggle(on ? 'is-lit' : 'is-dim', true);
      wire.dots.forEach(dot => dot.classList.toggle('is-lit', on));
    }
  }
  if (map) {
    const hit = event => event.target.closest && event.target.closest(NODES);
    map.addEventListener('pointerover', event => { if (event.pointerType === 'mouse') light(hit(event)); });
    map.addEventListener('pointerleave', () => light(null));
    map.addEventListener('focusin', event => light(hit(event)));
    map.addEventListener('focusout', event => { if (!map.contains(event.relatedTarget)) light(null); });
    if ('ResizeObserver' in window) new ResizeObserver(() => requestAnimationFrame(drawMap)).observe(map);
    else window.addEventListener('resize', drawMap);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(drawMap);
    drawMap();
  }

  /* ------------------------------------------------------ terms filter */
  const termsFilter = document.getElementById('terms-filter');
  if (termsFilter) {
    termsFilter.closest('.terms-tools').hidden = false;
    const count = document.getElementById('terms-filter-count');
    const cards = [...document.querySelectorAll('.card-entry')];
    const names = cards.map(c => fold(c.querySelector('.card-title').textContent));
    const letters = [...document.querySelectorAll('.glossary .letter')];
    let filterTimer = 0;
    termsFilter.addEventListener('input', () => {
      clearTimeout(filterTimer);
      filterTimer = setTimeout(() => {
        const words = fold(termsFilter.value).split(/\s+/).filter(Boolean);
        let n = 0;
        cards.forEach((c, i) => {
          const hit = words.every(word => names[i].includes(word));
          c.hidden = !hit;
          if (hit) n++;
        });
        for (const letter of letters) {
          let next = letter.nextElementSibling, any = false;
          while (next && !next.classList.contains('letter')) { if (!next.hidden) { any = true; break; } next = next.nextElementSibling; }
          letter.hidden = !any;
        }
        count.textContent = words.length ? `${n} ${L.terms_shown || 'shown'}` : '';
      }, 80);
    });
  }

  /* ------------------------------------------------------------ print */
  let opened = [];
  window.addEventListener('beforeprint', () => {
    opened = [...document.querySelectorAll('main details:not([open])')];
    opened.forEach(d => { d.open = true; });
  });
  window.addEventListener('afterprint', () => { opened.forEach(d => { d.open = false; }); opened = []; });

  /* ------------------------------------------------------ wide formulas */
  function measure(root) {
    for (const math of root.querySelectorAll('math:not([display="block"])')) {
      if (math.parentElement.classList.contains('math-wrap')) continue;
      const host = math.parentElement.closest('p, li, dd, td, th, div, summary, figcaption, blockquote');
      if (!host) continue;
      if (math.getBoundingClientRect().width > host.clientWidth - 2) {
        const wrap = document.createElement('span');
        wrap.className = 'math-wrap math-inline-wide';
        math.replaceWith(wrap);
        wrap.append(math);
      }
    }
    const wraps = [...root.querySelectorAll('.math-wrap')];
    const states = wraps.map(wrap => [wrap.scrollWidth > wrap.clientWidth + 2,
                                      wrap.scrollLeft + wrap.clientWidth >= wrap.scrollWidth - 2]);
    wraps.forEach((wrap, i) => {
      wrap.classList.toggle('is-wide', states[i][0]);
      wrap.classList.toggle('at-end', states[i][0] && states[i][1]);
    });
  }
  const parts = [...document.querySelectorAll('.cover, .content > section, .card-entry')];
  let near = null;
  function watch() {
    if (near) near.disconnect();
    if (!('IntersectionObserver' in window)) { parts.forEach(measure); return; }
    near = new IntersectionObserver(entries => {
      for (const seen of entries) {
        if (!seen.isIntersecting) continue;
        near.unobserve(seen.target);
        measure(seen.target);
      }
    }, { rootMargin: '800px 0px' });
    parts.forEach(part => near.observe(part));
  }
  document.addEventListener('scroll', event => {
    const wrap = event.target;
    if (wrap.classList && wrap.classList.contains('math-wrap')) {
      wrap.classList.toggle('at-end', wrap.scrollLeft + wrap.clientWidth >= wrap.scrollWidth - 2);
    }
  }, true);
  let resizeTimer = 0;
  window.addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(watch, 150); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(watch);
  watch();
})();
