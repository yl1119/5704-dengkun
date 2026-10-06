# 模型说明

本目录只记录模型名称、版本、来源、许可证和用途，不提交模型权重。

| 模型 | 版本 | 来源 | License | 用途 | 状态 |
|---|---|---|---|---|---|
| `BAAI/bge-m3` | Model card current | BAAI / Hugging Face | MIT | Dense Retrieval 默认候选 | 待在目标课程开发集确认 |
| 生成模型 | 待确定 | 待填写 | 待核验 | RAG 回答生成 | 待确认硬件后确定 |
| `BAAI/bge-reranker-v2-m3` | Model card current | BAAI / Hugging Face | MIT | 重排序拓展 | 拓展 |

## Dense 模型选择说明

当前默认候选为 `BAAI/bge-m3`。该模型支持多语言文本表示，适合中文课程知识问答的 Dense Retrieval 初始实验。本论文主实验仍将 BM25 作为独立关键词检索基线，Dense 实验只使用 BGE-M3 的 dense embedding 输出，不把模型内部 sparse 模式与 BM25 混为一谈。

官方来源：

- `https://huggingface.co/BAAI/bge-m3`
- `https://github.com/FlagOpen/FlagEmbedding`

正式实验前还需登记：

- 具体 revision；
- 向量维度；
- CPU/GPU 和显存；
- batch size；
- 最大输入长度；
- 实际许可证核验记录。
