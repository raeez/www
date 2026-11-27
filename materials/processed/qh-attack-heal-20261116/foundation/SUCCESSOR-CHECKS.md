# Foundation lane: integration checks on root's composed current preview

Input (read only): `/tmp/programme-public-current-successor-20261116/composed/`, for layout and testing pending
source-fidelity seals. Hashes as in its VALIDATION.json: content.json `ec6864c4e792cc8a9fd511c4be4f87837e39c73cda1006275bcc0df7480991fd`,
atlas.json `90a877c84798530bda9375d3e13c6b4586f9ffb96ca38546d5011e5998b9b848`, essay.md
`798cca686a8a5ccb7c1e3451fdccddcb7cdb94c87705296f81e41e87bc149ae4`.
Renderer: the frozen review set (worktree producer, patch `695ff9a8…`), unchanged. The atlas lane's renderer is not
in this tree, so the lane's test-only stub draws the atlas. No fonts. Command:
`P -B L/tests/successor/successor_checks.py` (writes only to `L/tests/successor/out/`; full results in
`successor-frozen-checks.json`).

| Step | Check | Result |
|---|---|---|
| 2 | Build and audit | 0 TeX errors (2923 formulas). Audit: 3 failures, all content: plain-text symbols outside TeX that the page audit reads as internal identifiers: "T2" ("detects the T2 coordinate") and "E3" twice ("A bare exterior E3 algebra has no coupling parameter"). Remedy: the content owner writes them in TeX (`\(T_2\)`, `\(E_3\)`) |
| 3 | Completeness | FAIL: fields the frozen renderer does not show: top-level `orientation` (title, 4 paragraphs, programme families grouping the 20 families), `as_of_utc` (13:50 UTC evidence boundary), `scientific_atlas` (pointer to atlas.json); `summary` on the 9 principal results; `atlasClaimId` on 29 statements (25 related, 3 family, 1 question; all resolve to atlas claims). Every other field, statement, status (including 1 'refuted form'), hypotheses list (29), card, family, cell, definition and glossary entry passes |
| 4 | Original stable anchors | ALL PASS: 428/428 of the 11:20 page; 117 ids added (98 statement anchors now explicit, the atlas and the contents); one anchored statement changes status: `s-decisive-centre-objectwise-coherence` checked -> conditional (for the content owner to confirm) |
| 5 | Atlas presence (stub) | domains shown 9, claims addressed 714; edges 83, comparisons 63, reading paths 22 absent with the stub: the atlas lane's renderer must draw them |
| 6 | Static DOM contract | ALL PASS |
| 8 | External gate | 0 hits; no internal path or process word |

Follow-up the renderer needs for this payload (foundation lane; to be delivered as a separate guarded follow-up on
top of the frozen review set, not by altering it): show `orientation` as its own part (paragraphs and the programme
families, each linking its member families), the principal `summary`, the `as_of_utc` time in the as-of line, a
visible atlas link for `atlasClaimId` once the atlas lane's claim anchors are agreed (CONTRACT.json proposal), and
validate `scientific_atlas` against atlas.json; extend tools/completeness.py to these fields.

## Second run: the regenerated composed preview, both producers

Root regenerated the preview with the content owner's status-language change to `/status_key`: content.json
`967de4d7a452faaf0b1ac3fb00e440a8c1b6c5670620b75e52e536f09afbd5b6`, atlas.json
`9acebb93b2fdd2f4ac070bf87024fc17e2e6fcb5f903e7cfe73b48d51be18682`, essay.md unchanged (hashes as in its VALIDATION.json).

| Producer | Completeness | Anchors | Contract | Gate | Audit |
|---|---|---|---|---|---|
| worktree (695ff9a8 + F1) | FAIL: the 9 summaries, the orientation part and the as-of time are not shown; 0 of 29 atlas links | 428/428 | PASS | clean | 3 content failures (T2, E3) |
| follow-up (+ F2) | ALL PASS: every field shown; 29 of 29 statements link to their atlas claim (stub anchors) | 428/428 | PASS | clean | the same 3 content failures |

With F1 the status-key label notes disappear: the content's status_key and the page now use the same words (Established,
Remaining, Scoped negative, ...). Atlas presence with the stub: domains shown 9, claims addressed 714; edges, comparisons and
reading paths are the atlas lane's renderer's. Outputs: `L/tests/successor/out/successor-{frozen,followup}-checks.json` and the
two pages beside them (the file named 'frozen' holds this second run, made with the worktree producer, 695ff9a8 + F1; the first
run's results are the table above).

## Third run: the current composed preview, after the F2 heals

The preview changed again (content.json `89c382de6ad86ad51f90299b06bfe48b8756186b58c4d0b92a942ce70cb7cd1b`, atlas.json
`f02f29ecaf761b7f994b131604612bc400cf624345241fcd7bf39efde4beac31`, essay.md `d10a1cf8…`; its VALIDATION.json lists no
pending owner seals). With the follow-up producer (+ F2, healed after A3's check): completeness ALL PASS (29 of 29 atlas
links), anchors 428/428, static contract ALL PASS, gate clean, 0 TeX errors; the same 3 content audit failures (T2, E3).

## Fourth run: the current composed preview (still in delta review)

content.json `6d8d82057edbc732e260972470f299f8c9916216311729ac81c69331b44891bd`, atlas.json
`0d465754715a930209c6c0ae2d9b30f9cb345116ff57954a748f8e0331ddb872`, essay.md `f2c74728…`; its VALIDATION.json lists two
pending owner seals (operations and binary-centres fidelity corrections), so it is not the sealed snapshot. With the
follow-up producer (+ F2): completeness ALL PASS (29 of 29 atlas links), anchors 428/428 (one anchored statement changes
status, for the content owner to confirm), static contract ALL PASS, gate clean, 0 TeX errors; the same 3 content audit
failures (T2, E3). Root's sealed snapshot is the input for the final run (`P -B L/tests/successor/successor_checks.py <folder>
--src L/followup/src/compiler/quantum-holography-status`, after F1 and F2 are applied in the composed tree simply drop --src).
