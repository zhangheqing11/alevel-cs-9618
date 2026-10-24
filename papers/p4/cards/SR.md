## SR　查找与排序 {#ch-SR}

<!-- auto:chapter-stats -->

### 核心思想

先问数据有没有顺序，再问要找一个值还是把全部元素重排。线性查找逐项比较，计数题必须走完全部；二分查找只适用于已按同一关键字排序的数据，每轮排除中点及一半区间。排序时，冒泡交换相邻项，插入排序暂存当前项、移动已排好部分，再放回空位。

P4 考的是把算法写出来：不用 `in`、`index()`、`count()`、`sort()`、`sorted()` 代劳。二维数组或记录按一个字段比较时，交换 / 移动的单位仍是一整条数据，不能只动关键字。

### 题型树
<!-- auto:type-tree -->

### P4-SR-01　线性查找与计数　{#P4-SR-01}

<!-- auto:stats P4-SR-01 -->

**考法**　逐项与目标值比较，返回是否找到、位置或出现次数；也可在用户反复输入的游戏里查答案。

**识别信号**　linear search；counts and returns the number of times；compares input to each answer。

**解题思路**
1. 读清返回类型：本题是出现次数，不是第一个下标，也不是 True。
2. 计数先置 0；循环访问全部有效元素；相等才加 1。
3. 计数题不能第一次命中就 return；return 放在循环后。
4. 用户输入校验属于调用前的步骤，查找函数用参数值，不在里面再问一次。

**Python 模板**

```python
def LinearSearch(DataArray, DataToFind):
    Count = 0
    for Index in range(len(DataArray)):
        if DataArray[Index] == DataToFind:
            Count = Count + 1
    return Count
```

**得分表述**（引自对应 MS）
- 「Function header (and close where appropriate) taking array and search value as parameters」⟦9618_s23_41:1(c)⟧
- 「Looping through each array element and keeping count of the number of times the parameter appears」⟦9618_s23_41:1(c)⟧
- 「Returning the calculated count value」⟦9618_s23_41:1(c)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去掉 `equivalent_of`；同一行同一标签计一次；s26 只进计数。本型 5 行，均已拆点。下表列出现行数最多的 8 个标签；同次数按标签名排序，不把行数当分值。）

| 技能标签 | 行数 |
|:--|--:|
| `linear-search` | 5 |
| `accumulator` | 4 |
| `input-prompt` | 4 |
| `module-header` | 4 |
| `count-loop` | 3 |
| `input-validation` | 2 |
| `loop-bounds` | 2 |
| `output-format` | 2 |

地图用于安排复习：先练覆盖行数较多的技能，再按当前题自己的 MS 检查每一点。多个标签可以属于同一个得分点，不能相加算分。

**易错与失分**
- 把“有无”函数照搬成计数函数，遇到首个匹配就退出，后面的重复值全漏掉。
- 用 count / in 代劳，运行结果正确也没展示题目要求的算法（D10）。
- 计数初始化在循环内，每次又变成 0；或者 return 写在第一次循环内。

#### 代表题精讲　⟦9618_s23_41:1(c)⟧

**在考什么**　QP p.2 是声明、文件与输出过程，p.3 是 1(c) 和输入 12 的测试；MS p.9 是本问的 3 点与 Python，p.11 是截图结果。完整程序包括 1(a)–(d)，使用该卷 Data.txt。

**完整作答**（整道大题的最终程序；分格提交时按小问截取代码，早期截图在后续修改前另存）

```python
# Question1_J2023: 1(a)-(d)
def PrintArray(DataArray):
    for Index in range(len(DataArray)):
        print(DataArray[Index], end=" ")
    print()


def LinearSearch(DataArray, DataToFind):
    Count = 0
    for Index in range(len(DataArray)):
        if DataArray[Index] == DataToFind:
            Count = Count + 1
    return Count


if __name__ == "__main__":
    DataArray = [0] * 25  # INTEGER, 25 elements, local to main
    try:
        with open("Data.txt", "r") as File:
            for Index in range(25):
                DataArray[Index] = int(File.readline())
    except OSError:
        print("Cannot open or read file")
    PrintArray(DataArray)
    Valid = False
    while not Valid:
        try:
            DataToFind = int(input("Enter a whole number (0 to 100): "))
            if DataToFind >= 0 and DataToFind <= 100:
                Valid = True
        except ValueError:
            print("Enter a whole number")
    Result = LinearSearch(DataArray, DataToFind)
    print("The number", DataToFind, "is found", Result, "times.")
```

