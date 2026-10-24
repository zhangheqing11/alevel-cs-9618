## BL　布尔代数与逻辑电路 {#ch-BL}

<!-- auto:chapter-stats -->

### 核心思想

BL 对应考纲 15.2，是 P1 逻辑门章（LG）的 A2 加深版。P1 用 `A AND B` 这样的文字写法，P3 换成布尔代数记号，并多了三样新工具：**积之和、卡诺图、布尔代数化简**。几乎每卷都有一道 8–10 分的组合题，按固定流水线往下问：

```
BL-01 电路 → 真值表 ──► BL-04 真值表 / 电路 → 积之和（不化简）
                                │
                                ▼
                     BL-05 填卡诺图 ──► BL-06 圈组 → 化简积之和
                                                │
                                                ▼
                                   BL-07 布尔代数 → 最简形式
                                   （另一种问法：直接给式子，用德摩根定律化简）
```

旁支两型：**BL-02 半加器 / 全加器**（认出电路、说出输出用途）、**BL-03 触发器**（画 SR 触发器、说明作用）。核验语料里各只出现在一份卷上，但考纲点名，写法固定。

**记号**（与 MS 一致）

| 记号 | 含义 | 例 |
|:--|:--|:--|
| `.` | AND（积） | A.B |
| `+` | OR（和） | A + B |
| 字母上的横线 | NOT | A̅ 读作 NOT A |
| 跨几个字母的长横线 | 对整个式子取反 | 本手册在纯文本里写成 NOT(A.B)；在卷面上照原样画一条长横线 |

本手册用 A̅、B̅、C̅、D̅ 表示单个变量取反。抽取出的 MS 文本把横线全部丢了，所以本章“完整作答”里的表达式都是看原页抄下、并按真值表验算过的。

**布尔代数定律表**（BL-07 要写出每一步用了哪条；名称用 MS 里出现过的叫法）

| 定律 | AND 形式 | OR 形式 |
|:--|:--|:--|
| Identity（单位律） | A.1 = A | A + 0 = A |
| Null（零律） | A.0 = 0 | A + 1 = 1 |
| Idempotent（等幂律） | A.A = A | A + A = A |
| Complement（互补律） | A.A̅ = 0 | A + A̅ = 1 |
| Double negation（双重否定） | NOT(A̅) = A | |
| Commutative / Associative（交换 / 结合） | A.B = B.A | A + B = B + A |
| Distributive（分配律） | A.(B + C) = A.B + A.C | A + B.C = (A + B).(A + C) |
| Absorption（吸收律） | A.(A + B) = A | A + A.B = A |
| Redundancy（冗余律） | A.(A̅ + B) = A.B | A + A̅.B = A + B |
| De Morgan（德摩根） | NOT(A.B) = A̅ + B̅ | NOT(A + B) = A̅.B̅ |

德摩根一句话：**横线断开，符号变号**（`.` 变 `+`，`+` 变 `.`）。只断横线不变号是考官报告点名的错误。

### 题型树
<!-- auto:type-tree -->

### P3-BL-01　由逻辑电路完成真值表　{#P3-BL-01}

<!-- auto:stats P3-BL-01 -->

**考法**　给出 3 或 4 个输入的电路（常有三输入门，中间结点标 P、Q、R、S），完成真值表，3 分；题目写 Show your working 时 Working space 里每个中间结点一列。也有不标中间结点、只填输出 Z 的（按行块给分），和 2 输出的小电路（每列 1 分）。

**识别信号**　The diagram shows a logic circuit. Complete the truth table for the given logic circuit. Show your working；表头 A B C (D) | P Q R S | Z，中间几列在 “Working space” 下面。

**解题思路**
1. **先认门、写出每个结点的式子**：从输入往输出，每个门一行，例如 P = B̅、Q = A.B.C。注意三输入门（三个输入一起 AND / OR / NAND / NOR）、XOR（不同为 1），以及同一输入线分叉到几个门（看黑点）。
2. **逐列填，不逐行填**：先把 P 整列填完，再 Q、R、S，最后 Z。整列填时只要记住一种门的规则，出错少。
3. **用快捷判断**：AND 列先找“全 1”的行，其余全 0；OR 列先找“全 0”的行，其余全 1；XOR 看两输入是否不同。
4. **核对**：Z 列的 1 的个数与你下一问（BL-04）的积项个数相同；中间列不能空格。

**得分表述**（引自对应 MS）
- 「One mark for working, all four columns P, Q, R and S」⟦9618_s24_31:6(a)⟧
- 「One mark for first four rows of column Z」⟦9618_s24_31:6(a)⟧
- 「One mark for first eight rows of column Z (Shaded)」⟦9618_s25_32:7(a)⟧
- 「One mark for every shaded block of rows for column Z correct (Max 3)」⟦9618_w23_31:6(a)⟧
- 「1 mark per correct output column」⟦9618_s22_32:6(a)⟧

