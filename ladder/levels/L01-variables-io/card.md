# L01 · 变量、数据类型、输入输出与运算

> 考纲 9.2、10.1、11.1（考纲 p.27–29）· 指南 §1–2（p.5–9）、§5.1–5.2（p.15）、§5.5–5.6（p.16–17）· 插页函数表（以 9618_w25_in_21 p.2–4 为代表）

## 本级目标

学完本级，你能：

1. 用指南格式写出声明、常量、赋值、输入、输出语句，并逐行译成 Python。
2. 说出 `/`、`DIV`、`MOD` 的区别，知道它们在 Python 里是 `/`、`//`、`%`。
3. 明白 Python 的 `input()` 永远返回字符串，什么时候必须 `int()` / `float()`。
4. 控制输出格式：伪代码 `OUTPUT` 的逗号不加空格；Python `print` 的逗号加空格；用 f-string 保留小数位。
5. 用 `&`（伪代码）/ `+`（Python）连接字符串，会用 `NUM_TO_STR` / `str()` 先把数字变成字符串。
6. 读懂练习模板里的模块头：`FUNCTION … ENDFUNCTION`、`PROCEDURE … ENDPROCEDURE` ↔ `def`（L04 细讲）。

## 伪代码 ↔ Python 对照

### 1. 注释、大小写与标识符（指南 p.5–7）

| 项目 | 剑桥伪代码 | Python |
|:--|:--|:--|
| 注释 | `// comment`（p.6） | `# comment` |
| 关键字 | 全大写：`IF`、`REPEAT`、`PROCEDURE`（p.5） | 全小写：`if`、`while`、`def` |
| 标识符风格 | 混合大小写，如 `NumberOfPlayers`（p.5） | snake_case，如 `number_of_players`；P4 题目指定名字时照抄题目 |
| 大小写敏感吗 | **不敏感**：`Countdown` 与 `CountDown` 不能当两个变量用（p.7） | **敏感**：`total` 和 `Total` 是两个变量 |
| 合法字符 | 字母、数字、下划线，字母开头（p.7） | 同左 |
| 缩进 | 通常 3 个空格，只为可读（p.5） | 4 个空格，**是语法的一部分** |

### 2. 数据类型与字面量（指南 p.7）

| 剑桥类型 | 字面量写法 | Python 类型 | Python 字面量 |
|:--|:--|:--|:--|
| `INTEGER` | `5`、`-3` | `int` | `5`、`-3` |
| `REAL` | `4.7`、`0.3`、`-4.0`、`0.0`——小数点两边都要有数字 | `float` | `4.7`、`0.3`、`-4.0`（Python 也接受 `.3`、`4.`，但别这样写） |
| `CHAR` | 单引号：`'x'`、`'@'` | `str`（长度为 1） | `"x"` 或 `'x'` |
| `STRING` | 双引号：`"This is a string"`、`""` | `str` | `"This is a string"`、`""` |
| `BOOLEAN` | `TRUE`、`FALSE` | `bool` | `True`、`False` |
| `DATE` | 通常 `dd/mm/yyyy`，最好注明类型与格式 | `datetime.date` | `date(2027, 5, 10)`（L05 再讲） |

Python 没有字符类型：`'x'` 和 `"x"` 都是长度为 1 的 `str`。

### 3. 声明、常量与赋值（指南 p.8–9）

```pseudocode
CONSTANT HourlyRate = 6.50
DECLARE NumberOfHours : INTEGER
DECLARE TotalToPay : REAL
NumberOfHours ← 38
TotalToPay ← NumberOfHours * HourlyRate
```

```python
HOURLY_RATE = 6.50

number_of_hours = 38
total_to_pay = number_of_hours * HOURLY_RATE
```

逐行对照：

- `DECLARE <identifier> : <data type>`（p.8）在 Python 里**没有对应语句**：变量在第一次赋值时才出现。想把类型写出来，可以加类型标注 `number_of_hours: int = 38`，但 Python 不会检查它。
- `CONSTANT <identifier> = <value>`（p.8）用的是 **`=`**，而且值只能是字面量（不能是变量或表达式）。Python 没有真正的常量，约定用全大写名字表示「别改它」。
- 赋值 `<identifier> ← <value>`（p.9）↔ Python 的 `=`。伪代码没有 `+=`，Python 的 `count += 1` 在伪代码里写成 `Count ← Count + 1`。