**运行核对**　官方 Data.txt 25 个整数完整读入；输入 12，输出 The number 12 is found 4 times.，与 MS p.11 相同。另核对空数组、重复值、完全找不到时计数为 0。

**与 MS 逐点对齐**　MS 未印逐点号码；下表 MP 按语料 `markpoints[].n` 顺序。

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function header (and close where appropriate) taking array and search value as parameters | 函数两个参数 | `module-header` |
| 2 | Looping through each array element and keeping count of the number of times the parameter appears | Count 先为 0；完整循环，相等才加 1 | `linear-search`、`accumulator` |
| 3 | Returning the calculated count value | 循环外 `return Count` | `return-value` |

**分值边界**　该小问 3 分；全部列点按该题 MS 计分。`//` 是同一点的替代说法，接续句是否独立成点以本表与原页为准。

**证据格怎么交**　1(c) 格只贴 LinearSearch；1(a)(ii) 是主程序文件读取段，1(b)(i) 是 PrintArray，1(d)(i) 是输入校验与调用。1(b)(iii) 截图先保留完整数组输出；1(d)(ii) 截图还须有输入 12 与找到 4 次（MS p.11）。

**直观**　像点名册里找同姓的人：每翻一项比较一次，不能找到第一个就宣布一共只有一人。

**对应练习与阶梯**　practice/p4/9618_s23_41_q1/（T35 并行生成，按目录命名规则定位）；前置阶梯 **L06 E02**（线性查找）、**L06 E05**（计数）。

**下一道变式**　⟦9618_s24_42:1(c)(i)⟧　QP p.3、MS p.8–10。Play() 反复输入答案，查找时跳过下标 0 的主词，答对后把答案置空，避免重复得分；输入 no 才结束。主题型仍是线性查找，但要维护每次输入的 Found 标志。

<!-- auto:drills P4-SR-01 -->

### P4-SR-02　二分查找（迭代或递归）　{#P4-SR-02}

<!-- auto:stats P4-SR-02 -->

**考法**　在已排序数组上迭代或递归二分查找；找到返回下标，空区间返回 −1。题给伪代码时按结构翻译。

**识别信号**　iterative BinarySearch；recursive BinarySearch；First / Last；Middle；returns the index or −1。

**解题思路**
1. 先保证升序；只查已填部分，Last 应为 NumberItems − 1。
2. 循环条件 First <= Last，使单元素区间也能检查。
3. 循环内用整除算中点，比较的是 DataStored[MidValue]，不是 MidValue 本身。
4. 小于中点数据就 Last = MidValue − 1；大于就 First = MidValue + 1；相等立即返回。
5. 区间变空再返回 −1；递归版同样在访问数组前检查空区间，并 return 递归结果。

**Python 模板**

```python
def BinarySearch(A, Target):
    First = 0
    Last = len(A) - 1
    while First <= Last:
        Middle = (First + Last) // 2
        if A[Middle] == Target:
            return Middle
        elif Target < A[Middle]:
            Last = Middle - 1
        else:
            First = Middle + 1
    return -1
```

**得分表述**（引自对应 MS）
- 「Function header BinarySearch taking DataToFind as a parameter」⟦9618_s24_41:1(e)(i)⟧
- 「Calculating the mid value (First + Last) \ 2 or equivalent inside loop」⟦9618_s24_41:1(e)(i)⟧
- 「Checking if the data at mid is the parameter and returning mid inside loop」⟦9618_s24_41:1(e)(i)⟧
- 「If DataToFind < mid, updating Last/Upper with mid – 1 inside loop」⟦9618_s24_41:1(e)(i)⟧
- 「If DataToFind > mid, updating First/Lower with mid + 1 inside loop」⟦9618_s24_41:1(e)(i)⟧
- 「Returning -1 when not found and a suitable loop with end criteria」⟦9618_s24_41:1(e)(i)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去掉 `equivalent_of`；同一行同一标签计一次；s26 只进计数。本型 5 行，均已拆点。下表列出现行数最多的 8 个标签；同次数按标签名排序，不把行数当分值。）

