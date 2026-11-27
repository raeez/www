// Print checks: A4 and Letter PDFs, light scheme and dark scheme (print must be light on both).
//   node tools/run.mjs tools/print.mjs <page.html> <outdir>
// Writes <outdir>/<paper>-<scheme>.pdf and reports whether Chrome fired beforeprint (every
// disclosure open while printing), and which statement titles are present in the PDF text.
import { execFileSync } from 'node:child_process';
import { resolve } from 'node:path';
import { fileUrl } from './cdp.mjs';

const norm = (s) => s.normalize('NFKC').replace(/[\s\u00ad\u2010\u2011-]+/g, '').toLowerCase();

export default async function (b, [pagePath, outdir]) {
  const out = { runs: [] };
  for (const scheme of ['light', 'dark']) {
    for (const paper of ['A4', 'Letter']) {
      if (scheme === 'dark' && paper === 'Letter') continue;
      const p = await b.page({ width: 1200, height: 900, scheme });
      await p.goto(fileUrl(pagePath), 600);
      await p.eval(`window.__printed = 0; window.addEventListener('beforeprint', () => { window.__printed = document.querySelectorAll('main details:not([open])').length === 0 ? 1 : -1; });`);
      const titles = await p.eval(`[...document.querySelectorAll('main .statement-title')].filter(e => !e.querySelector('math')).map(e => e.textContent.replace(/\\s+/g,' ').trim())`);
      const path = resolve(outdir, `${paper}-${scheme}.pdf`);
      await p.pdf(path, { paper });
      const printed = await p.eval('window.__printed');
      const info = execFileSync('pdfinfo', [path]).toString();
      const pages = +(info.match(/Pages:\s+(\d+)/) || [0, 0])[1];
      const size = (info.match(/Page size:\s+(.*)/) || [0, ''])[1].trim();
      const text = execFileSync('pdftotext', ['-enc', 'UTF-8', path, '-']).toString();
      const hay = norm(text);
      const missing = titles.filter((t) => !hay.includes(norm(t)));
      const controls = ['Open all', 'Close all', 'Search this page', 'Skip to the page'].filter((w) => text.includes(w));
      // A page with almost no text where content should be is a fragmentation failure (content dropped).
      const blankPages = text.split('\f').slice(0, -1).map((pg, i) => [i + 1, pg.trim().length]).filter(([, n]) => n < 200).map(([i]) => i);
      out.runs.push({ paper, scheme, path, pages, size, beforeprintFired: printed, titlesChecked: titles.length,
                      titlesMissing: missing.length, missingSample: missing.slice(0, 8), screenControlsInPrint: controls, blankPages,
                      chars: text.length, console: p.log.slice() });
      await p.close();
    }
  }
  return out;
}
