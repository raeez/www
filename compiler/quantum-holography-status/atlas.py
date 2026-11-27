"""The research atlas of the status page: domains, claims, typed relations, comparisons and reading paths.

The page's builder calls render(data, ctx) with the contents of atlas.json (schema
programme-scientific-atlas-public/v1, a reader-safe projection supplied with the content) and an
AtlasContext. It returns {'html', 'title', 'kicker', 'nav_label', 'css', 'js', 'problems'}: the body of
the atlas section, its heading words, its stylesheet and script, and a list of problems, each a build
failure. With a problem the body is empty, so no part of an invalid atlas reaches the page.

The renderer uses only the context: ctx.rich(text, terms) for TeX, emphasis and glossary terms,
ctx.anchor_for(statement id) for links to statements on the page, ctx.anchors for the ids already on
the page and ctx.labels for interface words set in page.json. It reads the page's reader-visible rules
(audit.FORBIDDEN) to check every string and id before rendering.

The page shows only what atlas.json records. A line joins two claims only where an edge records a
relation between them; nothing is inferred from a shared domain, comparison or reading path. No count
of claims is shown as a measure of progress, and no status is shown other than the supplied code and
its supplied label. The markup is complete without the script: it prints and reads without JavaScript.
"""
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA = 'programme-scientific-atlas-public/v1'
CODES = ['checked', 'conditional', 'scoped_negative', 'remaining']
CLAIM_FORMS = {'lemma': 'Lemma', 'proposition': 'Proposition', 'theorem': 'Theorem',
               'corollary': 'Corollary', 'counterexample': 'Counterexample',
               'conjecture': 'Conjecture', 'open-question': 'Open question'}
# The page's status for each atlas status (the content owner's status-language ruling): the visible word is chosen by
# the stored code and is the same on the page (Established, Conditional, Remaining, Scoped negative), and the colours
# are the page's semantic colours of these legacy codes. Per-record status labels are display aliases, never shown.
PAGE_STATUS = {'checked': 'checked', 'conditional': 'conditional', 'remaining': 'open', 'scoped_negative': 'refuted form'}
BUCKETS = [('establishedClaimIds', 'checked'), ('conditionalClaimIds', 'conditional'),
           ('scopedNegativeClaimIds', 'scoped_negative'), ('remainingClaimIds', 'remaining')]
PATH_KINDS = ['editorial_orientation', 'source_bound_dependency_path']
MATH_RE = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]', re.S)  # the page's TeX delimiters
ID_RE = re.compile(r'^[a-z0-9]+(?:[_-][a-z0-9]+)*$')
RELATION_RE = re.compile(r'^[A-Za-z](?:[A-Za-z0-9_ -]*[A-Za-z0-9])?$')  # words, joined by _, - or spaces
HASH_RE = re.compile(r'(?<![0-9a-f])(?=[0-9a-f]*[a-f])(?=[0-9a-f]*[0-9])[0-9a-f]{7,}(?![0-9a-f])', re.I)
HOST_RE = re.compile(r'https?://|\bwww\.', re.I)
PERCENT_RE = re.compile(r'\d\s*%|\bper\s?cent', re.I)
LABEL_RE = re.compile(r'\b(?:thm|prop|lem|lemma|def|defn|cor|sec|eq|rem|conj|ex|fig|tab|chap|app|hyp|claim|item):[\w-]+', re.I)
LINE_STYLES = 8  # the first eight relation types have their own line styles (.rk-0 to .rk-7); later ones share .rk-8
GROUP_SHOWN = 8  # a group of more claims shows its first eight and keeps the rest in a disclosure
INDEX_LONG = 40  # above this many claims the index scrolls in its own box on screen (atlas.css)
MAP_ROWS = 28  # the map is at most this many rows of marks tall (about one screen); wider maps scroll across
# Classes of the elements whose text is the content owner's (titles, statements, hypotheses, labels, summaries),
# as distinct from the atlas's own interface words. The gate scans and the tests read this one list.
SUPPLIED_CLASSES = (
    'atlas-link-title', 'atlas-claim-title', 'atlas-statement', 'atlas-hyps', 'atlas-item-hyps', 'atlas-domain-summary',
    'atlas-overview', 'atlas-path-summary', 'atlas-path-note', 'atlas-stage-desc', 'atlas-stage-label', 'atlas-rel-label',
    'atlas-rel-scope', 'atlas-note-text', 'atlas-claim-domain', 'atlas-track',
    'atlas-domain-h', 'atlas-comparison-h', 'atlas-path-h', 'atlas-conventions', 'atlas-claim-group-h',
    'atlas-row-domain', 'atlas-col-domain', 'atlas-domain-comps', 'atlas-rel-names', 'atlas-rel-name')
# Glossary buttons inside the atlas text (never inside a link): the page's glossary card opens from them. The
# foundation mount does not reserve the classes that ctx.rich itself emits (term, math-*), and the interaction
# script shares the card of a .term[data-term] with the atlas. With an older foundation that reserved .term, set
# False: the build then names the class instead of failing silently.
TERMS = True
# The page renderer's two formula boxes, renamed into the atlas namespace (exact forms of ctx.rich's output).
FORMULA_CLASSES = (('class="math-display"', 'class="atlas-math-display"'),
                   ('class="math-inline math-long"', 'class="math-inline atlas-math-long"'))

# Required and optional keys of each object. Any other key is an error, so that a private field
# cannot reach the page by accident.
SHAPE = {
    'atlas': ({'schema', 'domains', 'claims', 'edges', 'comparisons', 'readingPaths'}, {'asOf'}),
    'domain': ({'id', 'label', 'summary'}, {'conventions', 'relatedQuestionIds'}),
    'claim': ({'id', 'domainId', 'title', 'statement', 'status', 'hypotheses'},
              {'sourceLabel', 'comparisonIds', 'statementRef', 'sectionRef', 'form'}),
    'status': ({'code', 'label'}, set()),
    'edge': ({'id', 'source', 'target', 'relation', 'label', 'scope'}, set()),
    'comparison': ({'id', 'domainId', 'title', 'overview'} | {k for k, _ in BUCKETS}, {'questionId', 'relatedQuestionIds'}),
    'path': ({'id', 'title', 'kind', 'summary', 'stages'}, {'note'}),
    'stage': ({'label', 'description', 'claimIds'}, set()),
}

# Status marks: the page's own. The atlas draws each status with the page's mark for its page status
# (PAGE_STATUS), as the page draws it (ctx.mark), so the page and the atlas have one mark system and the key needs
# no sentence to translate between two. The word beside a mark is chosen by the stored code, as before.

