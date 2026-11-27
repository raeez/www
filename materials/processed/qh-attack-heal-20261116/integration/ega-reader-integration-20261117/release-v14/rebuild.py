#!/usr/bin/env python3
"""Rebuild the maintained v14 baseline in a fresh scratch directory and compare published bytes."""
import argparse
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

RELEASE = Path(__file__).resolve().parent


def load(path):
    return json.loads(path.read_text())


def record(path):
    raw = path.read_bytes()
    return {'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def require_pin(path, sha):
    if not path.is_file() or record(path)['sha256'] != sha:
        raise RuntimeError(f'input pin mismatch: {path}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('scratch', type=Path)
    parser.add_argument('--python', required=True)
    parser.add_argument('--node-modules', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--repository-root', type=Path)
    args = parser.parse_args()
    root = args.repository_root or next(p for p in RELEASE.parents if (p / 'AGENTS.md').is_file() and (p / 'compiler').is_dir())
    scratch = args.scratch.resolve()
    if scratch.exists() or args.report.exists():
        raise RuntimeError('scratch/report exists; refusing to overwrite')
    assets, custody = load(RELEASE / 'ASSETS.json'), load(RELEASE / 'CUSTODY.json')
    runtime, expected = load(RELEASE / 'RUNTIME.json'), load(RELEASE / 'EXPECTED-PUBLIC.json')
    env = dict(os.environ, NODE_PATH=str(args.node_modules.resolve()), PYTHONDONTWRITEBYTECODE='1')
    observed_runtime = {
        'python': subprocess.check_output([args.python, '-B', '-c', 'import sys;print(sys.version.split()[0])'], text=True).strip(),
        'fonttools': subprocess.check_output([args.python, '-B', '-c', 'import fontTools;print(fontTools.__version__)'], text=True).strip(),
        'node': subprocess.check_output(['node', '--version'], text=True).strip(),
        'jsdom': subprocess.check_output(['node', '-e', 'process.stdout.write(require("jsdom/package.json").version)'], env=env, text=True).strip(),
    }
    for name in ('fonttools', 'node', 'jsdom'):
        if observed_runtime[name] != runtime[name]:
            raise RuntimeError(f'exact baseline runtime mismatch for {name}: {observed_runtime[name]} != {runtime[name]}')
    for font in runtime['fonts']:
        resolved = Path(subprocess.check_output(['kpsewhich', font['name']], text=True).strip())
        require_pin(resolved, font['sha256'])
    scratch.mkdir(parents=True)
    stage, out, site = scratch / 'workspace', scratch / 'build', scratch / 'public'
    out.mkdir()
    inputs = []
    for row in custody['sources']:
        source = RELEASE / row['persistent_relative_path']
        require_pin(source, row['persistent']['sha256'])
        destination = stage / row['logical_path']
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        inputs.append({'logical_path': row['logical_path'], 'sha256': row['persistent']['sha256'], 'persistent_path': str(source)})
    for row in assets['dependencies']:
        source = root / row['repository_relative_path']
        require_pin(source, row['persistent']['sha256'])
        destination = stage / row['logical_path']
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.symlink_to(source)
        inputs.append({'logical_path': row['logical_path'], 'sha256': row['persistent']['sha256'], 'reused_asset': str(source)})
    tool_paths = {}
    for name, row in assets['tools'].items():
        tool_paths[name] = root / row['repository_relative_path']
        require_pin(tool_paths[name], row['sha256'])
    require_pin(RELEASE / custody['consumer_component']['persistent_relative_path'], custody['consumer_component']['persistent']['sha256'])
    node = ['node', '--max-old-space-size=8192', '--expose-gc']
    commands = [
        ('build', [args.python, '-B', str(stage / 'compiler/build-quantum-holography-status.py'), '--output', str(out / 'combined.html'), '--audit-dir', str(out / 'audit')]),
        ('split', [sys.executable, '-I', str(tool_paths['split']), str(out / 'combined.html'), str(site), '--book-name', 'index.html']),
        ('metadata', [sys.executable, '-I', str(tool_paths['metadata']), str(site)]),
        ('consumer', [sys.executable, '-I', str(RELEASE / 'consumer/derive.py'), str(site), str(stage / 'compiler/quantum-holography-status/reader.js'), '--report', str(out / 'DERIVED-CONSUMER-METADATA.json')]),
        ('index', node + [str(tool_paths['index']), str(site / 'reader-index.js')] + [str(site / n) for n in ('index.html', 'reference.html', 'atlas.html')]),
        ('public_check', [sys.executable, '-I', str(tool_paths['public_check']), str(site), str(out / 'PUBLIC-FILES-CHECK.json')]),
        ('consumer_check', node + [str(RELEASE / 'consumer/check.cjs'), str(site), str(out / 'CONSUMER-CHECK.json')]),
    ]
    executed = []
    for name, command in commands:
        start = datetime.datetime.now(datetime.timezone.utc).isoformat()
        log = out / (name + '.log')
        with log.open('wb') as stream:
            completed = subprocess.run(command, cwd=stage, env=env, stdout=stream, stderr=subprocess.STDOUT)
        executed.append({'step': name, 'command': command, 'started_utc': start, 'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'exit_code': completed.returncode, 'scratch_log': str(log)})
        print(name, 'exit', completed.returncode, flush=True)
        if completed.returncode:
            raise RuntimeError(f'{name} failed; inspect {log}')
    files = {}
    for name, row in expected['files'].items():
        observed = record(site / name)
        files[name] = {**observed, 'expected_sha256': row['sha256'], 'expected_bytes': row['bytes'], 'exact_match': observed['sha256'] == row['sha256'] and observed['bytes'] == row['bytes']}
    audit, public, consumer = load(out / 'audit/audit.json'), load(out / 'PUBLIC-FILES-CHECK.json'), load(out / 'CONSUMER-CHECK.json')
    safe = not audit['failures'] and audit['math_errors'] == 0 and not public['links']['bad_local_links'] and not any(x['private_or_attribution_hits'] for x in public['files'].values()) and consumer['status'] == 'PASS'
    all_match = all(row['exact_match'] for row in files.values())
    result = {'schema': 'qh-reader-clean-rebuild-verification/1', 'status': 'PASS_EXACT_REBUILD' if safe and all_match else 'FAIL',
              'verified_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'live_commit_reference': expected['live_commit'],
              'release_path': str(RELEASE), 'clean_scratch': str(scratch), 'logical_inputs': inputs, 'runtime': observed_runtime, 'commands': executed,
              'files': files, 'math_formulas': audit['math'], 'math_errors': audit['math_errors'], 'local_links_and_map_ids': public['links']['local_links_checked'],
              'bad_local_links': public['links']['bad_local_links'], 'private_or_attribution_hits': sum(len(x['private_or_attribution_hits']) for x in public['files'].values()),
              'consumer_check_count': consumer['check_count'], 'consumer_status': consumer['status'], 'search_units': consumer['search_units'],
              'preserved_heading_requirements': consumer['heading_requirements'], 'preserved_authored_links': consumer['authored_links'],
              'residual_nonreproducibility': [] if safe and all_match else ['See exact file comparisons and check diagnostics.'], 'network_or_publication_actions': False, 'native_visual_qa': 'PENDING'}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    shutil.copy2(out / 'CONSUMER-CHECK.json', args.report.parent / (args.report.stem + '-consumer.json'))
    print(json.dumps({'status': result['status'], 'exact_matches': sum(x['exact_match'] for x in files.values()), 'public_files': len(files), 'consumer_checks': consumer['check_count'], 'report': str(args.report)}))
    return 0 if result['status'] == 'PASS_EXACT_REBUILD' else 1


if __name__ == '__main__':
    sys.exit(main())
