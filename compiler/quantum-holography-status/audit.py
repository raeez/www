"""Checks run on every build of the status page.

Failures stop the page from being written to the repository root (unless --allow-draft):
  - a statement or cell with an unknown status, a missing cell, a TeX error, or a formula whose letters
    and digits the renderer would show differently;
  - unapproved external addresses and any resource that would load from another host;
  - an in-page link whose target does not exist;
  - reader-visible words that belong to project management rather than mathematics
    (the golden rule): names of tools or models, record and file names, paths, repository
    addresses, hashes, internal identifiers, workflow vocabulary, process stage labels, percentages
    and raw TeX. The same rules apply to the words of formulas, to every attribute value that is not
    technical, to image text, data blocks, page metadata, comments and the strings of the page
    script, and to element ids, which appear in shared addresses.
Warnings (reported, not blocking): words that may be workflow residue or may be mathematics and need the
content owner's reading, and statements without an id (no link reaches the statement itself).
"""
import base64
import binascii
import hashlib
import html
import re
import urllib.parse
import unicodedata
from collections import Counter
from html.parser import HTMLParser

from monograph import is_primary_page
from status import CELL_STATUSES, COLUMNS, STATEMENT_STATUSES, strip_tags

I = re.I
# Each rule is (pattern, reason, flags).
NAMES = (r'\b(astra|claude|codex|opus|fable|gpt-?\d|chatgpt|openai|anthropic|sonnet|haiku)\d*\b', 'model or tool name', I)
AGENTS = (r'\b(llm|language[ -]model|ai[ -]model|agent|subagent|prompt|chatbot)s?\b', 'model or agent vocabulary', I)
WORKFLOW = (r'\b(adoption|adopted[ -]record|inscribe|census|ledger|dossier|frontier[ -]engine|worktree|'
            r'commit|pull[ -]request|repository|pipeline|todo|backlog|audit|reviewer|checker|attacker|owner|ownership)s?\b',
            'workflow vocabulary', I)
SWARM = (r'\battack[- ]?heal\w*|\bswarms?\b', 'workflow vocabulary', I)
IDENT = (r'(?<![\w.])(T|N|B|R|P|C)\d{1,3}(?![\w])', 'internal identifier (or mathematics written without TeX)', 0)
E_IDENT = (r'(?<![\w.])E[1-8](?![\w])', 'possible internal identifier (or E_n written without subscript)', 0)
G_IDENT = (r'(?<![\w.])G\d{2,3}(?![\w])', 'internal identifier (or mathematics written without TeX)', 0)
VTAG = (r'\bv\d\b|-v\d\b', 'version tag (or a subscript written without TeX)', 0)
VERSION = (r'\b(version|revision)\s+\d+', 'version tag', I)
FILE = (r'\.(md|json|tex|py|tsv|csv|log)\b', 'file name', 0)
SOURCE_FILE = (r'\b[\w-]+\.(js|mjs|cjs|css|html?|ya?ml|sh|txt|diff|pdf)\b', 'file name', I)
PATH = (r'/Users/|~/[\w.-]|\b(?:engine|prep|chains|frontier|inscribe)/[\w.-]+(?:/|\.\w{1,4}\b)', 'path', 0)
LABEL = (r'\b[a-z]{2,5}:(thm|prop|lem|def|cor|qn|eq|sec|rem|op|cc|hyp|mix|p|t):[\w-]+', 'LaTeX label', 0)
# Capitalised or all-capital stage labels fail, also after a hyphen ("post-Wave 3"), and so do session, lane and
# sprint numbers in any case. The other stage words in lower case may be mathematics ("the s-wave 1", "phase 0")
# and are only warned about (WARN).
STAGE = (r'(?<!\w)(?:Wave|Phase|Session|Lane|Sprint|Round|Cycle|WAVE|PHASE|SESSION|LANE|SPRINT|ROUND|CYCLE)'
         r'[-\u2013\u2014 ]?[A-Z]?\d+\b', 'process stage label', 0)
STAGE_WORK = (r'(?<!\w)(session|lane|sprint)[-\u2013\u2014 ]?\d+\b', 'process stage label', I)
PERCENT = (r'\d+(?:\.\d+)?\s?%|\bper ?cent\b', 'percentage', I)
HASH = (r'(?<![0-9A-Za-z])(?=[0-9a-fA-F]*[a-fA-F])(?=[0-9a-fA-F]*\d)[0-9a-fA-F]{32,}(?![0-9A-Za-z])', 'hash', 0)
UUID = (r'(?<![0-9A-Za-z])[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}(?![0-9A-Za-z])', 'identifier (UUID)', 0)
# Only the four open repositories may be named anywhere; this page has no reason to name any.
REPO = (r'\b(?:github|gitlab|bitbucket|codeberg)\.(?:com|org)[/:](?!momentum-sez/(?:gstore|lex|op|stack)\b)[\w.-]+',
        'repository address', I)

