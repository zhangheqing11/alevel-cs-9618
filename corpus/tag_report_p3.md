# P3 全量标注与得分点拆分报告

## 覆盖与证据

- 全部 858 行均有主题型；独立行 617，D35/equivalent_of 继承行 241。
- 统计口径：2022–2026s 核验语料、包含 s26、排除 extension=true 与全部继承行；共 561 行、1580 分。题型计数只按 primary，cross 不重复计分。
- 拆分 59 行、290 条；去除继承后 43 行；核验去重 40 行、192 条。ms_max 限制候选得分点总分，条数不等于可获分数。
- low 3 行（0.35%），均为一题及其重复行；核验去重语料无 low。
- 盲标快照先于任何 pilot 读取冻结并提交（f8ea20a）；blind/manifest.json 记录两个真源 SHA256、输入文件散列及源版本，report_p3.py 会拒绝被改过的快照。最终主题型、cross、切分、text、marks、ms_max 均与盲标相同，仅复核了 skills。
- 只读对应行自己的 QP/MS；独立 has_figure 行的 QP 起始页，以及全部 BL 与拆分候选的 MS 原页均已目视核对。页单见 render_manifest_*.json 与 review_log.json；9618_s21_31:8(b) 的 QP p.11 及 9618_w25_32:10 的 QP p.11 另查续页。
- 真源为 p3_tags.jsonl / p3_markpoints.jsonl；compile_tags.py 与 compile_markpoints.py 可由人工判定与原文映射重建。check_p3.py 检查覆盖、题型、词表、分值、原文子串、豁免与继承；apply_p3.py 只合并五个授权字段，audit_merge.py 对比其余字段的原始 JSON 字节。

## 与 pilot 的盲标比较

- 主题型 81/81 = 100.00%；cross 集合 81/81 = 100.00%。无主题型或副题型分歧。
- 得分点切分 7/7 = 100.00%，覆盖 31 条。比较有序的压缩空白 text、marks 与 ms_max，无切分分歧。
- 技能比较按集合进行，标签顺序差异不算分歧。下表逐条列出全部分歧、原页复核结论与最终技能。

| 行 / MP | pilot 技能 | 盲标技能 | 最终技能 | 原页复核 |
|:--|:--|:--|:--|:--|
| 9618_w22_32:4(b) / 2 | record-type, data-types | data-types | record-type, data-types | MS p.6：补 record-type：MS 明确要求两条 DECLARE 字段声明及 STRING 类型，指南 §8.3 同时覆盖声明与类型。 |
| 9618_w22_32:4(b) / 4 | user-defined-type, data-types | user-defined-type | user-defined-type, data-types | MS p.6：补 data-types：除使用枚举类型外，MS 明说 correct data type from part 4(a)。 |
| 9618_w22_32:11(b) / 4 | flag-variable, nested-if | linked-list, relational-ops | linked-list, relational-ops | MS p.16：保留 linked-list、relational-ops：Pointer/Found 存的是结点位置（整数），不是 BOOLEAN 标志；此行判断空指针/找到位置，按具体操作标注。 |
| 9618_s24_31:3(b) / 2 | record-type, data-types | data-types | record-type, data-types | MS p.6：补 record-type：每两个完整字段声明一分，同时要求声明写法和字段类型。 |
| 9618_s25_33:11 / 5 | flag-variable | flag-variable, relational-ops | flag-variable, relational-ops | MS p.14：保留 flag-variable、relational-ops：读取 Stored 标志并显式比较 FALSE，两项均直接出现在该行。 |
| 9618_s25_33:12(b) / 2 | insertion-sort, pre-condition-loop, nested-loops | pre-condition-loop, insertion-sort | insertion-sort, pre-condition-loop, nested-loops | MS p.15：补 nested-loops：MS 的 inner loop 嵌套在题给 FOR 中，同时保留 pre-condition-loop 与 insertion-sort。 |
| 9618_s25_33:12(b) / 5 | insertion-sort, array-index | insertion-sort, accumulator | insertion-sort, array-index | MS p.15：改为 insertion-sort、array-index：Position 是用于移位的插入下标，不是累计个数或总和；MS 范例 Position ← Position – 1。 |

共 7 条技能集合分歧；skill_decisions 与同构项一致性修订见 pilot_review.json。
同构修订：9618_s21_31:2(c) MP2、9618_s23_32:6(a) MP2 补 record-type；9618_s21_31:8(b) 与 9618_s26_31:10(a) 的内层循环补 nested-loops，下标更新使用 array-index，避免误当累计计数。继承行同步更新。

## 核验语料题型统计（去重）

