## DT　数据类型与数据结构：伪代码 ↔ Python 对照与模板 {#core-DT}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。伪代码按 2027–29 指南书写，Python 按阶梯推荐写法（全表见 `ladder/design.md` §5）。P2 只认伪代码；Python 列用来在阶梯里把同一逻辑跑通、测过。

### 1. 数据类型（DT-01）

| 伪代码类型 | 字面量写法 | Python | 选它的信号 | 常见失分 |
|:--|:--|:--|:--|:--|
| `INTEGER` | `100`、`-3` | `int` | 个数、下标、序号 | 编号有前导零时用了 INTEGER |
| `REAL` | `15.75`、`4.0`（小数点两边都要有数字） | `float` | 钱、平均数、`/` 的结果 | 钱写 INTEGER |
| `CHAR` | `'B'`（单引号，一个字符） | `str`（长度 1） | 一个字母、一个分隔符 | 写成 `"B"` 也常给分，但 CHAR 用单引号 |
| `STRING` | `"Mr Khan"`（双引号） | `str` | 名字、编号、带引号的日期 | 引号里的日期写 DATE |
| `BOOLEAN` | `TRUE`、`FALSE` | `bool`（`True`、`False`） | 只有两种状态 | Python 首字母大写，伪代码全大写 |
| `DATE` | `27/10/2023`（不带引号） | `datetime.date` | 日期 | 与 `"27/10/2023"`（STRING）混淆 |

表达式的结果类型：`/` → REAL；`DIV`、`MOD`、`LENGTH()`、`INT()` → INTEGER；比较、`AND`、`OR`、`NOT`、`IS_NUM()`、`EOF()` → BOOLEAN；`&`、`MID()`、`LEFT()`、`RIGHT()`、`NUM_TO_STR()` → STRING。

### 2. 声明（DT-02、DT-03）

| 内容 | 伪代码 | Python | 不对应之处 |
|:--|:--|:--|:--|
| 变量 | `DECLARE Count : INTEGER` | `count = 0` | Python 没有声明，赋值才创建 |
| 常量 | `CONSTANT MaxItems = 500` | `MAX_ITEMS = 500` | 常量用 `=`，只能是字面量 |
| 一维数组 | `DECLARE Names : ARRAY[1:30] OF STRING` | `names = [""] * 30` | Python 下标 0–29 |
| 二维数组 | `DECLARE Grid : ARRAY[1:5, 1:5] OF CHAR` | `grid = [[" "] * 5 for _ in range(5)]` | 不能写 `[[" "] * 5] * 5`（五行是同一个列表） |
| 二维元素 | `Grid[2, 3] ← 'X'` | `grid[1][2] = "X"` | 伪代码一对方括号、逗号隔开 |
| 记录类型 | `TYPE Loan` / `DECLARE OnLoan : BOOLEAN` / `ENDTYPE` | `class Loan:` + `__init__` 里给字段赋初值 | 一个 DECLARE 一个字段 |
| 记录变量与字段 | `DECLARE ThisLoan : Loan`；`ThisLoan.OnLoan ← TRUE` | `this_loan = Loan()`；`this_loan.on_loan = True` | |
| 记录数组 | `DECLARE Loans : ARRAY[1:7000] OF Loan`；`Loans[Index].OnLoan` | `loans = [Loan() for _ in range(7000)]`；`loans[index].on_loan` | 不能写 `[Loan()] * 7000` |
| 整个记录 / 数组赋值 | `Pupil2 ← Pupil1`（复制） | `copy.copy(pupil1)` | Python 的 `=` 只是起别名 |

数组一律用**带上下界的全局声明**（决策 D24）：模块里直接用全局数组，不重新声明，也不把无界数组当参数。

### 3. 数组遍历模板（DT-05 至 DT-07）

**一维：看完全部元素**

```pseudocode
Total ← 0
FOR Index ← 1 TO 100
   Total ← Total + Data[Index]
NEXT Index
```

```python
total = 0
for index in range(100):
    total = total + data[index]
```

**一维：找到就停**（标志变量；循环条件不读数组，不需要短路，决策 D25）

```pseudocode
FoundAt ← -1
Index ← 1
WHILE FoundAt = -1 AND Index <= 500
   IF ErrCode[Index] = ErrNum THEN
      FoundAt ← Index
   ENDIF
   Index ← Index + 1
ENDWHILE
```

```python
found_at = -1
index = 0
while found_at == -1 and index < 500:
    if err_code[index] == err_num:
        found_at = index
    index = index + 1
```

**二维：两列表按行扫描 / 全表嵌套**

