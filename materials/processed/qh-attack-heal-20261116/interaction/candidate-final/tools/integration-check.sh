#!/bin/sh
# The interaction lane's checks on root's composed tree, for whatever content it carries (the final payload included).
#
#   NODE_PATH=<node_modules with jsdom> sh integration-check.sh <tree> <out-dir> [fonts]
#
# Reads <tree> only: its producer and content are copied to <out-dir>, built twice there (with the tree's status.js, and
# with the review baseline's status.js as the reference for the same content), and checked. Everything is written
# under <out-dir>. No browser is used, so nothing here says how the page looks; the jsdom timings are upper bounds.
#
#   I1 pins        which status.js, test file, CSS block and status.py proposals the tree carries (reported, not required)
#   I2 builds      both builds: audit result and TeX errors
#   I3 fidelity    reference against candidate, same content: statements, statuses, cells and tally as served; ids
#                  kept, in-page links, CSP, no network call or string code, no process or tool words in any inline script
#   I4 content     the candidate with its script running (tools/content-check.cjs): no script error; content as served;
#                  no duplicate id; every earlier address kept; links; search finds every statement, column scope and
#                  atlas unit by its own words (ranks in content-ranks.tsv); the atlas rendered (when the tree has one)
#   I5 served ids  the ids the producer serves equal the ids the script gives (tools/served-ids.cjs)
#   I6 tests       the lane's reader-task tests on the candidate
#   I7 cost        jsdom cost of the reference and the candidate (tools/jsdom-cost.cjs), three runs each
#   I8 labels      every place that names a status uses the same words for the same stored code (tools/status-labels.cjs;
#                  LABELS=<code-to-words.json> to check against a ruling, else against the page's own status key)
#
# ALLOW_REJECTED=1: when the build's audit refuses a page (its content fails the reader rules), the builder still writes it
# as audit-*/rejected.html; with this setting the checks go on with that page, for interaction only, and say so. The
# audit's findings stay failures for the content's owner.
set -u
LANE=$(cd "$(dirname "$0")/.." && pwd)
T=$(cd "${1:?usage: integration-check.sh <tree> <out-dir> [fonts]}" && pwd)
O=${2:?usage: integration-check.sh <tree> <out-dir> [fonts]}
mkdir -p "$O" && O=$(cd "$O" && pwd)
case "$O" in "$T"|"$T"/*) echo "the output folder must lie outside the tree"; exit 2;; esac
PY=${PY:-/tmp/qh-tracker-build-20261116-venv/bin/python}
FONTS=--no-fonts
[ "${3:-}" = fonts ] && FONTS=
P=compiler/quantum-holography-status
C=content/quantum-holography-status
LOG=$O/integration-check.log
: > "$LOG"
say() { echo "$*" | tee -a "$LOG"; }
sum() { shasum -a 256 "$1" | cut -c1-64; }
fail=0

say "== I1 pins (tree $T)"
JS=$T/$P/status.js
say "status.js $(sum "$JS")"
[ -f "$LANE/candidate-final/status.js" ] && say "  lane candidate $(sum "$LANE/candidate-final/status.js")$( [ "$(sum "$JS")" = "$(sum "$LANE/candidate-final/status.js")" ] && echo ' (the same)' || echo ' (different: the checks below test the tree'"'"'s file)')"
# The tests that belong to the tree's status.js: the tree's own, else those frozen with that status.js, else the live ones.
TESTS=$T/$P/tests/interaction.test.cjs
if [ ! -f "$TESTS" ]; then
  TESTS=$(cd "$LANE/../../../.." && pwd)/$P/tests/interaction.test.cjs
  for C in "$LANE"/candidate-final "$LANE"/candidate-r*; do
    [ -f "$C/status.js" ] && [ "$(sum "$C/status.js")" = "$(sum "$JS")" ] && { TESTS=$C/interaction.test.cjs; break; }
  done
fi
say "tests $TESTS $(sum "$TESTS")"
grep -q "States the script sets" "$T/$P/status.css" && say "status.css carries the CSS block" || say "status.css lacks the CSS block: the script's states are unstyled"
grep -q "screen-only" "$T/$P/status-print.css" && say "status-print.css carries the print block" || say "status-print.css lacks the print block"
for m in "def statement_id|P1 served statement ids" "data-needs-script hidden|P2 script-only controls served hidden" \
         "-scope\">|P3 mark descriptions" "def find_mount|P6 the search's place and words"; do
  pat=${m%%|*}; what=${m#*|}
  grep -qF -- "$pat" "$T/$P/status.py" && say "status.py has $what" || say "status.py lacks $what"
done

say "== I2 builds"
for V in candidate reference; do
  rm -rf "$O/tree-$V"
  mkdir -p "$O/tree-$V/compiler" "$O/tree-$V/content"
  cp "$T/compiler/build-quantum-holography-status.py" "$O/tree-$V/compiler/"
  cp -R "$T/$P" "$O/tree-$V/compiler/"
  [ -d "$T/compiler/quantum-holography-tracker" ] && cp -R "$T/compiler/quantum-holography-tracker" "$O/tree-$V/compiler/"
  cp -R "$T/$C" "$O/tree-$V/content/"
done
cp "$LANE/baseline-src/status.js" "$O/tree-reference/$P/status.js"
"$PY" -B "$O/tree-candidate/compiler/build-quantum-holography-status.py" $FONTS --output "$O/candidate.html" --audit-dir "$O/audit-candidate" >> "$LOG" 2>&1 || fail=1
"$PY" -B "$O/tree-reference/compiler/build-quantum-holography-status.py" --no-fonts --output "$O/reference.html" --audit-dir "$O/audit-reference" >> "$LOG" 2>&1 || fail=1
for V in candidate reference; do
  A=$O/audit-$V/audit.txt
  if [ -f "$A" ]; then say "$V: $(grep '^math' "$A" | head -1) | audit $(tail -1 "$A")"; else say "$V: no audit (build failed; see the log)"; fail=1; fi
done
for V in candidate reference; do
  if [ ! -f "$O/$V.html" ] && [ "${ALLOW_REJECTED:-}" = 1 ] && [ -f "$O/audit-$V/rejected.html" ]; then
    cp "$O/audit-$V/rejected.html" "$O/$V.html"
    say "$V: the audit refused this page; the checks below use it for interaction only (ALLOW_REJECTED=1)"
  fi
done
[ -f "$O/candidate.html" ] || { say "no candidate page: stop (ALLOW_REJECTED=1 continues with an audit-refused page)"; exit 1; }

say "== I3 fidelity (same content)"
python3 -I "$LANE/tools/fidelity.py" --same-content --js "$O/tree-candidate/$P/status.js" "$O/tree-candidate" "$O/reference.html" "$O/candidate.html" \
  "$LANE/baseline-build/ids-origin-master.txt" > "$O/fidelity.txt" 2>&1 || fail=1
grep -E '^(FAIL|SKIP)|^summary' "$O/fidelity.txt" | tee -a "$LOG"

say "== I4 content (script running)"
EXPECT=
[ -f "$T/$C/atlas.json" ] && EXPECT=--expect-atlas
node "$LANE/tools/content-check.cjs" "$O/candidate.html" --must "$LANE/baseline-build/baseline-page-ids.txt" \
  --must "$LANE/baseline-build/ids-origin-master.txt" --report "$LANE/baseline-build/published-ids-union.txt" $EXPECT \
  --ranks "$O/content-ranks.tsv" > "$O/content-check.txt" 2>&1 || fail=1
grep -E '^(FAIL|INFO)|^summary' "$O/content-check.txt" | tee -a "$LOG"

say "== I4b statements without a content id (content.json)"
python3 -I - "$T/$C/content.json" <<'PYEOF' | tee -a "$LOG"
import json, sys
c = json.load(open(sys.argv[1], encoding='utf-8'))
found = []
def walk(o, path):
    if isinstance(o, dict):
        if 'status' in o and 'text' in o and ('title' in o or 'id' in o):
            found.append((path, (o.get('id') or '').strip()))
        for k, v in o.items():
            walk(v, path + '/' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, path + '/' + str(i))
walk(c, '')
missing = [p for p, i in found if not i]
print(f'{len(found)} statements in content.json, {len(missing)} without an id' + (': ' + ', '.join(missing[:5]) if missing else ''))
PYEOF

say "== I5 served ids"
node "$LANE/tools/served-ids.cjs" "$O/candidate.html" "$O/candidate.html" 2>&1 | tee -a "$LOG"

say "== I6 reader-task tests"
node "$TESTS" "$O/candidate.html" > "$O/tests.txt" 2>&1 || fail=1
say "$(tail -1 "$O/tests.txt")"
grep -A3 '^FAIL' "$O/tests.txt" | tee -a "$LOG"

say "== I7 cost (jsdom, upper bounds)"
for V in reference candidate; do say "$V $(node "$LANE/tools/jsdom-cost.cjs" "$O/$V.html" 3 2>&1 | tail -1)"; done

say "== I8 status words by stored code"
node "$LANE/tools/status-labels.cjs" "$O/candidate.html" ${LABELS:+"$LABELS"} > "$O/status-labels.txt" 2>&1 || fail=1
cut -c1-200 "$O/status-labels.txt" | tee -a "$LOG"

say "== done $(date -u +%Y-%m-%dT%H:%M:%SZ): $( [ $fail = 0 ] && echo 'no check failed' || echo 'a check failed (see above)')"
say "Not checked here: the page image (widths 1400/1024/768/480/375, light and dark, reduced motion, keyboard focus, forced"
say "colours, print A4 and Letter), browser timing, screen readers. Those need a permitted browser."
exit $fail
