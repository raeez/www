"""Completeness of the atlas on a built page (or draft): everything in the atlas.json is drawn, with its stable anchor.

    python3 -B completeness.py <page.html> <atlas.json> [--baseline <earlier page.html>]

Checked: every domain, claim, comparison and reading path has its anchor (atlas-d-, atlas-c-, atlas-r-, atlas-k-,
atlas-p-); each claim carries its status code and its own supplied label, and lists every hypothesis; every edge is
listed in both claims' lists and drawn once in the map; every comparison lists each of its claims; every path shows
every stage; each domain lists its conventions; every question id has its link. With --baseline, the atlas anchors
of the earlier page that this page no longer has are listed (stable anchors; listed, not failed)."""
import html
import json
import re
import sys


def section(page):
    """The atlas section, to its own closing tag (sections inside it are counted)."""
    m = re.search(r'<section\b[^>]*\sid="atlas"[^>]*>', page)  # the id, wherever it stands in the tag
    a = m.start() if m else -1
    if a < 0:
        return ''
    depth = 0
    for t in re.finditer(r'<(/?)section\b[^>]*>', page[a:]):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return page[a:a + t.end()]
    return page[a:]


ID_PART = re.compile(r'^(?:[tnbrpc]\d{1,3}|e[1-8])$')  # parts shaped like the page's internal identifiers


def content_findings(data):
    """Listed for the content owner, never failed: id parts shaped like internal identifiers (they reach the
    address bar) and relation codes with more than one label. (Per-record status labels are display aliases under the
    status-language ruling and are not shown, so their variation is not a finding.)"""
    out = []
    ids = [('domain', x['id']) for x in data['domains']] + [('claim', x['id']) for x in data['claims']] + \
          [('comparison', x['id']) for x in data['comparisons']] + [('path', x['id']) for x in data['readingPaths']]
    shaped = [f'{k} {i}' for k, i in ids if any(ID_PART.match(p) for p in re.split(r'[-_]', i))]
    if shaped:
        out.append(f'{len(shaped)} ids have a part shaped like an internal identifier (shown in addresses), e.g. ' + ', '.join(shaped[:6]))
    bare = [e['id'] for e in data['edges'] if e['label'].strip() == e['relation'].strip()]
    if bare:
        out.append(f'{len(bare)} edges have their relation code as their label, shown as text in the relation sentences, e.g. ' + ', '.join(bare[:6]))
    rel = {}
    for e in data['edges']:
        rel.setdefault(e['relation'], set()).add(e['label'])
    for code, ls in sorted(rel.items()):
        if len(ls) > 1:
            out.append(f'relation {code!r} has {len(ls)} labels: ' + '; '.join(sorted(ls)))
    return out


def element(sec, eid, tag=None):
    """The element with this id, to its own closing tag, whatever its tag (article, details, div)."""
    m = re.search(r'<([a-z][\w-]*)\b[^>]*\sid="' + re.escape(eid) + r'"', sec)
    if not m:
        return ''
    tag = m.group(1)
    depth, i = 0, m.start()
    for t in re.finditer(r'<(/?)' + tag + r'\b[^>]*>', sec[m.start():]):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return sec[m.start():m.start() + t.end()]
    return sec[m.start():]


