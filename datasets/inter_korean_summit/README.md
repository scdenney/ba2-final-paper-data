# Inter-Korean Summit Press Coverage (Chosun Ilbo + Hankyoreh, 2000-2018)

**File:** `inter_korean_summit_sample.csv` — 451 articles, ~1.87 MB.

This corpus covers South Korean newspaper coverage of the three inter-Korean leadership summits since 2000:

- **2000 June Summit**: Kim Dae-jung (ROK) — Kim Jong-il (DPRK), Pyongyang.
- **2007 October Summit**: Roh Moo-hyun (ROK) — Kim Jong-il (DPRK), Pyongyang.
- **2018 multi-summit**: Moon Jae-in (ROK) — Kim Jong-un (DPRK), Panmunjom (April), Pyongyang (September), plus the May 26 secret meeting at the northern side of Panmunjom.

The two newspapers sit on opposite ends of the South Korean political spectrum: **Chosun Ilbo** (조선일보) is the country's flagship conservative daily; **Hankyoreh** (한겨레) is its flagship progressive daily. Their coverage of the same summit events is a textbook case of partisan framing.

The sample is **not balanced** — 2018 alone has 396 articles vs. 13 from 2000 and 42 from 2007. That reflects how much more coverage the 2018 summits received in the digital-news era. Treat `year` and `summit_episode` as descriptive metadata rather than balanced grouping factors. Article bodies are truncated to 3,500 characters (median ~1,400, so very few are actually truncated).

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `inter_korean_summit_0000` – `inter_korean_summit_0450` |
| `text` | string | Cleaned article body (Korean), truncated to 3,500 characters |
| `newspaper` | categorical | `Chosun Ilbo` or `Hankyoreh` (English) |
| `year` | integer | `2000`, `2007`, or `2018` |
| `summit_episode` | categorical | `2000_june_summit` / `2007_october_summit` / `2018_multi_summit` |
| `title` | string | Article headline (Korean) |

## Suggested research questions

1. **Did Chosun Ilbo and Hankyoreh frame the 2018 summits in measurably different sentiment registers?** Filter to `year == 2018`, apply the KNU sentiment dictionary, then use a Box Plot grouped by `newspaper`. Hypothesis: Hankyoreh's coverage is more positive about the summit diplomacy, Chosun Ilbo's is more skeptical. (sentiment + Box Plot grouping)
2. **What topics dominate each summit episode?** Fit an 8- to 10-topic LDA on the 451 articles, then chart topic prevalence by `summit_episode`. Expectation: 2000 articles emphasize Sunshine Policy and family reunions; 2007 articles introduce economic cooperation (Kaesong); 2018 articles foreground denuclearization, sanctions, and the US-DPRK Singapore process. (LDA + grouping)
3. **Are partisan framing differences greater at certain summits than others?** Run topic modeling on each year separately (2007 + 2018 only — 2000 has too few articles), then compare the newspaper-prevalence distributions across years. (LDA + cross-year comparison)
4. **Do Hankyoreh and Chosun Ilbo articles cluster together by topic even at the embedding level?** Embed all 396 2018 articles with KLUE BERT, run k-means with k=4-6, then check whether `newspaper` is concentrated in particular clusters. (embeddings + clustering)

## Provenance

Drawn from the `inter_korean_summit` corpus (article-level file) in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora).
