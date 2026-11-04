#!/usr/bin/env python3
"""Build quantum-holography-tracker.html from an input folder, then audit it.

    python3 compiler/build-quantum-holography-tracker.py --input <folder>
    python3 compiler/build-quantum-holography-tracker.py --allow-draft      # the stand-in

The input folder holds words/REPORT.html or words/REPORT.md, words/STATUS.md and
cards/TERMS.json; content/quantum-holography-tracker/README.md gives their formats.
Without --input the build reads content/quantum-holography-tracker/stand-in.

The page is written to the repository root only when the words are settled and every
audit passes, or when --allow-draft is given. A page that fails is written to the audit
folder instead, beside audit.txt and audit.json.
"""
import argparse
import gzip
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'compiler' / 'quantum-holography-tracker'))

import audit  # noqa: E402
import tracker  # noqa: E402

CONTENT = ROOT / 'content' / 'quantum-holography-tracker'


def math_font(explicit, disabled):
    if disabled:
        return None
    if explicit:
        return Path(explicit)
    if shutil.which('kpsewhich'):
        found = subprocess.run(['kpsewhich', 'Garamond-Math.otf'], capture_output=True, text=True).stdout.strip()
        if found:
            return Path(found)
    return None


def main():
    parser = argparse.ArgumentParser(description='Build and audit the quantum holography tracker page.')
    parser.add_argument('--input', type=Path, default=CONTENT / 'stand-in',
                        help='folder with words/ and cards/ (default: the stand-in)')
    parser.add_argument('--output', type=Path, default=ROOT / 'quantum-holography-tracker.html')
    parser.add_argument('--audit-dir', type=Path, default=CONTENT / 'audit')
    parser.add_argument('--allow-draft', action='store_true',
                        help='write the page although the words are not settled or an audit fails')
    parser.add_argument('--math-font', help='path to Garamond-Math.otf (default: found with kpsewhich)')
    parser.add_argument('--no-math-font', action='store_true', help='do not embed a math font')
    parser.add_argument('--compare', type=Path, help='an earlier single-file report, for the weight comparison')
    args = parser.parse_args()

    page = json.loads((CONTENT / 'page.json').read_text(encoding='utf-8'))
    font = math_font(args.math_font, args.no_math_font)
    build = tracker.Build(args.input, page, font)
    if font is None and not args.no_math_font:
        build.warnings.append('Garamond-Math.otf not found; the page uses the reader\'s math font')
    markup = build.run()

    compare = None
    if args.compare:
        data = args.compare.read_bytes()
        compare = {'path_name': args.compare.name, 'bytes': len(data), 'gzip_bytes': len(gzip.compress(data, 9))}
    result = audit.run(build, markup, ROOT.resolve(), compare)
    report = audit.text_report(result)

    args.audit_dir.mkdir(parents=True, exist_ok=True)
    (args.audit_dir / 'audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=1, default=str) + '\n',
                                               encoding='utf-8')
    (args.audit_dir / 'audit.txt').write_text(report, encoding='utf-8')
    print(report, end='')

    passed = not result['failures']
    if passed or args.allow_draft:
        args.output.write_text(markup, encoding='utf-8')
        print(f'\nwrote {args.output} ({len(markup.encode("utf-8")):,} bytes)'
              + ('' if passed else f' with {len(result["failures"])} audit failures (--allow-draft)'))
        return 0
    rejected = args.audit_dir / 'rejected.html'
    rejected.write_text(markup, encoding='utf-8')
    print(f'\nnot written: {len(result["failures"])} audit failures. The candidate page is {rejected}.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