```pseudocode
FOR Row ← 1 TO 1000
   IF Loyalty[Row, 2] >= 11 THEN
      OUTPUT Loyalty[Row, 1]
   ENDIF
NEXT Row

FOR Row ← 1 TO 6
   FOR Col ← 1 TO 128
      Total ← Total + Sample[Row, Col]
   NEXT Col
NEXT Row
```

```python
for row in range(1000):
    if loyalty[row][1] >= 11:
        print(loyalty[row][0])

for row in range(6):
    for col in range(128):
        total = total + sample[row][col]
```

**记录数组**

```pseudocode
FOR Index ← 1 TO 7000
   IF Loan[Index].StudentID = ThisID AND Loan[Index].OnLoan = TRUE THEN
      Count ← Count + 1
   ENDIF
NEXT Index
```

```python
for record in loan:
    if record.student_id == this_id and record.on_loan:
        count = count + 1
```

### 4. 冒泡排序（DT-08）

| 部件 | 伪代码 | Python |
|:--|:--|:--|
| 外层后测循环 | `REPEAT` … `UNTIL NoSwaps = TRUE` | `while True:` … `if no_swaps: break` |
| 每趟重置标志 | `NoSwaps ← TRUE` | `no_swaps = True` |
| 内层范围 | `FOR J ← 1 TO Boundary`（Boundary 初值 n − 1） | `for j in range(boundary):`（0 起） |
| 比较相邻 | `IF A[J] > A[J + 1] THEN` | `if a[j] > a[j + 1]:` |
| 交换 | `Temp ← A[J]`、`A[J] ← A[J + 1]`、`A[J + 1] ← Temp` | `a[j], a[j + 1] = a[j + 1], a[j]`（伪代码不能这样写） |
| 有交换 | `NoSwaps ← FALSE` | `no_swaps = False` |
| 缩小范围 | `Boundary ← Boundary - 1` | `boundary = boundary - 1` |
| 降序 | 比较改成 `<` | 比较改成 `<` |

### 5. 文本文件（DT-09 至 DT-11）

| 操作 | 伪代码 | Python | 不对应之处 |
|:--|:--|:--|:--|
| 打开读 | `OPENFILE FileName FOR READ` | `file = open(file_name, "r")` 或 `with open(file_name) as file:` | 伪代码打开后仍用**文件名**指代文件 |
| 打开写（新建 / 覆盖） | `OPENFILE "New.txt" FOR WRITE` | `open("New.txt", "w")` | 原内容全部丢失 |
| 打开追加 | `OPENFILE "Log.txt" FOR APPEND` | `open("Log.txt", "a")` | 写在原内容之后 |
| 读一行 | `READFILE FileName, Line` | `line = file.readline().rstrip("\n")` | READFILE 读出的行不含换行符 |
| 文件尾 | `EOF(FileName)` | 无直接对应；用 `for line in file:` | EOF 只能用于以 READ 打开的文件 |
| 写一行 | `WRITEFILE "New.txt", Line` | `file.write(line + "\n")` | `write` 不自动换行 |
| 关闭 | `CLOSEFILE FileName` | `file.close()`，或 `with` 自动关闭 | 伪代码必须写 CLOSEFILE |
| 数字写入前 | `NUM_TO_STR(Total)` | `str(total)` | 文本文件只存字符串 |
| 拼一行多项 | `ID & "^" & Name` | `id + "^" + name` 或 `"^".join(...)` | 伪代码用 `&` |

**读到文件尾**

```pseudocode
OPENFILE FileName FOR READ
WHILE NOT EOF(FileName)
   READFILE FileName, Line
   // process Line
ENDWHILE
CLOSEFILE FileName
```

```python
with open(file_name) as file:
    for raw in file:
        line = raw.rstrip("\n")
        # process line
```

**复制 / 过滤到另一个文件**

```pseudocode
OPENFILE InFile FOR READ
OPENFILE OutFile FOR WRITE           // APPEND if the output file already exists
WHILE NOT EOF(InFile)
   READFILE InFile, Line
   IF Line <> "" THEN
      WRITEFILE OutFile, Line
   ENDIF
ENDWHILE
CLOSEFILE InFile
CLOSEFILE OutFile
```

```python
with open(in_file) as source, open(out_file, "w") as target:
    for raw in source:
        line = raw.rstrip("\n")
        if line != "":
            target.write(line + "\n")
```

**滚动缓存：只保留最后三行**（⟦9618_s22_22:4(a)⟧ 的考点；技能标签见 D27 提议）

```pseudocode
LineX ← ""
LineY ← ""
LineZ ← ""
WHILE NOT EOF(ThisFile)
   READFILE ThisFile, NewLine
   LineX ← LineY                    // oldest is discarded first
   LineY ← LineZ
   LineZ ← NewLine                  // newest goes last
ENDWHILE
```

```python
line_x = line_y = line_z = ""
for raw in file:
    line_x, line_y, line_z = line_y, line_z, raw.rstrip("\n")
```

