# P2 全量标注与得分点拆分报告

## 覆盖、证据与可复现流程

- 全部 721 行均有主题型；核验语料 591 行、2025 分（2022–2026s，含 s26）；2021 扩展语料 130 行。
- 共 185 行拆出 1196 条候选得分点；核验语料 152 行、982 条。ms_max 用于候选总分超过小问分值，候选条数不等于可获分数。
- low 2 行，占 0.28%。
- 只读每行自己的 QP/MS；原页查看记录见 pipeline/tag/p2/review_log.json。所有独立卷起始图示页均查看，复杂跨页代码和流程图另查原页。D21 重复卷完全复制对应 _21 行。
- 721 行盲标、拆分及候选排除清单先完成，冻结于提交 5a95bb0；blind/ 保存原始快照与 SHA256 manifest。随后才首次读取两个 pilot 文件，未为提高一致率调整主题型或切分。
- 真源：pipeline/tag/p2/p2_tags.jsonl、p2_markpoints.jsonl。check_p2.py 检查覆盖、词表、原文子串、分值和 D21；apply_p2.py 只写五个授权字段；report_p2.py 重建本报告。

## 与试标的盲标比较

- 主题型：66/66 = 100.00%（要求 ≥90%）。
- 得分点切分：18/18 = 100.00%（要求 ≥80%）。逐行比较有序的压缩空白 text、marks 及 ms_max；18 行全部一致，110 条得分点，无切分分歧。技能集合独立比较，不混入切分一致率。
- 最终主题型与切分和盲标快照相同；以下列出所有副题型、技能集合差异。

### 副题型分歧与复核

| 行 | pilot | 本次 | 复核结论 |
|:--|:--|:--|:--|
| 9618_s24_22:3(a)(ii) | 无 | P2-DT-02 | 保留 DT-02：分别复核该题 MS p7，数组边界声明与 OF 记录类型是两个独立下划线计分片段；按 §4 §3 不适用的单条声明按“其他行”的副题型阈值，记录类型另占一分。 |
| 9618_w25_21:3(a)(ii) | 无 | P2-DT-02 | 保留 DT-02：分别复核该题 MS p9，数组边界声明与 OF 记录类型是两个独立下划线计分片段；按 §4 §3 不适用的单条声明按“其他行”的副题型阈值，记录类型另占一分。 |

### 技能集合差异

以下逐条按 §8.3 与该题 MS 文字复核。表中保留盲标差异，并列出最终技能；七处据原文补准，其他保留较具体或包含独立操作的 1–3 个标签。只比较集合，不把顺序差异当分歧。

