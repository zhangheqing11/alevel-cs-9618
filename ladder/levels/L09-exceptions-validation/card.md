# L09 · 异常处理、输入校验与 P4 工作方式

> 考纲 20.2（文件处理与异常处理）、12.3（错误类型、测试数据）（考纲 p.31、p.38）· 指南：**没有** TRY/EXCEPT（索引 p.30）；随机文件 §9.2（p.26–27，选学）· P4 考试形式（考纲 p.11、p.40）

## 本级目标

学完本级，你能：

1. 说出什么是异常（exception）、什么时候该用异常处理（考纲 20.2），并区分语法错误、逻辑错误、运行时错误（考纲 12.3）。
2. 用 Python 的 `try` / `except` / `else` / `finally` 处理类型转换失败、除以零、文件不存在等运行时错误。
3. 不用异常、只用插页函数和条件写出输入校验（P2 的写法）：范围、长度、格式、类型检查。
4. 按 P4 的方式写程序：标识符与文件名**照抄题目**（CamelCase），全局数组建成真实 list 并注释大小与类型，文件读写放进 `try`，按题目给的测试数据运行并保留完整的输入输出作为证据。

## 伪代码 ↔ Python 对照

### 1. 伪代码没有异常；P2 用条件做校验

2027–29 指南里没有 `TRY`、`EXCEPT` 关键字（索引 p.30）；考纲 20.2 只要求「write **program code** to use exception handling」（考纲 p.38）。所以：

- **P2（伪代码）**：用插页函数与条件先检查再转换，例如 `IF IS_NUM(Text) THEN Value ← STR_TO_NUM(Text)`（插页 p.2–3）。
- **P4（Python）**：可以「先试，失败了再处理」——`try: value = int(text)` / `except ValueError: …`。

```pseudocode
REPEAT
   OUTPUT "Enter a mark from 0 to 100"
   INPUT MarkText
   Valid ← FALSE
   IF IS_NUM(MarkText) THEN
      Mark ← STR_TO_NUM(MarkText)
      IF Mark >= 0 AND Mark <= 100 THEN
         Valid ← TRUE
      ENDIF
   ENDIF
   IF Valid = FALSE THEN
      OUTPUT "Invalid mark"
   ENDIF
UNTIL Valid = TRUE
```

```python
while True:
    mark_text = input("Enter a mark from 0 to 100: ")
    try:
        mark = int(mark_text)
        if 0 <= mark <= 100:
            break
    except ValueError:
        pass                      # not a whole number: fall through to the message
    print("Invalid mark")
```

注意 `IS_NUM("7.5")` 为 TRUE（插页 p.3：「represents a valid numeric value」），而 Python 的 `int("7.5")` 会抛 `ValueError`。要整数时，伪代码还要检查 `INT(Mark) = Mark`。

### 2. Python 的 `try` 语句

```python
try:
    value = int(text)            # code that might fail
except ValueError:
    print("Not a whole number")  # runs only if that exception happened
else:
    print("OK:", value)          # runs only if no exception happened
finally:
    print("Done")                # always runs
```

| 情况 | 抛出的异常 | 例 |
|:--|:--|:--|
| 字符串转数字失败 | `ValueError` | `int("abc")`、`int("7.5")`、`float("")` |
| 除以零 | `ZeroDivisionError` | `5 / 0`、`5 // 0`、`5 % 0` |
| 文件不存在 | `FileNotFoundError` | `open("Nope.txt")` |
| 下标越界 | `IndexError` | `[1, 2][5]` |
| 类型不对 | `TypeError` | `"Total: " + 5` |

- **只捕捉你预料到的异常**：写 `except ValueError:`，不要写不带类型的 `except:`——它会把你代码里的拼写错误也一起吞掉，测试时更难找原因。
- `try` 块里只放可能出错的那几行；校验失败后要么重新输入，要么给出明确的结果，不要让程序带着错误数据继续运行（ER s22 9618/41 Q1 p.36）。

### 3. 文件与异常

```python
def ReadScores(FileName: str) -> int:
    global NumberScores
    NumberScores = 0
    try:
        with open(FileName, "r") as File:          # opening and closing are both inside try
            for Line in File:
                ...
    except FileNotFoundError:
        print("File not found")
    return NumberScores
```

- 打开与关闭**都要在 `try` 里**；否则 `try` 失败后去关一个没打开的文件会再出错（ER s23 9618/41 Q3 p.39；ER s23 9618/42 Q3 p.43）。用 `with` 最省事：离开 `with` 块时文件自动关闭。
- 读文件时也要注意关闭的位置：不要在循环里关闭后又接着读（ER s22 9618/41 Q1 p.35；ECR P4 2024 p.7）。

### 4. 校验的种类（P2、P4 都考）

| 检查 | 伪代码（插页函数） | Python |
|:--|:--|:--|
| 存在（presence） | `Text <> ""` | `text != ""` |
| 长度（length） | `LENGTH(Name) = 3` | `len(name) == 3` |
| 类型（type） | `IS_NUM(Text)` | `try: int(text)` |
| 范围（range） | `Mark >= 0 AND Mark <= 100` | `0 <= mark <= 100` |
| 格式（format） | 逐字符 `MID` + 比较 | 逐字符比较（或 `isupper`/`isdigit`） |

- 「正好 3 个字符」是 `= 3`，不是 `<= 3`：ER s22 9618/41 Q1 p.36 点名，很多考生的检查让 2 个字符的名字也通过了。
- 几项数据要**分别**校验、分别提示（同一处点评）：一项无效时，不应把另一项有效的数据也一起拒掉。

