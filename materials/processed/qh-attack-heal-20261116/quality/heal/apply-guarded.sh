#!/bin/sh
# Applies the quality lane's heal patch to a tracker tree, only if every target file is byte-identical to the
# baseline. Usage: apply-guarded.sh <repository root> [foundation|interaction|all]   (default: all)
# Refuses (exit 2) on any before-hash mismatch; checks every after-hash once applied (exit 3 on mismatch).
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$1" && pwd)
PART=${2:-all}
case "$PART" in foundation|interaction) PATCH="$HERE/patches/$PART.diff" ;; all) PATCH="$HERE/PATCH.diff" ;; *) echo "unknown part $PART"; exit 1 ;; esac
python3 -I - "$HERE/MANIFEST.json" "$ROOT" "$PART" before <<'PY' || exit 2
import hashlib, json, sys
m = json.load(open(sys.argv[1])); root, part = sys.argv[2], sys.argv[3]
bad = 0
for f in m['files']:
    if not f['changed'] or (part != 'all' and f['owner'] != part):
        continue
    h = hashlib.sha256(open(f"{root}/{f['path']}", 'rb').read()).hexdigest()
    if h != f['before_sha256']:
        print('before-hash mismatch:', f['path']); bad = 1
sys.exit(bad)
PY
( cd "$ROOT" && patch -p1 --dry-run --quiet < "$PATCH" ) || { echo "patch does not apply cleanly"; exit 2; }
( cd "$ROOT" && patch -p1 --quiet --no-backup-if-mismatch < "$PATCH" )
python3 -I - "$HERE/MANIFEST.json" "$ROOT" "$PART" after <<'PY' || exit 3
import hashlib, json, sys
m = json.load(open(sys.argv[1])); root, part = sys.argv[2], sys.argv[3]
bad = 0
for f in m['files']:
    if not f['changed'] or (part != 'all' and f['owner'] != part):
        continue
    h = hashlib.sha256(open(f"{root}/{f['path']}", 'rb').read()).hexdigest()
    print(('ok  ' if h == f['after_sha256'] else 'BAD ') + f['path']); bad |= h != f['after_sha256']
sys.exit(bad)
PY
echo "applied $PART"