### 4. 输入与输出（指南 p.15）

```pseudocode
DECLARE PlayerName : STRING
DECLARE Age : INTEGER
OUTPUT "Enter your name"
INPUT PlayerName
OUTPUT "Enter your age"
INPUT Age
OUTPUT "Hello ", PlayerName, ", next year you will be ", Age + 1
```

```python
player_name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {player_name}, next year you will be {age + 1}")
```

两处不对应：

1. **输入的类型。** 伪代码 `INPUT Age` 时 `Age` 已声明为 `INTEGER`，读进来就是整数。Python 的 `input()` **永远返回 `str`**，要算数必须先 `int(…)` 或 `float(…)`。
2. **输出的分隔。** `OUTPUT` 用逗号分隔多个值（p.15），**逗号本身不加任何空格**，空格要写在字符串里（`"Hello "`）。Python 的 `print(a, b)` 在每个逗号处**自动加一个空格**：

| 想输出 | 伪代码 | Python（推荐 f-string） | Python 写错的样子 |
|:--|:--|:--|:--|
| `You have 3 lives left` | `OUTPUT "You have ", Lives, " lives left"` | `print(f"You have {lives} lives left")` | `print("You have ", lives, " lives left")` → `You have  3  lives left`（两处双空格） |
| `3 7` | `OUTPUT Total, " ", Count` | `print(f"{total} {count}")` 或 `print(total, count)` | `print(total, " ", count)` → `3   7` |

提示语：伪代码用一条 `OUTPUT` 在 `INPUT` 之前给提示（`INPUT` 后面只跟变量名，p.15）；Python 把提示语写进 `input("…")` 的括号里。

### 5. 算术：`/`、`DIV`、`MOD`（指南 p.15；插页 p.4）

| 表达式 | 伪代码结果 | Python 写法 | Python 结果 |
|:--|:--|:--|:--|
| `17 / 5` | `3.4`（`/` 的结果总是 REAL） | `17 / 5` | `3.4` |
| `10 / 2` | `5.0`（仍是 REAL） | `10 / 2` | `5.0`，打印出来是 `5.0` 不是 `5` |
| `17 DIV 5` | `3`（商的整数部分） | `17 // 5` | `3` |
| `17 MOD 5` | `2`（余数） | `17 % 5` | `2` |
| `X * X` | 指南**没有乘方运算符** | `x ** 2` 或 `x * x` | |

- 乘除优先于加减；复杂表达式用括号写清楚顺序（p.15）。`(A + B + C) / 3` 的括号不能省。
- 负数要小心：指南把 `DIV` 描述为「小数点前的整数」，按字面 `-7 DIV 2` 是 `-3`；Python 的 `//` 是向下取整，`-7 // 2` 是 `-4`，`-7 % 2` 是 `1`。考题几乎只用非负数；真遇到负数时 `int(a / b)` 才与指南的描述一致。

### 6. 类型转换与字符串连接（指南 p.17；插页 p.2、p.4）

| 目的 | 伪代码 | Python |
|:--|:--|:--|
| 读入整数 / 实数 | `INPUT Age`（`Age` 是 `INTEGER`）/ `INPUT Price`（`REAL`） | `age = int(input())` / `price = float(input())` |
| 数字 → 字符串 | `NUM_TO_STR(87.5)` 返回 `"87.5"`（插页 p.2） | `str(87.5)` |
| 字符串 → 数字 | `STR_TO_NUM("23.45")` 返回 `23.45`（插页 p.2） | `float("23.45")`；整数用 `int("23")` |
| 实数 → 整数（截掉小数部分） | `INT(27.5415)` 返回 `27`（p.17） | `int(27.5415)` |
| 连接字符串 | `"Summer" & " " & "Pudding"`（p.17）；`&` 也可连 CHAR 与 STRING（插页 p.4） | `"Summer" + " " + "Pudding"` |
| 连接数字与字符串 | `"Total: " & NUM_TO_STR(Total)`，或干脆 `OUTPUT "Total: ", Total` | `"Total: " + str(total)`，或 `f"Total: {total}"` |

