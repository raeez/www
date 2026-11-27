"""Like-for-like: the page built from integration's installed files against the page built with the v8 repair.
    python3 compare.py <baseline page> <repaired page>"""
import difflib
import re
import sys


def read(p):
    return open(p, encoding='utf-8').read()


def atlas(page):
    m = re.search(r'<section\b[^>]*\sid="atlas"[^>]*>', page)
    a, depth = m.start(), 0
    for t in re.finditer(r'<(/?)section\b[^>]*>', page[a:]):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return page[a:a + t.end()]
    return page[a:]


def visible(fragment):
    fragment = re.sub(r'<(template|script|style|svg|math)\b.*?</\1>', ' ', fragment, flags=re.S)
    return re.sub(r'<[^>]+>', ' ', fragment).split()


def main(b_path, r_path):
    b, r = read(b_path), read(r_path)
    ids = lambda s: re.findall(r'\sid="([^"]+)"', s)
    ib, ir = ids(b), ids(r)
    print(f'ids on the page: baseline {len(ib)}, repaired {len(ir)}; lost {sorted(set(ib) - set(ir))[:6]}, '
          f'new {sorted(set(ir) - set(ib))[:6]}; duplicates in the repaired page {len(ir) - len(set(ir))}')
    hooks = lambda s: tuple(len(re.findall(p, s)) for p in (r'data-status-code="[a-z_]+"', r'data-qh-unit-status="[^"]+"',
                                                         r'data-claim-id="', r'data-edge-id="', r'<a class="atlas-node '))
    print(f'atlas hooks (status-code, unit-status, claim-id, edge-id, map nodes): baseline {hooks(atlas(b))}, repaired {hooks(atlas(r))}')
    wb, wr = visible(atlas(b)), visible(atlas(r))
    d = [x for x in difflib.unified_diff(wb, wr, lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('---', '+++')]
    print(f'visible words of the atlas: baseline {len(wb)}, repaired {len(wr)}; changed {len(d)}: '
          f'removed {[x[1:] for x in d if x[0] == "-"][:12]} added {" ".join(x[1:] for x in d if x[0] == "+")[:400]!r}')
    fig = lambda s, fid: re.search(rf'<figure class="qh-fig" id="{fid}".*?</figure>', s, re.S).group(0)
    for fid in ('fig-gaussian-reduction', 'fig-local-expansions', 'fig-cohomology-jump', 'fig-infinite-rank', 'fig-adjunction-triangles'):
        try:
            same = fig(b, fid) == fig(r, fid)
        except AttributeError:
            same = None
        print(f'figure {fid}: {"unchanged" if same else "changed" if same is False else "missing"}')
    rest_b = re.sub(r'<figure class="qh-fig" id="fig-gaussian-reduction".*?</figure>', '', b.replace(atlas(b), ''), flags=re.S)
    rest_r = re.sub(r'<figure class="qh-fig" id="fig-gaussian-reduction".*?</figure>', '', r.replace(atlas(r), ''), flags=re.S)
    strip_assets = lambda s: re.sub(r'<(style|script)\b[^>]*>.*?</\1>', '', s, flags=re.S)
    print('the rest of the page (outside the atlas and the Gaussian figure, styles and scripts aside):',
          'identical' if strip_assets(rest_b) == strip_assets(rest_r) else 'DIFFERS')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
