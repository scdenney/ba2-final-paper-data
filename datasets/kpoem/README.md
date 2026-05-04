# Modern Korean Poems with Emotion Annotations

**File:** `kpoem_sample.csv` — 615 poems, ~0.38 MB.

This is a small, hand-curated corpus of modern Korean poetry. Each poem has been annotated by **five independent emotion annotators**, each of whom listed multiple emotion labels per poem from a Korean emotion taxonomy (e.g. 슬픔 sadness, 비장함 stoic resolve, 깨달음 epiphany, 서러움 grief, …). The corpus is a rare opportunity to compare a text-as-data sentiment / emotion analysis against human gold-label annotations on the same documents.

The five annotator label-lists per poem are pooled and the most-voted label is exposed as `dominant_emotion`; the count of mentions is exposed as `emotion_votes` (a confidence proxy).

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `kpoem_0000` – `kpoem_0614` |
| `text` | string | Cleaned poem body (Korean, line breaks collapsed to spaces) |
| `title` | string | Poem title (Korean) |
| `poet` | categorical | Poet name (Korean). Many famous modern Korean poets — 윤동주, 김소월, 이상화, etc. |
| `dominant_emotion` | categorical | Most-voted emotion label across the 5 annotators (Korean). 20+ unique values; top values include 슬픔 (sadness, n=122), 비장함 (stoic resolve, n=57), 불안/걱정 (anxiety/worry, n=56), 깨달음 (epiphany, n=50). |
| `emotion_votes` | integer | How many annotator-mentions the dominant emotion received (typically 2-5; 1 indicates a low-agreement poem) |

## Suggested research questions

1. **Does the KNU sentiment dictionary's positive/negative score align with the human-annotated `dominant_emotion`?** Apply KNU, then compare its scores against `dominant_emotion` (collapse the 20+ emotions into a positive/negative grouping yourself — see the data dictionary for a starter mapping). This is the only corpus in the menu where you can validate a sentiment tool against human gold labels.
2. **Do poems by the same poet cluster together?** Embed poems with KLUE BERT, run hierarchical clustering, then compare to the `poet` labels. Some poets have distinctive recurrent motifs (윤동주's self-doubt, 김소월's loss).
3. **What latent topics cut across the 20 emotion categories?** Fit a 6- to 8-topic LDA on all 615 poems, then chart topic prevalence by `dominant_emotion` (filter to top 5-6 emotions for legibility).
4. **Are low-agreement poems (`emotion_votes` <= 2) systematically different from high-agreement poems?** Use KLUE BERT embeddings and check whether low-agreement poems cluster apart, or are distributed evenly.

## Provenance

Drawn from the `kpoem` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) (615-poem original).