### 5. P4 的工作方式

| 要求 | 怎么做 | 依据 |
|:--|:--|:--|
| 标识符照抄题目 | 题目写 `ReadScores()`、`ScoreArray`、`NumberScores`，Python 里就用这些名字（不改成 snake_case）；文件名、保存的程序名也照抄 | skill `references/programming.md` §8；测试按这些名字调用 |
| 全局变量与数组 | 在模块顶层建出来：`ScoreArray = [-1] * 20  # INTEGER, 20 elements`；函数里赋值前写 `global` | D10；ER s23 9618/41 Q3 p.39 |
| 属性与变量的类型 | Python 没有声明：用初值和注释写明类型（`NumberScores = 0  # INTEGER`） | ECR P4 2024 p.16 的考官范答写法 |
| 把伪代码算法译成 Python | 按语言做必要的调整（下标从 0 起、循环终点、BYREF），但**不改变算法的功能** | ER s22 9618/41 p.35 |
| 测试证据 | 用题目给的测试数据运行；截图要包含**全部输入和输出**，必要时分几张截；字要清楚（白底黑字） | ER s22 9618/41 p.35–36；ER s23 9618/41 p.38 |
| 每一问都要贴代码 | 把这一问用到的全部代码都贴进证据文档，宁多勿少 | ER s22 9618/41 Q1 p.36 |
| 主程序 | Python 里写在文件末尾；本阶梯放在 `if __name__ == "__main__":` 下，方便测试导入 | — |

### 6. 随机文件（选学，指南 p.26–27）

指南有 `OPENFILE … FOR RANDOM`、`SEEK`、`GETRECORD`、`PUTRECORD`，按记录号直接读写定长记录。考纲 20.2 提到 serial、sequential、random 三种文件，但 **P4 的源文件不含二进制文件**（考纲 p.40），本阶梯不设随机文件练习。想了解 Python 里的做法，可以查 `pickle` 模块与文件的 `seek()`。

## 常见坑

1. **不带类型的 `except:`**：把 `NameError`、`TypeError` 这些你自己的错误也吞掉了，程序「不报错但不对」。
2. **`try` 块包得太大**：把整个程序都放进去，出错时不知道是哪一行。
3. **只在 `try` 里打开、却在外面关闭**（ER s23 9618/41 Q3 p.39）。
4. **`isdigit()` 代替类型检查**：`" 72 "`、`"-5"` 的结果与 `int()` 不同；题目说「整数」时，用 `try: int(…)` 最可靠。
5. **校验条件写松了**：「正好 3 个字符」写成 `<= 3`（ER s22 9618/41 Q1 p.36）；范围的两端写成 `<`。
6. **伪代码里写 `TRY`**：指南没有这个结构；P2 用 `IS_NUM` 与条件。按 D2，混入编程语言语法的写法不给分。
7. **改了题目给的标识符**：Python 习惯写 `read_scores`，但 P4 题目写 `ReadScores` 就必须用 `ReadScores`。
8. **没用题目给的测试数据，或截图不全**（ER s22 9618/41 p.36；ER s23 9618/41 p.38）。
9. **全局数组只写注释、没有真的建出来**，或只建了空 list（D10；ER s23 9618/41 Q3 p.39）。
10. **函数里该返回的却打印**、**该用参数的却 `input()`**（L04 常见坑 2、3 在 P4 里同样扣分：ER s23 9618/41 p.38）。

## 延伸阅读

- CS50P Lecture 3 “Exceptions” 讲义：[Runtime Errors](https://cs50.harvard.edu/python/notes/3/#runtime-errors)、[try](https://cs50.harvard.edu/python/notes/3/#try)、[else](https://cs50.harvard.edu/python/notes/3/#else)、[Creating a Function to Get an Integer](https://cs50.harvard.edu/python/notes/3/#creating-a-function-to-get-an-integer)、[pass](https://cs50.harvard.edu/python/notes/3/#pass)。CS50P Problem Set 3 “Fuel Gauge”：<https://cs50.harvard.edu/python/psets/3/fuel/>（可选加练：同时处理 `ValueError` 与 `ZeroDivisionError` 并重新输入）。（CC BY-NC-SA 4.0）
- 教材 Langfield & Duddell 2e：26.02 File processing（p.448）、26.03 Exception handling（p.455）；15.05 Types of error（p.296）、15.07 Test strategy, test plans and test data（p.304）。
- 官方：考纲 20.2（p.38）、12.3（p.31）；考纲 p.40「Submission of Paper 4」（证据文档）。

## 练习

从本级起，练习按 P4 的习惯使用题目指定的 CamelCase 标识符（`meta.entry` 也是这些名字）。

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-convert-mark/`](exercises/E01-convert-mark/spec.md) | 函数 | 否 | `try`/`except ValueError` + 范围检查 |
| [`exercises/E02-input-validation/`](exercises/E02-input-validation/spec.md) | 函数（含输入） | 否 | 两项数据分别校验、反复输入、精确的长度与范围 |
| [`exercises/E03-read-scores/`](exercises/E03-read-scores/spec.md) | 函数（全局数组） | 否 | 文件不存在、坏数据行；P4 式全局数组 |
| [`exercises/E04-format-check/`](exercises/E04-format-check/spec.md) | 函数 | 是 | 不用异常的格式校验（P2 写法） |
| [`exercises/E05-main-program/`](exercises/E05-main-program/spec.md) | 脚本 | 否 | 完整的 P4 式程序：全局数组 + 读文件 + 主程序输出 |
