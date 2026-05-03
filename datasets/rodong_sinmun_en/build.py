"""Build the `rodong_sinmun_en` slim CSV for BA2 Digital Korea Week 12.

Source: nlp_corpora/data/rodong_sinmun/rodong_sinmun_en.csv
(9,797 English-language Rodong Sinmun articles, 2018-01-02 to 2022-06-03).

Filter: keep 2018-01-01 through 2021-12-31 only -- drops sparse 2022.

Sample: stratified 600 articles weighted by year.

Truncation: body -> text capped at 3,500 characters.

Cleaning: NFC normalisation, whitespace collapse, drop URLs, strip HTML
entities, strip literal \\n / \\r / \\t artefacts.

Note: this corpus is in ENGLISH, not Korean -- it suits the syllabus's
accommodation clause for non-Korean readers. The KNU sentiment dictionary
will not work; students should use a different sentiment approach (e.g. a
small custom dictionary, or VADER) or focus on a non-sentiment method
(clustering, embeddings, LDA).
"""

import re
import unicodedata
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SRC = Path(
    "/PATH/TO/scdenney/nlp_corpora/data/"
    "rodong_sinmun/rodong_sinmun_en.csv"
)
RANDOM_STATE = 42
TRUNCATE_CHARS = 3500
TARGET_TOTAL = 600

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
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "body"]).copy()
    df = df[
        (df["date"] >= pd.Timestamp("2018-01-01"))
        & (df["date"] <= pd.Timestamp("2021-12-31"))
    ].copy()

    df["year"] = df["date"].dt.year.astype(int)
    df["text"] = df["body"].apply(clean_text)
    df = df[df["text"].str.len() >= 100].copy()
    df["text"] = df["text"].str.slice(0, TRUNCATE_CHARS)

    df["title"] = df["title"].fillna("").apply(clean_text)
    df["url"] = df["url"].fillna("").astype(str)

    # Stratified by year
    year_counts = df["year"].value_counts().sort_index()
    total = len(df)
    proportional = (year_counts / total * TARGET_TOTAL).round().astype(int).to_dict()

    pieces = []
    for year, g in df.groupby("year"):
        n = min(proportional.get(year, 0), len(g))
        if n > 0:
            pieces.append(g.sample(n=n, random_state=RANDOM_STATE))
    sampled = pd.concat(pieces, ignore_index=True)

    if len(sampled) > TARGET_TOTAL:
        sampled = sampled.sample(n=TARGET_TOTAL, random_state=RANDOM_STATE).reset_index(drop=True)

    sampled["date"] = sampled["date"].dt.strftime("%Y-%m-%d")
    sampled = sampled.sort_values(["year", "date"]).reset_index(drop=True)
    sampled["doc_id"] = [f"rodong_sinmun_en_{i:04d}" for i in range(len(sampled))]

    out = sampled[["doc_id", "text", "date", "year", "title", "url"]].copy()

    out_path = HERE / "rodong_sinmun_en_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print("=== rodong_sinmun_en ===")
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