def main(argv):
    page = open(argv[1], encoding='utf-8').read()
    data = json.load(open(argv[2], encoding='utf-8'))
    sec = section(page)
    if not sec:
        print('FAIL: no atlas section on the page')
        return 1
    ids = set(re.findall(r'\sid="([^"]+)"', sec))
    bad = []

    def need(cond, what):
        if not cond:
            bad.append(what)

    for d in data['domains']:
        need('atlas-d-' + d['id'] in ids, f'domain {d["id"]}: no anchor')
        conv = d.get('conventions') or []
        if conv:
            card = element(sec, 'atlas-d-' + d['id'])
            box = re.search(r'<div class="atlas-conventions"[^>]*>(.*?)</div>', card, re.S)
            need(box and len(re.findall(r'<li>', box.group(1))) == len(conv), f'domain {d["id"]}: conventions not all listed')
    for c in data['claims']:
        aid = 'atlas-c-' + c['id']
        need(aid in ids, f'claim {c["id"]}: no anchor')
        need('atlas-r-' + c['id'] in ids, f'claim {c["id"]}: no index row')
        art = element(sec, aid)
        if not art:
            continue
        head = art[:art.find('>') + 1]
        need(f'data-status-code="{c["status"]["code"]}"' in head, f'claim {c["id"]}: status code missing')
        need(re.search(r'<span class="atlas-chip-group">[^<]+</span>', art) is not None,
             f'claim {c["id"]}: no status word (chosen by its code) is shown')
        need(re.search(r'data-qh-unit-status="[^"]+"', head) is not None, f'claim {c["id"]}: not offered to the page search with its page status')
        hyps = re.search(r'<ol class="atlas-hyps">(.*?)</ol>', art, re.S)
        n = len(re.findall(r'<li\b', hyps.group(1))) if hyps else 0
        need(n == len(c['hypotheses']), f'claim {c["id"]}: {n} hypotheses shown for {len(c["hypotheses"])}')
    tags = re.findall(r'<(?:li|path)\b[^>]*\sdata-edge-id="[^"]+"[^>]*>', sec)
    by_edge = {}
    for t in tags:
        eid = re.search(r'data-edge-id="([^"]+)"', t).group(1)
        cls = re.search(r'class="([^"]*)"', t)
        by_edge.setdefault(eid, []).append(cls.group(1).split()[0] if cls else '')
    for e in data['edges']:
        kinds = by_edge.get(e['id'], [])
        need(kinds.count('atlas-rel') == 2, f'edge {e["id"]}: listed {kinds.count("atlas-rel")} times for 2 (both claims)')
        need(kinds.count('atlas-edge') == 1, f'edge {e["id"]}: drawn {kinds.count("atlas-edge")} times in the map for 1')
    buckets = ('establishedClaimIds', 'conditionalClaimIds', 'scopedNegativeClaimIds', 'remainingClaimIds')
    listed = 0
    for k in data['comparisons']:
        kid = 'atlas-k-' + k['id']
        need(kid in ids, f'comparison {k["id"]}: no anchor')
        art = element(sec, kid)
        for b in buckets:
            for cid in k.get(b) or []:
                listed += 1
                need(f'href="#atlas-c-{cid}"' in art, f'comparison {k["id"]}: claim {cid} not listed')
    for p in data['readingPaths']:
        pid = 'atlas-p-' + p['id']
        need(pid in ids, f'path {p["id"]}: no anchor')
        art = element(sec, pid)
        n = len(re.findall(r'<li class="atlas-stage[" ]', art))
        need(n == len(p['stages']), f'path {p["id"]}: {n} stages shown for {len(p["stages"])}')
        for s in p['stages']:
            for cid in s.get('claimIds') or []:
                need(f'href="#atlas-c-{cid}"' in art, f'path {p["id"]}: claim {cid} not linked')
    qids = [q for d in data['domains'] for q in d.get('relatedQuestionIds') or []]
    qids += [q for k in data['comparisons'] for q in ([k['questionId']] if k.get('questionId') else []) + (k.get('relatedQuestionIds') or [])]
    links = len(re.findall(r'class="atlas-question-link"', sec))
    need(links == len(qids), f'question links: {links} drawn for {len(qids)} question ids (an unresolved id fails the build)')
    print(f'atlas section: {len(data["domains"])} domains, {len(data["claims"])} claims, {len(data["edges"])} edges, '
          f'{len(data["comparisons"])} comparisons ({listed} listed claims), {len(data["readingPaths"])} paths, {len(qids)} question ids checked')
    if '--baseline' in argv:
        earlier = open(argv[argv.index('--baseline') + 1], encoding='utf-8').read()
        old = section(earlier)
        gone = sorted(i for i in set(re.findall(r'\sid="(atlas-[dckpr]-[^"]+)"', old)) if i not in ids)
        print(f'stable anchors: {len(gone)} atlas anchors of the earlier page are not on this page' + (': ' + ', '.join(gone[:30]) if gone else ''))
        here = set(re.findall(r'\sid="([^"]+)"', page))
        page_gone = sorted(i for i in set(re.findall(r'\sid="([^"]+)"', earlier.replace(old, ''))) if i not in here)
        print(f'stable anchors: {len(page_gone)} anchors of the earlier page outside the atlas are not on this page (listed, not failed)'
              + (': ' + ', '.join(page_gone[:30]) if page_gone else ''))
    for f in content_findings(data):
        print('  content finding:', f)
    for b in bad[:40]:
        print('  missing:', b)
    print('COMPLETENESS', 'PASS' if not bad else f'FAIL ({len(bad)})')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
