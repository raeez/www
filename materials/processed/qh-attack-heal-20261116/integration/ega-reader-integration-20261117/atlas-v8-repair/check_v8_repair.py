#!/usr/bin/env python3
"""Guard for atlas-v8-repair.patch (native QA findings G4, A2 and A6, with G5), run from the root of the tree the patch
is applied to (the integration tree).

    python3 check_v8_repair.py --check    # read-only: says whether the tree holds the installed bytes (and the patch
                                          # applies to them) or the repaired bytes, and checks this folder's SHA256SUMS
    python3 check_v8_repair.py --before   # strict: every file the patch touches is at its installed bytes
    git apply atlas-v8-repair.patch
    python3 check_v8_repair.py --after    # strict: every file the patch touches is at its repaired bytes

In every mode the files the patch leaves alone (listed as 'same') must be at their bytes. The expected hashes are read
from hashes.txt beside this guard: rows 'before|after|same <sha256> <bytes> <path>'. Exit 0 only when the tree is
wholly as the mode requires (--check: wholly before with the patch applying, or wholly after)."""
import hashlib
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATCH = HERE / 'atlas-v8-repair.patch'


def rows():
    out = []
    for line in (HERE / 'hashes.txt').read_text(encoding='utf-8').splitlines():
        if line.strip():
            kind, h, n, p = line.split(' ', 3)
            out.append((kind, h, int(n), p))
    return out


def at(p, h, n):
    f = Path(p)
    return f.is_file() and f.stat().st_size == n and hashlib.sha256(f.read_bytes()).hexdigest() == h


def state(table, kind):
    """The files of one kind that are not at their expected bytes."""
    return [p for k, h, n, p in table if k == kind and not at(p, h, n)]


def sums():
    """This folder's SHA256SUMS: every listed file at its listed bytes."""
    bad = []
    for line in (HERE / 'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        h, name = line.split(None, 1)
        f = HERE / name.strip().lstrip('*')
        if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest() != h:
            bad.append(name.strip())
    return bad


def main(argv):
    mode = argv[1] if len(argv) > 1 else '--check'
    table = rows()
    same = state(table, 'same')
    if mode == '--before':
        bad = state(table, 'before') + same
    elif mode == '--after':
        bad = state(table, 'after') + same
    elif mode == '--check':
        before, after = state(table, 'before'), state(table, 'after')
        folder = sums() if (HERE / 'SHA256SUMS').exists() else ['SHA256SUMS is missing']
        if folder:
            print('--check: this folder differs from its SHA256SUMS: ' + ', '.join(folder))
            return 1
        if same:
            print('--check: files the patch leaves alone differ: ' + ', '.join(same))
            return 1
        if not before:
            applies = subprocess.run(['git', 'apply', '--check', str(PATCH)], capture_output=True, text=True)
            if applies.returncode:
                print('--check: the installed bytes are present but the patch does not apply: ' + applies.stderr.strip())
                return 1
            print('--check: the tree holds the installed bytes; the patch applies (git apply --check); folder sums as listed')
            return 0
        if not after:
            print('--check: the tree holds the repaired bytes (the patch is applied); folder sums as listed')
            return 0
        print('--check: the tree is neither wholly installed nor wholly repaired; at neither: '
              + ', '.join(sorted(set(before) & set(after))))
        return 1
    else:
        print(__doc__)
        return 2
    print(f'{mode}: ' + ('as expected' if not bad else 'differs: ' + ', '.join(bad)))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