**易错与失分**
- 只填 Z、不填中间列：考官报告指出要连同全部正确的中间列一起完成才能拿满分（⟦9618_s24_31:6(a)⟧ 的考官报告）。Working 那 1 分要求 P、Q、R、S **四列全对**。
- 中间某一列错一格：考官报告指出常见的失分是某几列里有个别错误（⟦9618_w25_31:6(a)⟧ 的考官报告）。错的中间列会一路传到 Z。
- 三输入门当成两输入门：三输入 AND 要三个都是 1，三输入 NOR 要三个都是 0（⟦9618_w23_32:7(a)⟧ 就是三输入 NOR）。
- 给分档按该题 MS：有的按“前 4 行 / 后 4 行”，有的按阴影行块，16 行的表按“前 8 行 / 后 8 行”。每一块都要对才拿那一分。

#### 代表题精讲　⟦9618_s24_31:6(a)⟧

**在考什么**　三输入 A、B、C 的电路，中间结点 P、Q、R、S，输出 Z；Complete the truth table. Show your working. 3 分。讲解时请对照原卷 QP p.6（电路图与真值表在同一页）。

**第一步：认门**（看原图）
- P = B̅（B 经过一个 NOT 门）
- Q = A.B.C（三输入 AND：A、B、C）
- R = A.P.C，即 A.B̅.C（三输入 AND：A、P、C）
- S = A XOR P（XOR 门：A 与 P）
- Z = Q + R + S（三输入 OR）

**完整作答**

| A | B | C | P | Q | R | S | Z |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 |

逐列怎么来：P 是 B 取反；Q 只有 111 一行为 1；R 要 A = 1、P = 1（B = 0）、C = 1，只有 101 一行；S 在 A 与 P 不同时为 1（000、001：A = 0、P = 1；110、111：A = 1、P = 0）；Z 是 Q、R、S 中任一为 1。

**与 MS 对齐**　三个独立得分点：「One mark for working, all four columns P, Q, R and S」⟦9618_s24_31:6(a)⟧（四列全对才给）；「One mark for first four rows of column Z」⟦9618_s24_31:6(a)⟧（Z = 1、1、0、0）；第二个四行块 1 分（Z = 0、1、1、1）。上表与 MS 的表逐格相同。

**直观**　真值表是给电路“拍 8 张快照”：每一行把开关拨到一种组合，看每个结点的灯亮不亮。逐列填就像一次只看一盏灯。

**下一道变式**　⟦9618_w25_31:6(a)⟧　（P、Q 各是一个 NOT 门；R、S 是三输入 OR；Z 是三输入 AND，而且 B 直接接到 Z——所以 B = 0 的四行 Z 一定是 0。）

<!-- auto:drills P3-BL-01 -->

### P3-BL-02　半加器与全加器　{#P3-BL-02}

<!-- auto:stats P3-BL-02 -->

**考法**　先完成电路的真值表（BL-01），再问：①说出电路的名称（1 分）；②说出每个输出的用途（每个 1 分）；扩展语料里还有③写出两个输出的积之和并说明用途（4 分）。核验语料只在 ⟦9618_s22_32:6(b)(i)⟧、⟦9618_s22_32:6(b)(ii)⟧ 出现。

**识别信号**　State the name of this logic circuit；State the purpose of each output；两个输入、两个输出，一个 XOR 加一个 AND（半加器）；三个输入、两个输出（全加器）。

**解题思路**
1. **半加器**：两个 1 位二进制数 A、B 相加。和位 Sum = A XOR B（A.B̅ + A̅.B），进位 Carry = A.B。真值表：00→0 0，01→1 0，10→1 0，11→0 1（Sum、Carry）。
2. **全加器**：三个输入（A、B 和低位送来的进位 Cin）。Sum 在输入里有**奇数个** 1 时为 1；Carry out 在输入里**至少两个** 1 时为 1。它由两个半加器加一个 OR 门组成。
3. **认电路**：看见 XOR 与 AND 接在同样两个输入上 → 半加器；看见三个输入、输出一个是“奇数个 1”、一个是“至少两个 1” → 全加器。
4. **写用途**：一个输出是和位（sum），另一个是进位（carry）。写全称词 sum / carry，不要只写 “adds”。
5. 要写积之和（扩展语料 ⟦9618_s21_31:7(c)⟧）时，按 BL-04 的方法逐行写：全加器的 Sum = A̅.B̅.C + A̅.B.C̅ + A.B̅.C̅ + A.B.C，Carry = A̅.B.C + A.B̅.C + A.B.C̅ + A.B.C（由全加器真值表推出）。

