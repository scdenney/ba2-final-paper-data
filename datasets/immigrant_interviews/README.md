# Open-Text Survey Responses on Immigrant Admission (South Korea)

**File:** `immigrant_interviews_sample.csv` — 1,006 responses, ~0.11 MB.

This corpus is the **open-text portion** of a South Korean attitudinal survey on immigration: respondents were asked to articulate, in their own words, what kind of immigrant Korea should admit. The corpus is paired with rich respondent metadata (sex, age cohort, political identification, college attainment), making it ideal for **sentiment-by-subgroup** research designs.

## Note — text is very short

**Median text length is only ~11 characters.** These are 1-2 word phrases ("동포이니까" / "because they are co-ethnic", "유창한 한국어" / "fluent Korean"), not paragraphs. The KNU sentiment dictionary still finds hits in short Korean text, and KLUE BERT can produce embeddings for short responses; design your research question with the response length in mind.

This is an excellent corpus for a research question framed around **short-form sentiment** with a clean experimental-style design (4 subgroup factors with which to slice the sentiment scores).

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `immigrant_interviews_0000` – `immigrant_interviews_1005` |
| `text` | string | Cleaned open-text response (Korean), median ~11 characters |
| `sex` | categorical | `Male` / `Female` (~balanced) |
| `age_cohort` | categorical | `18-29` / `30-39` / `40-49` / `50-59` / `60+` |
| `political_id3` | categorical | `Progressive` / `Centrist` / `Conservative` |
| `college` | categorical | `Some college or more` / `No college` |

## Suggested research questions

1. **Do conservative and progressive respondents articulate measurably different sentiment when describing who Korea should admit?** Apply the KNU sentiment dictionary, then use a Box Plot grouped by `political_id3`.
2. **Do older respondents (60+) carry a more negative tone than younger respondents (18-29)?** Filter to the two extreme age cohorts, apply KNU, then compare via Box Plot.
3. **Are there systematic vocabulary clusters by political identification even at the embedding level?** Embed responses with KLUE BERT, run k-means with k=3, then cross-tab cluster membership against `political_id3`. KLUE BERT can produce embeddings even for very short text.
4. **A methodological reflection question — what happens when you try to fit LDA to this corpus?** Fit a 4-topic LDA, examine the top words per topic, and discuss why the topics look noisy or empty.

## Provenance

Drawn from the `immigrant_interviews` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora).
