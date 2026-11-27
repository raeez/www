// Static checks of a built status page against its reader inputs (EVAL-PLAN Q02-Q10, Q04-Q05 scans).
// Usage: QH_JSDOM=<path to jsdom package> node qh-static.mjs --html <preview.html> --content <content dir>
//        [--page <page.json>] [--baseline-html <preview.html>] [--out <result.json>]
// Reads only; writes only the --out file.
import fs from 'node:fs';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { JSDOM } = require(process.env.QH_JSDOM || 'jsdom');

const args = {};
for (let i = 2; i < process.argv.length; i += 2) args[process.argv[i].replace(/^--/, '')] = process.argv[i + 1];
const contentDir = args.content;
const page = JSON.parse(fs.readFileSync(args.page || `${contentDir}/page.json`, 'utf8'));
const contentRaw = fs.readFileSync(`${contentDir}/content.json`);
const c = JSON.parse(contentRaw.toString('utf8'));
const essayRaw = fs.existsSync(`${contentDir}/essay.md`) ? fs.readFileSync(`${contentDir}/essay.md`) : Buffer.from('');
const html = fs.readFileSync(args.html, 'utf8');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');

// 'refuted form' is a checked negative result in a stated scope (atlas code scoped_negative), with its hypotheses.
const STATEMENT_STATUSES = ['checked', 'pending', 'conditional', 'refuted form', 'conjecture', 'heuristic', 'open', 'published'];
const CELL_STATUSES = ['checked', 'partial', 'pending', 'published', 'open', 'not posed', 'refuted form'];
const COLUMNS = ['object', 'dual', 'modules', 'fusion', 'bulk', 'lines', 'states', 'dictionary'];
const label = st => page.status_labels[st];

function ident(text) {
  let t = (text || '').normalize('NFKD').replace(/[^\x00-\x7f]/g, '');
  t = t.replace(/[^\w\s-]/g, '').trim().toLowerCase();
  return t.replace(/[\s_-]+/g, '-').slice(0, 60) || 'x';
}
const MATH_RE = /\\\((.+?)\\\)|\\\[(.+?)\\\]/gs;
const LINK_RE = /\[([^\[\]]+)\]\((https?:\/\/[^\s)]+)\)/g;
const ARXIV_RE = /arxiv\.org\/(?:abs|html|pdf)\/((?:math|hep-th|math-ph|alg-geom|q-alg)\/\d{7}|\d{4}\.\d{4,5})(v\d+)?/i;
function unlink(text) {
  return (text || '').replace(LINK_RE, (m, lab, url) => {
    const a = url.match(ARXIV_RE);
    return a && !lab.includes(a[1]) ? `${lab} (arXiv:${a[1]}${a[2] || ''})` : lab;
  });
}
function* allStatements(c) {
  yield* (c.principal || []);
  for (const key of ['decisive', 'frontier']) {
    for (const q of ((c[key] || {}).questions || [])) {
      if (q.question) yield q.question;
      yield* (q.known || []);
    }
  }
  for (const r of (c.rows || [])) yield* (r.statements || []);
  for (const f of ((c.failures || {}).items || [])) if (f.witness) yield f.witness;
  for (const g of (c.open || [])) yield* (g.statements || []);
}

const dom = new JSDOM(html);
const doc = dom.window.document;
const out = { html: args.html, html_sha256: sha(Buffer.from(html, 'utf8')), html_bytes: Buffer.byteLength(html), checks: {} };
function check(id, pass, detail) { out.checks[id] = { pass, ...detail }; }

// Text of an element with formulae, marks and hidden-label spans removed; whitespace dropped.
function bareText(el) {
  const copy = el.cloneNode(true);
  copy.querySelectorAll('math, svg').forEach(n => n.replaceWith(' '));
  return copy.textContent.replace(/\s+/g, '');
}
// The plain (non-TeX) chunks of a rich-text field, as the reader must see them.
function plainChunks(text, linked = true) {
  const t = linked ? unlink(text) : (text || '');
  return t.split(MATH_RE).filter((x, i) => i % 3 === 0 && x !== undefined)
    .map(x => x.replace(/\*/g, '').replace(/\s+/g, '')).filter(x => x.length > 0);
}
function texSegments(text) {
  const out = [];
  for (const m of (text || '').matchAll(MATH_RE)) out.push((m[1] !== undefined ? m[1] : m[2]).trim());
  return out;
}
const missingText = [];
function expectText(field, text, el, where, linked = true) {
  if (!text || !String(text).trim()) return;
  if (!el) { missingText.push({ where, field, problem: 'container missing' }); return; }
  const hay = bareText(el).replace(/\*/g, '');
  for (const chunk of plainChunks(text, linked)) {
    if (!hay.includes(chunk)) { missingText.push({ where, field, chunk: chunk.slice(0, 120) }); }
  }
}

