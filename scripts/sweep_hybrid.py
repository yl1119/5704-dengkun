from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.evaluation.retrieval_metrics import evaluate
from src.retrievers.hybrid_retriever import fuse_results, reciprocal_rank_fusion
from src.utils.io import load_jsonl, load_yaml, read_csv, write_csv


def group_rows(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    grouped: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["question_id"]].append(row)
    return grouped


def evaluate_parameter(
    method: str,
    value: float,
    bm25: dict[str, list[dict[str, str]]],
    dense: dict[str, list[dict[str, str]]],
    gold: dict[str, set[str]],
    top_k: int,
    k_values: list[int],
) -> dict[str, float]:
    ranked: dict[str, list[str]] = {}
    for question_id in gold:
        if method == "weighted":
            results = fuse_results(
                bm25.get(question_id, []),
                dense.get(question_id, []),
                alpha=value,
                top_k=top_k,
            )
        else:
            results = reciprocal_rank_fusion(
                bm25.get(question_id, []),
                dense.get(question_id, []),
                rrf_k=int(value),
                top_k=top_k,
            )
        ranked[question_id] = [str(result["chunk_id"]) for result in results]
    return evaluate(ranked, gold, k_values)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sweep weighted or RRF fusion parameters.")
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = load_yaml(args.config)
    method = config["fusion_method"]
    if method not in {"weighted", "rrf"}:
        raise ValueError("fusion_method must be weighted or rrf.")

    bm25 = group_rows(read_csv(config["bm25_results"]))
    dense = group_rows(read_csv(config["dense_results"]))
    questions = load_jsonl(config["questions_path"])
    k_values = [int(value) for value in config["k_values"]]
    parameter_values = config["alpha_values"] if method == "weighted" else config["rrf_k_values"]
    rows = []

    scopes = [("overall", "all", questions)]
    for question_type in sorted({question["question_type"] for question in questions}):
        scopes.append(
            (
                "question_type",
                question_type,
                [question for question in questions if question["question_type"] == question_type],
            )
        )

    for raw_value in parameter_values:
        value = float(raw_value)
        for scope, question_type, scoped_questions in scopes:
            gold = {
                question["question_id"]: set(question["gold_chunk_ids"])
                for question in scoped_questions
            }
            metrics = evaluate_parameter(
                method,
                value,
                bm25,
                dense,
                gold,
                int(config["top_k"]),
                k_values,
            )
            rows.append(
                {
                    "fusion_method": method,
                    "parameter": "alpha" if method == "weighted" else "rrf_k",
                    "parameter_value": raw_value,
                    "scope": scope,
                    "question_type": question_type,
                    "question_count": len(gold),
                    **{name: round(metric, 6) for name, metric in sorted(metrics.items())},
                }
            )
    write_csv(config["output_path"], rows)
    print(f"Wrote {len(rows)} sweep rows to {config['output_path']}")


if __name__ == "__main__":
    main()
