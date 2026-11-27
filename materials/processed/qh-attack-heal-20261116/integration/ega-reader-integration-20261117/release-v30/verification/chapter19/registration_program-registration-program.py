#!/usr/bin/env python3
"""Bind the existing native v30 build, the publisher's live receipt, and native replay."""

import argparse
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from types import SimpleNamespace


HERE = Path(__file__).resolve().parent
NEXT = HERE.parent
LANE = NEXT.parent
SOURCE = NEXT / 'v30-source'
BUILD = NEXT / 'v30-build'
FINISH = BUILD / 'finishing'
EVIDENCE = HERE / 'native-evidence'
PREPARED = EVIDENCE / 'PREPARED.json'
HOSTED = BUILD / 'hosted/quantum-holography'
EDITION = 'release-v30'
PARENT_EDITION = 'release-v29'
CHAPTER = 'content/quantum-holography-status/chapters/19-interacting-theories.md'
COMPANION = 'content/quantum-holography-status/supplements/critical-points-and-sphere-insertions.tex'
NEW_PDFS = ('interacting-theories.pdf', 'critical-points-and-sphere-insertions.pdf')
CHAPTER_SHA = 'f2669549be9dc396c24fe3532b59f769fc353595721acec9ace1ea0418e15745'
PRIVATE_CHAPTER_PDF_SHA = 'b5fb983d2f7f80eb0080e7fd35556941f4c193f3b9a9a9c0812aec23c4c92b71'
COMPANION_SHA = '41df4d9806982d1982477e3ba8069cfe373c78e1fdd0d850f50769fe9c56e108'
COMPANION_PDF_SHA = '0a07e71181bd73547f4a451de1914e68ec30880c3b6914cff795ef65d1314ceb'
PDF_PREFLIGHT = LANE.parent / ('ega-celestial-yangian-20261120/owner-delivery/'
                              'holonomy-and-interacting/custody/PUBLIC-PDF-PREFLIGHT.json')


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sys.dont_write_bytecode = True
previous = load('ega_v29_registration', LANE / 'registration/register_v29.py')
native, exporter = previous.load_helpers()
previous.native, previous.exporter, previous.io = native, exporter, native.io
io = native.io
native.WORK = HERE
require, pin, read = previous.require, previous.pin, previous.read
ref, open_ref, pins, write_once = previous.ref, previous.open_ref, previous.pins, previous.write_once
READER = previous.READER_FILES
PDFS = previous.PDF_FILES + NEW_PDFS
FILES = READER + PDFS
PARENT_ARCHIVE = previous.EDITIONS / PARENT_EDITION
TARGET = previous.EDITIONS / EDITION
DRAFT = HERE / 'native-archives' / EDITION
SITE = previous.SITE


def git(*args, website):
    return previous.git(*args, worktree=website)


def verify_commit(commit, parent, site_pins, website):
    require(bool(re.fullmatch('[0-9a-f]{40}', commit)), 'Supply a full real website commit.')
    require(git('rev-list', '--parents', '-n', '1', commit, website=website).decode().split()
            == [commit, parent], f'{commit} must have exactly {parent} as parent.')
    require(git('show', f'{commit}:CNAME', website=website).strip() == b'raeez.com',
            'Unexpected Pages domain.')
    paths = {previous.MOUNT + name: name for name in site_pins}
    old = set(git('ls-tree', '--name-only', parent, '--', *paths, website=website).decode().splitlines())
    expected = set()
    for path, name in paths.items():
        data = pin(git('show', f'{commit}:{path}', website=website))
        require(data == site_pins[name], f'Website commit disagrees at {path}.')
        if path not in old or pin(git('show', f'{parent}:{path}', website=website)) != data:
            expected.add(path)
    actual = set(git('diff-tree', '--no-commit-id', '--name-only', '-r', commit,
                     website=website).decode().splitlines())
    require(expected and actual == expected, 'Unexpected changed paths in the website commit.')
    return sorted(actual)


def reference_bits(value):
    return {key: value[key] for key in ('sha256', 'bytes')}


def inventory(directory):
    members = list(directory.rglob('*'))
    require(not any(path.is_symlink() for path in members), f'Symlink in archived source: {directory}')
    return {path.relative_to(directory).as_posix(): pin(io.read_stable(path))
            for path in sorted(members) if path.is_file()}


def exact_directory(directory, names):
    require({path.name for path in directory.iterdir()} == set(names)
            and all((directory / name).is_file() and not (directory / name).is_symlink()
                    for name in names), f'Expected only the exact reader files in {directory}.')
    return pins(directory, names)


def attachment_source(raw, item):
    if 'start' in item:
        prefix = item['start'].encode()
        require(prefix and raw.count(prefix) == 1, 'The attachment source excerpt is ambiguous.')
        begin = raw.index(prefix)
        raw = raw[begin:begin + item['bytes']]
    return pin(raw)


def pdf_contents(path):
    detail = subprocess.check_output(['pdfinfo', str(path)], text=True)
    require(re.search(r'^Pages:\s+12\s*$', detail, re.M) and
            re.search(r'^Tagged:\s+yes\s*$', detail, re.M),
            f'Expected the tagged twelve-page native chapter print: {path}.')
    urls = subprocess.check_output(['pdfinfo', '-url', str(path)], text=True).splitlines()[1:]
    tuples = []
    for line in urls:
        page, location, address = line.split(maxsplit=2)
        require(location == 'Annotation' and page.isdecimal(), f'Unexpected PDF external link: {line}.')
        tuples.append((int(page), address))
    return subprocess.check_output(['pdftotext', '-layout', str(path), '-']), sorted(tuples)