**得分表述**（引自对应 MS）
- 「Half adder」⟦9618_s22_32:6(b)(i)⟧
- 「Purpose of E: Sum」⟦9618_s22_32:6(b)(ii)⟧
- 「Purpose of F: Carry」⟦9618_s22_32:6(b)(ii)⟧
- 「Full adder」⟦9618_s21_31:7(b)⟧
- 「Purpose: Carry output」⟦9618_s21_31:7(c)⟧

**易错与失分**
- 名称写成 “adder” 不写 half / full：MS 只列出 Half adder，要写全。
- 两个输出的用途写反：XOR 那个是和位，AND 那个是进位（1 + 1 = 10，进位是 1、和位是 0）。
- 把全加器当成“两个半加器”就停：作答名称写 full adder；结构说明只在题目问时写。

#### 代表题精讲　⟦9618_s22_32:6(b)(ii)⟧

**在考什么**　两输入 A、B，两输出 E、F 的电路；(a) 先填真值表，(b)(i) 说出电路名称，(b)(ii) State the purpose of each output E and F，2 分。讲解时请对照原卷 QP p.9（电路：A、B 同时接到一个 XOR 门〔输出 E〕和一个 AND 门〔输出 F〕）。

**完整作答**
- (a) 真值表：A B = 00 → E F = 0 0；01 → 1 0；10 → 1 0；11 → 0 1。
- (b)(i) Half adder。
- (b)(ii) Purpose of E：sum（两个位相加的和位）。Purpose of F：carry（进位）。

**与 MS 对齐**　(a)「1 mark per correct output column」⟦9618_s22_32:6(a)⟧，E 列、F 列各 1 分；(b)(i)「Half adder」⟦9618_s22_32:6(b)(i)⟧；(b)(ii) 两个独立得分点「Purpose of E: Sum」⟦9618_s22_32:6(b)(ii)⟧ 与「Purpose of F: Carry」⟦9618_s22_32:6(b)(ii)⟧。

**英文作答句**　(b)(i) Half adder. (b)(ii) E is the sum bit of A + B; F is the carry bit.

**直观**　手算 1 + 1：写 0 进 1。半加器就是这一步的电路：E 写下“这一位是几”，F 记下“要不要往前进 1”。全加器多了一个输入，用来接住低位送来的进位，所以能一位一位串起来做多位加法。

**下一道变式**　⟦9618_s21_31:7(c)⟧　（2021 扩展题。换成全加器：三个输入 A、B、C，P = A XOR B、Y = P XOR C、Q = A AND B、R = P AND C、Z = Q OR R；写出 Y、Z 的积之和并各说出用途，4 分，每个表达式、每个用途各 1 分。先做 ⟦9618_s21_31:7(a)⟧ 的真值表、⟦9618_s21_31:7(b)⟧ 说出电路名称，再按上面第 5 步逐行写积项。讲解时对照原卷 QP p.9。）

<!-- auto:drills P3-BL-02 -->

### P3-BL-03　触发器（SR、JK）　{#P3-BL-03}

<!-- auto:stats P3-BL-03 -->

**考法**　①画出 SR 触发器的逻辑电路并标出输入（4 分）；②说明触发器的作用（1 分）。核验语料只在 w22/32 出现。考纲 15.2 还要求 JK 触发器与触发器真值表，语料里尚未出现，下面按标准定义补充（非 MS）。

**识别信号**　Draw a logic circuit for an SR flip-flop and label the inputs（作答框右边已印好 Q 与 Q̅ 两个输出，左边两条输入线留空让你标）；State the purpose of a flip-flop。

**解题思路**
1. **两个同种门**：两个 NOR，或两个 NAND，不能混用。每个门两个输入、一个输出。
2. **交叉反馈**：每个门的输出接回另一个门的一个输入。
3. **接法与标注**（按 MS 两个范例）：
   - NOR 版：上门输入 = R（Reset）和下门的输出，上门输出 = Q；下门输入 = S（Set）和上门的输出，下门输出 = Q̅。
   - NAND 版：上门输入 = S（Set）和下门的输出，上门输出 = Q；下门输入 = R（Reset）和上门的输出，下门输出 = Q̅。
   - 记法：NOR 版“R 在 Q 那边”，NAND 版“S 在 Q 那边”。
4. **作用**：存储一个二进制位（1 bit）——它是存储器 / 寄存器的基本单元。
5. **SR 真值表**（NOR 版，非 MS）：S = 1、R = 0 → Q = 1（置位）；S = 0、R = 1 → Q = 0（复位）；S = 0、R = 0 → Q 保持原值（存储）；S = 1、R = 1 → 无效状态（Q 与 Q̅ 同为 0）。NAND 版输入为低电平有效（0 时起作用）。
6. **JK 触发器**（非 MS）：多一个时钟输入；J 相当于 S、K 相当于 R；J = K = 0 保持，J = 1、K = 0 置位，J = 0、K = 1 复位，J = K = 1 时输出翻转（toggle）——它解决了 SR 的 S = R = 1 无效状态。

