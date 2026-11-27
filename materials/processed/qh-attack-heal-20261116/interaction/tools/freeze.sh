#!/bin/sh
# Freeze the lane's current candidate into <lane>/<name>/ (read-only), from the worktree root:
#   sh materials/processed/qh-attack-heal-20261116/interaction/tools/freeze.sh <name> [<previous frozen name>]
# Copies status.js, the reader-task tests, the five verified builds (verify/*.html), the proposals, the contract, the
# consolidated ledger, the QA disposition and the check tools; writes the diff against the baseline (and against the
# previous frozen candidate when named) and SHA256SUMS. Refuses when a build does not carry this status.js verbatim.
set -eu
L=materials/processed/qh-attack-heal-20261116/interaction
N=${1:?usage: freeze.sh <name> [<previous>]}
D=$L/$N
[ -e "$D" ] && { echo "$D exists"; exit 1; }
JS=compiler/quantum-holography-status/status.js
TESTS=compiler/quantum-holography-status/tests/interaction.test.cjs
for V in standalone integration integration-css integration-atlas integration-py; do
  python3 -I - "$JS" "$L/verify/$V.html" <<'EOF' || { echo "verify/$V.html does not carry this status.js"; exit 1; }
import re, sys
js = open(sys.argv[1], encoding='utf-8').read().strip()
page = open(sys.argv[2], encoding='utf-8').read()
sys.exit(0 if any(s.strip() == js for s in re.findall(r'<script>(.*?)</script>', page, re.S)) else 1)
EOF
done
mkdir -p "$D/builds" "$D/proposals" "$D/tools"
cp "$JS" "$TESTS" "$D/"
for V in standalone integration integration-css integration-atlas integration-py; do cp "$L/verify/$V.html" "$D/builds/"; done
cp "$L"/proposals/*.patch "$L"/proposals/*.css "$L/proposals/STATUS-PY.md" "$D/proposals/"
cp "$L/CONTRACT.json" "$L/attack/CONSOLIDATED.yaml" "$D/"
[ -f "$L/QA-DISPOSITION.md" ] && cp "$L/QA-DISPOSITION.md" "$D/"
[ -f "$L/REVIEW-STATUS.md" ] && cp "$L/REVIEW-STATUS.md" "$D/"
cp "$L/tools/content-check.cjs" "$L/tools/integration-check.sh" "$L/tools/fidelity.py" "$L/tools/served-ids.cjs" "$L/tools/jsdom-cost.cjs" "$L/tools/status-labels.cjs" "$D/tools/"
diff -u --label a/$JS --label b/$JS "$L/baseline-src/status.js" "$JS" > "$D/status.js.diff" || true
if [ -n "${2:-}" ]; then
  diff -u --label "a/$JS ($2)" --label "b/$JS ($N)" "$L/$2/status.js" "$JS" > "$D/status.js-$2-to-$N.diff" || true
  diff -u --label "a/tests ($2)" --label "b/tests ($N)" "$L/$2/interaction.test.cjs" "$TESTS" > "$D/tests-$2-to-$N.diff" || true
fi
(cd "$D" && find . -type f ! -name SHA256SUMS | sort | xargs shasum -a 256 > SHA256SUMS)
chmod -R a-w "$D"
echo "frozen $D"
grep -E ' \./(status\.js|interaction\.test\.cjs)$' "$D/SHA256SUMS"
