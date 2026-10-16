# L04 · 过程与函数：参数、返回值、BYVAL/BYREF、作用域

> 考纲 9.1（分解）、11.3（过程、函数、参数、术语）、12.2（结构图）（考纲 p.27、p.30）· 指南 §8（p.22–24）

## 本级目标

学完本级，你能：

1. 按指南格式写过程与函数的头、体、结束，并正确调用：过程用 `CALL`，函数只出现在表达式里。
2. 判断一个模块该写成过程还是函数，函数用 `RETURN` 交回结果，而不是 `OUTPUT`。
3. 说清 BYVAL 与 BYREF 的区别，并在 Python 里用三种办法实现 BYREF 的效果（返回新值、修改可变对象、全局变量）。
4. 分清局部变量与全局变量；在 Python 里正确使用 `global`。
5. 用考纲术语描述模块：header、interface、parameter、argument、return value。
6. 把流程图、结构图、模块说明表变成伪代码与 Python。

## 伪代码 ↔ Python 对照

### 1. 过程：定义与调用（指南 p.22–23）

```pseudocode
PROCEDURE DefaultSquare()
   CALL Square(100)
ENDPROCEDURE

PROCEDURE Square(Size : INTEGER)
   FOR Side ← 1 TO 4
      CALL MoveForward(Size)
      CALL Turn(90)
   NEXT Side
ENDPROCEDURE
```

```python
def default_square() -> None:
    square(100)


def square(size: int) -> None:
    for side in range(1, 5):
        move_forward(size)
        turn(90)
```

| 伪代码 | Python | 说明 |
|:--|:--|:--|
| `PROCEDURE Square(Size : INTEGER)` | `def square(size: int) -> None:` | 过程没有返回值，Python 写 `-> None` |
| 参数格式 `<param> : <data type>`（p.22） | `<param>: <type hint>` | Python 不检查类型标注 |
| `ENDPROCEDURE` | （缩进结束） | |
| `CALL Square(100)`（p.22） | `square(100)` | 过程调用是一条完整语句；Python 不写 `CALL` |
| `CALL DefaultSquare()` | `default_square()` | 没有参数也要写括号；Python 少了括号（`default_square`）不报错，但什么也不执行 |

调用时实参的个数、类型、顺序要与定义一致（p.22）。

### 2. 函数：`RETURNS` 与 `RETURN`（指南 p.23–24）

```pseudocode
FUNCTION Max(Number1 : INTEGER, Number2 : INTEGER) RETURNS INTEGER
   IF Number1 > Number2 THEN
      RETURN Number1
   ELSE
      RETURN Number2
   ENDIF
ENDFUNCTION

OUTPUT "Penalty Fine = ", Max(10, Distance * 2)
```

```python
def max_of(number1: int, number2: int) -> int:
    if number1 > number2:
        return number1
    else:
        return number2


print(f"Penalty Fine = {max_of(10, distance * 2)}")
```

- 函数头写明返回类型 `RETURNS <data type>`（p.23）↔ `-> <type>`。
- `RETURN` 一执行就立刻离开函数，后面的语句不再执行（p.23）。Python 的 `return` 相同。
- **函数调用不是完整语句**：只能出现在表达式里（赋值右边、条件里、`OUTPUT` 里），**不能写 `CALL`**（p.23）。返回值替换掉调用处，再算整个表达式。
- Python 函数如果走到末尾还没有 `return`，返回的是 `None`——这是「忘了 return」时最常见的现象。
- Python 里别把函数取名为 `max`、`sum`、`len`：会盖掉内置函数。

**过程还是函数？** 要交回**一个**值给调用处 → 函数；只是做事（输出、修改全局数据、通过 BYREF 交回多个值）→ 过程。

### 3. 术语（考纲 11.3，p.30）

| 术语 | 指的是 | 例（以 `Max` 为例） |
|:--|:--|:--|
| procedure / function header | 模块的第一行 | `FUNCTION Max(Number1 : INTEGER, Number2 : INTEGER) RETURNS INTEGER` |
| interface | 调用者需要知道的全部：名字、参数（个数、顺序、类型、传递方式）、返回类型 | 名字 `Max`，两个 INTEGER 参数（BYVAL），返回 INTEGER |
| parameter | 定义里的变量名 | `Number1`、`Number2` |
| argument | 调用时传入的值 | `10`、`Distance * 2` |
| return value | 函数交回的值 | `Max(10, 4)` 的值 `10` |

### 4. BYVAL 与 BYREF（指南 p.24）

```pseudocode
PROCEDURE SWAP(BYREF X : INTEGER, Y : INTEGER)
   Temp ← X
   X ← Y
   Y ← Temp
ENDPROCEDURE
```

- `BYVAL`：过程拿到的是值的副本，过程里改参数，调用者的变量不变。
- `BYREF`：过程拿到的是调用者变量本身，过程里改参数，调用者的变量也变。
- 同一种传递方式的几个参数连着写时，关键字不必重复（p.24）：上例中 `X`、`Y` 都是 BYREF。没写传递方式的参数一律按 BYVAL（p.22、p.24）。
- **函数不应有 BYREF 参数**（p.24）。要交回多个值就写过程，用 BYREF。

