## AR　数组与记录 {#ch-AR}

<!-- auto:chapter-stats -->

### 核心思想

几乎每道 P4 大题的第一问都是“声明一个数组 / 记录”，最后一问常是“把数组按格式输出”。AR 章五个题型就是围着数组转的一条链：

1. **声明并存入**（AR-01 一维、AR-02 二维、AR-03 记录）：把题目给的大小、类型、初值变成一个**真实存在**的 Python list 或类。P4 的 MS 对声明给分很细：名字对、维数对、元素个数对、类型对（Python 用注释写类型）、全局还是局部对。
2. **按格式输出**（AR-04）：按下标顺序走一遍，按题目要求的样子输出——同一行空格分隔、每项一行、二维成网格、带说明文字；或者拼成一个字符串**返回**。
3. **统计与筛选**（AR-05）：走一遍数组，按条件挑出、计数、求和、求最值，存进新数组或输出。

一条贯穿全章的规则（决策 D10 ①）：**声明 = 建出来**。题目说“100 个整数的数组”，就写 `DataArray = [0] * 100  # INTEGER, 100 elements`；只写一个注释、或只写 `[]`，考官报告多次指出这样拿不到声明分。二维数组用 `[[0] * 列数 for i in range(行数)]`，不能写 `[[0] * 列数] * 行数`（所有行是同一个列表）。

另一条：**下标照题目**。题目的伪代码是 `ARRAY[0:99, 0:1]` 就是 0 起；题目让用户输入 1–30 的位置，存取时要减 1。

### 本章 Python 速查

```python
# 1D: fixed size, real list, type and size in a comment
DataArray = [0] * 100              # INTEGER, 100 elements
Names = [""] * 10                  # STRING, 10 elements

# 2D: rows x columns, every row its own list
Grid = [[-1] * 2 for i in range(100)]      # INTEGER, 100 x 2
Grid[0][0] = 123                   # pseudocode Grid[0, 0] <- 123

# record: a class with only attributes (fields)
class SaleData:
    def __init__(self):
        self.SaleID = ""           # STRING
        self.Quantity = 0          # INTEGER

Sales = [SaleData() for i in range(20)]    # array of 20 records, each a NEW object
Sales[0].Quantity = 2

# output: same line with spaces / one per line
for Index in range(len(DataArray)):
    print(DataArray[Index], end=" ")
print()                            # finish the line
```

### 题型树
<!-- auto:type-tree -->

### P4-AR-01　声明一维数组并存入数据　{#P4-AR-01}

<!-- auto:stats P4-AR-01 -->

**考法**　①声明全局一维数组（给出名字、元素个数、类型），常连同一个计数变量（`NumberItems`）；②声明后存入题目给的数据（按顺序、按要求转小写）；③数组局部于主程序，存入指定范围的随机数，要求**互不相同**；④一个数组存不下两项数据时，自己选结构（两个并行数组、二维数组、记录数组）。多是每题第一问，1–3 分；2022–25 有 5 行只给 1 分、不拆得分点。

**识别信号**　Write program code to declare the global 1D array …；with space for … integers / string elements；declare and initialise …；The array is declared and initialised local to the main program；store 20 unique random numbers between 0 and 100 (inclusive)。

**解题思路**
1. **读四件事**：名字（照抄）、元素个数、元素类型、全局还是局部于主程序。
2. **建出来**：`名字 = [初值] * 个数  # 类型, 个数 elements`。初值按类型选：整数 `0` 或题目给的 `-1`，字符串 `""`。
3. **全局**：写在文件顶层（所有函数外面）；子程序里要给它重新赋值（不是改元素）时加 `global`。**局部于主程序**：写在 `if __name__ == "__main__":` 下面（MS 范例写在顶层的主程序部分）。
4. **存入题给数据**：直接写列表字面量，或逐个赋值；顺序、大小写照题目。
5. **随机数**：`import random`，`random.randint(a, b)` 两端都包含。要求“不重复”时，每生成一个先在已存的部分里查一遍，重复就再生成——用条件循环，存进去才让计数加 1。

**Python 模板**

```python
import random

# global array + counter
DataStored = [0] * 20          # INTEGER, 20 elements
NumberItems = 0                # INTEGER

# global array initialised with given data, in the given order
Animals = ["horse", "lion", "rabbit", "mouse", "bird",
           "deer", "whale", "elephant", "kangaroo", "tiger"]   # STRING, 10 elements

if __name__ == "__main__":
    # local to the main program: 20 unique random integers 0..100 inclusive
    TheArray = [0] * 20        # INTEGER, 20 elements
    Count = 0
    while Count < 20:
        Generated = random.randint(0, 100)
        Unique = True
        for Index in range(Count):         # check only the filled part
            if TheArray[Index] == Generated:
                Unique = False
        if Unique:
            TheArray[Count] = Generated
            Count = Count + 1
    print(TheArray)
```

伪代码对照：

| 伪代码 | Python |
|:--|:--|
| `DECLARE DataArray : ARRAY[0:99] OF INTEGER` | `DataArray = [0] * 100  # INTEGER, 100 elements` |
| `DECLARE Animals : ARRAY[0:9] OF STRING` | `Animals = [""] * 10  # STRING, 10 elements` |
| `DECLARE NumberItems : INTEGER` | `NumberItems = 0  # INTEGER` |
| `INT(RAND(101))`（0–100 的整数） | `random.randint(0, 100)` |

**得分表述**（引自对应 MS）
- 「(global) 1D (Integer) array DataArray」⟦9618_w22_41:1(a)⟧
- 「Global array named Animals」⟦9618_s23_42:1(a)⟧
- 「10 string elements」⟦9618_s23_42:1(a)⟧
- 「with 20 generated random integers between 0 and 100 (inclusive)」⟦9618_w25_42:2(a)⟧
- 「all 20 random integers are unique」⟦9618_w25_42:2(a)⟧
- 「in the correct order and all in lower case」⟦9618_s23_42:1(b)⟧

**得分点地图**（口径：核验语料 2022–2026s、主题型为本型、已拆得分点的行，去掉 `equivalent_of` 行；同一行同一标签计一次；s26 行计入。共 7 行：⟦9618_s22_41:1(a)⟧、⟦9618_s23_42:1(a)⟧、⟦9618_s23_42:1(b)⟧、⟦9618_w22_41:1(a)⟧、⟦9618_w25_42:2(a)⟧ 与 s26 两行；另有 5 行 1 分题不拆）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 建出数组、名字对（array named …） | 5 | `declare-array` |
| 元素个数与类型（10 string elements / 100 elements） | 4 | `data-types` |
| 全局（global） | 3 | `global-scope` |
| 名字照抄题目 | 2 | `p4-identifiers` |
| 存入数据：按顺序、全部存入 | 2 | `initialise-variables`、`array-index` |
| 随机数；不重复 | 1 | `random-numbers`、`linear-search` |

“建出来 + 个数与类型”几乎每行都有；这两分只靠一行代码，最不该丢。

