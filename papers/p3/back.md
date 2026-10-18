## 书末　跨章入口、解释题与写代码题的得分链、命令词 {#back}

前面 9 章按题型拆开讲；本部分把它们收拢成四件事：①看到一道题，知道去哪一章、哪张卡，以及哪些概念会跨章出现；②Explain / Describe 类解释题怎样按 MS 的给分结构组织答案；③写伪代码（以及汇编、声明式子句、追踪表这类“写代码式”的题）每一环拿什么分；④每个命令词要你做什么。每一条都配了真实例题行，学的时候回到对应题型卡。

### 跨章入口一：卷面地图与按题目特征找题型

P3 和 P1 不一样：P1 常用一个长情境串起好几章，P3 的**一道大题通常只考一个主题**，各小问在同一章里由浅入深。卷面顺序也大致跟着考纲走：按脚本统计 2022–2025 的 18 份卷（核验语料，去掉与另一 variant 大半重复的卷，按每题小问的主题型多数定章），第 1 题有 17 份是 DR（浮点数或用户定义类型），最后一题有 15 份是 CT 或 FP。所以开卷先做 DR 的计算与声明，卷尾留足时间给写伪代码的 CT / FP 大题。

| 看到这些词或这种格式 | 去哪一章 | 题型 | 真题例 |
|:--|:--|:--|:--|
| mantissa、exponent、normalised、two’s complement 的浮点数 | DR | DR-09 至 DR-12（换算、规格化、最大最小值、精度与溢出） | ⟦9618_s24_31:1(a)⟧、⟦9618_w22_31:1(a)⟧、⟦9618_w25_33:2(a)⟧ |
| `TYPE … ENDTYPE`、enumerated、pointer `^`、`SET OF`、record | DR | DR-01 至 DR-05 | ⟦9618_s23_32:6(a)⟧、⟦9618_w25_33:1(a)(i)⟧、⟦9618_w24_31:6(b)⟧ |
| serial / sequential / random file organisation、direct access、hashing、collision | DR | DR-06 至 DR-08（概念；写文件代码是 FP-10） | ⟦9618_w24_32:2(a)⟧、⟦9618_s24_32:7(a)⟧、⟦9618_w24_31:5(a)⟧ |
| TCP/IP 四层、protocol、HTTP / FTP / POP3 / IMAP / SMTP、BitTorrent | CI | CI-01 至 CI-04 | ⟦9618_w24_31:4⟧、⟦9618_w23_31:2(b)⟧、⟦9618_w25_33:4⟧、⟦9618_w25_32:3(b)⟧ |
| circuit switching、packet switching、router | CI | CI-05 至 CI-07 | ⟦9618_w24_31:3(a)⟧、⟦9618_w25_33:3⟧、⟦9618_s23_32:7(b)⟧ |
| RISC / CISC、pipelining、interrupt；SISD / SIMD / MISD / MIMD；massively parallel；virtual machine | HV | HV-01 至 HV-05 | ⟦9618_w24_31:2⟧、⟦9618_s24_31:11(b)⟧、⟦9618_w23_31:5⟧、⟦9618_s23_31:8⟧、⟦9618_w22_32:5⟧ |
| 逻辑电路图、半加器 / 全加器、SR / JK 触发器、sum-of-products、Karnaugh map、De Morgan | BL | BL-01 至 BL-07 | ⟦9618_w25_32:6(a)⟧、⟦9618_s22_32:6(b)(i)⟧、⟦9618_w22_32:8(a)⟧、⟦9618_w25_32:6(b)(i)⟧、⟦9618_w25_33:6(b)⟧ |
| OS 隐藏硬件、multi-tasking、process states、scheduling、paging / segmentation、disk thrashing | SY | SY-01 至 SY-04 | ⟦9618_w25_31:4(b)⟧、⟦9618_w25_33:5(b)⟧、⟦9618_w25_32:5(a)⟧、⟦9618_w24_31:8(b)⟧ |
| interpreter、compilation 的阶段（lexical analysis、optimisation） | SY | SY-05、SY-06 | ⟦9618_s25_31:6⟧、⟦9618_w25_31:8(a)⟧ |
| syntax diagram、Backus-Naur Form（`::=`、`|`） | SY | SY-07 至 SY-09 | ⟦9618_w24_32:7(a)⟧、⟦9618_w24_32:7(b)⟧、⟦9618_w24_32:7(c)(i)⟧ |
| Reverse Polish Notation、用栈求值 | SY | SY-10 至 SY-12 | ⟦9618_w23_32:6(b)⟧、⟦9618_w25_33:7(b)⟧、⟦9618_s22_31:5(b)(i)⟧ |
| symmetric / asymmetric、public / private key、quantum cryptography、SSL / TLS、digital certificate、digital signature | SC | SC-01 至 SC-06 | ⟦9618_w22_32:6(a)⟧、⟦9618_w22_31:6(b)⟧、⟦9618_s23_32:5(a)⟧、⟦9618_s25_33:7⟧、⟦9618_w25_31:5(a)⟧、⟦9618_w22_31:6(c)⟧ |
| graph、A* / Dijkstra、machine learning 的类别、neural network、deep learning、back propagation、regression | AI | AI-01 至 AI-07 | ⟦9618_s25_31:10(a)⟧、⟦9618_s25_33:10(b)⟧、⟦9618_w25_33:8⟧、⟦9618_s23_32:10(b)⟧、⟦9618_w22_32:7⟧、⟦9618_w25_31:7(b)⟧、⟦9618_w25_32:9(b)⟧ |
| linear / binary search、insertion / bubble sort、Big O | CT | CT-01 至 CT-04 | ⟦9618_s22_32:8(b)(ii)⟧、⟦9618_s24_31:10(b)⟧、⟦9618_s25_33:12(b)⟧、⟦9618_s22_32:8(c)⟧ |
| ADT、stack、queue、linked list、binary tree（Top / Front / Rear / NextPointer / LeftPtr） | CT | CT-05 至 CT-09 | ⟦9618_w23_31:10(c)⟧、⟦9618_w23_31:10(b)⟧、⟦9618_s23_31:11(b)⟧、⟦9618_w22_32:11(a)⟧、⟦9618_s25_31:4(a)⟧ |
| recursion、base case、winding / unwinding、递归函数的追踪表 | CT | CT-10 至 CT-12 | ⟦9618_w25_31:9(b)⟧、⟦9618_w25_32:12(b)⟧、⟦9618_s23_31:12(b)⟧ |
| imperative / declarative / object-oriented / low-level | FP | FP-01 | ⟦9618_s21_31:9(c)⟧（2021 扩展卷） |
| `LDM` / `LDD` / `LDI` / `STO`、addressing mode、ACC | FP | FP-02、FP-03 | ⟦9618_s22_31:9(a)⟧、⟦9618_w25_32:11⟧ |
| class、object、getter / setter、inheritance、类图、`CLASS … ENDCLASS` | FP | FP-04 至 FP-06 | ⟦9618_w22_31:11(a)⟧、⟦9618_s25_31:11(a)⟧、⟦9618_w22_31:11(b)⟧ |
| 小写谓词 + 句点的事实库、goal、rule `… IF …` | FP | FP-07 至 FP-09 | ⟦9618_w23_32:11(a)⟧、⟦9618_s22_32:2(c)⟧、⟦9618_s24_31:8(c)⟧ |
| `OPENFILE`、`SEEK`、`GETRECORD`、`PUTRECORD`、`EOF`；exception | FP | FP-10、FP-11 | ⟦9618_s25_32:13⟧、⟦9618_w25_31:10⟧ |

