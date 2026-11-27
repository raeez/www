#!/bin/sh
# Applies QUALITY-ON-F1F2.diff to a tree that holds the foundation's final F1+F2 bytes (MANIFEST.json before-hashes):
# status.py, status.css, status-print.css (F2 candidates) and audit.py (the quality audit root integrated).
# Usage: apply.sh <repository root>. Refuses (exit 2) on any before-hash mismatch or a patch that does not apply
# cleanly; checks every after-hash once applied (exit 3).
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$1" && pwd)
check() {
python3 -I - "$HERE/MANIFEST.json" "$ROOT" "$1" <<'PY'
import hashlib, json, sys
m = json.load(open(sys.argv[1])); root, when = sys.argv[2], sys.argv[3]
bad = 0
for f in m['files']:
    h = hashlib.sha256(open(f"{root}/{f['path']}", 'rb').read()).hexdigest()
    want = f['before_sha256'] if when == 'before' else f['after_sha256']
    if h != want:
        print(f'{when}-hash mismatch: {f["path"]} ({h[:12]}, expected {want[:12]})'); bad = 1
    elif when == 'after':
        print('ok  ' + f['path'])
sys.exit(bad)
PY
}
check before || exit 2
( cd "$ROOT" && patch -p1 --dry-run --quiet < "$HERE/QUALITY-ON-F1F2.diff" ) || { echo "patch does not apply cleanly"; exit 2; }
( cd "$ROOT" && patch -p1 --quiet --no-backup-if-mismatch < "$HERE/QUALITY-ON-F1F2.diff" )
check after || exit 3
echo "applied QUALITY-ON-F1F2.diff"
