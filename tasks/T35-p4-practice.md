# T35 · P4 真题练习文件夹（执行：子智能体，六个子批并行）

## 目标

把 P4（Python 上机卷）2022–25 核验语料的 **54 道大题**各做成一个可以自动测的练习文件夹，供学生按题型练、按得分点自测。约定已由 D42 ④ 定稿：`papers/p4/practice-notes.md`（全文照做）+ `schemas/exercise-format.md` 末节「P4 真题练习」。

## 分批（六个子批同时开，各写各的目录）

按每道大题得分最多的章分三批（与学习顺序一致），每批再按考季拆两半。

| 子批 | 内容 | 题数 | 分 | 大题（目录名 = `practice/p4/<名>/`） |
|:--|:--|--:|--:|:--|
| **T35a** | 批 1 前半 · PR/AR/FL/SR/RC（s 季） | 9 | 201 | `9618_s22_41_q1`、`9618_s22_42_q2`、`9618_s23_41_q1`、`9618_s23_42_q1`、`9618_s24_41_q1`、`9618_s24_42_q1`、`9618_s24_42_q3`、`9618_s25_41_q2`、`9618_s25_43_q2` |
| **T35b** | 批 1 后半 · PR/AR/FL/SR/RC（w 季） | 8 | 164 | `9618_w22_41_q1`、`9618_w22_42_q1`、`9618_w23_41_q1`、`9618_w23_42_q2`、`9618_w24_41_q1`、`9618_w24_42_q3`、`9618_w25_42_q2`、`9618_w25_43_q3` |
| **T35c** | 批 2 前半 · SQ/LT（s 季 + w22_41） | 10 | 232 | `9618_s22_41_q3`、`9618_s22_42_q1`、`9618_s23_41_q3`、`9618_s23_42_q2`、`9618_s24_41_q3`、`9618_s25_41_q1`、`9618_s25_42_q1`、`9618_s25_42_q2`、`9618_s25_43_q1`、`9618_w22_41_q3` |
| **T35d** | 批 2 后半 · SQ/LT（w 季） | 9 | 215 | `9618_w22_42_q3`、`9618_w23_41_q2`、`9618_w23_42_q1`、`9618_w24_41_q3`、`9618_w24_42_q2`、`9618_w25_41_q1`、`9618_w25_41_q3`、`9618_w25_42_q3`、`9618_w25_43_q2` |
| **T35e** | 批 3 前半 · OP（s 季） | 9 | 263 | `9618_s22_41_q2`、`9618_s22_42_q3`、`9618_s23_41_q2`、`9618_s23_42_q3`、`9618_s24_41_q2`、`9618_s24_42_q2`、`9618_s25_41_q3`、`9618_s25_42_q3`、`9618_s25_43_q3` |
| **T35f** | 批 3 后半 · OP（w 季） | 9 | 275 | `9618_w22_41_q2`、`9618_w22_42_q2`、`9618_w23_41_q3`、`9618_w23_42_q3`、`9618_w24_41_q2`、`9618_w24_42_q1`、`9618_w25_41_q2`、`9618_w25_42_q1`、`9618_w25_43_q1` |

不在表里的：2021 扩展卷、s26（D1 留作模考）、与同季 `_41` 整卷相同的六份 `_43`（s22 / s23 / s24 / w22 / w23 / w24，D42 ④ 6）。

## 输入

- 约定：`papers/p4/practice-notes.md`（§1–§8）、`schemas/exercise-format.md`（含末节 P4 规则）、`schemas/exercise.schema.json`。
- 语料：`corpus/rows/p4/*.jsonl`（`types`、`markpoints`（逐字 MS + 技能）、`ms_max`、`er`）；`python3 skill/cie-9618-cs-tutor/scripts/rows.py render <行 id> [--ms]` 看原页。
- 原件（只读）：`/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/` 的 QP、MS 与源文件目录 `9618_<季><yy>_sf_<卷号>/`；每个源文件的相对路径、字节数、sha256 在 `pipeline/extract/source_files_p4.json`。
- 范本：P2 练习 `practice/p2/`（T25 三批，含 `README-batch*.md`、manifest 写法、人工核对清单）；工具 `tools/testkit.py`（`run_script`、`feed_input`、`output_lines`、**`use_files`**）、`conftest.py`（`sol`、`candidate_path`、`exercise_dir` fixture）。
- 决策：`docs/DECISIONS.md` D1、D3、D10、D11、D13、D24、D31、D37 ②、D42、D43。

