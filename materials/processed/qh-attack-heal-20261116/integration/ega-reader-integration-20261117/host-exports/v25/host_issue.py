"""Check the Git objects and browser-visible files on the two publication hosts."""
from concurrent.futures import ThreadPoolExecutor
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import subprocess
from urllib.request import Request, urlopen

HERE=Path(__file__).resolve().parent
loader=spec_from_file_location('reader_host_export',HERE/'host-export.py')
exporter=module_from_spec(loader)
loader.loader.exec_module(exporter)
NAMES=exporter.NAMES
PRIMARY_URL=exporter.OFFICIAL
RESEARCH_URL='https://research.momentum.inc/quantum-holography/'
MOUNT='quantum-holography'
pin=exporter.pin
read=exporter.json_file


def git(repo,*args):
    return subprocess.check_output(['git','--no-optional-locks','-C',str(repo),*args])


def object_bytes(repo,commit,name):
    return git(repo,'show',commit+':'+MOUNT+'/'+name)


def check_package(wanted):
    path=HERE/'HOST-READY.json'
    if pin(path.read_bytes())['sha256']!=wanted:
        raise ValueError('Unexpected hosted publication package')
    guard=read(path)
    for name,signature in guard['files'].items():
        if (HERE/name).resolve().parent!=HERE and (HERE/name).resolve().parent!=HERE/'headers':
            raise ValueError('Unexpected host asset path')
        if pin((HERE/name).read_bytes())!=signature:raise ValueError('Changed host asset '+name)
    return guard


def verify_git_role(label,repo,commit,base,expected_parent_files,expected_files):
    if len(commit)!=40 or any(c not in '0123456789abcdef' for c in commit):
        raise ValueError('Expected a complete '+label+' Git commit')
    if git(repo,'rev-parse',commit).decode().strip()!=commit:
        raise ValueError('Unresolved '+label+' publication')
    parent=git(repo,'rev-parse',commit+'^1').decode().strip()
    git(repo,'merge-base','--is-ancestor',base,parent)
    before={n:object_bytes(repo,parent,n) for n in NAMES}
    produced={n:object_bytes(repo,commit,n) for n in NAMES}
    oldpins={n:pin(b) for n,b in before.items()};actual={n:pin(b) for n,b in produced.items()}
    if oldpins!=expected_parent_files or actual!=expected_files:
        raise ValueError('Unexpected '+label+' predecessor or issued payload')
    wanted=sorted(MOUNT+'/'+n for n in NAMES if before[n]!=produced[n])
    changed=sorted(git(repo,'diff','--name-only',parent,commit,'--',MOUNT+'/').decode().splitlines())
    if wanted!=changed:raise ValueError('Extra or missing '+label+' reader paths')
    return {'repository':str(repo),'commit':commit,'parent':parent,'expected_ancestor':base,'previous_files':oldpins,'files':actual,'changed_reader_paths':wanted},produced


def verify_publication(edition,primary_commit,research_commit,package_sha):
    guard=check_package(package_sha)
    binding=read(HERE/'HEADERS.json')
    mounts=read(HERE/'MOUNTED-REPRODUCTION.json')
    clean=read(edition/'EXPECTED-PUBLIC.json')
    ready=read(edition/'LOCAL-READY.json')
    if ready['public_files']!=clean or ready['scope'] not in mounts['variants']:raise ValueError('Unknown pure reader scope')
    branch=mounts['variants'][ready['scope']]
    if branch['pure']!=clean or read(HERE/('EXPECTED-HOSTED-'+ready['scope']+'.json'))!=branch['hosted']:
        raise ValueError('Mismatched clean and mounted editions')
    base=read(edition/'verification/V24-ISSUED-BASELINE.json')
    a=binding['standalone_research'];m=binding['standalone_primary'];h=binding['primary_parent_observed']
    if a['files']!=base['four_files'] or a['commit']!=base['commit'] or m['files']!=a['files']:
        raise ValueError('Wrong portable v24 ancestry')
    headers=exporter.read_headers()
    for n in NAMES:
        clean_old=object_bytes(a['repository'],a['commit'],n)
        official_clean=object_bytes(m['repository'],m['commit'],n)
        first_mounted=object_bytes(h['repository'],binding['analytics_introduction'],n)
        last_mounted=object_bytes(h['repository'],h['commit'],n)
        if clean_old!=official_clean or pin(clean_old)!=a['files'][n] or first_mounted!=last_mounted or exporter.transform(n,clean_old,headers,canonical=False)!=last_mounted:
            raise ValueError('Earlier witnessed host history differs on '+n)
    primary,new_primary=verify_git_role('primary',h['repository'],primary_commit,h['commit'],h['files'],branch['hosted'])
    research,new_research=verify_git_role('research',a['repository'],research_commit,a['commit'],a['files'],clean)
    for n in NAMES:
        if exporter.transform(n,new_research[n],headers)!=new_primary[n] or exporter.transform(n,new_primary[n],headers,reverse=True)!=new_research[n]:
            raise ValueError('The roles differ beyond the exact approved header for '+n)
    primary['url']=PRIMARY_URL;research['url']=RESEARCH_URL
    return {'schema':'qh-issued-both-hosts/1','scope':ready['scope'],'edition':edition.name,'primary':primary,'research':research,'pure_files':clean,'hosted_files':branch['hosted'],'pure_ready':pin((edition/'LOCAL-READY.json').read_bytes()),'host_package_sha256':package_sha,'canonical':{n:PRIMARY_URL+('' if n=='index.html' else n) for n in NAMES[:3]},'previous_standalone_primary':m,'previous_standalone_research':a,'host_header_introduction':binding['analytics_introduction'],'header_manifest':guard['files']['HEADERS.json']}


def read_https(record):
    checks={}
    def fetch(row):
        role,name=row;url=record[role]['url']+name
        req=Request(url,headers={'User-Agent':'EGA-public-readback/1.0','Accept-Encoding':'identity'})
        with urlopen(req,timeout=45) as r:
            if r.status!=200 or r.geturl()!=url:raise ValueError('Unexpected HTTP resolution at '+url)
            actual=pin(r.read())
        if actual!=record[role]['files'][name or 'index.html']:raise ValueError('Remote bytes differ at '+url)
        return url,{'status':200,**actual}
    with ThreadPoolExecutor(max_workers=6) as workers:
        for url,row in workers.map(fetch,[(role,name) for role in ('primary','research') for name in ('',*NAMES)]):checks[url]=row
    return checks



def catalog_entry(issue,raw_index):
    return {'edition':'v25','commit':issue['primary']['commit'],'repository':issue['primary']['repository'],
            'pins':issue['hosted_files'],'rawIndex':{'path':'controls/v25-raw-index.js',**raw_index},
            'standalone':{'repository':issue['research']['repository'],'commit':issue['research']['commit'],'pins':issue['pure_files']},
            'primaryMount':{'url':PRIMARY_URL,'packageSha256':issue['host_package_sha256']},'standaloneUrl':RESEARCH_URL}
