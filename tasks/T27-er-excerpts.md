# T27 · 考官报告逐题摘录挂到行（执行工位，Sonnet 5.5 · effort high）

## 目标

把考官报告（Principal Examiner Report for Teachers，ER）里**逐题的评论**摘出来，挂到对应小问行的 `er` 字段上，供题型卡的「易错与失分」、教学 skill 讲解失分原因使用。ER **不是给分依据**（AGENTS.md §5），只用于易错。

## 输入

- `sources/pastpapers/9618_<季><yy>_er.pdf`：每季一份，共 10 份（s21–w25；s26 尚无 ER）。每份按 `Paper 9618/<卷号>` 分段（11–13、21–23、31–33、41–43），段内先是 Key messages、General comments，然后 `Question N` 下按 `(a)`、`(b) (i)` 等小问给评论。
- `corpus/rows/p1|p2|p3/*.jsonl`（P4 行由 codex-1 之后抽取；脚本要能在 P4 行出现后直接重跑）。
- `schemas/row.schema.json` 的 `er` 字段（字符串）、`schemas/corpus-format.md`。
- 参照写法：`pipeline/tag/apply_tags.py`（逐行只改自己拥有的字段、`--check` 模式）、`pipeline/tag/p2/apply_p2.py`（`OWNED` 字段表）。`pipeline/extract/run_all.py` 已把 `er` 列为下游字段，不会覆盖它。

## 产出

1. `pipeline/er/extract_er.py`：解析 10 份 ER → `corpus/er/<季><yy>.jsonl`，每条 `{"paper": "9618_s24_31", "label": "6(c)(ii)", "text": "...", "page": 31}`；另把每卷的 Key messages + General comments 存为 `{"paper": ..., "label": "_general", ...}`。文本照 ER 原文（合并换行与多余空白，私用区字符按 D26 / D29 归一），不改写、不概括。
2. `pipeline/er/apply_er.py`：把摘录挂到行。规则：
   - 行 `q` 与某条 `label` 完全相同 → 用它；否则用**最近的上级**（`6(c)` 覆盖 `6(c)(i)`、`6(c)(ii)`；`6` 覆盖 `6(a)`…）。同一行若上级与本级都有，`er` = 本级原文；上级的总评只在本级没有时使用，并在开头标注范围，如 `[Q6] …`。
   - 只拥有 `er` 字段：其他字段与行顺序逐字节不变（同 `apply_tags.py` 的做法）；可重复运行，`--check` 返回是否有改动。
   - `_general` 不挂到行，留在 `corpus/er/` 供 skill 使用。
   - `extension` 行（2021）照样挂；s26 行没有 ER，不写 `er`。
3. `corpus/er_report.md`：每卷统计（ER 条数、挂上的行数、未匹配的 ER 标签及原因、没有 ER 的行数）；抽查记录。
4. `pipeline/er/test_er.py`：标签解析（`(b) (i)`、`(b)(i)`、`Question 6` 接续页等）、上级回退、只改 `er` 字段、可重复运行。
5. 进度写 `tasks/progress/T27.md`。

## 校验与抽查

- 每卷：ER 里出现的每个题号都要么挂上，要么在报告里说明为何没挂（行不存在、ER 题号笔误等）——**不得猜着挂**。
- 随机抽 20 条（每个卷别至少 4 条），打开 ER 原页核对摘录与题号，把页码与结论写进 `corpus/er_report.md`。
- ER 偶有把 variant 写错、或一段话同时评论两小问：照原文挂到它写明的题号，疑点列进报告「需要总控决定」。

## 允许写的路径

`pipeline/er/**`、`corpus/er/**`、`corpus/er_report.md`、`corpus/rows/**`（只改 `er` 字段）、`tasks/progress/T27.md`。不要改 `pipeline/extract/`、`pipeline/tag/`（codex-1 在做 P4 与 T12d）；发现它们会冲掉 `er` 时写进「需要总控决定」。

## 完成标准

- `make check` 全绿；`make check-scope TASK=T27` 全绿；`python3 pipeline/er/apply_er.py --check` 报无改动；测试通过。
- PR 描述：每卷挂上的行数、覆盖率、未匹配清单、抽查结果、已知问题、「需要总控决定」。

## 工作方式

从最新 `origin/main` 开分支 `task/T27-er-excerpts`。交付：`git fetch origin && git rebase origin/main`（若 rows 有冲突：取 main 的 rows，重跑 `apply_er.py`）→ `make check` → `make check-scope TASK=T27` → `git push -u origin HEAD` → `gh pr create --base main --title "T27: attach examiner-report excerpts to rows"`。不要合并。
