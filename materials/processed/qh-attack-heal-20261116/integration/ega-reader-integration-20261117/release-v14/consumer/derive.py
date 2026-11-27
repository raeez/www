#!/usr/bin/env python3
"""Complete the exact maintained heading and link metadata after the page split."""
import argparse
import hashlib
import html
import json
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('site', type=Path)
    parser.add_argument('source_reader', type=Path)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    requirements = json.loads((here / 'requirements.json').read_text())
    source_reader = args.source_reader.read_text()
    final_reader = (here / 'reader.js').read_text()
    pages = {n: (args.site / n).read_text() for n in ('index.html', 'reference.html', 'atlas.html')}
    changes = []
    for name in pages:
        matches = [m for m in re.finditer(r'<script>(.*?)</script>', pages[name], re.S) if m.group(1).lstrip().startswith('/* The reader of the monograph.')]
        if len(matches) != 1 or matches[0].group(1).strip() != source_reader.strip():
            raise RuntimeError(f'embedded reader input mismatch: {name}')
        old = matches[0].group(1)
        if old.count(source_reader) != 1:
            raise RuntimeError('reader embedding boundary mismatch')
        new = old.replace(source_reader, final_reader, 1)
        pages[name] = pages[name].replace('<script>' + old + '</script>', '<script>' + new + '</script>', 1)
        changes.append({'kind': 'reader_component', 'page': name, 'before_sha256': hashlib.sha256(old.encode()).hexdigest(), 'after_sha256': hashlib.sha256(new.encode()).hexdigest()})
    for row in requirements['headings']:
        page, ident = row['page'], row['id']
        matches = list(re.finditer(r'(<h4\b[^>]*(?<![\w-])id="%s"[^>]*>)(.*?)</h4>' % re.escape(ident), pages[page], re.S))
        if len(matches) != 1 or html.unescape(re.sub(r'<[^>]+>', '', matches[0].group(2))) != row['title']:
            raise RuntimeError(f'authored heading mismatch: {ident}')
        old = matches[0].group(1)
        if 'data-reader-search-heading' in old:
            raise RuntimeError(f'heading already completed: {ident}')
        new = old[:-1] + ' data-reader-search-heading>'
        pages[page] = pages[page].replace(old, new, 1)
        changes.append({'kind': 'heading_marker', 'page': page, 'id': ident, 'old': old, 'new': new})
    for row in requirements['links']:
        page, label, href = row['page'], html.escape(row['label'], quote=False), row['href']
        target_page, ident = href.split('#')
        if target_page not in pages or len(re.findall(r'(?<![\w-])id="%s"' % re.escape(ident), pages[target_page])) != 1 or pages[page].count(label) != 1:
            raise RuntimeError(f'authored navigation guard failed: {href}')
        new = '<a href="' + html.escape(href, quote=True) + '">' + label + '</a>'
        pages[page] = pages[page].replace(label, new, 1)
        changes.append({'kind': 'authored_link', 'page': page, 'old': label, 'new': new})
    for name, markup in pages.items():
        (args.site / name).write_text(markup)
    args.report.write_text(json.dumps({'status': 'PASS', 'heading_markers': len(requirements['headings']), 'authored_links': len(requirements['links']), 'changes': changes}, ensure_ascii=False, indent=2) + '\n')
    print('PASS: five heading markers, eight authored links and the maintained reader component')


if __name__ == '__main__':
    main()
