"""Writes the guarded patch of the mirror against the baseline: heal/MANIFEST.json, heal/PATCH.diff and
heal/patches/<owner>.diff. Usage (from the worktree root):
  python3 -I -B <Q>/lead/make-guarded-patch.py <Q> <candidate id>
Reads BASELINE.json, the production files (which must still equal their baseline hashes) and the mirror.
"""
import difflib
import hashlib
import json
import sys
from pathlib import Path

Q, CANDIDATE = Path(sys.argv[1]), sys.argv[2]
ROOT = Path('.').resolve()
MIRROR = Q / 'heal' / 'mirror'
sha = lambda b: hashlib.sha256(b).hexdigest()
OWNER = {'compiler/quantum-holography-status/status.js': 'interaction',
         'content/quantum-holography-status/content.json': 'content owner',
         'content/quantum-holography-status/essay.md': 'content owner'}
LEDGER = {
    'compiler/build-quantum-holography-status.py': ['C02'],
    'compiler/quantum-holography-status/audit.py': ['C17', 'C25', 'C04 guard', 'C03 guard', 'C18 list', 'C20 warnings',
                                                    'A2-A2-04', 'A2-A2-05', 'A2-A2-06', 'A3-F-02', 'A3-F-03', 'A3-F-04',
                                                    'A3-F-05', 'A3-F-10', 'A3-F-11', 'A3-F-13 (formulas and jobs)',
                                                    'A4-F-01', 'A4-F-02 (messages)', 'A4-F-03', 'A4-F-04', 'A4-F-06',
                                                    'A4-F-08', 'A5-F-01', 'A5-F-02', 'A5-F-03', 'A5-F-04',
                                                    'S-REFUTED (status contract: refuted form, hypotheses)'],
    'compiler/quantum-holography-status/status-print.css': ['C01', 'A2-A2-07', 'A3-F-02 (comments)'],
    'compiler/quantum-holography-status/status.css': ['C01', 'C15', 'C06', 'C14', 'C23', 'A2-A1-01', 'A2-A2-09',
                                                      'A3-V-11', 'A3-V-13', 'A3-V-15', 'A3-F-06', 'A3-F-02 (comments)',
                                                      'A4-V-01', 'A4-V-02', 'A3-V-03 (a)', 'A5-V-01',
                                                      'S-REFUTED (status colour, hypotheses)'],
    'compiler/quantum-holography-status/status.js': ['C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14',
                                                     'C16', 'C23', 'A2-A1-01', 'A2-A1-03', 'A2-A1-04', 'A3-V-11', 'A3-V-12',
                                                     'A3-V-13', 'A3-F-06', 'A4-V-01', 'A4-V-03', 'A5-V-01',
                                                     'S-REFUTED (search skips the hypotheses label)',
                                                     'A7-V-02 (list items apart in search text)'],
    'compiler/quantum-holography-status/status.py': ['C03', 'C04', 'C14', 'C19', 'C23', 'C24', 'C28', 'A2-A2-01', 'A2-A2-02',
                                                     'A2-A2-03', 'A2-A2-11', 'A3-F-01', 'A3-F-06', 'A3-F-07', 'A3-F-08',
                                                     'A3-F-09', 'A3-F-13 (text-form jobs)', 'A4-V-03',
                                                     'S-REFUTED (status vocabulary, no coercion, hypotheses)',
                                                     'A7-F-01 / A7-V-04 (row filters from the rows)'],
    'content/quantum-holography-status/README.md': ['C02', 'C03', 'C17', 'C19 (documentation)'],
}
base = json.loads((Q / 'BASELINE.json').read_text(encoding='utf-8'))
entries = base['files'] if isinstance(base.get('files'), list) else [{'path': p, 'sha256': h} for p, h in base['files'].items()]
files, diffs = [], {}
for e in entries:
    path = e['path']
    before_bytes = (ROOT / path).read_bytes()
    assert sha(before_bytes) == e['sha256'], f'production file drifted from the baseline: {path}'
    after_bytes = (MIRROR / path).read_bytes()
    owner = OWNER.get(path, 'foundation')
    changed = before_bytes != after_bytes
    files.append({'path': path, 'owner': owner, 'before_sha256': e['sha256'], 'after_sha256': sha(after_bytes),
                  'changed': changed, 'ledger': LEDGER.get(path, []) if changed else []})
    if changed:
        a, b = before_bytes.decode('utf-8'), after_bytes.decode('utf-8')
        assert a.endswith('\n') and b.endswith('\n'), f'no final newline: {path}'
        diffs.setdefault(owner, []).append(''.join(difflib.unified_diff(
            a.splitlines(keepends=True), b.splitlines(keepends=True), f'a/{path}', f'b/{path}', n=3)))
order = ['foundation', 'interaction']
assert set(diffs) <= set(order), diffs.keys()
(Q / 'heal' / 'patches').mkdir(exist_ok=True)
patch_sha = {}
for owner in order:
    text = ''.join(diffs.get(owner, []))
    (Q / 'heal' / 'patches' / f'{owner}.diff').write_text(text, encoding='utf-8')
    patch_sha[owner] = sha(text.encode('utf-8'))
full = ''.join(''.join(diffs.get(o, [])) for o in order)
(Q / 'heal' / 'PATCH.diff').write_text(full, encoding='utf-8')
preview = (Q / 'candidate' / 'preview.html').read_bytes()
manifest = {
    'candidate': CANDIDATE,
    'base': 'BASELINE.json (13 files, verified against the worktree when this manifest was written)',
    'apply': 'heal/apply-guarded.sh <repository root> [foundation|interaction|all]',
    'files': files,
    'preview': {'candidate_sha256': sha(preview), 'bytes': len(preview),
                'nofonts_sha256': sha((Q / 'candidate' / 'preview-nofonts.html').read_bytes()),
                'note': 'byte-reproducible; build: python -B heal/mirror/compiler/build-quantum-holography-status.py '
                        '--output candidate/preview.html --audit-dir candidate/audit'},
    'patch_sha256': {**patch_sha, 'all': sha(full.encode('utf-8'))},
    'cross_lane_dependency': 'status.py (foundation) emits the bar search opener hidden and the card Close control as an '
                             'inert template; status.js (interaction) shows the opener and puts the Close control in the '
                             'card when it wires them. Each patch is safe alone: with the foundation patch alone no dead '
                             'or unreachable control appears and Tab behaves as on the baseline (jsdom J17); C14 and C23 '
                             'are healed only when both are applied.',
    'unchanged_reader_inputs': [f['path'] for f in files if f['path'].startswith('content/') and not f['changed']
                                and not f['path'].endswith('README.md')],
}
(Q / 'heal' / 'MANIFEST.json').write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'changed': [f['path'] for f in files if f['changed']], 'patch_sha256': manifest['patch_sha256'],
                  'manifest_sha256': sha((Q / 'heal' / 'MANIFEST.json').read_bytes())}, indent=1))
