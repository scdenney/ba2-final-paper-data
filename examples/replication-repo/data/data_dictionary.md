# Data dictionary — `rodong_sinmun_en_sample.csv`

One row per article; 600 rows. This is the model for *"column-by-column with types, units, examples"*: every column gets a **type**, a one-line **description**, **units** where it is numeric, and an **example** value. Do the same for **every column in the file you analyse — including any new ones you create**.

## `doc_id`
- **Type:** string
- **Description:** Unique article identifier, zero-padded.
- **Example:** `rodong_sinmun_en_0042`

## `text`
- **Type:** string (English)
- **Description:** Cleaned article body, truncated upstream to the first 3,500 characters.
- **Units:** characters (length); free text otherwise.
- **Example:** `"The army and people of the DPRK got more confident…"`

## `date`
- **Type:** string, format `YYYY-MM-DD`
- **Description:** Publication date.
- **Example:** `2018-01-02`

## `year`
- **Type:** integer
- **Description:** Publication year; the grouping variable for this analysis.
- **Values:** 2018, 2019, 2020, 2021.

## `title`
- **Type:** string (English)
- **Description:** Article headline; useful as a filter for topic-specific subsets.
- **Example:** `"Pyongyang Joint Declaration Published"`

## `url`
- **Type:** string
- **Description:** Link to the original article on rodong.rep.kp (often reachable only via the Wayback Machine).

---

## Derived variables (computed in `analysis/analysis.R`, not stored in the CSV)

Document the variables you create even when they live only inside the script. These are this analysis's:

| Variable | Type | Units | Description |
|---|---|---|---|
| `n_words` | integer | content words | Tokens per article after stop-word and non-letter removal. |
| `positive`, `negative` | integer | word counts | Bing-lexicon sentiment-word counts per article. |
| `net_per_100` | float | sentiment words per 100 content words | `(positive − negative) / n_words × 100`; the article-level score plotted in Figure 1. |
| `tf_idf` | float | unitless | Term frequency–inverse document frequency of each word within each year; ranks distinctive vocabulary in Figure 2. |

The output `figures/sentiment_by_year.csv` has one row per year, with `mean_net_per_100`, `median_net_per_100`, and `n_articles`.
