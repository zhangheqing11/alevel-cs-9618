# CIE 9618 Paper 1 · Theory Fundamentals 题型手册

> 2027 年 5–6 月考季用。语料：2022–2026s 全部 variant（核验语料）+ 2021（扩展）。给分依据只认每题自己的 MS；本手册的英文得分句都逐字引自对应 MS，并标出题号。

## 使用指南

### 这本手册怎么组织

- **9 章 88 个题型**，章序就是建议的学习顺序：IR 信息表示 → CM 通信 → HW 硬件 → LG 逻辑门 → PF 处理器 → SS 系统软件 → SP 安全与完整性 → EO 伦理与所有权 → DB 数据库。前面的章是后面的基础（IR 的二进制是 LG、PF 的前提；HW 的缓冲区与中断在 PF 再出现）。
- 每章开头是**核心思想**（这一章在解决什么问题、题型之间怎么连）和**题型树**（每型的星级、小问数、分值）；章末是**本章易混辨析**。
- 每个题型一张**题型卡**，固定 9 个部分：

| 部分 | 作用 |
|:--|:--|
| 考情 | 构建器按语料自动统计：小问数、分值、出现卷数、设问分布、★ |
| 考法 | 这个题型怎么问、常见几种变化 |
| 识别信号 | 题干里能认出它的英文原词 |
| 解题思路 | 编号步骤，照着做就能写出得分答案 |
| 得分表述 | 3–6 句最常出现、最能拿分的 MS 原句，可直接默写 |
| 易错与失分 | 来自 MS 的限定与常见混淆 |
| 代表题精讲 | 一道 2022–25 的典型题：在考什么 → 完整作答 → 与 MS 逐点对齐 → 英文作答句 |
| 下一道变式 | 同型、换了一个特征的另一题，自己做 |
| 刷题清单 | 构建器自动列出该型全部真题，新卷在前；2021 扩展单列 |

- 另有一份**核心概念表**（`P1核心概念`）：每章的术语按“英文得分句 / 中文定义 / 直观理解”三层列出。英文列带题号的是 MS 原句；标“非 MS 原句”的是标准定义，用于理解与默写。

### 记号

- **题号**写成短格式：`s24/12 Q3(b)(ii)` = 2024 年 6 月考季、Paper 1 第 2 套（variant 2）、第 3 题 (b)(ii)。季：`s` = 5–6 月，`w` = 10–11 月。
- **“英文句” + 题号**：逐字引自该题 MS 的句子（校验器逐字核对过）。
- **“讲解时请对照原卷 QP p.N”**：这道题要看图、表或作图区才能讲清，学习时打开原卷第 N 页。
- **★ 星级**由构建器按出现频率与分值算出，★★★ 为几乎每季必考。
- **2026 年 6 月的 12 份卷**（`s26`）留给考前限时整卷模考：专项刷题时跳过；手册的代表题与变式也避开了它们。

### 推荐用法

1. **首学一个题型**：读卡的“考法 → 识别信号 → 解题思路”，再看代表题精讲（直接看讲解，不必先做）。
2. **自己做“下一道变式”**，用英文作答，按该题 MS 批改。
3. **刷题**：从刷题清单里由新到旧取没做过的题；每次批改都对照 MS 原文，把丢分的那个词记下来。
4. **默写**：“得分表述”和核心概念表的英文列是定义题、解释题的标准句，考前反复默写。
5. 发现卡片里的错误或 MS 引文问题，记到 `handoff/勘误.md`，由总控修正。

## P1 考情总览

- **试卷**：1 小时 30 分钟，75 分；全部笔答；**禁用计算器**——进制、补码、文件大小都要手算，写出过程。
- **题目形式**：短答（state / identify / give）、描述与解释（describe / explain / justify）、计算与转换、补全表格与描述、画图（逻辑电路、拓扑、E-R 图）、SQL、汇编指令跟踪。
- **各章分量**（核验语料，构建器自动统计）：

<!-- auto:chapter-stats -->

读这张表：数据库、信息表示、处理器三章分值最多，合起来超过一半；逻辑门、伦理两章分值少，但逻辑门几乎每卷必考、套路固定，是最稳的分。

## 通用得分规则

