"""Static checks of the candidate page (no browser): html.parser tree, read-only."""
import sys, re, json, html as H
from html.parser import HTMLParser
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','source','track','wbr'}
class N:
    __slots__ = ('tag','a','kids','up')
    def __init__(s, tag, a, up): s.tag, s.a, s.kids, s.up = tag, dict(a), [], up
    def cls(s): return s.a.get('class','').split()
    def walk(s):
        yield s
        for k in s.kids:
            if isinstance(k, N): yield from k.walk()
    def text(s, skip=lambda n: False):
        out=[]
        def r(n):
            for k in n.kids:
                if isinstance(k,str): out.append(k)
                elif k.tag in ('svg','script','style','annotation') or skip(k): continue
                else: r(k)
        r(s); return re.sub(r'\s+',' ',''.join(out)).strip()
    def find(s, pred): return [n for n in s.walk() if pred(n)]
    def anc(s, pred):
        p = s.up
        while p is not None:
            if pred(p): return p
            p = p.up
        return None
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.root = N('#',{},None); s.cur = s.root
    def handle_starttag(s, t, a):
        n = N(t,a,s.cur); s.cur.kids.append(n)
        if t not in VOID: s.cur = n
    def handle_startendtag(s, t, a): s.cur.kids.append(N(t,a,s.cur))
    def handle_endtag(s, t):
        p = s.cur
        while p is not None and p.tag != t: p = p.up
        if p is not None and p.up is not None: s.cur = p.up
    def handle_data(s, d): s.cur.kids.append(d)
def parse(path):
    raw = open(path, encoding='utf-8').read()
    raw = re.sub(r'<script\b.*?</script>', '', raw, flags=re.S); raw = re.sub(r'<style\b.*?</style>', '', raw, flags=re.S)
    p = P(); p.feed(raw); return p.root
C = lambda c: (lambda n: c in n.cls())
root = parse(sys.argv[1])
ids = {n.a['id']: n for n in root.walk() if 'id' in n.a}
out = {}
# 1. contents
cont = root.find(lambda n: n.tag == 'nav' and 'contents' in n.cls())[0]
items = []
for a in cont.find(lambda n: n.tag == 'a'):
    href = a.a['href']; tgt = ids.get(href[1:])
    h2 = tgt.find(lambda n: n.tag == 'h2')[0].text() if tgt is not None and tgt.find(lambda n: n.tag=='h2') else None
    kick = tgt.find(C('kicker'))[0].text() if tgt is not None and tgt.find(C('kicker')) else None
    items.append({'href': href, 'title': a.find(C('contents-title'))[0].text(), 'holds': a.find(C('contents-holds'))[0].text(), 'target_exists': tgt is not None, 'target_h2': h2, 'target_kicker': kick})
out['contents'] = items
out['contents_label'] = cont.find(C('contents-label'))[0].text()
# order of main children
main = ids['main']
out['main_children'] = [ (k.tag, k.a.get('id') or ' '.join(k.cls())) for k in main.kids if isinstance(k, N)]
# 2. bar
nav = root.find(lambda n: n.tag=='nav' and 'nav' in n.cls())[0]
out['bar'] = [(a.a['href'], a.text()) for a in nav.find(lambda n: n.tag=='a')]
bi = root.find(C('bar-inner'))[0]
out['bar_children'] = [(k.tag, ' '.join(k.cls()), k.a.get('aria-label')) for k in bi.kids if isinstance(k, N)]
# 3. question cards
cards = []
for q in root.find(lambda n: 'question' in n.cls() and n.tag == 'div' and n.a.get('id','').startswith('q-')):
    sec = q.anc(lambda n: n.tag == 'section')['id'] if False else q.anc(lambda n: n.tag=='section').a['id']
    num = q.find(C('question-num'))[0].text()
    h3 = q.find(lambda n: n.tag=='h3')[0].text()
    ask = q.find(C('question-ask'))[0]
    asklab = [n.text() for n in ask.find(C('question-ask-label'))]
    own = [n for n in ask.kids if isinstance(n, N) and 'statement' in n.cls()]
    own = own[0] if own else None
    whylab = [n.text() for n in q.find(C('question-why-label'))]
    knownlab = [n.text() for n in q.find(C('known-label'))]
    folds = []
    for d in q.find(lambda n: n.tag=='details' and 'fold' in n.cls()):
        summ = [k for k in d.kids if isinstance(k,N) and k.tag=='summary'][0]
        art = [k for k in d.kids if isinstance(k,N) and k.tag=='article'][0]
        it = art.find(C('statement-title'))
        chip = art.find(C('status-chip'))[0].text()
        folds.append({'sum_title': summ.find(C('fold-title'))[0].text(), 'sum_status': summ.find(C('fold-status'))[0].text(),
                      'in_title': it[0].text() if it else '', 'in_chip': chip, 'id': art.a.get('id'), 'open': 'open' in d.a,
                      'ctx': [(a.a['href'], a.text()) for a in art.find(lambda n: n.tag=='a' and n.up is not None and 'statement-context' in n.up.cls())]})
    cards.append({'sec': sec, 'id': q.a['id'], 'num': num, 'h3': h3, 'ask_label': asklab, 'why_label': whylab, 'known_label': knownlab,
                  'own_id': own.a.get('id') if own else None, 'own_status': own.a.get('data-status') if own else None,
                  'own_title_shown': bool(own.find(C('statement-title'))) if own else None,
                  'own_ctx': bool(own.find(C('statement-context'))) if own else None, 'folds': folds})
