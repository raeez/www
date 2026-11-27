#!/usr/bin/env python3
"""Check the standalone opening PDF against Chromium's exact source snapshot."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import unicodedata

import fitz
from pypdf import PdfReader


def words(value):
    return re.findall(r'[^\W_]+', unicodedata.normalize('NFKC', value).casefold())


def typeset_prose(pdf_path):
    """Follow the prose font baselines separately from stacked math glyphs."""
    pages = []
    with fitz.open(pdf_path) as document:
        for number, page in enumerate(document, start=1):
            prose_fonts = set()
            for font in page.get_fonts():
                xref, _, font_type, name, *_ = font
                if not name and font_type == 'Type3':
                    kind, descriptor = document.xref_get_key(xref, 'FontDescriptor')
                    if kind != 'xref':
                        continue
                    name = document.xref_get_key(int(descriptor.split()[0]), 'FontName')[1]
                    if 'EBGaramond' in name:
                        prose_fonts.add(f'Type3 ({xref} 0 R)')
                elif 'EBGaramond' in name:
                    prose_fonts.add(name.split('+')[-1])

            spans = [span for block in page.get_text('dict')['blocks']
                     for line in block.get('lines', []) for span in line['spans']
                     if span['font'] in prose_fonts]
            rows = []
            for span in sorted(spans, key=lambda span: span['origin'][1]):
                y = span['origin'][1]
                if not rows or y - rows[-1][0] > 0.8:
                    rows.append((y, []))
                rows[-1][1].append(span)

            prose_lines = []
            for _, row in rows:
                spans = sorted(row, key=lambda span: span['origin'][0])
                pieces = [spans[0]['text']]
                for previous, span in zip(spans, spans[1:]):
                    if span['origin'][0] - previous['bbox'][2] > 0.65:
                        pieces.append(' ')
                    pieces.append(span['text'])
                prose_lines.append(''.join(pieces).strip())
            assert prose_lines.pop() == str(number)
            pages.append('\n'.join(prose_lines))
    return '\n'.join(pages)


def check(pdf_path, audit_path, opening_path):
    snapshot = json.loads(audit_path.read_text())
    source = json.loads(opening_path.read_text())
    sha = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    assert sha == snapshot['pdfSha']
    assert source['expanded_release_html_sha256'] == snapshot['sourceSha']
    assert len(snapshot['math']) == source['equations_exact_in_order']
    assert sum(item['display'] for item in snapshot['math']) == source['display_equations']

    text = subprocess.run(['pdftotext', '-layout', str(pdf_path), '-'], check=True,
                          capture_output=True, text=True).stdout
    audit_path.with_name('print-extracted.txt').write_text(text)
    prose = typeset_prose(pdf_path)
    audit_path.with_name('print-prose.txt').write_text(prose)
    joined = re.sub(r'(?<=\w)[‐\u00ad][ \t]*\n\s*(?=\w)', '', prose)
    expected = words(snapshot['prose'])
    assert words(joined) == words(snapshot['openingTitle']) + expected
    expected_ending = words(snapshot['expectedEnding'])
    assert expected_ending == words(joined)[-len(expected_ending):]
    assert 'if you could measure a quantum field' not in joined.casefold()
    assert re.search(r'\bIntroduction\b', joined, re.I)

    reader = PdfReader(pdf_path)
    assert str(reader.metadata.title) == snapshot['renderedTitle']
    assert '/StructTreeRoot' in reader.trailer['/Root']
    assert all(page.extract_text().strip() for page in reader.pages)
    assert len(reader.outline) == 2
    assert reader.outline[0]['/Title'] == snapshot['openingTitle']
    outline = [entry['/Title'] for entry in reader.outline[1]]
    assert outline == [entry['heading'] for entry in snapshot['headings']]
    assert not re.search(r'localhost|127\.0\.0\.1|/Users/', str(reader.metadata))
    outgoing = set()
    link_count = 0
    for page in reader.pages:
        for item in page.get('/Annots', []):
            link = item.get_object()
            if link.get('/Subtype') != '/Link':
                continue
            link_count += 1
            action = link.get('/A')
            if action and action.get('/S') == '/URI':
                outgoing.add(str(action['/URI']))
    assert outgoing == {reference['url'] for reference in snapshot['portableReferences']}
    assert all(uri.startswith('https://raeez.com/quantum-holography/#') for uri in outgoing)
    report = {
        'pdf_sha256': sha,
        'source_html_sha256': snapshot['sourceSha'],
        'source_markdown_sha256': source['expanded_frozen_markdown_sha256'],
        'printed_section_dom_sha256': snapshot['printSectionSha'],
        'printed_mathematical_body_dom_sha256': snapshot['printContentSha'],
        'unchanged_inline_stylesheets_sha256': snapshot['inlineStyleHashes'],
        'source_mathml_expressions_exact': len(snapshot['math']),
        'source_display_equations': source['display_equations'],
        'ordered_matched_prose_tokens': len(expected),
        'complete_source_ending': snapshot['expectedEnding'],
        'pdf_pages': len(reader.pages),
        'pdf_outline_items': [snapshot['openingTitle'], *outline],
        'pdf_link_annotations': link_count,
        'canonical_external_references': sorted(outgoing),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    check(*(Path(arg) for arg in sys.argv[1:]))
