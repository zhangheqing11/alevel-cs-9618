# L05 · 字符串与插页内置函数（含日期函数）

> 考纲 11.1「Use built-in functions and library routines」（字符串函数考试一定会给，考纲 p.29）· 指南 §5.5（p.16–17）· 插页函数表（以 9618_w25_in_21 p.2–4 为代表）

## 本级目标

学完本级，你能：

1. 熟练使用插页的字符串函数 `LEFT RIGHT MID LENGTH TO_UPPER TO_LOWER NUM_TO_STR STR_TO_NUM IS_NUM ASC CHR`，并写出对应的 Python（切片、方法、`ord`/`chr`）。
2. 在 1 起（伪代码）与 0 起（Python）下标之间换算，不差一。
3. 写出逐字符处理字符串的标准循环：`FOR Index ← 1 TO LENGTH(S)` + `MID(S, Index, 1)`。
4. 用插页日期函数 `DAY MONTH YEAR DAYINDEX SETDATE TODAY`，并知道它们在 `datetime.date` 里的对应写法与差别。
5. 分清 P2 伪代码里**能用**的函数（只有插页里的）与 P4 Python 里能用的方法。

## 伪代码 ↔ Python 对照

### 1. 下标：1 起 vs 0 起

| 位置 | 伪代码（`S ← "Computer"`） | Python（`s = "Computer"`） |
|:--|:--|:--|
| 第一个字符 | `MID(S, 1, 1)` → `"C"` | `s[0]` |
| 第 i 个字符 | `MID(S, i, 1)` | `s[i - 1]` |
| 最后一个字符 | `MID(S, LENGTH(S), 1)` 或 `RIGHT(S, 1)` | `s[len(s) - 1]` 或 `s[-1]` |
| 长度 | `LENGTH(S)` → `8` | `len(s)` |

- **伪代码里字符串不是数组。** 不能写 `S[1]`；取一个字符只能用 `MID(S, i, 1)`（或 `LEFT`/`RIGHT`）。这是考官报告反复点名的错误（ER s22 9618/22 Q6 p.18、ER s23 9618/22 Q4 p.20、ER s25 9618/23 Q5 p.28、ECR P2 2024 p.19）。
- Python 的字符串**不可改**：`s[0] = "c"` 报 `TypeError`。要「改」就造一个新串：`s = "c" + s[1:]`。伪代码同理，用 `&` 拼出新串再赋值。

### 2. 插页字符串函数 ↔ Python（插页 p.2–3；指南 p.16–17）

| 插页函数（原样签名） | 例（插页原例） | Python | 注意 |
|:--|:--|:--|:--|
| `LEFT(ThisString : STRING, x : INTEGER) RETURNS STRING` | `LEFT("ABCDEFGH", 3)` → `"ABC"` | `s[:x]` | 指南里没有 LEFT，只在插页里 |
| `RIGHT(ThisString : STRING, x : INTEGER) RETURNS STRING` | `RIGHT("ABCDEFGH", 3)` → `"FGH"` | `s[len(s) - x:]` | `s[-x:]` 在 `x = 0` 时返回**整个串**（`s[-0:]` 就是 `s[0:]`） |
| `MID(ThisString : STRING, x : INTEGER, y : INTEGER) RETURNS STRING` | `MID("ABCDEFGH", 2, 3)` → `"BCD"` | `s[x - 1:x - 1 + y]` | 第三个参数是**长度**，不是结束位置 |
| `LENGTH(ThisString : STRING) RETURNS INTEGER` | `LENGTH("Happy Days")` → `10` | `len(s)` | 只用于字符串，**不能**用来求数组长度（ER w25 p.15） |
| `TO_UPPER(x : <datatype>) RETURNS <datatype>`（CHAR 或 STRING） | `TO_UPPER("Error 803")` → `"ERROR 803"` | `s.upper()` | 方法要加括号；指南 p.17 另有只收 CHAR 的 `UCASE`/`LCASE`，以当卷插页为准 |
| `TO_LOWER(x : <datatype>) RETURNS <datatype>` | `TO_LOWER("JIM 803")` → `"jim 803"` | `s.lower()` | |
| `NUM_TO_STR(x : <datatype1>) RETURNS <datatype2>` | `NUM_TO_STR(87.5)` → `"87.5"` | `str(x)` | |
| `STR_TO_NUM(x : <datatype1>) RETURNS <datatype2>` | `STR_TO_NUM("23.45")` → `23.45` | `int(s)` / `float(s)` | `int("23.45")` 报 `ValueError` |
| `IS_NUM(ThisString : <datatype>) RETURNS BOOLEAN` | `IS_NUM("-12.36")` → `TRUE` | 没有直接对应 | `"-12.36".isdigit()` 是 `False`；可靠写法是 `try: float(s)`（L09） |
| `ASC(ThisChar : CHAR) RETURNS INTEGER` | `ASC('A')` → `65` | `ord(ch)` | |
| `CHR(x : INTEGER) RETURNS CHAR` | `CHR(65)` → `'A'` | `chr(x)` | |

