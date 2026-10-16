# T22 · P1 题型卡 + 核心概念表（设计工位，云端 Opus 5.5 · effort high）

> **云端会话**：只能使用仓库里的内容。`sources/`（原卷 PDF、考纲、教材、考官报告）不在仓库里，**看不到也不要去找**。题干、MS 原文、页码都在 `corpus/rows/p1/*.jsonl` 里；需要看图才能讲清的题，在卡里写「讲解时请对照原卷 QP p.N」，由学习会话在本地渲染原页。

## 目标

写出学生学 P1 用的手册内容：每个题型一张题型卡（照物理第二版的成熟结构），每章一份核心概念表（英文 MS 句 / 中文定义 / 直观理解三层）。构建器（`make build`）会把它们与统计合成 `output/p1/` 的手册。这是学生每天读的东西，**讲解质量第一**。

## 前提

- T24 已合并：`corpus/rows/p1/` 每行有 `types`（主题型 + 副题型）。`corpus/tag_report_p1.md` 里有 `low` 清单与分歧清单。
- 题型体系：`papers/p1/taxonomy.json`（v1.1，9 章 88 题型）、`papers/p1/tagging-guide.md`。

## 输入

- `schemas/card-format.md`（**严格遵守**：章文件结构、题型卡标题格式、auto 块、`⟦行 id⟧` 与 `「MS 原文」⟦行 id⟧` 引用语法）。
- `corpus/rows/p1/*.jsonl`（题干 `stem`/`stem_ctx`、`ms_text`、`types`、`qp_page`、`ms_page`、`has_figure`）。按题型取行：`python3 skill/cie-9618-cs-tutor/scripts/rows.py drills <题型码> --all`（云端无 PDF 时 `render` 不可用，其余子命令可用）。
- 教学协议：`skill/cie-9618-cs-tutor/SKILL.md` 与 `references/theory.md`、`references/few-shots.md`（讲解语气与三层定义的要求）。
- 物理版题型卡的写法示例见 `docs/` 不提供——按 `schemas/card-format.md` §2 的模板写：考法、识别信号、解题思路、得分表述、易错与失分、代表题精讲、下一道变式。
- `docs/DECISIONS.md`：**D1**（代表题与变式避开 `9618_s26_*`）、D14（副题型）、D15（LG 章）。

## 每张题型卡

1. `### P1-XX-NN　<中文名>　{#P1-XX-NN}`，下面放 `<!-- auto:stats P1-XX-NN -->`。
2. **考法**：这个题型怎么问、常见几种变化（从该型全部行归纳）。
3. **识别信号**：题干里能认出它的词句（英文原词）。
4. **解题思路**：编号步骤，能照着做。
5. **得分表述**：3–6 条，**每条都是 `「MS 原文片段」⟦行 id⟧`**——片段必须逐字取自该行 `ms_text`（`make check` 会逐字核对）。挑最常出现、最能拿分的说法。
6. **易错与失分**：从 MS 的「Do not accept / not … / must」类说明与常见混淆归纳；P1 的 ER 不在仓库，不要编造考官报告内容。
7. **代表题精讲**：`#### 代表题精讲　⟦行 id⟧`——选 2022–25 里分值较完整、最典型的一题；讲清在考什么 → 完整作答 → 与 MS 得分点逐条对齐 → 英文作答句。
8. **下一道变式**：`**下一道变式**　⟦行 id⟧`——同型、换了一个特征的另一题（不同卷），给学生自己做。
9. `<!-- auto:drills P1-XX-NN -->`。

章首写「核心思想」（这一章在讲什么、题型之间的关系）和 `<!-- auto:type-tree -->`；章末写「本章易混辨析」表。

## 核心概念表 `papers/p1/core/<章>.md`

每章的术语：`术语 | 英文得分句（「MS 原文」⟦行 id⟧） | 中文定义 | 直观理解 | 相关题型`。英文得分句必须是 MS 原文引用；没有 MS 定义句的术语，英文列写标准定义并注明「非 MS 原句」（不加「」）。

## 其他产出

- `papers/p1/front.md`：卷首使用指南、P1 考情总览（可放 `<!-- auto:chapter-stats -->`）、通用得分规则（从 MS 的通用说明归纳）。
- `papers/p1/back.md`：跨章入口、解释题得分链（Explain/Describe 类的套路）。
- `papers/p1/adjudication.csv`（`id,primary,cross,reason`）：T24 报告里的 `low` 行与分歧行，你的裁决结果。**不要直接改 `corpus/rows`**（归 T24），codex 会按此文件回写。

## 分批交付（每批一个 PR，便于审查与尽早开学）

1. 批 A：`front.md` + IR、CM、HW 三章（cards + core）+ `adjudication.csv`。
2. 批 B：LG、PF、SS。
3. 批 C：SP、EO、DB + `back.md`。

## 允许写的路径

`papers/p1/front.md`、`papers/p1/back.md`、`papers/p1/cards/**`、`papers/p1/core/**`、`papers/p1/adjudication.csv`、`tasks/progress/T22.md`。

## 完成标准（每批）

- `make check` 全绿（所有 `⟦⟧` 行存在、所有「」引文逐字命中 MS、卡片标题题型码合法）；`make check-scope TASK=T22` 全绿。
- `make build` 能生成 `output/p1/P1题型手册.md` 与 `.html`，本批每个题型都有卡。
- PR 描述：本批题型数、代表题清单、你裁决的行数、讲解中需要学习会话对照原页的题。