### 跨章入口二：同一道大题里的组合

一道大题内的几个小问通常属于同一章，但有几种组合在不同年份反复出现，而且偶尔跨章。读到 (a) 就能预判 (b)(c) 问什么。

| 组合 | 常见的小问顺序 | 跨的题型 | 真题例 |
|:--|:--|:--|:--|
| 记录类型 → 随机文件 | 先声明记录类型 `TYPE … ENDTYPE` → 再补全用这个类型读写随机文件的伪代码 | DR-03 → FP-10 | ⟦9618_s23_32:6(a)⟧、⟦9618_s23_32:6(b)⟧ |
| 记录 → 改写成类 | 给记录变量赋值 → 枚举类型 → 记录改成类：写 PRIVATE 属性、说明为什么 PRIVATE | DR-04、DR-02 → FP-06、FP-04 | ⟦9618_s22_32:1(a)⟧ 至 ⟦9618_s22_32:1(c)(ii)⟧ |
| 文件处理 + 异常 | 补全随机文件代码 → 定义异常处理 / 描述异常 → 说出异常的原因 | FP-10 + FP-11 | ⟦9618_w23_31:8(a)⟧ 至 ⟦9618_w23_31:8(c)⟧；⟦9618_w23_32:12(a)⟧、⟦9618_w23_32:12(b)⟧ |
| 编译 → RPN | 编译某阶段的作用 → 中缀写成 RPN → 用栈求值并画出栈的变化 | SY-06 → SY-11 → SY-12 | ⟦9618_w25_31:8(a)⟧ 至 ⟦9618_w25_31:8(c)⟧；⟦9618_w25_33:7(a)⟧ 至 ⟦9618_w25_33:7(c)⟧ |
| RPN → 栈的其他用途 | 写 RPN → 画栈的变化 → 描述求值步骤 → 说出栈的另外两种用途 | SY-11、SY-12、SY-10 → CT-05 | ⟦9618_s22_31:5(a)⟧ 至 ⟦9618_s22_31:5(c)⟧ |
| 用数组实现栈 → 递归 | 补全 Push / Pop → 递归的三个特征，或为什么用栈实现递归 / 编译器怎样用栈 | CT-06 → CT-10 / CT-11 | ⟦9618_w25_31:9(a)(i)⟧ 至 ⟦9618_w25_31:9(b)⟧；⟦9618_w25_32:12(a)(i)⟧ 至 ⟦9618_w25_32:12(b)⟧；⟦9618_w23_32:9(a)(i)⟧ 至 ⟦9618_w23_32:9(c)⟧ |
| 二叉树 → 递归 | 补全二叉树的结点图 → 描述递归 → 可用递归实现的 ADT | CT-09 → CT-10 | ⟦9618_s25_31:4(a)⟧ 至 ⟦9618_s25_31:4(c)⟧；⟦9618_s25_32:11(a)⟧、⟦9618_s25_32:11(b)⟧ |
| 栈 / 队列实现 → 比较与选择 | 声明 → 补全 Pop / Dequeue → 栈与队列比较、链表与数组比较、用两个栈实现队列 | CT-06 / CT-07 → CT-05 | ⟦9618_w23_31:10(a)⟧ 至 ⟦9618_w23_31:10(c)⟧；⟦9618_s23_31:11(a)⟧ 至 ⟦9618_s23_31:11(c)⟧ |
| 查找三连 | 二分查找的前提 → 补全查找伪代码 / 描述步骤 → 性能与 Big O | CT-01 → CT-02 → CT-04 | ⟦9618_s24_31:10(a)⟧ 至 ⟦9618_s24_31:10(c)⟧；⟦9618_s22_32:8(a)⟧ 至 ⟦9618_s22_32:8(c)⟧ |
| 声明式三连 | 写事实 → 求目标结果 → 写规则 | FP-07 → FP-08 → FP-09 | ⟦9618_s24_31:8(a)⟧ 至 ⟦9618_s24_31:8(c)⟧；⟦9618_w23_31:11(a)⟧ 至 ⟦9618_w23_31:11(c)⟧ |
| OOP 双连 | 补全类图 → 术语（PRIVATE 的理由、继承、多态） | FP-05 + FP-04 | ⟦9618_s25_31:11(a)⟧ 至 ⟦9618_s25_31:11(b)(ii)⟧；⟦9618_w24_31:9(a)⟧、⟦9618_w24_31:9(b)⟧ |
| 汇编双连 | 写汇编 → 运行后标签的值 | FP-03 → FP-02 | ⟦9618_w25_31:11(a)⟧、⟦9618_w25_31:11(b)⟧ |
| RISC → 流水线与中断 | RISC 的特征 → 中断处理过程 → 流水线对中断处理的影响 | HV-01 → HV-02 | ⟦9618_s24_31:11(a)⟧ 至 ⟦9618_s24_31:11(c)⟧；⟦9618_w22_31:10(a)⟧、⟦9618_w22_31:10(b)⟧ |
| 数字证书 → 数字签名 | 描述数字证书 → 它在数字签名中的作用 | SC-05 → SC-06 | ⟦9618_s24_31:7(a)⟧、⟦9618_s24_31:7(b)⟧ |

