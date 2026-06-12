# Talking Past the Table — replication repository

Replication materials for the BA2 Digital Korea final paper *"Talking Past the Table: Sentiment and Topic in the English-Language Rodong Sinmun, 2018–2021."*

**Research question.** Did the affective tone of the English-language *Rodong Sinmun* track the collapse of North Korea's summit diplomacy between 2018 and 2021, or did it hold its register independent of diplomatic fortunes?

**Headline finding.** Net sentiment is positive in every year and does not fall as diplomacy fails; it is *highest* in 2021, the most isolated year in the window. Distinctive vocabulary moves from nuclear-diplomacy terms (2018) to pandemic terms (2020) to economic-construction terms (2021), but the positive register is stable throughout.

## Reproduce

Requires R (≥ 4.2). From the repository root:

```bash
# 1. install dependencies (once)
Rscript -e 'install.packages(c("readr","dplyr","tidyr","stringr","tidytext","ggplot2"))'

# 2. regenerate both figures and the summary table
Rscript analysis/analysis.R
```

Outputs land in `figures/`:

- `figure1_sentiment_by_year.png` — net sentiment by year (Figure 1 in the paper)
- `figure2_distinctive_terms.png` — top TF-IDF terms by year (Figure 2)
- `sentiment_by_year.csv` — the numbers behind Figure 1

Runtime is a few seconds. Exact package versions are in `requirements.md`. Orange users: see `analysis/ORANGE_WORKFLOW.md` for the equivalent widget chain.

## Contents

| Path | What it is | FAIR |
|---|---|---|
| `README.md` | This file — project, RQ, finding, how to reproduce | F, A |
| `data/rodong_sinmun_en_sample.csv` | The corpus analysed | F, A |
| `data/SOURCE.md` | Where the corpus came from (menu repo + commit) | F, A |
| `data/data_dictionary.md` | Column-by-column reference | R |
| `analysis/analysis.R` | The analysis script | R, I |
| `analysis/ORANGE_WORKFLOW.md` | The equivalent Orange widget chain | R, I |
| `figures/` | PNG exports used in the paper | F, A |
| `requirements.md` | R version + package versions | I |
| `CITATION.cff` | How to cite this work | F, R |
| `LICENSE` | MIT (code) + CC-BY-4.0 (figures) | R |

## Citation

See `CITATION.cff`. Corpus reuse terms are in `data/SOURCE.md`.
