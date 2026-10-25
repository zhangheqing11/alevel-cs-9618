## LG　逻辑门与逻辑电路 {#ch-LG}

<!-- auto:chapter-stats -->

### 核心思想

这一章只有一件事：**同一个逻辑关系的四种写法——文字描述、逻辑表达式、电路图、真值表——之间互相翻译**。每卷必考，几乎每题 2–3 分，套路固定，是 P1 最稳的得分点。

```
                  LG-06 文字条件 + 参数表
                           │ 建立
                           ▼
   LG-02 画电路 ◄──── 逻辑表达式 ────► LG-04 填真值表
   LG-03 写表达式 ───►      ▲               │
                           └── LG-05 ───────┘
                          由真值表反推
```

1. **单个门**（LG-01）：六种门的功能、符号、真值表。后面所有题都建立在这张“六门表”上，必须背到不假思索。
2. **表达式 ↔ 电路**（LG-02、LG-03）：按括号层次一门一门对应。画电路是“由内向外”，写表达式是“由输入向输出”。
3. **表达式/电路 → 真值表**（LG-04）：八行输入按二进制顺序排好，每个门开一列中间结果，最后一列就是输出。
4. **真值表 → 表达式**（LG-05）：找输出为 1 的行，每行写一个 AND 项，再用 OR 连起来。
5. **文字 → 表达式/电路**（LG-06）：先把每个条件翻成“输入 = 1 还是 0”，再按 and / or 组合。

**六门表**（全章的地基）

| 门 | 表达式 | 输出为 1 的条件 | 输入 00 / 01 / 10 / 11 时的输出 | 符号要点 |
|:--|:--|:--|:--|:--|
| NOT | NOT A | 输入为 0 | 0→1，1→0 | 三角形 + 输出端小圆圈 |
| AND | A AND B | 两个输入都是 1 | 0 0 0 1 | D 形：平背、圆头 |
| OR | A OR B | 至少一个输入是 1 | 0 1 1 1 | 弯背、尖头 |
| NAND | A NAND B | 不是“两个都 1” | 1 1 1 0 | AND + 输出小圆圈 |
| NOR | A NOR B | 两个输入都是 0 | 1 0 0 0 | OR + 输出小圆圈 |
| XOR | A XOR B | 两个输入不同 | 0 1 1 0 | OR 的弯背后面再加一道弧线 |

记忆：NAND 是 AND 的取反，NOR 是 OR 的取反；XOR 是“不同才亮”。小圆圈（bubble）永远表示“取反”。

**全章通用约定**：除 NOT 外每个门两个输入；`A AND B AND C` 画成两个两输入 AND 串联；表达式里**每个门的结果都加括号**——MS 给分看的是括号层次是否和电路一致。

### 题型树
<!-- auto:type-tree -->

### P1-LG-01　逻辑门的功能与单门真值表　{#P1-LG-01}

<!-- auto:stats P1-LG-01 -->

**考法**　①用文字描述 NAND、NOR、XOR、OR 等门的功能（每门 1 分）；②画出某个门的两输入真值表（有时要先自己画表头）；③给出“输出为 1”，为每个门各写一组能做到的输入；④勾选表：按描述选门；⑤看已有电路，指出一个/两个**没用到**的门，并画符号、填真值表。

**识别信号**　Describe the operation / function of the … gate(s)；Complete the truth table for each of the following two logic gates；Create and complete the truth table for a two-input NAND gate；writing one set of values … that will give the output 1；Identify one logic gate not used in the given logic circuit。

**解题思路**
1. 描述功能用**一句“条件 + 否则”**：“The output is 1 when …, otherwise the output is 0.” 条件一定要写**两个输入各是什么**，不能只写“when the inputs are 1”。
2. 记不准时先在草稿上写出该门的四行真值表，再从表里读出“输出唯一不同的那一行”：AND 只有 11 得 1；OR 只有 00 得 0；NAND 只有 11 得 0；NOR 只有 00 得 1；XOR 是两行 01、10 得 1。描述就写这一行。
3. 画真值表：表头 `A | B | Output`，输入按 00、01、10、11 排；自己画表时表头本身也计分（⟦9618_s26_11:6(b)⟧ 有一分专给“正确的输入列”）。
4. “给出输出 1 的输入”：从上面那张表里挑一行输出为 1 的即可，任意一组都对。
5. “没用到的门”：先列出电路里出现的门，再从六门里挑一个不在里面的；符号和真值表必须与你写的门**一致**（MS 三分是“门 → 对应符号 → 对应真值表”连锁给分）。