**Python 没有 BYVAL / BYREF 关键字。** 赋值给参数只是让这个名字指向新对象，调用者看不到变化：对 `int`、`float`、`str`、`bool` 来说，效果就是 BYVAL。要得到 BYREF 的效果，用下面三种办法之一：

| 办法 | 写法 | 什么时候用 |
|:--|:--|:--|
| ① 返回新值（推荐） | `def swap(x: int, y: int) -> tuple[int, int]: return y, x`，调用：`a, b = swap(a, b)` | 交回一个或几个简单值 |
| ② 修改可变对象 | 传入 list，在函数里改它的元素：`data[0] = 99`（不要写 `data = […]`） | 数组：Python 里传 list 本身就有 BYREF 的效果 |
| ③ 全局变量 | 在函数里写 `global total` 后再赋值 | P4 题目明确说是全局变量时；要在代码注释里写明 |

P4 考官报告（ER s22 9618/41 Q3，p.37）：题目给出带 BYREF 参数的伪代码算法，很多考生照抄成 Python，没有处理 BYREF，结果函数里的修改在返回后全部丢失。可接受的做法是返回多个值，或用全局变量并清楚注明。

### 5. 作用域：局部与全局

```pseudocode
DECLARE Total : INTEGER          // global: declared in the main program
Total ← 0

PROCEDURE AddToTotal(Amount : INTEGER)
   DECLARE Doubled : INTEGER     // local: exists only inside this procedure
   Doubled ← Amount * 2
   Total ← Total + Doubled
ENDPROCEDURE
```

```python
total = 0                        # global


def add_to_total(amount: int) -> None:
    global total                 # needed because we assign to total below
    doubled = amount * 2         # local
    total = total + doubled
```

| 情况 | Python 需要 `global` 吗 |
|:--|:--|
| 只**读**全局变量 | 不需要 |
| 给全局变量**重新赋值**（`total = …`、`total += 1`） | **需要**。否则 Python 认为 `total` 是局部变量，读它时报 `UnboundLocalError` |
| 修改全局 list 的**元素**（`data[i] = …`、`data.append(…)`） | 不需要（没有给名字 `data` 重新赋值） |
| 给全局 list 整个**重新赋值**（`data = […]`） | 需要 |

- 题目说某变量是全局的，就**不要**在模块里再 `DECLARE` 一个同名局部变量（ER w25，p.16、p.18 点名）。Python 里对应的错误是函数里写了 `next_number = 1`，新建了一个同名局部变量。

### 6. 流程图 → 伪代码（考纲 9.2、11.1）

| 流程图符号 | 伪代码 |
|:--|:--|
| 圆角框 `START` / `END` | 程序或模块的开始与结束 |
| 平行四边形 `INPUT …` / `OUTPUT …` | `INPUT` / `OUTPUT` |
| 矩形 `Set X to …` | 赋值 `X ← …`；`CALL …` |
| 菱形（判断）后面**不回头** | `IF … THEN … ELSE … ENDIF` |
| 菱形在前、箭头**回到菱形之前** | `WHILE … ENDWHILE`（先判断） |
| 先执行一段、菱形在后、箭头回到那一段开头 | `REPEAT … UNTIL …`（后判断） |

- 判断框上的 Yes/No 决定条件写成什么：如果 **Yes 走出循环**，`WHILE` 的条件要取反，或者改用 `REPEAT … UNTIL <该条件>`。
- 把流程图写成伪代码时不要发明 `GOTO`、`BREAK`（ECR P2 2024 p.11 把 `BREAK`、结构交错列为常见错误）。

### 7. 结构图与模块说明表 → 模块头（考纲 12.2）

P2 常给一张「模块 | 说明」表或结构图，要求写模块头或整个模块。读表的顺序：

1. 说明里有「returns …」→ `FUNCTION … RETURNS <类型>`；否则 `PROCEDURE`。
2. 「called with / takes … as a parameter」→ 列出参数和类型；结构图里数据只从下层传回上层、或双向的参数 → 考虑 BYREF。
3. 「prompts for and inputs …」→ 模块里写 `OUTPUT` 提示 + `INPUT`，**不要**再把这些值做成参数；反过来，已经作为参数传入的值，**不要**在模块里再 `INPUT` 一遍（ER w25 p.16「Parameter versus INPUT」）。
4. 「uses module X」→ 在表达式里调用函数 X、用它的返回值；不要自己再写一遍 X 的算法（ECR P2 2024 p.29：考生用 `CALL` 调函数、没有把第一个函数的返回值传给第二个函数）。

## 常见坑

