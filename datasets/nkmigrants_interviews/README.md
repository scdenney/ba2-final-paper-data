# Open-Text Survey Responses on North Korean Migrants (South Korea)

**File:** `nkmigrants_interviews_sample.csv` — 6,023 responses, ~0.63 MB.

This corpus is the **open-text portion** of a South Korean attitudinal survey on integration of North Korean migrants (탈북민, often translated as "North Korean defectors" or "North Korean refugees" depending on political framing). Each respondent contributed **three responses** — on hiring, on accepting as a neighbor, and on voting for as a political candidate — yielding 6,023 rows from ~2,000 unique respondents. The corpus is paired with respondent metadata.

## Note — text is very short

**Median text length is only ~9 characters.** These are 1-2 word phrases (similar to the immigrant_interviews corpus). The KNU sentiment dictionary still finds hits, and KLUE BERT can produce embeddings even for short responses; design your research question with the response length in mind.

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

1. **Do respondents express more negative sentiment when describing North Korean migrants in the political-candidate (`vote`) frame than in the neighbor (`neighbor`) or hire (`hire`) frames?** Apply the KNU sentiment dictionary, then use a Box Plot grouped by `response_type`. Hypothesis: voting carries higher in-group / out-group stakes than employment or neighborhood.
2. **Does the conservative-progressive sentiment gap differ across the three response frames?** Compute mean KNU sentiment per `political_id3` x `response_type` cell (a 3x3 grid). Visualize as a heat map or grouped bar chart.
3. **Do respondents who report being socially close to NK migrants write systematically more positive responses than those who report being distant?** Box Plot of KNU sentiment by `close_nkmigrants`, with `response_type` as a facet.
4. **A methodological reflection question — at the embedding level, are the three response_types distinguishable?** Embed all 6,023 responses with KLUE BERT, run k-means with k=3, then cross-tab cluster membership against `response_type`.

## Provenance

This is **not** a scraped or curated public corpus. It is the open-text portion of a South Korean public-opinion survey designed and fielded by your instructor and a co-author for a peer-reviewed study.

- **Collected:** August–September 2021, South Korea (N ≈ 2,009 respondents × 3 tasks = 6,027 responses; sample here is 6,023 after dropping rows with missing text)
- **Original analysis:** Denney, S. & Green, C. K. (2024). "Public attitudes towards co-ethnic migrant integration: evidence from South Korea." *Journal of Ethnic and Migration Studies*, 50(8), 1998–2022. <https://doi.org/10.1080/1369183X.2023.2286207>
- **Survey design:** The published article (pp. 2006–2007) describes the conjoint experiment — what migrant attributes were varied (education, occupation, age, political history, skill match, time in South Korea), and how each respondent completed three judgment tasks (vote / hire / neighbor). The open-text responses in this corpus are the *post-task* explanations respondents wrote to justify each judgment. Read the paper before designing your research question.

If you choose this corpus, cite **both** the dataset (this repository) and the source paper. The full survey instrument and the paper PDF are available in the source corpus at [`scdenney/nlp_corpora`](https://github.com/scdenney/nlp_corpora/tree/main/data/nkmigrants_interviews).
