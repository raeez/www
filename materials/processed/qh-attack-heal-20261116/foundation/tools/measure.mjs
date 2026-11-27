// Layout measurements of a built page at the representative widths, in both themes.
//   node tools/run.mjs tools/measure.mjs <page.html> <label> [shots]
// Prints JSON: per width and scheme, document height, page-level horizontal overflow,
// section heights, elements wider than the viewport, and console errors. With "shots",
// saves a viewport screenshot at each width into shots/<label>-<width>-<scheme>.png.
import { fileUrl } from './cdp.mjs';
import { resolve } from 'node:path';

const WIDTHS = [1400, 1024, 768, 480, 375];

export default async function (b, [pagePath, label = 'page', shots]) {
  const url = fileUrl(pagePath);
  const out = { page: pagePath, rows: [] };
  for (const scheme of ['light', 'dark']) {
    for (const width of WIDTHS) {
      const p = await b.page({ width, height: 900, scheme, mobile: width <= 480, touch: width <= 480 });
      await p.goto(url, 500);
      const m = await p.eval(`(() => {
        const de = document.documentElement;
        const sections = {};
        for (const s of document.querySelectorAll('main > section[id], main > header[id], main > aside[id], main > [data-atlas-mount]')) {
          sections[s.id || s.getAttribute('data-atlas-mount')] = Math.round(s.getBoundingClientRect().height);
        }
        const vw = de.clientWidth;
        const wide = [];
        for (const el of document.querySelectorAll('main *')) {
          const r = el.getBoundingClientRect();
          if (r.width > 0 && (r.right > vw + 1 || r.left < -1)) {
            let scrolled = false;
            for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) {
              const o = getComputedStyle(a).overflowX;
              if (o === 'auto' || o === 'scroll' || o === 'hidden' || o === 'clip') { scrolled = true; break; }
            }
            if (!scrolled && getComputedStyle(el).position !== 'fixed') wide.push(el.localName + (el.id ? '#' + el.id : '') + '.' + (el.className && el.className.baseVal === undefined ? String(el.className).split(' ').join('.') : ''));
          }
          if (wide.length > 12) break;
        }
        return { height: de.scrollHeight, scrollWidth: de.scrollWidth, clientWidth: vw, overflowX: de.scrollWidth > vw + 1,
                 sections, wide, statementsVisible: [...document.querySelectorAll('main .statement')].filter(e => e.getClientRects().length).length };
      })()`);
      if (shots) await p.screenshot(resolve('shots', `${label}-${width}-${scheme}.png`));
      out.rows.push({ scheme, width, ...m, console: p.log.slice() });
      await p.close();
    }
  }
  return out;
}
