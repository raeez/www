// Reduced motion: scroll behaviour and transitions under prefers-reduced-motion: reduce and no-preference.
import { fileUrl } from './cdp.mjs';
export default async function (b, [pagePath]) {
  const out = {};
  for (const reduced of ['reduce', 'no-preference']) {
    const p = await b.page({ width: 1400, height: 900, scheme: 'light', reduced });
    await p.goto(fileUrl(pagePath), 500);
    out[reduced] = await p.eval(`(() => { const moving = [];
      for (const el of document.querySelectorAll('body *')) { const cs = getComputedStyle(el);
        const d = cs.transitionDuration.split(',').some(x => parseFloat(x) > 0) || cs.animationName !== 'none';
        if (d) moving.push(el.localName + '.' + String(el.className.baseVal ?? el.className).split(' ')[0]); if (moving.length > 10) break; }
      return { scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior, moving: [...new Set(moving)] }; })()`);
    await p.close();
  }
  return out;
}
