"""Writes the quality lane's integration patches against the files root has integrated (foundation snapshot
GUARD c9d1c8cd / patch 695ff9a8, interaction candidate-r3 status.js, quality build wrapper 7419f94a and audit 2e857726).
Usage (from quality/compose): python3 -I -B ../lead/make-integration-patches.py
Reads compose/reference (the integrated files), compose/composed (with the remaining quality delta) and
compose/language/page.json (the status-language labels); writes compose/patches/ and compose/INTEGRATION-MANIFEST.json.
"""
import difflib, hashlib, json
from pathlib import Path

C = Path('.')
sha = lambda b: hashlib.sha256(b).hexdigest()
P = C / 'patches'
P.mkdir(exist_ok=True)
for old in P.glob('*.diff'):
    old.unlink()


def udiff(path, a_bytes, b_bytes):
    a, b = a_bytes.decode('utf-8'), b_bytes.decode('utf-8')
    return ''.join(difflib.unified_diff(a.splitlines(keepends=True), b.splitlines(keepends=True), f'a/{path}', f'b/{path}', n=3))


REMAINING = ['compiler/quantum-holography-status/status.py', 'compiler/quantum-holography-status/status.css',
             'compiler/quantum-holography-status/status-print.css', 'compiler/quantum-holography-status/audit.py']
SOURCES = json.loads((C / 'reference' / 'REFERENCE-PINS.json').read_text())
parts, files = {}, []
text = ''
for path in REMAINING:
    a, b = (C / 'reference' / path).read_bytes(), (C / 'composed' / path).read_bytes()
    d = udiff(path, a, b)
    text += d
    files.append({'patch': 'QUALITY-REMAINING.diff', 'path': path, 'integrated_source': SOURCES[path]['source'],
                  'before_sha256': sha(a), 'after_sha256': sha(b), 'hunks': d.count('\n@@ ')})
(P / 'QUALITY-REMAINING.diff').write_text(text, encoding='utf-8')
lang_path = 'content/quantum-holography-status/page.json'
a, b = (C / 'reference' / lang_path).read_bytes(), (C / 'language' / 'page.json').read_bytes()
d = udiff(lang_path, a, b)
(P / 'STATUS-LANGUAGE.diff').write_text(d, encoding='utf-8')
files.append({'patch': 'STATUS-LANGUAGE.diff', 'path': lang_path, 'integrated_source': SOURCES[lang_path]['source'],
              'before_sha256': sha(a), 'after_sha256': sha(b), 'hunks': d.count('\n@@ ')})
# Optional, separate: the counterexample statement's heading level, and the earlier README notes.
sp = 'compiler/quantum-holography-status/status.py'
cur = (C / 'composed' / sp).read_bytes()
alt = cur.decode('utf-8').replace("witness = self.statement(w, f'failure {i} witness', chip=not all_added)",
                                  "witness = self.statement(w, f'failure {i} witness', heading='h3', chip=not all_added)").encode()
assert alt != cur
(P / 'OPTIONAL-heading.diff').write_text(udiff(sp, cur, alt), encoding='utf-8')
rp = 'content/quantum-holography-status/README.md'
ra, rb = (C / 'reference' / rp).read_bytes(), (C / '..' / 'heal' / 'mirror' / rp).read_bytes()
(P / 'OPTIONAL-README.diff').write_text(udiff(rp, ra, rb), encoding='utf-8')
manifest = {
    'base': {'description': 'files root has integrated', 'pins': {p: v for p, v in SOURCES.items()}},
    'patches': {name: sha((P / name).read_bytes()) for name in ('QUALITY-REMAINING.diff', 'STATUS-LANGUAGE.diff',
                                                                 'OPTIONAL-heading.diff', 'OPTIONAL-README.diff')},
    'files': files,
    'optional': [{'patch': 'OPTIONAL-heading.diff', 'path': sp, 'before_sha256': sha(cur), 'after_sha256': sha(alt)},
                 {'patch': 'OPTIONAL-README.diff', 'path': rp, 'before_sha256': sha(ra), 'after_sha256': sha(rb)}],
}
(C / 'INTEGRATION-MANIFEST.json').write_text(json.dumps(manifest, indent=1) + '\n', encoding='utf-8')
for f in files:
    print(f"{f['patch']:24} {f['path']:52} {f['before_sha256'][:8]} -> {f['after_sha256'][:8]}  hunks {f['hunks']}")
print({k: v[:8] for k, v in manifest['patches'].items()})