**得分表述**（引自对应 MS）
- 「One correct NAND or NOR gate with two separate inputs and one output」⟦9618_w22_32:8(a)⟧
- 「Second correct logic gate of same type as first with two separate inputs and one output」⟦9618_w22_32:8(a)⟧
- 「Correct connections between logic gates」⟦9618_w22_32:8(a)⟧
- 「Correctly labelled inputs」⟦9618_w22_32:8(a)⟧
- 「To store a binary digit / (single) bit」⟦9618_w22_32:8(b)⟧

**易错与失分**
- 用了其他门，或一个 NAND 一个 NOR：考官报告指出正确答案只用两个 NAND 或两个 NOR，同时见到很多不对的门（⟦9618_w22_32:8(a)⟧ 的考官报告）。
- 没有交叉反馈：考官报告指出正确的连接是每个门的输出回到另一个门作为一个输入（⟦9618_w22_32:8(a)⟧ 的考官报告）。
- S、R 标反：考官报告指出 Set、Reset 的上下顺序取决于用的是哪种门（⟦9618_w22_32:8(a)⟧ 的考官报告）。按上面的记法标。

#### 代表题精讲　⟦9618_w22_32:8(a)⟧

**在考什么**　Draw a logic circuit for an SR flip-flop and label the inputs. 4 分（MS 四点 Max 4）。讲解时请对照原卷 QP p.7（作答框，右侧已印 Q、Q̅）与 MS p.10–11（NAND、NOR 两个范例图）。

**完整作答**（NOR 版，文字描述连线；卷面上画图）

| 门 | 输入 1 | 输入 2 | 输出 |
|:--|:--|:--|:--|
| 上方 NOR 门 | R（Reset，左上输入线） | 下方门的输出 Q̅ | Q |
| 下方 NOR 门 | S（Set，左下输入线） | 上方门的输出 Q | Q̅ |

两条反馈线在两门之间交叉成一个 “X”。左上的空标 Reset，左下的空标 Set。

（NAND 版：两个门换成 NAND，左上标 Set、左下标 Reset，其余连线相同。）

**与 MS 对齐**　四个独立得分点：「One correct NAND or NOR gate with two separate inputs and one output」⟦9618_w22_32:8(a)⟧（第一个 NOR）；「Second correct logic gate of same type as first with two separate inputs and one output」⟦9618_w22_32:8(a)⟧（第二个也是 NOR）；「Correct connections between logic gates」⟦9618_w22_32:8(a)⟧（交叉反馈）；「Correctly labelled inputs」⟦9618_w22_32:8(a)⟧（NOR 版 R 在上、S 在下，与 MS 的 NOR 范例一致）。

**直观**　两个门互相“拉着对方的手”：一个输出 1 就让另一个输出 0，反过来又锁住自己——松开 S、R 之后状态还在，这就是“记住一位”。

**下一道变式**　核验语料没有第二道（同卷 ⟦9618_w22_32:8(b)⟧ 问作用：存储一个二进制位）。自练：画出 NAND 版 SR 触发器并标输入；写出 SR（NOR 版）四行真值表与 JK 四行真值表，与上面第 5、6 步对照（无 MS，按教材核对）。

<!-- auto:drills P3-BL-03 -->

### P3-BL-04　由真值表或电路写积之和表达式　{#P3-BL-04}

<!-- auto:stats P3-BL-04 -->

**考法**　①给真值表，Write the Boolean logic expression … as the sum-of-products（2–3 分）；②给电路（常是 BL-01 刚填完表的那个），写它的积之和（1–2 分）。给分档按该题 MS：每两个正确积项 1 分、全对才满分，或“全对 2 分 / 对三项 1 分”。

**识别信号**　Write the Boolean (logic) expression that corresponds to the given truth table / logic circuit as the (a) sum-of-products；答题线以 `Z =` / `T =` / `X =` 开头。

**解题思路**
1. 在真值表输出列里圈出**所有为 1 的行**（电路题：先用 BL-01 的真值表）。
2. 每一行写一个**积项**：该行每个输入都要出现；输入为 1 写原变量，为 0 写取反。例：A B C D = 0 1 0 1 → A̅.B.C̅.D。
3. 用 `+` 把所有积项连起来。**不化简**——题目要的是积之和本身。
4. 核对：积项个数 = 输出为 1 的行数；没有重复项、没有多余项。

**得分表述**（引自对应 MS）
- 「One mark for every two correct products (Max 3)」⟦9618_w24_31:7(a)⟧
- 「Two marks for all five correct terms and no extras」⟦9618_s24_31:6(b)⟧
- 「One mark for any three correct terms」⟦9618_s24_31:6(b)⟧
- 「Three marks for all eight correct products and no additional products」⟦9618_w24_32:6(a)⟧
- 「One mark for correct answer (terms may be in any order)」⟦9618_s25_32:7(b)⟧