| 技能标签 | 行数 |
|:--|--:|
| `binary-search` | 5 |
| `div-mod` | 5 |
| `module-header` | 5 |
| `recursion` | 4 |
| `relational-ops` | 4 |
| `return-value` | 4 |
| `pre-condition-loop` | 2 |
| `translate-pseudocode` | 1 |

地图用于安排复习：先练覆盖行数较多的技能，再按当前题自己的 MS 检查每一点。多个标签可以属于同一个得分点，不能相加算分。

**易错与失分**
- 用 `/` 算中点会得到浮点数，不能直接作下标；用 `//`。
- 上下界只改到 Middle，不排除中点，可能停在同一区间永远循环。
- MS p.11 Python 范例初始 `Last = NumberItems`，会把未存数据的一格纳入；存满 20 个再找大于最大值的数时可能越界。本卡用 NumberItems − 1，不照抄范例边界（D31、D44）。
- 本问 MP4/5 原句把“中点数据”简称 mid；不是拿目标与下标比较。

#### 代表题精讲　⟦9618_s24_41:1(e)(i)⟧

**在考什么**　QP p.2–5 是整题；1(e)(i) 在 p.4，测试表在 p.5。MS p.10–11 是 6 个点与 Python，p.13 是截图。完整程序先输入数据、冒泡排序，再迭代二分查找；三阶段截图应在相应阶段保存。

**完整作答**（整道大题的最终程序；分格提交时按小问截取代码，早期截图在后续修改前另存）

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

**运行核对**　QP p.5 两组数据都实际运行，排序为 1 2 6 8 10；找 2 返回 1，找 7 返回 −1。另测已存区间的首尾、区间为空、目标大于最大值；不访问空余格。

**与 MS 逐点对齐**　MS 未印逐点号码；下表 MP 按语料 `markpoints[].n` 顺序。

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function header BinarySearch taking DataToFind as a parameter | `def BinarySearch(DataToFind)` | `module-header` |
| 2 | Calculating the mid value (First + Last) \ 2 or equivalent inside loop | 循环内 `(First + Last) // 2` | `binary-search`、`div-mod` |
| 3 | Checking if the data at mid is the parameter and returning mid inside loop | 与 `DataStored[MidValue]` 相等时返回 MidValue | `binary-search`、`relational-ops`、`return-value` |
| 4 | If DataToFind < mid, updating Last/Upper with mid – 1 inside loop | 目标较小就 Last = MidValue − 1 | `binary-search` |
| 5 | If DataToFind > mid, updating First/Lower with mid + 1 inside loop | 目标较大就 First = MidValue + 1 | `binary-search` |
| 6 | Returning -1 when not found and a suitable loop with end criteria | First > Last 时退出并返回 −1 | `return-value`、`pre-condition-loop` |

**分值边界**　该小问 6 分；全部列点按该题 MS 计分。`//` 是同一点的替代说法，接续句是否独立成点以本表与原页为准。

**证据格怎么交**　1(e)(i) 格贴 BinarySearch；1(e)(ii) 贴读目标、调用与输出。1(e)(iii) 两轮分别输入 5、1、6、2、8、10、2 和 5、1、6、2、8、10、7。MS p.13 接受首轮找到下标 1（或题目列的其他下标约定），第二轮 −1；本程序统一 0 起。1(c)(ii)、1(d)(iii) 则保留各自早期测试，不用最终查找测试替代。

**直观**　像按页码找字典：看中间页，目标在前半就连中间页一起排除，只在余下页里继续。区间里只剩一页时仍要看。

**对应练习与阶梯**　practice/p4/9618_s24_41_q1/（T35 并行生成，按目录命名规则定位）；前置阶梯 **L11 E03**（二分查找）、**L06 E03**（先排序）。

**下一道变式**　⟦9618_w25_42:2(e)⟧　QP p.7、MS p.23–24。RecursiveBinarySearch() 有四个参数，递归传新上下界，数组不切片；找到返回原数组下标，未找到 −1。它与本卡的冒泡代表题共用整题程序，见 SR-03。

<!-- auto:drills P4-SR-02 -->

### P4-SR-03　冒泡排序　{#P4-SR-03}

<!-- auto:stats P4-SR-03 -->

**考法**　用冒泡排序升序或降序重排；关键字可能是数值、字符串长度、二维记录的字段。题目可要求适用于任意长度。

