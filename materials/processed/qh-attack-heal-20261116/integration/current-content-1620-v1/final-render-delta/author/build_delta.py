from pathlib import Path
import copy, hashlib, json, re

A=Path(__file__).resolve().parent
P=A.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
intake=json.loads((P/'coordination/INTAKE.json').read_text())
allowed=json.loads((P/'coordination/EXPECTED-SCOPE.json').read_text())
notation_source=P.parent.parent/'inputs/source-accepted-v3/integrated-handoffs/algebra-geometry/REPORT.md'
notation_pin={'path':str(notation_source),'sha256':sha(notation_source.read_bytes()),'lines':'89–99; especially the weighted-coend paragraph at line 97','reading_scope':'Selected accepted-source context only, to identify A1 as the affine line in M_A1.'}
trees={}
for row in intake['baselines']:
    raw=Path(row['snapshot']).read_bytes()
    assert sha(raw)==row['sha256'] and len(raw)==row['bytes']
    if row['snapshot'].endswith('.json'):
        trees[Path(row['snapshot']).name]=json.loads(raw)
ops=[]
def get(file,pointer):
    v=trees[file]
    for part in pointer.strip('/').split('/'):
        v=v[int(part)] if isinstance(v,list) else v[part]
    return v
def add(file,pointer,after,reason):
    before=get(file,pointer)
    assert isinstance(before,str) and before!=after
    ops.append({'file':file,'pointer':pointer,'before':before,'after':after,'reason':reason,
        'source_refs':[{'path':str(P/'baselines'/file),'sha256':next(x['sha256'] for x in intake['baselines'] if x['snapshot'].endswith('/'+file)),'pointer':pointer,'reading_scope':'Exact flagged logical field read in its claim/comparison context; no new scientific source or proof audit.'}]})

p='/rows/6/summary'
add('content.json',p,get('content.json',p).replace('adopted algebraic and formal','established algebraic and formal'),'Replace workflow wording with the same positive scientific status; retain every completion restriction.')
p='/decisive/questions/0/known/3/text'
t=get('content.json',p)
for before,after in [
    ('rank n≥2',r'rank \(n\ge2\)'),
    ('termwise R_N-free',r'termwise \(R_N\)-free'),
    ('R_N=C[hbar]/(hbar^N), N≥1',r'\(R_N=\mathbb C[\hbar]/(\hbar^N)\), \(N\ge1\)')]:
    assert t.count(before)==1
    t=t.replace(before,after)
add('content.json',p,t,'Delimit the distinct rank n and precision N variables and the existing finite-precision coefficient ring; preserve all domains and quantifiers.')

add('atlas.json','/claims/826/hypotheses/0',
    r'The contact-aware additive derived-coend formula on \(\mathbb A^1\) and \(\mathbb G_m\), with every incoming simplex and split positive vacuum.',
    'Format the existing affine-line and multiplicative-group notation.')
add('atlas.json','/claims/826/hypotheses/1',
    r'Retain the unchanged affine-line carrier and its original \(H_0=M_{\mathbb A^1}(k)=k\) target.',
    'The explicit affine-line context and adjacent A¹ identify the existing M_A1 subscript; preserve H0, k and the unchanged-carrier condition.')
p='/claims/832/statement'
add('atlas.json',p,get('atlas.json',p).replace('H_b(ΩG;C)',r'\(H_b(\Omega G;\mathbb C)\)'),
    'Delimit the existing loop-homology factor without changing its degree or multiplication statement.')
for i in range(834,843):
    p=f'/claims/{i}/hypotheses/1';t=get('atlas.json',p)
    assert t=='The target C is the native two-idempotent factorizing coalgebra with its genuine total pointing u_B and multiplication m. Complete character and action homotopy fibres, full pointing paths, both ordered cuts and all parameter spaces are retained.'
    add('atlas.json',p,
        r'The target \(C\) is the native two-idempotent factorizing coalgebra with its genuine total pointing \(u_B\) and multiplication \(m\). Complete character and action homotopy fibres, full pointing paths, both ordered cuts and all parameter spaces are retained.',
        'Format each of the nine exact logical copies consistently. Preserve the source notation u_B, without relabelling it to match C.')
