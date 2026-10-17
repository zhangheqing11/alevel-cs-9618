## IR　信息表示 {#ch-IR}

<!-- auto:chapter-stats -->

### 核心思想

计算机里只有 0 和 1。这一章回答一个问题：**数字、文字、图片、声音怎样变成一串位，以及这串位多大、能不能变小**。题型按这条线排开：

1. **位能表示什么**（IR-01）：n 位有 2ⁿ 种组合；KiB/MiB 按 1024 进，kB/MB 按 1000 进。后面所有计算都用到它。
2. **整数**（IR-02 至 IR-05）：同一串位可以读成无符号数、BCD、补码，读法不同值就不同；然后在这些表示上做加减，结果装不下就是溢出。
3. **文字**（IR-06）：字符集给每个字符一个唯一编码，文本就是编码按顺序排好。
4. **图像**（IR-07 至 IR-09）：位图 = 像素 × 每像素的位数；矢量图 = 一张“怎么画”的清单。
5. **声音**（IR-10、IR-11）：按固定间隔量振幅，每次量到的值存成一个二进制数。
6. **算大小**（IR-12）：把 4、5 的“每个单位几位 × 有多少单位”乘起来，再换单位。
7. **压缩**（IR-13 至 IR-15）：为什么压（IR-13）→ 选有损还是无损（IR-14）→ 具体怎么压（IR-15）。

本章有多类计算题，全部手算（禁用计算器），所以每道计算题都要写出 working：MS 普遍“1 mark for working, 1 mark for answer”，答案错了 working 仍可能得分。

### 题型树
<!-- auto:type-tree -->

### P1-IR-01　二进制量级与单位前缀　{#P1-IR-01}

<!-- auto:stats P1-IR-01 -->

**考法**　三种问法：①说出二进制前缀（kibi/mebi/gibi/tebi）与十进制前缀（kilo/mega/giga/tera）的一个区别；②填空换算（3 KiB = ? bytes，2 TB = ? GB）或在混合单位里挑最大的文件；③“n 位能表示几个不同值”“存这个数据最少要几位”——后者常做成一张勾选表，把十六进制数、颜色数、振幅数、IPv4/IPv6 地址混在一起（⟦9618_w25_13:2(a)⟧）。

**识别信号**　kibibyte / mebibyte / gibibyte / tebibyte 与 kilobyte / megabyte… 同时出现；binary prefix / denary (decimal) prefix；State the number of unique binary values that can be represented in n bits；minimum number of bits used to store each example of data。

**解题思路**
1. 前缀区别题：写成**一对**——“二进制前缀按 1024（2¹⁰）进，十进制前缀按 1000（10³）进”，最好再带一个具体数值的例子。
2. 换算题：二进制前缀每级 ×1024（1 KiB = 1024 B，1 MiB = 1024 KiB）；十进制前缀每级 ×1000。跨类比较时先全部换成 bytes 再比。
3. n 位有 **2ⁿ** 个不同值：8 位 256 个，16 位 65 536 个。
4. “最少几位”：找最小的 n 使 2ⁿ ≥ 需要表示的个数（无符号最大值 m 时找 2ⁿ > m）。十六进制每位 = 4 位；IPv4 固定 32 位，IPv6 固定 128 位。
5. 无符号 n 位的范围是 0 至 2ⁿ − 1（8 位：0–255）；补码的范围归 IR-03。

**得分表述**（引自对应 MS）
- 「Kibibyte is 1024 bytes and kilobyte is 1000 bytes」⟦9618_s23_11:3(d)(i)⟧
- 「Kibibyte is binary prefix and kilobyte is denary prefix」⟦9618_s23_11:3(d)(i)⟧
- 「one tebibyte is 1024 gibibytes and one terabyte is 1000 gigabytes」⟦9618_s22_11:1(a)⟧
- 「kibi is binary prefix and mega is denary prefix」⟦9618_w23_12:3(a)⟧
- 「A kibibyte has a binary prefix. Three kibibytes is the same as 3072 bytes」⟦9618_s24_13:1(a)⟧

**易错与失分**
- 只写“kibibyte is bigger”不给分：MS 要的是 1024 对 1000，或 binary 对 denary 这两组对比之一，两边都要写。
- 两个单位**不同级**时（⟦9618_w23_12:3(a)⟧ 比 kibibyte 与 megabyte、⟦9618_w24_11:1(a)⟧ 比 tebibyte 与 gigabyte）别硬套“1024 vs 1000”——要么各写各自的字节数，要么只写“kibi 是二进制前缀、mega 是十进制前缀”。
- 混合单位比大小（⟦9618_s24_12:7(a)⟧）：3300 KiB = 3 379 200 B，比 3 MiB = 3 145 728 B 大——只看数字前面的 3 会选错。
- “最少几位”看的是**个数**还是**最大值**：256 个颜色要 8 位（2⁸ = 256），但无符号数 256 要 9 位。

#### 代表题精讲　⟦9618_s24_13:1(a)⟧

**在考什么**　4 分填空，每空 1 分：两个前缀的类别 + 两个换算。考的是你是否把“kibi = 2¹⁰”和“mega = 10⁶”分清。

**完整作答**
- kibibyte 的 kibi 是 binary prefix → 第 1 空 **binary**。
- 3 KiB = 3 × 1024 = **3072** bytes。
- megabyte 的 mega 是十进制前缀 → **denary / decimal**（MS 两词都接受）。
- terabyte 与 gigabyte 都是十进制前缀，相差 1000 倍：2 TB = 2 × 1000 = **2000** GB。

**与 MS 对齐**　MS 四个得分点依次是 binary、3072、denary/decimal、2000，每空独立给分；第 2 空若写 3000（按 1000 算）只丢这一分。

**英文作答句**　A kibibyte has a binary prefix. Three kibibytes is the same as 3072 bytes. A megabyte has a denary prefix. Two terabytes is the same as 2000 gigabytes.

**直观**　二进制前缀是给“内存按 2 的幂造”量身定的尺子，十进制前缀是 SI 通用尺子；同一个“千”，一个是 1024，一个是 1000。

**下一道变式**　⟦9618_w25_13:2(a)⟧　（换成“最少几位”勾选表，6 行里混着十六进制数、振幅个数、IP 地址；讲解时请对照原卷 QP p.3 的表格。）

<!-- auto:drills P1-IR-01 -->

### P1-IR-02　进制转换（无符号与 BCD）　{#P1-IR-02}

<!-- auto:stats P1-IR-02 -->

**考法**　本章最常考的题型，几乎每卷都有。①单个转换：二进制 → 十进制 / 十六进制，十六进制 → 十进制，十进制 → BCD，BCD → 十进制，常 1 分一问；②带“Show your working”的 2 分转换（working 1 分 + 答案 1 分）；③填表：同一个数在 denary / binary / hexadecimal / BCD 各列之间补空，有时套在字符码值的情境里（码值已给）；④说明一串位为什么不是合法 BCD。

**识别信号**　Convert the unsigned binary integer / hexadecimal number / denary number into …；Binary Coded Decimal (BCD)；Complete the table by calculating the missing values；Show your working。

