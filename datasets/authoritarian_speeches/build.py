"""Build the `authoritarian_speeches` slim CSV for BA2 Digital Korea Week 12.

Source: nlp_corpora/data/president_speeches/president_speech_ko.csv (8,771 speeches,
1948-2022, 12 South Korean presidents).

Filter: Park Chung-hee (박정희) + Chun Doo-hwan (전두환) + Roh Tae-woo (노태우),
speeches dated on or before 1992-12-31.

Sample: stratified ~600 speeches (200 per president if available).

Truncation: speech_text -> text capped at 3,500 characters.

Cleaning: NFC normalisation, whitespace collapse, drop URLs, strip HTML
entities, strip literal \\n / \\r / \\t artefacts. NO morphological
tokenisation (students do that in Orange).
"""

import re
import unicodedata
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SRC = Path(
    "/PATH/TO/scdenney/nlp_corpora/data/"
    "president_speeches/president_speech_ko.csv"
)
RANDOM_STATE = 42
TRUNCATE_CHARS = 3500
TARGET_PER_PRESIDENT = 200

# Korean -> English president name map
PRESIDENT_MAP = {
    "박정희": "Park Chung-hee",
    "전두환": "Chun Doo-hwan",
    "노태우": "Roh Tae-woo",
}

# Cleaning helpers
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
    df = df.dropna(subset=["date", "speech_text"])
    df["year"] = df["date"].dt.year.astype(int)

    # Filter: three authoritarian-era presidents, before 1993
    df = df[df["president"].isin(PRESIDENT_MAP.keys())].copy()
    df = df[df["date"] <= pd.Timestamp("1992-12-31")].copy()

    # Clean text + truncate
    df["text"] = df["speech_text"].apply(clean_text)
    df = df[df["text"].str.len() >= 200].copy()  # require some substance
    df["text"] = df["text"].str.slice(0, TRUNCATE_CHARS)

    # Stratified sample per president
    pieces = []
    for pres, g in df.groupby("president"):
        n = min(TARGET_PER_PRESIDENT, len(g))
        pieces.append(g.sample(n=n, random_state=RANDOM_STATE))
    sampled = pd.concat(pieces, ignore_index=True)

    # English president labels
    sampled["president"] = sampled["president"].map(PRESIDENT_MAP)
    sampled["kind"] = sampled["kind"].fillna("Unknown").apply(clean_text)
    sampled["location"] = sampled["location"].fillna("Unknown").apply(clean_text)
    sampled["date"] = sampled["date"].dt.strftime("%Y-%m-%d")

    sampled["doc_id"] = [
        f"authoritarian_speeches_{i:04d}" for i in range(len(sampled))
    ]

    out = sampled[
        ["doc_id", "text", "president", "year", "date", "kind", "location"]
    ].copy()

    out_path = HERE / "authoritarian_speeches_sample.csv"
    out.to_csv(out_path, index=False, encoding="utf-8")

    size_mb = out_path.stat().st_size / 1024 / 1024
    print(f"=== authoritarian_speeches ===")
    print(f"  rows: {len(out)}")
    print(f"  size: {size_mb:.2f} MB")
    print(f"  president counts:\n{out.president.value_counts()}")
    print(
        f"  text length: mean={out.text.str.len().mean():.0f}, "
        f"median={out.text.str.len().median():.0f}, "
        f"max={out.text.str.len().max()}"
    )


if __name__ == "__main__":
    main()
