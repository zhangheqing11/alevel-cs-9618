## PG　编程：伪代码 ↔ Python 对照与模板 {#core-PG}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。伪代码按 2027–29 指南与当卷插页书写，Python 按阶梯推荐写法（全表见 `ladder/design.md` §5；字符串与日期的细节见阶梯 L05 对照卡）。P2 只认伪代码；Python 列用来在阶梯里把同一逻辑跑通、测过。

### 1. 运算符与表达式（PG-02、PG-03）

| 运算 | 伪代码 | Python | 不对应之处 / 常见失分 |
|:--|:--|:--|:--|
| 赋值 | `X ← X + 1` | `x = x + 1` 或 `x += 1` | 伪代码没有 `+=`，`=` 只用于比较和 CONSTANT |
| 相等 / 不等 | `=`、`<>` | `==`、`!=` | 伪代码写 `==`、`!=` 不给分 |
| 实数除法 | `Total / Count`（结果 REAL） | `total / count` | 求平均不能用 DIV |
| 整除 / 取余 | `17 DIV 5` = 3，`17 MOD 5` = 2 | `17 // 5`、`17 % 5` | 伪代码写 `%`、`//` 不给分 |
| 取整 | `INT(27.5415)` = 27 | `int(27.5415)` | 截去小数，不是四舍五入 |
| 乘方 | 题目给出时用 `^`：`Value ^ 2` | `value ** 2` | 题目没给 `^` 时写 `Value * Value` |
| 逻辑 | `AND`、`OR`、`NOT` | `and`、`or`、`not` | 伪代码不保证短路求值（D25） |
| 连接字符串 | `"Total: " & NUM_TO_STR(T)` | `"Total: " + str(t)` | `&` 不能直接接数值；`+` 不能接字符串 |
| 输出多项 | `OUTPUT "Total: ", T` | `print("Total:", t)` | 逗号分隔，不必转换 |
| 字符 / 字符串字面量 | `'A'`（CHAR）、`"Hello"`（STRING） | `"A"`、`"Hello"` | Python 不分 CHAR 与长度 1 的 str |

**运算顺序**：指南只规定乘除先于加减（与数学习惯相同），并建议复杂表达式用括号写明顺序。所以写代码时一律加括号（`(A > 3) AND (B < 5)`）；求值时由内向外，先算括号与函数调用，再算乘除、加减、比较，最后算逻辑运算。

### 2. 插页函数（PG-02、PG-03、PG-11、PG-12）

只能用当卷插页里的函数。下表按 2025 年插页（以 9618_w25_in_21 为代表）列出，Python 对应写法见阶梯 L05 对照卡 §2、§6。

| 插页函数 | 例 | Python | 注意 |
|:--|:--|:--|:--|
| `LEFT(S, x)` | `LEFT("ABCDEFGH", 3)` → `"ABC"` | `s[:x]` | |
| `RIGHT(S, x)` | `RIGHT("ABCDEFGH", 3)` → `"FGH"` | `s[len(s) - x:]` | `s[-x:]` 在 x = 0 时得整个串 |
| `MID(S, x, y)` | `MID("ABCDEFGH", 2, 3)` → `"BCD"` | `s[x - 1:x - 1 + y]` | y 是**长度**，不是结束位置 |
| `LENGTH(S)` | `LENGTH("Happy Days")` → 10 | `len(s)` | 只用于字符串 |
| `TO_UPPER(x)` / `TO_LOWER(x)` | `TO_UPPER('a')` → `'A'` | `x.upper()` / `x.lower()` | 指南另有只收 CHAR 的 UCASE / LCASE，以插页为准 |
| `NUM_TO_STR(x)` | `NUM_TO_STR(87.5)` → `"87.5"` | `str(x)` | |
| `STR_TO_NUM(x)` | `STR_TO_NUM("23.45")` → 23.45 | `int(s)` / `float(s)` | |
| `IS_NUM(S)` | `IS_NUM("-12.36")` → TRUE | 无直接对应（`try: float(s)`） | `isdigit()` 对负数、小数为 False |
| `ASC(c)` / `CHR(x)` | `ASC('A')` → 65，`CHR(66)` → `'B'` | `ord(c)` / `chr(x)` | |
| `INT(x)` | `INT(27.5415)` → 27 | `int(x)` | |
| `RAND(x)` | `RAND(87)` 可能得 35.430729 | `random.random() * x` | 0 到 x，不含 x |
| `DAY` / `MONTH` / `YEAR(D)` | `MONTH(04/10/2003)` → 10 | `d.day` / `d.month` / `d.year` | Python 是属性，不加括号 |
| `DAYINDEX(D)` | `DAYINDEX(09/05/2023)` → 3 | `d.isoweekday() % 7 + 1` | 星期日 = 1 |
| `SETDATE(Day, Month, Year)` | `SETDATE(26, 10, 2003)` | `date(2003, 10, 26)` | 参数顺序相反 |
| `TODAY()` | | `date.today()` | |
| `EOF(FileName)` | | 用 `for line in file:` | 文件题见 DT 章 |