**解题思路**
1. **二进制 → 十六进制**：从右往左每 4 位一组（不够左边补 0），每组换成 0–F。
2. **十六进制 → 十进制**：位权 16² = 256、16¹ = 16、16⁰ = 1；或先展开成二进制再按位权加。
3. **二进制 → 十进制**：把为 1 的位的位权（128, 64, 32, 16, 8, 4, 2, 1…）加起来。
4. **十进制 → 二进制 / 十六进制**：从最大位权往下减；或反复除以 16 取余数。
5. **BCD**：十进制的**每一位数字**单独写成 4 位；读 BCD 时反过来每 4 位读一个数字。BCD 不是“把整个数换成二进制”。
6. 无符号二进制 → BCD：先换成十进制，再逐位写 BCD——working 就写这两步。
7. 交卷前回代检查：十六进制答案再换回二进制，看是否与题目一致。

**得分表述**（引自对应 MS）
- 「1100 0000 1111 // 2048 + 1024 + 8 + 4 + 2 + 1」⟦9618_s24_12:7(c)⟧
- 「A04 = (10 * 256) + 4」⟦9618_s23_12:4(c)⟧
- 「Dividing by 16 // converting to binary (11111011)」⟦9618_s22_11:1(c)⟧
- 「149 decimal」⟦9618_w22_12:2(a)(iii)⟧
- 「The denary value in each group of 4 bits is greater than 9」⟦9618_w21_12:4(d)⟧

**易错与失分**
- “Show your working”的题只写答案：最多 1 分。MS 接受的 working 很宽（位权相加式、展开成二进制、除以 16），写出任何一种即可。
- BCD 与无符号二进制混淆：149 的二进制是 1001 0101，BCD 是 0001 0100 1001。
- BCD 每个数字必须写满 4 位：108 → 0001 0000 1000，中间的 0 写成 0000 不能省（⟦9618_w25_11:1(a)(ii)⟧）。
- 十六进制分组从**右**开始：101100111010 → 1011 0011 1010 → B3A。
- 要求 12 位二进制时补足前导 0（⟦9618_s25_12:2(a)⟧：558 → 0010 0010 1110）。

#### 代表题精讲　⟦9618_s24_12:7(c)⟧

**在考什么**　Convert the hexadecimal number C0F into denary. Show your working. 2 分 = working 1 分 + 答案 1 分。

**完整作答**（两条路都给出，考试写一条即可）
- 位权法：C0F = 12 × 16² + 0 × 16 + 15 = 12 × 256 + 15 = 3072 + 15 = **3087**。
- 二进制法：C = 1100，0 = 0000，F = 1111 → 1100 0000 1111 → 2048 + 1024 + 8 + 4 + 2 + 1 = 3087。
- 合理性检查：C00 已是 3072，再加 F（15）就是 3087，数量级对。

**与 MS 对齐**　working 一分：MS 列了 `1100 0000 1111`、位权相加式、`(12 * 16 * 16) + 15`、`3072 + 15` 等多种写法，写出其一即得；答案一分：3087。

**英文作答句**　Working: C0F = (12 × 256) + (0 × 16) + 15 = 3072 + 15. Answer: 3087.

**下一道变式**　⟦9618_w22_12:2(a)(iii)⟧　（无符号二进制 → BCD，working 要写出中间的十进制。）

<!-- auto:drills P1-IR-02 -->

### P1-IR-03　有符号整数：补码与反码　{#P1-IR-03}

<!-- auto:stats P1-IR-03 -->

**考法**　①补码 → 十进制（8 位或 12 位，常 1 分）；②负十进制 → n 位补码；③说明转换方法并给出结果（3 分：方法 2 + 结果 1）；④n 位补码能表示的最小、最大值（写成二进制或十进制）；⑤偶尔考反码（one's complement）。

**识别信号**　two's complement / one's complement；signed denary value −…；smallest / largest … two's complement … 8 / 12 / 16 bits；Explain how to convert the two's complement integer … into denary。

**解题思路**
1. **先看最高位**：0 → 正数，直接按无符号读；1 → 负数，用下面任一方法。
2. **方法 A（取反加一）**：每位取反、再加 1，得到它的绝对值，前面加负号。
3. **方法 B（负位权）**：最高位的位权当作负数（8 位 −128，12 位 −2048，16 位 −32768），其余位照常相加。
4. **十进制负数 → 补码**：先写出绝对值的 n 位二进制，再取反加一（或：从右往左照抄到第一个 1，左边全部取反）。
5. **范围**：n 位补码最小 = 1 后跟 n−1 个 0（−2ⁿ⁻¹），最大 = 0 后跟 n−1 个 1（2ⁿ⁻¹ − 1）。8 位：1000 0000（−128）到 0111 1111（+127）。
6. **反码**：负数 = 正数的每位取反，不加 1（−120：0111 1000 → 1000 0111）。

**得分表述**（引自对应 MS）
- 「Flip each bit then add 1」⟦9618_w24_13:8(b)⟧
- 「Most significant 1 bit is treated as the corresponding negative denary value」⟦9618_w24_13:8(b)⟧
- 「add the other positive corresponding denary values」⟦9618_w24_13:8(b)⟧
- 「Smallest: 1000 0000」⟦9618_s25_12:2(b)(ii)⟧
- 「Largest: 0111 1111」⟦9618_s25_12:2(b)(ii)⟧
- 「Working: +120 = 0111 1000」⟦9618_s23_12:4(b)⟧

**易错与失分**
- 取反加一之后忘了写负号：结果是 −97，不是 97。
- 补码最大值写成 1111 1111：那是 −1；最大值的最高位必须是 0。
- 12 位、16 位题按 8 位做：位数由题目决定，最高位的负位权跟着变（12 位是 −2048）。
- 反码与补码混用：题目写 one's complement 就只取反，不加 1。
- “Explain how to convert”的方法分要写**步骤**（flip、add 1、convert to denary），只写结果只得结果分。

#### 代表题精讲　⟦9618_w24_13:8(b)⟧

**在考什么**　Explain how to convert the two's complement integer 10011111 into denary, and give the value. 3 分：方法最多 2 分 + 正确结果 1 分。

**完整作答**
- 最高位是 1 → 负数。
- 方法 A：取反 10011111 → 01100000；加 1 → 01100001 = 64 + 32 + 1 = 97；所以值是 **−97**。
- 方法 B（核对）：−128 + 16 + 8 + 4 + 2 + 1 = −128 + 31 = −97。两种方法一致。

**与 MS 对齐**　MS 的方法分有两组，每组两点：①“Flip each bit then add 1”+“… method of converting the new binary number into denary”；②“Most significant 1 bit is treated as the corresponding negative denary value”+“… add the other positive corresponding denary values”。写清任一组的两步即得 2 分；第 3 分是 −97。

**英文作答句**　The most significant bit is 1, so the number is negative. Flip each bit (01100000) then add 1 (01100001), and convert this binary number into denary (97). The denary value is −97.

**直观**　8 位寄存器只有 256 个格子；补码把其中一半（最高位为 1 的那些）留给负数，−x 放在“再走 x 步就回到 0”的位置，所以取反加一正好算出 256 − x（详见 few-shots 示例 1）。

**下一道变式**　⟦9618_w23_12:3(b)(i)⟧　（反方向：−196 → 12 位补码。）

<!-- auto:drills P1-IR-03 -->

### P1-IR-04　BCD 与十六进制的应用　{#P1-IR-04}

<!-- auto:stats P1-IR-04 -->

**考法**　“应用 + 理由”两栏：说出 BCD 用在哪里并论证（2 分：应用 1 + 对应理由 1）；或直接列两个使用 BCD 的好处。核验语料只出现过 BCD，未考十六进制的应用。

