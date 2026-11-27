#!/bin/sh
# Guarded installation of reader-delta3 (the search's presentation on narrow screens) over reader-delta2a:
#   sh GUARD-READER-DELTA3.sh <tree>            install
#   sh GUARD-READER-DELTA3.sh <tree> --check    check the preconditions only
# It replaces exactly two files, each only if it is the previous frozen one or this delta's:
#   compiler/quantum-holography-status/reader.js               (reader-delta2a 9ed283cc...)
#   compiler/quantum-holography-status/tests/reader.test.cjs   (reader-delta2 c02d3060...)
# After installing, rebuild the companion index with this reader (reader/DEFERRED-REFERENCE.md section 7).
# Review status: lead-verified only; no independent review.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
T=${1:?usage: GUARD-READER-DELTA3.sh <tree> [--check]}
CHECK=
[ "${2:-}" = --check ] && CHECK=1
SRC=$HERE/reader-delta3
sum() { shasum -a 256 "$1" | cut -c1-64; }
READER=40ed4eb4fa623bb765c5e2b5249e0445969742b03614e878fb626462a810a0c9
RTESTS=708ef3dd098fb7fe7845456ff9c46f8fbeabdac445ba616ab4528d2005aceac9
PREV_READER=9ed283cc50fe1f36f7fff0c6e7d664c58d2df6bd867563356a40295c1e059eed
PREV_RTESTS=c02d306025f0d5a9330f9ffaaf900deed189057437052763e19b42d6ccc254a6
V1_STATUS=70c0663ab5bc95f67aa79bf7cb989e3d1d34ac2332d52a603349376dc003d8d5
echo "reader-delta3: lead-verified only; no independent review (REVIEW-STATUS.md)"
[ "$(sum "$SRC/reader.js")" = "$READER" ] || { echo "the frozen reader.js does not match its pin"; exit 1; }
[ "$(sum "$SRC/reader.test.cjs")" = "$RTESTS" ] || { echo "the frozen reader tests do not match their pin"; exit 1; }
D=$T/compiler/quantum-holography-status
[ -d "$D" ] || { echo "no compiler/quantum-holography-status in the tree ($D)"; exit 1; }
[ -f "$D/status.js" ] && [ "$(sum "$D/status.js")" = "$V1_STATUS" ] || { echo "status.js is not reader-v1's"; exit 1; }
case "$(sum "$D/reader.js")" in "$PREV_READER"|"$READER") ;; *) echo "reader.js in the tree is neither reader-delta2a's nor delta3's: merge by hand"; exit 1 ;; esac
case "$(sum "$D/tests/reader.test.cjs")" in "$PREV_RTESTS"|"$RTESTS") ;; *) echo "tests/reader.test.cjs is neither reader-delta2's nor delta3's: merge by hand"; exit 1 ;; esac
[ -n "$CHECK" ] && { echo "preconditions hold"; exit 0; }
chmod u+w "$D/reader.js" "$D/tests/reader.test.cjs"
cp "$SRC/reader.js" "$D/reader.js"
cp "$SRC/reader.test.cjs" "$D/tests/reader.test.cjs"
chmod u+w "$D/reader.js" "$D/tests/reader.test.cjs"
[ "$(sum "$D/reader.js")" = "$READER" ] && [ "$(sum "$D/tests/reader.test.cjs")" = "$RTESTS" ] && echo "installed reader-delta3: reader.js $READER"
