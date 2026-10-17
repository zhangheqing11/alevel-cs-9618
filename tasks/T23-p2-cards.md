# T23 · P2 题型卡 + 伪代码 ↔ Python 对照（设计工位，云端 Opus 5.5 · effort high）

> **云端会话**：只能使用仓库内容，`sources/` 不可见。题干、MS 原文、`markpoints`（得分点 + 技能标签）都在 `corpus/rows/p2/*.jsonl`。需要看代码排版或图才能讲清的题，在卡里写「讲解时请对照原卷 QP p.N」。抽取文本里的私用区字符按 D26 理解（如 U+F0AC 是 `←`）；引文照抄原文，校验器会归一。

## 目标

写出学生学 P2 用的手册：46 个题型各一张题型卡（结构同 P1，见已合并的 `papers/p1/cards/*.md`），每章一份「伪代码 ↔ Python 对照与模板」（`papers/p2/core/<章>.md`）。P2 是伪代码笔试，卡片的核心是**能照着写出拿满分的伪代码**。

## 输入

- `papers/p2/taxonomy.json`（4 章 46 题型）、`papers/p2/tagging-guide.md`、`papers/p2/skill_tags.json`（76 个技能标签）、`corpus/tag_report_p2.md`（统计、技能频次、低信心）。
- `corpus/rows/p2/*.jsonl`：`types`、`markpoints`（每条 `text` 是 MS 原文、`skills` 是技能标签）。按题型取行：`python3 skill/cie-9618-cs-tutor/scripts/rows.py drills <题型码> --all`。
- 范本：`papers/p1/cards/*.md`、`papers/p1/core/*.md`、`papers/p1/front.md`、`papers/p1/back.md`；`schemas/card-format.md`。
- 阶梯：`ladder/design.md` §5（伪代码 ↔ Python 速查）、§6（阶梯级与 P2 题型的衔接）、各级 `card.md`——题型卡要指明「先过哪一级阶梯」。
- 教学协议：`skill/cie-9618-cs-tutor/SKILL.md`、`references/programming.md`（**§6 P2 伪代码批改规则**）。
- `docs/DECISIONS.md`：**D1**（代表题与变式避开 s26）、**D2**（混入 Python 语法不给分；非指南写法仅在该题 MS 接受时给分）、D24（数组用带界全局声明）、D25（不依赖 AND 短路）、D26、**D27**（见下）。

## 每张题型卡（在 P1 的 9 个部分基础上，写代码类题型加三项）

1. 标题 + `<!-- auto:stats -->`；考法；识别信号；解题思路；得分表述（逐字 MS 引文 `「…」⟦行 id⟧`）；易错与失分；代表题精讲；下一道变式；`<!-- auto:drills -->`。
2. **写代码类题型**（tagging-guide §8 中「总是拆 / 作答是代码时拆」的题型）另加：
   - **伪代码模板**：这类题的标准骨架（模块头、局部声明、主循环、返回），严格按 2027–29 指南写法；
   - **得分点地图**：把该型 MS 常见得分点按出现频次列出，配对应的技能标签（来自 `markpoints`，可用脚本统计），告诉学生「这几分几乎每次都有」；
   - **同题 Python 版要点**：代表题的 Python 写法与伪代码的不对应之处（1 起下标、`MID` ↔ 切片、`REPEAT` 等），并指向对应阶梯级。
3. 代表题精讲里，伪代码完整作答要能直接拿满分，并逐条对齐 `markpoints`。

## 核心对照 `papers/p2/core/<章>.md`

替代 P1 的概念表：本章涉及的伪代码结构 ↔ Python 写法 ↔ 常见失分，术语类（如 abstraction、decomposition、各种测试方法）仍用三层定义（英文 MS 句 / 中文 / 直观）。

## D27 · 新技能标签

T28 报告缺「普通变量赋值」「滚动缓存/数组移位」两类技能。你来定新标签（名称、组、`name_zh`、`desc`），写进 PR 描述的「需要总控决定」——**不要直接改 `skill_tags.json` 与 rows**（归 T21/T28），总控合并后安排回填。

## 分批

1. 批 A：`papers/p2/front.md` + AD、DT 两章（cards + core）。
2. 批 B：PG、SD 两章 + `papers/p2/back.md`（跨章入口；写代码大题的通用得分链：模块头 → 声明 → 循环 → 处理 → 输出/返回）。

## 允许写的路径

`papers/p2/front.md`、`papers/p2/back.md`、`papers/p2/cards/**`、`papers/p2/core/**`、`papers/p2/adjudication.csv`、`tasks/progress/T23.md`。

## 完成标准（每批）

- `make check`（或 `python3 tools/check.py`）全绿；`make check-scope TASK=T23` 全绿；`build/build.py p2` 能生成本批的卡。
- 伪代码全部符合指南（关键字大写、`←`、`DECLARE`、`ENDIF`/`ENDWHILE`/`NEXT x`、文件操作语法）；codex 会逐条审计。
- PR 为普通 PR（不要 draft）；描述写本批题型数、代表题清单、D27 提议、需要对照原页的题。