### 6. 栈、队列、链表的数组实现（DT-13 至 DT-16）

| 操作 | 伪代码（1 起数组） | Python（0 起列表 + `global`） | 注意 |
|:--|:--|:--|:--|
| 栈：指针指最后一个值 | 空栈 `TopOfStack ← 0`；入栈先加 1 再存 | 空栈 `top = -1` | 题目约定优先 |
| 栈：指针指下一个空位 | 空栈 `SP ← 1`；入栈先存再加 1 | 空栈 `sp = 0` | ⟦9618_w24_22:3(b)⟧ 是这种 |
| 栈满 / 栈空 | `IF TopOfStack = MaxSize THEN` / `IF TopOfStack = 0 THEN` | `if top == max_size - 1:` / `if top == -1:` | 先检查再操作 |
| 出栈 | `Item ← Stack[TopOfStack]`、`TopOfStack ← TopOfStack - 1` | `item = stack[top]`、`top = top - 1` | 不必清除旧值 |
| 循环队列入队 | `Rear ← Rear + 1`；超过 Size 时 `Rear ← 1`；`Queue[Rear] ← Item`；`NumItems ← NumItems + 1` | `rear = (rear + 1) % size` | 先检查 `NumItems = Size` |
| 循环队列出队 | `Item ← Queue[Front]`；`Front ← Front + 1`；绕回；`NumItems ← NumItems - 1` | `front = (front + 1) % size` | 先检查 `NumItems = 0` |
| 链表结点 | 两个数组 `Data[i]`、`Pointer[i]`，或记录数组 `List[i].Data`、`List[i].Pointer` | 两个列表或对象列表 | 空指针按题目：0 或 −1 |
| 链表遍历 | `Current ← StartPointer`；`WHILE Current <> 0` … `Current ← List[Current].Pointer` | `while current != -1:` | Python 里 `lst[-1]` 不报错，先判空指针 |

**链表遍历**（按链表顺序输出所有数据，⟦9618_w24_23:3(c)⟧ 的四步）

```pseudocode
Current ← HeadPointer
WHILE Current <> 0                   // 0 is the null pointer in this design
   OUTPUT List[Current].Data
   Current ← List[Current].Pointer
ENDWHILE
```

```python
current = head_pointer
while current != -1:                 # -1 is the null pointer for a 0-based list
    print(lst[current].data)
    current = lst[current].pointer
```

