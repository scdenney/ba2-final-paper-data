# How to use the dataset menu

A short guide for BA2 Digital Korea students. Clone this repo, pick one corpus, build a research paper.

---

## 1. Clone or download

The simplest path is to clone the whole repo:

```bash
git clone https://github.com/scdenney/ba2-final-paper-data.git
```

Or click the green **Code** button on github.com and choose **Download ZIP**.

Total repo size is small (~18 MB) so cloning is fast.

---

## 2. Pick one dataset

Browse the [`datasets/`](datasets/) folder. Each subfolder contains:

- `README.md` — what the corpus is, where it came from, columns, suggested research questions
- `data_dictionary.md` — column-by-column reference
- `<dataset>_sample.csv` — the file you load
- `build.py` — the script that produced the CSV (provenance / reproducibility)

Read at least the README before deciding. Several corpora have caveats (e.g., short open-text responses are not suitable for LDA topic modelling; pre-modern / Hanja-heavy texts will tokenise less cleanly with Kiwi).

---

## 3. Load into Orange Data Mining

1. Open Orange.
2. Drop a **File** widget on the canvas.
3. Point it at your chosen `<dataset>_sample.csv`.
4. Set the role of the `text` column to **Text** and `doc_id` to **Meta**. Categorical metadata columns (`era`, `category`, `president`, `newspaper`, etc.) should be **Categorical Meta**; numeric columns (`votes`, `favoriteCount`, `year`) should be **Numeric Meta**.
5. Drop a **Corpus** widget after the File widget — confirm the text feature is recognised.
6. Apply the appropriate preprocessing script from the [course Data & Scripts page](https://scdenney.github.io/ba2-digital-korea/data/):
   - `custom_preprocessing_*.py` for nouns-only (clustering, LDA, embeddings)
   - `sentiment_preprocessing_*.py` for nouns + verbs + adjectives (sentiment analysis)
   - Set `TEXT_COLUMN = 'text'` at the top of the script — every CSV in this menu uses `text` as the document column name.

---

## 4. Load into R (if you prefer R)

```r
library(readr)
library(dplyr)

corpus <- read_csv("datasets/authoritarian_speeches/authoritarian_speeches_sample.csv")
glimpse(corpus)
```

For preprocessing, see the Week 3–4 R demo scripts on the course Data & Scripts page (`week03_preprocessing.R`, `week04_text_wrangling.R`).

---

## 5. FAIR principles for your replication repository

Your final paper requires a public GitHub replication repository structured per [FAIR principles](https://www.go-fair.org/fair-principles/) — Findable, Accessible, Interoperable, Reusable. The repository should contain:

- `README.md` — what the project is, the research question, the headline finding, instructions to reproduce
- `data/` — either the CSV directly, or a `data/SOURCE.md` pointing to *this* menu repo's URL plus the commit hash you cloned (preferred — don't duplicate the data)
- `data/data_dictionary.md` — column-by-column with types and example values
- `analysis/` — your Orange `.ows` workflow file and/or R script(s)
- `figures/` — PNG exports of every figure that appears in your paper
- `LICENSE` — MIT for code, CC-BY-4.0 for any new data you produced
- `CITATION.cff` — your name, paper title, course, date
- `requirements.md` — Orange version, R version, non-default packages used

A worked example of a FAIR-structured replication repository is in [`examples/`](examples/).

---

## Pinning a specific commit (for full reproducibility)

If you want your replication repo to point at this menu repo *exactly as it was when you cloned it*, record the commit hash:

```bash
cd /path/to/ba2-final-paper-data
git rev-parse HEAD
# copy the 40-character output into your data/SOURCE.md
```

Then in your replication repo's `data/SOURCE.md`:

```markdown
# Source data

This project uses dataset **<dataset name>** from the BA2 Digital Korea
final-paper menu repository:

- Repository: https://github.com/scdenney/ba2-final-paper-data
- Commit: <40-character SHA you recorded above>
- File: datasets/<dataset_folder>/<filename>.csv

To reproduce, clone the menu repo at the commit above:
git clone https://github.com/scdenney/ba2-final-paper-data.git
cd ba2-final-paper-data
git checkout <40-character SHA>
```

This is the FAIR-correct way to reference data without duplicating it.

---

## Questions

Email Dr. Denney: `s.c.denney@hum.leidenuniv.nl`.
