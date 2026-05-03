"""Build the `kpoem` slim CSV for BA2 Digital Korea Week 12.

Source: nlp_corpora/data/kpoem/kpoem_poems.tsv (615 modern Korean poems
with five independent annotators tagging emotion labels).

Sample: keep all 615 poems (no slim).

Convert TSV -> CSV.

The five annotator columns each contain a comma-separated list of
emotion labels (e.g. `슬픔, 비장함, 서러움`). We aggregate them into
a single `dominant_emotion` column: pool every label across all five
annotators, then take the most-voted label per poem. Ties are broken
by first-seen order. We also expose a count `emotion_votes` (how many
annotator-mentions the dominant label received).

Cleaning: NFC normalisation, whitespace collapse, drop URLs, strip HTML
entities, strip literal \\n / \\r / \\t artefacts.
"""

import re
import unicodedata
from collections import Counter
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SRC = Path(
    "/PATH/TO/scdenney/nlp_corpora/data/kpoem/"
    "kpoem_poems.tsv"
)
RANDOM_STATE = 42

ANNOTATOR_COLS = [
    "annotator_01",
    "annotator_02",
    "annotator_03",
    "annotator_04",
    "annotator_05",
]

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


def aggregate_emotions(row) -> tuple[str, int]:
    labels = []
    for col in ANNOTATOR_COLS:
        val = row[col]
        if pd.notna(val):
            labels.extend(
                [unicodedata.normalize("NFC", e.strip()) for e in str(val).split(",") if e.strip()]
            )
    if not labels:
        return ("unlabeled", 0)
    counter = Counter(labels)
    dominant, votes = counter.most_common(1)[0]
    return (dominant, votes)


def main() -> None:
    df = pd.read_csv(SRC, sep="\t")
    df = df.dropna(subset=["text"]).copy()

    df["text"] = df["text"].apply(clean_text)
    df["title"] = df["title"].fillna("").apply(clean_text)
    df["poet"] = df["poet"].fillna("Unknown").apply(clean_text)

    # Aggregate emotion labels
    emotions = df.apply(aggregate_emotions, axis=1)
    df["dominant_emotion"] = [e[0] for e in emotions]
    df["emotion_votes"] = [e[1] for e in emotions]

    df = df.sort_values("poem_id").reset_index(drop=True)
    df["doc_id"] = [f"kpoem_{i:04d}" for i in range(len(df))]

    out = df[
        ["doc_id", "text", "title", "poet", "dominant_emotion", "emotion_votes"]
    ].copy()

    out_path = HERE / "kpoem_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print("=== kpoem ===")
    print(f"  rows: {len(out)}")
    print(f"  size: {size_mb:.2f} MB")
    print(f"  dominant_emotion (top 10):\n{out.dominant_emotion.value_counts().head(10)}")
    print(
        f"  text length: mean={out.text.str.len().mean():.0f}, "
        f"median={out.text.str.len().median():.0f}, "
        f"max={out.text.str.len().max()}"
    )


if __name__ == "__main__":
    main()
