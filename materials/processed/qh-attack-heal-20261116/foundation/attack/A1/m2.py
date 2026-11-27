import sys, json, time
sys.path.insert(0, sys.argv[1])
from cdp import Chrome
S = sys.argv[1]; P = sys.argv[2]
URL = 'file://' + P
out = {}

def rect(c, sel, idx=0):
    return c.js(f'''(() => {{ const e = document.querySelectorAll({json.dumps(sel)})[{idx}]; if (!e) return null;
      const r = e.getBoundingClientRect(); return {{x: r.left + r.width/2, y: r.top + r.height/2, top: r.top, bottom: r.bottom, left: r.left, right: r.right, h: r.height, w: r.width}}; }})()''')

def tap(c, x, y, touch=False):
    if touch:
        c.send('Input.dispatchTouchEvent', {'type': 'touchStart', 'touchPoints': [{'x': x, 'y': y}]})
        c.send('Input.dispatchTouchEvent', {'type': 'touchEnd', 'touchPoints': []})
    else:
        c.click(x, y)

STATE = r'''(() => { const bar = document.querySelector('.bar').getBoundingClientRect().bottom;
  return {scrollY: Math.round(scrollY), hash: location.hash, barBottom: Math.round(bar), active: document.activeElement ? (document.activeElement.id || document.activeElement.className || document.activeElement.localName) : null}; })()'''

def card_parts(c, qid):
    return c.js(f'''(() => {{ const q = document.getElementById({json.dumps(qid)}); const bar = document.querySelector('.bar').getBoundingClientRect().bottom;
      const t = s => [...q.querySelectorAll(s)].map(e => e.textContent.replace(/\\s+/g,' ').trim().slice(0,90));
      const h3 = q.querySelector('h3').getBoundingClientRect();
      const ask = q.querySelector('.question-ask, :scope > .statement'); const kn = q.querySelector('.question-known, details.known');
      return {{h3Top: Math.round(h3.top), h3Bottom: Math.round(h3.bottom), barBottom: Math.round(bar), cardTop: Math.round(q.getBoundingClientRect().top),
        num: t('.question-num'), title: t('h3'), chips: t('.status-chip'), stTitles: t('.statement-title'), labels: t('.question-why-label, .known-label, .known > summary > span:first-child'),
        counts: t('.row-count'), askRect: ask ? [Math.round(ask.getBoundingClientRect().top), Math.round(ask.getBoundingClientRect().bottom), Math.round(ask.getBoundingClientRect().left), Math.round(ask.getBoundingClientRect().right)] : null,
        knownRect: kn ? [Math.round(kn.getBoundingClientRect().top), Math.round(kn.getBoundingClientRect().bottom), Math.round(kn.getBoundingClientRect().left), Math.round(kn.getBoundingClientRect().right)] : null,
        links: [...q.querySelectorAll('a[href]')].map(a => a.getAttribute('href'))}}; }})()''')