| 行 / 点 | MS 原文 | pilot 技能 | 盲标技能 | 最终技能与复核 |
|:--|:--|:--|:--|:--|
| 9618_w22_23:3 / 3 | If number greater than zero add to positive sum and If number less than zero add to negative sum | nested-if, accumulator | relational-ops, accumulator | relational-ops, accumulator；保留盲标：对应本点原文操作。 |
| 9618_w22_23:5(a)(i) / 3 | Extract and assign SID | string-functions, field-extract | field-extract | field-extract；保留盲标：对应本点原文操作。 |
| 9618_w22_23:5(a)(i) / 4 | Extract and assign SDesc | string-functions, field-extract | field-extract | field-extract；保留盲标：对应本点原文操作。 |
| 9618_w22_23:5(a)(i) / 5 | Calculation of length of SCost (remainder of string) | string-index | string-functions | string-functions；保留盲标：对应本点原文操作。 |
| 9618_w22_23:5(a)(i) / 6 | Extract and assign SCost following an attempt at MP5 | string-functions, field-extract | field-extract | field-extract；保留盲标：对应本点原文操作。 |
| 9618_w22_23:7(a) / 1 | Declaration and initialisation of local integer for Count | declare-variables, initialise-variables | declare-variables, initialise-variables, data-types | declare-variables, initialise-variables, data-types；保留盲标：对应本点原文操作。 |
| 9618_w22_23:7(a) / 3 | (Conditional) loop while error number input is in range // error code 999 reached | pre-condition-loop, loop-bounds | pre-condition-loop, array-index | pre-condition-loop, loop-bounds；据原文补准：范围/条件循环、比较、转换或写入，按 §8.3。 |
| 9618_w22_23:7(a) / 6 | if so check for blank error text in a loop | nested-if, parallel-arrays | array-index, char-compare | array-index, relational-ops；据原文补准：范围/条件循环、比较、转换或写入，按 §8.3。 |
| 9618_w22_23:7(b)(i) / 1 | (Conditional) loop terminating when item added OR end of array reached | linear-search, loop-bounds | pre-condition-loop, linear-search, logic-ops | pre-condition-loop, linear-search, logic-ops；保留盲标：对应本点原文操作。 |
| 9618_w22_23:7(b)(i) / 6 | Calculation of remaining unused elements and return Integer value (for both cases) | return-value | operator-precedence, return-value | operator-precedence, return-value；保留盲标：对应本点原文操作。 |
| 9618_s24_22:2(a) / 1 | Condition for selecting one of the input numbers as largest value | flowchart-draw, max-min | relational-ops, max-min | relational-ops, max-min；保留盲标：对应本点原文操作。 |
| 9618_s24_22:2(a) / 3 | Condition for selecting largest number for all three number input and assigning to Ans | max-min, logic-ops | max-min, nested-if | max-min, nested-if；保留盲标：对应本点原文操作。 |
| 9618_s24_22:2(b) / 4 | … loop for 3 iterations | count-loop, loop-bounds | loop-bounds | loop-bounds；保留盲标：对应本点原文操作。 |
| 9618_s24_22:6(a) / 6 | Attempt to strip characters back to space | string-functions, string-index | string-functions | string-functions；保留盲标：对应本点原文操作。 |
| 9618_s24_22:6(a) / 7 | Correct removal of word/words from end of string and remove final space | string-functions, string-index | string-functions | string-functions；保留盲标：对应本点原文操作。 |
| 9618_s24_22:8(b) / 3 | Identify first non-space character in a loop | char-compare, flag-variable | char-compare, linear-search | char-compare, linear-search；保留盲标：对应本点原文操作。 |
| 9618_s24_22:8(b) / 5 | Leading spaces removed from Line / / Create new string without leading space | string-functions, string-index | string-functions | string-functions；保留盲标：对应本点原文操作。 |
| 9618_s24_22:8(c) / 6 | Check return value following both MP5 function calls is not an empty string and if so write to F2 in a loop | nested-if, file-write | file-append, relational-ops | file-write, relational-ops；据原文补准：范围/条件循环、比较、转换或写入，按 §8.3。 |
| 9618_w25_21:2 / 2 | Loop through exactly 30 elements in the array | flowchart-draw, loop-bounds | loop-bounds, array-index | loop-bounds, array-index；保留盲标：对应本点原文操作。 |
| 9618_w25_21:4(a) / 2 | Input value and assign to first element | array-index | input-prompt, array-index | input-prompt, array-index；保留盲标：对应本点原文操作。 |
| 9618_w25_21:4(a) / 4 | Completely correct conditional loop including both tests | pre-condition-loop, loop-bounds | loop-bounds, relational-ops | pre-condition-loop, loop-bounds, relational-ops；据原文补准：范围/条件循环、比较、转换或写入，按 §8.3。 |
| 9618_w25_21:4(a) / 5 | Assign input value to current element if greater than previous element and input next value in a loop | array-index, relational-ops | input-prompt, array-index | input-prompt, array-index, relational-ops；据原文补准：范围/条件循环、比较、转换或写入，按 §8.3。 |
| 9618_w25_21:6(b) / 4 | attempt to form sum of digits in a loop | accumulator | accumulator, string-functions | accumulator, string-functions；保留盲标：对应本点原文操作。 |
| 9618_w25_21:6(b) / 5 | completely correct sum of digits in a loop | accumulator, type-conversion | accumulator, string-functions | accumulator, type-conversion, string-functions；据原文补准：范围/条件循环、比较、转换或写入，按 §8.3。 |
| 9618_w25_21:8(a) / 2 | Loop through all elements in Loan array | loop-bounds | loop-bounds, array-index | loop-bounds, array-index；保留盲标：对应本点原文操作。 |
| 9618_w25_21:8(a) / 3 | ... terminating if Max reached | pre-condition-loop, logic-ops | logic-ops, relational-ops | pre-condition-loop, logic-ops, relational-ops；据原文补准：范围/条件循环、比较、转换或写入，按 §8.3。 |
| 9618_w25_21:8(a) / 4 | Test for correct StudentID field in a loop | array-of-records | array-of-records, relational-ops | array-of-records, relational-ops；保留盲标：对应本点原文操作。 |
| 9618_w25_21:8(b) / 5 | … If book not returned yet, then set OnLoan field to FALSE | array-of-records, nested-if | array-of-records | array-of-records；保留盲标：对应本点原文操作。 |