1. **用 `CALL` 调函数，或把函数调用写成一条单独语句。** `CALL GetStat(Flag)`、`GetStat() → Flag`（ECR P2 2024 p.11）；`CALL Valid(MyString)` 再判断 `IF RESULT = TRUE`（ER s23 9618/22 Q8，p.18）。正确：`Flag ← GetStat()`、`IF Valid(MyString) = TRUE THEN`。Python 里的对应错误是调用了函数却没用它的返回值。
2. **用 `OUTPUT` 代替 `RETURN`。** 考官报告反复点名（ER w25 p.15；ER s23 9618/22 Q4，p.20；ECR P2 2024 p.27）。Python 里用 `print` 代替 `return`，调用处拿到的是 `None`。
3. **参数和 INPUT 混用。** 题目说值由参数传入，模块里就不要再 `INPUT` 覆盖它（ER w25 p.16；ECR P4 2021 p.38）；题目说模块要「prompt and input」，就不要把它们做成参数（ECR P2 2024 p.15）。
4. **该用 BYREF 的地方没写 BYREF**，或者 BYREF 参数漏了类型（ER w22 9618/23 Q5，p.28；ER w25 9618/22 Q7，p.27）。
5. **模块头写成 `Module X`，或过程/函数分不清**（ER s24 9618/21 Q7，p.15；ER w25 9618/22 Q7，p.27 把应是过程的 `Sort` 写成了函数）。
6. **`ENDPROCEDURE` 写在算法中间**（ECR P2 2024 p.11）。一个模块只有一个结束关键字，放在最后。
7. **Python 照抄 BYREF**：在函数里给参数赋值，以为调用者的变量会变（ER s22 9618/41 Q3，p.37）。用 §4 的三种办法之一。
8. **Python 忘了 `global`**：给全局计数器 `+= 1` 时报 `UnboundLocalError`。反过来也别处处写 `global`——只读、或只改 list 元素时不需要。
9. **Python 忘了 `return`**：函数结果是 `None`，接着做运算时报 `TypeError: unsupported operand type(s) … 'NoneType'`。
10. **函数里写了多余的 `input()` / `print()`**：函数型题目的测试直接调用函数，多余的 `input()` 会让测试卡住或失败。
11. **把全局变量重新声明成局部变量**（ER w25 p.16）：伪代码里多写一行 `DECLARE`，Python 里多写一行赋值，全局的值就再也改不到了。

## 延伸阅读

- CS50P Lecture 0 讲义：[Def](https://cs50.harvard.edu/python/notes/0/#def)、[Returning Values](https://cs50.harvard.edu/python/notes/0/#returning-values)。（CC BY-NC-SA 4.0）
- Think Python 3e（CC BY-NC-SA 4.0）：第 3 章 [3.1 Defining new functions](https://allendowney.github.io/ThinkPython/chap03.html#defining-new-functions)、[3.2 Parameters](https://allendowney.github.io/ThinkPython/chap03.html#parameters)、[3.3 Calling functions](https://allendowney.github.io/ThinkPython/chap03.html#calling-functions)、[3.5 Variables and parameters are local](https://allendowney.github.io/ThinkPython/chap03.html#variables-and-parameters-are-local)、[3.6 Stack diagrams](https://allendowney.github.io/ThinkPython/chap03.html#stack-diagrams)；第 6 章 [6.1 Some functions have return values](https://allendowney.github.io/ThinkPython/chap06.html#some-functions-have-return-values)、[6.2 And some have None](https://allendowney.github.io/ThinkPython/chap06.html#and-some-have-none)；第 9 章 [9.11 List arguments](https://allendowney.github.io/ThinkPython/chap09.html#list-arguments)（list 参数为什么有 BYREF 的效果）。
- 教材 Langfield & Duddell 2e：12.09 Modules（p.202）、14.08 Procedures（p.262）、14.09 Functions（p.265）、14.10–14.12 Passing parameters（p.267–269）；结构图见 15.02–15.03（p.289、p.292）。书中伪代码与 2027–29 指南不同时以指南为准。
- 官方：伪代码指南 §8（p.22–24）；SoW Unit 11（p.36–37：用「盒子」演示 BYVAL 与 BYREF）。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-trace-byref/`](exercises/E01-trace-byref/spec.md) | 干跑 | 否 | 读 BYVAL / BYREF / 函数调用；Python 用返回值实现 BYREF |
| [`exercises/E02-time-modules/`](exercises/E02-time-modules/spec.md) | 函数 + 输出 | 是 | 按模块说明表写三个模块；BYREF ↔ 返回元组；模块互相调用 |
| [`exercises/E03-ticket-globals/`](exercises/E03-ticket-globals/spec.md) | 函数（全局变量） | 是 | 全局变量、`global`、不要重复声明 |
| [`exercises/E04-flowchart-steps/`](exercises/E04-flowchart-steps/spec.md) | 输入输出 | 是 | 流程图 → 伪代码 → Python |
| [`exercises/E05-prime-modules/`](exercises/E05-prime-modules/spec.md) | 函数 | 是 | 函数在条件里被调用；用一个函数写另一个函数 |
