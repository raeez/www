#!/bin/sh
# Applies the quality lane's integration patches to root's integration tree, only if every target file is the
# integrated version this lane composed against (INTEGRATION-MANIFEST.json before-hashes).
# Usage: apply-integration.sh <repository root> [remaining|language|all]   (default: all)
#   remaining  QUALITY-REMAINING.diff  status.py, status.css, status-print.css, audit.py
#   language   STATUS-LANGUAGE.diff    page.json (status labels by stored code; separate, inspectable)
# Refuses (exit 2) on any before-hash mismatch or a patch that does not apply cleanly; checks every after-hash once
# applied (exit 3 on mismatch).
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$1" && pwd)
PART=${2:-all}
case "$PART" in remaining) LIST="QUALITY-REMAINING.diff" ;; language) LIST="STATUS-LANGUAGE.diff" ;;
  all) LIST="QUALITY-REMAINING.diff STATUS-LANGUAGE.diff" ;; *) echo "unknown part $PART"; exit 1 ;; esac
check() {
python3 -I - "$HERE/INTEGRATION-MANIFEST.json" "$ROOT" "$1" "$2" <<'PY'
import hashlib, json, sys
m = json.load(open(sys.argv[1])); root, patches, when = sys.argv[2], sys.argv[3].split(), sys.argv[4]
bad = 0
for f in m['files']:
    if f['patch'] not in patches:
        continue
    h = hashlib.sha256(open(f"{root}/{f['path']}", 'rb').read()).hexdigest()
    want = f['before_sha256'] if when == 'before' else f['after_sha256']
    if h != want:
        print(f'{when}-hash mismatch: {f["path"]} ({h[:12]}, expected {want[:12]})'); bad = 1
    elif when == 'after':
        print('ok  ' + f['path'])
sys.exit(bad)
PY
}
check "$LIST" before || exit 2
for p in $LIST; do ( cd "$ROOT" && patch -p1 --dry-run --quiet < "$HERE/patches/$p" ) || { echo "$p does not apply cleanly"; exit 2; }; done
for p in $LIST; do ( cd "$ROOT" && patch -p1 --quiet --no-backup-if-mismatch < "$HERE/patches/$p" ); done
check "$LIST" after || exit 3
echo "applied $PART"
