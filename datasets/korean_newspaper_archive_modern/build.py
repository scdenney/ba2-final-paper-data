"""Build the `korean_newspaper_archive_modern` slim CSV for BA2 Digital Korea
Week 12.

Source: nlp_corpora/data/korean_newspaper_archive/ (five CSVs covering
1883-1952; ~364K articles total). Each article is tagged with both a
`language` field (Modern Korean / Hanmun / etc.) and a `script` field
(Hangeul / Hanja / mixed).

Filter:
    - year >= 1920
    - language == 'Modern Korean'
    - text length > 500 characters

After filtering, ~2,823 articles remain. Most are concentrated in the late
colonial / early postcolonial regional press (남선신문, 남조선민보).

Sample: stratified 2,500 articles weighted across newspaper x decade.
(With only ~2,823 candidates after filters, we keep nearly all of them.)

Truncation: text capped at 3,500 characters.

Cleaning: NFC normalisation, whitespace collapse, drop URLs, strip HTML
entities, strip literal \\n / \\r / \\t artefacts.
"""

import re
import unicodedata
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SRC_DIR = Path(
    "/PATH/TO/scdenney/nlp_corpora/data/"
    "korean_newspaper_archive"
)
SRC_FILES = [
    "daehan_maeil_sinbo.csv",
    "dongnip_sinmun.csv",
    "hwangseong_sinmun_1898-1904.csv",
    "hwangseong_sinmun_1905-1910.csv",
    "other_newspapers.csv",
]
RANDOM_STATE = 42
# Articles in this slice are mostly 1940s-1950s regional press: short and
# dense. With 2,500 articles capped at 3,500 chars the CSV exceeded the 5 MB
# hard cap. We tighten the truncation to 2,000 chars (median article in
# candidate pool is ~720 chars, so very few articles are actually truncated)
# AND drop the target row count to 2,000 articles to land safely under 5 MB.
TRUNCATE_CHARS = 2000
TARGET_TOTAL = 2000
MIN_TEXT_CHARS = 500
MIN_YEAR = 1920

URL_RE = re.compile(r"https?://\S+|www\.\S+")
HTML_ENTITY_RE = re.compile(r"&[a-zA-Z]+;|&#\d+;")
LITERAL_NL_RE = re.compile(r"\\n|\\r|\\t")
WHITESPACE_RE = re.compile(r"\s+")


def clean_text(s) -> str:
    if not isinstance(s, str):
        return ""
    s = unicodedata.normalize("NFC", s)
    s = LITERAL_NL_RE.sub(" ", s)
    s = URL_RE.sub(" ", s)
    s = HTML_ENTITY_RE.sub(" ", s)
    s = s.replace("​", " ").replace("﻿", " ")
    s = WHITESPACE_RE.sub(" ", s).strip()
    return s


def main() -> None:
    pieces = []
    for fn in SRC_FILES:
        df = pd.read_csv(SRC_DIR / fn)
        pieces.append(df)
    all_df = pd.concat(pieces, ignore_index=True)

    # Source has both 'language' and 'script' columns. Rules use 'language'.
    all_df = all_df.dropna(subset=["text", "year", "language", "newspaper"]).copy()
    all_df["year"] = pd.to_numeric(all_df["year"], errors="coerce").astype("Int64")
    all_df = all_df.dropna(subset=["year"]).copy()
    all_df["year"] = all_df["year"].astype(int)

    all_df = all_df[
        (all_df["year"] >= MIN_YEAR)
        & (all_df["language"] == "Modern Korean")
    ].copy()

    all_df["text"] = all_df["text"].apply(clean_text)
    all_df = all_df[all_df["text"].str.len() > MIN_TEXT_CHARS].copy()
    all_df["text"] = all_df["text"].str.slice(0, TRUNCATE_CHARS)

    all_df["title"] = all_df["title"].fillna("").apply(clean_text)
    all_df["url"] = all_df["url"].fillna("").astype(str)
    all_df["decade"] = (all_df["year"] // 10 * 10).astype(int)

    # Stratified sample by newspaper x decade
    pieces = []
    candidate_counts = all_df.groupby(["newspaper", "decade"]).size()
    total_candidates = candidate_counts.sum()
    for (np_name, decade), g in all_df.groupby(["newspaper", "decade"]):
        proportional = max(1, round(len(g) / total_candidates * TARGET_TOTAL))
        n = min(proportional, len(g))
        pieces.append(g.sample(n=n, random_state=RANDOM_STATE))
    sampled = pd.concat(pieces, ignore_index=True)

    # If overshoot, sample down to TARGET_TOTAL
    if len(sampled) > TARGET_TOTAL:
        sampled = sampled.sample(n=TARGET_TOTAL, random_state=RANDOM_STATE).reset_index(drop=True)

    sampled = sampled.sort_values(["year", "newspaper"]).reset_index(drop=True)
    sampled["doc_id"] = [
        f"korean_newspaper_archive_modern_{i:04d}" for i in range(len(sampled))
    ]

    out = sampled[
        ["doc_id", "text", "year", "newspaper", "title", "url"]
    ].copy()

    out_path = HERE / "korean_newspaper_archive_modern_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print("=== korean_newspaper_archive_modern ===")
    print(f"  rows: {len(out)}")
    print(f"  size: {size_mb:.2f} MB")
    print(f"  newspaper counts:\n{out.newspaper.value_counts()}")
    print(f"  decade counts:\n{(out.year // 10 * 10).value_counts().sort_index()}")
    print(
        f"  text length: mean={out.text.str.len().mean():.0f}, "
        f"median={out.text.str.len().median():.0f}, "
        f"max={out.text.str.len().max()}"
    )


if __name__ == "__main__":
    main()
