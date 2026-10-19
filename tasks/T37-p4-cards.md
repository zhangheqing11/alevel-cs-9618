# T37 · P4 题型卡 + 伪代码 ↔ Python 对照（设计：子智能体 Opus 5.5 high，两批并行）

## 目标

写出学生学 P4（Python 上机卷）用的手册：36 个题型各一张题型卡、每章一份「伪代码 ↔ Python 对照与模板」，外加卷首与书末。P4 的卡片核心是**能照着在考场上从空文件写出拿满分的 Python**，并知道证据文档里每一格怎样给分。**讲解质量第一，证据规则第一**。

## 分批

| 批 | 章 | 题型数 | 另写 |
|:--|:--|--:|:--|
| A | PR、AR、FL、SR、RC | 17 | `papers/p4/front.md`（使用指南、记号、P4 考情总览 `auto:chapter-stats`、P4 通用得分规则：模块头 “(and end where appropriate)”、类型注释、按伪代码结构、截图格等，每条附 MS 原句） |
| B | SQ、LT、OP、MP | 19 | `papers/p4/back.md`（跨章入口：按题目特征找题型；一道大题的典型得分链：声明 → ADT 操作 → 读文件 → 主程序 → 截图；证据文档怎样交；P4 命令词与 MS 常用语） |

## 输入

- `papers/p4/taxonomy.json`（9 章 36 型）、`papers/p4/tagging-guide.md`（含 D43 修订）、`papers/p4/skill_tags.json`（extends P2）、`corpus/tag_report_p4.md`、`papers/p4/practice-notes.md`。
- `corpus/rows/p4/*.jsonl`：`types`、`markpoints`（2311 点，逐字 MS + 技能）、`ms_max`、`er`、`equivalent_of`。按题型取行：`python3 skill/cie-9618-cs-tutor/scripts/rows.py drills <题型码> --all`；看原页 `rows.py render <行 id> [--ms]`。**MS 的 Python 范例在 `ms_text` 里丢了缩进，必须看 MS 原页渲染图。**
- 原件（只读）：`/Users/zhangheqing/Desktop/alevel cs/sources/`——QP / MS / ER、源文件目录 `pastpapers/9618_<季><yy>_sf_<卷号>/`、2027–29 考纲（第 19–20 节）、伪代码指南 2027–29。
- **范本**：P2 手册（`papers/p2/cards/*.md`、`core/*.md`：伪代码模板、得分点地图、MP 对齐表、同题 Python 版要点）与 P3 写代码题型卡（`papers/p3/cards/CT.md`、`FP.md`）；`schemas/card-format.md` 严格遵守。阶梯 `ladder/levels/L01–L12/card.md`（P4 前置技能）。
- 决策：`docs/DECISIONS.md` D1、D2、D10、D13、D24、D25、D26、D29、D31、D33、D37、D40、D41、D42、D43、D44；教学协议 `skill/cie-9618-cs-tutor/SKILL.md` 与 `references/programming.md`。

## 每张题型卡

结构同 P2 写代码题型：标题 `### P4-XX-NN　中文名　{#P4-XX-NN}` + `<!-- auto:stats P4-XX-NN -->`、考法、识别信号、解题思路、得分表述（3–6 条 `「MS 原文」⟦行 id⟧`，优先取 MS 开头语言无关清单里的句子）、易错与失分（ER 只作易错，写“考官报告指出 …（行 id）”，不用「」）、代表题精讲、下一道变式、`<!-- auto:drills P4-XX-NN -->`。章首核心思想 + `<!-- auto:type-tree -->`，章末本章易混辨析。另加三项：

