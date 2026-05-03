# `kpoem` Data Dictionary

A reference key for the 615-poem sample of modern Korean poetry with
emotion annotations.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `kpoem_0042`

## `text`

- **Type:** string (Korean, NFC-normalised)
- **Description:** The cleaned poem body. Original line breaks have been
  collapsed to spaces (so the text is a single line per row, suitable for
  Orange's File widget). No truncation.
- **Length stats:** mean ~247 characters, median ~228, max 543.

## `title`

- **Type:** string (Korean)
- **Description:** Poem title.
- **Example:** `서시` ("Foreword" — Yun Dong-ju's most famous poem)

## `poet`

- **Type:** categorical (Korean)
- **Description:** Poet name. The corpus includes many of the
  best-known modern Korean poets:

| Korean | Romanisation / Notes |
|---|---|
| `윤동주` | Yun Dong-ju (1917-1945) — colonial-era resistance poet |
| `김소월` | Kim So-wol (1902-1934) — early-modern lyric poet |
| `이상화` | Yi Sang-hwa (1901-1943) — colonial-era nationalist poet |
| `한용운` | Han Yong-un (1879-1944) — Buddhist monk and resistance poet |
| `정지용` | Chong Chi-yong (1902-1950) — modernist poet |

(Not exhaustive — the poet column has ~30 unique values.)

## `dominant_emotion`

- **Type:** categorical (Korean)
- **Description:** Most-voted emotion label across the 5 annotators
  (see `build.py` for the aggregation logic). Top values:

| Korean value | English gloss | Sample n |
|---|---|---:|
| `슬픔` | Sadness | 122 |
| `비장함` | Stoic resolve / pathos | 57 |
| `불안/걱정` | Anxiety / worry | 56 |
| `깨달음` | Epiphany / realisation | 50 |
| `안타까움/실망` | Pity / disappointment | 46 |
| `아껴주는` | Tender / cherishing | 39 |
| `기대감` | Anticipation / hope | 36 |
| `서러움` | Grief / sorrow | 35 |
| `불쌍함/연민` | Compassion / pity | 26 |
| `힘듦/지침` | Exhaustion | 20 |
| `신기함/관심` | Curiosity / interest | 20 |
| `흐뭇함(귀여움/예쁨)` | Warmth / fondness | 18 |
| `감동/감탄` | Awe / admiration | 14 |
| `절망` | Despair | 13 |
| `패배/자기혐오` | Defeat / self-loathing | 13 |

20 categories total in the sample. For Box Plot grouping, filter to the
top 5–6 emotions to keep panels legible.

For a positive/negative collapse for sentiment validation:

- **Negative**: 슬픔, 불안/걱정, 안타까움/실망, 서러움, 불쌍함/연민,
  힘듦/지침, 절망, 패배/자기혐오, 비장함 (debatable — pathos)
- **Positive**: 깨달음, 아껴주는, 기대감, 신기함/관심, 흐뭇함(귀여움/예쁨), 감동/감탄

## `emotion_votes`

- **Type:** integer (typically 1–5)
- **Description:** Number of annotator-mentions the dominant emotion
  received. Higher = stronger inter-annotator agreement on that label.
  Use as a quality / confidence filter.
