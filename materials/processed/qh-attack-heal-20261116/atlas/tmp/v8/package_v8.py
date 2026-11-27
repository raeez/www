"""Packages the v8 repair: a unified patch from integration's installed files to this worktree's files, and the
before/after/same hash table the guard reads. Run from the worktree root:
    python3 package_v8.py <integration root> <out folder>"""
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

S = 'compiler/quantum-holography-status'
TOUCHED = [f'{S}/{f}' for f in ('figures.py', 'figures.css', 'figures.js', 'atlas.py', 'atlas.css', 'atlas.js',
                                'tests/test_figures.py', 'tests/figures.test.cjs', 'tests/test_atlas.py', 'tests/atlas.test.cjs')]
SAME = [f'{S}/{f}' for f in ('tests/figures_page.py', 'tests/fixtures/figures-synthetic.json', 'tests/fixtures/atlas-synthetic.json')]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(integ, out):
    integ, out = Path(integ), Path(out)
    out.mkdir(parents=True, exist_ok=True)
    rows, diffs = [], []
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for p in TOUCHED:
            before, after = integ / p, Path(p)
            if before.read_bytes() == after.read_bytes():
                sys.exit(f'{p} is unchanged: not a touched file')
            for side, src in (('a', before), ('b', after)):
                dst = tmp / side / p
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(src.read_bytes())
            rows.append(f'before {sha(before)} {before.stat().st_size} {p}')
            rows.append(f'after {sha(after)} {after.stat().st_size} {p}')
            d = subprocess.run(['git', 'diff', '--no-index', '--binary', '--', f'a/{p}', f'b/{p}'], cwd=tmp,
                               capture_output=True, text=True)
            if d.returncode not in (0, 1):
                sys.exit(d.stderr)
            diffs.append(d.stdout.replace(f'a/a/{p}', f'a/{p}').replace(f'b/b/{p}', f'b/{p}'))
    for p in SAME:
        if (integ / p).read_bytes() != Path(p).read_bytes():
            sys.exit(f'{p} differs from integration but is listed as untouched')
        rows.append(f'same {sha(p)} {Path(p).stat().st_size} {p}')
    (out / 'atlas-v8-repair.patch').write_text(''.join(diffs), encoding='utf-8')
    (out / 'hashes.txt').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    print(f'{len(TOUCHED)} files in the patch, {len(SAME)} guarded as untouched')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
