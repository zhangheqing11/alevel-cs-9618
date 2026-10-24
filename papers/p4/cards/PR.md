## PR　输入、字符串与计算 {#ch-PR}

<!-- auto:chapter-stats -->

### 核心思想

PR 是 P4 最“基础”的一章：不涉及数组以外的数据结构，考的是把一段**规则**变成 Python——键盘输入怎样校验（PR-01）、字符串怎样逐字符处理（PR-02）、公式与多分支怎样算（PR-03）。它们很少单独成大题，常常是某道大题里的一问（Q1 里的 `Initialise()`、Q3 里的 `SplitData()`），也常作为别的题型的一部分出现（主程序里的输入校验、读文件后的拆字段）。

三条主线：

1. **输入一定要转类型、一定要循环到合法**。`input()` 返回字符串；数字要 `int(...)`；“validate”“until it is valid”就是一个 `while 不合法:` 再输入的循环。两个值各自校验、各自循环。
2. **字符串就是字符数组**。`s[i]` 取第 i 个字符（0 起），`len(s)` 是长度，`s[a:b]` 是切片；逐字符循环 `for i in range(len(s))`。题目说“不要用内置函数拆分 / 比较”时，就自己一个字符一个字符地做。
3. **照题目给的规则或伪代码一句一句翻译**。MS 常有一分叫 “Remainder of function correct”：结构要与给定算法一致，不多不少。`MODULUS` / `MOD` → `%`，`DIV` → `//`，“round down” → `int()` 或 `//`。

P4 的共同习惯（每个题型都适用，卷首“通用得分规则”有原句）：标识符照抄题目（`Initialise`、`DataStored`），模块头要对（“header (and end where appropriate)”），有返回值的要 `return`、不要 `print` 代替。

### 本章 Python 速查

```python
# input: always a string -> convert
Quantity = int(input("How many numbers (1 to 20)? "))
while Quantity < 1 or Quantity > 20:          # validate: loop until valid
    Quantity = int(input("Invalid. Enter 1 to 20: "))

# strings: 0-based index, len(), slice [start:end) end not included
Word = "computer"
First = Word[0]             # "c"
Rest = Word[1:]             # "omputer"
Middle = Word[2:5]          # "mpu"  (pseudocode MID(Word, 3, 3) with 1-based MID)
Code = ord("A")             # 65
Letter = chr(66)            # "B"
Upper = Word.upper()        # "COMPUTER"

# arithmetic
Quotient = 17 // 5          # 3   (DIV)
Remainder = 17 % 5          # 2   (MOD / MODULUS)
Average = 17 / 5            # 3.4 (REAL)
RoundedDown = int(42 / 10)  # 4   ("round down" for positive numbers)
```

### 题型树
<!-- auto:type-tree -->

### P4-PR-01　键盘输入与输入校验　{#P4-PR-01}

<!-- auto:stats P4-PR-01 -->

**考法**　在一个过程 / 函数或主程序里，用 `input()` 读一个或几个值，转换类型后校验，**循环到合法为止**。常见几种：①先读“要输入几个”并校验范围，再按这个数循环读入、存进数组（`Initialise()`）；②读一个查找值并校验范围，再调用查找函数、按给定格式输出结果；③读名字和分数两项，名字校验长度、分数校验范围，各自循环；④读一个下标（1 起），校验范围、减 1 变成数组下标，再检查这个位置是否“已被选过”，直到选到可用的；⑤计数循环里每次读两项（高度、风险），每项都循环到合法，再用这两项建对象存进数组。2021–25 的题多是“Amend the main program to …”，分值 3–6。

**识别信号**　prompts the user to input …；reads the input and validates it is between … (inclusive)；take … as input until it is valid；loops until …；must be a whole number between …；a 3-character player name；checks if the card is available (it has not already been selected)；Amend the main program to ask the user to input …

**解题思路**
1. **列规格**：读几个值、各是什么类型（整数要 `int()`，大小写不敏感的要 `.lower()`）、各自的合法条件（范围的两端是否包含：inclusive → `>=`、`<=`）、不合法时怎么办（再输入）。
2. **一项一个校验循环**：`Value = int(input("…"))` → `while 不合法:` → 再读一次。两项数据就写两个循环；不要把两项绑在一个条件里（一项错了两项都重输）。
3. **计数循环套校验循环**：要读 4 组数据时，外层 `for x in range(4):`，里层是校验循环——外层计数只在拿到合法数据后才前进（`for` 自然做到这一点）。
4. **提示语写进 `input("…")`**：提示文字放在括号里，不要先 `print` 再 `input()`（练习的自动测试按这个约定，D13）。
5. **校验之后的动作照题目**：存进数组下一个空位（并让计数加 1）、调用题目给的函数并**接住返回值**、按题给格式输出。
6. 题目只说“validate”而 MS 要求“whole number”时，`int(input())` 本身就是转换；要防止输入字母导致程序崩溃，再包一层 `try` / `except ValueError`（可选，见模板）。