| 题型 | 名称 | 行数 | 分值 |
|:--|:--|--:|--:|
| P3-DR-01 | 用户定义类型的概念与分类 | 16 | 38 |
| P3-DR-02 | 声明与使用枚举类型和指针类型 | 17 | 30 |
| P3-DR-03 | 声明记录类型 | 9 | 31 |
| P3-DR-04 | 记录变量的声明与字段赋值 | 12 | 22 |
| P3-DR-05 | 声明集合类型 | 2 | 8 |
| P3-DR-06 | 文件组织方式 | 9 | 16 |
| P3-DR-07 | 文件存取方式 | 10 | 25 |
| P3-DR-08 | 散列算法与冲突处理 | 7 | 18 |
| P3-DR-09 | 浮点数换算成十进制 | 8 | 23 |
| P3-DR-10 | 十进制写成规格化浮点数 | 16 | 54 |
| P3-DR-11 | 规格化与可表示的最大最小值 | 7 | 12 |
| P3-DR-12 | 精度、范围、舍入误差与上溢下溢 | 10 | 25 |
| P3-CI-01 | 协议的必要性与协议栈 | 8 | 25 |
| P3-CI-02 | TCP/IP 四层的顺序与功能 | 11 | 35 |
| P3-CI-03 | 应用层协议：HTTP、FTP、POP3、IMAP、SMTP | 9 | 30 |
| P3-CI-04 | BitTorrent 点对点文件共享 | 2 | 7 |
| P3-CI-05 | 电路交换 | 5 | 15 |
| P3-CI-06 | 分组交换与路由器 | 7 | 25 |
| P3-CI-07 | 电路交换与分组交换的比较 | 4 | 16 |
| P3-HV-01 | RISC 与 CISC 处理器 | 6 | 18 |
| P3-HV-02 | 流水线与中断处理 | 5 | 16 |
| P3-HV-03 | 四种基本计算机体系结构 | 4 | 16 |
| P3-HV-04 | 大规模并行计算机 | 2 | 6 |
| P3-HV-05 | 虚拟机 | 6 | 27 |
| P3-BL-01 | 由逻辑电路完成真值表 | 9 | 24 |
| P3-BL-02 | 半加器与全加器 | 2 | 3 |
| P3-BL-03 | 触发器（SR、JK） | 2 | 5 |
| P3-BL-04 | 由真值表或电路写积之和表达式 | 8 | 18 |
| P3-BL-05 | 填写卡诺图 | 13 | 25 |
| P3-BL-06 | 卡诺图圈组与化简积之和 | 30 | 60 |
| P3-BL-07 | 布尔代数化简与德摩根定律 | 12 | 27 |
| P3-SY-01 | 操作系统：资源利用与隐藏硬件复杂性 | 2 | 6 |
| P3-SY-02 | 进程、多任务与进程状态 | 9 | 18 |
| P3-SY-03 | 进程调度与中断处理 | 9 | 29 |
| P3-SY-04 | 虚拟内存、分页、分段与磁盘抖动 | 6 | 16 |
| P3-SY-05 | 解释器怎样执行程序 | 1 | 4 |
| P3-SY-06 | 编译的各个阶段 | 8 | 21 |
| P3-SY-07 | 按语法图或 BNF 判断字符串是否合法 | 9 | 15 |
| P3-SY-08 | 写或补全 BNF | 11 | 30 |
| P3-SY-09 | 画或补全语法图 | 7 | 21 |
| P3-SY-10 | RPN 的用途与用栈求值的方法 | 4 | 13 |
| P3-SY-11 | 中缀表达式与 RPN 互相转换 | 17 | 37 |
| P3-SY-12 | RPN 求值与栈内容变化 | 11 | 44 |
| P3-SC-01 | 加密术语与对称、非对称加密 | 10 | 19 |
| P3-SC-02 | 用密钥对发送私密消息与已验证消息 | 5 | 18 |
| P3-SC-03 | 量子密码 | 6 | 16 |
| P3-SC-04 | SSL/TLS | 4 | 12 |
| P3-SC-05 | 数字证书 | 5 | 16 |
| P3-SC-06 | 数字签名的产生与验证 | 5 | 16 |
| P3-AI-01 | 图的结构与在 AI 中的用途 | 2 | 4 |
| P3-AI-02 | A* 与 Dijkstra 算法：目的与区别 | 5 | 9 |
| P3-AI-03 | 用 Dijkstra 算法求最短距离 | 4 | 20 |
| P3-AI-04 | 用 A* 算法求路径 | 2 | 10 |
| P3-AI-05 | 机器学习的类别 | 7 | 23 |
| P3-AI-06 | 人工神经网络与深度学习 | 9 | 23 |
| P3-AI-07 | 反向传播与回归 | 2 | 7 |
| P3-CT-01 | 线性查找与二分查找：条件与步骤 | 4 | 10 |
| P3-CT-02 | 写或补全查找算法 | 7 | 31 |
| P3-CT-03 | 写或补全排序算法 | 2 | 9 |
| P3-CT-04 | 算法效率与大 O 表示法 | 10 | 20 |
| P3-CT-05 | ADT 的概念、选择与相互实现 | 6 | 14 |
| P3-CT-06 | 用数组实现栈 | 10 | 33 |
| P3-CT-07 | 用数组实现队列 | 4 | 14 |
| P3-CT-08 | 链表的操作与实现 | 3 | 10 |
| P3-CT-09 | 二叉树：结点图、存储表与查找 | 8 | 32 |
| P3-CT-10 | 递归的概念、特征与适用场合 | 6 | 13 |
| P3-CT-11 | 递归与栈：编译器怎样实现递归 | 2 | 7 |
| P3-CT-12 | 追踪递归算法 | 2 | 9 |
| P3-FP-01 | 编程范式 | 0 | 0 |
| P3-FP-02 | 寻址方式与汇编代码执行结果 | 3 | 7 |
| P3-FP-03 | 用给定指令集写汇编代码 | 5 | 32 |
| P3-FP-04 | OOP 术语 | 14 | 39 |
| P3-FP-05 | 补全类图 | 5 | 23 |
| P3-FP-06 | 用伪代码定义类 | 3 | 11 |
| P3-FP-07 | 声明式编程：写事实 | 7 | 21 |
| P3-FP-08 | 声明式编程：目标及其结果 | 10 | 14 |
| P3-FP-09 | 声明式编程：写规则 | 5 | 20 |
| P3-FP-10 | 文件处理伪代码 | 8 | 43 |
| P3-FP-11 | 异常与异常处理 | 9 | 21 |