def verify_public_pdf(public, historical):
    preflight = read(PDF_PREFLIGHT)
    replacements = preflight['validated_canonical_destinations']
    require(pin(io.read_stable(historical)) == reference_bits(preflight['private_print']) and
            len(replacements) == 4 and set(replacements.values()) == {
                SITE + '#' + name for name in ('ch14-celestial-yangian-like',
                                                'ch14-celestial-reconstruction',
                                                'ch14-celestial-ordered-transport',
                                                'ch14-celestial-cut-support')},
            'The canonical PDF destination decision differs.')
    old_text, old_urls = pdf_contents(historical)
    new_text, new_urls = pdf_contents(public)
    require(old_text.strip() and old_text == new_text and
            set(replacements) <= {url for _, url in old_urls} and
            new_urls == sorted((page, replacements.get(url, url)) for page, url in old_urls) and
            all(url.startswith(SITE + '#') for _, url in new_urls),
            'The public print must keep all 12 pages and replace only the four private URI destinations.')


def official_build(final_file=None, portable=None):
    source_record = BUILD / 'WORKING-SOURCE.json'
    record = read(source_record)
    source_files = inventory(SOURCE)
    raw = FINISH / 'public'
    native_build = read(BUILD / 'NATIVE-START.json')
    completed = read(BUILD / 'FINISH-START.json')
    audit_file = BUILD / 'audit/audit.json'
    audit = read(audit_file)
    require(record['edition'] == EDITION and record['chapters'] == 19 and
            len(record['headings']) == 9 and len(source_files) == 67 and
            Path(record['source_root']) == SOURCE and record['files'] == source_files and
            record['content_id'] == native_build['content_id'] == pin(native.encode(source_files))['sha256'],
            'The working native source or build identity differs.')
    require(inventory(FINISH / 'workspace') == source_files and
            Path(completed['workspace']) == FINISH / 'workspace' and
            Path(completed['public']) == raw and
            completed['combined'] == pin(io.read_stable(BUILD / 'combined.html')) and
            not audit['failures'] and audit['math_errors'] == 0 and
            io.read_stable(FINISH / 'build/audit/audit.json') == io.read_stable(audit_file),
            'The split reader must use the exact audited 19-chapter compiler output.')
    raw_pins = exact_directory(raw, FILES)

    bindings = BUILD / 'attachments/BINDINGS.json'
    signed_file = BUILD / 'SIGNED-FIVE.json'
    signed = read(signed_file)
    registry = read(bindings)
    attachments = signed['attachments']
    require(signed['status'] == 'FIVE_EXACT_SCIENTIFIC_DOWNLOADS_BOUND' and
            signed['source_id'] == record['content_id'] and signed['sources'] == ref(bindings) and
            set(attachments) == set(registry['sources']) == set(PDFS) and
            registry['schema'] == 'quantum-holography-issued-attachments/1' and
            all(attachments[name] == raw_pins[name] for name in PDFS if name != NEW_PDFS[0]),
            'A retained PDF differs from its signed source binding.')
    require(source_files[CHAPTER]['sha256'] == CHAPTER_SHA and
            attachments[NEW_PDFS[0]]['sha256'] == PRIVATE_CHAPTER_PDF_SHA and
            source_files[COMPANION]['sha256'] == COMPANION_SHA and
            attachments[NEW_PDFS[1]]['sha256'] == COMPANION_PDF_SHA and
            registry['sources'][NEW_PDFS[0]] == {CHAPTER: source_files[CHAPTER]} and
            registry['sources'][NEW_PDFS[1]] == {COMPANION: source_files[COMPANION]},
            'The exact new chapter or companion binding differs.')
    for name, sources in registry['sources'].items():
        require(sources and io.read_stable(raw / name).startswith(b'%PDF-'), f'Invalid PDF: {name}')
        for relative, source_pin in sources.items():
            require(relative in source_files and
                    attachment_source(io.read_stable(SOURCE / relative), source_pin) == reference_bits(source_pin),
                    f'The source binding differs for {name}: {relative}.')

    author = io.decode(open_ref(signed['chapter_author']))
    independent = io.decode(open_ref(signed['independent_chapter']))
    historical = (Path(signed['independent_chapter']['path']).parent /
                  independent['pdf']['file']['path'])
    require(reference_bits(author['native_reader']['article']) == source_files[CHAPTER] ==
            reference_bits(independent['chapter']['source']['chapter']) and
            independent['decision'] == signed['independent_chapter']['exact_status'] ==
            'PASS_AT_STATED_SCIENTIFIC_SCOPES_AND_COMPLETE_NATIVE_PRINT' and
            reference_bits(independent['pdf']['file']) == attachments[NEW_PDFS[0]] ==
            pin(io.read_stable(historical)),
            'The original author freeze or independent print decision differs.')
    require(pin(open_ref(signed['companion']['tex'])) == source_files[COMPANION] and
            pin(open_ref(signed['companion']['pdf'])) == attachments[NEW_PDFS[1]],
            'The companion origins differ.')
    permalink = independent['reader']['immutable_url']
    require('/cuts/' + CHAPTER_SHA + '/' in permalink and permalink.endswith('/#ch19'),
            'The original native permanent link is not scoped to this chapter.')

    refs = {'working_source': ref(source_record), 'native_start': ref(BUILD / 'NATIVE-START.json'),
            'native_finish': ref(BUILD / 'FINISH-START.json'), 'audit': ref(audit_file),
            'signed_downloads': ref(signed_file), 'registry': ref(bindings),
            'author': ref(Path(signed['chapter_author']['path'])),
            'independent': ref(Path(signed['independent_chapter']['path'])),
            'native_seal': record['native_seal'],
            'authority': ref(NEXT / 'PUBLICATION-AUTHORITY-BINDING.json'),
            'historical_chapter_pdf': ref(historical)}
    open_ref(refs['native_seal'])
    if final_file is not None:
        final = read(final_file)
        public_pins = pins(portable, PDFS)
        corrected = public_pins[NEW_PDFS[0]]
        referee = final['public_print_referee']
        decision = io.decode(open_ref(referee))
        chapter_print = NEXT / 'PUBLIC-CHAPTER-PRINT.json'
        publisher = read(chapter_print)
        require(final['status'] == 'FIVE_EXACT_PUBLIC_DOWNLOADS_BOUND' and
                final['sources'] == signed['sources'] and
                final['source_id'] == record['content_id'] and final['attachments'] == public_pins and
                corrected == pin(open_ref(final['public_print'])) ==
                reference_bits(decision['public_print']) == pin(open_ref(publisher)) and
                publisher['edition'] == EDITION and publisher['source_chapter'] == CHAPTER_SHA and
                publisher['public_filename'] == NEW_PDFS[0] and publisher['control_sha256'] == referee['sha256'] and
                exact_directory(Path(final['final_directory']), (*PDFS, 'BINDINGS.json')) ==
                {**public_pins, 'BINDINGS.json': reference_bits(signed['sources'])} and
                decision['four_distinct_links_with_six_private_annotations_corrected'] is True and
                all(public_pins[name] == attachments[name] for name in PDFS if name != NEW_PDFS[0]),
                'Prepare only the signed public PDF and the four inherited download bytes.')
        verify_public_pdf(portable / NEW_PDFS[0], historical)
        attachments = public_pins
        refs['final_downloads'] = ref(final_file)
        refs['public_pdf_preflight'] = ref(PDF_PREFLIGHT)
        refs['public_print_referee'] = ref(Path(referee['path']))
        refs['publisher_print_selection'] = ref(chapter_print)
        refs['canonical_uri_verification'] = ref(Path(final['uri_verification']['path']))
        open_ref(final['uri_verification'])
        checked = BUILD / 'PUBLIC-NATIVE-AND-SEMANTIC.json'
        semantic = read(checked)
        require(semantic['status'] == 'VERIFIED_NINETEEN_NATIVE_CHAPTERS_AND_FIVE_PUBLIC_PRINTS' and
                semantic['source_id'] == record['content_id'] and semantic['pdf_bindings'] == attachments and
                semantic['native_files'] == raw_pins, 'The exact native reader and print check differs.')
        refs['native_semantic_check'] = ref(checked)
    return {'source_id': record['content_id'], 'source_files': source_files,
            'raw_files': raw_pins, 'attachments': attachments, 'headings': record['headings'],
            'native_permalink': permalink, 'evidence': refs}


