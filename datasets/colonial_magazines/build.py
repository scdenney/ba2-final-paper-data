"""Build the `colonial_magazines` slim CSV for BA2 Digital Korea Week 12.

Source: nlp_corpora/data/colonial_magazines/ -- five files:
    - kaebyok.csv          (개벽,    1920-1935, 2,462 rows)
    - samcheolli.csv       (삼천리,  1929-1942, 4,093 rows)
    - byeolgeongon.csv     (별건곤,  1926-1934, 2,847 rows)
    - donggwang.csv        (동광,    1926-1933, 1,434 rows)
    - other_magazines.csv  (various, 1896-1943, 4,490 rows)

Combined: ~15,326 articles.

Sample: stratified 500 articles, weighted across magazine title
(proportional, capped per magazine to keep diversity).

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
    "/PATH/TO/scdenney/nlp_corpora/data/colonial_magazines"
)
SRC_FILES = [
    "kaebyok.csv",
    "samcheolli.csv",
    "byeolgeongon.csv",
    "donggwang.csv",
    "other_magazines.csv",
]
RANDOM_STATE = 42
TRUNCATE_CHARS = 3500
TARGET_TOTAL = 500

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

    # Drop missing/empty text + clean + filter for substance
    all_df = all_df.dropna(subset=["text", "magazine"]).copy()
    all_df["text"] = all_df["text"].apply(clean_text)
    all_df = all_df[all_df["text"].str.len() >= 200].copy()
    all_df["text"] = all_df["text"].str.slice(0, TRUNCATE_CHARS)

    # Stratify by magazine title. Strategy:
    #   1. Allocate a baseline of 18 articles per magazine (so even tiny
    #      magazines get representation).
    #   2. Distribute the remaining budget proportionally to magazine size.
    #   3. Cap at the actual available count per magazine.
    mag_counts = all_df["magazine"].value_counts()
    n_mags = len(mag_counts)
    BASELINE = 18
    baseline_total = sum(min(BASELINE, c) for c in mag_counts.values)
    remainder = TARGET_TOTAL - baseline_total
    big_mags = mag_counts[mag_counts > BASELINE]
    big_total = big_mags.sum()
    proportional = {}
    for mag, count in mag_counts.items():
        baseline = min(BASELINE, count)
        bonus = 0
        if mag in big_mags.index and remainder > 0:
            bonus = round((count / big_total) * remainder)
        proportional[mag] = min(baseline + bonus, count)

    pieces = []
    for mag, g in all_df.groupby("magazine"):
        n = min(proportional.get(mag, 0), len(g))
        if n > 0:
            pieces.append(g.sample(n=n, random_state=RANDOM_STATE))
    sampled = pd.concat(pieces, ignore_index=True)

    # Trim if rounding overshot
    if len(sampled) > TARGET_TOTAL:
        sampled = sampled.sample(n=TARGET_TOTAL, random_state=RANDOM_STATE).reset_index(drop=True)

    sampled["author"] = sampled["author"].fillna("Unknown").apply(clean_text)
    sampled["title"] = sampled["title"].fillna("").apply(clean_text)
    sampled["article_type"] = sampled["article_type"].fillna("Unknown").apply(clean_text)
    sampled["year"] = pd.to_numeric(sampled["year"], errors="coerce").astype("Int64")
    sampled = sampled.dropna(subset=["year"]).copy()
    sampled["year"] = sampled["year"].astype(int)

    sampled["doc_id"] = [f"colonial_magazines_{i:04d}" for i in range(len(sampled))]
    out = sampled[
        ["doc_id", "text", "magazine", "year", "article_type", "author", "title"]
    ].copy()

    out_path = HERE / "colonial_magazines_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print("=== colonial_magazines ===")
    print(f"  rows: {len(out)}")
    print(f"  size: {size_mb:.2f} MB")
    print(f"  magazine counts:\n{out.magazine.value_counts()}")
    print(
        f"  text length: mean={out.text.str.len().mean():.0f}, "
        f"median={out.text.str.len().median():.0f}, "
        f"max={out.text.str.len().max()}"
    )


if __name__ == "__main__":
    main()
