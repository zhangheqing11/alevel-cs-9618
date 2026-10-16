# L07 · 文本文件：OPENFILE / READFILE / EOF / WRITEFILE / CLOSEFILE ↔ open / with

> 考纲 10.3（为什么需要文件；读写一行或多行的文本文件）、20.2（文件打开模式与关闭；A2 再深入）（考纲 p.28、p.38）· 指南 §9.1（p.25–26）· 插页 `EOF`（9618_w25_in_21 p.4）

## 本级目标

学完本级，你能：

1. 按指南写出文本文件的打开（`READ` / `WRITE` / `APPEND`）、逐行读到文件尾、写一行、关闭；并说出三种模式的区别。
2. 把 `WHILE NOT EOF(…)` + `READFILE` 正确译成 Python，处理好行尾的 `"\n"`。
3. 读文件到数组、处理后写到另一个文件；边读边统计。
4. 分清伪代码里「文件名就是文件标识」与 Python 里「文件对象」的区别；用 `with` 保证文件关闭。
5. 只做**文本**文件：P2 的范围是按顺序访问的简单文本文件（ECR P2 2024 p.29），P4 的源文件也不含二进制文件（考纲 p.40）。

## 伪代码 ↔ Python 对照

### 1. 打开、读、写、关（指南 p.25）

| 伪代码 | Python | 说明 |
|:--|:--|:--|
| `OPENFILE "Data.txt" FOR READ` | `file = open("Data.txt", "r")` | 文件标识可以是字符串字面量，也可以是存着文件名的 STRING 变量（p.25） |
| `OPENFILE FileName FOR WRITE` | `file = open(file_name, "w")` | **新建**文件；原有内容全部丢失（p.25） |
| `OPENFILE "Log.txt" FOR APPEND` | `file = open("Log.txt", "a")` | 写在原有内容之后（p.25） |
| `READFILE "Data.txt", LineOfText` | `line_of_text = file.readline().rstrip("\n")` | `READFILE` 读出下一行，赋给 STRING 变量（p.25）；Python 读出的行**带着** `"\n"` |
| `EOF("Data.txt")` | 没有直接对应 | 没有更多行可读（或空文件）时为 TRUE（p.25）；文件不是以 READ 打开时报错（插页 p.4） |
| `WRITEFILE "Out.txt", LineOfText` | `file.write(line_of_text + "\n")` | `WRITEFILE` 写一行；Python 的 `write` 不会自动换行 |
| `CLOSEFILE "Data.txt"` | `file.close()`，或用 `with` 自动关闭 | 不再需要时就关闭（p.25） |

同一时刻一个文件只用一种模式打开（p.25）。要先读再追加，就先 `CLOSEFILE`，再用新模式 `OPENFILE`（ER s25 9618/21 Q7 p.16 的题目正是这样要求的）。

**文件名 vs 文件对象。** 伪代码里，打开以后仍然用**文件名**指代这个文件：`READFILE "Data.txt", Line`、`CLOSEFILE "Data.txt"`。Python 里 `open` 返回一个**文件对象**，之后的读写关都通过它：`file.readline()`、`file.close()`。

### 2. 读到文件尾：`WHILE NOT EOF` ↔ Python 的三种写法

指南的例子（p.26）：把 `FileA.txt` 的每一行复制到 `FileB.txt`，空行换成一行短横线。

```pseudocode
DECLARE LineOfText : STRING
OPENFILE "FileA.txt" FOR READ
OPENFILE "FileB.txt" FOR WRITE
WHILE NOT EOF("FileA.txt")
   READFILE "FileA.txt", LineOfText
   IF LineOfText = "" THEN
      WRITEFILE "FileB.txt", " ----------------------------"
   ELSE
      WRITEFILE "FileB.txt", LineOfText
   ENDIF
ENDWHILE
CLOSEFILE "FileA.txt"
CLOSEFILE "FileB.txt"
```