### 3. 选择结构（PG-04）

| 结构 | 伪代码 | Python | 不对应之处 |
|:--|:--|:--|:--|
| 单分支 | `IF … THEN` … `ENDIF` | `if …:` | 伪代码必须写 ENDIF |
| 双分支 | `IF … THEN` … `ELSE` … `ENDIF` | `if …:` … `else:` | |
| 多分支 | ELSE 里嵌套 IF，每层一个 ENDIF | `if` / `elif` / `else` | 伪代码没有 ELSIF |
| CASE | `CASE OF X` / `1 : …` / `2 TO 5 : …` / `OTHERWISE : …` / `ENDCASE` | `match x:` / `case 1:` / `case _:`，或 if / elif | CASE 按顺序测试，第一个符合的执行后就结束 |

```pseudocode
CASE OF Mark
   80 TO 100 : Grade ← 'A'
   60 TO 79 : Grade ← 'B'
   OTHERWISE : Grade ← 'U'
ENDCASE

// the same without CASE
IF Mark >= 80 AND Mark <= 100 THEN
   Grade ← 'A'
ELSE
   IF Mark >= 60 AND Mark <= 79 THEN
      Grade ← 'B'
   ELSE
      Grade ← 'U'
   ENDIF
ENDIF
```

```python
if 80 <= mark <= 100:
    grade = "A"
elif 60 <= mark <= 79:
    grade = "B"
else:
    grade = "U"
```

### 4. 循环（PG-05、PG-09）

| 循环 | 伪代码 | Python | 选它的信号 |
|:--|:--|:--|:--|
| 计数循环 | `FOR I ← 1 TO 10` … `NEXT I` | `for i in range(1, 11):` | 次数已知 |
| 倒序 / 步长 | `FOR I ← 10 TO 1 STEP -1` | `for i in range(10, 0, -1):` | 从后往前 |
| 前测循环 | `WHILE <继续条件>` … `ENDWHILE` | `while <继续条件>:` | 次数未知，可能一次都不执行 |
| 后测循环 | `REPEAT` … `UNTIL <结束条件>` | `while True:` … `if <结束条件>: break` | 至少执行一次（先输入再检查） |

**输入到结束值为止**（先读一次，循环最后再读；结束值不被处理）

```pseudocode
INPUT ThisNum
WHILE ThisNum <> 99
   Total ← Total + ThisNum
   INPUT ThisNum
ENDWHILE
```

```python
this_num = int(input("Value: "))
while this_num != 99:
    total = total + this_num
    this_num = int(input("Value: "))
```

**输入直到合法**（后测循环）

```pseudocode
REPEAT
   OUTPUT "Enter a mark from 0 to 100: "
   INPUT Mark
UNTIL Mark >= 0 AND Mark <= 100
```

```python
while True:
    mark = int(input("Enter a mark from 0 to 100: "))
    if 0 <= mark <= 100:
        break
```

### 5. 过程、函数与参数（PG-06、PG-07）

