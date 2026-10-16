# L06/E02 · 线性查找：并行数组里找分数


### 中文导读

两个全局数组：`Names` 存学生名，`Marks` 存对应的分数，`NumStudents` 是实际人数。写函数 `LookUpMark(SearchName)`：找到第一个名字与 `SearchName` 相同（**不区分大小写**）的学生，返回他的分数；找不到返回 `-1`。找到后必须立即停止查找。Python 里两个数组作为参数传入。

### English task

A program uses two global 1D arrays, `Names` (`ARRAY[1:50] OF STRING`) and `Marks` (`ARRAY[1:50] OF INTEGER`). `Names[i]` and `Marks[i]` belong to the same student. The global integer `NumStudents` is the number of elements in use, from 0 to 50.

Write a function `LookUpMark()` that takes a name `SearchName` and returns the mark of the first student whose name matches `SearchName`, ignoring case. It returns `-1` if there is no match. The search must stop as soon as a match is found.

Then write the Python function `look_up_mark(names, marks, search_name)`. The two lists are passed as parameters and have the same length (the number of students).

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：用 `WHILE Index <= NumStudents AND Found = FALSE` 这类条件循环，或在 `FOR` 里找到后立即 `RETURN`；没有把 `FOR` 套在 `WHILE` 里（ER w25 p.15–16）。
- [ ] 伪代码：比较写成 `TO_UPPER(Names[Index]) = TO_UPPER(SearchName)`；分数用同一个下标 `Marks[Index]` 取出。
- [ ] 伪代码：循环上界是 `NumStudents`，不是 50，也不是 `LENGTH(Names)`（`LENGTH` 只用于字符串，ER w25 p.15）。
- [ ] 伪代码：以 `RETURN` 交回结果，函数里没有 `OUTPUT`（ECR P4 2021 p.25 点名「在函数里输出而不是返回」）。
- [ ] Python：没有用 `in` 或 `index()` 代替查找循环（ECR P4 2021 p.22）。

## 出处

自编。误区依据：ER w25 p.15–16（混合循环结构）；ECR P4 2021（9618_s21_42）p.22、p.25。语法依据：指南 p.10（数组）、p.21（WHILE）、p.23（FUNCTION）；插页 9618_w25_in_21 p.2（TO_UPPER）。