def prepare_parent(commit, website, official):
    """Read the actual v29 Git commit and its exact pre-publication bytes without waiting for replay."""
    baseline = LANE / 'full-issue'
    hosted = baseline / 'hosted/quantum-holography'
    parent_files = exact_directory(hosted, previous.PUBLIC_FILES)
    verify_commit(commit, previous.PARENT, parent_files, website)
    require({name: parent_files[name] for name in previous.PDF_FILES} ==
            {name: official['attachments'][name] for name in previous.PDF_FILES},
            'An inherited v29 PDF changed.')
    source_selection = LANE / 'checks/final-source-selection.json'
    selection = read(source_selection)
    prior_tree = Path(selection['source_root'])
    require(selection['edition'] == PARENT_EDITION and len(selection['files']) == 65 and
            selection['files'] == inventory(prior_tree) == inventory(baseline / 'workspace'),
            'The parent build does not use the selected v29 source.')
    changes = read(Path(official['evidence']['working_source']['path']))['changed_from_v29']
    observed = {name for name, value in official['source_files'].items()
                if value != selection['files'].get(name)}
    require(observed == set(changes) and set(selection['files']) <= set(official['source_files']),
            'The successor changes an unregistered v29 source member.')
    for name, step in changes.items():
        require(step == {'before': selection['files'].get(name), 'after': official['source_files'][name]},
                f'The official cumulative source delta disagrees at {name}.')

    controls = baseline / 'reader-compatibility'
    reviewed = LANE / 'history/reconstruction-history.json'
    proof = LANE / 'history/BOOKMARK-CHECK.json'
    history, decisions = previous.check_effective_history(
        baseline, {'bookmark_history': pin(io.read_stable(controls / 'working-history.json'))},
        reviewed, proof)
    raw_index = ref(baseline / 'public/reader-index.js')
    row = {'edition': 'v29', 'commit': commit, 'repository': '/Users/raeez/www',
           'pins': {name: parent_files[name] for name in READER},
           'rawIndex': {'path': 'controls/v29-raw-index.js', **reference_bits(raw_index)}}
    return history, row, decisions, controls, raw_index, parent_files, ref(source_selection)


def bind_history(history_file, previous_history, row):
    catalog = read(history_file)
    expected = dict(previous_history, editions=[*previous_history['editions'], row])
    require(len(catalog['editions']) == len(expected['editions']) and
            len({entry['edition'] for entry in catalog['editions']}) == len(expected['editions']),
            'Expected the inherited indexed catalog plus one real v29 row.')
    for actual, want in zip(catalog['editions'], expected['editions']):
        for role in ('rawIndex', 'receipt'):
            if role in want:
                evidence = actual[role]
                require(reference_bits(evidence) == reference_bits(want[role]) ==
                        pin(io.read_stable(history_file.parent / evidence['path'])),
                        f'Historical address input changed at {want["edition"]}.')
                evidence['path'] = want[role]['path']
    require(catalog == expected, 'The effective catalog changed v29 or an earlier address record.')
    return expected


