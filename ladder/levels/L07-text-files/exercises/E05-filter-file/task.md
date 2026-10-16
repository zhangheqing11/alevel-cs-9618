# L07/E05 · 过滤文件：拆字段、按条件写出、计数


### 中文导读

`marks.txt` 每行是 `名字,分数`，中间可能有空行。写函数 `FilterMarks(InFile, OutFile, PassMark)`：把分数 **≥ PassMark** 的行原样写进 `OutFile`（`OutFile` 新建，原有内容丢失），返回分数低于 `PassMark` 而没有写出的行数。空行既不写出，也不计数。分数一定是非负整数，名字里没有逗号。

### English task

Each line of a text file holds a name and an integer mark separated by a comma, for example `Ann,71`. The file may contain blank lines.

Write a function `FilterMarks()` that takes an input file name, an output file name and an integer `PassMark`. It:

- copies each line whose mark is greater than or equal to `PassMark` to the output file, unchanged and in the same order; the output file is a new file (any existing contents are lost)
- ignores blank lines (they are not copied and not counted)
- returns the number of lines that were not copied because the mark was below `PassMark`.

Marks are non-negative integers; names do not contain commas. Then write the Python function `filter_marks(in_name, out_name, pass_mark)`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 数据文件

`files/marks.txt`（7 行，以换行结束；第 5 行是空行）：

```text
Ann,71
Bo,39
Cy,40
Dee,88

Eve,0
Fay,100
```

## 人工核对清单

- [ ] 伪代码：两个文件分别以 `READ`、`WRITE` 打开，各 `CLOSEFILE` 一次，`CLOSEFILE` 在 `RETURN` 之前。
- [ ] 伪代码：用 `FOR` + `MID(Line, Index, 1) = ','` 找到逗号位置，再用 `RIGHT(Line, LENGTH(Line) - CommaPos)` 取出分数，`STR_TO_NUM` 转成数字；没有 `split`（D2）。
- [ ] 伪代码：空行判断 `IF Line <> "" THEN` 写在拆字段之前。
- [ ] 伪代码：计数器先初始化；`RETURN` 的是计数，没有 `OUTPUT`。
- [ ] Python：可以用 `line.split(",")`、`int(…)`；两个文件都用 `with`。

## 出处

自编。题型参考 9618_s24_22 Q8(c) 的 `Stage_2()`（ECR P2 2024 p.27–29：逐行读、处理、按条件写出、统计并汇报被去掉的行数）。语法依据：指南 p.25–26；插页 9618_w25_in_21 p.2（MID、RIGHT、LENGTH、STR_TO_NUM）。
