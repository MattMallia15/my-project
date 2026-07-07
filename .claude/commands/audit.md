---
description: Spawn the flask-route-auditor to audit routes or answer follow-up questions about them.
---

Spawn the `flask-route-auditor` subagent with the following user query:

$ARGUMENTS

If `$ARGUMENTS` is empty, run a full audit of `/home/user/my-project/app.py`.

If it's a follow-up question (e.g. "which finding is highest ROI to fix first?", "explain the CSRF one", "show me the exact fix for the DELETE endpoint"), pass it through as-is — the auditor will re-read what it needs and answer using its own report format where applicable.

Do NOT summarize or filter the auditor's reply. Paste it back verbatim so the user sees the raw agent output, then add one short line at the end noting how many tool calls it made and how long it took.
