# L03 · 循环：FOR / WHILE / REPEAT…UNTIL ↔ for / while

> 考纲 11.2（count-controlled、post-condition、pre-condition 循环；说明为什么选某种循环）（考纲 p.29）· 指南 §7（p.20–21）

## 本级目标

学完本级，你能：

1. 把 `FOR … TO … [STEP …] … NEXT` 准确译成 `for … in range(…)`，不差一。
2. 把 `WHILE … ENDWHILE` 译成 `while`；把 `REPEAT … UNTIL` 译成 `while True` + `break`，并且知道 `UNTIL` 的条件是**退出条件**。
3. 写出四种常用模式：计数器、累加器、哨兵值（rogue value）循环、输入校验循环；以及嵌套循环。
4. 在三种循环之间互相改写（P2 常考「用前测循环改写」）。
5. 为一个场景选择循环类型并说出理由（考纲 11.2 的「justify」）。

## 伪代码 ↔ Python 对照

### 1. 计数循环：`FOR … TO … NEXT` ↔ `for … in range`（指南 p.20）

```pseudocode
FOR Index ← 1 TO 30
   StudentNames[Index] ← ""
NEXT Index
```

```python
for index in range(1, 31):
    ...
```

（数组本身 L06 再学；这里只看循环头。）

| 伪代码 | 循环变量依次取 | Python | 要点 |
|:--|:--|:--|:--|
| `FOR I ← 1 TO 5` | 1 2 3 4 5 | `for i in range(1, 6):` | `range` **不含终点**：终点写 `5 + 1` |
| `FOR I ← 1 TO N` | 1 … N | `for i in range(1, n + 1):` | 最常用的一行，背下来 |
| `FOR I ← 0 TO N - 1` | 0 … N−1 | `for i in range(n):` | Python 默认从 0 起 |
| `FOR I ← 1 TO 10 STEP 3` | 1 4 7 10 | `for i in range(1, 11, 3):` | 步长写第三个参数 |
| `FOR Position ← 20 TO 10 STEP -1`（p.27） | 20 19 … 10 | `for position in range(20, 9, -1):` | 负步长时终点要再往下多 1 |
| `FOR I ← 5 TO 1 STEP -2` | 5 3 1 | `for i in range(5, 0, -2):` | |
| `FOR I ← 3 TO 1` | （一次都不执行） | `for i in range(3, 1):` | 起点大于终点且步长为正：不执行（p.20） |
| `FOR I ← 4 TO 4` | 4 | `for i in range(4, 5):` | 起点等于终点：执行一次（p.20） |

- 循环变量必须是 `INTEGER`，起止值与步长都是整数表达式（p.20）；Python 的 `range` 也只收整数。
- `NEXT` 后面重复写循环变量名是好习惯，嵌套循环时尤其要写（p.20）。
- 指南的嵌套 FOR 例子（p.20）：外层每行先把 `RowTotal` 清零，内层累加，外层再把 `RowTotal` 加进 `Total`——注意两个累加器初始化的**位置**不同。

```pseudocode
Total ← 0
FOR Row ← 1 TO MaxRow
   RowTotal ← 0
   FOR Column ← 1 TO 10
      RowTotal ← RowTotal + Amount[Row, Column]
   NEXT Column
   OUTPUT "Total for Row ", Row, " is ", RowTotal
   Total ← Total + RowTotal
NEXT Row
OUTPUT "The grand total is ", Total
```

```python
total = 0
for row in range(1, max_row + 1):
    row_total = 0
    for column in range(1, 11):
        row_total = row_total + amount[row][column]   # 2D list: L06
    print(f"Total for Row {row} is {row_total}")
    total = total + row_total
print(f"The grand total is {total}")
```

- Python 的 `for ch in text:`、`for item in items:` 直接遍历一个序列，**伪代码没有这种写法**：P2 里要写 `FOR I ← 1 TO LENGTH(Text)` 再用 `MID(Text, I, 1)` 取字符（L05）。ECR P2 2024 p.29 把伪代码里写 `FOR Line IN InputFile` 这类 Python 式语法列为常见错误。

### 2. 前测循环：`WHILE … ENDWHILE` ↔ `while`（指南 p.21）

```pseudocode
WHILE Number > 9
   Number ← Number - 9
ENDWHILE
```

```python
while number > 9:
    number = number - 9
```

- 先检查条件，条件为 `TRUE` 才执行循环体；第一次检查就是 `FALSE` 时一次都不执行（p.21）。
- 条件是**继续**条件：成立就继续。
- 9618 指南的 `WHILE` 行末**没有 `DO`**（p.21）。如果你在 IGCSE 习惯写 `WHILE … DO`，从现在起去掉。

### 3. 后测循环：`REPEAT … UNTIL` ↔ `while True` + `break`（指南 p.20–21）

```pseudocode
REPEAT
   OUTPUT "Please enter the password"
   INPUT Password
UNTIL Password = "Secret"
```