## 每个练习

- 目录 `practice/p4/<卷>_q<题号>/`：`task.md`、`meta.json`、`starter.py`、`test_task.py`、`files/`、`ref/solution.py`、至少 2 个 `ref/mutant_*.py`。
- `task.md`：中文导读 + **从 QP 原页转写的英文原题**（全部小问、类图、给定伪代码照原样含 `←` 与带界数组、数据格式、测试数据表）+ **证据文档对照表**（practice-notes §6：每个证据格 → 行 id → 每个得分点是自动测（测试名）还是人工核对）+ 人工核对清单 + MS 编号与语料 `markpoints[].n` 不一致时的对照（D37 ②）。
- `starter.py`：只有分节注释与 `if __name__ == "__main__":` 入口（P4 骨架例外），不预写声明、类与模块头。
- `files/`：数据 `.txt` 从源文件**逐字节复制**，sha256 与 `source_files_p4.json` 一致；不复制 evidence.doc 与考务说明。
- `test_task.py`：按小问分组、测试名带小问号（`test_1b_…`）、docstring 写行 id 与 `markpoints[].n`；读数据文件的函数型测试用 `use_files`；截图格按 practice-notes §5 换成 `run_script` 输出断言（只断言该行 MS 列出的值；与 QP 正确运行结果不一致时按 QP，D31，并在 task.md 写明）；单个练习总时长 < 5 秒。
- `ref/solution.py`：贴近 MS 的 Python 范例（`ms_text` 里范例丢了缩进，要看 MS 原页），修掉范例笔误；`ref/mutant_*.py` 从该题 `markpoints` 的真实易错点挑（practice-notes §7 列表），文件头注释写对应行 id、得分点与技能。
- `meta.json`：按 practice-notes §4（`id` 取大题第一行，`source.rows` 列全部行，`marks` 为分值和，`types` / `skills` 为并集，`pseudocode: false`，`entry: "main"`，`ms_verified: true`）。

## 共享文件

各子批**不要**新建或修改 `practice/p4/` 下的共享文件（如 `_test_support.py`、`README.md`）：需要的辅助函数写在各自 `test_task.py` 里，或用 `tools/testkit.py` 已有的；需要给 `tools/` 加东西写进 PR「需要总控决定」。每个子批只写自己的清单 `practice/p4/manifest-<子批>.json`（目录、行、分值、题型、源文件 sha256）与 `practice/p4/README-<子批>.md`（数量、选题、对照原页情况、接口约定、已知问题）。

## 允许写的路径

各子批：表中自己的练习目录 `practice/p4/<名>/**`、`practice/p4/manifest-<子批>.json`、`practice/p4/README-<子批>.md`、`tasks/progress/<子批>.md`（机器可读版见 `tasks/scope.json` 的 `T35a`–`T35f`）。

## 完成标准（每个子批）

- `make check-all` 全绿（参考解全过、每个 mutant 至少挂一个测试、meta 过 schema、`files/` 齐全）；`make check-scope TASK=<子批>` 全绿。
- 表中每道大题都有练习；每个证据格在 `task.md` 对照表里有一行；每个截图格至少一个自动测试。
- `files/` 的 sha256 全部与 `source_files_p4.json` 一致（PR 里列出）。
- PR 描述：练习数与分值、每题自动测 / 人工核对的分值占比、对照原页情况（哪些题看了 QP / MS 渲染图）、与 MS 不一致按 QP 处理的地方、「需要总控决定」。

## 工作方式

从最新 `origin/main` 开分支 `task/<子批>-p4-practice`（如 `task/T35a-p4-practice`）；每做完一道大题提交一次并更新进度日志；交付：rebase → `make check-all` → `make check-scope TASK=<子批>` → push → `gh pr create --base main --title "<子批>: P4 practice (<内容>)"`。不要合并。
