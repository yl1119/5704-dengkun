# 文献阅读卡：R05 RRF

## 基本信息

- 标题：Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods
- 作者：Gordon V. Cormack; Charles L. A. Clarke; Stefan Büttcher
- 年份：2009
- 出处：SIGIR
- DOI：10.1145/1571941.1572114

## 方法

RRF 根据不同检索器返回的排名计算融合分数，不要求不同检索器的原始分数处于相同尺度。

## 与本人课题的关系

作为分数加权融合之外的第二种 Hybrid 方法，用于融合方式消融。

## 对本人实验的启发

需要单独研究 `rrf_k`，并比较 RRF 与 Min-Max 归一化加权融合在四类问题上的差异。
