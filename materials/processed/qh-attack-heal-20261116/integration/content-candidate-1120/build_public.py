from pathlib import Path
import copy,hashlib,json,re
from build_atlas import P,CUT,LANES,normalize,build as build_atlas

def sha(raw):return hashlib.sha256(raw).hexdigest()
def pin(p):
    raw=p.read_bytes();return {'path':str(p),'sha256':sha(raw),'bytes':len(raw)}
def load(p):return json.loads(p.read_text())
def dump(p,v):
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n')
def walk(x,address=''):
    if isinstance(x,dict):
        yield address,x
        for k,v in x.items():yield from walk(v,address+'/'+k.replace('~','~0').replace('/','~1'))
    elif isinstance(x,list):
        for i,v in enumerate(x):yield from walk(v,address+'/'+str(i))
def pointer(doc,path):
    for k in path.strip('/').split('/'):
        k=k.replace('~1','/').replace('~0','~')
        doc=doc[int(k)] if isinstance(doc,list) else doc[k]
    return doc
def setpointer(doc,path,value):
    parts=path.strip('/').split('/');last=parts.pop().replace('~1','/').replace('~0','~')
    container=doc
    for k in parts:
        k=k.replace('~1','/').replace('~0','~')
        container=container[int(k)] if isinstance(container,list) else container[k]
    container[int(last) if isinstance(container,list) else last]=value