```python
while True:
    print("Please enter the password")
    password = input()
    if password == "Secret":
        break
```

- 循环体**至少执行一次**；执行完才检查条件，条件为 `TRUE` 时**结束**（p.21）。所以 `UNTIL` 后面是**退出**条件，与 `WHILE` 的继续条件正好相反。
- Python 没有后测循环。标准译法：`while True:` + 循环体 + 最后一行 `if <UNTIL 的条件>: break`。**条件原样照抄，不取反。**
- 另一种译法是用标志变量，同样保证先执行一次：

```python
finished = False
while not finished:
    print("Please enter the password")
    password = input()
    finished = password == "Secret"
```

- **`break` 只属于 Python。** 指南没有 `BREAK` 关键字；ECR P2 2024 p.11 把在伪代码里用 `BREAK` 跳出列为常见错误。伪代码里要提前结束，就用 `WHILE` / `REPEAT` 加一个 BOOLEAN 标志（见 §6）。

### 4. 选哪种循环（考纲 11.2）

| 情境 | 选 | 一句话理由（英文作答可用） |
|:--|:--|:--|
| 次数在循环开始前就知道（处理 30 个学生、打印 1 到 N） | `FOR` | The number of iterations is known before the loop starts. |
| 可能一次都不用执行（输入第一个值就是结束标志；数据可能为空） | `WHILE` | The condition is tested before the loop body, so the body may not be executed at all. |
| 至少要执行一次（先输入、再检查是否有效） | `REPEAT` | The loop body must be executed at least once before the condition is tested. |

（这几句是教学用的说法，不是 MS 原文；具体题目的得分表述以该题 MS 为准。）

### 5. 四种常用模式

**计数器与累加器**：在循环**之前**初始化，在循环**里面**更新。

**哨兵值（rogue value）循环**：数据个数事先不知道，用一个特殊值表示结束。先读一个（预读），`WHILE` 不是哨兵就处理并读下一个：

```pseudocode
DECLARE Number : INTEGER
DECLARE Total : INTEGER
Total ← 0
OUTPUT "Enter a number (-1 to stop)"
INPUT Number
WHILE Number <> -1
   Total ← Total + Number
   OUTPUT "Enter a number (-1 to stop)"
   INPUT Number
ENDWHILE
OUTPUT "Total: ", Total
```

```python
total = 0
number = int(input("Enter a number (-1 to stop): "))
while number != -1:
    total = total + number
    number = int(input("Enter a number (-1 to stop): "))
print(f"Total: {total}")
```

**输入校验循环**：至少要输入一次，所以用 `REPEAT`：

```pseudocode
REPEAT
   OUTPUT "Enter a mark from 0 to 100"
   INPUT Mark
UNTIL Mark >= 0 AND Mark <= 100
```

```python
while True:
    mark = int(input("Enter a mark from 0 to 100: "))
    if mark >= 0 and mark <= 100:
        break
```

**嵌套循环**：外层每走一步，内层走完一整圈（见 §1 指南例子）。

### 6. 循环之间的改写

同一件事（输出 1 到 10）的三种写法：

```pseudocode
FOR Count ← 1 TO 10
   OUTPUT Count
NEXT Count
```

```pseudocode
Count ← 1
WHILE Count <= 10
   OUTPUT Count
   Count ← Count + 1
ENDWHILE
```

```pseudocode
Count ← 1
REPEAT
   OUTPUT Count
   Count ← Count + 1
UNTIL Count > 10
```

- `FOR` → `WHILE` / `REPEAT`：自己初始化计数器、自己在循环体末尾加 1。
- `WHILE C` → `REPEAT`：条件变成 `UNTIL NOT C`（或写出等价的相反条件，如 `<= 10` ↔ `> 10`）；但只有当循环至少要执行一次时两者才等价。
- 不是所有 `WHILE` / `REPEAT` 都能改成 `FOR`：次数事先不知道就不能（SoW Unit 11 p.36）。

**提前结束**：伪代码不要在 `FOR` 里改循环变量来「跳出」，改用条件循环加标志：

```pseudocode
Found ← FALSE
Index ← 1
WHILE Index <= 10 AND Found = FALSE
   IF Values[Index] = Target THEN
      Found ← TRUE
   ENDIF
   Index ← Index + 1
ENDWHILE
```

Python 可以在 `for` 里 `break`；但**在 `for` 循环体里给循环变量赋值不会让循环提前结束**——下一轮 `range` 会把它覆盖。ECR P4 2024 p.11 的 VB.NET 范答用 `x = NumberWords + 1` 跳出 `For`，这一招在 Python 里无效。

## 常见坑