```python
with open("FileA.txt", "r") as file_a, open("FileB.txt", "w") as file_b:
    for line in file_a:                        # one line per iteration, until the end of the file
        line_of_text = line.rstrip("\n")       # READFILE gives the line without its newline
        if line_of_text == "":
            file_b.write(" ----------------------------\n")
        else:
            file_b.write(line_of_text + "\n")
# both files are closed here
```

| Python 写法 | 说明 |
|:--|:--|
| `for line in file:` | 最常用；每次一行，读完自动结束 |
| `while True:` / `line = file.readline()` / `if line == "": break` | 最接近 `WHILE NOT EOF` + `READFILE`：`readline()` 只在文件尾返回 `""`，空行返回的是 `"\n"` |
| `lines = file.read().splitlines()` | 一次读进全部行（已去掉换行），再按 list 处理 |

- 去掉换行用 `rstrip("\n")`；`strip()` 还会去掉行首尾的空格，题目要保留空格时别用它。
- 读数字：`STR_TO_NUM(LineOfText)` ↔ `int(line)` / `float(line)`。`int("85\n")` 能成功（`int` 会忽略首尾空白），但比较字符串时 `"85\n" == "85"` 为假。

### 3. 读进数组、写出数组

```pseudocode
// global: WordArray : ARRAY[1:100] OF STRING; NumberWords : INTEGER
PROCEDURE ReadWords(FileName : STRING)
   DECLARE LineOfText : STRING
   NumberWords ← 0
   OPENFILE FileName FOR READ
   WHILE NOT EOF(FileName)
      READFILE FileName, LineOfText
      NumberWords ← NumberWords + 1
      WordArray[NumberWords] ← LineOfText
   ENDWHILE
   CLOSEFILE FileName
ENDPROCEDURE
```

```python
word_array = [""] * 100   # ARRAY[1:100] OF STRING -> indexes 0 to 99
number_words = 0


def read_words(file_name: str) -> None:
    global number_words
    number_words = 0
    with open(file_name, "r") as file:
        for line in file:
            word_array[number_words] = line.rstrip("\n")
            number_words = number_words + 1
```

注意 `FileName` 是参数（变量），所以 `OPENFILE FileName FOR READ` **不加引号**；只有文件名写成字面量时才加引号（ECR P2 2024 p.29：考生给参数名加 `.txt` 后缀、使用时又给它加上引号）。

### 4. P4：文件与异常（L09 细讲）

P4 读源文件通常写在 `try` 里，文件打不开时给出提示（ECR P4 2024 p.5 的考官范答就是这样）。用异常处理时，打开**和关闭**都要放在 `try` 里，否则 `try` 失败后去关一个没打开的文件会再出错（ER s23 9618/41 Q3 p.39）。本级练习的文件都存在，先不写 `try`。

## 常见坑