// Q02 reader inputs
const base = args.baseline_manifest ? JSON.parse(fs.readFileSync(args.baseline_manifest, 'utf8')) : null;
out.inputs = { content_sha256: sha(contentRaw), essay_sha256: sha(essayRaw) };
if (base) {
  const want = Object.fromEntries(base.files.map(f => [f.path, f.sha256]));
  const ok = want['content/quantum-holography-status/content.json'] === out.inputs.content_sha256 &&
             want['content/quantum-holography-status/essay.md'] === out.inputs.essay_sha256;
  check('Q02', ok, { inputs: out.inputs });
}

// Q03 CSP string
const CSP = "default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; font-src data:; img-src data:; base-uri 'none'; form-action 'none'";
const cspMeta = doc.querySelector('meta[http-equiv="Content-Security-Policy"]');
check('Q03-csp', !!cspMeta && cspMeta.getAttribute('content') === CSP, { csp: cspMeta && cspMeta.getAttribute('content') });

// Q06 status fidelity and Q10 statement text completeness
const sts = [...allStatements(c)];
const arts = [...doc.querySelectorAll('main article.statement')];
// Each content statement is paired with its article by its anchor when it has an id (the page may order statements
// differently from the content: a question's own statement, folded related statements); statements without an id take
// the articles without an anchor, in order (A8-F-01).
const artById = new Map(arts.filter(a => a.id).map(a => [a.id, a]));
const anchorlessArts = arts.filter(a => !a.id);
let nextAnchorless = 0;
const pairedArts = sts.map(s => (s.id ? artById.get('s-' + ident(s.id)) : anchorlessArts[nextAnchorless++]) || null);
const statusProblems = [];
const counts = Object.fromEntries(STATEMENT_STATUSES.map(s => [s, 0]));
sts.forEach((s, i) => {
  const a = pairedArts[i];
  const st = STATEMENT_STATUSES.includes(s.status) ? s.status : null;
  if (st) counts[st]++;
  if (!a) { statusProblems.push({ i, problem: 'no article' }); return; }
  if (!st) statusProblems.push({ i, id: s.id, problem: `unknown content status ${s.status}` });
  // The status is rendered as written, never coerced to another (an unknown one fails the build).
  if (a.getAttribute('data-status') !== String(s.status)) statusProblems.push({ i, id: s.id, problem: `data-status ${a.getAttribute('data-status')} != ${s.status}` });
  const chip = a.querySelector('.statement-head .status-chip');
  if (st && (!chip || chip.textContent.trim() !== label(st))) statusProblems.push({ i, id: s.id, problem: `chip "${chip && chip.textContent.trim()}"` });
  if (st && !a.classList.contains('st-' + st.replace(/ /g, '-'))) statusProblems.push({ i, id: s.id, problem: `class ${a.className}` });
  // Hypotheses: every one rendered, in order, under the statement's text.
  const hyps = Array.isArray(s.hypotheses) ? s.hypotheses.filter(h => String(h).trim()) : [];
  const lis = [...a.querySelectorAll(':scope > .statement-hypotheses li, :scope > .statement-hyp li')];  // either markup (A8-F-01)
  if (lis.length !== hyps.length) statusProblems.push({ i, id: s.id, problem: `hypotheses ${lis.length} rendered of ${hyps.length}` });
  hyps.forEach((h, k) => expectText('hypothesis', h, lis[k], `statement ${i} ${s.id || ''} hypothesis ${k}`));
  if (s.id && a.id !== 's-' + ident(s.id)) statusProblems.push({ i, id: s.id, problem: `anchor ${a.id} != s-${ident(s.id)}` });
  if (!s.id && a.id) statusProblems.push({ i, problem: `unexpected id ${a.id}` });
  expectText('text', s.text, a.querySelector('.statement-text'), `statement ${i} ${s.id || ''}`);
  const titleEl = a.querySelector('.statement-title');
  if (s.title && titleEl) expectText('title', s.title, titleEl, `statement ${i} ${s.id || ''}`);
  const notes = a.querySelector('.statement-notes');
  if ((s.antecedents || '').trim()) expectText('antecedents', s.antecedents, notes, `statement ${i} ${s.id || ''}`);
  if ((s.cite || '').trim()) expectText('cite', s.cite, notes, `statement ${i} ${s.id || ''}`);
  if (['checked', 'pending'].includes(s.status) && (s.novelty || '').trim()) {
    const want = page.novelty_labels[s.novelty] || s.novelty;
    if (!notes || !notes.textContent.includes(want)) missingText.push({ where: `statement ${i}`, field: 'novelty', chunk: want });
  }
});
const tally = {};
// A tally pill per status in use; where pills show counts, each equals the statements of that status.
doc.querySelectorAll('.tally a[data-filter]').forEach(a => { const n = a.querySelector('.count'); tally[a.getAttribute('data-filter')] = n ? +n.textContent : null; });
const tallyOk = STATEMENT_STATUSES.every(s => counts[s] ? (s in tally && (tally[s] === null || tally[s] === counts[s])) : !(s in tally));
// Filters and the key follow the statuses in use: one filter per status with statements, each named by its label;
// every status a statement uses is explained in the key.
const filterOf = {};
doc.querySelectorAll('.row-tools .filter[data-filter]').forEach(b => { filterOf[b.getAttribute('data-filter')] = b.textContent.trim(); });
const keyLabels = [...doc.querySelectorAll('#status .key-item dt')].map(dt => dt.textContent.trim());
const inRows = new Set((c.rows || []).flatMap(r => (r.statements || []).map(s => s.status)));
STATEMENT_STATUSES.forEach(st => {
  if (inRows.has(st) && filterOf[st] !== label(st)) statusProblems.push({ status: st, problem: `filter "${filterOf[st]}"` });
  if (!inRows.has(st) && filterOf[st] !== undefined) statusProblems.push({ status: st, problem: 'row filter for a status no example row contains' });
  if (counts[st] && !keyLabels.includes(label(st))) statusProblems.push({ status: st, problem: 'not explained in the key' });
});
check('Q06', statusProblems.length === 0 && sts.length === arts.length && tallyOk,
      { content_statements: sts.length, dom_statements: arts.length, counts, tally, problems: statusProblems.slice(0, 40), problem_count: statusProblems.length });

