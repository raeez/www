#!/usr/bin/env python3
"""Prepare the eight authorized display/link leaves without editing the delivery."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json
import re

ROOT=Path(__file__).absolute().parent
assert not (ROOT/'FINAL-PINS.json').exists(), 'This bounded packet is already sealed.'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def pin(path):
    path=Path(path)
    return {'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size}
def read(path):return json.loads(Path(path).read_text())
def save(name,value):(ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def at(obj,pointer):
    for part in pointer.strip('/').split('/'):
        obj=obj[int(part)] if isinstance(obj,list) else obj[part]
    return obj
def replace(obj,pointer,value):
    parts=pointer.strip('/').split('/');node=obj
    for part in parts[:-1]:node=node[int(part)] if isinstance(node,list) else node[part]
    node[int(parts[-1]) if isinstance(node,list) else parts[-1]]=value
def enclosing(obj,pointer):
    parts=pointer.strip('/').split('/')[:-1]
    while parts:
        prefix='/'+'/'.join(parts);node=at(obj,prefix)
        if isinstance(node,dict) and 'id' in node:return prefix,node['id']
        parts.pop()
    raise AssertionError(pointer)
def differences(a,b,prefix=''):
    assert type(a) is type(b),prefix
    if isinstance(a,dict):
        assert list(a)==list(b),prefix
        for k in a:yield from differences(a[k],b[k],prefix+'/'+k)
    elif isinstance(a,list):
        assert len(a)==len(b),prefix
        for i,(x,y) in enumerate(zip(a,b)):yield from differences(x,y,prefix+'/'+str(i))
    elif a!=b:yield prefix

inspection=read(ROOT/'INSPECTION.json')
inputs=[inspection['frozen_delivery'],*inspection['public_inputs'],inspection['question_contract']['compiler']]
for rec in inputs:
    assert sha(rec['path'])==rec['sha256'],rec['path']
    assert Path(rec['path']).stat().st_size==rec['bytes'],rec['path']
source={Path(rec['path']).name:read(rec['path']) for rec in inspection['public_inputs']}
replayed=copy.deepcopy(source)
rules=[('E3',r'\(E_3\)'),('E3',r'\(E_3\)'),
       ('T2',r'\(\mathrm{T2}\)'),('T2',r'\(\mathrm{T2}\)'),
       ('T2',r'\(\mathrm{T2}\)'),('T2',r'\(\mathrm{T2}\)'),
       ('R2',r'\(\mathrm{R2}\)')]
operations=[]
for index,location in enumerate(inspection['locations']):
    filename=location['file'];pointer=location['pointer'];before=location['before']
    assert at(source[filename],pointer)==before,(filename,pointer)
    enclosing_pointer,enclosing_id=enclosing(source[filename],pointer)
    assert enclosing_id==location['enclosing_id'],(filename,pointer,enclosing_id)
    op={'artifact':filename,'op':'replace','pointer':pointer,
        'enclosing_pointer':enclosing_pointer,'id_guard':enclosing_id,'before':before}
    if index<7:
        old,new=rules[index]
        assert len(re.findall(r'(?<![A-Za-z0-9_])'+re.escape(old)+r'(?![A-Za-z0-9_])',before))==1
        assert before.count(old)==1
        value=before.replace(old,new)
        assert value.replace(new,old)==before
        op.update({'kind':'display_normalization','old_token':old,'new_token':new,'value':value})
    else:
        assert index==7 and pointer=='/comparisons/22/questionId'
        assert before==inspection['question_contract']['existing_inner_statement_id']
        value=inspection['question_contract']['existing_outer_question_id']
        outer=at(source['content.json'],inspection['question_contract']['outer_pointer'])
        inner=at(source['content.json'],inspection['question_contract']['inner_pointer'])
        assert outer['id']==value and inner['id']==before
        assert re.fullmatch(r'[a-z0-9-]+',value)
        op.update({'kind':'question_anchor_reference','value':value,
                   'resolved_anchor':'q-'+value,
                   'existing_outer_question_pointer':inspection['question_contract']['outer_pointer'],
                   'retained_inner_statement_pointer':inspection['question_contract']['inner_pointer']})
    replace(replayed[filename],pointer,op['value']);operations.append(op)
assert len(operations)==8

actual={name:list(differences(source[name],replayed[name])) for name in source}
expected={name:[op['pointer'] for op in operations if op['artifact']==name] for name in source}
assert all(set(actual[name])==set(expected[name]) for name in source)
assert sum(map(len,actual.values()))==8
question=inspection['question_contract']
assert at(replayed['content.json'],question['outer_pointer'])==at(source['content.json'],question['outer_pointer'])
assert at(replayed['content.json'],question['inner_pointer'])==at(source['content.json'],question['inner_pointer'])
for key in ['claims','edges','comparisons']:
    assert [x['id'] for x in source['atlas.json'][key]]==[x['id'] for x in replayed['atlas.json'][key]]
assert [x['status'] for x in source['atlas.json']['claims']]==[x['status'] for x in replayed['atlas.json']['claims']]
assert source['atlas.json']['readingPaths']==replayed['atlas.json']['readingPaths']
for rec in inputs:assert sha(rec['path'])==rec['sha256'],rec['path']

save('DELTA.json',{
    'schema':'exact-guarded-public-rendering-delta/v1',
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'base_delivery':inspection['frozen_delivery'],'public_inputs':inspection['public_inputs'],
    'scope':'Seven display-token normalizations and one question-anchor reference; no mathematical content or status change.',
    'operations':operations,
    'integration_rule':'Verify the exact file hashes and before values. Preserve each enclosing stable ID. Apply these eight leaves to a new integration candidate; keep the frozen delivery unchanged.'})

ruling=(
    'Apply the eight guarded replacements in `DELTA.json` to a new candidate based on delivery `63cb835d4a6c7d7187b5cc729f7ba3eb16ef65df665ed149cb62ff17b0d0d85f`.\n\n'
    'The two operadic labels `E3` become `\\(E_3\\)`. The four `T2` occurrences and the one `R2` occurrence remain literal construction labels, set upright as `\\(\\mathrm{T2}\\)` and `\\(\\mathrm{R2}\\)`. Their letters and digits are unchanged. Every other byte of each affected string is preserved.\n\n'
    'Set the `questionId` of comparison `d-centre-base-change` to `d-centre-base-change`. The compiler resolves this field through the outer question anchor `q-d-centre-base-change`; `decisive-centre-base-change` is the retained nested statement ID. Both content records remain unchanged.\n\n'
    'Validation covers the eight exact guards, enclosing IDs, complete JSON difference set and unchanged frozen inputs. The parent owns the bounded rendered readback and integration. The completed mathematical reviews remain closed.\n'
)
(ROOT/'INTEGRATION-RULING.md').write_text(ruling)
save('VALIDATION.json',{
    'schema':'bounded-public-rendering-validation/v1','created_utc':datetime.now(timezone.utc).isoformat(),
    'status':'PASS_EXACT_GUARDED_DELTA','guarded_leaves':8,'display_normalizations':7,'question_link_references':1,
    'exact_base_file_pins_verified':True,'all_before_values_match':True,'all_enclosing_id_guards_match':True,
    'complete_difference_set':actual,'all_other_json_values_preserved':True,
    'all_other_affected_string_bytes_preserved':True,'claim_statuses_and_all_stable_ids_preserved':True,
    'edge_endpoint_types_and_memberships_preserved':True,'reading_paths_preserved':True,
    'outer_and_inner_question_records_preserved':True,'existing_target_anchor':'q-d-centre-base-change',
    'question_contract':question,'question_contract_read_lines':[335,351],
    'frozen_delivery_and_compiler_unchanged':True,'source_proofs_or_completed_reviews_reopened':False,
    'rendered_readback':'Parent-owned and not performed in this author packet.',
    'mutated_paths_outside_owned_packet':[]})
artifacts=[pin(ROOT/name) for name in ['INSPECTION.json','DELTA.json','INTEGRATION-RULING.md','VALIDATION.json','build_delta.py']]
save('FINAL-PINS.json',{
    'schema':'bounded-public-rendering-final/v1','finalized_utc':datetime.now(timezone.utc).isoformat(),
    'status':'READY_FOR_PARENT_BOUNDED_RENDERED_READBACK','base_delivery':inspection['frozen_delivery'],
    'public_inputs':inspection['public_inputs'],'operations':8,'artifacts':artifacts,
    'authority':{'source_content_review_reopened':False,'frozen_delivery_edited':False,
                 'Opus_files_edited':False,'new_workers':False,'publication_or_adoption':False},
    'self_hash_not_included':True})
print(json.dumps({'final':pin(ROOT/'FINAL-PINS.json'),'delta':pin(ROOT/'DELTA.json'),
                  'validation':pin(ROOT/'VALIDATION.json'),'operations':8},indent=2))