| 内容 | 伪代码 | Python | 不对应之处 |
|:--|:--|:--|:--|
| 过程定义 | `PROCEDURE Show(Msg : STRING)` … `ENDPROCEDURE` | `def show(msg: str) -> None:` | 伪代码参数必须写类型 |
| 函数定义 | `FUNCTION Max(A : INTEGER, B : INTEGER) RETURNS INTEGER` … `ENDFUNCTION` | `def max_of(a: int, b: int) -> int:` | RETURNS 后写类型名 |
| 返回 | `RETURN Result` | `return result` | |
| 调用过程 | `CALL Show("Hi")` | `show("Hi")` | Python 不写 CALL |
| 调用函数 | `Big ← Max(3, 7)`（在表达式里） | `big = max_of(3, 7)` | 函数不用 CALL |
| 按引用传递 | `PROCEDURE Split(T : INTEGER, BYREF H : INTEGER, BYREF M : INTEGER)` | 没有 BYREF：`return h, m`，调用处 `h, m = split(t)` | 指南：BYREF 后连续同法传递的参数可不重复写关键字 |
| 全局变量 | 模块外 DECLARE，模块里直接用 | 模块里改全局变量要 `global x` | |
| 局部变量 | 模块里 DECLARE | 函数里赋值即局部 | 每次调用都重新创建 |

**BYREF 的 Python 写法**（阶梯 L04 E01、E02）

```pseudocode
PROCEDURE SplitMinutes(Total : INTEGER, BYREF Hours : INTEGER, BYREF Mins : INTEGER)
   Hours ← Total DIV 60
   Mins ← Total MOD 60
ENDPROCEDURE

CALL SplitMinutes(135, H, M)          // afterwards H = 2 and M = 15
```

```python
def split_minutes(total: int) -> tuple[int, int]:
    return total // 60, total % 60

h, m = split_minutes(135)             # the returned tuple replaces BYREF
```

### 6. 字符串处理模板（PG-11）

**逐字符扫描并造新串**

```pseudocode
NewString ← ""
FOR Index ← 1 TO LENGTH(InString)
   ThisChar ← MID(InString, Index, 1)
   IF ThisChar = Char1 THEN
      ThisChar ← Char2
   ENDIF
   NewString ← NewString & ThisChar
NEXT Index
```

```python
new_string = ""
for index in range(len(in_string)):
    this_char = in_string[index]
    if this_char == char1:
        this_char = char2
    new_string = new_string + this_char
```

**按分隔符拆字段**（最后一个字段后面没有分隔符，循环后补处理）

```pseudocode
Field ← ""
FOR Index ← 1 TO LENGTH(InString)
   ThisChar ← MID(InString, Index, 1)
   IF ThisChar = ',' THEN
      Total ← Total + STR_TO_NUM(Field)
      Field ← ""
   ELSE
      Field ← Field & ThisChar
   ENDIF
NEXT Index
Total ← Total + STR_TO_NUM(Field)
```

```python
field = ""
for this_char in in_string:
    if this_char == ",":
        total = total + int(field)
        field = ""
    else:
        field = field + this_char
total = total + int(field)
# P4 may simply use: total = sum(int(x) for x in in_string.split(","))
```

**定长字段**

| 字段 | 伪代码 | Python |
|:--|:--|:--|
| 前 5 个字符 | `LEFT(TLine, 5)` | `t_line[:5]` |
| 第 6 个起的 32 个 | `MID(TLine, 6, 32)` | `t_line[5:37]` |
| 第 38 个起到串尾 | `RIGHT(TLine, LENGTH(TLine) - 37)` | `t_line[37:]` |

**字符判断**

| 判断 | 伪代码 | Python |
|:--|:--|:--|
| 大写字母 | `Ch >= 'A' AND Ch <= 'Z'` | `"A" <= ch <= "Z"` |
| 任意字母 | `TO_UPPER(Ch) >= 'A' AND TO_UPPER(Ch) <= 'Z'` | `"A" <= ch.upper() <= "Z"` |
| 数字 | `Ch >= '0' AND Ch <= '9'` | `"0" <= ch <= "9"` |
| 不分大小写相等 | `TO_UPPER(A) = TO_UPPER(B)` | `a.upper() == b.upper()` |
| 第 i 个从右数 | `MID(S, LENGTH(S) - i + 1, 1)` | `s[len(s) - i]` |

### 7. 日期（PG-12）

```pseudocode
DECLARE ThisDate : DATE
ThisDate ← SETDATE(1, 3, ThisYear)            // 1 March
IF DAYINDEX(ThisDate) = 1 THEN                // Sunday
   OUTPUT "1 March is a Sunday"
ENDIF
IF MONTH(TODAY()) = MONTH(LastVisit) THEN
   Points ← Points + 4
ENDIF
```

