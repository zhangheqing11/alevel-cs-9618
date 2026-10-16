# L06 · 一维/二维数组 ↔ list；线性查找、冒泡排序

> 考纲 10.2（index、upper/lower bound；1D/2D 数组；冒泡排序、线性查找）、9.2（考纲 p.27–28）· 指南 §3（p.10–11）

## 本级目标

学完本级，你能：

1. 按指南格式声明一维、二维数组，说出 index、lower bound、upper bound；在 Python 里建出同样大小的 list，并用注释说明元素个数与类型（P4 要求）。
2. 在 1 起（伪代码 `ARRAY[1:n]`）与 0 起（Python）之间换算下标，不越界。
3. 用循环初始化、遍历、移动数组元素；知道整个数组赋值在伪代码里是**复制**、在 Python 里只是**起别名**。
4. 写出线性查找（找到就停）与冒泡排序（带交换标志、逐趟缩短），伪代码与 Python 各一份。
5. 分清 P2 能写的（只有循环与下标）与 P4 Python 能用的（`len`、`in`、`sort` 等），以及 P4 题目要求「写出算法」时不能用内置函数。

## 伪代码 ↔ Python 对照

### 1. 声明与初始化（指南 p.10–11）

```pseudocode
DECLARE StudentNames : ARRAY[1:30] OF STRING
DECLARE NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR
FOR Index ← 1 TO 30
   StudentNames[Index] ← ""
NEXT Index
```

```python
student_names = [""] * 30                             # ARRAY[1:30] OF STRING -> indexes 0 to 29
noughts_and_crosses = [[" "] * 3 for _ in range(3)]   # ARRAY[1:3,1:3] OF CHAR -> [0..2][0..2]
```

| 伪代码 | Python | 说明 |
|:--|:--|:--|
| `DECLARE A : ARRAY[1:30] OF STRING` | `a = [""] * 30` | 指南的数组长度固定、元素类型相同，下界通常为 1（p.10） |
| `DECLARE G : ARRAY[1:3,1:3] OF CHAR` | `g = [[" "] * 3 for _ in range(3)]` | 二维 = list 套 list |
| `A[1] ← "Ali"` | `a[0] = "Ali"` | 下标减 1 |
| `G[2,3] ← 'X'`（p.10） | `g[1][2] = "X"` | Python 写两对方括号，**不能**写 `g[1, 2]` |
| `A[n + 1] ← A[n]`（p.10） | `a[n] = a[n - 1]` | 下标可以是表达式 |
| 用 FOR 逐个赋值（p.11） | 同左，或建 list 时直接给初值 | 指南不允许 `StudentNames[1 TO 30] ← ""` 这种成组赋值（p.11） |

- **P4 写 Python 数组时要说明大小和类型**：建一个真实的 list（空的或填好初值的），并在注释里写元素个数和数据类型（ER s23 9618/41 Q3 p.39；ECR P4 2021 p.39）。上面代码里的注释就是这种写法。
- 1 起与 0 起的换算有两种做法：① 每个下标减 1（推荐，Python 的习惯）；② 多开一个元素、不用下标 0（`[""] * 31`），让下标与伪代码一一对应。一个程序里只用一种，并写注释。P4 题目自己规定了下标范围时，照题目来。

### 2. 整个数组赋值：伪代码复制，Python 起别名（指南 p.11）

```pseudocode
SavedGame ← NoughtsAndCrosses     // the whole array is copied (same size and type)
```

```python
saved_game = noughts_and_crosses                       # WRONG: two names for the same list
saved_game = [row[:] for row in noughts_and_crosses]   # a real copy of a 2D list
saved = nums[:]                                        # a real copy of a 1D list (or list(nums))
```

伪代码允许把同大小、同类型的整个数组赋给另一个（p.11），之后两者互不影响。Python 的 `=` 只是让新名字指向**同一个** list：改一个，另一个跟着变。二维的复制要逐行复制。

同样的原因，**不要**用 `[[" "] * 3] * 3` 建二维 list：三行是同一个 list，改 `g[0][0]` 三行都变。

### 3. 遍历与边界

