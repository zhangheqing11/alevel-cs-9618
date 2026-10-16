# T21 · P2 题型体系 + 得分点技能标签（设计工位，Opus）

## 目标

为 P2 Fundamental Problem-solving and Programming Skills 设计**题型体系**与**得分点技能标签词表**，并定义「≥4 分写代码小问」的 MS 得分点拆分规则。之后 codex 全量打标签与拆得分点（T24 的 P2 部分），你或另一设计工位写 P2 题型卡（T23）。P2 是伪代码笔试，题型要按「要你写/读/改的是什么程序结构 + 怎么得分」来划分，而不是按情境。

## 输入

- `corpus/rows/p2/*.jsonl`（721 行，33 份卷；`extension: true` 为 2021；`has_figure` 多，代码与表格需看原页：`skill/cie-9618-cs-tutor/scripts/rows.py render <行 id> [--ms]`）。
- 考纲第 9–12 节、伪代码指南 2027–29、P2 插页 `sources/pastpapers/9618_w25_in_21.pdf`（主 checkout 绝对路径 `/Users/zhangheqing/Desktop/alevel cs/sources/…`，只读）；考官报告 P2 段；ECR P2 2021/2024；Scheme of Work。
- **已合并的 P1 范例**：`papers/p1/taxonomy.json`、`papers/p1/tagging-guide.md`、`papers/p1/pilot_tags.csv`——照它的结构与写法做（字段、cues/not、边界判例、试标）。
- Python 阶梯：`ladder/design.md` §6（阶梯与 P2/P4 题型衔接）、**§7.8 技能标签表（D8：以它为种子合并成唯一词表）**。
- `schemas/taxonomy.schema.json`、`schemas/skill_tags.schema.json`、`schemas/row.schema.json`（`markpoints`、`ms_max`）、`docs/DECISIONS.md`（D2 伪代码判分口径、D8、D14）。

## 设计要求

1. **章节**：按考纲 9–12 节，建议 `AD`（算法设计与问题解决）、`DT`（数据类型与结构）、`PG`（编程）、`SD`（软件开发）。写代码的大题若跨章，按「主要考的编程结构」归章并在指南里写清规则。
2. **题型粒度**：P1 是 88 个题型配 979 行；P2 721 行，但大题分值高，题型数大致 40–70 个。一个题型 = 稳定的「识别信号 + 作答套路 + MS 得分点模式」，例如「按描述写字符串处理函数」「读文本文件逐行处理」「完成追踪表」「找出并改正代码错误」「画/读结构图」「写测试数据并说明类型」等。
3. **技能标签词表 `papers/p2/skill_tags.json`**：以 `ladder/design.md` §7.8 的全部标签为种子，补齐 P2 MS 得分点里常见的技能（如 `procedure-header`、`declare-locals`、`loop-to-eof`、`file-close`、`return-value`、`mid-substring`、`concatenate`、`byref-param`…）。每个标签：`tag`、`group`、`name_zh`、`desc`，尽量配 `example_ms`（写「MS 原文 + 行 id」纯文本）。目标 40–80 个，同义标签合并。
4. **得分点拆分规则**（写进 tagging-guide）：哪些行要拆（`component=2`、`marks ≥ 4`、要求写伪代码/程序的小问）；怎样从 MS 切出一条条 `markpoints`（`n`、逐字 `text`、`marks`、`skills`）；`Max n` 写进 `ms_max`；MS 给多种范答时怎么处理。
5. **试标**：选 3 份不同考季的 P2 卷（不用 s26，D1），全部小问标主/副题型；其中所有需拆分的编程小问，亲手拆出 markpoints 并打技能标签。

## 产出

- `papers/p2/taxonomy.json`、`papers/p2/skill_tags.json`、`papers/p2/tagging-guide.md`（含得分点拆分规则与判例）、`papers/p2/pilot_tags.csv`、`papers/p2/pilot_markpoints.jsonl`（每行 `{"id", "ms_max", "markpoints": [...]}`）。
- md 里引用真题一律写纯文本行 id，不用 ⟦⟧。

## 允许写的路径

`papers/p2/taxonomy.json`、`papers/p2/skill_tags.json`、`papers/p2/tagging-guide.md`、`papers/p2/pilot_tags.csv`、`papers/p2/pilot_markpoints.jsonl`、`tasks/progress/T21.md`。

## 完成标准

- `make check`、`make check-scope TASK=T21` 全绿（taxonomy、skill_tags 都过 schema）。
- 试标 3 份卷每行有主题型，低信心 < 10%；pilot_markpoints 的每个 `skills` 都在词表里，每条 `text` 是 MS 原文子串。
- PR 描述：章节与题型列表、词表规模与分组、拆分规则要点、试标统计、需要总控决定的事项（特别是：阶梯 §7.8 标签有没有改名/合并，阶梯练习的 `meta.skills` 需不需要跟着改）。
