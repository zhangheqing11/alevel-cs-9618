# T20 · P1 题型体系（设计工位，Opus）

## 目标

为 P1 Theory Fundamentals 设计**题型体系**：把 979 个最细小问（`corpus/rows/p1/`）归纳成稳定的题型树，作为之后全量打标签（T24，codex）和题型卡写作（T22）的基础。对照物理版：85 个题型覆盖 1250 个小问，每个题型有清晰的识别信号和易混边界。体系好不好，决定了手册能不能教、codex 能不能标准。

## 输入

- `corpus/rows/p1/*.jsonl`（979 行；`extension: true` 为 2021 扩展；`has_figure` 的行需看原页）。读取可用 `skill/cie-9618-cs-tutor/scripts/rows.py`（`get`、`find --grep`、`render`）。
- 考纲 `sources/official/9618_syllabus_2027-2029.pdf` 第 1–8 节；Learner Guide、Scheme of Work（`sources/official/support/`）；教材 `sources/textbooks/Langfield_Duddell_Coursebook_2e_2019.pdf`。
- 考官报告 `sources/pastpapers/9618_<季><yy>_er.pdf` 的 Paper 1 段（理解题目在考什么、常见失分）。
- 物理版的题型树作风格参考：`/Users/zhangheqing/Desktop/a2 physics/output/physics/p4-v2/P4学习与题型全册_第二版.md`（看「题型树」「识别信号」「易混辨析」怎么写）。
- `schemas/taxonomy.schema.json`、`schemas/card-format.md`、`docs/DECISIONS.md`。

## 设计要求

1. **章节**：按考纲 1–8 节建 8 章，章节码建议 `IR`（信息表示）、`CM`（通信）、`HW`（硬件）、`PF`（处理器基础）、`SS`（系统软件）、`SP`（安全、隐私与数据完整性）、`EO`（伦理与所有权）、`DB`（数据库）。可调整，说明理由。
2. **题型粒度**：一个题型 = 一种「识别信号 + 解题/作答套路 + 得分句模式」稳定的考法。大致 60–90 个；核验语料（2022–26s，不含 `equivalent_of` 重复行）里出现少于 2 次的考法并入相近题型，除非它代表考纲里一个独立知识点。
3. **每个题型**写全 `taxonomy.json` 字段：`code`、`chapter`、`name_zh`、`name_en`、`summary`（一行，打标签指南）、`cues`（题干信号词/句式，2–6 条）、`not`（易混题型码 + 区别一句）、`syllabus`（考纲节号）。
4. **题型顺序**：章内按「先概念后计算、先基础后综合」排，这就是学生的学习顺序。
5. **跨章**：一个小问可以有一个主题型和若干跨章题型；在指南里说明什么时候加跨章标签。

## 产出

- `papers/p1/taxonomy.json`（schema 合法）。
- `papers/p1/tagging-guide.md`：给 codex 的打标签说明——每个题型 2–3 个典型行 id 作样例（**写成纯文本行 id，不要用 ⟦⟧**，以免卡片校验误报）、边界判例、跨章规则、何时标 `tag_confidence: low`。
- `papers/p1/pilot_tags.csv`（`id,primary,cross,confidence,note`）：你亲手标注的**试标样本**——选 3 份不同考季的卷全部小问（不要用 s26，D1），验证体系可用；试标中发现的问题回改 taxonomy。
- 进度写 `tasks/progress/T20.md`。

## 允许写的路径

`papers/p1/taxonomy.json`、`papers/p1/tagging-guide.md`、`papers/p1/pilot_tags.csv`、`tasks/progress/T20.md`。

## 完成标准

- `make check`、`make check-scope TASK=T20` 全绿。
- 试标的 3 份卷每个小问都能找到主题型，低信心比例 < 10%。
- PR 描述：章节与题型数、每章题型列表（码 + 名称）、试标统计、你拿不准而需要总控决定的划分。

## 之后

T20 合并后：codex（T24）按 `tagging-guide.md` 给全部 979 行打标签；你（或另一个设计工位）接着写 T22 题型卡与核心概念表。
