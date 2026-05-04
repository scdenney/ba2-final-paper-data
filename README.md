# BA2 Digital Korea — Final Paper Dataset Menu

Curated 11-corpus menu for the BA2 Digital Korea final research paper. Pick one corpus and write a 2,500–6,000-word research paper. See the [Final Paper page](https://scdenney.github.io/ba2-digital-korea/final-paper/) on the course site for the brief, rubric, and submission details.

---

## Dataset menu

| # | Dataset | Rows | Best for |
|---:|---|---:|---|
| 1 | [Authoritarian-era presidential speeches](datasets/authoritarian_speeches/) | 600 | Political rhetoric under dictatorship; sentiment + grouping by `president` |
| 2 | [Inter-Korean summit coverage](datasets/inter_korean_summit/) | 451 | Comparative media framing (Chosun vs. Hankyoreh) across the 2000/2007/2018 summits |
| 3 | [Colonial magazines (multi-title)](datasets/colonial_magazines/) | 495 | Colonial-period intellectual debates across 19 magazines; LDA across magazine type |
| 4 | [*Kaebyok* (single-title)](datasets/kaebyok/) | 400 | Single-magazine diachronic analysis 1920–1935; the 1926 censorship gap |
| 5 | [Korean newspapers (Twitter)](datasets/kr_newspapers_twitter/) | 2,745 | Comparative outlet ideology x engagement, 6 outlets in 2017 |
| 6 | [KPoEM (Korean poems)](datasets/kpoem/) | 615 | Sentiment / emotion analysis on a labeled corpus (44-category KOTE labels) |
| 7 | [Immigrant interviews (open-text)](datasets/immigrant_interviews/) | 1,006 | Short-form sentiment / clustering with subgroup metadata (sex, age, political ID, college) |
| 8 | [NK migrants interviews (open-text)](datasets/nkmigrants_interviews/) | 6,023 | Short-form sentiment / clustering by frame (hire / neighbor / vote) and demographics |
| 9 | [Korean newspaper archive (modern slice)](datasets/korean_newspaper_archive_modern/) | 2,000 | Diachronic / cross-newspaper analysis of the late-colonial / liberation-era press |
| 10 | [*Rodong Sinmun* (English)](datasets/rodong_sinmun_en/) | 600 | Temporal clustering across diplomatic crises 2018–2021 (English text) |
| 11 | [NIKH high-school history textbooks](datasets/nikh_textbooks_hs/) | 21 | Authoritarian vs. Democratic curriculum comparison; diachronic textbook analysis 1973–2016 |

Each dataset folder contains a `README.md` (corpus background, columns, suggested research questions), a `data_dictionary.md` (column-by-column reference), and the `*_sample.csv` file ready to load into Orange Data Mining or R.

---

## Caveats — read before picking

Some corpora have method-compatibility constraints. Pick deliberately, not by accident.

- **#10 *Rodong Sinmun* is English-only.** The KNU sentiment dictionary and KLUE BERT (the Korean embedding model) will not apply. If you choose this corpus, use a different sentiment approach (e.g. VADER, a custom English lexicon) or a non-sentiment method (LDA or k-means clustering both work on English).
- **#3 Colonial magazines uses Hanmun-mixed pre-modern Korean** in places. Kiwi (the morphological analyzer in this course's preprocessing scripts) was trained on contemporary Korean and tokenizes pre-modern / Hanmun-heavy text less cleanly. KNU and KLUE BERT will likewise be noisy on this register. The corpus is interesting precisely because of these challenges — treat tokenization limitations as a methodological reflection point in your data and methods section.
- **#4 *Kaebyok*** has the same caveat to a lesser degree (single-title, mostly modern Korean but with some Hanmun).
- **#11 NIKH high-school textbooks is small (21 books) and is a textbook corpus, not contemporary press.** With only 21 documents, sample-size constraints limit the granularity of any per-era comparison; document this in your design. Some books in the H-series come from cleaned OCR rather than digital text, so expect occasional residual noise.
- **Sample balance varies.** Perfectly balanced for Box Plot grouping: #1 (200 speeches per president). Roughly balanced: #3, #4, #6. Imbalanced (faithful to source): #2 (heavily 2018 summit), #5 (left-leaning slightly larger), #9 (heavily 1940s–1950s, one newspaper dominates ~80% of the pool), #10 (year-proportional — 2018 dominates), #11 (Democratic era is 14 books vs. 7 Authoritarian, reflecting the source distribution). For an imbalanced corpus, consider filtering to a balanced sub-sample before running comparisons; document the choice in your write-up.

---

## Off-menu corpora

If you want to use a different corpus from [`scdenney/nlp_corpora`](https://github.com/scdenney/nlp_corpora), or another corpus entirely, email Steven before the **11 May workshop** with the corpus name and a one-sentence research question. Off-menu corpora will be considered, but they need approval.

---

## License

Data: CC-BY-4.0 (see [`LICENSE`](LICENSE)).

---

## Contact

Dr. Steven Denney — `s.c.denney@hum.leidenuniv.nl`