技能集合有 28 条差异。

## 核验语料题型统计

仅按主题型计数与计分，副题型不重复累计；包含 s26，排除全部 extension=true 的 2021 行。

| 题型 | 名称 | 行数 | 分值 |
|:--|:--|--:|--:|
| P2-AD-01 | 抽象：需要的信息与操作 | 15 | 30 |
| P2-AD-02 | 分解与逐步求精 | 9 | 26 |
| P2-AD-03 | 标识符命名与标识符表 | 7 | 16 |
| P2-AD-04 | 画或补全程序流程图 | 12 | 57 |
| P2-AD-05 | 流程图转伪代码 | 3 | 12 |
| P2-AD-06 | 用文字步骤描述算法 | 24 | 114 |
| P2-DT-01 | 选择数据类型 | 17 | 46 |
| P2-DT-02 | 记录类型：定义与字段访问 | 9 | 25 |
| P2-DT-03 | 数组：声明、术语与未用元素 | 19 | 31 |
| P2-DT-04 | 选择数据结构并说明好处 | 12 | 31 |
| P2-DT-05 | 一维数组处理模块 | 15 | 88 |
| P2-DT-06 | 二维数组处理模块 | 11 | 71 |
| P2-DT-07 | 记录数组处理模块 | 11 | 76 |
| P2-DT-08 | 冒泡排序 | 5 | 22 |
| P2-DT-09 | 读文本文件逐行处理 | 11 | 77 |
| P2-DT-10 | 写入或复制文本文件 | 9 | 66 |
| P2-DT-11 | 文件的用途、模式与存储格式 | 22 | 35 |
| P2-DT-12 | ADT 的概念与选择 | 10 | 21 |
| P2-DT-13 | 栈的操作与状态 | 9 | 30 |
| P2-DT-14 | 队列的操作与状态 | 6 | 16 |
| P2-DT-15 | 链表的操作与状态 | 11 | 33 |
| P2-DT-16 | 用数组实现栈、队列与链表 | 15 | 53 |
| P2-PG-01 | 识别程序结构与语句成分 | 12 | 36 |
| P2-PG-02 | 表达式求值 | 10 | 33 |
| P2-PG-03 | 写或补全单条语句与表达式 | 15 | 34 |
| P2-PG-04 | 选择结构：IF 与 CASE 的改写 | 4 | 12 |
| P2-PG-05 | 循环结构的选择与改写 | 6 | 11 |
| P2-PG-06 | 过程、函数与参数的概念 | 23 | 42 |
| P2-PG-07 | 写模块头 | 7 | 19 |
| P2-PG-08 | 良好编程实践 | 13 | 27 |
| P2-PG-09 | 输入-处理-输出算法 | 10 | 64 |
| P2-PG-10 | 数值计算与判断函数 | 13 | 79 |
| P2-PG-11 | 字符串处理模块 | 31 | 197 |
| P2-PG-12 | 日期处理 | 7 | 21 |
| P2-SD-01 | 开发生命周期的阶段与活动 | 14 | 37 |
| P2-SD-02 | 生命周期模型 | 9 | 18 |
| P2-SD-03 | 结构图 | 19 | 61 |
| P2-SD-04 | 状态转换图 | 12 | 45 |
| P2-SD-05 | 错误类型与 IDE 调试 | 15 | 32 |
| P2-SD-06 | 找出并改正伪代码错误 | 12 | 32 |
| P2-SD-07 | 追踪表（干跑） | 20 | 69 |
| P2-SD-08 | 分析给定伪代码 | 17 | 27 |
| P2-SD-09 | 测试方法与测试策略 | 19 | 51 |
| P2-SD-10 | 测试数据与有效性检查 | 17 | 48 |
| P2-SD-11 | 维护类型 | 6 | 13 |
| P2-SD-12 | 按新需求修改程序 | 18 | 41 |

