// In-page measurement helpers, installed as window.__a2 after each load. Read-only on the document
// except where a test says otherwise.
export const INSTALL = `() => {
  const MML = 'http://www.w3.org/1998/Math/MathML';
  const d = (el) => { if (!el || !el.localName) return String(el); let s = el.localName; if (el.id) s += '#' + el.id;
    if (el.classList && el.classList.length) s += '.' + [...el.classList].join('.');
    const t = (el.getAttribute && el.getAttribute('aria-label')) || el.textContent || ''; const tt = t.trim().replace(/\\s+/g, ' ').slice(0, 48);
    return s + (tt ? ' "' + tt + '"' : ''); };
  const clipAncestor = (el) => { for (let p = el.parentElement; p && p !== document.documentElement && p !== document.body; p = p.parentElement) {
      const c = getComputedStyle(p); if (c.overflowX !== 'visible' || c.overflowY !== 'visible') return p; } return null; };
  const focusInfo = () => {
    const el = document.activeElement; if (!el || el === document.body) return { el: d(el) };
    const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); const bar = document.querySelector('.bar').getBoundingClientRect();
    const ext = cs.outlineStyle !== 'none' ? (parseFloat(cs.outlineWidth) || 0) + (parseFloat(cs.outlineOffset) || 0) : 0;
    const ca = clipAncestor(el); let clipped = null;
    if (ca && ext > 0) { const cr = ca.getBoundingClientRect(), cc = getComputedStyle(ca);
      const pb = { l: cr.left + parseFloat(cc.borderLeftWidth), t: cr.top + parseFloat(cc.borderTopWidth), r: cr.right - parseFloat(cc.borderRightWidth), b: cr.bottom - parseFloat(cc.borderBottomWidth) };
      clipped = { top: +Math.max(0, pb.t - (r.top - ext)).toFixed(1), bottom: +Math.max(0, (r.bottom + ext) - pb.b).toFixed(1),
                  left: +Math.max(0, pb.l - (r.left - ext)).toFixed(1), right: +Math.max(0, (r.right + ext) - pb.r).toFixed(1), by: d(ca).slice(0, 40) }; }
    return { el: d(el), rect: [r.left, r.top, r.right, r.bottom].map(Math.round), outline: cs.outlineStyle + ' ' + cs.outlineWidth + ' off ' + cs.outlineOffset,
      fv: el.matches(':focus-visible'), underBar: !el.closest('.bar') && r.top < bar.bottom - 1 && r.bottom > bar.top, inView: r.bottom > 0 && r.top < innerHeight,
      clipped, scrollY: Math.round(scrollY) };
  };
  const SEL = 'a[href], button:not([disabled]), input:not([disabled]), select, textarea, summary, [tabindex]:not([tabindex="-1"])';
  const tabbables = () => [...document.querySelectorAll(SEL)].filter((el) => el.tabIndex >= 0 && el.checkVisibility({ checkVisibilityCSS: true }));
  const categorize = (list) => { const cats = {}; const rules = [['term', '.term'], ['cell-btn', '.cell-btn'], ['col-head', '.col-head'], ['summary', 'summary'],
      ['grid row link', '.grid tbody th a'], ['q-index link', '.q-index a'], ['heading anchor', '.anchor'], ['nav link', '.nav a'], ['tally link', '.tally a'],
      ['filter chip', '.filter'], ['link-btn', '.link-btn'], ['math scroller', '[data-scroll-focus]'], ['change link', '.change-link'], ['grid-wrap', '.grid-wrap'], ['input', 'input']];
    for (const el of list) { const k = (rules.find(([, s]) => el.matches(s)) || ['other'])[0]; cats[k] = (cats[k] || 0) + 1; } return cats; };
  const M = () => {
    const de = document.documentElement, vw = de.clientWidth;
    const o = { innerWidth, clientWidth: vw, scrollWidth: de.scrollWidth, docHeight: de.scrollHeight };
    const bar = document.querySelector('.bar').getBoundingClientRect(); o.barHeight = bar.height; o.scrollPaddingTop = getComputedStyle(de).scrollPaddingTop;
    const nav = document.querySelector('.nav'); const na = nav.querySelector('a');
    o.nav = { clientW: nav.clientWidth, scrollW: nav.scrollWidth, navH: +nav.getBoundingClientRect().height.toFixed(1), linkH: +na.getBoundingClientRect().height.toFixed(1), overflowY: getComputedStyle(nav).overflowY,
      lastLinkRight: Math.round(nav.querySelector('li:last-child a').getBoundingClientRect().right), navRight: Math.round(nav.getBoundingClientRect().right) };
    const gw = document.querySelector('.grid-wrap'); o.grid = { wrapClientW: gw.clientWidth, wrapScrollW: gw.scrollWidth, tableW: Math.round(document.querySelector('.grid').getBoundingClientRect().width), wrapOverflowY: getComputedStyle(gw).overflowY };
    const off = [];
    for (const el of document.querySelectorAll('body *')) {
      if (el.namespaceURI === MML && el.localName !== 'math') continue;
      if (el.closest('.visually-hidden, .skip, #card, script, style')) continue;
      const r = el.getBoundingClientRect(); if (!r.width && !r.height) continue;
      if (r.right > vw + 0.5 || r.left < -0.5) { const ca = clipAncestor(el); if (ca) continue; if (!el.checkVisibility()) continue;
        off.push(d(el).slice(0, 90) + ' L=' + Math.round(r.left) + ' R=' + Math.round(r.right)); if (off.length > 20) break; }
    }
    o.pageOverflowers = off;
    let hs = 0; const vclip = [];
    for (const b of document.querySelectorAll('.math-display, .math-long')) { if (!b.checkVisibility()) continue;
      if (b.scrollWidth > b.clientWidth + 1) hs++;
      if (b.scrollHeight > b.clientHeight + 1) vclip.push((d(b.closest('[id]')) || '').slice(0, 60) + ' sh=' + b.scrollHeight + ' ch=' + b.clientHeight); }
    o.math = { horizontallyScrolling: hs, verticallyClipped: vclip.length, vclipSample: vclip.slice(0, 6) };
    o.rowSummaryOverflow = [...document.querySelectorAll('.row > summary')].filter((s) => s.scrollWidth > s.clientWidth + 1).map((s) => s.parentElement.id + ' sw=' + s.scrollWidth + ' cw=' + s.clientWidth);
    o.statementOverflow = [...document.querySelectorAll('.statement')].filter((s) => s.checkVisibility() && s.scrollWidth > s.clientWidth + 1).slice(0, 8).map((s) => (s.id || d(s).slice(0, 50)) + ' sw=' + s.scrollWidth + ' cw=' + s.clientWidth);
    const qc = document.querySelector('.question.compare'); o.compareCols = qc ? getComputedStyle(qc).gridTemplateColumns : null;
    const f = document.querySelector('.find'); o.find = f ? { after: d(f.previousElementSibling).slice(0, 40), width: Math.round(f.getBoundingClientRect().width) } : null;
    return o;
  };
  window.__a2 = { d, focusInfo, tabbables, categorize, M, clipAncestor };
  return true;
}`;