**识别信号**　bubble sort；ascending order；any length；Do not use an inbuilt sorting method。

**解题思路**
1. 先确认比较方向和数据单位；升序遇到左大右小就交换。
2. 外层表示重复扫描，内层访问相邻两项，最后一对是 len(A)−2 与 len(A)−1。
3. 用临时变量保存被覆盖的值，再完成交换。
4. 无交换就停止：每轮开始 Swap=False，发生交换改 True。
5. 函数参数是数组，完成后 return 数组；别把长度写死为 20。

**Python 模板**

```python
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
```

**得分表述**（引自对应 MS）
- 「Function header (and end) taking (array) parameter and returning a sorted array after sorting」⟦9618_w25_42:2(c)⟧
- 「Outer loop …」⟦9618_w25_42:2(c)⟧
- 「… inner loop ...」⟦9618_w25_42:2(c)⟧
- 「… comparing elements and swapping into ascending order」⟦9618_w25_42:2(c)⟧
- 「Sort must work for array of any length i.e. loops for length of parameter array」⟦9618_w25_42:2(c)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去掉 `equivalent_of`；同一行同一标签计一次；s26 只进计数。本型 8 行，均已拆点。下表列出现行数最多的 8 个标签；同次数按标签名排序，不把行数当分值。）

| 技能标签 | 行数 |
|:--|--:|
| `bubble-sort` | 8 |
| `nested-loops` | 7 |
| `module-header` | 6 |
| `relational-ops` | 6 |
| `count-loop` | 4 |
| `return-value` | 3 |
| `array-2d` | 2 |
| `loop-bounds` | 2 |

地图用于安排复习：先练覆盖行数较多的技能，再按当前题自己的 MS 检查每一点。多个标签可以属于同一个得分点，不能相加算分。

**易错与失分**
- 内层循环到 len(A)，访问 A[Index+1] 就越界；range 的终点不包含。
- 每次覆盖 A[Index] 后才想起保存它，两个位置就变成同一个值。
- 本题函数必须支持任意长度；考官报告指出有些答案仍按固定大小循环（⟦9618_w25_42:2(c)⟧）。
- 不在每轮开始清除 Swap，排好序后仍永远循环。

#### 代表题精讲　⟦9618_w25_42:2(c)⟧

**在考什么**　QP p.6 的 2(a)–(c)、p.7–8 的主程序与测试；MS p.20–21 是本问（Python p.21），p.22、26 是截图条件。整题还包括去重随机数、输出、递归二分查找。随机数组每次不同，核对顺序与同一批元素，不照抄 MS 的某组数。

**完整作答**（整道大题的最终程序；分格提交时按小问截取代码，早期截图在后续修改前另存）

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

**运行核对**　随机种子 17 的可复现运行得到 20 个 0–100 的不同整数，排序后 3 到 98；三轮按题意输入最小 3、最大 98、缺失 0，分别 Found at position 0、19、Not found。随机种子只由验证脚本设置，卡里程序不固定随机数。另对长度 0–5、值为 0/1/2 的全部数组验证排序与元素保留。

**与 MS 逐点对齐**　MS 未印逐点号码；下表 MP 按语料 `markpoints[].n` 顺序。

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function header (and end) taking (array) parameter and returning a sorted array after sorting | 参数数组；最后 `return DataArray` | `module-header`、`return-value` |
| 2 | Outer loop … | `while Swap` 重复扫描 | `count-loop`、`bubble-sort` |
| 3 | … inner loop ... | `for Index in range(len(DataArray) - 1)` | `nested-loops`、`bubble-sort` |
| 4 | … comparing elements and swapping into ascending order | 左大右小，Temp 三步交换 | `relational-ops`、`bubble-sort` |
| 5 | Sort must work for array of any length i.e. loops for length of parameter array | 循环边界来自参数长度 | `loop-bounds` |

**分值边界**　该小问 5 分；全部列点按该题 MS 计分。`//` 是同一点的替代说法，接续句是否独立成点以本表与原页为准。

**证据格怎么交**　2(c) 格贴 BubbleSort；2(d)(i) 贴排序前 PrintArray、接收排序返回值、输出 Sorted 与再 PrintArray。2(d)(ii) 截图要有原来的 20 个数、Sorted、同一批数升序。2(f)(ii) 分别输入最小值、最大值、不在数组中的值：前两次位置 0 和 19，第三次 Not found（MS p.26）。测试三次时先看本次打印的数组，不假定上一次随机数组相同。

