"""Runs audit.run from a given producer folder on small synthetic pages, each carrying one leak class.
Usage: python -I -B qh-audit-fixtures.py <folder containing audit.py and status.py> [--out result.json]
Reads only; writes only --out. Each fixture states whether the healed audit must fail it (leak), pass it with no
specific warning (clean) or pass it with a specific warning (warn). Formula probes are rendered by the vendored Temml
(the tex2mathml bridge beside the producer folder), so their markup is what a build makes. Private-path probes are
read from the file named by QH_PRIVATE_PROBES (one probe per line, kept outside the repository so that no private
name is written here); without it those fixtures are reported as skipped.
"""
import importlib
import json
import os
import subprocess
import sys
from pathlib import Path

folder = sys.argv[1]
out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else None
BRIDGE = Path(folder).resolve().parent / 'quantum-holography-tracker' / 'tex2mathml.cjs'


def tex(source):
    """The MathML a build makes for the inline formula source."""
    r = subprocess.run(['node', str(BRIDGE)], input=json.dumps([{'tex': source, 'display': False}]),
                       capture_output=True, text=True, check=True)
    row = json.loads(r.stdout)[0]
    if 'html' not in row:
        raise SystemExit(f'Temml refused {source!r}: {row}')
    return row['html']
sys.dont_write_bytecode = True
sys.path.insert(0, folder)
audit = importlib.import_module('audit')


class Terms:
    entries = []
    used = {}


class MathJobs:
    jobs = []
    errors = []


class Build:
    """The parts of status.Build that audit.run reads."""
    def __init__(self):
        self.problems, self.warnings, self.term_links, self.math = [], [], Terms(), MathJobs()
        self.content = {'rows': [], 'principal': []}

    @staticmethod
    def all_statements(c):
        return iter(())


def page(body, head='<title>Status page</title>'):
    return f'<!DOCTYPE html><html><head>{head}</head><body>{body}</body></html>'


