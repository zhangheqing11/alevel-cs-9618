# T26 · 审计 P1 / P2 题型手册（执行工位 codex，跨模型交叉审计）

## 目标

P1（88 张卡）与 P2（46 张卡）的题型手册由 Claude 设计工位写成（T22、T23），总控抽查过但没有逐张核对。本任务由**另一家模型**逐张审计：卡里每一处给分说法、引文用法、代表题满分作答、得分点地图与选题是否站得住。**只出报告，不改卡片**（卡片归设计任务）；总控按报告转成修正任务。

分两半并行：

| 子任务 | 工位 | 审计范围 |
|:--|:--|:--|
| **T26a** | codex-1 | `papers/p1/front.md`、`papers/p1/cards/*.md`（9 章 88 张）、`papers/p1/core/*.md`、`papers/p1/back.md` |
| **T26b** | codex-2 | `papers/p2/front.md`、`papers/p2/cards/*.md`（4 章 46 张）、`papers/p2/core/*.md`、`papers/p2/back.md` |

## 输入

- 卡片与概念表（上表）；构建结果 `make build` 后的 `output/p<N>/`（看 auto 块填进去的考情与刷题清单）。
- `corpus/rows/p1|p2/*.jsonl`（`ms_text`、`types`、`markpoints`、`er`）；`skill/cie-9618-cs-tutor/scripts/rows.py`（`get`、`render <行 id> [--ms]`）。
- 原件（只读）：`/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/`（QP、MS、ER），`sources/official/9618_pseudocode_guide_2027-2029.pdf`（伪代码唯一权威写法）。
- 规则：`AGENTS.md` §5（给分只认该题自己的 MS；ER 只用于易错；教材只用于概念）、`schemas/card-format.md`、`docs/DECISIONS.md`（D1、D2、D15、D25、D26、D29–D32、D37）、`papers/p<N>/tagging-guide.md`。

## 审计项（每张卡都要过；`make check` 已保证引文是 ms_text 子串、行 id 存在，这里查的是**意义**）

1. **引文用法**：每条 `「MS 原文」⟦行 id⟧` 是否真的支持卡里紧挨着的那句说法——是该题自己的 MS、语境没被截断误用（如把 “Reject …” 当成要写的答案、把某一选项当成唯一答案、把另一小问的点挂到这一行）。
2. **代表题精讲**：对照该题 QP 与 MS 原页——题干转述是否准确；“完整作答”是否真能按该题 MS 拿满分（逐个 MP 对、Max 对、`(and subsequently close)` 等合并点没被拆开）；“与 MS 对齐”表的 MP 编号与原文是否对得上（编号不一致时按 D37②，卡里应有说明）。P2 另查：作答伪代码是否符合 2027–29 指南（关键字、`←`、`DECLARE`、`ENDIF`/`ENDWHILE`/`NEXT x`、`OPENFILE … FOR …`、插页函数名与参数顺序），有无 D2 禁用写法、有无依赖 AND 短路（D25）。
3. **选题规则**：代表题与变式都在 2022–25、都是该型主题型行（`types.primary`）、两者不同卷、不用 s26（D1）、不用 `equivalent_of` 重复行。
4. **事实与计数**：卡里手写的数字（“MS 列 8 点”“Max 6”“考了 n 次”“题数”）与原件 / 语料一致；P2 得分点地图按卡里写明的口径用脚本重算，差 ≥ 2 的列出。
5. **“讲解时请对照原卷 QP p.N”**：页码与所指图 / 表 / 代码是否正确。
6. **概念表与 front/back**：英文得分句是否来自所引行的 MS；中文定义与 MS 是否冲突（与教材冲突时以 MS 为准，AGENTS.md §5）；跨章入口表指向的题型码是否合理。
7. **Python 片段**（P2 为主）：能 `ast` 解析；短片段在示例输入上实际跑一遍，结果与卡里说的一致；不违背 D10（不拿内置函数替代题目要求的算法而不加说明）。

## 产出

- `papers/p<N>/audit/T26-findings.jsonl`：一条问题一行 `{"file","line","card","kind","severity","row","evidence","suggestion"}`；`kind` ∈ `quote-misuse`、`answer-not-full-marks`、`mp-alignment`、`pick-rule`、`count`、`qp-page`、`pseudocode`、`python`、`concept`、`other`；`severity` ∈ `error`（会让学生丢分或学错）、`warn`（不准确但不致错）、`nit`（措辞）。`evidence` 写原件页码与原文要点。
- `papers/p<N>/audit/T26-report.md`：每章统计（卡数、问题数按 kind / severity）、全部 `error` 的逐条说明、抽查范围说明（哪些是逐张全查、哪些靠脚本）、自动检查脚本的用法。
- 报告与 jsonl 里引用行号写**纯文本行 id**，不要用 `⟦⟧`，引用 MS 原文用普通引号 “”，不要用 `「」`（校验器会把它们当卡片引文审，同 T20 的约定）。
- 审计脚本放 `papers/p<N>/audit/`（选题规则、计数重算、页码引用、伪代码 lint、Python 片段运行），可重复运行。
- 进度写 `tasks/progress/T26a.md` / `T26b.md`。

## 允许写的路径

T26a：`papers/p1/audit/**`；T26b：`papers/p2/audit/**`（各自的进度日志同理）。**不要改** `papers/*/cards`、`core`、`front.md`、`back.md`、`corpus/`、`practice/`。

## 完成标准

- `make check` 全绿；`make check-scope TASK=T26a`（或 `T26b`）全绿。
- 每张卡的代表题都对照过 QP 与 MS 原页（报告里列出每张卡核对的页码）；`error` 项每条都有原件证据。
- PR 描述：审计卡数、问题数（按 severity）、最严重的 5 条、「需要总控决定」（如对规则本身的疑问）。

## 工作方式

从最新 `origin/main` 开分支 `task/T26a-p1-audit`（或 `task/T26b-p2-audit`）；交付：rebase → `make check` → `make check-scope TASK=T26a|T26b` → push → `gh pr create --base main --title "T26a: audit P1 handbook"`（或 `T26b: audit P2 handbook`）。不要合并。
