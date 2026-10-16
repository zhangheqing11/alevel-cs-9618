# T24 · P1 全量打标签（执行工位 codex-1）

> **优先级高于 T12 剩余的 P3/P4**：P1 是学生最先学的卷，题型卡（T22）要等你的标签统计。手上的那一卷做完、开出 PR 后就转 T24。

## 目标

按 `papers/p1/tagging-guide.md` 给 P1 的**全部 979 行**（核验 + 2021 扩展）写上 `types`、`tag_confidence`、`tag_note`，让构建器能统计每个题型的考情、刷题清单和星级。

## 输入

- `papers/p1/taxonomy.json`（v1.1，9 章 88 题型）、`papers/p1/tagging-guide.md`（**唯一打标签规则**，逐条遵守）、`papers/p1/pilot_tags.csv`（设计工位亲手标的 3 份卷 88 行）。
- `corpus/rows/p1/*.jsonl`；看原页：`python skill/cie-9618-cs-tutor/scripts/rows.py render <行 id> [--ms]`（`has_figure: true` 的行必须看原页）。
- `schemas/row.schema.json`（`types`、`tag_confidence`、`tag_note` 字段）、`docs/DECISIONS.md`（D14 副题型同章跨章都可）。

## 做法要求

1. **标签的真源放在单独文件**：`pipeline/tag/p1_tags.jsonl`（每行 `{"id", "primary", "cross", "confidence", "note"}`），再用 `pipeline/tag/apply_tags.py` 合并进 `corpus/rows/p1/*.jsonl`（只写 `types`、`tag_confidence`、`tag_note` 三个字段，其余字段逐字不动）。这样 T12 以后重跑抽取时，标签可以一键重新套上。
2. **先盲标再对照**：先独立标完全部 979 行（**包括试标的 88 行，不要先看 pilot_tags.csv**），再与 pilot 比对，算出主题型一致率；不一致的逐条复核。最终按你复核后的结论写，分歧清单写进报告供设计工位裁决。
3. `equivalent_of` 不为空的行：与原行同标签。
4. 拿不准就标 `low` 并写 `tag_note`（在哪两个题型之间、为什么）——宁可多标 low，不要硬猜。
5. 不新建题型码；不改 taxonomy 与指南（发现问题写进报告）。

## 产出

- `pipeline/tag/`（`p1_tags.jsonl`、`apply_tags.py`、必要的辅助脚本）。
- 更新后的 `corpus/rows/p1/*.jsonl`。
- `corpus/tag_report_p1.md`：每章每题型的行数与分值（核验语料）、`low` 清单（行 id + 犹豫的两个题型 + 理由）、与 pilot 的一致率和分歧清单、没有用到的题型（如有）、对指南的改进建议。

## 允许写的路径

`pipeline/tag/**`、`corpus/rows/p1/**`、`corpus/tag_report_p1.md`、`tasks/progress/T24.md`。

## 完成标准

- `make check` 全绿（每行的主题型、副题型都在 taxonomy 里）；`make check-scope TASK=T24` 全绿。
- 979 行全部有 `types.primary`；`low` 比例写进报告（预期 < 10%，超过时说明原因）。
- 与 pilot 的主题型一致率 ≥ 90%；低于时在 PR 里写明主要分歧类型。
- `make build` 能生成 `output/p1/index.json` 的统计（手册正文缺，会跳过 md，但统计脚本可用 `build/stats.py` 自查）。

## 工作方式

分支 `task/T24-p1-tagging`（从最新 origin/main 开）；进度写 `tasks/progress/T24.md`；交付：rebase → make check → make check-scope TASK=T24 → push → `gh pr create --base main --title "T24: tag all P1 rows"`。不要合并。