def run_check(label, arguments, directory):
    with (directory / (label + '.log')).open('xb') as log:
        subprocess.run([str(arg) for arg in arguments], cwd=HERE, check=True, stdout=log,
                       stderr=subprocess.STDOUT,
                       env=dict(os.environ, TMPDIR=str(directory), PYTHONDONTWRITEBYTECODE='1'))


def check_reader(site, output, decisions, headings):
    legacy_links = previous.check_reader(site, output, decisions)
    from lxml import html
    book = html.fromstring(io.read_stable(site / 'index.html'))
    chapters = book.xpath('//article[@data-chapter]/@id')
    require(chapters == [f'ch{i:02}' for i in range(1, 20)], 'The issue does not have 19 ordered chapters.')
    for heading in headings:
        require(len(book.xpath('//*[@id=$id]', id=heading['id'])) == 1,
                f"The reader lost the anchor {heading['id']}.")
    for name, region in zip(NEW_PDFS, ('ch19', 'ch19-diagonal-and-trace')):
        links = book.xpath('//a[@href=$path]', path=name)
        require(len(links) == 1 and links[0].get('type') == 'application/pdf' and
                links[0].text_content().strip() and links[0].xpath('ancestor::*[@id=$id]', id=region) and
                not links[0].xpath('ancestor-or-self::*[@hidden or @aria-hidden="true" or self::template]'),
                f'Missing the unique readable link for {name} in {region}.')
    for url in read(PDF_PREFLIGHT)['validated_canonical_destinations'].values():
        anchor = url.split('#', 1)[1]
        require(len(book.xpath('//*[@id=$id]', id=anchor)) == 1,
                f'The corrected chapter print links to missing anchor {anchor}.')
    index = io.read_stable(site / 'reader-index.js').decode()
    prefix = 'window.QH_READER_INDEX = '
    require(index.startswith(prefix), 'Unexpected native index format.')
    units = json.JSONDecoder().raw_decode(index, len(prefix))[0]['units']
    indexed = {unit['id'] for unit in units if unit.get('group') == 'ch19' and unit['page'] == 'index.html'}
    require({'ch19', *(heading['id'] for heading in headings)} <= indexed,
            'The search index is missing authored Chapter 19 anchors.')
    return legacy_links


def write_bytes(path, data):
    if path.exists():
        require(io.read_stable(path) == data, f'Existing bytes differ at {path}.')
    else:
        io.write_new(path, data, 0o600)


def export_handoff(record, work):
    staged = work / 'hosted-staging'
    if not HOSTED.exists():
        require(exact_directory(staged, FILES) == record['hosted_files'], 'The sealed host export changed.')
        HOSTED.parent.mkdir(parents=True, exist_ok=True)
        os.rename(staged, HOSTED)
        io.fsync_directory(HOSTED.parent)
    require(exact_directory(HOSTED, FILES) == record['hosted_files'], 'The official host export differs.')
    write_once(PREPARED, record)
    semantic = NEXT / 'hosted-semantic.json'
    write_bytes(semantic, open_ref(record['semantic_receipt']))
    print(json.dumps({'status': record['status'], 'hosted': record['hosted'],
                      'semantic': ref(semantic), 'receipt': ref(PREPARED)}, indent=2))


