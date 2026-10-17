## PG　编程 {#ch-PG}

<!-- auto:chapter-stats -->

### 核心思想

PG 章考的是“读得懂、写得出”伪代码本身：语句、结构、模块，以及不靠数组和文件的那几类写模块大题。12 个题型分四块：

1. **读语句、写语句**（PG-01 至 PG-03，考纲 11.1）：认出一段代码里有哪些结构（打勾表）；按给定的值算表达式；往空里填插页函数或补一条语句。都是 Q1、Q2 的 1–5 分表格题，靠的是插页函数表和运算规则，一行一分。
2. **结构的改写与选择**（PG-04、PG-05，考纲 11.2）：CASE ↔ IF、把嵌套 IF 化简成几条独立的 IF；判断哪种循环最合适并说明理由。
3. **模块与良好习惯**（PG-06 至 PG-08，考纲 11.3）：为什么用子程序和库程序、过程与函数的区别、参数、局部与全局、BYVAL 与 BYREF；照说明或结构图写模块头；常量、注释、缩进与效率。
4. **写模块大题**（PG-09 至 PG-12）：数据不在数组和文件里，而在**键盘输入**（PG-09）、**参数里的几个数**（PG-10）、**字符串**（PG-11）、**日期**（PG-12）里。其中 PG-11 字符串处理是全卷分值最多的单个题型，几乎每卷都有一道 6–8 分的大题。

整章有两条主线：

- **插页是这一章的词典。** 函数名、参数个数与顺序、返回类型都以插页为准：`MID(S, 起点, 长度)`、`SETDATE(日, 月, 年)`、`DAYINDEX` 里星期日 = 1、`RAND(x)` 返回 0 到 x（不含 x）的实数。写错一个参数，这一分就没有。
- **写模块的得分链与 DT 章相同**：模块头 → 声明与初值 → 循环（到 LENGTH、到结束值、到找到为止）→ 循环里取值与判断 → 处理（计数、累加、拼接）→ 循环后返回或输出。PG 大题的“结构分”在中间两环：逐字符取值、比较、拼接、转换；其余几环每题都一样，是送分。

### 本章伪代码速查（2027–29 指南 + 插页写法）

```pseudocode
// selection
IF Mark >= 50 THEN
   Result ← "Pass"
ELSE
   Result ← "Fail"
ENDIF

CASE OF Mark
   80 TO 100 : Grade ← 'A'
   60 TO 79 : Grade ← 'B'
   OTHERWISE : Grade ← 'U'
ENDCASE

// modules: a procedure with a BYREF parameter, a function with RETURNS
PROCEDURE SplitTime(Total : INTEGER, BYREF Hours : INTEGER, BYREF Mins : INTEGER)
   Hours ← Total DIV 60
   Mins ← Total MOD 60
ENDPROCEDURE

FUNCTION IsInRange(Value : INTEGER) RETURNS BOOLEAN
   RETURN Value >= 24 AND Value <= 37
ENDFUNCTION

CALL SplitTime(135, H, M)          // a procedure call is a complete statement
OK ← IsInRange(30)                 // a function call is used in an expression, never with CALL

// strings (insert functions only)
ThisChar ← MID(Name, Index, 1)     // one character at position Index
Code ← LEFT(Line, 5)               // first 5 characters
Rest ← RIGHT(Line, LENGTH(Line) - 5)
NewString ← NewString & ThisChar   // & joins strings and chars
Upper ← TO_UPPER(ThisChar)
Text ← "Total: " & NUM_TO_STR(Total)
Num ← STR_TO_NUM("23.45")

// dates and random numbers
MyDOB ← SETDATE(17, 11, 2007)      // day, month, year
IF DAYINDEX(MyDOB) = 1 THEN        // Sunday = 1, Monday = 2 ...
   OUTPUT "Born on a Sunday"
ENDIF
Dice ← INT(RAND(6)) + 1            // random integer 1 to 6
```

### 题型树
<!-- auto:type-tree -->

### P2-PG-01　识别程序结构与语句成分　{#P2-PG-01}

<!-- auto:stats P2-PG-01 -->

**考法**　①打勾表：每行（或每段）伪代码含有哪些成分——selection、iteration、assignment、input/output、subroutine——一行可以勾几个，一行全对才得 1 分（4–5 分）；②看一段代码写行号：初始化语句、循环开始的行、逻辑运算、变量自增的行，或数某函数的参数个数；③“Sequence 是一种程序结构，再说出算法需要的另一种结构并说明它的用途”（2 分）；④说出一段代码用的是哪种循环结构（1 分）。

**识别信号**　Complete the table by placing one or more ticks；selection / iteration (repetition) / assignment / input/output / subroutine (procedure or function)；Give a line number containing …；Sequence is one programming construct. Identify one other …；Identify the type of construct used。

**解题思路**
1. **逐个关键字认**，认到一个就勾对应的栏：
   - selection：`IF`、`ELSE`、`CASE OF`，以及 CASE 里单独给出的子句行（`OTHERWISE : …`、`30 : …`）。
   - iteration：`FOR`、`NEXT`、`WHILE`、`ENDWHILE`、`REPEAT`、`UNTIL`——只给出循环的一半（单独一行 `UNTIL Level > 25`）也算。
   - assignment：`←`；**`INPUT X` 也给 X 赋了值**——⟦9618_s25_21:1(b)⟧ 的 MS 在 `REPEAT INPUT Value UNTIL …` 这一格勾了 Assignment 和 Iteration。
   - input/output：`INPUT`、`OUTPUT`，以及文件的 `READFILE`、`WRITEFILE`。
   - subroutine：`CALL X(…)`，以及表达式里的函数调用 `AllDone()`、`Compound(3)`（名字后面紧跟圆括号）。`Result[3]` 是数组元素，不是调用。
2. **一格里有几种就勾几种**：外层 IF 里套着 FOR、FOR 里有 CALL 的那一格要勾三栏（⟦9618_w25_22:1(a)⟧）。漏一个勾这一行就没分。
3. **写行号题**：先在代码旁边给每一行标上“初值 / 循环头 / 条件 / 调用 / 自增”，再对号入座。“initialisation statement”指循环前第一次给计数器、累加器、结果赋值的那一行。
4. **“再说出一种结构”题**：结构名 1 分 + 在本题算法里的用途 1 分。用途要扣题：循环 → 重复到文件尾 / 循环 100 次；选择 → 判断输入是不是正数 / 元素是不是空。

**得分表述**（引自对应 MS）
- 「An iterative construct // a (count-controlled) loop」⟦9618_w23_21:2(b)⟧
- 「A selection construct // an IF statement」⟦9618_w23_21:2(b)⟧
- 「Construct: a conditional loop Use: To keep repeating until the end of the file is reached」⟦9618_s24_23:2(b)⟧
- 「Use: To loop through all 100 inputs // To loop 100 times」⟦9618_w24_23:2(b)⟧
- 「Use: To test whether the (array) element is blank」⟦9618_w25_23:2(b)⟧

**易错与失分**
- 文件读写不当成 input/output：`READFILE`、`WRITEFILE` 也是输入输出（⟦9618_s24_22:1(a)⟧ 有两行靠它得分）。
- 把数组元素当成函数调用：`WHILE Result[3] <> FALSE` 只勾 iteration（⟦9618_w24_23:1(a)⟧）。
- 只认最外层关键字：`IF … THEN READFILE … ENDIF` 要同时勾 selection 和 input/output。
- “再说出一种结构”时又写 sequence，或只写结构名不写用途。
- 用途写成通用定义（“a loop repeats code”）而不扣题目算法：MS 要的是“循环 100 次 / 到文件尾 / 判断元素是否为空”。

#### 代表题精讲　⟦9618_s24_22:1(a)⟧

**在考什么**　表里四段伪代码，每段勾 selection、iteration、input/output 中的一个或多个。每行全对 1 分，共 4 分。

**完整作答**
| 伪代码 | Selection | Iteration | Input/Output |
|:--|:--:|:--:|:--:|
| `FOR Index ← 1 TO 10` / `Data[Index] ← 0` / `NEXT Index` | | ✓ | |
| `WRITEFILE ThisFile, "****"` | | | ✓ |
| `UNTIL Level > 25` | | ✓ | |
| `IF Mark > 74 THEN` / `READFILE OldFile, Data` / `ENDIF` | ✓ | | ✓ |

**与 MS 对齐**　MS 四行的勾与上表完全相同，「One mark per row」⟦9618_s24_22:1(a)⟧。第 1 行的 `Data[Index] ← 0` 是赋值，但本题没有 assignment 栏，只勾 iteration；第 3 行只有 REPEAT 循环的后一半，照样算 iteration；第 4 行两个勾缺一不可。

**英文作答句**　（本题答案即上表。）

**直观**　关键字是路标：IF / CASE 是岔路口（选择），FOR / WHILE / REPEAT 是环岛（循环），INPUT / OUTPUT / READFILE / WRITEFILE 是进出口（输入输出），带圆括号的名字是“转去别的地方办事”（子程序）。

**下一道变式**　⟦9618_w23_21:2(b)⟧　（换成说出结构：sequence 之外，把算法写成伪代码还需要哪两种结构。）

<!-- auto:drills P2-PG-01 -->

### P2-PG-02　表达式求值　{#P2-PG-02}

<!-- auto:stats P2-PG-02 -->

**考法**　给出变量的值（或标识符表里的示例值），把 3–4 个表达式的结果填进表格，一般每行 1 分（也有“任两行对 1 分、全对 2 分”）。表达式里有：算术（`/`、`DIV`、`MOD`、`INT`）、关系与逻辑（`AND`、`OR`、`NOT`、括号）、插页字符串函数（`MID`、`RIGHT`、`LENGTH`、`TO_UPPER`、`TO_LOWER`、`NUM_TO_STR`、`STR_TO_NUM`）、日期函数（`DAY`、`MONTH`）；近两年还常有一行是错的，要写 ERROR。

**识别信号**　Evaluate each expression；Complete the table by evaluating each expression (using the example values)；Expression | Evaluates to / Evaluation；Write 'ERROR' if the expression contains an error。

**解题思路**
1. **由内向外**：先算最里层的括号和函数，把结果写在草稿上，再算外一层。
2. **结果写出类型**：字符串结果带双引号（`"20%"`、`"SI"`），单个字符可写 `'a'`；数值不带引号；布尔值写 `TRUE` / `FALSE`。
3. **字符串函数逐位数**：`MID(S, x, y)` 从第 x 个字符起取 y 个；`RIGHT(S, n)` 取最后 n 个；`LENGTH` 连空格、标点、括号一起数。先在草稿上给字符串标出位置号。
4. **算术**：`/` 的结果是实数（`249.50` 写成 `249.5` 也对）；`INT` 直接去掉小数部分、不四舍五入；`MOD` 取余数、`DIV` 取商。
5. **逻辑**：`NOT` 只作用于紧跟它的那一项，带括号的整体先算；`AND` 两边都真才真，`OR` 一边真就真。
6. **ERROR 从类型来**：`+` 的一边是字符串（`Index + "33"`）、函数的参数类型不对（`NUM_TO_STR` 收到字符串）、参数个数不对、`AND` 的一边不是布尔值，都写 ERROR。
7. **日期**：日期按 DD/MM/YYYY 读，`MONTH(23/04/2004)` = 4，`DAY(…)` 同理。

**得分表述**（引自对应 MS）
- 「NUM_TO_STR(INT(DepRate * 10)) & '%' "20%"」⟦9618_w23_22:1(b)⟧
- 「MID(TO_UPPER("Version"), 4, 2) "SI"」⟦9618_s22_21:1(c)⟧
- 「INT((31 / 3) + 1) 11」⟦9618_s22_21:1(c)⟧
- 「NUM_TO_STR(Index + "33") ERROR」⟦9618_w24_23:1(c)⟧
- 「1 mark for any two rows correct 1 mark for all rows correct」⟦9618_s22_23:1(b)(i)⟧

