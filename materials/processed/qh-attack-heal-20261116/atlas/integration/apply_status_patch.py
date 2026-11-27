#!/usr/bin/env python3
"""Integration of the research atlas into status.py: a proposal for the owner of status.py.

    python3 apply_status_patch.py --check <status.py>              report whether each hunk applies
    python3 apply_status_patch.py --write <status.py>              apply the five hunks in place
    python3 apply_status_patch.py --emit  <status.py> <out file>   write the patched text elsewhere

Each hunk replaces one anchor text that must occur exactly once in status.py; otherwise nothing is
written and the hunk is named. The whole-file hash is reported: BASELINE is the status.py this
proposal was made against, BASELINE_AFTER the result of patching it. On a changed status.py the
hunks still apply when their anchors are intact, and the result must then be verified by building
the page without atlas.json and comparing it with the unpatched build (same SOURCE_DATE_EPOCH).
Without atlas.json the patched builder imports nothing new and writes the same bytes.
"""
import hashlib
import sys
from pathlib import Path

BASELINE = '7e00aab95067023c4b686723227c7f3de17ebab5759ca87e95d46f1ff8a72fc9'
BASELINE_AFTER = 'b6a00a211d0e686efce42c71b8a28f6a20cb973bee28e4cf3ebafb4f38081954'

HUNKS = [
    ('the atlas is built after the principal results, only when the input folder holds atlas.json',
     "        principal = self.principal(c)\n",
     "        principal = self.principal(c)\n"
     "        atlas_section = ''\n"
     "        if (self.folder / 'atlas.json').exists():  # the research atlas\n"
     "            import atlas  # here: atlas.py imports status\n"
     "            atlas_section = atlas.section(self, self.folder)\n"),
    ('its navigation item, after Results',
     "        nav_items = [('programme', L['nav_programme']), ('results', L['nav_results'])]\n",
     "        nav_items = [('programme', L['nav_programme']), ('results', L['nav_results'])]\n"
     "        if atlas_section:\n"
     "            nav_items.append(('atlas', atlas.labels_for(self.page)['nav']))\n"),
    ('its place in the page, between the principal results and the decisive questions',
     "{cover}{changes}{key}{principal}{decisive}",
     "{cover}{changes}{key}{principal}{atlas_section}{decisive}"),
    ('its styles, after the screen and print sheets of the page',
     "        js = (HERE / 'status.js').read_text(encoding='utf-8')\n",
     "        if atlas_section:\n"
     "            css += '\\n' + atlas.stylesheet()\n"
     "        js = (HERE / 'status.js').read_text(encoding='utf-8')\n"),
    ('its script, in its own element after the page script',
     "        return head + f'<body>\\n{body}\\n<script>{js}</script>\\n</body>\\n</html>\\n'\n",
     "        extra = f'<script>{atlas.script()}</script>\\n' if atlas_section else ''\n"
     "        return head + f'<body>\\n{body}\\n<script>{js}</script>\\n{extra}</body>\\n</html>\\n'\n"),
]


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def patched(text):
    bad = [f'hunk {i} ({why}): its anchor occurs {text.count(old)} times, not once'
           for i, (why, old, _) in enumerate(HUNKS, 1) if text.count(old) != 1]
    if bad:
        return None, bad
    for _, old, new in HUNKS:
        text = text.replace(old, new)
    return text, []


def main(argv):
    if len(argv) < 3 or argv[1] not in ('--check', '--write', '--emit') or (argv[1] == '--emit' and len(argv) < 4):
        print(__doc__)
        return 2
    target = Path(argv[2])
    text = target.read_text(encoding='utf-8')
    before = sha(text)
    print(f'status.py sha256 {before} ({"the baseline" if before == BASELINE else "not the baseline: verify the result"})')
    out, bad = patched(text)
    if bad:
        print('\n'.join(bad))
        return 1
    after = sha(out)
    print(f'patched sha256   {after}' + (' (as expected)' if before == BASELINE and after == BASELINE_AFTER else ''))
    if before == BASELINE and after != BASELINE_AFTER:
        print('the patched baseline does not hash to BASELINE_AFTER')
        return 1
    if argv[1] == '--write':
        target.write_text(out, encoding='utf-8')
        print(f'patched {target}')
    elif argv[1] == '--emit':
        Path(argv[3]).write_text(out, encoding='utf-8')
        print(f'wrote {argv[3]}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
