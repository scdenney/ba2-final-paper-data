# Kaebyok (Gaebyeok / 開闢) Magazine, 1920-1935

**File:** `kaebyok_sample.csv` — 400 articles, ~2.52 MB.

*Kaebyok* (개벽, "Creation" / "Opening of the New World") was the flagship cultural-nationalist monthly of the colonial era — published by the Cheondogyo (Heavenly Way) religious movement from June 1920 onward. It was the most influential general-interest Korean-language magazine of its time: literary modernism, religious reform, women's rights, education, and (within censorship limits) anti-colonial politics all moved through its pages.

The magazine was forcibly **suspended in August 1926** by the Japanese colonial Government-General. A successor magazine using the same name was revived briefly in 1934-1935 but is editorially distinct.

The corpus has a **multi-year publication gap (1927-1933)** that is a direct artifact of colonial censorship — a rare case where a quantitative text feature (year-by-year article count) exposes a political event.

The sample is stratified across years (proportional), so the 1926 censorship gap is preserved (38 articles from 1926, 17 from 1934, 18 from 1935). Article bodies are truncated to 3,500 characters.

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `kaebyok_0000` – `kaebyok_0399` |
| `text` | string | Cleaned article body (Korean, often mixed with Hanja), truncated to 3,500 characters |
| `issue_date` | string (YYYY-MM-DD) | Issue publication date |
| `year` | integer | Publication year (1920–1926, 1934–1935) |
| `article_num` | integer | Within-issue article sequence number |

## Suggested research questions

1. **Did Kaebyok's editorial sentiment darken in the months leading to the August 1926 suspension?** Apply the KNU sentiment dictionary, then plot mean sentiment by `year`. Caveat: KNU is a contemporary dictionary and may misread colonial-era vocabulary — flag in your write-up.
2. **Are 1934-1935 articles thematically distinct from the 1920-1926 articles?** Fit an 8-topic LDA on the full 400-article sample, then chart topic prevalence by `year`. The successor *Kaebyok* of 1934 was launched in a much harsher political environment.
3. **Do articles cluster by issue-year at all?** Embed articles with KLUE BERT, run hierarchical clustering, then compare the dendrogram to the `year` labels.
4. **What dominant topics characterize the magazine's first five years (1920-1924, the editorially most radical period)?** Filter to those years (~278 articles), fit a 6-topic LDA, then read off the top-words per topic. Look for cultural-nationalism, religious-reform, women's-rights, and literary-modernism strands.

## Provenance

Drawn from the `kaebyok` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) (2,467-article original).