**得分表述**（引自对应 MS）
- 「The output is 0 when both inputs are 1, otherwise the output is 1」⟦9618_s24_12:1(a)⟧
- 「The output is 1 when both inputs are 0, otherwise the output is 0」⟦9618_s24_12:1(a)⟧
- 「Output is only 1 if one input is 1 and the other is 0」⟦9618_w24_13:1(a)⟧
- 「Output is only 0 if both inputs are the same」⟦9618_w24_13:1(a)⟧
- 「The output is 0 when both inputs are 0, otherwise the output is 1」⟦9618_s24_12:1(a)⟧
- 「1 is only output when both inputs are 0」⟦9618_s23_11:5(b)⟧

**易错与失分**
- 描述 NAND 写成“the output is 0 when the inputs are 1”：没说“**both** inputs”，读起来像只要一个输入为 1 就输出 0（那是 NOR）。
- XOR 写成“the output is 1 when one input is 1”：没排除两个都是 1 的情况。要写“one input is 1 **and the other is 0**”或“both inputs are different”。
- NAND / NOR 互换：NAND 的“唯一 0”在 11，NOR 的“唯一 1”在 00——先写四行表再描述就不会错。
- “没用到的门”选了电路里其实出现过的门；或门名写 NOR、符号却画成 OR（漏了小圆圈），连锁丢分。

#### 代表题精讲　⟦9618_s24_12:1(a)⟧

**在考什么**　Describe the operation of each of the following logic gates: NAND, NOR, XOR, OR. 4 分，每门 1 分。考你能否用“输入条件 → 输出”一句话准确说出门的行为。

**完整作答**
- NAND：两个输入都是 1 时输出 0，其他情况输出 1。
- NOR：两个输入都是 0 时输出 1，其他情况输出 0。
- XOR：一个输入是 1、另一个是 0 时输出 1，其他情况输出 0。
- OR：两个输入都是 0 时输出 0，其他情况输出 1。

**与 MS 对齐**　四句与 MS 逐门对应：NAND “The output is 0 when both inputs are 1, otherwise the output is 1”；NOR “The output is 1 when both inputs are 0, otherwise the output is 0”；XOR “The output is 1 when one of the inputs is 1 and the other input is 0, otherwise the output is 0”；OR “The output is 0 when both inputs are 0, otherwise the output is 1”。注意 MS 每门都是“唯一特殊行 + otherwise”的格式。

**英文作答句**　NAND: The output is 0 when both inputs are 1, otherwise the output is 1. NOR: The output is 1 when both inputs are 0, otherwise the output is 0. XOR: The output is 1 when one input is 1 and the other input is 0, otherwise the output is 0. OR: The output is 0 when both inputs are 0, otherwise the output is 1.

**直观**　每个两输入门的真值表里，总有“最特别的那一行”（或 XOR 的两行）。描述一个门，就是把那一行说出来，再加一句“其余相反”。

**下一道变式**　⟦9618_s22_11:2(c)(i)⟧　（反过来问：输出为 1 时，AND、NAND、XOR、NOR 各给一组输入。）

<!-- auto:drills P1-LG-01 -->

### P1-LG-02　由逻辑表达式画电路　{#P1-LG-02}

<!-- auto:stats P1-LG-02 -->

**考法**　给一个 3 或 4 输入的表达式（`X = NOT ((A AND B) OR (C AND D))` 之类），在已标好输入 A、B、C（、D）和输出 X 的作图区画电路。几乎都是 2 分：前一分给“内层的门”，后一分给“外层/最后的门”；偶有 3 分题按括号三段给分。同一表达式常在下一小问再要求填真值表（LG-04）。

**识别信号**　Draw a / the logic circuit for (this / the) logic expression；作图区左边一列输入字母、右边一个输出字母。