**易错与失分**
- 只写注释、没建出数组；或初值类型不对（字符串数组用整数或空值初始化）。考官报告点名了这两种（⟦9618_s23_42:1(a)⟧）。
- 用 Python list 时没体现元素个数：考官报告要求通过初始化 100 个值或注释写明来体现“100 个元素”的限制（⟦9618_w22_41:1(a)⟧）。
- 两项数据（名字和分数）建了结构却没写清类型和元素个数（⟦9618_s22_41:1(a)⟧ 的考官报告）。
- 随机数不唯一：发现重复后再生成一个，却不再检查新数是否又重复；或者把数手工写死、让用户输入。考官报告把“漏掉唯一性”列为常见错误（⟦9618_w25_42:2(a)⟧）。
- MS 的 Python 范例不能照抄成“声明”：⟦9618_s23_42:1(a)⟧ 的范例只写了 `global Animals #array 10 elements string`（MS p.4），没有建出数组——同一份考官报告恰恰说只写注释的答案较弱。按 D10 ① 建出真实的 list。

#### 代表题精讲　⟦9618_w25_42:2(a)⟧

**在考什么**　程序在一个**局部于主程序**的一维数组里存 20 个互不相同的随机整数，范围 0–100（含两端）。Write program code to declare the array local to the main program and store 20 unique random numbers … in the array. 3 分，MS 列 3 点，1 mark each。讲解时对照原卷 QP p.6（2(a)–2(c) 在这一页），MS p.18–19（Python 范例在 p.19）。

**完整作答**（整道大题的最终 Python；证据格按小问截取代码，早期测试截图在后续修改前另存）

```python
# Question2_N25: 2(a)-(f)
import random


def PrintArray(DataArray):
    for Index in range(len(DataArray)):
        print(DataArray[Index], end=" ")
    print()


def BubbleSort(DataArray):
    Swap = True
    while Swap:
        Swap = False
        for Index in range(len(DataArray) - 1):
            if DataArray[Index] > DataArray[Index + 1]:
                Temp = DataArray[Index]
                DataArray[Index] = DataArray[Index + 1]
                DataArray[Index + 1] = Temp
                Swap = True
    return DataArray


def RecursiveBinarySearch(DataArray, Lower, Upper, DataToFind):
    if Lower > Upper:
        return -1
    Middle = (Lower + Upper) // 2
    if DataArray[Middle] == DataToFind:
        return Middle
    elif DataArray[Middle] > DataToFind:
        return RecursiveBinarySearch(DataArray, Lower, Middle - 1, DataToFind)
    else:
        return RecursiveBinarySearch(DataArray, Middle + 1, Upper, DataToFind)


if __name__ == "__main__":
    TheArray = [0] * 20  # INTEGER, 20 elements, local to main
    Count = 0
    while Count < 20:
        Generated = random.randint(0, 100)
        Unique = True
        for Index in range(Count):
            if TheArray[Index] == Generated:
                Unique = False
        if Unique:
            TheArray[Count] = Generated
            Count = Count + 1
    PrintArray(TheArray)
    SortedArray = BubbleSort(TheArray)
    print("Sorted")
    PrintArray(SortedArray)
    DataToFind = int(input("Enter the number to find: "))
    Location = RecursiveBinarySearch(SortedArray, 0, len(SortedArray) - 1, DataToFind)
    if Location == -1:
        print("Not found")
    else:
        print("Found at position", Location)
```

**运行核对**　整题 2(a)–(f) 先打印 20 个不同的随机整数，再输出 Sorted 和同批数升序，并接受一个查找值。可复现验证中最小值、最大值、缺失值分别得到位置 0、19、Not found（见 SR-03）。整题 QP p.6–8 / MS p.18–26。

**与 MS 逐点对齐**

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Creation of 1D array … | `TheArray = [0] * 20` | `declare-array` |
| 2 | … with 20 generated random integers between 0 and 100 (inclusive) … | `random.randint(0, 100)`，存满 20 个 | `random-numbers` |
| 3 | … all 20 random integers are unique | 存之前在已存部分线性查找，重复就重新生成 | `random-numbers`、`linear-search` |

MS 的 Python 范例（p.19）只有一句 `TheArray = random.sample(range(0,101),20)`：`random.sample` 本身保证不重复，MS 接受。本手册教的是自己检查的写法：考试时可能不记得 `sample`，而“生成 → 查重 → 存入才计数”这套逻辑在别的题（不能重复选的卡、不能重复的输入）里还会用到。

**证据格怎么交**　2(a) 格贴主程序里声明并填数组的这一段（`import random` 一起贴上）。2(a) 本身没有截图格；它的数据在 2(d)(ii) 的截图里检验：「Output shows unsorted array of 20 integers between 0 and 100 inclusive before sorting」⟦9618_w25_42:2(d)(ii)⟧，接着是 `Sorted` 和排好序的同一批数。

**直观**　抽奖箱里有 0–100 号球，抽一个看看名单上有没有：有就放回去重抽，没有才登记。登记满 20 个为止。

**对应练习与阶梯**　练习目录 practice/p4/9618_w25_42_q2/（含 2(b) 输出、2(c) 冒泡排序、2(e) 递归二分查找）；先过阶梯 **L06 E02**（线性查找）、**L06 E01**（数组初始化干跑）。

**下一道变式**　⟦9618_s22_41:1(a)⟧　（换成“两项数据”：11 个玩家的名字和分数，自己选两个并行数组、二维数组或记录数组，并写清元素个数与类型。）

<!-- auto:drills P4-AR-01 -->

### P4-AR-02　二维数组　{#P4-AR-02}

<!-- auto:stats P4-AR-02 -->

**考法**　①声明全局或局部二维数组（行 × 列、元素类型），常连同计数变量；②用嵌套循环给每个元素赋初值（–1、空串、随机数）；③按行列存取：把两个参数存进“下一个空行”的两列，满了就输出提示。数据本身是表：作业号与优先级、玩家 ID / 关卡 / 分数。2–5 分。

**识别信号**　2D array of 10 by 10 integer elements；The program stores the jobs in a global 2D array；`DECLARE Jobs : ARRAY[0:99, 0:1] OF INTEGER`；The first dimension of the array has seven elements … The second dimension … has three elements；stores –1 in each of the array elements。

**解题思路**
1. **认维数**：伪代码 `ARRAY[0:99, 0:1]` = 100 行 × 2 列；文字“first dimension has seven elements, second dimension three” = 7 行 × 3 列。
2. **建出来**：`名字 = [[初值] * 列数 for i in range(行数)]`，注释写类型与 `行 x 列`。
3. **访问**：伪代码 `Jobs[R, C]` → Python `Jobs[R][C]`。
4. **初始化**：两层 `for`，外层行、内层列；循环次数各自等于该维的元素个数。
5. **存进下一空行**：计数变量就是下一空行的下标；先判断满（计数 = 行数）再存，存完计数加 1。

**Python 模板**