**易错与失分**
- 字符串结果漏了引号，或大小写写错：「Quotation marks must be present for final row and must be capital C」⟦9618_s21_22:1(a)(ii)⟧。
- `INT` 当成四舍五入：`INT(33.3)` 是 33，`INT(10.33… + 1)` 是 11。
- 数 `LENGTH` 时漏了空格和冒号：`"AB12345:Cleaning Brush (small)"` 有 30 个字符。
- `TO_UPPER` 之后再取子串：`MID(TO_UPPER("Version"), 4, 2)` 是 `"SI"`，不是 `"si"`。
- 把 `NOT` 的范围看大：`Fraction >= 0.2 AND NOT Active` 里 NOT 只作用于 `Active`。
- MS 偶有笔误：⟦9618_w22_22:1(c)⟧ 的 MS 把 QP 的 `Count >= 29` 印成了 `Count >= 99`，讲解以 QP 为准（决策 D16）。

#### 代表题精讲　⟦9618_w23_22:1(b)⟧

**在考什么**　示例值：`Total` = 124.00、`DepRate` = 2.00、`Description` = `"AB12345:Cleaning Brush (small)"`。Complete the table by evaluating each expression using the example values. 4 行各 1 分。

**完整作答**
| 表达式 | 草稿 | 结果 |
|:--|:--|:--|
| `(Total * DepRate) + 1.5` | 124.00 × 2.00 = 248.00，再加 1.5 | `249.50` |
| `RIGHT(Description, 7)` | 最后 7 个字符：`(small)` | `"(small)"` |
| `(LENGTH(Description) - 8) > 16` | 长度 = 7 + 1 + 22 = 30；30 − 8 = 22；22 > 16 | `TRUE` |
| `NUM_TO_STR(INT(DepRate * 10)) & '%'` | 2.00 × 10 = 20.0 → `INT` 得 20 → `"20"` → 接上 `'%'` | `"20%"` |

**与 MS 对齐**　MS 四行依次是 249.50、"(small)"、TRUE、"20%"，「One mark per row」⟦9618_w23_22:1(b)⟧。第 2、4 行是字符串，结果必须带引号；第 3 行要先数对长度：`AB12345` 7 个、冒号 1 个、`Cleaning Brush (small)` 22 个（含两个空格和一对括号）。

**英文作答句**　（本题答案即上表最右一列。）

**直观**　求值像剥洋葱：从最里层的括号剥起，每剥一层都在草稿上写下这一层“是什么东西”（一个数、一串字、一个真假）。

**下一道变式**　⟦9618_w25_22:1(c)⟧　（加了 ERROR 行和日期函数：`NUM_TO_STR(Result + "3.2")`、`MID(MonthLetter, MONTH(Birthday) - 2, 1)`。）

<!-- auto:drills P2-PG-02 -->

### P2-PG-03　写或补全单条语句与表达式　{#P2-PG-03}

<!-- auto:stats P2-PG-03 -->

**考法**　①在空里填插页函数，使每条赋值语句合法（左边变量的类型已给），每行 1 分；②补出函数名或参数，使表达式得出指定的值；③写一条语句：调用某个过程、把函数结果赋给变量、写一个条件子句；④把一条复杂语句或几行代码化简成一行（常用 `MOD`）；⑤说出可以代替最后一个 CASE 条件的关键字（OTHERWISE）。1–5 分。

**识别信号**　Complete the table by filling in each gap with a function (from the insert)；Complete each pseudocode expression so that it evaluates to the value shown；Any functions and operators used must be defined in the insert；Write the pseudocode statement for this call；Write a simplified version of the statement；could be replaced with a single pseudocode statement；Give the keyword。

**解题思路**
1. **看左边定返回类型**：`MyInt ← …` 要返回 INTEGER 的函数（`INT`、`LENGTH`、`STR_TO_NUM`、`ASC`、`DAY`、`MONTH`）；`MyChar ← …` 要 CHAR（`MID(…, …, 1)`、`CHR`）；`MyString ← …` 要 STRING（`NUM_TO_STR`、`TO_UPPER`、`LEFT`、`RIGHT`、`&`）。
2. **看括号里的参数定函数**：一个实数 → `INT`；字符串 + 两个整数 → `MID`；字符串 + 一个整数 → `LEFT` / `RIGHT`；一个字符 → `ASC`；一个整数 → `CHR`；一个日期 → `DAY` / `MONTH` / `YEAR` / `DAYINDEX`。
3. **要得出给定的值时倒推**：67 ← `ASC('C')`；`"and"` ← `MID("Random", 2, 3)`；1.4 ← `STR_TO_NUM(MID("Court1.4Upper", 6, 3))`。
4. **函数名照插页一字不差**，全大写：写 `MID`，不写 `Mid`、`SUBSTRING`、`len`。
5. **写调用语句**：过程用 `CALL 名字(参数, …)`，参数顺序照模块说明；函数不用 CALL，把返回值赋给变量：`TotalCost ← BulbCost(NumberPurchased)`。
6. **化简**：`(A = B) OR (A > B)` → `A >= B`；`(Active OR NOT Active) AND NOT Exempt` → `NOT Exempt`（前一半恒为 TRUE）；用一串 IF 实现 1 → 2 → 3 → 1 的轮转 → `X ← (X MOD 3) + 1`。

**得分表述**（引自对应 MS）
- 「MyChar ← MID ("Elwood", 3, 1)」⟦9618_s24_22:1(b)⟧
- 「Mark Row 4 as follows: STR_TO_NUM 1 mark MID("Court1.4Upper",6,3) 1 mark」⟦9618_s25_23:1(b)⟧
- 「CALL CountErrors("Jim01Prog.txt", 20)」⟦9618_w22_21:8(b)⟧
- 「One mark for assignment to LineNum making any use of MOD One for completely correct statement」⟦9618_s22_23:7(c)⟧
- 「Result[x + 1] <= Result[x]」⟦9618_w23_23:4(b)⟧
- 「Function names must be exactly as shown」⟦9618_w21_22:1(c)⟧

**易错与失分**
- 用了插页以外的函数（`LEN`、`SUBSTR`、`ROUND`、`str`）：不给分（D2）。
- 函数的返回类型和左边对不上：`MyChar ← LEFT("Elwood", 3)` 返回 3 个字符的串，不能赋给 CHAR。
- `MID` 的第三个参数写成结束位置：`MID("Random", 2, 3)` 是从第 2 个起取 3 个。
- 调用函数时写 CALL，或调用过程时把它放在赋值号右边。
- 化简后的式子与原来不等价：`(Result[x + 1] = Result[x]) OR (Result[x] > Result[x + 1])` 化简为 `Result[x + 1] <= Result[x]`，等号不能丢。

#### 代表题精讲　⟦9618_s24_22:1(b)⟧

**在考什么**　变量类型：`MyChar` 是 CHAR、`MyString` 是 STRING、`MyInt` 是 INTEGER。Complete the table by filling in each gap with a function (from the insert) so that each expression is valid. 4 行各 1 分，第 3、4 行各有两个空（函数套函数）。

**完整作答**
| 表达式 | 想法 |
|:--|:--|
| `MyInt ← INT(3.1415926)` | 实数 → 整数，只有 `INT` |
| `MyChar ← MID("Elwood", 3, 1)` | 字符串 + 两个整数 → `MID`；取 1 个字符，得 `'w'` |
| `MyString ← NUM_TO_STR(INT(27.509))` | 内层把实数变整数，外层把数变成字符串，得 `"27"` |
| `MyInt ← STR_TO_NUM(RIGHT("ABC123", 3))` | 内层取最后 3 个字符 `"123"`，外层变成整数 123 |

**与 MS 对齐**　MS 第 1、2 行只接受 `INT`、`MID`；第 3 行接受 `NUM_TO_STR(INT(…))`、`CHR(INT(…))`、`TO_UPPER(NUM_TO_STR(…))`、`TO_LOWER(NUM_TO_STR(…))`；第 4 行接受 `STR_TO_NUM(RIGHT(…))`、`LENGTH(RIGHT(…))`、`LENGTH(LEFT(…))`。「One mark per row」⟦9618_s24_22:1(b)⟧——一行里两个空都对才得分。

**英文作答句**　（本题答案即上表左列。）

**直观**　像拼插头：左边插座的形状（类型）定了，就找一个“出口”形状对得上、“入口”也能插进括号里那些东西的函数。

**下一道变式**　⟦9618_s25_23:1(b)⟧　（反过来给结果要你补函数：`'D'`、2、FALSE、1.4，最后一行两层函数各 1 分。）

<!-- auto:drills P2-PG-03 -->

### P2-PG-04　选择结构：IF 与 CASE 的改写　{#P2-PG-04}

<!-- auto:stats P2-PG-04 -->

**考法**　①把一个 CASE 结构改写成功能相同的嵌套 IF（4 分）；②把三层嵌套 IF 改写成四个独立的 `IF … THEN … ENDIF`，每个只含一条 CALL，条件写成一个化简后的逻辑表达式（每个 1 分）；③把只有两个分支的 CASE 改成一个 IF … ELSE（2 分）；④把两个 CASE 子句合并成一个，用变量代替字面值（2 分）。

**识别信号**　Write pseudocode with the same functionality without using a CASE structure；using a single selection construct；re-write the pseudocode as four separate IF...THEN...ENDIF statements；a single, simplified logic expression；Write pseudocode for a single clause to replace the two clauses。

**解题思路**
1. **CASE → 嵌套 IF**：第一个 CASE 值变成 `IF 变量 = 值 THEN`，下一个值写进上一个 IF 的 `ELSE` 里，依次往里套；`OTHERWISE` 成为最里层的 `ELSE`（或者在最前面先给变量赋默认值）。
2. **IF 与 ENDIF 一一配对**：套了 n 层就有 n 个 `ENDIF`。伪代码没有 `ELSIF` / `elif`，一律在 ELSE 里嵌套（D2）。
3. **范围子句**：`30 TO 40 : …` 改成 `IF X >= 30 AND X <= 40 THEN`；`< 30 : …` 改成 `IF X < 30 THEN`。CASE 是**按顺序**测试的，改写时保持原来的先后次序。
4. **嵌套 IF → 几个独立 IF**：把每个 CALL 所在的路径写出来（A 真、B 真、C 假 → Sub2），路径上的条件用 AND 连起来；两条路径调用同一个模块时，合并并化简（A 假且 C 假，B 真假都一样 → `(NOT A) AND (NOT C)`）。
5. **功能必须不变**：每个分支里的语句原样搬过去，一个都不能少、不能多。

**伪代码模板**

```pseudocode
// CASE OF Code / 1 : … / 2 : … / OTHERWISE : …   rewritten without CASE
IF Code = 1 THEN
   ThisChar ← 'a'
ELSE
   IF Code = 2 THEN
      ThisChar ← 'y'
   ELSE
      ThisChar ← '*'                  // OTHERWISE becomes the innermost ELSE
   ENDIF
ENDIF                                 // one ENDIF for every IF

// a range clause   30 TO 40 : Level ← "Medium"
IF ThisValue >= 30 AND ThisValue <= 40 THEN
   Level ← "Medium"
ENDIF

// one path of a nested IF as a separate statement
IF A AND B AND NOT C THEN
   CALL Sub2()
ENDIF
```

**得分表述**（引自对应 MS）
- 「ANY test of MySwitch = 1, 2 or 3」⟦9618_s22_21:6(b)⟧
- 「OTHERWISE, or initial assignment of default value」⟦9618_s22_21:6(b)⟧
- 「Completely correct IF...THEN...ELSE...ENDIF syntax」⟦9618_s22_21:6(b)⟧
- 「One mark per IF...THEN...ENDIF clause」⟦9618_w22_22:5⟧
- 「IF (NOT A) AND (NOT C) THEN CALL Sub3() ENDIF」⟦9618_w22_22:5⟧
- 「Both correct assignments and the correct test/logic」⟦9618_w24_22:5(c)⟧
- 「use of variable CaseVar rather than literal values」⟦9618_w25_23:5(b)(ii)⟧