```pseudocode
DECLARE Name : STRING
DECLARE Row : INTEGER
DECLARE Code : STRING
OUTPUT "Enter your name"
INPUT Name
OUTPUT "Enter your row"
INPUT Row
Code ← Name & "-" & NUM_TO_STR(Row)
OUTPUT "Your code is ", Code
```

```python
name = input("Enter your name: ")
row = int(input("Enter your row: "))
code = name + "-" + str(row)
print(f"Your code is {code}")
```

Python 的 `+` 两边必须都是 `str`：`"Row " + 12` 直接报 `TypeError`。反过来，忘了 `int()` 时 `"12" * 100` **不会报错**，而是把 `"12"` 重复 100 次——这种错最难查。

### 7. `INT` 与 `RAND`（指南 p.17）

| 伪代码 | 含义 | Python |
|:--|:--|:--|
| `INT(27.5415)` | 返回整数部分 `27` | `int(27.5415)` |
| `RAND(87)` | 返回 0 到 87 之间的实数，不含 87 | `random.random() * 87`（先 `import random`） |
| `INT(RAND(6)) + 1` | 掷骰子：1–6 的整数 | `random.randint(1, 6)`（两端都包含） |

### 8. 练习模板里的「外壳」：模块头 ↔ `def`（指南 p.22–24，L04 细讲）

P2 的写代码题几乎都是「写出过程/函数 X」，所以从 L01 起练习模板就给你模块头。先只记住下面的对应关系：

```pseudocode
FUNCTION Average(Total : INTEGER, Count : INTEGER) RETURNS REAL
   RETURN Total / Count
ENDFUNCTION

PROCEDURE Greet()
   DECLARE Name : STRING
   OUTPUT "Enter your name"
   INPUT Name
   OUTPUT "Hello ", Name
ENDPROCEDURE
```

```python
def average(total: int, count: int) -> float:
    return total / count


def greet() -> None:
    name = input("Enter your name: ")
    print(f"Hello {name}")


if __name__ == "__main__":
    greet()
```

| 伪代码 | Python | 说明 |
|:--|:--|:--|
| `FUNCTION Average(Total : INTEGER, …) RETURNS REAL` | `def average(total: int, …) -> float:` | 参数「名 : 类型」↔「名: 类型标注」；`RETURNS` ↔ `->` |
| `RETURN Total / Count` | `return total / count` | 函数型练习：用 `return` 交答案，不要 `print` |
| `ENDFUNCTION` / `ENDPROCEDURE` | 没有结束关键字，缩进结束就是结束 | |
| `PROCEDURE Greet()` | `def greet() -> None:` | 输入输出型练习：在过程里 `input()` / `print()` |
| `CALL Greet()`（p.22） | `greet()` | Python 调用不写 `CALL` |

`if __name__ == "__main__":` 的意思是「直接运行这个文件时才执行下面的调用」。测试会 `import` 你的文件再自己调用函数，所以这行守卫不能删，你的代码也不要写在 `def` 外面。

## 常见坑

1. **`input()` 是字符串。** `"3" + "4"` 得 `"34"`；`"12" * 100` 得一长串 `1212…`。凡是要算数的输入，读进来立刻 `int()` / `float()`。
2. **`print` 的逗号加空格，`OUTPUT` 的逗号不加。** 从伪代码直译 `OUTPUT "Total: ", Total` 成 `print("Total: ", total)` 会多出一个空格。统一用 f-string。
3. **`/` 永远是实数。** `10 / 2` 是 `5.0`。要整除就用 `DIV` / `//`。
4. **优先级与括号。** `Mark1 + Mark2 + Mark3 / 3` 只除了最后一项。ECR P2 2024 p.10（9618_s24_22 Q2(a)）点名的常见错误就是「求平均时漏括号」。
5. **伪代码连接字符串用 `&`，不是 `+`。** ECR P2 2021 p.45 与 ECR P2 2024 p.19 都把「用 `+` 连接字符串」列为常见错误。Python 正好相反：只能用 `+`（或 f-string）。
6. **常量用 `=`，赋值用 `←`**（p.8、p.9）。`CONSTANT Count ← 3` 是错的。赋值方向是「右边算好放进左边」：写 `Flag ← GetStat()`，不写 `GetStat() → Flag`（ECR P2 2024 p.11 点名）。
7. **大小写。** 伪代码标识符不分大小写，Python 分：先写 `total = 0` 后写 `Total + 1` 会得到 `NameError`。
8. **别拿内置名或关键字当变量名。** Python 里 `input = …`、`sum = 0`、`str = "…"`、`max = …` 会让同名内置函数失效；伪代码里别用 `LENGTH` 这类关键字作标识符（ECR P2 2024 p.19 点名）。
9. **浮点误差与舍入。** `0.1 + 0.2` 是 `0.30000000000000004`；显示两位小数用 `f"{x:.2f}"`。`round(2.5)` 是 `2`（Python 用「银行家舍入」），不要拿 `round` 当四舍五入。
10. **`int("3.5")` 报 `ValueError`。** 含小数点的输入用 `float()`；确实要整数部分就 `int(float(s))`。
11. **实数字面量两边都要有数字**：写 `0.5`、`4.0`，不写 `.5`、`4.`（p.7）。
12. **提示语要单独 `OUTPUT`。** 教材 14.06 节（p.258）有 `INPUT "Enter Y or N: " Answer` 的写法，但 2027–29 指南的格式是 `INPUT <identifier>`（p.15），提示用前一行的 `OUTPUT`。ECR P2 2024 p.15 把「输入前没有提示」列为常见错误。