**Python 模板**

```python
# global data (declare = create the real list, comment the type and size; D10 ①)
DataStored = [0] * 20      # INTEGER, 20 elements
NumberItems = 0            # INTEGER


def Initialise():                      # procedure: no parameter, no return
    global NumberItems                 # assigning to a global inside a subroutine
    Quantity = int(input("How many numbers will you enter (1 to 20)? "))
    while Quantity < 1 or Quantity > 20:               # loop until valid (inclusive)
        Quantity = int(input("Must be between 1 and 20. Enter again: "))
    for Count in range(Quantity):                      # read Quantity numbers
        DataStored[NumberItems] = int(input("Enter number: "))
        NumberItems = NumberItems + 1                  # next free space


def InputScore():                      # optional: also reject non-integer input
    Valid = False
    while not Valid:
        try:
            Score = int(input("Enter a score (1 to 100000): "))
            if Score >= 1 and Score <= 100000:
                Valid = True
            else:
                print("Out of range")
        except ValueError:
            print("Not a whole number")
    return Score


if __name__ == "__main__":
    NumberItems = 0
    Initialise()
```

伪代码对照（题目有时用伪代码描述输入循环）：

| 伪代码 | Python |
|:--|:--|
| `INPUT Quantity` | `Quantity = int(input("…"))`（数字要转换） |
| `REPEAT … UNTIL Quantity >= 1 AND Quantity <= 20` | 先读一次，`while Quantity < 1 or Quantity > 20:` 再读（条件取反） |
| `WHILE Valid = FALSE … ENDWHILE` | `while Valid == False:` 或 `while not Valid:` |
| `OUTPUT "The number ", N, " is found ", T, " times"` | `print("The number", N, "is found", T, "times")`（`print` 自动在各项之间加一个空格） |

**得分表述**（引自对应 MS）
- 「Prompt/output of suitable message to request the input of the quantity of numbers」⟦9618_s24_41:1(b)⟧
- 「validating between 1 and 20 inclusive」⟦9618_s24_41:1(b)⟧
- 「Taking each height as input until it is between 70 and 180 (inclusive)」⟦9618_w24_41:2(c)(ii)⟧
- 「Validate score input (integer (cast) between 1 and 100 000 inclusive)」⟦9618_s22_41:1(e)(i)⟧
- 「Converting input to array index (e.g. –1 each time)」⟦9618_s22_42:3(d)⟧
- 「Calling LinearSearch() with array and valid data input and storing/using return value」⟦9618_s23_41:1(d)(i)⟧

**得分点地图**（口径：核验语料 2022–2026s、主题型为本型、已拆得分点的行，去掉 `equivalent_of` 行；同一行同一标签计一次；s26 行计入。共 5 行：⟦9618_s22_41:1(e)(i)⟧、⟦9618_s22_42:3(d)⟧、⟦9618_s23_41:1(d)(i)⟧、⟦9618_s24_41:1(b)⟧、⟦9618_w24_41:2(c)(ii)⟧）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 提示并读入（Prompt … and reading in） | 5 | `input-prompt` |
| 校验：循环到合法（validating between … inclusive / looping until …） | 5 | `input-validation` |
| 范围比较写对（两端是否包含） | 5 | `relational-ops` |
| 转成整数（integer (cast)） | 3 | `type-conversion` |
| 模块头；返回值 | 2 | `module-header`、`return-value` |
| 存进数组下一格 / 输入值减 1 变下标 | 2 | `array-index` |
| 按数量循环读入 | 2 | `count-loop` |
| 声明记录“已选”的数组 | 2 | `declare-array` |

“提示 + 读入 + 范围校验循环”三分 5 行全有，与题目情境无关；其余技能（调用查找函数、建对象、输出结果）各只出现 1 次，跟着题目走。