def prepare(args):
    require(bool(re.fullmatch('[a-z0-9-]+', args.run)), 'Use a durable run label.')
    work = HERE / 'builds' / args.run
    handoff = work / 'build/SEALED-HOST-EXPORT.json'
    if handoff.is_file():
        record = read(handoff)
        require(record['parent'] == args.v29_commit and Path(record['build']) == work,
                'The previously sealed export is for another requested issue.')
        for key in ('build_receipt', 'history', 'semantic_receipt', 'link_receipt'):
            open_ref(record[key])
        export_handoff(record, work)
        return
    require(not PREPARED.exists() and not HOSTED.exists(), 'The completed official host export already exists.')
    release = args.portable.resolve(strict=True)
    official = official_build(args.final_downloads.resolve(strict=True), release)
    previous_history, row, decisions, controls, raw_index, parent_files, parent_selection = prepare_parent(
        args.v29_commit, args.website, official)
    history_file = args.history.resolve(strict=True)
    catalog = bind_history(history_file, previous_history, row)
    amended = args.amendment.resolve(strict=True)
    amendment = read(amended)
    raw = FINISH / 'public'
    portable = exact_directory(release, FILES)
    portable_marker = BUILD / 'PORTABLE-NINE.json'
    marker = read(portable_marker)
    require(marker['status'] == 'NINE_VERIFIED_PORTABLE_FILES' and Path(marker['source']) == release and
            marker['files'] == portable and marker['history'] == pin(io.read_stable(history_file)) and
            marker['amendment'] == pin(io.read_stable(amended)) and
            marker['public_print'] == reference_bits(official['evidence']['final_downloads']),
            'The official nine-file portable seal differs from the requested release inputs.')
    official['evidence']['official_portable'] = ref(portable_marker)
    require(amendment['schema'] == 'reader-address-amendment/3' and amendment['status'] == 'PASS' and
            amendment['inputs']['historic'] == read(history_file) and
            amendment['inputs']['raw'] == {name: official['raw_files'][name] for name in READER} and
            {r['page']: r['after'] for r in amendment['results']} ==
            {name: portable[name] for name in READER if name.endswith('.html')} and
            amendment['outputIndex'] == portable['reader-index.js'] and
            {name: portable[name] for name in PDFS} == official['attachments'],
            'The actual bookmark amendment does not bind these source, history and output bytes.')

    work.mkdir(parents=True, exist_ok=False)
    EVIDENCE.mkdir(exist_ok=True)
    operator = work / 'build/registration-program.py'
    write_bytes(operator, io.read_stable(Path(__file__).resolve()))
    official['evidence']['registration_program'] = ref(operator)
    shutil.copytree(SOURCE, work / 'workspace')
    shutil.copytree(raw, work / 'public')
    shutil.copytree(release, work / 'release')
    require(inventory(work / 'workspace') == official['source_files'] and
            exact_directory(work / 'public', FILES) == official['raw_files'] and
            exact_directory(work / 'release', FILES) == portable, 'Private archive inputs changed during capture.')
    compatibility = work / 'reader-compatibility'
    shutil.copytree(controls, compatibility, ignore=shutil.ignore_patterns(
        'working-history.json', 'current-history.json', 'check-amendment.cjs'))
    fixture_record = BUILD / 'INHERITED-RUNTIME.json'
    fixture = read(fixture_record)
    checker = Path(fixture['target'])
    require(checker == FINISH / 'reader-compatibility/tools/check-amendment.cjs' and
            fixture['fixture'] == pin(io.read_stable(checker)) ==
            pin(io.read_stable(Path(fixture['source']))),
            'The inherited native reader replay check differs from the fixture owner’s exact bytes.')
    write_bytes(compatibility / 'tools/check-amendment.cjs', io.read_stable(checker))
    official['evidence']['runtime_fixture'] = ref(checker)
    official['evidence']['runtime_fixture_record'] = ref(fixture_record)
    write_bytes(compatibility / row['rawIndex']['path'], open_ref(raw_index))
    require(pins(compatibility, catalog['controls']) == catalog['controls'], 'Archived control hashes changed.')
    for member in catalog['editions']:
        for role in ('rawIndex', 'receipt'):
            if role in member:
                entry = member[role]
                require(pin(io.read_stable(compatibility / entry['path'])) == reference_bits(entry),
                        f'Archived address inventory differs for {member["edition"]}.')
    history_bytes = native.encode(catalog)
    write_bytes(compatibility / 'working-history.json', history_bytes)
    report = {'edition': EDITION, 'frozen': False, 'bookmark_history': pin(history_bytes),
              'files': {name: portable[name] for name in READER}, 'attachments': official['attachments'],
              'working_native_source': official['evidence']['working_source'],
              'raw_address_amendment': ref(amended)}
    write_once(work / 'build/READER-BUILD.json', report)
    write_bytes(work / 'build/audit/audit.json', open_ref(official['evidence']['audit']))

    hosted = work / 'hosted-staging'
    headers = exporter.read_headers()
    for name in FILES:
        payload = io.read_stable(work / 'release' / name)
        mounted = exporter.transform(name, payload, headers) if name in READER else payload
        write_bytes(hosted / name, mounted)
    links = check_reader(hosted, work / 'build/HOSTED-LINKS.json', decisions, official['headings'])
    verified = work / 'build/HOSTED-SEMANTIC.json'
    run_check('semantic', [sys.executable, '-B', LANE / 'verify_issue_pages.py', hosted,
                           SOURCE, verified, '--edition', EDITION], work / 'build')
    hosted_pins = exact_directory(hosted, FILES)
    record = {'status': 'PRIVATE_PREPUBLICATION_V30', 'edition': EDITION, 'parent': args.v29_commit,
              'website_worktree': str(args.website.resolve()), 'parent_files': parent_files,
              'parent_source': parent_selection, 'parent_history': row,
              'build': str(work), 'hosted': str(HOSTED), 'official': official,
              'portable_files': portable, 'hosted_files': hosted_pins,
              'history': ref(compatibility / 'working-history.json'), 'old_bookmarks': decisions,
              'build_receipt': ref(work / 'build/READER-BUILD.json'),
              'link_receipt': links, 'semantic_receipt': ref(verified)}
    # Distinct private run directories retain any failed attempt. A successful handoff is immutable.
    write_once(handoff, record)
    export_handoff(record, work)


def prepared():
    plan = read(PREPARED)
    require(plan['status'] == 'PRIVATE_PREPUBLICATION_V30' and plan['edition'] == EDITION,
            'Use the exact completed prepublication receipt.')
    for key in ('history', 'build_receipt', 'link_receipt', 'semantic_receipt', 'parent_source'):
        open_ref(plan[key])
    for value in plan['official']['evidence'].values():
        open_ref(value)
    work = Path(plan['build'])
    require(inventory(work / 'workspace') == plan['official']['source_files'] and
            exact_directory(work / 'public', FILES) == plan['official']['raw_files'] and
            exact_directory(work / 'release', FILES) == plan['portable_files'] and
            exact_directory(Path(plan['hosted']), FILES) == plan['hosted_files'] and
            pin(io.read_stable(work / 'reader-compatibility/tools/check-amendment.cjs')) ==
            reference_bits(plan['official']['evidence']['runtime_fixture']),
            'Prepared source or public file bytes changed.')
    return plan


