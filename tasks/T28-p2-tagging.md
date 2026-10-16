# T28 · P2 全量打标签 + 拆得分点（执行工位 codex-2）

## 目标

按 `papers/p2/tagging-guide.md` 给 P2 的**全部 721 行**写上 `types`、`tag_confidence`、`tag_note`；并对指南 §8 规定要拆的写代码小问，把 MS 拆成 `markpoints`（逐字 `text` + `marks` + `skills`）和 `ms_max`。这些数据驱动 P2 题型卡（T23）、P2 练习文件夹（T25）和学生的「失分技能」统计。

> 与 codex-1 的 T24（P1 打标签）**并行**：两边目录完全分开，不要碰 `pipeline/tag/` 下 P1 的文件、`corpus/rows/p1/`。

## 输入

- `papers/p2/taxonomy.json`（4 章 46 题型）、`papers/p2/skill_tags.json`（76 个标签，**唯一词表**，D8/D20）、`papers/p2/tagging-guide.md`（**唯一规则**：定主题型、写代码题的「在场 + 优先级」、副题型、低信心、§8 得分点拆分）。
- 试标：`papers/p2/pilot_tags.csv`（3 份卷 66 行）、`papers/p2/pilot_markpoints.jsonl`（18 行 110 条得分点）。
- `corpus/rows/p2/*.jsonl`；看原页 `python3 skill/cie-9618-cs-tutor/scripts/rows.py render <行 id> [--ms]`（会自动用 venv）。
- `schemas/row.schema.json`（`types`、`tag_confidence`、`tag_note`、`markpoints`、`ms_max`）、`docs/DECISIONS.md`（D2、D14、D20、**D21**）。

## 做法要求

1. **真源单独存放**：`pipeline/tag/p2/p2_tags.jsonl`（`{"id","primary","cross","confidence","note"}`）与 `pipeline/tag/p2/p2_markpoints.jsonl`（`{"id","ms_max","markpoints":[…]}`，`ms_max` 不需要时为 `null`），用 `pipeline/tag/p2/apply_p2.py` 合并进 `corpus/rows/p2/*.jsonl`：只写 `types`、`tag_confidence`、`tag_note`、`markpoints`、`ms_max`（`null` 不写），其余字段逐字不动。
2. **先盲标再对照**：先独立完成全部 721 行（含试标行，**不先看 pilot 文件**），再与 `pilot_tags.csv` 比主题型一致率、与 `pilot_markpoints.jsonl` 比得分点切分；分歧逐条复核后按你的结论写，并把分歧清单写进报告。
3. **D21**：`9618_s21_23`、`9618_w21_23` 与同季 `_21` 卷逐题相同的行，标签与得分点**照抄 `_21` 卷对应行**（即使 `equivalent_of` 还没补齐）；`equivalent_of` 已有值的行同样照抄原行。
4. 每条 markpoint 的 `text` 必须是该行 `ms_text` 的子串（压缩空白后）；每个 `skills` 都在词表里；得分点总分等于分值，或写 `ms_max`。
5. 拿不准就标 `low` 并写 `tag_note`；不新建题型码或标签（需要新标签写进报告，由设计工位决定）。

## 产出

- `pipeline/tag/p2/`（两个 jsonl 真源 + `apply_p2.py` + 自检脚本）。
- 更新后的 `corpus/rows/p2/*.jsonl`。
- `corpus/tag_report_p2.md`：每题型行数与分值（核验语料）、拆分行数与得分点总数、各技能标签出现次数、`low` 清单、与 pilot 的一致率和分歧、建议新增的标签、出现 < 2 次的题型。

## 允许写的路径

`pipeline/tag/p2/**`、`corpus/rows/p2/**`、`corpus/tag_report_p2.md`、`tasks/progress/T28.md`。

## 完成标准

- `make check` 全绿（题型码、技能标签都合法；schema 合法）；`make check-scope TASK=T28` 全绿。
- 721 行全部有 `types.primary`；该拆的行全部有 `markpoints`；`low` < 10%（超过说明原因）。
- 与 pilot 主题型一致率 ≥ 90%，得分点切分与 pilot 一致的行 ≥ 80%；低于时在 PR 写明主要分歧类型。

## 工作方式

从最新 origin/main 开分支 `task/T28-p2-tagging`；进度写 `tasks/progress/T28.md`；交付：rebase → make check → make check-scope TASK=T28 → push → `gh pr create --base main --title "T28: tag P2 rows + split markpoints"`。不要合并。
