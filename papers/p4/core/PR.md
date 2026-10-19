## PR　输入、字符串与计算：伪代码 ↔ Python 对照与模板 {#core-PR}

P4 上机只写 Python，但题目常用伪代码描述算法（“A pseudocode algorithm for … is shown”），要一句一句翻译。左列按 2027–29 伪代码指南书写（指南页码见各节标题），右列是考场 Python 写法。英文列带 ⟦⟧ 的是该题 MS 原文。

### 1. 输入与输出（指南 §5.1，p.15）

| 伪代码 | Python | 不对应之处 / 常见失分 |
|:--|:--|:--|
| `INPUT Name` | `Name = input("Enter name: ")` | 提示语写进括号；练习的自动测试按这个约定（D13） |
| `INPUT Score`（INTEGER） | `Score = int(input("Enter score: "))` | 不转换就和数字比较会报 `TypeError` |
| `INPUT Price`（REAL） | `Price = float(input("Enter price: "))` | |
| `OUTPUT "You have ", Lives, " lives left"` | `print("You have", Lives, "lives left")` | `print` 在各项之间自动加一个空格；不想要空格用 `sep=""` 或 f-string |
| `OUTPUT Total` | `print(Total)` | 函数里要“返回”时不能用 `print` 代替 `return` |

### 2. 运算与类型转换（指南 §5.2–5.6，p.15–17）

| 伪代码 | Python | 例 |
|:--|:--|:--|
| `A / B` | `A / B` | `7 / 2` → `3.5`（总是小数） |
| `A DIV B` | `A // B` | `7 // 2` → `3` |
| `A MOD B`（题目也写 `MODULUS`） | `A % B` | `7 % 2` → `1` |
| `INT(X)` | `int(X)` | `int(27.54)` → `27`；正数即向下取整 |
| `INT(RAND(6)) + 1` | `random.randint(1, 6)` | `randint` 两端都包含；文件头要 `import random` |
| `=`、`<>` | `==`、`!=` | |
| `AND`、`OR`、`NOT` | `and`、`or`、`not` | |
| `NUM_TO_STR(X)`、`STR_TO_NUM(S)`（插页 / 题目给出时） | `str(X)`、`int(S)` / `float(S)` | |

**计算类的得分句**：「Modulus calculation」⟦9618_w23_42:2(a)(i)⟧；「multiplication by 1 and 3 alternately, adding to total, dividing by 10, rounding down/cast int」⟦9618_s24_41:3(d)(i)⟧——“rounding down”用 `int()` 或 `//` 都可以。

### 3. 字符串（指南 §5.5，p.16–17；考试时题目会给出所用的字符串函数）

| 伪代码 | Python | 注意 |
|:--|:--|:--|
| `LENGTH(S)` | `len(S)` | |
| `MID(S, X, Y)`（指南：从第 X 个字符起取 Y 个，1 起） | `S[X-1 : X-1+Y]` | `MID("ABCDEFGH", 2, 3)` → `"BCD"` |
| `MID(S, X, Y)`（题目写明 position 0 是第一个字符，如 ⟦9618_w23_41:1(a)(i)⟧） | `S[X : X+Y]` | 以题目的说明为准 |
| `RIGHT(S, X)` | `S[len(S)-X:]` | `RIGHT("ABCDEFGH", 3)` → `"FGH"` |
| `LCASE(C)`、`UCASE(C)` | `C.lower()`、`C.upper()` | 指南的参数是一个字符 |
| `S1 & S2` | `S1 + S2` | 数字要先 `str()` |
| `ASC(C)`、`CHR(N)`（题目给出时） | `ord(C)`、`chr(N)` | |
| 逐字符：`FOR I ← 1 TO LENGTH(S)` … `MID(S, I, 1)` | `for I in range(len(S)):` … `S[I]` | 下标从 0 到 `len(S) - 1` |

**字符串类的得分句**：「Calculating length of parameter string」⟦9618_w23_41:1(a)(i)⟧；「Accessing the remainder of the string」⟦9618_w23_41:1(a)(i)⟧；「concatenate current character to a string until ';' is found」⟦9618_w25_43:3(b)(ii)⟧。

### 4. 选择（指南 §6，p.18–19）