### 7. 术语（三层）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Array | 「allows the storage of many values using a single identifier」⟦9618_w23_23:2(b)⟧ | 用一个标识符存放多个同类型的值，用下标访问 | 一排编了号的柜子 | P2-DT-03、P2-DT-04 |
| Index / subscript | 「It identifies / references an individual array element」⟦9618_w22_21:1(b)(ii)⟧ | 指明数组中某一个元素位置的值（整数） | 柜子的号码 | P2-DT-03 |
| Lower / upper bound | 「Lower bound, upper bound」⟦9618_w21_22:1(b)⟧ | 下标能取的最小值与最大值 | 第一个与最后一个柜子的号 | P2-DT-03 |
| Same-type rule | 「An array can only store data of the same type」⟦9618_s25_22:7(c)(i)⟧ | 一个数组的所有元素类型相同 | 一排柜子只能放同一种东西 | P2-DT-03、P2-DT-04 |
| Record | 「A set of data / all data related to one customer」⟦9618_s23_21:3(a)(i)⟧ | 把同一对象的多项（可不同类型的）数据组合在一个标识符下的用户自定义类型 | 一张表格 | P2-DT-02、P2-DT-04 |
| Array of records | 「A (1D) array of records」⟦9618_s23_21:3(a)(ii)⟧ | 元素是记录的数组，存许多对象的多项数据 | 文件柜，每个抽屉一张表 | P2-DT-04、P2-DT-07 |
| Unused element | 「Use of any 'impossible' field value」⟦9618_s22_23:5(b)(ii)⟧ | 用一个不可能出现的值（空串、999、负数）标记未用元素 | 空柜子贴“空”字 | P2-DT-03 |
| Text file (benefit) | 「The data is stored permanently / non-volatile」⟦9618_w25_21:4(b)(i)⟧ | 存在外存上的字符序列，程序结束后仍在 | 写在本子上，不是记在脑子里 | P2-DT-11 |
| APPEND mode | 「Append」⟦9618_s23_21:8(d)⟧（加数据到已有文件时的模式） | 在文件已有内容之后写入 | 在本子最后一页接着写 | P2-DT-10、P2-DT-11 |
| Separator | 「character doesn't occur in data to be recorded」⟦9618_w21_21:5(a)⟧ | 一行里分开各项数据的字符，必须不出现在数据里 | 两件货物之间的隔板 | P2-DT-11 |
| Abstract data type (ADT) | A collection of data together with the operations that can be performed on it, independent of how it is implemented.（非 MS 原句） | 一组数据及可对它进行的操作，与具体实现无关 | 只说“能做什么”，不说“怎么做” | P2-DT-12 |
| Stack | 「The stack operates as a FILO device」⟦9618_w23_22:8(c)(i)⟧ | 后进先出；只在栈顶 PUSH、POP；一个栈顶指针 | 一摞盘子 | P2-DT-12、P2-DT-13 |
| Queue | 「First value added to queue is the first value removed」⟦9618_s25_23:2(c)⟧ | 先进先出；队尾加入、队首取出；两个指针 | 食堂排队 | P2-DT-12、P2-DT-14 |
| Circular queue | 「May behave as a circular queue」⟦9618_s25_23:2(c)⟧ | 指针越过数组末尾时绕回开头，位置可以重复使用 | 圆桌座位 | P2-DT-14、P2-DT-16 |
| Linked list node | 「Each node contains data and a pointer to the next node」⟦9618_w22_22:3(a)⟧ | 每个结点存数据和下一个结点的位置 | 寻宝纸条 | P2-DT-12、P2-DT-15 |
| Start pointer | 「Start pointer」⟦9618_s21_22:3(b)⟧ | 指向链表第一个结点的变量 | 第一张纸条在哪 | P2-DT-15 |
| Null pointer | 「There are no further nodes in the list」⟦9618_s21_22:3(c)⟧ | 表示“后面没有结点”的特殊指针值（0 或 −1，不是合法下标） | 纸条上写“到此为止” | P2-DT-15、P2-DT-16 |
| Choice of null value | 「0 is not a valid array / List index value」⟦9618_w24_23:3(a)(i)⟧ | 空指针要选一个不可能是下标的值 | 不存在的门牌号 | P2-DT-16 |
| Free list | 「Unused nodes are stored on a free list」⟦9618_w22_22:3(a)⟧ | 未用结点串成的另一条链，插入时从这里取结点 | 空白纸条堆 | P2-DT-15、P2-DT-16 |
| Efficient bubble sort | 「The inner loop iterates one less time (in algorithm B) each time the outer / repeat loop iterates」⟦9618_s26_22:5(b)(i)⟧ | 每趟缩小内层范围；某趟没有交换就停 | 已排好的不再看 | P2-DT-08 |

### 8. 常见失分（DT 章）

| 失分 | 正确做法 | 题型 |
|:--|:--|:--|
| 钱、平均数写 INTEGER；带引号的日期写 DATE | 有小数 → REAL；引号 → STRING | P2-DT-01 |
| `TYPE … END`、字段不写 DECLARE | `TYPE 名` / 每字段 `DECLARE 名 : 类型` / `ENDTYPE` | P2-DT-02 |
| `ARRAY[1..30]`、`ARRAY[1:100][1:2]` | `ARRAY[1:30]`、`ARRAY[1:100, 1:2]` | P2-DT-03 |
| 在模块里重新声明全局数组 | 直接使用全局数组 | P2-DT-05 至 P2-DT-08 |
| 返回 / 输出写在循环里 | 循环后判断，两种情况都返回 | P2-DT-05、P2-DT-07 |
| `WHILE Index <= n AND A[Index] <> X` 靠短路防越界 | 标志变量或分层判断（D25） | P2-DT-05、P2-DT-06 |
| `Arr[Index][2]`、`Loan.StudentID[Index]` | `Arr[Index, 2]`、`Loan[Index].StudentID` | P2-DT-06、P2-DT-07 |
| 交换没有临时变量；并行数组只换一个 | 三句交换；两个数组 / 两列都换 | P2-DT-08 |
| `FOR Line IN File`、`READFILE Line`（漏文件名） | `WHILE NOT EOF(F)` + `READFILE F, Line` | P2-DT-09 |
| 忘了 CLOSEFILE，或写在 RETURN 之后 | 循环后、返回前关闭 | P2-DT-09、P2-DT-10 |
| 已存在的文件用 WRITE 打开 | APPEND | P2-DT-10、P2-DT-11 |
| WRITEFILE 直接写数字 / 布尔值 | 先 `NUM_TO_STR`，布尔值编码成字符 | P2-DT-10、P2-DT-11 |
| 不先检查满 / 空就入栈、出队 | 先检查，不行就返回 FALSE | P2-DT-14、P2-DT-16 |
| 栈指针约定弄反（先存还是先加） | 照题目定义：指最后一个值 → 先加后存；指下一个空位 → 先存后加 | P2-DT-16 |
| 插入结点先改前一个结点的指针 | 先把新结点连到后面，再改前一个 | P2-DT-15 |