插页 p.2 还规定：长度为 1 的串既可看作 CHAR 也可看作 STRING；CHAR 可以赋给 STRING 或与之连接；长度大于 1 的 STRING 不能赋给 CHAR。

**出错方式不同。** 插页 p.2：函数调用格式不对、参数类型或取值不对都会报错——例如 `MID("ABC", 3, 5)` 超出了串尾。Python 切片**从不报越界错**：`"ABC"[2:7]` 安静地返回 `"C"`。所以 Python 测试通过，不代表你的伪代码参数在边界上也对，伪代码里要自己保证 `x + y - 1 <= LENGTH(S)`。

### 3. 逐字符处理：标准循环

```pseudocode
DECLARE Index : INTEGER
DECLARE Ch : CHAR
DECLARE Count : INTEGER
Count ← 0
FOR Index ← 1 TO LENGTH(Text)
   Ch ← MID(Text, Index, 1)
   IF Ch = ' ' THEN
      Count ← Count + 1
   ENDIF
NEXT Index
```

```python
count = 0
for index in range(1, len(text) + 1):     # mirrors the pseudocode exactly
    ch = text[index - 1]
    if ch == " ":
        count = count + 1

count = 0
for ch in text:                            # the usual Python way
    if ch == " ":
        count = count + 1
```

- Python 的 `for ch in text:` 最简洁，但**伪代码里没有这种写法**（ECR P2 2024 p.29 把 `FOR … IN …` 列为 Python 式错误；D2：P2 里混入编程语言语法，该得分点不给）。
- 造新串：`NewText ← NewText & Ch` ↔ `new_text = new_text + ch`；循环前先 `NewText ← ""`。
- 用条件循环逐字符扫描时（找到就停），条件里既要有标志，也要有「还没到串尾」：只判断标志的话，`MID` 可能被用超出串长的参数调用（ER s22 9618/22 Q8 p.19）。

### 4. 大小写与比较

- 比较字符串区分大小写（插页 p.4）。不区分大小写地比较：两边都先 `TO_UPPER`（ECR P2 2021 p.45：很多考生没有先统一大小写）。但题目要求区分大小写时，就**不要**转换（ER s23 9618/22 Q4 p.20 点名「违背要求先转了大小写」）。
- 判断字母：`Ch >= 'A' AND Ch <= 'Z'`（L02）；Python 可写 `"A" <= ch <= "Z"` 或 `ch.isupper()`（后者对非 ASCII 字母也为真）。
- 字母移位（凯撒密码）：`CHR((ASC(Ch) - ASC('A') + Shift) MOD 26 + ASC('A'))` ↔ `chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))`。

### 5. 数字与字符串