**识别信号**　Identify / Give one (practical) application where BCD is used and justify its use；State two benefits of using Binary Coded Decimal (BCD)；Application … Justification。

**解题思路**
1. 选一个 MS 反复出现的应用：**金融/银行计算**、**电子显示（计算器、数字时钟）**、**PC BIOS 里存日期时间**。
2. 理由必须**对应**所选应用：金融 → 十进制小数在普通二进制里不能精确表示、BCD 能精确表示金额、不会累积舍入误差；显示 → 显示器只需逐个数字显示、BCD 与十进制互转简单。
3. “好处”题：①与十进制互转简单；②便于数字设备显示；③能精确表示金额。

**得分表述**（引自对应 MS）
- 「An application that performs financial / banking calculations」⟦9618_w23_12:3(c)⟧
- 「because it is difficult to represent decimal values exactly in normal binary」⟦9618_w23_12:3(c)⟧
- 「Electronic displays, e.g. calculators, digital clocks」⟦9618_w23_12:3(c)⟧
- 「because visual displays only need to show individual digits」⟦9618_w23_12:3(c)⟧
- 「straightforward to convert to / from BCD and denary」⟦9618_w22_13:9(b)⟧
- 「can represent monetary values exactly」⟦9618_w22_13:9(b)⟧

**易错与失分**
- 理由与应用不配对：写“digital clock”却用金融的理由，理由分拿不到（MS 写的是 1 mark for a **corresponding** justification）。
- 只写“BCD is easier”太空泛：要说清“与十进制互转更简单”或“每个十进制数字单独编码，显示时直接逐位输出”。

#### 代表题精讲　⟦9618_w23_12:3(c)⟧

**在考什么**　Identify one practical application of BCD and justify why BCD is used in this application. 2 分：应用 1 + 理由 1。

**完整作答**　选金融：银行软件做金额计算时，0.10 这样的十进制小数在普通二进制里只能近似存储，反复计算会累积误差；BCD 把每个十进制数字单独存成 4 位，金额可以精确表示。

**与 MS 对齐**　应用分 ←“An application that performs financial / banking calculations”；理由分 ←“because it is difficult to represent decimal values exactly in normal binary and financial transactions use only two decimal places and must be accurate, no accumulating errors”。

**英文作答句**　Application: a banking application that performs financial calculations. Justification: it is difficult to represent decimal values exactly in normal binary, but financial transactions must be accurate to two decimal places, so BCD avoids accumulating rounding errors.

**下一道变式**　⟦9618_w22_13:9(b)⟧　（不给应用，直接列两个好处。）

<!-- auto:drills P1-IR-04 -->

### P1-IR-05　二进制加减法与溢出　{#P1-IR-05}

<!-- auto:stats P1-IR-05 -->

**考法**　①8 位或 12 位二进制加法（常要求 Show your working / Include any overflow bit(s)），偶有三个数相加；②二进制减法：题目给十进制或二进制，用“直接借位”或“加上补码”都可以；③溢出：说出它是什么、为什么会发生，或“Name and describe the error”。

**识别信号**　Add / Perform / Complete the following binary addition. Show your working；Subtract … using binary subtraction；Include any overflow bit(s)；State what is meant by an overflow；Name and describe the error that can occur。

**解题思路**
1. 竖式对齐，从右往左逐位：0+0=0、1+0=1、1+1=10（写 0 进 1）、1+1+1=11（写 1 进 1）。**进位写在上一列下方或上方**——这就是 working。
2. 结果超出位数时，把最左边多出的进位单独标出，写“overflow”。
3. 减法 A − B，二选一：
   - 加补码：B 取反加一得 −B，再 A + (−B)，丢掉最高位外的进位。
   - 直接借位：逐位相减，不够减向左借 1（借来的是 2）。
4. 题目给十进制时，先把两个数换成 8 位二进制——MS 常把“转换”单列 1 分。
5. 溢出的判断：结果需要的位数超过寄存器位数；补码时看“两个正数相加得负数 / 两个负数相加得正数”。

**得分表述**（引自对应 MS）
- 「Working – carried values clearly indicted」⟦9618_s24_11:7⟧
- 「Overflow clearly indicated as overflow」⟦9618_s24_11:7⟧
- 「Subtraction method - converting 10 to – 10 and adding // direct subtraction」⟦9618_s24_12:7(b)⟧
- 「An overflow error occurs」⟦9618_w25_11:1(b)(ii)⟧
- 「The answer cannot be represented in the number of bits available」⟦9618_w24_11:1(d)⟧
- 「The answer is larger than the maximum positive number that can be stored in the register」⟦9618_w24_11:1(d)⟧

**易错与失分**
- 不写进位：“Show your working”的题只写答案丢 working 分。
- 用补码做减法时把丢掉的第 9 位当成溢出：在补码加法里那个进位是正常现象，不是溢出（few-shots 示例 1）。
- 溢出的定义写成“the number is too big”太含糊：要说“cannot be represented in the number of bits available”或“larger than the maximum that can be stored in the register”。
- 三个数相加时一列可能出现 1+1+1+进位：逐列写清和与进位，别心算跳步。

#### 代表题精讲　⟦9618_s24_12:7(b)⟧

**在考什么**　Subtract the denary number 10 from the denary number 100 using binary subtraction. Show your working. 3 分：转换 1 + 方法 1 + 答案 1。

**完整作答**
- 转换：100 = 0110 0100，10 = 0000 1010。
- 方法（加补码）：+10 = 0000 1010 → 取反 1111 0101 → 加 1 → −10 = 1111 0110。
```
   0110 0100      (100)
 + 1111 0110      (−10)
 -----------
 1 0101 1010      → discard the 9th bit → 0101 1010
```
- 答案 **0101 1010**（= 64 + 16 + 8 + 2 = 90，检查 100 − 10 = 90 ✓）。

**与 MS 对齐**　①“Converting 100 to binary 0110 0100 and 10 to binary 0000 1010”；②“Subtraction method - converting 10 to – 10 and adding // direct subtraction”——写出 −10 = 1111 0110 并相加即得；③“correct answer 0101 1010”。

**英文作答句**　100 = 0110 0100 and 10 = 0000 1010. −10 in two's complement is 1111 0110. 0110 0100 + 1111 0110 = (1) 0101 1010; the carry out of the 8th bit is discarded. Answer: 0101 1010.

**下一道变式**　⟦9618_s24_11:7⟧　（三个 8 位数相加，结果溢出，要标出溢出位。）

<!-- auto:drills P1-IR-05 -->

### P1-IR-06　字符集　{#P1-IR-06}

<!-- auto:stats P1-IR-06 -->

**考法**　①字符集是什么；②一个单词/一段文字怎样用字符集表示成二进制（2 分）；③ASCII、扩展 ASCII、Unicode 各用几位、能表示多少字符；④两者的相同点、不同点，Unicode 相对 ASCII 的优点；⑤利用码值连续推出另一个字符的码（已知 '1' 是 49，求 '5'）。

**识别信号**　character set / ASCII / extended ASCII / Unicode；Explain how the word '…' is represented by a character set；differences / advantages … Unicode … ASCII；number of bits each character set allocates。

