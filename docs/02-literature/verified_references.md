# 已核验参考文献

以下条目已依据出版社、会议论文集、ACL Anthology、NeurIPS、NIST、DOI 或作者正式页面完成基本书目信息核验。最终写入论文时，应再按学校要求统一为 GB/T 7714 格式。

## 当前状态

- 已核验英文核心文献：17 篇
- 中文核心文献：待补充
- 已完成阅读卡：0 篇
- 精读目标：至少 5 篇

## 核心文献

### [R01] The Probabilistic Relevance Framework: BM25 and Beyond

- Authors: Stephen Robertson; Hugo Zaragoza
- Year: 2009
- Venue: Foundations and Trends in Information Retrieval, 3(4), 333–389
- DOI: `10.1561/1500000019`
- 类型：期刊综述
- 课题关系：BM25 理论、参数与概率相关性框架，是稀疏检索基线的主要依据。

### [R02] Dense Passage Retrieval for Open-Domain Question Answering

- Authors: Vladimir Karpukhin; Barlas Oğuz; Sewon Min; Patrick Lewis; Ledell Wu; Sergey Edunov; Danqi Chen; Wen-tau Yih
- Year: 2020
- Venue: EMNLP 2020, 6769–6781
- DOI: `10.18653/v1/2020.emnlp-main.550`
- 类型：会议论文
- 课题关系：Dense Retrieval 双编码器基线和稀疏/稠密对比依据。

### [R03] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

- Authors: Patrick Lewis; Ethan Perez; Aleksandra Piktus; Fabio Petroni; Vladimir Karpukhin; Naman Goyal; Heinrich Küttler; Mike Lewis; Wen-tau Yih; Tim Rocktäschel; Sebastian Riedel; Douwe Kiela
- Year: 2020
- Venue: NeurIPS 2020, Volume 33
- Stable ID: arXiv `2005.11401`
- 类型：会议论文
- 课题关系：RAG 基础框架和检索增强生成定义。

### [R04] Retrieval-Augmented Generation for Large Language Models: A Survey

- Authors: Yunfan Gao; Yun Xiong; Xinyu Gao; Kangxiang Jia; Jinliu Pan; Yuxi Bi; Yi Dai; Jiawei Sun; Meng Wang; Haofen Wang
- Year: 2023
- Stable ID: arXiv `2312.10997`
- 类型：预印本综述
- 课题关系：RAG 技术路线、检索优化和评估综述。
- 注意：引用时明确标注文献类型为预印本。

### [R05] Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods

- Authors: Gordon V. Cormack; Charles L. A. Clarke; Stefan Büttcher
- Year: 2009
- Venue: SIGIR 2009, 758–759
- DOI: `10.1145/1571941.1572114`
- 类型：会议论文
- 课题关系：RRF 融合公式和排名融合基线的主要来源。

### [R06] An Analysis of Fusion Functions for Hybrid Retrieval

- Authors: Sebastian Bruch; Siyu Gai; Amir Ingber
- Year: 2024
- Venue: ACM Transactions on Information Systems, 42(1), Article 20, 1–35
- DOI: `10.1145/3596512`
- 类型：期刊论文
- 课题关系：直接比较加权融合、分数归一化和 RRF，是本课题最重要的方法参考之一。
- 修正：导师清单中的 2023 应按正式卷期记为 2024。

### [R07] ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT

- Authors: Omar Khattab; Matei Zaharia
- Year: 2020
- Venue: SIGIR 2020, 39–48
- DOI: `10.1145/3397271.3401075`
- 类型：会议论文
- 课题关系：稠密检索和 late interaction 的拓展参考。

### [R08] SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking

- Authors: Thibault Formal; Benjamin Piwowarski; Stéphane Clinchant
- Year: 2021
- Venue: SIGIR 2021
- DOI: `10.1145/3404835.3463098`
- 类型：会议论文
- 课题关系：学习式稀疏检索与词项扩展的拓展参考。

### [R09] Unsupervised Dense Information Retrieval with Contrastive Learning

