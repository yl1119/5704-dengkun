from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.utils.io import read_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Plot a fusion-parameter metric curve.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--metric", default="MRR")
    parser.add_argument("--question-type", default="all")
    args = parser.parse_args()

    rows = [
        row
        for row in read_csv(args.input)
        if row["question_type"] == args.question_type
    ]
    if not rows:
        raise ValueError(f"No rows found for question type: {args.question_type}")
    rows.sort(key=lambda row: float(row["parameter_value"]))
    x_values = [float(row["parameter_value"]) for row in rows]
    y_values = [float(row[args.metric]) for row in rows]
    parameter_name = rows[0]["parameter"]

    plt.figure(figsize=(7, 4.5))
    plt.plot(x_values, y_values, marker="o")
    plt.xlabel(parameter_name)
    plt.ylabel(args.metric)
    plt.title(f"{args.metric} vs {parameter_name} ({args.question_type})")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=200)
    print(f"Saved curve to {output_path}")


if __name__ == "__main__":
    main()
