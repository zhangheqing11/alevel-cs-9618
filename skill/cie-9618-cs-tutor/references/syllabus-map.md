# 考纲节号 ↔ 卷 ↔ 教材章节 ↔ 官方辅助资料

考纲：2027–29 版（`sources/official/9618_syllabus_2027-2029.pdf`，与 2026 版相比只有措辞澄清）。教材：Langfield & Duddell《Computer Science for Cambridge International AS & A Level》第 2 版（2019，按 2021 起的 9618 考纲编写；`sources/textbooks/Langfield_Duddell_Coursebook_2e_2019.pdf`）。

**教材页码**：表中是印刷页码；**PDF 页 = 印刷页 + 6**（例如 Ch12 印刷第 178 页 = PDF 第 184 页）。读教材：

```bash
pdftotext -layout -f <PDF起> -l <PDF止> "$ALEVEL_CS_SOURCES/textbooks/Langfield_Duddell_Coursebook_2e_2019.pdf" -
```

Scheme of Work 的单元号与考纲大节号相同（Unit 1 = 第 1 节 …），所以表里不单列。

## 1. AS（P1：1–8 节；P2：9–12 节）

| 考纲 | 卷 | 教材 | 备注 |
|:--|:--|:--|:--|
| 1.1 Data Representation | P1 | Ch1 §1.01–1.04（3–16） | 二进制前缀、进制、BCD、补码、字符集 |
| 1.2 Multimedia（Graphics, Sound） | P1 | Ch1 §1.05–1.06（17–21） | 位图 / 矢量、声音采样 |
| 1.3 Compression | P1 | Ch1 §1.07（21–25） | 有损 / 无损、RLE |
| 2.1 Networks including the internet | P1 | Ch2（26–49）§2.01–2.09 | 比特流在 §2.07（40）；IP 在 §2.08（41） |
| 3.1 Computers and their components | P1 | Ch3（50–65）；监测与控制在 Ch7 §7.01–7.02（113–115） | 2027 考纲把监测与控制放在 3.1 |
| 3.2 Logic Gates and Logic Circuits | P1 | Ch4（66–79） | 门符号、真值表、电路、表达式 |
| 4.1 CPU Architecture | P1 | Ch5（80–90） | 寄存器传送记法 §5.07（88）、中断 §5.08（88） |
| 4.2 Assembly Language | P1 | Ch6 §6.01–6.06（91–103） | 两遍汇编 §6.04、寻址 §6.05 |
| 4.3 Bit manipulation | P1 | Ch6 §6.06 移位与位运算（98–103）；Ch7 §7.03（115） | 掩码控制设备 |
| 5.1 Operating Systems | P1 | Ch8 §8.01–8.04（122–127） | |
| 5.2 Language Translators | P1 | Ch8 §8.05–8.06（127–132） | IDE 功能 §8.06（129） |
| 6.1 Data Security | P1 | Ch9 §9.01–9.04（134–140） | |
| 6.2 Data Integrity | P1 | Ch9 §9.05（140–145） | 验证与核实 |
| 7.1 Ethics and Ownership | P1 | Ch10（146–156） | AI 的影响在 §10.06（153） |
| 8.1 Database Concepts | P1 | Ch11 §11.01–11.05（158–168） | ER 图、规范化 §11.05（165） |
| 8.2 DBMS | P1 | Ch11 §11.06（168） | |
| 8.3 DDL and DML | P1 | Ch11 §11.07（170–177） | SQL |
| 9.1 Computational Thinking Skills | P2 | Ch12 §12.01（179）、§12.09 模块（202） | 抽象、分解 |
| 9.2 Algorithms | P2 | Ch12 §12.02–12.08（180–201） | 标识符表、流程图、逐步求精 |
| 10.1 Data Types and Records | P2 | Ch13 §13.01–13.02（210–211）；Ch14 §14.03（248） | |
| 10.2 Arrays | P2 | Ch13 §13.03–13.05（212–225）；Ch14 §14.14（276） | 冒泡排序、线性查找 |
| 10.3 Files | P2 | Ch13 §13.06（226）；Ch14 §14.15（279） | 文本文件 |
| 10.4 Introduction to ADTs | P2 | Ch13 §13.07–13.10（227–238） | 栈、队列、链表（AS 只要求使用，不写伪代码） |
| 11.1 Programming Basics | P2 | Ch14 §14.01–14.04、§14.07（240–250、260） | 内置函数以当卷插页为准 |
| 11.2 Constructs | P2 | Ch14 §14.05–14.06（250–259）；Ch12 §12.06–12.07 | |
| 11.3 Structured Programming | P2 | Ch14 §14.08–14.13（262–275） | 参数传递 §14.10–14.12 |
| 12.1 Program Development Life Cycle | P2 | Ch15 §15.01（286） | |
| 12.2 Program Design | P2 | Ch15 §15.02–15.04（289–295） | 结构图、状态转换图 |
| 12.3 Program Testing and Maintenance | P2 | Ch15 §15.05–15.10（296–312） | 错误类型、测试方法、测试数据、维护类型 |

## 2. A Level（P3：13–20 节；P4：19–20 节，不含低级语言与声明式编程）

