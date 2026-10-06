from __future__ import annotations

import math
import re
from collections import Counter
from typing import Any


def tokenize(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", text.strip().lower())
    # Keep English words and numbers intact while using characters for Chinese
    # text. This dependency-free tokenizer is a reproducible baseline; replace
    # it with a domain tokenizer only through an explicit experiment config.
    tokens: list[str] = []
    for part in re.findall(r"[a-z0-9_]+|[\u4e00-\u9fff]|[^\w\s]", normalized):
        if re.fullmatch(r"[\u4e00-\u9fff]", part):
            tokens.append(part)
        elif part.strip():
            tokens.append(part)
    return tokens


class BM25Retriever:
    def __init__(self, documents: list[dict[str, Any]], k1: float = 1.5, b: float = 0.75):
        if not documents:
            raise ValueError("BM25 requires at least one document.")
        self.documents = documents
        self.k1 = k1
        self.b = b
        self.tokenized_corpus = [tokenize(document["text"]) for document in documents]
        self.term_frequencies = [Counter(tokens) for tokens in self.tokenized_corpus]
        self.document_lengths = [len(tokens) for tokens in self.tokenized_corpus]
        self.average_document_length = sum(self.document_lengths) / len(documents)
        document_frequency: Counter[str] = Counter()
        for tokens in self.tokenized_corpus:
            document_frequency.update(set(tokens))
        self.document_frequency = document_frequency

    def search(self, query: str, top_k: int) -> list[dict[str, Any]]:
        query_terms = tokenize(query)
        document_count = len(self.documents)
        scores: list[float] = []
        for term_frequencies, document_length in zip(self.term_frequencies, self.document_lengths):
            score = 0.0
            for term in query_terms:
                term_frequency = term_frequencies.get(term, 0)
                if term_frequency == 0:
                    continue
                document_frequency = self.document_frequency.get(term, 0)
                idf = math.log(1.0 + (document_count - document_frequency + 0.5) / (document_frequency + 0.5))
                denominator = term_frequency + self.k1 * (
                    1.0 - self.b + self.b * document_length / self.average_document_length
                )
                score += idf * term_frequency * (self.k1 + 1.0) / denominator
            scores.append(score)
        limit = min(top_k, len(self.documents))
        ranked_indices = sorted(range(len(scores)), key=lambda index: (-scores[index], index))[:limit]
        return [
            {
                "chunk_id": self.documents[index]["chunk_id"],
                "doc_id": self.documents[index].get("doc_id", ""),
                "title": self.documents[index].get("title", ""),
                "text": self.documents[index]["text"],
                "score": scores[index],
            }
            for index in ranked_indices
        ]