**直观**　像把相邻两张错序卡片互换：每扫一轮大数往右走；某轮完全没换，说明所有邻居都已正确。

**对应练习与阶梯**　practice/p4/9618_w25_42_q2/（T35 并行生成，按目录命名规则定位）；前置阶梯 **L06 E03**（冒泡排序）、**L11 E03**（后续二分查找）。

**下一道变式**　⟦9618_s24_41:1(d)(i)⟧　QP p.3、MS p.8–9。BubbleSort() 无参数，改排全局 DataStored 的有效部分，作为过程也不要求返回数组。比较、交换仍相同；外层可用固定遍数或交换标志控制。

<!-- auto:drills P4-SR-03 -->

### P4-SR-04　插入排序　{#P4-SR-04}

<!-- auto:stats P4-SR-04 -->

**考法**　暂存当前项，在前面已排好的一段中向后移动较大项，插入空位；也会考二维记录按优先级排序、有序表插入一条新记录。

**识别信号**　insertion sort；extracting element；moving elements；correct position；priority。

**解题思路**
1. 第 0 项自身已排序，从下标 1 开始取 CurrentValue。
2. Y 指向前一个元素；先检查 Y 非负，再比较当前项。
3. 只把比 CurrentValue 大的项右移；每移动一次 Y 减 1。
4. 停下时空位在 Y+1，把暂存值放回那里。
5. 记录或二维行要一起移动所有字段；最后按题目要求返回数组。

**Python 模板**

```python
def InsertionSort(DataArray):
    for X in range(1, len(DataArray)):
        CurrentValue = DataArray[X]
        Y = X - 1
        Moving = True
        while Y >= 0 and Moving:
            if DataArray[Y] > CurrentValue:
                DataArray[Y + 1] = DataArray[Y]
                Y = Y - 1
            else:
                Moving = False
        DataArray[Y + 1] = CurrentValue
    return DataArray
```

**得分表述**（引自对应 MS）
- 「InsertionSort() header (and close) taking array as a parameter and returning (attempt at) sorted array」⟦9618_s25_43:2(b)⟧
- 「Looping through/for each element」⟦9618_s25_43:2(b)⟧
- 「Extracting element and comparing to sorted list …」⟦9618_s25_43:2(b)⟧
- 「… moving elements in sorted list」⟦9618_s25_43:2(b)⟧
- 「… and inserting element in correct position (ascending order)」⟦9618_s25_43:2(b)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去掉 `equivalent_of`；同一行同一标签计一次；s26 只进计数。本型 6 行，均已拆点。下表列出现行数最多的 8 个标签；同次数按标签名排序，不把行数当分值。）

| 技能标签 | 行数 |
|:--|--:|
| `insertion-sort` | 6 |
| `module-header` | 6 |
| `relational-ops` | 5 |
| `count-loop` | 4 |
| `return-value` | 4 |
| `shift-values` | 4 |
| `array-index` | 2 |
| `nested-loops` | 2 |

地图用于安排复习：先练覆盖行数较多的技能，再按当前题自己的 MS 检查每一点。多个标签可以属于同一个得分点，不能相加算分。

**易错与失分**
- 不暂存 CurrentValue，第一次右移就把它覆盖。
- 插入位置写 Y 而非 Y+1，排到最左时还可能写到 Python 的最后一个元素。
- D25：模板把下标判断放在数组访问前的循环条件，条件里不访问数组，不依赖 AND 短路。Python 虽有短路，向伪代码迁移时也保持这个安全结构。
- 对二维作业只移动 priority 而不移动 job number，记录会被拆散。

#### 代表题精讲　⟦9618_s25_43:2(b)⟧

**在考什么**　QP p.4 声明、数据和插入排序，p.5–6 是输出与二分查找。MS p.20–22 是本问（Python p.21），p.25、32 是截图。完整程序包含 2(a)–(f)；本题数组有 14 项，原序与 QP 一致。

**完整作答**（整道大题的最终程序；分格提交时按小问截取代码，早期截图在后续修改前另存）

