#!/usr/bin/env python3
"""Build the page as it will be after the status.py patch, without editing the shared sources.

    python3 build_candidate.py <out dir> [--atlas <atlas.json>] [--no-fonts]

A candidate tree is made in this folder: the compiler and content files are symbolic links to the
worktree's files, except status.py, which is the guarded patch applied to the worktree's status.py.
With --atlas the file is placed in the candidate content folder as atlas.json. The builder then runs
from the candidate tree; the page and the audit go to <out dir>.
"""
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
WT = LANE.parents[3]
PY = '/tmp/qh-tracker-build-20261116-venv/bin/python'
COMPILER = WT / 'compiler'
CONTENT = WT / 'content' / 'quantum-holography-status'


def link(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.is_symlink() or dst.exists():
        dst.unlink()
    dst.symlink_to(src)


def main(argv):
    out = Path(argv[1]).resolve()
    atlas = Path(argv[argv.index('--atlas') + 1]).resolve() if '--atlas' in argv else None
    tree = LANE / 'candidate'
    if tree.exists():
        shutil.rmtree(tree)  # the candidate tree holds only links and the patched copy made here
    status_dir = tree / 'compiler' / 'quantum-holography-status'
    for f in sorted((COMPILER / 'quantum-holography-status').iterdir()):
        if f.is_file() and f.name != 'status.py':
            link(f, status_dir / f.name)
    rc = subprocess.run([PY, '-B', str(LANE / 'integration' / 'apply_status_patch.py'), '--emit',
                         str(COMPILER / 'quantum-holography-status' / 'status.py'), str(status_dir / 'status.py')]).returncode
    if rc:
        return rc
    link(COMPILER / 'build-quantum-holography-status.py', tree / 'compiler' / 'build-quantum-holography-status.py')
    link(COMPILER / 'quantum-holography-tracker', tree / 'compiler' / 'quantum-holography-tracker')
    content = tree / 'content' / 'quantum-holography-status'
    for name in ('content.json', 'essay.md', 'page.json', 'README.md'):
        link(CONTENT / name, content / name)
    if atlas:
        shutil.copyfile(atlas, content / 'atlas.json')
    out.mkdir(parents=True, exist_ok=True)
    # The builder resolves its own root from its path; run the candidate's copy by its candidate path.
    builder = tree / 'compiler' / 'build-quantum-holography-status.py'
    script = builder.read_text(encoding='utf-8')
    runner = tree / 'compiler' / 'build-candidate-runner.py'
    runner.write_text(script, encoding='utf-8')
    cmd = [PY, '-B', str(runner), '--output', str(out / 'preview.html'), '--audit-dir', str(out / 'audit')]
    if '--no-fonts' in argv:
        cmd.append('--no-fonts')
    return subprocess.run(cmd).returncode


if __name__ == '__main__':
    sys.exit(main(sys.argv))
