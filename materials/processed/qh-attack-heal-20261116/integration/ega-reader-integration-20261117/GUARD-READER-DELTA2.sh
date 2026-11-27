#!/bin/sh
# Guarded installation of the interaction lane's delta 2 (the reference in companion pages) on top of reader-v1
# (run by root only):
#   sh GUARD-READER-DELTA2.sh <tree>            install
#   sh GUARD-READER-DELTA2.sh <tree> --check    check the preconditions only
# It installs exactly these files of reader-delta2/ and touches nothing else:
#   compiler/quantum-holography-status/reader.js               (replaces reader-v1's)
#   compiler/quantum-holography-status/tests/reader.test.cjs   (replaces reader-v1's)
# status.js and the test book are reader-v1's, unchanged. The splitter, the index tool and the checks run from
# reader-delta2/tools/ after the build (reader/DEFERRED-REFERENCE.md §7).
# Review status: lead-verified only; no independent review under the hold.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
T=${1:?usage: GUARD-READER-DELTA2.sh <tree> [--check]}
CHECK=
[ "${2:-}" = --check ] && CHECK=1
SRC=$HERE/reader-delta2
sum() { shasum -a 256 "$1" | cut -c1-64; }
READER=826542e53b77bf06d023ec0e21b6c5a150faf224884ea7ca615194a03c4acb61
RTESTS=c02d306025f0d5a9330f9ffaaf900deed189057437052763e19b42d6ccc254a6
V1_READER=9134091e3c9474799bb60ba487573f29cdb128f5fa4ca0381086d22db11d14ea
V1_RTESTS=e4ab08fdecec54c5d870d1138d267f581dfbfa32caf296eccc7fc5a39c49eb8e
V1_STATUS=70c0663ab5bc95f67aa79bf7cb989e3d1d34ac2332d52a603349376dc003d8d5
V1_RBOOK=17b70de70e7ee5cf757dcce76a4109f61c519bf01b413c23137ff6a21661c659
echo "reader-delta2: lead-verified only; no independent review (REVIEW-STATUS.md)"
[ "$(sum "$SRC/reader.js")" = "$READER" ] || { echo "the frozen reader.js does not match its pin"; exit 1; }
[ "$(sum "$SRC/reader.test.cjs")" = "$RTESTS" ] || { echo "the frozen reader tests do not match their pin"; exit 1; }
D=$T/compiler/quantum-holography-status
[ -d "$D" ] || { echo "no compiler/quantum-holography-status in the tree ($D)"; exit 1; }
[ -f "$D/status.js" ] && [ "$(sum "$D/status.js")" = "$V1_STATUS" ] || { echo "status.js is not reader-v1's: install reader-v1 first (GUARD-READER.sh)"; exit 1; }
[ -f "$D/tests/fixtures/reader-book.json" ] && [ "$(sum "$D/tests/fixtures/reader-book.json")" = "$V1_RBOOK" ] || { echo "the test book is not reader-v1's: install reader-v1 first"; exit 1; }
case "$(sum "$D/reader.js")" in "$V1_READER"|"$READER") ;; *) echo "reader.js in the tree is neither reader-v1's nor delta 2's: merge by hand"; exit 1 ;; esac
case "$(sum "$D/tests/reader.test.cjs")" in "$V1_RTESTS"|"$RTESTS") ;; *) echo "tests/reader.test.cjs is neither reader-v1's nor delta 2's: merge by hand"; exit 1 ;; esac
[ -n "$CHECK" ] && { echo "preconditions hold"; exit 0; }
# The two files were checked above to be reader-v1's (installed read-only from its frozen folder) or this delta's:
# they are made writable, replaced, and left writable.
chmod u+w "$D/reader.js" "$D/tests/reader.test.cjs"
cp "$SRC/reader.js" "$D/reader.js"
cp "$SRC/reader.test.cjs" "$D/tests/reader.test.cjs"
chmod u+w "$D/reader.js" "$D/tests/reader.test.cjs"
[ "$(sum "$D/reader.js")" = "$READER" ] && [ "$(sum "$D/tests/reader.test.cjs")" = "$RTESTS" ] && echo "installed reader-delta2: reader.js $READER"