**得分点地图**（核验语料 4 道改写题：s22/21、w22/22 已拆分；w24/22、w25/23 按 MS 列点人工归纳）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 完整的 `IF … THEN … ELSE … ENDIF` 结构（每个 IF 有自己的 ENDIF） | 3 | `nested-if` |
| 每个分支的条件写对，赋值或调用与原来一致 | 3 | `relational-ops`、`logic-ops` |
| 默认分支：OTHERWISE 变成最后的 ELSE，或先赋默认值 | 1 | `initialise-variables` |
| 用变量代替字面值，把两个子句合成一个 | 1 | `case-range` |

**易错与失分**
- 写成 `ELSIF` / `ELSE IF` 而少写 ENDIF：嵌套 IF 每层都要有 ENDIF，结构分（MP4）就看这个。
- 漏了 OTHERWISE 对应的那一支：MS 专门有一分给默认值。
- 改写成几个并列的 `IF … ENDIF` 却没有让条件互斥：原来 CASE 只执行一个分支，并列 IF 可能执行两个。
- 嵌套 IF 化简时没有把路径列全：⟦9618_w22_22:5⟧ 里 Sub3 出现在两条路径上（A 假、B 真、C 假；A 假、B 假、C 假），合并后与 B 无关，得 `(NOT A) AND (NOT C)`；而 A 真、B 假时什么都不调用，不能并进去。

#### 代表题精讲　⟦9618_s22_21:6(b)⟧

**在考什么**　给出 `CASE OF MySwitch`：1 → `ThisChar ← 'a'`，2 → `'y'`，3 → `'7'`，OTHERWISE → `'*'`。Write pseudocode with the same functionality without using a CASE structure. 4 分。

**完整作答**

```pseudocode
IF MySwitch = 1 THEN
   ThisChar ← 'a'
ELSE
   IF MySwitch = 2 THEN
      ThisChar ← 'y'
   ELSE
      IF MySwitch = 3 THEN
         ThisChar ← '7'
      ELSE
         ThisChar ← '*'
      ENDIF
   ENDIF
ENDIF
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | ANY test of MySwitch = 1, 2 or 3 | `IF MySwitch = 1 THEN` | `relational-ops` |
| 2 | All three comparisons and corresponding assignments | 三个比较各配一条赋值 | `relational-ops` |
| 3 | OTHERWISE, or initial assignment of default value | 最里层 `ELSE ThisChar ← '*'` | `initialise-variables` |
| 4 | Completely correct IF...THEN...ELSE...ENDIF syntax | 三个 IF、三个 ENDIF 配对 | `nested-if` |

另一种同样满分的写法：先 `ThisChar ← '*'`，再写三个并列的 `IF MySwitch = n THEN ThisChar ← … ENDIF`——默认值先赋，满足条件时覆盖（MP3 的“initial assignment of default value”）。

**直观**　CASE 像电梯按钮面板，一按直达；嵌套 IF 像走楼梯，一层层问“是 1 楼吗？不是就上楼再问”，问到底还不是，就到了 OTHERWISE 那层。

**同题 Python 版要点**
- Python 有 `elif`，可以写成平的 `if / elif / else`；伪代码没有 ELSIF，只能嵌套。这是两种语言最容易串的地方。
- Python 3.10 起也有 `match … case`，`case _:` 对应 OTHERWISE。
- 先过阶梯 **L02 E01**（CASE 范围子句 ↔ if/elif）和 **L02 E05**（把嵌套 IF 改写成 CASE 的干跑题）。

```python
if my_switch == 1:
    this_char = "a"
elif my_switch == 2:
    this_char = "y"
elif my_switch == 3:
    this_char = "7"
else:
    this_char = "*"
```

**下一道变式**　⟦9618_w22_22:5⟧　（三层嵌套 IF → 四个独立 IF，每个条件是一个化简后的 AND / NOT 表达式；讲解时请对照原卷 QP p.10 的缩进。）

<!-- auto:drills P2-PG-04 -->

### P2-PG-05　循环结构的选择与改写　{#P2-PG-05}

<!-- auto:stats P2-PG-05 -->

**考法**　①给出的设计用的循环不是最合适的：说出更合适的循环并说明理由（2 分）；②解释现有循环为什么不合适（1 分）；③说出给定代码里循环的种类和结束条件（不写伪代码，2 分）；④为算法选一种循环并说明理由；⑤（2021 扩展）换成合适的循环后，要删掉、改掉哪几行。

**识别信号**　State a more appropriate loop structure. Justify your answer；does not use the most appropriate loop construct；Explain why this is not the most appropriate loop construct；Identify the type of loop and state the condition that ends the loop；Give the name of a suitable loop structure。

**解题思路**
1. **先问次数**：进入循环之前就知道要循环几次吗？知道（数组 10000 个元素、字符串的长度、参数给的次数）→ **count-controlled loop**（FOR）；不知道（输入到 99 为止、读到文件尾、找到为止）→ **conditional loop**（WHILE 或 REPEAT）。
2. **再问至少一次吗**：循环体至少要执行一次（先输入再判断、先生成再检查是否重复）→ **post-condition**（REPEAT … UNTIL）；可能一次都不执行（第一个输入就是结束值、文件为空）→ **pre-condition**（WHILE … ENDWHILE）。
3. **理由用 MS 的固定句**：The number of iterations is known / is not known；The loop can be terminated as soon as the value is found；The loop ends following a specific input。
4. **指出不合适**：FOR 循环在找到目标之后还继续比较（做无用功）；WHILE 循环手动维护计数器，其实次数是固定的（多了初值和自增两行）。
5. **识别循环**：`WHILE … ENDWHILE` = pre-condition；`REPEAT … UNTIL` = post-condition；`FOR … NEXT` = count-controlled。题目说 Do not include pseudocode statements 时，结束条件用一句英文写：when the value input is equal to zero。

**得分表述**（引自对应 MS）
- 「The number of iterations required is known」⟦9618_s25_21:4(a)⟧
- 「Name: (pre / post) conditional loop」⟦9618_w23_22:2(b)⟧
- 「the number of iterations is not known // loop ends following a specific input (in the loop)」⟦9618_w23_22:2(b)⟧
- 「Comparisons/tests continue to be made even if the search value / string / matching element has been found」⟦9618_w25_21:5(b)(i)⟧
- 「The loop / search can be terminated as soon as the (first occurrence of) SearchString / required value / required string / matching element is found」⟦9618_w25_21:5(b)(ii)⟧
- 「Type: pre-condition Condition: when the value of ThisNum / the input value is equal to zero」⟦9618_s22_22:5(a)⟧

**易错与失分**
- 只写名字不写理由，或理由写成“它更好 / 更快”：要说出“次数已知 / 未知”“找到就能停”。
- 把 conditional 写成 condition-controlled IF：IF 不是循环。
- 识别题把结束条件写反：`WHILE ThisNum <> 0` 的结束条件是“输入等于 0”，不是“不等于 0”。
- 说 REPEAT 合适却没说出“至少执行一次”的理由；或在可能一次都不该执行的场合（空文件）选了 REPEAT。

#### 代表题精讲　⟦9618_w25_21:5(b)(ii)⟧

**在考什么**　函数 FindFirst() 在全局数组 `MyData[1:10000]` 里找第一个等于 SearchString 的元素，返回下标，找不到返回 −1。原设计用 `FOR Index ← 1 TO 10000` 扫完整个数组，循环里先比较、再用 `IF FoundAt = -1` 保证只记第一个。(b)(i) 问为什么这个循环不合适（1 分），(b)(ii) Suggest and justify a more appropriate loop construct（2 分）。讲解时请对照原卷 QP p.8 的代码。

**完整作答**
- (b)(i) The FOR loop continues after the first matching element has been found, so comparisons are still made even though the search value has been found.
- (b)(ii) Construct: a conditional (pre-condition) loop. Justification: the search can be terminated as soon as the first occurrence of SearchString is found.

改写后的函数（供对照）：

```pseudocode
FUNCTION FindFirst(SearchString : STRING) RETURNS INTEGER
   DECLARE Index : INTEGER
   DECLARE FoundAt : INTEGER
   FoundAt ← -1
   Index ← 1
   WHILE FoundAt = -1 AND Index <= 10000      // the condition never reads the array
      IF MyData[Index] = SearchString THEN
         FoundAt ← Index                      // the loop ends on the next test
      ENDIF
      Index ← Index + 1
   ENDWHILE
   RETURN FoundAt