1. **Python 模板**：该型标准骨架（模块头、类型注释 / 数组注释（D10 ①）、指针初值照题目（D10 ②）、`try` / `except`、`if __name__ == "__main__":` 入口），按考场写法；需要时并列 QP 给的伪代码与对应 Python（1 起 / 0 起下标、带界数组 → 固定长度 list、`REPEAT`、`DIV` / `MOD`）。
2. **得分点地图**：按 `markpoints[].skills` 统计（口径：核验语料 2022–2026s、主题型行、同一行同一标签计一次、去掉 `equivalent_of`；s26 只进计数），告诉学生“这几分几乎每次都有”；写明口径。
3. **对应练习与阶梯**：指向该型代表题所在大题的练习目录 `practice/p4/<卷>_q<题号>/`（T35 正在并行生成，目录名按该规则，可在卡里写纯文本路径）与前置阶梯级 `Lxx Eyy`（确认存在）。

**代表题精讲**：在考什么 → 完整作答（**完整可运行的 Python**，能按该题 MS 拿满分；读文件的题用官方源文件跑一遍）→ 与 MS 逐点对齐（按 `markpoints[].n`，与 MS 印的编号不一致时列对照，D37 ②；`ms_max` 写清 Max）→ 证据格怎么交 → 直观。截图格（MP-03）讲“截图里必须看得到什么”（只按该行 MS）。

**选题**：代表题与变式都在 2022–25、主题型行、不同卷、非 s26、非 `equivalent_of`；找不到时按 D41 ① 的顺序替代（2021 扩展 → 同卷另一小问 → 写明无第二道）。

## T26 / T36 审计教训（务必避开）

1. 不把 MS 的 “no X / not X” 句当定义；不把单题结论推广成无条件规则，规则写清适用条件（如指针约定按各题题干）。
2. “完整作答”按独立得分点数：`//` 是同一点的替代说法；`Max n` 写清；“(and end where appropriate)”“…” 接续点不要拆错。
3. “讲解时请对照原卷 QP p.N”的页码逐个核对；类图、给定伪代码、测试数据表在哪一页写清。
4. 手写统计数字要么由脚本算出并写口径，要么不写；“最常见”只在 ER 原文这么说时用。
5. 官方代码或 MS 范例有缺陷（越界、笔误）时不照抄成标准答案：照 MS 说明得分点，自己的模板处理边界，并注明（D44 ④）。
6. Python 片段必须能运行：每个完整作答在示例数据上实际跑过（PR 里写明怎样跑的）；不用 `in`、`sort()`、`index()`、`max()` 代劳题目要求的算法（D10 ③），用到时注明。

## 允许写的路径

- A：`papers/p4/front.md`、`papers/p4/cards/{PR,AR,FL,SR,RC}.md`、`papers/p4/core/{PR,AR,FL,SR,RC}.md`、`tasks/progress/T37A.md`
- B：`papers/p4/back.md`、`papers/p4/cards/{SQ,LT,OP,MP}.md`、`papers/p4/core/{SQ,LT,OP,MP}.md`、`tasks/progress/T37B.md`
- 不要改 `corpus/`、`taxonomy.json`、`tagging-guide.md`、`practice/`（发现标签错写进 PR「需要总控决定」）。

## 完成标准（每批）

- `make check` 全绿；`make check-scope TASK=T37A|T37B` 全绿；`python3 build/build.py p4` 能生成（单批时 front / back 可能缺一，本批的卡都要出现在 `output/p4/`）。
- 每张卡的代表题都对照过 QP 与 MS 原页（PR 里列页码）；每个完整作答的 Python 都实际跑过。
- PR 描述：本批题型数、代表题与变式清单（附原页）、需要学习时对照原页的题、Python 运行方式与结果、自查上面六条教训的结果、「需要总控决定」。

## 工作方式

从最新 `origin/main` 开分支 `task/T37A-p4-cards`（或 B）；每写完一章提交一次并更新进度日志；交付：rebase → `make check` → `python3 build/build.py p4` → `make check-scope TASK=T37A|B` → push → `gh pr create --base main --title "T37 batch A: P4 front + PR/AR/FL/SR/RC cards"`（B：`T37 batch B: P4 SQ/LT/OP/MP cards + back`）。不要合并。
