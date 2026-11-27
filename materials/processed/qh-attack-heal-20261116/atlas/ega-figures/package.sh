#!/bin/zsh
# Packages the figure files of this tree into <out>: a new-file patch, a delta patch from the earlier frozen set
# (figures-files.patch b28e07b0, as copied into the foundation's staging), a guard, and the file hashes.
# Run from the worktree root: zsh <this> <out-dir>
set -e
OUT=$1; mkdir -p $OUT
FILES=(compiler/quantum-holography-status/figures.py compiler/quantum-holography-status/figures.css compiler/quantum-holography-status/figures.js
       compiler/quantum-holography-status/tests/test_figures.py compiler/quantum-holography-status/tests/figures.test.cjs
       compiler/quantum-holography-status/tests/figures_page.py compiler/quantum-holography-status/tests/fixtures/figures-synthetic.json)
: > $OUT/figures-files.patch
for f in $FILES; do git diff --no-index --binary -- /dev/null "$f" >> $OUT/figures-files.patch || true; done
for f in $FILES; do printf "%s %s %s\n" "$(shasum -a 256 $f | cut -d' ' -f1)" "$(wc -c < $f | tr -d ' ')" "$f"; done > $OUT/figures-hashes.txt
# delta from the earlier frozen set: rebuild the earlier tree from its patch, then diff file by file
OLD=$(mktemp -d); (cd $OLD && git init -q && git apply $2)
: > $OUT/figures-delta-from-b28e07b0.patch
for f in $FILES; do
  if [ -e $OLD/$f ]; then
    (cd $OLD && cp $OLDPWD/$f $OLD/$f.new && git diff --no-index --binary -- $f $f.new | sed -e "s#b/$f.new#b/$f#g" -e "s#$f.new#$f#g" >> $OUT/figures-delta-from-b28e07b0.patch; rm $OLD/$f.new) || true
  fi
done
rm -rf $OLD
echo "packaged into $OUT"
