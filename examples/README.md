# Worked example — a FAIR-structured replication repository

This folder is **not** a runnable analysis — it is a **template / illustration** of what a FAIR-structured replication repository for the BA2 Digital Korea final paper should look like.

When you build your own replication repository (separate from this menu repo), it should look roughly like the structure below:

```
your-final-paper-replication/
├── README.md                # one paragraph: project, RQ, headline finding, repro steps
├── LICENSE                  # MIT for code, CC-BY-4.0 for derived data
├── CITATION.cff             # you as author, paper title, date
├── requirements.md          # Orange version, R version, packages
├── data/
│   ├── SOURCE.md            # points to this menu repo + commit SHA + file path
│   └── data_dictionary.md   # column-by-column types + example values
├── analysis/
│   ├── workflow.ows         # your Orange workflow (if you used Orange)
│   └── analysis.R           # your R script (if you used R)
└── figures/
    ├── figure1_topic_prevalence_by_era.png
    ├── figure2_sentiment_box.png
    └── ...
```

---

## What each file does (mapped to FAIR principles)

| File / folder | FAIR principle | What it accomplishes |
|---|---|---|
| `README.md` | Findable, Accessible | Anyone landing on the repo learns what it is in 30 seconds. |
| `LICENSE` | Reusable | States the legal terms under which others can reuse your code and data. |
| `CITATION.cff` | Findable, Reusable | Provides a machine-readable citation; GitHub renders it as a "Cite this repository" button. |
| `requirements.md` | Interoperable | Lists software versions so anyone on a different machine can replicate. |
| `data/SOURCE.md` | Findable, Accessible | Points to the original dataset by URL + commit hash, instead of duplicating it. |
| `data/data_dictionary.md` | Reusable | Describes every column so the data is understandable without you in the room. |
| `analysis/` | Reusable, Interoperable | The actual workflow — Orange `.ows` and/or R script. |
| `figures/` | Findable, Accessible | Every figure in your paper, in a portable format (PNG). |

---

## A `README.md` template for your replication repository

```markdown
# [Your paper's title]

Replication repository for the BA2 Digital Korea final paper, Spring 2026.

**Author:** [Your name]
**Course:** BA2 Digital Korea (Spring 2026), Korean Studies, Leiden University
**Instructor:** Dr. Steven Denney

## Research question

[One-sentence research question.]

## Headline finding

[Two or three sentences summarising what you found.]

## How to reproduce

1. Install Orange Data Mining version [X.Y] (or R version [X.Y] if you used R).
2. Install the packages listed in `requirements.md`.
3. Clone this repository.
4. Load the dataset:
   - The `data/` folder contains a `SOURCE.md` pointing to the data file at a specific commit of `scdenney/ba2-final-paper-data`. Clone that repo at the named commit and copy the named file into `data/`.
5. Open `analysis/workflow.ows` in Orange (or run `analysis/analysis.R` in R).
6. Confirm that the workflow produces the figures in `figures/`.

## Files

- `data/data_dictionary.md` — column-by-column reference for the dataset
- `figures/` — PNG exports of every figure in the paper
- `analysis/` — the Orange workflow and/or R script
- `requirements.md` — software versions

## Licence

- Code in `analysis/`: MIT (see `LICENSE`)
- Any data files in `data/`: CC-BY-4.0 (see `LICENSE`)

## Citation

See `CITATION.cff`.
```

---

## A `data/SOURCE.md` template

```markdown
# Source data

This project uses dataset **<dataset name>** from the BA2 Digital Korea
final-paper menu repository.

- Menu repository: https://github.com/scdenney/ba2-final-paper-data
- Commit hash: <40-character SHA recorded at clone time>
- File path: datasets/<dataset_folder>/<filename>.csv

## To reproduce

```bash
git clone https://github.com/scdenney/ba2-final-paper-data.git
cd ba2-final-paper-data
git checkout <40-character SHA>
cp datasets/<dataset_folder>/<filename>.csv ../your-final-paper-replication/data/
```

This pins your analysis to the exact dataset state you used — the FAIR-correct
way to reference data without duplicating it in your repository.
```

---

## A `requirements.md` template

```markdown
# Requirements

To reproduce the analysis in this repository, you need:

- Orange Data Mining: version 3.36 (or later)
  - Add-ons: Text Add-on (3.16+), kiwipiepy 0.21+ (auto-installed by the preprocessing script)
- R: version 4.4.0 (or later)
  - Packages: `readr`, `dplyr`, `ggplot2`, `tidytext`, `topicmodels` (only if you used R)

The Korean morphological analyser (Kiwi) is installed automatically by the
preprocessing scripts on the course Data & Scripts page; no manual install needed.
```
