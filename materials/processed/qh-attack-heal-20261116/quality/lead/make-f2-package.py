"""Writes the quality lane's additive patch against the foundation's final F1+F2 bytes (compose/f2-package/).
Base: compose/f1f2/tree = root's integration (foundation 695ff9a8, quality wrapper 7419f94a and audit 2e857726, baseline
status.js) with f1-status-language.patch (961325...) and f2-successor-fields.patch (3f2c4493...) applied; every F2 candidate
hash checked. After: compose/f1f2/composed. Usage (from quality/compose): python3 -I -B ../lead/make-f2-package.py
"""
import difflib, hashlib, json
from pathlib import Path
sha = lambda b: hashlib.sha256(b).hexdigest()
OUT = Path('f2-package')
FILES = ['compiler/quantum-holography-status/status.py', 'compiler/quantum-holography-status/status.css',
         'compiler/quantum-holography-status/status-print.css', 'compiler/quantum-holography-status/audit.py']
UNCHANGED = ['compiler/build-quantum-holography-status.py', 'compiler/quantum-holography-status/status.js',
             'content/quantum-holography-status/page.json', 'content/quantum-holography-status/content.json',
             'content/quantum-holography-status/essay.md']
text, files = '', []
for p in FILES:
    a, b = (Path('f1f2/tree') / p).read_bytes(), (Path('f1f2/composed') / p).read_bytes()
    d = ''.join(difflib.unified_diff(a.decode().splitlines(keepends=True), b.decode().splitlines(keepends=True), f'a/{p}', f'b/{p}', n=3))
    text += d
    files.append({'path': p, 'before_sha256': sha(a), 'after_sha256': sha(b), 'hunks': d.count('\n@@ ')})
(OUT / 'QUALITY-ON-F1F2.diff').write_text(text, encoding='utf-8')
g = json.loads(Path('f1f2/F2-GUARD.json').read_text())
manifest = {
    'base': {'description': "root's integration with the foundation's final F1 and F2 applied",
             'root_integration': 'foundation 695ff9a8; quality build wrapper 7419f94a and audit 2e857726; baseline status.js',
             'f1': {'patch': 'f1-status-language.patch', 'sha256': sha(Path('f1f2/f1-status-language.patch').read_bytes())},
             'f2': {'patch': 'f2-successor-fields.patch', 'sha256': sha(Path('f1f2/f2-successor-fields.patch').read_bytes()),
                    'candidates': {f['path']: f['candidate_sha256'] for f in g['files']}},
             'unchanged_pins': {p: sha((Path('f1f2/tree') / p).read_bytes()) for p in UNCHANGED}},
    'patch': {'name': 'QUALITY-ON-F1F2.diff', 'sha256': sha(text.encode())},
    'files': files,
    'withdrawn': {'STATUS-LANGUAGE.diff': 'superseded by F1 (same five status labels; F1 also removes cell_glosses)'},
}
(OUT / 'MANIFEST.json').write_text(json.dumps(manifest, indent=1) + '\n', encoding='utf-8')
for f in files:
    print(f"{f['path']:52} {f['before_sha256'][:8]} -> {f['after_sha256'][:8]}  hunks {f['hunks']}")
print('patch', manifest['patch']['sha256'][:16])
