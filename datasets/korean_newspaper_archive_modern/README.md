# Modern-Korean Newspaper Articles, 1920-1952 (Late Colonial + Liberation Era)

**File:** `korean_newspaper_archive_modern_sample.csv` — 2,000 articles, ~4.51 MB.

The Korean Newspaper Archive at the National Institute of Korean History (NIKH) is the largest publicly indexed digital corpus of pre-1953 Korean newspapers. The full archive spans 1883-1952 and contains material in five languages and seven scripts (Modern Korean, Hanmun, Japanese, English; Hangeul, Hanja, mixed, etc.).

This sample is filtered to articles from 1920 onward, written in Modern Korean, and at least 500 characters long. The result is almost all from late-colonial and immediate post-liberation regional newspapers (남선신문, 남조선민보) plus scattered articles from major dailies (매일신보, 조선신문, etc.). The bulk of the pool is 1940s–1950s regional press — a faithful reflection of which Modern Korean long-form articles survive in the archive, not a sampling bias. Article bodies are truncated to 2,000 characters.

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `korean_newspaper_archive_modern_0000` – `korean_newspaper_archive_modern_1999` |
| `text` | string | Cleaned article body (Korean), truncated to 2,000 characters |
| `year` | integer | Publication year (1920–1952) |
| `newspaper` | categorical | Newspaper title (Korean). 14 values; 남조선민보 (~80%) and 마산일보 (~37%) dominate. |
| `title` | string | Article headline (Korean) |
| `url` | string | URL to the original archive entry on the NIKH database |

## Suggested research questions

1. **Do articles from the late colonial period (1940-1945) and the liberation period (1945-1952) differ in topic mix?** Bin articles into the two periods (or four — 1920s, 1930s, 1940s, 1950s), fit an 8-topic LDA on the full sample, then chart topic prevalence by period. Look for the appearance of liberation-era political topics (elections, US Military Government, Korean War). (LDA + temporal grouping)
2. **Is sentiment more negative in articles from the war years (1944-1953)?** Apply the KNU sentiment dictionary, then plot mean sentiment by year. Caveat: KNU is a contemporary dictionary; archaic 1940s vocabulary may be under-detected. (sentiment + temporal trend)
3. **Do the two big regional papers (남조선민보 and 마산일보) cluster separately from the central / wartime papers (매일신보, 조선신문)?** Filter to the four most common newspapers, embed with KLUE BERT, run k-means with k=4, then check whether `newspaper` is concentrated in particular clusters. (embeddings + clustering)
4. **A methodological reflection question — how does KLUE BERT handle archaic / mixed-script pre-1953 Korean?** Embed all 2,000 articles and visualize with t-SNE or UMAP colored by year. (embeddings — model-evaluation reflection)

## Provenance

Drawn from the `korean_newspaper_archive` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) (~364K articles in the full source).
