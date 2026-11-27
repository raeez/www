/* Resolve an incoming book address before the split reader restores the place and its search. */
(function () {
  'use strict';
  const data = JSON.parse(document.querySelector('script[data-bookmark-map]').textContent);
  const main = document.querySelector('main[data-reader]');
  const local = new Set(data.local);
  const runtime = new Set(data.runtime);
  const incomingQuery = location.search;
  let note = null;
  let pending = '';
  function fragment() {
    const hash = location.hash.slice(1);
    try { return decodeURIComponent(hash); } catch (error) { return hash; }
  }
  function clear() {
    if (note) note.remove();
    note = null;
  }
  function rememberChoice(id) {
    if (!history.state || history.state.bookAddressChoice !== id) {
      history.replaceState(Object.assign({}, history.state, { bookAddressChoice: id }), '', location.href);
    }
  }
  function url(href) {
    const u = new URL(href, location.href);
    u.search = location.search;
    return u;
  }
  function go(href) {
    const target = url(href);
    if (target.pathname === location.pathname ||
        (main && data.page === 'index.html' && location.pathname.endsWith('/') &&
         target.pathname === location.pathname + 'index.html')) {
      const here = new URL(location.href);
      here.hash = target.hash;
      history.replaceState(history.state, '', here.href);
      return;
    }
    if (pending === target.href) return;
    pending = target.href;
    location.replace(target.href);
  }
  function show(id, entry, reason) {
    if (note && note.dataset.fragment === id) return;
    clear();
    note = document.createElement('aside');
    note.className = 'reader-notice bookmark-message';
    note.dataset.notice = Array.isArray(entry) ? 'predecessor' : 'unknown';
    note.dataset.fragment = id;
    note.tabIndex = -1;
    note.setAttribute('aria-label', 'Bookmark');
    const p = document.createElement('p');
    p.textContent = reason || (!Array.isArray(entry) ? 'The destination for #' + id + ' is unavailable in this book.' :
      entry[0] === 'ambiguous' ? 'This saved address can refer to different passages. Choose a passage below.' :
      'This saved address names a changed passage. Its exact text is unavailable here. The related locations are listed below.');
    note.append(p);
    if (Array.isArray(entry)) {
      const ul = document.createElement('ul');
      entry.slice(1).forEach(href => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        const dest = url(href);
        a.setAttribute('href', !location.search && href.startsWith('#') ? href : dest.href);
        a.textContent = data.labels[href] || 'Open the passage';
        a.addEventListener('click', function (event) {
          if (event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
          event.preventDefault();
          if (main && dest.pathname === location.pathname) {
            const target = decodeURIComponent(dest.hash.slice(1));
            clear();
            const handled = !document.dispatchEvent(new CustomEvent('qh:navigate', {
              cancelable: true, detail: { id: target }
            }));
            if (handled && fragment() === target) {
              // Native navigation can close a shared search. Retain the complete arriving
              // query in this selected entry while leaving the old notice in Back history.
              if (location.search !== dest.search) history.replaceState(history.state, '', dest.href);
              return;
            }
          }
          location.assign(dest.href);
        });
        li.append(a); ul.append(li);
      });
      note.append(ul);
    }
    const parent = main || document.querySelector('main');
    parent.before(note);
    const current = note;
    requestAnimationFrame(() => {
      if (current === note && !document.querySelector('dialog[open]')) current.scrollIntoView({ block: 'start' });
    });
  }
  function filterAddress(id) {
    return id === 'examples-filter-note' && data.page === 'reference.html' && runtime.has(id);
  }
  function syncFilter(id) {
    const control = document.getElementById(id);
    if (control && !control.hidden) { clear(); return; }
    if (control || document.readyState !== 'loading') {
      show(id, null, 'The “Show all” control is unavailable while no status filter is active.');
    }
  }
  function route(event) {
    pending = '';
    const id = fragment();
    if (!id) {
      clear();
      if (!main) go(data.book);
      return;
    }
    if (filterAddress(id)) { syncFilter(id); return; }
    if (history.state && history.state.bookAddressChoice === id && main) { clear(); return; }
    const own = Object.prototype.hasOwnProperty.call(data.routes, id);
    if (!own && main && (local.has(id) || runtime.has(id))) { clear(); return; }
    const entry = own ? data.routes[id] : null;
    if (typeof entry === 'string') { clear(); go(entry); return; }
    show(id, entry);
    if (event) event.stopImmediatePropagation();
  }
  // A companion's native fallback tries the book for every unknown hash. Keep the
  // address on its actual page while an unavailable or changed-passage notice is open.
  document.addEventListener('qh:leave', e => {
    if (pending || (note && fragment() === note.dataset.fragment && e.detail && e.detail.how === 'replace')) {
      e.preventDefault();
    }
  }, true);
  document.addEventListener('qh:unknown-anchor', e => {
    if (note && e.detail && e.detail.id === note.dataset.fragment) e.preventDefault();
  }, true);
  document.addEventListener('qh:state', () => {
    const id = fragment();
    if (note && id !== note.dataset.fragment) clear();
    if (filterAddress(id)) { syncFilter(id); return; }
    // The native reader pushes its own history entry when a citation or its preview
    // opens the current object. Preserve that choice when the reader uses Forward.
    if (!note && local.has(id) && Array.isArray(data.routes[id])) rememberChoice(id);
  });
  document.addEventListener('click', e => {
    if (!main || e.defaultPrevented || e.button || e.ctrlKey || e.shiftKey || e.altKey || e.metaKey) return;
    const a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a || a.closest('.bookmark-message') || a.target || a.hasAttribute('download')) return;
    const dest = new URL(a.getAttribute('href'), location.href);
    let id;
    try { id = decodeURIComponent(dest.hash.slice(1)); } catch (error) { id = dest.hash.slice(1); }
    // A citation in the current text uses the current object's ID, even if a saved
    // address from another context needs a choice on entry.
    if (!id || local.has(id)) return;
    if (runtime.has(id)) return;
    // The native reader cancels an unrecognised in-page href before hashchange. Let
    // this actual navigation create the history entry even for an unavailable address.
    e.preventDefault();
    e.stopImmediatePropagation();
    if (dest.href === location.href) route(); else location.assign(dest.href);
  }, true);
  window.addEventListener('popstate', route, true);
  window.addEventListener('hashchange', route, true);
  window.addEventListener('pageshow', e => { if (e.persisted) route(); });
  route();
  const initialPlace = fragment();
  // Some split runtimes record their initial place before reopening a shared query.
  // Restore the actual incoming parameters once, after their synchronous startup.
  document.addEventListener('DOMContentLoaded', () => {
    if (filterAddress(fragment())) syncFilter(fragment());
    if (!main || pending || fragment() !== initialPlace || location.search === incomingQuery) return;
    const u = new URL(location.href);
    u.search = incomingQuery;
    history.replaceState(history.state, '', u.href);
  }, {once:true});
})();
