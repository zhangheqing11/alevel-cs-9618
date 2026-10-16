# L12/E05 · 多态：重写 GetArea，Describe 只写一次

| 属性 | 值 |
|:--|:--|
| id | `L12/E05` |
| 目录 | `ladder/levels/L12-oop/exercises/E05-shape-polymorphism/` |
| 形态 | `function`（三个类 + 一个函数） |
| entry | `TotalArea`（同一文件还有类 `Shape`、`Rectangle`、`Circle`） |
| pseudocode | `false` |
| files | `[]` |
| skills | `polymorphism`, `inheritance`, `encapsulation`, `output-format`, `p4-identifiers` |
| difficulty | 3 |
| title | `Polymorphism: override GetArea, write Describe once` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L12 card §3、§4 |

## 练习目标

用多态写代码：父类定义 `GetArea()`（返回 0）和 `Describe()`，子类只重写 `GetArea()`；`Describe()` 只在父类里写一次，却能对每个子类给出正确的面积；一个函数对一组不同类的对象统一调用 `GetArea()`。

## 题面

### 中文导读

`Shape`：私有属性 `Name`；构造取名字；`GetName()`；`GetArea()` 返回 `0.0`；`Describe()` 返回 `"<名字>: <面积，两位小数>"`，面积通过 `self.GetArea()` 得到。`Rectangle`、`Circle` 继承 `Shape`，构造分别取宽高、半径，并调用父类构造（名字分别是 `"Rectangle"`、`"Circle"`），各自重写 `GetArea()`（圆用 `math.pi`）。`Describe()` **只**写在 `Shape` 里。再写函数 `TotalArea(Shapes)` 返回一组图形的面积之和。

### English task

| `Shape` | |
|:--|:--|
| `Name : STRING` | private |
| `Constructor()` | takes the name as a parameter |
| `GetName()` | returns `Name` |
| `GetArea()` | returns `0.0` |
| `Describe()` | returns the name, a colon, a space and the area to two decimal places, for example `Circle: 12.57`. It gets the area by calling `GetArea()` on the object itself |

- `Rectangle` inherits from `Shape`. Its constructor takes a width and a height (real numbers), calls the parent constructor with the name `"Rectangle"`, and stores the width and height in private attributes. It overrides `GetArea()` to return width × height.
- `Circle` inherits from `Shape`. Its constructor takes a radius (a real number), calls the parent constructor with the name `"Circle"`, and stores the radius in a private attribute. It overrides `GetArea()` to return π × radius², using `math.pi`.
- `Describe()` is written only in `Shape`.
- Write a function `TotalArea()` that takes a list of shape objects and returns the sum of their areas.

## 接口

```python
import math


class Shape:
    def __init__(self, GivenName: str) -> None:
        raise NotImplementedError   # self.__Name (STRING)

    def GetName(self) -> str:
        raise NotImplementedError

    def GetArea(self) -> float:
        raise NotImplementedError

    def Describe(self) -> str:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, GivenWidth: float, GivenHeight: float) -> None:
        raise NotImplementedError   # parent constructor; self.__Width, self.__Height (REAL)

    def GetArea(self) -> float:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, GivenRadius: float) -> None:
        raise NotImplementedError   # parent constructor; self.__Radius (REAL)

    def GetArea(self) -> float:
        raise NotImplementedError


def TotalArea(Shapes: list[Shape]) -> float:
    """Return the sum of GetArea() for every shape in the list."""
    raise NotImplementedError
```

（不需要 `answer.pseudo`。）

## 必测行为

面积用 `pytest.approx(…, abs=1e-9)` 比较。T10 已用参考实现核对：`math.pi * 2 * 2 = 12.566…` 显示为 `12.57`，而 `3.14 * 4` 显示为 `12.56`。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `Rectangle(3, 4).GetArea()`、`Circle(1).GetArea()` | `12`、`math.pi` | 重写 |
| B2 | `Shape("Blob").GetArea()`、`Shape("Blob").Describe()` | `0.0`、`"Blob: 0.00"` | 父类本身 |
| B3 | `Circle(2).Describe()`、`Rectangle(2.5, 4).Describe()` | `"Circle: 12.57"`、`"Rectangle: 10.00"` | 继承来的 `Describe` 调用子类的 `GetArea`（多态） |
| B4 | `Rectangle(3, 4).GetName()`、`Circle(1).GetName()` | `"Rectangle"`、`"Circle"` | 父类构造被调用 |
| B5 | `TotalArea([Rectangle(3, 4), Circle(1), Shape("Blob")])`、`TotalArea([])` | `12 + math.pi`、`0.0` | |
| B6 | `"Describe" in Rectangle.__dict__`、`"Describe" in Circle.__dict__`；`issubclass(Rectangle, Shape)`、`issubclass(Circle, Shape)` | `False`、`False`；`True`、`True` | `Describe` 只写在父类里 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `Describe` 写成 `Shape.GetArea(self)`（固定调用父类版本）：所有面积都显示 `0.00` | B3 |
| M2 | 圆面积用 `3.14`：`Circle(2).Describe()` 得 `"Circle: 12.56"`，`Circle(1).GetArea()` 与 `math.pi` 不相等 | B1、B3、B5 |
| M3 | 子类构造没有调用父类构造：`GetName()` 抛 `AttributeError` | B3、B4 |
| M4 | 在 `Rectangle`、`Circle` 里各写一份 `Describe`（结果正确） | B6 |

## 人工核对清单

- [ ] `Describe` 用的是 `self.GetArea()` 与 `self.GetName()`，并能解释这一行在 `Circle` 对象上为什么调用的是 `Circle.GetArea`。
- [ ] `TotalArea` 用循环逐个调用 `GetArea()` 累加；可以用 `sum`（题目没有要求写算法），但要能写出循环版本。
- [ ] 所有属性私有并有类型注释；每个方法都有 `self`。
- [ ] 能用一句话说出多态的含义，并举出本题的例子。

## 出处

自编。依据：考纲 20.1（p.38：polymorphism、inheritance）；指南 p.28–29。
