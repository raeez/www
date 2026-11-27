# Native Chrome visual QA, primary account

**Attempt 2 (13:31–13:55 UTC): connected; visual QA of the foundation-lane candidate done.** Read `QA-FINDINGS.md`.

- Connection: `list_connected_browsers` returned one browser ("Browser 1", macOS, local, in use), and
  `tabs_context_mcp(createIfEmpty=true)` created task group 90502873. Exact results are in `CONNECTION-ATTEMPT-2.json`.
- **Prompts needing root or user interaction: none.** No per-site, file-access, script or connection prompt appeared.
  Two refusals are recorded word for word: the extension will not open `file://` URLs, and it will not act on a tab
  still on `chrome://newtab/` ("Can't interact with browser-internal or unparseable URLs. Navigate to a web page
  first."). Enabling `file://` would need Chrome's "Allow access to file URLs", a global permission change, so I served
  the frozen bytes from 127.0.0.1 instead.
- `resize_window` reports success but changes nothing (the viewport stays 1728×997). Exact widths therefore come from a
  plain-HTML iframe harness, `site/frame.html`.
- Result for candidate `b57caa1e`: a large improvement over the baseline in density, navigation and phone reading, but
  not ready. There are three S2 findings: the contents column touching the viewport edge at 1280 px, the inverted
  hierarchy in question cards, and the clipped first formula. There are seven S3 findings.
- The lane rebuilt `preview.html` at 13:37:47 UTC to `15ff3966…`. I compared that build statically only: its CSS
  suggests F2 and F10a are addressed, and F4, F5 and F9 persist.
- Cleanup: both task tabs closed, server stopped, the theme key removed from the throwaway origin. No worktree file was
  touched.
- Files written in attempt 2: `CONNECTION-ATTEMPT-2.json`, `QA-FINDINGS.md`, `shots/` (11 images), frozen copies in
  `candidate/` and `baseline/`, `site/` (serve folder and harness), `server.log`.

Attempt 1's record follows unchanged. Its section "What root needs before a native run can work" is superseded by
attempt 2.

---

## Attempt 1 (12:52–12:56 UTC): not connected

2026-11-16, 12:52–12:56 UTC. Outcome: **no browser is connected to this account.** The stop rule in the assignment
applied, so no visual QA was performed. The machine-readable record is `CONNECTION.json` in this directory.
`BRIEF.txt` and `LAUNCH.json` were already here before I wrote anything: they are root's launch record, and the
brief is the same text as my prompt. I wrote only `CONNECTION.json` and this report.

## Exact tool results

Native Claude-in-Chrome tools were loaded in one ToolSearch call (15 tools, `mcp__claude-in-chrome__*`). Then:

1. `list_connected_browsers` (no input) returned:

   ```
   []
   ```

2. `tabs_context_mcp` with `createIfEmpty: true` returned this error:

   ```
   Browser extension is not connected. Please ensure the Claude browser extension is installed and running (https://claude.ai/chrome), and that you are logged into claude.ai with the same account as Claude Code. If this is your first time connecting to Chrome, you may need to restart Chrome for the installation to take effect. If you continue to experience issues, please report a bug: https://github.com/anthropics/claude-code/issues/new?labels=bug,claude-in-chrome
   ```

There were no retries. No approval or permission prompt appeared, so there is no approval text to report. No tab was
created and none was closed.

## Session

Model `claude-opus-5-5` (from the system prompt); shell `CLAUDE_EFFORT=max`; Claude Code 2.1.325; entrypoint `cli`;
`CLAUDE_CONFIG_DIR` unset, so the default `~/.claude`. This is the primary account, not claude8.

## What the machine shows (read-only checks, 12:55–12:56 UTC)

- Chrome is running (one main process, pid 96969). No other Chromium-family browser is running.
- The Claude extension (`fcoeoabgfenejglbffodgkkbkcdhcgfn`, version 1.0.107) is installed in 20 Chrome profiles.
- Ten native-host processes are running. **All ten are the Claude desktop app's host**
  (`/Applications/Claude.app/Contents/Helpers/chrome-native-host`), started for that extension. **None is the
  Claude Code host** (`~/.claude/chrome/chrome-native-host`).
- Chrome has one Claude Code native-messaging manifest
  (`com.anthropic.claude_code_browser_extension.json`). It names the primary config dir's host, which exists. Its
  mtime, 12:51:54 UTC, is the same second as this session's launch with Chrome enabled (`LAUNCH.json`), so this
  session's own setup very likely wrote it. No Claude Code host process has started since.

My reading: the extension is running but is paired with the desktop app. No instance is registered with the account
this Claude Code session uses, and the extension has not opened the Claude Code host since this session refreshed its
manifest. The tool's own text names the remedies: sign the extension in to claude.ai with this session's account, and
restart Chrome on first install. The restart remedy fits these facts, but I did not test it. Both are login or restart
actions, which this assignment forbids me to take. I did not determine the cause beyond these facts.

## Not done (by the assignment)

- `switch_browser` was not called. By its own description it sends a Connect request to every extension and waits up
  to 2 minutes for a person to click Connect. Root may run it under the principal's authorization while someone is
  at Chrome. `select_browser` does not apply because there is no deviceId.
- No extension login, account change, Chrome restart, permission change, CDP, headless run, browser command line,
  alternate surface, local server or file navigation.
- No edits, staging, commits, pushes, publication or child agents. The worktree status equals the session-start
  snapshot (5 untracked paths, nothing staged).

## Candidate that was to be inspected

`materials/processed/qh-attack-heal-20261116/foundation/preview.html` in the foundation worktree. Its sha256
`b57caa1ee3621dc7d636a42fdaa2e23beee80f5ab9b59b9bd841f1b2100cc045` (2,338,060 bytes) matches VERIFY.md and was the
same at 12:52 and 12:56 UTC. The lane REPORT.md is still partial ("completed after the second verification wave").
This is the lane candidate only; root will supply the composed final candidate later.

## Visual QA status

- **Not performed.** I make no statement about the candidate's rhythm, harmony, balance, proportion, clarity or
  conceptual navigation, at any width or in either theme. No integrated or final QA is claimed.
- The earlier headless screenshots in `foundation/shots` and `foundation/tmp` are development evidence only, per
  RESTRICTION.md. I did not open or use them.
- VERIFY.md's "Required QA that this lane could not perform" items 1–7 remain open in full.

## What root needs before a native run can work

1. A person at Chrome connects an extension instance to the account this Claude Code session uses. That means
   opening the Claude extension in a running profile signed in to claude.ai with that account; per the tool text, a
   Chrome restart may be needed on first install.
2. `list_connected_browsers` should then show a deviceId. If several browsers connect, use `select_browser` with the
   chosen deviceId, or `switch_browser` with someone ready to click Connect.
3. Plan for the next gate now. The candidate is a local file, so opening it natively will likely need either Chrome's
   "Allow access to file URLs" setting for the extension (a permission change) or the page served from localhost,
   which brings up the extension's per-site permission prompt. I did not check either setting. Which route fits
   RESTRICTION.md and the principal's authorization is root's call.
