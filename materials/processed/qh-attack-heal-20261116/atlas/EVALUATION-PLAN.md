# Atlas lane: evaluation plan (precommitted before healing)

Scope: the research atlas component of quantum-holography-tracker.html, built by
compiler/build-quantum-holography-status.py. Owned files are listed in CONTRACT.json.
The plan fixes the checks, the pass thresholds and the blockers before any attack is healed.

## Reader tasks under test

| Id | Question the reader must answer | Pass condition |
|---|---|---|
| RT1 | What are the domains, and which named claims in each are established, conditional, scoped negative or remaining? | Each domain card shows label, summary and its claims by name under the four group names. No count, ratio, percentage or progress cue appears. |
| RT2 | What exactly does this claim state, under which hypotheses, with which status? | Statement, supplied status label, status shape, hypotheses (or "None listed"), source statement label when supplied, comparisons and page statement link when supplied. |
| RT3 | What is this claim related to, by which typed relation, in which direction, with which scope? | Every recorded edge into and out of the claim is listed with its label, direction and scope. The drawn graph has exactly these edges. The reader can go to a neighbour and back. |
| RT4 | For a named comparison, what is established, conditional, negative and remaining? | Four lists, always shown; every listed claim carries the matching status. |
| RT5 | In which order should I read, and is that order a dependency chain? | Ordered stages; editorial and dependency-bound paths are labelled differently; a dependency path shows the joining edges; the reader can follow a path stage by stage. |
| RT6 | Can I do RT1 to RT5 with the keyboard alone? | Every control is reachable; focus is visible; selection moves focus to the inspector heading; Escape returns to the index; no trap. |
| RT7 | Can I read the atlas on a phone and on paper? | No horizontal page scroll at 375, 480, 768, 1024, 1400 px; print (A4 and Letter) shows the index, every claim with its relations, comparisons and paths. |
| RT8 | Where is the claim I am looking for? | Index filter by words, domain and status, with a live count. |
| RT9 | Can I share or reopen a view? | #atlas-c-<id> opens that claim on arrival; back and forward restore earlier selections. |

## Implementation invariants

| Id | Invariant | Check |
|---|---|---|
| INV1 | Without atlas.json the page is byte-identical to the unpatched build. | Build baseline and patched candidate without atlas.json; compare sha256. Determinism checked by two baseline builds. |
| INV2 | An invalid atlas.json fails the audit and the page is not written to the root. | One negative unit test per validation rule; builder exit status 1 on an invalid candidate. |
| INV3 | No private field or private-looking string reaches the page. | Unknown keys rejected at every level; audit.FORBIDDEN applied to every string and id; tests for paths, file names, model names, hashes-as-ids. |
| INV4 | Drawn and listed relations equal the data, no more. | Unit test: rendered data-edge set equals edge ids; browser test: SVG path count in the inspector equals the selected claim's in+out edge count after relation filters. |
| INV5 | The atlas computes no percentage, progress or theorem count. | Unit test scans atlas markup outside supplied strings for %, "progress", "complete", "of N" phrasing. |
| INV6 | Zero audit failures, zero TeX errors, no broken anchor, no duplicate id. | Builder audit PASS on the synthetic fixture; browser test checks duplicate ids after inspector render. |
| INV7 | No network, same CSP. | Audit PASS; CSP meta unchanged; grep atlas.js for fetch/XMLHttpRequest/sendBeacon/WebSocket/EventSource/import(. |
| INV8 | Content, essay and foundation files unchanged. | sha256 of all 13 baseline files equals BASELINE.json at the end. |
| INV9 | No console error; no page-level horizontal overflow. | Headless Chrome via CDP at each width, light and dark. |
| INV10 | Reduced motion is respected. | Emulated prefers-reduced-motion: no transition or smooth scroll in atlas code paths. |
| INV11 | Contrast WCAG 2.1 AA for atlas text and marks. | Computed colours in both themes; text pairs at least 4.5:1, marks and lines at least 3:1. |
| INV12 | Status and mathematics fidelity. | Unit test: each rendered status label equals the supplied label; each TeX source appears as a MathML annotation. |

## Commands

    PY=/tmp/qh-tracker-build-20261116-venv/bin/python
    $PY -B -m unittest discover -s compiler/quantum-holography-status/tests -p 'test_atlas.py' -v
    $PY -B compiler/build-quantum-holography-status.py --output <lane>/preview.html --audit-dir <lane>/audit
    $PY -B <lane>/integration/apply_status_patch.py --check   (guard: before/after hashes)
    node compiler/quantum-holography-status/tests/atlas_browser.mjs <candidate preview> <lane>/browser

## Negative cases

Missing required field; unknown key; duplicate id; dangling domain, claim or comparison id; self edge;
duplicate edge; relation with two labels; comparison list that contradicts a status; claim and comparison
membership out of step; dependency path with an unjoined step; private path, file name, model name or
LaTeX label in any string; bad id characters; TeX error.

## Blockers

Any failed check above. Any valid attack of severity 1 to 3 that is not healed or shown invalid.
A live child agent. A visual state not inspected on the current candidate.

## Residuals that may remain outside the stable core

The reviewed atlas.json from the content owner is not yet supplied: production rendering of real data is
root's integration step. Screen-reader output was not observed with a real assistive technology.
Root applies the status.py patch; this lane does not edit status.py.

## Amendments (recorded after the plan was fixed; the checks above stay the acceptance bar)

1. Integration target. Root reported the foundation mount (render(data, ctx) inside [data-atlas-mount]) and
   the interaction isolation (no atlas history writes; qh:navigate, qh:state). INV1 now belongs to the
   foundation mount: without atlas.json the foundation build does not load atlas.py. It is checked as
   composed/c5-noatlas (no atlas section, audit PASS) and by the required worktree build, which equals the
   baseline outside @font-face and is reproducible byte for byte with a fixed SOURCE_DATE_EPOCH.
2. Browser checks. Root's restriction (RESTRICTION.md) suspends every Chrome, DevTools-protocol, headless and
   screenshot run. RT2-RT9, INV4, INV5, INV6 and INV9 (console errors) are checked in jsdom on the composed
   page (tests/atlas.test.cjs) and by Python checks of the built markup (tests/test_atlas.py). INV9 (layout
   overflow), INV10 (reduced motion), INV11 (contrast) and RT7 (narrow and print rendering) need a browser:
   they are not verified in this lane and are stated as residuals. The headless results made before the
   restriction (browser-dev/) are historical and are not counted.
