#!/usr/bin/env python3
"""Make the lane's guarded patch from the baseline snapshot (baseline/src, hash-checked against BASELINE.json).

    python3 tools/make_patch.py            (run from the lane directory)

Writes patch/foundation.patch (unified diff, paths a/<repo path> b/<repo path>, applies with `git apply`
or `patch -p1` at the repository root), patch/files/<repo path> (candidate bytes), and patch/GUARD.json
(baseline and candidate sha256 of every changed file). apply_guarded.py uses GUARD.json.
"""
import difflib
import hashlib
import json
import os
import shutil

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.abspath(os.path.join(LANE, '..', '..', '..', '..'))
OWNED = ['compiler/quantum-holography-status/status.py', 'compiler/quantum-holography-status/status.css',
         'compiler/quantum-holography-status/status-print.css', 'content/quantum-holography-status/page.json']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    base = {f['path']: f['sha256'] for f in json.load(open(os.path.join(LANE, 'BASELINE.json')))['files']}
    out = os.path.join(LANE, 'patch')
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(os.path.join(out, 'files'))
    guard = {'repo_root_marker': 'compiler/build-quantum-holography-status.py', 'files': []}
    diff = []
    for path in OWNED:
        old = open(os.path.join(LANE, 'baseline', 'src', path), 'rb').read()
        new = open(os.path.join(REPO, path), 'rb').read()
        assert sha(old) == base[path], f'baseline snapshot of {path} does not match BASELINE.json'
        if old == new:
            continue
        dst = os.path.join(out, 'files', path)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, 'wb').write(new)
        guard['files'].append({'path': path, 'baseline_sha256': sha(old), 'candidate_sha256': sha(new),
                               'baseline_bytes': len(old), 'candidate_bytes': len(new)})
        a = old.decode('utf-8').splitlines(keepends=True)
        b = new.decode('utf-8').splitlines(keepends=True)
        diff.append(f'diff --git a/{path} b/{path}\n')
        diff.extend(difflib.unified_diff(a, b, f'a/{path}', f'b/{path}', n=3))
    text = ''.join(diff)
    open(os.path.join(out, 'foundation.patch'), 'w', encoding='utf-8').write(text)
    guard['patch_sha256'] = sha(text.encode('utf-8'))
    json.dump(guard, open(os.path.join(out, 'GUARD.json'), 'w'), indent=1)
    shutil.copy(os.path.join(LANE, 'tools', 'apply_guarded.py'), os.path.join(out, 'apply_guarded.py'))
    for f in guard['files']:
        print(f['path'], f['baseline_sha256'][:16], '->', f['candidate_sha256'][:16])
    print('patch', guard['patch_sha256'][:16], len(text.encode('utf-8')), 'bytes')


if __name__ == '__main__':
    main()