def direct_public_receipt(path, commit, edition, files):
    receipt = read(path)
    require(receipt['edition'] == edition and receipt['commit'] == commit and
            receipt['chapters'] == (19 if edition == EDITION else 18),
            f'The publisher receipt is not for the live {edition} commit.')
    expected = {'': files['index.html'], **files}
    rows = {row['path']: row for row in receipt['files']}
    require(len(receipt['files']) == len(rows) and set(rows) == set(expected),
            f'Missing or duplicate HTTPS readback routes for {edition}.')
    converted = []
    for name, file_pin in expected.items():
        row = rows[name]
        require(row['status'] == 200 and row['url'] == SITE + name and reference_bits(row) == file_pin and
                (not name.endswith('.pdf') or row.get('content_type') == 'application/pdf'),
                f'No exact official HTTPS readback for {SITE + name}.')
        converted.append({'path': previous.MOUNT + name, 'http': 200, 'exact': True,
                          'served_sha256': file_pin['sha256'], 'expected_sha256': file_pin['sha256'],
                          'bytes': file_pin['bytes'], 'content_type': row.get('content_type')})
    return converted


def live_commit(plan, commit):
    website = Path(plan['website_worktree'])
    require(git('rev-parse', 'refs/remotes/origin/master', website=website).decode().strip() == commit,
            'The local fetched official reference does not designate this exact v30 commit.')
    return verify_commit(commit, plan['parent'], plan['hosted_files'], website)


def record_public(args):
    plan = prepared()
    changed = live_commit(plan, args.commit)
    pages_path = args.pages.resolve(strict=True)
    pages = read(pages_path)
    require(pages['status'] == 'built' and pages['commit'] == args.commit,
            'Provide the publisher’s filtered Pages build for this exact v30 commit.')
    parent = args.v29_semantic.resolve(strict=True)
    direct_public_receipt(parent, plan['parent'], PARENT_EDITION, plan['parent_files'])
    semantic = args.semantic.resolve(strict=True)
    result = direct_public_receipt(semantic, args.commit, EDITION, plan['hosted_files'])
    require(read(semantic)['chapter19']['source_sha256'] == CHAPTER_SHA and
            read(semantic)['chapter19']['chapter_url'] == SITE + '#ch19',
            'The actual served chapter identity differs.')
    write_once(EVIDENCE / 'PUSH.json', {
        'site': 'primary', 'repository': 'raeez/www', 'branch': 'master', 'previous': plan['parent'],
        'git_first_parent': plan['parent'], 'commit': args.commit, 'changed_paths': changed,
        'files': plan['hosted_files'], 'portable_files': plan['portable_files'],
    })
    record = {'url': SITE, 'edition': EDITION, 'commit': args.commit, 'parent': plan['parent'],
              'utc': read(semantic)['verified_utc'], 'pages': pages, 'pages_receipt': ref(pages_path),
              'public_readbacks': result, 'exact_live_semantics': ref(semantic),
              'v29_predecessor_readback': ref(parent), 'prepublication': ref(PREPARED)}
    print(write_once(EVIDENCE / 'PUBLICATION.json', record)['sha256'])


def recorded_public(plan, commit, digest):
    path = EVIDENCE / 'PUBLICATION.json'
    require(ref(path)['sha256'] == digest, 'Use the exact completed v30 publication receipt.')
    record = read(path)
    require(record['commit'] == commit and record['parent'] == plan['parent'] and
            record['url'] == SITE and record['prepublication'] == ref(PREPARED) and
            record['pages']['commit'] == commit and record['pages']['status'] == 'built' and
            io.decode(open_ref(record['pages_receipt'])) == record['pages'],
            'Live edition evidence has changed.')
    for key in ('exact_live_semantics', 'v29_predecessor_readback'):
        open_ref(record[key])
    direct_public_receipt(Path(record['v29_predecessor_readback']['path']),
                          plan['parent'], PARENT_EDITION, plan['parent_files'])
    require(record['public_readbacks'] == direct_public_receipt(Path(record['exact_live_semantics']['path']),
                                                commit, EDITION, plan['hosted_files']),
            'Publication receipt differs from the exact joined HTTPS readback.')
    push = read(EVIDENCE / 'PUSH.json')
    require(push['changed_paths'] == live_commit(plan, commit) and push['commit'] == commit and
            push['previous'] == push['git_first_parent'] == plan['parent'] and
            push['files'] == plan['hosted_files'] and push['portable_files'] == plan['portable_files'],
            'The canonical publication commit, ancestry or byte inventory changed.')


def parent_marker(plan):
    path = PARENT_ARCHIVE / 'MANIFEST.json'
    prior = read(path)
    require(prior['edition'] == PARENT_EDITION and prior['commit'] == plan['parent'] and
            prior['public_exports']['primary']['files'] | prior['public_exports']['primary']['attachments']
            == plan['parent_files'],
            'The canonical v29 native parent archive is absent or differs from the real v29 commit.')
    manifest = ref(path)
    selection = {'edition': PARENT_EDITION, 'commit': plan['parent'],
                 'manifest': PARENT_EDITION + '/MANIFEST.json', 'sha256': manifest['sha256']}
    sources = io.decode(open_ref(plan['parent_source']))
    require(inventory(PARENT_ARCHIVE / 'source-tree') == sources['files'] and
            read(PARENT_ARCHIVE / 'compatibility/current-history.json') == io.decode(open_ref(plan['history'])),
            'The canonical v29 source/archive history differs from the actual v30 compatibility basis.')
    require(pin(io.read_stable(previous.DRIVER)) ==
            pin(io.read_stable(PARENT_ARCHIVE / 'tools/build_reader.py')),
            'The normal driver differs from its inherited canonical v29 tool.')
    return selection, manifest


