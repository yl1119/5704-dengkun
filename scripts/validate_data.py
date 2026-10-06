from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.utils.io import load_jsonl


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate corpus and question JSONL files.")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--questions", required=True)
    args = parser.parse_args()
    corpus = load_jsonl(args.corpus)
    questions = load_jsonl(args.questions)
    chunk_ids = {item["chunk_id"] for item in corpus}
    if len(chunk_ids) != len(corpus):
        raise ValueError("Duplicate chunk_id found in corpus.")
    question_ids = {item["question_id"] for item in questions}
    if len(question_ids) != len(questions):
        raise ValueError("Duplicate question_id found in questions.")
    missing = {
        chunk_id
        for question in questions
        for chunk_id in question["gold_chunk_ids"]
        if chunk_id not in chunk_ids
    }
    if missing:
        raise ValueError(f"Unknown gold chunk IDs: {sorted(missing)}")
    print(f"Valid corpus: {len(corpus)} chunks")
    print(f"Valid questions: {len(questions)} questions")


if __name__ == "__main__":
    main()
