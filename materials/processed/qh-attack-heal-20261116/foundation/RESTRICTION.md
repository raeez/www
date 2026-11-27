# Browser restriction (from root, received during the lane)

Root's safety correction: an earlier Browser Use URL-policy refusal prohibited obtaining tracker-page browser
inspection through raw CDP, browser commands, alternate browser surfaces or indirect execution. That refusal is
binding for this task.

Effect on this lane, from the moment it was received:

- No further headless Chrome, CDP, preview, screenshot or print-to-PDF runs of the tracker page. No alternate
  browser surface (including the Chrome extension).
- No lane-owned Chrome or harness process was running when the correction arrived (checked with `ps`).
- Artifacts produced earlier are preserved unchanged: `baseline/measure.json`, `baseline/contract.json`,
  `baseline/print*`, `tmp/*` results, `shots/*`, and the attackers' scratch evidence under `attack/A1`, `attack/A2`.
- Those browser results are development evidence only. They do not count as accepted visual QA, for the
  baseline or for the candidate. Accepted visual, print, keyboard and console QA is a stated requirement for root.
- Verification continues with non-browser checks: the build and its audit, the static fidelity check
  (`tools/fidelity.py`), static DOM-structure contract checks (`tools/contract_static.py`), the atlas and
  hypotheses fixture tests, CSS rule inspection, and the patch tools. jsdom is not installed in this tree or in
  the integration tree, and no dependency is installed for it, so status.js behaviour cannot be exercised here.
- The tools `tools/run.mjs`, `tools/cdp.mjs` and the scenarios that drive Chrome are kept as artifacts and are not
  run again by this lane.
- Reviewers: no reviewer was active when the correction arrived (A1 and A2 had returned). Every reviewer launched
  or resumed afterwards receives this restriction verbatim and works read-only without any browser.

## Forwarding record

- Second wave (R-A1 and R-A2, resumed): each received the restriction verbatim, with explicit instructions not to
  launch any browser surface or rerun earlier browser scripts. Both reported that they used none.
- Root's scope message (the principal's words on rhythm, harmony, balance, proportion, communication and
  visualization) and the principal's five-failures rule were forwarded verbatim and whole, with the brief whole,
  to the third-wave reviewers (A3, a fresh design-lens attacker, and R-A2, resumed), together with this restriction.
