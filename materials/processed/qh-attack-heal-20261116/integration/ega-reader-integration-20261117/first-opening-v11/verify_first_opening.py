"""The first-opening packet's four HTML guards and search counts, on a built release (index.html, reader-index.js).
    python3 -I verify_first_opening.py <site folder> <OUTPUT-GUARDS.json> <SOURCE-REPLACEMENTS.json> <out.json>"""
import json, sys, re
site, guards_p, repl_p, out = sys.argv[1:5]
g = json.load(open(guards_p)); ops = {o['id']: o for o in json.load(open(repl_p))['operations']}
page = open(f'{site}/index.html', encoding='utf-8').read(); idx = open(f'{site}/reader-index.js', encoding='utf-8').read()
res = {'guards': [], 'search': {}}
for op in g['operations']:
    r = {'id': op['id'], 'old_count': page.count(op['old']), 'new_count': page.count(op['new']) if op['new'] else None}
    r['pass'] = r['old_count'] == 0 and (op['new'] == '' or r['new_count'] == 1)
    res['guards'].append(r)
res['guards'].append({'id': 'no audience element', 'count': page.count('class="mg-front-audience"'), 'pass': 'class="mg-front-audience"' not in page})
dec = lambda s: json.dumps(s, ensure_ascii=False)[1:-1]  # noqa: E731  (the index is JSON text)
old_ch1 = re.sub(r'\*\*', '', ops['OPEN-CH01']['old'])[:80]; new_ch1 = re.sub(r'\*\*', '', ops['OPEN-CH01']['new'])[:80]
old_front = ops['OPEN-FRONT']['old'].split('\n\n')[1][:80]  # the removed "This work develops ..." paragraph
res['search'] = {'old_chapter1_text': idx.count(dec(old_ch1)), 'new_chapter1_text': idx.count(dec(new_ch1)),
                 'old_audience': idx.count(dec(ops['OPEN-AUDIENCE']['old'])), 'removed_front_paragraph': idx.count(dec(old_front))}
res['search']['pass'] = res['search']['old_chapter1_text'] == 0 and res['search']['new_chapter1_text'] >= 1 and res['search']['old_audience'] == 0 and res['search']['removed_front_paragraph'] == 0
res['pass'] = all(x['pass'] for x in res['guards']) and res['search']['pass']
json.dump(res, open(out, 'w'), indent=1, ensure_ascii=False)
for x in res['guards']: print(('PASS ' if x['pass'] else 'FAIL ') + json.dumps(x))
print(('PASS ' if res['search']['pass'] else 'FAIL ') + 'search ' + json.dumps(res['search']))
print('ALL PASS' if res['pass'] else 'FAILURES ABOVE')