// Q07 grid fidelity
const gridProblems = [];
// The text form of rendered reader text: MathML read with its structure (base_sub, base^sup, (n)/(d), √x), the TeX
// annotation and invisible parts dropped, white space collapsed.
const grp = t => { t = t.trim(); return t.length <= 1 ? t : `(${t})`; };
function textForm(node) {
  if (!node) return '';
  if (node.nodeType === 3) return node.nodeValue;
  if (node.nodeType !== 1) return '';
  const name = node.localName;
  if (['annotation', 'annotation-xml', 'mphantom', 'script', 'style'].includes(name)) return '';
  if (name === 'mspace') return ' ';
  const kids = [...node.childNodes].map(textForm);
  const parts = kids.filter(k => k.trim());
  if (name === 'msub' && parts.length === 2) return `${parts[0]}_${grp(parts[1])}`;
  if (name === 'msup' && parts.length === 2) return `${parts[0]}^${grp(parts[1])}`;
  if (name === 'msubsup' && parts.length === 3) return `${parts[0]}_${grp(parts[1])}^${grp(parts[2])}`;
  if (name === 'mfrac' && parts.length === 2) return `${grp(parts[0])}/${grp(parts[1])}`;
  if (name === 'msqrt') return '√' + grp(parts.join(''));
  if (name === 'mroot' && parts.length === 2) return `${grp(parts[1])}√${grp(parts[0])}`;
  return kids.join('');
}
const spokenText = node => textForm(node).replace(/\s+/g, ' ').trim();
const colsById = Object.fromEntries((c.columns || []).map(col => [col.id, col]));
const trs = [...doc.querySelectorAll('table.grid tbody tr')];
(c.rows || []).forEach((r, i) => {
  const tr = trs[i];
  if (!tr) { gridProblems.push({ row: r.id, problem: 'no grid row' }); return; }
  const rid = 'row-' + ident(r.id || r.name);
  const link = tr.querySelector('th a');
  if (!link || link.getAttribute('href') !== '#' + rid) gridProblems.push({ row: r.id, problem: `row link ${link && link.getAttribute('href')}` });
  const tds = [...tr.querySelectorAll('td')];
  COLUMNS.forEach((cid, j) => {
    const cell = (r.cells || {})[cid];
    const td = tds[j];
    if (!cell || !td) { gridProblems.push({ row: r.id, col: cid, problem: 'missing' }); return; }
    if (td.getAttribute('data-status') !== cell.status) gridProblems.push({ row: r.id, col: cid, problem: `status ${td.getAttribute('data-status')} != ${cell.status}` });
    const btn = td.querySelector('.cell-btn');
    // The accessible name is the row name and the column name in their text forms (no TeX), then the status, C04.
    // The full name: the row's own summary (the grid header may show a short label; A4-F-05).
    const rowDet = doc.getElementById(rid);
    const rowName = spokenText((rowDet && rowDet.querySelector('summary .row-name')) || tr.querySelector('th a'));
    const colDef = doc.getElementById('col-' + cid);
    const colName = colDef ? spokenText(colDef.querySelector('dt')) : (colsById[cid] || {}).name;
    const want = `${rowName}, ${colName}: ${label(cell.status)}`;
    if (!btn || btn.getAttribute('aria-label') !== want) gridProblems.push({ row: r.id, col: cid, problem: 'aria-label', got: btn && btn.getAttribute('aria-label') });
    if (btn && btn.getAttribute('data-row') !== rid) gridProblems.push({ row: r.id, col: cid, problem: 'data-row' });
    expectText('cell note (grid)', cell.note, td.querySelector('.cell-note'), `grid ${r.id}/${cid}`);
  });
  const det = doc.getElementById(rid);
  if (!det) { gridProblems.push({ row: r.id, problem: 'no row details' }); return; }
  const marks = [...det.querySelectorAll('.row-marks svg.mark')].map(m => [...m.classList].find(k => k.startsWith('mark-')).slice(5));
  const wantMarks = COLUMNS.map(cid => (((r.cells || {})[cid] || {}).status || 'not posed').replace(/ /g, '-'));
  if (marks.join() !== wantMarks.join()) gridProblems.push({ row: r.id, problem: `row marks ${marks.join()} != ${wantMarks.join()}` });
  expectText('row summary', r.summary, det.querySelector('.row-summary'), `row ${r.id}`);
  const lines = [...det.querySelectorAll('.cell-lines .cell-line')];
  COLUMNS.forEach((cid, j) => {
    const cell = (r.cells || {})[cid];
    if (cell && cell.note) expectText('cell note (row)', cell.note, lines[j], `row ${r.id}/${cid}`);
  });
});
check('Q07', gridProblems.length === 0 && trs.length === (c.rows || []).length,
      { rows: (c.rows || []).length, grid_rows: trs.length, problems: gridProblems.slice(0, 40), problem_count: gridProblems.length,
        aria_labels_with_tex: trs.flatMap(tr => [...tr.querySelectorAll('.cell-btn')]).filter(b => /\\\(|\\\[/.test(b.getAttribute('aria-label') || '')).length });

// Other rendered fields (Q10 continued)
(c.lead || []).forEach((p, i) => expectText('lead', p, doc.querySelector('.lead'), `lead ${i}`));
(c.status_key || []).forEach((k, i) => expectText('status key', k.explanation, doc.querySelector('#status'), `key ${i}`));
(c.columns || []).forEach(col => expectText('column explanation', col.explanation, doc.getElementById('col-' + col.id), `col ${col.id}`));
for (const key of ['decisive', 'frontier']) {
  const fr = c[key] || {};
  (fr.questions || []).forEach((q, i) => {
    const qid = 'q-' + ident(q.id || q.title || String(i));
    const el = doc.getElementById(qid);
    if (!el) { missingText.push({ where: `${key} ${i}`, field: 'question', problem: `no ${qid}` }); return; }
    expectText('question title', q.title, el.querySelector('.question-head'), `${key} ${q.id}`);
    expectText('why', q.why, el.querySelector('.question-why'), `${key} ${q.id}`);
  });
  if (fr.intro) expectText('intro', fr.intro, doc.querySelector(`#${key} .section-intro`), `${key} intro`);
}
((c.failures || {}).items || []).forEach((f, i) => {
  const el = doc.getElementById('f-' + ident(f.id || String(i)));
  const claim = (f.claim || '').replace(/^\s*false\s*[:.]\s*/i, '');
  // the page capitalises the first letter of the claim
  expectText('claim', claim.slice(1), el && el.querySelector('.claim-text'), `failure ${f.id}`);
});
(c.open || []).forEach((g, i) => {
  const el = doc.getElementById('open-' + ident(g.id || g.heading || String(i)));
  expectText('open heading', g.heading, el && el.querySelector('h3'), `open ${i}`);
  if (g.intro) expectText('open intro', g.intro, el && el.querySelector('.group-intro'), `open ${i}`);
});
const glossByTerm = new Map();
(c.glossary || []).forEach(g => {
  const el = [...doc.querySelectorAll('.glossary .gloss')].find(x => bareText(x.querySelector('dt')) === plainChunks(g.term).join('') || x.id === 'term-' + ident(g.term));
  glossByTerm.set(g.term, el);
  expectText('glossary definition', g.definition, el && el.querySelector('dd'), `term ${g.term}`);
});
if (c.essay_lead) expectText('essay lead', c.essay_lead, doc.querySelector('.essay-lead'), 'essay lead');
check('Q10', missingText.length === 0, { missing: missingText.slice(0, 60), missing_count: missingText.length });

// Q11 completeness of the whole payload: every reader text anywhere in content.json appears in the page, so a field
// the renderer does not know (a new key) is reported rather than silently dropped. Keys that are not reader text are
// skipped: ids and links to other data, statuses, private sources, dates, glossary surface forms, data-file metadata.
const NON_READER = new Set(['id', 'status', 'source', 'atlasClaimId', 'ref', 'as_of', 'as_of_utc', 'since', 'forms',
                            'novelty', 'added', 'schema', 'asOf', 'path', 'kind']);
const pageText = bareText(doc.body).replace(/\*/g, '');
const pageTextLower = pageText.toLowerCase();
const unrendered = [];
(function walk(node, path) {
  if (typeof node === 'string') {
    // A counterexample's claim is shown without its 'False:' prefix and with a capital first letter.
    const claim = /\.claim$/.test(path);
    const text = claim ? node.replace(/^\s*false\s*[:.]\s*/i, '') : node;
    const lost = plainChunks(text).find(chunk => claim ? !pageTextLower.includes(chunk.toLowerCase()) : !pageText.includes(chunk));
    if (lost) unrendered.push({ path, chunk: lost.slice(0, 80) });
    return;
  }
  if (Array.isArray(node)) { node.forEach((v, i) => walk(v, `${path}[${i}]`)); return; }
  if (node && typeof node === 'object') {
    for (const [k, v] of Object.entries(node)) if (!NON_READER.has(k) && !/Ids?$/.test(k)) walk(v, path ? `${path}.${k}` : k);
  }
})(c, '');
const bySection = {};
unrendered.forEach(u => { const k = u.path.replace(/\[\d+\]/g, '[]'); bySection[k] = (bySection[k] || 0) + 1; });
check('Q11-complete-payload', unrendered.length === 0,
      { unrendered_count: unrendered.length, by_field: bySection, sample: unrendered.slice(0, 16) });

// Q08 mathematics fidelity: every TeX segment of rendered fields appears as an annotation, and nothing else does.
function collectTex(node, keyName, acc) {
  if (typeof node === 'string') { if (keyName !== 'source' && keyName !== 'id' && keyName !== 'ref') texSegments(node).forEach(t => acc.add(t)); return; }
  if (Array.isArray(node)) { node.forEach(x => collectTex(x, keyName, acc)); return; }
  if (node && typeof node === 'object') for (const [k, v] of Object.entries(node)) collectTex(v, k, acc);
}
const contentTex = new Set();
collectTex(c, '', contentTex);
// The essay is reader text too: its TeX must be set as mathematics (gap found by A2; added to Q08).
texSegments(essayRaw.toString('utf8')).forEach(t => contentTex.add(t));
const anns = [...doc.querySelectorAll('math annotation[encoding="application/x-tex"]')].map(a => a.textContent.trim());
const annSet = new Set(anns);
const texNotRendered = [...contentTex].filter(t => !annSet.has(t));
// TeX of the atlas data supplied with the content (atlas.json beside content.json) is rendered by the atlas module: its
// formulas are allowed annotations (their completeness is the atlas checks' business) (A8-F-01).
const atlasTex = new Set();
if (fs.existsSync(`${contentDir}/atlas.json`)) collectTex(JSON.parse(fs.readFileSync(`${contentDir}/atlas.json`, 'utf8')), '', atlasTex);
const annNotInContent = [...annSet].filter(t => !contentTex.has(t) && !atlasTex.has(t));
const mathCount = doc.querySelectorAll('math').length;
const texErrors = doc.querySelectorAll('code.tex-error').length;
// Every formula carries its TeX annotation, except inside a grid row link, where the producer drops it so that the
// link's name holds no TeX (A8-F-01).
const bareMath = [...doc.querySelectorAll('math')].filter(m => !m.querySelector('annotation[encoding="application/x-tex"]'));
const bareOutsideRowLinks = bareMath.filter(m => !m.closest('a.row-link'));
check('Q08', texErrors === 0 && texNotRendered.length === 0 && annNotInContent.length === 0 && bareOutsideRowLinks.length === 0,
      { math_elements: mathCount, annotations: anns.length, distinct_content_tex: contentTex.size, atlas_tex: atlasTex.size,
        tex_errors: texErrors, content_tex_not_rendered: texNotRendered.slice(0, 20), content_tex_not_rendered_count: texNotRendered.length,
        annotations_not_in_content: annNotInContent.slice(0, 20), math_without_annotation: bareMath.length,
        math_without_annotation_outside_row_links: bareOutsideRowLinks.length });

// Q08 (continued): no raw TeX delimiters in reader-visible text, formulas removed.
const vis = doc.body.cloneNode(true);
vis.querySelectorAll('script, style, math').forEach(n => n.replaceWith(' '));
const rawTex = [...vis.textContent.matchAll(/\\[()\[\]]/g)].map(m => vis.textContent.slice(Math.max(0, m.index - 40), m.index + 40).replace(/\s+/g, ' '));
check('Q08-raw-tex', rawTex.length === 0, { count: rawTex.length, sample: rawTex.slice(0, 6) });
// Q15 (static part): accessible names and titles carry no TeX source.
const texNames = [...doc.querySelectorAll('[aria-label], [title]')].flatMap(el => ['aria-label', 'title'].map(a => el.getAttribute(a)).filter(v => v && /\\[A-Za-z()\[\]{}]/.test(v)));
check('Q15-tex-in-names', texNames.length === 0, { count: texNames.length, sample: texNames.slice(0, 4) });

// Q09 anchors
const ids = [...doc.querySelectorAll('[id]')].map(e => e.id);
const idCount = ids.reduce((m, x) => (m[x] = (m[x] || 0) + 1, m), {});
const dups = Object.keys(idCount).filter(k => idCount[k] > 1);
const expected = new Set(['main', 'card', 'programme', 'status', 'results', 'examples', 'open']);
if ((c.decisive || {}).questions) expected.add('decisive');
if ((c.frontier || {}).questions) expected.add('frontier');
if (((c.failures || {}).items || []).length) expected.add('failures');
if ((c.glossary || []).length) expected.add('terms');
if (((c.changes || {}).items || []).length) expected.add('changes');
sts.forEach(s => { if (s.id) expected.add('s-' + ident(s.id)); });
(c.rows || []).forEach(r => expected.add('row-' + ident(r.id || r.name)));
['decisive', 'frontier'].forEach(k => ((c[k] || {}).questions || []).forEach((q, i) => expected.add('q-' + ident(q.id || q.title || String(i)))));
((c.failures || {}).items || []).forEach((f, i) => expected.add('f-' + ident(f.id || String(i))));
(c.open || []).forEach((g, i) => expected.add('open-' + ident(g.id || g.heading || String(i))));
(c.columns || []).forEach(col => expected.add('col-' + col.id));
const idSet = new Set(ids);
const missingAnchors = [...expected].filter(x => !idSet.has(x));
const hrefs = [...doc.querySelectorAll('a[href^="#"]')].map(a => a.getAttribute('href').slice(1)).filter(Boolean);
const broken = [...new Set(hrefs.filter(h => !idSet.has(h)))];
const idCollisions = [];
const seenStmt = new Map();
sts.forEach(s => { if (s.id) { const a = ident(s.id); if (seenStmt.has(a) && seenStmt.get(a) !== s.id) idCollisions.push([seenStmt.get(a), s.id]); seenStmt.set(a, s.id); } });
let baselineLost = null;
if (args['baseline-html']) {
  const bdoc = new JSDOM(fs.readFileSync(args['baseline-html'], 'utf8')).window.document;
  const bids = new Set([...bdoc.querySelectorAll('[id]')].map(e => e.id));
  baselineLost = [...bids].filter(x => !idSet.has(x));
}
check('Q09', dups.length === 0 && missingAnchors.length === 0 && broken.length === 0 && idCollisions.length === 0 && (!baselineLost || baselineLost.length === 0),
      { ids: ids.length, expected: expected.size, duplicates: dups, missing: missingAnchors.slice(0, 30), broken_hrefs: broken.slice(0, 30),
        statement_id_collisions: idCollisions, baseline_ids_lost: baselineLost && baselineLost.slice(0, 40), baseline_ids_lost_count: baselineLost && baselineLost.length,
        statements_without_anchor: sts.filter(s => !s.id).length });

// Q04 public safety over the whole document (data: URIs removed), and Q05 external gate on visible text.
const noData = html.replace(/data:[a-z]+\/[a-z0-9.+-]+(;[a-z0-9=-]+)*,[^"')\s]*/gi, 'data:');
const sourceFragments = new Set();
(function collectSources(node, keyName) {
  if (typeof node === 'string') {
    if (keyName === 'source') node.split(/[\s,;§()]+/).forEach(tok => { tok = tok.replace(/[.:]+$/, ''); if (tok.length >= 6 && (/\//.test(tok) || /\.(md|tex|json|py|lean|v|txt|log|tsv|csv)$/i.test(tok) || /^[A-Z]{1,8}\d*-[A-Z]*\d+/.test(tok))) sourceFragments.add(tok); });
    return;
  }
  if (Array.isArray(node)) { node.forEach(x => collectSources(x, keyName)); return; }
  if (node && typeof node === 'object') for (const [k, v] of Object.entries(node)) collectSources(v, k);
})(c, '');
const readerFieldText = [];
(function collectReader(node, keyName) {
  if (typeof node === 'string') { if (keyName !== 'source') readerFieldText.push(node); return; }
  if (Array.isArray(node)) { node.forEach(x => collectReader(x, keyName)); return; }
  if (node && typeof node === 'object') for (const [k, v] of Object.entries(node)) collectReader(v, k);
})(c, '');
const readerJoined = readerFieldText.join('\u0001') + fs.readFileSync(args.page || `${contentDir}/page.json`, 'utf8') + essayRaw.toString('utf8');
// A fragment that the reader fields themselves contain is reader text, not a leak.
const sourceHits = [...sourceFragments].filter(f => noData.includes(f) && !readerJoined.includes(f));
const body = doc.body.cloneNode(true);
body.querySelectorAll('script, style, math').forEach(n => n.replaceWith(' '));
const visible = body.textContent.replace(/\s+/g, ' ');
const attrVals = [];
doc.querySelectorAll('*').forEach(el => { for (const at of el.attributes) if (!/^(style|d|viewBox|class|xmlns.*|src|href|id|data-status|data-filter|data-row|data-col|data-term|aria-controls|aria-describedby|aria-labelledby|width|height|cx|cy|r|x|y|rx|fill|stroke.*|transform|points|encoding|display|mathvariant|stretchy|.*space|lspace|rspace|linethickness|scriptlevel|columnalign|rowspacing|columnspacing|form|accent.*|largeop|movablelimits|symmetric|fence|separator|minsize|maxsize|height|depth|voffset|tabindex|type|role|datetime|charset|content|name|property|rel|lang|http-equiv|hidden|focusable|aria-hidden|aria-haspopup|aria-expanded|aria-pressed|aria-modal|data-expand|data-hit|data-scope|data-status-facet|data-find.*)$/.test(at.name)) attrVals.push(`${at.name}=${at.value}`); });
const metaVals = [...doc.querySelectorAll('head meta[content], head title')].map(m => m.getAttribute('content') || m.textContent);
const readerStrings = visible + ' \u0001 ' + attrVals.join(' \u0001 ') + ' \u0001 ' + metaVals.join(' \u0001 ');
const mathTex = [...doc.querySelectorAll('math annotation')].map(a => a.textContent).join(' \u0001 ');
const CLOSED = /~\/(kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|\/Users\/[^/ ]+\/(kernel|centcom|moxie|moxie-whitepaper|momentum|momentum-dev|momentum-docs|mass-webapp|mass-bom|api-gateway|attestation-engine|templating-engine|starters|organization-info|investment-info|treasury-info|identity-info|consent-info|governance-info|institutional-world-model-whitepaper|programmable-institutions-whitepaper|mass-whitepaper|ecosystem)|kernel\/formal|kernel\/docs|kernel\/mez|kernel\/\.claude|centcom\//g;
const scans = {
  closed_source_paths_whole_doc: [...noData.matchAll(CLOSED)].map(m => m[0]),
  private_paths_whole_doc: [...noData.matchAll(/\/Users\/|~\/[A-Za-z]|file:\/\//g)].map(m => noData.slice(Math.max(0, m.index - 40), m.index + 60)),
  internal_path_words_whole_doc: [...noData.matchAll(/\b(engine|frontier|prep|chains|attack-heal|campaign|push|wave-\d+|briefs)\/[\w./-]+/gi)].map(m => m[0]).slice(0, 20),
  hex_hashes_whole_doc: [...noData.matchAll(/(?<![\w-])[0-9a-f]{32,}(?![\w-])/gi)].map(m => m[0]).slice(0, 20),
  model_tool_names_reader: [...readerStrings.matchAll(/\b(astra|claude|codex|opus|fable|gpt-?\d*|chatgpt|openai|anthropic|sonnet|haiku|llm|gemini|copilot)\b/gi)].map(m => readerStrings.slice(Math.max(0, m.index - 50), m.index + 50)),
  hard_patterns_in_tex: [...mathTex.matchAll(/\/Users\/|~\/|\b(astra|claude|codex|opus|fable|chatgpt|openai|anthropic)\b|(?<![\w-])[0-9a-f]{32,}(?![\w-])|\.(md|json|py)\b/gi)].map(m => mathTex.slice(Math.max(0, m.index - 40), m.index + 40)),
  model_tool_names_script: [...html.replace(/data:[^"')\s]+/g, '').matchAll(/<script[^>]*>[\s\S]*?<\/script>/g)].flatMap(m => [...m[0].matchAll(/\b(astra|claude|codex|opus|fable|gpt-?\d+|chatgpt|openai|anthropic)\b/gi)].map(x => x[0])),
  process_words_reader: [...readerStrings.matchAll(/\b(draft|drafts|wave \d+|waves|phase [A-Z]?\d|sprint|session|worktree|commit|git branch|pipeline|ledger|audit|attack|heal(ing)?|agent|prompt|adopted|adoption|census|frontier engine|campaign|this edition|in progress|progress)\b/gi)].map(m => readerStrings.slice(Math.max(0, m.index - 60), m.index + 60)),
  version_tokens_reader: [...readerStrings.matchAll(/\b(v\d+(\.\d+)*|version\s+\d|revision\s+\d|rev\s*\d)\b/gi)].map(m => readerStrings.slice(Math.max(0, m.index - 50), m.index + 50)),
  percentages_reader: [...readerStrings.matchAll(/\d+(\.\d+)?\s?(%|per ?cent)/gi)].map(m => readerStrings.slice(Math.max(0, m.index - 60), m.index + 40)),
  external_gate_visible: [...visible.matchAll(/\b(v[0-9]+|version\s+[0-9]|prior\s+draft|previous\s+(draft|version)|superseded|post-(M|W|L|R|Z)[0-9]|phase\s+L[0-9]|to\s+our\s+knowledge|we\s+believe|essentially|basically)\b/gi)].map(m => visible.slice(Math.max(0, m.index - 60), m.index + 60)),
  source_fragments_checked: sourceFragments.size,
  source_fragment_hits: sourceHits.slice(0, 20)
};
const hardHits = scans.closed_source_paths_whole_doc.length + scans.private_paths_whole_doc.length + scans.internal_path_words_whole_doc.length +
  scans.hex_hashes_whole_doc.length + scans.model_tool_names_reader.length + scans.model_tool_names_script.length + scans.hard_patterns_in_tex.length + sourceHits.length;
check('Q04', hardHits === 0, { hard_hits: hardHits, review_hits: scans.process_words_reader.length + scans.version_tokens_reader.length + scans.percentages_reader.length, scans });
check('Q05', scans.external_gate_visible.length === 0 && scans.closed_source_paths_whole_doc.length === 0, { hits: scans.external_gate_visible });

out.summary = Object.fromEntries(Object.entries(out.checks).map(([k, v]) => [k, v.pass ? 'PASS' : 'FAIL']));
if (args.out) fs.writeFileSync(args.out, JSON.stringify(out, null, 1) + '\n');
console.log(JSON.stringify(out.summary));
for (const [k, v] of Object.entries(out.checks)) if (!v.pass) console.log(k, JSON.stringify(v).slice(0, 1500));
