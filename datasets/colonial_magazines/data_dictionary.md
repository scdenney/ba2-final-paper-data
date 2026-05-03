# `colonial_magazines` Data Dictionary

A reference key for the 495-article sample of colonial-era Korean magazines.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `colonial_magazines_0042`

## `text`

- **Type:** string (Korean, frequently mixed with Hanja, NFC-normalised)
- **Description:** The cleaned article body. Truncated to the first 3,500
  characters; shorter articles are kept in full.

## `magazine`

- **Type:** categorical (Korean originals)
- **Description:** Magazine title. 19 values in the sample.

### The "Big Four" (urban progressive monthlies, large article counts)

| Korean value | Romanisation | Years | English gloss |
|---|---|---|---|
| `삼천리` | Samcheolli | 1929-1942 | "Three-thousand Ri" (a poetic name for Korea) |
| `별건곤` | Byeolgeongon | 1926-1934 | "Another World" — popular-culture / general-interest monthly |
| `개벽` | Kaebyok | 1920-1935 | "Creation" — flagship Cheondogyo cultural-nationalist monthly |
| `동광` | Donggwang | 1926-1933 | "Eastern Light" — Heungsadan-affiliated reform monthly |

### Late-Joseon and early colonial society magazines (smaller titles)

| Korean value | Romanisation | English gloss |
|---|---|---|
| `대조선독립협회회보` | Daejoseon Dongnip Hyeophoe Hoebo | Independence Club bulletin (1896-1898) |
| `대한자강회월보` | Daehan Jaganghoe Wolbo | Korea Self-Strengthening Society monthly |
| `대한협회회보` | Daehan Hyeophoe Hoebo | Korea Society bulletin |
| `대한학회월보` | Daehan Hakhoe Wolbo | Korea Academic Society monthly |
| `대한흥학보` | Daehan Heunghakbo | Korean Promotion of Learning bulletin |
| `대한유학생회학보` | Daehan Yuhaksaeng Hoehakbo | Korean Students Abroad Association bulletin |
| `서우` | Seo-u | "Western Friend" — Pyongan-area reform society |
| `서북학회월보` | Seobuk Hakhoe Wolbo | Northwest Academic Society monthly |
| `호남학보` | Honam Hakbo | Honam (southwestern) Academic Society bulletin |
| `기호흥학회월보` | Giho Heunghakhoe Wolbo | Giho (central-region) Promotion of Learning monthly |
| `태극학보` | Taegeuk Hakbo | Taegeuk Academic bulletin |
| `대동학회월보` | Daedong Hakhoe Wolbo | Greater East Academic Society monthly |
| `대동아` | Daedonga | "Greater East Asia" (late colonial / wartime) |
| `만국부인` | Mangukbuin | "Women of the World" — early women's magazine |
| `삼천리문학` | Samcheolli Munhak | "Three-thousand Ri Literature" — literary spinoff of Samcheolli |

## `year`

- **Type:** integer (1896–1943)
- **Description:** Publication year. Most articles fall in the 1920s-1930s
  cultural-rule period.

## `article_type`

- **Type:** categorical (Korean originals)
- **Description:** Genre label from the source. Many values, often
  unstandardised across magazines. The most common include:

| Korean value | English gloss |
|---|---|
| `논설` | Editorial / argumentative essay |
| `시` | Poem |
| `소설` | Short fiction / novella |
| `수필` | Essay / personal essay |
| `기행` | Travel writing |
| `평론` | Criticism / review |
| `좌담` | Roundtable transcript |
| `보고` | Report / dispatch |
| `Unknown` | Original source did not record an article type |

For Box Plot grouping, the top three (`논설`, `시`, `소설`) collectively
cover the bulk of the sample.

## `author`

- **Type:** string (Korean / pen names)
- **Description:** Attributed author, where given. Many famous early-20th-century
  Korean writers appear here (e.g. 이광수, 김동인, 백남운). `Unknown` for
  unattributed articles. Treat as descriptive metadata.

## `title`

- **Type:** string (Korean)
- **Description:** Article title.
