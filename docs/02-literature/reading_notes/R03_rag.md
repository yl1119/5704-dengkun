# 文献阅读卡：R03 RAG

## 基本信息

- 标题：Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- 作者：Patrick Lewis 等
- 年份：2020
- 出处：NeurIPS 2020
- 预印本：arXiv:2005.11401

## 研究问题

如何利用外部非参数知识库增强生成模型在知识密集型任务上的表现。

## 方法

将检索器返回的文档片段作为生成模型上下文，并联合考察检索和生成两个环节。

## 与本人课题的关系

为 BM25-RAG、Dense-RAG 和 Hybrid-RAG 的问答评估提供总体框架。

## 对本人实验的启发

必须把“检索命中”与“最终答案正确”分开评估，不能只用生成答案判断检索方法优劣。
