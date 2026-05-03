# `kaebyok` Data Dictionary

A reference key for the 400-article sample of *Kaebyok* (개벽, 1920-1935).

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `kaebyok_0042`

## `text`

- **Type:** string (Korean, often mixed with Hanja, NFC-normalized)
- **Description:** The cleaned article body. Truncated to the first 3,500
  characters; shorter articles are kept in full.

## `issue_date`

- **Type:** string, format `YYYY-MM-DD`
- **Description:** Issue publication date. Monthly cadence — most months
  yield several articles.
- **Example:** `1924-03-01`

## `year`

- **Type:** integer
- **Description:** Publication year. Two clusters of values:

| Year | Articles in sample | Note |
|---|---:|---|
| `1920` | 38 | Founding year (June onwards) |
| `1921` | 58 | |
| `1922` | 56 | |
| `1923` | 63 | |
| `1924` | 63 | |
| `1925` | 49 | |
| `1926` | 38 | Forcibly suspended in August 1926 |
| `1934` | 17 | Successor magazine revival |
| `1935` | 18 | Final years |

The gap between 1926 and 1934 is the **colonial-censorship gap** and is
the single most useful feature of this corpus for a temporal-trend
research design.

## `article_num`

- **Type:** integer
- **Description:** Sequence number of the article within its issue.
  Articles 1, 2, 3, … in a given issue are typically the editorial,
  feature, and follow-on pieces. Useful as a tie-breaker in sorting,
  but not a substantive grouping variable.