```python
ROWS = 100
Jobs = [[-1] * 2 for x in range(ROWS)]   # global INTEGER 2D array, 100 x 2
NumberOfJobs = 0                          # global INTEGER


def Initialise():
    global NumberOfJobs
    for Row in range(ROWS):               # first dimension
        for Col in range(2):              # second dimension
            Jobs[Row][Col] = -1
    NumberOfJobs = 0


def AddJob(JobNumber, Priority):
    global NumberOfJobs
    if NumberOfJobs == ROWS:              # full: no free row
        print("Not added")
    else:
        Jobs[NumberOfJobs][0] = JobNumber # next free row
        Jobs[NumberOfJobs][1] = Priority
        NumberOfJobs = NumberOfJobs + 1
        print("Added")
```

伪代码对照：

| 伪代码 | Python | 坑 |
|:--|:--|:--|
| `DECLARE Jobs : ARRAY[0:99, 0:1] OF INTEGER` | `Jobs = [[0] * 2 for x in range(100)]` | 不能写 `[[0] * 2] * 100` |
| `Jobs[R, C] ← -1` | `Jobs[R][C] = -1` | 两对方括号 |
| `FOR R ← 0 TO 99` / `FOR C ← 0 TO 1` | `for R in range(100):` / `for C in range(2):` | 终点 + 1 |
| `DECLARE HighScores : ARRAY[0:6, 0:2] OF STRING` | `HighScores = [[""] * 3 for y in range(7)]` | 7 行 3 列，不是 3 行 7 列 |

**得分表述**（引自对应 MS）
- 「(global) 2-D array Jobs with correct identifier (and Integer data type)」⟦9618_w22_42:1(a)⟧
- 「with 100 elements by 2 elements」⟦9618_w22_42:1(a)⟧
- 「looping through both array element dimensions」⟦9618_w22_42:1(b)⟧
- 「Storing parameters job number and priority to only the next available array position」⟦9618_w22_42:1(c)⟧
- 「all elements initialised to empty string ("")」⟦9618_w24_42:3(a)⟧
- 「that is random between 1 and 100 (allow inclusive or exclusive)」⟦9618_s22_42:2(a)⟧

**得分点地图**（口径同 AR-01。共 5 行：⟦9618_s22_42:2(a)⟧、⟦9618_w22_42:1(a)⟧、⟦9618_w22_42:1(b)⟧、⟦9618_w22_42:1(c)⟧、⟦9618_w24_42:3(a)⟧）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 二维数组，行 × 列个数对 | 5 | `array-2d` |
| 建出数组、名字对 | 3 | `declare-array` |
| 元素类型对 | 3 | `data-types` |
| 嵌套循环走遍两维 | 3 | `nested-loops` |
| 每个元素赋初值 | 3 | `initialise-variables` |
| 模块头 | 2 | `module-header` |

“二维、个数对”5 行全有。声明与嵌套初始化合起来占本型大部分分数。

**易错与失分**
- 建成一维数组，或行列个数不对（如 2 × 10、3 个元素各含 7 格）。考官报告多次指出（⟦9618_s22_42:2(a)⟧、⟦9618_w24_42:3(a)⟧）。
- 只写注释表达“要建一个数组”，没真正建出、也没初始化（⟦9618_w24_42:3(a)⟧ 的考官报告）。
- 初始化的元素个数差一：一维只走了 19 个而不是 20 个（⟦9618_w22_42:1(b)⟧ 的考官报告）。
- 判断满的条件写错：`NumberOfJobs == 99` 或 `> 100`；把参数改成在过程里 `input()`（⟦9618_w22_42:1(c)⟧ 的考官报告）。
- `[[0] * 2] * 100`：100 行其实是同一个列表，改一行全都变。

#### 代表题精讲　⟦9618_w22_42:1(c)⟧

**在考什么**　作业按优先级存放。题目给出伪代码声明 `DECLARE Jobs : ARRAY[0:99, 0:1] OF INTEGER`：`Jobs[0, 0]` 存第一个作业的编号，`Jobs[0, 1]` 存它的优先级；全局变量 `NumberOfJobs` 是当前作业数。1(a) 声明，1(b) `Initialise()` 全部置 –1、计数置 0。1(c) 写过程 `AddJob()`：接收作业号和优先级两个参数，存进下一个空元素；成功输出 `Added`，失败输出 `Not added`。5 分，MS 列 6 点（Max 5）。讲解时对照原卷 QP p.2（情境、伪代码声明、1(a)、1(b)）与 p.3（1(c)、1(d) 测试数据表），MS p.5（1(c)，Python 范例在同页）。

**完整作答**（整道大题的最终 Python；证据格按小问截取代码，早期测试截图在后续修改前另存）

```python
# Question1_N22: 1(a)-(g)
Jobs = [[0] * 2 for Row in range(100)]  # global INTEGER, 100 x 2
NumberOfJobs = 0  # global INTEGER


def Initialise():
    global NumberOfJobs
    for Row in range(100):
        for Col in range(2):
            Jobs[Row][Col] = -1
    NumberOfJobs = 0


def AddJob(JobNumber, Priority):
    global NumberOfJobs
    if NumberOfJobs == 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs][0] = JobNumber
        Jobs[NumberOfJobs][1] = Priority
        NumberOfJobs = NumberOfJobs + 1
        print("Added")


def InsertionSort():
    for I in range(1, NumberOfJobs):
        CurrentJob = Jobs[I][0]
        CurrentPriority = Jobs[I][1]
        J = I - 1
        Moving = True
        while J >= 0 and Moving:
            if Jobs[J][1] > CurrentPriority:
                Jobs[J + 1][0] = Jobs[J][0]
                Jobs[J + 1][1] = Jobs[J][1]
                J = J - 1
            else:
                Moving = False
        Jobs[J + 1][0] = CurrentJob
        Jobs[J + 1][1] = CurrentPriority


def PrintArray():
    for X in range(NumberOfJobs):
        print(Jobs[X][0], "priority", Jobs[X][1])


if __name__ == "__main__":
    Initialise()
    AddJob(12, 10)
    AddJob(526, 9)
    AddJob(33, 8)
    AddJob(12, 9)
    AddJob(78, 1)
    InsertionSort()
    PrintArray()
```

**运行核对**　整题 1(a)–(g) 按 QP 的 5 组数据运行：5 次 Added，随后 78 priority 1、33 priority 8、526 priority 9、12 priority 9、12 priority 10，与 MS p.10 一致。满数组另测第 101 次不写入。整题 QP p.2–4 / MS p.3–10。

**与 MS 逐点对齐**（MS 印 6 点，Max 5；与语料编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function header (and end where appropriate) with two (integer) parameters | `def AddJob(JobNumber, Priority):` | `module-header` |
| 2 | Checks if array is full … | `if NumberOfJobs == 100:` | `relational-ops` |
| 3 | … if full outputs "Not added" | `print("Not added")` | `output-format` |
| 4 | Storing parameters job number and priority to only the next available array position | `Jobs[NumberOfJobs][0]`、`[1]` | `array-2d`、`array-index` |
| 5 | Incrementing NumberOfJobs | `NumberOfJobs = NumberOfJobs + 1` | `accumulator` |
| 6 | Outputting "Added" if successful | `print("Added")` | `output-format` |

