#!/usr/bin/env python3
"""Apply the foundation lane's changes to a repository root only where each target still has the baseline bytes.

    python3 apply_guarded.py <repository-root> [--check]

For every file in GUARD.json: if the target's sha256 equals baseline_sha256, the candidate bytes from files/
replace it (and the result is checked against candidate_sha256); if it already equals candidate_sha256 it is
left alone; any other hash is a divergence: nothing is written for any file, and the divergent paths are listed
so that the hunks in foundation.patch can be merged by hand. --check reports without writing.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest() if os.path.exists(path) else None


def main():
    root = os.path.abspath(sys.argv[1])
    check = '--check' in sys.argv
    guard = json.load(open(os.path.join(HERE, 'GUARD.json')))
    if not os.path.exists(os.path.join(root, guard['repo_root_marker'])):
        sys.exit(f'{root} is not the repository root (no {guard["repo_root_marker"]})')
    plan, divergent = [], []
    for f in guard['files']:
        h = sha(os.path.join(root, f['path']))
        if h == f['candidate_sha256']:
            print('already applied', f['path'])
        elif h == f['baseline_sha256']:
            plan.append(f)
        else:
            divergent.append((f['path'], h))
    if divergent:
        for path, h in divergent:
            print('DIVERGENT', path, h)
        sys.exit('no file written: merge the hunks of foundation.patch for the divergent paths')
    for f in plan:
        print(('would replace ' if check else 'replace ') + f['path'])
        if not check:
            data = open(os.path.join(HERE, 'files', f['path']), 'rb').read()
            open(os.path.join(root, f['path']), 'wb').write(data)
            assert sha(os.path.join(root, f['path'])) == f['candidate_sha256'], f['path']
    print('OK')


if __name__ == '__main__':
    main()
