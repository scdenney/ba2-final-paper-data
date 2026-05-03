"""Build the `immigrant_interviews` slim CSV for BA2 Digital Korea Week 12.

Source: nlp_corpora/data/immigrant_interviews/immigrant_interview.csv
(1,008 open-text survey responses from a South Korean attitudinal survey on
who should be admitted as immigrants).

Sample: keep all 1,008 rows (source is already only ~90 KB).

Caveat: median text length ~11 characters. These are 1-2 word phrases, not
documents. Suitable for sentiment scoring or simple clustering on short
responses; NOT suitable for LDA topic modelling at the response level.

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
    "immigrant_interviews/immigrant_interview.csv"
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
    df["text"] = df["text"].apply(clean_text)
    df = df[df["text"].str.len() >= 1].copy()

    df = df.sort_values("respid").reset_index(drop=True)
    df["doc_id"] = [f"immigrant_interviews_{i:04d}" for i in range(len(df))]

    out = df[
        ["doc_id", "text", "sex", "age_cohort", "political_id3", "college"]
    ].copy()

    out_path = HERE / "immigrant_interviews_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print("=== immigrant_interviews ===")
    print(f"  rows: {len(out)}")
    print(f"  size: {size_mb:.2f} MB")
    print(
        f"  text length: mean={out.text.str.len().mean():.1f}, "
        f"median={out.text.str.len().median()}, "
        f"max={out.text.str.len().max()}"
    )
    print(f"  political_id3 counts:\n{out.political_id3.value_counts()}")


if __name__ == "__main__":
    main()
