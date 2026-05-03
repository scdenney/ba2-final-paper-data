# `kr_newspapers_twitter` Data Dictionary

A reference key for the 2,745-tweet sample of South Korean newspaper
Twitter feeds.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `kr_newspapers_twitter_0042`

## `text`

- **Type:** string (Korean, NFC-normalized)
- **Description:** Tweet body. URLs and HTML entities stripped. Mostly
  short headline-style text.
- **Length stats:** mean ~46 characters, median ~38, max ~116.

## `paper_name`

- **Type:** categorical (Twitter handle stem)
- **Description:** Newspaper. Six values:

| Value | Korean name | Editorial line |
|---|---|---|
| `chosun` | 조선일보 (Chosun Ilbo) | Conservative — flagship right-leaning daily |
| `dongamedia` | 동아일보 (Dong-a Ilbo) | Conservative |
| `joongangilbo` | 중앙일보 (Joongang Ilbo) | Conservative — Samsung-affiliated |
| `hankyungmedia` | 한국경제 (Hankyung Daily Economic) | Center-right (business / market focus) |
| `hanitweet` | 한겨레 (Hankyoreh) | Progressive — flagship left-leaning daily |
| `kyunghyang` | 경향신문 (Kyunghyang Shinmun) | Progressive |

## `created`

- **Type:** string, format `YYYY-MM-DD`
- **Description:** Tweet date. Range covers 2018–2019. Most are
  late-2018 to early-2019 captures.

## `favoriteCount`

- **Type:** integer
- **Description:** Twitter likes (favorites) count at scrape time.
  Highly skewed — most tweets have 0–10, a few have hundreds. Use a
  log transform if you treat this as a continuous variable.

## `retweetCount`

- **Type:** integer
- **Description:** Retweets count at scrape time. Same skew caveat.

## `pol_id`

- **Type:** categorical (English)
- **Description:** Editorial-line label aggregated from `paper_name`.
  Two values, both well-represented:

| Value | Papers | Tweets |
|---|---|---:|
| `left` | Hankyoreh + Kyunghyang | 1,496 |
| `right` | Chosun + Dong-a + Joongang + Hankyung | 1,249 |

This is the natural Box Plot grouping variable for sentiment / topic
comparisons.