**解题思路**
1. “怎样表示”两步骨架：**每个字符有唯一的二进制码** → **文本中的字符按顺序替换成码并依次存储**。
2. 位数与字符数：ASCII 7 位（128 个）；扩展 ASCII 8 位（256 个）；Unicode 可用 16 或 32 位（MS 也接受 8/16/32），能表示所有语言的字符和 emoji。
3. 不同点成对写：“Unicode … whereas ASCII …”——位数、字符范围、多语言。
4. 相同点：都给每个字符唯一编码；Unicode 包含 ASCII 的全部字符（ASCII 是 Unicode 的子集）。
5. 码值连续：数字字符 '0'–'9' 与字母各自按顺序编码，'5' 的码 = '1' 的码 + 4。

**得分表述**（引自对应 MS）
- 「All of the characters/symbols that the computer can use/represent」⟦9618_s22_13:1(a)(i)⟧
- 「Each character has a unique binary code」⟦9618_s24_13:1(d)(ii)⟧
- 「The binary code for each character is stored in sequence」⟦9618_s24_13:1(d)(ii)⟧
- 「Unicode can represent a wider range of characters than ASCII」⟦9618_w22_11:1(c)⟧
- 「Unicode will contain all the characters that ASCII contains // ASCII is a subset of Unicode」⟦9618_w22_11:1(c)⟧

**易错与失分**
- 只写“each character is converted to binary”而没说**唯一**编码、**按顺序**存放：两个得分点各差一个限定词。
- 位数写错：ASCII 是 7 位，扩展 ASCII 才是 8 位（⟦9618_s24_13:1(d)(i)⟧ 三格全对才给 1 分）。
- 不同点只写一边：“Unicode uses more bits”要配上“ASCII uses 7 or 8 bits”更稳。
- 码值已给、只做进制转换的题属于 IR-02，不要在那里展开字符集原理。

#### 代表题精讲　⟦9618_w22_11:1(c)⟧

**在考什么**　Give one similarity and two differences between the ASCII and Unicode character sets. 3 分：相同点 1 + 不同点 2。

**完整作答**
- 相同点：两者都用一个唯一的编码表示每个字符；而且 Unicode 包含 ASCII 的全部字符。
- 不同点 1：Unicode 每个字符最多可用 32 位，ASCII 只用 7 或 8 位。
- 不同点 2：Unicode 能表示的字符范围更广，包括不同语言的文字；ASCII 只覆盖一种语言（英文拉丁字母）。

**与 MS 对齐**　相同点从“both can use 8 bits”“both represent each character using a unique code”“Unicode will contain all the characters that ASCII contains // ASCII is a subset of Unicode”中任取一条；不同点从“Unicode can go up to 32 bits per character whereas ASCII is 7 or 8 bits”“Unicode can represent a wider range of characters than ASCII”“different languages are represented using Unicode, ASCII is only for one language”中取两条。

**英文作答句**　Similarity: both represent each character using a unique code. Difference 1: Unicode can go up to 32 bits per character whereas ASCII is 7 or 8 bits. Difference 2: Unicode can represent characters from different languages, whereas ASCII is only for one language.

**下一道变式**　⟦9618_s24_13:1(d)(ii)⟧　（换成“Explain how the word 'Clock' is represented”。）

<!-- auto:drills P1-IR-06 -->

### P1-IR-07　位图编码与术语　{#P1-IR-07}

<!-- auto:stats P1-IR-07 -->

**考法**　①描述/解释位图怎样编码（3 分骨架题，近几年反复出现）；②术语定义：pixel、colour depth / bit depth、image resolution、screen resolution、file header（填表、连线或直接定义）；③文件头里还存什么；④为什么实际文件比算出来的大。

**识别信号**　Describe / Explain how the data for a bitmapped image is encoded；Define / Complete the table by defining；pixel / colour depth / bit depth / image resolution / file header；Identify … other items that could be included in the file header；Explain why the actual file size may be larger。

**解题思路**
1. 编码题的四点骨架（按顺序写）：图像由**像素**组成 → 每个像素**一种颜色** → 每种颜色有**唯一的二进制码** → 每个像素的颜色码**按顺序**存储。
2. 定义题背 MS 原句（见下方得分表述与概念表），每个定义里的限定词不能丢：colour depth 是“每个像素/每种颜色用几位”。
3. image resolution = 图像宽 × 高的像素数；screen resolution = 屏幕能显示的宽 × 高像素数。
4. 文件头里的项目：文件类型、文件大小、图像尺寸、色深、分辨率、压缩类型、像素数据的偏移位置。题目已经给出的项不能再写。
5. “为什么比算的大”：文件还有 header / metadata。

**得分表述**（引自对应 MS）
- 「Image is made of pixels and each pixel has one colour」⟦9618_s24_12:2(d)(i)⟧
- 「Each colour has a unique binary code」⟦9618_s24_12:2(d)(i)⟧
- 「Code for the colour of each pixel is stored in sequence」⟦9618_s24_12:2(d)(i)⟧
- 「the number of bits used to represent a colour」⟦9618_w24_12:7(a)(i)⟧
- 「stores data about the image file / metadata」⟦9618_w24_12:7(a)(i)⟧
- 「The file will have a header」⟦9618_w25_11:7(d)(ii)⟧

**易错与失分**
- 编码题写成“the image is stored in binary”——太空，四个得分点一个都没扣上。
- 把 colour depth 写成“the number of colours”：MS 主句是“number of bits”，“number of colours that can be represented”只是另一种接受的说法，别写成“颜色的种类”。
- 文件头题重复题干已给的项（如题干已说 colour depth 和 resolution，⟦9618_s23_11:1(b)(i)⟧）不得分。
- image resolution 与 screen resolution 混淆：一个属于图像文件，一个属于显示设备。

#### 代表题精讲　⟦9618_s24_12:2(d)(i)⟧

**在考什么**　Describe how the data for a bitmapped image is encoded. 3 分，三个独立得分点。

**完整作答**　位图被分成一格一格的像素，每个像素只有一种颜色。图像里用到的每种颜色都对应一个唯一的二进制码（码的长度就是色深）。存储时从第一个像素开始，按顺序把每个像素的颜色码依次写入文件。

**与 MS 对齐**　①“Image is made of pixels and each pixel has one colour”；②“Each colour has a unique binary code”；③“Code for the colour of each pixel is stored in sequence”。三句一一对应，缺“unique”或“in sequence”都可能丢分。

**英文作答句**　The image is made of pixels and each pixel has one colour. Each colour has a unique binary code. The code for the colour of each pixel is stored in sequence.

**直观**　像十字绣图纸：先规定“红 = 01、白 = 10、蓝 = 11”（唯一编码），再从左上角一格一格抄下去（按顺序存放）。

**下一道变式**　⟦9618_w24_12:7(a)(i)⟧　（改考定义：colour depth 与 file header。）

<!-- auto:drills P1-IR-07 -->

### P1-IR-08　改变位图参数的影响　{#P1-IR-08}

<!-- auto:stats P1-IR-08 -->

**考法**　①说明提高/降低色深或分辨率对图像质量与文件大小的影响（常分“Effect on image / Effect on image file”两栏，各 2 分）；②说出可以改哪两个参数来减小文件；③勾选表：每个操作使文件变大/变小/不变；④增加每像素位数的一个缺点。

**识别信号**　Explain / Describe the effect of increasing / decreasing the bit depth / colour depth / image resolution；Effect on image … Effect on image file；Identify two elements … changed to reduce its file size；Tick … the effect of each action on the image file size。

