"""Build the `kaebyok` slim CSV for BA2 Digital Korea Week 12.

Source: nlp_corpora/data/kaebyok/kaebyok_corpus.csv (2,467 articles, 1920-1935).

Note: there is a multi-year gap between 1926 and 1934 -- the Japanese colonial
authorities banned 開闢 in August 1926, and a different magazine succeeded it
under the same name in 1934. Sampling preserves both clusters.

Sample: stratified 400 articles across the issue-date dimension.

Truncation: text capped at 3,500 characters.

Cleaning: NFC normalisation, whitespace collapse, drop URLs, strip HTML
entities, strip literal \\n / \\r / \\t artefacts.
"""

import re
import unicodedata
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SRC = Path(
    "/PATH/TO/scdenney/nlp_corpora/data/kaebyok/"
    "kaebyok_corpus.csv"
)
RANDOM_STATE = 42
TRUNCATE_CHARS = 3500
TARGET_TOTAL = 400

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
    df = pd.read_csv(SRC)

    df["issue_date"] = pd.to_datetime(df["issue_date"], errors="coerce")
    df = df.dropna(subset=["issue_date", "text"]).copy()
    df["year"] = df["issue_date"].dt.year.astype(int)

    df["text"] = df["text"].apply(clean_text)
    df = df[df["text"].str.len() >= 200].copy()
    df["text"] = df["text"].str.slice(0, TRUNCATE_CHARS)

    # Stratify by year (so the censorship gap is preserved)
    year_counts = df["year"].value_counts().sort_index()
    total = len(df)
    proportional = (year_counts / total * TARGET_TOTAL).round().astype(int).to_dict()

    pieces = []
    for year, g in df.groupby("year"):
        n = min(proportional.get(year, 0), len(g))
        if n > 0:
            pieces.append(g.sample(n=n, random_state=RANDOM_STATE))
    sampled = pd.concat(pieces, ignore_index=True)

    # Trim to exactly target if rounding overshot
    if len(sampled) > TARGET_TOTAL:
        sampled = sampled.sample(n=TARGET_TOTAL, random_state=RANDOM_STATE).reset_index(drop=True)

    sampled["issue_date"] = sampled["issue_date"].dt.strftime("%Y-%m-%d")
    sampled["article_num"] = sampled["article_num"].astype(int)

    sampled = sampled.sort_values(["year", "issue_date", "article_num"]).reset_index(drop=True)
    sampled["doc_id"] = [f"kaebyok_{i:04d}" for i in range(len(sampled))]
    out = sampled[["doc_id", "text", "issue_date", "year", "article_num"]].copy()

    out_path = HERE / "kaebyok_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print("=== kaebyok ===")
    print(f"  rows: {len(out)}")
    print(f"  size: {size_mb:.2f} MB")
    print(f"  year counts:\n{out.year.value_counts().sort_index()}")
    print(
        f"  text length: mean={out.text.str.len().mean():.0f}, "
        f"median={out.text.str.len().median():.0f}, "
        f"max={out.text.str.len().max()}"
    )


if __name__ == "__main__":
    main()