WORDS = [NAMES, AGENTS, WORKFLOW, SWARM]   # names and workflow words; scanned on NFKC-folded text
IDENTIFIERS = [IDENT, E_IDENT, G_IDENT]    # shapes that formulas also produce (P1, C2): warnings outside prose
FORBIDDEN = WORDS + IDENTIFIERS + [VTAG, VERSION, FILE, PATH, LABEL, STAGE, STAGE_WORK, PERCENT, HASH, UUID, REPO]
SHAPELESS = [r for r in FORBIDDEN if r not in IDENTIFIERS and r is not PERCENT]  # formula text, reader attributes
CODE = WORDS + [VTAG, VERSION, FILE, PATH, LABEL, STAGE, STAGE_WORK, HASH, UUID, REPO]  # data attributes, prose strings
# Script strings that are code (one lower-case token: a class, an event, a variable's name) and comments are held to
# names, paths, files, hashes, labels, stage words and unmistakable workflow words, not to ordinary words such as
# owner, commit, agent or prompt.
RECORD_WORDS = (r'\b(ledger|dossier|inscribe|adoption|adopted[ -]record|census|worktree|frontier[ -]engine|backlog|'
                r'reviewer|attacker|subagent|llm|chatbot)s?\b', 'workflow vocabulary', I)
CODE_TOKENS = [r for r in CODE if r not in (AGENTS, WORKFLOW)] + [RECORD_WORDS]
SHAPELESS_TOKENS = [r for r in SHAPELESS if r not in (AGENTS, WORKFLOW)] + [RECORD_WORDS]
COMMENT = CODE_TOKENS + [SOURCE_FILE]

# Raw TeX delimiters left in reader text mean a formula was not set as mathematics.
RAW_TEX = (r'\\[()\[\]]', 'raw TeX in reader text', 0)
# TeX source in an attribute is read aloud or shown as code.
TEX_IN_ATTRIBUTE = re.compile(r'\\[A-Za-z()\[\]{}]')
# TeX source: names, files, paths, hashes and addresses only; ~ is a TeX tie and chains/cochains is mathematics.
TEX_FORBIDDEN = [NAMES, FILE, (r'/Users/|\b(?:engine|prep|frontier|inscribe)/[\w.-]+', 'path', 0), HASH, UUID, REPO,
                 LABEL]
TEX_WARN = [(r'\d\s*(?:\\[,;:!> ]|~)?\s*\\%', 'percentage in a formula', 0)]
# Element ids appear in shared addresses: no tool, workflow or path names, no work-stage or version numbers, no
# three-digit identifiers (t152) and no hashes; shorter identifier shapes, the other stage words and draft are
# warned about, since ids also come from mathematics (r3, e8, plane-wave-1, cycle-3).
ID_FORBIDDEN = WORDS + [
    (r'(?<![a-z0-9])(session|lane|sprint)-?\d+|/', 'stage number or path in an id', I),
    (r'(?<![a-z0-9])[tnbrpcg]\d{3}(?![a-z0-9])', 'internal identifier in an id', I),
    (r'(?<![a-z0-9])v\d+(?![a-z0-9])|(?<![a-z0-9])(version|revision)-?\d', 'version tag in an id', I),
    (r'(?<![0-9a-z])(?=[0-9a-f]*[a-f])(?=[0-9a-f]*\d)[0-9a-f]{32,}(?![0-9a-z])', 'hash in an id', I),
    (r'(?<![0-9a-z])[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}(?![0-9a-z])', 'identifier (UUID) in an id', I)]
ID_WARN = [(r'(?<![a-z0-9])[tnbrpcg]\d{1,2}(?![a-z0-9])', 'identifier-like token in an id', I),
           (r'(?<![a-z0-9])(wave|phase|round|cycle)-?\d+', 'possible process stage label in an id', I),
           (r'(?<![a-z0-9])drafts?(?![a-z0-9])', 'possible process vocabulary in an id (draft)', I)]

# Possible workflow residue in reader text: reported for the content owner, not blocking.
WARN = [
    (r'\badopted\b', 'possible workflow vocabulary (adopted)', I),
    (r'\bspines?\b', 'possible workflow vocabulary (spine)', I),
    (r'\bdrafts?\b', 'possible process vocabulary (draft)', I),
    (r'\b(saved|stored|recorded)\s+(?:[\w-]+\s+){0,3}(certificates?|computations?|arithmetic|matrix|matrices)\b|\breplayed\b',
     'reference to a stored artefact the reader cannot inspect', I),
    (r'(?<![\w\\])[A-Za-z]_(?:\{[^}]*\}|[A-Za-z0-9])', 'possible formula outside TeX delimiters', 0),
    (r'\b(receipts?|frozen|snapshots?|manifests?|provenance)\b', 'possible process vocabulary', I),
]
STAGE_WARN = (r'(?<!\w)(wave|phase|round|cycle)[-\u2013\u2014 ]?\d+\b', 'possible process stage label', 0)
WARN.append(STAGE_WARN)

