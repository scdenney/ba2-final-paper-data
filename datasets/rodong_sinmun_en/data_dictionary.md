# `rodong_sinmun_en` Data Dictionary

A reference key for the 600-article sample of the English-language
edition of *Rodong Sinmun* (2018-2021).

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `rodong_sinmun_en_0042`

## `text`

- **Type:** string (English)
- **Description:** The cleaned article body. Truncated to the first
  3,500 characters; shorter articles are kept in full.
- **Length stats:** mean ~1,400 characters, median ~1,100, max 3,500.

## `date`

- **Type:** string, format `YYYY-MM-DD`
- **Description:** Exact article date.
- **Range:** `2018-01-02` to `2021-12-31`.

## `year`

- **Type:** integer
- **Description:** Article year. Four values, weighted by year volume:

| Year | Articles | Diplomatic context |
|---|---:|---|
| `2018` | ~178 | Summit-diplomacy year (Singapore, Panmunjom, Pyongyang) |
| `2019` | ~167 | Hanoi summit failure; rhetoric hardens |
| `2020` | ~144 | Border closure; pandemic isolationism |
| `2021` | ~111 | Eighth Party Congress; "frontal breakthrough" line |

This is the natural temporal grouping variable.

## `title`

- **Type:** string (English)
- **Description:** Article headline. Useful as a filter to identify
  topic-specific subsets (e.g. articles whose title mentions "south
  Korea", "U.S.", or "imperialist").

## `url`

- **Type:** string
- **Description:** URL to the original article on rodong.rep.kp (the
  official Rodong Sinmun website). Useful for spot-checking individual
  articles. Note: the official site is intermittently unreachable from
  outside North Korea; the Wayback Machine usually has copies.