```python
from datetime import date

this_date = date(this_year, 3, 1)             # year, month, day
if this_date.isoweekday() % 7 + 1 == 1:       # same numbering as DAYINDEX
    print("1 March is a Sunday")
if date.today().month == last_visit.month:
    points = points + 4
```

### 8. 随机数（PG-09）

| 要求 | 伪代码 | Python |
|:--|:--|:--|
| 0 到 n − 1 的整数 | `INT(RAND(n))` | `random.randint(0, n - 1)` |
| 1 到 6 的整数 | `INT(RAND(6)) + 1` | `random.randint(1, 6)` |
| Low 到 High（含两端） | `INT(RAND(High - Low + 1)) + Low` | `random.randint(low, high)` |
| −10 到 10 | `INT(RAND(21)) - 10` | `random.randint(-10, 10)` |
| 随机大写字母 | `CHR(INT(RAND(26)) + 65)` | `chr(random.randint(65, 90))` |

### 9. 术语（三层）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Sequence | 「To specify the order in which the steps of the algorithm have to be followed so that the task is completed correctly」⟦9618_w25_23:2(b)⟧ | 语句按先后顺序逐条执行 | 菜谱按步骤做 | P2-PG-01 |
| Selection | 「A selection construct // an IF statement」⟦9618_w23_21:2(b)⟧ | 按条件选择执行哪一部分代码（IF、CASE） | 岔路口 | P2-PG-01、P2-PG-04 |
| Iteration | 「An iterative construct // a (count-controlled) loop」⟦9618_w23_21:2(b)⟧ | 重复执行一段代码（FOR、WHILE、REPEAT） | 环岛 | P2-PG-01、P2-PG-05 |
| Count-controlled loop（选择理由） | 「The number of iterations required is known」⟦9618_s25_21:4(a)⟧ | 次数已知时用 FOR 循环 | 跑 10 圈 | P2-PG-05 |
| Conditional loop（选择理由） | 「the number of iterations is not known // loop ends following a specific input (in the loop)」⟦9618_w23_22:2(b)⟧ | 次数未知、由条件决定何时停时用 WHILE / REPEAT | 跑到累了为止 | P2-PG-05、P2-PG-09 |
| Subroutine（使用理由） | 「When a part of an algorithm performs a specific task」⟦9618_w22_22:1(a)(i)⟧ | 有名字、完成一个特定任务、可被调用的一段代码（过程或函数） | 一个可以随叫随到的帮手 | P2-PG-06 |
| Function vs procedure | 「A function returns a (single) value and a procedure does not」⟦9618_s25_23:6(a)⟧ | 函数返回一个值、在表达式里调用；过程不返回值、用 CALL 调用 | 函数是问答，过程是跑腿 | P2-PG-06、P2-PG-07 |
| Parameter | 「Term: Parameter(s) Use: to pass values / arguments to the procedure」⟦9618_w22_22:1(a)(ii)⟧ | 调用模块时用来传入数据的标识符 | 交给帮手的材料 | P2-PG-06、P2-PG-07 |
| Procedure interface | 「Provides a mechanism to allow calling program to pass data」⟦9618_w22_23:5(a)(ii)⟧ | 模块与调用者之间传数据的约定：参数的个数、类型、顺序 | 插头与插座的规格 | P2-PG-06 |
| Return type | 「The (data) type returned (by the function)」⟦9618_w25_23:1(b)(ii)⟧ | 函数头里 RETURNS 后面的类型 | 回执的格式 | P2-PG-07 |
| By reference (BYREF) | 「is reflected in the (subsequent) value in the calling module」⟦9618_s24_23:7(a)(ii)⟧ | 传的是变量本身，模块里的改动在调用者那里也生效 | 交出原件 | P2-PG-06、P2-PG-07 |
| By value (BYVAL) | 「is NOT reflected in the (subsequent) value in the calling module」⟦9618_s24_23:7(a)(ii)⟧ | 传的是值的副本，模块里的改动不影响调用者（未注明时默认按值） | 交出复印件 | P2-PG-06 |
| Local variable | 「Local variables are used within a module // are accessible only within the module (in which they are declared)」⟦9618_s25_23:1(a)(ii)⟧ | 在模块里声明、只在该模块里可用的变量，模块运行时才存在 | 自己抽屉里的东西 | P2-PG-06 |
| Global variable | 「Global variables are accessible to all parts of the program」⟦9618_s25_23:1(a)(ii)⟧ | 在所有模块之外声明、程序各处都能用的变量 | 公共白板 | P2-PG-06 |
| Benefit of local variables | 「The same variable name can be reused in other parts of the program」⟦9618_s25_23:1(a)(iii)⟧ | 同名可复用、模块自成一体、不会意外改到别处、内存可回收 | 各管各的抽屉 | P2-PG-06 |
| Lifetime of a local variable | 「A new (instance of) variable MyString is created each time the procedure is called / executed」⟦9618_w23_21:6(b)⟧ | 每次调用都新建，模块结束就消失，上次的值不保留 | 每次上课发一张新草稿纸 | P2-PG-06 |
| Library routine | 「They are tried and tested so free from errors」⟦9618_w22_21:1(a)⟧ | 别人写好、测试过、可直接调用的现成模块 | 买来的成品零件 | P2-PG-06 |
| Constant | 「The value cannot be changed // avoids being different in two places」⟦9618_s25_21:2(b)(ii)⟧ | 用名字代表一个运行中不变的值，只在一处定义 | 墙上的价目表 | P2-PG-08 |
| Comment | 「Change the statement into a comment」⟦9618_s23_22:5(d)⟧（让编译器忽略一句的办法） | `//` 之后的说明文字，编译器忽略 | 页边的批注 | P2-PG-08 |
| Efficient search | 「The loop / search can be terminated as soon as the (first occurrence of) SearchString / required value / required string / matching element is found」⟦9618_w25_21:5(b)(ii)⟧ | 找到目标就停止，不做多余的比较 | 找到钥匙就不再翻抽屉 | P2-PG-05、P2-PG-08 |

