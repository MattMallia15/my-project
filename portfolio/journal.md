# Decision Journal

Append every meaningful decision (taken or deliberately deferred). Format:

```
## YYYY-MM-DD — ACTION TICKER
Size: N shares (~$X, Y% of book)
Price: $XX.XX
Reason: <one or two sentences>
Invalidates: <what would tell me I was wrong>
Tag: value | tactical | rebalance | macro | trim | exit
```

---

## 2026-06-17 — Baseline captured
Starting positions and open orders recorded in `holdings.csv` and `open_orders.md`. Strategy codified in `strategy.md`. Current market view in `market_view.md`. No new actions today.

---

## 2026-06-18 — AMEND SELL ACN (limit $215 → $170)
Size: 25 shares (~$3,900 at $156 spot, ~3.8% of book)
Price: SELL 25 @ $170, GTC
Reason: Q3 FY26 print — revenue miss $18.7B vs $18.93B est, EPS beat but bookings DOWN YoY ($19.3B vs $19.7B), FY26 guide cut to 3-4% local-currency growth from 4-6%. Original "AI-services beneficiary" thesis falsified by guide cut. Stock -6% net (intraday low $156, recovered from -16% pre-market). $170 is +9% above spot, ~$3 above today's intraday high — patient exit targeting a recovery toward no-news pricing without needing fundamentals to improve.
Invalidates:
- Order doesn't fill within 60-90 days and ACN drifts in $145-160 range → re-evaluate; either lower the limit or accept hold-longer.
- Bookings re-accelerate in Q4 FY26 print (Sept 2026) → re-tag as value rather than exit.
- Stock breaks $145 with no positive catalyst → consider market exit; thesis fully broken.
Tag: exit (thesis falsified)

---

## 2026-06-18 — AMEND SELL WBD (limit $29 → $30)
Size: 170 shares (~$4,590 at $27 spot, ~4.2% of book)
Price: SELL 170 @ $30, GTC
Reason: Confirmed Paramount Skydance takeout at $31 cash + $0.25/qtr ticking fee post-Oct-1 2026. $30 limit sits below takeout but captures most of the arb if deal-risk discount narrows. Spread at $30 vs spot $27 = ~$3 (10%); at takeout $31 = ~$1 (3.3%) remaining give-up. Want more of the deal value than $29 would have captured. Willing to wait for regulatory milestones to narrow the spread; if they don't, hold to close for full $31 + ticking.
Invalidates:
- Deal-break (Paramount walks, antitrust kills it) → market gap-down likely; cancel limit, evaluate position from a stub-value basis.
- Higher counter-bid emerges (unlikely but not zero) → raise limit accordingly.
- Spread doesn't narrow within 90 days → accept holding to close for the full $31.
Tag: rebalance (merger-arb event trade)