题目叫它 procedure，MS 第 1 点写的是 “Function header”——Python 里都是 `def`，不影响。1(a) 的 MS Python 范例只有注释 `Jobs # global integer, 100 by 2 elements`（MS p.3），1(b) 的范例再用 `Jobs.append([-1,-1])` 填 100 行；本手册按 D10 ①在 1(a) 就建出 100 × 2 的数组，1(b) 用嵌套循环置 –1（对应 1(b) 的得分点 “looping through both array element dimensions”）。

**证据格怎么交**　1(a) 格贴两行声明，1(b) 格贴 `Initialise()`，1(c) 格贴 `AddJob()`，1(d) 格贴主程序（2 分：先调 `Initialise()`，再按表中顺序调 5 次 `AddJob()`）。

**直观**　Jobs 是一张 100 行 2 列的登记表，`NumberOfJobs` 是“下一行写在哪”的书签：写一行、书签往下挪一行；书签到了第 100 行就说“登记表满了”。

**对应练习与阶梯**　练习目录 practice/p4/9618_w22_42_q1/（含 1(e) 插入排序、1(f) 输出）；先过阶梯 **L06 E04**（二维数组的行、列）、**L06 E01**。

**下一道变式**　⟦9618_s22_42:2(a)⟧　（换成“局部于主程序的 10 × 10 数组 + 嵌套循环存随机数”：4 分，MS 允许随机数范围含不含 1、100 两端。）

<!-- auto:drills P4-AR-02 -->

### P4-AR-03　记录结构　{#P4-AR-03}

<!-- auto:stats P4-AR-03 -->

**考法**　按题目给的字段说明或伪代码 `TYPE … ENDTYPE` 声明记录。Python 没有记录，用**只有属性的类**：在 `__init__` 里给每个字段赋初值，注释写类型。变化：①两个字段（ID 字符串、数量整数）；②三个整数字段（照伪代码 `TYPE NewRecord` 翻译）；③字段里有一个数组（队列记录：100 个整数的数组 + 两个指针）；④接着声明“记录数组”与计数变量。每行 2–3 分。

**识别信号**　Write program code to declare the record type …；declare a record structure, SaleData；If your programming language does not support record structures, a class can be declared instead；If you are writing in Python, use comments to declare the appropriate data types；An empty record has the integer –1 stored in each field；`TYPE … ENDTYPE`。

**解题思路**
1. **类名照抄记录名**：`class SaleData:`。
2. **每个字段一个属性**，写在 `__init__` 里：`self.SaleID = ""  # STRING`。考法①②的 MS 也接受“构造方法带参数、把参数赋给字段”的写法（⟦9618_s23_42:2(a)⟧ 的 MS 写明 if a class then a constructor assigning attributes …）。
3. **字段是数组**：在 `__init__` 里建出来：`self.QueueArray = [0] * 100  # INTEGER, 100 elements`。
4. **字段名照抄**题目（大小写也照抄）。题目没要求私有时用公有属性 `self.字段`，主程序可以直接 `记录.字段` 赋值。
5. **记录数组**：`Records = [RecordData() for i in range(50)]`，每个元素是新对象；不能写 `[RecordData()] * 50`。

**Python 模板**

```python
class SaleData:                   # TYPE SaleData
    def __init__(self):
        self.SaleID = ""          # STRING   (DECLARE SaleID : STRING)
        self.Quantity = 0         # INTEGER  (DECLARE Quantity : INTEGER)


class RecordData:                 # constructor with parameters is also accepted
    def __init__(self, IDP, TotalP):
        self.ID = IDP             # STRING
        self.Total = TotalP       # INTEGER


Records = [RecordData("", 0) for i in range(50)]   # global array of 50 records
NumberRecords = 0                                   # global INTEGER

ThisSale = SaleData()             # one record variable
ThisSale.SaleID = "ABC"
ThisSale.Quantity = 2
```

伪代码对照：

| 伪代码 | Python |
|:--|:--|
| `TYPE NewRecord` … `ENDTYPE` | `class NewRecord:` + `def __init__(self):` |
| `DECLARE Key : INTEGER`（字段） | `self.Key = 0  # INTEGER` |
| `DECLARE Item : NewRecord` | `Item = NewRecord()` |
| `Item.Key ← 5` | `Item.Key = 5` |
| `DECLARE HashTable : ARRAY[0:199] OF NewRecord` | `HashTable = [NewRecord() for i in range(200)]` |

**得分表述**（引自对应 MS）
- 「Record declaration named SaleData // class declaration (and end) named SaleData」⟦9618_s23_42:2(a)⟧
- 「Record/class NewRecord declared」⟦9618_s25_42:2(a)⟧
- 「3 variables within structure (all integer)」⟦9618_s25_42:2(a)⟧
- 「ID as a string and total as an Integer」⟦9618_w23_41:2(c)(i)⟧
- 「containing a 1D array of (100) integers QueueArray」⟦9618_w24_42:2(a)⟧
- 「(global) 1D Array named Records of type RecordData」⟦9618_w23_41:2(c)(ii)⟧

**得分点地图**（口径同 AR-01。共 6 行：⟦9618_s23_42:2(a)⟧、⟦9618_s25_42:2(a)⟧、⟦9618_w23_41:2(c)(i)⟧、⟦9618_w23_41:2(c)(ii)⟧、⟦9618_w24_42:2(a)⟧ 与 s26 一行）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 记录 / 类声明，名字对 | 5 | `record-type` |
| 字段类型对（string / integer） | 5 | `data-types` |
| 用类代替记录 | 4 | `class-definition` |
| 字段是数组 / 记录数组 | 2 | `declare-array` |

几乎所有行都是“声明 + 字段类型”两分。

**易错与失分**
- 建了一维数组或单独几个变量，没有把字段放进一个结构里。考官报告指出了这一点（⟦9618_s23_42:2(a)⟧、⟦9618_w24_42:2(a)⟧）。
- 用类时没有构造方法，字段没在 `__init__` 里创建（⟦9618_w23_41:2(c)(i)⟧ 的考官报告）。
- 字段是数组时只写注释、没真正建出数组（⟦9618_w24_42:2(a)⟧ 的考官报告）。
- 记录数组的计数变量被声明成了数组；只写注释没建出数组或变量（⟦9618_w23_41:2(c)(ii)⟧ 的考官报告）。
- MS 范例有误：⟦9618_w24_42:2(a)⟧ 的 Python 范例在 `__init__` 里写 `HeadPointer = 0 #integer`，少了 `self.`（MS p.18），这只是局部变量，记录里并没有这个字段；同一题 2(b) 的范例（p.19）才写成 `self.HeadPointer`。自己写一律 `self.字段`。

#### 代表题精讲　⟦9618_w24_42:2(a)⟧

**在考什么**　用记录结构设计线性队列。记录 `Queue` 的字段：`QueueArray`（最多 100 个整数的一维数组）、`Headpointer`（第一个数据的下标）、`Tailpointer`（下一个空位的下标）。Write program code to declare the record structure Queue and its fields；语言不支持记录时可以用类；用 Python 时用注释声明类型。3 分，MS 列 3 点（“1 mark each to max”）。2(b) 接着写主程序：新建记录 `TheQueue`，头指针 –1、尾指针 0、数组每个元素 –1（3 分）。讲解时对照原卷 QP p.8（2(a)、2(b) 都在这一页），MS p.18（2(a)）、p.19（2(b)）。

