# T40 · 分数线表（执行工位 codex）

## 目标

把 10 份官方分数线（Grade thresholds）PDF 抽成机器可读表，供冲刺阶段“按分数线估分”（学生做完整卷 / 四卷后估等级）和学习记录使用。

## 输入

- `sources/pastpapers/9618_<季><yy>_gt.pdf`：s21–w25 共 10 份（s26 尚无）。每份两部分：①各 component（11–13、21–23、31–33、41–43）的满分与 A–E 最低原始分（component 没有 A*）；②各 option（AX、AY、AZ、BX…）的组合、加权后满分、A*–E 分数线。
- `schemas/` 现有格式约定（CSV 用 `utf-8-sig`）。

## 产出

1. `pipeline/thresholds/extract_gt.py`：解析 10 份 PDF → 两张表；可重复运行。
2. `corpus/thresholds/components.csv`：`session,year,component,max_raw,A,B,C,D,E`（每季 12 行）。
3. `corpus/thresholds/options.csv`：`session,year,option,components,max_weighted,A*,A,B,C,D,E`（`components` 写成 `11;21;31;41` 这样的分号串）。
4. `corpus/thresholds/README.md`：字段说明；**学生（全 A Level，四卷）对应哪个 option**（同一 variant 组合 AX / AY / AZ 等）；加权说明（各卷原始分 → 加权满分 300 的换算方式以 PDF 或考纲原文为准，查不到就写明“不确定”，不要猜）。
5. `pipeline/thresholds/test_gt.py`：抽取结果与 PDF 文字逐值对照（至少每份 3 个随机格子 + 全表行数、满分一致性）；`corpus/thresholds/check_report.md` 记录人工抽查 20 格（PDF 页码）。

## 规则

- 数值照 PDF 原样；PDF 有缺格、脚注或某季特殊说明（如某 option 不开）照录并在 README 注明。
- 只读 `sources/`，不提交 PDF。

## 允许写的路径

`pipeline/thresholds/**`、`corpus/thresholds/**`、`tasks/progress/T40.md`。

## 完成标准

- `make check` 全绿；`make check-scope TASK=T40` 全绿；`python3 -m pytest pipeline/thresholds` 通过。
- 10 季全部抽出；component 表 120 行。
- PR 描述：行数、加权方式的结论与出处、异常格子、「需要总控决定」。

## 工作方式

从最新 `origin/main` 开分支 `task/T40-grade-thresholds`；交付：rebase → `make check` → `make check-scope TASK=T40` → push → `gh pr create --base main --title "T40: grade threshold tables"`。不要合并。