两个提醒：

1. **主题不决定题型，命令决定。** 同一道栈的大题，问 Complete the pseudocode 是 CT-06，问 Compare and contrast 是 CT-05，问 why a stack is used when a recursive algorithm is executed 是 CT-11。先看这一小问在问什么，再去对应的卡。
2. **前面小问给的名字，后面照抄。** 记录类型名与字段名（DR-03 → FP-10）、栈的数组与指针名（CT-06 的声明 → Push / Pop）、事实库的谓词与参数顺序（FP-07 → FP-09），后面一字不差地用。

### 跨章入口三：同一个概念出现在几章

P3 有几样东西在不同章里换着角色出现。复习一章时顺手把这些“桥”连起来，遇到跨章的问法就不会卡住。

| 概念 | 在哪些题型里出现 | 各自问的是什么 |
|:--|:--|:--|
| 栈（LIFO） | CT-05、CT-06；SY-10 至 SY-12；CT-11；HV-02、SY-03 | ADT 与数组实现；RPN 求值时数值进栈、遇运算符弹出两个；递归调用时压入返回地址与局部变量；中断时把寄存器内容存进栈（⟦9618_s24_31:11(b)⟧） |
| 散列（hash） | DR-08；FP-10 | 散列算法、冲突与处理方法是概念；随机文件里用 `Location ← Hash(…)` 算出位置再 `SEEK` 是代码（⟦9618_w23_31:8(a)⟧） |
| 记录（record） | DR-01、DR-03、DR-04；FP-10；CT-09；FP-06 | 声明与赋值；随机文件以记录为单位读写；二叉树结点存成记录数组；记录改写成类 |
| 指针 | DR-02；CT-06 至 CT-09 | DR-02 是指针**类型**（`^`）的声明；CT 里的“指针”是存数组下标的整数变量 |
| 中断 | HV-02；SY-03；FP-11 | 流水线怎样处理中断；调度中的中断处理；**异常不是中断**（考官报告多次指出考生把两者混淆，见 FP-11） |
| 编译器 | SY-05、SY-06；SY-11；CT-11 | 解释器与编译的阶段；编译时把表达式转成 RPN；编译器用栈实现递归 |
| 图（graph） | CT-05；AI-01、AI-03、AI-04 | 图是一种 ADT；AI 用图表示状态与路径，用 Dijkstra / A* 求最短路径 |
| 二进制补码 | DR-09 至 DR-11；FP-02、FP-03 | 浮点数的尾数与指数用补码；汇编的 `SUB` 结果可以是负数 |
| 协议的分层 | CI-01 至 CI-03；SC-04 | TCP/IP 各层的功能；SSL / TLS 在客户端与服务器之间建立安全连接 |
| AND / NOT | BL-04、BL-07；FP-09；CT-02、FP-10 | 布尔表达式；声明式规则里的 `AND`、`NOT`；伪代码循环条件里的 `AND`（不依赖短路，D25） |