```python
# Question2_J25: 2(a)-(f)
def InsertionSort(DataArray):
    for X in range(1, len(DataArray)):
        CurrentValue = DataArray[X]
        Y = X - 1
        Moving = True
        while Y >= 0 and Moving:
            if DataArray[Y] > CurrentValue:
                DataArray[Y + 1] = DataArray[Y]
                Y = Y - 1
            else:
                Moving = False
        DataArray[Y + 1] = CurrentValue
    return DataArray


def OutputArray(DataArray):
    for Index in range(len(DataArray)):
        print(DataArray[Index], end=" ")
    print()


def Search(DataArray, ItemToFind):
    Low = 0
    High = len(DataArray) - 1
    while Low <= High:
        Middle = (Low + High) // 2
        if DataArray[Middle] == ItemToFind:
            return Middle
        elif DataArray[Middle] < ItemToFind:
            Low = Middle + 1
        else:
            High = Middle - 1
    return -1


if __name__ == "__main__":
    DataArray = [0, 3, 4, 56, 67, 44, 43, 32, 31, 345, 45, 6, 54, 1]  # INTEGER, 14
    OutputArray(DataArray)
    DataArray = InsertionSort(DataArray)
    OutputArray(DataArray)
    for Value in [0, 345, 67, 2]:
        Location = Search(DataArray, Value)
        if Location == -1:
            print(Value, "not found")
        else:
            print(Value, "found at index:", Location)
```

**运行核对**　QP 原数组排序为 0 1 3 4 6 31 32 43 44 45 54 56 67 345；四次查找 0、345、67、2 的结果为 0、13、12、未找到，与 MS p.25、32 相符。另核对空数组、单元素、重复值、逆序、已排好序；模板在每次数组访问前保证下标有效。

**与 MS 逐点对齐**　MS 未印逐点号码；下表 MP 按语料 `markpoints[].n` 顺序。

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | InsertionSort() header (and close) taking array as a parameter and returning (attempt at) sorted array | 函数收数组，最后返回 | `module-header`、`return-value` |
| 2 | Looping through/for each element | `for X in range(1, len(DataArray))` | `count-loop` |
| 3 | Extracting element and comparing to sorted list … | CurrentValue 暂存；与左侧较大项比较 | `insertion-sort`、`relational-ops` |
| 4 | … moving elements in sorted list | `DataArray[Y+1] = DataArray[Y]` | `insertion-sort`、`shift-values` |
| 5 | … and inserting element in correct position (ascending order) | 循环后 `DataArray[Y+1] = CurrentValue` | `insertion-sort`、`array-index` |

**分值边界**　该小问 5 分；全部列点按该题 MS 计分。`//` 是同一点的替代说法，接续句是否独立成点以本表与原页为准。

**证据格怎么交**　2(b) 格贴 InsertionSort；2(c) 格贴 OutputArray；2(d)(i) 贴排序前后输出与接收返回值。2(d)(ii) 截图显示原数组与升序数组；2(e) 贴 Search；2(f)(ii) 截图显示找 0、345、67 的位置以及 2 找不到，0 起下标为 0、13、12（MS p.32）。

**直观**　像整理手里的扑克牌：左手已经有序，右手拿一张暂存，左手较大的牌向右让位，把新牌放进空格。

**对应练习与阶梯**　practice/p4/9618_s25_43_q2/（T35 并行生成，按目录命名规则定位）；前置阶梯 **L11 E04**（插入排序）、**L06 E01**（数组追踪）。

**下一道变式**　⟦9618_w22_42:1(e)⟧　QP p.3、MS p.7。按 Jobs 的第二列 priority 升序，移动时 job number 与 priority 一起移；循环只处理 NumberOfJobs 项，不能把空行 −1 排到前面。

<!-- auto:drills P4-SR-04 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| 线性 / 二分 | 线性可用于未排序；二分必须按相同关键字有序 | 每项比较 / 中点折半 |
| 计数 / 第一个位置 | 计数需继续；位置题可以找到就返回 | returns count / index |
| 中点下标 / 中点数据 | Middle 是位置；A[Middle] 才是拿来比较的数 | 更新边界用位置，比较用值 |
| 冒泡 / 插入 | 相邻两项交换 / 暂存一项、移动有序前缀 | swap / shift and insert |
| 过程 / 函数 | 原地修改可以两者都用，但返回值按题目要求 | procedure / returns sorted array |
| 二维关键字 / 整行 | 用某一列比较，移动所有列 | job number 与 priority 不可分开 |