| 伪代码 | Python | 说明 |
|:--|:--|:--|
| `FOR Index ← 1 TO 30` … `A[Index]` | `for index in range(30):` … `a[index]` | 或 `for item in a:`（只读时） |
| 上界写常量或已知值 | `len(a)` | 伪代码的 `LENGTH()` 只用于字符串，**不能**求数组长度（ER w25 p.15） |
| `FOR Row ← 1 TO 3` / `FOR Column ← 1 TO 3` … `G[Row, Column]` | `for row in range(3):` / `for column in range(3):` … `g[row][column]` | 外层行、内层列 |
| 比较相邻元素 `A[J]` 与 `A[J + 1]`：`J` 只能到 `n - 1` | `for j in range(n - 1):` | 否则越过上界 |

Python 的**负下标不报错**：伪代码里 `A[0]` 越过下界会出错，而 Python 的 `a[-1]` 安静地给出最后一个元素。从 1 起的算法翻译时少减或多减一次 1，Python 不一定报错，只会给出错误结果。

### 4. 线性查找：找到就停

```pseudocode
FUNCTION FindPosition(Target : INTEGER) RETURNS INTEGER
   // Data is a global ARRAY[1:100] OF INTEGER
   DECLARE Index : INTEGER
   DECLARE Found : BOOLEAN
   Index ← 1
   Found ← FALSE
   WHILE Index <= 100 AND Found = FALSE
      IF Data[Index] = Target THEN
         Found ← TRUE
      ELSE
         Index ← Index + 1
      ENDIF
   ENDWHILE
   IF Found = TRUE THEN
      RETURN Index
   ELSE
      RETURN 0
   ENDIF
ENDFUNCTION
```

```python
def find_position(data: list[int], target: int) -> int:
    """Return the 1-based position of the first match, or 0."""
    for index in range(len(data)):
        if data[index] == target:
            return index + 1
    return 0
```

- 「找到就停」在伪代码里用**条件循环**（`WHILE`/`REPEAT`）加标志，或者在 `FOR` 里找到后立即 `RETURN`。**不要**把 `FOR` 套在 `WHILE` 里假装能提前退出——ER w25 p.15–16 专门举了这个「混合结构」的反例，说它不能正确实现「满足条件就退出」，相应的循环分不给。
- P4 里题目要求「search each element in turn」时，必须写循环；用 `if target in data` 不符合要求（ECR P4 2021 p.22）。函数要**返回**结果，不要在函数里直接输出（ECR P4 2021 p.25）。

### 5. 冒泡排序：交换标志 + 逐趟缩短

```pseudocode
// Data is a global ARRAY[1:N] OF INTEGER; N is a global INTEGER
PROCEDURE BubbleSort()
   DECLARE Boundary : INTEGER
   DECLARE J : INTEGER
   DECLARE Temp : INTEGER
   DECLARE Swapped : BOOLEAN
   Boundary ← N - 1
   REPEAT
      Swapped ← FALSE
      FOR J ← 1 TO Boundary
         IF Data[J] > Data[J + 1] THEN
            Temp ← Data[J]
            Data[J] ← Data[J + 1]
            Data[J + 1] ← Temp
            Swapped ← TRUE
         ENDIF
      NEXT J
      Boundary ← Boundary - 1
   UNTIL Swapped = FALSE OR Boundary < 1
ENDPROCEDURE
```

```python
def bubble_sort(data: list[int]) -> None:
    """Sort data in place into ascending order."""
    boundary = len(data) - 1
    while True:
        swapped = False
        for j in range(boundary):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        boundary = boundary - 1
        if not swapped or boundary < 1:
            break
```

- 每一趟把本趟最大的值「冒」到末尾，所以下一趟可以少比一次（`Boundary` 减 1）；一趟里没有交换，说明已经有序，可以提前结束。
- **降序**只要把比较改成 `<`（ECR P4 2021 p.25：很多考生在要求降序时仍写 `>`）。
- 交换要用临时变量（伪代码）；Python 可以写 `a, b = b, a`。
- Python 函数直接修改传入的 list，调用者看到的就是排好序的 list——这就是 L04 说的「list 参数有 BYREF 的效果」。函数里写 `data = sorted(data)` 只是让局部名字指向新 list，调用者的 list 不变。

### 6. 并行数组

两个（或多个）同样大小的数组用同一个下标表示同一条数据，例如 `Names[i]` 与 `Marks[i]`。排序时交换一个数组的元素，**另一个数组也要同步交换**（ER w22 9618/22 Q7 p.24–25 的冒泡排序题要求两个数组同时交换）。L08 会用记录数组代替并行数组。

## 常见坑

