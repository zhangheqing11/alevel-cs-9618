# L11 · 递归；二分查找、插入排序；算法比较（Big O）

> 考纲 19.2（递归：要素、写与追踪、何时有利、编译器用栈与展开）、19.1（线性/二分查找、插入/冒泡排序、性能比较、Big O）（考纲 p.37）· 指南 §8（过程与函数 p.22–24）

## 本级目标

学完本级，你能：

1. 说出递归的三个要素：基本情况（base case）、向基本情况靠近的递归调用、返回时的「展开」（unwinding）；用调用栈追踪一个递归过程。
2. 写出递归函数与递归过程（伪代码与 Python），并能改写成迭代版本。
3. 写出二分查找（迭代与递归），说出它的前提（数组已排序）与性能（每次比较排除一半）。
4. 写出插入排序，并能与冒泡排序区分；说出两者的性能如何受初始顺序影响。
5. 用 Big O 比较算法的时间与空间复杂度。

## 伪代码 ↔ Python 对照

### 1. 递归的要素（考纲 19.2）

```pseudocode
FUNCTION Factorial(N : INTEGER) RETURNS INTEGER
   IF N = 0 THEN
      RETURN 1                          // base case: no recursive call
   ELSE
      RETURN N * Factorial(N - 1)       // general case: a smaller problem
   ENDIF
ENDFUNCTION
```

```python
def Factorial(N: int) -> int:
    if N == 0:
        return 1                        # base case
    return N * Factorial(N - 1)         # general case
```

- **基本情况**：不再调用自己、直接给出结果。没有它，或者永远到不了它，递归就不会停。
- **一般情况**：用更小的问题调用自己（`N - 1`），每次都更接近基本情况。
- **展开**：最深的一层先返回，返回值一层层代回去：`Factorial(3)` = `3 * Factorial(2)` = `3 * (2 * Factorial(1))` = `3 * (2 * (1 * Factorial(0)))` = `3 * 2 * 1 * 1` = 6。

**追踪表**（调用栈）：每次调用压一层，返回时弹一层。

| 调用 | 等待中的表达式 | 返回值 |
|:--|:--|:--|
| `Factorial(3)` | `3 * Factorial(2)` | 6 |
| `Factorial(2)` | `2 * Factorial(1)` | 2 |
| `Factorial(1)` | `1 * Factorial(0)` | 1 |
| `Factorial(0)` | （基本情况） | 1 |

编译器 / 解释器用**栈**保存每一层调用的参数、局部变量和返回地址；基本情况返回后逐层弹栈，这就是展开（考纲 19.2）。

**递归过程**里，递归调用之前的语句按「深入」的顺序执行，之后的语句按「返回」的顺序执行（L11/E01 专门练这一点）。

### 2. 递归与迭代

| | 递归 | 迭代 |
|:--|:--|:--|
| 写法 | 问题本身是递归定义的（阶乘、树的遍历）时更短、更接近定义 | 需要自己维护循环变量 |
| 内存 | 每层调用都占栈空间；层数太多会栈溢出 | 通常只需固定的几个变量 |
| 速度 | 有函数调用的额外开销 | 一般更快 |

Python 默认最多约 1000 层调用，超过会抛 `RecursionError`——这也是「没有基本情况」时你会看到的错误。

### 3. 二分查找（考纲 19.1）

前提：数组已经**排好序**。每次和中间元素比较，排除一半。

```pseudocode
// global: SearchArray : ARRAY[0:99] OF INTEGER (sorted); NumberItems : INTEGER
FUNCTION BinarySearch(SearchItem : INTEGER) RETURNS INTEGER
   DECLARE Low : INTEGER
   DECLARE High : INTEGER
   DECLARE Mid : INTEGER
   Low ← 0
   High ← NumberItems - 1
   WHILE Low <= High
      Mid ← (Low + High) DIV 2
      IF SearchArray[Mid] = SearchItem THEN
         RETURN Mid
      ENDIF
      IF SearchArray[Mid] < SearchItem THEN
         Low ← Mid + 1
      ELSE
         High ← Mid - 1
      ENDIF
   ENDWHILE
   RETURN -1
ENDFUNCTION
```

```python
def BinarySearch(SearchArray: list[int], SearchItem: int) -> int:
    Low = 0
    High = len(SearchArray) - 1
    while Low <= High:
        Mid = (Low + High) // 2
        if SearchArray[Mid] == SearchItem:
            return Mid
        if SearchArray[Mid] < SearchItem:
            Low = Mid + 1
        else:
            High = Mid - 1
    return -1
```

伪代码里数组是带上下界的全局数组（真题写法），不作为参数传入；Python 版把数组作为参数传入。递归版本把 `Low`、`High` 作为参数：`Low > High` 是基本情况（找不到，返回 -1）；否则比较中间元素，再对左半或右半**返回**递归调用的结果。