ENDFUNCTION
```

**与 MS 对齐**　(b)(ii) 两分：「Construct: A conditional loop」⟦9618_w25_21:5(b)(ii)⟧ + 「The loop / search can be terminated as soon as the (first occurrence of) SearchString / required value / required string / matching element is found」⟦9618_w25_21:5(b)(ii)⟧。(b)(i) 的一分对应「The loop continues after the (first instance) of the search value / string / matching element has been found」⟦9618_w25_21:5(b)(i)⟧。改写后内层的 `IF FoundAt = -1` 也不需要了：找到就停，不会再遇到第二个。

**英文作答句**　A conditional loop should be used, because the search can stop as soon as the first matching element is found, instead of always checking all 10000 elements.

**直观**　在一排储物柜里找自己的包：找到了就该停手，不用把一万个柜子全打开。

**下一道变式**　⟦9618_s25_21:4(a)⟧　（方向相反：外层是条件循环，但次数其实已知，应改成 count-controlled。）

<!-- auto:drills P2-PG-05 -->

### P2-PG-06　过程、函数与参数的概念　{#P2-PG-06}

<!-- auto:stats P2-PG-06 -->

**考法**　概念短答，1–3 分一问，常连着出：①程序员为什么用子程序 / 模块（2 分）；②为什么用库程序（3 分）；③过程与函数的区别，哪个模块该写成函数；④术语：参数（parameter）、过程接口（procedure interface）、函数头里名字 / 参数 / 返回类型各是什么；⑤局部变量与全局变量的区别、局部变量的好处；⑥BYVAL 与 BYREF 的效果；⑦把过程改成函数还要改什么；⑧把局部变量改成全局（或反过来）为什么程序不按预期工作。

**识别信号**　State two reasons why the programmer may decide to use a subroutine / modules；library routines；Explain one difference between functions and procedures；Give the correct term for the identifiers；procedure interface；local and global variables；passed by value / passed by reference；Identify the modules that would be implemented as functions。

**解题思路**
1. **用子程序 / 模块的理由**（选两三条写）：同一任务要在多处重复做；某一部分算法完成一个明确的任务；程序更简单、复杂度降低；单独测试、调试、维护更容易；可以复用已有的模块。
2. **用库程序的理由**：经过测试、基本没有错误；提供程序员自己写不出的功能（加密、复杂统计）；现成可用、节省开发时间；库更新时自动得到改进。
3. **过程 vs 函数**：函数返回一个值（在表达式里调用）；过程不返回值（用 CALL 调用），但可以用 BYREF 参数把值带回。“returns a …”“结构图里有返回值箭头” → 函数。
4. **参数**：调用时把数据传给模块的标识符；过程接口 = 模块与调用者之间传数据的约定：几个参数、各自的类型和顺序。
5. **局部 vs 全局**：局部变量只在声明它的模块里能用，模块运行时才占内存；全局变量程序各处都能用，整个运行期间都占内存。局部变量的好处：同名可在别处复用、模块自成一体、不会意外改到外面的变量、内存可以回收。
6. **BYVAL vs BYREF**：BYVAL 传的是值的副本，模块里改了，调用者的变量不变；BYREF 传的是变量本身（地址），模块里一改，调用者的变量跟着变。答题时把**两个模块名和参数名都写进去**，说清“模块结束后调用者那边的值变不变”。

**得分表述**（引自对应 MS）
- 「When a task which is repeated / reused / performed in several places」⟦9618_w22_22:1(a)(i)⟧
- 「Testing / debugging / maintenance is easier」⟦9618_w22_22:1(a)(i)⟧
- 「They are tried and tested so free from errors」⟦9618_w22_21:1(a)⟧
- 「Term: Parameter(s) Use: to pass values / arguments to the procedure」⟦9618_w22_22:1(a)(ii)⟧
- 「A function returns a (single) value and a procedure does not」⟦9618_s25_23:6(a)⟧
- 「Local variables are used within a module // are accessible only within the module (in which they are declared)」⟦9618_s25_23:1(a)(ii)⟧
- 「A new (instance of) variable MyString is created each time the procedure is called / executed」⟦9618_w23_21:6(b)⟧

**易错与失分**
- BYREF 题只写“by reference 会改变值”：2 分题要说清**谁的值在什么时候变**，并点名模块（Mod-G 改了 Par3，Mod-C 里随之改变；Mod-F 改了，Mod-C 里不变）。
- 过程与函数的区别写成“函数有参数、过程没有”：两者都可以有参数，区别在返回值。
- 库程序的好处写“程序更快”：MS 要的是“测试过、无错误 / 写不出来的功能 / 节省开发时间 / 自动更新”。
- 把局部变量的好处写成“更安全”这类空话：要落到“同名复用、不会意外改到别处、模块自成一体”。
- 把局部变量当成“上次调用还记得的值”：局部变量每次调用都新建，旧内容丢失（⟦9618_w23_21:6(b)⟧）。

#### 代表题精讲　⟦9618_s24_23:7(a)(ii)⟧

**在考什么**　七个模块的说明表里，Mod-C 用参数 Par1、Par3 调用，并反复调用 Mod-F 再调用 Mod-G；Mod-F 以 Par3 为参数（按值传递），Mod-G 以 Par3 为参数（按引用传递）。Explain the effect of the two different ways of passing the parameter Par3. 2 分。讲解时请对照原卷 QP p.16 的模块表。

**完整作答**
- Mod-G (BYREF): any change made to Par3 inside Mod-G is reflected in the value of Par3 in the calling module Mod-C after Mod-G terminates.
- Mod-F (BYVAL): Mod-F works on a copy of Par3, so any change made to Par3 inside Mod-F is not reflected in the value of Par3 in Mod-C after Mod-F terminates.

**与 MS 对齐**　MS 两个要点正是这两句（Mod-G 的改动带回 Mod-C；Mod-F 的改动不带回），给分方式是「1 mark for a reasonable attempt to explain 2 marks for full explanation including context」⟦9618_s24_23:7(a)(ii)⟧——“context”就是写出 Mod-C、Mod-F、Mod-G 和 Par3 这些名字。

**英文作答句**　When Par3 is passed by reference to Mod-G, Mod-G uses the original variable, so any change it makes is seen by Mod-C afterwards; when Par3 is passed by value to Mod-F, Mod-F only gets a copy, so changes made inside Mod-F do not affect Par3 in Mod-C.

**直观**　BYVAL 是给对方一份复印件，对方在复印件上怎么涂改，你的原件不变；BYREF 是把原件交出去，对方改了，拿回来的就是改过的。阶梯 **L04 E01** 用干跑题把这两种传法各走一遍。

**下一道变式**　⟦9618_w23_21:6(b)⟧　（局部变量的生命周期：把全局 MyString 改成过程里的局部变量后，每次调用都新建，之前拼好的内容丢失。）

<!-- auto:drills P2-PG-06 -->

### P2-PG-07　写模块头　{#P2-PG-07}

<!-- auto:stats P2-PG-07 -->

**考法**　按模块说明、参数说明或结构图，写出 PROCEDURE / FUNCTION 的头部：模块名、每个参数的名字与类型、需要时加 BYREF、函数要写 `RETURNS` 类型。MS 按下划线部分给分，每部分 1 分，1–5 分。

**识别信号**　Write the pseudocode module header(s) for …；Write the pseudocode to define the module headers；Write the header for the function in pseudocode；Write pseudocode for the new module header；结构图上带参数箭头的模块；“is changed to a function that returns …”。

**解题思路**
1. **先定过程还是函数**：要返回一个值（说明里写 returns、结构图里有从下往上的返回箭头）→ `FUNCTION 名字(…) RETURNS 类型`；否则 → `PROCEDURE 名字(…)`。
2. **读结构图的箭头**：从上往下指向被调模块的是传入参数；从下往上回到调用者的是返回值；**同一个参数下去又回来（双头箭头）是 BYREF**。实心圆点表示标志（BOOLEAN），空心圆表示数据。
3. **每个参数写 `名字 : 类型`**，类型从说明里找（“P1 and T1 are of type real”）；参数名照抄结构图或说明。
4. **BYREF 写在参数名前面**：`BYREF P2 : BOOLEAN`。只有需要把新值带回调用者的参数才用 BYREF；函数的参数不用 BYREF（指南：parameters should not be passed by reference to a function）。
5. **函数头末尾**写 `RETURNS 类型`，是类型名（REAL、BOOLEAN），不是变量名，也不加冒号。
6. 头部写完顺手写上 `ENDPROCEDURE` / `ENDFUNCTION`：写整个模块时，头与结尾合成一分。

**伪代码模板**

```pseudocode
// no value returned; one value carried back through a BYREF parameter
PROCEDURE ModuleName(Param1 : STRING, BYREF Param2 : BOOLEAN)
ENDPROCEDURE

// one value returned; parameters passed by value
FUNCTION ModuleName(Param1 : REAL, Param2 : INTEGER) RETURNS REAL
ENDFUNCTION

// no parameters
FUNCTION Confirm() RETURNS BOOLEAN
ENDFUNCTION
```

**得分表述**（引自对应 MS）
- 「FUNCTION Calculate(Expression : STRING) RETURNS REAL」⟦9618_w22_21:7(a)(ii)⟧
- 「One mark for BYREF」⟦9618_w23_23:7(b)(ii)⟧
- 「Keyword RETURNS and type string」⟦9618_s24_23:6(b)(i)⟧
- 「One mark per underlined part in each case」⟦9618_s24_21:7(b)(ii)⟧
- 「PROCEDURE Sub_Part3A(V: INTEGER, W: BOOLEAN, BYREF U : STRING)」⟦9618_s25_23:6(b)⟧
- 「PROCEDURE LoanReturn (LoanID, BookID : STRING, BYREF Fine : REAL)」⟦9618_s21_21:2(b)⟧

**得分点地图**（核验语料 7 道写模块头的题；MS 按下划线给分、未拆分，以下按各题标准答案人工归纳）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 关键字 PROCEDURE / FUNCTION 选对，模块名照抄 | 7 | `module-header` |
| 每个参数写出名字和类型 | 7 | `module-header`、`data-types` |
| 函数头写 `RETURNS` 与返回类型 | 6 | `module-header`、`data-types` |
| 需要带回值的参数加 `BYREF` | 4 | `byval-byref` |

四项里前三项几乎每题都有；BYREF 一旦出现就单独占一分。

**易错与失分**
- 用 `MODULE`、`SUB`、`def` 当关键字（ER s24 9618/21 Q7(b)(ii) p.15：有考生写了 Module 而没有判断是 FUNCTION 还是 PROCEDURE）。
- 漏了 BYREF（同一份 ER 点名 Sub-A 常丢这一分）；或者把 BYREF 加给了函数的参数。
- `RETURNS` 后面写变量名（`RETURNS Count`）或写成 `RETURN`、`RETURNS : STRING`。
- 参数不写类型，或几个参数共用一个类型时写乱：最稳妥的是每个参数各写 `名字 : 类型`。
- 把结构图里从下往上的返回值也写成参数。

#### 代表题精讲　⟦9618_s24_21:7(b)(ii)⟧

**在考什么**　结构图：Update 通过选择菱形 A 调用 Sub-A、Sub-B、Sub-C 之一。Update → Sub-A：向下传 Name（空心圆），P2 是实心圆点、双头箭头（下去又回来）；Update → Sub-B：向下传 P1，向上返回 T1。说明：Name 是会员姓名；P1、T1 是 REAL。Write the pseudocode module headers for Sub-A and Sub-B. 4 分。讲解时请对照原卷 QP p.17 的结构图（看清 P2 的双头箭头与实心圆点）。

**完整作答**

```pseudocode
PROCEDURE Sub-A(Name : STRING, BYREF P2 : BOOLEAN)
ENDPROCEDURE

FUNCTION Sub-B(P1 : REAL) RETURNS REAL
ENDFUNCTION
```

**与 MS 对齐**
| MP | MS 要求（原文，按下划线部分） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | PROCEDURE Sub-A | Sub-A 没有返回值 → 过程 | `module-header` |
| 2 | (Name : STRING, BYREF P2 : BOOLEAN) | Name 是姓名 → STRING；P2 实心圆点 = 标志 → BOOLEAN，双头箭头 → BYREF | `byval-byref`、`data-types` |
| 3 | FUNCTION Sub-B | T1 向上返回 → 函数 | `module-header` |
| 4 | (P1 : REAL) RETURNS REAL | P1、T1 都是 REAL；T1 是返回值，不写进参数表 | `data-types` |

MS 原文就是 `PROCEDURE Sub-A (Name : STRING, BYREF P2 : BOOLEAN)` 与 `FUNCTION Sub-B (P1 : REAL) RETURNS REAL`。模块名里的连字符照抄题目。

**直观**　结构图上的箭头就是“快递单”：往下的是寄出去的包裹（参数），往上的是寄回来的回执（返回值），寄出去又被改了寄回来的，就是 BYREF。

**同题 Python 版要点**
- Python 没有 BYREF：要带回的值用 `return` 交回（多个值返回元组），调用处重新赋值——`p2 = sub_a(name, p2)`。
- Python 的类型注解只是提示（`p1: float`），不写也能运行；伪代码的类型必须写。
- 先过阶梯 **L04 E02**（按模块说明表写模块，BYREF ↔ 返回元组）。

```python
def sub_a(name: str, p2: bool) -> bool:
    # ... statements that may change p2 ...
    return p2                   # BYREF P2: hand the new value back

def sub_b(p1: float) -> float:
    t1 = p1                     # ... the calculation of t1 ...
    return t1
```

**下一道变式**　⟦9618_s25_23:6(b)⟧　（三个模块头：一个过程一个参数、一个函数返回 BOOLEAN、一个过程三参数其中一个 BYREF，共 5 分。）

<!-- auto:drills P2-PG-07 -->

### P2-PG-08　良好编程实践　{#P2-PG-08}

<!-- auto:stats P2-PG-08 -->

**考法**　①代码里写死了邮费、税率等字面值：说出更好的表示方法（常量，1 分）并结合本程序说明好处（2–3 分）；②说出让代码容易读懂的特征（3 分）；③有意义的名字为什么是好习惯，再举两个别的好习惯；④编译出错的复杂语句想暂时让编译器忽略：怎么做（改成注释）；⑤说明一个算法为什么低效并给出改进（循环里反复调用返回值不变的函数、找到之后还在找）；⑥利用数据已排序，查找怎样提前结束。

**识别信号**　Identify a more appropriate way of representing …；Describe the advantages / benefits of your answer … with reference to this program；features that make them easier to understand；Give the reason why this is good practice. Give two other examples of good practice；Explain why this is not efficient and suggest a more efficient solution；already organised in ascending order。

**解题思路**
1. **常量题**：答 Use (of) constants；好处按 MS 的四句写，并把情境里的名词放进去：值只输入一次；避免输错或在不同地方用了不同的值；值要变时只改一处，易维护；程序更易读懂。
2. **易读特征**：缩进、空白 / 空行、注释、有意义的变量名（CamelCase）、关键字大写——看题目给的那几行代码里**确实有**的才写。
3. **其他好习惯**：注释、缩进、空白、常量、局部变量与参数、模块化。
4. **让编译器忽略一句**：把这一句改成注释（行首加 `//`）。
5. **效率题**：先说问题（做了重复或多余的工作 + 为什么多余），再说改法（把不变的结果在循环前算一次存进局部变量，循环里用变量；找到就用条件循环提前结束）。
6. **有序数据**：读到的值已经大于要找的值时就可以停止，后面不可能再出现。

