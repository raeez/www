(() => { document.querySelectorAll('main details').forEach(d => d.open = true);
  const rows = [];
  for (const box of document.querySelectorAll('main .math-display, main .math-long')) {
    const m = box.querySelector('math'); if (!m) continue;
    const rr = m.getBoundingClientRect(); let right = rr.left + Math.max(rr.width, m.scrollWidth);
    for (const k of m.querySelectorAll('semantics > *:first-child')) right = Math.max(right, k.getBoundingClientRect().right);
    let left = rr.right; for (const k of m.querySelectorAll('semantics > *:first-child')) left = Math.min(left, k.getBoundingClientRect().left);
    const tex = (m.querySelector('annotation') || {}).textContent || '';
    rows.push([box.classList.contains('math-display') ? 'D' : 'L', Math.round(right - left), tex.length, (box.closest('[id]') || {}).id]);
  }
  rows.sort((a, b) => b[1] - a[1]);
  return rows.slice(0, 25);
})()