**解题思路**
1. 每个影响写成**结果 + 原因**两句：MS 常把“效果”与“because …”分成两个得分点。
2. 色深 ↓ → 可用的颜色/色调变少 → 图像与原图差距变大、细节丢失；每像素位数变少 → 数据变少 → 文件变小。
3. 分辨率 ↓ → 像素变少 → 细节丢失、更模糊（像素化）；像素少 → 数据少 → 文件变小。提高时全部反过来。
4. 勾选表：改**屏幕**分辨率、改某个形状的颜色（色深不变）都**不**改变文件大小。
5. “减小文件的两个参数”：colour/bit depth 与 image resolution。

**得分表述**（引自对应 MS）
- 「There will be fewer shades of colour available」⟦9618_s25_13:1(a)(ii)⟧
- 「so the image does not match the original as detail is lost」⟦9618_s25_13:1(a)(ii)⟧
- 「Fewer bits are used to store each pixel」⟦9618_s25_13:1(a)(ii)⟧
- 「so less data is stored, therefore the file size is reduced」⟦9618_s25_13:1(a)(ii)⟧
- 「Decreasing resolution means details within the image are lost because there are fewer pixels」⟦9618_w24_12:7(a)(ii)⟧
- 「the image is sharper / less pixelated」⟦9618_w23_13:2(a)⟧

**易错与失分**
- 只写“file size decreases”不写原因（fewer bits per pixel / fewer pixels）：两栏各丢一分。
- 把降低色深说成“image becomes smaller”：图像尺寸不变，变的是颜色数。
- 勾选题把屏幕分辨率当成图像分辨率（⟦9618_w22_12:8(a)⟧，讲解时请对照原卷 QP p.15）。
- “降低色深”作为有损压缩**方法**来描述时属于 IR-15，不在这里。

#### 代表题精讲　⟦9618_s25_13:1(a)(ii)⟧

**在考什么**　Explain the effect of decreasing the bit depth on the image and on the image file. 4 分：图像 2 + 文件 2，每栏“效果 + 原因”。

**完整作答**
- 对图像：色深降低后每个像素能取的颜色变少，可用的色调变少；原图里相近的颜色被并成同一种，细节丢失，图像不再像原图。
- 对文件：每个像素用更少的位存储，总数据量变少，所以文件变小。

**与 MS 对齐**　图像栏：“There will be fewer shades of colour available”+“so the image does not match the original as detail is lost”；文件栏：“Fewer bits are used to store each pixel”+“so less data is stored, therefore the file size is reduced”。

**英文作答句**　Effect on image: there will be fewer shades of colour available, so the image does not match the original as detail is lost. Effect on image file: fewer bits are used to store each pixel, so less data is stored and the file size is reduced.

**下一道变式**　⟦9618_w24_12:7(a)(ii)⟧　（换成改变分辨率，同样两栏。）

<!-- auto:drills P1-IR-08 -->

### P1-IR-09　矢量图及与位图的比较　{#P1-IR-09}

<!-- auto:stats P1-IR-09 -->

**考法**　①矢量图术语：drawing object、property、drawing list（定义、连线、填空，或给出图形里的例子）；②描述 drawing list 的内容；③矢量图相对位图的好处、两者的差异；④为某个用途（如标志）选择位图或矢量图并论证（选择本身不给分）。

**识别信号**　vector graphic / drawing list / drawing object / property；differences between a vector graphic and a bitmap image；benefits of creating a vector graphic instead of a bitmap image；Tick … bitmap image or vector graphic … Justify。

**解题思路**
1. 三个术语的层次：**drawing object** 是一个形状（线、矩形、字母）；**property** 是某个形状的一项属性（线色、线宽、填充色、坐标）；**drawing list** 是整张图所有对象及画出它们所需命令的清单。
2. 位图存“每个像素是什么颜色”，矢量图存“怎样画每个形状”。
3. 矢量图的好处（成对写差异时对着位图说）：放大不失真（重新计算，不会像素化）；单个对象可以单独编辑；文件通常更小。
4. 选择题：照片、细节丰富 → 位图；标志、简单几何图形、需要多种尺寸 → 矢量图。理由要扣题目情境。

**得分表述**（引自对应 MS）
- 「an attribute of a drawing object」⟦9618_w24_12:7(b)⟧
- 「all the drawing objects/shapes in an image」⟦9618_w24_12:7(b)⟧
- 「A list that stores the command/description/equation required to draw each object」⟦9618_s24_12:2(d)(ii)⟧
- 「can be enlarged without pixelation / loss of quality」⟦9618_w22_12:8(b)⟧
- 「individual components of the image can be edited」⟦9618_w22_12:8(b)⟧
- 「generally a smaller file size」⟦9618_w22_12:8(b)⟧

**易错与失分**
- property 与 drawing object 搞反：property 是**属性**（颜色、粗细），object 是**形状本身**。
- 写“vector graphics are better quality”：MS 要具体机制——放大时重新计算、不像素化。
- 论证选择时只写一般优点、不扣情境：有情境的 justify 题要说“这个 logo 会用在不同尺寸的文件上”之类。

#### 代表题精讲　⟦9618_w24_12:7(b)⟧

**在考什么**　Define the vector graphic terms property and drawing list. 2 分，每个定义 1 分。

**完整作答**
- property：矢量图中某个绘图对象的一项属性，定义了它外观的一个方面，例如线的颜色或粗细。
- drawing list：图中全部绘图对象的清单，存着画出每个对象所需的命令/数学描述。

**与 MS 对齐**　property ←“an attribute of a drawing object // data about a shape // defines one aspect of the appearance of a drawing object”；drawing list ←“all the drawing objects/shapes in an image // stores the commands/descriptions / mathematical equations required to draw each object”。

**英文作答句**　Property: an attribute of a drawing object, for example its line colour. Drawing list: all the drawing objects in an image, storing the commands required to draw each object.

**下一道变式**　⟦9618_w22_12:8(b)⟧　（改问矢量图相对位图的两个好处。）

<!-- auto:drills P1-IR-09 -->

### P1-IR-10　声音的数字化与术语　{#P1-IR-10}

<!-- auto:stats P1-IR-10 -->

**考法**　①描述声音怎样在计算机中表示 / 模拟声波怎样转成数字数据（2–3 分骨架题）；②术语：sampling、sampling rate、sampling resolution、analogue data（定义、连线、按描述写术语）；③解释具体数值，如“44.1 kHz 采样率”“2 字节采样分辨率”是什么意思。

**识别信号**　Describe how sound is represented in a computer；Explain how an analogue sound wave is converted into digital data；sampling rate / sampling resolution / analogue data；Complete the table by giving the term for each description。

**解题思路**
1. 表示/转换题三点骨架：按**固定时间间隔**测量声波的**振幅** → 每个测量值（样本）给一个对应的**二进制数** → 这些二进制数**按顺序**存储。
2. sampling rate = 每秒（单位时间）取样的次数；sampling resolution = 存每个样本用的位数。
3. 具体数值：44.1 kHz = 每秒测量 44 100 次；2 字节采样分辨率 = 每个样本 16 位、可记录 2¹⁶ = 65 536 种振幅。
4. analogue data = 连续变化、可以取任意值的数据。

**得分表述**（引自对应 MS）
- 「The amplitude is recorded a set number of times a second」⟦9618_s23_13:3(c)(i)⟧
- 「Each (instance of an) amplitude is given a corresponding binary number」⟦9618_s23_13:3(c)(i)⟧
- 「The binary number (of each amplitude) is saved in sequence」⟦9618_s23_13:3(c)(i)⟧
- 「the number of samples taken per unit time / per second」⟦9618_w22_11:1(d)(i)⟧
- 「data values that are continuously changing」⟦9618_w23_13:1(a)⟧

