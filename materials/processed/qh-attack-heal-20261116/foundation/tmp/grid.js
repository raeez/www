(() => { const w = document.querySelector('.grid-wrap'), g = document.querySelector('.grid');
  const th = [...g.querySelectorAll('thead th')].map(t => Math.round(t.getBoundingClientRect().width));
  return { wrap: w.clientWidth, table: Math.round(g.getBoundingClientRect().width), scrolls: w.scrollWidth > w.clientWidth + 1, th,
           tableHeight: Math.round(g.getBoundingClientRect().height), rowH: Math.round(g.tBodies[0].rows[0].getBoundingClientRect().height) }; })()
