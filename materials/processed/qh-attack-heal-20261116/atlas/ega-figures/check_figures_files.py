#!/usr/bin/env python3
"""Guard for figures-files.patch, run from the root of the tree it is applied to.

    python3 check_figures_files.py --before   # the seven figure paths are free (the patch only creates files)
    git apply figures-files.patch
    python3 check_figures_files.py --after    # the seven files are exactly these bytes"""
import hashlib
import sys
from pathlib import Path

EXPECTED = {
    'compiler/quantum-holography-status/figures.py': ('9029374abc657b054653ada037dac42406936b1bd600340b9f83d9105b180930', 26427),
    'compiler/quantum-holography-status/figures.css': ('9c4d8472ebc2ef6064847b8b2bf1fb6449754fb37b8f2612e3e27c13e588726f', 7383),
    'compiler/quantum-holography-status/figures.js': ('dec21245efb86623863fee1f6a4329dbd4e9dfbf8f21e6c269c5f3354c2965b0', 8491),
    'compiler/quantum-holography-status/tests/test_figures.py': ('919af1bd887b1548cb2115d4cc94e5200382d69ae18f7e68af0fdf35de0687d6', 8154),
    'compiler/quantum-holography-status/tests/figures.test.cjs': ('8139e90e96cbbbba2c5b5aaad372b495b98b7bbf45d65e0eff913122bd7ac6c2', 4672),
    'compiler/quantum-holography-status/tests/figures_page.py': ('8ac23dc036107435dc8adba1fc2c5e0a7d79e9f75fbffe6e13614f66bf30a73a', 2413),
    'compiler/quantum-holography-status/tests/fixtures/figures-synthetic.json': ('8653fb6c8a34688ca06f784d2552c3cafe91ce8450ff47e7757b1568fc5dd9ea', 3920),
}


def main(argv):
    after = '--after' in argv
    bad = []
    for p, (h, n) in EXPECTED.items():
        f = Path(p)
        if after and (not f.exists() or f.stat().st_size != n or hashlib.sha256(f.read_bytes()).hexdigest() != h):
            bad.append(p)
        if not after and f.exists():
            bad.append(p + ' already exists')
    print(('after: all seven figure files as expected' if after else 'before: the seven figure paths are free') if not bad else 'differs: ' + ', '.join(bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
