// Evaluate one JS expression at several widths.
//   node tools/run.mjs tools/probe.mjs <page.html> <widths> <expression-file.js> [scheme] [fragment]
import { readFileSync } from 'node:fs';
import { fileUrl } from './cdp.mjs';

export default async function (b, [pagePath, widths, exprFile, scheme = 'light', fragment = '']) {
  const expr = readFileSync(exprFile, 'utf8');
  const out = {};
  for (const w of widths.split(',')) {
    const p = await b.page({ width: +w, height: 900, scheme, mobile: +w <= 480 });
    await p.goto(fileUrl(pagePath) + (fragment ? '#' + fragment : ''), 600);
    out[w] = { value: await p.eval(expr), console: p.log.slice() };
    await p.close();
  }
  return out;
}
