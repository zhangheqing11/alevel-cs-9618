# T12 · 抽文本、拆最细小问（执行工位 codex-1）

> **开工前提**：T01 已合并（`corpus/inventory.csv` 在 main 上，PDF 已下载到主 checkout 的 `sources/pastpapers/`）。总控会通知你。在此之前先做 T13。

## 目标

把 2021–2026s 全部 9618 真题（四张卷、全部 variant）切成**最细一级小问**，每个小问配上它自己的 MS 原文，写成 `corpus/rows/p<N>/<卷>.jsonl`。下游的题型归类、手册统计、引文审计、练习生成全部依赖这份数据，**准确性优先于速度**。

## 输入

- `corpus/inventory.csv`（卷清单、文件名、`total_marks`）。
- PDF：`$ALEVEL_CS_SOURCES/pastpapers/`（默认 `/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/`）。worktree 里没有 `sources/`，用这个绝对路径；只读。
- 规范：`schemas/corpus-format.md`（**逐条遵守**）、`schemas/row.schema.json`。

## 9618 试卷特征（帮助你写解析器）

- 四张卷总分均为 75（以 inventory 的 `total_marks` 为准）。
- QP：大题号 `1`、`2`…，小问 `(a)(b)`、再下 `(i)(ii)`；每个计分小问行末有 `[n]`。表格题、"Complete the table/diagram" 常只有一个 `[n]`。P2/P4 有大段代码清单与表格，P4 题干会指定标识符名与文件名。
- MS（2021 起的新版式）：前几页是通用评分说明，之后是 **Question | Answer | Marks** 三列表格，Question 列形如 `1(a)(i)`。Answer 常是要点列表、"One mark per bullet point / Max 3"、"MP1…MP7"。P2 的伪代码题和 P4 的编程题会给示例代码；P4 通常并列 Java / VB.NET / Python 三种示例——**全部保留在 `ms_text` 里**。
- P2 带一份插页（`in`，内置函数表），不是题目，不要切。
- 有时 MS 的 Marks 列给的是小问总分而 Answer 下有更细分点：以 QP 的 `[n]` 为准确定行，MS 文本挂到对应行。

## 建议做法

1. `pipeline/extract/pdf_text.py`：逐页抽文本（`pdftotext -layout` 保表格列位，PyMuPDF 取页码/坐标作辅助），缓存放到 `/tmp/alevel-cs-extract/`（仓库外，不提交）。
2. `split_qp.py`：识别题号层级与 `[n]`，得到叶子列表（题号、分值、页码、题干、父级上下文）。
3. `parse_ms.py`：解析 MS 表格，按 Question 列切块。
4. `align.py`：按题号对齐 QP 叶子与 MS 块；对不上的标 `ms-misaligned`；检查分值和 = `total_marks`；QP `[n]` 与 MS Marks 列不一致时标 `marks-unclear` 并在报告里列出。
5. `dedupe.py`：同季不同 variant、或跨卷逐字相同的小问填 `equivalent_of`。
6. `run_all.py`：一键重跑；输出 JSONL 与报告。

## 产出

- `pipeline/extract/*.py`（可重跑、无手工步骤；手工修正写成 `pipeline/extract/overrides.json`：按行 id 覆盖字段，并注明原因）。
- `corpus/rows/p<N>/<卷>.jsonl`。
- `corpus/extract_report.md`：每卷叶子数、分值和、各类 flag 数；全部未解决问题清单；**每张卷随机抽 5 个叶子人工对照 PDF 的核验记录**（题号、你看到的、是否一致）。

## 分批交付（每批一个 PR，按 AS 先行）

1. P1（`corpus/rows/p1/`）——设计工位要先用它设计 P1 题型。
2. P2。
3. P3。
4. P4。

## 允许写的路径

`pipeline/extract/**`、`corpus/rows/**`、`corpus/extract_report.md`、`tasks/progress/T12.md`。

## 完成标准（每批）

- `make check` 全绿：schema 合法、id 唯一、**每卷分值和 = total_marks**、每行有 MS（或已标 `ms-misaligned`）。
- `make check-scope TASK=T12` 全绿。
- flag 比例：`ms-misaligned` + `split-uncertain` 合计 < 3% 的行；超过时在 PR 里说明原因。
- 报告里有抽查记录。

## 工作方式

```bash
cd ~/Desktop/"alevel cs" && git fetch origin
git worktree add ~/Desktop/alevel-cs-wt/T12 -b task/T12-extract-rows origin/main
cd ~/Desktop/alevel-cs-wt/T12 && codex
```

进度写 `tasks/progress/T12.md`；交付：`git fetch origin && git rebase origin/main` → `make check` → `make check-scope TASK=T12` → `git push -u origin HEAD` → `gh pr create --base main --title "T12 P1: …"`。不要合并。
