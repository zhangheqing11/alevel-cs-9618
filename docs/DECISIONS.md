# 决策记录

> 总控维护。每条：日期 · 来源 · 决定 · 依据。任务卡与 skill 与此冲突时以此为准，并修正那一方。

## 2026-10-16 · T10 批 1 / T11 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D1 | T11 | **保留 `9618_s26_*`（12 份）给 4–5 月限时整卷模考**；专项刷题与复测跳过。题型卡代表题/变式若来自 s26 照常使用。T20–T23 选代表题与变式时**优先避开 s26**。 | 学生选择 |
| D2 | T11、T10 | P2 要求 pseudocode 时，混入编程语言语法或插页以外的语言函数（`def`、`len()`、切片、`FOR x IN file` 等）**该得分点不给**；非指南但非语言特有的写法（如考官范答中的 `ELSIF`、`INPUT a, b, c`）只有该题 MS 原文显示接受时才给，否则按不给并给出指南写法。阶梯与手册只教指南写法。 | s24 ER：“if the question asks for pseudocode, then variations with their studied programming language will be unacceptable”；`FOR Line IN InputFile` 列为常见错误；s23 ER 同义 |
| D3 | T11 | 编程题型**没有练习文件夹时不能标「已掌握」**：伪代码按 MS 批，Python 按样例手动核对，标「学习中」，解释证据写「无 pytest，待练习建成后补测」。 | 学生规则：编程题以测试过关 |
| D4 | T11 | 错误分类增加「手算与单位」。 | 禁用计算器（考纲 p.11） |
| D5 | T11 | 学习会话只 `git add ledger handoff attempts` 并 commit，不 push/pull/切分支；**总控负责推送**（合并 PR 后 `git pull --rebase` 再 `git push`）。 | 主 checkout 由总控与学习会话共用 |
| D6 | T11 | 草稿图片放 `work/tmp/figures/`（已 gitignore）。辅助脚本留在 `skill/cie-9618-cs-tutor/scripts/`，总控以后补冒烟测试。 | — |
| D7 | T10 | `tools/testkit.py` 新增 `output_lines(text)`（规则同 `ScriptResult.lines`），供 `io`/`trace` 型测试配 `capsys`。 | 避免每个测试各写一份 |
| D8 | T10 | **技能标签只有一份词表**：T21 以 `ladder/design.md` §7.8 为种子合并进 `papers/p2/skill_tags.json`（不做映射）；之后阶梯与 P2/P4 练习的 `meta.skills`、行的 `markpoints[].skills` 都取自它（P4 用 `extends`）。 | 失分技能要跨阶梯与真题统计 |
| D9 | T10 | `ledger/ladder.csv` 的「优先级」列一律 `★★★`（全部必修）。 | 阶梯无构建统计 |

## 2026-10-16 · T10 批 2 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D10 | T10 | P4 批改与教学口径：①数组要建出真实 list 并注释大小与类型（只写注释或空 list 不给声明分）；②题目给了指针初值就照题目用；③题目要求写算法时不用 `in`、`sort()`、`index()`、`max()` 等内置函数代劳。已写进 skill `references/programming.md` §8。 | ER s23 9618/41 Q3 p.39；ECR P4 2021 p.39 |
| D11 | T10 | T14 照抄规格里的数据文件：规格中的 `·` 表示普通空格；规格注明「最后一行不换行」的文件（如 L07 `trailing.txt`）必须不以换行结尾。 | 文件内容决定测试结果 |