### 10. 常见失分（PG 章）

| 失分 | 正确做法 | 题型 |
|:--|:--|:--|
| 字符串结果漏引号；INT 当成四舍五入 | 字符串带 `""`；INT 只截去小数 | P2-PG-02 |
| 用插页以外的函数（`len`、`SUBSTRING`、`ROUND`） | 只用插页函数，名字一字不差 | P2-PG-02、P2-PG-03、P2-PG-11 |
| `ELSIF` / `elif`、少写 ENDIF | ELSE 里嵌套 IF，每层一个 ENDIF | P2-PG-04 |
| 选循环只写名字不写理由 | 次数已知 / 未知；找到就能停 | P2-PG-05 |
| BYREF 题只写“值会变” | 点名两个模块，说清模块结束后调用者的值变不变 | P2-PG-06 |
| 漏写 BYREF、`RETURNS` 后写变量名、函数参数加 BYREF | 带回值的过程参数加 BYREF；`RETURNS 类型名` | P2-PG-07 |
| 常量好处不结合情境 | 写出 postal rate / tax rate 只输入一次、只改一处 | P2-PG-08 |
| WHILE 条件里的变量还没有值；结束值被计入 | 循环前先读一次，循环最后再读 | P2-PG-09 |
| 随机数范围差一 | `INT(RAND(High - Low + 1)) + Low` | P2-PG-09 |
| 累乘器初值 0；只在一种情况下 RETURN | 累乘器为 1；每条路径都返回 | P2-PG-10 |
| `S[Index]` 取字符；`LEFT` 取中间字符 | `MID(S, Index, 1)` | P2-PG-11 |
| 拼接串没有先赋 `""`；用 OUTPUT 代替 RETURN | 循环前 `NewString ← ""`；循环后 RETURN | P2-PG-11 |
| 题目没要求却转换大小写 | 只在“不区分大小写”时用 TO_UPPER | P2-PG-11 |
| 拆分隔符时漏最后一个字段 | 循环后再处理一次 | P2-PG-11 |
| `SETDATE` 参数顺序错、`DAYINDEX` 记成星期一 = 1 | 日、月、年；星期日 = 1 | P2-PG-12 |
| 用 `Year`、`Day` 作标识符 | 换成 `ThisYear`、`DayNumber` | P2-PG-12 |
