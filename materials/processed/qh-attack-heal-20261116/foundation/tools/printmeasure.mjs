// Section and row heights under print media at the A4 text width, every disclosure open.
//   node tools/run.mjs tools/printmeasure.mjs <page.html>
import { fileUrl } from './cdp.mjs';
export default async function (b, [pagePath]) {
  const p = await b.page({ width: 673, height: 1000, scheme: 'light', media: 'print' });
  await p.goto(fileUrl(pagePath), 600);
  const r = await p.eval(`(() => { document.querySelectorAll('main details').forEach(d => d.open = true);
    const h = (e) => Math.round(e.getBoundingClientRect().height);
    const out = { sections: {}, rows: [], gridTable: h(document.querySelector('table.grid')) };
    document.querySelectorAll('main > section[id], main > header, main > nav, main > div').forEach(s => out.sections[s.id || s.className] = h(s));
    document.querySelectorAll('details.row').forEach(d => out.rows.push([d.id, h(d), h(d.querySelector('.cell-lines')), h(d.querySelector('summary'))]));
    const st = document.querySelector('.rows .statement'); out.stmtFont = getComputedStyle(st).fontSize; out.stmtPad = getComputedStyle(st).padding;
    out.rowBody = getComputedStyle(document.querySelector('.row-body')).padding;
    out.cellLineCols = getComputedStyle(document.querySelector('.cell-line')).gridTemplateColumns;
    return out; })()`);
  await p.close();
  return r;
}
