#!/usr/bin/env Rscript
# analysis.R — Sentiment and distinctive-vocabulary analysis of the
# English-language Rodong Sinmun, 2018-2021.
#
# Reproduces both figures in the sample paper. Run from the repository
# root:
#     Rscript analysis/analysis.R
#
# Inputs : data/rodong_sinmun_en_sample.csv
# Outputs: figures/figure1_sentiment_by_year.png
#          figures/figure2_distinctive_terms.png
#          figures/sentiment_by_year.csv   (the numbers behind Figure 1)

suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(tidyr)
  library(stringr)
  library(tidytext)
  library(ggplot2)
})

set.seed(42)

# --- Locate inputs / outputs relative to the repo root -----------------
in_path <- "data/rodong_sinmun_en_sample.csv"
if (!file.exists(in_path)) in_path <- file.path("..", in_path)   # if run from analysis/
fig_dir <- if (dir.exists("figures")) "figures" else file.path("..", "figures")
dir.create(fig_dir, showWarnings = FALSE)

# --- Read --------------------------------------------------------------
articles <- read_csv(in_path, show_col_types = FALSE) |>
  mutate(year = factor(year))

# Corpus-specific tokens (masthead / wire-service words) that carry no
# substantive meaning. Decisions like this belong in the methods section.
custom_stop <- c("sinmun", "rodong", "kcna")

# --- Tokenise: one row per word; drop stop words and non-letters -------
tokens <- articles |>
  select(doc_id, year, text) |>
  unnest_tokens(word, text) |>
  filter(str_detect(word, "^[a-z]+$")) |>
  anti_join(stop_words, by = "word") |>
  filter(!word %in% custom_stop)

# Content words per article (denominator for length-normalised sentiment)
doc_len <- tokens |> count(doc_id, name = "n_words")

# --- METHOD 1: dictionary sentiment (Bing lexicon) ---------------------
# Net polarity per article, normalised per 100 content words so that long
# articles do not dominate the comparison.
doc_sent <- tokens |>
  inner_join(get_sentiments("bing"), by = "word") |>
  count(doc_id, year, sentiment) |>
  pivot_wider(names_from = sentiment, values_from = n, values_fill = 0) |>
  left_join(doc_len, by = "doc_id") |>
  mutate(net_per_100 = (positive - negative) / n_words * 100)

# Numbers behind Figure 1
summary_tbl <- doc_sent |>
  group_by(year) |>
  summarise(mean_net_per_100   = round(mean(net_per_100), 3),
            median_net_per_100 = round(median(net_per_100), 3),
            n_articles         = n(), .groups = "drop")
write_csv(summary_tbl, file.path(fig_dir, "sentiment_by_year.csv"))
print(summary_tbl)

# Figure 1: distribution of article-level net sentiment by year
p1 <- ggplot(doc_sent, aes(year, net_per_100)) +
  geom_boxplot(fill = "#bcd4e6", outlier.alpha = 0.3) +
  geom_hline(yintercept = 0, linetype = "dashed", colour = "grey40") +
  labs(title = "Net sentiment of Rodong Sinmun (English), 2018-2021",
       subtitle = "Bing lexicon; (positive - negative) per 100 content words",
       x = "Year", y = "Net sentiment per 100 content words") +
  theme_minimal(base_size = 12)
ggsave(file.path(fig_dir, "figure1_sentiment_by_year.png"), p1,
       width = 7, height = 4.2, dpi = 150)

# --- METHOD 2: distinctive vocabulary by year (TF-IDF) -----------------
top_terms <- tokens |>
  count(year, word, sort = TRUE) |>
  bind_tf_idf(word, year, n) |>
  group_by(year) |>
  slice_max(tf_idf, n = 10, with_ties = FALSE) |>
  ungroup() |>
  mutate(word = reorder_within(word, tf_idf, year))

p2 <- ggplot(top_terms, aes(tf_idf, word, fill = year)) +
  geom_col(show.legend = FALSE) +
  facet_wrap(~ year, scales = "free_y") +
  scale_y_reordered() +
  labs(title = "Most distinctive words by year (TF-IDF)",
       x = "TF-IDF", y = NULL) +
  theme_minimal(base_size = 11)
ggsave(file.path(fig_dir, "figure2_distinctive_terms.png"), p2,
       width = 8, height = 5, dpi = 150)

message("Done. Figures written to ", normalizePath(fig_dir))