**完整作答**（整道大题的最终 Python；证据格按小问截取代码，早期测试截图在后续修改前另存）

```python
# Question2_N24: 2(a)-(g)
class Queue:
    def __init__(self):
        self.QueueArray = [-1] * 100  # INTEGER, 100 elements
        self.HeadPointer = -1  # INTEGER
        self.TailPointer = 0  # INTEGER, next free position


def Enqueue(AQueue, TheData):
    if AQueue.HeadPointer == -1:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.HeadPointer = 0
        AQueue.TailPointer = AQueue.TailPointer + 1
        return 1
    else:
        if AQueue.TailPointer > 99:
            return -1
        else:
            AQueue.QueueArray[AQueue.TailPointer] = TheData
            AQueue.TailPointer = AQueue.TailPointer + 1
            return 1


def ReturnAllData(TheQueue):
    Temp = ""
    if TheQueue.HeadPointer != -1:
        for X in range(TheQueue.HeadPointer, TheQueue.TailPointer):
            Temp = Temp + str(TheQueue.QueueArray[X]) + " "
    return Temp


def Dequeue(TheQueue):
    if TheQueue.HeadPointer == -1 or TheQueue.HeadPointer == TheQueue.TailPointer:
        return -1
    Temp = TheQueue.QueueArray[TheQueue.HeadPointer]
    TheQueue.HeadPointer = TheQueue.HeadPointer + 1
    return Temp


if __name__ == "__main__":
    TheQueue = Queue()
    for X in range(10):
        DataInput = int(input("Enter an integer that is 0 or more: "))
        while DataInput < 0:
            DataInput = int(input("Invalid. Enter an integer that is 0 or more: "))
        ReturnValue = Enqueue(TheQueue, DataInput)
        if ReturnValue == -1:
            print("Queue full")
        else:
            print("Inserted")
    print(ReturnAllData(TheQueue))
    for X in range(2):
        ReturnValue = Dequeue(TheQueue)
        if ReturnValue == -1:
            print("Queue empty")
        else:
            print(ReturnValue, "is returned")
    print(ReturnAllData(TheQueue))
```

**运行核对**　整题 2(a)–(g) 输入 10、9、−1、8、7、6、5、4、3、2、1，−1 被拒，10 个有效数各入队一次；输出 10 到 1，随后出队 10、9，剩下 8 到 1。另一轮按 2(g)(ii) 不含 −1 的数据运行，同样符合 MS p.26、30。整题 QP p.8–11 / MS p.18–30。

**与 MS 逐点对齐**

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Record structure or class with constructor Queue (and end where appropriate) … | `class Queue:` 带 `__init__` | `record-type`、`class-definition` |
| 2 | … containing a 1D array of (100) integers QueueArray | `self.QueueArray = [-1] * 100` | `record-type`、`declare-array` |
| 3 | … containing HeadPointer and TailPointer as integers | 两个 `self.` 属性，注释 INTEGER | `record-type`、`data-types` |

字段名：QP p.8 印的是 `Headpointer`、`Tailpointer`（小写 p），MS 写 `HeadPointer`、`TailPointer`。本作答统一采用 MS 的 `HeadPointer`、`TailPointer`；QP 与 MS 的大小写不一致，代码中须保持同一种拼法。2(b) 的三个得分点是“新建记录”“头指针 –1、尾指针 0”“100 个元素都置 –1”，主程序三段各对一点。

**证据格怎么交**　2(a) 格贴整个 `class Queue`；2(b) 格贴 TheQueue = Queue()，其构造方法已设置全部初值。后续 Enqueue、ReturnAllData、Dequeue 分别进 2(c)、2(d)、2(f)；2(e)(ii) 与 2(g)(ii) 按各自数据截图，显示拒绝 −1、全部有效输入及出队结果。

**直观**　记录就是一张表格模板：一栏放 100 格的数组，两栏各放一个数字。`Queue()` 是照模板印出一张空表，主程序再往三栏里填初值。

**对应练习与阶梯**　练习目录 practice/p4/9618_w24_42_q2/（后续小问是入队、出队与 `ReturnAllData()`）；先过阶梯 **L08 E01**（TYPE ↔ class、记录数组）、**L08 E02**（记录数组要逐个新建）。

**下一道变式**　⟦9618_w23_41:2(c)(i)⟧　（两个字段的记录 `RecordData`：ID 字符串、Total 整数；紧接着的 2(c)(ii) 要声明 50 个 `RecordData` 的全局数组 `Records` 与计数变量。）

<!-- auto:drills P4-AR-03 -->

### P4-AR-04　按格式输出数组内容　{#P4-AR-04}

<!-- auto:stats P4-AR-04 -->

**考法**　按下标顺序走一遍数组，按题目的格式输出。几种格式：①同一行、空格分隔（`10 4 5 13 25`）；②每项一行，带固定文字（`123 priority 1`、`FYI 10 000`）；③二维数组成网格，一行一行输出；④输出栈的全部 10 个元素再输出栈指针；⑤输出二叉树每个结点的左指针、数据、右指针（按存放顺序，不沿指针）；⑥把所有元素拼成一个带空格的字符串**返回**（`FormatArray()`、`ReturnAllData()`）；⑦主程序调用一次排序 / 读文件，再输出返回的整个数组；⑧对象数组按下标逐个用 getter 输出。分值多为 2–4。

**识别信号**　outputs the contents of the array in the order they are stored；The items are printed on the same line；outputs each … on a line, for example: …；The values should be output as a 2D grid；concatenates the contents of the array into one string with a space between each array element；Write a procedure to output all … elements；in the order they are saved in the array。

**解题思路**
1. **认格式**：同一行 → `print(x, end=" ")`，循环后 `print()`；每项一行 → 循环里 `print(...)`；网格 → 外层行、内层列，每行结束 `print()`。题目给了样例就照样例的文字与顺序。
2. **走多少个**：全部元素用数组长度；只输出“有效的”用计数变量（`NumberOfJobs`）或指针（`HeadPointer` 到 `TailPointer - 1`）控制，不要把空值也输出。
3. **返回字符串**：`Text = ""`，循环里 `Text = Text + str(x) + " "`，循环后 `return Text`（题目说 returns 就不要 `print`）。
4. **对象数组**：属性私有时用 getter：`Items[i].GetName()`。
5. **写成过程**：题目让“写一个过程输出”，代码要放进 `def` 里，再在主程序调用（常要求排序前后各调一次）。

**Python 模板**