**易错与失分**
- 写“the sound is recorded”却不说**测的是振幅**、**按固定间隔**：第一个得分点拿不到。
- sampling rate 与 sampling resolution 互换：rate 是“多少次/秒”，resolution 是“每次多少位”。
- “sampling”本身的定义（按固定间隔测量并存储）和“sampling rate”不同，连线题常把两者放在一起考（⟦9618_w23_13:1(b)⟧，讲解时请对照原卷 QP p.2）。

#### 代表题精讲　⟦9618_s23_13:3(c)(i)⟧

**在考什么**　Describe how sound is represented in a computer. 3 分，三个独立得分点。

**完整作答**　声音是连续变化的模拟波。计算机每隔固定的时间测量一次声波的振幅（每秒测量的次数就是采样率）。每次测得的振幅换成一个对应的二进制数（位数就是采样分辨率），这些二进制数按测量的先后顺序存储。

**与 MS 对齐**　①“The amplitude is recorded a set number of times a second”；②“Each (instance of an) amplitude is given a corresponding binary number”；③“The binary number (of each amplitude) is saved in sequence”。

**英文作答句**　The amplitude of the sound wave is recorded a set number of times a second. Each amplitude is given a corresponding binary number. The binary numbers are saved in sequence.

**直观**　像每隔一小段时间给声波拍一张“高度照片”：拍得越勤（采样率高）、量高度的刻度越细（采样分辨率高），拼回去的波形越像原来的声音。

**下一道变式**　⟦9618_w24_13:6(c)(i)⟧　（同一骨架，问法换成“analogue sound wave → digital data”。）

<!-- auto:drills P1-IR-10 -->

### P1-IR-11　采样参数改变的影响　{#P1-IR-11}

<!-- auto:stats P1-IR-11 -->

**考法**　①解释提高（或降低）采样率、采样分辨率对录音准确度的影响及原因；②对文件大小的影响；③勾选表或连线：每个操作对准确度/文件大小的影响（改录音时长不影响准确度）；④情境题：采样率翻倍对一个设备（如视频门铃）存储与传输性能的影响。

**识别信号**　Explain the effect of increasing / decreasing the sampling rate / sampling resolution；on the accuracy / precision of the (sound) recording / on the file size；Tick … the effect of each action；Draw lines from each change to the impacts。

**解题思路**
1. 采样率 ↑ → 样本之间的**时间间隔**更小（sound is recorded more often）→ 数字波形更接近模拟波形 → **量化误差**更小、更准确；样本更多 → 数据更多 → 文件更大。
2. 采样分辨率 ↑ → 每个样本**位数**更多 → 能表示的振幅值更多 → 每个样本更接近真实振幅 → 量化误差更小；每个样本位数多 → 文件更大。
3. 降低时全部反过来。
4. 情境题把“文件更大”落到情境：存储更快被填满、传输更慢。
5. 时长只影响文件大小，不影响准确度。

**得分表述**（引自对应 MS）
- 「There are smaller 'gaps' in the sound wave // sound is recorded more often」⟦9618_s23_13:3(c)(ii)⟧
- 「Digital waveform is closer to the analogue waveform」⟦9618_s23_13:3(c)(ii)⟧
- 「The quantisation errors are smaller」⟦9618_s23_13:3(c)(ii)⟧
- 「There are more bits per sample // a wider range of amplitudes can be stored」⟦9618_s23_13:3(c)(ii)⟧
- 「which means that the file size increases」⟦9618_w22_11:1(d)(ii)⟧
- 「because fewer bits are used to store each sample」⟦9618_w22_12:6(b)(ii)⟧

**易错与失分**
- 把采样率的原因（间隔更小）安到采样分辨率上，或反过来：两个参数的**机制**不同，结论（更接近原声、量化误差更小）相同。
- 只写“better quality”：MS 要“closer to the analogue waveform”或“quantisation errors are smaller”这类具体说法。
- 情境题只写“file is bigger”而没说对设备的影响（⟦9618_s24_11:2(d)⟧：传输更久、存储更快装满、能存的视频更少）。

#### 代表题精讲　⟦9618_s23_13:3(c)(ii)⟧

**在考什么**　Explain the reasons why increasing the sampling rate and the sampling resolution will improve the precision of the second recording. 4 分：采样率最多 2 + 采样分辨率最多 2。

**完整作答**
- 采样率：每秒取样次数增加，样本之间的“空隙”变小，声音被记录得更频繁，所以数字波形更接近原来的模拟波形。
- 采样分辨率：每个样本的位数增加，可以存储更多不同的振幅值，所以每个样本的二进制振幅更接近真实振幅，量化误差更小。

**与 MS 对齐**　采样率：“There are smaller 'gaps' in the sound wave // sound is recorded more often”+“Digital waveform is closer to the analogue waveform”（或“The quantisation errors are smaller”）；采样分辨率：“There are more bits per sample // a wider range of amplitudes can be stored”+“Each binary amplitude/note (in the digital recording) is closer to the analogue amplitude/note”。

**英文作答句**　Sampling rate: the sound is recorded more often, so there are smaller gaps in the sound wave and the digital waveform is closer to the analogue waveform. Sampling resolution: there are more bits per sample, so a wider range of amplitudes can be stored and each binary amplitude is closer to the analogue amplitude, so the quantisation errors are smaller.

**下一道变式**　⟦9618_w23_12:6(b)⟧　（只问采样分辨率对准确度的影响，3 分。）

<!-- auto:drills P1-IR-11 -->

### P1-IR-12　多媒体文件大小与位深计算　{#P1-IR-12}

<!-- auto:stats P1-IR-12 -->

**考法**　①位图文件大小：宽 × 高 × 色深，换成 bytes / kB / MB / KiB / MiB；②视频：再 × 每秒帧数（× 秒数）；③声音：采样率 × 采样分辨率 × 时长；④由颜色数求最少色深，或由位数求最多颜色数。几乎都是 2 分（working 1 + 答案 1）。

**识别信号**　Calculate (an estimate for) the file size … Show your working；Give your answer in megabytes / mebibytes / kibibytes / bytes；pixels wide … pixels high … bit depth；frames … per second；sampling rate … sampling resolution；smallest bit depth / largest number of different colours。

**解题思路**
1. 统一成**位**：位图 bits = 宽 × 高 × 色深（色深给的是 bytes 就先 × 8，或直接用字节算）。
2. 视频 = 一帧的大小 × 每秒帧数 × 秒数；声音 = 采样率（次/秒）× 每样本位数 × 秒数（分钟先 × 60）。
3. ÷ 8 得 bytes。
4. 看单位要求：kB/MB/GB 每级 ÷ 1000；KiB/MiB 每级 ÷ 1024。
5. 题目给 2 的幂（2048、1024、512）时多半要用二进制前缀：先写成 2ⁿ 再约分，手算最快。
6. 最少色深：最小的 n 使 2ⁿ ≥ 颜色数；n 位最多 2ⁿ 种颜色。
7. 合理性检查：一张几百万像素、16 位色的照片应在几 MB 量级。

