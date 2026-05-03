# `inter_korean_summit` Data Dictionary

A reference key for the 451-article sample of South Korean press coverage
of the inter-Korean leadership summits.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `inter_korean_summit_0042`

## `text`

- **Type:** string (Korean, NFC-normalised)
- **Description:** The cleaned article body. Truncated to the first 3,500
  characters; shorter articles are kept in full.

## `newspaper`

- **Type:** categorical (English)
- **Description:** Source publication. The ideological positioning of these
  two papers is well-established and is the natural Box Plot grouping
  variable.

| Value | Korean original | Editorial line |
|---|---|---|
| `Chosun Ilbo` | 조선일보 | Conservative; sceptical of engagement with North Korea |
| `Hankyoreh` | 한겨레 | Progressive; broadly supportive of engagement |

## `year`

- **Type:** integer
- **Description:** Coverage year. Three values:

| Value | Articles | Summit context |
|---|---:|---|
| `2000` | 13 | Kim Dae-jung — Kim Jong-il, Pyongyang (June) |
| `2007` | 42 | Roh Moo-hyun — Kim Jong-il, Pyongyang (October) |
| `2018` | 396 | Moon Jae-in — Kim Jong-un, multiple meetings (April–September) |

The 2018 imbalance reflects the digital-news era and high public
interest, not a sampling decision.

## `summit_episode`

- **Type:** categorical
- **Description:** Three labels, mapping one-to-one with `year`:

| Value | Meaning |
|---|---|
| `2000_june_summit` | First inter-Korean leadership summit, 13–15 June 2000 |
| `2007_october_summit` | Second inter-Korean leadership summit, 2–4 October 2007 |
| `2018_multi_summit` | The three 2018 meetings: Panmunjom (27 April), the secret 26 May meeting, and Pyongyang (18–20 September) |

## `title`

- **Type:** string (Korean)
- **Description:** Article headline. Useful for spot-reading individual
  documents but not as a grouping variable.