**易错与失分**
- 动手化简：考官报告指出直接写出正确积项、不去化简的考生拿到了分（⟦9618_s24_31:6(b)⟧、⟦9618_s24_32:6(b)⟧ 的考官报告）。积之和题只写积项。
- 漏项或重复项：考官报告指出 2 分的答案通常是漏了一项以上或有一项重复（⟦9618_w24_32:6(a)⟧ 的考官报告）；考官报告还指出只有六项全对才拿 3 分（⟦9618_w24_31:7(a)⟧ 的考官报告）。
- 取反写错位置：每个积项里只有“该行为 0 的输入”加横线；横线要清楚地只盖住一个字母。
- 写成输出为 0 的行：积之和只取输出为 **1** 的行。

#### 代表题精讲　⟦9618_w24_31:7(a)⟧

**在考什么**　四输入 A、B、C、D，输出 T 的真值表；Write the Boolean logic expression that corresponds to the given truth table as the sum-of-products. 3 分。讲解时请对照原卷 QP p.6（真值表）。

**完整作答**　T = 1 的六行是 0001、0011、1001、1011、1101、1111：

T = A̅.B̅.C̅.D + A̅.B̅.C.D + A.B̅.C̅.D + A.B̅.C.D + A.B.C̅.D + A.B.C.D

**与 MS 对齐**　「One mark for every two correct products (Max 3)」⟦9618_w24_31:7(a)⟧：六个积项，每两个对 1 分，三分要六项全对。上式与 MS p.8 印的六项相同（顺序不限）。

**直观**　积之和就是把“哪些情况灯会亮”一条一条列出来：每个积项描述一种完整的开关组合，`+` 表示“这几种情况里任何一种发生都亮”。

**下一道变式**　⟦9618_s23_32:9(a)⟧　（同样是 16 行真值表、六个 1：数清楚六行，每两项 1 分。）

<!-- auto:drills P3-BL-04 -->

### P3-BL-05　填写卡诺图　{#P3-BL-05}

<!-- auto:stats P3-BL-05 -->

**考法**　按给定的真值表或积之和表达式，填 3 变量（2 × 4）或 4 变量（4 × 4）卡诺图，2 分：全对 2 分、错一格 1 分。偶尔问使用卡诺图的好处（1 分）。

**识别信号**　Complete the Karnaugh map (K-map) for the given truth table / for the (following) Boolean expression；空图的行列标签是 00、01、11、10；Describe one benefit of using a Karnaugh map。

**解题思路**
1. **认清行列**：看图左上角的斜线——斜线上方的变量（如 AB）是列，下方的（如 CD）是行。行列标签按**格雷码**顺序 00、01、11、10（相邻两格只差一位），第三列是 11 不是 10。
2. **一项一格**：四个变量都出现的积项对应一格。例：A̅.B.C̅.D → 列 AB = 01、行 CD = 01。从真值表填时，输出为 1 的行逐行找格。
3. **缺变量的项占多格**：如在 4 变量图里填 A.B.C̅（缺 D），就填列 AB = 11、行 CD = 00 与 01 两格。
4. **其余每格写 0**：考官报告一再强调整张图要用 0 和 1 填满，不留空、不用其他符号。
5. **核对**：图里 1 的个数 = 真值表里输出为 1 的行数（或积项个数，无缺变量时）。
6. **好处**：不用布尔代数也能化简；保证得到最优解；把复杂的逻辑问题变简单。

**得分表述**（引自对应 MS）
- 「Two marks if no errors present」⟦9618_s23_31:7(a)⟧
- 「One mark if one error present」⟦9618_s23_31:7(a)⟧
- 「One mark if only one error present」⟦9618_w25_31:6(b)(i)⟧
- 「It is guaranteed to give you an optimal solution」⟦9618_s26_31:6(b)⟧
- 「Converts complex logic problems into simpler ones」⟦9618_s26_31:6(b)⟧

**易错与失分**
- 只填 1、其余留空：考官报告指出只有全图用 0 和 1 填满、不留空、不用别的符号才拿满分（⟦9618_s23_31:7(a)⟧、⟦9618_w25_31:6(b)(i)⟧ 的考官报告）。
- 1 填错格：考官报告建议数一数图里 1 的个数是否与表达式一致（⟦9618_w25_31:6(b)(i)⟧ 的考官报告）。另一种常见的错是按二进制顺序把第三列当成 10（第三列是 11；这条是教学经验，考官报告没有提）。
- 行列弄反：先看斜线两边的变量名，再下笔。

#### 代表题精讲　⟦9618_s23_31:7(a)⟧