合计：561 行、1580 分。

## 技能频次

单位为使用该技能的得分点条数；全部语料列含扩展与继承，核验去重列排除扩展与继承。0 仅表示本次拆分未使用。

| 技能 | 全部语料 | 核验去重 |
|:--|--:|--:|
| accumulator | 3 | 2 |
| array-2d | 0 | 0 |
| array-copy | 0 | 0 |
| array-index | 16 | 9 |
| array-of-records | 6 | 4 |
| assign-value | 17 | 6 |
| binary-search | 24 | 19 |
| binary-tree | 9 | 6 |
| boolean-return | 0 | 0 |
| boundary-values | 0 | 0 |
| bubble-sort | 0 | 0 |
| byval-byref | 0 | 0 |
| case-of | 0 | 0 |
| case-range | 0 | 0 |
| char-code | 0 | 0 |
| char-compare | 0 | 0 |
| char-loop | 0 | 0 |
| class-definition | 12 | 8 |
| containment | 0 | 0 |
| count-loop | 5 | 2 |
| counting-array | 0 | 0 |
| data-types | 37 | 27 |
| date-functions | 0 | 0 |
| declare-array | 0 | 0 |
| declare-variables | 0 | 0 |
| div-mod | 1 | 1 |
| encapsulation | 3 | 2 |
| exception-handling | 0 | 0 |
| field-extract | 0 | 0 |
| file-append | 0 | 0 |
| file-close | 5 | 4 |
| file-open-read | 2 | 1 |
| file-write | 4 | 2 |
| find-fix-errors | 0 | 0 |
| flag-variable | 9 | 8 |
| flowchart-draw | 0 | 0 |
| flowchart-to-pseudocode | 0 | 0 |
| getter-setter | 14 | 11 |
| global-scope | 0 | 0 |
| inheritance | 4 | 2 |
| initialise-variables | 19 | 16 |
| input-prompt | 2 | 2 |
| input-validation | 0 | 0 |
| insertion-sort | 30 | 12 |
| linear-search | 5 | 5 |
| linked-list | 3 | 3 |
| logic-ops | 5 | 5 |
| loop-bounds | 7 | 4 |
| loop-choice | 0 | 0 |
| loop-step | 0 | 0 |
| loop-to-eof | 3 | 2 |
| max-min | 0 | 0 |
| module-header | 9 | 7 |
| nested-if | 3 | 1 |
| nested-loops | 5 | 2 |
| operator-precedence | 0 | 0 |
| output-format | 5 | 5 |
| p4-identifiers | 0 | 0 |
| parallel-arrays | 12 | 3 |
| polymorphism | 2 | 1 |
| post-condition-loop | 3 | 2 |
| pre-condition-loop | 11 | 8 |
| procedure-call | 4 | 1 |
| queue-array | 13 | 9 |
| random-file | 23 | 20 |
| random-numbers | 0 | 0 |
| record-type | 22 | 14 |
| recursion | 0 | 0 |
| relational-ops | 22 | 17 |
| return-value | 9 | 4 |
| sentinel-loop | 0 | 0 |
| shift-values | 5 | 2 |
| stack-array | 22 | 13 |
| string-concat | 0 | 0 |
| string-functions | 0 | 0 |
| string-index | 0 | 0 |
| trace-dry-run | 0 | 0 |
| translate-pseudocode | 0 | 0 |
| type-conversion | 0 | 0 |
| user-defined-type | 23 | 12 |

