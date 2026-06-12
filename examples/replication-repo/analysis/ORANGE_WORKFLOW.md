# The Orange equivalent

This example uses R, because the figures then regenerate from one command and the reproduction check is unambiguous. Most of you will use Orange. If you do, **save your workflow (`File → Save`) as `workflow.ows` and put it in this `analysis/` folder** — that file *is* your analysis, the same way `analysis.R` is here — and describe the widget chain in your README.

The analysis here maps onto Orange roughly as follows.

## Method 1 — sentiment by year (Figure 1)

```
Corpus  →  Preprocess Text  →  Sentiment Analysis  →  Box Plot
                                (Liu Hu)               (group by: year)
```

- **Corpus** — load `rodong_sinmun_en_sample.csv`; set `text` as the text feature and `year` as a categorical meta variable.
- **Preprocess Text** — lowercase, tokenise by word, remove English stopwords. *For a Korean corpus this is where the Kiwi tokeniser goes, via the Python Script widget, before anything else.*
- **Sentiment Analysis** — the Liu Hu dictionary is Orange's counterpart to the Bing lexicon used in the R script.
- **Box Plot** — value = sentiment score, grouped by `year`.

## Method 2 — distinctive words by year (Figure 2)

```
Corpus  →  Preprocess Text  →  Bag of Words (TF-IDF)  →  Select Rows / Word Cloud
```

- Set Bag of Words to TF-IDF weighting; use **Select Rows** to filter one `year` at a time and read off the highest-weighted terms, or feed a single year to **Word Cloud**.

A grader opening your `.ows` in Orange should be able to press play and reproduce your figures, so check that the File widget uses a **relative** path (`data/...`), not an absolute one from your own machine.
