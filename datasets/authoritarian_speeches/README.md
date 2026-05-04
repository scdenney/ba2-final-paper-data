# Authoritarian-Era Presidential Speeches (South Korea, 1961-1992)

**File:** `authoritarian_speeches_sample.csv` — 600 speeches, ~3.23 MB.

This corpus is the official rhetoric of the three South Korean presidents who governed the country during its authoritarian-developmental period:

- **Park Chung-hee** (박정희): from his 1961 coup through his assassination in October 1979 — the era of state-led industrialization, Yusin constitutional autocracy, and Cold War alignment with the US and Japan.
- **Chun Doo-hwan** (전두환): from the 1980 Gwangju massacre through 1988 — the Fifth Republic, military rule with managed economic growth.
- **Roh Tae-woo** (노태우): from June 1987's "democratic transition" declaration through 1992 — the early-democracy bridge years (Sixth Republic, Northern Diplomacy, Olympic-era opening).

The sample is stratified at **200 speeches per president**, so any Box Plot grouped by `president` compares equal-sized populations. Speech bodies are truncated to 3,500 characters (median is ~2,200, so very few are actually truncated).

## Columns

| Column | Type | Description |
|---|---|---|
| `doc_id` | string | Synthetic ID, `authoritarian_speeches_0000` – `authoritarian_speeches_0599` |
| `text` | string | Cleaned speech body (Korean), truncated to 3,500 characters |
| `president` | categorical | English name: `Park Chung-hee` / `Chun Doo-hwan` / `Roh Tae-woo` (200 each) |
| `year` | integer | Speech year (1961–1992) |
| `date` | string (YYYY-MM-DD) | Speech date |
| `kind` | categorical | Speech type — original Korean labels (e.g. 신년사 New Year address, 연설 speech, 치사 commemorative address). See data dictionary for translations of common values. |
| `location` | string | Where the speech was delivered (Korean) |

## Suggested research questions

1. **Did regime sentiment soften across the three authoritarian presidents?** Apply the KNU sentiment dictionary, then use a Box Plot grouped by `president`. The democratic transition arc would predict Roh > Chun > Park in positive sentiment — but the official rhetoric may not match that pattern.
2. **Do the three presidents have distinguishable rhetorical fingerprints?** Embed speeches with KLUE BERT, run k-means with k=3, then check whether the clusters align with the `president` labels.
3. **What topics distinguish New Year addresses from commemorative speeches?** Filter to two `kind` values and fit a 6-topic LDA on the combined subset, then chart topic prevalence by `kind`.
4. **Did 'security' / 'unification' rhetoric grow or shrink under the democratization pressure of 1987-1992?** Fit an 8-topic LDA on the full 600 speeches, then plot topic prevalence by `year`. Look for shifts in the late-Chun and Roh years.

## Provenance

Drawn from the `president_speeches` corpus in [scdenney/nlp_corpora](https://github.com/scdenney/nlp_corpora) (8,771-speech original, all 12 South Korean presidents 1948-2022).
