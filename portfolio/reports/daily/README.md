# Daily Market Reports

End-of-day reports written here as `YYYY-MM-DD.md`. The agent generates these when the user asks "give me today's daily report" or "do the EOD" at session close. The user can also request it the next morning.

## Template structure

```markdown
# Daily Market Report — Weekday, DD Month YYYY

*Generated end of session. [Note any holiday/short session.]*

---

## 1. Top-line market
[Table: S&P 500, Nasdaq, Dow, Russell 2000 — close, % change, notes]

[1-2 sentences on the story of the day. Top movers if relevant.]

---

## 2. Major news drivers
[Bullet headlines by category: macro, geopolitics, earnings, analyst actions. Only items that materially affect the user's book or the broader market context. No filler.]

---

## 3. Your portfolio today

### Holdings — material moves & news
[Table: holding, action today, notes — only rows with real content; "Quiet" is fine when nothing meaningful happened]

### Open orders status
[Table: ticker, order, spot, status]

---

## 4. What to expect tomorrow & next week
[Earnings + macro calendar items relevant to current positions. Time-specific if known.]

---

## 5. Open decisions still hanging
[Numbered list of decisions from company_notes.csv `next_step` column that are still open. Updated each report.]

---

## 6. End-of-day cash policy
[Per the FX rule: confirm whether any USD/foreign cash needs conversion. List any pending.]

---

*Sources cross-referenced this session: [list].*
```

## Rules

- Generate at session close (US 4pm ET) or on request.
- Pull live prices via WebSearch/WebFetch — never quote from memory.
- Tag any stale/unverifiable data explicitly as "unverified" in the table.
- Keep tables compact; bullets for analysis.
- Always end with the open-decisions list — that's the action layer.
