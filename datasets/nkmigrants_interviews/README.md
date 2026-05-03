# Open-Text Survey Responses on North Korean Migrants (South Korea)

**File:** `nkmigrants_interviews_sample.csv` — 6,023 responses, ~0.63 MB.

This corpus is the **open-text portion** of a South Korean attitudinal survey on integration of North Korean migrants (탈북민, often translated as "North Korean defectors" or "North Korean refugees" depending on political framing). Each respondent contributed **three responses** — on hiring, on accepting as a neighbor, and on voting for as a political candidate — yielding 6,023 rows from ~2,000 unique respondents. The corpus is paired with respondent metadata.

## CRITICAL CAVEAT — text is very short

**Median text length is only ~9 characters.** These are 1-2 word phrases (similar to the immigrant_interviews corpus).

- **Suitable for**: sentiment scoring with the KNU dictionary, simple clustering, vocabulary frequency comparisons by `response_type` or by respondent demographics.
- **NOT suitable for**: LDA topic modeling at the response level — documents are too short for word co-occurrence to be meaningful.

If you want to do topic modeling on this corpus, **aggregate responses into 'piles' grouped by `response_type` (and optionally by demographic subgroup)**. For example, concatenate all `hire` responses from progressive respondents into one mega-document, all `hire` responses from conservatives into another, and so on. That preserves both the response-type distinction and the subgroup distinction.

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `nkmigrants_interviews_0000` – `nkmigrants_interviews_6022` |
| `text` | string | Cleaned open-text response (Korean), median ~9 characters |
| `response_type` | categorical | `hire` / `neighbor` / `vote` (which question this response answers) |
| `sex` | categorical | `Male` / `Female` |
| `age_cohorts` | categorical | Age band (e.g. `19-29`, `30s`, `40s`, `50s`, `60+`) |
| `political_id3` | categorical | `Progressive` / `Centrist` / `Conservative` |
| `close_nkmigrants` | categorical | Self-reported social distance from NK migrants — `Close` / `Distant` / `Neither close nor distant` |

## Suggested research questions

1. **Do respondents express more negative sentiment when describing North Korean migrants in the political-candidate (`vote`) frame than in the neighbor (`neighbor`) or hire (`hire`) frames?** Apply the KNU sentiment dictionary, then use a Box Plot grouped by `response_type`. Hypothesis: voting carries higher in-group / out-group stakes than employment or neighborhood. (sentiment + Box Plot grouping by frame)
2. **Does the conservative-progressive sentiment gap differ across the three response frames?** Compute mean KNU sentiment per `political_id3` x `response_type` cell (a 3x3 grid). Visualize as a heat map or grouped bar chart. (sentiment + cross-grouping)
3. **Do respondents who report being socially close to NK migrants write systematically more positive responses than those who report being distant?** Box Plot of KNU sentiment by `close_nkmigrants`, with `response_type` as a facet. (sentiment + grouping by attitudinal proxy)
4. **A methodological reflection question — at the embedding level, are the three response_types distinguishable?** Embed all 6,023 responses with KLUE BERT, run k-means with k=3, then cross-tab cluster membership against `response_type`. (embeddings + cluster validation)

## Provenance

Drawn from the `nkmigrants_interviews` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) (6,027-row original).