add('atlas.json','/claims/834/hypotheses/2',
    r'\(F=C_V\) for any arbitrary unbounded dg chiral algebra \(V\) with a genuine unit; \(v:J\to C_V\) is any actual coherent coassociative pointing.',
    'Preserve the actual F,C_V,V,v,J notation and all unbounded/coherent/unit hypotheses.')
add('atlas.json','/claims/835/hypotheses/2',
    r'\(F=P(M)\otimes^{!}C_V\) with \(M\) an arbitrary unbounded right differential-module complex and \(V\) an arbitrary unbounded genuine-unit dg chiral algebra; \(u:J\to F\) is any coherent pointing.',
    'Format the existing extraordinary tensor product and unchanged pointing arrow; no new pointing-path hypothesis.')
add('atlas.json','/claims/847/hypotheses/2',
    r'Exactly \(r=3\) labelled spectators, \(b=(1,1,1)\), \(\mu=1\), arbitrary \(N_{12},N_{13},N_{23}\ge0\), every \(q\ge2\) and every homogeneity.',
    'Combine the three rendered N warnings into one underlying leaf edit, retaining every bound, charge and homogeneity quantifier.')
add('atlas.json','/claims/848/hypotheses/2',
    r'Every spectator count \(r\), every marked count \(m\), arbitrary spectator-pair bounds and positive odd \(\mu\). The unconditional amplitude has at most three positive \(b_j\), each at most two. The conditional triangle implication allows arbitrary sizes with at most three active labels.',
    'Delimit existing variables while keeping the unconditional amplitude and conditional triangle hypotheses separate.')
add('atlas.json','/claims/849/hypotheses/2',
    r'Exactly three spectators, at most two positive \(b_j\) of arbitrary size, every integer \(\mu\ge1\) and every marked count. Retain collisions and multiple marked roots.',
    'Preserve the separate two-active-bound triangle range, including integer mu rather than positive odd mu.')
p='/comparisons/72/overview'
add('atlas.json',p,get('atlas.json',p).replace('Strong orientation has its adopted rank-two scope.','Strong orientation holds at its established rank-two scope.'),
    'Replace workflow wording without widening the rank-two theorem or the stronger residual.')
p='/comparisons/75/overview'
add('atlas.json',p,get('atlas.json',p).replace('Adopted algebraic/formal/classical-smooth dualities','Established algebraic/formal/classical-smooth dualities'),
    'Retain the established status of the same three domain-specific dualities in ordinary scientific prose.')
assert len(ops)==21
assert {(o['file'],o['pointer']) for o in ops}=={(o['file'],o['pointer']) for o in allowed['allowed_scalar_leaves']}
for op in ops:
    if op['file']=='atlas.json' and op['pointer'] in ['/claims/826/hypotheses/0','/claims/826/hypotheses/1']:
        op['source_refs'].append(notation_pin)
trial=copy.deepcopy(trees)
for op in ops:
    v=trial[op['file']];parts=op['pointer'].strip('/').split('/')
    for part in parts[:-1]:v=v[int(part)] if isinstance(v,list) else v[part]
    key=int(parts[-1]) if isinstance(v,list) else parts[-1]
    assert v[key]==op['before'];v[key]=op['after']
def inventory(v,key):
    if isinstance(v,dict):return ([v[key]] if key in v else [])+[z for a in v.values() for z in inventory(a,key)]
    if isinstance(v,list):return [z for a in v for z in inventory(a,key)]
    return []
for file in trees:
    for key in ['id','status','statusCode','statusLabel','source','sourceRefs','url','href']:
        assert inventory(trees[file],key)==inventory(trial[file],key)
assert trees['atlas.json']['edges']==trial['atlas.json']['edges']
assert get('atlas.json','/claims/825/hypotheses/0')==trial['atlas.json']['claims'][825]['hypotheses'][0]
raw_before=json.dumps(trees,ensure_ascii=False)
raw_after=json.dumps(trial,ensure_ascii=False)
for phrase in ['author draft','frozen native weight quotients']:
    assert raw_before.count(phrase)==raw_after.count(phrase)>0
