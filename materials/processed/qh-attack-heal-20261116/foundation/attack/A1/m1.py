import sys, json, time
sys.path.insert(0, sys.argv[1])
from cdp import Chrome
S = sys.argv[1]; P = sys.argv[2]
URL = 'file://' + P
GEOM = r'''
(() => {
  const out = {};
  const sy = window.scrollY;
  out.vw = innerWidth; out.vh = innerHeight;
  out.scrollHeight = document.documentElement.scrollHeight;
  out.docOverflowX = document.documentElement.scrollWidth - document.documentElement.clientWidth;
  const ids = ['programme','status','results','decisive','frontier','examples','failures','open','essay','terms'];
  out.sections = {};
  for (const id of ids) { const e = document.getElementById(id); if (!e) continue; const r = e.getBoundingClientRect();
    out.sections[id] = {top: Math.round(r.top + sy), h: Math.round(r.height)}; }
  const misc = {lead: '.lead', tally: '.tally', find: '.find', foot: '.foot'};
  out.misc = {};
  for (const k in misc) { const e = document.querySelector(misc[k]); if (!e) continue; const r = e.getBoundingClientRect(); out.misc[k] = {top: Math.round(r.top+sy), h: Math.round(r.height)}; }
  // statements per section
  out.stmts = {};
  for (const id of ids) { const e = document.getElementById(id); if (!e) continue;
    const all = e.querySelectorAll('article.statement'); const noid = [...all].filter(a => !a.id).length;
    out.stmts[id] = {n: all.length, noid}; }
  out.stmtsTotal = document.querySelectorAll('article.statement').length;
  out.stmtsNoId = [...document.querySelectorAll('article.statement')].filter(a => !a.id).length;
  // decisive & frontier detail
  for (const id of ['decisive','frontier']) {
    const sec = document.getElementById(id); if (!sec) continue;
    const st = sec.getBoundingClientRect().top + sy;
    const idx = sec.querySelector('.q-index');
    const qs = [...sec.querySelectorAll('.questions > .question')];
    const d = {};
    d.indexTopRel = idx ? Math.round(idx.getBoundingClientRect().top + sy - st) : null;
    d.indexH = idx ? Math.round(idx.getBoundingClientRect().height) : null;
    d.introH = sec.querySelector('.section-intro') ? Math.round(sec.querySelector('.section-intro').getBoundingClientRect().height) : null;
    d.firstQTopRel = qs.length ? Math.round(qs[0].getBoundingClientRect().top + sy - st) : null;
    d.nq = qs.length;
    d.q = qs.map((q, i) => {
      const r = q.getBoundingClientRect();
      const ask = q.querySelector('.question-ask') || q;
      const asked = q.querySelector(':scope > .statement, :scope > .question-ask > .statement');
      const why = q.querySelector('.question-why');
      const kn = q.querySelector('.question-known, details.known');
      const links = [...q.querySelectorAll('a[href]')].map(a => a.getAttribute('href')).filter(h => h !== '#' + q.id);
      return {i: i+1, id: q.id, h: Math.round(r.height),
        askH: asked ? Math.round(asked.getBoundingClientRect().height) : null,
        whyH: why ? Math.round(why.getBoundingClientRect().height) : null,
        knownH: kn ? Math.round(kn.getBoundingClientRect().height) : null,
        nKnown: q.querySelectorAll('.question-known .statement, details.known .statement').length,
        knownOpen: kn && kn.localName === 'details' ? kn.open : null,
        otherLinks: links};
    });
    out[id] = d;
  }
  // grid
  const gw = document.querySelector('.grid-wrap');
  if (gw) { const r = gw.getBoundingClientRect(); out.grid = {top: Math.round(r.top+sy), h: Math.round(r.height), clientW: gw.clientWidth, scrollW: gw.scrollWidth,
     tableW: Math.round(document.querySelector('.grid').getBoundingClientRect().width),
     colHeads: [...document.querySelectorAll('.col-head')].map(b => [b.textContent, Math.round(b.getBoundingClientRect().width)]),
     rowHeadW: Math.round(document.querySelector('.grid tbody th').getBoundingClientRect().width)}; }
  const rows = document.querySelector('.rows'); if (rows) { const r = rows.getBoundingClientRect(); out.rowsBlock = {top: Math.round(r.top+sy), h: Math.round(r.height)}; }
  // nav
  const nav = document.querySelector('.nav'); const nr = nav.getBoundingClientRect();
  out.nav = {left: Math.round(nr.left), right: Math.round(nr.right), scrollW: nav.scrollWidth, clientW: nav.clientWidth,
    links: [...nav.querySelectorAll('a')].map(a => { const r = a.getBoundingClientRect(); return [a.textContent, Math.round(r.left), Math.round(r.right), r.right <= nr.right ? 'visible' : (r.left < nr.right ? 'partly' : 'hidden')]; })};
  const bar = document.querySelector('.bar'); out.barH = Math.round(bar.getBoundingClientRect().height);
  // tabbables before first q-index link
  const TAB = 'a[href], button:not([disabled]), input:not([disabled]), summary, [tabindex]:not([tabindex="-1"])';
  const tabs = [...document.querySelectorAll(TAB)].filter(e => { if (e.closest('[hidden], #card')) return false;
     for (let c = e, p = e.parentElement; p; c = p, p = p.parentElement) { if (p.localName === 'details' && !p.open && !(c.localName==='summary' && c.parentNode===p)) return false; } 
     const cs = getComputedStyle(e); return cs.visibility !== 'hidden' && e.getClientRects().length > 0; });
  const firstIdx = document.querySelector('#decisive .q-index a');
  out.tabsTotal = tabs.length;
  out.tabsBeforeDecisiveIndex = tabs.indexOf(firstIdx);
  const firstFrontier = document.querySelector('#frontier .q-index a');
  out.tabsBeforeFrontierIndex = tabs.indexOf(firstFrontier);
  const firstCell = document.querySelector('.cell-btn');
  out.tabsBeforeGrid = tabs.indexOf(firstCell);
  out.termButtonsInDecisive = document.querySelectorAll('#decisive .term').length;
  out.tabsInDecisive = tabs.filter(t => t.closest('#decisive')).length;
  return out;
})()
'''
c = Chrome(S + '/chrome')
try:
    c.open_page()
    res = {}
    for (w, h) in [(1400, 900), (1024, 768), (768, 1024), (480, 900), (375, 812)]:
        c.viewport(w, h, mobile=(w <= 480))
        c.media('light', 'reduce')
        c.goto(URL, settle=2.0)
        res[f'{w}'] = c.js(GEOM)
        if w in (1400, 375):
            c.shot(f'{S}/top-{w}-light.png')
    res['console'] = c.console_errors()
    json.dump(res, open(S + '/m1.json', 'w'), indent=1)
finally:
    c.close()
print('ok')