FIXTURES = [
    ('leak', 'tag-merge', page('<p><span class="status-chip">Proved</span><span>Audit of the bulk</span></p>')),
    ('leak', 'mtext', page('<p>x <math><mrow><mtext>see the ledger in ADOPTION.md</mtext></mrow></math></p>')),
    ('leak', 'aria-title', page('<button aria-label="ledger T12" title="/Users/x/prep/a.md">x</button>')),
    ('leak', 'id', page('<p id="s-ast-t152-wave-3">x</p>')),
    ('leak', 'process', page('<p>wave 3 of the attack-heal swarm, phase 2, session 12, 87% complete</p>')),
    ('leak', 'head', page('<p>x</p>', '<title>Status by Claude</title><meta name="description" content="written with codex">')),
    ('leak', 'raw-tex-text', page('<p>this establishes only \\(c=33\\) here</p>')),
    ('leak', 'tex-in-aria', page('<button aria-label="\\(W\\)-algebras, Koszul dual: Open problem">x</button>')),
    ('clean', 'plain-math-prose', page('<p>The vertex algebra is strongly rational; its phase space and branch cuts are classical.</p>')),
    ('clean', 'citation', page('<p>Reference: Costello and Gwilliam (2016), Factorization algebras.</p>')),
    # A2's cycle-2 probes (A2-A2-04, A2-A2-05, A2-A2-06)
    ('leak', 'id-ledger', page('<p id="s-ledger-entry">x</p>')),
    ('leak', 'id-inscribe-adoption', page('<p id="term-inscribe-adoption">x</p>')),
    ('warn', 'id-phase-2', page('<p id="s-phase-2-result">x</p>')),
    ('leak', 'id-session-12', page('<p id="open-session-12">x</p>')),
    ('leak', 'id-identifier-three-digits', page('<p id="s-ast-t152">x</p>')),
    ('warn', 'id-identifier-shape', page('<p id="s-decisive-native-r3-covariant">x</p>')),
    ('leak', 'visible-G10', page('<p>as in G10 above</p>')),
    ('leak', 'visible-version-2', page('<p>see version 2 of the argument</p>')),
    ('leak', 'visible-Round-4', page('<p>Round 4 settled this</p>')),
    ('warn', 'visible-round-4-lowercase', page('<p>after round 4 the bound holds</p>')),
    ('leak', 'json-data-block', page('<script type="application/json" id="qh-atlas-data">{"summary": "Astra-authored", "source": "/Users/x/a/ADOPTION.md", "note": "Wave 3"}</script><p>x</p>')),
    ('leak', 'css-comment', page('<p>x</p>', '<title>Status page</title><style>/* written by claude */ p { color: red }</style>')),
    ('leak', 'html-comment', page('<!-- ledger entry T12 --><p>x</p>')),
    ('leak', 'svg-title', page('<p><svg role="img"><title>ledger entry</title></svg> x</p>')),
    ('leak', 'mathrm-word', page('<p>x <math><mi mathvariant="normal">ledger</mi></math></p>')),
    ('leak', 'operatorname-word', page('<p>x <math><mi>audit</mi></math></p>')),
    ('leak', 'soft-hyphen', page('<p>the led&shy;ger shows it</p>')),
    ('leak', 'aria-roledescription', page('<div aria-roledescription="ledger">x</div>')),
    ('clean', 'chains-cochains', page('<p>The map from chains/cochains to the dual complex is an equivalence.</p>')),
    ('clean', 'tie-slash-in-tex', page('<p>x <math><semantics><mi>A</mi><annotation encoding="application/x-tex">A~/~B</annotation></semantics></math></p>')),
    ('warn', 's-wave-1', page('<p>the s-wave 1 contribution cancels</p>')),
    ('warn', 'phase-0', page('<p>the phase 0 term vanishes</p>')),
    ('warn', 'percent-in-formula', page('<p>x <math><mtext>50% of modes</mtext></math></p>')),
    # R3-F cycle 3 (A3-F-02): surfaces the audit did not read
    ('leak', 'svg-text', page('<p><svg role="img"><text>ledger entry</text></svg> x</p>')),
    ('leak', 'svg-desc', page('<p><svg role="img"><desc>drawn by claude</desc></svg> x</p>')),
    ('leak', 'data-attribute', page('<p data-label-published="output of the attack heal swarm">x</p>')),
    ('leak', 'json-single-quoted-type', page("<script type='application/json'>{\"note\": \"see the ledger\"}</script><p>x</p>")),
    ('leak', 'other-data-type', page('<script type="text/plain">notes from the swarm</script><p>x</p>')),
    ('leak', 'aria-label-single-quoted', page("<button aria-label='ledger'>x</button>")),
    ('leak', 'js-string', page("<p>x</p><script>var note = 'see the ledger';</script>")),
    ('leak', 'js-line-comment', page('<p>x</p><script>var a = 1; // written with codex\nvar b = a / 2;</script>')),
    ('leak', 'css-generated-content', page('<p>x</p>', '<title>Status page</title><style>p::after { content: "Wave 3"; }</style>')),
    ('leak', 'meta-other', page('<p>x</p>', '<title>Status page</title><meta name="keywords" content="ledger, audit">')),
    ('leak', 'comment-names-source-file', page('<p>x</p>', '<title>Status page</title><style>/* the rules of status.css */ p { color: red }</style>')),
    ('clean', 'js-regex-and-division', page("<p>x</p><script>var r = /['\"]/g, h = 10 / 2; var s = 'Open all';</script>")),
    # A3-F-03: hashes, repository addresses, versions in ids
    ('leak', 'hash-visible', page('<p>built from 0123456789abcdef0123456789abcdef01234567</p>')),
    ('leak', 'hash-aria', page('<button aria-label="0123456789abcdef0123456789abcdef01234567">x</button>')),
    ('leak', 'hash-id', page('<p id="s-0123456789abcdef0123456789abcdef01234567">x</p>')),
    ('leak', 'repository-address', page('<p>see github.com/example/private-notes</p>')),
    ('clean', 'open-repository-address', page('<p>The library is at github.com/momentum-sez/lex for reference.</p>')),
    ('leak', 'id-version-tag', page('<p id="s-main-theorem-v2">x</p>')),
    ('leak', 'id-version-word', page('<p id="s-version-2-result">x</p>')),
    ('warn', 'id-draft', page('<p id="s-draft-result">x</p>')),
    # A3-F-04: no-break spaces from Temml's \text{}, stage labels after a hyphen, percent in TeX
    ('leak', 'text-Phase-2', page('<p>x ' + tex(r'\text{Phase 2}') + '</p>')),
    ('leak', 'text-language-model', page('<p>x ' + tex(r'\text{language model}') + '</p>')),
    ('leak', 'text-pull-request', page('<p>x ' + tex(r'\text{pull request}') + '</p>')),
    ('leak', 'text-attack-heal', page('<p>x ' + tex(r'\text{attack heal}') + '</p>')),
    ('leak', 'post-Wave-3', page('<p>the post-Wave 3 bound</p>')),
    ('leak', 'pre-Phase-2', page('<p>the pre-Phase 2 form</p>')),
    ('warn', 'post-wave-3-lowercase', page('<p>the post-wave 3 bound</p>')),
    ('warn', 'tex-percent', page('<p>x ' + tex(r'87\%') + '</p>')),
    # A3-F-05: Temml keeps one digit after a letter in \mathrm{} and \mathit{}
    ('leak', 'mathrm-letters-digits', page('<p>x ' + tex(r'\mathrm{T15}') + '</p>')),
    ('clean', 'mathrm-subscript', page('<p>x ' + tex(r'\mathrm{M}_{24}') + '</p>')),
    # A3-F-10: ids and formula shapes that are mathematics
    ('clean', 'id-background-2', page('<p id="s-background-2-charge">x</p>')),
    ('clean', 'id-around-4', page('<p id="s-around-4-loops">x</p>')),
    ('warn', 'id-plane-wave-1', page('<p id="s-plane-wave-1-solutions">x</p>')),
    ('warn', 'id-phase-0', page('<p id="s-phase-0-term-vanishes">x</p>')),
    ('warn', 'id-cycle-3', page('<p id="s-hochschild-cycle-3-classes">x</p>')),
    ('clean', 'id-spine', page('<p id="s-spine-of-the-ribbon-graph">x</p>')),
    ('warn', 'visible-spine', page('<p>The spine of the ribbon graph is a deformation retract.</p>')),
    ('warn', 'mtext-P1', page('<p>x ' + tex(r'\text{the projective line P1}') + '</p>')),
    ('warn', 'aria-P1', page('<button aria-label="the projective line P1">x</button>')),
    # A3-F-11: capitals, zero-width characters, letters in other forms
    ('leak', 'all-caps-WAVE-3', page('<p>WAVE 3 settled this</p>')),
    ('leak', 'zero-width-inside-word', page('<p>the led\u200bger shows it</p>')),
    ('leak', 'mathit-word', page('<p>x ' + tex(r'\mathit{ledger}') + '</p>')),
    ('warn', 'mathbf-word', page('<p>x ' + tex(r'\mathbf{audit}') + '</p>')),
    ('warn', 'mathsf-word', page('<p>x ' + tex(r'\mathsf{audit}') + '</p>')),
    ('leak', 'mathrm-Wave-3', page('<p>x ' + tex(r'\mathrm{Wave}\,3') + '</p>')),
    # Cycle 3b (R3-F A4-F-01, -03, -04, -06, -08)
    ('clean', 'long-integer-in-tex', page('<p>x ' + tex(r'|\mathbb{M}|=808017424794512875886459904961710757005754368000000000') + '</p>')),
    ('clean', 'long-integer-in-prose', page('<p>The order is 808017424794512875886459904961710757005754368000000000 exactly.</p>')),
    ('leak', 'rm-unbraced-digits', page('<p>x ' + tex(r'\rm M24') + '</p>')),
    ('leak', 'mathrm-digits-superscript', page('<p>x ' + tex(r'\mathrm{X12}^2') + '</p>')),
    ('leak', 'mathrm-digits-beside-subscript', page('<p>x ' + tex(r'\mathrm{M24}\subset M_{24}') + '</p>')),
    ('clean', 'mathrm-one-digit', page('<p>x ' + tex(r'\mathrm{SO}(3)\times\mathrm{x1}') + '</p>')),
    ('leak', 'svg-data-uri-base64', page('<p><img alt="" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnPjx0ZXh0PmxlZGdlciBUMTI8L3RleHQ+PC9zdmc+"> x</p>')),
    ('leak', 'svg-data-uri-percent', page('<p><img alt="" src="data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%3E%3Ctext%3EWave%203%3C%2Ftext%3E%3C%2Fsvg%3E"> x</p>')),
    ('leak', 'svg-data-uri-css', page('<p>x</p>', "<title>Status page</title><style>p { background: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Ctitle%3Edrawn by claude%3C/title%3E%3C/svg%3E\"); }</style>")),
    ('clean', 'js-template-interpolation', page('<p>x</p><script>var owner = {id: 1}; var s = `<b>${owner.id}</b>`;</script>')),
    ('clean', 'js-comment-ordinary-words', page('<p>x</p><script>/* the owner of the card; commit the change */ var a = 1; // owner keeps focus\n</script>')),
    ('clean', 'js-token-list', page('<p>x</p><script>var stop = ["agent", "prompt"];</script>')),
    ('leak', 'js-prose-string-workflow', page("<p>x</p><script>var note = 'Checked by the ledger';</script>")),
    ('leak', 'name-with-digits', page('<p>prepared with claude8 tools</p>')),
    ('leak', 'uuid', page('<p>run 6627d653-9a29-44e3-8423-caa22e437a3c</p>')),
    ('leak', 'tex-label', page('<p>x ' + tex(r'x').replace('<annotation encoding="application/x-tex">x', '<annotation encoding="application/x-tex">x\\label{ch:thm:main-result}') + '</p>')),
    ('clean', 'tex-label-ordinary', page('<p>x ' + tex(r'x=1').replace('<annotation encoding="application/x-tex">x=1', '<annotation encoding="application/x-tex">\\label{eq:main} x=1') + '</p>')),
    ('warn', 'tex-thin-space-percent', page('<p>x ' + tex(r'87\,\%') + '</p>')),
    ('leak', 'en-dash-stage', page('<p>Wave\u20133 settled this</p>')),
    ('leak', 'id-frontier-engine', page('<p id="s-frontier-engine-result">x</p>')),
    ('warn', 'process-words', page('<p>the snapshot and its provenance</p>')),
    ('leak', 'css-custom-property-string', page('<p>x</p>', '<title>Status page</title><style>:root { --note: "see the ledger"; }</style>')),
    # Cycle 3c (R3-F A5-F-01..04)
    ('leak', 'js-string-inside-interpolation', page("<p>x</p><script>var done = 1; var s = `Checked ${done ? 'by Claude' : ''}`;</script>")),
    ('leak', 'js-nested-string-workflow', page('<p>x</p><script>var a = 1; var s = `x ${a ? "Wave 3 of the ledger" : ""}`;</script>')),
    ('leak', 'js-nested-template', page('<p>x</p><script>var a = 1; var s = `x ${a ? `written by codex` : ""}`;</script>')),
    ('leak', 'svg-data-uri-charset-base64', page('<p><img alt="" src="data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnPjx0ZXh0PmxlZGdlciBUMTI8L3RleHQ+PC9zdmc+"> x</p>')),
    ('leak', 'svg-data-uri-image-set', page('<p>x</p>', "<title>Status page</title><style>p { background-image: image-set(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Ctext%3Ewritten by claude%3C/text%3E%3C/svg%3E\" 1x); }</style>")),
    ('leak', 'svg-data-uri-style-attribute', page("<p style=\"background: url('data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27%3E%3Ctext%3EWave 3%3C/text%3E%3C/svg%3E')\">x</p>")),
    ('leak', 'svg-data-uri-srcset', page('<p><img alt="" srcset="data:image/svg+xml;base64,PHN2Zz48L3N2Zz4= 1x, data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnPjx0ZXh0PmxlZGdlciBUMTI8L3RleHQ+PC9zdmc+ 2x"> x</p>')),
    ('clean', 'mathit-letters-digits', page('<p>x ' + tex(r'\mathit{T15}') + '</p>')),
    ('leak', 'uuid-in-id', page('<p id="s-6627d653-9a29-44e3-8423-caa22e437a3c">x</p>')),
    ('clean', 'data-attribute-token', page('<p data-relation="owner">x</p>')),
    ('clean', 'css-selector-token', page('<p>x</p>', '<title>Status page</title><style>[data-kind="agent"] { color: red; }</style>')),
]
probes = os.environ.get('QH_PRIVATE_PROBES')
skipped = []
if probes and Path(probes).is_file():
    for n, line in enumerate(l.strip() for l in Path(probes).read_text(encoding='utf-8').splitlines()):
        if line:
            FIXTURES.append(('leak', f'private-path-{n + 1}', page(f'<p>{line}</p>')))