### 解释题得分链

Explain / Describe / Outline 类题目占 P3 文字题的大头。MS 的得分点有几种固定结构；看清是哪一种，答案就照那个结构写，每一句对一个得分点。

#### 链 1　说法 → “…”展开

**结构**　MS 先列一个基本说法（1 分），再列一个以 `…` 开头的展开点（1 分），说明它带来什么或怎样做到。“…”点不能单独成立，必须跟在它前面那一句后面。

**骨架**　*X is / does …, so that / which means …*

**例**
- 异常处理：「Exception handling is a process that responds to unwanted / unexpected events when a program runs」⟦9618_w25_31:10⟧，后接「to prevent the program / computer from stopping unexpectedly」⟦9618_w25_31:10⟧。
- 流水线：「Pipelining allows several instructions to be processed simultaneously / concurrently」⟦9618_s23_32:8(a)⟧，后接「therefore, increasing the CPU instruction throughput」⟦9618_s23_32:8(a)⟧。
- 散列算法：「It is a mathematical formula」⟦9618_w24_31:5(a)⟧，后接「used to perform a calculation applied to the key field of the record being searched / stored」⟦9618_w24_31:5(a)⟧。

**适用**　定义类与作用类：FP-04、FP-11、HV-02、DR-08、CT-10、SC-03、AI-06。

#### 链 2　按顺序的过程步骤

**结构**　MS 把一个过程拆成若干先后步骤，每步 1 分，分值通常少于步骤数。顺序本身不单独给分，但写乱了常常漏步。

**骨架**　*First … → then … → … → finally / repeat until …*　按时间顺序一句一步，主语写清楚（the sender / receiver、the processor、each packet、the interpreter）。

