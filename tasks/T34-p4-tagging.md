# T34 · P4 全量打标签 + 拆得分点（执行工位 codex）

## 目标

按 `papers/p4/tagging-guide.md` 给 P4 的**全部 744 行**（32 卷，含 2021 扩展 99 行、s26 三卷）写上 `types`、`tag_confidence`、`tag_note`；并按指南 §8 把 **≥ 2 分且 MS 有计分清单**的行拆成 `markpoints`（逐字 `text` + `marks` + `skills`）和 `ms_max`。这些数据驱动 P4 题型卡、P4 练习（T35）和学生的「失分技能」统计。做法与 P3 的 T31 相同（`pipeline/tag/p3/` 是现成范本）。

> 这是**跨模型盲标**：P4 的题型体系与试标由 Claude（T33）设计，本任务检验指南能否让另一个模型独立标出一致的结果。

## 输入

- `papers/p4/taxonomy.json`（9 章 36 型）、`papers/p4/tagging-guide.md`（**唯一规则**：定主题型、§3 写代码题归类（先认模块身份，再按得分点数取最多）、副题型、低信心、§6 特殊行、§7 边界判例、§8 得分点拆分与技能标签）。
- 技能词表：`papers/p4/skill_tags.json`（`extends` `papers/p2/skill_tags.json`，D8；P4 新增 11 个）。
- 试标：`papers/p4/pilot_tags.csv`（9618_s23_42、9618_w24_41、9618_s25_43 共 71 行）、`papers/p4/pilot_markpoints.jsonl`（57 行 218 条得分点）。
- `corpus/rows/p4/*.jsonl`；看原页 `python3 skill/cie-9618-cs-tutor/scripts/rows.py render <行 id> [--ms]`。原卷与源文件在 `/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/`（只读）。
- `schemas/row.schema.json`、`docs/DECISIONS.md`（D2、D8、D21、D26、D29、D33、D35、**D42**）。

## 做法要求

1. **真源单独存放**：`pipeline/tag/p4/p4_tags.jsonl`（`{"id","primary","cross","confidence","note"}`）与 `pipeline/tag/p4/p4_markpoints.jsonl`（`{"id","ms_max","markpoints":[…]}`），用 `pipeline/tag/p4/apply_p4.py` 合并进 `corpus/rows/p4/*.jsonl`：只写 `types`、`tag_confidence`、`tag_note`、`markpoints`、`ms_max`；其余字段（含 `er`、`equivalent_of`，D33）逐字保留；可重复运行，`--check` 报告是否有改动。可以复用 / 泛化 `pipeline/tag/p3/apply_p3.py` 的写法，但不要改 P2 / P3 的脚本（它们的 `--check` 仍须 0 改动）。
2. **先盲标再对照**：先独立完成全部 744 行（含试标卷，**不先看 pilot 文件**），盲标结果另存 `pipeline/tag/p4/blind/`；再与 `pilot_tags.csv` 比主题型一致率、与 `pilot_markpoints.jsonl` 比得分点切分；分歧逐条看原页复核后按你的结论写，分歧清单写进报告。
3. **拆分口径（D42 ①②）**：门槛 **≥ 2 分**；只从 MS 开头的语言无关清单切，Java / VB.NET / Python / 伪代码范例一律不拆；计数句（“1 mark for each completed statement (5)”）作一条、`marks` = 数量；两段计分合成一张清单并写 `ms_max`；1 分行与 MS 没有计分清单的行不拆（`tag_note` 写「MS 无计分清单，未拆」，不算低信心）。
4. **重复行（D42 ③）**：`equivalent_of` 有值的行，以及与同季 `_41` 卷逐字相同的 162 行（T12f 正在补 `equivalent_of`，名单见 `tasks/T12f-p4-equivalents.md`），标签与得分点**照抄 `_41` 卷对应行**。
5. 每条 markpoint 的 `text` 必须是该行 `ms_text` 的子串（D26 / D29 归一、压缩空白后，不放宽大小写）；每个 `skills` 都在 P4 词表（含 extends）里；得分点总分等于分值，或写 `ms_max`。
6. 拿不准就标 `low` 并写 `tag_note`；不新建题型码或标签（需要新标签写进报告「需要总控决定」）。

## 产出

- `pipeline/tag/p4/`（两个 jsonl 真源 + `apply_p4.py` + 自检脚本 + 盲标快照 + 测试）。
- 更新后的 `corpus/rows/p4/*.jsonl`。
- `corpus/tag_report_p4.md`：每题型行数与分值（核验语料，去重）、拆分行数与得分点总数、各技能标签出现次数、`low` 清单、与 pilot 的一致率与分歧、建议新增的标签、核验语料出现 < 2 次的题型。

## 允许写的路径

`pipeline/tag/p4/**`、`corpus/rows/p4/**`、`corpus/tag_report_p4.md`、`tasks/progress/T34.md`。需要改 `pipeline/tag/p2/`、`pipeline/tag/p3/` 或 `tools/` 时，先写进「需要总控决定」，不要直接改。

## 完成标准

- `make check` 全绿（题型码、技能标签、schema、markpoints 子串合法）；`make check-scope TASK=T34` 全绿；`apply_p4.py --check`、`pipeline/tag/p3/apply_p3.py --check`、`pipeline/er/apply_er.py --check` 都 0 改动。
- 744 行全部有 `types.primary`；该拆的行全部有 `markpoints`；`low` < 10%（超过说明原因）。
- 与 pilot 主题型一致率 ≥ 90%，得分点切分与 pilot 一致的行 ≥ 80%；低于时在 PR 写明主要分歧类型，并指出是指南哪一条不清楚。

## 工作方式

从最新 `origin/main` 开分支 `task/T34-p4-tagging`；进度写 `tasks/progress/T34.md`；交付：rebase → make check → make check-scope TASK=T34 → push → `gh pr create --base main --title "T34: tag P4 rows + split markpoints"`。不要合并。

**与 T12f 的关系**：T12f 同时在补 P4 的 `equivalent_of`，也会改 `corpus/rows/p4/`。T12f 合并后你 rebase 时若 `corpus/rows/p4/*.jsonl` 冲突，取 `origin/main` 的版本，再重跑 `apply_p4.py` 生成 rows（真源在 `pipeline/tag/p4/`，不受影响），然后重新跑完成标准里的检查。T12f 未合并时可以照常交付，在 PR 注明。
