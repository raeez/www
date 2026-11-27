(() => { document.querySelectorAll('main details').forEach(d => d.open = true);
  const out = [];
  for (const box of document.querySelectorAll('.math-display')) {
    const m = box.querySelector('math'); if (!m) { out.push(null); continue; }
    const fs = parseFloat(getComputedStyle(m).fontSize);
    let L = Infinity, R = -Infinity;
    for (const k of m.querySelectorAll('semantics > *:first-child')) { const r = k.getBoundingClientRect(); L = Math.min(L, r.left); R = Math.max(R, r.right); }
    out.push(Math.round((R - L) / fs * 100) / 100);
  }
  return out; })()