# Private repository paths may appear nowhere (the open-source whitelist rule). The prefixes are kept as sha256
# digests so that this source does not name them: the first segment of a path ('name/') and its first two
# segments ('name/sub') are hashed and compared.
PRIVATE_PATHS = frozenset('''
074314280fb69d4497fe05bdf5c1afa592529badaa2aa45d3977491a98d6b650 0f0c109367312909f0a73e7be978a5adce2ec5a7feb78a430c930b45c84b92b5
0feb8fe5e14658c352f1e5051f3032556acdb3caed068d90f3d17a1e4ba1ebf0 21c5c81f865cef50ad8c8bc7b7bffeb10a8b7a995fb59bdc3273bfed5a62c1fe
3294dd3ffcd4ac1baf8bc580a4c3901a44331a40308cae543dbb64b55cafc799 4b8f6a7b734a5bc07d44f1b48c47ce927d2fcf6a26e98f4148049ea6f2d11362
52f81478627543702e4286c60b1b6e19c5734e08754f7444477885aaf9088c90 5c35afb373ac73845c89cc4beebf0b88e58976c619171aca897481e3415ad10d
71b3bd90e717a4b99372e5821b34fc5d0405305e257db9148bf4423d70c7d62c 7987fbbfa66ef82f5457cad8a619067e30fa1ce05183f1a627f1229e1a1fab9b
86a7eae394fe6f1c3510ba16f0ad09442a9f560017e144b90c210ca24e5da5cb 884fcd3f10aa57b0758368bcbbb20dc8e925faae72298ddfef08b9362e603055
8a3ce3236497dd4956ca4a0dcaec9ce51d399f94602fccf8b215c813ca052c19 8f9d884f9509a3377727d3be2318e83135aa7fcec179aa860ab80efe9cdf9594
931982e266f477223eef88b5f734b477fdebdfa3aa0e59c5b989877aab318467 9612ab93cc1f852101f179a016789b34d1cd66424d7fde133cabd9bbca977fb1
a8f1e005d3fa85084e9f3883f52c4f2feeed59bc396ca8d4bb278cd50f13805d ba6c4f2fb2cfebaab4041155a9846c544ceb25ab90d0615b2020d22c9c51dc5c
bb88c90eb892f0607b857314e0a59853ce9ea9b2b1f80734a7cdae07f16a8074 cf370513aefd771df5d778af934dab6de4e12d24a4701ad64138fa984083238c
d181bea4e3b8cb401130960de3ec1f436f4c791bc1a49843357a36f135de83fd d7d2d55bd6664726c7523a4c9209ff614e2e69f8cb29c2ad195ced1590886bed
ea694b45b054ae5ee726d0bfc5d64403a1bb0cabc9b4b665b9decb14f078dc4a f7bc9cf6b0188bbe91b3fa17e6d6b18c3afb84e9d3e2a11fe5baee75764b0710
'''.split())
PATH_TOKEN = re.compile(r'(?<![\w.-])([A-Za-z][\w.-]*)/([\w.-]*)')

# Attributes: reader text is held to the prose rules; technical values are skipped; every other value (data-*,
# unknown attributes) is held to the rules for code.
READER = {'aria-label', 'title', 'alt', 'placeholder', 'aria-description', 'aria-roledescription', 'aria-placeholder',
          'aria-valuetext', 'aria-braillelabel', 'aria-brailleroledescription', 'label', 'summary', 'abbr'}
LINKS = {'href', 'src', 'srcset', 'action', 'poster', 'data', 'xlink:href', 'cite', 'formaction'}
TECHNICAL = set('''class id style type role lang dir name content charset http-equiv rel media integrity crossorigin
    nonce sizes loading decoding datetime tabindex hidden open colspan rowspan scope headers for form autocomplete
    autocapitalize autocorrect spellcheck inputmode enterkeyhint encoding display mathvariant viewbox d points width
    height x y x1 x2 y1 y2 cx cy r rx ry transform opacity focusable stretchy fence separator lspace rspace minsize
    maxsize movablelimits accent accentunder scriptlevel displaystyle columnalign rowalign columnspacing rowspacing
    columnlines rowlines frame framespacing equalrows equalcolumns linethickness depth voffset notation mathsize
    mathcolor mathbackground largeop symmetric stroke fill start reversed disabled readonly required checked selected
    multiple maxlength minlength min max step size span translate draggable inert popover async defer nomodule
    referrerpolicy preserveaspectratio offset'''.split())
TECHNICAL_PREFIXES = ('aria-', 'stroke-', 'fill-', 'xmlns', 'stop-', 'font-', 'text-', 'clip', 'marker', 'mask')
TECHNICAL_META = {'viewport', 'referrer', 'robots', 'color-scheme', 'theme-color', 'format-detection',
                  'supported-color-schemes'}
