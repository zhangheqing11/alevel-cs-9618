# T38 · 审计 P4 题型手册（+ 抽查 P4 练习）（执行工位 codex）

## 目标

P4 手册 36 张卡（T37）一部分由 Claude 写（PR、AR、SQ、LT 四章），一部分由 Codex 续写（FL、SR、RC、OP、MP 五章 + front / back），总控只抽查过一张。本任务逐张审计，**只出报告，不改卡片**；总控裁决后另开修正任务（T38b）。同时抽查 6 道 P4 真题练习的转写与证据格对照，作为 T35 的独立复核。做法与 T26（P1 / P2）、T36（P3）完全相同。

## 审计范围

1. `papers/p4/front.md`、`papers/p4/cards/*.md`（9 章 36 型）、`papers/p4/core/*.md`、`papers/p4/back.md`。
2. P4 练习抽查 6 道（每个 T35 子批 1 道）：`practice/p4/9618_s24_42_q3`（T35a）、`9618_w25_43_q3`（T35b）、`9618_s25_42_q1`（T35c）、`9618_w24_41_q3`（T35d）、`9618_s24_41_q2`（T35e）、`9618_w25_42_q1`（T35f）。

## 审计项

卡片（每张都要过）：T26 卡的 7 项——①引文是否支持那句说法；②代表题“完整作答”能否按该题 MS 拿满分（逐个独立得分点，`//` 是替代说法，Max 写清，“(and end where appropriate)” 等接续点没拆错）、MP 对齐表编号（D37 ②）；③选题规则（2022–25、主题型行、不同卷、非 s26、非 `equivalent_of`；不足时按 D41 ①）；④手写计数与得分点地图（按卡里写明的口径用脚本重算，差 ≥ 2 列出）；⑤“讲解时请对照原卷 QP / MS p.N”页码；⑥概念句与 MS / 考纲一致；⑦Python 片段——**完整作答要在官方源文件 / QP 测试数据上实际运行**，输出与 MS 截图一致；不用内置函数代劳题目算法（D10 ③）。另加 P4 专项：⑧Python 模板与“证据格怎么交”是否符合 `papers/p4/practice-notes.md` 与 MS；⑨D45 列出的 MS 范例缺陷在相关卡里是否说明、是否被照抄；⑩OP 章多张卡共用 s23/41 Q2 作代表题——评估是否需要换题（给出建议与候选行，不改）。

练习（6 道）：task.md 原题转写对照 QP 原页（小问、类图、给定伪代码、数据格式、测试数据表）；证据格对照表与 MS 每个得分点一一对应、自动 / 人工归类合理；测试是否过度限定（正确的不同写法能否通过）或漏测；参考解是否照抄了 D45 缺陷。

## 产出

- `papers/p4/audit/T38-findings.jsonl`：一条一行 `{"file","line","card","kind","severity","row","evidence","suggestion"}`；`kind` ∈ `quote-misuse`、`answer-not-full-marks`、`mp-alignment`、`pick-rule`、`count`、`qp-page`、`python`、`concept`、`evidence-cell`、`practice-transcription`、`practice-test`、`other`；`severity` ∈ `error` / `warn` / `nit`；`evidence` 写原件页码与要点。
- `papers/p4/audit/T38-report.md`：每章统计、全部 error 的逐条说明、每张卡核对的 QP / MS 页码、每个完整作答的运行方式与结果、6 道练习的抽查结果、OP 章换题建议。
- 审计脚本放 `papers/p4/audit/`（可重复运行）。报告与 jsonl 里行号写**纯文本行 id**，不要用 `⟦⟧` 与 `「」`。

## 允许写的路径

`papers/p4/audit/**`、`tasks/progress/T38.md`。不改卡片、练习、语料。

## 完成标准

- `make check` 全绿；`make check-scope TASK=T38` 全绿。
- 36 张卡的代表题都对照过原页；每个 error 都有原件证据。
- PR 描述：审计卡数、问题数（按 severity）、最严重的 5 条、练习抽查结论、「需要总控决定」。