- 字符串比较按字符编码逐个比：`"10" < "9"` 为真。比数值大小前先 `STR_TO_NUM` / `int()`。
- `&` 只能连接字符串（及 CHAR）。`"Total: " & Count` 里的 `Count` 若是 INTEGER，必须先 `NUM_TO_STR(Count)`（ECR P2 2024 p.16：「cannot use & operator with an integer」；ER w25 p.16）。
- 补前导零（如月份 `"05"`）：`IF LENGTH(MM) = 1 THEN MM ← "0" & MM ENDIF` ↔ Python `f"{month:02d}"`。

### 6. 日期函数 ↔ `datetime.date`（插页 p.3）

日期格式默认 DD/MM/YYYY（插页 p.3）。Python 先 `from datetime import date`。

| 插页函数 | 例（插页原例） | Python | 注意 |
|:--|:--|:--|:--|
| `DAY(ThisDate : DATE) RETURNS INTEGER` | `DAY(04/10/2003)` → `4` | `d.day` | 属性，不加括号 |
| `MONTH(ThisDate : DATE) RETURNS INTEGER` | `MONTH(04/10/2003)` → `10` | `d.month` | |
| `YEAR(ThisDate : DATE) RETURNS INTEGER` | `YEAR(04/10/2003)` → `2003` | `d.year` | |
| `DAYINDEX(ThisDate : DATE) RETURNS INTEGER` | `DAYINDEX(09/05/2023)` → `3`（星期日 = 1，星期一 = 2 …） | `d.isoweekday() % 7 + 1` | Python 的 `isoweekday()` 是星期一 = 1 … 星期日 = 7，`weekday()` 是星期一 = 0 |
| `SETDATE(Day, Month, Year : INTEGER) RETURNS DATE` | `SETDATE(26, 10, 2003)` | `date(2003, 10, 26)` | **参数顺序相反**：Python 是 年、月、日 |
| `TODAY() RETURNS DATE` | | `date.today()` | 结果每天不同，测试里不用 |

### 7. P2 与 P4 的边界（D2）

- **P2 伪代码**：只能用插页里的函数与运算符。`LEN()`、`len()`、`.upper()`、`split`、`find`、切片 `S[1:3]` 都不给分（ECR P2 2024 p.27：`LEN()` 不是插页函数；ER w25 p.15：语言特有的函数或方法不得分）。要拆分、查找就自己写循环。
- **P4 Python**：可以用 `split`、`strip`、`find`、`in` 等，除非题目要求你写出算法（ECR P4 2021 p.22：题目要逐个检查元素，考生用了内置的 `in`，不符合要求）。

## 常见坑

1. **把字符串当数组**（见 §1 引用）：伪代码写 `S[i]`；Python 写 `s[i]` 但忘了减 1。
2. **`MID` 的第三个参数当成结束位置**：`MID(S, 2, 4)` 是从第 2 个起取 **4 个**字符，不是取到第 4 个。Python 对应写成 `s[1:5]`，常见错是写成 `s[1:4]` 或 `s[2:6]`。
3. **长度参数差一。** ECR P2 2024 p.27：用子串函数时「长度参数差一」很常见。连考官范答也中招——同一题的范答（p.26）用 `SpaceCount` 记下第一个非空格字符的位置，再写 `NewLine ← RIGHT(Line, LENGTH(Line) - SpaceCount - 1)`。代入 `"  IF X2 > 13 THEN"`（长 17，`SpaceCount = 3`）得 `RIGHT(Line, 13)`，即 `" X2 > 13 THEN"`，把 `IF` 也删掉了；应为 `LENGTH(Line) - SpaceCount + 1`。**每写一个长度表达式，代一个具体例子算一遍。**
4. **用 `LEFT` 取中间的一个字符**（ER s22 9618/22 Q6 p.18、ER s23 9618/22 Q4 p.20）。取第 i 个字符用 `MID(S, i, 1)`。
5. **调用了 `LEFT`/`RIGHT` 却没用返回值**（ER s22 9618/22 Q7 p.19）。函数不会改原串：要写 `S ← RIGHT(S, LENGTH(S) - 1)`。Python 同理：`s.upper()` 不改 `s`，要 `s = s.upper()`。
6. **`MID` 的第三个参数写成整个串的长度**（ER s23 9618/22 Q8 p.22）：从中间取到串尾，长度是 `LENGTH(S) - Start + 1`。
7. **`&` 连接整数**、**用 `+` 连接字符串**（ECR P2 2024 p.16、p.19；ER w25 p.16）。
8. **`s[-x:]` 实现 RIGHT**：`x = 0` 时得到整个串。用 `s[len(s) - x:]`。
9. **`isdigit()` 当成 `IS_NUM`**：`"-5".isdigit()`、`"3.5".isdigit()` 都是 `False`。
10. **`SETDATE` 的参数顺序**照搬到 `date(26, 10, 2003)`：Python 报 `ValueError`（26 年 10 月 2003 日不存在）。
11. **`DAYINDEX` 直接用 `isoweekday()`**：星期二得 2 而不是 3。
12. **逐字符扫描时条件顺序**：判空要写在取字符之前，如 ECR P2 2024 p.27 的写法 `WHILE Line <> "" AND LEFT(Line, 1) = Space`。Python 的 `and` 会短路（左边为假就不算右边），写反了会 `IndexError`；指南没有规定 `AND` 是否短路，所以伪代码里也按「先判空」的顺序写。

