#!/usr/bin/env python3
"""Guard for atlas-files.patch, run from the root of the tree the patch is applied to.

    python3 check_atlas_files.py --before   # the six atlas paths are absent (or already exactly these files)
    git apply atlas-files.patch
    python3 check_atlas_files.py --after    # the six files are exactly these bytes

The patch only creates the six files of the atlas and touches no existing file. With --baseline <BASELINE.json>
the guard also checks that the shared tracker files still have the pinned baseline bytes (true of the atlas
worktree; in an integrated tree the foundation, interaction and content files differ by design)."""
import hashlib
import json
import sys
from pathlib import Path

EXPECTED = {
    'compiler/quantum-holography-status/atlas.py': ('884e66c65c41ee8900e740eef50ea99ddd9c3d976efb6355bbe2db2d148d4c91', 63837),
    'compiler/quantum-holography-status/atlas.css': ('b9ffd03d0316dadd6ca586c7352126c89511382d2c7e123ccb5c55584dc3b41c', 36594),
    'compiler/quantum-holography-status/atlas.js': ('897ebd2c5ca618243fdaeb6e879ce9dd6a735f974d2cb6f646f4266be8c8f105', 41299),
    'compiler/quantum-holography-status/tests/test_atlas.py': ('f656c54359c31d48209bc5ba0509b5905155e53d373e6ef2b07992156a647a67', 35143),
    'compiler/quantum-holography-status/tests/atlas.test.cjs': ('93b954f69700129f7e6b9b1aea7b50bd3d09a2e42bf3c0113d4a7f0aa17572c6', 31843),
    'compiler/quantum-holography-status/tests/fixtures/atlas-synthetic.json': ('2a5f0c7bc84e66832d6bb48edea0570ff8f28b6d049d6c16388bde4b4b6f9d32', 10171),
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(argv):
    mode = '--after' if '--after' in argv or '--before' not in argv else '--before'
    bad, present = [], 0
    for rel, (h, n) in EXPECTED.items():
        p = Path(rel)
        if mode == '--before':
            if p.exists() and (sha(p) != h or p.stat().st_size != n):
                bad.append(f'{rel} exists with other content; the patch would not apply')
            elif p.exists():
                present += 1
        elif not p.exists() or sha(p) != h or p.stat().st_size != n:
            bad.append(f'{rel} is not the expected file')
    if '--baseline' in argv:
        pins = json.loads(Path(argv[argv.index('--baseline') + 1]).read_text(encoding='utf-8'))['files']
        for f in pins:
            p = Path(f['path'])
            if not p.exists() or sha(p) != f['sha256']:
                bad.append(f'baseline file {f["path"]} differs from its pin')
        print(f'baseline pins checked: {len(pins)}')
    if mode == '--before' and present == len(EXPECTED):
        ok = 'the six atlas files are already exactly these files: do not apply the patch again'
    elif mode == '--before' and present:
        ok = f'{present} of the six files are already exactly these files and the rest are absent: apply the patch with --exclude for those'
    elif mode == '--before':
        ok = 'the six atlas paths are free: apply the patch'
    else:
        ok = 'all six atlas files as expected'
    print(f'{mode[2:]}: ' + (ok if not bad else '; '.join(bad)))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
