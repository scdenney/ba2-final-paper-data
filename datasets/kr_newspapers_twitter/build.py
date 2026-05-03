"""Build the `kr_newspapers_twitter` slim CSV for BA2 Digital Korea Week 12.

Source: nlp_corpora/data/kr_newspapers/korean_newspapers_twitter.csv
(2,748 tweets from six South Korean news outlets, with left/right labels).

Sample: keep all 2,748 rows (source is already only ~600 KB).

No truncation needed (tweets capped at ~155 chars by Twitter character limit
and source download).

Cleaning: NFC normalisation, whitespace collapse, drop URLs, strip HTML
entities, strip literal \\n / \\r / \\t artefacts.
"""

import re
import unicodedata
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SRC = Path(
    "/PATH/TO/scdenney/nlp_corpora/data/kr_newspapers/"
    "korean_newspapers_twitter.csv"
)
RANDOM_STATE = 42

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
    df = df.dropna(subset=["text"]).copy()

    df["text"] = df["text"].apply(clean_text)
    df = df[df["text"].str.len() >= 5].copy()

    # Parse created date to a clean YYYY-MM-DD
    df["created"] = pd.to_datetime(df["created"], errors="coerce")
    df = df.dropna(subset=["created"]).copy()
    df["created"] = df["created"].dt.strftime("%Y-%m-%d")

    df["favoriteCount"] = pd.to_numeric(df["favoriteCount"], errors="coerce").fillna(0).astype(int)
    df["retweetCount"] = pd.to_numeric(df["retweetCount"], errors="coerce").fillna(0).astype(int)

    df = df.sort_values(["paper_name", "created"]).reset_index(drop=True)
    df["doc_id"] = [f"kr_newspapers_twitter_{i:04d}" for i in range(len(df))]

    out = df[
        [
            "doc_id",
            "text",
            "paper_name",
            "created",
            "favoriteCount",
            "retweetCount",
            "pol_id",
        ]
    ].copy()

    out_path = HERE / "kr_newspapers_twitter_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print("=== kr_newspapers_twitter ===")
    print(f"  rows: {len(out)}")
    print(f"  size: {size_mb:.2f} MB")
    print(f"  paper x pol:\n{out.groupby(['paper_name','pol_id']).size()}")
    print(
        f"  text length: mean={out.text.str.len().mean():.0f}, "
        f"median={out.text.str.len().median():.0f}, "
        f"max={out.text.str.len().max()}"
    )


if __name__ == "__main__":
    main()