out['cards'] = cards
# 4. context lines: parent check
ctx_bad = []; ctx_n = 0; ctx_by = {}
for p in root.find(C('statement-context')):
    ctx_n += 1
    a = p.find(lambda n: n.tag=='a')[0]; href = a.a['href']
    art = p.anc(lambda n: n.tag=='article')
    parent = art.anc(lambda n: n.a.get('id','').startswith(('q-','row-','open-')))
    kind = href.split('-')[0][1:]
    ctx_by[kind] = ctx_by.get(kind, 0) + 1
    if parent is None or '#' + parent.a['id'] != href: ctx_bad.append((art.a.get('id'), href, parent.a.get('id') if parent is not None else None))
out['ctx_total'] = ctx_n; out['ctx_by_kind'] = ctx_by; out['ctx_parent_mismatch'] = ctx_bad[:10]
# 5. anchored statements without context
noctx = {}
for art in root.find(lambda n: n.tag=='article' and 'statement' in n.cls()):
    if not art.a.get('id'): continue
    if art.find(C('statement-context')): continue
    place = ('question-own' if art.anc(C('question-ask')) else 'failure-witness' if art.anc(C('failure')) else
             'principal' if art.anc(lambda n: n.a.get('id')=='results') else 'other')
    noctx.setdefault(place, []).append((art.a['id'], bool(art.find(C('statement-title')))))
out['anchored_without_context'] = {k: {'n': len(v), 'title_suppressed': sum(1 for _, t in v if not t), 'sample': v[:3]} for k, v in noctx.items()}
# 6. glossary letter index
gi = root.find(C('gloss-index'))[0]
letters = [(a.text(), a.a['href']) for a in gi.find(lambda n: n.tag=='a')]
gloss = [(g.a['id'], g.find(lambda n: n.tag=='dt')[0].text()) for g in root.find(C('gloss'))]
order = [gid for gid, _ in gloss]
import unicodedata
def first_alnum(t):
    return next((ch for ch in unicodedata.normalize('NFKD', t) if ch.isalnum()), '#').upper()
letter_check = []
for L_, href in letters:
    tid = href[1:]; pos = order.index(tid); term = dict(gloss)[tid]
    firsts = [i for i, (gid, t) in enumerate(gloss) if first_alnum(t) == L_]
    letter_check.append((L_, term[:40], pos, firsts[:1] == [pos], first_alnum(term) == L_, firsts[0] if firsts else None, firsts[-1] if firsts else None))
out['letters'] = [l for l, _ in letters]
out['letter_check'] = letter_check
out['gloss_first_terms'] = [t for _, t in gloss[:6]]
out['gloss_nonalpha_initial'] = [(i, t) for i, (_, t) in enumerate(gloss) if not t[:1].isalpha()]
# 7. q-index caption and entries
out['q_index'] = [(n.find(C('q-index-label'))[0].text(), [c.text() for c in n.find(C('q-index-cap'))], len(n.find(lambda m: m.tag=='li'))) for n in root.find(C('q-index'))]
# 8. row-marks titles
rm = root.find(C('row-marks'))
out['row_marks'] = {'n': len(rm), 'with_title': sum(1 for r in rm for s in r.find(lambda n: n.tag=='svg') if s.find(lambda n: n.tag=='title') or 'title' in s.a)}
# 9. links to #status, legend
out['links_to_status'] = [ (a.anc(lambda n: n.tag in ('nav','section','div') and (n.a.get('id') or n.cls())).a.get('id') or ' '.join(a.anc(lambda n: n.tag in ('nav','section','div') and (n.a.get('id') or n.cls())).cls())) for a in root.find(lambda n: n.tag=='a' and n.a.get('href')=='#status')]
# 10. cell meanings
cm = root.find(C('cell-note-meaning'))
mt = {}
for p in cm:
    td = p.anc(lambda n: n.tag=='td'); mt.setdefault(td.a['data-status'], set()).add(p.text()[:90])
out['cell_meaning'] = {k: sorted(v) for k, v in mt.items()}
# 11. grid hint
out['grid_hint'] = root.find(C('grid-hint'))[0].text()
# 12. section heads
out['sections'] = {s.a['id']: {'kicker': (s.find(C('kicker')) or [None])[0].text() if s.find(C('kicker')) else None, 'h2': s.find(lambda n: n.tag=='h2')[0].text(), 'cls': s.a.get('class')} for s in root.find(lambda n: n.tag=='section')}
out['atlas_mount'] = len(root.find(lambda n: 'data-atlas-mount' in n.a))
out['hyp_blocks'] = len(root.find(C('statement-hyp')))
json.dump(out, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
print('ok')
