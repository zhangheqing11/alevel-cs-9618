# T31 · P3 全量打标签 + 拆得分点（执行工位 codex）

## 目标

按 `papers/p3/tagging-guide.md` 给 P3 的**全部 858 行**写上 `types`、`tag_confidence`、`tag_note`；并对指南 §8 规定要拆的写代码 / 类图小问，把 MS 拆成 `markpoints`（逐字 `text` + `marks` + `skills`）和 `ms_max`。这些数据驱动 P3 题型卡（T32）和学生的「失分技能」统计。做法与 P2 的 T28 完全相同（`pipeline/tag/p2/` 是现成范本）。

> 这是**跨模型盲标**：P3 的题型体系与试标由 Claude（T30）设计，本任务检验指南能否让另一个模型独立标出一致的结果。

## 输入

- `papers/p3/taxonomy.json`（9 章 79 题型）、`papers/p3/tagging-guide.md`（**唯一规则**：定主题型、写代码题归类、副题型、低信心、特殊行、§8 得分点拆分含 A / B 两种 MS 写法）。
- 技能词表：`papers/p3/skill_tags.json`（`extends` `papers/p2/skill_tags.json`，D8 / D34；P3 新增 `random-file`、`user-defined-type`）。
- 试标：`papers/p3/pilot_tags.csv`（3 卷 81 行）、`papers/p3/pilot_markpoints.jsonl`（7 行 31 条得分点）。
- `corpus/rows/p3/*.jsonl`；看原页 `python3 skill/cie-9618-cs-tutor/scripts/rows.py render <行 id> [--ms]`。原卷在 `/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/`（只读）。
- `schemas/row.schema.json`、`docs/DECISIONS.md`（D2、D8、D21、D33、**D34、D35**）。

## 做法要求

1. **真源单独存放**：`pipeline/tag/p3/p3_tags.jsonl`（`{"id","primary","cross","confidence","note"}`）与 `pipeline/tag/p3/p3_markpoints.jsonl`（`{"id","ms_max","markpoints":[…]}`），用 `pipeline/tag/p3/apply_p3.py` 合并进 `corpus/rows/p3/*.jsonl`：只写 `types`、`tag_confidence`、`tag_note`、`markpoints`、`ms_max`；其余字段（**含 T27 的 `er`**，D33）逐字保留；可重复运行，`--check` 报告是否有改动。可以复用 / 泛化 `pipeline/tag/p2/apply_p2.py`，但不要改动 P2 的行为（P2 的 `--check` 仍须 0 改动）。
2. **先盲标再对照**：先独立完成全部 858 行（含试标卷，**不先看 pilot 文件**），盲标结果另存 `pipeline/tag/p3/blind/`；再与 `pilot_tags.csv` 比主题型一致率、与 `pilot_markpoints.jsonl` 比得分点切分；分歧逐条看原页复核后按你的结论写，分歧清单写进报告。
3. **D35 重复行**：`equivalent_of` 有值的行，以及与同季 `_31` 卷同题号逐字相同的 119 行（codex-1 的 T12e 正在补 `equivalent_of`），标签与得分点**照抄 `_31` 卷对应行**。
4. 每条 markpoint 的 `text` 必须是该行 `ms_text` 的子串（压缩空白后）；每个 `skills` 都在 P3 词表（含 extends）里；得分点总分等于分值，或写 `ms_max`。
5. 拿不准就标 `low` 并写 `tag_note`；不新建题型码或标签（需要新标签写进报告「需要总控决定」）。

## 产出

- `pipeline/tag/p3/`（两个 jsonl 真源 + `apply_p3.py` + 自检脚本 + 盲标快照 + 测试）。
- 更新后的 `corpus/rows/p3/*.jsonl`。
- `corpus/tag_report_p3.md`：每题型行数与分值（核验语料，去重）、拆分行数与得分点总数、各技能标签出现次数、`low` 清单、与 pilot 的一致率与分歧、建议新增的标签、核验语料出现 < 2 次的题型。

## 允许写的路径

`pipeline/tag/p3/**`、`corpus/rows/p3/**`、`corpus/tag_report_p3.md`、`tasks/progress/T31.md`。若泛化 apply 脚本需要改 `pipeline/tag/p2/apply_p2.py`，先写进「需要总控决定」，不要直接改。

## 完成标准

- `make check` 全绿（题型码、技能标签、schema 合法）；`make check-scope TASK=T31` 全绿；`apply_p3.py --check` 0 改动；`pipeline/er/apply_er.py --check` 0 改动。
- 858 行全部有 `types.primary`；该拆的行全部有 `markpoints`；`low` < 10%（超过说明原因）。
- 与 pilot 主题型一致率 ≥ 90%，得分点切分与 pilot 一致的行 ≥ 80%；低于时在 PR 写明主要分歧类型，并指出是指南哪一条不清楚。

## 工作方式

从最新 origin/main 开分支 `task/T31-p3-tagging`；进度写 `tasks/progress/T31.md`；交付：rebase → make check → make check-scope TASK=T31 → push → `gh pr create --base main --title "T31: tag P3 rows + split markpoints"`。不要合并。
