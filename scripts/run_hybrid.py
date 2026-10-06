from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.retrievers.hybrid_retriever import fuse_results, reciprocal_rank_fusion
from src.utils.io import load_yaml, read_csv, write_csv


def group_rows(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["question_id"]].append(row)
    return grouped


def main() -> None:
    parser = argparse.ArgumentParser(description="Fuse BM25 and dense retrieval results.")
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = load_yaml(args.config)
    bm25 = group_rows(read_csv(config["bm25_results"]))
    dense = group_rows(read_csv(config["dense_results"]))
    rows = []

    fusion_method = config.get("fusion_method", "weighted")
    for question_id in sorted(set(bm25) | set(dense)):
        if fusion_method == "weighted":
            fused = fuse_results(
                bm25.get(question_id, []),
                dense.get(question_id, []),
                alpha=float(config["alpha"]),
                top_k=int(config["top_k"]),
            )
        elif fusion_method == "rrf":
            fused = reciprocal_rank_fusion(
                bm25.get(question_id, []),
                dense.get(question_id, []),
                rrf_k=int(config["rrf_k"]),
                top_k=int(config["top_k"]),
            )
        else:
            raise ValueError(f"Unsupported fusion_method: {fusion_method}")
        for rank, result in enumerate(fused, start=1):
            rows.append(
                {
                    "question_id": question_id,
                    "rank": rank,
                    "chunk_id": result["chunk_id"],
                    "doc_id": result.get("doc_id", ""),
                    "score": result["score"],
                    "latency_ms": "",
                    "retriever": f"hybrid_{fusion_method}",
                }
            )
    write_csv(config["output_path"], rows)
    print(f"Wrote {len(rows)} rows to {config['output_path']}")


if __name__ == "__main__":
    main()