**得分表述**（引自对应 MS）
- 「Working: (1500 * 3000 * 8) / 1000 / 1000」⟦9618_s23_11:1(b)(ii)⟧
- 「Answer: 2.5 mebibytes」⟦9618_w23_12:6(c)⟧
- 「(4000*3000*30*16) / (8*1000*1000*1000)」⟦9618_w25_13:7(b)⟧
- 「50 000 * 1200 * 16 bits」⟦9618_w22_13:1(b)⟧
- 「Answer: 1024 kibibytes」⟦9618_w25_11:7(d)(i)⟧

**易错与失分**
- 色深给的是**字节**（题干 “The bit depth is 4 bytes” ⟦9618_s24_13:2(a)⟧）时还 ÷ 8：4000 × 3000 × 4 已经是字节数。
- 单位混用：题目要 MiB 却 ÷ 1000，或要 MB 却 ÷ 1024。
- 声音时长是分钟却忘了 × 60（20 分钟 = 1200 秒）。
- 不写 working：错一个数字就整题 0 分；写了算式，答案错仍有 1 分。
- “256 colours”求最少位数写 256：要的是位数 8。

#### 代表题精讲　⟦9618_w23_12:6(c)⟧

**在考什么**　2048 × 1024 像素、每像素 10 位，估算文件大小（mebibytes）。2 分：working 1 + 答案 1。

**完整作答**
```
bits  = 2048 × 1024 × 10
bytes = 2048 × 1024 × 10 / 8
MiB   = 2048 × 1024 × 10 / (8 × 1024 × 1024)
      = 2^11 × 2^10 × 10 / (2^3 × 2^20)
      = 10 / 4 = 2.5 MiB
```
合理性：200 万像素左右、每像素一个多字节 → 两三 MiB，对得上。

**与 MS 对齐**　working ←“(2048 × 1024 × 10) / (8 × 1024 × 1024)”；答案 ←“Answer: 2.5 mebibytes”。

**英文作答句**　File size = (2048 × 1024 × 10) / (8 × 1024 × 1024) = 2.5 mebibytes.

**直观**　“乘出总位数 → 除 8 变字节 → 按要求的前缀一级一级除”三步走；2 的幂的数字配二进制前缀，几乎总能约得干干净净。

**下一道变式**　⟦9618_w22_13:1(b)⟧　（换成声音：50 kHz、16 位、20 分钟，答案用 megabytes。）

<!-- auto:drills P1-IR-12 -->

### P1-IR-13　压缩的理由　{#P1-IR-13}

<!-- auto:stats P1-IR-13 -->

**考法**　“为什么要压缩”放进具体情境：发邮件附件、上传/下载照片、从网站下载程序、实时视频会议。还有反向题：为什么这个视频**不需要**压缩。2–4 分，好处常写成“好处 + 对谁有什么后果”两步。

**识别信号**　Explain the reasons why … is compressed (before it is transmitted / attached to an email)；Explain the benefits … of … being a compressed file；Give two reasons why the video does not need to be compressed。

**解题思路**
1. 压缩让文件变小，好处从四个方向找：**存储**（占用更少空间、能存更多）；**传输时间**（上传/下载更快）；**带宽**（占用更少，别的传输不受影响）；**限制**（附件大小上限、流量额度）。
2. 每个好处再接一句情境后果：“… so the teacher does not have to wait as long”。分值 ≥ 3 时，这句“后果”通常独立得分。
3. 情境是**实时流媒体**时，再写缓冲与实时性：减少缓冲、对话不延迟、带宽低的人也能参加（这部分属位流知识，副题型 P1-CM-12）。
4. 反向题（不需要压缩）：专用连接、不共享带宽；连接已经够快；文件本来就小；不保存所以不占存储。

**得分表述**（引自对应 MS）
- 「The customers will be able to download the photographs in less time」⟦9618_s23_11:1(c)(i)⟧
- 「and they will take less of the customer's bandwidth」⟦9618_s23_11:1(c)(i)⟧
- 「The photographs will take up less space on the customer's storage medium」⟦9618_s23_11:1(c)(i)⟧
- 「Transmission time is reduced」⟦9618_w24_11:4(b)(i)⟧
- 「so the teacher does not have to wait as long for it to arrive」⟦9618_w24_11:4(b)(i)⟧
- 「Email accounts often have a maximum size for an attachment」⟦9618_w23_11:1(c)⟧

**易错与失分**
- 写“to make the file smaller”就停：那是压缩本身，不是好处；要接着说小了**所以**怎样。
- 好处不扣对象：题目问“benefit the customers / the teacher”，就写顾客/老师的存储、等待时间、带宽。
- 同一个好处换个说法写两遍（“faster to download”和“less time to download”）只算一分。

#### 代表题精讲　⟦9618_s23_11:1(c)(i)⟧

**在考什么**　照片压缩后上传网站、顾客下载。Explain the reasons why compressing the photographs will benefit the customers. 3 分。

**完整作答**　压缩后的照片文件更小：①顾客下载照片用的时间更少；②下载时占用顾客的带宽更少；③照片保存到顾客设备上占用的存储空间更少，因此顾客能存更多照片、给其他文件留出空间。

**与 MS 对齐**　“The customers will be able to download the photographs in less time”→“…and they will take less of the customer's bandwidth”→“The photographs will take up less space on the customer's storage medium”，后面还可接“…therefore the customers can store more images”。任写三点即满分。

**英文作答句**　The customers will be able to download the photographs in less time, and the downloads will take less of the customer's bandwidth. The photographs will also take up less space on the customer's storage medium, so the customers can store more images.

**下一道变式**　⟦9618_s24_12:2(d)(iii)⟧　（反向：为什么传给 VR 头显的视频不需要压缩。）

<!-- auto:drills P1-IR-13 -->

### P1-IR-14　有损与无损：选择与论证　{#P1-IR-14}

<!-- auto:stats P1-IR-14 -->

**考法**　①为给定场景（实时视频、照片、文本、声音）选有损或无损并论证——选择本身常常不给分；②解释为什么文本必须用无损；③列出用有损（而不是无损）的好处；④判断一种做法（如降低采样率）属于有损还是无损并说明理由。

**识别信号**　Identify whether the lossy or lossless compression method is more appropriate … Justify；Tick one box … Lossy / Lossless … Justification；Explain why lossless compression is more appropriate than lossy for a text file；Give three benefits of … lossy compression instead of lossless；State whether this is lossless or lossy compression。

**解题思路**
1. 定义打底：**有损**永久删除部分数据，原文件不能完全恢复，但压得更小；**无损**不丢任何数据，可以完全还原。
2. 文本、程序、数据库 → 无损：每个字符都必须保留，否则文件损坏、意思改变。
3. 照片、视频、音乐 → 通常有损：删掉的细节人眼/人耳察觉不到，而文件小得多。
4. 论证骨架：“选择 → 文件小多少（或不丢什么）→ 在这个情境里带来什么后果”。实时视频的后果是：带宽更少 → 缓冲更少 → 播放更流畅。
5. “这个做法是有损吗”：只要原数据不能还原（降低采样率、降低色深、降低分辨率）就是有损。

**得分表述**（引自对应 MS）
- 「Loss of quality will not be noticed」⟦9618_w23_12:6(a)⟧
- 「Smaller file sizes will reduce buffering so the video will play more smoothly」⟦9618_w23_12:6(a)⟧
- 「all the data is required // no data can be lost」⟦9618_w22_12:8(c)(ii)⟧
- 「otherwise text file will be corrupted / not make sense」⟦9618_w22_12:8(c)(ii)⟧
- 「There will be fewer samples per second, so data will be permanently lost」⟦9618_w25_12:6(a)⟧
- 「The file uses less bandwidth to transmit than if lossless compression was used」⟦9618_s24_13:2(b)(i)⟧

