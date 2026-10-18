## BL　布尔代数与逻辑电路：核心概念 {#core-BL}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。本章 MS 的表达式在抽取文本里丢了横线，所以表达式类词条一律写成“非 MS 原句”，并用 A̅ 表示 NOT A。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Truth table (working) | 「One mark for working, all four columns P, Q, R and S」⟦9618_s24_31:6(a)⟧ | 列出所有输入组合下各中间结点与输出的值；Working space 的中间列算过程分 | 给电路拍 8 张（或 16 张）快照 | P3-BL-01 |
| Three-input gate | 非 MS 原句：A three-input AND gate outputs 1 only when all three inputs are 1; a three-input OR / NOR gate looks at all three inputs together | 一个门有三个输入，三个输入一起参与运算 | 三把钥匙同时转才开的锁（AND） | P3-BL-01 |
| Half adder | 「Half adder」⟦9618_s22_32:6(b)(i)⟧ | 把两个 1 位二进制数相加的电路，输出和位（XOR）与进位（AND） | 手算 1 + 1：写 0 进 1 | P3-BL-02 |
| Full adder | 「Full adder」⟦9618_s21_31:7(b)⟧ | 把两个位与低位送来的进位相加的电路，三个输入、两个输出（和位、进位输出） | 能接住上一位进位的加法器，可串成多位加法 | P3-BL-02 |
| Sum bit | 「Purpose: Sum bit」⟦9618_s21_31:7(c)⟧ | 加法结果的本位；输入中有奇数个 1 时为 1 | 竖式里“这一位写几” | P3-BL-02 |
| Carry | 「Purpose: Carry output」⟦9618_s21_31:7(c)⟧ | 送往高一位的进位；半加器在两个输入都为 1 时为 1，全加器在至少两个输入为 1 时为 1 | 竖式里“往前进 1” | P3-BL-02 |
| Flip-flop | 「To store a binary digit / (single) bit」⟦9618_w22_32:8(b)⟧ | 能保持一个二进制位的时序电路，是寄存器、存储器的基本单元 | 一个能记住开或关的开关 | P3-BL-03 |
| SR flip-flop | 非 MS 原句：An SR flip-flop is made from two NAND gates or two NOR gates, with the output of each gate fed back as an input to the other; its inputs are Set and Reset | 两个同种门（NAND 或 NOR）交叉反馈；S 置 1、R 置 0、都不动时保持；NOR 版 S = R = 1 为无效状态 | 两个人互相拉着手，一方的状态锁住另一方 | P3-BL-03 |
| JK flip-flop | 非 MS 原句：A JK flip-flop has inputs J, K and a clock; when J = K = 1 the output toggles, so there is no invalid state | 带时钟的触发器；J = K = 0 保持，J = 1 置位，K = 1 复位，J = K = 1 翻转 | 修好了 SR“两键同按就乱”的毛病 | P3-BL-03 |
| Sum-of-products | 非 MS 原句：one product (AND) term for each row of the truth table whose output is 1, joined by OR (+) | 积之和：每个输出为 1 的行写一个积项（为 0 的输入取反），用 + 连起来 | 把“灯亮的情况”一条条列出来 | P3-BL-04 |
| Karnaugh map (K-map) | 「It is guaranteed to give you an optimal solution」⟦9618_s26_31:6(b)⟧ | 把真值表排成方格，行列按格雷码，使相邻格只差一个变量，用来圈组化简 | 把真值表折成一张方格纸 | P3-BL-05、P3-BL-06 |
| Gray code order | 非 MS 原句：K-map rows and columns are labelled 00, 01, 11, 10 so that adjacent cells differ by one variable | 卡诺图行列的排列顺序，相邻两个只差一位 | 第三列是 11，不是 10 | P3-BL-05 |
| Loop / group | 「One mark for each correct loop (Max 2)」⟦9618_w24_31:7(c)⟧ | 圈住 2 的幂个相邻的 1（矩形，可绕边、可重叠），圈尽量大、个数尽量少 | 找“不管某开关怎么拨都亮”的区域 | P3-BL-06 |
| Simplified sum-of-products | 「Boolean terms and operator correct and no other terms present」⟦9618_w24_31:7(d)(i)⟧ | 每个圈写一项（只留圈内不变的变量），用 + 连接；孤立的 1 也要写成完整项 | 每个圈浓缩成一句话 | P3-BL-06 |
| De Morgan’s laws | 非 MS 原句：NOT(A.B) = A̅ + B̅ and NOT(A + B) = A̅.B̅ | 对积取反等于各自取反后相或；对和取反等于各自取反后相与 | 横线断开，符号变号 | P3-BL-07 |
| Double negation law | 非 MS 原句：NOT(NOT A) = A | 两次取反抵消 | 负负得正 | P3-BL-07 |
| Distributive law | 非 MS 原句：A.(B + C) = A.B + A.C | 展开或提公因式 | 像代数里的乘法分配律 | P3-BL-07 |
| Absorption law | 非 MS 原句：A + A.B = A and A.(A + B) = A | 一项被包含它的更短项“吸收” | 已经说了“A 就亮”，再加“A 且 B 也亮”是废话 | P3-BL-07 |
| Redundancy law | 非 MS 原句：A + A̅.B = A + B | 与 A 同时或的项里，A̅ 是多余的 | A 不成立时才轮到看 A̅.B，A̅ 本来就成立 | P3-BL-07 |
| Simplest form | 「One mark for simplest form (Max 1)」⟦9618_s23_31:7(d)⟧ | 用布尔代数把化简积之和再提公因式，得到项与变量最少的写法 | 把两句有共同主语的话合成一句 | P3-BL-07 |
