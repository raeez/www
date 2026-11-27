"""Install a privately reproduced reader after its official Git and HTTPS readback."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode=True
import reviewed_io as io
import host_issue as hosts

ED=Path('materials/processed/qh-attack-heal-20261116/integration/ega-reader-integration-20261117')
FILES=('index.html','reference.html','atlas.html','reader-index.js')
PAGE='content/quantum-holography-status/page.json'
FRONT='content/quantum-holography-status/reader-data/manifest.json'
PRIMARY=Path('/Users/raeez/www')
OFFICIAL='https://raeez.com/quantum-holography/'
MOUNT='quantum-holography'

def signature(raw):
    return {'sha256':sha256(raw).hexdigest(),'bytes':len(raw)}

def read(path,wanted=None):
    value=io.read_stable(path)
    if wanted is not None:io.require(signature(value)=={k:wanted[k] for k in ('sha256','bytes')},'Unexpected '+str(path))
    return value

def obj(path,wanted=None):
    return io.decode(read(path,wanted))

def keeponce(path,data):
    if path.exists():io.require(read(path)==data,'Existing receipt differs in '+str(path))
    else:io.write_new(path,data)

def git(*args):
    return subprocess.check_output(['git','--no-optional-locks','-C',str(PRIMARY),*args])

def verify(args):
    edition=args.edition.resolve(strict=True);ver=edition/'verification';root=edition.parents[len(ED.parts)]
    io.require(edition==root/ED/'release-v25','Select the release-v25 archive in a full authoring checkout')
    order=edition/'LOCAL-READY.json';io.require(io.sha(read(order))==args.accepted_digest,'Wrong verified edition hash')
    ready=obj(order);io.require(ready['status']=='READY_FOR_ISSUE' and ready['edition']=='release-v25','Incomplete issue archive')
    for rel,expected_pin in ready['receipts'].items():read(edition/io.relative(rel),expected_pin)
    expected=obj(edition/'EXPECTED-PUBLIC.json')
    host_guard=hosts.check_package(args.host_package_sha256)
    host_dir=root/ED/'host-exports/v25'
    io.require(io.sha(read(host_dir/'HOST-READY.json'))==args.host_package_sha256,'Install the exact checked host export alongside the pure edition')
    for relative,val in host_guard['files'].items():read(host_dir/io.relative(relative),val)
    role_files=obj(host_dir/'MOUNTED-REPRODUCTION.json')['variants'][ready['scope']]
    io.require(role_files['pure']==expected,'Hosting package does not describe the signed pure edition')
    mounted=role_files['hosted']
    baseline=obj(ver/'V24-ISSUED-BASELINE.json');previous=edition.parent/'release-v24'
    prev_commit=baseline['commit'];parent_src=obj(previous/'SOURCE-MANIFEST.json',baseline['source_manifest'])
    prior=obj(previous/'MANIFEST.json',baseline['manifest']);prior_c=obj(previous/'compatibility/current-history.json',baseline['current_catalog'])
    frozen=obj(edition/'compatibility/history.json')
    io.require(prior_c==obj(ver/'PREDECESSOR-ISSUED-HISTORY.json') and prev_commit==ready['base_public_commit']==prior['commit'],'Wrong issued native parent')
    io.require(prior_c['editions']==frozen['editions'] and prior_c['reviewedPassageSuccessors']==frozen['reviewedPassageSuccessors'],'Inherited addresses changed')
    if ready['scope']=='math-notices':
        wanted='controls/reader-book-math-notices.js'
        expected_catalog=io.decode(io.enc(prior_c));expected_catalog['controls'][wanted]=signature(read(edition/'compatibility'/wanted));expected_catalog['runtime']['bookReader']=wanted
        io.require(frozen==expected_catalog and obj(ver/'NOTICE-BROWSER.json')['files']==expected,'Scoped book runtime discrepancy')
    else:io.require(ready['scope']=='core' and frozen==prior_c,'Unexpected core history or scope')
    for name in frozen['runtime'].values():read(edition/'compatibility'/io.relative(name),frozen['controls'][name])
    source=obj(edition/'SOURCE-MANIFEST.json');plan=obj(ver/'NATIVE-INSTALL-PLAN.json')['files'];native_src=obj(ver/'NATIVE-SOURCE.json')
    io.require(set(plan)=={PAGE,FRONT} and len(source['files'])==56 and source['content_id']==ready['content_id'],'Source inventory or identity mismatch')
    read(root/'compiler/build-quantum-holography-reader.py',native_src['entrypoint'])
    for key in ['scientific_horizon_utc','base_scientific_census_utc','targeted_accessions','targeted_accession']:
        io.require(source[key]==parent_src[key]==prior[key],'Changed scientific accession metadata '+key)
    surfaces=obj(ver/'SURFACES.json')
    io.require(surfaces['status']=='PASS' and surfaces['files']==expected and surfaces['predecessor']==baseline['four_files'],'Inconsistent structural proof')
    for n in FILES[:3]:
        target=OFFICIAL+('' if n=='index.html' else n)
        io.require(surfaces['pages'][n]['canonical']==surfaces['pages'][n]['og_url']==target,'Wrong canonical or sharing metadata')
    io.require(surfaces['pages']['index.html']['same_signed_rendered_paragraphs']==53 and len(surfaces['pages']['index.html']['local_links'])==42,'The accepted opening differs')
    source_bound=obj(ver/'REPRODUCTION.json');io.require(source_bound['status']=='PASS' and source_bound['files']==expected,'Wrong final reproduction')
    for name,is_frozen in [('NORMAL-CLI.json',False),('FROZEN-CLI.json',True)]:
        sub=obj(ver/name);io.require(sub['edition']=='release-v25' and sub['frozen'] is is_frozen and sub['files']==expected,'Wrong build identity')
    raw_record=source_bound['raw']['reader-index.js']
    read(edition/'compatibility/controls/v25-raw-index.js',raw_record)
    old_pins={str(io.relative(q['path']).relative_to('source-tree')):{k:q[k] for k in ('sha256','bytes')} for q in parent_src['files']}
    new_pins={};changed={}
    for r in source['files']:
        rel=io.relative(r['path']).relative_to('source-tree')
        body=read(edition/'source-tree'/rel,r);state=read(root/rel)
        io.require((root/rel).resolve(strict=True)==root/rel,'Unexpected editable path indirection '+str(rel))
        new_pins[str(rel)]=signature(body)
        if str(rel) in plan:
            spec=plan[str(rel)];io.require(old_pins[str(rel)]==spec['from'] and signature(body)==spec['to'] and signature(state) in (spec['from'],spec['to']),'Editable source drift '+str(rel))
            changed[root/rel]=(state,body)
        else:io.require(body==state,'Unrelated authoring source drift '+str(rel))
    io.require(old_pins.keys()==new_pins.keys() and {k for k in new_pins if new_pins[k]!=old_pins[k]}==set(plan),'Edition diff does not match guarded plan')
    before_page=obj(previous/'source-tree'/PAGE);after_page=obj(edition/'source-tree'/PAGE)
    io.require(before_page['site']=='https://research.momentum.inc/quantum-holography','Wrong previous official metadata')
    before_page['site']=OFFICIAL.rstrip('/');io.require(before_page==after_page,'Unexpected page metadata change')
    old_manifest=obj(previous/'source-tree'/FRONT);new_manifest=obj(edition/'source-tree'/FRONT)
    old_manifest['introduction']=read(ver/'AUTHORED-FRONT.md').decode()
    io.require(old_manifest==new_manifest,'Unrelated source manifest changes')
    pointer=edition.parent/'CURRENT-EDITION.json';initial_ptr=read(pointer)
    if args.source_only:
        io.require(signature(initial_ptr)==baseline['working_pointer'],'Install parent differs from v24')
        print('Verified private v25 source-only installation plan, complete 56-file source and optional runtime scope:',ready['scope']);return
    io.require(args.official_result is not None,'Pass the actual post-publication OFFICIAL-ISSUE.json')
    issue=obj(args.official_result)
    replay=hosts.verify_publication(edition,issue['primary']['commit'],issue['research']['commit'],args.host_package_sha256)
    io.require(issue.get('status')=='PASS' and all(issue.get(k)==v for k,v in replay.items()),'Actual dual-host publication differs from the checked roles')
    for role,site in [('primary',hosts.PRIMARY_URL),('research',hosts.RESEARCH_URL)]:
        for n in ('',*FILES):
            item=issue['bare_https'][site+n]
            io.require(item['status']==200 and {k:item[k] for k in ('bytes','sha256')}==issue[role]['files'][n or 'index.html'],'Bare HTTPS mismatch '+site+n)
    commit=issue['primary']['commit'];first_parent=issue['primary']['parent']
    row=hosts.catalog_entry(issue,raw_record)
    new_catalog={**frozen,'editions':[*frozen['editions'],row]};new_history=io.enc(new_catalog)
    hist=edition/'compatibility/current-history.json';initial_history=read(hist);io.require(initial_history in (io.enc(frozen),new_history),'Unexpected native history')
    after_ptr_shape={'edition':'release-v25','commit':commit,'manifest':'release-v25/MANIFEST.json'}
    parsed_ptr=io.decode(initial_ptr)
    io.require(signature(initial_ptr)==baseline['working_pointer'] or all(parsed_ptr.get(k)==v for k,v in after_ptr_shape.items()),'The native authoring issue changed')
    edges=obj(ver/'FINAL-LINKS.json');native=obj(ver/'NATIVE-AUDIT.json');notation=obj(ver/'FINAL-NOTATION.json');parity=obj(ver/'V25-PARITY.json')
    io.require(not native['failures'] and not native['math_errors'] and notation['status']=='PASS' and not edges['links']['bad_local_links'],'Invalid final Web output')
    copies={'verification/OFFICIAL-ISSUE.json':read(args.official_result)}
    for i,item in enumerate(issue.get('independent_receipts',[]),1):
        copies['verification/HOST-ISSUE-SOURCE-'+str(i)+'.json']=read(Path(item['path']),item)
    installed={'utc':issue['at_utc'],'public_commit':commit,'files':{k:{'native':str(root/k),'installed':v['to']} for k,v in plan.items()},'plan':signature(read(ver/'NATIVE-INSTALL-PLAN.json')),'reproduction':signature(read(ver/'REPRODUCTION.json'))}
    copies['verification/EDITABLE-INSTALLED.json']=io.enc(installed)
    digests={**{k:v['sha256'] for k,v in ready['receipts'].items()},'LOCAL-READY.json':args.accepted_digest,'compatibility/current-history.json':io.sha(new_history),**{k:io.sha(b) for k,b in copies.items()}}
    final={k:prior[k] for k in ('schema','scientific_horizon_utc','base_scientific_census_utc','targeted_accessions','targeted_accession','chapters','authored_opening_figure','source_complementary_receipts')}
    final.update(edition='v25',utc=issue['at_utc'],public_reader=OFFICIAL,commit=commit,base_public_commit=prev_commit,primary_parent_commit=first_parent,primary_repository=str(PRIMARY),content_id=source['content_id'],native_scope=ready['scope'],native_changed_files=sorted(plan),reviewed_passage_successors=frozen['reviewedPassageSuccessors'],reader_runtime=frozen['runtime'],native_inputs=len(source['files']),full_rebuild_matches_published=mounted,standalone_full_rebuild_matches_published=expected,historic_locators_verified=parity['historicLocatorsVerified'],search_units=parity['searchUnits'],local_links_checked=edges['links']['local_links_checked'],formulas_checked=native['math'],math_errors=native['math_errors'],prior_design_record=prior['native_visual_status'],native_visual_status='The signed introduction, byline, figure and local destinations were inspected in the desktop and narrow reader.',inherited_science_manifest={'edition':'v24',**baseline['manifest']},receipts=digests)
    final['public_exports']={
        'primary':{'url':hosts.PRIMARY_URL,'repository':issue['primary']['repository'],'commit':commit,'parent':first_parent,'files':mounted,'ordinary_host_export':'host-exports/v25/host-export.py','host_package_sha256':args.host_package_sha256},
        'standalone':{'url':hosts.RESEARCH_URL,'repository':issue['research']['repository'],'commit':issue['research']['commit'],'parent':issue['research']['parent'],'files':expected,'ordinary_build':'compiler/build-quantum-holography-reader.py'}}
    final['earlier_standalone_commits']={'research':issue['previous_standalone_research']['commit'],'primary':issue['previous_standalone_primary']['commit']}
    final_data=io.enc(final);manifest=edition/'MANIFEST.json';ptr_data=io.enc({**after_ptr_shape,'sha256':io.sha(final_data)})
    if manifest.exists():io.require(read(manifest)==final_data,'Existing installation differs from the verified issue')
    for rel,body in copies.items():
        f=edition/rel
        if f.exists():io.require(read(f)==body,'Existing issue record differs '+rel)
    if initial_ptr==ptr_data:
        io.require(initial_history==new_history and manifest.exists() and all(a==b for a,b in changed.values()),'Partially installed selected edition')
        print('Verified current primary issue',commit,io.sha(final_data));return
    io.require(signature(initial_ptr)==baseline['working_pointer'],'Native parent changed')
    if not args.install:
        print('Verified dry run: ',len(changed),'editable changes, 56 sources, manifest',io.sha(final_data),'history',io.sha(new_history),'pointer',io.sha(ptr_data));return
    backup=ver/'editable-install';backup.mkdir(exist_ok=True)
    def event(e):
        with (backup/'operations.jsonl').open('a') as f:
            f.write(json.dumps(e)+'\n');f.flush();os.fsync(f.fileno())
    swaps=[];created_manifest=not manifest.exists()
    with io.locked_targets([str(x) for x in [*changed,hist,pointer]]) as locks:
        def replace(p,before,after):
            if before!=after:io.exchange_guarded(p,before,after,backup/'previous',event,locks);swaps.append((p,before,after))
            else:io.require(read(p)==after,'Concurrent change '+str(p))
        try:
            for p,(a,b) in changed.items():replace(p,a,b)
            replace(hist,initial_history,new_history)
            for rel,body in copies.items():keeponce(edition/rel,body)
            for name,expected_pin in new_pins.items():read(root/name,expected_pin)
            keeponce(manifest,final_data);replace(pointer,initial_ptr,ptr_data)
            for p,a,b in swaps:io.require(read(p)==b,'Installed bytes changed '+str(p))
        except BaseException:
            for p,a,b in reversed(swaps):
                if read(p)==b:io.exchange_guarded(p,b,a,backup/'rollback',event,locks)
            if created_manifest and manifest.is_file() and read(manifest)==final_data:
                manifest.unlink();io.fsync_directory(manifest.parent)
            raise
    print('Installed',commit,'manifest',io.sha(final_data),'history',io.sha(new_history),'pointer',io.sha(ptr_data))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('edition',type=Path);p.add_argument('accepted_digest');p.add_argument('host_package_sha256');p.add_argument('official_result',type=Path,nargs='?')
    g=p.add_mutually_exclusive_group();g.add_argument('--install',action='store_true');g.add_argument('--source-only',action='store_true')
    verify(p.parse_args())