1. **`EOF()` 漏了参数**、写成 `EOF()` 或 `EOF` 不带括号（ECR P2 2024 p.29；ER s23 9618/22 Q8 p.23；ER s23 9618/23 Q8 p.26）。
2. **用计数循环读文件**：`FOR Index ← 1 TO EOF(Filename)`、`FOR n ← 1 TO LENGTH("Stock.txt")`（ER s22 9618/21 Q8 p.11 等；ER s23 9618/22 Q8 p.23；ECR P2 2024 p.29）。文件有几行事先不知道，要用 `WHILE NOT EOF(…)`。
3. **Python 式写法** `FOR Line IN InputFile`（ECR P2 2024 p.29）；D2：P2 里混入编程语言语法，该得分点不给。
4. **漏写 `CLOSEFILE`，或 `CLOSEFILE` 后面漏了文件名**（ER s22 9618/22 Q4 p.17；ER s24 9618/22 Q8 p.21、9618/23 Q8 p.28；ER s25 9618/22 p.17、p.21）。
5. **模式用错**：要往已有文件追加却用了 `WRITE`，把原有内容清掉（ECR P2 2024 p.29）；或者对 `WRITE` 模式打开的文件用 `EOF()` 做循环条件（ER s23 9618/22 Q8 p.22）。
6. **字面量文件名漏了引号**（ER s23 9618/22 Q8 p.22；ER s25 9618/22 Q5 p.21；ER w22 9618/21 Q8 p.18）；反过来，**变量**文件名加了引号（ECR P2 2024 p.29）。先把文件名存进一个 STRING 常量或变量再用，是考官认可的好习惯（ER s25 9618/22 Q5 p.21）。
7. **`RETURN` 在 `CLOSEFILE` 之前**：函数读到满足条件就立刻 `RETURN TRUE`，结果跳过了 `CLOSEFILE`（ER w22 9618/21 Q8 p.18）。Python 用 `with` 就不会有这个问题。
8. **在循环里打开或关闭文件**：每读一行就重新打开，或在循环里就关掉再接着读（ECR P4 2024 p.7；ER s24 9618/21 Q8 p.15：不必要地打开、关闭文件）。
9. **把 `INPUT`、`OUTPUT` 当文件标识**（ECR P2 2024 p.29）。
10. **Python 的 `"\n"`**：读进来的行没去换行，和字符串比较总是不相等；写出去的行没加换行，所有内容粘成一行。
11. **Python 的 `"w"` 会立即清空文件**——即使你一行也没写。只想读时用 `"r"`。
12. **2024 年考官范答写的是 `OPEN InFile FOR READ`**（ECR P2 2024 p.28）；2027–29 指南的关键字是 **`OPENFILE`**（p.25）。照指南写（D2）。

## 延伸阅读

- CS50P Lecture 6 “File I/O” 讲义：[open](https://cs50.harvard.edu/python/notes/6/#open)、[with](https://cs50.harvard.edu/python/notes/6/#with)（`rstrip` 去换行、逐行读）、[CSV](https://cs50.harvard.edu/python/notes/6/#csv)（选读）。CS50P Problem Set 6 “Lines of Code”：<https://cs50.harvard.edu/python/psets/6/lines/>（E02 的改编来源）。（CC BY-NC-SA 4.0）
- Think Python 3e（CC BY-NC-SA 4.0）：[7.2 Reading the word list](https://allendowney.github.io/ThinkPython/chap07.html#reading-the-word-list)（`open`、`readline`、`for line in file`、`strip`）、[8.6 Writing files](https://allendowney.github.io/ThinkPython/chap08.html#writing-files)（`"w"` 模式、`write`、`close`）、[13.1 Filenames and paths](https://allendowney.github.io/ThinkPython/chap13.html#filenames-and-paths)。
- 教材 Langfield & Duddell 2e：13.06 Text files（p.226）、14.15 Text files（p.279）；A2 的 26.02 File processing（p.448）。书中伪代码与 2027–29 指南不同时以指南为准。
- 官方：伪代码指南 §9.1（p.25–26）；SoW Unit 10（p.33：给有错的文件伪代码让学生找错）。

## 练习

| 练习 | 形态 | 先写伪代码 | 数据文件 | 练什么 |
|:--|:--|:--|:--|:--|
| [`exercises/E01-trace-file-copy/`](exercises/E01-trace-file-copy/spec.md) | 干跑 | 否 | `words.txt`、`out.txt` | 读到文件尾、空行判断、写新文件、WRITE 覆盖旧内容 |
| [`exercises/E02-count-code-lines/`](exercises/E02-count-code-lines/spec.md) | 函数 | 是 | 4 个 `.txt` | 逐行判断：空行、只有空格的行、注释行 |
| [`exercises/E03-load-words/`](exercises/E03-load-words/spec.md) | 函数 | 是 | `game.txt`、`tie.txt`、`empty.txt` | 读进数组、去换行、跳过空行 |
| [`exercises/E04-append-and-write/`](exercises/E04-append-and-write/spec.md) | 函数 | 是 | `log.txt`、`report.txt` | APPEND 与 WRITE 的区别；每行加换行 |
| [`exercises/E05-filter-file/`](exercises/E05-filter-file/spec.md) | 函数 | 是 | `marks.txt` | 读一个文件、拆字段、按条件写另一个文件、计数 |
