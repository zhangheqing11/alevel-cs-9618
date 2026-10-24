## RC　递归 {#ch-RC}

<!-- auto:chapter-stats -->

### 核心思想

递归（recursion）把当前问题缩成同类的小问题，再把小问题的返回值组合成本层答案。每次调用都有自己的参数和局部变量；不是“跳回开头继续用同一套变量”。先写基本情况（base case），再写会更接近基本情况的递归调用，最后检查每个分支都把答案 return 给上一层。

一条小追踪：数 [0,5,0] 里的 0 → 1 + 数 [5,0] → 1 + 数 [0] → 1 + 1 + 数 [] → 1 + 1 + 0 = 2。读数组前先判断空，空数组的结果是 0。

两个题型：**RC-01** 按文字描述或题给伪代码写一个递归子程序（基本情况 + 缩小的递归调用 + 每个分支都 `return`）；**RC-02** 把题给的迭代版改成递归，或把递归改成迭代（循环变量对应递归参数，累加器对应返回值的组合）。二分查找、递归插入排序仍在 SR，树遍历在 LT——那里的递归只是实现手段，得分点在算法本身。P3-CT-10～CT-12 问的是同一件事的理论面：递归的定义与要素、为什么用栈实现、追踪递归调用。

### 题型树
<!-- auto:type-tree -->

### P4-RC-01　按描述或伪代码写递归子程序　{#P4-RC-01}

<!-- auto:stats P4-RC-01 -->

**考法**　按文字或给定伪代码写递归函数；分别处理基本情况、命中与不命中分支，并正确缩小参数。

**识别信号**　recursive function；returns 0 if no elements；recursive call passing array without first element。

**解题思路**
1. 写明函数结果的意义：本题返回当前数组里目标的出现次数。
2. 基本情况：NumberElements == 0 就 return 0，先于 ArrayCopy[0]。
3. 取首项比较：命中贡献 1，未命中贡献 0。
4. 两条分支都递归传剩余数组、元素数减 1、相同目标；都 return 递归结果。
5. 本题明确要求传“不含首项的数组”，用切片 ArrayCopy[1:]；不能只改数量却传原数组。

**Python 模板**

```python
def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if NumberElements == 0:
        return 0
    if ArrayCopy[0] == DataToFind:
        return 1 + RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
    else:
        return RecursiveCount(ArrayCopy[1:], NumberElements - 1, DataToFind)
```

