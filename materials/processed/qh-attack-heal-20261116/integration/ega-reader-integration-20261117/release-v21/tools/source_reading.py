"""Read the edition's editable text with its own Markdown grammar."""
from html import escape
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import SimpleNamespace
import json
import re
import sys


class SourceMath:
    def add(self, tex, display):
        attr = ' display="block"' if display else ''
        return (f'<math{attr}><semantics><mrow></mrow>'
                f'<annotation encoding="application/x-tex">{escape(tex)}</annotation></semantics></math>')


def reading(manifest):
    source = manifest.resolve().parents[3]
    spec = spec_from_file_location('qh_monograph', source / 'compiler/quantum-holography-status/monograph.py')
    parser = module_from_spec(spec)
    spec.loader.exec_module(parser)
    book = parser.Book(SimpleNamespace(math=SourceMath()), manifest, lambda _: '')
    book.pending_refs = []
    book.load()
    intro = book.m['introduction']
    if intro.endswith('.md') and (manifest.parent / intro).is_file():
        intro = (manifest.parent / intro).read_text()
    blocks = parser.parse_blocks(re.sub(r'<!--.*?-->', '', intro, flags=re.S).splitlines())
    book.current = 'front'
    reference = book.render(blocks, envs=False)
    chapters = []
    for row in book.chapters:
        chapter = row['id']
        path = manifest.parent / row['path']
        first_line = next((s.strip() for s in book.texts[chapter].splitlines() if s.strip()), '')
        title = re.sub(r'^#\s+(?:\d+\.\s*)?', '', first_line)
        if title != row['title']:
            raise ValueError(f'{chapter}: chapter source title {title!r} differs from the published title {row["title"]!r}')
        opening, _ = book.split_sections(book.blocks[chapter])
        book.current = chapter
        first = next((block for block in opening if block['t'] == 'p'), None)
        chapters.append({'id': chapter, 'title': title, 'first_html': book.para(first) if first else None,
                         'has_math': any(b['t'] == 'math' or parser.INLINE_MATH.search(b.get('text', ''))
                                         for b in book.walk(book.blocks[chapter]))})
    return {'title': book.m['title'], 'subtitle': book.m.get('subtitle', ''), 'introduction': intro,
            'reference': reference, 'front_figures': book.m.get('front_figures', []), 'chapters': chapters}


if __name__ == '__main__':
    print(json.dumps(reading(Path(sys.argv[1])), ensure_ascii=False))
