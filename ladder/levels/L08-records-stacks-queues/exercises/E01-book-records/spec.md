# L08/E01 · 图书记录：TYPE ↔ class，记录数组上的计数与查找

| 属性 | 值 |
|:--|:--|
| id | `L08/E01` |
| 目录 | `ladder/levels/L08-records-stacks-queues/exercises/E01-book-records/` |
| 形态 | `function`（一个记录类 + 三个函数） |
| entry | `make_book`（同一文件还有类 `Book`、函数 `count_on_loan`、`titles_before`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `record-type`, `array-of-records`, `linear-search`, `accumulator`, `return-value` |
| difficulty | 3 |
| title | `Book records: TYPE and class, counting and searching an array of records` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L08 card §1；常见坑 1、2、3 |

## 练习目标

按指南定义记录类型、声明记录数组、用「下标 + 点号」访问字段；在 Python 里写出等价的 class，并在 list of 记录上计数、按条件筛选。

## 题面

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

## 接口

```python
class Book:
    """Record type Book."""

    def __init__(self) -> None:
        raise NotImplementedError   # set title, author, year, on_loan to their initial values


def make_book(title: str, author: str, year: int) -> Book:
    """Return a new Book with the given fields; on_loan is False."""
    raise NotImplementedError


def count_on_loan(books: list[Book]) -> int:
    """Return how many books are on loan."""
    raise NotImplementedError


def titles_before(books: list[Book], year: int) -> list[str]:
    """Return the titles of books published before year, in list order."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// define the record type Book here

// declare the global array Library and the global integer NumBooks here

FUNCTION CountOnLoan() RETURNS INTEGER

ENDFUNCTION

PROCEDURE ListTitlesBefore(Year : INTEGER)

ENDPROCEDURE
```

## 必测行为

除 B1、B2 外，测试用 `make_book` 建立 `BOOKS`：`("Dune", "Herbert", 1965)`、`("Emma", "Austen", 1815)`、`("Ubik", "Dick", 1969)`、`("Kim", "Kipling", 1901)`，再把 `Emma` 与 `Ubik` 的 `on_loan` 设为 `True`。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `Book()` | `title == ""`、`author == ""`、`year == 0`、`on_loan is False` | 初值 |
| B2 | `make_book("Dune", "Herbert", 1965)` | 是 `Book` 实例；`title == "Dune"`、`author == "Herbert"`、`year == 1965`、`on_loan is False` | |
| B3 | 两次 `Book()` 得到的对象 | 修改其中一个的字段，另一个不变 | 每条记录是独立对象 |
| B4 | `count_on_loan(BOOKS)`、`count_on_loan([])` | `2`、`0` | |
| B5 | `titles_before(BOOKS, 1966)` | `["Dune", "Emma", "Kim"]` | 保持顺序 |
| B6 | `titles_before(BOOKS, 1965)`、`titles_before(BOOKS, 1800)` | `["Emma", "Kim"]`、`[]` | 「早于」不含当年（边界） |
| B7 | 调用 B4–B6 后 `BOOKS` | 各字段不变 | 查找不修改记录 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `titles_before` 用 `<=`：`titles_before(BOOKS, 1965)` 包含 `"Dune"` | B6 |
| M2 | `make_book` 把书名和作者填反 | B2、B5、B6 |
| M3 | `count_on_loan` 把所有书都数进去：返回 `4` | B4 |
| M4 | `count_on_loan` 和字符串比较：`if book.on_loan == "TRUE"`，返回 `0` | B4 |

## 人工核对清单

- [ ] 伪代码：`TYPE Book` 下每个字段一行 `DECLARE Title : STRING` 等，最后 `ENDTYPE`；`TYPE` 前没有 `DECLARE`（ECR P2 2024 p.12）。
- [ ] 伪代码：`DECLARE Library : ARRAY[1:500] OF Book`——类型是 `Book`，范围用冒号（ECR P2 2024 p.13）。
- [ ] 伪代码：访问字段写成 `Library[Index].OnLoan`、`Library[Index].Title`，没有二维下标（ER w25 p.16）；循环上界是 `NumBooks`。
- [ ] 伪代码：`IF Library[Index].OnLoan = TRUE THEN`（或 `IF Library[Index].OnLoan THEN`）；`OnLoan` 是 BOOLEAN，不是字符串。
- [ ] Python：`__init__` 里四个字段都有初值，类型从初值看得出来（或加类型标注/注释）——P4 要求说明字段的数据类型（ECR P4 2021 p.39）。

## 出处

自编。误区依据：ECR P2 2024（9618_s24_22 Q3）p.12–13；ER w25 p.16；ECR P4 2021 p.39。语法依据：指南 p.13–14（TYPE、记录数组、点号）。