## 技能频次

单位为含该技能的得分点条数；同一点同一技能只计一次。列出完整词表，0 表示本次拆分未使用；不代表整个题库不考该技能。

| 技能 | 全部语料 | 核验语料 |
|:--|--:|--:|
| trace-dry-run | 0 | 0 |
| translate-pseudocode | 0 | 0 |
| flowchart-to-pseudocode | 5 | 3 |
| flowchart-draw | 5 | 5 |
| find-fix-errors | 0 | 0 |
| boundary-values | 2 | 2 |
| data-types | 37 | 33 |
| declare-variables | 54 | 46 |
| initialise-variables | 75 | 60 |
| type-conversion | 24 | 24 |
| div-mod | 17 | 14 |
| operator-precedence | 32 | 26 |
| relational-ops | 113 | 93 |
| logic-ops | 46 | 39 |
| input-prompt | 26 | 22 |
| output-format | 99 | 85 |
| nested-if | 23 | 20 |
| case-of | 3 | 3 |
| case-range | 0 | 0 |
| count-loop | 32 | 27 |
| loop-step | 5 | 1 |
| pre-condition-loop | 34 | 23 |
| post-condition-loop | 19 | 14 |
| sentinel-loop | 12 | 12 |
| input-validation | 5 | 5 |
| nested-loops | 16 | 13 |
| loop-bounds | 113 | 84 |
| loop-choice | 2 | 0 |
| flag-variable | 30 | 16 |
| module-header | 65 | 54 |
| byval-byref | 2 | 2 |
| procedure-call | 57 | 42 |
| return-value | 54 | 41 |
| boolean-return | 30 | 25 |
| global-scope | 0 | 0 |
| accumulator | 80 | 66 |
| max-min | 13 | 9 |
| linear-search | 33 | 21 |
| bubble-sort | 27 | 9 |
| counting-array | 3 | 0 |
| random-numbers | 15 | 14 |
| binary-search | 0 | 0 |
| insertion-sort | 0 | 0 |
| recursion | 0 | 0 |
| string-functions | 79 | 70 |
| char-loop | 23 | 17 |
| string-index | 12 | 6 |
| string-concat | 40 | 37 |
| char-compare | 39 | 27 |
| char-code | 2 | 2 |
| field-extract | 27 | 27 |
| date-functions | 11 | 11 |
| declare-array | 3 | 2 |
| array-index | 82 | 62 |
| array-2d | 45 | 36 |
| array-copy | 0 | 0 |
| parallel-arrays | 2 | 2 |
| record-type | 16 | 16 |
| array-of-records | 44 | 41 |
| file-open-read | 48 | 42 |
| loop-to-eof | 24 | 21 |
| file-write | 23 | 21 |
| file-append | 11 | 7 |
| file-close | 30 | 25 |
| stack-array | 8 | 8 |
| queue-array | 5 | 5 |
| linked-list | 6 | 6 |
| binary-tree | 0 | 0 |
| class-definition | 0 | 0 |
| encapsulation | 0 | 0 |
| getter-setter | 0 | 0 |
| inheritance | 0 | 0 |
| polymorphism | 0 | 0 |
| containment | 0 | 0 |
| exception-handling | 0 | 0 |
| p4-identifiers | 0 | 0 |

## 低信心与低频题型

| 行 | 主题型 | 原因 |
|:--|:--|:--|
| 9618_s22_21:1(a) | P2-AD-06 | 无合适题型：仅识别 algorithm 术语，非要求描述步骤；最接近 AD-06，待设计工位裁决。 |
| 9618_w23_21:8(c)(i) | P2-DT-11 | 无合适题型：网络消息字段最小长度导致不能传输空行，非写代码、非文件内部格式；最近归 DT-11 文件传输格式限制，待设计工位裁决。 |

