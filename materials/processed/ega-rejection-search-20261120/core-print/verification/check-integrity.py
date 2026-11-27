#!/usr/bin/env python3
"""Check the private PDF's page bounds, metadata and destination integrity."""

import argparse
import hashlib
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup
import fitz
from pypdf import PdfReader

FORBIDDEN = re.compile(
    r'/Users/|/private/|/tmp/|\bfile://|\b(?:localhost|worktree|centcom|TODO|FIXME)\b|'
    r'127\.0\.0\.1|materials/processed|qh-attack-heal|Co-Authored-By|'
    r'\b(?:Claude|Fable|Astra|Codex|OpenAI|Anthropic|GPT-?\d)\b|'
    r'\b(?:draft|review packet|acceptance gate|release candidate|production history|internal milestone)\b',
    re.I,
)
PUBLIC_REPOSITORIES = {'gstore', 'lex', 'op', 'stack'}
PAGES_MARKERS = {
    'consecutive_cuts': ('Both cuts fail along the entire diagonal', 'its support depends on the coalgebra'),
    'sewing': ('on the logarithmic coordinate cover', 'changing the finite tree acts unitarily'),
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def check(args):
    raw = args.pdf.read_bytes()
    candidate = PdfReader(args.pdf)
    old = PdfReader(args.issued_pdf)
    assert candidate.metadata.title == old.metadata.title
    assert candidate.metadata.creator == old.metadata.creator
    assert candidate.metadata.producer == old.metadata.producer
    assert len(candidate.pages) == len(old.pages)
    for page, prior in zip(candidate.pages, old.pages):
        assert list(page.mediabox) == list(prior.mediabox)

    markdown = args.markdown.read_text()
    metadata = ' '.join(str(value) for value in candidate.metadata.values())
    paths = {'source': markdown, 'metadata': metadata, 'pdf_prose': args.prose.read_text()}
    for name, value in paths.items():
        assert not FORBIDDEN.search(value), f'Forbidden content in {name}: {FORBIDDEN.search(value)}'
        assert set(re.findall(r'https?://github\.com/momentum-sez/([a-z0-9-]+)', value)) <= PUBLIC_REPOSITORIES
        rest = re.sub(r'https?://github\.com/momentum-sez/[a-z0-9-]+', '', value)
        assert not re.search(r'https?://github\.com/[^/\s]+/[^/\s]+', rest)

    opening = json.loads(args.opening_receipt.read_text())
    audit = json.loads(args.print_audit.read_text())
    assert sha(raw) == audit['pdfSha']
    assert sha(markdown.encode()) == opening['expanded_frozen_markdown_sha256']
    assert audit['mathErrors'] == 0 and audit['errors'] == []
    assert audit['contentSha'] == audit['printContentSha']
    assert audit['missingImages'] == []
    assert len(audit['math']) == opening['equations_exact_in_order']
    assert sum(x['display'] for x in audit['math']) == opening['display_equations']
    tex_pattern = re.compile(r'\\\[(.*?)\\\]|\\\((.*?)\\\)', flags=re.S)
    assert [(item['display'], item['tex'].strip()) for item in audit['math']] == [
        (m[1] is not None, (m[1] or m[2]).strip()) for m in tex_pattern.finditer(markdown)]
    assert [style['complete']['sha256'] for style in opening['printed_embedded_styles']] == audit['inlineStyleHashes']

    candidates = BeautifulSoup(args.html.read_bytes(), 'lxml')
    ids = {}
    for row in candidates.find_all(id=True):
        ids[row['id']] = ids.get(row['id'], 0) + 1
    links = set()
    for reference in audit['portableReferences']:
        fragment = reference['fragment'].removeprefix('#')
        assert ids.get(fragment) == 1, fragment
        assert reference['url'] == 'https://raeez.com/quantum-holography/#' + fragment
        links.add(fragment)

    pages = []
    occurrences = {key: {marker: [] for marker in markers} for key, markers in PAGES_MARKERS.items()}
    with fitz.open(args.pdf) as document:
        for i, page in enumerate(document, start=1):
            view = page.rect
            spans = [span for block in page.get_text('dict')['blocks'] if 'lines' in block
                     for line in block['lines'] for span in line['spans'] if span['text'].strip()]
            assert spans
            left = min(span['bbox'][0] for span in spans)
            top = min(span['bbox'][1] for span in spans)
            right = max(span['bbox'][2] for span in spans)
            bottom = max(span['bbox'][3] for span in spans)
            assert 0 <= left < right <= view.width
            assert 0 <= top < bottom <= view.height
            unwrapped = re.sub(r'(?<=\w)[‐\u00ad][ \t]*\n\s*(?=\w)', '', page.get_text())
            text = ' '.join(unwrapped.split())
            for markers in occurrences.values():
                for phrase in markers:
                    if phrase in text:
                        markers[phrase].append(i)
            pages.append({
                'page': i,
                'text_spans': len(spans),
                'ink_bounding_box_points': [round(value, 2) for value in (left, top, right, bottom)],
            })
    assert all(page_nos for markers in occurrences.values() for page_nos in markers.values()), occurrences
    return {
        'status': 'PASS',
        'pdf': {'bytes': len(raw), 'sha256': sha(raw)},
        'earlier_and_new_metadata_title': candidate.metadata.title,
        'markdown_and_browser_math_exact': len(audit['math']),
        'portable_chapter_destinations_unique_and_present': sorted(links),
        'standalone_scan_hits': {name: [] for name in paths},
        'affected_paragraphs': occurrences,
        'pages': pages,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('pdf', 'issued-pdf', 'markdown', 'prose', 'opening-receipt', 'print-audit', 'html'):
        parser.add_argument('--' + name, type=Path, required=True)
    print(json.dumps(check(parser.parse_args()), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
