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
    'compiler/quantum-holography-status/atlas.py': ('3c9ba4d290f6971ebb79b3e08141191acecca128bf764bf2f4b17e76cffedcb6', 62892),
    'compiler/quantum-holography-status/atlas.css': ('5cb1f925f6f5b22fb9d3ceb5ed6d2c4d8fa412ec12c3c7bf1fc9eac39e495037', 36315),
    'compiler/quantum-holography-status/atlas.js': ('672246e70631b8cef81767576b153aa75604d3bbc6e5171eeff52efecca4d33c', 41279),
    'compiler/quantum-holography-status/tests/test_atlas.py': ('c8177f915abab8582d6bb30898ceda6c5d478fdbe280f67864deead89a6a1c47', 35602),
    'compiler/quantum-holography-status/tests/atlas.test.cjs': ('77fcd4cff28a36bb158bd3999fb6f8f6c50c2a0a648755b455b0ac933ebeb188', 32197),
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
