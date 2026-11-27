#!/usr/bin/env python3
"""Guard for atlas-delta.c24-c29.patch, run from the root of a tree that holds the c24 atlas set (patch d0623e3b...).

    python3 check_atlas_delta.c24-c29.py --before   # the six atlas files are exactly the c24 set
    git apply atlas-delta.c24-c29.patch
    python3 check_atlas_delta.c24-c29.py --after    # the six atlas files are exactly the c29 set

The delta changes only the six atlas files: the page-search status of every claim and the status words chosen by
the stored code (the content owner's status-language ruling), the page's mark beside each status in the key, a
named finding when the page cannot show it, the mark colour left to the page, and their tests."""
import hashlib
import sys
from pathlib import Path

BEFORE = {
    'compiler/quantum-holography-status/atlas.py': ('0505671d059eda436f9ba77883ca4ff1f9a3f4d8df4d164fd53244d7490f8174', 62768),
    'compiler/quantum-holography-status/atlas.css': ('b7a7e4ec92d047e61712a68d7c64ab9519df6aedf0b0bfd2f25dff2f577265e0', 36580),
    'compiler/quantum-holography-status/atlas.js': ('897ebd2c5ca618243fdaeb6e879ce9dd6a735f974d2cb6f646f4266be8c8f105', 41299),
    'compiler/quantum-holography-status/tests/test_atlas.py': ('96bdb27b9a3f50752668d93c205c389fab4f01f2c4e546d20dfe0a8accff8d14', 34199),
    'compiler/quantum-holography-status/tests/atlas.test.cjs': ('a92ac84ebbe68d925586ed18a444fda1f4f12217819df9dc93645c09ebdba65a', 30103),
    'compiler/quantum-holography-status/tests/fixtures/atlas-synthetic.json': ('2a5f0c7bc84e66832d6bb48edea0570ff8f28b6d049d6c16388bde4b4b6f9d32', 10171),
}
AFTER = {
    'compiler/quantum-holography-status/atlas.py': ('3c9ba4d290f6971ebb79b3e08141191acecca128bf764bf2f4b17e76cffedcb6', 62892),
    'compiler/quantum-holography-status/atlas.css': ('5cb1f925f6f5b22fb9d3ceb5ed6d2c4d8fa412ec12c3c7bf1fc9eac39e495037', 36315),
    'compiler/quantum-holography-status/atlas.js': ('672246e70631b8cef81767576b153aa75604d3bbc6e5171eeff52efecca4d33c', 41279),
    'compiler/quantum-holography-status/tests/test_atlas.py': ('c8177f915abab8582d6bb30898ceda6c5d478fdbe280f67864deead89a6a1c47', 35602),
    'compiler/quantum-holography-status/tests/atlas.test.cjs': ('77fcd4cff28a36bb158bd3999fb6f8f6c50c2a0a648755b455b0ac933ebeb188', 32197),
    'compiler/quantum-holography-status/tests/fixtures/atlas-synthetic.json': ('2a5f0c7bc84e66832d6bb48edea0570ff8f28b6d049d6c16388bde4b4b6f9d32', 10171),
}


def main(argv):
    pins = AFTER if '--after' in argv else BEFORE
    bad = [p for p, (h, n) in pins.items() if not Path(p).exists() or Path(p).stat().st_size != n
           or hashlib.sha256(Path(p).read_bytes()).hexdigest() != h]
    print(('after: the c29 set' if '--after' in argv else 'before: the c24 set') + (' as expected' if not bad else ': differs: ' + ', '.join(bad)))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
