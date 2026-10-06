# 文献阅读卡：R02 Dense Retrieval

## 基本信息

- 标题：Dense Passage Retrieval for Open-Domain Question Answering
- 作者：Vladimir Karpukhin 等
- 年份：2020
- 出处：EMNLP
- DOI：10.18653/v1/2020.emnlp-main.550

## 研究问题

如何使用稠密向量表示进行问题到相关段落的检索。

## 方法

采用问题编码器和段落编码器，将问题与段落映射到向量空间并按相似度排序。

## 与本人课题的关系

为 Dense Retrieval 基线和语义改写型问题分析提供依据。

## 对本人实验的启发

需要固定 embedding 模型、相似度函数、归一化方式和索引设置，不能将 Dense 的变化与融合权重变化混在一起。