# Interface words (design). page.json may replace any of them: a label 'atlas_<key>' replaces <key>,
# and the page's own 'atlas', 'atlas_kicker' and 'nav_atlas' replace the heading, kicker and nav label.
LABELS = {
    'nav': 'Atlas',
    'kicker': 'Atlas',
    'heading': 'The programme as a map',
    'intro': 'Select a claim to read its statement, hypotheses and named relations.',
    'parts': 'Parts of the atlas',
    'key': 'How to read the atlas',
    'key_status': 'Statuses',
    'key_relations': 'Relations',
    'key_relations_none': 'No relation between claims is recorded.',
    'key_plain': 'Relations past the eighth type share the plain line; each is named in the lists of its claims.',
    'more': 'Show the rest of this group',
    'key_separate': 'The four statuses are those of the whole page.',
    'part_map': 'Map',
    'part_domains': 'Domains',
    'part_claims': 'Claims',
    'part_comparisons': 'Comparisons in the atlas',
    'part_paths': 'Reading paths',
    'part_full': 'The claims in full',
    'lead_map': 'Every claim of the atlas by domain, and every relation recorded between claims.',
    'lead_domains': 'What each domain holds, under the four statuses.',
    'lead_claims': 'The index of claims. Select a claim to read it in full with its relations.',
    'lead_comparisons': 'For each comparison: what is established, what is conditional, what is negative and what remains.',
    'lead_paths': 'Orders in which to read the claims. Each path says whether its stages are joined by recorded relations.',
    'group_checked': 'Established',
    'group_conditional': 'Conditional',
    'group_scoped_negative': 'Scoped negative',
    'group_remaining': 'Remaining',
    'gloss_checked': 'A checked conclusion, within its stated scope.',
    'gloss_conditional': 'An implication that holds under the hypotheses listed with it, at least one of which is not established.',
    'gloss_scoped_negative': 'A negative result, established within its stated scope.',
    'gloss_remaining': 'Not settled: a comparison that remains to be made.',
    'key_plain_all': ('Each line is a recorded relation, drawn in one style; the lists of each claim name the relation '
                      'and give its scope.'),
    'conventions': 'Conventions',
    'conventions_link': 'Conventions of this domain',
    'rel_list': 'The relations recorded in the atlas',
    'question_own': 'Question',
    'questions_related': 'Related questions',
    'question_link': 'Read the question',
    'domain_comparisons': 'Comparisons in this domain:',
    'domain_fold': 'Conventions, claims and comparisons of this domain',
    'domain_fold_plain': 'Claims and comparisons of this domain',
    'same_hyps': 'Same hypotheses as No. {n}.',
    'map': 'Claims and recorded relations, by domain',
    'map_caption': ('Each mark is a claim, numbered as in the index; a long domain runs over several columns. Each line '
                    'is a recorded relation, with its arrow at the second claim of the relation.'),
    'map_scroll': 'Map of claims by domain',
    'locator': 'Place in the atlas',
    'locator_caption': ('Each dot is a claim at its place in the map; each band is a domain. The selected claim is marked '
                        'with its number.'),
    'locator_link': 'Show in the map',
    'map_keys': ('The arrow keys move through the claims of the map, Enter shows the claim, Escape leaves the map. '
                 'The index of claims below lists the same claims with their titles.'),
    'index': 'Index of claims',
    'index_caption': ('Every claim of the atlas, with its domain, its status and the number of relations recorded '
                      'into it and from it.'),
    'col_number': 'No.',
    'number': 'No.',
    'col_claim': 'Claim',
    'col_domain': 'Domain',
    'col_status': 'Status',
    'col_in': 'Into',
    'col_out': 'From',
    'hypotheses': 'Hypotheses',
    'hypotheses_inline': 'Hypotheses:',
    'hypotheses_none': 'None listed.',
    'source': 'Source statement:',
    'in_comparisons': 'In comparisons:',
    'statement_link': 'The statement on this page',
    'rel_in': 'Relations into this claim',
    'rel_out': 'Relations from this claim',
    'rel_none': 'None recorded.',
    'this_claim': 'this claim',
    'this_claim_lead': 'This claim',
    'none_listed': 'None listed.',
    'path_editorial': 'Editorial order',
    'path_editorial_note': 'A suggested order of reading. A stage need not depend on the stage before it.',
    'path_dependency': 'Joined by recorded relations',
    'path_dependency_note': ('Every claim of a stage is joined to a claim of the stage next to it by a recorded relation, '
                             'shown with the stage. Each relation is given in its own direction.'),
    'stage': 'Stage {n}',
    'joined': 'Stage {n} is joined to stage {m} by',
    'join_back': 'runs from stage {n} to stage {m}',
    # Words of the script. They travel as text in an inert template inside the atlas, so that the
    # page's audit reads them and the embedded fonts include their letters.
    'js_filter': 'Filter the claims',
    'js_words': 'Words',
    'js_field_hint': 'Words in a claim: title, statement, hypotheses or source',
    'js_number': 'No.',
    'js_tip_to': '\u2192',
    'js_tip_from': '\u2190',
    'js_tip_more': 'Every relation is listed with the claim.',
    'js_filter_note': 'The filter reads the titles, statements, hypotheses and source statements of the claims in the atlas.',
    'js_domain': 'Domain',
    'js_status': 'Status',
    'js_clear': 'Clear',
    'js_count_all': 'The index lists every claim.',
    'js_count_some': 'The index lists the claims that match.',
    'js_count_none': 'No claim matches.',
    'js_pane': 'Selected claim',
    'js_empty': 'Select a claim in the map, the index, a domain, a comparison or a reading path to see it here.',
    'js_close': 'Close',
    'js_relations': 'Relations of this claim',
    'js_relations_none': 'No relation of this claim is recorded.',
    'js_side_in': 'Into this claim',
    'js_side_out': 'From this claim',
    'js_hood_cap': 'The diagram shows the first twelve claims on each side; the lists below give every relation.',
    'js_show': 'Show relations:',
    'js_hidden': 'Not shown here:',
    'js_follow': 'Follow this path',
    'js_prev': 'Previous',
    'js_next': 'Next',
    'js_leave': 'Leave the path',
    'js_position': 'Stage {n}',
    'js_resume': 'Return to the path',
}


def labels_for(page_labels):
    labels = dict(LABELS)
    page_labels = page_labels or {}
    for k, v in page_labels.items():
        if k.startswith('atlas_') and isinstance(v, str) and k[6:] in LABELS:
            labels[k[6:]] = v
    for page_key, key in (('atlas', 'heading'), ('atlas_kicker', 'kicker'), ('nav_atlas', 'nav')):
        if isinstance(page_labels.get(page_key), str) and page_labels[page_key].strip():
            labels[key] = page_labels[page_key]
    return labels


def stylesheet():
    return (HERE / 'atlas.css').read_text(encoding='utf-8')


def script():
    return (HERE / 'atlas.js').read_text(encoding='utf-8')


def render(data, ctx):
    """The atlas for the page's mount: see the module docstring for the result."""
    labels = labels_for(getattr(ctx, 'labels', None))
    atlas = validate(data, ctx)
    check = Atlas(None)  # the interface words, page.json overrides included, meet the same rules as the data
    for key, value in sorted(labels.items()):
        check.safe(f'label {key}', value)
    problems = atlas.errors + check.errors
    if atlas.structural or check.errors:
        return {'html': '', 'problems': problems}
    renderer = Renderer(ctx, atlas, labels)
    body = renderer.html()
    twice = sorted(i for i, n in renderer.uses.items() if n > 1)
    taken = set(renderer.uses) & set(getattr(ctx, 'anchors', ()))
    if twice or taken:
        return {'html': '', 'problems': [f'atlas id used twice: {i}' for i in twice] +
                [f'atlas id already used on the page: {i}' for i in sorted(taken)]}
    return {'html': body, 'title': labels['heading'], 'kicker': labels['kicker'], 'nav_label': labels['nav'],
            'css': stylesheet(), 'js': script(), 'problems': problems + renderer.problems}


def cls(code):
    return code.replace('_', '-')


# Validation -------------------------------------------------------------------------------------

def validate(data, ctx=None):
    """Check atlas.json. With a context, each statementRef must name a statement anchored on the page."""
    atlas = Atlas(ctx)
    atlas.check(data)
    return atlas


def joined(a, b, edges):
    return [e for e in edges if (e['source'] == a and e['target'] == b) or (e['source'] == b and e['target'] == a)]