**解题思路**
1. **拆层**：从最内层括号开始，给每个运算编号。例 `Y = ((P AND Q) XOR ((NOT Q) OR R)) AND NOT P`：① P AND Q；② NOT Q；③ ② OR R；④ ① XOR ③；⑤ NOT P；⑥ ④ AND ⑤。门的个数 = 运算的个数（这里 6 个），**画完数一遍**，多一个少一个都扣分。
2. **从左往右画**：最内层的门靠近输入，最外层的门靠近输出 X。
3. **连输入**：同一个输入要用到几次，就从输入线上分叉几次（画一个实心点表示连接）；不要为同一个字母另起一个输入。
4. **NOT 的位置**：`NOT A` 是只对 A 取反，NOT 门画在 A 的输入线上；`NOT (…)` 是对整个括号取反，NOT 门画在那个括号对应的门的输出后面（也可以把它和前一个门合并成 NAND/NOR，但只有 MS 写了 `//` 等价写法时才放心这样做）。
5. **核对**：从输出往回读一遍，把读出的表达式和题目对比（这就是 LG-03 的方法）。

**得分表述**（引自对应 MS）
- 「1 mark for both AND gates with correct inputs」⟦9618_s24_12:1(b)⟧
- 「correct OR and NOT gates with correct inputs and no superfluous gates」⟦9618_s24_12:1(b)⟧
- 「1 mark for P AND Q and NOT Q OR R」⟦9618_w23_13:4(b)⟧
- 「1 mark for NOT gate and AND gate and XOR gate」⟦9618_w23_13:4(b)⟧
- 「NOT A AND NOT B and NOT B AND NOT C // A NOR B and B NOR C」⟦9618_w22_11:3(a)⟧

**易错与失分**
- 多画门（superfluous gates）：例如把 `NOT A AND NOT B` 画成两个 NOT + 一个 AND 没问题，但再额外加一个 NOT 就违背表达式。MS 明写“no superfluous gates”。
- 三输入门：`A AND B AND C` 不要画一个三输入 AND，拆成两个两输入 AND。
- `NOT T NOR P`（⟦9618_s23_12:6(a)⟧）：NOT 只作用在 T 上，然后才与 P 做 NOR；不是 `NOT (T NOR P)`。
- 符号画得含糊：OR 与 XOR 只差后面一道弧线，AND 与 NAND 只差一个小圆圈——画清楚。
- 输入线交叉时没有分叉点，阅卷看不出是否相连。

#### 代表题精讲　⟦9618_w23_13:4(b)⟧

**在考什么**　Draw a logic circuit for the logic expression `Y = ((P AND Q) XOR ((NOT Q) OR R)) AND NOT P`。2 分，三个输入 P、Q、R，P 和 Q 都要用两次。

**完整作答**（按层描述，画时从左到右）
1. 第一层：一个 AND 门，输入 P、Q；一个 NOT 门，输入 Q；一个 NOT 门，输入 P。
2. 第二层：一个 OR 门，输入是“NOT Q 的输出”和 R。
3. 第三层：一个 XOR 门，输入是“P AND Q 的输出”和“OR 门的输出”。
4. 第四层：一个 AND 门，输入是“XOR 的输出”和“NOT P 的输出”，输出接 Y。
5. 数门：AND、NOT、NOT、OR、XOR、AND，共 6 个，与表达式里的 6 个运算一致。P 线分叉到第一个 AND 和 NOT P；Q 线分叉到第一个 AND 和 NOT Q。

**与 MS 对齐**　第 1 分 ←“P AND Q and NOT Q OR R”（内层两部分都对）；第 2 分 ←“NOT gate and AND gate and XOR gate”（NOT P、最后的 AND、中间的 XOR 都对且接线正确）。

**英文作答句**　（作图题无文字作答；画完可在旁边标每个门的输出，如 `P AND Q`、`NOT Q OR R`，便于自查。）

**直观**　表达式是“俄罗斯套娃”，电路就是把套娃从里到外一层层摆在纸上：最里面的娃离输入最近，最外面的娃直接连输出。

**下一道变式**　⟦9618_w25_13:3(b)⟧　（四个输入，NOR 与外层 NOT 一起出现：`X = NOT (((A AND B) OR C) AND (C NOR D))`。）

<!-- auto:drills P1-LG-02 -->

### P1-LG-03　由电路写逻辑表达式　{#P1-LG-03}

<!-- auto:stats P1-LG-03 -->

**考法**　给电路图，写出 X（有时同时写 X 和 Y 两个输出）的逻辑表达式，常注明“Do not simplify”。2–3 分，按门或按括号段给分。

**识别信号**　Write the logic expression(s) for the (following / given) logic circuit；Write the Boolean expression that corresponds to the following logic circuit；电路图下方 `X = ……`。

