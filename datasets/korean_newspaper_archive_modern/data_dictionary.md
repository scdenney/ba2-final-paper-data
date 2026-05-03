# `korean_newspaper_archive_modern` Data Dictionary

A reference key for the 2,000-article sample of late-colonial /
liberation-era Korean-language newspaper articles.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `korean_newspaper_archive_modern_0042`

## `text`

- **Type:** string (Korean, NFC-normalized)
- **Description:** The cleaned article body. Truncated to the first
  2,000 characters; shorter articles are kept in full.
- **Length stats:** mean ~820 characters, median ~720, max 2,000.

## `year`

- **Type:** integer (1920–1952)
- **Description:** Publication year.

| Decade | Articles |
|---|---:|
| 1920s | ~19 |
| 1930s | ~21 |
| 1940s | ~1,046 |
| 1950s | ~914 |

The 1940s-1950s skew is a faithful reflection of which Modern-Korean
long-form articles survive in the source archive (most pre-1940 Korean
newspaper articles use Hanmun or mixed Hanja-Hangeul script and are
therefore filtered out by the `language == 'Modern Korean'` rule).

## `newspaper`

- **Type:** categorical (Korean originals)
- **Description:** Newspaper title. 14 values in the sample, but two
  dominate.

| Korean value | Romanization | Period | Region | Notes |
|---|---|---|---|---|
| `남조선민보` | Namjoseon Minbo | mid-1940s | South (Busan/Masan area) | Largest single source — liberation-era regional daily |
| `마산일보` | Masan Ilbo | late-1940s/1950s | South (Masan) | Second-largest source |
| `남선신문` | Namseon Sinmun | 1940s | South | Regional |
| `매일신보` | Maeil Sinbo | 1920s-1940s | National (colonial-era) | Government-General mouthpiece |
| `조선신문` | Joseon Sinmun | 1920s-1930s | National | |
| `조선시보` | Joseon Sibo | 1920s | Busan | Mostly Japanese-language paper, this is the Korean section |
| `조선중앙일보(여운형)` | Joseon Jungang Ilbo (Yeo Un-hyung) | 1930s | National | Edited by Yo Un-hyong |
| `중외일보` | Jungwoe Ilbo | 1920s-1930s | National | |
| `대한일보` | Daehan Ilbo | late 1940s | South | |
| `중앙일보` | Jungang Ilbo | 1930s-1940s | National | |
| `중앙신문` | Jungang Sinmun | 1940s | National | |
| `평화일보` | Pyeonghwa Ilbo | late 1940s | South | |
| `국제신문` | Gukje Sinmun | late 1940s | South | |
| `경성일보` | Gyeongseong Ilbo | 1920s | Seoul (colonial) | Mostly Japanese-language paper |

For Box Plot grouping, filter to the top 3-4 newspapers to avoid
many-tiny-bars problems.

## `title`

- **Type:** string (Korean)
- **Description:** Article headline.

## `url`

- **Type:** string
- **Description:** URL to the original archive entry on the NIKH
  (National Institute of Korean History) database. Useful for
  spot-checking individual articles. Some entries may be empty if the
  source did not record a URL.