- `Mid` 用 `DIV` / `//`：`/` 的结果是实数，不能当下标。
- 条件是 `Low <= High`；更新是 `Mid + 1` / `Mid - 1`。写成 `Low < High` 会漏掉只剩一个元素的情况；写成 `Low ← Mid` 可能永远不结束。
- 性能：n 个元素最多比较约 log₂n 次（1024 个元素约 10–11 次），线性查找最坏要 n 次（考纲 19.1：二分查找的性能如何随数据量变化）。

### 4. 插入排序（考纲 19.1）

思路：把数组分成「已排好的前半」和「未排的后半」；每次取未排部分的第一个元素，从后往前和已排部分比较，比它大的都往后挪一格，然后把它放进空出的位置。

伪代码里用标志结束内层循环，**不要**写 `WHILE Position >= 0 AND TheArray[Position] > ItemToInsert`：指南没有规定 `AND` 是否短路，`Position` 为 -1 时 `TheArray[-1]` 可能越界。9618_s24_42 Q3 给出的递归插入排序也是用标志 `LoopAgain` 来写的（ECR P4 2024 p.29）。

```pseudocode
// global: TheArray : ARRAY[0:99] OF INTEGER; NumberItems : INTEGER
PROCEDURE InsertionSort()
   DECLARE Index : INTEGER
   DECLARE Position : INTEGER
   DECLARE ItemToInsert : INTEGER
   DECLARE KeepGoing : BOOLEAN
   FOR Index ← 1 TO NumberItems - 1
      ItemToInsert ← TheArray[Index]
      Position ← Index - 1
      KeepGoing ← TRUE
      WHILE KeepGoing = TRUE
         IF Position < 0 THEN
            KeepGoing ← FALSE
         ELSE
            IF TheArray[Position] > ItemToInsert THEN
               TheArray[Position + 1] ← TheArray[Position]
               Position ← Position - 1
            ELSE
               KeepGoing ← FALSE
            ENDIF
         ENDIF
      ENDWHILE
      TheArray[Position + 1] ← ItemToInsert
   NEXT Index
ENDPROCEDURE
```

```python
def InsertionSort(TheArray: list[int]) -> None:
    for Index in range(1, len(TheArray)):
        ItemToInsert = TheArray[Index]
        Position = Index - 1
        while Position >= 0 and TheArray[Position] > ItemToInsert:   # Python's "and" stops early
            TheArray[Position + 1] = TheArray[Position]
            Position = Position - 1
        TheArray[Position + 1] = ItemToInsert
```

| | 冒泡排序（L06） | 插入排序 |
|:--|:--|:--|
| 每一趟做什么 | 比较**相邻**两个元素，逆序就交换；一趟把最大值送到末尾 | 取下一个元素，在已排好的部分里找到它的位置**插进去**（其余元素后移） |
| 已经有序时 | 带标志的版本一趟就结束 | 每个元素只比较一次 |
| 稳定（相等元素保持原顺序） | 是（只在 `>` 时交换） | 是（只在 `>` 时后移） |

考官报告指出，要求写插入排序时很多考生写成了冒泡排序或两者混合，并且漏了「插入值已到正确位置就停止」的条件（ER s25 9618/43 Q2 p.48；ER w22 9618/42 Q1 p.48）。

### 5. Big O（考纲 19.1）

| 算法 | 最好 | 平均 / 最坏 | 额外空间 |
|:--|:--|:--|:--|
| 线性查找 | O(1) | O(n) | O(1) |
| 二分查找（迭代） | O(1) | O(log n) | O(1) |
| 二分查找（递归） | O(1) | O(log n) | O(log n)：调用栈 |
| 冒泡排序（带标志） | O(n)：已经有序 | O(n²) | O(1) |
| 插入排序 | O(n)：已经有序 | O(n²) | O(1) |

O(n²) 的意思是：数据量翻倍，时间大约变成 4 倍；O(log n) 是：数据量翻倍，只多比较一次。

### 6. 递归遍历二叉树（接 L10）

```pseudocode
PROCEDURE InOrder(NodePointer : INTEGER)
   IF NodePointer <> -1 THEN
      CALL InOrder(LeftPointer[NodePointer])
      OUTPUT TreeData[NodePointer]
      CALL InOrder(RightPointer[NodePointer])
   ENDIF
ENDPROCEDURE
```

```python
def InOrder(NodePointer: int) -> None:
    if NodePointer != -1:
        InOrder(LeftPointer[NodePointer])
        print(TreeData[NodePointer])
        InOrder(RightPointer[NodePointer])
```

- 中序（左、根、右）：二叉查找树按从小到大输出。前序（根、左、右）、后序（左、右、根）只是把输出的那一行移到前面或后面。
- 基本情况是「空指针」：`NodePointer = -1` 时什么也不做。Python 里一定要先判断，否则 `TreeData[-1]` 不报错，递归永远停不下来，最后抛 `RecursionError`。

