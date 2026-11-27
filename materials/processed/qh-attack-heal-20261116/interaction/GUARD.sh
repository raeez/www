#!/bin/sh
# Guarded application of the interaction lane's change to an integration tree (run by root only).
#   sh GUARD.sh <tree>                    install candidate-r4
#   sh GUARD.sh <tree> --reviewed         install candidate-final instead
#   add --check to either to check the preconditions only
# It installs exactly two files and touches nothing else:
#   compiler/quantum-holography-status/status.js                    (replaces the tree's file)
#   compiler/quantum-holography-status/tests/interaction.test.cjs   (new, or replaces a version from this lane)
# The foundation's CSS and status.py proposals are separate (proposals/STATUS-PY.md) and are not applied here.
#
# Review status (REVIEW-STATUS.md): candidate-final is the last revision with an independent review, which left two
# severity 3 items open (C4-A-01 = C4-B-02, C4-B-01: only where a part holds text no known unit holds). candidate-r4
# heals them; its changes since candidate-final have NO independent review (the review is queued, not launched).
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
T=${1:?usage: GUARD.sh <tree> [--reviewed] [--check]}
shift
CHECK=
WHICH=r4
for a in "$@"; do
  case "$a" in
    --check) CHECK=1 ;;
    --reviewed) WHICH=final ;;
    *) echo "unknown option $a"; exit 2 ;;
  esac
done
BASE_JS=ef3581907e176897da4a644f61038c147295fae8256cf8ba9a930bd5ab95e12e
FINAL_JS=3d0634285158fe5ebd42b510d045e5635cf0e14daae2c97c1385432c9c2df3d4
FINAL_TEST=794ea4dbd43407728c36d16ae58f60e4a9bd9bd1f8ef2cc112197690183f386c
R4_JS=ddc7df31aae27343a5f5114f35f0d5a7f4ca4096682a74b77ef566be0ceb78bf
R4_TEST=8a92a7a42d023168bbbb45b6d6ad65d36389254461bbc267e5aa442d4967b279
if [ "$WHICH" = r4 ]; then
  SRC=$HERE/candidate-r4; JS_AFTER=$R4_JS; TEST_AFTER=$R4_TEST
  echo "candidate-r4: its changes since candidate-final have no independent review (REVIEW-STATUS.md)"
else
  SRC=$HERE/candidate-final; JS_AFTER=$FINAL_JS; TEST_AFTER=$FINAL_TEST
  echo "candidate-final: independently reviewed; two severity 3 items open (REVIEW-STATUS.md)"
fi
sum() { shasum -a 256 "$1" | cut -c1-64; }
[ "$(sum "$SRC/status.js")" = "$JS_AFTER" ] || { echo "the frozen status.js does not match its pin"; exit 1; }
[ "$(sum "$SRC/interaction.test.cjs")" = "$TEST_AFTER" ] || { echo "the frozen test file does not match its pin"; exit 1; }
JS=$T/compiler/quantum-holography-status/status.js
TEST=$T/compiler/quantum-holography-status/tests/interaction.test.cjs
[ -f "$JS" ] || { echo "no status.js in the tree ($JS)"; exit 1; }
HAVE=$(sum "$JS")
case "$HAVE" in
  "$JS_AFTER") echo "status.js already installed" ;;
  "$BASE_JS"|"$FINAL_JS"|"$R4_JS") ;;
  *) echo "status.js in the tree is neither the baseline nor a frozen candidate of this lane ($HAVE): merge by hand"; exit 1 ;;
esac
if [ -e "$TEST" ]; then
  case "$(sum "$TEST")" in
    "$FINAL_TEST"|"$R4_TEST") ;;
    *) echo "a different tests/interaction.test.cjs exists: merge by hand"; exit 1 ;;
  esac
fi
[ -n "$CHECK" ] && { echo "preconditions hold"; exit 0; }
[ -w "$JS" ] || { echo "status.js in the tree is not writable ($JS)"; exit 1; }
mkdir -p "$(dirname "$TEST")"
[ ! -e "$TEST" ] || [ -w "$TEST" ] || { echo "the tree's test file is not writable ($TEST)"; exit 1; }
cp "$SRC/status.js" "$JS"
cp "$SRC/interaction.test.cjs" "$TEST"
[ "$(sum "$JS")" = "$JS_AFTER" ] && [ "$(sum "$TEST")" = "$TEST_AFTER" ] && echo "installed: status.js $JS_AFTER, tests $TEST_AFTER"
