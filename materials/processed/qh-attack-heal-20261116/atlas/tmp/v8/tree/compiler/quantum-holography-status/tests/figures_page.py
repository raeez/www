"""A preview page of figure records, for the reader tests and for native visual QA (not a product page).

    python3 figures_page.py <records.json or manifest.json> <out.html> [<compiler dir with status.py>]

With a compiler dir, the text and TeX of every record go through that tree's renderer (Build.rich, then the
MathML substitution) and its stylesheet supplies the page's tokens; without one, TeX is left as written."""
import html
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import figures as F  # noqa: E402


def main(argv):
    records = json.loads(Path(argv[1]).read_text(encoding='utf-8')).get('figures') or []
    out = Path(argv[2])
    css, ctx, finish = '', None, (lambda s: s)
    if len(argv) > 3:
        tree = Path(argv[3]).resolve()
        sys.path.insert(0, str(tree))
        import status  # noqa: E402
        page = json.loads((tree.parent.parent / 'content' / 'quantum-holography-status' / 'page.json').read_text(encoding='utf-8'))
        build = status.Build(tree.parent.parent / 'content' / 'quantum-holography-status', page, {}, None)

        class Ctx:
            def rich(self, text, terms=False):
                return build.rich(text, terms=False)
        ctx = Ctx()
        css = (tree / 'status.css').read_text(encoding='utf-8')

        def finish(s):
            build.math.render()
            return build.math.substitute(s)
    else:
        class Ctx:
            def rich(self, text, terms=False):
                return html.escape(text, quote=False)
        ctx = Ctx()
    parts, problems = [], []
    for r in records:
        if r.get('model') not in F.MODELS:
            continue
        o = F.render(r, ctx)
        problems += o['problems']
        parts.append(o['html'])
    a = F.assets()
    body = finish('\n'.join(parts))
    out.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                   f'<title>Figure preview</title><style>{css}\n{a["css"]}\nmain{{max-width:72rem;margin:0 auto;padding:16px}}</style></head>'
                   f'<body><main>{body}</main><script>{a["js"]}</script></body></html>', encoding='utf-8')
    print(f'{len(parts)} figures; problems: {problems}')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