**在考什么**　Complete the Karnaugh map (K-map) for the following Boolean expression：Z = A̅.B̅.C̅.D̅ + A̅.B̅.C̅.D + A̅.B.C̅.D̅ + A̅.B.C̅.D + A.B.C̅.D̅ + A.B.C̅.D。图的列为 AB、行为 CD。2 分。讲解时请对照原卷 QP p.8（表达式与空图）。

**完整作答**　六个积项各对应一格：

| 积项 | AB（列） | CD（行） |
|:--|:-:|:-:|
| A̅.B̅.C̅.D̅ | 00 | 00 |
| A̅.B̅.C̅.D | 00 | 01 |
| A̅.B.C̅.D̅ | 01 | 00 |
| A̅.B.C̅.D | 01 | 01 |
| A.B.C̅.D̅ | 11 | 00 |
| A.B.C̅.D | 11 | 01 |

| CD \ AB | 00 | 01 | 11 | 10 |
|:-:|:-:|:-:|:-:|:-:|
| 00 | 1 | 1 | 1 | 0 |
| 01 | 1 | 1 | 1 | 0 |
| 11 | 0 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 | 0 |

**与 MS 对齐**　「Two marks if no errors present」⟦9618_s23_31:7(a)⟧，「One mark if one error present」⟦9618_s23_31:7(a)⟧：上图与 MS p.6 的图逐格相同；十个 0 也要写上。

**英文作答句**　（填图题无作答句。好处题可写：）Using a K-map is guaranteed to give an optimal solution, and it converts a complex logic problem into a simpler one without needing Boolean algebra.

**直观**　卡诺图是把真值表“折”成一张方格纸：格雷码排法让上下左右相邻的格子只差一个变量，后面圈组时，相邻的 1 才能合并。

**下一道变式**　⟦9618_w24_32:6(b)⟧　（由同题 (a) 的真值表填 4 × 4 图：输出为 1 的八行恰好落在 CD = 01 和 CD = 10 两整行。）

<!-- auto:drills P3-BL-05 -->

### P3-BL-06　卡诺图圈组与化简积之和　{#P3-BL-06}

<!-- auto:stats P3-BL-06 -->

**考法**　两问成对：①Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products（2–3 分，每个正确的圈 1 分）；②Write the Boolean (logic) expression from your answer … as a simplified sum-of-products（1–2 分：任一项对 1 分，全部项与运算符对、没有多余项再 1 分）。题目常加 “Do not carry out any further simplification”。

**识别信号**　Draw loop(s) around appropriate group(s) … optimal sum-of-products；Write … as a (the) simplified sum-of-products。

**解题思路**
1. **圈的规则**
   - 只圈 1，不圈 0。
   - 每个圈里 1 的个数是 2 的幂：1、2、4、8（、16），并且是矩形（一行、一列、2 × 2、2 × 4 …）。
   - 圈要**尽量大**、圈的数目要**尽量少**；圈可以**重叠**。
   - 图的边缘是相连的：最左列与最右列相邻，最上行与最下行相邻（四个角也互相相邻）。
   - 每个 1 至少在一个圈里；一个 1 和谁都不相邻时，它自己就是一组（可以不画圈，但表达式里必须写它）。
2. **由圈写项**：看这个圈覆盖的格子里，哪些变量**始终不变**——不变为 1 写原变量，不变为 0 写取反；变了的变量丢掉。4 变量图里：8 格的圈剩 1 个变量，4 格剩 2 个，2 格剩 3 个，单格 4 个都要写。
3. 各项用 `+` 连起来，就是化简积之和。题目说 Do not carry out any further simplification 时到此为止（提公因式是 BL-07）。

**得分表述**（引自对应 MS）
- 「One mark for each correct loop (Max 2)」⟦9618_w24_31:7(c)⟧
- 「Any correct Boolean term」⟦9618_w24_31:7(d)(i)⟧
- 「Boolean terms and operator correct and no other terms present」⟦9618_w24_31:7(d)(i)⟧
- 「One correct Boolean term with a + / OR sign」⟦9618_w25_31:6(b)(iii)⟧
- 「All Boolean terms and operators correct and no other terms present」⟦9618_w25_31:6(b)(iii)⟧

**易错与失分**
- 一个大圈套住所有 1（6 个 1 不是 2 的幂），或把每两个 1 各圈一次：考官报告列出这两种错误（⟦9618_w22_31:7(b)⟧ 的考官报告）。考官报告还提醒圈里只能有 1、个数是 2、4、8（⟦9618_w25_31:6(b)(ii)⟧ 的考官报告）。
- 没想到边缘相连：左右两列的 1 可以合成一个圈（代表题就是）。
- 孤立的 1 不写进表达式：考官报告指出那个不在组里的 1 仍要出现在最终表达式里（⟦9618_w25_31:6(b)(iii)⟧ 的考官报告）。
- 写化简积之和时继续提公因式：考官报告指出直接按圈写、不再化简的考生拿到这一分（⟦9618_s24_31:6(c)(iii)⟧ 的考官报告）。

