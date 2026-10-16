## LG　逻辑门与逻辑电路：核心概念 {#core-LG}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Logic gate | A logic gate is an electronic component that performs a Boolean operation on one or more binary inputs to produce a single binary output.（非 MS 原句） | 对一个或多个二进制输入做布尔运算、产生一个二进制输出的电子元件 | 一个只认 0 和 1 的小开关盒 | P1-LG-01 |
| NOT | The output is the opposite of the input.（非 MS 原句） | 一个输入，输出取反 | 唱反调 | P1-LG-01 |
| AND | The output is 1 only when both inputs are 1.（非 MS 原句） | 两个输入都为 1 时输出 1 | 两个开关串联：都合上灯才亮 | P1-LG-01 |
| OR | 「The output is 0 when both inputs are 0, otherwise the output is 1」⟦9618_s24_12:1(a)⟧ | 至少一个输入为 1 时输出 1 | 两个开关并联：合上任一个灯就亮 | P1-LG-01 |
| NAND | 「The output is 0 when both inputs are 1, otherwise the output is 1」⟦9618_s24_12:1(a)⟧ | AND 的结果取反：只有两个输入都为 1 时输出 0 | “不是两个都同意”就通过 | P1-LG-01 |
| NOR | 「The output is 1 when both inputs are 0, otherwise the output is 0」⟦9618_s24_12:1(a)⟧ | OR 的结果取反：只有两个输入都为 0 时输出 1 | “谁都没按”才亮 | P1-LG-01 |
| XOR | 「Output is only 1 if both inputs are different」⟦9618_w24_13:1(a)⟧ | 两个输入不同时输出 1，相同时输出 0 | 楼梯两头的开关：拨任一个都会改变灯的状态 | P1-LG-01 |
| Truth table | A table that shows the output for every possible combination of inputs.（非 MS 原句） | 列出所有输入组合及其对应输出的表；n 个输入有 2ⁿ 行 | 把所有情况试一遍的清单 | P1-LG-01、P1-LG-04、P1-LG-05 |
| Working space | 「1 mark for first 4 rows, 1 mark for second 4 rows」⟦9618_s25_11:1(b)⟧ | 真值表旁写中间结果（每个门一列）的区域；本身不计分，分数按输出列的行组给 | 竖式里的进位草稿 | P1-LG-04 |
| Logic expression | 「X = (A AND B) XOR (NOT C AND B)」⟦9618_s22_13:7(a)⟧ | 用输入字母、门名（AND、OR、NOT、NAND、NOR、XOR）和括号写出的输出与输入的关系 | 电路的“文字版” | P1-LG-02、P1-LG-03、P1-LG-05、P1-LG-06 |
| Bracketing | 「XOR (with remainder correct and bracketed and nothing extra)」⟦9618_s22_13:7(a)⟧ | 每个门的结果整体加括号，使表达式的运算层次与电路一致 | 括号就是电路里的一根导线把一块结果送进下一个门 | P1-LG-03 |
| Logic circuit | 「correct OR and NOT gates with correct inputs and no superfluous gates」⟦9618_s24_12:1(b)⟧ | 用门符号和连线表示表达式；除 NOT 外每门两输入，不加多余的门 | 套娃摆开：里层靠输入，外层靠输出 | P1-LG-02、P1-LG-03 |
| Sum of products | 「Q = (R AND S AND NOT T) OR (NOT R AND NOT S AND T)」⟦9618_w25_11:3(b)⟧ | 对真值表里每个输出为 1 的行写一个 AND 项（0 的输入加 NOT），再用 OR 连起来 | 点名：列出每一种会亮灯的情况 | P1-LG-05 |
| Parameter table | 「Y = E AND (B OR C OR D)」⟦9618_w24_11:5(b)⟧ | 情境题里规定每个输入取 1、取 0 各代表什么条件的表；条件对应 0 时要写 NOT | 翻译词典：把文字条件翻成字母 | P1-LG-06 |