JS_TYPES = {'', 'text/javascript', 'application/javascript', 'application/x-javascript', 'module', 'text/ecmascript',
            'application/ecmascript'}
SCRIPT = re.compile(r'<script\b([^>]*)>(.*?)</script\s*>', re.S | re.I)
TYPE_ATTR = re.compile(r'''\btype\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))''', re.I)
CSS_CONTENT = re.compile(r'''\bcontent\s*:\s*(?:"((?:[^"\\]|\\.)*)"|'((?:[^'\\]|\\.)*)')''', re.S)
# Temml joins a \mathrm{…} (or \rm) run of letters and digits into one name and keeps one digit after a letter
# (\mathrm{T15} shows T1): a letter followed by two or more digits there fails, with the fix named.
FONT_GROUP = re.compile(r'\\mathrm\s*\{\s*([A-Za-z][A-Za-z0-9 ]*?)\s*\}|\\rm(?![A-Za-z])\s*([A-Za-z][A-Za-z0-9 ]*)')
SVG_DATA = re.compile(r'data:image/svg\+xml((?:;[^,;]*)*),', re.I)
MATH = re.compile(r'<math\b.*?</math>', re.S)
TEX_ANNOTATION = re.compile(r'<annotation encoding="application/x-tex">(.*?)</annotation>', re.S)
TOKEN = re.compile(r'<(mi|mn|mo|mtext|ms)\b[^>]*>([^<]*)</\1>')
LETTER_RUN = re.compile(r'(?:<mi\b[^>]*>[^<]</mi>\s*){3,}')
JS_KEYWORDS_BEFORE_REGEX = {'return', 'typeof', 'case', 'do', 'else', 'in', 'of', 'new', 'delete', 'void', 'throw',
                            'instanceof', 'yield', 'await'}

def norm(text):
    """Text as scanned: format characters (soft hyphen, zero-width spaces and joiners) removed and every run of
    white space, no-break spaces included, one plain space."""
    text = ''.join(ch for ch in text if ch < '\x80' or unicodedata.category(ch) != 'Cf')
    return re.sub(r'\s+', ' ', text)


def fold(text):
    """Compatibility forms (mathematical italic or bold letters, ligatures) as plain letters, for the word rules."""
    return unicodedata.normalize('NFKC', text)


def visible_text(markup, spaced=False):
    """The reader-visible body text with formulas removed. With spaced=True every tag boundary becomes a
    space, so that words in adjacent elements (a status chip and a title) do not fuse."""
    body = markup[markup.find('<body'):]
    body = re.sub(r'<script\b.*?</script>', ' ', body, flags=re.S)
    body = re.sub(r'<style\b.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<math\b.*?</math>', ' ', body, flags=re.S)
    body = re.sub(r'<svg\b.*?</svg>', ' ', body, flags=re.S)
    if spaced:
        return norm(html.unescape(re.sub(r'<[^>]+>', ' ', body)))
    return norm(strip_tags(body))


def scan(text, patterns, label=''):
    found = []
    for pattern, why, flags in patterns:
        for m in re.finditer(pattern, text, flags=flags):
            ctx = text[max(0, m.start() - 50): m.end() + 50]
            found.append(f'{why}{label}: "{m.group(0)}" in …{ctx}…')
    return found


def private_paths(text, label=''):
    found = []
    for m in PATH_TOKEN.finditer(text):
        first = m.group(1).lower()
        for prefix in (first + '/', f'{first}/{m.group(2).lower()}'):
            if hashlib.sha256(prefix.encode()).hexdigest() in PRIVATE_PATHS:
                found.append(f'private repository path{label}: "{m.group(0)}" in …{text[max(0, m.start() - 50): m.end() + 50]}…')
                break
    return found


def held(text, rules, label=''):
    """The rules on text: word rules on its folded form, the rest as written, and private paths."""
    words = [r for r in rules if r in WORDS or r is RECORD_WORDS]
    rest = [r for r in rules if r not in words]
    return scan(fold(text), words, label) + scan(text, rest, label) + private_paths(text, label)


def _read_string(src, i):
    """src[i] opens a quoted string; returns the index after it and its text."""
    q, j = src[i], i + 1
    while j < len(src) and src[j] != q:
        j += 2 if src[j] == '\\' else 1
    return j + 1, src[i + 1:j]


def _read_template(src, i):
    """src[i] opens a template literal; returns the index after it, its text without interpolations, and the code of
    each ${...} interpolation (nested strings and templates kept whole)."""
    j, n, text, codes = i + 1, len(src), [], []
    while j < n and src[j] != '`':
        if src[j] == '\\':
            text.append(src[j:j + 2])
            j += 2
            continue
        if src.startswith('${', j):
            k, depth = j + 2, 1
            while k < n and depth:
                if src[k] in '"\'':
                    k = _read_string(src, k)[0]
                    continue
                if src[k] == '`':
                    k = _read_template(src, k)[0]
                    continue
                depth += {'{': 1, '}': -1}.get(src[k], 0)
                k += 1
            codes.append(src[j + 2:k - 1])
            text.append(' ')
            j = k
            continue
        text.append(src[j])
        j += 1
    return j + 1, ''.join(text), codes