```python
def PrintArray(DataArray):                 # same line, space between
    for Index in range(len(DataArray)):
        print(DataArray[Index], end=" ")
    print()


def PrintJobs(Jobs, NumberOfJobs):         # one item per line, fixed words
    for X in range(NumberOfJobs):          # only the stored jobs
        print(Jobs[X][0], "priority", Jobs[X][1])


def PrintGrid(Grid):                       # 2D grid: rows and columns
    for Row in range(len(Grid)):
        for Col in range(len(Grid[Row])):
            print(Grid[Row][Col], end=" ")
        print()                            # new line after each row


def FormatArray(DataArray):                # return, do not print
    OutputText = ""
    for Index in range(len(DataArray)):
        OutputText = OutputText + str(DataArray[Index]) + " "
    return OutputText


if __name__ == "__main__":
    PrintArray([10, 4, 5, 13, 25])
    PrintJobs([[123, 1], [39, 3], [120, 7]], 3)
    PrintGrid([[1, 2, 3], [4, 5, 6]])
    print(FormatArray(["ant", "bee", "cat"]))
```

伪代码对照：

| 伪代码 | Python | 坑 |
|:--|:--|:--|
| `OUTPUT Jobs[X, 0], " priority ", Jobs[X, 1]` | `print(Jobs[X][0], "priority", Jobs[X][1])` | `print` 自动加空格；用 `+` 拼接时数字要 `str()` |
| 同一行输出（伪代码没有直接写法，常先拼成字符串） | `print(x, end=" ")`，循环后 `print()` | 忘了最后的 `print()`，下一次输出会接在同一行 |
| `Text ← Text & NUM_TO_STR(X) & " "` | `Text = Text + str(X) + " "` | |

**得分表述**（引自对应 MS）
- 「Outputting all 10 × 10 values with each 2nd dimension on a complete line」⟦9618_s22_42:2(b)(ii)⟧
- 「Outputting the job and priority for each element on the same line, with a line break between each job」⟦9618_w22_42:1(f)⟧
- 「outputting player name, space, score. Each player must start on a new line」⟦9618_s22_41:1(c)⟧
- 「Looping through each parameter array element, concatenating with space and returning」⟦9618_w24_41:1(b)(i)⟧
- 「Starting at HeadPointer and incrementing until TailPointer – 1」⟦9618_w24_42:2(d)⟧
- 「Calling procedure before and after bubble sort」⟦9618_s22_42:2(b)(ii)⟧

**得分点地图**（口径同 AR-01。本型 23 行中 22 行已拆（1 行 1 分不拆），含 s26 六行）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 走遍全部（或全部有效）元素 | 21 | `count-loop` |
| 按格式输出（同一行 / 换行 / 文字） | 20 | `output-format` |
| 过程 / 函数头 | 15 | `module-header` |
| 调用（排序、读文件、本过程） | 8 | `procedure-call` |
| 循环边界：只到计数 / 指针 | 5 | `loop-bounds` |
| 二维按行列 | 4 | `array-2d` |
| 调用对象方法；返回拼好的串 | 4 + 4 | `method-call`、`return-value` |
| getter；拼接字符串 | 3 + 3 | `getter-setter`、`string-concat` |

**“遍历 + 按格式输出 + 模块头”三分在 22 行里有 15–21 行出现**，是反复出现的基础技能；格式（同一行还是换行、有没有空格）需要按题目单独核对。

**易错与失分**
- 把全部数据输出在一行，没有分成网格的行；或者自作主张对齐每列（超出要求，但费时间）。考官报告指出前者是常见错误（⟦9618_s22_42:2(b)(ii)⟧）。
- 把数组里的空值也输出：应当用计数变量或检查空值控制输出哪些（⟦9618_w22_42:1(f)⟧ 的考官报告）。
- 缺空格或换行；直接把整个数组 `print(DataArray)` 输出（⟦9618_s22_41:1(c)⟧、⟦9618_w25_42:2(b)⟧ 的考官报告）。
- 函数要返回拼好的串，却在函数里直接输出；元素之间漏了空格（⟦9618_w24_41:1(b)(i)⟧ 的考官报告）。
- 队列只输出有数据的部分：从 HeadPointer 到 TailPointer – 1（⟦9618_w24_42:2(d)⟧ 的考官报告）；栈用指针判断到哪里结束，而不是看数据（⟦9618_s22_42:1(b)⟧ 的考官报告）。
- 写在主程序里而不是题目要求的过程里（⟦9618_s23_41:1(b)(i)⟧ 的考官报告）。
- MS 范例有误：⟦9618_s22_42:2(b)(ii)⟧ 的 Python 范例定义 `def Printarray`，主程序第一次却调用 `printarray(ArrayData)`（MS p.18，小写 p），照抄会 `NameError`。

#### 代表题精讲　⟦9618_s22_42:2(b)(ii)⟧

**在考什么**　2(a) 主程序声明 10 × 10 整数二维数组并全部存入 1–100 的随机数；2(b) 给出冒泡排序的伪代码（把每一行排成升序），2(b)(i) 把它加进主程序。2(b)(ii)：Write program code for a procedure to output all the values in the 2D array … as a 2D grid, with values in rows and columns. Call the procedure before and after your bubble sort code. 3 分，MS 列 3 点。讲解时对照原卷 QP p.4（2(a) 与冒泡排序伪代码）、p.5（2(b)(ii)、(iii)），MS p.17–18（Python 范例在 p.18）。

题给伪代码（QP p.4）：

```pseudocode
ArrayLength ← 10
FOR X ← 0 TO ArrayLength - 1
   FOR Y ← 0 TO ArrayLength - 2
      FOR Z ← 0 TO ArrayLength - Y - 2
         IF ArrayData[X, Z] > ArrayData[X, Z + 1] THEN
            TempValue ← ArrayData[X, Z]
            ArrayData[X, Z] ← ArrayData[X, Z + 1]
            ArrayData[X, Z + 1] ← TempValue
         ENDIF
      NEXT Z
   NEXT Y
NEXT X
```

**完整作答**（整道大题的最终 Python；证据格按小问截取代码，早期测试截图在后续修改前另存）

```python
# Question2_J22: 2(a)-(c)
import random


def PrintArray(ArrayData):
    for X in range(10):
        for Y in range(10):
            print(ArrayData[X][Y], end=" ")
        print()


def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + Upper - 1) // 2  # formula printed in the question
        if Mid < Lower:
            Mid = Lower  # prevent a negative/out-of-interval index for a singleton
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1


if __name__ == "__main__":
    ArrayData = [[0] * 10 for X in range(10)]  # INTEGER, 10 x 10, local to main
    for X in range(10):
        for Y in range(10):
            ArrayData[X][Y] = random.randint(1, 100)
    PrintArray(ArrayData)
    ArrayLength = 10
    for X in range(ArrayLength):
        for Y in range(ArrayLength - 1):
            for Z in range(ArrayLength - Y - 1):
                if ArrayData[X][Z] > ArrayData[X][Z + 1]:
                    TempValue = ArrayData[X][Z]
                    ArrayData[X][Z] = ArrayData[X][Z + 1]
                    ArrayData[X][Z + 1] = TempValue
    PrintArray(ArrayData)
    print(BinarySearch(ArrayData, 0, 9, ArrayData[0][0]))
    print(BinarySearch(ArrayData, 0, 9, 101))
```

