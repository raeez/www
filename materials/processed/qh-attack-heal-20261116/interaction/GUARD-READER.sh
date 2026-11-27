#!/bin/sh
# Guarded installation of the interaction lane's reader handoff v1 into a tree (run by root only):
#   sh GUARD-READER.sh <tree>            install
#   sh GUARD-READER.sh <tree> --check    check the preconditions only
# It installs exactly these files of reader-v1/ and touches nothing else:
#   compiler/quantum-holography-status/reader.js                       (new, or replaces an earlier copy of this lane's reader)
#   compiler/quantum-holography-status/status.js                       (reader mode; replaces the baseline or a frozen candidate)
#   compiler/quantum-holography-status/tests/reader.test.cjs           (new, or replaces an earlier copy)
#   compiler/quantum-holography-status/tests/fixtures/reader-book.json (new, or replaces an earlier copy)
#   compiler/quantum-holography-status/tests/interaction.test.cjs      (the r4 tests, which status.js in reader mode passes)
# Required beside it, and not installed here (the foundation's files):
#   - the page runs status.js BEFORE reader.js (reader.with_status_js=true);
#   - reader/monograph-css-required.css is appended to the foundation's monograph.css.
# Review status (REVIEW-STATUS.md): reader.js and the status.js reader mode are lead-verified only; no independent review
# under the hold.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
T=${1:?usage: GUARD-READER.sh <tree> [--check]}
CHECK=
[ "${2:-}" = --check ] && CHECK=1
SRC=$HERE/reader-v1
sum() { shasum -a 256 "$1" | cut -c1-64; }
READER=9134091e3c9474799bb60ba487573f29cdb128f5fa4ca0381086d22db11d14ea
STATUS=70c0663ab5bc95f67aa79bf7cb989e3d1d34ac2332d52a603349376dc003d8d5
RTESTS=e4ab08fdecec54c5d870d1138d267f581dfbfa32caf296eccc7fc5a39c49eb8e
RBOOK=17b70de70e7ee5cf757dcce76a4109f61c519bf01b413c23137ff6a21661c659
ITESTS=8a92a7a42d023168bbbb45b6d6ad65d36389254461bbc267e5aa442d4967b279
echo "reader-v1: reader.js and the status.js reader mode have no independent review (REVIEW-STATUS.md)"
[ "$(sum "$SRC/reader.js")" = "$READER" ] || { echo "the frozen reader.js does not match its pin"; exit 1; }
[ "$(sum "$SRC/status.js")" = "$STATUS" ] || { echo "the frozen status.js does not match its pin"; exit 1; }
[ "$(sum "$SRC/reader.test.cjs")" = "$RTESTS" ] || { echo "the frozen reader tests do not match their pin"; exit 1; }
[ "$(sum "$SRC/reader-book.json")" = "$RBOOK" ] || { echo "the frozen test book does not match its pin"; exit 1; }
[ "$(sum "$SRC/interaction.test.cjs")" = "$ITESTS" ] || { echo "the frozen interaction tests do not match their pin"; exit 1; }
D=$T/compiler/quantum-holography-status
[ -d "$D" ] || { echo "no compiler/quantum-holography-status in the tree ($D)"; exit 1; }
# status.js: the review baseline, candidate-final, candidate-r4 or this handoff's
case "$(sum "$D/status.js")" in
  ef3581907e176897da4a644f61038c147295fae8256cf8ba9a930bd5ab95e12e|3d0634285158fe5ebd42b510d045e5635cf0e14daae2c97c1385432c9c2df3d4|ddc7df31aae27343a5f5114f35f0d5a7f4ca4096682a74b77ef566be0ceb78bf|$STATUS) ;;
  *) echo "status.js in the tree is neither the baseline nor a frozen candidate of this lane: merge by hand"; exit 1 ;;
esac
# reader.js and the reader tests: absent, or an earlier copy of this lane's file (identified by its opening line)
first() { head -c 200 "$1" | tr -d '\n'; }
if [ -e "$D/reader.js" ]; then
  case "$(first "$D/reader.js")" in "/* The reader of the monograph."*) ;; *) echo "a different reader.js exists: merge by hand"; exit 1 ;; esac
fi
if [ -e "$D/tests/reader.test.cjs" ]; then
  case "$(first "$D/tests/reader.test.cjs")" in "#!/usr/bin/env node/* Reading-flow tests for the monograph reader"*) ;; *) echo "a different tests/reader.test.cjs exists: merge by hand"; exit 1 ;; esac
fi
if [ -e "$D/tests/interaction.test.cjs" ]; then
  case "$(sum "$D/tests/interaction.test.cjs")" in 794ea4dbd43407728c36d16ae58f60e4a9bd9bd1f8ef2cc112197690183f386c|$ITESTS) ;; *) echo "a different tests/interaction.test.cjs exists: merge by hand"; exit 1 ;; esac
fi
[ -n "$CHECK" ] && { echo "preconditions hold"; exit 0; }
for f in "$D/status.js" "$D/reader.js" "$D/tests/reader.test.cjs" "$D/tests/interaction.test.cjs" "$D/tests/fixtures/reader-book.json"; do
  [ ! -e "$f" ] || [ -w "$f" ] || { echo "not writable: $f"; exit 1; }
done
mkdir -p "$D/tests/fixtures"
cp "$SRC/reader.js" "$D/reader.js"
cp "$SRC/status.js" "$D/status.js"
cp "$SRC/reader.test.cjs" "$D/tests/reader.test.cjs"
cp "$SRC/reader-book.json" "$D/tests/fixtures/reader-book.json"
cp "$SRC/interaction.test.cjs" "$D/tests/interaction.test.cjs"
[ "$(sum "$D/reader.js")" = "$READER" ] && [ "$(sum "$D/status.js")" = "$STATUS" ] && [ "$(sum "$D/tests/reader.test.cjs")" = "$RTESTS" ] &&
  [ "$(sum "$D/tests/fixtures/reader-book.json")" = "$RBOOK" ] && [ "$(sum "$D/tests/interaction.test.cjs")" = "$ITESTS" ] &&
  echo "installed reader-v1: reader.js $READER, status.js $STATUS"
