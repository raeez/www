#!/usr/bin/env python3
"""Render raeez.com's hosted reader from a normal four-file EGA build."""
from hashlib import sha256
from pathlib import Path
import argparse
import json
import os
import re
import shutil
import tempfile

NAMES = ('index.html', 'reference.html', 'atlas.html', 'reader-index.js')
CONFIG = Path(__file__).resolve().parent
OFFICIAL = 'https://raeez.com/quantum-holography/'


def pin(raw):
    return {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)}


def json_file(path):
    return json.loads(path.read_bytes())


def read_headers(config=CONFIG):
    record=json_file(config/'HEADERS.json')
    result={}
    for name in NAMES[:3]:
        row=record['pages'][name];pair=[]
        for role in ('standalone','raeez_com'):
            item=row[role];p=config/item['path'];raw=p.read_bytes()
            if pin(raw)!={k:item[k] for k in ('bytes','sha256')}:
                raise ValueError('Unrecognized header in '+str(p))
            pair.append(raw)
        result[name]=tuple(pair)
    return result


def transform(name,raw,headers,reverse=False,canonical=True):
    if name=='reader-index.js':
        return raw
    i=raw.index(b'</head>')
    head,body=raw[:i],raw[i:]
    clean,mounted=headers[name]
    old,new=(mounted,clean) if reverse else (clean,mounted)
    marker=b'googletagmanager.com/gtag/js?id='
    if head.count(b'http-equiv="Content-Security-Policy"')!=1:
        raise ValueError('Expected exactly one policy in '+name)
    if old in head:
        if head.count(old)!=1 or (not reverse and marker in head):
            raise ValueError('Unexpected or duplicate analytics markup in '+name)
        head=head.replace(old,new,1)
    elif new not in head or head.count(new)!=1:
        raise ValueError('The reader header differs from both issued forms in '+name)
    if head.count(marker)!=(0 if reverse else 1) or head.count(b"gtag('config'")!=(0 if reverse else 1):
        raise ValueError('Unexpected analytics script count in '+name)
    if canonical:
        url=(OFFICIAL+('' if name=='index.html' else name)).encode()
        if head.count(b'<link rel="canonical" href="'+url+b'">')!=1 or head.count(b'<meta property="og:url" content="'+url+b'">')!=1:
            raise ValueError('Expected the official canonical and Open Graph addresses in '+name)
    return head+body


def export(source,destination,expected=None,config=CONFIG):
    source,destination=source.resolve(),destination.resolve()
    if source==destination:
        raise ValueError('Select a distinct directory for the raeez.com build.')
    headers=read_headers(config)
    output={n:transform(n,(source/n).read_bytes(),headers) for n in NAMES}
    hashes={n:pin(data) for n,data in output.items()}
    if expected is not None and hashes!=expected:
        raise ValueError('The hosted files differ from the accepted official export.')
    if destination.exists():
        if sorted(p.name for p in destination.iterdir())!=sorted(NAMES) or any((destination/n).read_bytes()!=output[n] for n in NAMES):
            raise FileExistsError('Existing hosted directory contains different files: '+str(destination))
        return hashes
    destination.parent.mkdir(exist_ok=True,parents=True)
    scratch=Path(tempfile.mkdtemp(prefix='.'+destination.name+'-',dir=destination.parent))
    try:
        for n,data in output.items():(scratch/n).write_bytes(data)
        os.rename(scratch,destination)
    finally:
        if scratch.exists():shutil.rmtree(scratch)
    return hashes


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('standalone_build',type=Path)
    p.add_argument('raeez_output',type=Path)
    p.add_argument('--expected',type=Path,help='verify this frozen hosted four-file hash table')
    args=p.parse_args()
    result=export(args.standalone_build,args.raeez_output,json_file(args.expected) if args.expected else None)
    print(json.dumps(result,indent=2))