## 延伸阅读

- CS50P Lecture 0 讲义：[More on Strings](https://cs50.harvard.edu/python/notes/0/#more-on-strings)（`strip`、`title` 等方法）。CS50P Problem Set 2：[camelCase](https://cs50.harvard.edu/python/psets/2/camel/)、[Vanity Plates](https://cs50.harvard.edu/python/psets/2/plates/)（可选加练：都是逐字符检查）。（CC BY-NC-SA 4.0）
- Think Python 3e 第 8 章（CC BY-NC-SA 4.0）：[8.1 A string is a sequence](https://allendowney.github.io/ThinkPython/chap08.html#a-string-is-a-sequence)、[8.2 String slices](https://allendowney.github.io/ThinkPython/chap08.html#string-slices)、[8.3 Strings are immutable](https://allendowney.github.io/ThinkPython/chap08.html#strings-are-immutable)、[8.4 String comparison](https://allendowney.github.io/ThinkPython/chap08.html#string-comparison)、[8.5 String methods](https://allendowney.github.io/ThinkPython/chap08.html#string-methods)；第 7 章 [7.1 Loops and strings](https://allendowney.github.io/ThinkPython/chap07.html#loops-and-strings)。
- 教材 Langfield & Duddell 2e：14.07 Built-in functions（p.260）。书中函数表比当前插页旧，以插页为准。
- 官方：伪代码指南 §5.5（p.16–17）；P2 插页 `sources/pastpapers/9618_w25_in_21.pdf` p.2–4（考试时以当卷插页为准）。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-insert-library/`](exercises/E01-insert-library/spec.md) | 函数 | 否 | 用切片实现 `LEFT/RIGHT/MID/LENGTH`，以后翻译伪代码时直接用 |
| [`exercises/E02-trace-strings/`](exercises/E02-trace-strings/spec.md) | 干跑 | 否 | 读插页函数、负步长取字符、`ASC`/`CHR` |
| [`exercises/E03-letter-stats/`](exercises/E03-letter-stats/spec.md) | 函数 | 是 | 逐字符循环、CASE 与 OTHERWISE 里的判断、BYREF 交回三个计数 |
| [`exercises/E04-trim-spaces/`](exercises/E04-trim-spaces/spec.md) | 函数 | 是 | 去首尾空格：`LEFT`/`RIGHT`/`LENGTH` 的长度表达式 |
| [`exercises/E05-caesar-shift/`](exercises/E05-caesar-shift/spec.md) | 函数 | 是 | `ASC`/`CHR`/`MOD` 循环移位，保留大小写 |
| [`exercises/E06-date-functions/`](exercises/E06-date-functions/spec.md) | 函数 | 是 | 插页日期函数 ↔ `datetime.date`；补前导零 |
