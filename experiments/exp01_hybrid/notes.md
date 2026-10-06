# EXP-003 Hybrid Retrieval

## Purpose

比较 BM25 与 Dense 分数融合后的检索效果。

## Configuration

```text
hybrid_score = alpha * normalized_bm25
             + (1 - alpha) * normalized_dense
```

## Result

当前结果：

- Weighted Hybrid 最优总体 MRR 出现在 `alpha=0.0`，MRR 为 `0.179690`；
- RRF 扫描最优总体 MRR 出现在 `rrf_k=20`，MRR 为 `0.142741`；
- 当前两种融合均未超过 Dense Baseline 的 MRR `0.183690`；
- 该结果只能作为当前自撰数据版本的初步结果，不能直接作为最终论文结论。

完整解释见 `results/retrieval_report.md`。
