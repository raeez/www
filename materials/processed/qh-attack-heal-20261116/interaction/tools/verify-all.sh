#!/bin/sh
# Rebuild every variant this lane checks, from the worktree's current status.js, and run the audit, the fidelity checks
# and the reader-task tests on each. No browser is used. Run from the worktree root:
#   NODE_PATH=<node_modules with jsdom> sh materials/processed/qh-attack-heal-20261116/interaction/tools/verify-all.sh [fonts]
# With "fonts", the standalone build embeds the TeX Live fonts (the final check); otherwise all builds use --no-fonts.
set -u
PY=/tmp/qh-tracker-build-20261116-venv/bin/python
L=materials/processed/qh-attack-heal-20261116/interaction
LOG=$L/verify/verify-all.log
JS=compiler/quantum-holography-status/status.js
TESTS=compiler/quantum-holography-status/tests/interaction.test.cjs
mkdir -p $L/verify
: > $LOG
say() { echo "$*" | tee -a $LOG; }
node --check $JS || { say "status.js: syntax error"; exit 1; }
say "status.js sha256 $(shasum -a 256 $JS | cut -c1-64)"
say "tests     sha256 $(shasum -a 256 $TESTS | cut -c1-64)"
FONTS=--no-fonts
[ "${1:-}" = fonts ] && FONTS=
# 1 standalone: the worktree's own producer (baseline status.py, status.css, status-print.css) with this status.js
$PY -B compiler/build-quantum-holography-status.py $FONTS --output $L/verify/standalone.html --audit-dir $L/verify/audit-standalone >> $LOG 2>&1
say "standalone audit: $(tail -2 $L/verify/audit-standalone/audit.txt | head -1)"
# 2-4 the hashed snapshots of the other lanes' producer files, each with this status.js
for T in integration integration-css integration-atlas integration-py; do
  cp $JS $L/$T/compiler/quantum-holography-status/status.js
  $PY -B $L/$T/compiler/build-quantum-holography-status.py --no-fonts --output $L/verify/$T.html --audit-dir $L/verify/audit-$T >> $LOG 2>&1
  say "$T audit: $(tail -1 $L/verify/audit-$T/audit.txt)"
done
for V in standalone integration integration-css integration-atlas integration-py; do
  say "== $V fidelity: $(python3 -I $L/tools/fidelity.py --js $JS "$PWD" $L/baseline-build/baseline-nofonts.html $L/verify/$V.html $L/baseline-build/ids-origin-master.txt | tail -1)"
  node $L/tools/content-check.cjs $L/verify/$V.html --must $L/baseline-build/baseline-page-ids.txt --must $L/baseline-build/ids-origin-master.txt \
    --report $L/baseline-build/published-ids-union.txt --ranks $L/verify/content-ranks-$V.tsv > $L/verify/content-check-$V.txt 2>&1
  say "== $V content: $(tail -1 $L/verify/content-check-$V.txt) | $(grep -E '^INFO C5 (statement|scope|atlas)' $L/verify/content-check-$V.txt | sed 's/INFO C5 //' | tr '\n' ' ')"
  node $TESTS $L/verify/$V.html > $L/verify/tests-$V.txt 2>&1
  say "== $V tests: $(grep -E '^[0-9]+ tests' $L/verify/tests-$V.txt) $(grep -c '^FAIL' $L/verify/tests-$V.txt) failed"
  grep -A3 '^FAIL' $L/verify/tests-$V.txt | tee -a $LOG
done
say "done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