**运行核对**　整题 2(a)–(c) 先输出 10×10 随机网格，再输出每行升序的同一网格；最后查找首行已有数返回有效下标，查 101 返回 −1，与 MS p.21、24 的截图条件一致（随机网格不要求与示例数值相同）。整题 QP p.4–6 / MS p.13–24。

补全 2(c) 时必须注意：QP p.6 / MS p.22–23 印的 Mid = (Lower + Upper − 1) DIV 2 在 Lower=Upper=0 时得 −1，可能造成错误访问或递归不前进。照 MS 填空得分；自己写时按模板处理边界。本完整程序保留原公式并在 Mid < Lower 时把 Mid 设为 Lower，确保中点在有效区间；不是静默照抄有缺陷的算法（D44）。

**与 MS 逐点对齐**

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | procedure header (and end where appropriate) | `def PrintArray(ArrayData):` | `module-header` |
| 2 | Outputting all 10 × 10 values with each 2nd dimension on a complete line | 内层 `end=" "`、内层结束 `print()` | `nested-loops`、`output-format`、`array-2d` |
| 3 | Calling procedure before and after bubble sort | 排序前后各一次 `PrintArray(ArrayData)` | `procedure-call` |

伪代码的 `FOR Y ← 0 TO ArrayLength - 2` 对应 `range(0, ArrayLength - 1)`，`FOR Z ← 0 TO ArrayLength - Y - 2` 对应 `range(0, ArrayLength - Y - 1)`：每个终点都 + 1。

**证据格怎么交**　2(b)(ii) 格贴 `PrintArray()` 和主程序里两次调用的那几行（主程序已改过，贴改过的版本）。2(b)(iii) 截图格：「output showing array unsorted and then sorted on 1 of the dimensions」⟦9618_s22_42:2(b)(iii)⟧——排序前、排序后两个 10 × 10 网格都要在截图里。

**直观**　网格就是写信：一行写 10 个字，写完一行按回车，再写下一行。`end=" "` 是“写完一个字不回车、空一格”。

**对应练习与阶梯**　练习目录 practice/p4/9618_s22_42_q2/（含 2(c) 递归二分查找）；先过阶梯 **L03 E05**（嵌套 FOR 的乘法表网格）、**L06 E04**。

**下一道变式**　⟦9618_w22_42:1(f)⟧　（每项一行、带固定文字：`123 priority 1`；只输出已存的 `NumberOfJobs` 个作业。）

<!-- auto:drills P4-AR-04 -->

### P4-AR-05　数组的统计与筛选　{#P4-AR-05}

<!-- auto:stats P4-AR-05 -->

**考法**　遍历数组（常是字符串数组、记录数组或对象数组），按条件筛选、分类、统计：①把“数字,颜色”字符串拆开，按颜色分进 6 个数组；②按用户输入的最大高度、最大宽度、是否常绿三个条件挑出合适的树（对象，用 getter），存进新数组并逐个调用输出过程，一棵也没有时输出提示；③算出用户答对的百分比并输出没答出的词；④输出非空记录的关键字段；⑤算每匹马的平均成功率并找出最高者。2–8 分。

**识别信号**　creates a new array of all the … that meet all the requirements；If there are no … that meet …, a suitable message is output；finds and outputs the longest / shortest；calculate and output the average / percentage；The integer is stored in the array that matches the colour；outputs the key field of each element … that does not contain an empty record。

**解题思路**
1. **输入只读一次**：筛选条件（用户的要求）在循环**之前**读，不要放进循环里每次都问。
2. **遍历**：`for Index in range(len(数组)):`，取出一个元素；对象用 getter，记录用 `.字段`，字符串先拆。
3. **条件**：多个条件同时满足用 `and`；“not more than” → `<=`；按类别分组用 `if / elif`。
4. **动作**：满足就存进新数组（`append` 或下一个空位）、计数、累加，或调用题目给的过程。
5. **循环后**：没有任何元素满足时输出提示（看计数或新数组长度）；平均 = 总和 / 个数；百分比 = 个数 / 总数 × 100。
6. **最值**：先设 `Max = 第一个`，再逐个比；题目要求自己找时不用 `max()`（D10 ③）。

**Python 模板**

```python
def ChooseItems(Items):                          # Items: array of objects with getters
    MaxHeight = int(input("Maximum height in cm: "))   # read the criteria ONCE
    MaxWidth = int(input("Maximum width in cm: "))
    Chosen = []                                  # new array of the matching objects
    for Index in range(len(Items)):
        Item = Items[Index]
        if Item.GetMaxHeight() <= MaxHeight and Item.GetMaxWidth() <= MaxWidth:
            Chosen.append(Item)
            print(Item.GetTreeName())
    if len(Chosen) == 0:                         # after the loop
        print("No suitable items")
    return Chosen


def Longest(Words):                              # max without max()
    LongestWord = Words[0]
    for Index in range(1, len(Words)):
        if len(Words[Index]) > len(LongestWord):
            LongestWord = Words[Index]
    return LongestWord


def Percentage(Found, Total):
    return Found / Total * 100
```

**得分表述**（引自对应 MS）
- 「Looping through each line in parameter DataArray」⟦9618_s25_41:2(b)⟧
- 「Comparing 2nd value/colour to each colour to select array」⟦9618_s25_41:2(b)⟧
- 「storing 1st value/integer in correct array」⟦9618_s25_41:2(b)⟧
- 「comparing each evergreen input with Evergreen」⟦9618_s24_41:2(e)(i)⟧
- 「Outputting suitable message if no trees appropriate」⟦9618_s24_41:2(e)(i)⟧
- 「Calculates and outputs percentage of answers found」⟦9618_s24_42:1(c)(ii)⟧

**得分点地图**（口径同 AR-01。共 9 行：⟦9618_s24_41:2(e)(i)⟧、⟦9618_s24_42:1(c)(ii)⟧、⟦9618_s25_41:2(b)⟧、⟦9618_s25_42:2(f)(i)⟧、⟦9618_w24_41:2(e)(ii)⟧ 与 s26 四行）

| 得分点（MS 常见写法） | 行数 | 技能标签 |
|:--|--:|:--|
| 遍历每个元素 | 8 | `count-loop` |
| 过程 / 函数头（参数是数组） | 6 | `module-header` |
| 输出结果或“没有符合”的提示 | 6 | `output-format` |
| 比较条件 | 5 | `relational-ops` |
| 读入筛选条件 | 4 | `input-prompt` |
| 对象数组；多条件 `and`；调用 getter；字符串拆分 | 3 | `array-of-objects`、`logic-ops`、`method-call`、`string-functions` |

**遍历每个元素**几乎每行都有；本型的分数集中在“遍历 → 比较 → 存 / 输出”这条链上，再加循环后的提示或统计。