**解题思路**
1. **认门**：先把图上每个门的名字写在门旁边（AND、OR、NAND、NOR、XOR、NOT）。小圆圈 = 取反；OR 后面多一道弧 = XOR。
2. **从输入到输出逐门写**：每个门的输出写成“(输入 1  门名  输入 2)”，并**整体加括号**，再把它当作一个整体送进下一个门。
3. **最后一个门**两边都是括号块，写成 `(左块) 门名 (右块)`。
4. 两个输出（X、Y）的电路各写各的；共用的输入照写。
5. **核对**：数一下表达式里的运算个数 = 图上门的个数；不化简、不改写（题目写了 Do not simplify 时，化简后哪怕等价也可能不得分）。

**得分表述**（引自对应 MS）
- 「XOR (with remainder correct and bracketed and nothing extra)」⟦9618_s22_13:7(a)⟧
- 「X = (A AND B) XOR (NOT C AND B)」⟦9618_s22_13:7(a)⟧
- 「X = (NOT (A XOR B)) NAND ((B AND C) OR A)」⟦9618_w25_12:9(a)⟧
- 「X = Q AND (NOT P OR R)」⟦9618_s25_11:1(a)⟧
- 「Y = S XOR (Q NOR R)」⟦9618_s25_11:1(a)⟧

**易错与失分**
- 漏括号：`A AND B XOR NOT C AND B` 有歧义，MS 要求“bracketed”。每个门的结果都括起来最安全。
- 把 NAND 写成 `NOT A AND B`：NAND 是对整个 AND 结果取反，写 `A NAND B` 或 `NOT (A AND B)`。
- NOT 的位置：图上 NOT 在输入线上 → `NOT C`；在门的输出后 → `NOT (…)`。看小三角在哪里。
- 两个输入次序可以交换（`(B AND C) OR A` 与 `A OR (B AND C)` 等价，MS 常用 `//` 列出两种），但门不能换。
- 电路图看错门：抽取文本里没有图，**本型每题都要对照原卷 QP 的电路图**。

#### 代表题精讲　⟦9618_s22_13:7(a)⟧

**在考什么**　Write the logic expression for the following logic circuit. 3 分（讲解时请对照原卷 QP p.14 的电路图）。电路有三个门加一个 NOT：A、B 进一个 AND；C 先过 NOT，再和 B 进第二个 AND；两个 AND 的输出进 XOR 得 X。

**完整作答**
1. 上面的门：`A AND B`。
2. 下面的门：C 先取反，再和 B 相与：`NOT C AND B`（写成 `B AND NOT C` 也对）。
3. 最后一个门是 XOR，两边各一个括号块：`X = (A AND B) XOR (NOT C AND B)`。

**与 MS 对齐**　MS 三段各 1 分：“A AND B”→“NOT C AND B // B AND NOT C”→“XOR (with remainder correct and bracketed and nothing extra)”。第三分要求括号正确且没有多余的东西——这就是“每个门加括号”的理由。

**英文作答句**　X = (A AND B) XOR (NOT C AND B)

**下一道变式**　⟦9618_w25_12:9(a)⟧　（换成 NOT 在门的输出后、最后一个门是 NAND，且注明 Do not simplify。讲解时请对照原卷 QP p.14。）

<!-- auto:drills P1-LG-03 -->

### P1-LG-04　构造真值表　{#P1-LG-04}

<!-- auto:stats P1-LG-04 -->

**考法**　①由逻辑表达式完成三输入真值表（最常见，2 分：前 4 行 1 分、后 4 行 1 分）；②由电路图完成真值表；③多输出电路：每个输出列各 1 分；④改错：给出一张有错的真值表，写出输出错的行号。

**识别信号**　Complete the truth table for this / the (following) logic expression / the given logic circuit；表旁的 Working space；There are … errors in the truth table … writing the row numbers。

**解题思路**
1. **输入列**：三个输入按二进制计数 000 到 111 排八行（题目已印好，确认顺序）。规律：最左列 0000 1111，中列 0011 0011，右列 0101 0101。
2. **拆门**：按 LG-02 的拆层方法给表达式里每个运算编号，在 Working space 里**每个运算开一列**，从内层到外层依次算。
3. **逐列算**：每一列只用一个门的规则，查六门表；NOT 列直接把来源列翻过来。
4. **最后一列** = 输出。抄到 X 列。
5. **快速检查**：利用“支配值”核对——AND 里有一个 0 必为 0；OR 里有一个 1 必为 1；NAND 里有一个 0 必为 1；NOR 里有一个 1 必为 0。例如外层是 `… AND NOT P`，那么 P = 1 的后四行必全为 0。
6. 改错题：同样把整张表算出来，再逐行比对给出的输出，写出不同的行号。

