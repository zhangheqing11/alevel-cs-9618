# L07/E02 · 数代码行：跳过空行与注释行


### 中文导读

写函数 `CountCodeLines(FileName)`：数一个伪代码程序文件里有几行「代码」。不算的行：空行（没有字符，或只有空格）和注释行（去掉开头空格后以 `//` 开头）。行尾带注释的代码行（如 `OUTPUT A + B   // show the sum`）照常算。

### English task

Write a function `CountCodeLines()` that takes the name of a text file containing a pseudocode program and returns the number of lines of code in it. A line is **not** counted if:

- it is empty or contains only space characters, or
- after any leading spaces are removed, it begins with `//` (a comment line).

A line of code that ends with a comment is still counted. Then write the Python function `count_code_lines(file_name)`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 数据文件

全部以换行结束，`trailing.txt` 除外。`·` 在这里只用来标出空格，**实际文件里是普通空格**。

`files/program1.txt`（9 行）：

```text
// Program to add two numbers
DECLARE A : INTEGER
DECLARE B : INTEGER

···// read the values
INPUT A
INPUT B
OUTPUT A + B   // show the sum
····
```

（第 4 行是空行；第 5 行开头 3 个空格；第 9 行只有 4 个空格。）

`files/comments.txt`（3 行）：

```text
// one

··// two
```

`files/empty.txt`：空文件（0 字节）。

`files/trailing.txt`（2 行，**最后一行没有换行**）：

```text
OUTPUT 1
OUTPUT 2
```

## 人工核对清单

- [ ] 伪代码：`OPENFILE FileName FOR READ`——`FileName` 是参数，**不加引号**（ECR P2 2024 p.29）；`WHILE NOT EOF(FileName)`，`EOF` 带参数。
- [ ] 伪代码：去开头空格用 `LEFT`/`RIGHT`/`LENGTH`（或 `MID` 循环找第一个非空格字符），判断注释用 `LEFT(Line, 2) = "//"`；判空写在取字符之前。
- [ ] 伪代码：`CLOSEFILE FileName` 写在 `RETURN` 之前（ER w22 9618/21 Q8 p.18）。
- [ ] Python：用 `with open(file_name) as file:`；可以用 `strip`、`lstrip`、`startswith`（这是 P4 风格，P2 伪代码里不行）。

## 出处

改编自 CS50P Problem Set 6 “Lines of Code”（<https://cs50.harvard.edu/python/psets/6/lines/>，David J. Malan，CC BY-NC-SA 4.0）。改动：注释符号改为剑桥伪代码的 `//`；文件名改为函数参数；去掉命令行参数与错误退出；数据文件全部重写。