def prose_like(text):
    """A string a reader may see (it has a space or a capital first letter), as against a one-token code string."""
    return bool(re.search(r'\s', text.strip()) or re.match(r'\s*[A-Z]', text))


def svg_images(text, css=False, srcset=False):
    """The text of every SVG image given as a data: URI in an attribute value or a style sheet, base64 or
    percent-encoded, whatever its parameters (srcset candidates, CSS url() and image-set() included); None for an
    image that cannot be read."""
    found = []
    for m in SVG_DATA.finditer(text):
        start = m.end()
        quote = text[m.start() - 1] if m.start() and text[m.start() - 1] in '"\'' else ''
        if quote:
            end = text.find(quote, start)
        elif srcset or css:
            end = start + re.search(r'[\s)]|$', text[start:]).start()
        else:
            end = len(text)
        payload = text[start:len(text) if end < 0 else end].rstrip(',')
        try:
            payload = urllib.parse.unquote(payload)
            if any(p.strip().lower() == 'base64' for p in m.group(1).split(';')):
                payload = re.sub(r'\s+', '', payload)
                payload = base64.b64decode(payload + '=' * (-len(payload) % 4)).decode('utf-8', 'replace')
            found.append(' '.join(re.sub(r'<[^>]+>', ' ', payload).split()))
        except (ValueError, binascii.Error):
            found.append(None)
    return found


def held_images(images, label):
    """The rules on the text of SVG images; an image that cannot be read fails."""
    out = []
    for text in images:
        out += [f'an SVG image that cannot be read{label}'] if text is None else held(norm(text), FORBIDDEN, label)
    return out


def js_parts(src):
    """String literals and comments of a script: a small scanner for strings, template text, comments and
    regular-expression literals (told from division by the previous significant character or keyword)."""
    strings, comments = [], []
    i, n, prev = 0, len(src), ''
    while i < n:
        c = src[i]
        if c in '"\'':
            i, text = _read_string(src, i)
            strings.append(text)
            prev = c
            continue
        if c == '`':
            i, text, codes = _read_template(src, i)
            strings.append(text)
            for code in codes:
                more, notes = js_parts(code)
                strings += more
                comments += notes
            prev = c
            continue
        if c == '/' and src.startswith('//', i):
            j = src.find('\n', i)
            j = n if j < 0 else j
            comments.append(src[i + 2:j])
            i = j
            continue
        if c == '/' and src.startswith('/*', i):
            j = src.find('*/', i + 2)
            j = n if j < 0 else j
            comments.append(src[i + 2:j])
            i = j + 2
            continue
        if c == '/':
            word = re.search(r'([A-Za-z_$][\w$]*)\s*$', src[max(0, i - 20):i])
            if prev == '' or prev in '(,=:[!&|?{};+-*%<>~^' or (word and word.group(1) in JS_KEYWORDS_BEFORE_REGEX):
                j, in_class = i + 1, False
                while j < n and src[j] != '\n':
                    if src[j] == '\\':
                        j += 2
                        continue
                    if src[j] == '[':
                        in_class = True
                    elif src[j] == ']':
                        in_class = False
                    elif src[j] == '/' and not in_class:
                        break
                    j += 1
                i, prev = j + 1, '/'
                continue
        if not c.isspace():
            prev = c
        i += 1
    return strings, comments


class _Attributes(HTMLParser):
    """Every attribute of every element, whichever quoting it uses, and the page's metadata."""

    def __init__(self, author='', home='', site=''):
        super().__init__(convert_charrefs=True)
        self.author, self.home = author, home
        self.print_overview = site.rstrip('/') + '#programme-overview'
        self.attributes, self.metas, self.ids = [], [], []
        self.outside_references = []
        self.author_anchor = None
        self.environments = {}
        self.block_titles = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        primary_page = (tag == 'a' and values.get('class') == 'mg-primary-page'
                        and is_primary_page(values.get('href') or ''))
        if 'data-env' in values:
            self.environments[values.get('id')] = values
        if 'data-block-title' in values and 'id' in values:
            self.block_titles.add(values['id'])
        if tag == 'a':
            self.author_anchor = None
        for name, value in attrs:
            if value:
                name = name.lower()
                scholarly_href = primary_page and name == 'href' and value == values['href']
                self.attributes.append((tag, name, value, scholarly_href))
                if name == 'id':
                    self.ids.append(value)
                if name in {'src', 'href', 'action', 'srcset', 'poster', 'data'} and re.match(r'^(https?:)?//', value, re.I):
                    if tag == 'link' and name == 'href' and 'canonical' in (values.get('rel') or '').lower().split():
                        continue
                    if (tag == 'a' and name == 'href' and values.get('class') == 'mg-print-overview'
                            and value == self.print_overview):
                        continue
                    if scholarly_href:
                        continue
                    if tag == 'a' and name == 'href' and value == self.home:
                        self.author_anchor = (len(self.outside_references), [])
                    self.outside_references.append(value)
        if tag == 'meta':
            self.metas.append({k.lower(): (v or '') for k, v in attrs})

    def handle_data(self, data):
        if self.author_anchor is not None:
            self.author_anchor[1].append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.author_anchor is not None:
            index, label = self.author_anchor
            if ''.join(label).strip() == self.author:
                self.outside_references[index] = None
            self.author_anchor = None


