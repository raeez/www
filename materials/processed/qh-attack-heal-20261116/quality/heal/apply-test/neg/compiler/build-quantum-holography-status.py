#!/usr/bin/env python3
"""Build quantum-holography-tracker.html, the programme's status page, then audit it.

    python3 compiler/build-quantum-holography-status.py
    python3 compiler/build-quantum-holography-status.py --input <folder> --output <file>

The input folder (default content/quantum-holography-status) holds content.json, essay.md
and page.json; its README.md gives their formats. The page is written to the repository
root only when every audit passes, or when --allow-draft is given; otherwise it is written
to the audit folder beside audit.txt and audit.json.

This replaces, for this URL, the older long-report builder build-quantum-holography-tracker.py,
which reads a different input and writes the same output path.
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'compiler' / 'quantum-holography-status'))

import audit  # noqa: E402
import status  # noqa: E402

CONTENT = ROOT / 'content' / 'quantum-holography-status'
TEXT_FONTS = {
    ('QH Garamond', 400, 'normal'): 'EBGaramond-Regular.otf',
    ('QH Garamond', 400, 'italic'): 'EBGaramond-Italic.otf',
    ('QH Garamond', 600, 'normal'): 'EBGaramond-SemiBold.otf',
}


def find(name):
    if shutil.which('kpsewhich'):
        found = subprocess.run(['kpsewhich', name], capture_output=True, text=True).stdout.strip()
        if found:
            return Path(found)
    return None


def main():
    parser = argparse.ArgumentParser(description='Build and audit the quantum holography status page.')
    parser.add_argument('--input', type=Path, default=CONTENT)
    parser.add_argument('--output', type=Path, default=ROOT / 'quantum-holography-tracker.html')
    parser.add_argument('--audit-dir', type=Path, default=CONTENT / 'audit')
    parser.add_argument('--allow-draft', action='store_true', help='write the page although an audit fails')
    parser.add_argument('--no-fonts', action='store_true', help='embed no fonts (faster, for layout work)')
    args = parser.parse_args()

    page = json.loads((CONTENT / 'page.json').read_text(encoding='utf-8'))
    text_fonts, math_font = {}, None
    if not args.no_fonts:
        for key, name in TEXT_FONTS.items():
            path = find(name)
            if path:
                text_fonts[key] = path
        math_font = find('Garamond-Math.otf')
    build = status.Build(args.input, page, text_fonts, math_font)
    if not args.no_fonts and len(text_fonts) < len(TEXT_FONTS):
        build.warnings.append('EB Garamond not found in TeX Live; the page falls back to system serif fonts')
    if not args.no_fonts and math_font is None:
        build.warnings.append('Garamond-Math.otf not found; the page uses the reader\'s math font')
    markup = build.run()
    result = audit.run(build, markup)
    report = audit.text_report(result)

    args.audit_dir.mkdir(parents=True, exist_ok=True)
    (args.audit_dir / 'audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (args.audit_dir / 'audit.txt').write_text(report, encoding='utf-8')
    print(report, end='')

    if not result['failures'] or args.allow_draft:
        args.output.write_text(markup, encoding='utf-8')
        print(f'wrote {args.output}')
        return 0
    rejected = args.audit_dir / 'rejected.html'
    rejected.write_text(markup, encoding='utf-8')
    print(f'audit failed; page written to {rejected}')
    return 1


if __name__ == '__main__':
    sys.exit(main())