## 延伸阅读

- CS50P Lecture 0 “Functions, Variables” 讲义：<https://cs50.harvard.edu/python/notes/0/>——重点看 [Formatting Strings](https://cs50.harvard.edu/python/notes/0/#formatting-strings)、[Integers or int](https://cs50.harvard.edu/python/notes/0/#integers-or-int)、[Float Basics](https://cs50.harvard.edu/python/notes/0/#float-basics)、[More on Floats](https://cs50.harvard.edu/python/notes/0/#more-on-floats)、[Def](https://cs50.harvard.edu/python/notes/0/#def)、[Returning Values](https://cs50.harvard.edu/python/notes/0/#returning-values)。（CC BY-NC-SA 4.0）
- CS50P Problem Set 0 “Tip Calculator”：<https://cs50.harvard.edu/python/psets/0/tip/>（E03 的改编来源；CC BY-NC-SA 4.0）
- Think Python 3e（Allen B. Downey，CC BY-NC-SA 4.0）：第 1 章 [Arithmetic operators](https://allendowney.github.io/ThinkPython/chap01.html#arithmetic-operators)、[Values and types](https://allendowney.github.io/ThinkPython/chap01.html#values-and-types)；第 2 章 [Variables](https://allendowney.github.io/ThinkPython/chap02.html#variables)、[Variable names](https://allendowney.github.io/ThinkPython/chap02.html#variable-names)、[The print function](https://allendowney.github.io/ThinkPython/chap02.html#the-print-function)；第 5 章 [5.1 Integer division and modulus](https://allendowney.github.io/ThinkPython/chap05.html#integer-division-and-modulus)。
- 教材 Langfield & Duddell 2e：12.04–12.05 Variables / Assignments（p.184）、14.02 Programming basics（p.243）、14.03 Data types（p.248）、14.07 Built-in functions（p.260）。书中伪代码与 2027–29 指南不同时以指南为准。
- 官方：伪代码指南 §1–2、§5（p.5–9、p.15–17）；P2 插页函数表（`sources/pastpapers/9618_w25_in_21.pdf` p.2–4）。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-trace-basics/`](exercises/E01-trace-basics/spec.md) | 干跑 | 否 | 读伪代码：`/`、`DIV`、`MOD`、优先级、`OUTPUT` 分隔、`&` |
| [`exercises/E02-split-seconds/`](exercises/E02-split-seconds/spec.md) | 输入输出 | 是 | 秒数换算时分秒：`DIV` 与 `MOD` |
| [`exercises/E03-bill-split/`](exercises/E03-bill-split/spec.md) | 输入输出 | 是 | 常量、实数输入、两位小数输出 |
| [`exercises/E04-fix-average/`](exercises/E04-fix-average/spec.md) | 输入输出 | 是 | 找出并改正伪代码中的 4 处错误 |
| [`exercises/E05-ticket-code/`](exercises/E05-ticket-code/spec.md) | 输入输出 | 是 | 数字与字符串的转换和连接 |
