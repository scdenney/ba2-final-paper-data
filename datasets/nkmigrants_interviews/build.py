"""Build the `nkmigrants_interviews` slim CSV for BA2 Digital Korea Week 12.

Source: nlp_corpora/data/nkmigrants_interviews/nkmigrants_interviews.csv
(6,027 open-text survey responses from a South Korean attitudinal survey
on relations with North Korean migrants -- three response_types per
respondent: hire / neighbor / vote).

Sample: keep all 6,027 rows (source is ~4.4 MB, under the 5 MB cap).

Caveat: median text length ~9 characters. Same caveat as immigrant_interviews
-- short responses, suitable for sentiment + simple clustering, NOT LDA at
the response level. To do anything interesting with topics, students should
aggregate by `respid` x `response_type` (concatenate the three response_types
per respondent, or compare hire-pile vs neighbor-pile vs vote-pile across
respondents).

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
    "nkmigrants_interviews/nkmigrants_interviews.csv"
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
    df["text"] = df["response_text"].apply(clean_text)
    df = df[df["text"].str.len() >= 1].copy()

    df = df.sort_values(["respid", "response_type"]).reset_index(drop=True)
    df["doc_id"] = [f"nkmigrants_interviews_{i:04d}" for i in range(len(df))]

    out = df[
        [
            "doc_id",
            "text",
            "response_type",
            "sex",
            "age_cohorts",
            "political_id3",
            "close_nkmigrants",
        ]
    ].copy()

    out_path = HERE / "nkmigrants_interviews_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print("=== nkmigrants_interviews ===")
    print(f"  rows: {len(out)}")
    print(f"  size: {size_mb:.2f} MB")
    print(
        f"  text length: mean={out.text.str.len().mean():.1f}, "
        f"median={out.text.str.len().median()}, "
        f"max={out.text.str.len().max()}"
    )
    print(f"  response_type counts:\n{out.response_type.value_counts()}")


if __name__ == "__main__":
    main()
