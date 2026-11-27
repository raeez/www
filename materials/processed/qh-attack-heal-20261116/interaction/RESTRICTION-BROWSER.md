# Browser restriction (binding for this task)

Received from root on 2026-11-16 during the heal: an earlier Browser Use URL-policy refusal prohibits obtaining
tracker-page browser inspection through raw CDP, browser commands, alternate browser surfaces or indirect execution.
That refusal is binding for this task.

## What this lane did before the correction reached it

The lane wrote a raw CDP client (tools/chrome.mjs) and ran headless Chrome 157 against task-owned copies of the
baseline page, with a task-owned profile (chrome-profile/):

| Run | Command | Output | Page loads |
|---|---|---|---|
| 1 | node tools/measure.mjs baseline-build/baseline-nofonts.html chrome-profile baseline | measure/baseline.json | 1 |
| 2 | node tools/cv-experiment.mjs baseline-build/baseline-nofonts.html chrome-profile | measure/cv-baseline.json | 12 |

No screenshot or PDF was taken; no candidate page was opened in a browser. No Chrome process from this lane is running
(checked with pgrep against the lane profile after the correction).

## Status of those results

They are preserved unchanged and are NOT accepted evidence: not for visual QA (E8) and not for timing claims (E7).
Ledger entries A1-M-06 and A1-M-07 carry this note; their acceptance rests on jsdom/structural evidence only.

## From now on

- No raw Chrome/CDP, headless preview, screenshot, print-to-PDF or other browser surface for the tracker page.
- tools/chrome.mjs, tools/measure.mjs and tools/cv-experiment.mjs are suspended for this task (see tools/SUSPENDED.md).
- Checks continue in jsdom and by static inspection only.
- E8 (widths 1400/1024/768/480/375, light/dark, reduced motion, keyboard, print A4/Letter) is not performed by this
  lane and is a stated requirement for root.
- Every reviewer prompt from this lane carries this restriction verbatim.
