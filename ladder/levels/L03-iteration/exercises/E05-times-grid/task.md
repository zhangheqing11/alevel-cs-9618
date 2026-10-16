# L03/E05 · 乘法表：嵌套 FOR 与总累加器


### 中文导读

输入 N（1 到 9），输出 N×N 乘法表：第 i 行是 i×1、i×2、…、i×N，数字之间用一个空格分隔。最后一行输出所有乘积之和 `Total: <和>`。伪代码里一行要先拼成字符串（用 `&` 和 `NUM_TO_STR`），再 `OUTPUT`；行尾多一个空格没关系。

### English task

Write a procedure `TimesGrid()` that:

- prompts for and inputs an integer `N` from 1 to 9
- outputs `N` lines; line `i` contains the products `i * 1`, `i * 2`, …, `i * N`, separated by single spaces
- finally outputs `Total: ` followed by the sum of all the products in the grid.

Use nested `FOR` loops. In pseudocode, build each line as a string with `&` and `NUM_TO_STR()` before outputting it. Then write the Python procedure `times_grid()`. A trailing space at the end of a line is allowed.

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示。除题目规定的输出外不要打印其他内容。

## 人工核对清单

- [ ] 伪代码：外层 `FOR Row ← 1 TO N … NEXT Row`，内层 `FOR Column ← 1 TO N … NEXT Column`，`NEXT` 后写循环变量名（指南 p.20）。
- [ ] 伪代码：每行开始前 `Line ← ""`；内层用 `Line ← Line & NUM_TO_STR(Row * Column) & " "`；内层结束后 `OUTPUT Line`（插页 p.2 NUM_TO_STR，指南 p.17 &）。
- [ ] 伪代码：`Total ← 0` 在两层循环之外；以 `ENDPROCEDURE` 结束。
- [ ] Python：每行结束后换行（`print()` 或拼好字符串后 `print(line)`）。

## 出处

自编。结构参考指南 p.20 的嵌套 FOR 例子（行累加器与总累加器）。语法依据：指南 p.17（&）、p.20（FOR、NEXT）；插页 9618_s26_in_21 p.2（NUM_TO_STR）。