### 7. 考官写的 Python 也要测

ECR P4 2024 p.33–34 给出的 `IterativeInsertion()` 范答（9618_s24_42 Q3(c)）是从数组末尾往前、逐步缩短 `NumberElements` 来处理的。按原样运行，`[100, 85, 644, 22, 15, 8, 1]` 得到 `[1, 15, 85, 100, 644, 22, 8]`，并没有排好序（T10 已核对）。正确的迭代版本像 §4 那样从下标 1 起向后处理。教训：**把算法翻译成代码后，一定要用数据跑一遍**——P4 本来就要求你贴运行截图。

另外，同一题给出的伪代码写的是 `CALL RecursiveInsertion(IntegerArray, NumberElements - 1)`（ECR P4 2024 p.29）：按指南 p.23，函数应在表达式里调用、不写 `CALL`。题目里的伪代码就照题目理解，自己写时按指南。

## 常见坑

1. **没有基本情况，或一般情况不向基本情况靠近**（例如 `Factorial(N)` 里写成 `Factorial(N)`、`N + 1`）：Python 抛 `RecursionError`。
2. **递归调用的参数写错**：ER s24 9618/42 Q3 p.45、ECR P4 2024 p.32：没有给 `NumberElements` 减 1。
3. **调用了递归函数却没用它的返回值**：递归版二分查找里写 `RecursiveBinarySearch(…)` 而不是 `return RecursiveBinarySearch(…)`，结果是 `None`。
4. **在递归函数里又加了循环**，导致调用一再重复（ER s24 9618/42 Q3 p.45）；或在使用前覆盖了参数的值（ECR P4 2024 p.32）。
5. **题目要迭代却写了递归**（ER s24 9618/41 Q1 p.39），或**要二分查找却写了线性查找**（ER s25 9618/43 Q2 p.49）。看清题目要求。
6. **改迭代时没去掉递归调用**，或只删了递归调用、其他地方没改（ER s24 9618/42 Q3 p.45；ECR P4 2024 p.35）。
7. **二分查找的 `Mid` 用了 `/`**；条件写成 `Low < High`；更新写成 `Low ← Mid`。
8. **插入排序写成了冒泡排序**，或漏了停止条件（ER s25 9618/43 Q2 p.48；ER w22 9618/42 Q1 p.48）。
9. **排序时把空元素（如 -1）也一起排了**（ER w22 9618/42 Q1 p.48）：只排已用的那部分。
10. **并行数组只移动了一个**（ER w22 9618/42 Q1 p.48；L06 E03）。
11. **P4 里用 `sort()`、`in`、`index()`、`max()` 代劳**：题目要求写出算法时不得分（D10）。

## 延伸阅读

- Think Python 3e（CC BY-NC-SA 4.0）：第 5 章 [5.8 Recursion](https://allendowney.github.io/ThinkPython/chap05.html#recursion)、[5.9 Stack diagrams for recursive functions](https://allendowney.github.io/ThinkPython/chap05.html#stack-diagrams-for-recursive-functions)、[5.10 Infinite recursion](https://allendowney.github.io/ThinkPython/chap05.html#infinite-recursion)；第 6 章 [6.6 Recursion with return values](https://allendowney.github.io/ThinkPython/chap06.html#recursion-with-return-values)、[6.7 Leap of faith](https://allendowney.github.io/ThinkPython/chap06.html#leap-of-faith)、[6.8 Fibonacci](https://allendowney.github.io/ThinkPython/chap06.html#fibonacci)。
- 教材 Langfield & Duddell 2e：23.01–23.04 Linear search / Bubble sort / Insertion sort / Binary search（p.412–413）、23.13 Big O notation（p.429）；24.01–24.05 Recursion（p.435–441）。书中伪代码与 2027–29 指南不同时以指南为准。
- 官方：考纲 19.1–19.2（p.37）。
- CS50P 没有递归与这些算法的专讲，本级不列 CS50P 讲次。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-trace-recursion/`](exercises/E01-trace-recursion/spec.md) | 干跑 | 否 | 递归过程的「深入」与「展开」顺序；递归函数的返回值 |
| [`exercises/E02-recursive-functions/`](exercises/E02-recursive-functions/spec.md) | 函数（检查确实递归） | 是 | 基本情况与一般情况：数字、数位、字符串 |
| [`exercises/E03-binary-search/`](exercises/E03-binary-search/spec.md) | 函数（检查读取次数） | 是 | 迭代与递归二分查找 |
| [`exercises/E04-insertion-sort/`](exercises/E04-insertion-sort/spec.md) | 函数（原地修改） | 是 | 一次插入 + 完整插入排序 |
| [`exercises/E05-tree-traversal/`](exercises/E05-tree-traversal/spec.md) | 函数（全局数组，检查确实递归） | 是 | 中序遍历、数结点、求高度 |
