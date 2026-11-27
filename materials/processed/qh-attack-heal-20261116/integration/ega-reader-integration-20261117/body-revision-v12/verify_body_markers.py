"""The body packet's 21 old-output markers on a rebuilt release: each must be gone from all four outputs, unless the
marker's words recur in that operation's new source text (then it is reported, not failed).
    python3 -I verify_body_markers.py <site folder> <OUTPUT-GUARDS.json> <SOURCE-REPLACEMENTS.json> <out.json>"""
import json, re, sys, html
site, guards_p, repl_p, out = sys.argv[1:5]
files = {f: open(f'{site}/{f}', encoding='utf-8').read() for f in ('index.html', 'reference.html', 'atlas.html', 'reader-index.js')}
ops = {o['id']: o for o in json.load(open(repl_p))['operations']}
plain = lambda s: ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', s)).split())  # noqa: E731
def new_text(o):
    if o['kind'] == 'replace-text':
        return o['new']
    return ' '.join(json.dumps(c['new'], ensure_ascii=False) for c in o['changes'])
res = []
for g in json.load(open(guards_p))['guards']:
    m = g['marker']; jm = json.dumps(m, ensure_ascii=False)[1:-1]
    counts = {f: t.count(jm if f.endswith('.js') else m) for f, t in files.items()}
    recur = plain(m).replace('**', '') in ' '.join(new_text(ops[g['source_operation']]).replace('**', '').split())
    ok = sum(counts.values()) == 0 or recur
    res.append({'op': g['source_operation'], 'marker': m[:70], 'counts': counts, 'recurs_in_new_source': recur, 'pass': ok})
json.dump({'markers': res, 'pass': all(r['pass'] for r in res)}, open(out, 'w'), indent=1, ensure_ascii=False)
for r in res:
    print(('PASS ' if r['pass'] else 'FAIL ') + r['op'] + ' ' + json.dumps({k: v for k, v in r['counts'].items() if v}) + (' (recurs in new text)' if r['recurs_in_new_source'] else ''))
print('ALL PASS' if all(r['pass'] for r in res) else 'FAILURES ABOVE')