**得分表述**（引自对应 MS）
- 「Use of constants」⟦9618_s23_22:1(a)(i)⟧
- 「Postal rates are entered once only」⟦9618_s23_22:1(a)(ii)⟧
- 「When required, the constant representing the postal rate value is changed once only」⟦9618_s23_22:1(a)(ii)⟧
- 「Sensible / meaningful variable names // use of Camel Case」⟦9618_s23_22:1(b)⟧
- 「Change the statement into a comment」⟦9618_s23_22:5(d)⟧
- 「The functions will return the same value every time they are called」⟦9618_s24_23:5(b)⟧
- 「Assign FormatA(Label) and FormatB(Label) to two (local) variables before the loop」⟦9618_s24_23:5(b)⟧
- 「is greater than the value being searched for」⟦9618_s23_21:8(e)⟧

**易错与失分**
- 常量的好处写成“值不能改所以安全”而不结合情境：题目要 with reference to this program，写出“postal rate / tax rate”。
- 易读特征写了代码里没有的东西（比如那几行根本没有空行）。
- 效率题只写改法不写问题，或只说“函数调用太多”而没说出**为什么**多余（参数在循环里不变，返回值每次相同）。
- “让编译器忽略”写成删除语句或加断点：题目说了不想删；断点是运行时调试。

#### 代表题精讲　⟦9618_s23_22:1(a)(ii)⟧

**在考什么**　邮费程序把 $3.75 等邮费直接写进了多处代码（`ItemPostalCost ← 3.75`）。(a)(i) 说出更合适的表示方法（1 分）；(a)(ii) Describe the advantages of your answer to part (a)(i) with reference to this program. 3 分。

**完整作答**
- (a)(i) Use constants for the postal costs, for example `CONSTANT SmallItemCost = 3.75`.
- (a)(ii) 写三点：
  1. Each postal rate is entered once only, in the constant declaration.
  2. It avoids input errors and accidental changes, so the same postal rate cannot have different values at different points in the program.
  3. When the postal rates change, only the constant needs to be changed, once, so the program is easier to maintain.

**与 MS 对齐**　三点依次对应 MS 的 1、2、3：「Postal rates are entered once only」⟦9618_s23_22:1(a)(ii)⟧；「Avoids input error / changing the cost accidentally // avoids different values for postal rates at different points in the program」⟦9618_s23_22:1(a)(ii)⟧；「When required, the constant representing the postal rate value is changed once only」⟦9618_s23_22:1(a)(ii)⟧。MS 第 4 点 Makes the program easier to understand 也可以写，Max 3。

**英文作答句**　Using a constant means the postal rate is entered only once, so it cannot be mistyped or have different values in different places, and when the rate changes it only has to be changed in one statement.

**直观**　常量像墙上贴的价目表：价格只写在一个地方，所有人都照着它收钱；涨价时只换这一张表。

**下一道变式**　⟦9618_s24_23:5(b)⟧　（效率题：循环里每次都调用 FormatA(Label)、FormatB(Label)，参数不变、结果不变；说出问题并给出改法，4 分。）

<!-- auto:drills P2-PG-08 -->

### P2-PG-09　输入-处理-输出算法　{#P2-PG-09}

<!-- auto:stats P2-PG-09 -->

**考法**　按要点（或编号步骤）写一段伪代码或一个过程 / 函数，数据从键盘一个一个输入或用随机数生成，不存进数组：①输入到结束值（99、0、−1）为止，分类计数或累加，最后输出；②输入固定个数（100 个）的值，按条件求和；③分两段输入、各自累加，再求平均；④生成随机数：猜数游戏（太大 / 太小提示，猜中为止）、生成两个不同的随机数、掷骰子 n 次求平均、生成 25 个递增的随机数；⑤枚举一个范围里满足条件的整数并计数。5–8 分。

**识别信号**　An algorithm will: • input … one at a time • … • output …；prompt and input …；repeat … until the value input is 99；The value 99 must not be counted；generate a random integer value between … and … inclusive；Write pseudocode for the algorithm. You must declare all variables used。

**解题思路**
1. **先定循环**（PG-05 的判断）：输入个数已知 → `FOR Count ← 1 TO 100`；输入到某个值为止 → 先读一次，再 `WHILE 值 <> 结束值`，循环体最后再读一次（结束值就不会被处理）；至少做一次、做到满足条件为止（猜中、两个数不同）→ `REPEAT … UNTIL`。
2. **声明所有变量**：题目写 You must declare all variables used 时，循环变量、输入变量、计数器、累加器都要 DECLARE，类型写对（输入的是实数就用 REAL）。
3. **初值写在循环前**：计数器、累加器设 0；分两段累加的两个总和都要设 0。
4. **输入前先提示**：`OUTPUT "Enter …"` 再 `INPUT X`。MS 常有一分是 prompt and input … in a loop。
5. **循环里判断与处理**：奇偶用 `X MOD 2 = 1`；正数用 `X > 0`；满足就计数 / 累加。
6. **随机整数**：`INT(RAND(n))` 得 0 到 n − 1 的整数；要 Low 到 High（含两端）就写 `INT(RAND(High - Low + 1)) + Low`，例如 1–100 → `INT(RAND(100)) + 1`，−10 到 10 → `INT(RAND(21)) - 10`。
7. **循环后输出**，带说明文字，用逗号分隔：`OUTPUT "Total: ", Total`。求平均用 `/`，不要用 DIV。

**伪代码模板**

```pseudocode
// A: input until a rogue value; the rogue value is never processed
DECLARE ThisNum : INTEGER
DECLARE Count : INTEGER
DECLARE Total : INTEGER
Count ← 0
Total ← 0
OUTPUT "Enter a value (99 to end): "
INPUT ThisNum                                 // read once before the loop
WHILE ThisNum <> 99
   Count ← Count + 1
   Total ← Total + ThisNum
   OUTPUT "Enter a value (99 to end): "
   INPUT ThisNum                              // read again as the last statement
ENDWHILE
OUTPUT "Count: ", Count, " Total: ", Total

// B: a fixed number of inputs
FOR Index ← 1 TO 100
   OUTPUT "Enter an integer: "
   INPUT ThisNum
   IF ThisNum > 0 THEN
      Total ← Total + ThisNum
   ENDIF
NEXT Index

// C: repeat until a condition is met (at least once)
Target ← INT(RAND(100)) + 1                  // random integer 1 to 100
REPEAT
   OUTPUT "Enter a guess between 1 and 100: "
   INPUT Guess
   IF Guess > Target THEN
      OUTPUT "Too high"
   ENDIF
   IF Guess < Target THEN
      OUTPUT "Too low"
   ENDIF
UNTIL Guess = Target
OUTPUT "Correct"
```

**得分表述**（引自对应 MS）
- 「Conditional loop while ThisNum <> 99」⟦9618_w23_22:4(a)⟧
- 「Increment appropriate count in a loop, both counts must have been initialised before loop」⟦9618_w23_22:4(a)⟧
- 「Prompt and input a value in a loop」⟦9618_w24_23:2(a)⟧
- 「Output of Total after the loop」⟦9618_w24_23:2(a)⟧
- 「Correct syntax for random number between 1 and 100」⟦9618_s25_21:3⟧
- 「Output the counter, following a reasonable attempt, after the loop」⟦9618_s22_21:6(a)⟧

**得分点地图**（核验语料 10 道已拆分题；“题数”= 有这类得分点的题数）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 输出结果（循环后输出一次，或按要求在循环里输出），带说明文字 | 9 | `output-format` |
| 声明所有用到的变量（含循环变量；常要求写明类型） | 8 | `declare-variables`、`data-types` |
| 用 MOD / DIV / INT（判断奇偶、取个位、把随机实数取整） | 6 | `div-mod` |
| 用 RAND 生成指定范围的随机整数 | 5 | `random-numbers` |
| 循环里的比较（> 0、太大 / 太小、两个数是否相同） | 5 | `relational-ops` |
| 循环里计数 / 累加 | 5 | `accumulator` |
| 计数器、累加器在循环前赋初值 | 4 | `initialise-variables` |
| 计数循环次数正确（100 次、25 次、参数给的次数） | 4 | `count-loop`、`loop-bounds` |
| 循环里先提示再输入 | 4 | `input-prompt` |
| 过程 / 函数的头与结尾（题目要求写模块时） | 3 | `module-header` |
| 输入到结束值为止，结束值不参与处理 | 3 | `sentinel-loop` |
| 后测循环（直到猜中、直到两个数不同） | 3 | `post-condition-loop` |

几乎每题都有：**声明 + 循环 + 循环里的输入与判断 + 循环后输出**。随机数一出现，`RAND` 与 `INT` 往往各占一分。

**易错与失分**
- WHILE 的条件引用了一个还没有输入过的变量：先读一次再进循环（ER w23 9618/22 Q4(a) p.18：很多 WHILE 循环用的 ThisNum 没有初值）。
- 结束值被计数或累加：读入结束值后要立刻离开循环，或在处理前判断。
- 循环条件自己加戏：题目只说到 99 结束，就写 `ThisNum <> 99`，不要写成 `ThisNum < 99`（同一份 ER 点名）。
- 判断奇偶写成 `%`、`IF Num = Even`：用插页的 `MOD`。
- 输出时用 `&` 连接整数：`OUTPUT "Odd: " & COdd` 错，用逗号或先 `NUM_TO_STR`。
- 随机数范围差一：`INT(RAND(100))` 是 0–99，要 1–100 还得加 1。
- 求平均用 DIV，或除以错误的个数。

#### 代表题精讲　⟦9618_w23_22:4(a)⟧

**在考什么**　过程 Count()：①输入一个值（都是正整数）；②分别数奇数和偶数的个数；③重复第 1 步，直到输入 99；④输出两个计数，并配说明文字。99 不能被计数。Write pseudocode for the procedure Count(). 6 分（MS 列 7 点）。

**完整作答**

```pseudocode
PROCEDURE Count()
   DECLARE ThisNum : INTEGER
   DECLARE COdd : INTEGER
   DECLARE CEven : INTEGER
   COdd ← 0
   CEven ← 0
   OUTPUT "Enter a positive integer (99 to end): "
   INPUT ThisNum
   WHILE ThisNum <> 99
      IF ThisNum MOD 2 = 1 THEN
         COdd ← COdd + 1
      ELSE
         CEven ← CEven + 1
      ENDIF
      OUTPUT "Enter a positive integer (99 to end): "
      INPUT ThisNum
   ENDWHILE
   OUTPUT "Number of odd values: ", COdd
   OUTPUT "Number of even values: ", CEven
ENDPROCEDURE
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure heading and ending | `PROCEDURE Count()` … `ENDPROCEDURE` | `module-header` |
| 2 | Local COdd, CEven and ThisNum declared as integers | 三个 `DECLARE … : INTEGER` | `declare-variables`、`data-types` |
| 3 | Conditional loop while ThisNum <> 99 | `WHILE ThisNum <> 99` | `sentinel-loop` |
| 4 | Input ThisNum in a loop | 循环体最后的 `INPUT ThisNum` | `input-prompt` |
| 5 | Check ThisNum is odd or even in a loop | `IF ThisNum MOD 2 = 1 THEN` | `div-mod` |
| 6 | Increment appropriate count in a loop, both counts must have been initialised before loop | `COdd ← COdd + 1` / `CEven ← CEven + 1`；两个初值在循环前 | `accumulator`、`initialise-variables` |
| 7 | After the loop output COdd and CEven with a suitable message following a reasonable attempt at counting | 循环后两条带说明文字的 OUTPUT | `output-format` |

Max 6，写满 7 点留一分余量。MS 范例用一句 `DECLARE COdd, CEven, ThisNum : INTEGER`，本手册按指南一行声明一个。

**直观**　门口的检票员：来一个人看一眼票是单号还是双号，在对应的本子上记一笔；看到写着 99 的“下班牌”就收工，最后报两个本子上的数。

**同题 Python 版要点**
- “先读一次 + 循环最后再读”的结构 Python 照搬；Python 的 `input()` 返回字符串，要 `int(…)`；提示语写在 `input("…")` 里（决策 D13）。
- 奇偶判断 `MOD` ↔ `%`。先过阶梯 **L03 E02**（哨兵值求平均：WHILE + 预读，正是本题的结构）；随机数写法见 **L01** 对照卡第 7 节（`INT(RAND(6)) + 1` ↔ `random.randint(1, 6)`）。

```python
def count() -> None:
    c_odd = 0
    c_even = 0
    this_num = int(input("Enter a positive integer (99 to end): "))
    while this_num != 99:
        if this_num % 2 == 1:
            c_odd = c_odd + 1
        else:
            c_even = c_even + 1
        this_num = int(input("Enter a positive integer (99 to end): "))
    print("Number of odd values:", c_odd)
    print("Number of even values:", c_even)
