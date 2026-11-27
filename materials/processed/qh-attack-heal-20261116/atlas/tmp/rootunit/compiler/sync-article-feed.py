#!/usr/bin/env python3
"""Synchronize existing full-article feed entries from maintained local pages."""
import argparse
import hashlib
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent.parent


class Article(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.source = source
        self.lines = [0]
        for match in re.finditer('\n', source):
            self.lines.append(match.end())
        self.depth = 0
        self.start = self.end = None
        self.capture = None
        self.title = self.subtitle = self.description = ''
        self.feed(source)
        if self.start is None or self.end is None:
            raise ValueError('Expected one complete article-body element')
        self.body = source[self.start:self.end]

    def source_offset(self):
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = attrs.get('content', '')
        if 'article-title' in classes:
            self.capture = ('title', tag)
        elif 'article-subtitle' in classes:
            self.capture = ('subtitle', tag)
        if tag == 'div':
            if self.depth:
                self.depth += 1
            elif 'article-body' in classes:
                if self.start is not None:
                    raise ValueError('Multiple article-body elements')
                self.depth = 1
                self.start = self.source_offset() + len(self.get_starttag_text())

    def handle_endtag(self, tag):
        if self.capture and self.capture[1] == tag:
            self.capture = None
        if tag == 'div' and self.depth:
            self.depth -= 1
            if not self.depth:
                self.end = self.source_offset()

    def handle_data(self, data):
        if self.capture:
            name = self.capture[0]
            setattr(self, name, getattr(self, name) + data)


def replace_once(pattern, replacement, source):
    result, count = re.subn(pattern, lambda match: replacement, source, count=1, flags=re.S)
    if count != 1:
        raise ValueError(f'Missing feed field: {pattern}')
    return result


def synchronize(entry, article, slug):
    url = f'https://raeez.com/{slug}.html'
    content = ('<div class="feed-content">\n'
               f'  <p><em>{escape(article.subtitle or article.description)}</em></p>\n'
               f'  {article.body}\n'
               '  <hr/>\n'
               f'  <p><a href="{url}">Read the full article on raeez.com →</a></p>\n'
               '</div>')
    content = content.replace(']]>', ']]]]><![CDATA[>')
    entry = replace_once(r'<content type="html">.*?</content>',
                         f'<content type="html"><![CDATA[{content}]]></content>', entry)
    entry = replace_once(r'<title type="text">.*?</title>',
                         f'<title type="text">{escape(article.title)}</title>', entry)
    entry = replace_once(r'<summary type="text">.*?</summary>',
                         f'<summary type="text">{escape(article.description)}</summary>', entry)
    digest = hashlib.sha256(article.body.encode()).hexdigest()[:16]
    return replace_once(r'<dc:identifier>.*?</dc:identifier>',
                        f'<dc:identifier>urn:sha256:{digest}</dc:identifier>', entry)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slugs', nargs='+', help='Existing full-article feed entries to synchronize')
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--updated', help='ISO timestamp for entries whose content changes')
    args = parser.parse_args()
    if not args.check and not args.updated:
        parser.error('--updated is required when writing the feed')
    requested = set(args.slugs)
    if any(not re.fullmatch(r'[a-z0-9-]+', slug) for slug in requested):
        parser.error('Slugs must contain lowercase letters, digits, and hyphens')
    source = (ROOT / 'feed.xml').read_text()
    found, changed = set(), []

    def entry(match):
        old = match.group()
        identity = re.search(r'<id>https://raeez.com/([a-z0-9-]+)\.html</id>', old)
        if not identity or identity[1] not in requested:
            return old
        slug = identity[1]
        if slug in found:
            raise ValueError(f'Duplicate feed entry: {slug}')
        found.add(slug)
        article = Article((ROOT / (slug + '.html')).read_text())
        new = synchronize(old, article, slug)
        if new != old:
            changed.append(slug)
            if not args.check:
                new = replace_once(r'<updated>.*?</updated>',
                                   f'<updated>{escape(args.updated)}</updated>', new)
        return new

    result = re.sub(r'<entry>.*?</entry>', entry, source, flags=re.S)
    ET.fromstring(result)
    if found != requested:
        raise ValueError(f'Missing feed entries: {sorted(requested - found)}')
    if args.check and changed:
        raise ValueError(f'Feed differs from local articles: {changed}')
    if changed:
        result = replace_once(r'<updated>.*?</updated>',
                              f'<updated>{escape(args.updated)}</updated>', result)
        (ROOT / 'feed.xml').write_text(result)
    print(f'{"CHECKED" if args.check else "SYNCHRONIZED"} {len(found)} entries; {len(changed)} changed')


if __name__ == '__main__':
    main()