def link_attribute_errors(value, name, scholarly_href):
    label = f' (in {name})'
    if not scholarly_href:
        return held(value, [FILE, PATH, HASH, UUID, REPO], label)
    # Some publishers identify a PDF by a hexadecimal filename. The filename is a
    # public resource locator. The host, preceding path, query and visible label
    # still undergo their ordinary checks.
    url = urllib.parse.urlsplit(value)
    directory, _, filename = url.path.rpartition('/')
    hash_input = value
    if re.fullmatch(r'[0-9a-fA-F]{32,}(?:\.pdf)?', filename):
        hash_input = url._replace(path=directory + '/paper').geturl()
    return held(value, [FILE, PATH, UUID, REPO], label) + scan(hash_input, [HASH], label)


def environment_errors(parser, declarations):
    errors = []
    for ident, form in declarations.items():
        group = parser.environments.get(ident, {})
        if (group.get('data-env'), group.get('data-status')) != form:
            errors.append(f'#{ident}: the rendered form or status differs from the declaration')
        if (group.get('role') != 'group' or group.get('aria-labelledby') != ident + '-h' or
                ident + '-h' not in parser.block_titles):
            errors.append(f'#{ident}: the mathematical environment has no associated title')
        if ('data-term' in group) != (form.kind == 'definition') or ('data-result' in group) != form.is_result:
            errors.append(f'#{ident}: the term or result classification differs from the declaration')
        if group.get('data-kind') != form.kind:
            errors.append(f'#{ident}: the native kind differs from the authored statement form')
        if form.is_result and group.get('data-result-family') != form.style:
            errors.append(f'#{ident}: the result has a different status style')
    return errors