## low 清单

| 行 | 主题型 | 理由 |
|:--|:--|:--|
| 9618_s21_31:3(a) | P3-SY-04 | 指南 §7.18 连线：分页/虚拟内存 2 分、内核中断/调度 2 分、多任务 1 分；两主题并列且题干无偏向，暂取 SY-04，供总控裁决。 |
| 9618_s21_32:3(a) | P3-SY-04 | 指南 §7.18 连线：分页/虚拟内存 2 分、内核中断/调度 2 分、多任务 1 分；两主题并列且题干无偏向，暂取 SY-04，供总控裁决。 |
| 9618_s21_33:3(a) | P3-SY-04 | 指南 §7.18 连线：分页/虚拟内存 2 分、内核中断/调度 2 分、多任务 1 分；两主题并列且题干无偏向，暂取 SY-04，供总控裁决。 |

## 核验语料不足两次的题型

| 题型 | 名称 | 去重行数 |
|:--|:--|--:|
| P3-SY-05 | 解释器怎样执行程序 | 1 |
| P3-FP-01 | 编程范式 | 0 |

## 拆分豁免与边界记录

| 行 | 依据 |
|:--|:--|
| 9618_s25_31:4(a) | 作答是二叉树结点图或指针/记录数组表，不是代码；指南 §8.1 明确排除。 |
| 9618_s25_32:11(a) | 作答是二叉树结点图或指针/记录数组表，不是代码；指南 §8.1 明确排除。 |
| 9618_w24_31:11(a) | 作答是二叉树结点图或指针/记录数组表，不是代码；指南 §8.1 明确排除。 |
| 9618_w24_31:11(b) | 作答是二叉树结点图或指针/记录数组表，不是代码；指南 §8.1 明确排除。 |
| 9618_w24_32:11(a) | 作答是二叉树结点图或指针/记录数组表，不是代码；指南 §8.1 明确排除。 |
| 9618_w24_32:11(b) | 作答是二叉树结点图或指针/记录数组表，不是代码；指南 §8.1 明确排除。 |
| 9618_w24_33:11(a) | 作答是二叉树结点图或指针/记录数组表，不是代码；指南 §8.1 明确排除。 |
| 9618_w24_33:11(b) | 作答是二叉树结点图或指针/记录数组表，不是代码；指南 §8.1 明确排除。 |

- 9618_s22_32:8(a)：MS p.8 只列四条填空片段，并未给完整代码。与 QP p.11 四个留空行一一对应，按原文片段拆四点，不补出 MS 不存在的整行。指南 §8.2 B 未明确覆盖这种简写，已在 tag_note 说明。
- 9618_w23_32:12(b)：SEEK 行有两处空，MS 按 blank 给分，合并为 2 分；9618_s24_31:10(b) 与 9618_s24_33:10(b) 的 WHILE 两处空按 completed line 合并为 1 分。
- 9618_s24_33:10(b) 虽不属于 D35 的逐字重复行，但本卷 QP/MS 独立核验后，五条对应答案与 _31 相同；仅复用内容完全相同的映射。
- 布尔表达式上划线只用于原页判型，不改抽取原文；所有得分点 text 仍是该行 ms_text 压缩空白后的子串。

## 需要总控决定

- 9618_s21_31:3(a)（及重复行）：SY-04 与 SY-03 各占两条连线，SY-02 占一条。暂取 SY-04，cross 为 SY-03、SY-02，low；请裁决并补清 §7.18 的同票规则。
- 9618_s22_32:1(b)(iii)：DR-02 summary 把枚举字段赋值收入，但 DR-04 summary/not 与指南 §7.4 又将字段赋值归 DR-04。此处按直接产出取 DR-04，建议统一 taxonomy 边界措辞。
- 9618_s22_32:8(a)：建议 §8.2 B 明确“MS 仅提供填空答案片段”可按 QP 留空行逐一映射且保留片段，不强行拼出非 MS 子串的整行。
- 无建议新增的题型或技能标签；P3 词表 extends P2 已满足本次标注需要。共享文件及 P2 apply 未改。
