from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.retrievers.bm25_retriever import BM25Retriever
from src.utils.io import load_jsonl, load_yaml, write_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the BM25 retrieval baseline.")
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = load_yaml(args.config)
    documents = load_jsonl(config["corpus_path"])
    questions = load_jsonl(config["questions_path"])
    retriever = BM25Retriever(documents, k1=float(config["k1"]), b=float(config["b"]))

    rows = []
    for question in questions:
        started = time.perf_counter()
        results = retriever.search(question["question"], int(config["top_k"]))
        latency_ms = (time.perf_counter() - started) * 1000
        for rank, result in enumerate(results, start=1):
            rows.append(
                {
                    "question_id": question["question_id"],
                    "rank": rank,
                    "chunk_id": result["chunk_id"],
                    "doc_id": result["doc_id"],
                    "score": result["score"],
                    "latency_ms": latency_ms,
                    "retriever": "bm25",
                }
            )
    write_csv(config["output_path"], rows)
    print(f"Wrote {len(rows)} rows to {config['output_path']}")


if __name__ == "__main__":
    main()