以下规则从 MS 的写法归纳而来，适用于全卷。每条都附了一处 MS 原文作例子；具体某题的给分永远以那题自己的 MS 为准。

### 1. 一个得分点一分，点数要够

P1 的 MS 绝大多数是“列出可得分点，每点 1 分，封顶 n 分”：「1 mark per bullet point, max 2 marks」⟦9618_w25_12:5(a)⟧。所以：

- 分值 = 需要写出的**独立**得分点数。3 分题写 3 个不同的点，最好多写一个作保险。
- 同一个意思换说法写两遍只算一分（“faster to download”和“takes less time to download”）。
- MS 里以 `…` / `...` 开头的点是**前一点的展开**，通常要和前一点一起写才成立：先写“Transmission time is reduced”，再写“… so the teacher does not have to wait as long”。

### 2. 读懂 MS 的记号

| 记号 | 含义 |
|:--|:--|
| `/` | 同一得分点里可以互换的词（`private / dedicated`） |
| `//` | 同一得分点的另一种写法，任写其一 |
| `( )` | 括号里的内容不要求，只提供语境 |
| `e.g.` / `Examples:` | 举例，列出的不是全部可接受答案 |
| `max n` | 本组最多给 n 分 |
| `NE` | not enough，说得不够，不给分：「just faster is NE」⟦9618_s26_11:7(c)(ii)⟧ |

### 3. 选择本身常常不给分，分数在理由上

“Tick … and justify”“State whether … monitoring or control … Justify”这类题，MS 常写「No marks for the identification of the system」⟦9618_w24_11:5(c)⟧。选对了但没写理由 = 0 分；理由写充分了，有时即使选的是另一边也能按那一边的理由给分（MS 同时列出两边理由时）。

### 4. 有情境就扣情境

题目给了具体系统（视频门铃、银行 App、CCTV 主机），答案要说**这个系统**的东西：「Dedicated to one task applied to example」⟦9618_w23_11:9(b)⟧。泛泛背定义、不提情境，常常拿不到 justify / explain 的分。

### 5. 题干已经给的不能再写

“Identify two **other** items …”“Describe two **other** reasons …”时，题干里已经出现的那一项不得分（如题干已给 colour depth 与 resolution，再写它们就白写，见 ⟦9618_s23_11:1(b)(i)⟧）。

### 6. 两边都要写

- 比较、区别题成对写：“X …, whereas Y …”。只写一边通常只得一半或不得分。
- “Discuss the benefits and drawbacks”只写一边会封顶：「max 3 if only either benefits or drawbacks discussed, not both」⟦9618_s26_12:6(d)⟧。
- “应用 + 理由”题，理由必须对应所写的应用：「1 mark for application and 1 mark for corresponding justification」⟦9618_s25_12:2(c)⟧。

### 7. 计算题：过程分与答案分分开

计算、转换题普遍「1 mark for working, 1 mark for answer」⟦9618_w22_11:1(b)⟧。

- 题目写了 Show your working 就一定写过程：答案错了，过程仍可能得 1 分；只写答案、答案又错，就是 0 分。
- 单位按题目要求（MB 与 MiB 不同），二进制答案按题目要求的位数写满。

### 8. 连线、勾选题的分档

连线与勾选题常按“对几行给几分”分档：「1 mark for 1 correct line」⟦9618_w23_13:1(b)⟧，「2 marks for 3 correct lines」⟦9618_w23_13:1(b)⟧；也有整题全对才给分的：「1 mark for all 3 appropriate sensors」⟦9618_w24_11:5(a)⟧。每一行都值得检查。

### 9. 画图：标注齐全、不多画

拓扑、电路、E-R 图按“该有的连接都有、没有多余的连接”给分：「All computers directly connected to switch and no other connections」⟦9618_w25_12:5(b)⟧；逻辑电路同理：「1 mark for correct OR and NOT gates with correct inputs and no superfluous gates」⟦9618_s24_12:1(b)⟧。所有部件都要标名称。

### 10. 用精确的术语

- 写机制而不是形容词：“the switch checks the destination address of each packet”，而不是“the switch sends it to the right place”；“quantisation errors are smaller”，而不是“better quality”。
- 不写品牌名，写设备或软件的类别。
- 定义里的限定词逐个保留：unique、in sequence、temporary、per second、at regular intervals……少一个常常整点不给。