1. **`range` 差一。** `range(1, 10)` 只到 9。SoW Unit 11 p.36 专门安排「循环跑了 11 次而不是 10 次」的找错练习；每写一个 `range`，都用最后一个值检查一遍。
2. **负步长的终点。** `FOR I ← 5 TO 1 STEP -2` 是 `range(5, 0, -2)`，不是 `range(5, 1, -2)`（后者不含 1）。
3. **`REPEAT` 译成了 `while 条件:`。** 两个错误常一起出现：条件没有取反，循环体也可能一次都不执行。用 `while True` + `if <UNTIL 条件>: break`，条件照抄。
4. **条件里写了 `←`。** `UNTIL RNum ← 100` 是错的，应为 `=`（ECR P2 2021 p.26）。Python 里相应的错误是条件里写 `=`。
5. **死循环。** `WHILE` 循环体里没有更新条件用到的变量；Python 里按 `Ctrl+C` 停止，再检查哪一行负责「向结束靠近」。
6. **累加器放错位置。** `Total ← 0` 写进循环里，每轮都被清零；嵌套循环里每行要清零的 `RowTotal` 才放进外层循环（指南 p.20）。
7. **哨兵值被当成数据。** 先加再判断，或者先读再加却没预读，都会把 `-1` 算进总和、多数一次。
8. **循环变量名前后不一致。** ECR P2 2021 p.30：考生声明 `Count`，后面写成 `Counter`。Python 里这会变成 `NameError`，或者悄悄多出一个新变量。
9. **忘了声明、忘了初始化。** ECR P2 2021 p.32 的点评指出考生没有声明循环变量；ECR P2 2024 p.29 也专门提到「用变量计数之前先初始化」。伪代码里循环变量、计数器、累加器都要 `DECLARE` 并赋初值。
10. **`FOR` 漏了 `←`。** `FOR Index 1 TO LENGTH(Line)` 是 ECR P2 2024 p.27 点名的常见错误；正确是 `FOR Index ← 1 TO LENGTH(Line)`。
11. **伪代码里用 `BREAK`。** 见 §3；ECR P2 2024 p.11 点名。
12. **`print(…, end="")` 之后忘了换行。** 横着打印一行数字后，要再 `print()` 一次，否则下一行输出会接在同一行上。

## 延伸阅读

- CS50P Lecture 2 “Loops” 讲义：<https://cs50.harvard.edu/python/notes/2/>——[While Loops](https://cs50.harvard.edu/python/notes/2/#while-loops)、[For Loops](https://cs50.harvard.edu/python/notes/2/#for-loops)、[Improving with User Input](https://cs50.harvard.edu/python/notes/2/#improving-with-user-input)（`while True` + `break` 做输入校验，E03 的思路来源）、[Mario](https://cs50.harvard.edu/python/notes/2/#mario)（嵌套循环）。（CC BY-NC-SA 4.0）
- CS50P Problem Set 2 “Coke Machine”：<https://cs50.harvard.edu/python/psets/2/coke/>（E04 的改编来源；CC BY-NC-SA 4.0）。
- Think Python 3e（CC BY-NC-SA 4.0）：第 3 章 [3.4 Repetition](https://allendowney.github.io/ThinkPython/chap03.html#repetition)（`for` 与 `range`）；第 7 章 [7.3 Updating variables](https://allendowney.github.io/ThinkPython/chap07.html#updating-variables)、[7.4 Looping and counting](https://allendowney.github.io/ThinkPython/chap07.html#looping-and-counting)。注意：第 3 版不讲 `while` 和 `break`，这两样以 CS50P Lecture 2 为准。
- 教材 Langfield & Duddell 2e：12.07 Loops（p.192）、14.06 Iteration（p.255）。书中说 Python 没有后测循环、改用前测循环；本卡 §3 给出与 `REPEAT` 语义一致的 `while True` + `break` 写法。
- 官方：伪代码指南 §7（p.20–21）；SoW Unit 11（p.36：循环互改、找差一错误）。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-trace-loops/`](exercises/E01-trace-loops/spec.md) | 干跑 | 否 | 读 FOR（含 STEP、负步长、零次）、WHILE、REPEAT |
| [`exercises/E02-rogue-average/`](exercises/E02-rogue-average/spec.md) | 输入输出 | 是 | 哨兵值 WHILE 循环、计数器、累加器、零数据 |
| [`exercises/E03-valid-mark/`](exercises/E03-valid-mark/spec.md) | 函数（含输入） | 是 | REPEAT 输入校验 ↔ `while True` + `break` |
| [`exercises/E04-coin-machine/`](exercises/E04-coin-machine/spec.md) | 输入输出 | 是 | REPEAT 累加到够数、常量、合法值判断 |
| [`exercises/E05-times-grid/`](exercises/E05-times-grid/spec.md) | 输入输出 | 是 | 嵌套 FOR、拼一行输出、总累加器 |
| [`exercises/E06-count-digits/`](exercises/E06-count-digits/spec.md) | 函数 | 是 | 选循环：REPEAT vs WHILE；用 `DIV`/`MOD` 拆数位 |
