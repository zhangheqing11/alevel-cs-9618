# L08/E01 · 图书记录：TYPE ↔ class，记录数组上的计数与查找


### 中文导读

图书馆每本书存一条记录：书名 `Title`、作者 `Author`、出版年 `Year`、是否借出 `OnLoan`。伪代码：定义记录类型 `Book`；声明全局记录数组 `Library`（500 个元素）与在用个数 `NumBooks`；写函数 `CountOnLoan()` 返回借出的本数；写过程 `ListTitlesBefore(Year)`，按数组顺序输出所有出版年**早于** `Year` 的书名。Python：写 class `Book`（四个字段都有初值），以及 `make_book`、`count_on_loan`、`titles_before`（返回书名 list，代替伪代码的逐个输出）。

### English task

Each book in a library is stored as a record with the fields `Title` (string), `Author` (string), `Year` (integer) and `OnLoan` (Boolean).

Write pseudocode to:

1. define the record type `Book`
2. declare the global array `Library` of 500 `Book` records and the global integer `NumBooks` (the number of elements in use)
3. write a function `CountOnLoan()` that returns how many books in `Library` are on loan
4. write a procedure `ListTitlesBefore()` that takes an integer `Year` and outputs, in array order, the title of each book published before `Year`.

Then write Python:

- a class `Book` whose constructor takes no parameters and sets `title = ""`, `author = ""`, `year = 0`, `on_loan = False`
- `make_book(title, author, year)` returns a new `Book` with those fields and `on_loan` set to `False`
- `count_on_loan(books)` returns how many books in the list are on loan
- `titles_before(books, year)` returns, in list order, the titles of the books published before `year`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`TYPE Book` 下每个字段一行 `DECLARE Title : STRING` 等，最后 `ENDTYPE`；`TYPE` 前没有 `DECLARE`（ECR P2 2024 p.12）。
- [ ] 伪代码：`DECLARE Library : ARRAY[1:500] OF Book`——类型是 `Book`，范围用冒号（ECR P2 2024 p.13）。
- [ ] 伪代码：访问字段写成 `Library[Index].OnLoan`、`Library[Index].Title`，没有二维下标（ER w25 p.16）；循环上界是 `NumBooks`。
- [ ] 伪代码：`IF Library[Index].OnLoan = TRUE THEN`（或 `IF Library[Index].OnLoan THEN`）；`OnLoan` 是 BOOLEAN，不是字符串。
- [ ] Python：`__init__` 里四个字段都有初值，类型从初值看得出来（或加类型标注/注释）——P4 要求说明字段的数据类型（ECR P4 2021 p.39）。

## 出处

自编。误区依据：ECR P2 2024（9618_s24_22 Q3）p.12–13；ER w25 p.16；ECR P4 2021 p.39。语法依据：指南 p.13–14（TYPE、记录数组、点号）。
