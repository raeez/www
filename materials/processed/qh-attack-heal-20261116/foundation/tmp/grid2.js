(() => { const w = document.querySelector('.grid-wrap'), g = document.querySelector('.grid');
  const cell = document.querySelector('.grid tbody td .cell-btn').getBoundingClientRect();
  return { wrap: w.clientWidth, table: Math.round(g.getBoundingClientRect().width), fits: g.getBoundingClientRect().width <= w.clientWidth + 1,
           pageOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
           cellTarget: [Math.round(cell.width), Math.round(cell.height)], tableHeight: Math.round(g.getBoundingClientRect().height),
           headH: Math.round(g.tHead.getBoundingClientRect().height) }; })()
