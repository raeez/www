#!/usr/bin/env python3
"""Guard for atlas-c5-marks.patch (C5: the atlas draws the page's own status marks), run from the root of the tree.

    python3 check_atlas_c5.py --before   # the three files are root's installed atlas set; the other three as listed
    git apply atlas-c5-marks.patch
    python3 check_atlas_c5.py --after    # the three files are exactly the C5 bytes; the other three untouched

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
