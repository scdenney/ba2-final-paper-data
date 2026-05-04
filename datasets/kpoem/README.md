# Modern Korean Poems

**File:** `kpoem_sample.csv` — 615 poems, ~0.34 MB.

A small, hand-curated corpus of modern Korean poetry. Each row is a single poem with its title and poet. No emotion annotations are included — this is plain poetry text, suitable for the same kinds of analysis you would run on any Korean prose corpus on the menu.

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `kpoem_0000` – `kpoem_0614` |
| `text` | string | Cleaned poem body (Korean, line breaks collapsed to spaces) |
| `title` | string | Poem title (Korean) |
| `poet` | categorical | Poet name (Korean). ~30 unique values; many famous modern Korean poets — 윤동주, 김소월, 이상화, 한용운, 정지용, etc. |

## Suggested research questions

1. **Do poems by the same poet cluster together?** Embed the poems with KLUE BERT, run hierarchical clustering, and compare cluster assignments to the `poet` labels. Some poets have distinctive recurrent motifs (윤동주's self-doubt, 김소월's loss). A good answer identifies one or two poets whose poems cluster tightly and one or two whose poems scatter, and reads vocabulary from the tightest cluster to label what makes it distinctive.
2. **What latent topics run across the poems, and do they map onto poet?** Fit an 8- to 10-topic LDA on all 615 poems, then chart topic prevalence by `poet` (filter to the 8–10 most prolific poets for legibility). Are some topics tightly tied to a single poet, while others are shared across many poets?
3. **Which poets carry the most positive-vs-negative affect, by KNU dictionary?** Apply the KNU sentiment dictionary, score each poem, then aggregate by `poet`. Which poets carry the most consistently negative (or positive) average score? Note in your write-up that KNU is contemporary South Korean and undercounts the figurative or archaic vocabulary common in early-20th-century poetry.

## Provenance

Drawn from the `kpoem` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) (615-poem original).
