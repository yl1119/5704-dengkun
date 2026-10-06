from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.retrievers.dense_retriever import DenseRetriever
from src.utils.io import load_jsonl, load_yaml, write_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the dense retrieval baseline.")
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = load_yaml(args.config)
    documents = load_jsonl(config["corpus_path"])
    questions = load_jsonl(config["questions_path"])
    retriever = DenseRetriever(
        documents,
        model_name=config["embedding_model"],
        normalize_embeddings=bool(config.get("normalize_embeddings", True)),
        batch_size=int(config.get("batch_size", 32)),
    )

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
                    "retriever": "dense",
                }
            )
    write_csv(config["output_path"], rows)
    print(f"Wrote {len(rows)} rows to {config['output_path']}")


if __name__ == "__main__":
    main()