```

**下一道变式**　⟦9618_s25_21:3⟧　（猜数游戏：随机生成 1–100 的整数，REPEAT 直到猜中，太大、太小各给提示，8 分，MS 列 9 点。）

<!-- auto:drills P2-PG-09 -->

### P2-PG-10　数值计算与判断函数　{#P2-PG-10}

<!-- auto:stats P2-PG-10 -->

**考法**　写一个模块，对参数（或一次输入的少数几个值）做算术与判断，不循环读入、不处理数组：①阶乘、反求阶乘的底数；②判断三条边能否构成直角三角形；③按重量返回 Accept / Recheck / Reject 之类的多分支结果；④时间进位（秒满 60 进分、分满 60 进时、到 24 归零并调用别的模块）；⑤计时：由 Tick 计数算出结束时刻和提醒时刻；⑥校验位：各位数字求和、取余数、拼到原数后面或校验；⑦积分换免费咖啡、按 20 个一组算价格；⑧调用已有模块取得几个端点，再算中点。6–8 分。

**识别信号**　A function … will be called with … integer parameter(s) … and return …；factorial；right-angled；check digit；HH, MM and SS；The value returned from the function will be as follows: Outcome | Return value；return −1 if the number is negative；Assume that the parameter is valid。

**解题思路**
1. **头部**：几个参数、什么类型、返回什么类型——照题目逐条写（PG-07）。
2. **先处理非法 / 特殊情况**：负数返回 −1、长度不够返回 FALSE、没找到返回 −1。可以先用 IF 判断，再在 ELSE 里做正常计算。
3. **计算写成一条条赋值**：每个中间结果存进有意义的局部变量（`Len1 ← (x1 - x2) ^ 2 + (y1 - y2) ^ 2`）。括号写清楚；平均、中点要整数时用 `INT(…)` 或 `DIV`。
4. **逐位取数**用 `MOD 10` 取个位、`DIV 10` 去掉个位，循环到 0；也可以 `NUM_TO_STR` 后逐字符取再 `STR_TO_NUM`（PG-11 的手法）。
5. **多分支返回**：按题目的表格从最极端的情况开始判断（先 Reject，再 Recheck，最后 Accept），嵌套 IF 写全；也可以在每个分支里直接 `RETURN`。
6. **反复相乘 / 进位**：累乘器初值是 1（累加器才是 0）；进位按秒 → 分 → 时的顺序嵌套判断。
7. **返回**：所有路径都要有返回值，类型与头部一致；过程题则输出结果。

**伪代码模板**

```pseudocode
FUNCTION Calculate(Number : INTEGER) RETURNS INTEGER
   DECLARE Result : INTEGER
   DECLARE Count : INTEGER
   IF Number < 0 THEN                       // invalid input first
      Result ← -1
   ELSE
      Result ← 1                            // a product starts at 1, a sum at 0
      FOR Count ← 1 TO Number
         Result ← Result * Count
      NEXT Count
   ENDIF
   RETURN Result                            // one RETURN covers both cases
ENDFUNCTION

// digits of a whole number with MOD and DIV
Total ← 0
WHILE Number > 0
   Total ← Total + (Number MOD 10)          // the last digit
   Number ← Number DIV 10                   // remove the last digit
ENDWHILE

// several outcomes: test the extreme cases first
IF Weight >= Max + 3 OR Weight <= Min - 3 THEN
   Outcome ← 'R'
ELSE
   IF Weight > Min + 2 AND Weight < Max - 2 THEN
      Outcome ← 'A'
   ELSE
      Outcome ← 'C'
   ENDIF
ENDIF
```

**得分表述**（引自对应 MS）
- 「Function heading and ending including parameter and return value」⟦9618_s22_23:6(a)⟧
- 「Check for illegal value (< 0)」⟦9618_s22_23:6(a)⟧
- 「Return INTEGER value correctly in both cases: ThisNum < 0 and >= 0」⟦9618_s22_23:6(a)⟧
- 「Check for Recheck (or just default to third option)」⟦9618_w22_23:6(b)⟧
- 「Return result correctly in both cases」⟦9618_s24_21:6(a)⟧
- 「Correct calculation of EndTick and WarningTick」⟦9618_w24_22:4⟧

**得分点地图**（核验语料 13 道已拆分题）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 模块头与结尾（参数、返回类型） | 11 | `module-header` |
| 判断条件写对（非法值、范围、相等、`>=` 与 `>`） | 9 | `relational-ops` |
| 计算式写对（括号、乘方、平均、中点、时间换算） | 8 | `operator-precedence` |
| 各种情况都返回正确的值 | 7 | `return-value`（返回 TRUE / FALSE 另有 2 题记 `boolean-return`） |
| 声明局部变量 | 6 | `declare-variables` |
| 计数、累加、逐次相乘 | 6 | `accumulator` |
| 嵌套 IF 覆盖所有情况 | 5 | `nested-if` |
| 赋初值（累乘器为 1） | 5 | `initialise-variables` |
| AND / OR 组合条件 | 4 | `logic-ops` |
| 输出结果（过程题） | 4 | `output-format` |
| 数字与字符串互转 | 4 | `type-conversion` |
| `DIV` / `MOD` / `INT` | 3 | `div-mod` |

几乎每次都有的是：**模块头、判断条件、计算式、返回**。先把这四样写对，再去挣中间的算法分。

**易错与失分**
- 累乘器初值写 0：结果永远是 0。
- 只在一种情况下返回（忘了负数那一支），或在 IF 里 RETURN 了却缺了 ENDIF（ER s22 9618/23 Q6(a) p.23：MP3 与 MP7 常因 IF … THEN … ENDIF 不完整一起丢）。
- 用 `^` 以外的写法表示乘方（题目给了 `^` 就用它），或把 `A × A` 写成 `A x A`。
- 整数结果没有取整：中点 `(Start + End) / 2` 是实数，要 `INT(…)` 或 `DIV`。
- 改写参数本身又在后面用到原值：需要原值时先复制到局部变量。
- 用 `math.factorial`、`sqrt` 之类插页以外的函数。

#### 代表题精讲　⟦9618_s22_23:6(a)⟧

**在考什么**　阶乘：n 的阶乘是 1 到 n 所有整数的乘积；0 的阶乘是 1。函数 Factorial()：以一个整数为参数；计算并返回它的阶乘；参数为负时返回 −1。Write pseudocode for the function Factorial(). 6 分（MS 列 7 点）。

**完整作答**

```pseudocode
FUNCTION Factorial(ThisNum : INTEGER) RETURNS INTEGER
   DECLARE Value : INTEGER
   DECLARE Count : INTEGER
   IF ThisNum < 0 THEN
      Value ← -1
   ELSE
      Value ← 1
      FOR Count ← 1 TO ThisNum           // no iterations when ThisNum = 0, so 0! = 1
         Value ← Value * Count
      NEXT Count
   ENDIF
   RETURN Value
ENDFUNCTION
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function heading and ending including parameter and return value | `FUNCTION Factorial(ThisNum : INTEGER) RETURNS INTEGER` … `ENDFUNCTION` | `module-header` |
| 2 | Declaration and initialisation (to 1) of local Integer Value for result | `DECLARE Value : INTEGER`、`Value ← 1` | `declare-variables`、`initialise-variables` |
| 3 | Check for illegal value (< 0) | `IF ThisNum < 0 THEN` | `relational-ops` |
| 4 | (Conditional) loop while ThisNum not zero // loop for ThisNum iterations | `FOR Count ← 1 TO ThisNum` | `loop-bounds` |
| 5 | Attempt to form answer by successive multiplication | `Value ← Value * Count` | `operator-precedence` |
| 6 | Completely correct MP5 | 从 1 乘到 ThisNum，0 时不乘 | `operator-precedence` |
| 7 | Return INTEGER value correctly in both cases: ThisNum < 0 and >= 0 | 一个 `RETURN Value` 覆盖两种情况 | `return-value` |

Max 6。MS 范例用 `WHILE ThisNum <> 0` 倒着乘；MP4 写明“loop for ThisNum iterations”同样给分，所以用 FOR 正着乘也是满分。MS 另有一套递归解法的计分清单（递归是 A2 内容，P2 不必用）。

**直观**　阶乘像搭积木塔：第一层放 1，之后每一层把高度乘上新的层号；层号是负数的塔不存在，就举牌 −1。

**同题 Python 版要点**
- `FOR Count ← 1 TO ThisNum` ↔ `for count in range(1, this_num + 1):`；`range` 不含终点，要加 1。
- 不要用 `math.factorial()`：题目考的是循环相乘本身。
- 先过阶梯 **L04 E05**（素数模块：在函数里循环、判断、返回）与 **L03 E06**（用 DIV / MOD 逐位处理，对应校验位一类变式）。

```python
def factorial(this_num: int) -> int:
    if this_num < 0:
        return -1
    value = 1
    for count in range(1, this_num + 1):
        value = value * count
    return value
```

**下一道变式**　⟦9618_w25_21:6(b)⟧　（校验位：各位数字求和、取除以 10 的余数作为校验位，再把它接到原数后面返回；可以转字符串逐位取，也可以用 MOD / DIV。）

<!-- auto:drills P2-PG-10 -->

### P2-PG-11　字符串处理模块　{#P2-PG-11}

<!-- auto:stats P2-PG-11 -->

**考法**　写一个以字符串为参数（或返回字符串）的模块，全卷分值最多的单个题型，6–8 分一问，几乎每卷都有。内容按做法分三类：
- **逐字符扫描**：数某个字符出现几次、数 1 的个数加奇偶校验位、把某个字符全部替换、判断回文、检查每个字符是不是字母 / 数字、在字符串里找某个字符是否存在。
- **取字段**：按固定长度切出几项数据（前 5 位是编号、接着 32 位是说明、剩下的是价格）；按位置取消息里的字段；按分隔符（逗号）逐个取出数字求和；从 DDMMYYYY 串里取日、月、年。
- **找位置再截取 / 拼出新串**：去掉开头的空格、删掉 `//` 之后的注释、把超长的标题逐词截短并加 `...`、只保留卡号最后 4 位其余换成 `*`、把根名与编号拼成文件名、生成由某字符组成的串。

**识别信号**　take a string … as a parameter；return the (new / modified) string；count the number of times that the character occurs；palindrome；A text string contains … data items concatenated；separated by commas / the comma character is used as a separator；removing any leading space characters；replaced by …；case sensitive / Upper-case and lower-case characters need to be treated the same；implement your own version of the MID() function。

**解题思路**
1. **认出是哪一类**：要看每个字符 → 子模板 A；字段位置或分隔符给定 → 子模板 B；要先找到某个位置（第一个非空格、第一个 `//`）再整段切 → 子模板 C。
2. **逐字符的标准循环**：`FOR Index ← 1 TO LENGTH(S)`，循环里第一句 `ThisChar ← MID(S, Index, 1)`。字符串不是数组，**不能写 `S[Index]`**。
3. **要造新串**：循环前 `NewString ← ""`，循环里 `NewString ← NewString & ThisChar`，循环后 `RETURN NewString`。
4. **字符判断**：等于某字符 `ThisChar = Char1`；数字 `ThisChar >= '0' AND ThisChar <= '9'`（或 `IS_NUM(ThisChar)`）；字母 `(ThisChar >= 'A' AND ThisChar <= 'Z') OR (ThisChar >= 'a' AND ThisChar <= 'z')`，或先 `TO_UPPER(ThisChar)` 再比一个范围；空格 `ThisChar = ' '`。
5. **大小写**：题目说不区分大小写 → 比较前两边都 `TO_UPPER`；题目说 case sensitive → **不要**转换。
6. **长度表达式代一个例子算**：从第 Start 个取到串尾，长度是 `LENGTH(S) - Start + 1`；去掉前 n 个字符是 `RIGHT(S, LENGTH(S) - n)`；固定长度字段之后的“剩下部分”是 `RIGHT(S, LENGTH(S) - 前面字段的总长)`。
7. **数字与字符串互转**：拼进字符串前 `NUM_TO_STR`；取出的数字字符参与计算前 `STR_TO_NUM`。
8. **返回**放在循环之后；函数用 `RETURN`，不要用 `OUTPUT` 代替。