**易错与失分**
- 只校验了一部分：名字要求“3 个字符”，写成 `len(Name) <= 3`，2 个字符的名字也被接受。考官报告指出名字常被检查成“3 个或更少”（⟦9618_s22_41:1(e)(i)⟧）。
- 校验放错位置：题目只要求校验“要输入几个”，却去限制后面每个数在 1–20 之间。考官报告指出了这个错误（⟦9618_s24_41:1(b)⟧）。
- 计数循环与校验循环搅在一起：一旦合法就跳出外层循环，或者不合法时计数照样加 1，结果只读到 3 组。考官报告把这两种列为常见错误（⟦9618_w24_41:2(c)(ii)⟧）。
- 下标差一：题目让用户输入 1–30，数组下标是 0–29，要减 1；题目要求返回下标时返回的却是卡片本身。考官报告指出返回卡片而非下标是常见错误（⟦9618_s22_42:3(d)⟧）。
- 只检查“是不是数字”而没有转成整数、没检查范围；考官报告说较好的答案会转换成整数或检查是否整数，再检查范围（⟦9618_s23_41:1(d)(i)⟧）。
- 调用查找函数后没有存下返回值，或把输出写进了查找函数里（⟦9618_s23_41:1(d)(i)⟧ 的考官报告）。
- MS 的 Python 范例不能照抄：⟦9618_s22_41:1(e)(i)⟧ 的范例先写 `score = -1`、再用 `while Score < 1 …`，大小写不一致，运行会报 `NameError`（MS p.10）；按得分点理解即可，自己写时变量名前后一致。

#### 代表题精讲　⟦9618_s24_41:1(b)⟧

**在考什么**　程序先读入一批整数，再排序、查找。1(a) 声明全局数组 `DataStored`（最多 20 个整数）和全局变量 `NumberItems`。1(b) 写过程 `Initialise()`：提示用户输入要输入几个数、读入并校验在 1 到 20 之间（含两端）、再提示输入每个数并存进 `DataStored`。5 分，MS 列 5 点，1 mark each。讲解时对照原卷 QP p.2（1(a)、1(b) 都在这一页；1(c) 主程序与测试数据在 p.3），MS p.5–6（Python 范例在 p.6）。

**完整作答**（整道大题的最终 Python；证据格按小问截取代码，早期测试截图在后续修改前另存）

```python
# Question1_J24: 1(a)-(e)
DataStored = [0] * 20  # global INTEGER array, 20 elements
NumberItems = 0  # global INTEGER


def Initialise():
    global NumberItems
    Quantity = int(input("How many numbers (1 to 20)? "))
    while Quantity < 1 or Quantity > 20:
        Quantity = int(input("Invalid. Enter 1 to 20: "))
    for Count in range(Quantity):
        DataStored[NumberItems] = int(input("Enter number: "))
        NumberItems = NumberItems + 1


def BubbleSort():
    for Pass in range(NumberItems - 1):
        for Index in range(NumberItems - Pass - 1):
            if DataStored[Index] > DataStored[Index + 1]:
                Temp = DataStored[Index]
                DataStored[Index] = DataStored[Index + 1]
                DataStored[Index + 1] = Temp


def BinarySearch(DataToFind):
    First = 0
    Last = NumberItems - 1
    while First <= Last:
        MidValue = (First + Last) // 2
        if DataStored[MidValue] == DataToFind:
            return MidValue
        elif DataToFind < DataStored[MidValue]:
            Last = MidValue - 1
        else:
            First = MidValue + 1
    return -1


if __name__ == "__main__":
    NumberItems = 0
    Initialise()
    for X in range(NumberItems):
        print(DataStored[X], end=" ")
    print()
    BubbleSort()
    for X in range(NumberItems):
        print(DataStored[X], end=" ")
    print()
    Search = int(input("Enter a number to find: "))
    print(BinarySearch(Search))
```

**运行核对**　最终程序已补齐 1(a)–(e)：初次输入 30、5、3、9、4、1、2 时，30 被拒、读入 5 项，先输出 3 9 4 1 2，再升序输出；最终版还会询问查找值。1(c)(ii) 的早期截图应在加入排序 / 查找前保留；最终两组指定查找测试见 SR-02。整题 QP p.2–5 / MS p.4–13。

**与 MS 逐点对齐**（MS 印的点与语料 `markpoints[].n` 一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure heading (and close where appropriate) with **no** parameter. | `def Initialise():`，没有参数，也没有 `return` 值 | `module-header` |
| 2 | Prompt/output of suitable message to request the input of the quantity of numbers **and** reading in quantity of numbers **and** storing/using … | `Quantity = int(input("How many …"))` | `input-prompt`、`type-conversion` |
| 3 | … validating between 1 and 20 inclusive | `while Quantity < 1 or Quantity > 20:` 再输入 | `input-validation`、`relational-ops` |
| 4 | Looping quantity input number of times, taking an **integer** input each time … | `for Count in range(Quantity):` 里 `int(input(…))` | `count-loop`、`input-prompt` |
| 5 | ... storing each input in next space in DataStored | `DataStored[NumberItems] = …`，`NumberItems` 加 1 | `array-index` |

