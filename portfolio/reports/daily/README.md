# Daily Market Reports

Two variants live here, both written as Markdown:

- **Pre-market reports** → `YYYY-MM-DD-premarket.md`. Generated BEFORE the US open on request ("pre-market report" / "morning brief"). Covers what happened since the last close (overnight + weekend if Monday), futures direction, key pre-market movers in the user's book, today's session catalysts, and open decisions.
- **End-of-day reports** → `YYYY-MM-DD.md`. Generated AFTER the US close ("EOD report" / "daily wrap"). Covers the day's actual moves, news drivers, portfolio P&L moves, look-ahead, and open decisions.

**The agent must always check today's date before generating, and pull live prices via WebSearch.** Don't assume the date from prior context — confirm fresh. If the user says the date is wrong, regenerate immediately.

## Template: Pre-market report

```markdown
# Pre-Market Report — Weekday, DD Month YYYY

*Generated before US open. Last regular session: [last open day]. [Note any holidays or short sessions.]*

---

## 1. Pre-market top-line
[Table: S&P / Dow / Nasdaq futures, oil (Brent + WTI), any other relevant: DXY, key bond yields. Move % since last close.]

[1-2 sentence story going in.]

---

## 2. What happened since last close
[Bullets: overnight news, weekend if Mon, geopolitical, macro releases that landed in non-US hours. Focus on what materially moves the user's book.]

---

## 3. Pre-market movers

### Big moves elsewhere (context, not in book)
[Brief bullets — only if interesting context]

### Movers IN the user's book
[Table: holding, pre-market move, read]

---

## 4. Your portfolio: what to watch today
[Live risk items going into the session.]
[Open orders status table.]

---

## 5. This week's calendar (rest of week)
[Compact table: date, event, why it matters.]

---

## 6. Open decisions still hanging
[Numbered list from company_notes.csv next_step column.]

---

## 7. End-of-day cash policy check
[FX cash to convert? List any.]

---

*Sources cross-referenced this session: [list].*
```

## Template: End-of-day report

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
