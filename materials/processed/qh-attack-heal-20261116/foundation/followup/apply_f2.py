#!/usr/bin/env python3
"""Apply the F2 follow-up (successor content fields) to the producer copy in followup/src, guarded: each
replacement must match exactly once. Run from the lane directory: python3 followup/apply_f2.py

F2 shows the composed successor payload's new fields: the top-level `orientation` (its own part: explanation,
programme families linking their member families, reading guidance), the principal results' `summary`, the
`as_of_utc` time in the as-of line, a link from a statement with `atlasClaimId` to its claim when the atlas draws
that claim's anchor (AtlasContext.claim_anchor), and validates `scientific_atlas` against atlas.json."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'src')


def edit(rel, pairs):
    p = os.path.join(SRC, rel)
    s = open(p, encoding='utf-8').read()
    for o, n in pairs:
        assert s.count(o) == 1, (rel, s.count(o), o[:110])
        s = s.replace(o, n)
    open(p, 'w', encoding='utf-8').write(s)
    print(rel, 'ok', len(pairs))


edit('compiler/quantum-holography-status/status.py', [
    ("""    def question_anchor(self, question_id):""",
     """    @staticmethod
    def claim_anchor(claim_id):
        \"\"\"The id the atlas gives the element of a claim ('atlas-claim-…'); a statement of the page whose content names
        this claim (atlasClaimId) links to it when the atlas draws it.\"\"\"
        return 'atlas-claim-' + ident(claim_id or '')

    def question_anchor(self, question_id):"""),
    ("""        id_attr = f' id="{sid}"' if sid else ''
        added = ' added' if s.get('added') else ''""",
     """        id_attr = f' id="{sid}"' if sid else ''
        claim = (s.get('atlasClaimId') or '').strip()
        if claim:
            id_attr += f' data-atlas-claim="{html.escape(claim)}"'
        added = ' added' if s.get('added') else ''"""),
    ("""        hypotheses = [h for h in (s.get('hypotheses') or []) if (h or '').strip()]""",
     """        summary = (s.get('summary') or '').strip()
        if summary:
            out.append(f'<p class="statement-summary">{self.rich(summary, seen)}</p>')
        hypotheses = [h for h in (s.get('hypotheses') or []) if (h or '').strip()]"""),
    ("""        if notes:
            out.append('<p class="statement-notes">' + ' <span class="sep" aria-hidden="true">·</span> '.join(notes) + '</p>')
        out.append('</article>')""",
     """        if notes:
            out.append('<p class="statement-notes">' + ' <span class="sep" aria-hidden="true">·</span> '.join(notes) + '</p>')
        if claim:
            out.append(f'\\x00ACLAIM:{ident(claim)}\\x00')  # a link to the claim, filled in once the atlas is drawn
        out.append('</article>')"""),
    ("""        data_path = self.folder / 'atlas.json'
        if not data_path.exists():
            return '', None""",
     """        data_path = self.folder / 'atlas.json'
        if not data_path.exists():
            if (self.content or {}).get('scientific_atlas'):
                self.problems.append('scientific_atlas names an atlas, but there is no atlas.json in the content folder')
            return '', None"""),
    ("""        data = json.loads(data_path.read_text(encoding='utf-8'))
        result = module.render(data, AtlasContext(self)) or {}""",
     """        data = json.loads(data_path.read_text(encoding='utf-8'))
        pointer = (self.content or {}).get('scientific_atlas') or {}
        if pointer:
            if pointer.get('path', 'atlas.json') != 'atlas.json':
                self.problems.append(f'scientific_atlas: path {pointer.get("path")!r}; the atlas is read from atlas.json in the content folder')
            for key in ('schema', 'asOf'):
                if pointer.get(key) and data.get(key) != pointer.get(key):
                    self.problems.append(f'scientific_atlas: {key} {pointer.get(key)!r} but atlas.json has {data.get(key)!r}')
        result = module.render(data, AtlasContext(self)) or {}"""),
    ("""                f'<p class="as-of">{html.escape(L["as_of"])} <time datetime="{html.escape(c["as_of"])}">'
                f'{html.escape(long_date(c["as_of"]))}</time>'""",
     """                f'<p class="as-of">{html.escape(L["as_of"])} {self.as_of_html(c)}'"""),
    ("""                f'<time datetime="{html.escape(c["as_of"])}">{html.escape(long_date(c["as_of"]))}</time></p>'""",
     """                f'{self.as_of_html(c)}</p>'"""),
    ("""            'terms': (many(len(self.term_links.entries), 'definitions_one', 'definitions_many'), ''),""",
     """            'terms': (many(len(self.term_links.entries), 'definitions_one', 'definitions_many'), ''),
            'orientation': (many(len((c.get('orientation') or {}).get('programmeFamilies') or []), 'groups_one', 'groups_many'), ''),"""),
    ("""    def counts(self, c):""",
     """    def as_of_html(self, c):
        \"\"\"The date of the content, with the time of its evidence boundary when the content gives one (as_of_utc).\"\"\"
        day = c.get('as_of') or ''
        when = c.get('as_of_utc') or ''
        m = re.fullmatch(r'(\\d{4}-\\d{2}-\\d{2})T(\\d{2}):(\\d{2})(?::\\d{2}(?:\\.\\d+)?)?Z', when)
        if when and not m:
            self.problems.append(f'as_of_utc {when!r} is not a UTC time (YYYY-MM-DDTHH:MMZ)')
        if m and m.group(1) != day:
            self.problems.append(f'as_of {day!r} and as_of_utc {when!r} name different days')
        shown = long_date(day) + (f', {m.group(2)}:{m.group(3)} UTC' if m else '')
        return f'<time datetime="{html.escape(when if m else day)}">{html.escape(shown)}</time>'

    def orientation(self, c):
        \"\"\"How the programme fits together: the content's explanation, its families of examples in groups (each
        group links its families in the table), and the content's guidance for reading the page.\"\"\"
        o = c.get('orientation') or {}
        if not o:
            return ''
        L = self.page['labels']
        rows = {r.get('id'): r for r in c.get('rows', [])}
        text = ''.join(f'<p>{self.rich(p)}</p>' for p in o.get('explanation') or [] if (p or '').strip())
        groups = []
        for i, g in enumerate(o.get('programmeFamilies') or []):
            gid = 'pf-' + ident(g.get('id') or g.get('title') or str(i))
            self.anchors.add(gid)
            links = []
            for fid in g.get('familyIds') or []:
                r = rows.get(fid)
                if r is None:
                    self.problems.append(f'orientation {g.get("id")!r}: no family {fid!r} in the table')
                    continue
                rid = 'row-' + ident(r.get('id') or r['name'])
                links.append(f'<li><a href="#{rid}">{self.rich(r["name"], terms=False)}</a></li>')
            groups.append(f'<div class="pf" id="{gid}"><h3><a class="anchor" href="#{gid}">{self.rich(g.get("title", ""), terms=False)}</a></h3>'
                          f'<div class="pf-text prose">{self.paragraphs(g.get("text", ""))}</div>'
                          f'<p class="pf-label">{html.escape(L["orientation_families"])}</p><ul class="pf-families">{"".join(links)}</ul></div>')
        guide = ''.join(f'<div class="guide-item"><dt>{self.rich(x.get("title", ""), terms=False)}</dt>'
                        f'<dd>{self.rich(x.get("text", ""))}</dd></div>' for x in o.get('readerGuidance') or [])
        body = (f'<div class="orientation-text prose">{text}</div>' if text else '') + \\
               (f'<div class="pfs">{"".join(groups)}</div>' if groups else '') + \\
               (f'<div class="guidance"><h3 class="guidance-title">{html.escape(L["orientation_guidance"])}</h3><dl class="guide">{guide}</dl></div>'
                if guide else '')
        return self.section('orientation', o.get('title') or L['orientation'], body, cls='wide orientation',
                            kicker=L.get('orientation_kicker'))

    def counts(self, c):"""),
    ("""        cover = self.cover(c)
        changes = self.changes(c)""",
     """        cover = self.cover(c)
        orientation = self.orientation(c)
        changes = self.changes(c)"""),
    ("""        parts = {}
        if atlas:
            parts['atlas'] = html.escape(atlas_nav)""",
     """        parts = {}
        if orientation:
            parts['orientation'] = self.rich((c.get('orientation') or {}).get('title') or L['orientation'], terms=False)
        if atlas:
            parts['atlas'] = html.escape(atlas_nav)"""),
    ("""        nav_items = [('programme', L['nav_programme'])]
        if atlas:""",
     """        nav_items = [('programme', L['nav_programme'])]
        if orientation:
            nav_items.append(('orientation', L['nav_orientation']))
        if atlas:"""),
    ("""{cover}{changes}{atlas}{principal}{key}{examples}""", """{cover}{changes}{orientation}{atlas}{principal}{key}{examples}"""),
    ("""        unnumbered = sorted(set(re.findall('\\x00PART:([\\\\w-]+)\\x00', body)) - set(number))""",
     """        atlas_ids = set(re.findall(r'\\sid="([^"]+)"', atlas))
        body = re.sub('\\x00ACLAIM:([\\\\w-]+)\\x00',
                      lambda m: (f'<p class="statement-notes statement-atlas"><span class="note-label"><a href="#atlas-claim-{m.group(1)}">'
                                 f'{html.escape(L["in_atlas"])}</a></span></p>'
                                 if f'atlas-claim-{m.group(1)}' in atlas_ids else ''), body)
        unnumbered = sorted(set(re.findall('\\x00PART:([\\\\w-]+)\\x00', body)) - set(number))"""),
])

edit('compiler/quantum-holography-status/status.css', [
    (""".section.wide > .section-head, .section.wide > .section-intro, .section.wide > .row-tools, .section.wide > .rows {""",
     """.section.wide > .section-head, .section.wide > .section-intro, .section.wide > .row-tools, .section.wide > .rows,
.section.wide > .orientation-text, .section.wide > .guidance {"""),
    (""".statement-text p:last-child { margin-bottom: 0; }""",
     """.statement-text p:last-child { margin-bottom: 0; }
/* A principal result's summary, before its hypotheses and its statement. */
.statement-summary { margin: 0 0 var(--s2); color: var(--ink-2); }
/* The claim of the atlas that a statement shows, when the atlas draws it: a note label, which the search skips. */
.statement-notes.statement-atlas { margin-top: var(--s1); }

/* How the programme fits together: the content's explanation on the reading column, its groups of families on the
   wide frame (two columns from 1180px), each linking its families in the table, then the reading guidance. */
.pfs { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--s3) var(--s5); max-width: var(--measure); margin: var(--s4) auto 0; }
@media (min-width: 1180px) { .pfs { max-width: var(--wide); grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.pf { border-top: 1px solid var(--rule); padding-top: var(--s2); min-width: 0; }
.pf h3 { font-size: var(--text-h3); font-weight: 400; margin: 0 0 var(--s1); }
.pf-text { color: var(--ink-2); }
.pf-text p:last-child { margin-bottom: 0; }
.pf-label { margin: var(--s2) 0 var(--s1); font-size: var(--text-xs); font-variant-caps: all-small-caps; font-variant-numeric: oldstyle-nums;
            letter-spacing: var(--track); color: var(--ink-4); }
.pf-families { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: var(--s1) 18px; font-size: var(--text-sm); }
.guidance { margin-top: var(--s5); }
.guidance-title { font-size: var(--text-h3); font-weight: 400; margin: 0 0 var(--s2); }
.guide { margin: 0; display: grid; gap: var(--s2); }
.guide-item dt { font-weight: 600; }
.guide-item dd { margin: var(--s1) 0 0; color: var(--ink-2); }"""),
])

edit('compiler/quantum-holography-status/status.css', [
    # A10-A3-02: with more parts the bar can overflow at any width, so the end fade stays (it covers only the list's
    # end padding when the links fit).
    ("""@media (min-width: 1040.02px) { .nav { -webkit-mask-image: none; mask-image: none; } }""",
     """/* The end fade stays at every width: it marks links beyond the edge, and covers only the list's end padding when they fit. */"""),
])

edit('compiler/quantum-holography-status/status.py', [
    # A10-A3-04: the separator binds to the link after it, so a narrow date line breaks before '· Contents'
    ("""f' <span class="sep" aria-hidden="true">·</span> <a href="#changes">""", """f' <span class="sep" aria-hidden="true">·</span>&nbsp;<a href="#changes">"""),
    ("""f' <span class="sep" aria-hidden="true">·</span> <a href="#contents">""", """f' <span class="sep" aria-hidden="true">·</span>&nbsp;<a href="#contents">"""),
])

edit('compiler/quantum-holography-status/status-print.css', [
    ("""  /* Counterexamples */""",
     """  /* How the programme fits together: block flow on paper (a grid that crosses a page can lose an item). */
  .pfs { display: block; }
  .pf { break-inside: avoid; margin: 0 0 10pt; }
  .statement-atlas { display: none !important; }

  /* Counterexamples */"""),
])

p = os.path.join(SRC, 'content/quantum-holography-status/page.json')
raw = open(p, encoding='utf-8').read()
d = json.loads(raw)
add = {'orientation': 'How the programme fits together', 'orientation_kicker': 'Orientation', 'nav_orientation': 'Orientation',
       'orientation_families': 'Families of examples', 'orientation_guidance': 'How to read the page',
       'groups_one': '1 group of families', 'groups_many': '{n} groups of families', 'in_atlas': 'In the atlas'}
anchor = '    "part": "§{n}",\n'
assert raw.count(anchor) == 1
raw = raw.replace(anchor, anchor + ''.join(f'    {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)},\n' for k, v in add.items() if k not in d['labels']))
d2 = json.loads(raw)
assert all(d2['labels'][k] == v for k, v in add.items())
open(p, 'w', encoding='utf-8').write(raw)
print('page.json ok', len(add), 'labels')