MS 的 Python 范例（p.6）用 `DataStored.append(…)`，并把 `NumberItems` 直接设成输入的数量；而 1(a) 的 Python 范例只写了 `global DataStored #integer`，没有真的建出数组。本手册按决策 D10 ①建出 20 个元素的真实 list，所以第 5 点用“下一个空位 + 计数加 1”的写法；两种写法都满足“storing each input in next space”。

**证据格怎么交**　证据文档 1(b) 格贴 `Initialise()` 的完整代码（从 `def` 到最后一行）。1(a) 的两行声明贴在 1(a) 格，主程序贴在 1(c)(i) 格；1(c)(ii) 是截图格，MS 要截图里看得到：数量先输入 30 被拒、再输入 5（「Output showing quantity entered twice (30 and 5) with first being invalid」⟦9618_s24_41:1(c)(ii)⟧），以及数组输出 3 9 4 1 2。

**直观**　像点菜前先问“几位？”——回答 30 位，服务员说“最多 20 位”，再问一次；回答 5 位，就拿 5 份菜单，一份一份收回来放进桌上的 20 个格子里，格子从左往右放。

**对应练习与阶梯**　练习目录 practice/p4/9618_s24_41_q1/（T35 生成，含 1(a)–1(e) 全题）；先过阶梯 **L03 E03**（输入校验循环）、**L09 E02**（两项分别校验、反复输入）。

**下一道变式**　⟦9618_w24_41:2(c)(ii)⟧　（计数循环里套两个校验循环：4 道栏杆，每道的高度 70–180、风险 1–5 各自循环到合法，再用这两个值创建 `Fence` 对象存进数组 `Course`。MS 最多 5 分。）

<!-- auto:drills P4-PR-01 -->

### P4-PR-02　字符串处理　{#P4-PR-02}

<!-- auto:stats P4-PR-02 -->

**考法**　对字符串参数或输入逐字符处理，常带“不要用内置函数”的限制。2022–25 的四种：①把题给的伪代码（数小写元音，`MID` 从 0 起）翻译成 Python；②逐字符比较两个字符串，判断谁的字母顺序在前，返回 1 或 2（不能用内置比较函数）；③按分号把一个字符串拆成 4 段存进数组并返回（不能用 `split`）；④校验位：取输入的前 6 位数字按规则算出校验位，与第 7 位（或 `X`）比较，合法的去掉校验位后入队，并数出不合法的个数。分值 4–6。

**识别信号**　takes a string as a parameter；one character at a time；Do not use an inbuilt function to split the string；Do not use an in-built string comparison function；check digit；character in position …；The first character in a string is in position 0；MID / LENGTH 的伪代码说明。

**解题思路**
1. **先认下标约定**：Python 的 `s[0]` 是第一个字符。题目伪代码的 `MID(X, Y, Z)` 若写明“position 0 是第一个字符”，就对应 `X[Y:Y+Z]`；若按 2027–29 指南（1 起），对应 `X[Y-1:Y-1+Z]`。
2. **逐字符循环**：`for Index in range(len(S)):` 里用 `S[Index]`；要边读边判断何时停（遇到分隔符、两个字符不同），用 `while` 加下标。
3. **拼字符串**：`Temp = ""` 起步，`Temp = Temp + Character`；遇到分隔符就把 `Temp` 存进数组下一格、计数加 1、`Temp` 清空。
4. **比较字符**：`<`、`>` 直接比较两个字符（按字符编码，小写字母按字母序）；题目禁止内置比较函数时，指的是不能直接比较整个字符串，逐个字符比较是允许的。
5. **数字字符要转**：`int(S[0])` 才是数字 9；`"X"` 不能 `int()`，要先判断。
6. **返回还是输出**：题目说 returns 就 `return`，主程序再输出。

**Python 模板**

```python
def SplitData(DataString):                 # split at ';' without split()
    Parts = [""] * 4                       # STRING, 4 elements (size from the question)
    NextPart = 0                           # next free index in Parts
    Temp = ""
    for Index in range(len(DataString)):   # every character
        Character = DataString[Index]
        if Character == ";":               # separator: store the finished piece
            Parts[NextPart] = Temp
            NextPart = NextPart + 1
            Temp = ""
        else:
            Temp = Temp + Character        # build the current piece
    return Parts


def CompareStrings(First, Second):         # one character at a time
    Count = 0
    while First[Count] == Second[Count]:   # the question promises a difference exists
        Count = Count + 1
    if First[Count] < Second[Count]:
        return 1
    else:
        return 2
```

伪代码对照（题目给的字符串函数说明各卷不同，以题目为准）：

