# L02 · 选择：IF / CASE ↔ if/elif、match

> 考纲 11.1（逻辑运算）、11.2（IF、嵌套 IF、CASE）、12.3（测试数据）（考纲 p.29、p.31）· 指南 §5.3–5.4（p.16）、§6（p.18–19）· 插页比较运算说明（9618_w25_in_21 p.4）

## 本级目标

学完本级，你能：

1. 写对比较与逻辑表达式：`= <> AND OR NOT` ↔ `== != and or not`，复合条件两边都写完整。
2. 用 `IF … THEN … ELSE … ENDIF` 与嵌套 IF 写多分支，并译成 Python 的 `if/elif/else`。
3. 用 `CASE OF … OTHERWISE … ENDCASE`（含 `TO` 范围子句）写多分支，并译成 `if/elif` 或 `match`。
4. 判断一段 IF 能不能改写成 CASE，说出理由。
5. 为一个条件选出边界测试值（刚好在边界上、边界两侧）。

## 伪代码 ↔ Python 对照

### 1. 比较运算（指南 p.16；插页 p.4）

| 含义 | 伪代码 | Python |
|:--|:--|:--|
| 等于 | `=` | `==` |
| 不等于 | `<>` | `!=` |
| 大于 / 小于 | `>` / `<` | `>` / `<` |
| 大于等于 / 小于等于 | `>=` / `<=` | `>=` / `<=` |

- 结果总是 `BOOLEAN`（p.16）。
- 字符与字符串的比较**区分大小写**：`"Program" = "program"` 为 `FALSE`（插页 p.4）。Python 同样区分：`"Program" == "program"` 是 `False`。
- 字符按字符编码比大小：`'A' < 'B'`，所有大写字母都小于小写字母（`'Z'` < `'a'`）。Python 相同。

### 2. 逻辑运算（指南 p.16）

```pseudocode
IF Mark >= 66 AND Mark <= 173 THEN
   OUTPUT "In range"
ENDIF
IF NOT (Answer = 'Y' OR Answer = 'y') THEN
   OUTPUT "Cancelled"
ENDIF
```

```python
if mark >= 66 and mark <= 173:      # Python-only shortcut: if 66 <= mark <= 173:
    print("In range")
if not (answer == "Y" or answer == "y"):
    print("Cancelled")
```

- 复合条件的**每一半都必须是完整的比较**：`Mark >= 66 AND Mark <= 173`。
- Python 允许链式比较 `66 <= mark <= 173`；**伪代码不允许**，P2 里必须写成两个比较用 `AND` 连起来。
- 复杂表达式加括号写清顺序（p.16）。
- BOOLEAN 变量可以直接当条件：`IF Found THEN` 或 `IF Found = TRUE THEN`；Python 写 `if found:`。

### 3. `IF … THEN … ELSE … ENDIF`（指南 p.18）

指南的嵌套 IF 例子（p.18）与逐行翻译：

```pseudocode
IF ChallengerScore > ChampionScore THEN
   IF ChallengerScore > HighestScore THEN
      OUTPUT ChallengerName, " is champion and highest scorer"
   ELSE
      OUTPUT ChallengerName, " is the new champion"
   ENDIF
ELSE
   OUTPUT ChampionName, " is still the champion"
   IF ChampionScore > HighestScore THEN
      OUTPUT ChampionName, " is also the highest scorer"
   ENDIF
ENDIF
```

```python
if challenger_score > champion_score:
    if challenger_score > highest_score:
        print(f"{challenger_name} is champion and highest scorer")
    else:
        print(f"{challenger_name} is the new champion")
else:
    print(f"{champion_name} is still the champion")
    if champion_score > highest_score:
        print(f"{champion_name} is also the highest scorer")
```

| 伪代码 | Python | 说明 |
|:--|:--|:--|
| `IF <condition> THEN` | `if <condition>:` | `THEN` ↔ 冒号 |
| `ELSE` | `else:` | `else` 要和对应的 `if` 对齐 |
| `ENDIF` | （没有） | 每个 IF 都要有自己的 `ENDIF`；Python 靠缩进结束 |

### 4. 多分支：嵌套 IF ↔ `elif`（指南 p.18）

指南**没有 `ELSEIF` 关键字**。三个以上分支时，在 `ELSE` 里再嵌一个 `IF`（或改用 CASE，见 §5）。Python 用 `elif` 把这种嵌套「压平」：

```pseudocode
IF Mark >= 80 THEN
   Grade ← "A"
ELSE
   IF Mark >= 60 THEN
      Grade ← "B"
   ELSE
      Grade ← "C"
   ENDIF
ENDIF
```

```python
if mark >= 80:
    grade = "A"
elif mark >= 60:
    grade = "B"
else:
    grade = "C"
```