#### 代表题精讲　⟦9618_w24_31:7(c)⟧

**在考什么**　同题 (b) 已把真值表填进 4 × 4 卡诺图（列 AB、行 CD）。(c) Draw loop(s) around appropriate group(s) in the K-map to produce an optimal sum-of-products，2 分；接着 (d)(i) 写化简积之和，2 分（⟦9618_w24_31:7(d)(i)⟧）。讲解时请对照原卷 QP p.7（空图）与 MS p.9（带圈的图）。

**完整作答**

(b) 填好的图：

| CD \ AB | 00 | 01 | 11 | 10 |
|:-:|:-:|:-:|:-:|:-:|
| 00 | 0 | 0 | 0 | 0 |
| 01 | **1** | 0 | **1** | **1** |
| 11 | **1** | 0 | **1** | **1** |
| 10 | 0 | 0 | 0 | 0 |

(c) 两个四格圈：
- 圈 1：列 11 与 10 × 行 01 与 11（2 × 2 方块）。
- 圈 2：列 00 与 10 × 行 01 与 11——列 00 和列 10 隔着左右边缘相邻，这个圈从图的右边“绕”到左边。两个圈在列 10 重叠。

(d)(i) 由圈写项：
- 圈 1：A 始终为 1，B 变化，C 变化，D 始终为 1 → A.D。
- 圈 2：A 变化，B 始终为 0，C 变化，D 始终为 1 → B̅.D。

T = A.D + B̅.D

**与 MS 对齐**　(c)「One mark for each correct loop (Max 2)」⟦9618_w24_31:7(c)⟧：两个圈各 1 分，与 MS p.9 的图相同（MS 把绕边的圈画成左右两个半圈）。(d)(i)「Any correct Boolean term」⟦9618_w24_31:7(d)(i)⟧ 1 分；「Boolean terms and operator correct and no other terms present」⟦9618_w24_31:7(d)(i)⟧ 1 分。MS 写的是 A.D + B̅.D，两项顺序可互换。

**直观**　圈组就是在找“不管某个开关怎么拨灯都亮”的区域：圈 1 里不管 B、C 怎么变，只要 A 和 D 都是 1 灯就亮——所以 B、C 可以从这一项里删掉。

**下一道变式**　⟦9618_w25_31:6(b)(ii)⟧　（3 变量图：两个两格圈，外加一个和谁都不相邻的 1；接着 ⟦9618_w25_31:6(b)(iii)⟧ 写化简积之和时，那个单独的 1 要写成完整的三变量项。）

<!-- auto:drills P3-BL-06 -->

### P3-BL-07　布尔代数化简与德摩根定律　{#P3-BL-07}

<!-- auto:stats P3-BL-07 -->

**考法**　①给一个式子，Simplify … using Boolean algebra (including De Morgan’s laws). Show your working（3–4 分：每用对一条定律 1 分 + 最终答案 1 分）；②只对式子应用德摩根定律（1 分）；③把卡诺图得到的化简积之和 Use Boolean algebra to give your answer … in its simplest form（1 分，通常是提公因式）。

**识别信号**　Simplify the following expression using Boolean algebra, including De Morgan’s laws. Show your working / Show all the stages；Apply De Morgan’s laws to the expression；Use Boolean algebra to give your answer to part … in its simplest form。

**解题思路**
1. **先拆长横线**（有长横线时）：从最外层开始用德摩根——横线断开、`.` ↔ `+` 互换。每拆一层写一行。
2. **双重否定**：两条横线叠在一起就抵消（NOT(NOT X) = X）。
3. **整理**：分配律展开或提公因式；等幂律（A.A = A）、互补律（A + A̅ = 1、A.A̅ = 0）、单位律（A.1 = A）消项；吸收律（A + A.B = A）、冗余律（A + A̅.B = A + B）收尾。
4. **每行一步，写明定律名**：MS 按“用对一条定律”给分，写出中间行才能拿过程分。
5. **最简形式题**：两项有公因式就提出来，如 A̅.C̅ + B.C̅ = C̅.(A̅ + B)（⟦9618_s23_31:7(d)⟧）。

**得分表述**（引自对应 MS）
- 「Correct application of De Morgan’s Law」⟦9618_w22_32:8(c)⟧
- 「Correct application of Double Negation Law or Distributive Law」⟦9618_w22_32:8(c)⟧
- 「Correct application of Idempotent, Distributive or Absorption laws」⟦9618_s25_32:7(c)⟧
- 「One mark for correct working from points (Max 2)」⟦9618_w23_31:6(b)⟧
- 「One mark for simplest form (Max 1)」⟦9618_s23_31:7(d)⟧