class Atlas:
    """The checked contents of atlas.json, with the relations indexed by claim."""

    def __init__(self, ctx):
        self.ctx = ctx
        self.errors = []
        self.structural = []
        self.domains, self.claims, self.edges, self.comparisons, self.paths = [], [], [], [], []
        self.claim = {}
        self.domain = {}
        self.number = {}
        self.into = {}
        self.out = {}
        self.relations = {}      # relation code -> (label, line style, order of first use)
        self.status_labels = {}  # status code -> supplied label
        self.joins = {}          # (path id, stage index) -> [(edge, backward)]

    def err(self, text, reader=False):
        """Every error fails the build. A structural error (shape, type, reference) also stops rendering; a finding
        of the reader rules in a text does not, so that a draft build (--allow-draft) still shows the atlas."""
        self.errors.append(text)
        if not reader:
            self.structural.append(text)

    def keys(self, obj, kind, where):
        if not isinstance(obj, dict):
            self.err(f'{where}: an object is required')
            return False
        required, optional = SHAPE[kind]
        for k in sorted(required - set(obj)):
            self.err(f'{where}: missing key {k!r}')
        for k in sorted(set(obj) - required - optional):
            # A field the atlas does not show fails the build, so that no field of a new payload is dropped
            # silently; the atlas still draws in a draft, from the fields it knows (it reads no other).
            self.err(f'{where}: unknown key {k!r}; the atlas does not show it', reader=True)
        return True

    def text(self, obj, key, where, empty=False):
        value = obj.get(key)
        if not isinstance(value, str):
            if key in obj:
                self.err(f'{where}.{key}: a string is required')
            return ''
        if not empty and not value.strip():
            self.err(f'{where}.{key}: empty text')
        self.safe(f'{where}.{key}', value)
        return value

    def ref(self, obj, key, where, known, kind):
        value = obj.get(key)
        if not isinstance(value, str) or value not in known:
            self.err(f'{where}.{key}: no {kind} with id {value!r}')
            return None
        return value

    def ident(self, obj, where, seen):
        value = obj.get('id')
        if not isinstance(value, str) or not ID_RE.match(value) or len(value) > 64:
            self.err(f'{where}.id: {value!r} is not a lower-case id of letters, digits, - and _ (at most 64)')
            return None
        if value in seen:
            self.err(f'{where}.id: duplicate id {value!r}')
            return None
        seen.add(value)
        self.safe(f'{where}.id', value)
        return value

    def questions(self, obj, key, where, many):
        """Ids of questions of the page; each must name a question anchored on the page (#q-...)."""
        if key not in obj:
            return []
        value = obj.get(key)
        values = value if many else [value]
        if (many and not isinstance(value, list)) or not all(isinstance(x, str) and x for x in values):
            self.err(f'{where}.{key}: {"a list of question ids" if many else "a question id"} is required')
            return []
        out = []
        for x in values:
            anchor = 'q-' + self.ctx.ident(x) if self.ctx is not None else None
            if anchor is None or anchor not in getattr(self.ctx, 'anchors', ()):
                # A reference the page cannot resolve fails the build but is not drawn; the atlas still draws for a draft.
                self.err(f'{where}.{key}: no question on the page with id {x!r}', reader=True)
            else:
                out.append(anchor)
        return out

    def texts(self, obj, key, where):
        value = obj.get(key, [])
        if not isinstance(value, list) or not all(isinstance(x, str) and x.strip() for x in value):
            self.err(f'{where}.{key}: a list of non-empty strings is required')
            return []
        for j, x in enumerate(value):
            self.safe(f'{where}.{key}[{j}]', x)
        return value

    def ids(self, obj, key, where, known, kind):
        value = obj.get(key, [])
        if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
            self.err(f'{where}.{key}: a list of ids is required')
            return []
        out = []
        for x in value:
            if x not in known:
                self.err(f'{where}.{key}: no {kind} with id {x!r}')
            elif x in out:
                self.err(f'{where}.{key}: {x!r} is listed twice')
            else:
                out.append(x)
        return out

    def safe(self, where, value):
        """The page's reader-visible rules, and the atlas's own, applied to every string and id.

        The text is read as written and again with _ and - read as spaces, because the page's rules
        use word boundaries and _ is a word character."""
        import audit  # the page's rules; the builder has imported it before the atlas is rendered
        bare = MATH_RE.sub(' ', value)
        spaced = re.sub(r'[_-]', ' ', bare)
        found = set()
        for pattern, why, flags in audit.FORBIDDEN:
            for text in (bare, spaced):
                m = re.search(pattern, text, flags)
                if m and (why, m.group(0)) not in found:
                    found.add((why, m.group(0)))
                    self.err(f'{where}: {why} {m.group(0)!r}', reader=not where.endswith('.id'))
        for rule, why in ((HOST_RE, 'address of another host'), (HASH_RE, 'hash-like token'),
                          (PERCENT_RE, 'percentage'), (LABEL_RE, 'label of the form name:part')):
            m = rule.search(bare)
            if m:
                self.err(f'{where}: {why} {m.group(0)!r}', reader=not where.endswith('.id'))

    def check(self, data):
        if not self.keys(data, 'atlas', 'atlas'):
            return
        if data.get('schema') != SCHEMA:
            self.err(f'atlas.schema: {data.get("schema")!r} is not {SCHEMA!r}')
        if 'asOf' in data and not isinstance(data['asOf'], str):
            self.err('atlas.asOf: a string is required')
        lists = {}
        for key in ('domains', 'claims', 'edges', 'comparisons', 'readingPaths'):
            value = data.get(key, [])
            if not isinstance(value, list):
                self.err(f'atlas.{key}: a list is required')
                value = []
            lists[key] = value
        if not lists['domains']:
            self.err('atlas.domains: at least one domain is required')
        if not lists['claims']:
            self.err('atlas.claims: at least one claim is required')
        self.check_domains(lists['domains'])
        self.check_claims(lists['claims'])
        self.check_edges(lists['edges'])
        self.styles()
        self.check_comparisons(lists['comparisons'])
        self.check_membership()
        self.check_paths(lists['readingPaths'])

    def check_domains(self, domains):
        seen = set()
        for i, d in enumerate(domains):
            where = f'domains[{i}]'
            if not self.keys(d, 'domain', where):
                continue
            did = self.ident(d, where, seen)
            label = self.text(d, 'label', where)
            summary = self.text(d, 'summary', where)
            conventions = self.texts(d, 'conventions', where) if 'conventions' in d else []
            questions = self.questions(d, 'relatedQuestionIds', where, True)
            if did:
                self.domain[did] = {'id': did, 'label': label, 'summary': summary, 'conventions': conventions,
                                    'questions': questions}
                self.domains.append(self.domain[did])

    def check_claims(self, claims):
        seen = set()
        titles = {}
        for i, c in enumerate(claims):
            where = f'claims[{i}]'
            if not self.keys(c, 'claim', where):
                continue
            cid = self.ident(c, where, seen)
            where = f'claims[{i}] ({cid})' if cid else where
            domain = self.ref(c, 'domainId', where, self.domain, 'domain')
            code, label = None, ''
            st = c.get('status')
            if 'status' in c and self.keys(st, 'status', where + '.status'):
                code = st.get('code')
                if not isinstance(code, str) or code not in CODES:
                    self.err(f'{where}.status.code: {code!r} is not one of {", ".join(CODES)}')
                    code = None
                label = self.text(st, 'label', where + '.status')
                if code and label and label not in self.status_labels.setdefault(code, []):
                    self.status_labels[code].append(label)  # display aliases: kept and checked, never shown (the code chooses the word)
            hyps = c.get('hypotheses')
            if not isinstance(hyps, list) or not all(isinstance(h, str) and h.strip() for h in hyps):
                if 'hypotheses' in c:
                    self.err(f'{where}.hypotheses: a list of non-empty strings is required')
                hyps = []
            for j, h in enumerate(hyps):
                self.safe(f'{where}.hypotheses[{j}]', h)
            if code == 'conditional' and not hyps and isinstance(c.get('hypotheses'), list):
                self.err(f'{where}: a conditional claim must list the hypotheses it is conditional on', reader=True)
            if code == 'scoped_negative' and not hyps and isinstance(c.get('hypotheses'), list):
                self.err(f'{where}: a scoped negative claim must list the hypotheses of its scope', reader=True)
            source = self.text(c, 'sourceLabel', where) if 'sourceLabel' in c else None
            form = self.text(c, 'form', where) if 'form' in c else None
            if form and form not in CLAIM_FORMS:
                self.err(f'{where}.form: unknown mathematical form {form!r}')
            comparisons = c.get('comparisonIds')
            if comparisons is not None and (not isinstance(comparisons, list)
                                            or not all(isinstance(x, str) for x in comparisons)):
                self.err(f'{where}.comparisonIds: a list of ids is required')
                comparisons = []
            ref = None
            section = None
            if 'sectionRef' in c:
                value = c['sectionRef']
                resolve = getattr(self.ctx, 'section_anchor', None)
                section = resolve(value) if resolve and isinstance(value, str) else None
                if not section or not source:
                    self.err(f'{where}.sectionRef: a chapter section and source label are required for {value!r}')
            if 'statementRef' in c:
                value = c.get('statementRef')
                anchor = self.ctx.anchor_for(value) if self.ctx is not None and isinstance(value, str) else None
                if not anchor:
                    self.err(f'{where}.statementRef: no statement on the page with id {value!r}')
                else:
                    ref = anchor
            title = self.text(c, 'title', where)
            key = ' '.join(title.split()).casefold()
            if key and cid:
                if key in titles:
                    self.err(f'{where}.title: claims {titles[key]!r} and {cid!r} have the same title')
                else:
                    titles[key] = cid
            claim = {'id': cid, 'domainId': domain, 'title': title, 'statement': self.text(c, 'statement', where),
                     'code': code, 'label': label, 'form': form, 'hypotheses': hyps, 'sourceLabel': source,
                     'comparisonIds': comparisons, 'statementRef': ref, 'sectionRef': section}
            if cid and code and domain:
                self.claim[cid] = claim
                self.claims.append(claim)
                self.number[cid] = len(self.claims)
                self.into[cid] = []
                self.out[cid] = []

    def check_edges(self, edges):
        seen = set()
        triples = set()
        for i, e in enumerate(edges):
            where = f'edges[{i}]'
            if not self.keys(e, 'edge', where):
                continue
            eid = self.ident(e, where, seen)
            where = f'edges[{i}] ({eid})' if eid else where
            source = self.ref(e, 'source', where, self.claim, 'claim')
            target = self.ref(e, 'target', where, self.claim, 'claim')
            ok = bool(source and target and eid)
            if source and source == target:
                self.err(f'{where}: a claim related to itself')
                ok = False
            relation = e.get('relation')
            if not isinstance(relation, str) or not RELATION_RE.match(relation):
                self.err(f'{where}.relation: {relation!r} is not a relation code (words joined by _, - or spaces)')
                ok = False
            else:
                self.safe(f'{where}.relation', relation)
            label = self.text(e, 'label', where)
            scope = self.text(e, 'scope', where, empty=True)
            if not ok:
                continue
            if (source, target, relation) in triples:
                self.err(f'{where}: a second {relation!r} edge from {source!r} to {target!r}')
                continue
            triples.add((source, target, relation))
            if relation in self.relations:
                if label not in self.relations[relation][0]:
                    self.relations[relation][0].append(label)  # each edge's own label is shown with the edge
            else:
                n = len(self.relations)
                self.relations[relation] = ([label], n, n)
            edge = {'id': eid, 'source': source, 'target': target, 'relation': relation, 'label': label, 'scope': scope}
            self.edges.append(edge)
            self.out[source].append(edge)
            self.into[target].append(edge)

    def styles(self):
        """Line style of each relation: its own when there are at most LINE_STYLES types, else the plain line for all."""
        plain = len(self.relations) > LINE_STYLES
        for rel, (labels, n, order) in list(self.relations.items()):
            self.relations[rel] = (labels, LINE_STYLES if plain else n, order)

    def check_comparisons(self, comparisons):
        seen = set()
        for i, k in enumerate(comparisons):
            where = f'comparisons[{i}]'
            if not self.keys(k, 'comparison', where):
                continue
            kid = self.ident(k, where, seen)
            where = f'comparisons[{i}] ({kid})' if kid else where
            domain = self.ref(k, 'domainId', where, self.domain, 'domain')
            item = {'id': kid, 'domainId': domain, 'title': self.text(k, 'title', where),
                    'overview': self.text(k, 'overview', where), 'buckets': [],
                    'question': self.questions(k, 'questionId', where, False),
                    'questions': self.questions(k, 'relatedQuestionIds', where, True)}
            listed = {}
            for key, code in BUCKETS:
                members = self.ids(k, key, where, self.claim, 'claim')
                kept = []
                for cid in members:
                    if cid in listed:
                        self.err(f'{where}: claim {cid!r} is in both {listed[cid]} and {key}')
                        continue
                    listed[cid] = key
                    kept.append(cid)
                    if self.claim[cid]['code'] != code:
                        self.err(f'{where}.{key}: claim {cid!r} has status {self.claim[cid]["code"]!r}, not {code!r}')
                item['buckets'].append((code, kept))
            if not listed:
                self.err(f'{where}: the comparison lists no claim')
            if kid and domain:
                self.comparisons.append(item)

    def check_membership(self):
        listed = {}
        for k in self.comparisons:
            for _, members in k['buckets']:
                for cid in members:
                    listed.setdefault(cid, set()).add(k['id'])
        known = {k['id'] for k in self.comparisons}
        for c in self.claims:
            mine = listed.get(c['id'], set())
            if c['comparisonIds'] is not None:
                own = set(c['comparisonIds'])
                for kid in sorted(own - known):
                    self.err(f'claims ({c["id"]}).comparisonIds: no comparison with id {kid!r}')
                for kid in sorted((own & known) ^ mine):
                    self.err(f'claim {c["id"]!r} and comparison {kid!r} disagree on whether the claim is in it')
            c['comparisonIds'] = [k['id'] for k in self.comparisons if k['id'] in mine]

    def check_paths(self, paths):
        seen = set()
        for i, p in enumerate(paths):
            where = f'readingPaths[{i}]'
            if not self.keys(p, 'path', where):
                continue
            pid = self.ident(p, where, seen)
            where = f'readingPaths[{i}] ({pid})' if pid else where
            kind = p.get('kind')
            if not isinstance(kind, str) or kind not in PATH_KINDS:
                self.err(f'{where}.kind: {kind!r} is not one of {", ".join(PATH_KINDS)}')
                kind = None
            title = self.text(p, 'title', where)
            summary = self.text(p, 'summary', where)
            note = self.text(p, 'note', where) if 'note' in p else ''
            stages = p.get('stages')
            if not isinstance(stages, list) or not stages:
                self.err(f'{where}.stages: at least one stage is required')
                stages = []
            items = []
            for j, s in enumerate(stages):
                sw = f'{where}.stages[{j}]'
                if not self.keys(s, 'stage', sw):
                    continue
                items.append({'label': self.text(s, 'label', sw), 'description': self.text(s, 'description', sw, empty=True),
                              'claimIds': self.ids(s, 'claimIds', sw, self.claim, 'claim')})
            if kind == 'source_bound_dependency_path' and pid:
                self.check_joins(pid, where, items)
            if pid and kind:
                self.paths.append({'id': pid, 'title': title, 'kind': kind, 'summary': summary, 'note': note, 'stages': items})

    def check_joins(self, pid, where, items):
        """Every claim of a stage is joined by a recorded relation to a claim of the stage next to it:
        the first stage to the second, every later stage to the one before it."""
        if len(items) < 2:
            self.err(f'{where}: a path joined by recorded relations needs at least two stages')
        for j, s in enumerate(items):
            if not s['claimIds']:
                self.err(f'{where}.stages[{j}]: a stage of a path joined by recorded relations needs a claim')
        for j, s in enumerate(items):
            other = j + 1 if j == 0 else j - 1
            if other >= len(items):
                continue
            for cid in s['claimIds']:
                if not any(joined(cid, o, self.edges) for o in items[other]['claimIds']):
                    self.err(f'{where}.stages[{j}]: claim {cid!r} is joined to no claim of stage {other + 1} '
                             f'by a recorded relation')
        for j in range(1, len(items)):
            before, here = set(items[j - 1]['claimIds']), set(items[j]['claimIds'])
            self.joins[(pid, j)] = [(e, e['source'] in here) for e in self.edges
                                    if (e['source'] in before and e['target'] in here)
                                    or (e['source'] in here and e['target'] in before)]