**得分表述**（引自对应 MS）
- 「1 mark for first 4 rows, 1 mark for second 4 rows」⟦9618_s25_11:1(b)⟧
- 「1 mark for each set of highlighted rows」⟦9618_w22_13:5(b)⟧
- 「1 mark for A column and 1 mark for B column」⟦9618_s26_12:8(a)⟧
- 「1 mark for 1 or 2 row numbers correct, 2 marks all three correct」⟦9618_w25_12:9(b)⟧

**易错与失分**
- 跳过中间列直接心算：一错整组四行全丢。Working space 不计分，但它是让 X 列对的唯一保障。
- 输入顺序看错（P、Q、R 与 A、B、C 的列序）：先看表头，表达式里的字母对应哪一列。
- NOT 作用范围搞错：`NOT (A NAND B) XOR (…)`（⟦9618_w23_11:4(a)⟧）里 NOT 只作用于 `(A NAND B)`，不是整个式子。
- 多输出电路（⟦9618_s26_13:2(a)⟧ 等）的列序是 X、Y、Z 输入，A、B 输出——别把输入当输出填。

#### 代表题精讲　⟦9618_w22_13:5(b)⟧

**在考什么**　Complete the truth table for the logic expression `Y = (NOT P AND Q) OR (Q AND NOT R)`。2 分，每组 4 行 1 分。

**完整作答**　开两列中间结果：

| P | Q | R | NOT P AND Q | Q AND NOT R | Y |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 | **0** |
| 0 | 0 | 1 | 0 | 0 | **0** |
| 0 | 1 | 0 | 1 | 1 | **1** |
| 0 | 1 | 1 | 1 | 0 | **1** |
| 1 | 0 | 0 | 0 | 0 | **0** |
| 1 | 0 | 1 | 0 | 0 | **0** |
| 1 | 1 | 0 | 0 | 1 | **1** |
| 1 | 1 | 1 | 0 | 0 | **0** |

检查：两项都含 `AND Q`，所以 Q = 0 的四行（1、2、5、6 行）必为 0 ✓；Q = 1 时，P = 0 或 R = 0 就输出 1，只有 P = 1、R = 1 那行（第 8 行）为 0 ✓。

**与 MS 对齐**　MS 的 Y 列为 0 0 1 1 / 0 0 1 0，前 4 行一分、后 4 行一分。

**英文作答句**　（填表题无文字作答。）

**直观**　真值表就是“把八种输入情况全部试一遍”。中间列像做算术时的竖式：每一步只做一次运算，错了也能一眼找到在哪一步。

**迁移与卡点**
- **卡点**：NOT 的作用范围。`NOT P AND Q` 里 NOT 只管 P；`NOT (A AND …)` 里 NOT 管整个括号——先给表达式分层编号，最外层的运算最后算。心算直接填 X 列，是整组四行一起丢的主因。
- **考官在换什么**：输入个数（2 或 3）、来源（表达式还是电路图）、输出列数、是否改错。给分永远按行块（前四行 / 后四行）或按列。
- **从代表题到变式**：代表题两项用 OR 合并；变式 NOT 套在最外层——中间列从 `B XOR C` 开始，再 `A AND (…)`，最后整列取反。搬过去的是“每个运算开一列”；要多做的是最后一步整列翻转。
- **反例**：输入列的顺序看错（P、Q、R 对应哪一列）；NAND 按 AND 算完忘了翻转。

**下一道变式**　⟦9618_s25_12:4(b)⟧　（`X = NOT (A AND (B XOR C))`：NOT 套在最外层；先算 `B XOR C` 列。）

<!-- auto:drills P1-LG-04 -->

### P1-LG-05　由真值表写逻辑表达式　{#P1-LG-05}

<!-- auto:stats P1-LG-05 -->

**考法**　①写出给定真值表的逻辑表达式（1–2 分）；②四个表达式里勾出与真值表一致的那个；③三张真值表与三个（或更多）表达式连线配对。

