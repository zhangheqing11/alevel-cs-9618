# T32 · P3 题型卡 + 核心概念表（设计工位，本地 Opus 5.5 · effort high，三批并行）

## 目标

写出学生学 P3 用的手册：79 个题型各一张题型卡、每章一份核心概念表，外加卷首与书末。P3 是 A2 理论卷，但写代码的小问很多（DR 记录 / 集合声明、CT 查找排序与 ADT、FP 类定义与文件处理），这些题型的卡要像 P2 那样带伪代码模板与得分点地图。**讲解质量第一，证据规则第一**。

## 分批（三批同时开，各写各的文件）

| 批 | 章 | 题型数 | 另写 |
|:--|:--|--:|:--|
| A（cc-H） | DR、CI、HV、BL | 31 | `papers/p3/front.md`、`papers/p3/adjudication.csv`（T31 的 `low` 行与分歧行） |
| B（cc-I） | SY、SC、AI | 25 | — |
| C（cc-J） | CT、FP | 23 | `papers/p3/back.md`（跨章入口，覆盖全部 9 章；解释题得分链；写代码题得分链） |

## 输入

- `papers/p3/taxonomy.json`（9 章 79 型，D34）、`papers/p3/tagging-guide.md`、`papers/p3/skill_tags.json`（extends P2）、`corpus/tag_report_p3.md`。
- `corpus/rows/p3/*.jsonl`：`types`、`markpoints`（59 行）、`ms_text`、`er`（考官报告摘录，D33）、`equivalent_of`（D35）。按题型取行：`python3 skill/cie-9618-cs-tutor/scripts/rows.py drills <题型码> --all`；看原页 `rows.py render <行 id> [--ms]`。
- 原件（本机可读，只读）：`/Users/zhangheqing/Desktop/alevel cs/sources/`——QP / MS / ER、2027–29 考纲（第 13–20 节）、伪代码指南 2027–29、教材 Langfield & Duddell。
- **范本**：P1 手册（`papers/p1/front.md`、`cards/*.md`、`core/*.md`、`back.md`，T22 + T26c 修正后）用于理论题型；P2 手册（`papers/p2/cards/*.md`、`core/*.md`，T23 + T26d 修正后）用于写代码题型（伪代码模板、得分点地图、MP 对齐表、同题 Python 版要点）。`schemas/card-format.md` 严格遵守。
- `docs/DECISIONS.md`：D1、D2、D25、D26、D29、D33–D35、D37、D39、**D40**；教学协议 `skill/cie-9618-cs-tutor/SKILL.md`、`references/theory.md`。

## 每张题型卡

结构同 P1：标题 `### P3-XX-NN　中文名　{#P3-XX-NN}` + `<!-- auto:stats P3-XX-NN -->`、考法、识别信号、解题思路、得分表述（3–6 条 `「MS 原文」⟦行 id⟧`）、易错与失分、代表题精讲（在考什么 → 完整作答 → 与 MS 逐点对齐 → 英文作答句 / 规范代码 → 直观）、下一道变式、`<!-- auto:drills P3-XX-NN -->`。章首核心思想 + `<!-- auto:type-tree -->`，章末本章易混辨析。

**写代码 / 类图题型**（指南 §8 的拆分题型：DR-03、DR-05、CT-02、CT-03、CT-06、CT-07、FP-06、FP-10，以及作答为代码时的 CT-08、CT-09、FP-05）另加：伪代码模板（2027–29 指南写法）、得分点地图（按 `markpoints[].skills` 统计，口径同 P2：核验语料、主题型行、同题同标签计一次、去掉 `equivalent_of`）、与 P4 / 阶梯的衔接（指向具体 `Lxx Eyy`，确认存在）。汇编（FP-02/03）、Prolog（FP-07～09）、BNF / 语法图、逻辑电路与卡诺图按理论卡写，但要给“逐步作答模板”。

**易错与失分**可以引用考官报告：用行的 `er` 字段（写成“考官报告指出 …（行 id）”，不用「」），**不得作为给分依据**。

## T26 审计教训（P1 / P2 手册被另一模型挑出的 26 条，务必避开）

1. 不要把 MS 里“no X / not X”的句子当成 X 的定义放进概念表或得分表述（D40②）。
2. 不要把单题的结论推广成无条件规则（外键一端必为多端、指针相等必为一项、“任意字符就只能长度前缀”、“值不变就不写”）；规则要写清适用条件，有反例时点明。
3. “完整作答”要按该题 MS 数**独立得分点**：`//` 分隔的是同一点的替代说法，不能累计；`Max n` 要写清。
4. “讲解时请对照原卷 QP p.N”的页码要逐个核对（图在哪一页、作答区在哪一页）。
5. 跟踪表、填表题按该题 MS 自己的格式与约定写；教学表比 MS 多列的行要注明。
6. 手写的统计数字（“一半”“考了 n 次”）要么由脚本算出并写明口径，要么不写。
7. 图（网络拓扑、电路、状态图）改用文字 + 简图时，连线关系必须与 MS 得分点一致。
8. 概念与考纲 / 真题的分类不冲突（例：ACC 是 special purpose register）。

## 允许写的路径

- A：`papers/p3/front.md`、`papers/p3/adjudication.csv`、`papers/p3/cards/{DR,CI,HV,BL}.md`、`papers/p3/core/{DR,CI,HV,BL}.md`、`tasks/progress/T32A.md`
- B：`papers/p3/cards/{SY,SC,AI}.md`、`papers/p3/core/{SY,SC,AI}.md`、`tasks/progress/T32B.md`
- C：`papers/p3/back.md`、`papers/p3/cards/{CT,FP}.md`、`papers/p3/core/{CT,FP}.md`、`tasks/progress/T32C.md`
- 不要改 `corpus/`、`taxonomy.json`、`tagging-guide.md`（发现标签错写进 A 的 `adjudication.csv` 或 PR「需要总控决定」）。

## 完成标准（每批）

- `make check` 全绿；`make check-scope TASK=T32A|T32B|T32C` 全绿；`python3 build/build.py p3` 能生成（B、C 单独开分支时 front.md 可能还没有：构建器要求 front/cards/back 至少其一存在即可，本批的卡都要出现在 `output/p3/`）。
- 每张卡的代表题都对照过 QP 与 MS 原页（PR 里列页码）；代表题与变式 2022–25、主题型行、不同卷、非 s26、非 `equivalent_of`。
- 伪代码块结构配对、无 D2 禁用写法、不依赖 AND 短路。
- PR 描述：本批题型数、代表题与变式清单、核对的原页、需要学习时对照原页的题、自查 T26 八条教训的结果、「需要总控决定」。

## 工作方式

从最新 `origin/main` 开分支 `task/T32A-p3-cards`（或 B / C）；交付：rebase → `make check` → `python3 build/build.py p3` → `make check-scope TASK=T32A|B|C` → push → `gh pr create --base main --title "T32 batch A: P3 front + DR/CI/HV/BL cards"`（B：`SY/SC/AI cards`；C：`CT/FP cards + back`）。不要合并。
