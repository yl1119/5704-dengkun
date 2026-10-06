# 实验目录规范

每个实验至少包含：

```text
experiment_id/
├── config.yaml
├── command.txt
├── notes.md
├── metrics.csv
└── results.csv
```

## `notes.md` 必填内容

```markdown
# Experiment ID

## Purpose

## Compared with

## Configuration

## Dataset

## Random seed

## Command

## Result

## Conclusion

## Problems
```

每个结果必须能追溯到配置、命令、数据版本和运行环境。不得只提交截图或手工挑选的最优结果。
