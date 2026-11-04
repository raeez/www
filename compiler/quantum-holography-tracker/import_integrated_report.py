#!/usr/bin/env python3
"""Convert a single-file integrated programme report into the tracker's input folder.

The output folder has the layout the tracker build reads:

    words/REPORT.html   the report body as an HTML fragment with MathML
    words/STATUS.md     the status of the words (a converted report is a stand-in)
    cards/TERMS.json    one card per term

The conversion moves material and never changes its words:

- equations kept in the report's compressed equation table are restored in place;
- the interactive question graph is removed, and its own data (each question's
  statement and next step, and each obstruction family) becomes the status section;
- the embedded search library and the attached PDF documents are not carried. Links
  to them stay in the text, without their targets, and the tracker build reports
  each one as a pointer that needs words.

Usage:
    python3 compiler/quantum-holography-tracker/import_integrated_report.py REPORT.html OUTPUT_DIR
"""
import argparse
import datetime as dt
import json
import lzma
import re
from pathlib import Path

from bs4 import BeautifulSoup, Tag

ALPHABET = ('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            '!#$%&()*+-;.=>?@^_`{|}~')
DIGITS = {c: i for i, c in enumerate(ALPHABET)}

# Interactive elements of the question graph. Their content is regenerated from data.
GRAPH_UI = ['.frontier-controls', '#frontier-family-description', '#frontier-selected-title',
            '#frontier-next-map', '.frontier-diagram', '#frontier-edge-list',
            'details.frontier-all-relations']


def base85(text):
    text = text.strip()
    out = bytearray()
    for start in range(0, len(text), 5):
        chunk = text[start:start + 5]
        value = 0
        for i in range(5):
            value = value * 85 + DIGITS[chunk[i] if i < len(chunk) else '~']
        for i in range(4 if len(chunk) == 5 else len(chunk) - 1):
            out.append((value >> (24 - 8 * i)) & 255)
    return bytes(out)


def script_text(html, ident):
    match = re.search(r'<script\b[^>]*\bid="%s"[^>]*>(.*?)</script>' % re.escape(ident), html, re.S)
    if not match:
        raise SystemExit(f'missing embedded data: {ident}')
    return match.group(1)


def compressed_json(html, ident):
    return json.loads(lzma.decompress(base85(script_text(html, ident)),
                                      format=lzma.FORMAT_ALONE).decode('utf-8'))


def fragment(markup):
    return BeautifulSoup(markup, 'html.parser')


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:60]


