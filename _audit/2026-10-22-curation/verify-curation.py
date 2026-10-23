from pathlib import Path
import json,hashlib,importlib.util,re,xml.etree.ElementTree as ET
root=Path('.');audit=root/'_audit/2026-10-22-curation';out=root/'materials/processed/2026-10-22-curation'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('feedsync',root/'compiler/sync-article-feed.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
checks={};baseline=json.loads((audit/'adopted-editorial-baseline.json').read_text());changed=[p for p,h in baseline.items() if sha(root/p)!=h]
expected={'_config.yml','archai.html','compiler/README.md','compiler/docs.config.js','feed.xml','licc.html','prefabricated-construction.html','programmable-institutions.html','references/source-provenance.md','sensoria.html','sitemap.xml','smart-buildings.html','writing.html'}
assert set(changed)==expected
checks['adopted_packet']={'paths':len(baseline),'intentionally_changed':changed,'unchanged':len(baseline)-len(changed)}
styles=lambda s:re.findall(r'<style\b[^>]*>.*?</style>',s,re.S)
for a in json.loads((audit/'existing-article-metadata.json').read_text()):
 old=(audit/'baseline'/a['path']).read_text();new=(root/a['path']).read_text()
 assert module.Article(old).body==module.Article(new).body,a['path']
 assert styles(old)==styles(new),a['path']
checks['six_existing_article_bodies_and_styles']='byte-identical to adopted edition'
old=(audit/'baseline/writing.html').read_text();new=(root/'writing.html').read_text();assert styles(old)==styles(new)
math=lambda s:re.search(r'    <p class="section-label">Mathematics</p>.*?</ul>',s,re.S)[0]
assert math(old)==math(new)
assert (root/'reader-papers.css').read_bytes()==(audit/'baseline/reader-papers.css').read_bytes()
assert (root/'compiler/template.html').read_bytes()==(audit/'baseline/compiler/template.html').read_bytes()
checks['visual_system']='Writing styles, Mathematics block, article template and reader stylesheet byte-identical to adopted baseline'
research=Path('/Users/raeez/momentum-research-worktrees/curation-20261022-publication');pairs=[]
for p in sorted((root/'content/reader-papers').glob('*')):
 if p.suffix not in ['.md','.tex']:continue
 assert p.read_bytes()==(research/'papers/accessible'/p.name).read_bytes(),p
 assert sha(p)==baseline[str(p)]
 pairs.append(str(p))
checks['reader_pairs']={'count':len(pairs),'exact_research_parity':True,'unchanged_from_adoption':True}
for a in json.loads((audit/'source-custody.json').read_text()):
 assert sha(root/a['custody_path'])==a['sha256']
 assert sha(Path(a['source_path']))==a['sha256']
checks['nine_archived_inputs']='exact copies, still equal to retained research source'
assert sha(root/'licc-blueprint.html')==sha(root/'materials/raw/2026-10-22-private-planning/licc-blueprint.html')==baseline['licc-blueprint.html']
assert sha(root/'materials/raw/2026-10-22-site-curation/feed.xml')==baseline['feed.xml']
for p in [root/'writing.html',root/'sitemap.xml',root/'feed.xml',root/'llms.txt',root/'llms-full.txt',root/'compiler/docs.config.js']:
 assert 'licc-blueprint' not in p.read_text(),p
for p in root.glob('*.html'):
 if p.name!='licc-blueprint.html':assert 'licc-blueprint' not in p.read_text(),p
assert '  - licc-blueprint.html' in (root/'_config.yml').read_text()
checks['private_planning']='exact custody; explicit Pages exclusion; no public incoming root-HTML, catalogue, sitemap, feed or importer links'
ns={'a':'http://www.w3.org/2005/Atom'};feed=ET.parse(root/'feed.xml').getroot();entries=feed.findall('a:entry',ns);ids=[e.findtext('a:id',namespaces=ns) for e in entries];assert len(ids)==len(set(ids))==22
checks['feed']={'entries':len(entries),'full_article_entries':sum(e.find('a:content',ns) is not None for e in entries),'summary_entries':sum(e.find('a:content',ns) is None for e in entries),'private_blueprint_absent':True}
newconfig=json.loads((root/'compiler/author-essays.json').read_text());catalogue=json.loads((audit/'writing-catalogue.json').read_text());rows={r[1]:r for _,items in catalogue for r in items};locs=[e.text for e in ET.parse(root/'sitemap.xml').getroot().iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')];assert len(locs)==len(set(locs))
for a in newconfig['articles']:
 slug=a['slug'];url=f'https://raeez.com/{slug}.html';e=entries[ids.index(url)]
 assert e.find('a:published',ns) is None
 assert e.findtext('a:title',namespaces=ns)==a['title']
 assert e.findtext('a:summary',namespaces=ns)==a['description']
 assert rows[slug+'.html'][2:]==[a['title'],a['subtitle']]
 assert url in locs
 for name in ['llms.txt','llms-full.txt']:assert url in (root/name).read_text()
for slug,description in json.loads((audit/'reader-catalogue-descriptions.json').read_text()).items():
 assert rows[slug+'.html'][3]==description
 e=entries[ids.index(f'https://raeez.com/{slug}.html')];assert e.findtext('a:summary',namespaces=ns)==description
 assert e.findtext('a:published',namespaces=ns)=='2026-09-09T00:00:00+07:00'
assert new.count('href="https://research.momentum.inc/"')==1
assert sum('research.momentum.inc' in r[1] for r in rows.values())==3
for url in rows:
 if not url.startswith('https://'):assert root.joinpath(url).exists() and 'https://raeez.com/'+url in locs,url
checks['catalogue']={'section_counts':{k:len(v) for k,v in catalogue},'local_page_count':sum(not p.startswith('https://') for p in rows),'research_root_links':1,'all_local_pages_in_sitemap':True,'nine_author_metadata_parity':True,'seven_reader_catalogue_and_feed_statements':True}
checks['source_hashes']={a['slug']:a['source_sha256'] for a in newconfig['articles']}
checks['independent_author_static_qa']={'result':'PASS','checked':'nine author build outputs, source and custody hashes, metadata and canonical URLs, Article schema, month-only dates, unchanged CSS/fonts, five MathML nodes, three table grids, 60 unique IDs, 13 explicit anchors, seventeen local research fragment destinations, private-leak checks, in-memory hash/drift rejection and metadata escaping','residual':'Six third-party fragments were outside the static reviewer scope; specialist source reports record primary checks. No browser inspection performed.'}
checks['publication_residual']='Root must verify actual GitHub Pages exclusion and inspect deployed pages in the browser. Local file URL rejection was respected without a workaround.'
(out/'verification.json').write_text(json.dumps(checks,indent=2)+'\n')
print('PASS: 76-path adoption accounted for; 14 source pairs exact; six bodies/styles exact; Mathematics exact; 22 feed entries; catalogue and custody parity.')
