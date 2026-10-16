# L12/E04 · 包含：图书馆里的图书对象数组


### 中文导读

按下面两张表写类 `Book` 与 `Library`。`Library` 的构造要把 5 个元素都初始化为书名为空串的 `Book` 对象。查找只看已经加进来的书（前 `NumberBooks` 本）。

### English task

| `Book` | |
|:--|:--|
| `Title : STRING` | private |
| `OnLoan : BOOLEAN` | private |
| `Constructor()` | takes the title as a parameter; initialises `Title` to it and `OnLoan` to `FALSE` |
| `GetTitle()` | returns `Title` |
| `GetOnLoan()` | returns `OnLoan` |
| `LendOut()` | returns `FALSE` if the book is already on loan; otherwise sets `OnLoan` to `TRUE` and returns `TRUE` |
| `ReturnBook()` | sets `OnLoan` to `FALSE` |

| `Library` | |
|:--|:--|
| `Books[0:4] : Book` | private; an array of 5 elements of type `Book` |
| `NumberBooks : INTEGER` | private; the number of books added so far |
| `Constructor()` | initialises each element of `Books` to a `Book` object with the title `""`, and `NumberBooks` to 0 |
| `AddBook()` | takes a `Book` object; returns `FALSE` if the array is full, otherwise stores the book in the next element, adds 1 to `NumberBooks` and returns `TRUE` |
| `FindBook()` | takes a title; returns the index of the first of the added books with that title, or -1 |
| `LendBook()` | takes a title; returns `FALSE` if no added book has that title, otherwise returns the result of calling `LendOut()` on that book |
| `CountOnLoan()` | returns how many of the added books are on loan |

Write both classes in Python. `Library` contains `Book` objects; it must not inherit from `Book`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] `Library` 构造里用循环（或列表推导）创建 5 个 `Book("")`；没有写 `[Book("")] * 5`（卡片 §5）。
- [ ] `Library` 的方法通过 `GetTitle()`、`LendOut()`、`GetOnLoan()` 访问书的数据，没有读写 `Book` 的私有属性。
- [ ] `AddBook` 的参数是 `Book` 对象（不是书名字符串）——ECR P4 2024 p.23 点名过「传整数而不是 Node 对象」的同类错误。
- [ ] 能说出包含与继承的区别，并用「有一个 / 是一个」判断本题为什么是包含（ER s24 9618/42 Q2 p.44）。

## 出处

自编。结构参考 9618_s24_42 Q2 的 `TreeClass` 包含 `Node`（ECR P4 2024 p.19–20：构造里把 20 个元素初始化为 Node 对象）。误区依据：ER s24 9618/42 Q2 p.44；ECR P4 2024 p.20、p.23。