核验语料出现不足 2 次的主题型：无。

## 未拆行审计与需要总控决定

候选题型且 ≥4 分的未拆行全部逐项列在 split_exemptions.jsonl；文字解释按 §8.1 不拆，下划线、填空和按行计分按 §8.2.9 不拆。

| 行 | 未拆依据 |
|:--|:--|
| 9618_s24_21:3(b) | §8.1：作答为文字说明（实现方式、效率或需求变更），非代码/流程图。 |
| 9618_s24_21:7(b)(ii) | MS 按下划线/按行给分，未拆。 |
| 9618_s25_21:7(b)(ii) | §8.1：作答为文字说明（实现方式、效率或需求变更），非代码/流程图。 |
| 9618_s25_23:6(b) | 已看 MS 原页，各下划线片段独立计分；MS 按下划线/按行给分，未拆。 |
| 9618_s26_22:5(b)(i) | §8.1：作答为文字说明（实现方式、效率或需求变更），非代码/流程图。 |
| 9618_s26_23:5(b) | MS 按下划线/按行给分，未拆：仅给完整补空代码及 1 mark per gap，没有逐点文字清单。 |
| 9618_w21_22:2(a) | 已看 MS p4，五个无编号红框各一分；图内文字未进入 ms_text，只有 One mark for each outlined group。按 §8.2.9 同类图示/按区域给分未拆。需要总控决定：补抽本题 MS 流程图文字后拆分，或确认图示给分例外。 |
| 9618_w22_21:4(b) | §8.1：作答为文字说明（实现方式、效率或需求变更），非代码/流程图。 |
| 9618_w22_22:3(b) | §8.1：作答为文字说明（实现方式、效率或需求变更），非代码/流程图。 |
| 9618_w22_23:4(b)(ii) | §8.1：作答为文字说明（实现方式、效率或需求变更），非代码/流程图。 |
| 9618_w23_21:3(b) | DT-16 但作答是文字补空算法步骤，非代码或流程图，依 §8.1 不拆。 |
| 9618_w23_23:3(b) | 用文字补全数组队列的入队步骤，DT-16 但非代码/流程图，依 §8.1 不拆。 |
| 9618_w24_21:3(c) | §8.1：作答为文字说明（实现方式、效率或需求变更），非代码/流程图。 |
| 9618_w24_22:3(b) | MS 按下划线/按行给分，未拆：完整代码后只有 One mark per gap，没有逐点文字。 |
| 9618_w24_23:4(a) | MS 按下划线/按行给分，未拆：完整代码只有 One mark per highlighted part，没有逐点文字。 |
| 9618_w25_22:4(b) | MS 按下划线/按行给分，未拆：仅按 boldened gaps 计分，无逐点文字清单。 |
| 9618_w25_22:7(b) | MS 按下划线/按行给分，未拆。 |
| 9618_w25_23:3 | 已看 MS p7：MP1 仅描述两个 Exists 赋值，MP2–5 只指向代码加粗部分，无逐点文字；MS 按下划线/按行给分，未拆。D17 的 PopData 类型名当变量笔误原样保留，教学应使用 ThisPop。 |

- **需要总控决定：9618_w21_22:2(a)** 的五个流程图红框内文字未抽入 ms_text，现有文本只有按框计分说明。已看 QP p5、MS p4；当前按 §8.2.9 同类图示给分例外处理。请补抽图中文字后拆分，或确认按区域给分的例外。未越权改原始抽取字段。
- **需要总控决定：技能词表缺少通用变量赋值 / 滚动缓存移位技能**。s22/22:4(a) MP5/6、w21/22:6(d) MP6、w23/21:6(a) MP5 暂取 initialise-variables 最近项，note 已说明；建议设计工位增加准确标签后回填，当前不私建技能。
- w25/23:3 已按 §8.2.9 加粗代码给分例外不拆。D17 的 PopData 类型名当变量笔误原样保留；本次仅标注，不改 MS。w22/22:1(c) 的 D16 官方笔误同样保留。
- 其余范围内没有新增题型或技能。2021 重复卷和 s26 均完成标注；保留整卷标志由既有规则消费，本任务没有改动抽取字段或共享文件。