**例**
- 用栈求 RPN 的值：从左到右读 →「Values are pushed onto a stack until an operator is found」⟦9618_w23_32:6(b)⟧ → 弹出两个值做运算、结果压回 →「This repeats until a single value remains, which is the solution」⟦9618_w23_32:6(b)⟧（见 SY-10）。
- 分组交换：「the message is divided into small chunks called packets」⟦9618_w25_33:3⟧ → 每个包加包头 → 独立选路 →「packets are reassembled at the destination into the whole message」⟦9618_w25_33:3⟧（见 CI-06）。
- 接收方验证数字签名：解密得到摘要 → 重新哈希 →「The two message digests are compared」⟦9618_w22_31:6(c)⟧ → 相同则未被篡改（见 SC-06）。
- 中断处理：「Once the processor detects an interrupt at the start/end of the fetch-execute cycle」⟦9618_s24_31:11(b)⟧ →「the current program is temporarily stopped and the status of each register stored on the stack」⟦9618_s24_31:11(b)⟧ → 执行 ISR → 恢复寄存器（见 HV-02）。
- 二分查找：取中间 → 比较 → 舍去一半 → 重复（⟦9618_s22_32:8(b)(ii)⟧，见 CT-01）。

**适用**　Describe how / Explain how … works / Describe the process of：SY-10、CI-06、CI-04、SC-04、SC-06、HV-02、SY-04（分段）、SY-05、CT-01、AI-07。

#### 链 3　成对比较：X …, whereas Y …

**结构**　每个得分点同时写出两边在同一方面的不同。只写一边的句子通常不给分。

**骨架**　*X does …, whereas Y does …*　每一对比较同一个方面（指针个数、路径、顺序、带宽、启发式）。

**例**
- 栈与队列：「A stack has only one moveable pointer whereas a queue has two」⟦9618_w23_31:10(c)⟧。
- 电路交换与分组交换：「All of the transmission in circuit switching follows the same path whereas different packets in packet switching can take different routes」⟦9618_s23_32:7(b)⟧。
- A* 与 Dijkstra：A* 用启发式函数找更好的路径，而「Dijkstra’s just explores all possible routes」⟦9618_s25_33:10(b)⟧。

**适用**　difference / compare / contrast：CT-05、CI-07、AI-02、AI-05、SC-01、CT-04。

#### 链 4　分栏作答：每一栏单独封顶

**结构**　题目点名两件或三件事（好处与坏处、两种角色、两种数据结构、方法与 Big O），MS 每一栏单独封顶。一栏写得再多也补不了另一栏。

**骨架**　题目给了几个标题就用几个标题分开写，每栏写到它的上限。

**例**
- 虚拟机的描述、好处、坏处：「One mark for each correct benefit (Max 2)」⟦9618_w22_32:5⟧，描述与坏处另各封顶（见 HV-05）。
- 为什么用链表而不是数组实现栈：「One mark for linked list and one mark for array」⟦9618_w23_32:9(b)⟧——只夸链表最多 1 分（见 CT-05）。
- 比较查找方法并写 Big O：方法与 Big O 两部分各自封顶（⟦9618_s24_32:8(b)⟧，见 CT-01、CT-04）。
- 异常处理的解释与例子：解释 Max 2、例子 Max 1（⟦9618_w25_31:10⟧，见 FP-11）。
- properties、methods、inheritance 各最多 2 分（⟦9618_s22_31:7(b)⟧，见 FP-04）。

**适用**　benefits and drawbacks / Explain the roles of A and B / Describe X and Y：HV-05、SC-03、CI-05、CI-06、CT-05、FP-04、FP-11、DR-06。

#### 链 5　成对给分：说出一点 + 展开这一点

**结构**　MS 写明一个好处（或方法、特征）占 2 分：说出来 1 分，说明它怎样起作用或带来什么 1 分。只列名字、不展开，只拿一半。

**骨架**　*Point, because / by / which … .*　题目要两个好处，就写两组“点 + 展开”。

**例**
- 用虚拟机试新系统的好处：「Two marks each benefit description max 4」⟦9618_s22_31:6⟧，例如“不用买新硬件”要接在“可以在不同的虚拟硬件上试”之后。
- 分组交换怎样确保收到完整消息：「Two marks for each description mark as 2 x 2」⟦9618_w25_31:3(c)⟧（见 CI-06）。
- 操作系统怎样隐藏硬件的复杂性：「One mark for identification and one mark for a description」⟦9618_w25_31:4(b)⟧（见 SY-01）。

