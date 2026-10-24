# T38b / T38c · 按 P4 审计修正手册与练习（执行工位 codex）

审计报告：`papers/p4/audit/T38-report.md`、`papers/p4/audit/T38-findings.jsonl`（F01–F09 = jsonl 行序）。裁决：`docs/DECISIONS.md` **D46**。

## T38b · 改 P4 卡（一个会话）

1. F01–F04 按 findings 的 `suggestion` 与 D46 改：F01 AR-03 字段名说明；F02 LT-04 “语法错误”改为运行时 TypeError；F03 core/SQ.md 伪代码改成 `Stored ← PushAnimal(AnimalReturned)`（不 CALL 函数）；F04 OP-03 写明同题 MS 接受“撤销本次增量或赋最大值”，ER 不覆盖 MS。
2. **OP 换题**（D46）：OP-02 代表题改为 `9618_s24_42:2(a)(iii)`、OP-03 改为 `9618_w25_42:1(a)(iv)`、OP-07 改为 `9618_s25_42:3(d)(ii)`；原代表题挪作“下一道变式”或删去（变式与代表题须不同卷）。新代表题照卡片标准写全：对照 QP / MS 原页、完整可运行 Python（在官方源文件 / QP 数据上跑过，输出与 MS 一致）、MP 对齐表、证据格怎么交、对应练习路径。参考审计报告里的换题说明。
3. 产出 `papers/p4/audit/T38-fixes.md`（F 编号 / 换题 → 文件与行 → 改动摘要 → 运行结果）。
4. 允许路径：`papers/p4/cards/**`、`papers/p4/core/**`、`papers/p4/front.md`、`papers/p4/back.md`、`papers/p4/audit/T38-fixes.md`、`tasks/progress/T38b.md`。
5. 交付：`make check` → `python3 build/build.py p4` → `make check-scope TASK=T38b` → PR “T38b: fix P4 handbook per audit (incl. OP rep swaps)”。

## T38c · 排查并修正全部 54 道 P4 练习（三个会话并行）

| 子任务 | 练习（= 原 T35 子批的目录） | 含审计已发现 |
|:--|:--|:--|
| T38c1 | T35a + T35b 的 17 道 | F05 `9618_s24_42_q3` |
| T38c2 | T35c + T35d 的 19 道 | F06 `9618_s25_42_q1`、F07 `9618_w24_41_q3` |
| T38c3 | T35e + T35f 的 18 道 | F08 `9618_s24_41_q2`、F09 `9618_w25_42_q1` |

每道练习按 `schemas/exercise-format.md` P4 规则第 6、7 条（D46）排查三类问题并修正：

1. **调用链漏测**：对照表里标“自动”的主程序 / 调用点，测试是否真的观测到了调用？没有就用 `tools/testkit.run_script_traced` 补测（调用了什么、参数、返回值是否被输出 / 使用），或改标“人工”。**每道含主程序的练习加 `ref/mutant_hollow_main.py`**（功能模块照参考解，主程序不调用模块、直接打印期望结果），`make check-all` 会要求它挂掉。
2. **过严误拒**：整段输出提取数字严格相等、要求同一行、数组 / 容量收紧成恰好、未经 QP 规定的格式——放宽到 QP / MS 实际要求（D31）。
3. **等价改写自测**：每道写 1–2 个“正确但写法不同”的版本（不同循环、多一行说明文字、信息分两行、数组大一些……），必须全部通过；写在临时目录，不入库，结果记进报告。

同时更新该题 `task.md` 证据格对照表的自动 / 人工归类、manifest 的 `auto_marks` / `manual_marks` / `auto_share`，以及 README 里受影响的数字。

产出：修正后的练习、`practice/p4/T38c-sweep-<1|2|3>.md`（逐题：发现的问题、改动、hollow-main 结果、等价改写结果、自动占比变化）。允许路径见 `tasks/scope.json` 的 `T38c1`–`T38c3`（各自的练习目录、manifest、README 与 sweep 报告）。交付：`make check-all` → `make check-scope TASK=T38c<n>` → PR “T38c<n>: harden P4 practice tests (call chains, over-strict output)”。
