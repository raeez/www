#!/usr/bin/env python3
"""Preserve the exact editable input baseline and minimal release custody."""
import datetime
import hashlib
import json
import shutil
from pathlib import Path

RELEASE = Path(__file__).resolve().parent.parent
REPOSITORY = next(p for p in RELEASE.parents if (p / 'AGENTS.md').is_file() and (p / 'compiler').is_dir())
OLD = Path('/tmp/qh-v14-sol-integration-20261117')
FINAL = OLD / 'repair-v1'
E = RELEASE.parent


def load(path):
    return json.loads(path.read_text())


def record(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(name, value):
    target = RELEASE / name
    if target.exists():
        raise RuntimeError(f'refusing to overwrite {target}')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def copy(source, relative, expected=None):
    source = Path(source)
    before = record(source)
    if expected is not None and before['sha256'] != expected:
        raise RuntimeError(f'input drift: {source}')
    target = RELEASE / relative
    if target.exists():
        raise RuntimeError(f'refusing to overwrite {target}')
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    target.chmod(0o644)
    if target.read_bytes() != source.read_bytes() or record(source) != before:
        raise RuntimeError(f'copy drift: {source}')
    return {'original': before, 'persistent': record(target), 'persistent_relative_path': str(target.relative_to(RELEASE))}


def main():
    if (RELEASE / 'source-tree').exists():
        raise RuntimeError('source baseline already exists')
    final_manifest = FINAL / 'MANIFEST-v14-repair-v1.json'
    if record(final_manifest)['sha256'] != 'c105f904ace52d65467409379de98dfd06b71c085cf74768e7415eba43b99269':
        raise RuntimeError('published manifest pin mismatch')
    publication = Path('/tmp/qh-hosting-recovery-20261117/prepared/v14-publication-20261117T1920Z/PUBLICATION.json')
    pub = load(publication)
    if pub['commit'] != '1bb5537744d4526287b611f9552c9aacaaaca610' or pub['status'] != 'PUBLISHED_AND_VERIFIED' or not all(x['exact_match'] for x in pub['readbacks']):
        raise RuntimeError('publication receipt mismatch')
    baseline = load(OLD / 'coordination/BASELINE.json')
    replay = load(OLD / 'coordination/SOURCE-GUARD-LEDGER.json')
    expected = {row['relative_path']: row['sha256'] for row in baseline['sources']}
    for row in replay['files'].values():
        expected[str(Path(row['target']).relative_to(OLD / 'workspace'))] = row['after']['sha256']
    derived = replay['derived_digest_synchronization']
    expected[str(Path(derived['path']).relative_to(OLD / 'workspace'))] = derived['after']['sha256']
    if len(expected) != 55:
        raise RuntimeError('accepted input inventory is not 55')
    sources, dependencies = [], []
    for relative, sha in sorted(expected.items()):
        original = OLD / 'workspace' / relative
        if record(original)['sha256'] != sha:
            raise RuntimeError(f'accepted source drift: {relative}')
        if '/vendor/' in relative:
            reused = REPOSITORY / relative
            if record(reused)['sha256'] != sha:
                raise RuntimeError(f'repository dependency drift: {relative}')
            dependencies.append({'logical_path': relative, 'original': record(original), 'repository_relative_path': relative, 'persistent': record(reused), 'copied': False})
        else:
            sources.append({'logical_path': relative, **copy(original, 'source-tree/' + relative, sha)})
    tools = {}
    paths = {
        'split': E / 'interaction-reader-delta4/tools/split-reference.py',
        'index': E / 'interaction-reader-delta4/tools/reader-index.cjs',
        'split_checks': E / 'interaction-reader-delta4/tools/split-checks.cjs',
        'metadata': E / 'tools/set_page_metadata.py',
        'public_check': E / 'tools/check_public.py',
    }
    for name, path in paths.items():
        tools[name] = {**record(path), 'repository_relative_path': str(path.relative_to(REPOSITORY)), 'copied': False}
    component = copy(FINAL / 'consumer/reader.js', 'consumer/reader.js')
    copy(FINAL / 'coordination/READER-INDEXING-ONLY.patch', 'consumer/READER-INDEXING-ONLY.patch')
    decision_path = Path('/tmp/qh-post-reset-reader-20261117/build-consumer-decision/DECISION.json')
    if record(decision_path)['sha256'] != '2bed11c249cc61370953a7ce66a08d52d7a39bd753295d1afaf4c10ada89bc5a':
        raise RuntimeError('consumer requirement pin mismatch')
    decision = load(decision_path)
    requirements = {'schema': 'qh-reader-consumer-requirements/1', 'source_decision_sha256': record(decision_path)['sha256'],
                    'headings': [{'page': x['required_search_unit']['page'], 'id': x['required_search_unit']['id'], 'title': x['required_search_unit']['title']} for x in decision['heading_search_requirements']],
                    'links': [{'page': x['origin_page'], 'label': x['authored_label'], 'href': x['authored_href']} for x in decision['supplement_link_requirements']]}
    save('consumer/requirements.json', requirements)
    evidence = []
    for source, name in [(publication, 'PUBLICATION.json'), (final_manifest, 'PUBLISHED-MANIFEST-v14.json'), (decision_path, 'CONSUMER-DECISION.json'),
                         (FINAL / 'build/CONSUMER-REPAIR-VALIDATION.json', 'CONSUMER-VALIDATION.json'),
                         (Path('/tmp/frontier-post-reset-review-20261117/reader-fidelity/COMBINED-RECEIPT.json'), 'SOURCE-FIDELITY-RECEIPT.json'),
                         (Path('/tmp/qh-post-reset-reader-20261117/repair-v1/SEAL.json'), 'AUTHOR-SEAL.json'),
                         (OLD / 'coordination/SOURCE-GUARD-LEDGER.json', 'SOURCE-GUARD-LEDGER.json')]:
        evidence.append(copy(source, 'evidence/' + name))
    public = load(final_manifest)['public_files']
    save('EXPECTED-PUBLIC.json', {'live_commit': pub['commit'], 'published_utc': pub['recorded_utc'], 'publication_receipt': 'evidence/PUBLICATION.json',
                                'files': {name: {'sha256': row['sha256'], 'bytes': row['bytes'], 'public_path': 'quantum-holography/' + name} for name, row in public.items()}, 'native_visual_qa': 'PENDING'})
    save('ASSETS.json', {'repository_root_at_preservation': str(REPOSITORY), 'dependencies': dependencies, 'tools': tools})
    save('CUSTODY.json', {'schema': 'qh-reader-durable-input-custody/1', 'preserved_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         'release': 'v14 consumer-repair-v1', 'live_commit': pub['commit'], 'logical_source_count': 55, 'editable_copied_source_count': len(sources),
                         'reused_dependency_count': len(dependencies), 'sources': sources, 'dependencies': dependencies, 'consumer_component': component,
                         'evidence': evidence, 'broad_temporary_trees_or_duplicate_logs_copied': False, 'public_files_copied': False,
                         'existing_owner_or_public_files_modified': [], 'native_visual_qa': 'PENDING'})
    save('SOURCE-COORDINATES.json', {'schema': 'qh-reader-editable-source-coordinates/1', 'base_release': 'v14 consumer-repair-v1', 'live_commit': pub['commit'],
                                    'source_root': str(RELEASE / 'source-tree'), 'reader_source_root': str(RELEASE / 'source-tree/content/quantum-holography-status'),
                                    'logical_sources': [{'logical_path': row['logical_path'], 'path': row['persistent']['path'], 'sha256': row['persistent']['sha256'], 'bytes': row['persistent']['bytes']} for row in sources],
                                    'consumer_component': component['persistent'], 'consumer_requirements': str(RELEASE / 'consumer/requirements.json'),
                                    'golden_rule': 'Mathematical and physical exposition stays in the manuscript sources; coordination, checks and build records stay outside them.'})
    print(json.dumps({'status': 'PRESERVED_AWAITING_CLEAN_REBUILD', 'release_path': str(RELEASE), 'copied_editable_sources': len(sources), 'reused_dependency_files': len(dependencies), 'logical_sources': 55}))


if __name__ == '__main__':
    main()