**适用**　Describe two ways / two benefits，以及“说出一个并说明作用”：HV-05、CI-06、SY-01、SC-04（⟦9618_s25_32:10⟧：协议名一分、作用一分）。

#### 链 6　因果链：原因 → 机制 → 后果

**结构**　问“为什么会出现某个问题 / 会发生什么”。MS 按因果顺序排 3–5 个点：在什么情况下 → 中间发生了什么 → 最后导致什么。

**骨架**　*When …, … happens, which leads to …, so eventually …*

**例**
- 磁盘抖动：使用虚拟内存时 →「As the main memory fills up, more and more pages need to be swapped in and out of virtual memory」⟦9618_w24_31:8(b)⟧ → 磁盘访问极频繁 →「Eventually, more time is spent swapping pages than processing data」⟦9618_w24_31:8(b)⟧（见 SY-04）。
- 浮点数的舍入误差：0.20 不能用二进制精确表示 →「therefore, there will be a loss of precision due to a rounding error/truncation」⟦9618_w23_31:1(b)⟧（见 DR-12）。
- 上溢：两个大数相乘 → 结果超出可表示范围 → 尾数或指数的最高位丢失（⟦9618_w25_33:2(b)⟧，见 DR-12）。

**适用**　Explain the problem / the effect / the circumstances：DR-12、SY-04、HV-02（流水线对中断的影响）。

#### 链 7　为什么合适：特性 → 正好满足需求

**结构**　问“为什么用 X 做这件事”。先说 X 的关键特性，再说这个特性怎样对上这件事的需求；常再加一句“换成另一种会怎样”。

**骨架**　*X has property P; the task needs Q; P gives Q (whereas Y would …).*

**例**
- 为什么用栈实现递归：「Stacks store data in Last In First Out (LIFO) / First In Last Out (FILO) order」⟦9618_w25_32:12(b)⟧ → 每次调用压栈 → 到基本情况开始展开 →「data is popped from the stack in the reverse order to which it was pushed onto it」⟦9618_w25_32:12(b)⟧（见 CT-11）。
- 为什么打印任务用队列：「Print jobs are expected to be actioned by the printer in the order they are received」⟦9618_s23_32:11(b)⟧ → 队列先进先出 → 换成栈，第一个任务要等其他任务全打完（见 CT-05）。

**适用**　Explain why X is suitable / works better：CT-05、CT-11、CT-10（何时用递归有益）。

#### 链 8　通用步骤 + 套进题目的数据

**结构**　题目给了具体的表达式、数据或例子，要求“描述这一个怎样做”。MS 对只写通用步骤的答案封顶，满分要求把步骤套进题目给的数。

**骨架**　每一步都带上题目里的具体值：*Push 10, push 3, push 2; at the operator \*, pop 2 and 3 …*

**例**　描述用栈求某个 RPN 表达式的主要步骤：「Max 3 generic answer only」⟦9618_s22_31:5(b)(ii)⟧——4 分题只写通用步骤最多 3 分，要写出“把哪几个数压栈、遇到哪个运算符弹出哪两个”。

**适用**　SY-10；其他题目问“描述这一个（this / the given …）怎样做”时，也把题目给的数据写进每一步。

### 写代码题得分链

P3 的写代码题有两类：**伪代码**（CT 的查找、排序、栈、队列；DR 的类型声明；FP 的类与文件处理），以及**“写代码式”的非伪代码题**（汇编、声明式子句、类图、追踪表与栈的变化）。前者按一条通用的链给分，后者各有固定的给分结构。

#### 伪代码五环

