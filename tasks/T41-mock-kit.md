# T41 · 整卷模考批改包（执行工位 codex）

## 目标

D1 把 2026 年 6 月的 12 份卷留作考前限时整卷模考；另有 2021 样卷（Specimen）可作补充。学生做完一份整卷后，需要一份**照着就能自己批改**的批改包：逐题列分值、该题自己的 MS 原文、拆好的得分点勾选表、考官报告易错，最后汇总原始分并按分数线估等级。本任务写生成脚本。

## 输入

- `corpus/rows/p<N>/*.jsonl`（`marks`、`ms_text`、`markpoints`、`ms_max`、`types`、`er`、`qp_page`、`ms_page`、`has_figure`）；`corpus/inventory.csv`（QP / MS / 插页 / 源文件路径）。
- `corpus/thresholds/`（T40 的分数线表；T40 未合并前，估分部分用占位并在报告注明）。
- 题型手册构建结果的锚点格式（`output/p<N>/P<N>题型手册.html#<题型码>`），用于“丢分后去哪张卡”。

## 产出

1. `pipeline/mock/make_mock.py <卷 id> [--out DIR]`：为一份卷生成 `output/mock/<卷 id>/`（`output/` 已 gitignore，不提交生成物）：
   - `marking.md` / `marking.html`：卷头（考试时长、总分、所需材料：QP 路径、P2 插页、P4 源文件目录）；逐小问一节：题号、分值、主题型（链接到手册卡）、`has_figure` 提示“对照 QP p.N”、该题 MS 原文、有 `markpoints` 时的勾选表（MP / 原文 / 分值 / 技能标签 / ✓✗ 空列）、`ms_max`、考官报告摘录（标明“仅供易错参考，不是给分依据”）。
   - `score.csv`：`row_id,marks_available,marks_awarded,lost_skills,note` 的空表（`utf-8-sig`），给学生填。
2. `pipeline/mock/score_mock.py <score.csv>`：汇总原始分、按题型 / 技能标签统计失分，给出该 component 在最近一季分数线下的等级（A–E；四卷都做时按 option 估 A*–E），输出一段可以贴进学习记录的摘要。
3. `pipeline/mock/test_mock.py`：用 1 份 s26 卷与 1 份普通卷测试——小问数与分值合计 75、MS 原文完整、markpoints 勾选表齐全、估分边界（刚好等于分数线）正确。
4. `pipeline/mock/README.md`：用法（考前怎么做、做完怎么批、批完把 `score.csv` 交给学习会话）。

## 规则

- 批改依据只用该题自己的 MS（AGENTS.md §5）；ER 只作易错参考，明确标注。
- 模考包不显示题型卡的代表题答案或刷题提示以外的内容；不复制题干（学生看原卷 QP）。
- 只读 `sources/`；生成物放 `output/`，不入库。
- 不改 `Makefile`（需要 `make mock` 目标时写进「需要总控决定」，总控来加）。

## 允许写的路径

`pipeline/mock/**`、`tasks/progress/T41.md`。

## 完成标准

- `make check` 全绿；`make check-scope TASK=T41` 全绿；`python3 -m pytest pipeline/mock` 通过。
- 能为全部 12 份 s26 卷生成批改包（PR 里贴一份 `marking.md` 的开头片段与文件清单）。
- PR 描述：用法、估分规则（与 T40 的关系）、已知限制、「需要总控决定」。

## 工作方式

从最新 `origin/main` 开分支 `task/T41-mock-kit`；交付：rebase → `make check` → `make check-scope TASK=T41` → push → `gh pr create --base main --title "T41: mock exam marking kit"`。不要合并。
