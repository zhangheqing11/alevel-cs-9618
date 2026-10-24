# 交接 · T35 P4 真题练习（T35a–f）

任务卡：`tasks/T35-p4-practice.md`（分批表、每个练习的产出、完成标准）。约定：`papers/p4/practice-notes.md`（§1–§8，全文照做）、`schemas/exercise-format.md` 末节「P4 真题练习」。

## 现状（2026-10-24）

| 子批 | 分支 | 已完成 | 剩下 |
|:--|:--|:--|:--|
| T35a（批 1 前半 · s 季，9 题） | `task/T35a-p4-practice`（已推） | 6 题已提交（总控 `make check-all` 196 道全过）：s22_41_q1、s22_42_q2、s23_41_q1、s23_42_q1、s24_41_q1、s24_42_q1；`manifest-T35a.json` 已有前 6 题 | s24_42_q3、s25_41_q2、s25_43_q2；`README-T35a.md`；交付 |
| T35b（批 1 后半 · w 季，8 题） | `task/T35b-p4-practice`（已推） | 7 题已提交；第 8 题 `9618_w25_43_q3` 以 **WIP 提交**（a0e7778，**未验证；总控跑 `make check-all` 时报 `missing task.md`**，其余 7 题全过） | 验证并补完 w25_43_q3；`manifest-T35b.json`、`README-T35b.md`；交付 |
| T35c（批 2 前半 · SQ/LT，10 题） | 新开 `task/T35c-p4-practice` | — | 全部 |
| T35d（批 2 后半 · SQ/LT，9 题） | 新开 `task/T35d-p4-practice` | — | 全部 |
| T35e（批 3 前半 · OP，9 题） | 新开 `task/T35e-p4-practice` | — | 全部 |
| T35f（批 3 后半 · OP，9 题） | 新开 `task/T35f-p4-practice` | — | 全部 |

六个子批写的目录互不重叠，可以同时开。T35a / b 已完成的 13 道是全体子批的**范本**（先读 2–3 道：一道读文件的如 `9618_s22_41_q1`、一道无数据文件的如 `9618_s24_41_q1`、一道带随机数的如 T35b 的 `9618_w25_42_q2`）。

## 每道大题的执行方案（照这个顺序做，做完一道提交一道）