**伪代码模板**（三个子模板）

**子模板 A　逐字符扫描：计数 / 替换 / 造新串 / 检查格式**（范例：⟦9618_s23_21:4⟧、⟦9618_s23_22:4⟧、⟦9618_s25_23:5⟧）

```pseudocode
FUNCTION ScanString(InString : STRING, Target : CHAR) RETURNS STRING
   DECLARE NewString : STRING
   DECLARE ThisChar : CHAR
   DECLARE Index : INTEGER
   NewString ← ""                                 // build-up string starts empty
   FOR Index ← 1 TO LENGTH(InString)              // every character: 1 to LENGTH
      ThisChar ← MID(InString, Index, 1)          // one character at a time
      IF ThisChar = Target THEN                   // the test: equal / letter / digit / space
         ThisChar ← '*'                           // the processing: replace, count, set a flag
      ENDIF
      NewString ← NewString & ThisChar            // concatenate inside the loop
   NEXT Index
   RETURN NewString                               // after the loop
ENDFUNCTION
```

- 计数版：把“造新串”两句换成 `Count ← 0`（循环前）与 `Count ← Count + 1`（IF 里），返回 Count。
- 检查格式版（全是字母？）：循环前 `Valid ← TRUE`，遇到不合格的字符 `Valid ← FALSE`，循环后 `RETURN Valid`。
- 从右往左取第 Index 个：`MID(S, LENGTH(S) - Index + 1, 1)`（回文比较用）。
- 奇偶校验位：数完 1 的个数后 `IF Count MOD 2 = 0 THEN BitString ← BitString & '0' ELSE BitString ← BitString & '1' ENDIF`。

**子模板 B　取字段：定长切分与按分隔符拆分**（范例：⟦9618_w22_23:5(a)(i)⟧、⟦9618_w23_21:8(d)⟧、⟦9618_s22_22:6⟧）

```pseudocode
// fixed-length fields: <StockID: 5><Description: 32><Cost: the rest>
SID ← LEFT(TLine, 5)
SDesc ← MID(TLine, 6, 32)                         // starts after the first 5 characters
SCost ← RIGHT(TLine, LENGTH(TLine) - 37)          // the rest: total length - (5 + 32)

// separated fields: "12,13,451,22"
Total ← 0
Count ← 0
NumString ← ""
FOR Index ← 1 TO LENGTH(InString)
   ThisChar ← MID(InString, Index, 1)
   IF ThisChar = ',' THEN                         // a separator ends one field
      Total ← Total + STR_TO_NUM(NumString)
      Count ← Count + 1
      NumString ← ""                              // reset for the next field
   ELSE
      NumString ← NumString & ThisChar            // keep building the field
   ENDIF
NEXT Index
Total ← Total + STR_TO_NUM(NumString)             // the last field has no comma after it
Count ← Count + 1
```

**子模板 C　先找位置，再整段截取**（范例：⟦9618_s24_22:8(b)⟧、⟦9618_s24_21:8(a)⟧）

```pseudocode
FUNCTION DeleteSpaces(Line : STRING) RETURNS STRING
   DECLARE NewLine : STRING
   DECLARE Index : INTEGER
   DECLARE FirstPos : INTEGER
   FirstPos ← 0                                   // 0 means "not found yet"
   Index ← 1
   WHILE FirstPos = 0 AND Index <= LENGTH(Line)   // the condition never calls MID
      IF MID(Line, Index, 1) <> ' ' THEN
         FirstPos ← Index                         // stop at the first non-space
      ENDIF
      Index ← Index + 1
   ENDWHILE
   IF FirstPos = 0 THEN
      NewLine ← ""                                // empty, or spaces only
   ELSE
      NewLine ← RIGHT(Line, LENGTH(Line) - FirstPos + 1)
   ENDIF
   RETURN NewLine
ENDFUNCTION
```

- 删注释：找第一个 `MID(Line, Index, 2) = "//"` 的位置 P（循环只到 `LENGTH(Line) - 1`），再 `LEFT(Line, P - 1)`。
- 条件循环找位置时，循环条件只用标志和下标，`MID` 放在循环体里（不依赖 AND 短路，决策 D25）。

**得分表述**（引自对应 MS）
- 「Loop for length of OldString」⟦9618_s23_21:4⟧
- 「Extract char and test in a loop」⟦9618_s23_21:4⟧
- 「Use of concatenate to build NewString replace char if necessary, in a loop」⟦9618_s23_21:4⟧
- 「If comma, convert NumString to integer and update Total and Count」⟦9618_s22_22:6⟧
- 「Calculation of length of SCost (remainder of string)」⟦9618_w22_23:5(a)(i)⟧
- 「Identify first non-space character in a loop」⟦9618_s24_22:8(b)⟧
- 「Convert characters to same case」⟦9618_s22_21:7(a)⟧
- 「Use of concatenate – must have been initialised in a loop」⟦9618_s23_23:4⟧

**得分点地图**（核验语料 30 道已拆分题；“题数”= 有这类得分点的题数）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 用插页函数取字符或子串（`MID` / `LEFT` / `RIGHT` / `LENGTH`，参数个数与顺序都对） | 25 | `string-functions` |
| 模块头与结尾（参数类型、`RETURNS` 类型） | 18 | `module-header` |
| 循环后返回结果（字符串或计数） | 17 | `return-value` |
| 循环范围：从 1 到 `LENGTH(…)`（或到找到为止） | 14 | `loop-bounds` |
| 字符判断与比较（等于参数、是否字母 / 数字 / 空格、统一大小写后比较） | 14 | `char-compare` |
| 用 `&` 在循环里拼出新串（循环前先赋 `""`） | 12 | `string-concat` |
| 逐字符循环 | 11 | `char-loop` |
| 按固定长度或分隔符取出字段 | 7 | `field-extract` |
| 声明局部变量（含循环变量） | 7 | `declare-variables` |
| 结果串、计数器、标志赋初值 | 6 | `initialise-variables` |
| 各种情况下返回 TRUE / FALSE | 6 | `boolean-return` |
| 调用题目给的模块并使用返回值 | 6 | `procedure-call` |
| 长度检查等比较（长度不足先返回） | 6 | `relational-ops` |
| 数字与字符串互转（`STR_TO_NUM` / `NUM_TO_STR`） | 4 | `type-conversion` |
| 循环里计数（数字符、数 1 的个数） | 4 | `accumulator` |

按子模板看：逐字符循环（`char-loop`）出现在 11 道题里，取字段（`field-extract`）7 道，其余是“找位置 / 截取 / 拼接”。不论哪一类，**插页函数用对、循环到 LENGTH、循环里拼接、循环后返回**这四分几乎每次都有。

**易错与失分**
- 把字符串当数组：`OldString[Index]`（ER s23 9618/21 Q4 p.14：少数考生没有用插页的字符串函数，而是把字符串当数组取字符）。
- 题目没要求却先统一大小写（同一份 ER 点名丢分），或题目要求不区分大小写却没转换。
- 用 `LEFT` 去取中间的一个字符；用 `OUTPUT` 代替 `RETURN`；用关键字（`STRING`）作标识符（ER s23 9618/22 Q4 p.20）。
- 拼接串忘了在循环前赋 `""`：MS 写明 must have been initialised。
- 长度参数差一：`MID(S, Start, LENGTH(S))` 会越过串尾；从 Start 取到串尾的长度是 `LENGTH(S) - Start + 1`。
- 按分隔符拆时漏了最后一个字段（最后一个数字后面没有逗号）。
- 调用了 `LEFT` / `RIGHT` 却没有把返回值存起来：函数不会改原串。
- 用 `+` 拼字符串、用 `&` 拼整数、用插页以外的函数（`LEN`、`SUBSTRING`、`split`、`find`），或写 `FOR ThisChar IN InString`（D2）。

#### 代表题精讲　⟦9618_s23_21:4⟧

**在考什么**　函数 Replace()：①三个参数——一个字符串（原串）、一个字符（原字符）、一个字符（新字符）；②把原串里所有的原字符换成新字符，形成新串；③返回新串。Write pseudocode for function Replace(). 6 分。子模板 A 的标准实例。

**完整作答**

```pseudocode
FUNCTION Replace(OldString : STRING, Char1 : CHAR, Char2 : CHAR) RETURNS STRING
   DECLARE NewString : STRING
   DECLARE ThisChar : CHAR
   DECLARE Index : INTEGER
   NewString ← ""
   FOR Index ← 1 TO LENGTH(OldString)
      ThisChar ← MID(OldString, Index, 1)
      IF ThisChar = Char1 THEN
         ThisChar ← Char2
      ENDIF
      NewString ← NewString & ThisChar
   NEXT Index
   RETURN NewString
ENDFUNCTION
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function heading and ending, including parameters and return type | `FUNCTION Replace(…) RETURNS STRING` … `ENDFUNCTION` | `module-header` |
| 2 | Declaration of local variables used including loop counter | `NewString`、`ThisChar`、`Index` 都声明了 | `declare-variables` |
| 3 | Loop for length of OldString | `FOR Index ← 1 TO LENGTH(OldString)` | `char-loop`、`loop-bounds` |
| 4 | Extract char and test in a loop | `MID(OldString, Index, 1)` + `IF ThisChar = Char1` | `string-functions`、`char-compare` |
| 5 | Use of concatenate to build NewString replace char if necessary, in a loop | 替换后 `NewString ← NewString & ThisChar` | `string-concat` |
| 6 | Return NewString after reasonable attempt | 循环后 `RETURN NewString` | `return-value` |

MS 范例的函数头印成了 `Function Replace(OldString : STRING, Char1, Char2 : CHAR) RETURNS : STRING`；指南写法是 `FUNCTION`、`RETURNS STRING`（RETURNS 后不加冒号），本手册照指南写。题目没有说不区分大小写，所以**不要**转换大小写。

**直观**　抄一行字，看到要换的那个字就写成新字，其余照抄；抄完把新的那一行交上去。

**同题 Python 版要点**
- `MID(S, Index, 1)` ↔ `s[index - 1]`（或直接 `for index in range(len(s))` 用 `s[index]`）；`LENGTH` ↔ `len`；`&` ↔ `+`。
- 不要用 `old_string.replace(char1, char2)`：一行就完成了，但题目考的是逐字符算法。
- 先过阶梯 **L05 E01**（用切片实现 LEFT / RIGHT / MID）、**L05 E03**（逐字符循环统计）、**L05 E04**（去首尾空格：长度表达式不差一，对应子模板 C）；格式检查类再做 **L09 E04**。

```python
def replace(old_string: str, char1: str, char2: str) -> str:
    new_string = ""
    for index in range(len(old_string)):
        this_char = old_string[index]
        if this_char == char1:
            this_char = char2
        new_string = new_string + this_char
    return new_string