def build():
    build_atlas(False)
    atlas=load(P/'public/atlas.json')
    baseline=load(P/'baseline/content.json');content=copy.deepcopy(baseline)
    base_ids={x['id'] for _,x in walk(baseline) if isinstance(x.get('id'),str)}
    old_question_ids=[x['id'] for x in baseline['decisive']['questions']]
    claims={c['id']:c for c in atlas['claims']}
    comparisons={c['id']:c for c in atlas['comparisons']}
    domain_ids={d['id'] for d in atlas['domains']}
    all_atlas_ids=[row['id'] for field in ('domains','claims','comparisons','edges','readingPaths') for row in atlas[field]]
    assert len(set(all_atlas_ids))==len(all_atlas_ids),'cross-kind atlas ID collision'
    for c in atlas['claims']:
        assert c['domainId'] in domain_ids,('unknown claim domain',c['id'])
        for comparison_id in c['comparisonIds']:
            assert comparison_id in comparisons,('unknown comparison',c['id'],comparison_id)
            assert comparisons[comparison_id]['domainId']==c['domainId'],('cross-domain comparison',c['id'],comparison_id)
    replacements=[];private=[]
    status={'checked':'checked','conditional':'conditional','scoped_negative':'refuted form','remaining':'open'}
    for address,obj in walk(content):
        cid=obj.get('id')
        if cid not in claims or 'text' not in obj:continue
        c=claims[cid];before=copy.deepcopy(obj)
        obj['title']=c['title'];obj['status']=status[c['status']['code']]
        obj['text']=c['statement']+ ('\n\nScope: '+' '.join(c['hypotheses']) if c['hypotheses'] else '')
        obj['hypotheses']=copy.deepcopy(c['hypotheses'])
        obj['atlasClaimId']=cid
        if c.get('sourceLabel'):obj['sourceLabel']=c['sourceLabel']
        replacements.append({'pointer':address,'id':cid,'before':before,'after':copy.deepcopy(obj),
                             'atlas_claim_id':cid,'operation':'Exact current claim and every stated hypothesis; stable legacy ID retained.'})

    overview_path=P/'overview/OVERVIEW.json';overlay_path=P/'overview/LEGACY-OVERLAY.json';essay_path=P/'overview/ESSAY.md'
    assert all(p.exists() for p in (overview_path,overlay_path,essay_path,P/'overview/FINAL-PINS.json')),'overview not frozen'
    overlay=load(overlay_path)
    overlay_rows=overlay if isinstance(overlay,list) else overlay.get('changes',overlay.get('updates',[]))
    for r in overlay_rows:
        address=r.get('pointer',r.get('baseline_pointer'))
        assert address and 'before' in r and 'after' in r,r
        assert pointer(baseline,address)==r['before'],('overview baseline guard',r.get('id'),address)
        assert set(r.get('claimIds',[]))<=(set(claims)|base_ids),('unknown overlay claim binding',r.get('id'),r.get('claimIds'))
        current=pointer(content,address)
        assert current==r['before'] or current==r['after'],('overlapping semantic update requires explicit composition',r.get('id'),address)
        setpointer(content,address,copy.deepcopy(r['after']))
    overview=load(overview_path)
    for key in ('title','subtitle','lead','essay_lead'):
        if key in overview:content[key]=copy.deepcopy(overview[key])
    if 'orientation' in overview:content['orientation']=copy.deepcopy(overview['orientation'])
    content['as_of']='2026-11-16';content['as_of_utc']=CUT
    content['scientific_atlas']={'schema':atlas['schema'],'asOf':CUT,'path':'atlas.json'}
    if 'guidance' in overview:content['reader_guidance']=copy.deepcopy(overview['guidance'])

    # Private provenance is preserved in the companion binding ledger. The
    # reader artifact carries scientific text and named external antecedents.
    source_keys={'source','sources','source_path','source_refs','novelty'}
    def clean(x,address=''):
        if isinstance(x,dict):
            for key in list(x):
                nextpath=address+'/'+key.replace('~','~0').replace('/','~1')
                if key in source_keys:
                    private.append({'pointer':nextpath,'value':x.pop(key),'disposition':'retained in private bindings; not a public reader value'})
                else:clean(x[key],nextpath)
        elif isinstance(x,list):
            for i,v in enumerate(x):clean(v,address+'/'+str(i))
    clean(content)
    after_ids={x['id'] for _,x in walk(content) if isinstance(x.get('id'),str)}
    assert base_ids<=after_ids,('existing reader IDs removed',sorted(base_ids-after_ids))
    assert [x['id'] for x in content['decisive']['questions']]==old_question_ids
    assert len(content['rows'])==len(baseline['rows'])==20
    assert len(old_question_ids)==22
    family_orientation=content.get('orientation',{}).get('programmeFamilies',[])
    if family_orientation:
        oriented_ids=[x for family in family_orientation for x in family['familyIds']]
        assert len(oriented_ids)==len(set(oriented_ids))==20,'family orientation duplicate or omission'
        assert set(oriented_ids)=={r['id'] for r in baseline['rows']},'family orientation differs from catalogue'
    rendered=json.dumps(content,ensure_ascii=False)+'\n'+essay_path.read_text()
    assert not re.search(r'/Users/|/private/tmp/|(?<![A-Za-z])\/tmp\/|[a-f0-9]{64}',rendered),'private material in public prose'
    dump(P/'public/content.json',content)
    (P/'public/essay.md').write_bytes(essay_path.read_bytes())
    dump(P/'PUBLIC-PRIVATE-BINDINGS.json',{
        'schema':'programme-public-composition-bindings/v1','cutoff_utc':CUT,
        'baseline':pin(P/'baseline/content.json'),'atlas_bindings':pin(P/'ATLAS-PRIVATE-BINDINGS.json'),
        'overview':pin(overview_path),'overview_private_bindings':pin(P/'overview/PRIVATE-BINDINGS.json'),
        'overview_final':pin(P/'overview/FINAL-PINS.json'),
        'legacy_claim_replacements':replacements,'exact_guarded_overlays':overlay_rows,
        'private_baseline_fields':private,
        'same_source_scope_refinements':pin(P/'SOURCE-SCOPE-REFINEMENTS.json') if (P/'SOURCE-SCOPE-REFINEMENTS.json').exists() else None,
        'preservation':{'all_existing_ids':sorted(base_ids),'all22_question_ids':old_question_ids,'all20_family_ids':[x['id'] for x in content['rows']]},
        'new_source_groups_are_not_theorem_counts':True,'shared_public_writes':False})
    dump(P/'PUBLIC-VALIDATION.json',{
        'status':'PASS','scope':'Exact public composition, ID preservation, source/private separation and schema validation; no additional theorem or proof claim.',
        'cutoff_utc':CUT,'existing_ids_preserved':len(base_ids),'family_rows_preserved':20,
        'decisive_question_ids_preserved':22,'legacy_claim_objects_updated':len(replacements),
        'all_atlas_references_known':True,'all_family_orientation_routes_cover_catalogue':True,
        'guarded_overlays':len(overlay_rows),'private_reader_values_absent':True,
        'outputs':[pin(P/'public'/n) for n in ('content.json','essay.md','atlas.json')],
        'shared_public_writes':False})
    print(json.dumps(load(P/'PUBLIC-VALIDATION.json'),indent=2))

if __name__=='__main__':build()
