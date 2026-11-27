#!/usr/bin/env python3
"""Independent final public composition, provenance and retention verification."""
from pathlib import Path
from copy import deepcopy
from collections import Counter
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('input_directory')
parser.add_argument('--output-name', default='composition-final')
args = parser.parse_args()
SOURCE = Path(args.input_directory)
PUBLIC = SOURCE/'public' if (SOURCE/'public').is_dir() else SOURCE
COORDINATION = SOURCE/'coordination' if (SOURCE/'coordination').is_dir() else SOURCE
OUT = Path('/tmp/programme-public-fidelity-1120-20261116/current')/args.output_name
BASE = Path('/tmp/programme-public-current-successor-20261116/baseline-reviewed')
ORIGINAL = Path('/tmp/programme-public-content-0835-20261116/public')
EXPECTED_ESSAY = '0f35958c6a64e03627a71c9289a838c5eb26790e619d601b4403c231d15e85f6'
assert (SOURCE/'FINAL-PINS.json').is_file(), 'Require a frozen final manifest, not a mutable draft.'
assert not (OUT/'FINAL-PINS.json').exists(), 'Do not overwrite a sealed review.'
OUT.mkdir(parents=True, exist_ok=True)

def sha(data): return hashlib.sha256(data).hexdigest()
def file_sha(path): return sha(Path(path).read_bytes())
def canon(value): return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def load(path): return json.loads(Path(path).read_text())
def dump(name,value): (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def walk(value,pointer=''):
    yield pointer,value
    if isinstance(value,dict):
        for key,child in value.items(): yield from walk(child,pointer+'/'+key.replace('~','~0').replace('/','~1'))
    elif isinstance(value,list):
        for index,child in enumerate(value): yield from walk(child,pointer+'/'+str(index))
def get(value,pointer):
    if not pointer:return value
    for token in pointer.strip('/').split('/'):
        token=token.replace('~1','/').replace('~0','~')
        value=value[int(token)] if isinstance(value,list) else value[token]
    return value
def put(value,pointer,new,remove=False):
    parent,key=pointer.rsplit('/',1); target=get(value,parent)
    key=key.replace('~1','/').replace('~0','~'); key=int(key) if isinstance(target,list) else key
    if remove:del target[key]
    else:target[key]=deepcopy(new)
def artifact(value):return Path(value).name

errors=[];checks=[];guards=[];source_usage=[]
def check(name,passed,detail=None):
    checks.append({'check':name,'pass':bool(passed),'detail':detail})
    if not passed:errors.append({'check':name,'detail':detail})

final_manifest=load(SOURCE/'FINAL-PINS.json')
seen_pins=set();pin_errors=[]
def verify_pins(value,base):
    for _,row in walk(value):
        if not isinstance(row,dict) or not isinstance(row.get('sha256'),str):continue
        raw=row.get('path') or row.get('file') or row.get('relative_path')
        if not isinstance(raw,str):continue
        path=Path(raw); path=path if path.is_absolute() else base/path
        key=(str(path),row['sha256'])
        if key in seen_pins:continue
        seen_pins.add(key)
        ok=path.is_file() and file_sha(path)==row['sha256']
        if ok and isinstance(row.get('bytes'),int):ok=path.stat().st_size==row['bytes']
        if not ok:pin_errors.append({'path':str(path),'expected':row['sha256'],'actual':file_sha(path) if path.is_file() else None})
verify_pins(final_manifest,SOURCE)
composition=load(COORDINATION/'COMPOSITION.json')
check('final composition is not draft', not composition.get('draft_mode',False))
check('scientific cutoff',composition['evidence_boundary_utc']=='2026-11-16T13:50:00Z')
check('no pending owner seals',not composition.get('pending_owner_seals'))
check('no grand conflicts',not composition.get('grand_conflicts'))
verify_pins(composition,SOURCE)
for entry in composition['owner_seals']:
    pin=entry['manifest'];p=Path(pin['path']);verify_pins(load(p),p.parent)
check('all final/source/owner manifest pins',not pin_errors,{'verified':len(seen_pins),'errors':pin_errors})

expected={name:load(BASE/name) for name in ['atlas.json','content.json']}
actual={name:load(PUBLIC/name) for name in expected}
original={name:load(ORIGINAL/name) for name in expected}
base=deepcopy(expected)
source_cache={}
def declared(path):
    path=str(Path(path).resolve())
    if path in source_cache:return source_cache[path]
    doc=load(path);changes=[];appends=[]
    for key in ['operations','mutations','replacements','patches','changes']:
        for index,row in enumerate(doc.get(key,[])):
            if not isinstance(row,dict) or 'pointer' not in row:continue
            file=artifact(row.get('artifact',row.get('file',row.get('target','content.json'))))
            pointer=row['pointer']
            if row.get('selector'):
                selector=row['selector'];collection=selector['collection'].strip('/')
                matches=[i for i,v in enumerate(actual[file][collection]) if v.get('id')==selector['id']]
                if len(matches)!=1:continue
                pointer='/'+collection+'/'+str(matches[0])+pointer
            before=row.get('before',row.get('old_value'))
            after=row.get('after',row.get('value',row.get('new_value')))
            changes.append({'file':file,'pointer':pointer,'before':before,'after':after,'missing':row.get('before_missing',row.get('expected_absent',row.get('op')=='add')),'locator':f'/{key}/{index}'})
    additions=doc.get('additions',[])
    if isinstance(additions,list):
        for index,row in enumerate(additions):
            collection=row.get('collection_pointer',row.get('collection'))
            appends.append({'file':artifact(row['artifact']),'collection':'/'+collection.strip('/'),'value':row['value'],'locator':f'/additions/{index}'})
    elif isinstance(additions,dict):
        for collection,rows in additions.items():
            for index,row in enumerate(rows):appends.append({'file':'atlas.json','collection':'/'+collection,'value':row,'locator':f'/additions/{collection}/{index}'})
    for key,collection in [('new_claims','claims'),('newClaims','claims'),('new_edges','edges'),('newEdges','edges'),('newComparisons','comparisons'),('newReadingPaths','readingPaths')]:
        for index,row in enumerate(doc.get(key,[])):appends.append({'file':'atlas.json','collection':'/'+collection,'value':row,'locator':f'/{key}/{index}'})
    for index,row in enumerate(doc.get('appends',[])):
        for j,value in enumerate(row.get('new_values',[])):appends.append({'file':artifact(row['artifact']),'collection':row['pointer'].removesuffix('/-'),'value':value,'locator':f'/appends/{index}/new_values/{j}'})
    for index,row in enumerate(doc.get('addStatements',[])):appends.append({'file':'content.json','collection':row['pointer'].removesuffix('/-'),'value':row['value'],'locator':f'/addStatements/{index}'})
    source_cache[path]=(changes,appends)
    return changes,appends

# New array members do not displace any existing index. Install their initial
# exact source values before applying field replacements to those new members.
for index,row in enumerate(composition['appends']):
    choices=declared(row['source'])[1]
    matches=[x for x in choices if x['file']==row['file'] and x['collection']==row['collection'] and x['value']==row['value']]
    check(f'append {index} exact source authority',bool(matches),{'source':row['source'],'id':row.get('id')})
    if matches:source_usage.append({'kind':'append','composition_index':index,'source':row['source'],'source_locator':matches[0]['locator']})
    target=get(expected[row['file']],row['collection'])
    ok=len(target)==row['index'];check(f'append {index} index guard',ok)
    if ok:target.append(deepcopy(row['value']))
for index,row in enumerate(composition['ordered_changes']):
    choices=declared(row['source'])[0]
    matches=[x for x in choices if x['file']==row['file'] and x['pointer']==row['pointer'] and x['after']==row['after'] and (row.get('before_missing',False) or x['before']==row.get('before'))]
    check(f'change {index} exact source authority',bool(matches),{'source':row['source'],'pointer':row['pointer']})
    if matches:source_usage.append({'kind':'change','composition_index':index,'source':row['source'],'source_locator':matches[0]['locator']})
    try:current=get(expected[row['file']],row['pointer']);missing=False
    except (KeyError,IndexError):current=None;missing=True
    ok=missing if row.get('before_missing') else not missing and current==row['before']
    guards.append({'index':index,'file':row['file'],'pointer':row['pointer'],'pass':ok})
    check(f'change {index} exact before',ok)
    if ok:put(expected[row['file']],row['pointer'],row['after'])
for index,row in enumerate(composition['legacy_claim_mirrors']):
    target=get(expected['content.json'],row['pointer']);check(f'legacy mirror {index} guard',target==row['before'])
    claim=next(x for x in expected['atlas.json']['claims'] if x['id']==row['atlasClaimId'])
    after=row['after'];text=claim['statement']+ ('\n\nScope: '+' '.join(claim['hypotheses']) if claim['hypotheses'] else '')
    check(f'legacy mirror {index} exact scientific text',after['text']==text and after['title']==claim['title'] and after['hypotheses']==claim['hypotheses'])
    put(expected['content.json'],row['pointer'],after)
for index,row in enumerate(composition['reciprocal_comparison_indices']):
    claim=next(x for x in expected['atlas.json']['claims'] if x['id']==row['claim_id'])
    comparison=next(x for x in expected['atlas.json']['comparisons'] if x['id']==row['comparison_id'])
    check(f'reciprocal {index} guard',claim['comparisonIds']==row['before'])
    status_field={'checked':'establishedClaimIds','conditional':'conditionalClaimIds','scoped_negative':'scopedNegativeClaimIds','remaining':'remainingClaimIds'}[claim['status']['code']]
    check(f'reciprocal {index} actual matching membership',claim['id'] in comparison[status_field] and row['status']==claim['status']['code'] and set(row['after'])==set(row['before'])|{row['comparison_id']})
    claim['comparisonIds']=row['after']
for row in composition.get('source_labels_preserved_privately',[]):
    check('private source label guard '+row['pointer'],get(expected[row['file']],row['pointer'])==row['before'])
    put(expected[row['file']],row['pointer'],None,True)
idplan=load(composition['explicit_id_plan']['path'])
for index,row in enumerate(idplan['changes']):
    parent,key=row['pointer'].rsplit('/',1);target=get(expected[row['file']],parent)
    check(f'legacy id {index} absent',key not in target)
    check(f'legacy id {index} observed anchor',row['existing_served_anchor']=='s-'+row['after'])
    check(f'legacy id {index} target title',target['title']==row['current_title'])
    target[key]=row['after']
expected['atlas.json']['asOf']=composition['evidence_boundary_utc']
expected['content.json']['as_of_utc']=composition['evidence_boundary_utc']
expected['content.json']['scientific_atlas']['asOf']=composition['evidence_boundary_utc']
composition_differences=[]
def differences(before,after,pointer=''):
    if before==after:return
    if isinstance(before,dict) and isinstance(after,dict):
        for key in sorted(before.keys()|after.keys()):
            path=pointer+'/'+key.replace('~','~0').replace('/','~1')
            if key not in before or key not in after:yield {'pointer':path,'expected':before.get(key),'actual':after.get(key)}
            else:yield from differences(before[key],after[key],path)
    elif isinstance(before,list) and isinstance(after,list) and len(before)==len(after):
        for i,(old,new) in enumerate(zip(before,after)):yield from differences(old,new,pointer+'/'+str(i))
    else:yield {'pointer':pointer,'expected':before,'actual':after}
for file in expected:
    check(file+' exactly declared composition',expected[file]==actual[file])
    composition_differences.extend({'file':file,**row} for row in differences(expected[file],actual[file]))
check('final essay exact accepted bytes',file_sha(PUBLIC/'essay.md')==EXPECTED_ESSAY)

old_ids={v['id'] for _,v in walk(original['content.json']) if isinstance(v,dict) and isinstance(v.get('id'),str)}
new_ids={v['id'] for _,v in walk(actual['content.json']) if isinstance(v,dict) and isinstance(v.get('id'),str)}
check('all original content identities retained',old_ids<=new_ids,sorted(old_ids-new_ids))
for collection in ['claims','comparisons','edges','domains','readingPaths']:
    old=[x['id'] for x in original['atlas.json'][collection]];now=[x['id'] for x in actual['atlas.json'][collection]]
    check('atlas '+collection+' original order retained',now[:len(old)]==old)
    check('atlas '+collection+' identities unique',len(now)==len(set(now)))
for key,path in [('families','/rows'),('questions','/decisive/questions')]:
    check(key+' identities and order retained',[x['id'] for x in get(actual['content.json'],path)]==[x['id'] for x in get(original['content.json'],path)])
edge_fields=['id','source','target','relation']
check('all53 old graph edge tuples retained',len(original['atlas.json']['edges'])==53 and all({k:old[k] for k in edge_fields}=={k:new[k] for k in edge_fields} for old,new in zip(original['atlas.json']['edges'],actual['atlas.json']['edges'])))
claims={x['id']:x for x in actual['atlas.json']['claims']}
for comparison in actual['atlas.json']['comparisons']:
    for field,status in [('establishedClaimIds','checked'),('conditionalClaimIds','conditional'),('scopedNegativeClaimIds','scoped_negative'),('remainingClaimIds','remaining')]:
        for identity in comparison[field]:
            check('comparison '+comparison['id']+'/'+identity,identity in claims and claims[identity]['status']['code']==status and comparison['id'] in claims[identity]['comparisonIds'])
for edge in actual['atlas.json']['edges']:check('edge endpoints '+edge['id'],edge['source'] in claims and edge['target'] in claims)

math=[];math_locations=[];privacy=[];delimiters=[];boundary=[]
pattern=re.compile(r'\\\((.*?)\\\)|\\\[(.*?)\\\]',re.S)
reader_documents={**actual,'essay.md':(PUBLIC/'essay.md').read_text()}
old_process_values=load('/tmp/programme-public-fidelity-1120-20261116/repair-overlay/composition/REMAINING-PROCESS-VALUES.json')
old_process_checks=[]
for index,row in enumerate(old_process_values):
    live_values=[v for _,v in walk(reader_documents[row['file']]) if isinstance(v,str)]
    absent=row['text'] not in live_values
    old_process_checks.append({'index':index,'file':row['file'],'old_pointers':row['pointers'],'old_text_sha256':sha(row['text'].encode()),'old_value_absent':absent})
    check(f'known residual process value {index} replaced',absent)
for file,document in reader_documents.items():
    for pointer,value in walk(document):
        if not isinstance(value,str):continue
        if re.search(r'/Users/|/private/tmp/|(?<![A-Za-z])/tmp/|\b[a-f0-9]{64}\b',value):privacy.append({'file':file,'pointer':pointer,'value':value})
        if value.count('\\(')!=value.count('\\)') or value.count('\\[')!=value.count('\\]'):delimiters.append({'file':file,'pointer':pointer})
        if re.search(r'[A-Za-z]\\\(|\\\)[A-Za-z0-9]',value):boundary.append({'file':file,'pointer':pointer,'value':value})
        for match in pattern.finditer(value):
            math.append({'tex':match.group(1) if match.group(1) is not None else match.group(2),'display':match.group(2) is not None});math_locations.append({'file':file,'pointer':pointer})
renderer=Path('/Users/raeez/www-worktrees/2026-11-15-qh-frontier-2203/compiler/quantum-holography-tracker/tex2mathml.cjs')
run=subprocess.run(['node',str(renderer)],input=json.dumps(math),text=True,capture_output=True)
math_errors=[]
if run.returncode:math_errors.append({'error':run.stderr})
else:
    results=json.loads(run.stdout)
    if len(results)!=len(math):math_errors.append({'error':'renderer count mismatch'})
    math_errors.extend({**math_locations[i],'tex':math[i]['tex'],'error':x['error']} for i,x in enumerate(results) if 'error' in x)
check('all delimited formulas render',not math_errors,{'count':len(math),'errors':math_errors})
check('balanced formula delimiters',not delimiters,delimiters)
check('no private source paths/hashes in reader data',not privacy,privacy)
check('no interword mathematical delimiter corruption',not boundary,boundary)
status_changes=[{'id':old['id'],'before':old['status'],'after':claims[old['id']]['status']} for old in original['atlas.json']['claims'] if old['status']['code']!=claims[old['id']]['status']['code']]
result={'schema':'independent-final-public-composition-check/v1','checked_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS' if not errors else 'REPAIR_REQUIRED','scope':'Exact public composition, declared source values, identity/graph/status bookkeeping and transcription; independent mathematical fidelity is supplied by the separately bound lane and global receipts. No source theorem rerun or site rendering.','candidate_final_manifest':str(SOURCE/'FINAL-PINS.json'),'candidate_final_sha256':file_sha(SOURCE/'FINAL-PINS.json'),'counts':{'checks':len(checks),'owner_and_output_pins':len(seen_pins),'declared_changes':len(composition['ordered_changes']),'appends':len(composition['appends']),'claims':len(claims),'old_claims_retained':len(original['atlas.json']['claims']),'old_edges_retained':53,'new_edges':len(actual['atlas.json']['edges'])-53,'original_content_ids':len(old_ids),'explicit_new_legacy_ids':len(idplan['changes']),'math_expressions':len(math)},'status_changes':status_changes,'errors':errors}
dump('COMPOSITION-CHECK.json',result);dump('CHECKS.json',checks);dump('GUARDS.json',guards);dump('DECLARED-SOURCE-VALUES.json',source_usage);dump('TRANSCRIPTION-CHECK.json',{'math_count':len(math),'math_errors':math_errors,'delimiter_errors':delimiters,'privacy_hits':privacy,'interword_math_candidates':boundary})
dump('BASELINE-PROCESS-RESIDUALS.json',old_process_checks)
dump('COMPOSITION-DIFFERENCES.json',composition_differences)
print(json.dumps(result,ensure_ascii=False,indent=2))
