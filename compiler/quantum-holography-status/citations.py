"""Bibliographical locators that remain usable in the offline book and its printed pages."""
import re
from urllib.parse import unquote, urlsplit

ARXIV = re.compile(r'/(?:abs|html|pdf)/([\w.-]+/\d{7}(?:v\d+)?|\d{4}\.\d{4,5}(?:v\d+)?)(?:\.pdf)?/?$', re.I)
DOI = re.compile(r'(10\.\d{4,9}/[-._;()/:A-Z0-9]+)$', re.I)
STACKS = re.compile(r'/tag/([0-9A-Z]{4})/?$')


def locator_suffix(target, label):
    """Return missing identifiers and PDF page locators as plain bibliographical text."""
    try:
        url = urlsplit(target)
        host = (url.hostname or '').lower().removeprefix('www.')
    except ValueError:
        return ''
    path = unquote(url.path)
    parts = []
    if host == 'arxiv.org' and (m := ARXIV.fullmatch(path)):
        if m[1].lower() not in label.lower():
            parts.append('arXiv:' + m[1])
    elif host in ('doi.org', 'dx.doi.org', 'link.springer.com', 'journals.aps.org') and (m := DOI.search(path)):
        if m[1].lower() not in label.lower():
            parts.append('doi:' + m[1])
    elif host == 'stacks.math.columbia.edu' and (m := STACKS.fullmatch(path)):
        if m[1] not in label:
            parts.append('Tag ' + m[1])
    page = re.fullmatch(r'page=([1-9]\d*)', url.fragment)
    if page and not re.search(r'\bPDF\s+(?:p\.|page)\s*' + page[1] + r'\b', label, re.I):
        parts.append('PDF p. ' + page[1])
    return ' (' + ', '.join(parts) + ')' if parts else ''
