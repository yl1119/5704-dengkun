from __future__ import annotations

from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer


class DenseRetriever:
    def __init__(
        self,
        documents: list[dict[str, Any]],
        model_name: str,
        normalize_embeddings: bool = True,
        batch_size: int = 32,
    ):
        if not documents:
            raise ValueError("Dense retrieval requires at least one document.")
        self.documents = documents
        self.model = SentenceTransformer(model_name)
        self.normalize_embeddings = normalize_embeddings
        self.document_embeddings = self.model.encode(
            [document["text"] for document in documents],
            batch_size=batch_size,
            show_progress_bar=True,
            normalize_embeddings=normalize_embeddings,
            convert_to_numpy=True,
        )

    def search(self, query: str, top_k: int) -> list[dict[str, Any]]:
        query_embedding = self.model.encode(
            [query],
            normalize_embeddings=self.normalize_embeddings,
            convert_to_numpy=True,
        )[0]
        scores = np.asarray(self.document_embeddings @ query_embedding, dtype=float)
        limit = min(top_k, len(self.documents))
        ranked_indices = np.argsort(-scores, kind="stable")[:limit]
        return [
            {
                "chunk_id": self.documents[index]["chunk_id"],
                "doc_id": self.documents[index].get("doc_id", ""),
                "title": self.documents[index].get("title", ""),
                "text": self.documents[index]["text"],
                "score": float(scores[index]),
            }
            for index in ranked_indices
        ]
