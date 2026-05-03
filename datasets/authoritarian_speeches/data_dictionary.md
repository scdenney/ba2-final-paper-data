# `authoritarian_speeches` Data Dictionary

A reference key for the 600-speech sample of Park Chung-hee, Chun Doo-hwan,
and Roh Tae-woo presidential rhetoric. Use this if a Korean categorical
label slows you down — it is not meant to teach you the political content;
that is what you discover by reading the speeches.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `authoritarian_speeches_0042`

## `text`

- **Type:** string (Korean, NFC-normalized)
- **Description:** The cleaned speech body. Truncated to the first 3,500
  characters; shorter speeches are kept in full.
- **Example:** `존경하는 국민 여러분, 오늘 우리는 …`

## `president`

- **Type:** categorical
- **Description:** Speaker (English Romanization). Three values, 200 speeches each.

| Value | Korean original | Period in office |
|---|---|---|
| `Park Chung-hee` | 박정희 | 1961-05-16 to 1979-10-26 |
| `Chun Doo-hwan` | 전두환 | 1980-09-01 to 1988-02-24 |
| `Roh Tae-woo` | 노태우 | 1988-02-25 to 1993-02-24 (only ≤1992 in this sample) |

## `year`

- **Type:** integer (1961–1992)
- **Description:** Speech year. Park dominates 1961–1979; Chun dominates
  1980–1988; Roh dominates 1988–1992. There is some overlap in transition
  years.

## `date`

- **Type:** string, format `YYYY-MM-DD`
- **Description:** Exact speech date.
- **Example:** `1972-10-17` (Yusin proclamation day, if you happen to draw it)

## `kind`

- **Type:** categorical (Korean originals)
- **Description:** Speech type / occasion. Common values and English glosses:

| Korean value | English gloss |
|---|---|
| `연설` | Speech / address |
| `신년사` | New Year address |
| `치사` | Commemorative / congratulatory remarks |
| `훈시` | Instructional address (often to subordinates / military) |
| `유시` | Edict-style proclamation |
| `담화` | Public statement |
| `기념사` | Anniversary address |
| `만찬사` | Banquet remarks |
| `환영사` | Welcome remarks |
| `송별사` | Farewell remarks |
| `연두기자회견` | New-year press conference (Park-era staple) |

The list is not exhaustive — there are dozens of niche labels. For Box
Plot grouping, the top three (`연설`, `신년사`, `치사`) collectively cover
most speeches.

## `location`

- **Type:** string (Korean)
- **Description:** Where the speech was delivered. Many entries are
  `청와대` (Cheong Wa Dae / Blue House), but ribbon-cuttings and inspections
  carry place names. Mostly free text — not suitable as a Box Plot grouping
  variable directly, but can be filtered.
