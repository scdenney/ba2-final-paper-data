# `kpoem` Data Dictionary

A reference key for the 615-poem sample of modern Korean poetry.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `kpoem_0042`

## `text`

- **Type:** string (Korean, NFC-normalized)
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

| Korean | Romanization / Notes |
|---|---|
| `윤동주` | Yun Dong-ju (1917-1945) — colonial-era resistance poet |
| `김소월` | Kim So-wol (1902-1934) — early-modern lyric poet |
| `이상화` | Yi Sang-hwa (1901-1943) — colonial-era nationalist poet |
| `한용운` | Han Yong-un (1879-1944) — Buddhist monk and resistance poet |
| `정지용` | Chong Chi-yong (1902-1950) — modernist poet |

(Not exhaustive — the poet column has ~30 unique values.)
