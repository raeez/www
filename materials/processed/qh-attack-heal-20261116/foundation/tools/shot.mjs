// Viewport screenshots at chosen fragments, widths and schemes.
//   node tools/run.mjs tools/shot.mjs <page.html> <outprefix> <width>[,<width>...] <fragment|top>[,<fragment>...] [scheme=light] [height=900] [reduced]
import { fileUrl } from './cdp.mjs';
import { resolve } from 'node:path';

export default async function (b, [pagePath, prefix, widths, frags, scheme = 'light', height = '900', reduced]) {
  const done = [];
  for (const w of widths.split(',')) {
    for (const f of frags.split(',')) {
      const p = await b.page({ width: +w, height: +height, scheme, mobile: +w <= 480, reduced: reduced ? 'reduce' : 'no-preference' });
      await p.goto(fileUrl(pagePath) + (f && f !== 'top' ? '#' + f : ''), 700);
      if (f && f !== 'top') await p.eval(`(() => { const e = document.getElementById(${JSON.stringify(f)}); if (e) { e.scrollIntoView({ block: 'start', behavior: 'instant' }); } })()`);
      await new Promise((r) => setTimeout(r, 250));
      const path = resolve(`${prefix}-${w}-${scheme}-${f || 'top'}.png`);
      await p.screenshot(path);
      done.push({ path, console: p.log.slice() });
      await p.close();
    }
  }
  return done;
}