1. **数组声明写错。** 漏 `DECLARE`、漏元素类型或类型写错（如把记录数组写成 `OF STRING`）、范围里用逗号代替冒号（`ARRAY[1,2000]` 变成了二维）——ECR P2 2024 p.13 点名；二维数组两个范围的写法错误（ER w24 9618/22 Q2 p.21）。
2. **访问下界之外的元素。** 数组从 1 起，循环却访问了 `Data[0]`（ECR P2 2024 p.16：「data[0] is accessed but array starts at index 1」）。
3. **冒泡排序内层循环越界。** 比较 `A[J + 1]` 时 `J` 跑到了 `n`（ER w22 9618/22 Q7 p.25；ECR P4 2021 p.25：内层循环上界太大，访问 `theArray[y+1]` 越界——如果声明的 list 比要求的长，测试时还看不出来）。
4. **数组没有初始化就用来计数**（ECR P2 2021 p.32：考生没有把计数数组 `CharCount` 的元素初始化）。
5. **Python 起别名**：`copy = nums`、`[[0] * 3] * 3`（§2）。
6. **Python 二维下标写成 `g[x, y]`**，或用伪代码的写法访问二维 list（ER s22 9618/42 Q2 p.39）。
7. **用 `LENGTH()` 求数组长度**（ER w25 p.15）。
8. **全局数组在模块里又声明成局部数组**（ER w25 9618/21 Q4 p.18：很多考生把全局数组声明成了局部数组）。
9. **用 FOR 套在 WHILE 里实现「找到就停」**（ER w25 p.15–16）。
10. **P4 里该写算法的地方用了内置函数**：`in`、`index()`、`sort()`、`max()`（ECR P4 2021 p.22）。题目没有限制时可以用，但要先确认。
11. **Python 负下标**：`a[i - 1]` 在 `i = 0` 时是 `a[-1]`，不报错，结果是最后一个元素。

## 延伸阅读

- CS50P Lecture 2 讲义：[More About Lists](https://cs50.harvard.edu/python/notes/2/#more-about-lists)、[Length](https://cs50.harvard.edu/python/notes/2/#length)。（CC BY-NC-SA 4.0）
- Think Python 3e 第 9 章（CC BY-NC-SA 4.0）：[9.1 A list is a sequence](https://allendowney.github.io/ThinkPython/chap09.html#a-list-is-a-sequence)、[9.2 Lists are mutable](https://allendowney.github.io/ThinkPython/chap09.html#lists-are-mutable)、[9.7 Looping through a list](https://allendowney.github.io/ThinkPython/chap09.html#looping-through-a-list)、[9.9 Objects and values](https://allendowney.github.io/ThinkPython/chap09.html#objects-and-values)、[9.10 Aliasing](https://allendowney.github.io/ThinkPython/chap09.html#aliasing)、[9.11 List arguments](https://allendowney.github.io/ThinkPython/chap09.html#list-arguments)；第 7 章 [7.6 Search](https://allendowney.github.io/ThinkPython/chap07.html#search)。
- 教材 Langfield & Duddell 2e：13.03–13.05 Arrays（p.212–218）、14.14 Arrays（p.276）、23.01–23.02 Linear search / Bubble sort（p.412）。书中伪代码与 2027–29 指南不同时以指南为准。
- 官方：伪代码指南 §3（p.10–11）；SoW Unit 10（p.32：用纸格与卡片演示数组、冒泡排序与线性查找，并给有错的算法让学生干跑找错）。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-trace-arrays/`](exercises/E01-trace-arrays/spec.md) | 干跑 | 否 | 初始化、整体右移、整个数组复制 vs Python 别名、二维下标 |
| [`exercises/E02-linear-search/`](exercises/E02-linear-search/spec.md) | 函数 | 是 | 找到就停；并行数组里返回分数（找不到返回 -1） |
| [`exercises/E03-bubble-sort/`](exercises/E03-bubble-sort/spec.md) | 函数（原地修改） | 是 | 带标志的冒泡排序；升序/降序；原地修改 list |
| [`exercises/E04-noughts-crosses/`](exercises/E04-noughts-crosses/spec.md) | 函数 | 是 | 二维数组：行、列、两条对角线 |
| [`exercises/E05-tally-counts/`](exercises/E05-tally-counts/spec.md) | 函数 | 是 | 计数数组：初始化、值 → 下标的换算 |
