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


def place_figures(markdown, article):
    """Insert each configured figure after the paragraph containing its anchor, as the PDF does.

    A figure without an anchor opens the article body, where the PDF sets its cover figure.
    The essay text is not changed; only figure blocks are added between paragraphs.
    """
    figures = article.get('figures', [])
    for number, figure in reversed(list(enumerate(figures, 1))):
        path = ROOT / figure['src']
        if not path.is_file():
            raise ValueError(f'Missing figure {figure["src"]}: {article["slug"]}')
        size = re.search(r'<svg[^>]*\bwidth="([\d.]+)pt" height="([\d.]+)pt"', path.read_text()[:2000])
        width, height = (float(size[1]), float(size[2])) if size else (0, 0)
        scale = min(1.0, width / figure.get('column_pt', 380)) if width else 1.0
        # The SVGs keep a 4 pt crop margin; the bleed lets the drawn figure meet the text edges.
        bleed = figure.get('margin_pt', 4) / width if width else 0
        block = ('\n\n```{=html}\n'
                 f'<figure class="essay-figure" id="figure-{number}" style="--figure-scale:{scale:.3f};--figure-bleed:{bleed:.4f}">'
                 f'<a class="essay-figure-link" href="{escape(figure["src"], quote=True)}">'
                 f'<img src="{escape(figure["src"], quote=True)}" alt="{escape(figure["alt"], quote=True)}"'
                 + (f' width="{width * 4 / 3:.0f}" height="{height * 4 / 3:.0f}"' if width else '')
                 + (" loading=\"lazy\"" if number > 1 else "") + ' decoding="async"></a></figure>\n```\n')
        anchor = figure.get('after')
        if anchor is None:
            markdown = block.lstrip('\n') + '\n' + markdown.lstrip('\n')
            continue
        start = markdown.find(anchor)
        if start < 0 or markdown.find(anchor, start + 1) >= 0:
            raise ValueError(f'Figure anchor not found once: {anchor[:60]}')
        end = markdown.find('\n\n', start)
        end = len(markdown) if end < 0 else end
        markdown = markdown[:end] + block + markdown[end:]
    return markdown


def set_note(markdown, article):
    """Set the paragraph that begins with the configured prefix as a note below a rule."""
    prefix = article.get('note_prefix')
    if not prefix:
        return markdown
    matches = list(re.finditer(r'(?:^|\n\n)(' + re.escape(prefix) + r'[^\n]*(?:\n[^\n]+)*)', markdown))
    if len(matches) != 1:
        raise ValueError(f'Note paragraph not found once: {article["slug"]}')
    paragraph = matches[0]
    return (markdown[:paragraph.start(1)] + '::: {.article-note}\n' + paragraph[1] + '\n:::'
            + markdown[paragraph.end(1):])


def meta_line(article):
    """Date, then the author and a marked PDF link when configured, as on the research site."""
    parts = [escape(article['date_label'])]
    if article.get('meta_author'):
        parts.append(escape(article['meta_author']))
    if article.get('pdf'):
        label = escape(article.get('pdf_label', 'PDF'))
        marked = ' class="article-pdf"' if article.get('meta_author') else ''
        parts.append(f'<a{marked} href="{escape(article["pdf"], quote=True)}">{label}</a>')
    return ' · '.join(parts)


def render(article, config, template):
    source = ROOT / config['source_directory'] / (article['slug'] + '.md')
    raw = checked_bytes(source, article['source_sha256'])
    checked_bytes(ROOT / article['archived_source'], article['archive_sha256'])
    heading, markdown = raw.decode().split('\n', 1)
    if heading != '# ' + article['title']:
        raise ValueError(f'Source title mismatch: {source.name}')
    markdown = place_figures(markdown, article)
    markdown = set_note(markdown, article)
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
        data['dateModified'] = article.get('revision_date', config['revision_date'])
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
        'metaHtml': meta_line(article),
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
