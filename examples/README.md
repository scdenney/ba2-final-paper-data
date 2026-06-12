# Example submission

This folder shows what a finished BA2 Digital Korea final-paper submission looks like, end to end. It is here so you can see the **structure, level of detail, and reproducibility** expected — not so you can copy the analysis. It deliberately uses a different corpus (the English-language *Rodong Sinmun*) and different methods from most of yours, so treat it as a model of *form*, not content.

| Item | What it is |
|---|---|
| `sample-paper.pdf` (source: `sample-paper.md`) | A short research report in the required section structure, with both figures embedded inline. |
| `replication-repo/` | A complete, FAIR-structured replication repository laid out exactly as you would push it to your own public GitHub repo. |

## The sample paper

`sample-paper.pdf` follows the five-section structure from the brief: research question, brief literature review, data and methods, analysis and findings, summary and conclusion. Things to notice:

- Every decision a replicator needs is in **data and methods**, and every figure is read in plain language in **findings**. That is the level of detail to aim for — document the *decisions*, interpret the *figures*.
- Both figures sit **inline** in the body, right next to the text that discusses them. The same PNGs also live in `replication-repo/figures/`.
- The replication-repository URL is a **footnote on the title**.
- It runs short (~1,300 words) to stay readable as a model. **Your paper must be 2,500–6,000 words**; expand the findings and literature review, not the framing.

## The replication repository

`replication-repo/` contains all eight required items. Clone-and-run works — from inside that folder:

```bash
Rscript analysis/analysis.R
```

regenerates both figures from the data in `data/`. Open `replication-repo/README.md` first; that is the file I read when I spot-check repositories.

```
replication-repo/
├── README.md            # project, RQ, headline finding, how to reproduce
├── data/
│   ├── SOURCE.md        # provenance: menu repo URL + pinned commit
│   ├── data_dictionary.md
│   └── rodong_sinmun_en_sample.csv
├── analysis/
│   ├── analysis.R       # the script that makes the figures
│   └── ORANGE_WORKFLOW.md
├── figures/
│   ├── figure1_sentiment_by_year.png
│   └── figure2_distinctive_terms.png
├── requirements.md
├── CITATION.cff
└── LICENSE
```

Orange users: you would put a saved `.ows` workflow in `analysis/` in place of (or alongside) the R script — see `replication-repo/analysis/ORANGE_WORKFLOW.md`.
