#!/usr/bin/env python3
"""Guard for atlas-native-repair.patch (native QA C1-C4, C6, C7, C11, C13, C15, C16, C19), run from the root of root's integration tree.

    python3 check_atlas_native_repair.py --before   # the six atlas files are exactly the integrated set (c29)
    git apply atlas-native-repair.patch
    python3 check_atlas_native_repair.py --after    # the six atlas files are exactly the repaired set

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
    'compiler/quantum-holography-status/atlas.py': ('fd65eec00267341eca5673f799d176ab70cc947ff537905e26db57d85244c9b5', 65464),
    'compiler/quantum-holography-status/atlas.css': ('a358605c9befb63b451642bbc8c1f58dc2d0365f3d682e86fc1619c581a09ecf', 39712),
    'compiler/quantum-holography-status/atlas.js': ('276565d774c4ec6125973907325751af0f72be0d4c95c132932b22655d6c0654', 47321),
    'compiler/quantum-holography-status/tests/test_atlas.py': ('b33eb4eaf560c7a6b9e808621d32910a8da573f313ca58c1e6b1aa08b5f69c94', 41164),
    'compiler/quantum-holography-status/tests/atlas.test.cjs': ('5570b7923f68aa98fe5bdfae81cf77ffaea1363375bdf31f4c280630d73694a2', 35442),
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
