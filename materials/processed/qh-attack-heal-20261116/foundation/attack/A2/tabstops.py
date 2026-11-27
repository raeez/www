# Static estimate of the initial tab sequence (all disclosures closed, before status.js adds the search,
# the question-section toolbars and the formula focus stops), for comparing baseline and candidate.
import re, sys
from html.parser import HTMLParser
from collections import Counter
VOID = {'meta', 'link', 'br', 'hr', 'img', 'input', 'source', 'area', 'col', 'embed', 'param', 'track', 'wbr'}
MML = {'math', 'semantics', 'mrow', 'mi', 'mo', 'mn', 'msub', 'msup', 'msubsup', 'mfrac', 'mtext', 'mspace', 'annotation', 'munder', 'mover',
       'munderover', 'msqrt', 'mroot', 'mtable', 'mtr', 'mtd', 'mpadded', 'mstyle', 'menclose', 'mphantom', 'mmultiscripts', 'mprescripts', 'none', 'ms'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.stack = []; s.stops = Counter(); s.total = 0
    def blocked(s, tag):
        # inside a closed details unless this is that details' own summary; inside [hidden]; inside a display:none class
        for i, (t, a) in enumerate(s.stack):
            cls = (a.get('class') or '').split()
            if 'hidden' in a or 'statement-context' in cls: return True
            if t == 'details' and 'open' not in a:
                # allowed only if we are its direct summary
                if not (tag == 'summary' and i == len(s.stack) - 1): return True
        return False
    def handle_starttag(s, tag, attrs):
        a = dict(attrs)
        if tag in MML:
            if tag not in VOID: s.stack.append((tag, a))
            return
        focusable = (tag == 'a' and 'href' in a) or tag in ('button', 'input', 'summary') or ('tabindex' in a and a['tabindex'] != '-1')
        if focusable and a.get('tabindex') != '-1' and 'disabled' not in a and not s.blocked(tag):
            cls = (a.get('class') or '').split()
            kind = next((k for k in ('term', 'cell-btn', 'col-head', 'fold-head', 'row-link', 'filter', 'link-btn', 'anchor', 'find-open', 'theme', 'grid-wrap') if k in cls), tag)
            s.stops[kind] += 1; s.total += 1
        if tag not in VOID: s.stack.append((tag, a))
    def handle_endtag(s, tag):
        if tag in VOID: return
        for k in range(len(s.stack) - 1, -1, -1):
            if s.stack[k][0] == tag: del s.stack[k:]; break
for name in sys.argv[1:]:
    h = open(name, encoding='utf-8').read(); p = P(); p.feed(h[h.find('<body'):h.rfind('<script>')])
    print(name.split('/foundation/')[-1], 'static tab stops:', p.total, dict(p.stops.most_common()))
