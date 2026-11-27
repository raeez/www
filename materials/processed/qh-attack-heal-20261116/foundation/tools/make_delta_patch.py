#!/usr/bin/env python3
"""Make a guarded delta patch between two states of the lane's four owned files.

    python3 tools/make_delta_patch.py <from-dir> <to-dir> <out-dir> [<label>]

<from-dir> and <to-dir> are repository-shaped folders (compiler/quantum-holography-status/..., content/...),
for example patch/files (the integrated state) and the repository root. Writes <out-dir>/<label>.patch (unified
diff, applies with `patch -p1` at the repository root), <out-dir>/files/<repo path> (the new bytes),
<out-dir>/GUARD.json (from and to sha256 of every changed file) and <out-dir>/apply_guarded.py.
"""
import difflib
import hashlib
import json
import os
import shutil
import sys

OWNED = ['compiler/quantum-holography-status/status.py', 'compiler/quantum-holography-status/status.css',
         'compiler/quantum-holography-status/status-print.css', 'content/quantum-holography-status/page.json']
HERE = os.path.dirname(os.path.abspath(__file__))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    src, dst, out = (os.path.abspath(a) for a in sys.argv[1:4])
    label = sys.argv[4] if len(sys.argv) > 4 else 'delta'
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(os.path.join(out, 'files'))
    guard = {'repo_root_marker': 'compiler/build-quantum-holography-status.py', 'from': src, 'files': []}
    diff = []
    for path in OWNED:
        old = open(os.path.join(src, path), 'rb').read()
        new = open(os.path.join(dst, path), 'rb').read()
        if old == new:
            continue
        target = os.path.join(out, 'files', path)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        open(target, 'wb').write(new)
        guard['files'].append({'path': path, 'baseline_sha256': sha(old), 'candidate_sha256': sha(new),
                               'baseline_bytes': len(old), 'candidate_bytes': len(new)})
        a = old.decode('utf-8').splitlines(keepends=True)
        b = new.decode('utf-8').splitlines(keepends=True)
        diff.append(f'diff --git a/{path} b/{path}\n')
        diff.extend(difflib.unified_diff(a, b, f'a/{path}', f'b/{path}', n=3))
    text = ''.join(diff)
    open(os.path.join(out, f'{label}.patch'), 'w', encoding='utf-8').write(text)
    guard['patch'] = f'{label}.patch'
    guard['patch_sha256'] = sha(text.encode('utf-8'))
    json.dump(guard, open(os.path.join(out, 'GUARD.json'), 'w'), indent=1)
    shutil.copy(os.path.join(HERE, 'apply_guarded.py'), os.path.join(out, 'apply_guarded.py'))
    for f in guard['files']:
        print(f['path'], f['baseline_sha256'][:16], '->', f['candidate_sha256'][:16])
    print('patch', guard['patch_sha256'][:16], len(text.encode('utf-8')), 'bytes')


if __name__ == '__main__':
    main()