c = Chrome(S + '/chrome')
try:
    c.open_page()
    # ---------- A. 1400 desktop route ----------
    c.viewport(1400, 900); c.media('light', 'reduce')
    c.goto(URL, 2.0)
    r = c.js(r'''(() => { const a = [...document.querySelectorAll('.nav a')].find(a => a.getAttribute('href') === '#decisive'); const b = a.getBoundingClientRect(); return {x: b.left + b.width/2, y: b.top + b.height/2}; })()''')
    tap(c, r['x'], r['y']); time.sleep(0.8)
    st = c.js(STATE)
    st['h2Top'] = round(c.js("document.getElementById('decisive-h').getBoundingClientRect().top"))
    st['indexTop'] = round(c.js("document.querySelector('#decisive .q-index').getBoundingClientRect().top"))
    st['indexBottom'] = round(c.js("document.querySelector('#decisive .q-index').getBoundingClientRect().bottom"))
    st['visibleIndexEntries'] = c.js("[...document.querySelectorAll('#decisive .q-index li')].filter(li => { const r = li.getBoundingClientRect(); return r.bottom <= innerHeight && r.top >= 51; }).length")
    out['A1_after_nav_click'] = st
    c.shot(f'{S}/r1400-1-decisive.png')
    # scroll index entry 12 into view and click it
    c.js("document.querySelectorAll('#decisive .q-index li')[11].scrollIntoView({block:'center'})"); time.sleep(0.3)
    e = rect(c, '#decisive .q-index li a', 11)
    tap(c, e['x'], e['y']); time.sleep(0.8)
    out['A2_after_index_click'] = c.js(STATE)
    out['A2_card'] = card_parts(c, 'q-d-elliptic-relative-cubic')
    c.shot(f'{S}/r1400-2-q12.png')
    # back
    c.js("history.back()"); time.sleep(0.8)
    out['A3_after_back'] = c.js(STATE)
    # Q3 middle: blank left column
    c.js("(() => { const q = document.getElementById('q-d-centre-base-change'); scrollTo(0, q.getBoundingClientRect().top + scrollY + 2600); })()"); time.sleep(0.4)
    out['A4_q3_mid'] = card_parts(c, 'q-d-centre-base-change')
    c.shot(f'{S}/r1400-3-q3-mid.png')

    # ---------- B. 375 touch route ----------
    c.viewport(375, 812, mobile=True)
    c.send('Emulation.setTouchEmulationEnabled', {'enabled': True, 'maxTouchPoints': 5})
    c.media('light', 'reduce')
    c.goto(URL, 2.0)
    out['B0_media'] = c.js("({hover: matchMedia('(hover: hover)').matches, coarse: matchMedia('(pointer: coarse)').matches, fine: matchMedia('(pointer: fine)').matches})")
    r = c.js(r'''(() => { const a = [...document.querySelectorAll('.nav a')].find(a => a.getAttribute('href') === '#decisive'); const b = a.getBoundingClientRect(); return {x: Math.min(b.left + b.width/2, 300), y: b.top + b.height/2, right: b.right}; })()''')
    tap(c, r['x'], r['y'], touch=True); time.sleep(0.8)
    st = c.js(STATE)
    st['h2Top'] = round(c.js("document.getElementById('decisive-h').getBoundingClientRect().top"))
    st['indexTop'] = round(c.js("document.querySelector('#decisive .q-index').getBoundingClientRect().top"))
    st['visibleIndexEntries'] = c.js("[...document.querySelectorAll('#decisive .q-index li')].filter(li => { const r = li.getBoundingClientRect(); return r.bottom <= innerHeight && r.top >= 51; }).length")
    out['B1_after_nav_tap'] = st
    c.shot(f'{S}/r375-1-decisive.png')
    c.js("document.querySelectorAll('#decisive .q-index li')[11].scrollIntoView({block:'center'})"); time.sleep(0.3)
    c.shot(f'{S}/r375-2-index.png')
    e = rect(c, '#decisive .q-index li a', 11)
    tap(c, e['x'], e['y'], touch=True); time.sleep(0.8)
    out['B2_after_index_tap'] = c.js(STATE)
    out['B2_card'] = card_parts(c, 'q-d-elliptic-relative-cubic')
    c.shot(f'{S}/r375-3-q12.png')
    # scroll to the "Related statements" head of Q12
    c.js("document.querySelector('#q-d-elliptic-relative-cubic .known-head').scrollIntoView({block:'start'})"); time.sleep(0.3)
    c.shot(f'{S}/r375-4-q12-known.png')

    # ---------- C. grid task at 375 touch ----------
    c.js("location.hash = 'examples'"); time.sleep(0.6)
    c.js("document.querySelector('.grid-wrap').scrollIntoView({block:'start'})"); time.sleep(0.3)
    c.shot(f'{S}/g375-1-grid.png')
    # scroll the grid so the states column is visible, then tap Virasoro x states
    c.js("(() => { const td = document.querySelector('.cell-btn[data-row=\"row-virasoro\"]').closest('tr').cells[7]; const gw = document.querySelector('.grid-wrap'); gw.scrollLeft = td.offsetLeft - 120; td.scrollIntoView({block:'center', inline:'nearest'}); })()"); time.sleep(0.4)
    e = c.js("(() => { const b = document.querySelector('.cell-btn[data-row=\"row-virasoro\"]').closest('tr').cells[7].querySelector('button'); const r = b.getBoundingClientRect(); return {x: r.left + r.width/2, y: r.top + r.height/2, label: b.getAttribute('aria-label')}; })()")
    tap(c, e['x'], e['y'], touch=True); time.sleep(0.6)
    out['C1_cell'] = e
    out['C1_card'] = c.js("(() => { const k = document.getElementById('card'); const r = k.getBoundingClientRect(); return {hidden: k.hidden, cls: k.className, top: Math.round(r.top), bottom: Math.round(r.bottom), h: Math.round(r.height), text: k.textContent.replace(/\\s+/g,' ').trim().slice(0,400), links: [...k.querySelectorAll('a')].map(a => [a.getAttribute('href'), a.textContent])}; })()")
    c.shot(f'{S}/g375-2-cellcard.png')
    l = c.js("(() => { const a = document.querySelector('#card a.card-more'); if (!a) return null; const r = a.getBoundingClientRect(); return {x: r.left + r.width/2, y: r.top + r.height/2}; })()")
    if l:
        tap(c, l['x'], l['y'], touch=True); time.sleep(0.8)
    out['C2_after_row_link'] = c.js(STATE)
    out['C2_row'] = c.js("(() => { const d = document.getElementById('row-virasoro'); const r = d.getBoundingClientRect(); const cl = [...d.querySelectorAll('.cell-line')].map(x => x.textContent.replace(/\\s+/g,' ').trim().slice(0,80)); return {open: d.open, top: Math.round(r.top), h: Math.round(r.height), cellLines: cl.length, firstLines: cl.slice(6,8), stmts: d.querySelectorAll('.statement').length, links: [...d.querySelectorAll('.row-body a[href]')].map(a => a.getAttribute('href')).slice(0,10)}; })()")
    c.shot(f'{S}/g375-3-row.png')

    # ---------- D. hash links, fresh loads (375 touch) ----------
    for tid in ['s-affine-energy-lifting', 's-virasoro-doublet-fields']:
        c.goto('about:blank', 0.2)
        c.goto(URL + '#' + tid, 2.0)
        out['D_' + tid] = c.js(f'''(() => {{ const e = document.getElementById({json.dumps(tid)}); const r = e.getBoundingClientRect(); const d = e.closest('details');
           const bar = document.querySelector('.bar').getBoundingClientRect().bottom;
           return {{top: Math.round(r.top), bottom: Math.round(r.bottom), barBottom: Math.round(bar), detailsOpen: d ? d.open : null, scrollY: Math.round(scrollY),
             context: (e.closest('.question') ? 'question ' + e.closest('.question').id : (e.closest('details.row') ? 'row ' + e.closest('details.row').id : '')),
             contextHeadVisible: (() => {{ const q = e.closest('.question') || e.closest('details.row'); if (!q) return null; const h = q.querySelector('h3, summary'); const hr = h.getBoundingClientRect(); return hr.bottom > bar && hr.top < innerHeight; }})() }}; }})()''')
        c.shot(f'{S}/h375-{tid}.png')

    # ---------- E. tally "Open problem" route (375 touch) ----------
    c.goto('about:blank', 0.2)
    c.goto(URL, 2.0)
    c.js("document.querySelector('.tally').scrollIntoView({block:'center'})"); time.sleep(0.3)
    e = rect(c, '.tally a[data-filter="open"]')
    tap(c, e['x'], e['y'], touch=True); time.sleep(1.0)
    out['E_tally_open'] = c.js("(() => ({count: (document.querySelector('.find-count')||{}).textContent, groups: [...document.querySelectorAll('.find-group-head')].map(g => g.textContent), shownLinks: document.querySelectorAll('.find-link').length, more: (document.querySelector('.find-more')||{}).textContent || null, url: location.search, findTop: Math.round(document.querySelector('.find').getBoundingClientRect().top), resultsH: Math.round(document.querySelector('.find-results').getBoundingClientRect().height)}))()")
    c.shot(f'{S}/t375-open.png')
    out['console'] = c.console_errors()
    json.dump(out, open(S + '/m2.json', 'w'), indent=1)
finally:
    c.close()
print('ok')
