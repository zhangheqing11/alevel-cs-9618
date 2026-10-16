# L01/E05 · 票号：数字与字符串的转换和连接


### 中文导读

剧院的票号由姓名、一个短横线和一个数字组成，数字 = 排号 × 100 + 座号。例如 Mia 坐第 12 排 7 号，票号是 `Mia-1207`。输入姓名、排号、座号（排号和座号都是 1 到 99 的整数），输出两行：票号，以及「第几排第几座」。伪代码里用 `&` 和 `NUM_TO_STR` 拼出票号。

### English task

A theatre ticket code is made from the customer's name, a hyphen, and the number `Row * 100 + Seat`. For example, Mia in row 12, seat 7 has the code `Mia-1207`.

Write a procedure `TicketCode()` that:

- prompts for and inputs a name, a row number and a seat number (row and seat are integers from 1 to 99)
- builds the ticket code as a single string, using `&` and the function `NUM_TO_STR()` from the insert
- outputs two lines in the form:

```text
Your code is Mia-1207
Row 12, seat 7
```

Then write the Python procedure `ticket_code()` that inputs the name, row and seat (in that order, one per line) and prints the same two lines.

`NUM_TO_STR(x : <datatype1>) RETURNS <datatype2>` returns a string representation of a numeric value, e.g. `NUM_TO_STR(87.5)` returns `"87.5"`.（插页 p.2 原样）

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示。除题目规定的输出外不要打印其他内容。

## 人工核对清单

- [ ] 伪代码：`Row`、`Seat` 声明为 `INTEGER`，`Name`、`Code` 声明为 `STRING`。
- [ ] 伪代码：`Code ← Name & "-" & NUM_TO_STR(Row * 100 + Seat)`——用 `&`，不用 `+`（ECR P2 2021 p.45 点名）；数字先经 `NUM_TO_STR` 再连接。
- [ ] 伪代码：第二行可以用 `OUTPUT "Row ", Row, ", seat ", Seat`（逗号分隔，不需要转换），能说出它和 `&` 写法的区别。
- [ ] 每个 `INPUT` 前有提示语。
- [ ] Python：能说出 M1 为什么不报错却给出怪结果（`str * int` 是重复）。

## 出处

自编。语法与函数依据：指南 p.15（OUTPUT）、p.17（&）；插页 9618_s26_in_21 p.2（NUM_TO_STR）、p.4（& 运算符）。