| 伪代码 | Python |
|:--|:--|
| `IF X > 0 THEN` … `ELSE` … `ENDIF` | `if X > 0:` … `else:` …（缩进代替 `ENDIF`） |
| `ELSE` 里嵌 `IF` | `elif` |
| `CASE OF Move` / `'A' : X ← X - 1` / `OTHERWISE : …` / `ENDCASE` | `if Move == "A":` / `elif …` / `else:` |
| 范围子句 `1 TO 5 : …` | `if Risk >= 1 and Risk <= 5:` |

### 5. 循环（指南 §7，p.20–21）

| 伪代码 | Python | 坑 |
|:--|:--|:--|
| `FOR I ← 1 TO 10` … `NEXT I` | `for I in range(1, 11):` | `range` 不含终点 |
| `FOR X ← 0 TO LengthString - 1` | `for X in range(0, LengthString):` | 终点 + 1 |
| `FOR I ← 10 TO 1 STEP -1` | `for I in range(10, 0, -1):` | |
| `WHILE Number <> 0` … `ENDWHILE` | `while Number != 0:` | |
| `REPEAT` … `UNTIL Valid = TRUE` | 先做一次再 `while not Valid:`；或 `while True:` … `if Valid: break` | REPEAT 至少执行一次；条件是“停”的条件，Python `while` 写“继续”的条件 |

### 6. 输入校验模板（PR-01）

```pseudocode
REPEAT
   OUTPUT "How many numbers will you enter (1 to 20)?"
   INPUT Quantity
UNTIL Quantity >= 1 AND Quantity <= 20
```

```python
Quantity = int(input("How many numbers will you enter (1 to 20)? "))
while Quantity < 1 or Quantity > 20:                  # NOT (stop condition)
    Quantity = int(input("Must be between 1 and 20. Enter again: "))
print("Accepted", Quantity)
```

校验的得分句：「validating between 1 and 20 inclusive」⟦9618_s24_41:1(b)⟧；「Taking each risk as input until it is between 1 and 5 (inclusive)」⟦9618_w24_41:2(c)(ii)⟧。两项数据各写一个循环。

### 7. 考场上的一个完整程序长什么样

P4 每道大题都是一个程序文件（题目让你 Save your program as Question1_J24 之类）。各小问往同一个文件里加：

```python
import random                     # only if the question needs it

# ---- global variables / arrays (declare = create; comment type and size) ----
DataStored = [0] * 20             # INTEGER, 20 elements
NumberItems = 0                   # INTEGER


# ---- subroutines: one per part of the question ----
def Initialise():                 # procedure (no return value)
    global NumberItems            # needed only when assigning to a global
    NumberItems = 0


def Total():                      # function (returns a value)
    Sum = 0
    for X in range(NumberItems):
        Sum = Sum + DataStored[X]
    return Sum


# ---- main program ----
if __name__ == "__main__":
    Initialise()
    print("Total:", Total())
```

- 主程序写在 `if __name__ == "__main__":` 下面：练习的测试导入你的文件时不会运行主程序。MS 范例常把主程序写在顶层；主程序的得分点写的是调用什么、输出什么，没有对入口写法的要求。
- 子程序里**给**全局变量赋值要先写 `global`；只读不写可以不写（MS 范例常常照样写上 `global`）。
- 每个小问的代码贴进证据文档对应的格；后面的小问改了前面的代码时（Amend …），贴改过的版本。

### 8. 常见失分对照

| 失分 | 例 | 改成 |
|:--|:--|:--|
| 没转类型 | `Score = input()` 后 `Score > 100` | `int(input())` |
| 提示与输入分开写 | `print("Enter")`、`input()` | `input("Enter: ")` |
| 校验只做一半 | 名字 `len(Name) <= 3` | `len(Name) != 3` 就重输 |
| 两项绑在一起校验 | 一个 `while` 同时检查名字和分数 | 一项一个循环 |
| 函数里 `print` 代替 `return` | `print(Total)` | `return Total`，主程序再 `print` |
| `range` 终点差一 | `range(0, Length - 1)` 对应 `FOR X ← 0 TO Length - 1` | `range(0, Length)` |
| 用 `/` 当整除 | `Mid = (Low + High) / 2` | `//` |
| 抄 MS 范例的笔误 | `score = -1` 后用 `Score`（⟦9618_s22_41:1(e)(i)⟧ MS p.10） | 名字前后一致 |
