# `nikh_textbooks_hs` Data Dictionary

A reference key for the 21-textbook high-school slice of the NIKH history-textbook
corpus, restricted to the Authoritarian (1973–1990) and Democratic (1996–2016) eras.
Use this if a Korean categorical label slows you down — it is not meant to teach you
the curricular history; that is what you discover by reading the textbooks.

---

## `doc_id`

- **Type:** string
- **Description:** Synthetic ID, zero-padded.
- **Example:** `nikh_hs_0007`

## `text`

- **Type:** string (Korean, NFC-normalized)
- **Description:** The cleaned textbook body. Truncated to the first 5,000
  characters; this captures roughly the opening chapters (framing material,
  early-period coverage). Original full-text length per book ranges from
  ~170,000 to ~460,000 characters.
- **Example:** `대한민국의 역사는 …`

## `era`

- **Type:** categorical
- **Description:** Curator-assigned historical era. Two values in this slice.

| Value | Approximate years | Curricula included | Count |
|---|---|---|---|
| `Authoritarian` | 1973–1990 | 3rd, 4th, 5th National Curricula (state-monopoly publication) | 7 |
| `Democratic` | 1996–2016 | 6th, 7th, and 7th-revised Curricula (diversified publishers) | 14 |

The original NIKH `period` column has five values (`Late Choson`, `Colonial`,
`Postwar`, `Authoritarian`, `Democratic`); this slice keeps only the last two.

## `year`

- **Type:** integer (1973–2016)
- **Description:** Year of textbook publication. Authoritarian rows
  cluster in the 1973–1990 window; Democratic rows span 1996–2016 with
  several from the mid-2000s curricular reforms.

## `level`

- **Type:** categorical
- **Description:** Educational level. Always `High School` in this slice
  (kept for transparency; the source corpus also includes Elementary,
  Middle School, Public schools, and General).

## `book_id`

- **Type:** string
- **Description:** Original NIKH identifier. Two formats:

| Format | Source | Example |
|---|---|---|
| `ta_*` | NIKH digitized series (clean digital text) | `ta_h31`, `ta_h71` |
| `H-*` | Revised 7th Curriculum (DeepSeek-OCR'd from PDFs, then cleaned) | `H-10(4,2007)`, `H-54(2,2016)` |

The `H-*` identifiers encode publisher ID and edition year in parentheses.

## `title`

- **Type:** string (Korean)
- **Description:** Full textbook title. Common patterns: `고등학교 국사`
  (High School National History) for the state-monopoly era; `한국사` (Korean
  History) and `한국근현대사` (Korean Modern and Contemporary History) for
  the post-7th-Curriculum era.

## `curriculum`

- **Type:** categorical
- **Description:** Named national curriculum. Values in this slice:
  `3rd Curriculum`, `4th Curriculum`, `5th Curriculum`, `5th-6th Transition`,
  `6th Curriculum`, `7th Curriculum`, `7th Curriculum (Revised)`.

## `nikh_period`

- **Type:** categorical
- **Description:** Source-assigned curriculum period (longer-form labels
  paralleling `curriculum`). Examples:
  `3rd National Curriculum (1973-1981)`, `7th National Curriculum (2002–)`.

## `publisher`

- **Type:** string (Korean)
- **Description:** Publishing institution. Authoritarian-era books are
  published by the Ministry of Education (`문교부`, the pre-1990 name).
  Democratic-era books include both ministry editions (`교육부`,
  `교육인적자원부`) and approved private publishers (e.g. `천재교육`,
  `금성출판사`, `지학사`).

| Korean | English | Era |
|---|---|---|
| `문교부` | Ministry of Education (pre-1990 name) | Authoritarian (1st–4th Curricula) |
| `교육부` | Ministry of Education | Democratic (5th–6th Curricula, 1987–2002) |
| `교육인적자원부` | Ministry of Education and Human Resources Development | Democratic (7th Curriculum) |
| `천재교육`, `금성출판사`, `지학사` | Private publishers approved under the revised 7th Curriculum | Democratic (post-2002) |
