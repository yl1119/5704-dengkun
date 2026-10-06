# 检索实验结果报告

## 运行信息

- 运行日期：2026-10-06
- 课程：数据结构与算法基础
- 知识库：`course-corpus-v001`
- 知识片段数：960
- 测试集：`test-v001`
- 测试问题数：150
- 问题分类：术语定义 38、原理解释 38、流程步骤 37、易混辨析 37
- Dense 模型：`BAAI/bge-m3`
- 评测脚本：`scripts/evaluate_retrieval.py`
- 主要指标：Recall@K、Hit Rate@K、MRR、nDCG@K

## 总体结果

| Retriever | Recall@1 | Recall@3 | Recall@5 | Recall@10 | Hit Rate@10 | MRR |
|---|---:|---:|---:|---:|---:|---:|
| BM25 | 0.026667 | 0.100000 | 0.186667 | 0.293333 | 0.313333 | 0.094000 |
| Dense | 0.000000 | 0.213333 | 0.420000 | 0.743333 | 0.813333 | 0.183690 |
| Weighted Hybrid, alpha=0.5 | 0.020000 | 0.126667 | 0.270000 | 0.596667 | 0.646667 | 0.145339 |
| RRF, k=60 | 0.020000 | 0.160000 | 0.236667 | 0.583333 | 0.626667 | 0.142741 |

完整结果见 `results/tables/retrieval_comparison_summary.csv`。

## 按问题类型的观察

### BM25

- 术语定义问题 Recall@10：0.815789；
- 原理解释问题 Recall@10：0.026316；
- 流程步骤问题 Recall@10：0.243243；
- 易混辨析问题 Recall@10：0.081081。

BM25 在术语定义问题上相对较强，但在需要语义理解、步骤概括和多个概念联合判断的问题上明显较弱。

### Dense

- 术语定义问题 Recall@10：0.947368；
- 原理解释问题 Recall@10：0.894737；
- 流程步骤问题 Recall@10：0.837838；
- 易混辨析问题 Recall@10：0.283784。

Dense 在本数据集的四类问题上均优于 BM25 的总体表现，尤其是原理解释和流程步骤问题。

## 融合参数结果

- Weighted Hybrid 扫描 `alpha=0.0,0.1,...,1.0`；
- RRF 扫描 `rrf_k=10,20,40,60,80,100`；
- Weighted Hybrid 的总体 MRR 最优点：`alpha=0.0`，MRR 为 `0.179690`；
- RRF 的总体 MRR 最优点：`rrf_k=20`，MRR 为 `0.142741`。

## 当前结论

1. 在当前自撰课程数据和自动生成测试集上，Dense Retrieval 明显优于 BM25。
2. 当前 Weighted Hybrid 的最优权重为 `alpha=0.0`，等价于只使用 Dense Retrieval，尚未证明加权融合优于 Dense Baseline。
3. 当前 RRF 也没有超过 Dense Baseline。
4. 这不是“混合检索无效”的最终论文结论，因为当前知识库和测试集仍需人工复核，且问题与知识片段由同一生成脚本构造，存在数据分布过于规则的风险。
5. 下一步应人工改写和复核测试问题，增加真实课程资料中的术语、语义改写、章节交叉和易混概念，再重新运行全部方法。

## 文件清单

- `results/tables/bm25_generated_retrieval_results.csv`
- `results/tables/dense_generated_retrieval_results.csv`
- `results/tables/hybrid_generated_retrieval_results.csv`
- `results/tables/hybrid_rrf_generated_retrieval_results.csv`
- `results/tables/hybrid_generated_weight_sweep.csv`
- `results/tables/hybrid_generated_rrf_sweep.csv`
- `results/tables/retrieval_comparison_summary.csv`
- `results/figures/alpha_mrr_curve.png`