def convert(source, out):
    html = source.read_text(encoding='utf-8')
    equations = compressed_json(html, 'main-math-data')
    terms = compressed_json(html, 'term-data')
    graph = json.loads(script_text(html, 'frontier-data'))

    page = BeautifulSoup(html, 'html.parser')
    for script in page.find_all('script'):
        script.decompose()
    main = page.find('main')
    header = page.find('header')
    nav = page.find('nav')

    # Restore every stored equation in place.
    for host in main.select('[data-main-math]'):
        host.replace_with(fragment(equations[int(host['data-main-math'], 16)]))

    library = main.find('section', id='library')
    if library:
        library.decompose()
    for selector in GRAPH_UI:
        for node in main.select(selector):
            node.decompose()
    for node in main.find_all('style'):
        node.decompose()
    for node in main.select('p.statement-source'):
        if not node.get_text(strip=True):
            node.decompose()
    for node in main.select('p.part-title'):
        node['data-role'] = 'eyebrow'
        del node['class']

    # Attachments: keep the link and its words; drop the embedded file.
    attachments = 0
    for link in main.find_all('a', href=re.compile(r'^data:')):
        link['href'] = 'data:application/pdf;name=' + slug(link.get_text(' ', strip=True))
        attachments += 1

    # The original contents labels become the sections' contents labels.
    for item in nav.find_all('a', href=True):
        target = main.find(id=item['href'][1:])
        if target is None:
            continue
        label = item.get_text(' ', strip=True)
        section = target if target.name == 'section' else target.find_parent('section')
        headings = section.find_all(re.compile(r'^h[1-6]$')) if section else []
        if section is not None and headings and headings[0] is target and \
                section.parent is main:
            section['data-toc'] = label
        else:
            target['data-toc'] = label

    # The status section, from the question graph's own data.
    status = fragment('<section id="status" data-role="status"><ol data-role="board"></ol></section>')
    board = status.find('ol')

    def item(state, title, text, role=None):
        li = status.new_tag('li', attrs={'data-state': state})
        heading = status.new_tag('h3')
        heading.string = title
        li.append(heading)
        if text:
            para = status.new_tag('p')
            if role:
                para['data-role'] = role
            para.string = text
            li.append(para)
        board.append(li)

    for family in graph['families']:
        item('failing', family['title'], family['description'])
    for node in graph['nodes']:
        settled = node['next'].strip().lower().startswith('none')
        item('established' if settled else 'remains', node['title'], node['next'], 'next')

    hero = fragment('<header data-role="hero"></header>')
    top = hero.find('header')
    for cls, role in (('eyebrow', 'eyebrow'), ('lede', 'dek')):
        node = header.find('p', class_=cls)
        if node:
            para = hero.new_tag('p', attrs={'data-role': role})
            para.string = node.get_text()
            top.append(para)
    title = hero.new_tag('h1')
    title.string = header.find('h1').get_text(' ', strip=True)
    top.insert(1, title)

    body = '\n'.join(str(node) for node in main.contents if isinstance(node, Tag))
    report = str(hero) + '\n' + str(status) + '\n' + body + '\n'

    # Cards: the term table. A card's related ids are the other terms its definition
    # uses, in order of first use; links between terms in the source are kept the same way.
    names = []
    for other, row in terms.items():
        for name in [row['term'], *(row.get('aliases') or [])]:
            names.append((name, other))
    names.sort(key=lambda pair: -len(pair[0]))
    matcher = re.compile(r'(?<![\w-])(' + '|'.join(re.escape(n) for n, _ in names) +
                         r')(?:s|es)?(?![\w-])', re.I)
    lookup = {n.lower(): other for n, other in names}

    cards = []
    for ident, row in terms.items():
        definition = fragment(row['definition'])
        wrapper = definition.find('div', class_='statement')
        if wrapper is not None and len(definition.find_all(recursive=False)) == 1:
            wrapper.unwrap()
        related = []
        for link in definition.find_all('a', attrs={'data-term': True}):
            other = link['data-term']
            if other != ident and other in terms and other not in related:
                related.append(other)
            link.unwrap()
        plain = fragment(str(definition))
        for note in plain.find_all('annotation'):
            note.decompose()
        for match in matcher.finditer(plain.get_text(' ')):
            other = lookup[match.group(1).lower()]
            if other != ident and other not in related:
                related.append(other)
        cards.append({
            'id': ident,
            'display_name': row['term'],
            'definition': str(definition).strip(),
            'motivation': '',
            'context': '',
            'related': related,
            'aliases': row.get('aliases') or [],
        })

    as_of = header.find(id='as-of')
    stamp = re.search(r'\d{4}-\d{2}-\d{2}', as_of.get_text()) if as_of else None
    date = stamp.group(0) if stamp else dt.date.today().isoformat()

    (out / 'words').mkdir(parents=True, exist_ok=True)
    (out / 'cards').mkdir(parents=True, exist_ok=True)
    (out / 'words' / 'REPORT.html').write_text(report, encoding='utf-8')
    (out / 'cards' / 'TERMS.json').write_text(
        json.dumps(cards, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'words' / 'STATUS.md').write_text(
        'Status: stand-in\n'
        f'Date: {date}\n'
        f'Changed: converted from the integrated report of {date} without changing its words; '
        f'{len(equations)} stored equations restored; {attachments} attachment links kept without '
        f'their files; the status section built from {len(graph["nodes"])} questions and '
        f'{len(graph["families"])} obstruction families, with states assigned by the conversion; '
        f'{len(cards)} cards from the term table, with no motivation or context, and related ids '
        f'taken from the terms each definition uses.\n',
        encoding='utf-8')
    print(f'wrote {out}: {len(report):,} characters of report, {len(cards)} cards, '
          f'{len(board.find_all("li"))} status items')


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('source', type=Path)
    parser.add_argument('out', type=Path)
    args = parser.parse_args()
    convert(args.source, args.out)


if __name__ == '__main__':
    main()