```

**下一道变式**　⟦9618_s22_22:6⟧　（子模板 B：按逗号拆出每个数字，求总和与平均并输出；记得处理最后一个数字。）

<!-- auto:drills P2-PG-11 -->

### P2-PG-12　日期处理　{#P2-PG-12}

<!-- auto:stats P2-PG-12 -->

**考法**　用插页的日期函数：①写一条语句，用 `SETDATE` 把某个日期赋给 DATE 变量（含声明，1–3 分）；②写一条语句，用 `MONTH` 等算出月份差（2 分）；③补全条件，判断某天是不是星期四（`DAYINDEX`，2 分）；④写一个条件：今天与上次来访是不是星期几相同（`TODAY`、`DAYINDEX`）；⑤写模块：找三月的第三个星期日（循环 + `SETDATE` + `DAYINDEX`）；用 BYREF 参数更新积分与上次来访日期（`TODAY`、`MONTH`）。

**识别信号**　of type DATE；Write a pseudocode statement, using a function from the insert, to assign the value corresponding to 15/11/2005；test whether … was born on a Thursday；Date functions from the insert should be used in your solution；the current date；the same month / the same day of the week。

**解题思路**
1. **插页的六个日期函数**：`SETDATE(Day, Month, Year)` 返回 DATE；`DAY(D)`、`MONTH(D)`、`YEAR(D)` 返回整数；`DAYINDEX(D)` 返回星期几（**星期日 = 1**，星期一 = 2 … 星期六 = 7）；`TODAY()` 返回今天的日期。
2. **SETDATE 的参数顺序是日、月、年**：15/11/2005 → `SETDATE(15, 11, 2005)`。
3. **星期几对数字**：星期日 1、星期一 2、星期二 3、星期三 4、星期四 5、星期五 6、星期六 7。判断星期四：`DAYINDEX(MyDOB) = 5`。
4. **生成日期再判断**：要“某月第几个星期几”，就让日号从 1 往上加，每次 `SETDATE(DayNumber, 3, ThisYear)`，用 `DAYINDEX` 判断，数到第三个为止。
5. **同月 / 同星期**：比较两个日期的 `MONTH(…)` 或 `DAYINDEX(…)`，不要直接比整个日期。
6. **带回修改**：模块要改调用者的日期和积分时，两个参数都 BYREF（PG-07）。
7. **参数名别用函数名**：`Year`、`Day`、`Month` 是插页函数名，参数写 `ThisYear`。

**伪代码模板**

```pseudocode
// statements
DECLARE StartDate : DATE
StartDate ← SETDATE(15, 11, 2005)               // day, month, year
NumMonths ← 12 - MONTH(MyDOB)
IF DAYINDEX(MyDOB) = 5 THEN                     // Sunday = 1, so Thursday = 5
   OUTPUT "Born on a Thursday"
ENDIF

// generate dates in a loop and test each one
FUNCTION NthWeekday(ThisYear : INTEGER, ThisMonth : INTEGER, Target : INTEGER, N : INTEGER) RETURNS INTEGER
   DECLARE DayNumber : INTEGER
   DECLARE Found : INTEGER
   DECLARE ThisDate : DATE
   DayNumber ← 0
   Found ← 0
   REPEAT
      DayNumber ← DayNumber + 1
      ThisDate ← SETDATE(DayNumber, ThisMonth, ThisYear)
      IF DAYINDEX(ThisDate) = Target THEN
         Found ← Found + 1
      ENDIF
   UNTIL Found = N
   RETURN DayNumber
ENDFUNCTION
```

**得分表述**（引自对应 MS）
- 「StartDate ← SETDATE (15, 11, 2005)」⟦9618_s23_21:2(b)⟧
- 「NumMonths ← 12 - MONTH(MyDOB)」⟦9618_s23_22:2(b)⟧
- 「IF DAYINDEX(MyDOB) = 5 THEN」⟦9618_s23_23:2(a)⟧
- 「Correctly generate value of type DATE using SETDATE() in a loop」⟦9618_w24_23:6⟧
- 「Test if value represents a Sunday using DAYINDEX() in a loop」⟦9618_w24_23:6⟧
- 「Use of TODAY() function to obtain current date」⟦9618_s25_23:7(a)(i)⟧
- 「DAYINDEX(LastVisitDate) = DAYINDEX(TODAY())」⟦9618_s25_23:7(a)(ii)⟧

**得分点地图**（核验语料 5 道日期题：w24/23 Q6、s25/23 Q7(a) 已拆分；s23/21、s23/22、s23/23 的单条语句按 MS 下划线人工归纳）

| 得分点（MS 常见写法） | 题数 | 技能标签 |
|:--|--:|:--|
| 用 `SETDATE(日, 月, 年)` 得到 DATE 值并赋给变量 | 3 | `date-functions` |
| 用 `DAYINDEX` 判断星期几（星期日 = 1） | 3 | `date-functions` |
| 用 `DAY` / `MONTH` / `YEAR` 取出一部分再计算或比较 | 2 | `date-functions` |
| 模块头与结尾（参数类型、返回类型） | 2 | `module-header` |
| 循环里计数（数到第三个星期日）或按条件增加积分 | 2 | `accumulator` |
| 用 `TODAY()` 取得当前日期 | 1 | `date-functions` |
| 需要带回的日期、积分用 `BYREF` | 1 | `byval-byref` |
| 声明 DATE 类型的变量 | 1 | `data-types` |

**易错与失分**
- `SETDATE` 的参数顺序写成 年、月、日，或少了参数、参数是字符串（ER w24 9618/23 Q6 p.28：常见 SETDATE 缺参数或参数类型不对）。
- 生成了日期却没有存进 DATE 类型的变量（同一份 ER：MP5 常因此丢分）。
- `DAYINDEX` 记成星期一 = 1：插页规定星期日 = 1。
- 用 `Year` 作参数名：与插页函数同名（ER w24 9618/23 Q6 p.27）。
- 计数器没有在循环前赋初值；用 OUTPUT 代替 RETURN。
- 日期写成字符串 `"15/11/2005"` 赋给 DATE 变量。

#### 代表题精讲　⟦9618_w24_23:6⟧

**在考什么**　有的国家在三月的第三个星期日开始夏令时。函数 AdjustClock()：参数是一个表示年份的整数；返回那一年三月里调钟那天的日号。例如 `DayNumber ← AdjustClock(2022)` 使 DayNumber 得 20。Date functions from the insert should be used in your solution. 7 分（MS 列 8 点）。

**完整作答**

```pseudocode
FUNCTION AdjustClock(ThisYear : INTEGER) RETURNS INTEGER
   DECLARE DayNumber : INTEGER
   DECLARE SundayCount : INTEGER
   DECLARE ThisDate : DATE
   DayNumber ← 0
   SundayCount ← 0
   REPEAT
      DayNumber ← DayNumber + 1
      ThisDate ← SETDATE(DayNumber, 3, ThisYear)
      IF DAYINDEX(ThisDate) = 1 THEN              // Sunday = 1
         SundayCount ← SundayCount + 1
      ENDIF
   UNTIL SundayCount = 3
   RETURN DayNumber
ENDFUNCTION
```

**与 MS 对齐**
| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function heading, parameter, ending and return type | `FUNCTION AdjustClock(ThisYear : INTEGER) RETURNS INTEGER` … `ENDFUNCTION` | `module-header` |
| 2 | Declare local integer variable that is used to create a date | `DECLARE DayNumber : INTEGER` | `declare-variables`、`data-types` |
| 3 | Loop until 3rd Sunday found | `REPEAT … UNTIL SundayCount = 3` | `post-condition-loop`、`loop-bounds` |
| 4 | Attempt to use both SETDATE() and DAYINDEX() in a loop | 循环里两个函数都用了 | `date-functions` |
| 5 | Correctly generate value of type DATE using SETDATE() in a loop | `ThisDate ← SETDATE(DayNumber, 3, ThisYear)`，ThisDate 是 DATE | `date-functions` |
| 6 | Test if value represents a Sunday using DAYINDEX() in a loop | `IF DAYINDEX(ThisDate) = 1 THEN` | `date-functions` |
| 7 | Increment Sunday count in a loop and initialised correctly before loop | `SundayCount ← 0` 在循环前，`+ 1` 在 IF 里 | `accumulator`、`initialise-variables` |
| 8 | Return day number of third Sunday | `RETURN DayNumber` | `return-value` |

Max 7。验算 2022 年：3 月 1 日是星期二，星期日是 6、13、20 日，第三个是 20，与题目例子一致。MS 另有一套不用循环的计分清单（先求 3 月 1 日的 DAYINDEX，再直接算），两种都可以满分。

**直观**　翻三月的日历，从 1 号往后一天天看，每碰到一个星期日就扳一个手指，扳到第三个手指时，手指按着的那天就是答案。

**同题 Python 版要点**
- `SETDATE(d, m, y)` ↔ `date(y, m, d)`：**参数顺序相反**。
- `DAYINDEX(d)` ↔ `d.isoweekday() % 7 + 1`（Python 的 `isoweekday()` 星期一 = 1 … 星期日 = 7）。
- Python 没有后测循环，`REPEAT … UNTIL` 改写成 `while` + 条件（或 `while True` + `break`）。
- 先过阶梯 **L05 E06**（日期函数：插页 ↔ `datetime.date`）。

```python
from datetime import date

def adjust_clock(this_year: int) -> int:
    day_number = 0
    sunday_count = 0
    while sunday_count < 3:
        day_number = day_number + 1
        this_date = date(this_year, 3, day_number)       # year, month, day
        if this_date.isoweekday() % 7 + 1 == 1:          # DAYINDEX = 1 means Sunday
            sunday_count = sunday_count + 1
    return day_number
```

**下一道变式**　⟦9618_s25_23:7(a)(i)⟧　（过程 UpdateVisit()：两个 BYREF 参数；用 `TODAY()` 与 `MONTH()` 判断是否同月，同月积分加 4、否则加 1，再把上次来访日期改成今天。）

<!-- auto:drills P2-PG-12 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| PG-01 vs SD-08 | 只认出结构、写行号 → PG-01；解释代码的作用、为什么某分支不执行 → SD-08 | tick / line number 还是 explain why |
| PG-02 vs PG-03 | 给表达式求值 → PG-02；给结果或类型、要你填函数或写语句 → PG-03 | Evaluates to 一栏空着还是 Expression 一栏空着 |
| PG-02 vs SD-06 | 求值，错的那行写 ERROR → PG-02；说出每条语句错在哪 / 改正 → SD-06 | Write 'ERROR' 还是 State the error |
| PG-03 vs PG-12 | 单条语句以插页一般函数为主 → PG-03；核心是 SETDATE、DAYINDEX 等日期函数 → PG-12 | 有没有 DATE 变量 |
| PG-04 vs PG-05 | 改写选择结构（IF ↔ CASE）→ PG-04；选择或改写循环 → PG-05 | CASE / IF 还是 loop |
| PG-05 vs AD-05 | 判断哪种循环更合适并说理由 → PG-05；给流程图说出循环名称 → AD-05 | appropriate / justify 还是 flowchart |
| PG-06 vs PG-07 | 解释概念（参数、BYREF、局部变量、过程与函数）→ PG-06；写出模块头 → PG-07 | explain / state 还是 write the header |
| PG-06 vs AD-02 | 为什么用子程序、库程序 → PG-06；把问题拆成具体模块并写用途 → AD-02 | subroutine / library 还是 decomposition / sub-modules |
| PG-07 vs SD-03 | 由结构图或说明写模块头 → PG-07；由说明或模块头画结构图 → SD-03 | header 还是 structure chart |
| PG-08 vs AD-03 | 常量、注释、缩进、效率 → PG-08；变量名与标识符表 → AD-03 | constants / efficient 还是 identifier table |
| PG-09 vs PG-10 | 循环读入一串输入、统计 → PG-09；对参数或一次输入的几个值计算判断 → PG-10 | input … until / one at a time 还是 parameter |
| PG-09 vs DT-05 | 输入的值不存储 → PG-09；输入的值存进数组再处理 → DT-05 | 有没有 store … in the array |
| PG-10 vs PG-11 | 本质是算术（逐位求和、校验位），哪怕某种解法转成了字符串 → PG-10；参数是字符串、考子串与逐字符 → PG-11 | 题目给的参数是数还是串 |
| PG-11 vs DT-09 / DT-10 | 只处理一个字符串 → PG-11；还要读写文件且文件操作 ≥ 2 分 → DT-09 / DT-10 | 有没有 OPENFILE |
| `MID` vs `LEFT` / `RIGHT` | 取中间某个位置的字符或子串 → `MID(S, 起点, 长度)`；取开头 / 结尾 n 个 → `LEFT` / `RIGHT` | 起点是不是 1 或串尾 |
| BYVAL vs BYREF | 只把值传进去 → BYVAL（默认）；要把改动带回调用者 → BYREF | 双头箭头、changed values must be available after the call |
