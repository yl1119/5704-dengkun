# 数据管理说明

## 数据边界

本项目当前采用“数据结构与算法基础”作为课程范围。课程主题参考 MIT OpenCourseWare 6.006、Princeton Algorithms 与 OpenDSA 的公开课程页面；知识库正文由本项目根据公开主题自行撰写，不复制受版权限制的讲义或教材正文。正式实验前必须记录资料来源、许可证、采集日期、课程、版本和允许的使用范围。

正式知识库目标为 800–2000 个知识片段。本项目已生成 `data/generated/course_chunks.jsonl`，包含 960 个自撰知识片段、16 个章节和 96 个课程概念。每条记录包含章节字段，用于分析不同章节上的检索表现。知识库、测试集和索引均由本项目独立维护。

## GitHub 提交规则

- 只提交小型样例数据、元数据和数据处理说明；
- 不提交大型原始文件、受版权限制教材/论文 PDF、隐私数据；
- `data/raw/`、`data/processed/` 和 `data/indexes/` 已被忽略；
- 每次实验记录数据版本，如 `course-corpus-v001` 和 `test-v001`。

## 文档格式

```json
{
  "chunk_id": "CHUNK-001",
  "doc_id": "DOC-001",
  "title": "课程文档标题",
  "course": "课程名称",
  "chapter_id": "CHAPTER-01",
  "chapter_title": "章节名称",
  "section": "章节名称",
  "text": "文档块正文",
  "source": "来源地址或文件标识",
  "license": "许可证",
  "version": "course-corpus-v001"
}
```

## 测试问题格式

```json
{
  "question_id": "Q-001",
  "question": "问题文本",
  "question_type": "term_definition",
  "gold_chunk_ids": ["CHUNK-001"],
  "gold_answer": "标准答案",
  "difficulty": "easy",
  "annotation_notes": "相关性判定说明",
  "version": "test-v001"
}
```

## 正式测试集分类

- `term_definition`：术语定义；
- `principle_explanation`：原理解释；
- `process_steps`：流程步骤；
- `confusable_concepts`：易混辨析。

正式测试集不少于 150 条，建议四类尽量均衡。测试集冻结后不得根据结果修改标注；如发现错误，必须提升版本并重跑所有方法。

`samples/` 中的数据仅用于验证代码流程；`generated/` 中的数据是当前论文实验的初始数据版本，正式提交论文前仍需人工复核和导师确认。

## 数据来源与生成方式

- 公开主题参考：见 `data/metadata/source_registry.csv`；
- 正文来源：项目自撰课程笔记；
- 生成脚本：`scripts/generate_course_dataset.py`；
- 数据版本：`course-corpus-v001`；
- 测试集版本：`test-v001`；
- 重新生成命令：

```bash
python scripts/generate_course_dataset.py
```
