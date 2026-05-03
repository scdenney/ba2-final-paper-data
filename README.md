# BA2 Digital Korea — Final Paper Dataset Menu

A curated menu of ten Korean (and one English) text corpora for the **BA2 Digital Korea** final research-paper assignment, Spring 2026, taught by Dr. Steven Denney at Korean Studies, Leiden University.

For the assignment itself, see the [course site](https://scdenney.github.io/ba2-digital-korea/final-paper/).

This repo is a **slimmed, pre-vetted snapshot** drawn from the upstream NLP corpora collection at [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora). It is deliberately scoped to one assignment — pick one corpus, write a 2,000–5,000-word research paper, build a public FAIR-structured replication repository.

---

## How to use

1. Clone this repository (or download a ZIP from the green "Code" button):
   ```bash
   git clone https://github.com/scdenney/ba2-final-paper-data.git
   ```
2. Browse the `datasets/` folder. Each dataset has its own README, data dictionary, build script, and a `*_sample.csv` file ready to load into Orange Data Mining or R.
3. Pick **one** corpus. Generate a research question. Bring both to the **11 May workshop** for in-class approval.

For loading guidance and a worked example, see [`how-to-use.md`](how-to-use.md) and the [`examples/`](examples/) folder.

---

## The dataset menu

| # | Dataset | Folder | Rows | Best for |
|---:|---|---|---:|---|
| 1 | Authoritarian-era presidential speeches | `datasets/authoritarian_speeches/` | 600 | Political rhetoric under dictatorship; sentiment + grouping by `president` |
| 2 | Inter-Korean summit coverage | `datasets/inter_korean_summit/` | 451 | Comparative media framing (Chosun vs. Hankyoreh) across the 2000/2007/2018 summits |
| 3 | Colonial magazines (multi-title) | `datasets/colonial_magazines/` | 495 | Colonial-period intellectual debates across 19 magazines; LDA across magazine type |
| 4 | *Kaebyok* (single-title) | `datasets/kaebyok/` | 400 | Single-magazine diachronic analysis 1920–1935; the 1926 censorship gap |
| 5 | Korean newspapers (Twitter) | `datasets/kr_newspapers_twitter/` | 2,745 | Comparative outlet ideology × engagement, 6 outlets in 2017 |
| 6 | KPoEM (Korean poems) | `datasets/kpoem/` | 615 | Sentiment / emotion analysis on a labelled corpus (44-category KOTE labels) |
| 7 | Immigrant interviews (open-text) | `datasets/immigrant_interviews/` | 1,006 | Sentiment / clustering on micro-texts (see caveat below) |
| 8 | NK migrants interviews (open-text) | `datasets/nkmigrants_interviews/` | 6,023 | Same use case + caveat as #7 |
| 9 | Korean newspaper archive (modern slice) | `datasets/korean_newspaper_archive_modern/` | 2,000 | Diachronic / cross-newspaper analysis of the late-colonial / liberation-era press |
| 10 | *Rodong Sinmun* (English) | `datasets/rodong_sinmun_en/` | 600 | Temporal clustering across diplomatic crises 2018–2021 (English text) |

**Total repo size:** ~18 MB (clones quickly).

---

## Caveats — read before picking

Some corpora have method-compatibility constraints. Pick deliberately, not by accident.

- **#7 Immigrant interviews and #8 NK migrants interviews are *short* open-text responses** (median 11 and 9 characters respectively). These are conjoint-experiment justifications, not interview transcripts — single words, two-word phrases. They are usable for **sentiment** (one polarity-bearing word per response) and for **clustering** (small vocabulary, sharp groups), but **LDA topic modelling at the response level will not work** — there isn't enough text per row for a topic model to fit. If you want to use one of these for a topic model, you would need to aggregate responses by respondent × question type first.
- **#10 *Rodong Sinmun* is English-only.** The KNU sentiment dictionary is Korean and won't apply; KLUE BERT (the Korean embedding model) won't apply either. If you choose this corpus, you must use a different sentiment approach (e.g., VADER, a custom English lexicon) or a different method entirely (e.g., LDA, k-means clustering — both of which work fine on English).
- **#3 Colonial magazines uses Hanmun-mixed pre-modern Korean** in places. Kiwi (the morphological analyser used in this course's preprocessing scripts) was trained on contemporary Korean and will tokenise pre-modern / Hanmun-heavy text less cleanly. KNU and KLUE BERT will likewise be noisy on this register. Choose this corpus deliberately — it is interesting precisely *because* of the linguistic challenges — and treat tokenisation limitations as a methodological reflection point in your data and methods section.
- **#4 *Kaebyok*** has the same caveat to a lesser degree (single-title, mostly modern-ish Korean but with some Hanmun).
- **Sample balance varies across datasets.** Perfectly balanced for Box Plot grouping: #1 (200 speeches per president). Roughly balanced: #3, #4, #6. **Imbalanced (faithful to source):** #2 (heavily 2018 summit), #5 (left-leaning slightly larger), #9 (heavily 1940s–1950s, one newspaper dominates ~80% of the pool), #10 (year-proportional to source — 2018 dominates). For an imbalanced corpus, consider filtering down to a balanced sub-sample yourself before running the comparison; document the choice in your data and methods section.

---

## Off-menu corpora

If you want to use a different corpus from [`scdenney/nlp_corpora`](https://github.com/scdenney/nlp_corpora), email Steven by **Sunday 10 May, end of day** with the corpus name and a one-sentence research question. Off-menu requests after that point are not guaranteed approval.

---

## Provenance & reproducibility

Each dataset folder contains a `build.py` script that produced its `*_sample.csv` from the upstream raw corpus. Scripts use `random_state=42` for any sampling. Light cleaning was applied (NFC unicode normalisation, whitespace collapse, removal of URLs, HTML entities, and literal `\n`/`\r`/`\t` artefacts). **No morphological tokenisation** was performed — students do that in Orange via the Python Script widget using the preprocessing scripts published on the [course Data & Scripts page](https://scdenney.github.io/ba2-digital-korea/data/).

To re-build any dataset from the upstream source, clone [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) and adjust the source-path constant near the top of the relevant `build.py` to point at your local clone.

---

## Licence

- **Data** in this repository: derived from publicly-available primary sources curated in `scdenney/nlp_corpora`. Released for educational use under [CC-BY-4.0](LICENSE).
- **Code** (the `build.py` scripts and any `examples/`): [MIT](LICENSE).

If you publish work that uses one of these datasets, please cite the upstream source corpus from `scdenney/nlp_corpora` in addition to this menu repo (see [`CITATION.cff`](CITATION.cff)).

---

## Contact

Dr. Steven Denney — `s.c.denney@hum.leidenuniv.nl`