| 伪代码 | Python | 注意 |
|:--|:--|:--|
| `LENGTH(S)` | `len(S)` | |
| `MID(S, P, N)`（题目写明 0 起） | `S[P:P+N]` | 切片终点不包含 |
| `MID(S, P, N)`（指南 1 起） | `S[P-1:P-1+N]` | 起点减 1 |
| `RIGHT(S, N)` | `S[len(S)-N:]` | `S[-N:]` 在 N = 0 时返回整串；`LEFT` 不在 2027–29 指南的函数表里，题目给出时对应 `S[:N]` |
| `LCASE(C)` / `UCASE(C)` | `C.lower()` / `C.upper()` | 指南里参数是单个字符；Python 的方法对整串也可用 |
| `S1 & S2` | `S1 + S2` | 数字先 `str()` |
| `ASC(C)` / `CHR(N)` | `ord(C)` / `chr(N)` | |

**得分表述**（引自对应 MS）
- 「Looping through each character in each string parameter」⟦9618_w24_41:1(c)⟧
- 「Comparing character from parameter to ';'」⟦9618_w25_43:3(b)(ii)⟧
- 「concatenate current character to a string until ';' is found」⟦9618_w25_43:3(b)(ii)⟧
- 「Checking the first character against all vowels」⟦9618_w23_41:1(a)(i)⟧
- 「comparing check digit to character in position 6」⟦9618_s24_41:3(d)(i)⟧
- 「Returning string array without semicolons」⟦9618_w25_43:3(b)(ii)⟧

**得分点地图**（口径同 PR-01。共 4 行：⟦9618_s24_41:3(d)(i)⟧、⟦9618_w23_41:1(a)(i)⟧、⟦9618_w24_41:1(c)⟧、⟦9618_w25_43:3(b)(ii)⟧）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 函数 / 过程头（参数个数对） | 4 | `module-header` |
| 字符比较（与元音、`;`、`X`、另一串的同位字符） | 4 | `char-compare` |
| 按位置取字符或子串 | 3 | `string-index` |
| 逐字符循环 / 循环次数对 | 2 + 2 + 2 | `char-loop`、`count-loop`、`loop-bounds` |
| 用字符串函数（长度、截取） | 2 | `string-functions` |
| 累加 / 计数 | 2 | `accumulator` |
| 返回结果 | 2 | `return-value` |

模块头和“逐字符比较”4 行全有；“按位置取字符”3 行有。

**易错与失分**
- 比较整个字符串而不是逐字符，或循环有错导致没有逐个检查；返回值 1、2 弄反。考官报告指出了这三种错误（⟦9618_w24_41:1(c)⟧）。
- 把伪代码翻译成 Python 时漏改循环条件：伪代码 `FOR X ← 0 TO LengthString - 1` 对应 `range(0, LengthString)`，不是 `range(0, LengthString - 1)`；`MID` 的参数用错。考官报告提醒要照给定结构翻译，不增不减（⟦9618_w23_41:1(a)(i)⟧）。
- 拆分后没有存进数组，或没有 `return` 而是直接输出（⟦9618_w25_43:3(b)(ii)⟧ 的考官报告）。
- 校验位题：只读了 1 次输入，或把 10 个字符当 10 次输入；合法时存的是带校验位的 7 位，没去掉校验位；没数不合法的个数（⟦9618_s24_41:3(d)(i)⟧ 的考官报告）。
- 校验位题 MS 的 Python 范例（p.36）在第 7 位是 `X` 而算出的校验位不是 10 时，会执行 `int(Data[6])` 而报 `ValueError`；照得分点写，自己的代码先判断是不是 `X` 再转换。

#### 代表题精讲　⟦9618_w25_43:3(b)(ii)⟧

**在考什么**　程序里有一个字符串 `"x=0;y=1;x=x+y;y++;"`，由 4 条语句组成，每条以分号结尾。函数 `SplitData()` 接收一个字符串参数，把它拆成 4 行代码：每行存进数组的一个新元素，**不带分号**，最后返回这个字符串数组。不许用内置函数拆分。6 分，MS 列 6 点，1 mark each。讲解时对照原卷 QP p.13（3(b)(i)–(iv) 都在这一页），MS p.35–37（Python 范例在 p.37）。

**完整作答**（整道大题的最终 Python；证据格按小问截取代码，早期测试截图在后续修改前另存）

```python
# Question3_N25: 3(a)-(b)
def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if NumberElements == 0:
        return 0
    if ArrayCopy[0] == DataToFind:
        return 1 + RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
    else:
        return RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)


def SplitData(DataString):
    Parts = [""] * 4  # STRING, 4 elements
    Next = 0
    Temp = ""
    for Index in range(len(DataString)):
        Character = DataString[Index]
        if Character == ";":
            Parts[Next] = Temp
            Next = Next + 1
            Temp = ""
        else:
            Temp = Temp + Character
    return Parts


if __name__ == "__main__":
    MyArray = [0, 5, 1, 2, 5, 9, 9, 6, 5, 0]  # INTEGER, 10 elements
    print(RecursiveCount(MyArray, 10, 0))
    Code = "x=0;y=1;x=x+y;y++;"  # local STRING
    Statements = SplitData(Code)
    for Index in range(4):
        print(Statements[Index])
```

