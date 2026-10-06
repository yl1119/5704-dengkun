from __future__ import annotations

import math
from collections import defaultdict
from typing import Iterable


def group_ranked_results(rows: Iterable[dict[str, str]]) -> dict[str, list[str]]:
    grouped: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["question_id"]].append((int(row["rank"]), row["chunk_id"]))
    return {
        question_id: [chunk_id for _, chunk_id in sorted(items)]
        for question_id, items in grouped.items()
    }


def recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        return 0.0
    return len(set(retrieved[:k]) & relevant) / len(relevant)


def hit_rate_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    return float(bool(set(retrieved[:k]) & relevant))


def reciprocal_rank(retrieved: list[str], relevant: set[str]) -> float:
    for rank, chunk_id in enumerate(retrieved, start=1):
        if chunk_id in relevant:
            return 1.0 / rank
    return 0.0


def ndcg_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    dcg = sum(
        1.0 / math.log2(rank + 1)
        for rank, chunk_id in enumerate(retrieved[:k], start=1)
        if chunk_id in relevant
    )
    ideal_hits = min(len(relevant), k)
    idcg = sum(1.0 / math.log2(rank + 1) for rank in range(1, ideal_hits + 1))
    return dcg / idcg if idcg else 0.0


def evaluate(
    ranked_results: dict[str, list[str]],
    gold: dict[str, set[str]],
    k_values: list[int],
) -> dict[str, float]:
    if not gold:
        raise ValueError("Gold questions cannot be empty.")
    totals: defaultdict[str, float] = defaultdict(float)
    for question_id, relevant in gold.items():
        retrieved = ranked_results.get(question_id, [])
        totals["MRR"] += reciprocal_rank(retrieved, relevant)
        for k in k_values:
            totals[f"Recall@{k}"] += recall_at_k(retrieved, relevant, k)
            totals[f"HitRate@{k}"] += hit_rate_at_k(retrieved, relevant, k)
            totals[f"nDCG@{k}"] += ndcg_at_k(retrieved, relevant, k)
    question_count = len(gold)
    return {name: value / question_count for name, value in totals.items()}
