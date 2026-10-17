# T26c / T26d · 按审计结论修正 P1 / P2 题型手册（执行工位 codex）

## 目标

把 T26 跨模型审计找出的 26 条问题按 **D40** 改进手册。问题清单与证据：`papers/p1/audit/T26-findings.jsonl` + `T26-report.md`（P1），`papers/p2/audit/T26-findings.jsonl` + `T26-report.md`（P2）。编号 F01–F13 = 各 jsonl 的行序。每条按该条 `suggestion` 改，D40 的四条裁决优先于 `suggestion`。

| 子任务 | 工位 | 改什么 |
|:--|:--|:--|
| **T26c** | codex-1 | P1 的 F01–F13（`papers/p1/cards/*.md`、`papers/p1/core/*.md`、`front.md`、`back.md`） |
| **T26d** | codex-2 | P2 的 F01–F13（`papers/p2/cards/*.md`、`papers/p2/core/*.md`、`front.md`、`back.md`）；外加 **D39** 的 P3 指南措辞：`papers/p3/tagging-guide.md` §7 加“同票”判例规则、§8.2 B 写明“MS 只给填空答案片段时按 QP 留空行逐行对应拆分”、`papers/p3/taxonomy.json` 中 P3-DR-02 的 `summary` 与 DR-04 分界统一（记录字段赋值含赋枚举值归 DR-04） |

## 改法要求

1. **只改有问题的那几处**，同类表述在同一文件或相关章节重复出现的一并改（审计条目里点名的“同步”位置，如 DB-03 解题思路、章末辨析、core 同类规则）；不重写整张卡，不改无关措辞。
2. **证据规则不变**（AGENTS.md §5）：给分说法只认该题自己的 MS；「…」⟦行 id⟧ 只放 MS 原文（`make check` 会核对）；新写的非 MS 句子不得加「」。
3. **满分作答类**（如 P1 F02 EO-05）：重写后的作答要能按该题 MS 拿满分，“与 MS 对齐”表逐点对得上；动笔前重读该题 QP / MS 原页。
4. 图（如 P1 F01 星型网络示意图）改完后 `make build`，在 `output/p<N>/*.html` 里确认显示正确。
5. 不改 `corpus/`、`practice/`、`ladder/`、`taxonomy.json`（T26d 的 P3-DR-02 `summary` 除外）。

## 产出

- 修正后的卡片 / 概念表 / front / back（T26d 另有 P3 指南与 taxonomy 一处）。
- `papers/p<N>/audit/T26-fixes.md`：表格逐条列 F 编号 → 改了哪个文件哪几行 → 改动摘要；没有照 `suggestion` 改的说明原因。
- 重跑各自的 `papers/p<N>/audit/check_handbook.py`，结果写进 `T26-fixes.md`。
- 进度写 `tasks/progress/T26c.md` / `T26d.md`。

## 允许写的路径

T26c：`papers/p1/cards/**`、`papers/p1/core/**`、`papers/p1/front.md`、`papers/p1/back.md`、`papers/p1/audit/**`。
T26d：`papers/p2/cards/**`、`papers/p2/core/**`、`papers/p2/front.md`、`papers/p2/back.md`、`papers/p2/audit/**`、`papers/p3/tagging-guide.md`、`papers/p3/taxonomy.json`。

## 完成标准

- `make check`、`make build` 全绿；`make check-scope TASK=T26c|T26d` 全绿。
- 13 条都有处理记录；error 级每条附改后的原文片段。
- PR 描述：逐条 F 编号与处理结果、仍需总控决定的事项。

## 工作方式

从最新 `origin/main` 开分支 `task/T26c-p1-fixes`（或 `task/T26d-p2-fixes`）；交付：rebase → `make check` → `make build` → `make check-scope TASK=T26c|T26d` → push → `gh pr create --base main --title "T26c: fix P1 handbook per audit"`（或 `T26d: fix P2 handbook per audit`）。不要合并。
