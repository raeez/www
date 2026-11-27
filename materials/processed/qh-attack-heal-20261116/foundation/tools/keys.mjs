// Keyboard walk: real Tab key events from the top of the page (or from a fragment).
//   node tools/run.mjs tools/keys.mjs <page.html> [count=60] [fragment] [width=1400]
// Reports each focused element, whether it shows a focus indicator (outline or box-shadow),
// whether it is inside the viewport after focus, and repeated stops (a trap sign).
import { fileUrl } from './cdp.mjs';

export default async function (b, [pagePath, count = '60', fragment = '', width = '1400']) {
  const p = await b.page({ width: +width, height: 900, scheme: 'light', reduced: 'reduce' });
  await p.goto(fileUrl(pagePath) + (fragment ? '#' + fragment : ''), 600);
  if (fragment) await p.eval(`(document.getElementById(${JSON.stringify(fragment)}) || document.body).focus && 0`);
  const stops = [];
  for (let i = 0; i < +count; i++) {
    await p.key('Tab');
    const d = await p.eval(`(() => {
      const el = document.activeElement;
      if (!el || el === document.body) return { tag: 'body' };
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      const bar = document.querySelector('.bar');
      const barH = bar ? bar.getBoundingClientRect().bottom : 0;
      const label = (el.getAttribute('aria-label') || el.textContent || '').replace(/\\s+/g, ' ').trim().slice(0, 60);
      const ring = (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) || (cs.boxShadow && cs.boxShadow !== 'none');
      let host = el.closest('[id]');
      return { tag: el.localName, cls: String(el.className).slice(0, 40), label, ring,
               inView: r.bottom > 0 && r.top < innerHeight && r.width > 0, underBar: r.top < barH && !el.closest('.bar'),
               within: host ? host.id : '' };
    })()`);
    stops.push(d);
  }
  const seen = new Map();
  stops.forEach((s, i) => { const k = s.tag + '|' + s.cls + '|' + s.label + '|' + s.within; seen.set(k, (seen.get(k) || []).concat(i)); });
  const repeats = [...seen.entries()].filter(([, v]) => v.length > 1).map(([k, v]) => ({ k, at: v }));
  const out = { stops, noRing: stops.filter((s) => s.tag !== 'body' && !s.ring).length,
                outOfView: stops.filter((s) => s.tag !== 'body' && !s.inView).length,
                underBar: stops.filter((s) => s.underBar).length, repeats, console: p.log.slice() };
  await p.close();
  return out;
}
