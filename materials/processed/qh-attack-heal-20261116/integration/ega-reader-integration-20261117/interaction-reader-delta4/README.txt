reader-delta4: the splitter matches element id attributes only (website lead's relay, 2026-11-17).

tools/split-reference.py 1f312cdf... (reader-delta2) -> cd104f4a5dcf458f98290ee21ac4f4fefe47795e84fd6016c0fa06ee845c7637
Patch: split-reference.py-delta2-to-delta4.patch (f05e0506...). Other tools in tools/ are reader-delta2's, byte for byte.
Change: the id pattern was \bid="...", which also matched data-edge-id="..."; it is now (?<![\w-])id="..." (three places).
Effect, same input page: all three output pages byte-identical apart from the map; reference.html map unchanged (604 ids); atlas.html map 5,577 -> 3,133 entries; the 2,444 entries removed are 1,215 distinct data-edge-id values, none an element id; every listed id is an element id and every element id of the parts is kept.
Checks: split checks 12 of 12. Page checks 18 of 19; the one failure (fig-state-line-cap lacks data-qh-figure) is in the old test page built before the foundation's fix, not in the splitter.
Production: as in DEFERRED-REFERENCE.md section 7, with F=.../interaction/reader-delta4. Verify: sh GUARD-SPLITTER-DELTA4.sh --check
reader-delta3 (search) is unchanged. Review: lead-verified only.
