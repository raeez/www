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

  /* ------------------------------------------------------------ cards */
  let anchor = null;     // the term in the page that the card belongs to
  let pinned = false;    // opened by click, tap or Enter: stays until closed
  let byHover = false;   // opened by a resting mouse: closes when the mouse leaves
  let trail = [];        // ids visited inside the card, for Back
  let current = null;
  let openTimer = 0, closeTimer = 0;
  let pointerAt = -1e9;  // when the last pointer press happened
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
    backButton.hidden = trail.length === 0;
    if (trail.length) backName.textContent = nameOf(trail[trail.length - 1]);
    card.setAttribute('aria-label', cardTitle.textContent);
    return true;
  }

  function place() {
    if (!anchor || card.hidden) return;
    const sheet = narrow.matches;
    card.classList.toggle('sheet', sheet);
    if (sheet) {
      card.style.left = card.style.top = card.style.maxHeight = '';
      keepAboveSheet();
      return;
    }
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

  function open(term, options = {}) {
    const id = term.dataset.term;
    if (!id) return;
    if (anchor && anchor !== term) anchor.setAttribute('aria-expanded', 'false');
    trail = [];
    if (!fill(id)) return;
    anchor = term;
    term.setAttribute('aria-expanded', 'true');
    card.hidden = false;
    pinned = Boolean(options.pin);
    byHover = Boolean(options.hover);
    place();
    if (options.focus) cardTitle.focus({ preventScroll: true });
  }

  function close(restoreFocus) {
    clearTimeout(openTimer);
    clearTimeout(closeTimer);
    if (card.hidden) return;
    card.hidden = true;
    card.classList.remove('sheet');
    const was = anchor;
    if (was) was.setAttribute('aria-expanded', 'false');
    anchor = null; pinned = false; byHover = false; trail = []; current = null;
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
  }

  backButton.addEventListener('click', () => {
    const id = trail.pop();
    if (id) { fill(id); place(); }
  });
  closeButton.addEventListener('click', () => close(true));
  closeButton.setAttribute('aria-label', L.close || 'Close');

  for (const term of document.querySelectorAll('main [data-term]')) {
    term.setAttribute('aria-haspopup', 'dialog');
    term.setAttribute('aria-controls', 'qh-card');
    term.setAttribute('aria-expanded', 'false');
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
    if (card.hidden || narrow.matches || scrollFrame) return;
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
    if (document.body.classList.contains('toc-open') && !toc.contains(event.target) && event.target !== tocButton) {
      setDrawer(false);
    }
  }, true);

  const tocLinks = [...toc.querySelectorAll('a[href^="#"]')];
  const targets = tocLinks.map(link => [link, document.getElementById(decodeURIComponent(link.hash.slice(1)))])
    .filter(pair => pair[1]);
  let spyFrame = 0;
  function spy() {
    spyFrame = 0;
    const line = 120;
    let topLink = null, subLink = null;
    for (const [link, target] of targets) {
      if (target.getBoundingClientRect().top - line <= 0) {
        if (link.closest('.sub')) subLink = link; else { topLink = link; subLink = null; }
      }
    }
    for (const link of tocLinks) link.classList.remove('is-active');
    for (const li of toc.querySelectorAll('li.is-current')) li.classList.remove('is-current');
    if (topLink) {
      topLink.classList.add('is-active');
      topLink.parentElement.classList.add('is-current');
    }
    if (subLink && topLink && topLink.parentElement.contains(subLink)) subLink.classList.add('is-active');
  }
  window.addEventListener('scroll', () => { if (!spyFrame) spyFrame = requestAnimationFrame(spy); }, { passive: true });
  spy();

  const hero = document.querySelector('.hero');
  if (hero && 'IntersectionObserver' in window) {
    new IntersectionObserver(([seen]) => {
      document.body.classList.toggle('scrolled', !seen.isIntersecting);
    }, { rootMargin: '-52px 0px 0px 0px' }).observe(hero.querySelector('.title') || hero);
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
    const none = board.querySelector('.filter-none');
    if (tools && input) {
      tools.hidden = false;
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

  /* ------------------------------------------------------ wide formulas */
  function measure() {
    for (const math of document.querySelectorAll('main math:not([display="block"])')) {
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
    for (const wrap of document.querySelectorAll('.math-wrap')) {
      const wide = wrap.scrollWidth > wrap.clientWidth + 2;
      wrap.classList.toggle('is-wide', wide);
      wrap.classList.toggle('at-end', wide && wrap.scrollLeft + wrap.clientWidth >= wrap.scrollWidth - 2);
    }
  }
  document.addEventListener('scroll', event => {
    const wrap = event.target;
    if (wrap.classList && wrap.classList.contains('math-wrap')) {
      wrap.classList.toggle('at-end', wrap.scrollLeft + wrap.clientWidth >= wrap.scrollWidth - 2);
    }
  }, true);
  let resizeTimer = 0;
  window.addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(measure, 150); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
  measure();
})();
