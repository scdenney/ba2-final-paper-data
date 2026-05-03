# `immigrant_interviews` Data Dictionary

A reference key for the 1,006-response sample of open-text survey
responses on immigrant admission to South Korea.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `immigrant_interviews_0042`

## `text`

- **Type:** string (Korean, NFC-normalised)
- **Description:** The cleaned open-text response.
- **Length stats:** mean ~17 characters, median ~11, max 271.
- **Note:** Most responses are 1-2 word phrases. See README for
  implications.

## `sex`

- **Type:** categorical (English)
- **Description:** Respondent sex.

| Value | n |
|---|---:|
| `Male` | 504 |
| `Female` | 502 |

## `age_cohort`

- **Type:** categorical (English)
- **Description:** Respondent age band.

| Value | n |
|---|---:|
| `60+` | ~220 |
| `40-49` | ~212 |
| `50-59` | ~212 |
| `30-39` | ~192 |
| `18-29` | ~170 |

(Counts approximate; minor drop from cleaning.)

## `political_id3`

- **Type:** categorical (English)
- **Description:** Self-reported political identification, three-way.

| Value | n |
|---|---:|
| `Centrist` | ~475 |
| `Progressive` | ~303 |
| `Conservative` | ~228 |

## `college`

- **Type:** categorical (English)
- **Description:** Educational attainment.

| Value | n |
|---|---:|
| `Some college or more` | ~775 |
| `No college` | ~233 |
