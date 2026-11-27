#!/usr/bin/env python3
"""Render maintained author essays with the existing article template."""
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
    def __init__(self, html):
        super().__init__()
        self.ids, self.links, self.h1 = [], [], 0
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if 'id' in attributes:
            self.ids.append(attributes['id'])
        if tag == 'a' and 'href' in attributes:
            self.links.append(attributes['href'])
        if tag == 'h1':
            self.h1 += 1


def checked_bytes(path, expected):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError(f'Source changed: {path.relative_to(ROOT)}')
    return raw


def render(article, config, template):
    source = ROOT / config['source_directory'] / (article['slug'] + '.md')
    raw = checked_bytes(source, article['source_sha256'])
    checked_bytes(ROOT / article['archived_source'], article['archive_sha256'])
    heading, markdown = raw.decode().split('\n', 1)
    if heading != '# ' + article['title']:
        raise ValueError(f'Source title mismatch: {source.name}')
    body = subprocess.run(
        ['pandoc', '--from=markdown', '--to=html5', '--mathml',
         '--section-divs', '--wrap=none', '--fail-if-warnings'],
        input=markdown, text=True, capture_output=True, check=True,
    ).stdout

    def metadata(match):
        data = json.loads(match[2])
        data['@type'] = 'Article'
        data['headline'] = article['title']
        data['description'] = article['description']
        data['dateModified'] = config['revision_date']
        if article.get('publication_date'):
            data['datePublished'] = article['publication_date']
        serialized = json.dumps(data, ensure_ascii=False, indent=4).replace('<', '\\u003c')
        return match[1] + '\n' + serialized + '\n    ' + match[3]

    html = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',
                  metadata, template, flags=re.S)
    values = {
        'title': escape(article['title']),
        'description': escape(article['description'], quote=True),
        'subtitle': escape(article['subtitle']),
        'slug': article['slug'],
        'metaHtml': escape(article['date_label']),
        'content': body,
    }
    for key, value in values.items():
        html = html.replace('{{' + key + '}}', value)
    html = html.replace('</head>', '<link rel="stylesheet" href="reader-papers.css">\n</head>')
    page = Page(html)
    if page.h1 != 1 or len(page.ids) != len(set(page.ids)):
        raise ValueError(f'Heading or identifier error: {article["slug"]}')
    for link in page.links:
        if link.startswith('#') and link[1:] not in page.ids:
            raise ValueError(f'Missing reference {link}: {article["slug"]}')
    if '{{' in html:
        raise ValueError(f'Unresolved template: {article["slug"]}')
    if re.findall(r'<style\b[^>]*>.*?</style>', html, re.S) != re.findall(r'<style\b[^>]*>.*?</style>', template, re.S):
        raise ValueError(f'Article changed template styles: {article["slug"]}')
    return html


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check maintained HTML without writing')
    parser.add_argument('slugs', nargs='*', help='Build only these configured essays')
    args = parser.parse_args()
    config = json.loads((ROOT / 'compiler/author-essays.json').read_text())
    template = checked_bytes(ROOT / 'compiler/template.html', config['template_sha256']).decode()
    articles = config['articles']
    slugs = [article['slug'] for article in articles]
    if len(slugs) != len(set(slugs)) or any(slug not in slugs for slug in args.slugs):
        raise ValueError('Duplicate or unknown article slug')
    for article in articles:
        if args.slugs and article['slug'] not in args.slugs:
            continue
        html = render(article, config, template)
        output = ROOT / (article['slug'] + '.html')
        if args.check:
            if output.read_text() != html:
                raise ValueError(f'HTML differs from maintained source: {output.name}')
        else:
            output.write_text(html)
        print(f'{"CHECKED" if args.check else "BUILT"} {output.name}')


if __name__ == '__main__':
    main()
