# Article Log & Recommendation Algorithm

The agent maintains this log to learn what the user finds interesting and tune future article suggestions.

## How to use
Whenever the agent surfaces articles, the user replies with which ones they actually want to read or act on. The agent appends them here with an engagement tag.

## Engagement tags (weights for scoring)
- `acted` — read and changed a position / view (weight 3)
- `saved` — bookmarked / wanted later (weight 2)
- `read` — read it through (weight 1)
- `skipped` — surfaced but ignored (weight 0)
- `disliked` — explicit "don't show me this kind" (weight -2)

## Recommendation algorithm

For each candidate article, compute a relevance score:

```
score =
    Σ over (topics, themes, tickers) of [
        match_count × engagement_weight_of_most_recent_match
    ]
    + boost: +2 if any ticker ∈ holdings.csv
    + boost: +1 if any ticker ∈ open_orders.md or watchlist.md
    + boost: +1 if theme matches current market_view.md thesis
    - penalty: -1 if same source as any of the last 3 surfaced articles
    - penalty: -3 if any topic is on the disliked list
```

Use last N=30 logged articles for the matching window. Surface the top 3-5 candidates per request.

## Disliked themes
(none yet — add when user says "don't show me X")

## Log
Format:
```
- YYYY-MM-DD | engagement | tickers | themes,topics | source | title | url
```

---

(no entries yet — first surfacing in this session)