def parent_replay_capture(plan, selection, path):
    path = path.resolve(strict=True)
    require(path.parent == LANE / 'registration/native-evidence', 'Use the v29 operator’s native capture.')
    capture = read(path)
    require(capture['schema'] == 'qh-v29-default-capture/1' and capture['edition'] == PARENT_EDITION and
            capture['commit'] == plan['parent'] and capture['selector'] == selection,
            'The v29 normal replay must have captured this exact selected edition before promotion.')
    open_ref(capture['source_manifest'])
    workspace = Path(capture['workspace'])
    parent_sources = io.decode(open_ref(plan['parent_source']))['files']
    require(workspace.is_absolute() and inventory(workspace) == parent_sources and
            io.decode(open_ref(capture['working_history'])) == io.decode(open_ref(plan['history'])),
            'The v29 normal replay capture differs from the inherited source and history.')
    return ref(path)


def seal_native(plan):
    selection, manifest = parent_marker(plan)
    require(read(previous.SELECTOR) == selection, 'Only the actual selected v29 can seed native v30.')
    raw_registry = open_ref(plan['official']['evidence']['registry'])
    record = {'status': 'VERIFIED_PRIVATE_PUBLIC_PAYLOAD', 'issued_edition_number': 30,
              'public_files': {name: plan['portable_files'][name] for name in READER},
              'verified_reader_attachments': plan['official']['attachments'],
              'attachment_bindings': pin(raw_registry), 'build_evidence': plan['build_receipt'],
              'prepublication': ref(PREPARED), 'v29_manifest': manifest,
              'native_permanent_link': plan['official']['native_permalink']}
    ready = EVIDENCE / 'READY.json'
    write_once(ready, record)
    native.prepare(SimpleNamespace(build=Path(plan['build']), ready=ready, hosted=Path(plan['hosted'])))
    write_bytes(DRAFT / 'attachments/BINDINGS.json', raw_registry)
    for role, evidence in plan['official']['evidence'].items():
        if role != 'historical_chapter_pdf':
            write_bytes(DRAFT / 'verification/chapter19' / (role + '-' + Path(evidence['path']).name),
                        open_ref(evidence))
    manifest = read(DRAFT / 'SOURCE-MANIFEST.json')
    rows = {row['path'].removeprefix('source-tree/'): reference_bits(row) for row in manifest['files']}
    staging = read(DRAFT / 'verification/STAGING.json')
    require(rows == inventory(DRAFT / 'source-tree') == plan['official']['source_files'] and
            manifest['content_id'] == staging['content_id'] == plan['official']['source_id'] and
            staging['edition'] == EDITION and staging['parent'] == selection and
            staging['attachments'] == plan['official']['attachments'] and
            pin(io.read_stable(DRAFT / 'compatibility/tools/check-amendment.cjs')) ==
            reference_bits(plan['official']['evidence']['runtime_fixture']),
            'The private native archive missed exact source, revision parent or attachment bytes.')
    print(ref(DRAFT / 'verification/STAGING.json')['sha256'])


def replay(plan, directory, frozen):
    label = 'frozen' if frozen else 'default'
    output = directory / label
    receipt = output / 'build/READER-BUILD.json'
    if not receipt.is_file():
        require(not output.exists(), f'Preserve the interrupted replay; select a fresh replay label: {output}.')
        script = TARGET / 'rebuild.py' if frozen else previous.DRIVER
        native_run = io.decode(open_ref(plan['official']['evidence']['native_start']))
        compiler_python = Path(native_run['command'][0])
        require(compiler_python.is_absolute() and compiler_python.is_file(),
                'The interpreter used by the official native compiler is unavailable.')
        command = [str(compiler_python), '-B', str(script), str(output)]
        with (directory / (label + '.log')).open('xb') as log:
            subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, cwd=previous.REPO, check=True)
    result = read(receipt)
    require(result['edition'] == EDITION and result['frozen'] is frozen and
            result['files'] | result['attachments'] == plan['portable_files'] ==
            exact_directory(output / 'release', FILES),
            f'The {label} native replay differs from the nine published portable inputs.')
    headers = exporter.read_headers()
    for name in FILES:
        data = io.read_stable(output / 'release' / name)
        projected = exporter.transform(name, data, headers) if name in READER else data
        require(pin(projected) == plan['hosted_files'][name],
                f'The {label} native replay produces different hosted bytes for {name}.')
    return ref(receipt)


