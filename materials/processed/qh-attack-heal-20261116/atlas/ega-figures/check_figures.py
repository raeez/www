#!/usr/bin/env python3
"""Guard for the figure patches, run from the root of the tree a patch is applied to.

    python3 check_figures.py --before-new     # the seven figure paths are free; then: git apply figures-files.patch
    python3 check_figures.py --before-delta   # the earlier frozen set (b28e07b0) is present; then: git apply figures-delta-from-b28e07b0.patch
    python3 check_figures.py --after          # the seven files are exactly the frozen bytes

The expected hashes are read from figures-hashes.txt and earlier-hashes.txt in this guard's folder."""
import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def table(name):
    rows = {}
    for line in (HERE / name).read_text(encoding='utf-8').splitlines():
        h, n, p = line.split(' ', 2)
        rows[p] = (h, int(n))
    return rows


def same(p, h, n):
    f = Path(p)
    return f.exists() and f.stat().st_size == n and hashlib.sha256(f.read_bytes()).hexdigest() == h


def main(argv):
    mode = argv[1] if len(argv) > 1 else '--after'
    want = table('figures-hashes.txt')
    if mode == '--before-new':
        bad = [p + ' already exists' for p in want if Path(p).exists()]
    elif mode == '--before-delta':
        bad = [p for p, (h, n) in table('earlier-hashes.txt').items() if not same(p, h, n)]
    else:
        bad = [p for p, (h, n) in want.items() if not same(p, h, n)]
    print(f'{mode}: ' + ('as expected' if not bad else 'differs: ' + ', '.join(bad)))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
