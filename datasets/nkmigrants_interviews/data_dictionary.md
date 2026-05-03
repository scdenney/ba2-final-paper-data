# `nkmigrants_interviews` Data Dictionary

A reference key for the 6,023-response sample of open-text survey
responses on North Korean migrants in South Korea.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `nkmigrants_interviews_0042`

## `text`

- **Type:** string (Korean, NFC-normalized)
- **Description:** The cleaned open-text response.
- **Length stats:** mean ~13 characters, median ~9, max 156.
- **Note:** Mostly 1-2 word phrases. See README for analytical implications.

## `response_type`

- **Type:** categorical (English)
- **Description:** Which question this response answers.

| Value | n | Question framing |
|---|---:|---|
| `hire` | 2,008 | Would you hire a North Korean migrant? Why / why not? |
| `neighbor` | 2,007 | Would you accept a North Korean migrant as a neighbor? |
| `vote` | 2,008 | Would you vote for a North Korean migrant for political office? |

This is the natural Box Plot grouping variable for any response-frame
comparison.

## `sex`

- **Type:** categorical (English)
- **Description:** Respondent sex (`Male` / `Female`).

## `age_cohorts`

- **Type:** categorical
- **Description:** Respondent age band. Encoded values include ranges
  like `19-29`, `30s`, `40s`, `50s`, `60+`. Treat as ordinal.

## `political_id3`

- **Type:** categorical (English)
- **Description:** Self-reported political identification, three-way.

| Value | Notes |
|---|---|
| `Progressive` | Left-leaning; in this corpus, often associated with sympathy / acceptance discourse |
| `Centrist` | Middle |
| `Conservative` | Right-leaning |

## `close_nkmigrants`

- **Type:** categorical (English)
- **Description:** Self-reported social distance from North Korean migrants.
  Typical values include:

| Value | Meaning |
|---|---|
| `Close` | Reports being socially close to NK migrants |
| `Distant` | Reports being socially distant |
| `Neither close nor distant` | Middle / non-committal |

Useful as a moderator variable: do attitudinally proximate respondents
write differently from attitudinally distant ones?
