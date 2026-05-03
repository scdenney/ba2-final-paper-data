"""Build the `inter_korean_summit` slim CSV for BA2 Digital Korea Week 12.

Source: nlp_corpora/data/inter_korean_summit/inter_korean_summit_articles.csv
(article-level file: 455 articles, 2000 / 2007 / 2018 summits, Chosun Ilbo +
Hankyoreh).

Filter: keep all 455 articles (no further sub-sampling).

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
    "/PATH/TO/scdenney/nlp_corpora/data/"
    "inter_korean_summit/inter_korean_summit_articles.csv"
)
RANDOM_STATE = 42
TRUNCATE_CHARS = 3500

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

    # Source already has a 'text' column with article body
    df["text"] = df["text"].apply(clean_text)
    df["title"] = df["headline"].fillna("").apply(clean_text)
    df = df[df["text"].str.len() >= 100].copy()
    df["text"] = df["text"].str.slice(0, TRUNCATE_CHARS)

    # Keep all rows (deterministic sort then re-id)
    df = df.sort_values(["year", "newspaper", "doc_id"]).reset_index(drop=True)
    df["doc_id"] = [f"inter_korean_summit_{i:04d}" for i in range(len(df))]
    df["year"] = df["year"].astype(int)

    out = df[
        ["doc_id", "text", "newspaper", "year", "summit_episode", "title"]
    ].copy()

    out_path = HERE / "inter_korean_summit_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print("=== inter_korean_summit ===")
    print(f"  rows: {len(out)}")
    print(f"  size: {size_mb:.2f} MB")
    print(f"  newspaper x year:\n{out.groupby(['year','newspaper']).size()}")
    print(
        f"  text length: mean={out.text.str.len().mean():.0f}, "
        f"median={out.text.str.len().median():.0f}, "
        f"max={out.text.str.len().max()}"
    )


if __name__ == "__main__":
    main()
