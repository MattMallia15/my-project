# Monthly Portfolio Review Reports

Written here as `YYYY-MM.md` on or after month-end. The agent produces this when the user asks "give me the monthly" or "do the month review." Significantly deeper than the daily — one full section per holding plus portfolio-level analysis.

## Template structure

```markdown
# Monthly Portfolio Review — Month YYYY

*Generated [date]. Reporting period: 1-N of [Month] YYYY.*

---

## 1. Portfolio summary

| Metric | This month | Last month | Δ |
|---|---|---|---|
| Total NAV (USD/EUR base) | | | |
| Cash deployed (DCA) | | | |
| Decisions logged | | | |
| Trades executed | | | |
| Open orders | | | |
| Monthly P&L (TWR) | | | |
| YTD P&L (TWR) | | | |

---

## 2. Asset allocation snapshot

[Table: by class — equity single-name, equity ETF/index, bonds, commodities, cash]
[Table: by region — US, Europe ex-UK, UK, Asia ex-Japan, Japan, ANZ, EM, Other]
[Table: by currency — economic exposure look-through]

Flag any drift past strategy caps. List the deltas vs target allocation.

---

## 3. Position-by-position review

For EVERY holding in holdings.csv, produce this block:

### TICKER (Account)
**Position:** N shares · MV $X · Y% of NAV
**Cost basis:** $X (avg, opened [date])
**MTD P&L:** ±X%
**YTD P&L:** ±X%
**Thesis status:** Intact / Wounded / Falsified / Re-anchored / Tactical-tagged

**Original thesis (one line):** [from journal.md or stated by user]

**What changed this month:**
- News events
- Earnings or guide changes
- Analyst actions
- Position adjustments

**Strategy alignment:**
- Passes value gates? Y/N (PE, EV/EBITDA, FCF, debt/equity, Altman)
- Sector / single-name caps OK?
- Profitability gate? Y/N (or tactical-tagged exception)

**Decision for next month:** Hold / Trim / Add / Re-evaluate / Exit
[with specific price or condition if applicable]

---

## 4. Strategy & view check

- Rules in strategy.md violated this month?
- Has market_view.md played out as expected? What's been falsified/validated?
- Blanks in strategy.md still unfilled?
- Any drift in tactical vs value allocation?

---

## 5. Open decisions outstanding

[Filtered list from company_notes.csv where `next_step` is non-empty.]

---

## 6. Plan for next month

- Specific actions to take (with dates if known)
- Triggers to watch (earnings, macro, regulatory)
- Cash to deploy (DCA + any freed capital from trims/exits)
- Watchlist re-entries that may activate

---

## 7. Lessons learned

- Decisions that worked / didn't work — and why
- Any rule updates that should go into strategy.md
- Anything that surprised you about your own behavior (anchoring, chasing, holding too long, cutting too quickly)

---

*Sources cross-referenced this session: [list].*
```

## Rules

- Run on or after month-end (last trading day of month, or by 3rd of next month).
- Pull fresh prices for every holding — never quote from memory.
- One section per holding, no exceptions.
- The "lessons learned" section is the one that compounds over time — keep it honest.
- After generating, regenerate `company_notes.xlsx` if any rows were added.
