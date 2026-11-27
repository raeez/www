(function () {
  'use strict';
  var root = document.documentElement;

  /* Theme: follows the system until the reader chooses; the choice is remembered on this device. */
  var themeButton = document.querySelector('.theme');
  function currentTheme() {
    var set = root.getAttribute('data-theme');
    if (set) return set;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  if (themeButton) {
    themeButton.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('qh-theme', next); } catch (e) { /* storage unavailable */ }
    });
  }

  /* One floating card serves terms, grid cells and column heads. */
  var card = document.getElementById('card');
  var cardInner = card ? card.querySelector('.card-inner') : null;
  var owner = null;
  var pinned = false;
  var hideTimer = null;
  var hoverCapable = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  function place(target) {
    var r = target.getBoundingClientRect();
    var narrow = window.innerWidth <= 640;
    card.classList.toggle('sheet', narrow && !hoverCapable);
    if (narrow && !hoverCapable) { card.style.left = ''; card.style.top = ''; return; }
    var width = card.offsetWidth;
    var height = card.offsetHeight;
    var left = r.left + window.scrollX + r.width / 2 - width / 2;
    left = Math.max(window.scrollX + 12, Math.min(left, window.scrollX + document.documentElement.clientWidth - width - 12));
    var below = r.bottom + window.scrollY + 8;
    var above = r.top + window.scrollY - height - 8;
    var top = (r.bottom + height + 16 > window.innerHeight && r.top - height - 16 > 0) ? above : below;
    card.style.left = left + 'px';
    card.style.top = top + 'px';
  }

  function contentFor(el) {
    if (el.classList.contains('term')) {
      var entry = document.getElementById(el.getAttribute('data-term'));
      if (!entry) return null;
      var dt = entry.querySelector('dt');
      var dd = entry.querySelector('dd');
      return '<p class="card-term">' + dt.innerHTML + '</p><div>' + dd.innerHTML + '</div>' +
             '<a class="card-more" href="#' + entry.id + '">' + (document.querySelector('#terms h2') ? document.querySelector('#terms h2').textContent : 'Terms') + '</a>';
    }
    if (el.classList.contains('cell-btn')) {
      var note = el.parentNode.querySelector('.cell-note');
      var row = el.getAttribute('data-row');
      var rowLink = document.querySelector('.grid tbody th a[href="#' + row + '"]');
      return note.innerHTML + (rowLink ? '<a class="card-more" href="#' + row + '">' + rowLink.textContent + '</a>' : '');
    }
    if (el.classList.contains('col-head')) {
      var def = document.getElementById('col-' + el.getAttribute('data-col'));
      if (!def) return null;
      return '<p class="card-term">' + def.querySelector('dt').innerHTML + '</p><div>' + def.querySelector('dd').innerHTML + '</div>';
    }
    return null;
  }

  function show(el, pin) {
    if (!card) return;
    clearTimeout(hideTimer);
    var html = contentFor(el);
    if (html === null) return;
    if (owner && owner !== el) owner.setAttribute('aria-expanded', 'false');
    owner = el;
    pinned = !!pin;
    cardInner.innerHTML = html;
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

  var triggers = '.term, .cell-btn, .col-head';
  document.addEventListener('click', function (event) {
    var el = event.target.closest(triggers);
    if (el) {
      event.preventDefault();
      if (owner === el && pinned) { hide(); return; }
      show(el, true);
      return;
    }
    if (card && !card.hidden && !event.target.closest('#card')) hide();
  });
  if (hoverCapable) {
    document.addEventListener('mouseover', function (event) {
      var el = event.target.closest(triggers);
      if (el && !pinned) { show(el, false); return; }
      if (event.target.closest('#card')) clearTimeout(hideTimer);
    });
    document.addEventListener('mouseout', function (event) {
      var el = event.target.closest(triggers + ', #card');
      if (el && !(event.relatedTarget && el.contains(event.relatedTarget))) hideSoon();
    });
  }
  document.addEventListener('focusin', function (event) {
    var el = event.target.closest(triggers);
    if (el && !pinned) show(el, false);
  });
  document.addEventListener('focusout', function (event) {
    if (event.target.closest(triggers) && !(event.relatedTarget && event.relatedTarget.closest && event.relatedTarget.closest('#card'))) hideSoon();
  });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && card && !card.hidden) {
      var back = owner;
      hide();
      if (back) back.focus();
    }
  });
  window.addEventListener('resize', function () { if (owner && card && !card.hidden) place(owner); });

  /* Rows open when they are the target of a link, and a link into a row opens it. */
  function openTarget() {
    var id = decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    var target = document.getElementById(id);
    if (!target) return;
    var details = target.closest('details');
    if (details && !details.open) {
      details.open = true;
      requestAnimationFrame(function () { target.scrollIntoView(); });
    }
  }
  window.addEventListener('hashchange', openTarget);
  openTarget();

  var rows = Array.prototype.slice.call(document.querySelectorAll('details.row'));
  document.querySelectorAll('[data-expand]').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('data-expand') === 'all';
      rows.forEach(function (d) { d.open = open; });
    });
  });

  /* Status filter for the statements of the rows. */
  var filters = Array.prototype.slice.call(document.querySelectorAll('.filter'));
  function applyFilter() {
    var on = filters.filter(function (f) { return f.getAttribute('aria-pressed') === 'true'; })
                    .map(function (f) { return f.getAttribute('data-filter'); });
    document.querySelectorAll('.rows .statement').forEach(function (s) {
      s.hidden = on.length > 0 && on.indexOf(s.getAttribute('data-status')) < 0;
    });
    if (on.length) {
      rows.forEach(function (d) {
        d.open = !!d.querySelector('.statement:not([hidden])');
      });
    }
  }
  filters.forEach(function (f) {
    f.addEventListener('click', function () {
      f.setAttribute('aria-pressed', f.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      applyFilter();
    });
  });
  document.querySelectorAll('.tally a[data-filter]').forEach(function (a) {
    a.addEventListener('click', function () {
      var want = a.getAttribute('data-filter');
      filters.forEach(function (f) { f.setAttribute('aria-pressed', f.getAttribute('data-filter') === want ? 'true' : 'false'); });
      applyFilter();
    });
  });

  /* Mark the section in view in the bar. */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.nav a'));
  if ('IntersectionObserver' in window && navLinks.length) {
    var byId = {};
    navLinks.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && byId[e.target.id]) {
          navLinks.forEach(function (a) { a.removeAttribute('aria-current'); });
          byId[e.target.id].setAttribute('aria-current', 'true');
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(byId).forEach(function (id) { var s = document.getElementById(id); if (s) observer.observe(s); });
  }

  /* Printing shows every row. */
  window.addEventListener('beforeprint', function () { rows.forEach(function (d) { d.open = true; }); });
})();