| 环 | 拿什么分 | MS 的写法 | 怎样丢分 |
|:--|:--|:--|:--|
| 1 声明 | 常量、数组（上下界与类型）、记录 / 类的头尾、指针变量 | 「correctly defined constant」⟦9618_s23_31:11(a)⟧；「three correctly defined integers」⟦9618_s23_31:11(a)⟧；「One mark for TYPE TAppointments and ENDTYPE correct」⟦9618_s23_32:6(a)⟧ | 数组上界多 1；漏 `ENDTYPE` / `ENDCLASS`；名字没照题目给的标识符表 |
| 2 初值 | 标志设 FALSE、上下界或位置从下界开始、文件名变量 | 「Found ← FALSE」⟦9618_s24_31:10(b)⟧ | 初值放进循环里（每轮被重置）；漏掉一个标志 |
| 3 循环与结束条件 | 前测 / 后测 / 计数循环，条件写全 | 「WHILE Found = FALSE AND NotInList = FALSE」⟦9618_s24_31:10(b)⟧；「UNTIL EOF(DentalFile)」⟦9618_s23_32:6(b)⟧ | 条件只写一半；用 `=` 与 `<>` 写反；在条件里读数组元素、依赖 AND 短路（D25） |
| 4 核心动作 | 中点与移动上下界、后移元素、移动指针、`SEEK` + `GETRECORD` / `PUTRECORD` | 「TopOfList ← CurrentItem + 1」⟦9618_s24_31:10(b)⟧；「Temporary assignment of the element being ‘inserted’ before inner loop」⟦9618_s25_33:12(b)⟧；「Re-insertion of the element outside the inner loop」⟦9618_s25_33:12(b)⟧ | 用 `/` 不用 `DIV`；`Low ← Mid`（范围不缩小）；`GETRECORD` 前没有 `SEEK` |
| 5 收尾 | 关闭文件、返回值、找不到时的提示 | 「CLOSEFILE "ActiveFile.txt"」⟦9618_s23_31:10⟧；「IF Stored = FALSE THEN」⟦9618_s25_33:11⟧ | 只关了一个文件；函数漏 `RETURN`；没处理“找不到 / 已满” |

**填空题的推断法**　P3 的伪代码题多半是“Complete the pseudocode”，一行一分。空行几乎都能从**已给的行**推出来：

- **配对**：有 `CLOSEFILE` 就要有 `OPENFILE`；有 `NEXT` 就要有 `FOR`；有 `ENDWHILE` 就要有 `WHILE`；有 `GETRECORD` 读进来，前面就要有 `SEEK`。
- **对称**：已有 `NotInList ← FALSE` 就补 `Found ← FALSE`；ELSE 里是 `High ← Mid - 1`，对面就是 `Low ← Mid + 1`；THEN 里置 `Found ← TRUE`，条件就是“相等”。
- **名字**：变量、字段、文件名一律用代码里已经出现的（⟦9618_s25_32:13⟧ 的五个空全部能这样推出来，见 FP-10）。

**两条底线**（决策 D2、D25）：要求伪代码时，不能混入 Python 写法（`def`、`len()`、`for x in`、`open()`），否则那一分不给；循环条件不依赖 AND 短路，读数组元素放进循环体。

#### 非伪代码的“写代码式”题

| 题型 | 给分结构 | MS 的写法 | 要点 |
|:--|:--|:--|:--|
| 汇编（FP-03） | 每个动作一分 + 标签的设置另给分 | 「One mark for labelling that address e.g. Twenty away from the program code」⟦9618_s22_31:9(b)⟧ | 只用题给指令；代码写横线上、标签写表里；操作数不加尖括号 |
| 声明式规则与目标（FP-08、FP-09） | 每个子目标一分 + 运算符与标点全对一分 | 「all correct Boolean operators and punctuation (allow , for AND) and no additional lines of code」⟦9618_s24_31:8(c)⟧ | 变量照抄规则头；否定写 `NOT 子目标`；不多写行 |
| 声明式事实（FP-07） | 一句一分 | 「One mark for each correctly completed clause」⟦9618_w23_32:11(a)⟧ | 全小写、句点结尾、参数顺序照库 |
| 类与类图（FP-05、FP-06） | 大半的分是“名字对上” | 「must use the identifiers used in the assignments」⟦9618_w22_31:11(b)⟧ | 属性名、setter / getter 名、参数名前后一致；setter 带参数与类型 |
| 递归追踪表（CT-12） | 按列、按深入 / 展开两段给分 | 「Call number column correct」⟦9618_s23_31:12(b)⟧ | 照 MS 的简化格式：先一路深入到基本情况，再逐层返回 |
| RPN 求值时栈的变化（SY-12） | MS 把栈的各个状态圈成几组，一组一分（一组可能包含好几步） | 「1 mark per ring」⟦9618_s22_31:5(b)(i)⟧；「Do not allow operators in stacks」⟦9618_s22_31:5(b)(i)⟧ | 每一步都画出栈；栈里只放数，运算符不进栈 |
| 逻辑表达式、卡诺图、BNF、语法图（BL、SY-07 至 SY-09） | 按子表达式、按圈、按产生式或连线给分 | 见各自题型卡 | 照题目给的名字与符号写，不多不少 |

