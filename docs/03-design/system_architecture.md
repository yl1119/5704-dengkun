# 系统架构

## 核心模块

1. `data ingestion`：导入课程资料并登记来源；
2. `preprocessing`：清洗、去重、切分和元数据生成；
3. `indexing`：建立 BM25 倒排索引和 Dense 向量索引；
4. `retrieval`：BM25、Dense、Hybrid 三类检索器；
5. `rerank`：拓展阶段的重排序模块；
6. `rag`：上下文构造、答案生成和来源引用；
7. `evaluation`：检索指标、问答指标和错误分析；
8. `experiment runner`：读取配置、执行实验并保存结果。

## 代码目录映射

```text
src/data/          数据读取、格式校验和预处理
src/retrievers/    BM25、Dense、Hybrid 检索器
src/rag/           RAG Prompt 和生成流程
src/evaluation/    Recall、Hit Rate、MRR、nDCG 等
src/utils/         配置和通用函数
scripts/           命令行入口
configs/           实验配置
```

## 数据流约束

- 每个文档块必须具有唯一 `chunk_id`；
- 每个问题必须具有唯一 `question_id`；
- 检索结果必须保存 `question_id`、`chunk_id`、`rank` 和 `score`；
- RAG 答案必须保存所用文档 ID；
- 所有实验必须保留配置、命令、数据版本和输出结果；
- 正式测试集不得混入开发集或调参过程。
