from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.evaluation.retrieval_metrics import evaluate, group_ranked_results
from src.utils.io import load_jsonl, load_yaml, read_csv, write_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate retrieval result CSV files.")
    parser.add_argument("--config", required=True)
    parser.add_argument("--results", required=True)
    args = parser.parse_args()
    config = load_yaml(args.config)
    questions = load_jsonl(config["questions_path"])
    gold = {
        question["question_id"]: set(question["gold_chunk_ids"])
        for question in questions
    }
    result_rows = read_csv(args.results)
    ranked_results = group_ranked_results(result_rows)
    metrics = evaluate(ranked_results, gold, [int(value) for value in config["k_values"]])
    overall_row = {
        "scope": "overall",
        "question_type": "all",
        "results_file": args.results,
        "question_count": len(gold),
        **{name: round(value, 6) for name, value in sorted(metrics.items())},
    }
    output_rows = [overall_row]
    question_types = sorted({question["question_type"] for question in questions})
    for question_type in question_types:
        typed_questions = [
            question for question in questions if question["question_type"] == question_type
        ]
        typed_gold = {
            question["question_id"]: set(question["gold_chunk_ids"])
            for question in typed_questions
        }
        typed_metrics = evaluate(
            ranked_results,
            typed_gold,
            [int(value) for value in config["k_values"]],
        )
        output_rows.append(
            {
                "scope": "question_type",
                "question_type": question_type,
                "results_file": args.results,
                "question_count": len(typed_gold),
                **{name: round(value, 6) for name, value in sorted(typed_metrics.items())},
            }
        )
    write_csv(config["output_path"], output_rows)
    print(json.dumps(output_rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