def promote(args):
    # The parent releases this lock after capturing its normal replay inputs.
    with (LANE / 'registration/.registration.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        promote_registered(args)


def promote_registered(args):
    require(bool(re.fullmatch('[a-z0-9-]+', args.replay_run)), 'Use a durable replay label.')
    plan = prepared()
    recorded_public(plan, args.commit, args.publication_sha256)
    before = previous.authoring_identity()
    parent, parent_manifest = parent_marker(plan)
    capture = parent_replay_capture(plan, parent, args.v29_capture)
    selection = read(previous.SELECTOR)
    if selection == parent:
        seal_native(plan)
        write_once(EVIDENCE / 'ROLLBACK-BASIS.json', {
            'selector': selection, 'selector_before': ref(previous.SELECTOR),
            'v29_manifest': parent_manifest, 'v30_staging': ref(DRAFT / 'verification/STAGING.json'),
            'v29_normal_replay_capture': capture,
            'journal': str(HERE / 'native-archives' / ('install-' + EDITION) / 'journal.jsonl'),
        })
    else:
        require(selection['edition'] == EDITION and selection['commit'] == args.commit,
                'The native selector changed before v30 promotion.')

    native.HOST = Path(plan['website_worktree'])
    options = dict(archive=DRAFT, issue=EVIDENCE)
    native.install(SimpleNamespace(**options, install=False))
    native.install(SimpleNamespace(**options, install=True))
    installed = read(TARGET / 'MANIFEST.json')
    selector = {'edition': EDITION, 'commit': args.commit, 'manifest': EDITION + '/MANIFEST.json',
                'sha256': ref(TARGET / 'MANIFEST.json')['sha256']}
    require(read(previous.SELECTOR) == selector and installed['primary_parent_commit'] == plan['parent'] and
            installed['public_exports']['primary']['files'] | installed['public_exports']['primary']['attachments']
            == plan['hosted_files'] and inventory(TARGET / 'source-tree') == plan['official']['source_files'],
            'The registered edition, native source or PDFs differ from the published successor.')
    require(all(pin(io.read_stable(previous.REPO / path)) == value
                for path, value in plan['official']['source_files'].items()),
            'The editable native source differs from the issued archive.')

    directory = HERE / 'replays' / args.replay_run
    directory.mkdir(parents=True, exist_ok=True)
    frozen = replay(plan, directory, True)
    default = replay(plan, directory, False)
    require(read(previous.SELECTOR) == selector and previous.authoring_identity() == before and
            ref(PARENT_ARCHIVE / 'MANIFEST.json') == parent_manifest,
            'The existing authoring identity or an immutable predecessor changed.')
    history = read(TARGET / 'compatibility/current-history.json')
    previous_history = io.decode(open_ref(plan['history']))
    require(history['editions'][:-1] == previous_history['editions'] and
            history['editions'][-1]['edition'] == 'v30' and history['editions'][-1]['commit'] == args.commit,
            'The native registration did not append exactly the issued v30 address inventory.')
    record = {'edition': EDITION, 'commit': args.commit, 'previous': plan['parent'],
              'native_archive': str(TARGET), 'native_manifest': ref(TARGET / 'MANIFEST.json'),
              'native_source': ref(TARGET / 'SOURCE-MANIFEST.json'), 'selection': selector,
              'permanent_chapter_reading': plan['official']['native_permalink'],
              'official_chapter': SITE + '#ch19',
              'immutable_website_commit': 'https://github.com/raeez/www/commit/' + args.commit,
              'website': ref(EVIDENCE / 'PUBLICATION.json'), 'default': default, 'frozen': frozen,
              'v29_normal_replay_capture': capture,
              'five_attachment_bindings': ref(TARGET / 'attachments/BINDINGS.json'),
              'preserved_authoring': before}
    installed = EVIDENCE / 'INSTALLED-AND-REPLAYED.json'
    print(write_once(installed, record)['sha256'])
    write_once(EVIDENCE / 'OWNER-HANDOFF.json', {
        'edition': EDITION, 'commit': args.commit, 'parent': plan['parent'], 'proof': ref(installed),
        'archive': str(TARGET), 'canonical': SITE, 'native_permanent_chapter': record['permanent_chapter_reading'],
    })


def preflight(args):
    result = official_build()
    history, row, _, _, _, _, _ = prepare_parent(args.v29_commit, args.website, result)
    print(json.dumps({'status': 'WORKING_SOURCE_AND_ACTUAL_V29_GIT_BOUND',
                      'parent': row, 'prior_editions': len(history['editions']),
                      'source_members': len(result['source_files']), 'source_id': result['source_id'],
                      'raw_reader': {name: result['raw_files'][name] for name in READER},
                      'historical_print_only': result['attachments'][NEW_PDFS[0]],
                      'native_chapter_permalink': result['native_permalink']}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)

    def with_parent(command):
        command.add_argument('--v29-commit', required=True)
        command.add_argument('--website', type=Path, default=previous.GIT_WORKTREE)

    inspect = commands.add_parser('preflight')
    with_parent(inspect)
    inspect.set_defaults(function=preflight)
    stage = commands.add_parser('prepare')
    with_parent(stage)
    stage.add_argument('--history', type=Path, required=True)
    stage.add_argument('--amendment', type=Path, required=True)
    stage.add_argument('--portable', type=Path, default=FINISH / 'release')
    stage.add_argument('--final-downloads', type=Path, default=BUILD / 'FINAL-FIVE.json')
    stage.add_argument('--run', default='first')
    stage.set_defaults(function=prepare)

    public = commands.add_parser('record-public')
    public.add_argument('--commit', required=True)
    public.add_argument('--pages', type=Path, required=True)
    public.add_argument('--semantic', type=Path, required=True)
    public.add_argument('--v29-semantic', type=Path, default=LANE / 'checks/first-public-semantic.json')
    public.set_defaults(function=record_public)

    seal = commands.add_parser('seal-native', help='prepare the private archive against the actual v29 selector')
    seal.set_defaults(function=lambda _: seal_native(prepared()))

    install = commands.add_parser('promote')
    install.add_argument('--commit', required=True)
    install.add_argument('--publication-sha256', required=True)
    install.add_argument('--replay-run', default='first')
    install.add_argument('--v29-capture', type=Path,
                         default=LANE / 'registration/native-evidence/DEFAULT-CAPTURED.json')
    install.add_argument('--install-native', action='store_true', required=True,
                         help='Invoke only under the original publisher’s explicit native transition authority.')
    install.set_defaults(function=promote)
    args = parser.parse_args()
    if args.command == 'preflight':
        args.function(args)
        return
    with (HERE / '.registration.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        args.function(args)


if __name__ == '__main__':
    main()


