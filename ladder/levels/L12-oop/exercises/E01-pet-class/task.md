# L12/E01 · 第一个类：私有属性、构造、getter/setter


### 中文导读

按下表写类 `Pet`。属性必须是私有的。

### English task

The class `Pet` is defined by this table:

| `Pet` | |
|:--|:--|
| `Name : STRING` | private; the pet's name |
| `Age : INTEGER` | private; the pet's age in years |
| `Constructor()` | takes a name and an age as parameters and initialises `Name` and `Age` to them |
| `GetName()` | returns `Name` |
| `GetAge()` | returns `Age` |
| `SetAge()` | takes an integer parameter; if it is from 0 to 50 inclusive, stores it in `Age` and returns `TRUE`, otherwise leaves `Age` unchanged and returns `FALSE` |
| `Birthday()` | adds 1 to `Age` |

Write pseudocode for the class, then write it in Python. In Python, declare the private attributes as `self.__Name` and `self.__Age` in the constructor, with comments giving their data types.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`CLASS Pet` / `PRIVATE Name : STRING` / `PRIVATE Age : INTEGER` / `PUBLIC PROCEDURE NEW(GivenName : STRING, GivenAge : INTEGER)` / 各方法 / `ENDCLASS`（指南 p.28）。
- [ ] 伪代码：getter 是 `PUBLIC FUNCTION GetName() RETURNS STRING`；`SetAge` 是 `FUNCTION … RETURNS BOOLEAN`；`Birthday` 是 `PROCEDURE`。
- [ ] Python：用 `__init__`；属性在 `__init__` 里初始化并有类型注释；每个方法第一个参数是 `self`。
- [ ] 能说出：为什么外部代码不能直接写 `P.__Age = 99`，以及 `SetAge` 的校验体现了封装的什么好处。

## 出处

自编。类的写法依据：指南 p.28–29。误区依据：ER s22 9618/41 Q2 p.36（构造、getter、`self`）；ER s23 9618/41 Q2 p.38（getter 打印而不返回）；ECR P4 2021 p.39（属性未设为私有）。
