#!/usr/bin/env python3
"""Verify and package only the requested final reader-text correction."""
from __future__ import annotations

import copy
import hashlib
import json
import re
import subprocess
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT.parents[1]
SITE = Path('/Users/raeez/www-worktrees/2026-11-16-qh-max-integration/content/quantum-holography-status')
MATH_RENDERER = Path('/Users/raeez/www-worktrees/2026-11-16-qh-max-integration/compiler/quantum-holography-tracker/tex2mathml.cjs')


def pin(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def parts(pointer):
    assert pointer.startswith('/')
    return [x.replace('~1', '/').replace('~0', '~') for x in pointer[1:].split('/')]


def get(value, pointer):
    for part in parts(pointer):
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def put(value, pointer, after):
    tokens = parts(pointer)
    for part in tokens[:-1]:
        value = value[int(part)] if isinstance(value, list) else value[part]
    key = int(tokens[-1]) if isinstance(value, list) else tokens[-1]
    value[key] = after


def walk(value, pointer=''):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, pointer + '/' + key.replace('~', '~0').replace('/', '~1'))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, pointer + '/' + str(index))
    else:
        yield pointer, value


def numbers(value):
    return re.findall(r'\d+', unicodedata.normalize('NFKC', value))


def main():
    delta_path = ROOT / 'author/DELTA.json'
    document = json.loads(delta_path.read_text())
    operations = document.get('replacements', document.get('operations'))
    assert isinstance(operations, list) and operations
    scope = json.loads((ROOT / 'coordination/EXPECTED-SCOPE.json').read_text())
    allowed = {(x['file'], x['pointer']) for x in scope['allowed_scalar_leaves']}
    before = {name: json.loads((ROOT / 'baselines' / name).read_text()) for name in ('content.json', 'atlas.json')}
    after = copy.deepcopy(before)
    seen, math_jobs, number_checks = set(), [], []
    for op in operations:
        filename = op.get('file', op.get('artifact'))
        pointer = op['pointer']
        key = (filename, pointer)
        assert key in allowed and key not in seen, key
        assert isinstance(op['before'], str) and isinstance(op['after'], str), key
        assert get(after[filename], pointer) == op['before'], key
        assert op['before'] != op['after'], key
        assert numbers(op['before']) == numbers(op['after']), ('numerical scope changed', key)
        number_checks.append({'file': filename, 'pointer': pointer, 'numerical_tokens_unchanged': True})
        text = op['after']
        assert text.count('\\(') == text.count('\\)') and text.count('\\[') == text.count('\\]'), key
        for match in re.finditer(r'\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]', text):
            math_jobs.append({'tex': match.group(1) if match.group(1) is not None else match.group(2), 'display': match.group(2) is not None})
        outside = re.sub(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]', '', text)
        assert not re.search(r'\badopted\b|G_m|M_A|N_1|N_2|b_j|u_B|C_V|H_b|R_N', outside, re.I), ('target warning remains', key)
        put(after[filename], pointer, text)
        seen.add(key)
    assert seen == allowed, ('flagged fields not covered', sorted(allowed - seen))
    changes = []
    for filename in before:
        old, new = dict(walk(before[filename])), dict(walk(after[filename]))
        assert old.keys() == new.keys(), filename
        actual_changes = {(filename, pointer) for pointer in old if old[pointer] != new[pointer]}
        assert actual_changes == {key for key in seen if key[0] == filename}, filename
        changes.extend(sorted(actual_changes))
        dump(ROOT / 'proposed' / filename, after[filename])
    # The two legitimate warnings and their surrounding fields were not selected.
    before_flat = json.dumps(before, ensure_ascii=False)
    after_flat = json.dumps(after, ensure_ascii=False)
    for literal in ('author draft', 'frozen native weight quotients', 'unadopted'):
        assert before_flat.count(literal) == after_flat.count(literal), literal
    essay = ROOT / 'baselines/essay.md'
    (ROOT / 'proposed/essay.md').write_bytes(essay.read_bytes())
    for filename in ('content.json', 'atlas.json', 'essay.md'):
        assert pin(SITE / filename)['sha256'] == pin(ROOT / 'baselines' / filename)['sha256'], ('live guard changed', filename)
    rendered = subprocess.run(['node', str(MATH_RENDERER)], input=json.dumps(math_jobs), capture_output=True, text=True, check=True)
    math_results = json.loads(rendered.stdout)
    errors = [dict(job, error=row['error']) for job, row in zip(math_jobs, math_results) if 'error' in row]
    assert len(math_results) == len(math_jobs) and not errors, errors
    frozen_manifest = FROZEN / 'FINAL-PINS.json'
    frozen = json.loads(frozen_manifest.read_text())
    for row in frozen['files']:
        actual = pin(Path(row['path']))
        assert actual['sha256'] == row['sha256'] and actual['bytes'] == row['bytes'], row['path']
    now = datetime.now(timezone.utc).isoformat()
    validation = {'schema': 'bounded-final-render-delta-validation/v1', 'created_utc': now, 'status': 'PASS',
                  'author_delta': pin(delta_path), 'changed_scalar_leaves': len(changes), 'exact_changed_fields': changes,
                  'unselected_values_exact': True, 'all_ids_statuses_memberships_edges_cutoffs_exact': True,
                  'numerical_scope_checks': number_checks, 'math_occurrences_checked': len(math_jobs), 'math_errors': errors,
                  'essay_unchanged': pin(essay)['sha256'] == pin(ROOT / 'proposed/essay.md')['sha256'],
                  'legitimate_citation_and_mathematical_warning_phrases_preserved': True,
                  'frozen_packet': pin(frozen_manifest), 'frozen_artifacts_verified_unchanged': len(frozen['files']),
                  'math_renderer': pin(MATH_RENDERER), 'combined_render_or_visual_review_claimed': False,
                  'proof_reassessment': False, 'canonical_writes': False}
    dump(ROOT / 'validation/VALIDATION.json', validation)
    dump(ROOT / 'validation/MATH-JOBS.json', math_jobs)
    dump(ROOT / 'validation/MATH-RESULTS.json', math_results)
    file_ops = []
    for filename in ('content.json', 'atlas.json'):
        old, new = pin(ROOT / 'baselines' / filename), pin(ROOT / 'proposed' / filename)
        file_ops.append({'source': new, 'destination': str(SITE / filename),
                         'before': {'state': 'exact', 'sha256': old['sha256'], 'bytes': old['bytes']},
                         'after': {'sha256': new['sha256'], 'bytes': new['bytes']}})
    guard = {'schema': 'root-only-bounded-public-text-correction/v1', 'created_utc': now,
             'scientific_cutoff_utc': '2026-11-16T16:20:00Z', 'file_operations': file_ops,
             'leaf_operations': operations, 'unchanged_essay': pin(essay),
             'original_packet': pin(frozen_manifest), 'audit_input': pin(ROOT / 'baselines/combined-audit.json'),
             'validation': pin(ROOT / 'validation/VALIDATION.json'), 'all_unselected_values_preserved': True,
             'root_only_installation_combined_render_and_release': True, 'source_proofs_reopened': False,
             'scientific_status_changed': False, 'existing_id_changed': False, 'shared_writes': False}
    dump(ROOT / 'GUARDED-DELTA.json', guard)
    print(json.dumps({'status': 'PASS', 'guard': pin(ROOT / 'GUARDED-DELTA.json'),
                      'changed_fields': len(changes), 'math_occurrences': len(math_jobs),
                      'files': [x['source'] for x in file_ops]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