| 考纲 | 卷 | 教材 | 备注 |
|:--|:--|:--|:--|
| 13.1 User-defined data types | P3 | Ch16 §16.01（314） | 枚举、指针、集合、记录、类 |
| 13.2 File organisation and access | P3 | Ch16 §16.02（317–319）；Ch23 §23.11 哈希表（426） | 串行 / 顺序 / 随机、哈希 |
| 13.3 Floating-point numbers | P3 | Ch16 §16.03（320–328） | 规格化、精度与范围 |
| 14.1 Protocols | P3 | Ch17 §17.02–17.07（331–339） | TCP/IP 四层、HTTP / FTP / POP3 / IMAP / SMTP / BitTorrent |
| 14.2 Circuit switching, packet switching | P3 | Ch17 §17.01（330） | |
| 15.1 Processors, Parallel Processing and VMs | P3 | Ch18（340–349） | RISC / CISC、流水线、SISD…MIMD、虚拟机 |
| 15.2 Boolean Algebra and Logic Circuits | P3 | Ch19（350–366） | 半加器 / 全加器、触发器、布尔代数、卡诺图 |
| 16.1 Purposes of an OS | P3 | Ch20 §20.01–20.05（368–375） | 调度、分页、分段、抖动 |
| 16.2 Translation Software | P3 | Ch20 §20.06（375–385） | 编译阶段、BNF 与语法图、RPN |
| 17.1 Encryption, protocols, certificates | P3 | Ch21（386–396） | 对称 / 非对称、数字签名与证书、SSL / TLS、量子加密 |
| 18.1 Artificial Intelligence | P3 | Ch22（397–410） | 图、Dijkstra 与 A*（不要求写算法）、神经网络、机器学习 |
| 19.1 Algorithms | P3 + P4 | Ch23（411–433） | 查找、排序、ADT（链表、二叉树、栈、队列、图、字典）、Big O |
| 19.2 Recursion | P3 + P4 | Ch24（434–442） | |
| 20.1 Programming Paradigms：概述、命令式、OOP | P3 + P4 | Ch25（443–445）；OOP 在 Ch27（459–486） | |
| 20.1 低级语言编程 | **只 P3** | Ch28（487–497） | P4 不考 |
| 20.1 声明式编程（Prolog） | **只 P3** | Ch29（498–512） | P4 不考 |
| 20.2 File Processing and Exception Handling | P3 + P4 | Ch26（446–458） | P4 官方源文件只有文本文件；随机文件代码以 P3 / 伪代码为主 |

**使用教材时注意**

- 教材按 2021 起的考纲写，范围以 2027–29 考纲为准。讲某一小节前先对照考纲的「Candidates should be able to / Notes and guidance」，超出的内容标「拓展」。
- 教材的伪代码大体符合指南，但字符串函数等与当前插页不同处，以 2027–29 指南和当卷插页为准。
- 教材的 Python 示例只是一种写法；P4 的得分习惯看 MS 里的 Python 示例（例如用 `#int` 注释体现声明、私有属性 `self.__Name`）。
- 教材的 exam-style 题与示范答案是作者写的，不是官方 MS（教材扉页自己也这样声明）。

## 3. 范答与考官点评对应的卷

| 资料（`sources/official/support/`） | 对应的卷 | 内容 |
|:--|:--|:--|
| `9618_Example_Candidate_Responses_Paper_1_for_examination_from_2021.pdf` | `9618_s21_13` | 真实考生 high / middle / low + 考官逐点点评 |
| `…_Paper_2_…_2021.pdf` | `9618_s21_22` | 同上 |
| `…_Paper_3_…_2021.pdf` | `9618_s21_32` | 同上 |
| `…_Paper_4_…_2021.pdf` | `9618_s21_42` | 同上 |
| `9618_Example_Candidate_Responses_Paper_1_for_examination_from_2024.pdf` | `9618_s24_13` | 考官撰写的全卷范答 + 常见错误点评 |
| `…_Paper_2_…_2024.pdf` | `9618_s24_22` | 同上 |
| `…_Paper_3_…_2024.pdf` | `9618_s24_32` | 同上 |
| `…_Paper_4_…_2024.pdf` | `9618_s24_42` | 同上（含 Java / VB / Python 三种代码） |
| `9618_Specimen_Paper_Answers_Paper_<1\|2\|3>_for_examination_from_2021.pdf` | 2021 样卷 1 / 2 / 3（`sources/official/specimen/`） | 样卷范答 + 点评 |
| 考官报告 `sources/pastpapers/9618_<季><yy>_er.pdf` | 该季全部卷 | 按 `Paper 9618/<卷号>` 分段，段内 `Question n` 逐题点评 |

全部只用于易错与范答展示，给分只认该题自己的 MS。

## 4. 官方教学顺序（Scheme of Work，仅供参考）

AS 理论建议顺序：1 信息表示 → 3 硬件 → 4 处理器 → 2 通信 → 7 伦理 → 6 安全 → 5 系统软件 → 12 软件开发 → 8 数据库；9–11（算法、数据类型、编程）贯穿整个 AS。A Level：13 → 15 → 16 → 14 → 17 → 18；19–20 贯穿整个 A Level。

本系统的实际顺序以各卷 `taxonomy.json` 的章节顺序和 SKILL.md §3.4 为准（AS 先行、理论与编程交替）。
