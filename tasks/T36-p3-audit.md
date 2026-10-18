# T36 · 审计 P3 题型手册（执行工位 codex，跨模型交叉审计）

## 目标

P3 题型手册（9 章 79 张卡）由 Claude 设计工位在 T32 分三批写成（#40 / #41 / #43），总控对照 PDF 抽查过 51 条引文，但没有逐张核对。本任务由**另一家模型**逐张审计，做法、产出格式与 T26（P1 / P2 审计）相同。**只出报告，不改卡片**；总控按报告裁决后另开修正任务。

## 审计范围

`papers/p3/front.md`、`papers/p3/cards/*.md`（DR 12、CI 7、HV 5、BL 7、SY 12、SC 6、AI 7、CT 12、FP 11）、`papers/p3/core/*.md`、`papers/p3/back.md`。`papers/p3/adjudication.csv` 已由 D41 ④ 定案，不在范围内。

## 输入

- 上述文件；`make build` 后的 `output/p3/`（看 auto 块填进去的考情与刷题清单）。
- `corpus/rows/p3/*.jsonl`（`ms_text`、`types`、`markpoints`、`er`）；`skill/cie-9618-cs-tutor/scripts/rows.py`（`get`、`render <行 id> [--ms]`）。
- 原件（只读）：`/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/`（QP、MS、ER），`sources/official/9618_pseudocode_guide_2027-2029.pdf`（伪代码唯一权威写法）。
- 规则：`AGENTS.md` §5、`schemas/card-format.md`、`tasks/T26-card-audit.md`（审计项 1–7、findings 字段与取值）、`docs/DECISIONS.md`（D1、D2、D10、D25、D26、D29、D33–D35、D37、D39、D40、**D41**）、`papers/p3/tagging-guide.md`。

## 审计项

**T26 的 7 项全部照做**（引文用法、代表题精讲满分与 MP 对齐、选题规则、事实与计数、“讲解时请对照原卷 QP p.N”页码、概念表与 front / back、Python 片段）。另加 P3 特有的五项：

1. **抽取文本丢了的符号**：布尔表达式的横线（BL 章）、浮点数的上标与负号（DR 章，如 “2120” = 2^120）、图里的连线与权值（AI 章）在 `ms_text` 里会丢。卡里凡是写了这类表达式、数值或连线的地方，一律对照 **MS / QP 原页渲染图**核对，不能只比 `ms_text`。BL 的表达式再用真值表验算一遍。
2. **算法过程表**：Dijkstra、A*、RPN 栈、追踪表、二分查找等逐步表，按 QP 原页的图 / 数据重算一遍，最后结果与 MS 一致，中间步骤自洽（“教学格式，MS 不要求”的列不算错）。
3. **伪代码与汇编、Prolog**：写代码题型（DR-03、DR-05、CT-02、CT-03、CT-06～CT-09、FP-05、FP-06、FP-10 等）的伪代码符合 2027–29 指南，无 D2 禁用写法，不依赖 AND 短路（D25）；汇编题的指令与该卷 QP 给的指令表一致；Prolog 子句的语法与该题 MS 一致。
4. **D41 已定的例外不报**：D41 ① 接受的变式替代（SY-05、AI-04、AI-07、CT-03、FP-01 用 2021 扩展，CT-08 用同卷另一小问，HV-04、BL-02、BL-03 无第二道）、D41 ② `9618_w24_31:7(d)(ii)` 按 D.(A + B̅) 讲、D41 ③ 范围类型只作该题 MS 答案，都不算问题；但卡里实际写法与 D41 不符时要报。
5. **条件性规则**：密钥用法（加密 / 签名场合不同）、Dijkstra 只限非负权、MS 个别题接受的说法（如 `9618_s25_33:10(b)` 的“A* 能处理负权”）是否写明了适用条件，没有被写成普遍规律。

## 产出

- `papers/p3/audit/T36-findings.jsonl`：一条问题一行 `{"file","line","card","kind","severity","row","evidence","suggestion"}`；`kind` 在 T26 的取值上加 `symbol-lost`（抽取丢符号导致的错）、`algorithm-trace`（过程表算错）、`assembly-prolog`；`severity` ∈ `error` / `warn` / `nit`，含义同 T26。`evidence` 写原件页码与原文要点。
- `papers/p3/audit/T36-report.md`：每章统计（卡数、问题数按 kind / severity）、全部 `error` 的逐条说明、每张卡核对的 QP / MS 页码、哪些逐张全查与哪些靠脚本、脚本用法。
- 报告与 jsonl 里引用行号写**纯文本行 id**，不用 `⟦⟧`；引用 MS 原文用普通引号 “”，不用 `「」`（校验器会把它们当卡片引文审）。
- 审计脚本放 `papers/p3/audit/`（选题规则、计数重算、页码引用、伪代码 lint、Python 片段运行、真值表验算），可重复运行。T26 的 `papers/p1/audit/`、`papers/p2/audit/` 脚本可以复制过来改。

## 允许写的路径

`papers/p3/audit/**`、`tasks/progress/T36.md`。**不要改** `papers/p3/cards`、`core`、`front.md`、`back.md`、`corpus/`、`practice/`。

## 完成标准

- `make check` 全绿；`make check-scope TASK=T36` 全绿。
- 79 张卡的代表题都对照过 QP 与 MS 原页（报告列出页码）；带图、表达式、过程表的题看过原页渲染图；`error` 项每条都有原件证据。
- PR 描述：审计卡数、问题数（按 severity）、最严重的 5 条、「需要总控决定」（如对规则本身的疑问）。

## 工作方式

从最新 `origin/main` 开分支 `task/T36-p3-audit`；进度写 `tasks/progress/T36.md`；交付：rebase → `make check` → `make check-scope TASK=T36` → push → `gh pr create --base main --title "T36: audit P3 handbook"`。不要合并。