**得分表述**（引自对应 MS）
- 「Function header (and end) taking three parameters」⟦9618_w25_43:3(a)(i)⟧
- 「Checking number of elements for 0 and returning 0 (e.g. ArrayCopy = [] // len(ArrayCopy) == 0)」⟦9618_w25_43:3(a)(i)⟧
- 「(otherwise) comparing first array element to parameter DataToFind …」⟦9618_w25_43:3(a)(i)⟧
- 「… if match return recursive call adding 1」⟦9618_w25_43:3(a)(i)⟧
- 「… if no match return recursive call without adding 1」⟦9618_w25_43:3(a)(i)⟧
- 「… all recursive calls have array without first element, NumberElements-1 and DataToFind」⟦9618_w25_43:3(a)(i)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去掉 `equivalent_of`；同一行同一标签计一次；s26 只进计数。本型 2 行，均已拆点。下表最多列 8 个覆盖行数较多的标签；同次数按标签名排序，不把行数当分值。）

| 技能标签 | 行数 |
|:--|--:|
| `recursion` | 2 |
| `array-index` | 1 |
| `div-mod` | 1 |
| `module-header` | 1 |
| `relational-ops` | 1 |
| `return-value` | 1 |
| `translate-pseudocode` | 1 |

地图用于安排复习：先练覆盖行数较多的技能，再按当前题自己的 MS 检查每一点。多个标签可以属于同一个得分点，不能相加算分。

**易错与失分**
- 只写递归调用却不 return，最外层会得到 None。考官报告指出有答案调用了函数却没有返回调用结果（⟦9618_w25_43:3(a)(i)⟧）。
- 元素数变小、数组没切掉首项，每层都会重复比较同一个数。
- 先取 ArrayCopy[0] 再判空，递归到最后一层就越界。
- 把命中的 1 加进 DataToFind，改变了查找目标；应加在返回值上。

#### 代表题精讲　⟦9618_w25_43:3(a)(i)⟧

**在考什么**　QP p.12 是描述、参数和数组，p.13 是测试与拆字符串；MS p.32–33 是本问（Python p.33），p.34 与 p.39 是截图结果。6 点各 1 分。以下整题程序还实现 3(b) 的逐字符拆分，不用 split()。参数顺序按本程序签名一致传递；MS 示例把目标放第一位，是另一种一致的排列。

**完整作答**（整道大题的最终程序；分格提交时按小问截取代码，早期截图在后续修改前另存）

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

**运行核对**　QP 给的十个数查 0，输出 2；随后四行字符串拆分结果与 MS p.34、39 相同，退出码 0。补测空数组返回 0、全命中、全不命中；用调用包装器确认长度 n 的输入实际有 n+1 次调用。

**与 MS 逐点对齐**　MS 未印逐点号码；下表 MP 按语料 `markpoints[].n` 顺序。

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function header (and end) taking three parameters | 三个参数的函数头 | `module-header` |
| 2 | Checking number of elements for 0 and returning 0 (e.g. ArrayCopy = [] // len(ArrayCopy) == 0) | 空时先返回 0 | `recursion`、`return-value` |
| 3 | (otherwise) comparing first array element to parameter DataToFind … | 比较 ArrayCopy[0] 与目标 | `relational-ops`、`array-index` |
| 4 | … if match return recursive call adding 1 | 命中 `return 1 + RecursiveCount(...)` | `recursion`、`return-value` |
| 5 | … if no match return recursive call without adding 1 | 未命中 `return RecursiveCount(...)` | `recursion`、`return-value` |
| 6 | … all recursive calls have array without first element, NumberElements-1 and DataToFind | 两分支都传 `[1:]`、数量−1、同一目标 | `recursion`、`array-index` |

**分值边界**　该小问 6 分；全部列点按该题 MS 计分。`//` 是同一点的替代说法，接续句是否独立成点以本表与原页为准。

**证据格怎么交**　3(a)(i) 贴 RecursiveCount，3(a)(ii) 贴 MyArray 与调用、输出，3(a)(iii) 截图须有 2（MS p.34）。3(b)(i) 贴字符串赋值，3(b)(ii) 贴 SplitData，3(b)(iii) 贴调用与逐项输出；3(b)(iv) 截图有四行 x=0、y=1、x=x+y、y++，无分号（MS p.39）。

**直观**　把一叠卡分工：我只看第一张，剩下交给下一层；它告诉我后面有几个，我再加上自己这一张的贡献。

**对应练习与阶梯**　practice/p4/9618_w25_43_q3/（T35 并行生成，按目录命名规则定位）；前置阶梯 **L11 E01**（递归追踪）、**L11 E02**（递归函数）。

**下一道变式**　⟦9618_w23_42:2(b)(i)⟧　QP p.6–8（递归伪代码在 p.7）、MS p.19–21。RecursiveValue(Number, ToFind) 遍历候选因数，Number=0 返回 0；否则 ToFind % Number == 0 时返回 Number 加递归结果，两个分支都传 Number−1 与原 ToFind。5 个填空合为语料 MP1（5 分），递归调用 MP2、其余结构 MP3，共 7 分。

<!-- auto:drills P4-RC-01 -->

### P4-RC-02　迭代与递归互相改写　{#P4-RC-02}

<!-- auto:stats P4-RC-02 -->

**考法**　把循环算法改成递归，或把递归展开为迭代；结果相同且符合要求的控制结构。

**识别信号**　Rewrite as a recursive function；iterative algorithm；no loop repeated inside each recursive call。

**解题思路**
1. 从原算法分出每轮做的工作、循环状态、结束条件与最终结果。
2. 结束条件变成基本情况：字符串长度为 0 返回 0。
3. 一次调用只处理一个首字符，循环状态改由更短的参数表达。
4. 原来的累计动作变成返回值的组合：元音返回 1 + 剩余结果，非元音只返回剩余结果。
5. 删掉原遍历循环；不能在每层递归里又完整循环整串。反向改成迭代时，用循环状态和累计变量代替调用链。

**Python 模板**

```python
def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    First = Value[0]
    if First == "a" or First == "e" or First == "i" or First == "o" or First == "u":
        return 1 + RecursiveVowels(Value[1:])
    else:
        return RecursiveVowels(Value[1:])
```

**得分表述**（引自对应 MS）
- 「Recursive call」⟦9618_w23_41:1(b)(i)⟧
- 「Function header (and end where appropriate) taking string parameter (returning integer where given)」⟦9618_w23_41:1(b)(i)⟧
- 「Base case checking (length is 0) and returning 0」⟦9618_w23_41:1(b)(i)⟧
- 「Extracting first character and checking if a vowel …」⟦9618_w23_41:1(b)(i)⟧
- 「… if it is a vowel, returning 1 + recursive call with 1 less character」⟦9618_w23_41:1(b)(i)⟧
- 「… if not a vowel, return recursive call with 1 less character」⟦9618_w23_41:1(b)(i)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去掉 `equivalent_of`；同一行同一标签计一次；s26 只进计数。本型 2 行，均已拆点。下表最多列 8 个覆盖行数较多的标签；同次数按标签名排序，不把行数当分值。）

| 技能标签 | 行数 |
|:--|--:|
| `module-header` | 2 |
| `recursion` | 2 |
| `return-value` | 2 |
| `accumulator` | 1 |
| `char-compare` | 1 |
| `relational-ops` | 1 |
| `string-index` | 1 |

地图用于安排复习：先练覆盖行数较多的技能，再按当前题自己的 MS 检查每一点。多个标签可以属于同一个得分点，不能相加算分。

**易错与失分**
- 用循环重写了一遍原函数，没有任何递归调用。考官报告指出有答案仍然是迭代版本（⟦9618_w23_41:1(b)(i)⟧）。
- 每次递归调用里保留原 for，造成同一字符重复计算。考官报告也指出了这一问题（同上）。
- 转为小写会改变这题“只数小写元音”的规格；不能为了方便把 A 也算进去。
- 递归求和若使用全局 Total，容易让两次独立调用共享旧结果；本题直接组合返回值。

#### 代表题精讲　⟦9618_w23_41:1(b)(i)⟧

**在考什么**　QP p.2 是 IterativeVowels 的完整伪代码与 MID 的 0 起约定；p.3 是 1(a)、1(b) 和测试字符串。MS p.6–8 是本问（Python p.8），6 点各 1 分。完整程序同时保留严格按给定结构翻译的迭代函数，和新写的递归函数。

**完整作答**（整道大题的最终程序；分格提交时按小问截取代码，早期截图在后续修改前另存）

```python
# Question1_N23: 1(a)-(b)
def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for X in range(LengthString):
        FirstCharacter = Value[0]
        if (FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i"
                or FirstCharacter == "o" or FirstCharacter == "u"):
            Total = Total + 1
        Value = Value[1:]
    return Total


def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    FirstCharacter = Value[0]
    if (FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i"
            or FirstCharacter == "o" or FirstCharacter == "u"):
        return 1 + RecursiveVowels(Value[1:])
    else:
        return RecursiveVowels(Value[1:])


if __name__ == "__main__":
    print(IterativeVowels("house"))
    print(RecursiveVowels("imagine"))
```

**运行核对**　运行整题依次输出 3 与 4，与 MS p.6、8 一致。补测空串、大小写混合、全元音、无元音，结果与逐字符计数相同；调用计数确认长度 n 的递归有 n+1 次调用。

**与 MS 逐点对齐**　MS 未印逐点号码；下表 MP 按语料 `markpoints[].n` 顺序。

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Recursive call | 两个非空分支均调用 RecursiveVowels | `recursion` |
| 2 | Function header (and end where appropriate) taking string parameter (returning integer where given) | 一个字符串参数的函数头 | `module-header` |
| 3 | Base case checking (length is 0) and returning 0 | `len(Value) == 0` 返回 0 | `recursion`、`return-value` |
| 4 | Extracting first character and checking if a vowel … | 取 Value[0]，比较五个小写元音 | `string-index`、`char-compare` |
| 5 | … if it is a vowel, returning 1 + recursive call with 1 less character | 元音 `return 1 + ...`，传 Value[1:] | `recursion`、`return-value` |
| 6 | … if not a vowel, return recursive call with 1 less character | 非元音直接返回更短字符串的调用结果 | `recursion` |

**分值边界**　该小问 6 分；全部列点按该题 MS 计分。`//` 是同一点的替代说法，接续句是否独立成点以本表与原页为准。

**证据格怎么交**　1(a)(i) 贴迭代函数，1(a)(ii) 贴 house 调用与输出，1(a)(iii) 截图有 3。1(b)(i) 贴递归函数，1(b)(ii) 贴 imagine 调用与输出，1(b)(iii) 截图有 4（MS p.6、8）。可以分别保存阶段截图；最终程序的两行输出与两个要求相符。

**直观**　循环像一个人把卡片逐张看完并记总数；递归像每人看一张，把“后面有几个”的回答传回来再相加。两者需要相同的停止点和计数规则。

**对应练习与阶梯**　practice/p4/9618_w23_41_q1/（T35 并行生成，按目录命名规则定位）；前置阶梯 **L11 E01**（追踪与调用栈）、**L11 E02**（迭代 / 递归）。

**下一道变式**　⟦9618_w22_42:3(d)⟧　QP p.8–9（迭代原算法在 p.9）、MS p.23。把队列总和改为递归。MS 示例的参数是“当前项下标”，主程序传 TailPointer−1，基例取 HeadPointer 处的值；原迭代 Start 是尾后位置、从 Start−1 开始，不能把两种参数含义混在一起。不要把语料 MP2 的 //20 当普适基例：按该题指针位置定停止条件。

<!-- auto:drills P4-RC-02 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| 基本情况 / 递归情况 | 直接给答案 / 缩小后调用自己再组合 | 是否还需要子问题 |
| 调用 / 返回调用结果 | 调用后丢弃结果 / 把子问题答案送回上一层 | 函数前是否需要 return |
| 数量−1 / 切掉一项 | 数量与实际数组必须同步 | 参数描述写不含首项 |
| 加 1 / 加当前值 | 计次数 / 求数值总和 | count / total |
| 原始 MID / 指南 MID | 旧题给出 0 起时照题；自写伪代码按指南 1 起 | 题干对函数的定义 |
| RC / SR、LT | RC 是递归机制；二分 / 排序 / 树仍按主要算法找对应卡 | 得分点落在哪个操作 |
