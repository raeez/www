#!/usr/bin/env python3
"""Guard for atlas-scale-repair.patch (native QA C1, with C2, C3, C4 and C6), run from the root of root's integration tree.

    python3 check_atlas_scale_repair.py --before   # the six atlas files are exactly the integrated set (c29)
    git apply atlas-scale-repair.patch
    python3 check_atlas_scale_repair.py --after    # the six atlas files are exactly the repaired set

Only the atlas lane's six files change; no content, status, hypothesis, anchor or other lane's file is touched."""
import hashlib
import sys
from pathlib import Path

BEFORE = {
    'compiler/quantum-holography-status/atlas.py': ('3c9ba4d290f6971ebb79b3e08141191acecca128bf764bf2f4b17e76cffedcb6', 62892),
    'compiler/quantum-holography-status/atlas.css': ('5cb1f925f6f5b22fb9d3ceb5ed6d2c4d8fa412ec12c3c7bf1fc9eac39e495037', 36315),
    'compiler/quantum-holography-status/atlas.js': ('672246e70631b8cef81767576b153aa75604d3bbc6e5171eeff52efecca4d33c', 41279),
    'compiler/quantum-holography-status/tests/test_atlas.py': ('c8177f915abab8582d6bb30898ceda6c5d478fdbe280f67864deead89a6a1c47', 35602),
    'compiler/quantum-holography-status/tests/atlas.test.cjs': ('77fcd4cff28a36bb158bd3999fb6f8f6c50c2a0a648755b455b0ac933ebeb188', 32197),
    'compiler/quantum-holography-status/tests/fixtures/atlas-synthetic.json': ('2a5f0c7bc84e66832d6bb48edea0570ff8f28b6d049d6c16388bde4b4b6f9d32', 10171),
}
AFTER = {
    'compiler/quantum-holography-status/atlas.py': ('c61a3ef4f8e653df54c81ee7d4fae3f8426eb975b5c498a9bd6ddd6d0b8e122a', 64517),
    'compiler/quantum-holography-status/atlas.css': ('7542bc564dbb69d79b30695882a6ece42dd42878576fe7432df805cb6a489273', 38223),
    'compiler/quantum-holography-status/atlas.js': ('6194a1021a20f1517f251c4f40e4a79819a5686a82a76cafb29cb5d06114d1b8', 42336),
    'compiler/quantum-holography-status/tests/test_atlas.py': ('26605350333002e38ca3a5c5e941325641c07747be39a17c9255bc3cbf5123ea', 39208),
    'compiler/quantum-holography-status/tests/atlas.test.cjs': ('e8a9a031bebb5f4b26908b34d9333f40eefb98ef553de7f135f4bbeb7bed8c0e', 33851),
    'compiler/quantum-holography-status/tests/fixtures/atlas-synthetic.json': ('2a5f0c7bc84e66832d6bb48edea0570ff8f28b6d049d6c16388bde4b4b6f9d32', 10171),
}


def main(argv):
    after = '--after' in argv
    pins = AFTER if after else BEFORE
    bad = [p for p, (h, n) in pins.items() if not Path(p).exists() or Path(p).stat().st_size != n
           or hashlib.sha256(Path(p).read_bytes()).hexdigest() != h]
    print(('after: the repaired set' if after else 'before: the integrated set (c29)') + (' as expected' if not bad else ': differs: ' + ', '.join(bad)))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
