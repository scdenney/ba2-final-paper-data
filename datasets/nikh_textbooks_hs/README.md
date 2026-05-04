# NIKH High-School History Textbooks (Authoritarian and Democratic Eras, South Korea)

**File:** `nikh_textbooks_hs_sample.csv` — 21 textbooks, ~0.22 MB.

This corpus is the high-school slice of the National Institute of Korean History (NIKH; 국사편찬위원회) textbook collection, restricted to two contrasting eras of South Korean curriculum politics:

- **Authoritarian** (1954–1992): textbooks produced under the 1st through 5th National Curricula — Park Chung-hee (including the Yusin period), Chun Doo-hwan, and the late-Cold-War transition years. State-monopoly textbook publication, anti-communist framing, developmentalist national narrative.
- **Democratic** (1992–2016): textbooks produced under the 6th and 7th Curricula and their revisions — Kim Young-sam through Park Geun-hye. Diversification of approved publishers, gradual incorporation of social-history and democratization narratives, and the periodic textbook controversies of the 2000s and 2010s.

The corpus is small but ideal for **diachronic comparison of national-history pedagogy** at a single educational level. Holding `level` constant at high school removes the most obvious confound (textbooks written for younger readers use simpler vocabulary and different topics), so observed differences are more plausibly attributable to era and curriculum politics. Textbook bodies are truncated to 5,000 characters each, which captures roughly the opening chapters of each book — typically the framing material that introduces the national narrative.

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `nikh_hs_0000` – `nikh_hs_0020` |
| `text` | string | Cleaned textbook body (Korean), truncated to the first 5,000 characters |
| `era` | categorical | `Authoritarian` (7 books) or `Democratic` (14 books) |
| `year` | integer | Publication year (1973–2016) |
| `level` | categorical | Always `High School` (kept for transparency) |
| `book_id` | string | Original NIKH identifier (`ta_*` for the digitized series, `H-*` for the revised 7th Curriculum) |
| `title` | string | Full title in Korean |
| `curriculum` | string | Named curriculum (e.g. `3rd Curriculum`, `7th Curriculum (Revised)`) |
| `nikh_period` | string | Source-assigned curriculum period |
| `publisher` | string | Publishing institution (Korean) — e.g. 문교부 (Ministry of Education, pre-1990 name), 교육부, 천재교육, 금성출판사 |

## Suggested research questions

1. Did high-school history textbooks soften in tone after the 1992 democratic transition, or did the official rhetoric remain comparable across eras?
2. What topics distinguish Authoritarian-era textbooks (1973–1990) from Democratic-era textbooks (1996–2016) — for example, in coverage of the colonial period, the Korean War, or the post-1948 republic?
3. Within the Democratic era, do textbooks from different publishers (e.g. 천재교육, 금성출판사, 지학사) cluster apart, or do they share a common state-curriculum vocabulary?
4. How does the relative weight of national-narrative vocabulary (민족, 국가, 통일) shift across the 40-year span — is there a discernible diachronic trend, or are shifts confined to specific curricular reforms?

## Provenance

Drawn from the `nikh` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) (67-book full corpus across five eras and five educational levels).
