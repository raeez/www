#!/usr/bin/env python3
"""Reproduce the issued reader in a fresh output directory."""
from pathlib import Path
import argparse
import subprocess
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    edition = Path(__file__).resolve().parent
    subprocess.run([sys.executable, '-B', str(edition / 'tools/build_reader.py'),
                    str(args.output.resolve()), '--edition', str(edition), '--frozen'], check=True)
