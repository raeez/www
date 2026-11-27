"""Every authored diagram record drawn through the page's own context (Temml, marks, interface words), whether or not
its chapter places it yet. Reports problems, TeX errors and definition targets missing from a built book, and writes a
gallery page of all the drawings with the page's sheets.
    <python with fontTools> check_diagrams.py <producer folder> <content folder> <manifest.json> <book.html> <out.json> <gallery.html>"""
import hashlib, html, json, re, subprocess, sys
from pathlib import Path
prod, content, manifest, book_html, out, gallery = map(Path, sys.argv[1:7])
sys.path.insert(0, str(prod)); sys.dont_write_bytecode = True
import status, monograph
page = json.loads((content / 'page.json').read_text(encoding='utf-8'))
def find(name):
    r = subprocess.run(['kpsewhich', name], capture_output=True, text=True).stdout.strip()
    return Path(r) if r else None
fonts = {k: find(v) for k, v in {('QH Garamond', 400, 'normal'): 'EBGaramond-Regular.otf', ('QH Garamond', 400, 'italic'): 'EBGaramond-Italic.otf',
                                  ('QH Garamond', 600, 'normal'): 'EBGaramond-SemiBold.otf'}.items()}
b = status.Build(content, page, {k: v for k, v in fonts.items() if v}, find('Garamond-Math.otf'))
b.content = json.loads((content / 'content.json').read_text(encoding='utf-8'))
b.term_links = status.Terms([])
bk = monograph.Book(b, manifest, status.mark, page.get('reader') or {})
bk.pending_refs, bk.pending_defs, bk.section_index = [], [], {}
book_ids = set(re.findall(r'\sid="([^"]+)"', book_html.read_text(encoding='utf-8')))
placed = set(re.findall(r'<figure class="mg-diagram" id="([^"]+)"', book_html.read_text(encoding='utf-8')))
rows, parts = [], []
for rec in bk.m.get('diagrams', []):
    bk.current = rec['chapter_id']; n0 = len(bk.problems)
    html_ = monograph.Diagram(bk, rec).render()
    targets = [(n.get('definition_ref') or {}).get('section_id') for n in rec['nodes'] if isinstance(n.get('definition_ref'), dict)]
    rows.append({'id': rec['id'], 'chapter': rec['chapter_id'], 'placed_in_book': rec['id'] in placed, 'nodes': len(rec['nodes']),
                 'edges': len(rec['edges']), 'kinds': sorted({e['kind'] for e in rec['edges']}),
                 'undirected_edges': [e['id'] for e in rec['edges'] if e.get('direction') == 'undirected'],
                 'record_fields_shown': [k for k in ('legend', 'hypotheses', 'relations', 'equations', 'formulas', 'prohibitions', 'witness', 'status') if k in rec],
                 'rendered': bool(html_), 'problems': bk.problems[n0:],
                 'definition_targets_missing_from_book': sorted({t for t in targets if t and t not in book_ids})})
    parts.append(f'<section class="mg-gallery-item"><p class="mg-gallery-where">{html.escape(rec["id"])} · {html.escape(rec["chapter_id"])} · '
                 f'{html.escape(rec.get("section_id", ""))}</p><div class="mg-figure">{html_}</div></section>')
body = '<main id="main" class="mg-gallery"><h1 class="mg-gallery-h">Diagram records as the reader draws them</h1>' + ''.join(parts) + '</main>'
body = re.sub('[\x02\x03]([^\x02\x03]*)[\x02\x03]', 'section', body)
b.math.render(); body = b.math.substitute(body)
tex = [e['error'][:120] + ' in ' + e['tex'][:60] for e in b.math.errors]
css = '\n'.join([(prod / 'status.css').read_text(encoding='utf-8'), (prod / 'monograph.css').read_text(encoding='utf-8'),
                 '.mg-gallery{max-width:calc(var(--mg-frame) + 2*var(--gutter));margin:0 auto;padding:var(--s4) var(--gutter)}'
                 '.mg-gallery-item{margin:0 0 var(--s6);padding-top:var(--s2);border-top:1px solid var(--rule)}'
                 '.mg-gallery-where{font-size:var(--text-sm);color:var(--ink-3);margin:0 0 var(--s2)}.mg-gallery-h{font-weight:400}'])
gallery.write_text('<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
                   '<meta name="robots" content="noindex"><title>Diagram records — reader rendering</title>'
                   f'<style>{b.font_faces(body)}\n{css}</style></head><body>{body}</body></html>\n', encoding='utf-8')
res = {'manifest_sha256': hashlib.sha256(manifest.read_bytes()).hexdigest(), 'book_sha256': hashlib.sha256(book_html.read_bytes()).hexdigest(),
       'gallery_sha256': hashlib.sha256(gallery.read_bytes()).hexdigest(), 'records': rows, 'tex_errors': tex,
       'total_problems': sum(len(r['problems']) for r in rows)}
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('records', len(rows), 'rendered', sum(r['rendered'] for r in rows), 'placed', sum(r['placed_in_book'] for r in rows),
      'problems', res['total_problems'], 'tex errors', len(tex), 'missing targets', sum(len(r['definition_targets_missing_from_book']) for r in rows))
