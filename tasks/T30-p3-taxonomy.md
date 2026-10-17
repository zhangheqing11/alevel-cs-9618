# T30 · P3 题型体系 + 打标签指南 + 试标（设计工位，Opus 5.5 · effort high）

## 目标

为 P3 Advanced Theory 设计**题型体系**：把 858 个最细小问（`corpus/rows/p3/`，32 卷，T12 #22 已合并）归纳成稳定的题型树，作为之后全量打标签（T31，codex 或 Sonnet）和题型卡写作（T32）的基础。做法与 P1 的 T20、P2 的 T21 相同；P1 的成品（`papers/p1/taxonomy.json` 88 型、`tagging-guide.md`）与 P2 的成品（`papers/p2/taxonomy.json` 46 型、`tagging-guide.md` 含得分点拆分规则）是直接范本。

P3 的特点：理论卷，但**写代码的小问很多**（命令词 Write 185 次，最多）——递归、ADT 与查找排序算法、OOP 类与方法、Prolog 子句、BNF / 语法图、异常处理、文件随机存取；另有大量看图题（`has_figure` 426 行：浮点格子、逻辑电路与 K 图、状态图、RPN 栈、图与 A* / Dijkstra）。

## 输入

- `corpus/rows/p3/*.jsonl`（858 行；`extension: true` 为 2021 扩展；`equivalent_of` 为重复题；核验语料去重后约 637 行）。读取用 `skill/cie-9618-cs-tutor/scripts/rows.py`（`get`、`find --grep`、`render`）。
- 考纲 `sources/official/9618_syllabus_2027-2029.pdf` 第 13–20 节（A Level 部分）；考纲更新说明 `9618_syllabus_update_2027-2029.pdf`（**2027 起删改的知识点要在题型里注明**，删掉的不再设题型或标为不再考）；Learner Guide、Scheme of Work（`sources/official/support/`）；教材 `sources/textbooks/Langfield_Duddell_Coursebook_2e_2019.pdf`。
- 伪代码指南 `sources/official/9618_pseudocode_guide_2027-2029.pdf`（P3 的 OOP、递归、文件随机存取写法以它为准）。
- 考官报告 `sources/pastpapers/9618_<季><yy>_er.pdf` 的 Paper 3 段（理解题目在考什么、常见失分）。
- 原卷：`sources/pastpapers/9618_<季><yy>_<qp|ms>_3<n>.pdf`（只读）。
- `schemas/taxonomy.schema.json`、`schemas/card-format.md`、`docs/DECISIONS.md`（D1、D2、D8、D26、D29）。

## 设计要求

1. **章节**：按考纲 13–20 节建 8 章。章节码建议：`DR`（13 数据表示：用户定义类型、文件组织与存取、浮点数）、`CI`（14 通信与互联网技术：协议、电路 / 分组交换）、`HV`（15 硬件与虚拟机：RISC / CISC、流水线、并行、虚拟机、布尔代数、K 图、触发器）、`SY`（16 系统软件：OS 目的、翻译软件、BNF / 语法图、RPN）、`SC`（17 安全：加密、协议、数字签名与证书）、`AI`（18 人工智能：图、A* / Dijkstra、机器学习）、`CT`（19 计算思维与问题求解：算法、ADT、递归、Big O）、`FP`（20 进一步编程：范式、OOP、Prolog、文件处理与异常）。可调整，写明理由；码不得与 P1/P2 的章节码冲突。
2. **题型粒度**：一个题型 = 一种「识别信号 + 作答套路 + 得分句模式」稳定的考法；大致 50–80 个。核验语料（2022–26s，去掉 `equivalent_of` 重复行）里出现少于 2 次的考法并入相近题型，除非它代表考纲里一个独立知识点。
3. **每个题型**写全 `taxonomy.json` 字段：`code`（`P3-<章>-<两位>`）、`chapter`、`name_zh`、`name_en`、`summary`、`cues`（2–6 条题干原词）、`not`（易混题型码 + 一句区别，含与 P1 / P2 / P4 的边界，如 P3 的 OOP 伪代码 vs P4 的 OOP 编程、P3 的 ADT 算法 vs P2-DT-16）、`syllabus`。
4. **题型顺序**：章内「先概念后计算 / 写代码、先基础后综合」，即学生学习顺序。
5. **主题型 + 副题型**规则（参照 P1 / P2 指南 §4）。
6. **写代码类题型的得分点拆分**（参照 `papers/p2/tagging-guide.md` §8）：定下哪些 P3 题型「总是拆 / 作答是代码时拆」，拆分与打技能标签的规则。**技能标签用唯一词表 `papers/p2/skill_tags.json`（D8）**；确实缺的标签写成提议放进 PR「需要总控决定」（名称、group、name_zh、desc、example_ms），不要直接改词表。
7. **考纲变化**：对照 2027–29 考纲与更新说明，标出语料里已不在新考纲内的考法（在 `summary` 或指南里注明，题型仍可保留供参考但要说清）。

## 产出

- `papers/p3/taxonomy.json`（schema 合法，`component: 3`）。
- `papers/p3/tagging-guide.md`：给打标签工位的说明——每个题型 2–3 个典型行 id（**纯文本行 id，不要用 ⟦⟧**）、边界判例（按频率排）、跨章规则、低信心规则、得分点拆分规则与判例、特殊行（看图、重复、OCR 疑点）。
- `papers/p3/pilot_tags.csv`（`id,primary,cross,confidence,note`）：亲手试标 **3 份不同考季的卷全部小问**（不用 s26，D1；三卷覆盖 variant 1/2/3 至少各一），试标发现的问题回改 taxonomy。
- `papers/p3/pilot_markpoints.jsonl`：试标卷里要拆的写代码小问，按指南拆得分点并打技能标签（格式照 `papers/p2/pilot_markpoints.jsonl`）。
- 进度写 `tasks/progress/T30.md`。

## 允许写的路径

`papers/p3/taxonomy.json`、`papers/p3/tagging-guide.md`、`papers/p3/pilot_tags.csv`、`papers/p3/pilot_markpoints.jsonl`、`tasks/progress/T30.md`。

## 完成标准

- `make check`、`make check-scope TASK=T30` 全绿。
- 试标的 3 份卷每个小问都有主题型，低信心比例 < 10%。
- PR 描述：章节与题型数、每章题型列表（码 + 名称）、试标统计、得分点拆分范围、考纲变化处理、新技能标签提议、你拿不准而需要总控决定的划分。

## 之后

T30 合并后：T31 按 `tagging-guide.md` 给 858 行全量打标签并拆得分点（盲标后与本试标对比一致率）；T32 写 P3 题型卡与核心概念表（同 P1 的 T22）。
