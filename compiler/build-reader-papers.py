#!/usr/bin/env python3
"""Render the seven retained Markdown papers through the site's article template."""
import argparse
import hashlib
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parent.parent


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.h1 = [], [], 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag == 'h1':
            self.h1 += 1


def render(paper, previous, following, config):
    source = ROOT / config['source_directory'] / (paper['slug'] + '.md')
    raw = source.read_bytes()
    if hashlib.sha256(raw).hexdigest() != paper['source_sha256']:
        raise ValueError(f"Source changed: {source.name}")
    heading, markdown = raw.decode().split('\n', 1)
    if heading != '# ' + paper['title']:
        raise ValueError(f"Source title mismatch: {source.name}")
    result = subprocess.run(
        ['pandoc', '--from=markdown', '--to=html5', '--mathml',
         '--section-divs', '--wrap=none', '--fail-if-warnings'],
        input=markdown, text=True, capture_output=True, check=True,
    )
    body = result.stdout
    # The source's two fifth-level subheads sit directly beneath second-level sections.
    # Preserve their text while giving the HTML a continuous heading hierarchy.
    body = re.sub(r'<(/?)h5(?=[ >])', r'<\1h3', body)
    # Add destinations only to the bibliography; preserve the complete paper text.
    def reference(match):
        prefix, ref_id, middle, title, suffix = match.groups()
        url = config['technical_links'].get(ref_id)
        if url:
            return prefix + ref_id + middle + f'<a href="{escape(url, quote=True)}">{title}</a>' + suffix
        return match.group(0)
    body = re.sub(r'(<div id=")(ref-[^\"]+)("[^>]*>\s*</div>\s*<p>.*?<em>)(.*?)(</em>)', reference, body)
    template = (ROOT / 'compiler/template.html').read_text()
    template = re.sub(r'[ \t]+(?=\n)', '', template)
    def metadata(match):
        data = json.loads(match[2])
        data['headline'] = paper['title']
        data['description'] = paper['description']
        return match[1] + '\n' + json.dumps(data, ensure_ascii=False, indent=4) + '\n    ' + match[3]
    template = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',
                      metadata, template, flags=re.S)
    values = {
        'title': escape(paper['title']),
        'description': escape(paper['description'], quote=True),
        'subtitle': escape(paper['description']),
        'slug': paper['slug'],
        'metaHtml': 'September 2026',
        'content': body,
    }
    for key, value in values.items():
        template = template.replace('{{' + key + '}}', value)
    template = template.replace('</head>', '<link rel="stylesheet" href="reader-papers.css">\n</head>')
    links = []
    for item, relation, label in ((previous, 'prev', 'Previous'), (following, 'next', 'Next')):
        if item:
            links.append(f'<a rel="{relation}" href="{item["slug"]}.html">{label}: {escape(item["title"])}</a>')
    sequence = '<nav class="reading-sequence" aria-label="Reading sequence">' + '\n'.join(links) + '</nav>\n'
    template = template.replace('            <footer class="article-footer">', sequence + '            <footer class="article-footer">')
    return template


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify checked-in HTML against retained sources')
    args = parser.parse_args()
    config = json.loads((ROOT / 'compiler/reader-papers.json').read_text())
    papers = config['papers']
    if len(papers) != 7 or len({p['slug'] for p in papers}) != 7:
        raise ValueError('Expected seven distinct papers')
    for index, paper in enumerate(papers):
        html = render(paper, papers[index-1] if index else None,
                      papers[index+1] if index+1 < len(papers) else None, config)
        page = Page(html)
        if page.h1 != 1 or len(page.ids) != len(set(page.ids)):
            raise ValueError(f"Heading/identifier error: {paper['slug']}")
        for link in page.links:
            if link.startswith('#') and link[1:] not in page.ids:
                raise ValueError(f"Missing reference {link}: {paper['slug']}")
            if re.search(r'\.pdf(?:[?#]|$)', link, re.I):
                raise ValueError(f"PDF publication link: {link}")
        if '{{' in html or 'application/pdf' in html:
            raise ValueError(f"Unresolved template or PDF metadata: {paper['slug']}")
        output = ROOT / (paper['slug'] + '.html')
        if args.check:
            if output.read_text() != html:
                raise ValueError(f"HTML differs from source rendering: {output.name}")
        else:
            output.write_text(html)
        print(f"{'CHECKED' if args.check else 'BUILT'} {output.name}: {len(page.ids)} anchors")


if __name__ == '__main__':
    main()
