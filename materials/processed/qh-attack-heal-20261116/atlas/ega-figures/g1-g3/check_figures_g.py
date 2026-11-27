#!/usr/bin/env python3
"""Guard for figures-g1-g3.patch (native findings G1-G3 on the Gaussian figure), run from the root of the tree.

    python3 check_figures_g.py --before   # the five files are the installed five-model set; figures.js and figures_page.py as listed
    git apply figures-g1-g3.patch
    python3 check_figures_g.py --after    # the five files are exactly the repaired bytes; the other two untouched

Expected hashes are read from hashes.txt beside this guard (rows: before|after|same sha256 bytes path)."""
import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main(argv):
    mode = 'after' if '--after' in argv else 'before'
    bad = []
    for line in (HERE / 'hashes.txt').read_text(encoding='utf-8').splitlines():
        kind, h, n, p = line.split(' ', 3)
        if kind not in (mode, 'same'):
            continue
        f = Path(p)
        if not f.exists() or f.stat().st_size != int(n) or hashlib.sha256(f.read_bytes()).hexdigest() != h:
            bad.append(f'{p} ({kind})')
    print(f'--{mode}: ' + ('as expected' if not bad else 'differs: ' + ', '.join(bad)))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