1. **列行**：`python3 skill/cie-9618-cs-tutor/scripts/rows.py drills` 或直接读 `corpus/rows/p4/<卷>.jsonl`，取该大题全部小问行（`q` 以题号开头），记下每行 `types`、`markpoints`（`n`、`text`、`marks`、`skills`）、`ms_max`、`er`、`qp_page`、`ms_page`。
2. **看原页**：渲染 QP 该题所有页、MS 对应页（`rows.py render <行> --pages N --out <临时目录>`，读图）。**MS 的 Python 缩进只能看渲染图**（`ms_text` 与 `pdftotext` 都会把缩进弄乱；判定范例有错之前必须看图）。证据文档格子可用 `textutil -convert txt <sf>/evidence.doc -output <临时>` 读（只读源文件，输出放临时目录）。
3. **数据文件**：从 `$ALEVEL_CS_SOURCES/pastpapers/<sf 目录>/<相对路径>` 用 `shutil.copyfile` 复制到 `files/`（路径见 `pipeline/extract/source_files_p4.json`），复制后核 sha256；CRLF、最后一行是否换行原样保留（仓库无 autocrlf）。不复制 evidence.doc 与考务说明。旧年份有额外一层目录，别假设 txt 在 sf 根。
4. **task.md**：中文导读 → **QP 原题英文转写**（全部小问、类图、给定伪代码含 `←` 与带界数组、数据格式、测试数据表）→ 「Python 接口」（入口、QP 未命名模块用 MS 范例名字、按 QP 处理与 MS 不一致之处，D31）→ **证据文档对照表**（每个证据格 → 行 id → 每个得分点是自动测（写测试名）还是人工核对）→ 人工核对清单 → MS 印的 MP 编号与语料 `markpoints[].n` 不一致时的对照（D37 ②）。
5. **starter.py**：只有分节注释与 `if __name__ == "__main__":` 入口，不预写声明、类与模块头（P4 骨架例外）。
6. **ref/solution.py**：贴近 MS 的 Python 范例，修掉范例笔误（在 task.md 注明）；完整可运行。
7. **test_task.py**：按小问分组，测试名带小问号（`test_1b_…`），docstring 写行 id 与 `markpoints[].n`；读数据文件的函数型测试用 `testkit.use_files`；截图格按 practice-notes §5 换成 `run_script` 输出断言（只断言该行 MS 列出的值）；随机数用 seed 包装或注入；单个练习总时长 < 5 秒；不对写法过拟合（`while` 代 `for` 等正确写法要能过），但要抓住用内置 `sort` / `index` / `in` / `max` 代劳题目算法的做法（D10 ③）。
8. **ref/mutant_*.py**：≥ 2 个，从该题 `markpoints` 的真实易错点挑（practice-notes §7 列表），文件头注释写行 id、得分点与技能。
9. **meta.json**：按 practice-notes §4（`id` 取大题第一行、`source.rows` 列全、`marks` 为分值和、`types` / `skills` 为并集、`pseudocode: false`、`entry: "main"`、`ms_verified: true`）。
10. **单题验证**：`CANDIDATE=practice/p4/<名>/ref/solution.py ~/.venvs/alevel-cs/bin/python -m pytest -q practice/p4/<名>/test_task.py` 全过；对每个 mutant 同样跑，必须至少一个测试失败。
11. **manifest + 进度**：在 `practice/p4/manifest-<子批>.json` 加本题条目（字段照 `manifest-T35a.json`：`directory`、`id`、`paper`、`marks`、`auto_marks` / `manual_marks` / `auto_share`、`types`、`rows[]`（`auto_mps` / `manual_mps` 用语料 `markpoints[].n`）、源文件 sha256、看过的原页）；更新 `tasks/progress/<子批>.md`；提交 `<子批>: add P4 practice <目录名> (<一句话内容>)`。

**自动 / 人工占比口径**（T35b 已用）：按得分点分值加权（`markpoints[].marks`；无 markpoints 的 1 分行按行分值）；只考函数头 / 类型注释 / 结构（translate-pseudocode、nothing superfluous）的点记人工，带行为的点记自动；可选点多于该行分值时按比例折算。

## 子批收尾

`README-<子批>.md`（数量、分值、选题、对照原页情况、接口约定、按 QP 处理的地方、已知问题）→ rebase → `make check-all`（全仓练习都要跑，约 3–5 分钟）→ `make check-scope TASK=<子批>` → push → `gh pr create --base main --title "<子批>: P4 practice (<内容>)"`。PR 描述按任务卡「完成标准」：练习数与分值、每题自动 / 人工占比、对照原页情况、按 QP 处理的地方、files sha256、「需要总控决定」。

## 已知的坑（来自 T35a / b 进度日志与 T37 的发现）

- zsh 不按空格拆未加引号的变量；路径含空格（`alevel cs`）一律加引号。
- QP 未命名的模块用 MS 范例名字，写进「Python 接口」。
- QP 给的伪代码本身可能有缺陷（如 `9618_s22_42` 的 Mid 公式）：测试避开或按 QP 正确运行结果断言，task.md 注明。
- 已核实的 MS 范例缺陷（不要照抄成参考解）：`9618_s22_41:1(e)(i)` score/Score；`9618_w22_41:2(c)(i)` range(0, 4)；`9618_w24_42:2(a)` 少 `self.`；`9618_s22_42:2(b)(ii)` printarray/Printarray；`9618_s24_41:3(d)(i)` `int(Data[6])` 遇 X 报错；`9618_w22_42:3(b)` 漏 `global HeadPointer`；`9618_s23_41:3(c)` 两栈都空时把 "" 压回。
- 局部数组的取值可用 `sys.settrace` 跟踪（T35b `9618_w24_42_q3` 的做法）。

## 各子批的提示词

见 `tasks/PROMPTS.md` 末尾「T35a 续做 / T35b 续做 / T35c / T35d / T35e / T35f」。
