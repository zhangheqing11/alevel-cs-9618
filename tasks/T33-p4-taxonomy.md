# T33 · P4 题型体系 + 技能标签扩展 + 打标签指南 + 试标（设计工位，本地 Opus 5.5 · effort high）

## 目标

为 P4 Practical（2 小时 30 分钟上机，学生用 **Python**）设计题型体系、技能标签扩展与得分点拆分规则，作为之后全量打标签（T34，codex）、P4 题型卡（T36）和 **P4 上机练习**（T35，用官方源文件）的基础。做法与 P2 的 T21 相同：P2 的 `papers/p2/taxonomy.json`、`skill_tags.json`、`tagging-guide.md`（§3 写代码题归类、§8 得分点拆分）是直接范本。

## P4 的特点

- 744 行（32 卷；2021 扩展 99 行；`equivalent_of` 43 行；`has_figure` 584 行）。命令词 Write 502、Test 131、Amend 59：几乎全是“写程序 / 改程序 / 测试并截图”。
- MS 并列 Java、VB.NET、Python 三种范例与一份语言无关的得分点清单；**题型与得分点只按语言无关的清单定**，范例只看 Python 版。
- 题目常给源文件（`sources/pastpapers/9618_<季><yy>_sf_<卷号>/`：数据 `.txt` + 证据文档模板），一道大题连问：声明 → 读文件进数组 / 记录 → 写算法（查找、排序、递归、ADT、OOP、哈希、二叉树、链表）→ 主程序调用 → 测试截图。
- “Test your program … take a screenshot”类小问（约 131 行）的得分是**输出内容**。

## 输入

- `corpus/rows/p4/*.jsonl`（`ms_text`、`er`）；`rows.py drills / render`；`pipeline/extract/source_files_p4.json`（源文件清单）。
- 原件（只读）：`/Users/zhangheqing/Desktop/alevel cs/sources/`——P4 QP / MS / ER、sf 目录、2027–29 考纲（第 19–20 节及 P4 说明）、伪代码指南、ECR P4、Specimen P4（`sources/official/specimen/9618_y21_sp_*_4*`）。
- 已完成的设计：P2、P3 的 taxonomy 与指南（P4 与 P3 的 CT/FP、P2 的 DT 有大量同名算法，`not` 字段写清边界）；`papers/p2/skill_tags.json`（唯一词表，D8）；阶梯 `ladder/design.md` §6–§7（L09–L12 是 P4 的 Python 基础）。
- `schemas/taxonomy.schema.json`、`schemas/skill_tags.schema.json`、`schemas/row.schema.json`、`docs/DECISIONS.md`（D2、D8、D10、D24、D25、D31、D34、D37）。

## 设计要求

1. **章节与题型**：按 P4 实际考的程序任务分章（建议参考：文件与数组 / 记录处理、查找排序、递归、ADT 的数组实现、OOP、二叉树 / 链表 / 哈希、异常处理、测试与证据）；章节码不得与 P1–P3 冲突；大致 30–60 型。每型 `code`（`P4-<章>-<两位>`）、`name_zh`、`name_en`、`summary`、`cues`、`not`、`syllabus`。
2. **技能标签**：建 `papers/p4/skill_tags.json`（`extends` `papers/p2/skill_tags.json`），只收 P4 才需要的新标签（如 Python 类与构造器、私有属性、getter / setter、继承与 `super()`、异常处理 try/except、读文件到记录列表、截图输出类得分点等——以 MS 实际得分点为准）。P2 已有的不重复。
3. **得分点拆分**：定下哪些题型总是拆、哪些不拆（如纯截图题按输出内容成条），写进指南 §8；MS 给三语言范例时只从语言无关清单切 `text`。
4. **P4 练习衔接说明** `papers/p4/practice-notes.md`：为 T35 提出 P4 练习文件夹的约定草案——怎样用 sf 源文件、Python-only、证据文档的截图要求怎样换成可自动测的输出、哪些题型适合自动测、哪些只能人工核对；与 `schemas/exercise-format.md`、D10 / D24 / D31 的关系。**只写提议**，总控定稿。
5. **试标**：3 份不同考季、不同 variant 的 P4 卷（不用 s26，D1）全部小问标主 / 副题型，所有要拆的小问亲手拆 `markpoints` 并打技能标签。

## 产出

`papers/p4/taxonomy.json`（`component: 4`）、`papers/p4/skill_tags.json`、`papers/p4/tagging-guide.md`、`papers/p4/pilot_tags.csv`、`papers/p4/pilot_markpoints.jsonl`、`papers/p4/practice-notes.md`、`tasks/progress/T33.md`。md 里引用真题写纯文本行 id，不用 ⟦⟧ 与「」。

## 允许写的路径

上一节所列文件。

## 完成标准

- `make check`、`make check-scope TASK=T33` 全绿（taxonomy、skill_tags 过 schema；pilot_markpoints 的 skills 都在 P4 词表（含 extends）里，`text` 是 MS 子串）。
- 试标 3 卷每行有主题型，低信心 < 10%。
- PR 描述：章节与题型列表、新技能标签及理由、拆分规则要点、试标统计、practice-notes 要点、「需要总控决定」。

## 工作方式

从最新 `origin/main` 开分支 `task/T33-p4-taxonomy`；交付：rebase → `make check` → `make check-scope TASK=T33` → push → `gh pr create --base main --title "T33: P4 taxonomy, skill tags, tagging guide and pilot"`。不要合并。
