# Preprocessing notes — final paper menu

The default Python preprocessing scripts on the BA2 [Data &amp; Scripts](https://scdenney.github.io/ba2-digital-korea/data/) page (`custom_preprocessing_*.py`, `sentiment_preprocessing_*.py`) work cleanly on most corpora. Four corpora need a different approach. **Find your corpus in the table below — if a "yes" appears in any column, read that section before you start.**

| Corpus | Hanja-heavy (§1) | English-only (§2) | Short text (§3) | Emotion / irregular V&A (§4) |
|---|:---:|:---:|:---:|:---:|
| authoritarian_speeches | — | — | — | — |
| **colonial_magazines** | **yes** | — | — | use after §1 |
| **immigrant_interviews** | — | — | **yes** | — |
| inter_korean_summit | — | — | — | — |
| **kaebyok** | **yes** | — | — | **yes** |
| **korean_newspaper_archive_modern** | **yes** | — | — | — |
| kpoem | — | — | — | — |
| **kr_newspapers_twitter** | — | — | **yes** (mild) | — |
| nikh_textbooks_hs | — | — | — | — |
| **nkmigrants_interviews** | — | — | **yes** | — |
| **rodong_sinmun_en** | — | **yes** | — | n/a |

If your row is all dashes, the default `sentiment_preprocessing_*.py` or `custom_preprocessing_*.py` will work as-is. If anything affecting your corpus shaped your preprocessing, mention it briefly in your data &amp; methods section.

The audit below was run on a sample of 80 documents per corpus in May 2026.

---

## §1. Hanja-heavy corpora — use `hanja_preprocessing_*.py`

Affects: **colonial_magazines · kaebyok · korean_newspaper_archive_modern**

These three colonial-era corpora contain **a quarter to a third Hanja (Chinese-character) text**. The default script tokenizes the Korean parts but treats each Hanja character as an unknown symbol and drops it. You will lose roughly a quarter of the meaning-bearing tokens.

| Corpus | % Hanja characters | % docs containing Hanja |
|---|---|---|
| colonial_magazines | 26% | 100% |
| kaebyok | 27% | 100% |
| korean_newspaper_archive_modern | 34% | 100% |

**What to do:** download `hanja_preprocessing_mac-users.py` (or `hanja_preprocessing_windows-users.py`) instead of the standard preprocessing script. It auto-installs the `hanja` package, converts each Hanja character to its Korean (Hangul) reading, *then* runs Kiwi tokenization. Drop the script into Orange's Python Script widget the same way you dropped in the standard one.

**Trade-off to mention in your write-up:** the conversion is a substitution, not an interpretation. A reader fluent in 한문 would distinguish meanings that the Hangul reading collapses (e.g. 國 → 국 conflates "nation" with anything else read 국). Good enough for distant-reading; not enough for a deep philological analysis.

---

## §2. English-only corpus — do not use the Korean script

Affects: **rodong_sinmun_en**

Kiwi is a *Korean* tokenizer; it produces nothing useful on English text. Our audit confirmed this: 80 of 80 sampled documents return zero tokens after the Korean POS filter.

**What to do:**

- Skip the Python script entirely. Use Orange's built-in **Preprocess Text** widget with English settings (lowercase, English stopwords, regular-expression tokenizer with `\w+`, optionally Porter stemmer). Connect a **Bag of Words** widget after it.
- For sentiment analysis, do **not** use the KNU dictionary (Korean). Use **VADER** or **AFINN**, both supported in Orange's Sentiment Analysis widget.

This is the standard English text-mining pipeline — closer to most public Orange tutorials.

---

## §3. Short-text corpora — choose your method carefully

Affects: **immigrant_interviews · nkmigrants_interviews · kr_newspapers_twitter**

These corpora have very short documents — too short for LDA and TF-IDF clustering to produce stable output.

| Corpus | Mean chars/doc | Docs with &lt; 5 tokens after POS filter |
|---|---|---|
| immigrant_interviews | 18 | 64 of 80 |
| nkmigrants_interviews | 13 | 66 of 80 |
| kr_newspapers_twitter | 37 | 12 of 80 |

The default Python script still tokenizes correctly — the issue is downstream, not in preprocessing. Pick a method that works with short documents:

| Method | Short-text fit |
|---|---|
| Sentiment via KNU dictionary | **fine** (short docs simply have fewer hits — that is realistic) |
| KLUE BERT embeddings + clustering | **fine** (each document is a single vector regardless of length) |
| LDA / topic modeling | **avoid** (most docs collapse to 1–3 tokens; topics will be noise) |
| TF-IDF + hierarchical clustering | **avoid for interviews**, marginal for Twitter |

If you want LDA on these corpora, **concatenate** within a meaningful unit before modeling — e.g. all answers by the same interviewee, or all tweets from the same outlet.

---

## §4. Korean emotion-bearing irregular adjectives — extend `POS_TAGS` if you do sentiment analysis

Affects: **kaebyok** (24% irregular tokens) most strongly. Optional for any Korean corpus where you do dictionary-based sentiment analysis.

Kiwi has separate tags for *irregular* verbs and adjectives (`VV-I`, `VA-I`, plus `VV-R`, `VA-R`). **Most emotion-bearing adjectives in Korean are irregular**: 외롭다 (lonely), 괴롭다 (in pain), 부끄럽다 (ashamed), 그립다 (longing), 슬프다, 어렵다, 아름답다 — all `VA-I`. The default `sentiment_preprocessing_*.py` keeps only `NNG`, `NNP`, `VV`, `VA` and drops these.

For prose corpora the loss is small (≤ 2%). For kaebyok and other early-20th-century material it climbs to ~24%.

**What to do:** open the `sentiment_preprocessing_*.py` script you downloaded and add four lines to the `POS_TAGS` list:

```python
POS_TAGS = [
    'NNG',
    'NNP',
    'VV',
    'VA',
    'VV-I',   # irregular verb stems (듣, 짓)
    'VA-I',   # irregular adjective stems (괴롭, 외롭, 슬프)
    'VV-R',   # rare alternate-form verbs
    'VA-R',   # rare alternate-form adjectives
]
```

**One related caveat — the KNU dictionary stores full dictionary forms (괴롭다, with `-다`); Kiwi outputs bare stems (괴롭, without `-다`).** So even after you add `VA-I`, the stem `괴롭` will not directly match the KNU entry `괴롭다`. Two ways to handle this:

- **Cleaner:** in the dictionary-loading step, strip a trailing `다` from any KNU entry that ends in `다`. Now both your tokens and the dictionary entries are in stem form.
- **Quicker but lossier:** append `다` to each verb/adjective token before scoring.

This caveat only matters for verbs and adjectives. KNU's *noun* entries (사랑, 괴로움, 슬픔) match Kiwi's noun output directly — and that's where most polarity in prose lives. The issue is most visible on emotion-heavy material.
