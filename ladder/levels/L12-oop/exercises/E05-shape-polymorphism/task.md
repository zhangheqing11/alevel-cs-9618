# L12/E05 · 多态：重写 GetArea，Describe 只写一次


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] `Describe` 用的是 `self.GetArea()` 与 `self.GetName()`，并能解释这一行在 `Circle` 对象上为什么调用的是 `Circle.GetArea`。
- [ ] `TotalArea` 用循环逐个调用 `GetArea()` 累加；可以用 `sum`（题目没有要求写算法），但要能写出循环版本。
- [ ] 所有属性私有并有类型注释；每个方法都有 `self`。
- [ ] 能用一句话说出多态的含义，并举出本题的例子。

## 出处

自编。依据：考纲 20.1（p.38：polymorphism、inheritance）；指南 p.28–29。