- 伪代码里每层嵌套都要有自己的 `ENDIF`：两层嵌套就是两个 `ENDIF`。
- 条件按顺序检查，第一个成立的分支执行后整个结构结束。所以「`>= 80`」必须写在「`>= 60`」前面。
- 2024 年 ECR P2 的考官范答（p.14–15）里出现过 `ELSIF`；2027–29 指南没有这个关键字。本阶梯一律用指南写法；P2 批改时 `ELSIF` 能否得分只看该题 MS。

### 5. `CASE OF` ↔ `if/elif` 或 `match`（指南 p.19）

指南的例子（p.19）：

```pseudocode
INPUT Move
CASE OF Move
   'W' : Position ← Position - 10
   'S' : Position ← Position + 10
   'A' : Position ← Position - 1
   'D' : Position ← Position + 1
   OTHERWISE : CALL Beep
ENDCASE
```

两种 Python 写法都可以：

```python
move = input()
if move == "W":
    position = position - 10
elif move == "S":
    position = position + 10
elif move == "A":
    position = position - 1
elif move == "D":
    position = position + 1
else:
    beep()
```

```python
move = input()
match move:
    case "W":
        position = position - 10
    case "S":
        position = position + 10
    case "A":
        position = position - 1
    case "D":
        position = position + 1
    case _:
        beep()
```

**范围子句**：`<value1> TO <value2> :`（p.19）。一个子句里要写多条语句时，值单独占一行、语句缩进写在下面（p.19 的格式）：

```pseudocode
CASE OF Mark
   80 TO 100 : Grade ← "A"
   60 TO 79 :
               Grade ← "B"
               OUTPUT "Good"
   OTHERWISE : Grade ← "C"
ENDCASE
```

```python
if 80 <= mark <= 100:
    grade = "A"
elif 60 <= mark <= 79:
    grade = "B"
    print("Good")
else:
    grade = "C"
```

```python
match mark:
    case m if 80 <= m <= 100:
        grade = "A"
    case m if 60 <= m <= 79:
        grade = "B"
        print("Good")
    case _:
        grade = "C"
```

| 伪代码 | `if/elif` | `match`（Python 3.10+） |
|:--|:--|:--|
| `CASE OF Move` | （每个分支都写 `move == …`） | `match move:` |
| `'W' : …` | `if move == "W":` | `case "W":` |
| `80 TO 100 : …` | `elif 80 <= mark <= 100:` | `case m if 80 <= m <= 100:`（守卫） |
| `OTHERWISE : …` | `else:` | `case _:` |
| `ENDCASE` | （没有） | （没有） |

- CASE 的子句**按顺序检查**，第一个匹配的执行后整个 CASE 结束，后面的不再检查（p.19）；Python 的 `elif` 链与 `match` 也一样，不会「贯穿」。
- `OTHERWISE` 如果有，必须是最后一个子句（p.19）。
- 指南的 CASE 是「根据**一个变量**的值」选分支（p.19）。条件涉及两个变量、或不是「等于某值 / 在某范围」时，只能用 IF——这就是「哪些 IF 不能改写成 CASE」的判断依据（SoW Unit 11 p.35 的互转活动）。
- 指南的子句是「一个值」或「一个 `TO` 范围」。几个不相邻的值要么分开写几个子句，要么用 IF + `OR`；Python 的 `match` 可以写 `case "F" | "U":`。

### 6. 返回 BOOLEAN 与 STRING 的函数（指南 p.23–24）

```pseudocode
FUNCTION IsAdult(Age : INTEGER) RETURNS BOOLEAN
   IF Age >= 18 THEN
      RETURN TRUE
   ELSE
      RETURN FALSE
   ENDIF
ENDFUNCTION
```

```python
def is_adult(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False
```

更简洁的写法是直接返回条件本身：伪代码 `RETURN Age >= 18`，Python `return age >= 18`。注意 Python 的布尔值是 `True` / `False`（首字母大写），不是字符串 `"TRUE"`。

## 常见坑

