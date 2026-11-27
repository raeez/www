(() => { const vw = document.documentElement.clientWidth; const out = [];
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect(); if (!r.width || r.right <= vw + 1) continue;
    let clipped = false;
    for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) { const o = getComputedStyle(a).overflowX; if (o !== 'visible') { clipped = true; break; } }
    if (clipped || getComputedStyle(el).position === 'fixed') continue;
    if (el.closest('#card')) continue;
    out.push(el.localName + '.' + String(el.className.baseVal ?? el.className).split(' ').slice(0,2).join('.') + ' right=' + Math.round(r.right) + ' in=' + ((el.closest('[id]') || {}).id || ''));
    if (out.length > 8) break; }
  return { vw, sw: document.documentElement.scrollWidth, out }; })()