**易错与失分**
- 把用户的要求放在循环里读，每比较一个对象都要重新输入；对象的属性不用 getter 访问。考官报告指出了这两点（⟦9618_s24_41:2(e)(i)⟧）。
- 拆分后比较的是数字而不是颜色；把拆出的数据都存进一个数组，没有用 6 个数组（⟦9618_s25_41:2(b)⟧ 的考官报告）。
- 没有判断哪些记录是空的（如关键字段为 –1）就输出（⟦9618_s25_42:2(f)(i)⟧ 的考官报告）。
- 百分比的分母用错；输出“没答出的词”时把数组第一个元素（主词）也算了进去（⟦9618_s24_42:1(c)(ii)⟧ 的考官报告）。
- 读文件时没去掉换行，颜色变成 `"red\n"`，和 `"red"` 比较永远不相等。MS 范例（p.22）用 `SplitLine[1].strip()` 处理这一点；本手册在读文件时就 `strip()`。

#### 代表题精讲　⟦9618_s25_41:2(b)⟧

**在考什么**　文本文件 TheData.txt 有 72 行，每行“整数,颜色”（如 `10,red`），共 6 种颜色。2(a) 的 `ReadData()` 把文件每行读进一个一维数组并返回（FL-01 的代表题）。2(b) 写过程 `SplitData()`：参数是字符串数组 `DataArray`；声明 6 个一维数组，每种颜色一个；把每个字符串拆成整数和颜色，整数存进对应颜色的数组。6 分，MS 列 6 点，1 mark each。讲解时对照原卷 QP p.4（2(a)、2(b) 在这一页；2(c)–(e) 在 p.5），MS p.21–22（Python 范例在 p.22）。

**完整作答**（整道大题的最终 Python；证据格按小问截取代码，早期测试截图在后续修改前另存）

```python
# Question2_J25: 2(a)-(e)
def ReadData():
    DataList = []  # STRING, unknown number of lines
    FileName = input("Enter the filename: ")
    try:
        with open(FileName, "r") as File:
            for Line in File:
                DataList.append(Line.rstrip("\n"))
    except OSError:
        print("Cannot open or read the file")
    return DataList


def StoreData(DataToStore, FileName):
    try:
        with open(FileName, "a") as File:  # MP1 append and automatic close
            for Item in DataToStore:  # MP2
                File.write(str(Item))  # MP3
                File.write("\n")  # MP4
    except OSError:
        print("Cannot create or write to file")  # MP5


def SplitData(DataArray):
    Red = []  # INTEGER arrays, unknown size, one per colour
    Green = []
    Blue = []
    Orange = []
    Yellow = []
    Pink = []
    for Index in range(len(DataArray)):
        Parts = DataArray[Index].split(",")
        Number = int(Parts[0])
        Colour = Parts[1]
        if Colour == "red":
            Red.append(Number)
        elif Colour == "green":
            Green.append(Number)
        elif Colour == "blue":
            Blue.append(Number)
        elif Colour == "orange":
            Orange.append(Number)
        elif Colour == "yellow":
            Yellow.append(Number)
        elif Colour == "pink":
            Pink.append(Number)
    StoreData(Red, "Red.txt")
    StoreData(Green, "Green.txt")
    StoreData(Blue, "Blue.txt")
    StoreData(Orange, "Orange.txt")
    StoreData(Yellow, "Yellow.txt")
    StoreData(Pink, "Pink.txt")


if __name__ == "__main__":
    DataFromFile = ReadData()
    SplitData(DataFromFile)
```

**运行核对**　整题 2(a)–(e) 输入 TheData.txt，读取官方 72 行，按颜色分类并追加到六个文件。Red.txt 的 12 行为 10、9、1、76、19、38、34、46、14、45、37、43；不再用控制台的 red/pink 列表代替文件证据。缺文件与追加路径验证见 FL-01、FL-03。整题 QP p.4–5 / MS p.18–29。

**与 MS 逐点对齐**

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure header (and end) taking (1D array) DataArray (of strings) as a parameter | `def SplitData(DataArray):` | `module-header` |
| 2 | Declaration/use of 6 1D arrays (equivalent), one for each colour | `Red = []` 等 6 个 | `declare-array` |
| 3 | Looping through each line in parameter DataArray … | `for Index in range(len(DataArray)):` | `count-loop` |
| 4 | … splitting by comma | `.split(",")` | `field-extract`、`string-functions` |
| 5 | Comparing 2nd value/colour to each colour to select array … | `if Colour == "red":` … `elif` | `relational-ops`、`nested-if` |
| 6 | … storing 1st value/integer in correct array | `Red.append(Number)` | `array-index`、`type-conversion` |

这里 6 个数组用空列表加 `append`：题目没给每种颜色的元素个数，MS 范例也是这样写的。题目给出元素个数时（AR-01）才必须建出定长的 list。`split` 是允许的：题目没有禁止内置拆分函数（与 PR-02 的 `SplitData()` 不同）。

**证据格怎么交**　2(b) 格贴整个 `SplitData()`（之后 2(d) 改了它，2(d) 格贴改过的版本）。2(e)(ii) 的截图格看“输入文件名 TheData.txt 的提示与输入”和“红色文件的内容，文件名要在同一张截图里”（见 FL-03）。

**直观**　分拣快递：每个包裹贴着“数字,颜色”的标签，撕下标签看颜色，把包裹放进对应颜色的筐里。

**对应练习与阶梯**　练习目录 practice/p4/9618_s25_41_q2/（2(a)–2(e) 全题，带官方 TheData.txt 与 6 个空颜色文件）；先过阶梯 **L07 E05**（拆字段、按条件写出）、**L06 E05**（按值分组计数）。

**下一道变式**　⟦9618_s24_41:2(e)(i)⟧　（换成“多条件筛选对象”：用户输入最大高度、最大宽度、是否常绿，用 getter 逐个比较 Tree 对象，满足全部条件的存进新数组并调用 `PrintTrees()`；一棵都没有时输出提示。MS 列 7 点，Max 6。）

<!-- auto:drills P4-AR-05 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| AR-01 vs AR-02 vs AR-03 | 一维 → AR-01；行 × 列 → AR-02；元素有多个不同类型的字段 → AR-03 | 题目给的声明形状 |
| AR-01 / AR-02 vs SQ / LT | 数组与指针是栈、队列、链表、二叉树、哈希表的 → 对应 SQ / LT 题型 | 有没有 Pointer、Push、Enqueue |
| AR-03 vs OP-01 | 只有字段、可以用公有属性 → AR-03；题目要求私有属性、构造方法、方法 → OP-01 | record 还是 class with private attributes |
| AR-04 vs LT-01 / LT-04 | 按下标顺序输出 → AR-04；沿指针走链表、中序 / 后序遍历树 → LT | in the order they are stored 还是 following the pointers |
| AR-04 vs AR-05 | 全部输出 → AR-04；先按条件挑选、统计 → AR-05 | meet the requirements / percentage / longest |
| AR-05 vs SR-01 | 多条件、范围、最值、分组 → AR-05；只和一个目标值比较“是否等于”→ SR-01 | 比较对象是一个值还是一组条件 |
| `[[0] * 2 for i in range(100)]` vs `[[0] * 2] * 100` | 前者 100 个独立的行；后者 100 个引用指向同一行 | 改一个元素，别的行跟着变 |
| `print(x, end=" ")` vs `print(x)` | 前者不换行、后面接空格；后者输出后换行 | 同一行 / 每项一行 |