- Authors: Gautier Izacard; Mathilde Caron; Lucas Hosseini; Sebastian Riedel; Piotr Bojanowski; Armand Joulin; Edouard Grave
- Year: 2022
- Venue: Transactions on Machine Learning Research
- Stable ID: arXiv `2112.09118`
- 类型：期刊论文
- 课题关系：无监督稠密检索、跨领域泛化和 BM25 对比依据。

### [R10] BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models

- Authors: Nandan Thakur; Nils Reimers; Andreas Rücklé; Abhishek Srivastava; Iryna Gurevych
- Year: 2021
- Venue: NeurIPS Datasets and Benchmarks Track
- Stable ID: arXiv `2104.08663`
- 类型：会议论文/基准
- 课题关系：统一检索评估和多检索器公平比较的方法依据。

### [R11] Passage Re-ranking with BERT

- Authors: Rodrigo Nogueira; Kyunghyun Cho
- Year: 2019
- Stable ID: arXiv `1901.04085`
- 类型：预印本
- 课题关系：rerank 拓展目标的基础参考。

### [R12] Pyserini: A Python Toolkit for Reproducible Information Retrieval Research with Sparse and Dense Representations

- Authors: Jimmy Lin; Xueguang Ma; Sheng-Chieh Lin; Jheng-Hong Yang; Ronak Pradeep; Rodrigo Nogueira
- Year: 2021
- Venue: SIGIR 2021, 2356–2362
- DOI: `10.1145/3404835.3463238`
- 类型：会议论文
- 课题关系：稀疏、稠密和混合检索的统一可复现实验参考。

### [R13] Billion-Scale Similarity Search with GPUs

- Authors: Jeff Johnson; Matthijs Douze; Hervé Jégou
- Year: 2021（在线发表 2019）
- Venue: IEEE Transactions on Big Data, 7(3), 535–547
- DOI: `10.1109/TBDATA.2019.2921572`
- 类型：期刊论文
- 课题关系：FAISS 与向量相似度检索的工程参考。

### [R14] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

- Authors: Nils Reimers; Iryna Gurevych
- Year: 2019
- Venue: EMNLP-IJCNLP 2019, 3982–3992
- DOI: `10.18653/v1/D19-1410`
- 类型：会议论文
- 课题关系：句向量语义检索和余弦相似度方法依据。

### [R15] Overview of the TREC 2019 Deep Learning Track

- Authors: Nick Craswell; Bhaskar Mitra; Emine Yilmaz; Daniel Campos; Ellen M. Voorhees
- Year: 2019
- Venue: The Twenty-Eighth Text REtrieval Conference, NIST Special Publication 500-331
- Stable URL: NIST TREC 2019 Proceedings
- 类型：评测报告
- 课题关系：检索基准、统一测试与排序评价方法参考。
- 修正：原清单遗漏 Ellen M. Voorhees。

### [R16] RAGAs: Automated Evaluation of Retrieval Augmented Generation

- Authors: Shahul Es; Jithin James; Luis Espinosa Anke; Steven Schockaert
- Year: 2024
- Venue: EACL 2024 System Demonstrations, 150–158
- DOI: `10.18653/v1/2024.eacl-demo.16`
- 类型：会议论文
- 课题关系：回答 faithfulness 和 RAG 自动评估参考。

### [R17] Introduction to Information Retrieval

- Authors: Christopher D. Manning; Prabhakar Raghavan; Hinrich Schütze
- Year: 2008
- Publisher: Cambridge University Press
- DOI: `10.1017/CBO9780511809071`
- ISBN: `978-0-521-86571-5`
- 类型：专著
- 课题关系：倒排索引、相关性、Recall、MRR 等信息检索基础。

## 待完成事项

- [ ] 将上述条目转换为学校要求的 GB/T 7714 格式；
- [ ] 为 R01、R02、R03、R05、R06、R10、R16 中至少 5 篇建立阅读卡；
- [ ] 补充 5–8 篇经核验的中文核心文献；
- [ ] 文献综述中区分“用于方法设计”和“用于实验评价”的文献。