1. **`=` 与 `==`。** 伪代码比较用 `=`；Python 比较用 `==`，`if x = 5:` 是语法错误。反过来，伪代码的条件里永远不出现 `←`：ECR P2 2021 p.26 的考官点评指出 `UNTIL RNum ← 100` 里的箭头应是等号。
2. **`<>` 在 Python 里不存在**，写 `!=`。
3. **复合条件写一半。** `IF RNum >= 66 AND <= 173` 不可接受（ECR P2 2021 p.27 点名）；Python 里同样是语法错误。Python 的 `66 <= rnum <= 173` 只能用在 Python 里。
4. **`or` 的经典 Python 陷阱。** `if answer == "y" or "Y":` **永远成立**（非空字符串 `"Y"` 本身为真）。要写 `answer == "y" or answer == "Y"`，或 `answer in ("y", "Y")`。
5. **边界用错 `>` / `>=`。** 「80 分及以上为 A」是 `>= 80`。测试时一定要试边界上的值（80）和两侧（79、81）——考纲 12.3 要求会选 normal / abnormal / extreme(boundary) 测试数据（考纲 p.31）。
6. **分支顺序。** `elif` 链里先写宽条件（`>= 40`）会把后面的窄条件（`>= 80`）吃掉。从最严格的条件写起，或者每个分支写成完整的范围。
7. **漏写或交错的 `ENDIF`。** ECR P2 2024 p.11 与 p.15 都点名「结构没有结束关键字」「交错而不是嵌套」。写完数一数：几个 `IF` 就几个 `ENDIF`。Python 里对应的错误是缩进对错层。
8. **大小写敏感的比较。** 用户输入 `y` 而你只比较 `'Y'`，就会走错分支。ECR P2 2021 p.45 指出很多考生比较字符串前没有统一大小写；L05 学 `TO_UPPER` / `.upper()` 后再解决。
9. **`TRUE` / `True`。** Python 写 `true` 会得到 `NameError`；也不要返回字符串 `"TRUE"`——它不是布尔值。
10. **`OTHERWISE` 接住了不该接的。** ECR P2 2021 p.32：考生用 `OTHERWISE` 统计「其他字符」，结果把非字母也算了进去。`OTHERWISE` 是「以上都不是」，需要时在里面再加一个判断。
11. **`match` 的名字陷阱。** `case PASS_MARK:` 不是「等于常量 PASS_MARK」，而是把值**绑定**到一个叫 `PASS_MARK` 的新名字上（永远匹配）。比较常量请用字面量或守卫：`case m if m == PASS_MARK:`。
12. **实数不要用 `=` / `==` 比较。** `0.1 + 0.2 == 0.3` 是 `False`。比较实数用 `>=`、`<=` 范围，或比较差的绝对值。

## 延伸阅读

- CS50P Lecture 1 “Conditionals” 讲义：<https://cs50.harvard.edu/python/notes/1/>——[if Statements](https://cs50.harvard.edu/python/notes/1/#if-statements)、[Control Flow, elif, and else](https://cs50.harvard.edu/python/notes/1/#control-flow-elif-and-else)、[or](https://cs50.harvard.edu/python/notes/1/#or)、[and](https://cs50.harvard.edu/python/notes/1/#and)、[Modulo](https://cs50.harvard.edu/python/notes/1/#modulo)、[match](https://cs50.harvard.edu/python/notes/1/#match)。（CC BY-NC-SA 4.0）
- CS50P Problem Set 1 “Math Interpreter”：<https://cs50.harvard.edu/python/psets/1/interpreter/>（E03 的改编来源）；可选加练 “Meal Time”：<https://cs50.harvard.edu/python/psets/1/meal/>。（CC BY-NC-SA 4.0）
- Think Python 3e 第 5 章（CC BY-NC-SA 4.0）：[5.2 Boolean Expressions](https://allendowney.github.io/ThinkPython/chap05.html#boolean-expressions)、[5.3 Logical operators](https://allendowney.github.io/ThinkPython/chap05.html#logical-operators)、[5.4 if statements](https://allendowney.github.io/ThinkPython/chap05.html#if-statements)、[5.5 The else clause](https://allendowney.github.io/ThinkPython/chap05.html#the-else-clause)、[5.6 Chained conditionals](https://allendowney.github.io/ThinkPython/chap05.html#chained-conditionals)、[5.7 Nested Conditionals](https://allendowney.github.io/ThinkPython/chap05.html#nested-conditionals)；第 6 章 [6.5 Boolean functions](https://allendowney.github.io/ThinkPython/chap06.html#boolean-functions)。
- 教材 Langfield & Duddell 2e：12.06 Logic statements（p.188）、14.04 Boolean expressions（p.249）、14.05 Selection（p.250）。注意：书写于 2019 年，说「Python 没有 CASE 语句」；Python 3.10 起有 `match`。
- 官方：伪代码指南 §5.3–5.4、§6（p.16、p.18–19）；SoW Unit 11（p.35，IF 与 CASE 互转）。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-grade-bands/`](exercises/E01-grade-bands/spec.md) | 函数 | 是 | CASE 范围子句、OTHERWISE、边界值 |
| [`exercises/E02-leap-year/`](exercises/E02-leap-year/spec.md) | 函数 | 是 | 复合条件、嵌套 IF、返回 BOOLEAN |
| [`exercises/E03-calculator/`](exercises/E03-calculator/spec.md) | 输入输出 | 是 | 按字符 CASE、CASE 里嵌 IF、除零 |
| [`exercises/E04-char-type/`](exercises/E04-char-type/spec.md) | 函数 | 是 | 字符范围比较、`AND` |
| [`exercises/E05-trace-postage/`](exercises/E05-trace-postage/spec.md) | 干跑 | 否 | 读嵌套 IF 与 `DIV`；判断能否改写成 CASE |