else:
    skipped.append('private-path probes (QH_PRIVATE_PROBES not set)')

result = {'folder': folder, 'fixtures': {}}
ok = True
for kind, name, markup in FIXTURES:
    r = audit.run(Build(), markup)
    failed = bool(r['failures'])
    # leak: must fail; clean: must pass with no specific warning; warn: must pass with a specific warning.
    # The stub content has no grid, so the structural 'the grid has 0 rows' warning is always present and ignored.
    specific = [w for w in r['warnings'] if not w.startswith('the grid has')]
    warned = bool(specific)
    good = failed if kind == 'leak' else (not failed and warned) if kind == 'warn' else (not failed and not warned)
    ok = ok and good
    result['fixtures'][name] = {'kind': kind, 'flagged': failed, 'warned': warned, 'as_expected': good, 'failures': r['failures'][:4], 'warnings': specific[:2]}
    print(f"{'PASS' if good else 'FAIL'} {kind:5} {name:26} flagged={failed} warned={warned} {(r['failures'] or specific)[:1]}")
result['skipped'] = skipped
for s in skipped:
    print('SKIP', s)
result['all_as_expected'] = ok
print('ALL AS EXPECTED' if ok else 'NOT ALL AS EXPECTED')
if out:
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=1, ensure_ascii=False)
