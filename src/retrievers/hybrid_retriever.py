from __future__ import annotations

from collections import defaultdict
from typing import Any


def min_max_normalize(scores: dict[str, float]) -> dict[str, float]:
    if not scores:
        return {}
    minimum = min(scores.values())
    maximum = max(scores.values())
    if maximum == minimum:
        return {item_id: 1.0 for item_id in scores}
    scale = maximum - minimum
    return {item_id: (score - minimum) / scale for item_id, score in scores.items()}


def fuse_results(
    bm25_rows: list[dict[str, Any]],
    dense_rows: list[dict[str, Any]],
    alpha: float,
    top_k: int,
) -> list[dict[str, Any]]:
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must be between 0 and 1.")

    metadata: dict[str, dict[str, Any]] = {}
    bm25_scores: dict[str, float] = {}
    dense_scores: dict[str, float] = {}

    for row in bm25_rows:
        chunk_id = str(row["chunk_id"])
        metadata[chunk_id] = row
        bm25_scores[chunk_id] = float(row["score"])
    for row in dense_rows:
        chunk_id = str(row["chunk_id"])
        metadata.setdefault(chunk_id, row)
        dense_scores[chunk_id] = float(row["score"])

    normalized_bm25 = min_max_normalize(bm25_scores)
    normalized_dense = min_max_normalize(dense_scores)
    fused_scores: defaultdict[str, float] = defaultdict(float)
    for chunk_id, score in normalized_bm25.items():
        fused_scores[chunk_id] += alpha * score
    for chunk_id, score in normalized_dense.items():
        fused_scores[chunk_id] += (1.0 - alpha) * score

    ranked_ids = sorted(fused_scores, key=fused_scores.get, reverse=True)[:top_k]
    return [
        {
            **metadata[chunk_id],
            "score": fused_scores[chunk_id],
            "bm25_score_normalized": normalized_bm25.get(chunk_id, 0.0),
            "dense_score_normalized": normalized_dense.get(chunk_id, 0.0),
        }
        for chunk_id in ranked_ids
    ]


def reciprocal_rank_fusion(
    bm25_rows: list[dict[str, Any]],
    dense_rows: list[dict[str, Any]],
    rrf_k: int,
    top_k: int,
) -> list[dict[str, Any]]:
    if rrf_k < 0:
        raise ValueError("rrf_k must be non-negative.")

    metadata: dict[str, dict[str, Any]] = {}
    fused_scores: defaultdict[str, float] = defaultdict(float)
    component_ranks: defaultdict[str, dict[str, int | None]] = defaultdict(
        lambda: {"bm25_rank": None, "dense_rank": None}
    )

    for source_name, rows in (("bm25", bm25_rows), ("dense", dense_rows)):
        sorted_rows = sorted(rows, key=lambda row: int(row["rank"]))
        for fallback_rank, row in enumerate(sorted_rows, start=1):
            chunk_id = str(row["chunk_id"])
            rank = int(row.get("rank", fallback_rank))
            metadata.setdefault(chunk_id, row)
            component_ranks[chunk_id][f"{source_name}_rank"] = rank
            fused_scores[chunk_id] += 1.0 / (rrf_k + rank)

    ranked_ids = sorted(fused_scores, key=lambda item_id: (-fused_scores[item_id], item_id))[:top_k]
    return [
        {
            **metadata[chunk_id],
            "score": fused_scores[chunk_id],
            **component_ranks[chunk_id],
        }
        for chunk_id in ranked_ids
    ]
