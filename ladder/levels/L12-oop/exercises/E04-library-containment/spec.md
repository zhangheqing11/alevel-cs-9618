# L12/E04 · 包含：图书馆里的图书对象数组

| 属性 | 值 |
|:--|:--|
| id | `L12/E04` |
| 目录 | `ladder/levels/L12-oop/exercises/E04-library-containment/` |
| 形态 | `function`（两个类；测试创建对象、调用方法，并检查对象数组与类的关系） |
| entry | `Library`（同一文件还有 `Book`） |
| pseudocode | `false` |
| files | `[]` |
| skills | `containment`, `encapsulation`, `array-of-records`, `linear-search`, `p4-identifiers` |
| difficulty | 4 |
| title | `Containment: a library holds an array of book objects` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L12 card §5、§6 |

## 练习目标

写一个「拥有」另一个类的对象数组的类：构造时把数组的每个元素都初始化为对象；只在已用的部分里查找；通过 `Book` 的公有方法读取它的私有数据；`Library` 不继承 `Book`。这是 P4 的 `TreeClass` 包含 `Node` 那类题的基本形（9618_s24_42 Q2，ECR P4 2024 p.19–20）。

## 题面

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

## 接口

```python
class Book:
    def __init__(self, GivenTitle: str) -> None:
        raise NotImplementedError   # self.__Title (STRING), self.__OnLoan (BOOLEAN)

    def GetTitle(self) -> str:
        raise NotImplementedError

    def GetOnLoan(self) -> bool:
        raise NotImplementedError

    def LendOut(self) -> bool:
        raise NotImplementedError

    def ReturnBook(self) -> None:
        raise NotImplementedError


class Library:
    def __init__(self) -> None:
        raise NotImplementedError   # self.__Books (Book, 5 elements), self.__NumberBooks (INTEGER)

    def AddBook(self, NewBook: Book) -> bool:
        raise NotImplementedError

    def FindBook(self, Title: str) -> int:
        raise NotImplementedError

    def LendBook(self, Title: str) -> bool:
        raise NotImplementedError

    def CountOnLoan(self) -> int:
        raise NotImplementedError
```

（不需要 `answer.pseudo`。）

## 必测行为

除 B1、B2 外，测试先 `L = Library()`，再依次 `AddBook(Book(t))`，`t` 取 `"Dune"`、`"Emma"`、`"Ubik"`、`"Kim"`、`"Ulysses"`。

| # | 操作 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `B = Book("Dune")`：`GetTitle()`、`GetOnLoan()`；`LendOut()` 两次；`ReturnBook()` 后 `GetOnLoan()` | `"Dune"`、`False`；`True`、`False`；`False` | `Book` 本身 |
| B2 | 新建 `Library()`：`vars()` 的键；`_Library__Books` | 恰好是 `{"_Library__Books", "_Library__NumberBooks"}`；是长度为 5 的 `list`，每个元素都是 `Book` 实例且互不相同（`is` 比较），书名都是 `""`；`FindBook("")` 返回 `-1` | 对象数组真实建出；只查已加入的书 |
| B3 | 加入 5 本后再 `AddBook(Book("Extra"))` | 前 5 次 `True`，第 6 次 `False` | 满（边界） |
| B4 | `FindBook("Emma")`、`FindBook("Ulysses")`、`FindBook("Nope")` | `1`、`4`、`-1` | |
| B5 | `LendBook("Emma")` 两次；`LendBook("Nope")` | `True`、`False`；`False` | 调用 `Book` 的方法 |
| B6 | 接 B5：`CountOnLoan()` | `1` | |
| B7 | `issubclass(Library, Book)` | `False` | 包含，不是继承 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `Library` 继承 `Book`（`class Library(Book):`，构造里调用 `super().__init__("")`） | B2、B7 |
| M2 | 构造里把 `Books` 建成空 list，`AddBook` 用 `append` | B2 |
| M3 | `FindBook` 直接读 `self.__Books[i].__Title`：Python 改写成 `_Library__Title`，抛 `AttributeError` | B4、B5、B6 |
| M4 | `FindBook` 查遍全部 5 个元素（不看 `NumberBooks`）：`FindBook("")` 返回 `0` | B2 |

## 人工核对清单

- [ ] `Library` 构造里用循环（或列表推导）创建 5 个 `Book("")`；没有写 `[Book("")] * 5`（卡片 §5）。
- [ ] `Library` 的方法通过 `GetTitle()`、`LendOut()`、`GetOnLoan()` 访问书的数据，没有读写 `Book` 的私有属性。
- [ ] `AddBook` 的参数是 `Book` 对象（不是书名字符串）——ECR P4 2024 p.23 点名过「传整数而不是 Node 对象」的同类错误。
- [ ] 能说出包含与继承的区别，并用「有一个 / 是一个」判断本题为什么是包含（ER s24 9618/42 Q2 p.44）。

## 出处

自编。结构参考 9618_s24_42 Q2 的 `TreeClass` 包含 `Node`（ECR P4 2024 p.19–20：构造里把 20 个元素初始化为 Node 对象）。误区依据：ER s24 9618/42 Q2 p.44；ECR P4 2024 p.20、p.23。
