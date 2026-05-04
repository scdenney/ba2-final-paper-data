# South Korean Newspaper Twitter Posts (2018-2019)

**File:** `kr_newspapers_twitter_sample.csv` — 2,745 tweets, ~0.45 MB.

This corpus is the official Twitter feed of six South Korean newspapers, ideologically labeled as either **left** (Hankyoreh, Kyunghyang) or **right** (Chosun Ilbo, Dong-a, Joongang Ilbo, Hankyung). Each tweet is short — Twitter's 280-character limit, with most well below that — so the unit of analysis is closer to a news headline than a full article.

The corpus is small but **balanced for partisan comparison**: 1,496 tweets from left-leaning outlets vs. 1,249 from right-leaning outlets. It is the only short-form, social-media corpus in the menu.

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `kr_newspapers_twitter_0000` – `kr_newspapers_twitter_2744` |
| `text` | string | Cleaned tweet text (Korean), no URLs |
| `paper_name` | categorical | Newspaper handle: `chosun`, `dongamedia`, `joongangilbo`, `hankyungmedia`, `hanitweet`, `kyunghyang` |
| `created` | string (YYYY-MM-DD) | Tweet date |
| `favoriteCount` | integer | Twitter likes count at scrape time |
| `retweetCount` | integer | Retweets count at scrape time |
| `pol_id` | categorical | Editorial line: `left` (Hankyoreh + Kyunghyang) or `right` (Chosun + Dong-a + Joongang + Hankyung) |

## Suggested research questions

1. **Do left-leaning and right-leaning Korean newspapers tweet about measurably different topics?** Fit a 6- to 8-topic LDA on all 2,745 tweets, then chart topic prevalence by `pol_id`. Hypothesis: the left papers will weight social-issue and labor topics; the right papers will weight national-security and market topics.
2. **Is sentiment systematically more negative in tweets from right-leaning papers (during the Moon administration)?** Apply the KNU sentiment dictionary, then use a Box Plot grouped by `pol_id`. The Moon government was progressive; right-leaning outlets were in regular opposition mode.
3. **What predicts a viral tweet — sentiment, topic, or paper?** Bin `favoriteCount` into high/low (e.g. top quartile vs. rest). Do high-engagement tweets cluster on particular topics or sentiment ranges? Use embeddings or LDA to characterize the high-engagement group.
4. **Caveat method-question: is 38-character text long enough for KLUE BERT embeddings to give meaningful clusters?** Run k-means on KLUE BERT embeddings of the full corpus and compare to a TF-IDF + k-means baseline.

## Provenance

Drawn from the `kr_newspapers` Twitter corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) (2,748-tweet original).