def run(build, markup):
    failures = list(build.problems)
    warnings = list(build.warnings)
    c = build.content

    # Structure.
    rows = c.get('rows', [])
    if len(rows) != 20:
        warnings.append(f'the grid has {len(rows)} rows (the examples grid has 20)')
    for r in rows:
        for cid in COLUMNS:
            if cid not in (r.get('cells') or {}):
                failures.append(f'row {r.get("id")}: no cell for {cid}')
    for s in build.all_statements(c):
        if s.get('status') not in STATEMENT_STATUSES:
            failures.append(f'unknown status {s.get("status")!r}')
    # The status contract: a scoped negative result ('refuted form') must state its scope as hypotheses (root's
    # ruling: explicit scope is mandatory). A status in use without a key entry fails in the producer.
    for s in build.all_statements(c):
        if s.get('status') == 'refuted form' and not s.get('hypotheses'):
            failures.append(f'the statement {s.get("id") or strip_tags(s.get("title") or "")[:60]!r} has the status '
                            f'\'refuted form\' but states no hypotheses: a scoped negative result must give its scope')

    # The personal home is a navigation destination on the named author link.
    bare = re.sub(r'<script\b.*?</script>', ' ', markup, flags=re.S)
    parser = _Attributes(build.page['author'], build.page['home'], build.page['site'])
    parser.feed(re.sub(r'<(script|style)\b.*?</\1>', ' ', markup, flags=re.S))
    parser.close()
    if build.book:
        failures.extend(environment_errors(parser, build.book.environment_forms))
    for url in parser.outside_references:
        if url is not None:
            failures.append(f'outside reference: {url[:100]}')
    for m in re.finditer(r'url\(\s*([^)]*)\)', markup):
        url = m.group(1).strip('\'" ')
        if not url.startswith('data:') and not url.startswith('#'):
            failures.append(f'outside url(): {url[:100]}')
    if re.search(r'<link[^>]+rel="(stylesheet|preconnect|dns-prefetch|preload)"', markup):
        failures.append('a <link> that loads or prefetches another resource')
    if re.search(r'\b(fetch|XMLHttpRequest|sendBeacon|WebSocket|EventSource)\s*\(', markup):
        failures.append('a network call in the page script')

    # In-page links.
    ids = set(re.findall(r'\sid="([^"]+)"', markup))
    for m in re.finditer(r'href="#([^"]*)"', bare):
        if m.group(1) and m.group(1) not in ids:
            failures.append(f'broken in-page link #{m.group(1)}')
    for m in re.finditer(r'(?:data-term|aria-controls|aria-describedby|data-row)="([^"]+)"', markup):
        if m.group(1) not in ids:
            failures.append(f'reference to missing id {m.group(1)}')
    id_counts = Counter(re.findall(r'\sid="([^"]+)"', markup))
    for i in sorted(k for k, n in id_counts.items() if n > 1):
        failures.append(f'duplicate id {i}')

    # The golden rule, on everything a reader sees, hears or shares: the text as written and with tag boundaries
    # spaced, the words of formulas, every attribute that is not technical, image text, data blocks, script
    # strings, generated content, comments, metadata and ids.
    flagged, cautions = [], []
    for text in (visible_text(markup), visible_text(markup, spaced=True)):
        flagged += held(text, FORBIDDEN + [RAW_TEX])
    cautions += scan(visible_text(markup, spaced=True), WARN)

    mtext = norm(' '.join(strip_tags(m) for m in re.findall(r'<mtext\b[^>]*>(.*?)</mtext>', markup, flags=re.S)))
    flagged += held(mtext, SHAPELESS, ' (in a formula)')
    cautions += scan(mtext, IDENTIFIERS + [PERCENT] + WARN, ' (in a formula)')
    names, runs, spoken = [], [], []
    for m in MATH.finditer(markup):
        whole = m.group(0)
        tex = TEX_ANNOTATION.search(whole)
        body = whole[:tex.start()] + whole[tex.end():] if tex else whole
        tokens = [(kind, fold(html.unescape(text))) for kind, text in TOKEN.findall(body)]
        names += [text for kind, text in tokens if kind == 'mi' and len(text.strip()) >= 3]  # \operatorname, \mathrm
        runs += [fold(''.join(re.findall(r'>([^<])</mi>', run))) for run in LETTER_RUN.findall(body)]
        spoken.append(' '.join(text.strip() for kind, text in tokens if kind != 'mtext' and text.strip()))
        if tex:
            source = html.unescape(tex.group(1))
            for g in FONT_GROUP.finditer(source):
                group = (g.group(1) or g.group(2)).replace(' ', '')
                if re.search(r'[A-Za-z]\d{2,}', group):
                    failures.append(f'formula "{source[:100]}": {g.group(0).strip()} would lose digits (the renderer keeps '
                                    f'one digit after a letter in such a group); set the digits outside it, as in '
                                    f'\\mathrm{{M}}_{{24}}')
    flagged += scan(' '.join(names), WORDS, ' (in a formula)')
    spoken_text = norm(' | '.join(spoken))
    flagged += scan(spoken_text, [STAGE, STAGE_WORK], ' (in a formula)')
    cautions += scan(spoken_text, [STAGE_WARN], ' (in a formula)')
    cautions += scan(' '.join(runs), WORDS, ' (letters set one by one in a formula)')
    tex = norm(html.unescape(' '.join(TEX_ANNOTATION.findall(markup))))
    flagged += scan(tex, TEX_FORBIDDEN, ' (in TeX source)') + private_paths(tex, ' (in TeX source)')
    cautions += scan(tex, TEX_WARN, ' (in TeX source)')

    images = norm(html.unescape(' '.join(re.sub(r'<[^>]+>', ' ', s) for s in re.findall(r'<svg\b.*?</svg>', markup, flags=re.S))))
    flagged += held(images, FORBIDDEN, ' (in an image)')

    comments = []
    for attrs, body in SCRIPT.findall(markup):
        kind = TYPE_ATTR.search(attrs)
        kind = next((g for g in kind.groups() if g is not None), '').strip().lower() if kind else ''
        if kind in JS_TYPES:
            strings, notes = js_parts(body)
            prose = [t for t in strings if prose_like(t)]
            tokens = [t for t in strings if not prose_like(t)]
            flagged += held(norm(' | '.join(prose)), CODE, ' (in a script string)')
            flagged += held(norm(' | '.join(tokens)), CODE_TOKENS, ' (in a script string)')
            comments += notes
        else:
            flagged += held(norm(body), FORBIDDEN, ' (in a data block)')
    for sheet in re.findall(r'<style\b[^>]*>(.*?)</style>', markup, flags=re.S):
        comments += re.findall(r'/\*(.*?)\*/', sheet, flags=re.S)
        sheet = re.sub(r'/\*.*?\*/', ' ', sheet, flags=re.S)
        flagged += held_images(svg_images(sheet, css=True), ' (in an image in the styles)')
        sheet = re.sub(r'url\(\s*("[^"]*"|\'[^\']*\'|[^)]*)\)', ' ', sheet)
        sheet = re.sub(r'(["\'])data:[^"\']*\1', ' ', sheet)
        generated = [a or b for a, b in CSS_CONTENT.findall(sheet)]
        flagged += held(norm(' | '.join(generated)), FORBIDDEN, ' (in generated content)')
        strings = [a or b for a, b in re.findall(r'"((?:[^"\\]|\\.)*)"|\'((?:[^\'\\]|\\.)*)\'', sheet)]
        flagged += held(norm(' | '.join(t for t in strings if prose_like(t))), SHAPELESS, ' (in a style string)')
        flagged += held(norm(' | '.join(t for t in strings if not prose_like(t))), SHAPELESS_TOKENS, ' (in a style string)')
    comments += re.findall(r'<!--(.*?)-->', markup, flags=re.S)
    flagged += held(norm(' | '.join(comments)), COMMENT, ' (in a comment)')

    for tag, name, value, scholarly_href in parser.attributes:
        if re.search(r'data:image/svg', value, re.I):  # in any attribute, style and srcset included
            flagged += held_images(svg_images(value, css=name == 'style', srcset=name in ('srcset', 'imagesrcset')),
                                   f' (in an image in {name})')
        if name == 'id' or name in TECHNICAL or (name.startswith(TECHNICAL_PREFIXES) and name not in READER):
            continue
        value = norm(value)
        if name in READER:
            flagged += held(value, SHAPELESS, f' (in {name})')
            cautions += scan(value, IDENTIFIERS, f' (in {name})')
            if TEX_IN_ATTRIBUTE.search(value):
                flagged.append(f'TeX source in {name}: "{value[:120]}"')
        elif name in LINKS:
            if not value.lower().startswith('data:'):
                flagged += link_attribute_errors(value, name, scholarly_href)
        else:
            flagged += held(value, CODE if prose_like(value) else CODE_TOKENS, f' (in {name})')
    for meta in parser.metas:
        key = meta.get('name') or meta.get('property') or meta.get('itemprop') or ''
        if 'http-equiv' in meta or 'charset' in meta or key.lower() in TECHNICAL_META:
            continue
        flagged += held(norm(meta.get('content', '')), FORBIDDEN, f' (in meta {key})')
    title = re.search(r'<title>(.*?)</title>', markup, flags=re.S)
    if title:
        flagged += held(norm(html.unescape(title.group(1))), FORBIDDEN, ' (in title)')
    for i in dict.fromkeys(list(id_counts) + parser.ids):
        flagged += scan(i, ID_FORBIDDEN, ' (in id)')
        cautions += scan(i, ID_WARN, ' (in id)')
    failures.extend(dict.fromkeys(flagged))
    warnings.extend(dict.fromkeys(cautions))
    anchorless = [strip_tags(s.get('title') or '') or (s.get('text') or '')[:80]
                  for s in build.all_statements(c) if not (s.get('id') or '').strip()]
    if anchorless:
        warnings.append(f'{len(anchorless)} statements have no id, so no link reaches the statement itself '
                        f'(listed in audit.json under statements_without_id); first: {anchorless[0][:80]}')

    # Metadata carries no tool credit either.
    head = re.sub(r'<(style|script)\b.*?</\1>', ' ', markup[:markup.find('</head>')], flags=re.S)
    if re.search(r'generator|astra|claude|codex|gpt', head, re.I):
        failures.append('tool or model named in the page head')

    tally = {}
    for s in build.all_statements(c):
        tally[s.get('status')] = tally.get(s.get('status'), 0) + 1
    cells = {}
    for r in rows:
        for cell in (r.get('cells') or {}).values():
            cells[cell.get('status')] = cells.get(cell.get('status'), 0) + 1
    jobs = len(build.math.jobs)
    return {
        'failures': failures,
        'warnings': warnings,
        'bytes': len(markup.encode('utf-8')),
        'statements': tally,
        'environments': dict(Counter(a['data-env'] for a in parser.environments.values())),
        'cells': cells,
        'terms': len(build.term_links.entries),
        'terms_attached': len(build.term_links.used),
        'terms_unused': sorted(e['term'] for e in build.term_links.entries if e['id'] not in build.term_links.used),
        'math': jobs - len(getattr(build.math, 'text_jobs', {})),
        'math_jobs': jobs,
        'math_errors': len(build.math.errors),
        'fonts': getattr(build, 'font_report', {}),
        'statements_without_id': anchorless,
    }


def text_report(result):
    lines = [f'bytes: {result["bytes"]:,}', f'statements: {result["statements"]}', f'cells: {result["cells"]}',
             f'terms: {result["terms"]} (attached in text: {result["terms_attached"]})',
             f'math: {result["math"]} formulas ({result.get("math_jobs", result["math"])} rendering jobs; '
             f'errors: {result["math_errors"]})', f'fonts: {result["fonts"]}']
    if result['terms_unused']:
        lines.append('terms never attached in the text: ' + ', '.join(result['terms_unused']))
    kinds = Counter(w.split(':')[0] for w in result['warnings'])
    if kinds:
        lines.append('warnings by kind: ' + '; '.join(f'{k}: {n}' for k, n in kinds.most_common()))
    for w in result['warnings']:
        lines.append('WARNING ' + w)
    for f in result['failures']:
        lines.append('FAIL ' + f)
    lines.append('PASS' if not result['failures'] else f'{len(result["failures"])} failure(s)')
    return '\n'.join(lines) + '\n'
