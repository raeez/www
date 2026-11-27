#!/usr/bin/env python3
"""Read the issued EGA commits and both live hosts into a verifiable receipt."""
import argparse
from datetime import datetime,timezone
import json
from pathlib import Path
from host_issue import pin,read,verify_publication,read_https

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pure_archive',type=Path)
    parser.add_argument('host_package_sha256')
    parser.add_argument('primary_commit')
    parser.add_argument('research_commit')
    parser.add_argument('output_directory',type=Path)
    parser.add_argument('--receipt',type=Path,action='append',default=[],help='bind an independent publisher or HTTPS receipt')
    a=parser.parse_args()
    record=verify_publication(a.pure_archive.resolve(),a.primary_commit,a.research_commit,a.host_package_sha256)
    record['bare_https']=read_https(record)
    record['independent_receipts']=[{'path':str(p.resolve()),**pin(p.read_bytes())} for p in a.receipt]
    out=a.output_directory/'OFFICIAL-ISSUE.json';out.parent.mkdir(exist_ok=True,parents=True)
    record['status']='PASS'
    if out.is_file():
        previous=read(out);record['at_utc']=previous['at_utc']
        if previous!=record:raise ValueError('Existing official issue record differs.')
    else:
        record['at_utc']=datetime.now(timezone.utc).isoformat()
        with out.open('x',encoding='utf-8') as f:f.write(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(out,pin(out.read_bytes())['sha256'])
if __name__=='__main__':main()
