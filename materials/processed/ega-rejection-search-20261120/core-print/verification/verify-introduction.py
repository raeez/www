#!/usr/bin/env python3
"""Prepare and bind a private introduction print of an already-built reader."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import runpy
import subprocess

from bs4 import BeautifulSoup

SOURCE = Path('content/quantum-holography-status/reader-data/expanded-introduction.md')
BODY = b'<div class="mg-introduction-text">'
LEGACY = b'<div class="mg-front-intro">'
CANONICAL = 'https://raeez.com/quantum-holography/'
BASE = '04dbd695741f1437957ff8951b87ef1d41d0f5b0'


def pin(value):
    raw = value.encode() if isinstance(value, str) else value
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def get_functions(review):
    checks = runpy.run_path(str(review / 'tracker-introduction-20261120-garden/verification/check-opening.py'))
    preservation = runpy.run_path(str(review / 'tracker-introduction-20261119/check_preservation.py'))
    return checks, preservation['get_html_block']


def validate_source(html, markdown, checks):
    visible = markdown.decode()
    actual, prose = checks['extract_body'](html)
    expected = [(item[1] is not None, item[1] or item[2]) for item in checks['TEX'].finditer(visible)]
    normal = checks['normalize_equations']
    assert normal(actual) == normal(expected), 'Ordered MathML annotations or display roles differ from the source.'
    assert prose == checks['source_text'](visible), 'Visible text differs from the Markdown.'
    return actual, expected, prose


def intro_shell(raw, block):
    marker, = re.findall(rb'<section\b[^>]*\bid="book-abstract"[^>]*>', raw)
    return block(raw, marker)[0]


def style_rules(raw):
    styles = re.findall(rb'<style\b[^>]*>(.*?)</style>', raw.split(b'</head>', 1)[0], re.S)
    strip_fonts = re.compile(rb'(?<=base64,)[A-Za-z0-9+/=]+(?=\))')
    return [{'complete': pin(style), 'rules': pin(strip_fonts.sub(b'', style))}
            for style in styles]


def prepare(args):
    observed = args.reader.read_bytes()
    current = (args.source_root / SOURCE).read_bytes()
    old_source = (args.frozen / 'source-tree' / SOURCE).read_bytes()
    selected = json.loads(args.selection.read_bytes())
    assert selected['files'][SOURCE.as_posix()] == pin(current)['sha256']
    manifest = json.loads((args.source_root / SOURCE.parent / 'manifest.json').read_bytes())
    assert manifest['expanded_introduction'] == {'file': SOURCE.name, 'pdf': True}
    assert current != old_source

    host = runpy.run_path(str(args.host_transform))
    headers = host['read_headers']()
    mounted = host['transform']('index.html', observed, headers)
    assert host['transform']('index.html', mounted, headers, reverse=True) == observed
    assert mounted.split(b'</head>', 1)[1] == observed.split(b'</head>', 1)[1]

    checks, block = get_functions(args.reviews)
    old = subprocess.check_output(['git', '--no-optional-locks', 'show', f'{BASE}:quantum-holography/index.html'])
    old_shell, current_shell = intro_shell(old, block), intro_shell(mounted, block)
    old_math, _, old_prose = validate_source(old_shell, old_source, checks)
    math, expected_math, prose = validate_source(current_shell, current, checks)
    old_legacy, old_children = block(old, LEGACY)
    new_legacy, new_children = block(mounted, LEGACY)
    assert [tag for tag, _ in old_children] == [tag for tag, _ in new_children]
    assert len(new_children) == 54 and new_children[4][0] == 'figure'
    assert sum(tag == 'p' for tag, _ in new_children) == 53
    legacy_number = 0
    legacy_changed = []
    for (tag, before), (_, after) in zip(old_children, new_children):
        if tag != 'p':
            assert before == after
            continue
        legacy_number += 1
        if before != after:
            legacy_changed.append(legacy_number)
    legacy_prose = BeautifulSoup(new_legacy, 'lxml')
    for node in legacy_prose.select('math, figure'):
        node.decompose()
    assert checks['words'](legacy_prose.get_text(' ', strip=True)) == checks['source_text'](manifest['introduction'])

    old_css, new_css = style_rules(old), style_rules(mounted)
    assert [row['rules'] for row in old_css] == [row['rules'] for row in new_css], \
        'Rules other than the embedded font data differ.'
    old_soup = BeautifulSoup(old_shell, 'lxml')
    soup = BeautifulSoup(current_shell, 'lxml')
    heading = lambda node: [(h.name, h.get('id'), h.get_text(' ', strip=True)) for h in node.select('.mg-introduction-text h3, .mg-introduction-text h4')]
    assert heading(soup) == heading(old_soup)
    links = lambda node: [(a.get('href'), a.get_text(' ', strip=True)) for a in node.select('a[href]')]
    assert links(soup) == links(old_soup)
    assert sum(href == SOURCE.name.replace('expanded-', '').replace('.md', '.pdf') for href, _ in links(soup)) == 1

    body, _ = block(mounted, BODY)
    old_body, _ = block(old, BODY)
    args.preview.write_bytes(mounted)
    report = {
        'baseline_commit': BASE,
        'source_asset': str(args.reader),
        'frozen_selection': pin(args.selection.read_bytes()),
        'unmounted_html': pin(observed),
        'mounted_html': pin(mounted),
        'expanded_release_html_sha256': pin(mounted)['sha256'],
        'expanded_frozen_markdown_sha256': pin(current)['sha256'],
        'prior_expanded_markdown': pin(old_source),
        'expanded_opening_section_sha256': pin(current_shell)['sha256'],
        'expanded_opening_body': pin(body),
        'prior_expanded_opening_body': pin(old_body),
        'legacy_opening': pin(new_legacy),
        'legacy_paragraphs': 53,
        'legacy_figure_after': 4,
        'legacy_paragraphs_changed_in_the_reader_outside_print': legacy_changed,
        'previous_word_count': len(old_prose),
        'matched_visible_text_words': len(prose),
        'previous_mathml_count': len(old_math),
        'equations_exact_in_order': len(math),
        'tex_annotations_byte_equal_after_outer_trim': sum(
            (a[0], a[1].strip()) == (b[0], b[1].strip()) for a, b in zip(math, expected_math)),
        'display_equations': sum(display for display, _ in math),
        'headings': heading(soup),
        'links': links(soup),
        'stylesheet_identity_apart_from_embedded_fonts': True,
        'prior_embedded_styles': old_css,
        'printed_embedded_styles': new_css,
    }
    return report


def bind(args):
    _, block = get_functions(args.reviews)
    early = args.preview.read_bytes()
    final = args.reader.read_bytes()
    host = runpy.run_path(str(args.host_transform))
    final_mounted = host['transform']('index.html', final, host['read_headers']())
    early_body = block(early, BODY)[0]
    final_body = block(final_mounted, BODY)[0]
    assert early_body == final_body, 'The final release differs from the printed mathematical body.'
    assert intro_shell(early, block) == intro_shell(final_mounted, block)
    assert style_rules(early) == style_rules(final_mounted)
    if args.mounted_release:
        args.mounted_release.parent.mkdir(parents=True, exist_ok=True)
        args.mounted_release.write_bytes(final_mounted)
    return {
        'release_asset': str(args.reader),
        'release_html': pin(final),
        'mounted_release_html': pin(final_mounted),
        'mounted_print_preview_html': pin(early),
        'identical_expanded_introduction': pin(early_body),
        'identical_full_intro_section': pin(intro_shell(early, block)),
        'identical_inline_styles': style_rules(early),
        'pdf': pin(args.pdf.read_bytes()) if args.pdf else None,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode', choices=('prepare', 'bind'))
    for name in ('reader', 'preview', 'reviews', 'host-transform', 'source-root', 'selection', 'frozen', 'pdf', 'mounted-release'):
        p.add_argument('--' + name, type=Path)
    args = p.parse_args()
    print(json.dumps(prepare(args) if args.mode == 'prepare' else bind(args), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
