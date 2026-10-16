# L12/E01 · 第一个类：私有属性、构造、getter/setter

| 属性 | 值 |
|:--|:--|
| id | `L12/E01` |
| 目录 | `ladder/levels/L12-oop/exercises/E01-pet-class/` |
| 形态 | `function`（测试创建对象、调用方法，并检查属性确实私有） |
| entry | `Pet` |
| pseudocode | `true` |
| files | `[]` |
| skills | `class-definition`, `encapsulation`, `getter-setter`, `boundary-values`, `p4-identifiers` |
| difficulty | 2 |
| title | `A first class: private attributes, constructor, getters and setters` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L12 card §1、§2 |

## 练习目标

按「类说明表」写出一个完整的类：两个私有属性、构造、两个 getter、一个带校验的 setter、一个修改自身状态的方法；每个方法都有 `self`；属性名与方法名照抄题目。

## 题面

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

## 接口

```python
class Pet:
    def __init__(self, GivenName: str, GivenAge: int) -> None:
        raise NotImplementedError   # self.__Name (STRING), self.__Age (INTEGER)

    def GetName(self) -> str:
        raise NotImplementedError

    def GetAge(self) -> int:
        raise NotImplementedError

    def SetAge(self, NewAge: int) -> bool:
        raise NotImplementedError

    def Birthday(self) -> None:
        raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
CLASS Pet
   // private attributes, constructor NEW, then the methods

ENDCLASS
```

## 必测行为

| # | 操作 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `P = Pet("Kitty", 3)`；`P.GetName()`、`P.GetAge()` | `"Kitty"`、`3` | 构造与 getter |
| B2 | `P.SetAge(10)` 后 `P.GetAge()` | 返回 `True`；`10` | |
| B3 | `P.SetAge(51)`、`P.SetAge(-1)` 后 `P.GetAge()` | 都返回 `False`；年龄不变 | 越界（异常数据） |
| B4 | `P.SetAge(0)`、`P.SetAge(50)` | 都返回 `True` | 两端（边界） |
| B5 | `Pet("Rex", 4)` 调用 `Birthday()` 两次后 `GetAge()` | `6` | 方法修改对象自己的属性 |
| B6 | 两个对象 `Pet("A", 1)`、`Pet("B", 2)`，对第一个 `SetAge(9)` | 第二个的年龄仍是 `2` | 每个对象有自己的属性 |
| B7 | 私有：`vars(Pet("Kitty", 3))` 的键 | 恰好是 `{"_Pet__Name", "_Pet__Age"}`；`hasattr(P, "Name")` 与 `hasattr(P, "Age")` 都是 `False` | 属性名照抄题目，且是私有的 |
| B8 | 返回类型 | `GetName` → `str`、`GetAge` → `int`、`SetAge` → `bool` | getter 返回而不是打印 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 属性是公有的：`self.Name`、`self.Age` | B7 |
| M2 | `GetAge` 用 `print` 代替 `return`：返回 `None` | B1、B2、B3、B5、B6、B8 |
| M3 | `SetAge` 不校验，任何值都存入并返回 `True` | B3 |
| M4 | `Birthday` 写成 `Age = self.__Age + 1`（赋给局部变量）：年龄不变 | B5 |

## 人工核对清单

- [ ] 伪代码：`CLASS Pet` / `PRIVATE Name : STRING` / `PRIVATE Age : INTEGER` / `PUBLIC PROCEDURE NEW(GivenName : STRING, GivenAge : INTEGER)` / 各方法 / `ENDCLASS`（指南 p.28）。
- [ ] 伪代码：getter 是 `PUBLIC FUNCTION GetName() RETURNS STRING`；`SetAge` 是 `FUNCTION … RETURNS BOOLEAN`；`Birthday` 是 `PROCEDURE`。
- [ ] Python：用 `__init__`；属性在 `__init__` 里初始化并有类型注释；每个方法第一个参数是 `self`。
- [ ] 能说出：为什么外部代码不能直接写 `P.__Age = 99`，以及 `SetAge` 的校验体现了封装的什么好处。

## 出处

自编。类的写法依据：指南 p.28–29。误区依据：ER s22 9618/41 Q2 p.36（构造、getter、`self`）；ER s23 9618/41 Q2 p.38（getter 打印而不返回）；ECR P4 2021 p.39（属性未设为私有）。
