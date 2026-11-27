#!/bin/sh
# Guarded installation of reader-delta5 (opening snippets) over reader-delta3:
#   sh GUARD-READER-DELTA3.sh <tree>            install
#   sh GUARD-READER-DELTA3.sh <tree> --check    check the preconditions only
# It replaces exactly two files, each only if it is the previous frozen one or this delta's:
#   compiler/quantum-holography-status/reader.js               (reader-delta3 40ed4eb4...)
#   compiler/quantum-holography-status/tests/reader.test.cjs   (reader-delta3 708ef3dd...)
# No index rebuild is needed (snippets are drawn when results are shown).
# Review status: lead-verified only; no independent review.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
T=${1:?usage: GUARD-READER-DELTA3.sh <tree> [--check]}
CHECK=
[ "${2:-}" = --check ] && CHECK=1
SRC=$HERE/reader-delta5
sum() { shasum -a 256 "$1" | cut -c1-64; }
READER=f3e45fbb616ae5b86aafa4e89e4e4dedba8eb519ec1ee490639fb92c06018c64
RTESTS=2535d0405a35e884673190b612ec7b8889c4c859cf7db0fc189e4b4bcbd6ac01
PREV_READER=40ed4eb4fa623bb765c5e2b5249e0445969742b03614e878fb626462a810a0c9
PREV_RTESTS=708ef3dd098fb7fe7845456ff9c46f8fbeabdac445ba616ab4528d2005aceac9
V1_STATUS=70c0663ab5bc95f67aa79bf7cb989e3d1d34ac2332d52a603349376dc003d8d5
echo "reader-delta5: lead-verified only; no independent review (REVIEW-STATUS.md)"
[ "$(sum "$SRC/reader.js")" = "$READER" ] || { echo "the frozen reader.js does not match its pin"; exit 1; }
[ "$(sum "$SRC/reader.test.cjs")" = "$RTESTS" ] || { echo "the frozen reader tests do not match their pin"; exit 1; }
D=$T/compiler/quantum-holography-status
[ -d "$D" ] || { echo "no compiler/quantum-holography-status in the tree ($D)"; exit 1; }
[ -f "$D/status.js" ] && [ "$(sum "$D/status.js")" = "$V1_STATUS" ] || { echo "status.js is not reader-v1's"; exit 1; }
case "$(sum "$D/reader.js")" in "$PREV_READER"|"$READER") ;; *) echo "reader.js in the tree is neither reader-delta3's nor delta5's: merge by hand"; exit 1 ;; esac
case "$(sum "$D/tests/reader.test.cjs")" in "$PREV_RTESTS"|"$RTESTS") ;; *) echo "tests/reader.test.cjs is neither reader-delta3's nor delta5's: merge by hand"; exit 1 ;; esac
[ -n "$CHECK" ] && { echo "preconditions hold"; exit 0; }
chmod u+w "$D/reader.js" "$D/tests/reader.test.cjs"
cp "$SRC/reader.js" "$D/reader.js"
cp "$SRC/reader.test.cjs" "$D/tests/reader.test.cjs"
chmod u+w "$D/reader.js" "$D/tests/reader.test.cjs"
[ "$(sum "$D/reader.js")" = "$READER" ] && [ "$(sum "$D/tests/reader.test.cjs")" = "$RTESTS" ] && echo "installed reader-delta5: reader.js $READER"
