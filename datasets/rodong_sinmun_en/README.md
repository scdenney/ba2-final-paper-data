# Rodong Sinmun (English Edition), 2018-2021

**File:** `rodong_sinmun_en_sample.csv` — 600 articles, ~0.91 MB.

*Rodong Sinmun* (로동신문, "Workers' Newspaper") is the official organ of the Workers' Party of Korea — the most authoritative public-facing voice of the North Korean state. The English edition is a curated subset prepared explicitly for international audiences: it tracks the regime's preferred framing of high-stakes diplomacy (the 2018-2019 US-DPRK process, the 2020 pandemic, the 2021 sanctions environment).

The sample window 2018-01 through 2021-12 covers:

- **2018**: Year of summit diplomacy — Singapore (June, Trump-Kim), Panmunjom and Pyongyang (Moon-Kim), inter-Korean opening.
- **2019**: Hanoi summit failure (February), end-of-year crisis, North Korean rhetoric hardens.
- **2020**: Border closure and pandemic isolationism, total breakdown of inter-Korean and US-DPRK channels.
- **2021**: Eighth Party Congress, "frontal breakthrough" line, missile testing resumes.

The sample is stratified by year (proportional): roughly 178 / 167 / 144 / 111 articles for 2018 / 2019 / 2020 / 2021. Article bodies are truncated to 3,500 characters.

## CRITICAL CAVEAT — text is in ENGLISH, not Korean

This is the only corpus in the menu in **English**. Implications:

- **The KNU sentiment dictionary will not work** — it is a Korean-language dictionary. To do sentiment analysis on this corpus, use a different approach:
  - VADER (rule-based English sentiment, freely available)
  - A small custom dictionary built from regime-specific vocabulary (e.g. tag the words "imperialist", "provocation", "criminal" as negative; "victory", "achievement", "great" as positive)
  - Or skip sentiment and choose a non-sentiment method (clustering, embeddings, LDA — all work fine on English)
- **KLUE BERT (Korean BERT) is also wrong for this corpus.** If you want embeddings, use an English BERT variant (e.g. `bert-base-uncased`) or the multilingual XLM-R.
- Topic modeling (LDA), TF-IDF clustering, and English BERT embeddings all work as normal.

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `rodong_sinmun_en_0000` – `rodong_sinmun_en_0599` |
| `text` | string | Cleaned article body (English), truncated to 3,500 characters |
| `date` | string (YYYY-MM-DD) | Article date |
| `year` | integer | `2018` / `2019` / `2020` / `2021` |
| `title` | string | Article headline (English) |
| `url` | string | URL to the original Rodong Sinmun page |

## Suggested research questions

1. **What topics dominate each year of the 2018-2021 window?** Fit an 8- to 10-topic LDA on all 600 articles, then chart topic prevalence by `year`. Hypothesis: 2018 articles emphasize summit diplomacy; 2019-2020 articles introduce pandemic and isolation themes; 2021 articles return to militancy.
2. **Did the regime's English-language rhetoric harden after the February 2019 Hanoi summit failure?** Build a small custom sentiment dictionary (regime-specific positive / negative words), then compare pre-Hanoi (2018 + Jan-Feb 2019) vs. post-Hanoi (Mar 2019 onward) mean sentiment.
3. **Do articles cluster cleanly by year at the embedding level?** Embed articles with English BERT (or multilingual XLM-R), run k-means with k=4, then check whether `year` is concentrated in particular clusters.
4. **What is the dominant rhetorical 'frame' in articles about the US and South Korea, and how does it differ?** Filter articles whose `title` mentions "U.S." vs. those whose title mentions "south Korea", then run topic modeling on each subset separately and compare top-words.

## Provenance

Drawn from the `rodong_sinmun` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) (9,797-article original, 2018-01-02 to 2022-06-03).
