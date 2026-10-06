# 2027 届本科毕业论文

## 基本信息

- 姓名：邓坤
- 学号：202319120404
- 专业：智能科学与技术
- 指导教师：曾维
- 毕业论文题目：面向高校课程知识问答的混合检索增强生成方法研究
- 研究方向：混合检索 / RAG 知识问答
- 课题定位：稀疏检索与稠密检索的融合机制和融合权重
- 当前阶段：已完成 960 片段知识库、150 题测试集和四类检索实验
- 最后更新：2026-10-06

## 一、研究问题

本课题面向高校课程知识问答场景，独立构建包含约 800–2000 个知识片段的课程知识库，以及不少于 150 条问题的分类测试集。针对 BM25 擅长课程术语和精确词项匹配、Dense Retrieval 擅长语义改写但可能忽略编号和专有名词的互补特点，分别建立两条单独基线，并研究分数加权融合与倒数排名融合（RRF）。论文重点研究融合机制、权重参数及不同问题类型下的性能差异，而不是把主要工作放在系统界面实现上。最终统一比较 Recall@K、Hit Rate、MRR 等检索指标，以及回答正确率和 faithfulness，并解释混合检索在哪些题型上有效、在哪些题型上反而变差。

## 二、最低完成要求

- [ ] 冻结具体课程范围、知识来源和数据使用边界
- [ ] 独立构建包含 800–2000 个知识片段的课程知识库，每条记录所属章节
- [ ] 构建不少于 150 条问题的独立测试集，并完成四类问题标注
- [ ] 实现 BM25 关键词检索基线
- [ ] 实现 Dense 向量检索基线
- [ ] 至少实现分数加权融合或 RRF，并建议两种都实现用于消融
- [ ] 冻结三种检索共用的评测脚本和判定标准
- [ ] 统一比较 Recall@K、Hit Rate、MRR 和检索延迟
- [ ] 完成基础 RAG 问答闭环
- [ ] 比较最终问答准确性、完整性和 faithfulness
- [ ] 研究 `alpha∈[0,1]` 的权重曲线或 RRF 的 `k` 参数
- [ ] 按术语定义、原理解释、流程步骤、易混辨析分组统计
- [ ] 完成融合方式、权重和 Top-k 消融实验
- [ ] 分析混合检索相对单一检索变差的典型案例
- [ ] 完成 5–8 页 Baseline 与问题分析报告
- [ ] 完成毕业论文

## 三、拓展目标

- [ ] rerank 重排序
- [ ] query rewrite 查询改写
- [ ] 动态融合策略
- [ ] 不可回答问题检测
- [ ] 不同 embedding 模型比较

## 四、技术路线

```text
课程资料采集与来源登记
        ↓
清洗、去重、章节识别、文档切分
        ↓
课程知识库 + 独立测试集
        ↓
BM25 检索 ──────┐
Dense 检索 ──────┼→ 分数归一化与融合 → 可选 rerank → Top-k 上下文
                  ↓
               RAG 生成
                  ↓
检索评估 + 问答评估 + 参数实验 + 消融实验 + 失败案例分析
```

详细说明：[技术路线](docs/01-topic/technical_route.md)

## 五、当前进展

- 当前阶段：仓库初始化和实验规范建立
- 最近完成：建立统一仓库结构；明确 BM25、Dense、加权融合和 RRF 路线；建立冻结评测协议和分类评测要求
- 当前问题：当前数据为项目自撰初始版本，测试集仍需人工复核；RAG 生成模型尚未确定；当前融合未超过 Dense 基线
- 下一步：人工复核并改写测试集；补充真实课程资料；确定生成模型；完成问答正确率与 faithfulness 实验

## 六、主要实验结果

| Experiment | Main Setting | Result | Status |
|---|---|---|---|
| EXP-001 BM25 | `top_k=1/3/5/10` | MRR 0.094000 | Completed |
| EXP-002 Dense | `BAAI/bge-m3` | MRR 0.183690 | Completed |
| EXP-003 Weighted Hybrid | best alpha=0.0, MRR 0.179690 | Completed |
| EXP-004 RRF Hybrid | best rrf_k=20, MRR 0.142741 | Completed |
| EXP-005 Top-k | `k=1/3/5/10` | 已生成统一结果 | Completed |
| EXP-006 Ablation | 融合方式/权重/Top-k | 部分完成 | In progress |

> 不得在运行实验前填写或编造结果。

## 七、仓库目录说明

| 目录 | 内容 |
|---|---|
| `docs/01-topic/` | 题目、任务要求和技术路线冻结区 |
| `docs/02-literature/` | 候选文献、核验文献和阅读卡 |
| `docs/03-design/` | 系统架构和实验设计 |
| `docs/04-meetings/` | 导师会议和阶段汇报记录 |
| `src/` | 数据处理、检索、RAG 和评估代码 |
| `configs/` | 可复现实验配置 |
| `scripts/` | 命令行执行入口 |
| `data/` | 数据说明、元数据、小型样例和测试集 |
| `experiments/` | 每次实验的配置、命令、结果和结论 |
| `results/` | 表格、图片和轻量日志 |
| `thesis/` | 论文提纲、图表、草稿和参考文献 |
| `progress/` | 里程碑、周报和问题清单 |

## 八、本人主要贡献

1. 确定高校课程知识库范围并整理课程资料及元数据。
2. 构建独立测试集并标注标准答案与相关文档。
3. 实现 BM25、Dense 和 Hybrid 三类检索方法。
4. 实现分数归一化、加权融合和 RRF，并研究 `alpha` 或 `rrf_k` 参数。
5. 冻结统一评测口径，按四类问题统计检索表现。
6. 分析混合检索变好或变差的典型案例，解释稀疏与稠密检索的互补边界。
7. 完成代码、实验、数据处理、结果分析和毕业论文撰写。

## 九、参考项目与第三方代码

| 项目/模型 | URL | License | 使用内容 | 本项目修改内容 |
|---|---|---|---|---|
| 待填写 | 待填写 | 待核验 | 待填写 | 待填写 |

任何第三方项目、模型和数据在使用前必须登记来源、版本和许可证。不得直接提交版权受限教材、论文 PDF、隐私数据或未经许可的大型数据集。

## 十、环境与复现

- OS：Windows / Linux（实际实验环境待登记）
- Python：3.10+
- 主要依赖：见 `requirements.txt`
- 配置入口：`configs/`
- 运行入口：`scripts/`

快速开始：

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt

python scripts/run_bm25.py --config configs/bm25.yaml
python scripts/run_dense.py --config configs/dense.yaml
python scripts/run_hybrid.py --config configs/hybrid.yaml
python scripts/evaluate_retrieval.py --config configs/evaluation.yaml
```

样例数据只用于检查流程，不能作为论文正式实验结果。

## GitHub 提交规则

可以提交源代码、配置、小型样例数据、元数据、文献清单、实验日志、CSV 结果、图表和论文 Markdown/LaTeX。不要提交大型原始数据、完整模型权重、大量 checkpoint、虚拟环境、构建目录、含隐私的数据或有版权限制的教材/论文 PDF。
