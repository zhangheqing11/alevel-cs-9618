# 交接 · T38 审计 P4 题型手册（+ 抽查 6 道 P4 练习）

任务卡：`tasks/T38-p4-audit.md`（范围、10 项审计项、产出格式、完成标准）。前例：P1 / P2 的 T26（`papers/p1/audit/`、`papers/p2/audit/`：`check_handbook.py`、`run_python.py`、`T26-report.md`、`T26-findings.jsonl`）、P3 的 T36（`papers/p3/audit/`）——**先通读 `papers/p2/audit/T26-report.md` 与 `papers/p3/audit/T36-report.md` 学格式与口径，脚本可以复制改写。**

## 执行方案

1. **建 worktree**（交接 README §1，新分支 `task/T38-p4-audit`），`make build` 生成 `output/p4/`。
2. **机械检查脚本**（`papers/p4/audit/check_handbook.py`，从 P2 版改）：
   - 选题规则：抽出每张卡的代表题 / 变式行 id，查年份 2022–25、`types.primary` = 本型、两者不同卷、非 s26、非 `equivalent_of`（例外按 D41 ①，卡里应写明）。
   - 页码：卡里所有 “QP / MS p.N” 与行的 `qp_page` / `ms_page` 比对，差异列出供人工看图确认。
   - 得分点地图重算：口径（核验语料 2022–2026s、主题型行、同一行同一标签计一次、去 `equivalent_of`；s26 只进计数）与卡里写明的口径一致，差 ≥ 2 的列出。
   - Python：所有 ```python 块 `ast` 解析；“完整作答”块提取成文件，复制官方源文件（`pipeline/extract/source_files_p4.json`，`$ALEVEL_CS_SOURCES/pastpapers/<sf>/`）到临时目录后运行，记录输出（`papers/p4/audit/run_python.py`）。
3. **逐张人工审**（按章：PR、AR、FL、SR、RC、SQ、LT、OP、MP，再 front / back）：每张卡渲染代表题的 QP 与 MS 原页（`rows.py render <行> [--ms] --pages N --out <临时>`），逐项过任务卡的 10 个审计项；运行结果与 MS 截图比对；把问题写进 jsonl（每条附原件页码与要点）。
4. **6 道练习抽查**：每道对照 QP 原页核 task.md 转写、对照 MS 核证据格对照表；用参考解跑 `make try EX=practice/p4/<名>`（把 `ref/solution.py` 复制到 `attempts/` 同路径后跑，跑完删掉 attempts 副本）；再写一个“正确但写法不同”的版本（如 `while` 代 `for`、不同变量名）跑一遍，看测试是否过度限定。
5. **报告**：`T38-report.md`（每章统计、error 逐条、每张卡核对的页码、运行方式与结果、练习抽查、OP 章换题建议）。
6. 交付：rebase → `make check` → `make check-scope TASK=T38` → push → `gh pr create --base main --title "T38: audit P4 handbook"`。

## 提醒

- 只出报告，不改卡片、练习、语料；建议写进 `suggestion`。
- D45 已列出 12 处已知 MS 范例缺陷：审计时检查卡里是否说明、有无照抄；它们本身不算新问题。
- 报告与 jsonl 用纯文本行 id（不用 `⟦⟧`、`「」`），以免校验器把它们当卡片引文。