for op in ops:
    assert op['after'].count('\\(')==op['after'].count('\\)')
    stripped=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]','',op['after'],flags=re.S)
    assert not re.search(r'G_m|M_A1|N_12|N_13|N_23|b_j|u_B|C_V|H_b|R_N|\badopted\b',stripped,re.I)
validation={'status':'PASS local exact guards and protected-field retention; main owns final rendering/native QA',
    'replacements':21,'math_logical_fields':18,'process_wording_fields':3,
    'nine_u_B_copies_all_preserved':True,'rendered_duplicates_deduplicated':True,
    'status_ids_sources_urls_edges_unchanged':True,'essay_untouched':True,
    'protected_citation_and_frozen_phrase_unchanged':True,'unadopted_false_positive_untouched':True,
    'new_research_review_or_worker':False,'writes_outside_author_folder':False}
def dump(name,value):(A/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
dump('DELTA.json',{'schema':'bounded-final-render-author-delta/v1','scope':intake['scope'],
    'beforefilepins':intake['baselines'],'replacements':ops,'list_appends':[],'essay_edits':[],
    'application_order':'Apply exact scalar guards to the installed-baseline copies before main final render. No old-seal mutation is authorized.'})
dump('READS.json',{'scope':'Typography and three process-wording corrections only.',
    'intake':{'path':str(P/'coordination/INTAKE.json'),'sha256':sha((P/'coordination/INTAKE.json').read_bytes()),'read_scope':'complete'},
    'brief':{'path':str(P/'coordination/BRIEF.txt'),'sha256':sha((P/'coordination/BRIEF.txt').read_bytes()),'read_scope':'complete'},
    'audit':{'path':str(P/'baselines/combined-audit.json'),'sha256':sha((P/'baselines/combined-audit.json').read_bytes()),'read_scope':'16 raw-formula and three whole-word adopted warnings as quoted in complete intake; stable-ID warnings excluded'},
    'consumer_reads':[{'file':f,'sha256':next(x['sha256'] for x in intake['baselines'] if x['snapshot'].endswith('/'+f)),'pointers':[o['pointer'] for o in ops if o['file']==f],'read_scope':'Complete selected scalar fields in their surrounding mathematical context; full parse/hash for protection checks only'} for f in trees],
    'notation_controls':['M_A1 is the explicitly named affine-line carrier, also written A¹ in the preceding hypothesis.','B in u_B, J in pointing arrows, and charge q are preserved exactly; rank n and precision N remain distinct.'],
    'underlying_proofs_read':False,'essay_read_scope':'Hash verification only; no essay edit required.'})
dump('VALIDATION.json',validation)
reads=json.loads((A/'READS.json').read_text())
reads['allowed_scope']={'path':str(P/'coordination/EXPECTED-SCOPE.json'),'sha256':sha((P/'coordination/EXPECTED-SCOPE.json').read_bytes()),'read_scope':'complete'}
reads['notation_source']=notation_pin
reads['full_context_records_read']=['atlas.json:/claims/826','atlas.json:/claims/832','atlas.json:/claims/834','atlas.json:/claims/835','atlas.json:/claims/847','atlas.json:/claims/848','atlas.json:/claims/849','atlas.json:/comparisons/72','atlas.json:/comparisons/75']
dump('READS.json',reads)
(A/'HANDOFF.md').write_text('Ready for main composition: DELTA.json contains 21 exact scalar guards, comprising 18 mathematical typography fields and three process-wording fields. Nine repeated u_B hypotheses are repaired consistently; repeated rendered warnings for one logical field produce only one operation. Scientific statements, statuses, quantifiers, IDs, source links and old edges remain intact. The essay, legitimate author-draft citation, frozen-native-weight-quotient phrase and unadopted substring are unchanged. Main retains final rendering/native QA and installation. No prior seal or shared file was edited.\n')
dump('CHECKPOINT.json',{'task':'Bounded final-render author correction','status':'complete; main render/nativeQA pending','replacements':21,'delta_sha256':sha((A/'DELTA.json').read_bytes()),'ownership':str(A),'no_old_seal_mutation':True})
print(json.dumps({'delta':sha((A/'DELTA.json').read_bytes()),'reads':sha((A/'READS.json').read_bytes()),'validation':validation},indent=2))