**易错与失分**
- 只写选择不写理由：“No mark for choice”的题全部分数在理由上。
- “有损 vs 无损”的比较题要写“**than if lossless compression was used**”这类比较，而不是只写压缩的一般好处（⟦9618_s24_13:2(b)(i)⟧）。
- 实时视频选无损也能得分，但理由必须是 MS 认可的方向（原片分辨率不高、接收端带宽高、观众不接受任何画质损失）；没有理由的选择 0 分。
- “降低采样率”判断题要说出**数据永久丢失、原声不能重建**，不能只写“quality is lower”。

#### 代表题精讲　⟦9618_w23_12:6(a)⟧

**在考什么**　实时音乐会视频要流式传给订阅者。Tick one box to identify the most appropriate type of compression and justify your answer. 3 分全在理由（讲解时请对照原卷 QP p.9 的勾选框）。

**完整作答**　选有损。①观众察觉不到画质的轻微损失；②视频要实时观看，文件越小需要的带宽越少；③文件小可以减少缓冲，视频播放更流畅；（④观众可能用不同设备观看，不一定需要高分辨率。）

**与 MS 对齐**　选有损时的四个得分点：“Loss of quality will not be noticed”“Needs to be viewed in real time so less bandwidth needed if file size smaller”“Smaller file sizes will reduce buffering so the video will play more smoothly”“Viewers may watch on different devices, so may not need high quality resolution”，任取三条。

**英文作答句**　Lossy. The loss of quality will not be noticed by viewers. The video needs to be viewed in real time, so less bandwidth is needed if the file size is smaller. Smaller file sizes will reduce buffering, so the video will play more smoothly.

**下一道变式**　⟦9618_w22_12:8(c)(ii)⟧　（反方向：解释文本文件为什么用无损。）

<!-- auto:drills P1-IR-14 -->

### P1-IR-15　压缩方法　{#P1-IR-15}

<!-- auto:stats P1-IR-15 -->

**考法**　①描述一种无损方法（几乎都是游程编码 RLE）压缩文本或位图；②按 RLE 编码/解码一段数据（填表）；③解释 RLE 为什么可能不省空间（要举例）；④描述有损方法：声音降低采样率/采样分辨率、删去人耳听不到的频率；图像降低色深/分辨率/减少调色板。

**识别信号**　Describe / Explain how … can be compressed using run-length encoding (RLE)；Describe one lossless / lossy method of compressing a text file / sound file / image；Complete the table（uncompressed 与 RLE compressed 对照）；Explain the reasons why RLE may not reduce the file size。

**解题思路**
1. RLE 三点骨架：**找出连续重复的相同字符/相同颜色的像素** → 用**一个副本** → 加上**重复次数**来代替这一串。题目问“lossless method”时，第一点可直接写“Run-length encoding”（常独立得分）。
2. 编码填表：数清每段连续相同值的个数，写成“次数 + 值”（按题目第一行给的格式写）；解码反过来展开。
3. RLE 不省空间：数据里很少连续重复 → 每个值都要多存一个“1”→ 反而变大。例：Red-Green-Blue → Red 1 Green 1 Blue 1。
4. 有损方法“方法 + 为什么变小”成对写：降低采样率 → 每秒存的样本少；降低采样分辨率 → 每个样本位数少；去掉人耳听不到的声音 → 存的测量值少。

**得分表述**（引自对应 MS）
- 「Repeated sequences of the same characters are replaced by」⟦9618_w24_11:4(b)(ii)⟧
- 「a single copy of the character」⟦9618_w24_11:4(b)(ii)⟧
- 「and a count of the number of characters」⟦9618_w24_11:4(b)(ii)⟧
- 「Identifies consecutive repeating pixels of the same colour」⟦9618_s24_13:2(b)(ii)⟧
- 「Stores the colour /pattern and the number of times it repeats」⟦9618_s24_13:2(b)(ii)⟧
- 「An image may not have many sequences of the same colour」⟦9618_s23_11:1(c)(ii)⟧

**易错与失分**
- 漏掉“consecutive / repeated sequences”：RLE 只压**连续**的重复，全文出现很多次但不相邻的字符不会被合并。
- “单个副本”和“次数”只写其中之一：两者各占一个得分点。
- 填 RLE 表时次数与值的顺序跟题目示例不一致（⟦9618_w22_12:8(c)(i)⟧ 用“次数在前”，讲解时请对照原卷 QP p.16）。
- 把“降低色深”写成无损方法：它会永久丢失数据，是有损。

#### 代表题精讲　⟦9618_w24_11:4(b)(ii)⟧

**在考什么**　Describe one lossless method of compressing a text file. 3 分。

**完整作答**　使用游程编码 RLE。程序扫描文本，找出连续重复出现的同一字符；每一段这样的重复都换成该字符的一个副本加上它重复的次数。例如 `AAAAABBB` 存成 `5A3B`，解压时按次数展开，原文一字不差地恢复，所以是无损的。

**与 MS 对齐**　四个可得分点取三：“Run-Length Encoding // RLE”→“Repeated sequences of the same characters are replaced by”→“... a single copy of the character”→“... and a count of the number of characters”。

**英文作答句**　Run-length encoding (RLE) can be used. Repeated sequences of the same character are replaced by a single copy of the character and a count of the number of characters.

**下一道变式**　⟦9618_s23_11:1(c)(ii)⟧　（反过来：RLE 为什么可能不减小位图的文件大小，要举例。）

<!-- auto:drills P1-IR-15 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| IR-01 位数 vs IR-12 位深 | 纯数字“n 位几个值 / 最少几位”→ IR-01；放在图像颜色数里 → IR-12 | 题干有没有 image / colour / pixel |
| IR-02 vs IR-03 | 无符号与 BCD 转换 → IR-02；出现 two's / one's complement、负数、补码最值 → IR-03 | two's complement、signed、smallest/largest |
| IR-03 vs IR-05 | 只转换 → IR-03；要做加减（哪怕用补码减）→ IR-05 | add / subtract / binary addition |
| IR-02 vs IR-06 | 码值已给，只换进制 → IR-02；要用“码值连续”推出别的字符 → IR-06 | “The Unicode value for '1' is 49. Write the value for '5'” |
| IR-07 vs IR-08 vs IR-12 | 术语与编码 → IR-07；改参数的影响（定性）→ IR-08；算大小 → IR-12 | define / effect of / calculate |
| IR-10 vs IR-11 | 怎样采样、术语 → IR-10；改采样率/分辨率的影响 → IR-11 | what is meant by / effect of increasing |
| IR-08/IR-11 vs IR-15 | 改参数对质量与大小的影响 → IR-08/IR-11；把“降低色深/采样率”当压缩**方法**描述 → IR-15 | describe one lossy method |
| IR-13 vs IR-14 vs IR-15 | 为什么压 → IR-13；选有损还是无损 → IR-14；怎样压 → IR-15 | reasons / lossy or lossless / how … RLE |
| 溢出 vs 补码进位 | 补码加法丢掉的第 9 位是正常现象；结果超出可表示范围才是溢出 | 两个同号数相加得异号结果 |