**运行核对**　最终程序包含 3(a) 递归计数与 3(b) 拆分：先输出 2，再依次输出 x=0、y=1、x=x+y、y++ 四行。3(a)(iii) 与 3(b)(iv) 的截图分别按各自证据格保存。整题 QP p.12–13 / MS p.32–39。

**与 MS 逐点对齐**（MS 印的点与语料编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function header, taking one string parameter | `def SplitData(DataString):` | `module-header` |
| 2 | Loop e.g. four times/through each character in parameter | `for Index in range(len(DataString)):` | `char-loop`、`loop-bounds` |
| 3 | Comparing character from parameter to ';' … | `if Character == ";":` | `char-compare` |
| 4 | … concatenate current character to a string until ';' is found | `Temp = Temp + Character` | `string-concat` |
| 5 | … when ';' found storing string in array | `Parts[Next] = Temp` | `declare-array`、`array-index` |
| 6 | Returning string array without semicolons | `return Parts`（分号从没加进 `Temp`） | `return-value` |

MS 的 Python 范例（p.37）是另一种结构：外层 `for x in range(4)` 数“段”，里层 `while Character != ";"` 一个个字符往后读，用 `try` / `except` 防止读过串尾。两种都满足 MP2（“four times”或“through each character”都写在 MS 里）。本手册的写法只有一层循环，下标不会越界，不需要 `try`。

**证据格怎么交**　3(b)(ii) 格贴整个 `SplitData()`；3(b)(i)（1 分：把字符串存进变量）与 3(b)(iii)（调用并逐行输出）贴主程序；3(b)(iv) 截图格要看得到 4 行输出 `x=0`、`y=1`、`x=x+y`、`y++`（⟦9618_w25_43:3(b)(iv)⟧ 的 MS 只列这 4 行）。

**直观**　像抄写员沿着一行字往右看：每看到一个字就抄进草稿；看到分号，就把草稿撕下来放进下一个格子，换一张新草稿。

**对应练习与阶梯**　练习目录 practice/p4/9618_w25_43_q3/（T35 生成，含 3(a) 递归与 3(b) 拆分）；先过阶梯 **L05 E03**（逐字符循环）、**L05 E01**（切片实现 LEFT / RIGHT / MID）。

**下一道变式**　⟦9618_w24_41:1(c)⟧　（换成“两个串逐字符比较”：`CompareStrings()` 返回 1 或 2，不能用内置的字符串比较，要找到第一个不同的字符再比。4 分。）

<!-- auto:drills P4-PR-02 -->

### P4-PR-03　数值计算与分支逻辑　{#P4-PR-03}

<!-- auto:stats P4-PR-03 -->

**考法**　按题目给的公式、规则或伪代码计算，返回或输出结果。2022–25 的几种：①把题给的迭代伪代码（求一个数所有因数之和，用 `MODULUS`）翻译成 Python；②按规则给手牌算分：红 +5、蓝 +10、黄 +15，再加上牌面数字，用 getter 取属性；③比较两个玩家的得分，输出赢家或平局；④读入方向字母 A / W / S / D，校验后按方向改坐标；⑤两个角色比五场，每场比较两个函数的返回值、给赢家加 1 分、输出每场结果，最后比总分；⑥输入树名与当前高度，算出长到最高要几年。常在 OOP 情境里出现（要用 getter、调用对象的方法），分值 2–7。

**识别信号**　calculates and returns …；If … is …, … points are added；The character with the highest … gets 1 point；If both … the same …, a message is output stating that … is a draw；The operator MODULUS calculates the remainder；totals all the divisors；calculate and output how many years …；If ‘A’ is input, the character moves left (x coordinate minus 1)。

**解题思路**
1. **把规则列成表**：条件 → 动作。互斥的条件用 `if` / `elif` / `else`；不互斥的（每张牌都要加数字，再按颜色加分）分开写。
2. **找循环**：“for each card / event / divisor”→ 计数循环；题目给了伪代码就照伪代码的循环（`WHILE Number <> 0` → `while Number != 0:`）。
3. **累加器**：循环前 `Total = 0`，循环里 `Total = Total + …`；循环后 `return Total`。
4. **比较与平局**：三路比较 `>`、`<`、相等各一个分支；“draw”是单独的输出。
5. **运算符翻译**：`MOD` / `MODULUS` → `%`；`DIV` → `//`；`/` 结果是小数；“round down”用 `int()`（正数）或 `//`。
6. **取对象的数据用 getter**：属性是私有的，`Card.GetColour()`、不是 `Card.Colour`。