最后一条通用提醒：**写代码题的分在得分点上，不在“程序能不能跑”上。** 一段几乎写对、只差一个 `ENDWHILE` 的代码，可能只丢一分；一段思路巧妙但漏了初值、关闭文件和返回的代码，可能丢掉一半。先拿稳声明、初值、收尾这些“骨架分”，再去挣中间的算法分。

### P3 常见命令词的作答要求

P3 出现最多的命令词依次是 Write、Describe、Complete、Explain、State、Identify、Outline、Draw、Calculate、Show。下表按“要你做什么 → 怎样拿分”排列，每个配一道真题。

| 命令词 | 要你做什么 | 怎样拿分 | 例 |
|:--|:--|:--|:--|
| Write（伪代码 / 声明） | 写出声明、语句或一段算法 | 按五环拿分；名字照抄；按 2027–29 指南写 | ⟦9618_w23_31:10(a)⟧ |
| Write（RPN / 浮点 / 子句 / 规则） | 写出一个表示或一句代码 | 格式就是分：RPN 的顺序、浮点的位数、子句的小写与句点 | ⟦9618_w25_33:7(b)⟧、⟦9618_s24_31:8(c)⟧ |
| Complete（伪代码 / 表 / 图） | 填满每一个空 | 一空或一行一分；用配对、对称、名字推出空行 | ⟦9618_s25_32:13⟧ |
| Describe | 说出特征，或过程的各个步骤 | 每点独立成句；过程题按顺序（链 2）；带 this 时套进题目的数据（链 8） | ⟦9618_w25_33:3⟧ |
| Explain | 说明原因、机制或怎样起作用 | 说法 → 展开（链 1）；原因 → 后果（链 6）；为什么合适（链 7） | ⟦9618_w25_32:12(b)⟧ |
| Outline | 简要列出要点，常需带一句展开 | 名字 + 一句作用；只列名字往往只拿一部分 | ⟦9618_w24_32:10(a)⟧ |
| State / Give / Name | 给出一个事实、名称或简短的一句 | 点数 = 分值；用 MS 的术语原词 | ⟦9618_w25_31:9(b)⟧、⟦9618_s23_32:7(b)⟧ |
| Identify | 认出并说出名称或特征 | 一个名称一分；后面跟 describe / state the purpose 时分在后半 | ⟦9618_w24_31:2⟧ |
| Define | 给术语下定义 | 用该领域的词，不用术语本身解释它（见 FP-04） | ⟦9618_w22_31:11(a)⟧ |
| Compare / Compare and contrast | 比较两样东西 | 成对写，X …, whereas Y …（链 3）；contrast 之外也可写相同点 | ⟦9618_w23_31:10(c)⟧ |
| Justify | 给一个选择提供理由 | 两边都要写：选的这个为什么好、另一个为什么不行（链 4） | ⟦9618_w23_32:9(b)⟧ |
| Calculate / Convert | 浮点数换算、最短距离、RPN 转中缀 | 写出过程与分段结果：浮点换算按步骤给分（⟦9618_s24_31:1(a)⟧），RPN 转中缀按子表达式给分（⟦9618_w25_32:8(b)⟧） | ⟦9618_s24_31:1(a)⟧、⟦9618_w25_32:8(b)⟧ |
| Show / Evaluate（RPN） | 画出栈在每一步的变化，或求出值 | 每一步画一个栈，只放数；MS 按圈出的一组组状态给分 | ⟦9618_s22_31:5(b)(i)⟧、⟦9618_s24_31:5(c)⟧ |
| Use（only the given instruction set） | 只用题给指令写汇编 | 动作分 + 标签分（见 FP-03） | ⟦9618_s22_31:9(b)⟧ |
| Draw | 画语法图、触发器电路、二叉树、连线 | 该有的连接都有、没有多余的；连线题看清是否多给了干扰项 | ⟦9618_w24_32:7(c)(i)⟧ |
| Tick | 每行勾一个框 | 按勾对的行数分档 | ⟦9618_w22_31:10(a)⟧ |

**分值就是要写的点数**：2 分题写两个独立点，4 分题写四个；把握不大时多写一个正确的点作保险；但同一个意思换说法只算一次（FP-04 的“对象与类的三点区别”就是这样丢分的），前后矛盾的说法也可能让那一点不给分。
