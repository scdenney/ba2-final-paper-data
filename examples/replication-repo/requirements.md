# Requirements

## Software

- **R** 4.5.1 (any R ≥ 4.2 should work).
- This example uses the R path. An **Orange** submission would instead list **Orange Data Mining 3.36** here, plus the **Text** add-on and its version.

## R packages

Non-default packages used by `analysis/analysis.R`, with the versions this example was run against:

| Package | Version tested | Purpose |
|---|---|---|
| readr | 2.1.6 | read the CSV |
| dplyr | 1.2.0 | data manipulation |
| tidyr | 1.3.2 | reshape (`pivot_wider`) |
| stringr | 1.6.0 | token filtering |
| tidytext | 0.4.3 | tokenisation, Bing lexicon, TF-IDF |
| ggplot2 | 4.0.2 | figures |

Install all at once:

```r
install.packages(c("readr", "dplyr", "tidyr", "stringr", "tidytext", "ggplot2"))
```

The Bing sentiment lexicon ships with `tidytext`; no download or licence acceptance is needed (unlike AFINN or NRC, which pull from the `textdata` package on first use). That is one reason the script runs non-interactively on a fresh machine.