**识别信号**　Write the logic expression / logic statement for this / the following truth table；Tick one box to identify the correct logic statement for this truth table；Draw one line to match each truth table with its logic expression。

**解题思路**
1. **积之和（sum of products）——万能法**：
   - 找出输出为 1 的所有行。
   - 每一行写一个 AND 项：输入是 1 就写字母，是 0 就写 `NOT` 字母。例：R = 1、S = 1、T = 0 → `(R AND S AND NOT T)`。
   - 用 OR 把所有项连起来。
2. **先看有没有捷径**：输出列是否和某一个输入列完全相同或完全相反（⟦9618_s23_13:1(a)⟧ 的输出就是 B 列取反，答案 `NOT B`）；是否只取决于两个输入（例如 A、B 相同时为 1 → `NOT (A XOR B)`）。捷径写出来更短，但不确定时用积之和最稳。
3. **选择/连线题不要正推**：把每个选项代入两三行“有特点”的行（输出为 1 的行、全 0 行、全 1 行）检验，排除不符的。
4. 写完用 LG-04 的方法把表达式代回八行核对一遍。

**得分表述**（引自对应 MS）
- 「One correct term: (R AND S AND NOT T)」⟦9618_w25_11:3(b)⟧
- 「Second correct term plus the OR in correct place」⟦9618_w25_11:3(b)⟧
- 「Q = (R AND S AND NOT T) OR (NOT R AND NOT S AND T)」⟦9618_w25_11:3(b)⟧
- 「(NOT A AND NOT B AND NOT C) OR (NOT A AND NOT B AND C)」⟦9618_s26_12:8(b)⟧
- 「(A XOR B) NOR C」⟦9618_s24_11:1(a)⟧

**易错与失分**
- 用输出为 0 的行写项：积之和只取输出为 1 的行。
- 项里漏写一个输入：`(R AND S)` 会把 R = 1、S = 1、T = 1 那行也变成 1。三输入题的每个项都要写全三个字母（除非你已确认可以化简）。
- 项与项之间用了 AND：项之间一定是 OR。
- 只有一个 1 的表：答案只有一个 AND 项，不需要 OR。

#### 代表题精讲　⟦9618_w25_11:3(b)⟧

**在考什么**　Write the logic expression for the following truth table（输入 R、S、T，输出 Q）。2 分：每个正确的项 1 分，第二分还要求 OR 放对位置。

**完整作答**
1. 输出 Q = 1 的行只有两行：R S T = 0 0 1 和 1 1 0。
2. 第一行：R = 0、S = 0、T = 1 → `(NOT R AND NOT S AND T)`。
3. 第二行：R = 1、S = 1、T = 0 → `(R AND S AND NOT T)`。
4. 用 OR 连接：`Q = (R AND S AND NOT T) OR (NOT R AND NOT S AND T)`。
5. 核对：两个项各只在自己那一行为 1，其他六行都是 0 ✓。

**与 MS 对齐**　第 1 分 ←“One correct term: (R AND S AND NOT T)”（或另一个项）；第 2 分 ←“Second correct term plus the OR in correct place”。

**英文作答句**　Q = (R AND S AND NOT T) OR (NOT R AND NOT S AND T)

**直观**　积之和就像点名：“当 R、S 在而 T 不在时亮灯，或者当 R、S 都不在而 T 在时亮灯。”每个 AND 项精确描述一种情况，OR 把这些情况列成清单。

**下一道变式**　⟦9618_s24_11:1(a)⟧　（勾选题：四个候选表达式里选一个，用代入行检验来排除。）

<!-- auto:drills P1-LG-05 -->

### P1-LG-06　由问题描述建立逻辑表达式　{#P1-LG-06}

<!-- auto:stats P1-LG-06 -->

**考法**　给一个情境（温室自动窗、安保系统的灯和警报）和四栏参数表（Parameter / Description of parameter / Binary value / Condition），再用文字列出输出为 1 的条件；要求写逻辑表达式，或直接画电路。可能有两个输出（X、Y）。

**识别信号**　… operates according to the following criteria；四栏参数表，每个参数两行（1 和 0 各代表什么）；The window opens (X = 1) if: … and … or …。