**Python 模板**

```python
def CalculateValue(Player):                # Player is a Hand object
    Score = 0                              # accumulator before the loop
    for Count in range(5):                 # every card: indexes 0 to 4
        CardGot = Player.GetCard(Count)    # getters, attributes are private
        Score = Score + CardGot.GetNumber()
        Colour = CardGot.GetColour()
        if Colour == "red":                # mutually exclusive rules: if / elif / else
            Score = Score + 5
        elif Colour == "blue":
            Score = Score + 10
        else:
            Score = Score + 15
    return Score                           # return, not print


# three-way comparison with a draw
Score1 = 30
Score2 = 41
if Score1 > Score2:
    print("Player 1 wins")
elif Score2 > Score1:
    print("Player 2 wins")
else:
    print("It is a draw")
```

伪代码对照：

| 伪代码 | Python |
|:--|:--|
| `X MOD Y`（题目写 `MODULUS` 同义） | `X % Y` |
| `X DIV Y` | `X // Y` |
| `INT(X / 10)` | `int(X / 10)`（正数时即向下取整） |
| `WHILE Number <> 0 … ENDWHILE` | `while Number != 0:` |
| `IF … THEN … ELSE IF … ENDIF ENDIF` | `if … elif … else` |
| `CASE OF Move … 'A' : X ← X - 1 … ENDCASE` | `if Move == "A": X = X - 1` / `elif …` |

**得分表述**（引自对应 MS）
- 「Modulus calculation」⟦9618_w23_42:2(a)(i)⟧
- 「Return of correct value at correct place」⟦9618_w23_42:2(a)(i)⟧
- 「adding 5 to score for red, 10 to score for blue, 15 to score if yellow」⟦9618_w22_41:2(c)(i)⟧
- 「Using GetCard(), GetColour() and GetNumber() correctly」⟦9618_w22_41:2(c)(i)⟧
- 「comparing the return values from the two function calls」⟦9618_w24_42:1(e)(ii)⟧
- 「outputting message if it's a draw」⟦9618_w24_42:1(e)(ii)⟧

**得分点地图**（口径同 PR-01。共 6 行：⟦9618_s24_41:2(e)(ii)⟧、⟦9618_w22_41:2(c)(i)⟧、⟦9618_w22_41:2(c)(ii)⟧、⟦9618_w22_42:2(f)⟧、⟦9618_w23_42:2(a)(i)⟧、⟦9618_w24_42:1(e)(ii)⟧）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 多分支：按条件加分 / 比较后决定输出 | 4 | `nested-if` |
| 输出结果（赢家、平局、年数） | 3 | `output-format` |
| 计数循环（每张牌、每场比赛） | 3 | `count-loop` |
| 累加分数 / 总和 | 3 | `accumulator` |
| 调用对象的方法 | 3 | `method-call` |
| 读入数据 | 2 | `input-prompt` |
| 函数头；返回结果 | 2 | `module-header`、`return-value` |
| 遍历对象数组 | 2 | `array-of-objects` |
| 比较两个值 | 2 | `relational-ops` |

本型的分数主要在**分支与累加**上；6 行里 3 行是 OOP 情境（要调用方法、用 getter）。`div-mod`、`translate-pseudocode` 各 1 行，都在代表题里。

**易错与失分**
- 不会写取余，或在翻译伪代码时加了算法里没有的步骤。考官报告指出了这两点（⟦9618_w23_42:2(a)(i)⟧）。
- 把计算写成某个类的方法，而题目要的是独立函数；参数传了一张牌而不是整手牌；只加了颜色分、没加牌面数字；用 `print` 输出分数而不是返回。考官报告列了这几种（⟦9618_w22_41:2(c)(i)⟧）。
- 把每场比赛的数据手工写进代码，而不是从对象里取；属性是私有的却不用 getter（⟦9618_w24_42:1(e)(ii)⟧ 的考官报告）。
- MS 的 Python 范例有误：⟦9618_w22_41:2(c)(i)⟧ 的范例写 `for Count in range(0, 4):`，只算了 4 张牌（MS p.13；同页 Java 范例是 `X<5`）。得分点写的是 “looping through all 5 Card objects”，要写 `range(0, 5)`。

#### 代表题精讲　⟦9618_w23_42:2(a)(i)⟧

**在考什么**　题目给出迭代函数 `IterativeCalculate()` 的伪代码：求参数的所有因数之和（参数 10 → 1 + 2 + 5 + 10 = 18；参数 4 → 7）。`MODULUS` 求余数。Write program code for `IterativeCalculate()`. 5 分，MS 列 5 点，One mark each。讲解时对照原卷 QP p.6（情境与伪代码）与 p.7（小问），MS p.17–18（Python 范例在 p.18）。

