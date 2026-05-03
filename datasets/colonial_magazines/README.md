# Colonial-Era Korean Magazines (1896-1943)

**File:** `colonial_magazines_sample.csv` — 495 articles, ~2.27 MB.

This corpus is the surviving record of Korean-language print culture under Japanese colonial rule — the magazines through which colonial-era intellectuals, journalists, and writers debated cultural nationalism, modernization, gender, education, and (within censorship limits) politics. It spans almost the entire colonial period, from late-Joseon proto-magazines of the 1890s through to wartime mobilization magazines of the 1940s.

The sample is stratified across **19 magazine titles** with a baseline of ~18 articles per magazine plus a proportional bonus for the four big titles (Kaebyok, Samcheolli, Byeolgeongon, Donggwang). Article bodies are truncated to 3,500 characters (median ~1,800).

**Caveat:** colonial-era Korean writing frequently mixes Hangeul with Hanja (Chinese characters) and uses pre-modern orthography. Modern Korean tokenizers and the KNU sentiment dictionary were not built for this register and may behave unevenly — flag this in your write-up.

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `colonial_magazines_0000` – `colonial_magazines_0494` |
| `text` | string | Cleaned article body (Korean, frequently mixed with Hanja), truncated to 3,500 characters |
| `magazine` | categorical | Magazine title (Korean). 19 values; see data dictionary for English glosses. |
| `year` | integer | Publication year (1896–1943) |
| `article_type` | categorical | Genre label from the source (e.g. 논설 editorial, 시 poem, 소설 fiction). Many values; some `Unknown`. |
| `author` | string | Author name where attributed (mostly Korean, some pen names). `Unknown` for unattributed articles. |
| `title` | string | Article title (Korean) |

## Suggested research questions

1. **Do the 'Big Four' progressive magazines (Kaebyok, Samcheolli, Byeolgeongon, Donggwang) cluster separately from the smaller academic-society magazines?** Filter to a manageable subset, embed with KLUE BERT, run hierarchical clustering, then compare the dendrogram to the `magazine` labels. The Big Four were urban, middle-brow, and politically active; the smaller society magazines are scholarly and reform-oriented. (embeddings + clustering)
2. **How do topics differ between the early colonial period (1896-1919) and the cultural-rule / 'cultural-nationalism' period (1920-1932)?** Bin articles by decade, fit a 10-topic LDA on the full sample, then chart topic prevalence by decade. Look for the appearance of modernist literary topics and women's-rights discourse in the 1920s. (LDA + temporal grouping)
3. **Is sentiment systematically more positive in literary articles (시, 소설) than in editorials (논설)?** Apply the KNU sentiment dictionary, then use a Box Plot grouped by `article_type` (filter to the 3-4 most common types). (sentiment + Box Plot grouping)
4. **Did Samcheolli's tone shift after 1937 (start of the Sino-Japanese War, intensification of Japanese mobilization)?** Filter to magazine == "삼천리", then plot KNU sentiment across years. (sentiment + temporal)

## Provenance

Drawn from the `colonial_magazines` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) — five separate CSVs combined (kaebyok, samcheolli, byeolgeongon, donggwang, and other_magazines for 15 smaller titles), ~15,326 articles in the full source.