# Rendering --------------------------------------------------------------------------------------

class Renderer:
    """The atlas markup. Hooks: a claim is article[data-claim-id][data-status-code] with the anchor
    atlas-c-<id>; a relation is [data-edge-id][data-source][data-target][data-relation] wherever it is
    listed or drawn; a reading path is article[data-path-id][data-path-kind]."""

    def __init__(self, ctx, atlas, labels):
        self.ctx = ctx
        self.a = atlas
        self.L = labels
        self.uses = {}  # anchor -> times used; two uses is a problem
        self.problems = []  # reader findings of the renderer (the build fails; a draft still draws)
        self.unmarked = set()  # page statuses the page could not draw, each reported once

    def mark(self, code, label=None):
        """The page's mark for an atlas status: the mark of its page status (PAGE_STATUS), drawn by the page (ctx.mark),
        labelled when a label is given. Without a page (ctx without mark) no mark is drawn and the word stands alone.
        A page that cannot draw a status's mark fails the build: the alias is the content owner's ruling."""
        page = PAGE_STATUS.get(code)
        if not page or not hasattr(self.ctx, 'mark'):
            return ''
        drawn = self.ctx.mark(page, label) if label else self.ctx.mark(page)
        if not drawn and page not in self.unmarked:
            self.unmarked.add(page)
            self.problems.append(f'the page has no mark for its status {page!r}, the page status of the atlas status {code!r}')
        return drawn or ''

    def glyph(self, code):
        """The same mark as SVG content for a map node: the inner drawing of the page's mark, in a group that carries
        the page's colour class for that status (mark-<status>), at the node's left."""
        page = PAGE_STATUS.get(code)
        m = re.match(r'<svg\b[^>]*>(?:<title>.*?</title>)?(.*)</svg>\s*$', self.mark(code), re.S)
        if not page or not m:
            return ''
        return f'<g class="atlas-node-mark mark-{page.replace(" ", "-")}" transform="translate(-19 -6) scale(.75)">{m.group(1)}</g>'

    def esc(self, key, **kw):
        text = self.L[key]
        return html.escape(text.format(**kw) if kw else text)

    def rich(self, text, terms=True):
        markup = self.ctx.rich(text, terms=terms and TERMS)
        for old, new in FORMULA_CLASSES:
            markup = markup.replace(old, new)
        return markup

    def paragraphs(self, text):
        blocks = [b.strip() for b in re.split(r'\n\s*\n', text or '') if b.strip()]
        return ''.join(f'<p>{self.rich(b)}</p>' for b in blocks)

    def anchor(self, aid):
        self.uses[aid] = self.uses.get(aid, 0) + 1
        return aid

    def html(self):
        a, L = self.a, self.L
        parts = [('atlas-overview', L['part_map'], True), ('atlas-domains', L['part_domains'], True),
                 ('atlas-claims', L['part_claims'], True),
                 ('atlas-comparisons', L['part_comparisons'], bool(a.comparisons)),
                 ('atlas-paths', L['part_paths'], bool(a.paths))]
        nav = ''.join(f'<li><a href="#{pid}">{html.escape(t)}</a></li>' for pid, t, on in parts if on)
        words = ' '.join(f'<span data-word="{k[3:].replace("_", "-")}">{html.escape(v)}</span>'
                         for k, v in sorted(L.items()) if k.startswith('js_'))
        main = f'{self.overview()}{self.domains()}{self.claims()}{self.comparisons()}{self.paths()}'
        return (f'<p class="section-intro prose atlas-intro">{html.escape(L["intro"])}</p>'
                f'<nav class="atlas-parts" aria-label="{self.esc("parts")}"><ul>{nav}</ul></nav>'
                f'<div class="atlas-body"><template class="atlas-wordlist">{words}</template>'
                f'<div class="atlas-main">{main}</div>{self.claim_list()}</div>')

    # Pieces ---------------------------------------------------------------------------------------

    def title(self, c):
        return self.rich(c['title'], terms=False)

    def num(self, cid):
        """The index number of a claim; read aloud and in plain text as 'No. 5', so never as a count."""
        return f'<span class="atlas-num"><span class="atlas-vh">{self.esc("number")} </span>{self.a.number[cid]}</span>'

    def link(self, cid, labelled=False):
        """A claim named anywhere in the atlas: its index number, its mark and its title, as one link."""
        c = self.a.claim[cid]
        # Where the list is not grouped by status, the mark is named by its group, the word the key gives the mark
        # (the claim's own label is shown with the claim); in a grouped list the group heading names it.
        label = self.L['group_' + c['code']] if labelled else None
        return (f'<a class="atlas-link" href="#atlas-c-{cid}">{self.num(cid)}'
                f'{self.mark(c["code"], label)}<span class="atlas-link-title">{self.title(c)}</span></a>')

    def item(self, cid, seen=None):
        """A claim in a grouped list; a conditional claim and a scoped negative keep their hypotheses. Within one
        comparison (seen), a list of hypotheses already shown is named by the claim that shows it, not repeated."""
        c = self.a.claim[cid]
        hyps = ''
        key = tuple(c['hypotheses'])
        if seen is not None and c['code'] in ('conditional', 'scoped_negative') and key and key in seen:
            return (f'<li>{self.link(cid)}<p class="atlas-item-same">'
                    f'{self.esc("same_hyps", n=self.a.number[seen[key]])}</p></li>')
        if seen is not None and key:
            seen.setdefault(key, cid)
        if c['code'] in ('conditional', 'scoped_negative') and c['hypotheses']:
            lis = ''.join(f'<li>{self.rich(h)}</li>' for h in c['hypotheses'])
            hyps = (f'<div class="atlas-item-hyps"><span class="atlas-note-label">{self.esc("hypotheses_inline")}</span>'
                    f'<ol>{lis}</ol></div>')
        return f'<li>{self.link(cid)}{hyps}</li>'

    def group(self, code, members, kind='group', seen=None):
        shown = ''.join(self.item(cid, seen) for cid in members[:GROUP_SHOWN])
        rest = ''.join(self.item(cid, seen) for cid in members[GROUP_SHOWN:])
        body = (f'<ul class="atlas-claimlist">{shown}</ul>' if shown
                else f'<p class="atlas-none">{self.esc("none_listed")}</p>')
        if rest:
            body += (f'<details class="atlas-more"><summary class="atlas-more-h">{self.esc("more")}</summary>'
                     f'<ul class="atlas-claimlist">{rest}</ul></details>')
        prefix = 'ag' if kind == 'group' else 'ab'
        return (f'<div class="atlas-{kind} {prefix}-{cls(code)}"><h5 class="atlas-group-h">{self.mark(code)}'
                f'<span>{self.esc("group_" + code)}</span></h5>{body}</div>')

    def part(self, pid, title, body, extra_cls='', lead=None):
        self.anchor(pid)
        self.anchor(f'{pid}-h')
        lead = f'<p class="atlas-part-lead">{self.esc(lead)}</p>' if lead else ''
        return (f'<section class="atlas-part{extra_cls}" id="{pid}" aria-labelledby="{pid}-h">'
                f'<header class="atlas-part-head"><h3 class="atlas-part-h" id="{pid}-h"><a class="anchor" href="#{pid}">'
                f'{html.escape(title)}</a></h3>{lead}</header>{body}</section>')

    def overview(self):
        """The first part: the map of every claim and relation, with the key as its legend."""
        return self.part('atlas-overview', self.L['part_map'], self.key() + self.map(), extra_cls=' atlas-overview',
                         lead='lead_map')

    def key(self):
        items = []
        for code in CODES:
            items.append(f'<div class="atlas-key-item" data-key-status="{code}"><dt>{self.mark(code)}<span>{self.esc("group_" + code)}'
                         f'</span></dt><dd>{self.esc("gloss_" + code)}</dd></div>')
        if self.a.relations and any(k == LINE_STYLES for _, k, _ in self.a.relations.values()):
            # Too many types for distinct line styles: one plain line; each relation is named where it is listed.
            names = sorted(self.a.relations.items(), key=lambda kv: ' / '.join(kv[1][0]).lower())
            items_ = ''.join(f'<li data-key-relation="{html.escape(rel)}" data-key-style="{LINE_STYLES}">'
                             f'{html.escape(" / ".join(labels))}</li>' for rel, (labels, _, _) in names)
            rels = (f'<p class="atlas-rel-plain">{swatch(LINE_STYLES)}<span>{self.esc("key_plain_all")}</span></p>'
                    f'<details class="atlas-more atlas-rel-all"><summary class="atlas-more-h">{self.esc("rel_list")}</summary>'
                    f'<ul class="atlas-rel-names">{items_}</ul></details>')
        elif self.a.relations:
            rels = ''.join(f'<li data-key-relation="{html.escape(rel)}" data-key-style="{k}">{swatch(k)}'
                           f'<span class="atlas-rel-name">{html.escape(" / ".join(labels))}</span></li>'
                           for rel, (labels, k, _) in self.a.relations.items())
            rels = f'<ul class="atlas-rel-key">{rels}</ul>'
        else:
            rels = f'<p class="atlas-none">{self.esc("key_relations_none")}</p>'
        self.anchor('atlas-key-h')
        return (f'<div class="atlas-key" role="group" aria-labelledby="atlas-key-h">'
                f'<p class="atlas-key-h" id="atlas-key-h">{self.esc("key")}</p>'
                f'<div class="atlas-key-cols"><div><p class="atlas-key-sub">{self.esc("key_status")}</p>'
                f'<dl class="atlas-key-status">{"".join(items)}</dl>'
                f'<p class="atlas-key-note">{self.esc("key_separate")}</p></div>'
                f'<div class="atlas-key-relations"><p class="atlas-key-sub">{self.esc("key_relations")}</p>{rels}</div>'
                f'</div></div>')

    def unit_status(self, code):
        """For the page search: every claim is offered with the page status of its atlas status (data-qh-unit-status),
        so the page's status filters find it and its result shows the page's mark and word for that status."""
        page = PAGE_STATUS.get(code)
        return f' data-qh-unit-status="{html.escape(page)}"' if page else ''


    def domains(self):
        a = self.a
        cards = []
        for d in a.domains:
            did = self.anchor(f'atlas-d-{d["id"]}')
            self.anchor(f'{did}--h')
            members = [c for c in a.claims if c['domainId'] == d['id']]
            groups = ''.join(self.group(code, [c['id'] for c in members if c['code'] == code]) for code in CODES)
            own = [k for k in a.comparisons if k['domainId'] == d['id']]
            comps = self.question_links(d['questions'], 'questions_related')
            conv = ''
            if d['conventions']:
                items = ''.join(f'<li>{self.rich(x)}</li>' for x in d['conventions'])
                conv = (f'<div class="atlas-conventions" id="{self.anchor(did + "--conv")}">'
                        f'<p class="atlas-sub-h">{self.esc("conventions")}</p><ul>{items}</ul></div>')
            if own:
                links = ', '.join(f'<a href="#atlas-k-{k["id"]}">{self.rich(k["title"], terms=False)}</a>' for k in own)
                comps += (f'<p class="atlas-domain-comps"><span class="atlas-note-label">{self.esc("domain_comparisons")}</span> '
                          f'{links}</p>')
            cards.append(f'<article class="atlas-domain" id="{did}" data-domain-id="{d["id"]}" data-qh-unit aria-labelledby="{did}--h">'
                         f'<h4 class="atlas-domain-h" id="{did}--h" data-qh-unit-title><a class="anchor" href="#{did}">'
                         f'{self.rich(d["label"], terms=False)}</a></h4>'
                         f'<div class="atlas-domain-summary prose">{self.paragraphs(d["summary"])}</div>'
                         f'<details class="atlas-fold atlas-domain-fold"><summary class="atlas-fold-h atlas-more-h">'
                         f'{self.esc("domain_fold" if conv else "domain_fold_plain")}</summary>'
                         f'{conv}<div class="atlas-groups">{groups}</div>{comps}</details></article>')
        return self.part('atlas-domains', self.L['part_domains'], f'<div class="atlas-domains">{"".join(cards)}</div>',
                         lead='lead_domains')

    def claims(self):
        return self.part('atlas-claims', self.L['part_claims'], self.index(), lead='lead_claims')

    def map_layout(self):
        """The geometry of the map, shared by the map and the locator of the pane: the domains as lanes (their widths),
        the size of the drawing, and the place of every claim. A domain with many claims runs over several columns of
        its lane; the number of rows is the smallest that keeps the whole map within a full column, and at most
        MAP_ROWS, so the map keeps a screen's height; an atlas too wide for the budget scrolls across."""
        if getattr(self, '_layout', None):
            return self._layout
        a = self.a
        lanes = a.domains
        col_w, row_h, top, half, min_lane, budget = 58, 26, 18, 22, 96, 1100
        per = {d['id']: [c for c in a.claims if c['domainId'] == d['id']] for d in lanes}
        counts = [len(per[d['id']]) for d in lanes]
        tallest = max(counts + [1])

        def widths(rows):
            return [max(-(-max(n, 1) // rows) * col_w, min_lane) for n in counts]

        rows = None
        for r in range(min(12, tallest), tallest + 1):
            if sum(widths(r)) <= budget:
                rows = r
                break
        rows = min(rows or tallest, MAP_ROWS)
        lane_ws = widths(rows)
        width = sum(lane_ws)
        height = top * 2 + (rows - 1) * row_h + 18
        pos = {}
        x0 = 0
        for d, w in zip(lanes, lane_ws):
            members = per[d['id']]
            cols = max(1, -(-len(members) // rows))
            start = x0 + (w - cols * col_w) / 2
            for k, c in enumerate(members):
                pos[c['id']] = (start + (k // rows) * col_w + col_w / 2, top + 9 + (k % rows) * row_h)
            x0 += w
        self._layout = {'lanes': lanes, 'lane_ws': lane_ws, 'width': width, 'height': height, 'pos': pos,
                        'col_w': col_w, 'half': half}
        return self._layout

    def map(self):
        """Every claim by domain, joined by the recorded edges, at its own size (it scrolls in its box rather than
        shrinking), laid out by map_layout. Each mark is a link to its claim; the drawing is hidden from assistive
        technology, which reads the index instead."""
        a = self.a
        g = self.map_layout()
        lanes, lane_ws, width, height, pos = g['lanes'], g['lane_ws'], g['width'], g['height'], g['pos']
        col_w, half = g['col_w'], g['half']
        edges = []
        for e in a.edges:
            (sx, sy), (tx, ty) = pos[e['source']], pos[e['target']]
            if abs(sx - tx) > .01:
                way = 1 if tx > sx else -1
                x_0, x_1 = sx + way * half, tx - way * half
                bend = (x_1 - x_0) / 2
                d_ = f'M{x_0:.1f} {sy:.1f}C{x_0 + bend:.1f} {sy:.1f} {x_1 - bend:.1f} {ty:.1f} {x_1:.1f} {ty:.1f}'
            else:
                x_0 = sx + half
                bulge = min(10 + abs(ty - sy) * .2, col_w - 2 * half + 10)
                d_ = f'M{x_0:.1f} {sy:.1f}C{x_0 + bulge:.1f} {sy:.1f} {x_0 + bulge:.1f} {ty:.1f} {x_0:.1f} {ty:.1f}'
            k = a.relations[e['relation']][1]
            edges.append(f'<path class="atlas-edge rk-{k}" d="{d_}" {edge_hooks(e)} marker-end="url(#atlas-arrow)"/>')
        nodes = []
        for c in a.claims:
            x, y = pos[c['id']]
            nodes.append(f'<a class="atlas-node an-{cls(c["code"])}" href="#atlas-c-{c["id"]}" tabindex="-1" '
                         f'data-claim-ref="{c["id"]}" transform="translate({x:.1f} {y:.1f})">'
                         f'<rect class="atlas-pill" x="-{half}" y="-9" width="{2 * half}" height="18" rx="9"/>'
                         f'{self.glyph(c["code"])}'
                         f'<text x="7" y="4.5">{a.number[c["id"]]}</text></a>')
        grid = ' '.join(f'{w}fr' for w in lane_ws)
        heads = ''.join(f'<a class="atlas-track" href="#atlas-d-{d["id"]}">{self.rich(d["label"], terms=False)}</a>' for d in lanes)
        feet = ''.join(f'<span class="atlas-track">{self.rich(d["label"], terms=False)}</span>' for d in lanes)
        defs = ('<defs>' + ''.join(
            f'<marker id="{mid}" class="{mid}" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" '
            f'markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0.6 7.6 4 0 7.4z"/></marker>'
            for mid in ('atlas-arrow', 'atlas-arrow-on')) + '</defs>')
        edges_x = [sum(lane_ws[:i]) for i in range(1, len(lane_ws))]
        rules = ''.join(f'<path d="M{x} 0V{height}"/>' for x in edges_x)
        bands = ''.join(f'<rect x="{sum(lane_ws[:i])}" y="0" width="{lane_ws[i]}" height="{height}"/>' for i in range(1, len(lanes), 2))
        for aid in ('atlas-map', 'atlas-map-h', 'atlas-arrow', 'atlas-arrow-on', 'atlas-map-keys'):
            self.anchor(aid)
        return (f'<figure class="atlas-map" id="atlas-map" aria-labelledby="atlas-map-h">'
                f'<p class="atlas-fig-h" id="atlas-map-h">{self.esc("map")}</p>'
                f'<div class="atlas-map-frame"><span class="atlas-map-edge atlas-map-edge-l" aria-hidden="true"></span>'
                f'<span class="atlas-map-edge atlas-map-edge-r" aria-hidden="true"></span>'
                f'<div class="atlas-map-scroll" tabindex="0" role="region" aria-label="{self.esc("map_scroll")}" '
                f'aria-describedby="atlas-map-keys">'
                f'<div class="atlas-map-inner" style="--map-w:{width}">'
                f'<div class="atlas-tracks" style="grid-template-columns:{grid}">{heads}</div>'
                f'<svg class="atlas-map-svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
                f'aria-hidden="true" focusable="false">{defs}<g class="atlas-track-bands">{bands}</g>'
                f'<g class="atlas-track-rules">{rules}</g>'
                f'<g class="atlas-edges">{"".join(edges)}</g><g class="atlas-nodes">{"".join(nodes)}</g></svg>'
                f'<div class="atlas-tracks atlas-tracks-foot" style="grid-template-columns:{grid}" aria-hidden="true">{feet}</div>'
                f'</div></div>'
                f'</div><p class="atlas-vh" id="atlas-map-keys">{self.esc("map_keys")}</p>'
                f'<p class="atlas-vh" aria-live="polite" data-atlas-map-say></p>'
                f'<figcaption class="atlas-caption">{self.esc("map_caption")}</figcaption></figure>')

    def index(self):
        a = self.a
        rows = []
        for c in a.claims:
            rid = self.anchor(f'atlas-r-{c["id"]}')
            d = a.domain[c['domainId']]
            label = self.rich(d['label'], terms=False)
            rows.append(f'<tr id="{rid}" data-claim-ref="{c["id"]}">'
                        f'<td class="atlas-col-num">{a.number[c["id"]]}</td>'
                        f'<th scope="row" class="atlas-col-claim"><a class="atlas-link" href="#atlas-c-{c["id"]}">'
                        f'<span class="atlas-link-title">{self.title(c)}</span></a>'
                        f'<span class="atlas-row-domain">{label}</span></th>'
                        f'<td class="atlas-col-domain"><a href="#atlas-d-{d["id"]}">{label}</a></td>'
                        f'<td class="atlas-col-status">{self.mark(c["code"])}<span>{self.esc("group_" + c["code"])}</span></td>'
                        f'<td class="atlas-col-n">{len(a.into[c["id"]])}</td><td class="atlas-col-n">{len(a.out[c["id"]])}</td></tr>')
        self.anchor('atlas-index')
        long = ' atlas-index-long' if len(a.claims) > INDEX_LONG else ''
        return (f'<div class="atlas-index{long}" id="atlas-index"><div class="atlas-table-wrap">'
                f'<table class="atlas-table"><caption><span class="atlas-fig-h">{self.esc("index")}</span>'
                f'<span class="atlas-caption">{self.esc("index_caption")}</span></caption>'
                f'<thead><tr><th scope="col" class="atlas-col-num">{self.esc("col_number")}</th>'
                f'<th scope="col" class="atlas-col-claim">{self.esc("col_claim")}</th>'
                f'<th scope="col" class="atlas-col-domain">{self.esc("col_domain")}</th>'
                f'<th scope="col" class="atlas-col-status">{self.esc("col_status")}</th>'
                f'<th scope="col" class="atlas-col-n">{self.esc("col_in")}</th>'
                f'<th scope="col" class="atlas-col-n">{self.esc("col_out")}</th></tr></thead>'
                f'<tbody>{"".join(rows)}</tbody></table></div></div>')

    def claim_list(self):
        """Every claim in full, by domain. Without the script and in print it is the last part of the
        atlas; with the script it is the pane that shows the claim the address names, under the locator."""
        groups = []
        for d in self.a.domains:
            members = [c for c in self.a.claims if c['domainId'] == d['id']]
            if members:
                groups.append(f'<div class="atlas-claim-group"><h4 class="atlas-claim-group-h">'
                              f'{self.rich(d["label"], terms=False)}</h4>{"".join(self.claim(c) for c in members)}</div>')
        return self.part('atlas-full', self.L['part_full'], self.locator() + ''.join(groups), extra_cls=' atlas-claims-full')

    def locator(self):
        """The whole atlas in small, for the pane: the map's domains as bands (alternating as in the map) and every
        claim as a dot at its place in the map, from the same layout as the map. The script marks the selected claim
        with its number and status mark, as on its pill in the map, and marks its domain's band; the link returns to
        the map, where the same pill is highlighted. Hidden without the script (no claim is selected then) and in
        print. A dot is only a place: no relation is drawn or implied."""
        g = self.map_layout()
        width, height, pos = g['width'], g['height'], g['pos']
        x, bands = 0, []
        for i, (d, w) in enumerate(zip(g['lanes'], g['lane_ws'])):
            bands.append(f'<rect class="atlas-locator-track{" is-alt" if i % 2 else ""}" data-domain-ref="{html.escape(d["id"])}" '
                         f'x="{x}" y="0" width="{w}" height="{height}"/>')
            x += w
        dots = ''.join(f'<circle data-claim-ref="{html.escape(c["id"])}" cx="{pos[c["id"]][0]:.1f}" cy="{pos[c["id"]][1]:.1f}" r="9"/>'
                       for c in self.a.claims)
        return (f'<div class="atlas-locator" hidden>'
                f'<div class="atlas-locator-head"><p class="atlas-sub-h">{self.esc("locator")}</p>'
                f'<a class="atlas-locator-link" href="#atlas-map">{self.esc("locator_link")}</a></div>'
                f'<div class="atlas-locator-plot" style="aspect-ratio:{width} / {height}">'
                f'<svg class="atlas-locator-svg" viewBox="0 0 {width} {height}" aria-hidden="true" focusable="false">'
                f'<g class="atlas-locator-tracks">{"".join(bands)}</g><g class="atlas-locator-dots">{dots}</g>'
                f'<circle class="atlas-locator-ring" cx="0" cy="0" r="30"/></svg>'
                f'<span class="atlas-locator-no" aria-hidden="true"></span></div>'
                f'<p class="atlas-locator-caption">{self.esc("locator_caption")}</p></div>')

    def claim(self, c):
        a = self.a
        cid, code = c['id'], c['code']
        aid = self.anchor(f'atlas-c-{cid}')
        self.anchor(f'{aid}--h')
        d = a.domain[c['domainId']]
        form = c['form']
        env = f' data-kind="{form}" data-env="{form}"' if form else ''
        form_label = html.escape(CLAIM_FORMS[form]) + '. ' if form else ''
        hyps = ''.join(f'<li>{self.rich(h)}</li>' for h in c['hypotheses'])
        hyps = f'<ol class="atlas-hyps">{hyps}</ol>' if hyps else f'<p class="atlas-none">{self.esc("hypotheses_none")}</p>'
        notes = []
        if c['sourceLabel']:
            source = self.rich(c['sourceLabel'], terms=False)
            if c['sectionRef']:
                source = f'<a class="atlas-page-link" href="{html.escape(c["sectionRef"])}">{source}</a>'
            notes.append(f'<p class="atlas-note atlas-note-source"><span class="atlas-note-label">{self.esc("source")}</span> '
                         f'<span class="atlas-note-text">{source}</span></p>')
        if c['comparisonIds']:
            names = {k['id']: k for k in a.comparisons}
            links = ', '.join(f'<a href="#atlas-k-{kid}">{self.rich(names[kid]["title"], terms=False)}</a>'
                              for kid in c['comparisonIds'])
            notes.append(f'<p class="atlas-note"><span class="atlas-note-label">{self.esc("in_comparisons")}</span> '
                         f'<span class="atlas-note-text">{links}</span></p>')
        if c['statementRef']:
            notes.append(f'<p class="atlas-note"><a class="atlas-page-link" href="{html.escape(c["statementRef"])}">'
                         f'{self.esc("statement_link")}</a></p>')
        if d['conventions']:
            notes.append(f'<p class="atlas-note"><a class="atlas-conv-link" href="#atlas-d-{d["id"]}--conv">'
                         f'{self.esc("conventions_link")}</a></p>')
        return (f'<article class="atlas-claim as-{cls(code)}" id="{aid}" data-claim-id="{cid}" data-status-code="{code}" '
                f'data-domain-id="{d["id"]}" data-number="{a.number[cid]}" data-qh-unit{self.unit_status(code)}{env} aria-labelledby="{aid}--h">'
                f'<header class="atlas-claim-head"><p class="atlas-claim-meta">'
                f'<span class="atlas-chip ac-{cls(code)}">{self.mark(code)}<span class="atlas-chip-group">'
                f'{self.esc("group_" + code)}</span></span>'
                f'<span class="atlas-claim-no">{self.esc("number")} {a.number[cid]}</span>'
                f'<span class="atlas-claim-domain"><a href="#atlas-d-{d["id"]}">{self.rich(d["label"], terms=False)}</a></span></p>'
                f'<h5 class="atlas-claim-title" id="{aid}--h" data-qh-unit-title>{form_label}{self.title(c)}</h5></header>'
                f'<div class="atlas-statement">{self.paragraphs(c["statement"])}</div>'
                f'<div class="atlas-hyp-block"><p class="atlas-sub-h">{self.esc("hypotheses")}</p>{hyps}</div>'
                f'{"".join(notes)}{self.relations(c, "in")}{self.relations(c, "out")}</article>')

    def question_links(self, anchors, label):
        """Reuse the Reference heading in the link, including when the Atlas is a separate page."""
        if not anchors:
            return ''
        headings = getattr(self.ctx, 'question_heading_html', {})
        links = ', '.join(f'<a class="atlas-question-link" href="#{q}" data-question-ref="{q}">'
                          f'{headings.get(q) or self.esc("question_link")}</a>' for q in anchors)
        return f'<p class="atlas-note"><span class="atlas-note-label">{self.esc(label)}</span> {links}</p>'

    def sentence(self, e, me=None):
        """One recorded relation as the sentence '<source> <label> <target>', in the edge's own direction.
        `me` names the claim the list belongs to, which is written as 'this claim'."""
        k = self.a.relations[e['relation']][1]
        rel = f'<span class="atlas-rel-label">{swatch(k)}{html.escape(e["label"])}</span>'
        if me == e['target']:
            body = f'{self.link(e["source"], labelled=True)} {rel} <span class="atlas-rel-self">{self.esc("this_claim")}</span>'
        elif me == e['source']:
            body = f'<span class="atlas-rel-self">{self.esc("this_claim_lead")}</span> {rel} {self.link(e["target"], labelled=True)}'
        else:
            body = f'{self.link(e["source"], labelled=True)} {rel} {self.link(e["target"], labelled=True)}'
        scope = f'<span class="atlas-rel-scope">{self.rich(e["scope"])}</span>' if e['scope'].strip() else ''
        return f'<span class="atlas-rel-sentence">{body}</span>{scope}'

    def relations(self, c, way):
        a = self.a
        edges = a.into[c['id']] if way == 'in' else a.out[c['id']]
        edges = sorted(edges, key=lambda e: a.relations[e['relation']][2])  # stable: data order within a relation
        items = ''.join(f'<li class="atlas-rel" {edge_hooks(e)}>{self.sentence(e, c["id"])}</li>' for e in edges)
        heading = self.esc('rel_in' if way == 'in' else 'rel_out')
        body = (f'<ul class="atlas-rels" data-dir="{way}">{items}</ul>' if items
                else f'<p class="atlas-none">{self.esc("rel_none")}</p>')
        return f'<div class="atlas-rel-block" data-dir="{way}"><p class="atlas-sub-h">{heading}</p>{body}</div>'

    def comparisons(self):
        a = self.a
        if not a.comparisons:
            return ''
        out = []
        for k in a.comparisons:
            kid = self.anchor(f'atlas-k-{k["id"]}')
            self.anchor(f'{kid}--h')
            d = a.domain[k['domainId']]
            seen = {}
            buckets = ''.join(self.group(code, members, kind='bucket', seen=seen) for code, members in k['buckets'])
            out.append(f'<details class="atlas-fold atlas-comparison" id="{kid}" data-comparison-id="{k["id"]}" data-qh-unit '
                       f'aria-labelledby="{kid}--h"><summary class="atlas-fold-h">'
                       f'<span class="atlas-claim-domain">{self.rich(d["label"], terms=False)}</span>'
                       f'<h4 class="atlas-comparison-h" id="{kid}--h" data-qh-unit-title>{self.rich(k["title"], terms=False)}</h4>'
                       f'</summary><div class="atlas-fold-body">'
                       f'<p class="atlas-claim-domain"><a href="#atlas-d-{d["id"]}">{self.rich(d["label"], terms=False)}</a></p>'
                       f'<div class="atlas-overview prose">{self.paragraphs(k["overview"])}</div>'
                       f'{self.question_links(k["question"], "question_own")}{self.question_links(k["questions"], "questions_related")}'
                       f'<div class="atlas-buckets">{buckets}</div></div></details>')
        return self.part('atlas-comparisons', self.L['part_comparisons'], f'<div class="atlas-comparisons">{"".join(out)}</div>',
                         lead='lead_comparisons')

    def paths(self):
        a = self.a
        if not a.paths:
            return ''
        out = []
        for p in a.paths:
            pid = self.anchor(f'atlas-p-{p["id"]}')
            self.anchor(f'{pid}--h')
            dep = p['kind'] == 'source_bound_dependency_path'
            kind = (f'<p class="atlas-path-kind"><span class="atlas-kind-tag">'
                    f'{self.esc("path_dependency" if dep else "path_editorial")}</span> '
                    f'{self.esc("path_dependency_note" if dep else "path_editorial_note")}</p>')
            stages = []
            for j, s in enumerate(p['stages']):
                join = ''
                if dep and j > 0:
                    lines = ''.join(f'<li {edge_hooks(e)}>{self.sentence(e)}'
                                    + (f' <span class="atlas-join-back">({self.esc("join_back", n=j + 1, m=j)})</span>' if back else '')
                                    + '</li>' for e, back in a.joins.get((p['id'], j), []))
                    join = (f'<div class="atlas-join"><p class="atlas-sub-h">{self.esc("joined", n=j + 1, m=j)}</p>'
                            f'<ul class="atlas-join-list">{lines}</ul></div>')
                single = (len(s['claimIds']) == 1 and
                          s['label'].strip() == a.claim[s['claimIds'][0]]['title'].strip())
                claims = '' if single else ''.join(f'<li>{self.link(cid, labelled=True)}</li>' for cid in s['claimIds'])
                claims = f'<ul class="atlas-claimlist">{claims}</ul>' if claims else ''
                desc = (f'<div class="atlas-stage-desc prose">{self.paragraphs(s["description"])}</div>'
                        if s['description'].strip() else '')
                stages.append(f'<li class="atlas-stage" data-stage="{j}">'
                              f'<h5 class="atlas-stage-h"><span class="atlas-stage-n">{self.esc("stage", n=j + 1)}</span> '
                              + (self.link(s['claimIds'][0], labelled=True) if single else
                                 f'<span class="atlas-stage-label">{self.rich(s["label"], terms=False)}</span>') + '</h5>'
                              f'{join}{desc}{claims}</li>')
            tag = f'<span class="atlas-kind-tag">{self.esc("path_dependency" if dep else "path_editorial")}</span>'
            out.append(f'<details class="atlas-fold atlas-path {"ap-dependency" if dep else "ap-editorial"}" id="{pid}" '
                       f'data-path-id="{p["id"]}" data-path-kind="{p["kind"]}" data-qh-unit aria-labelledby="{pid}--h">'
                       f'<summary class="atlas-fold-h">{tag}'
                       f'<h4 class="atlas-path-h" id="{pid}--h" data-qh-unit-title>{self.rich(p["title"], terms=False)}</h4>'
                       f'</summary><div class="atlas-fold-body">'
                       f'{kind}<div class="atlas-path-summary prose">{self.paragraphs(p["summary"])}</div>'
                       + (f'<p class="atlas-path-note">{self.rich(p["note"])}</p>' if p['note'].strip() else '') +
                       f'<ol class="atlas-stages">{"".join(stages)}</ol></div></details>')
        return self.part('atlas-paths', self.L['part_paths'], f'<div class="atlas-paths">{"".join(out)}</div>',
                         lead='lead_paths')


def edge_hooks(e):
    return (f'data-edge-id="{e["id"]}" data-source="{e["source"]}" data-target="{e["target"]}" '
            f'data-relation="{e["relation"]}"')


def swatch(k):
    return (f'<svg class="atlas-swatch rk-{k}" viewBox="0 0 28 8" width="28" height="8" aria-hidden="true" focusable="false">'
            f'<path d="M1 4H27"/></svg>')
