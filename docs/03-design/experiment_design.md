# 第一版实验设计

## 1. 核心问题

1. 我要和谁比较？
   - BM25 关键词检索；
   - Dense 向量检索；
   - Weighted Hybrid 分数加权融合；
   - RRF 倒数排名融合。
2. 测哪些指标？
   - 检索：Recall@K、Hit Rate@K、MRR、平均/P95 延迟；
   - 问答：准确性、完整性、faithfulness、引用正确性；
   - 工程：索引时间、索引大小和内存占用。
3. 每个实验改变什么变量？
   - 检索器、融合方式、融合权重、RRF-k、Top-k；
   - 拓展实验改变 rerank、query rewrite 或动态融合组件。
4. 什么结果能证明方法有效？
   - Hybrid 在固定测试集上相对 BM25/Dense 提升主要检索指标；
   - 提升能够传递到问答准确性或 faithfulness；
   - 提升不是仅由更多上下文或更高延迟换取；
   - 消融实验能解释各组件贡献。

## 2. 公平比较要求

- 使用相同课程知识库版本；
- 使用相同测试集版本；
- 使用相同文档块和相关文档标注；
- 使用相同 Top-k（参数实验除外）；
- RAG 实验使用相同生成模型和 Prompt；
- 使用同一评估脚本；
- 报告完整实验，不只报告最优结果。
- 评测协议见 `evaluation_protocol.md`，正式实验前先冻结协议。

## 3. 必做实验

### EXP-001：BM25 Baseline

- 目的：获得关键词检索基础结果；
- 变量：固定 `k1=1.5`、`b=0.75`，比较 `k=1/3/5/10`；
- 输出：检索指标、逐题结果、平均/P95 延迟。

### EXP-002：Dense Baseline

- 目的：获得语义检索基础结果；
- 变量：固定 embedding 模型和余弦相似度；
- 输出：与 EXP-001 完全相同的指标。

### EXP-003：Weighted Hybrid 主实验

- 目的：验证混合检索是否优于单一检索；
- 变量：`alpha=0.0,0.1,...,1.0`；
- 融合：`alpha * BM25 + (1-alpha) * Dense`；
- 前提：两类分数先按查询归一化。

### EXP-004：RRF 主实验

- 目的：比较不依赖原始分数尺度的排名融合；
- 变量：`rrf_k ∈ {10,20,40,60,80,100}`；
- 输出：与加权融合相同的总体和分类指标。

### EXP-005：Top-k 参数实验

- 取值：`k=1/3/5/10`；
- 同时记录检索效果、RAG 效果、上下文长度和延迟。

### EXP-006：消融实验

- Hybrid 去掉 BM25；
- Hybrid 去掉 Dense；
- 去掉分数归一化；
- 加权融合替换为 RRF；
- 固定权重替换为最优开发集权重；
- 比较不同 Top-k；
- 若实现 rerank，则比较有/无 rerank；
- 若实现 query rewrite，则比较有/无 rewrite。

### EXP-007：典型失败案例

至少覆盖：

- BM25 命中、Dense 未命中；
- Dense 命中、BM25 未命中；
- 两者均未命中；
- 检索命中但最终答案错误；
- 知识库无答案但系统错误回答；
- 公式、课程术语、章节编号和专有名词导致的失败。

## 4. 结果表

| Retriever | Recall@1 | Recall@3 | Recall@5 | Recall@10 | MRR | Avg Latency |
|---|---:|---:|---:|---:|---:|---:|
| BM25 |  |  |  |  |  |  |  |
| Dense |  |  |  |  |  |  |  |
| Weighted Hybrid |  |  |  |  |  |  |
| RRF |  |  |  |  |  |  |

## 5. 分类型结果

| Question Type | BM25 Recall@5 | Dense Recall@5 | Hybrid Recall@5 | 现象解释 |
|---|---:|---:|---:|---|
| term_definition |  |  |  |  |
| principle_explanation |  |  |  |  |
| process_steps |  |  |  |  |
| confusable_concepts |  |  |  |  |