题给伪代码（QP p.6，按原样）：

```pseudocode
FUNCTION IterativeCalculate(Number : INTEGER) RETURNS INTEGER
    DECLARE Total : Integer
    DECLARE ToFind : Integer
    ToFind ← Number
    Total ← 0
    WHILE Number <> 0
       IF ToFind MODULUS Number = 0 THEN
          Total ← Total + Number
       ENDIF
       Number ← Number - 1
    ENDWHILE
    RETURN Total
ENDFUNCTION
```

**完整作答**（整道大题的最终 Python；证据格按小问截取代码，早期测试截图在后续修改前另存）

```python
# Question2_N23: 2(a)-(b)
def IterativeCalculate(Number):
    ToFind = Number
    Total = 0
    while Number != 0:
        if ToFind % Number == 0:
            Total = Total + Number
        Number = Number - 1
    return Total


def RecursiveValue(Number, ToFind):
    if Number == 0:
        return 0
    if ToFind % Number == 0:
        return Number + RecursiveValue(Number - 1, ToFind)
    else:
        return RecursiveValue(Number - 1, ToFind)


if __name__ == "__main__":
    print(IterativeCalculate(10))
    print(RecursiveValue(50, 50))
```

**运行核对**　整题 2(a)–(b) 输出 18、93，分别符合 MS p.18、21；另调用 IterativeCalculate(4) 返回 7。整题 QP p.6–8 / MS p.17–21。

**与 MS 逐点对齐**（MS 印的点与语料编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function header with parameter | `def IterativeCalculate(Number):` | `module-header` |
| 2 | Correct loop | `while Number != 0:`（从 Number 数到 1） | `count-loop`、`loop-bounds` |
| 3 | Modulus calculation | `ToFind % Number == 0` | `div-mod` |
| 4 | Return of correct value at correct place | 循环之后 `return Total` | `return-value` |
| 5 | Remainder of function correct | 初值、累加、`Number - 1` 与伪代码一一对应 | `translate-pseudocode`、`accumulator` |

**证据格怎么交**　2(a)(i) 格贴 IterativeCalculate；2(b)(i) 格贴 RecursiveValue，2(b)(ii) 贴调用，2(b)(iii) 截图显示 93（MS p.21）。2(a)(ii) 格贴主程序（2 分：调用 `IterativeCalculate(10)`、输出返回值）；2(a)(iii) 截图格只要看得到 `18`（「One mark for screenshot showing 18」⟦9618_w23_42:2(a)(iii)⟧）。

**直观**　从 10 往下一个个试：10 能整除 10 吗？能，记下 10；9 呢？不能；……一直试到 1。把能整除的都加起来。

**对应练习与阶梯**　练习目录 practice/p4/9618_w23_42_q2/（T35 生成，含 2(b) 递归版）；先过阶梯 **L01 E02**（DIV 与 MOD）、**L03 E06**（选 WHILE 还是 REPEAT）。

**下一道变式**　⟦9618_w22_41:2(c)(i)⟧　（换成 OOP 情境的规则计算：遍历手里 5 张牌，用 `GetCard()`、`GetColour()`、`GetNumber()` 按颜色加分并加上牌面数字，返回总分。注意上面“易错”里提到的 MS 范例 `range(0, 4)` 笔误。）

<!-- auto:drills P4-PR-03 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| PR-01 vs MP-02 | 有“循环到合法”的校验 → PR-01；输入只是数据来源、逐个交给某模块处理并输出返回值 → MP-02 | validate / until valid |
| PR-01 vs SR-01 | 读入后在数组里逐个比较、计数或查找占 ≥ 2 分 → SR-01（PR-01 作副题型） | search / count the number of times |
| PR-02 vs AR-04 | 处理一个字符串的字符 → PR-02；把整个数组拼成一行输出或返回 → AR-04 | 参数是字符串还是数组 |
| PR-02 vs PR-03 | 计算对象是字符（校验位、逐位处理）→ PR-02；对象是数值与规则 → PR-03 | character / position 还是 points / total |
| PR-02 / PR-03 vs OP-03 | 写成类的方法、用的是对象自己的属性 → OP-03；独立函数、通过参数拿对象 → PR | 题目说 method 还是 function |
| PR-03 vs RC-01 | 题目要求递归实现 → RC-01；迭代 → PR-03 | recursive |
| 返回 vs 输出 | returns → `return`，由主程序输出；outputs → `print` | 题干动词 |
| `/`、`//`、`%` | `/` 得小数；`//` 整除（DIV）；`%` 余数（MOD） | divide / round down / remainder |