**解题思路**
1. **翻译每个条件**：对照参数表，把每个条件写成“字母”或“NOT 字母”。条件正好是 1 那一行的含义 → 写字母；是 0 那一行的含义 → 写 `NOT` 字母。例：“wind speed is acceptable”而 W = 1 表示 Too high → `NOT W`。
2. **按文字结构组合**：条目之间的 and 用 AND，条目内部的 or 用 OR；**一个条目内部的 or 整体加括号**，再与其他条目 AND。“one or more of …”就是把它们全部 OR 起来。
3. 写成表达式；若要画电路，再按 LG-02 画。
4. 核对：随便取一个应输出 1 的情况代入，看表达式是否得 1。

**得分表述**（引自对应 MS）
- 「X = E AND A AND C」⟦9618_w24_11:5(b)⟧
- 「Y = E AND (B OR C OR D)」⟦9618_w24_11:5(b)⟧
- 「1 mark for T AND NOT W」⟦9618_w22_12:3(a)⟧
- 「1 mark for NOT R OR NOT M」⟦9618_w22_12:3(a)⟧
- 「1 mark for final AND」⟦9618_w22_12:3(a)⟧

**易错与失分**
- 忽略 0/1 的含义：“rain is not detected”是 `NOT R`，“manual override is off”是 `NOT M`——都对应参数表里的 0。
- or 的范围没括起来：`E AND B OR C OR D` 会被读成 `(E AND B) OR C OR D`，系统关着时有人靠近也会报警。
- 把不相关的参数也写进去：只用条件里提到的参数（⟦9618_w24_11:5(b)⟧ 的灯 X 不涉及门 B、D）。

#### 代表题精讲　⟦9618_w22_12:3(a)⟧

**在考什么**　温室自动窗 X。参数：T 温度（1 = Too high）、W 风速（1 = Too high）、R 雨（1 = Detected）、M 手动超控（1 = On）。窗打开（X = 1）当：温度过高**且**风速可接受，**且**没有检测到雨**或**手动超控关闭。要求画电路，3 分（讲解时请对照原卷 QP p.4 的参数表）。

**完整作答**
1. “温度过高” → `T`；“风速可接受”是 W = 0 → `NOT W`；合起来 `T AND NOT W`。
2. “没有检测到雨” → `NOT R`；“手动超控关闭” → `NOT M`；两者是 or → `NOT R OR NOT M`（这一块整体是一个括号）。
3. 两个条目 and：`X = (T AND NOT W) AND (NOT R OR NOT M)`。
4. 画电路：NOT 门接 W，与 T 进 AND；NOT 门接 R、NOT 门接 M，两者进 OR；AND 与 OR 的输出进最后一个 AND，输出 X。共 3 个 NOT、2 个 AND、1 个 OR。

**与 MS 对齐**　“T AND NOT W”1 分 →“NOT R OR NOT M”1 分 →“final AND”1 分，正好对应上面的三步。

**英文作答句**　X = (T AND NOT W) AND (NOT R OR NOT M)

**下一道变式**　⟦9618_w24_11:5(b)⟧　（安保系统：两个输出，只写表达式；注意“one or more doors are open, or a person is detected”要整体括起来。）

<!-- auto:drills P1-LG-06 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| LG-02 vs LG-03 | 给表达式画电路 → LG-02；给电路写表达式 → LG-03 | “Draw a logic circuit” 还是 “Write the logic expression for the … circuit” |
| LG-04 vs LG-05 | 由表达式/电路填输出列 → LG-04；由已填好的真值表反推表达式 → LG-05 | 真值表的输出列是空的还是填好的 |
| LG-06 vs LG-02/LG-03 | 起点是文字条件 + 参数表 → LG-06；起点是现成表达式或电路图 → LG-02/LG-03 | 有没有 “operates according to the following criteria” 和四栏参数表 |
| LG-01 vs LG-04 | 单个门的四行表 → LG-01；多个门组合的八行表 → LG-04 | 两输入还是三输入、有没有 Working space |
| NAND vs NOR | NAND：只有 11 输出 0；NOR：只有 00 输出 1 | 想清楚“唯一特殊行”在哪 |
| OR vs XOR | 11 时 OR 输出 1、XOR 输出 0 | 题目描述里有没有 “different” / “only one” |
| `NOT A AND B` vs `NOT (A AND B)` | 前者只把 A 取反；后者对 AND 的结果取反（= `A NAND B`） | 看 NOT 后面有没有括号 / 图上 NOT 在输入线上还是门后 |