**易错与失分**
- 德摩根只断横线、不变符号：考官报告指出常见错误是把盖住两项的长横线拆给每一项各一条，原来的 AND 却仍写 AND、没有改成 OR（⟦9618_w22_32:8(c)⟧ 的考官报告）。
- 化简没走到底：考官报告指出有些考生化简了一大半，却没到最简形式（⟦9618_w23_32:7(c)⟧ 的考官报告）。最后检查还能不能用吸收律、冗余律或提公因式。
- 只写答案：Show your working 的题过程分占大头，按 MS 只写答案最多拿答案那 1 分。
- 提醒：⟦9618_w24_31:7(d)(ii)⟧ 的 MS 把最简形式印成 D.(A.B̅)，这是官方笔误（决策 D41 ②）：由同题 (d)(i) 的 A.D + B̅.D 提公因式应得 D.(A + B̅)（按 7(a) 的真值表验算：T = 1 的六行都满足 D = 1 且 A = 1 或 B = 0）。教学按 D.(A + B̅)；给分仍按 MS，该点是「One mark for simplest form (Max 1)」⟦9618_w24_31:7(d)(ii)⟧，批改时按“最简形式”给这 1 分。

#### 代表题精讲　⟦9618_w22_32:8(c)⟧

**在考什么**　Simplify the following expression using Boolean algebra, including De Morgan’s laws. Show your working. 3 分（MS 三点：德摩根 1、双重否定或分配律 1、正确答案 1）。式子有三层横线，讲解时请对照原卷 QP p.7（式子）与 MS p.12（逐步过程）。

式子（纯文本写法）：X = NOT[ NOT(A̅.B̅) . NOT(A̅.C) . NOT(B.D) ]
——最外一条长横线盖住全部；里面三个括号各有自己的横线；A̅、B̅ 是单个变量的横线。

**完整作答**

```
  NOT[ NOT(A̅.B̅) . NOT(A̅.C) . NOT(B.D) ]
= NOT(NOT(A̅.B̅)) + NOT(NOT(A̅.C)) + NOT(NOT(B.D))     De Morgan's law
= A̅.B̅ + A̅.C + B.D                                   Double negation
= A̅.(B̅ + C) + B.D                                   Distributive law
```

**与 MS 对齐**　三个独立得分点：第一行「Correct application of De Morgan’s Law」⟦9618_w22_32:8(c)⟧（最外层横线断开，两个 `.` 变 `+`，每项头上留下两条横线）；第二行「Correct application of Double Negation Law or Distributive Law」⟦9618_w22_32:8(c)⟧（两条横线抵消）；第三行 Correct answer：MS 的最终答案是 A̅.(B̅ + C) + B.D。

**英文作答句**　Apply De Morgan's law to the outer bar (break the bar and change each AND to OR); apply the double negation law to remove the double bars; apply the distributive law to take out the common factor A̅.

**直观**　德摩根像“把否定分给每个人”：‘不是（甲和乙都来）’等于‘甲不来，或者乙不来’。横线一断开，“和”就变成“或”。

**下一道变式**　⟦9618_w23_31:6(b)⟧　（Y 的四个积项都含 A̅.D̅：先提公因式 A̅.D̅，括号里反复用互补律（C̅ + C = 1，再 B̅ + B = 1）化成 1，最终 Y = A̅.D̅。MS：过程 Max 2 + 答案 1。）

<!-- auto:drills P3-BL-07 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| BL-04 积之和 vs BL-06 化简积之和 | BL-04 每个输出为 1 的行一项、不化简；BL-06 由卡诺图的圈写项 | 题干有没有 simplified、前面有没有 K-map |
| BL-06 化简积之和 vs BL-07 最简形式 | 化简积之和按圈直接写、不提公因式；最简形式再用布尔代数提公因式 | “Do not carry out any further simplification” 还是 “in its simplest form” |
| 格雷码 00、01、11、10 vs 二进制 00、01、10、11 | 卡诺图的行列按格雷码；真值表的行按二进制 | 填卡诺图时第三列是 11 |
| 德摩根 NOT(A.B) vs A̅.B̅ | NOT(A.B) = A̅ + B̅（符号变号）；A̅.B̅ = NOT(A + B) | 长横线断开后中间的符号有没有变 |
| 半加器 vs 全加器 | 半加器两个输入（A、B）；全加器三个输入（A、B、进位输入） | 数输入个数 |
| SR 触发器 NOR 版 vs NAND 版 | NOR 版 R 在 Q 那边、高电平有效；NAND 版 S 在 Q 那边、低电平有效 | 看用的是哪种门 |
| SR vs JK 触发器 | JK 多时钟输入；J = K = 1 时翻转，没有 SR 的无效状态 | 题目点名 JK / 提到 clock |
| BL-01（P3）vs P1 LG-04 | 同样是电路 → 真值表；P3 的电路常有三输入门和 Working space 中间列 | 卷号：P3 的行一律用 P3 题型 |
