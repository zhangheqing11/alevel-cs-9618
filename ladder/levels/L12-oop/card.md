# L12 · 面向对象：类、私有属性、构造、getter/setter、继承、多态、包含

> 考纲 20.1（OOP 术语：objects、properties/attributes、methods、classes、inheritance、polymorphism、containment (aggregation)、encapsulation、getters、setters、instances；设计类；写 OOP 代码）（考纲 p.38）· 指南 §10（p.28–29）

## 本级目标

学完本级，你能：

1. 用考纲术语解释类、对象（实例）、属性、方法、封装、getter/setter、继承、多态、包含（聚合）。
2. 读写指南格式的 `CLASS … ENDCLASS`：`PRIVATE`/`PUBLIC`、构造过程 `NEW`、`INHERITS`、`SUPER`、`NEW <类名>(…)` 创建对象、`对象.方法()` 调用。
3. 按 P4 题目的「类说明表」写 Python 类：私有属性 `self.__Name`（加类型注释）、`__init__` 构造、照题目命名的 getter/setter、每个方法都有 `self`。
4. 写子类：调用父类构造、重写方法并在需要时调用父类方法；用多态写出对不同子类都适用的代码。
5. 区分包含与继承：一个类「拥有」另一个类的对象（数组）时用包含，不要用继承。

## 伪代码 ↔ Python 对照

### 1. 类、私有属性与方法（指南 p.28）

指南的例子（p.28）：

```pseudocode
PRIVATE Attempts : INTEGER
Attempts ← 3
PUBLIC PROCEDURE SetAttempts(Number : INTEGER)
   Attempts ← Number
ENDPROCEDURE
PRIVATE FUNCTION GetAttempts() RETURNS INTEGER
   RETURN Attempts
ENDFUNCTION
```

方法与属性默认是公有的；访问级别与题目有关时，会用 `PUBLIC` / `PRIVATE` 写明（p.28）。调用方法：`Player.SetAttempts(5)`、`OUTPUT Player.GetAttempts()`（p.28）。

| 伪代码 | Python | 说明 |
|:--|:--|:--|
| `CLASS Pet` … `ENDCLASS` | `class Pet:` | |
| `PRIVATE Name : STRING` | 在 `__init__` 里写 `self.__Name = …  # STRING` | 两个下划线开头 = 私有；Python 没有属性声明，用初值和注释表明类型（P4 题目要求「include attribute declarations using comments」，ECR P4 2024 p.15） |
| `PUBLIC PROCEDURE NEW(GivenName : STRING)` | `def __init__(self, GivenName: str) -> None:` | 构造过程名为 `NEW`（p.28）；Python 只能用 `__init__` |
| `PUBLIC FUNCTION GetName() RETURNS STRING` | `def GetName(self) -> str:` | **每个方法第一个参数都是 `self`** |
| `Name ← GivenName`（类内部） | `self.__Name = GivenName` | 类内部访问属性要写 `self.` |
| `MyCat ← NEW Cat("Kitty", "Shorthaired")`（p.29） | `MyCat = Cat("Kitty", "Shorthaired")` | Python 不写 `NEW` |
| `Player.SetAttempts(5)`（p.28） | `Player.SetAttempts(5)` | 方法调用通过对象 |

**Python 的「私有」是名字改写**：在类 `Pet` 里写的 `self.__Name`，实际存成 `self._Pet__Name`。类外面写 `MyPet.__Name` 会抛 `AttributeError`——这正是封装：外部只能通过 getter/setter 访问。子类里写 `self.__Name` 也会被改写成 `self._Cat__Name`，**子类同样访问不到父类的私有属性**，要用父类的 getter。

### 2. 构造过程、getter 与 setter

```pseudocode
CLASS Pet
   PRIVATE Name : STRING
   PRIVATE Age : INTEGER
   PUBLIC PROCEDURE NEW(GivenName : STRING, GivenAge : INTEGER)
      Name ← GivenName
      Age ← GivenAge
   ENDPROCEDURE
   PUBLIC FUNCTION GetName() RETURNS STRING
      RETURN Name
   ENDFUNCTION
   PUBLIC PROCEDURE SetAge(NewAge : INTEGER)
      Age ← NewAge
   ENDPROCEDURE
ENDCLASS
```

```python
class Pet:
    def __init__(self, GivenName: str, GivenAge: int) -> None:
        self.__Name = GivenName   # STRING
        self.__Age = GivenAge     # INTEGER

    def GetName(self) -> str:
        return self.__Name

    def SetAge(self, NewAge: int) -> None:
        self.__Age = NewAge
```

- **构造函数的参数只要题目列出的那些**；题目说「初始化为 0 / -1」的属性直接在 `__init__` 里赋值，不要额外做成参数（ER s22 9618/41 Q2 p.36；ECR P4 2024 p.16：「taking three parameters instead of one」「assigning parameter values to the left pointer and the right pointer instead of initialising to -1」）。
- **用语言自己的构造方法**：Python 是 `__init__`，不是自己写一个叫 `Constructor` 的普通方法（ER s22 9618/41 Q2 p.36）。
- **getter**：没有参数（除了 `self`），**返回**属性的值，不是打印（ER s22 9618/41 Q2 p.36；ER s23 9618/41 Q2 p.38）。
- **setter**：一个参数，把它存进属性；不要在 setter 里 `input()`，也不要返回参数（ER s23 9618/41 Q2 p.38）。

### 3. 继承：`INHERITS` 与 `SUPER`（指南 p.28）

指南 p.28 的原例（这里的 `Pet` 只有 `Name` 一个属性，与 §2 的例子不同）：

```pseudocode
CLASS Pet
   PRIVATE Name : STRING
   PUBLIC PROCEDURE NEW(GivenName : STRING)
      Name ← GivenName
   ENDPROCEDURE
ENDCLASS

CLASS Cat INHERITS Pet
   PRIVATE Breed : STRING
   PUBLIC PROCEDURE NEW(GivenName : STRING, GivenBreed : STRING)
      SUPER.NEW(GivenName)
      Breed ← GivenBreed
   ENDPROCEDURE
ENDCLASS
```

（指南原文 `Cat` 里那一行印作 `PRIVATE Breed: STRING`，冒号前少一个空格；这里按指南其他各处 `<identifier> : <data type>` 的格式写。）

```python
class Pet:
    def __init__(self, GivenName: str) -> None:
        self.__Name = GivenName       # STRING


class Cat(Pet):
    def __init__(self, GivenName: str, GivenBreed: str) -> None:
        super().__init__(GivenName)   # the parent constructor sets the inherited attributes
        self.__Breed = GivenBreed     # STRING


MyCat = Cat("Kitty", "Shorthaired")   # guide p.29: MyCat ← NEW Cat("Kitty", "Shorthaired")
```

- 子类的构造**先调用父类构造**；父类已有的属性不要在子类里再定义一遍（ER s23 9618/41 Q2 p.38：有考生没用继承，而是新建一个类、把属性重新定义）。
- **重写**（override）：子类定义一个与父类同名的方法。需要父类原来的行为时调用 `super().方法名(…)`，避免重复代码（ER s23 9618/41 Q2 p.38 称这是更好的写法）。伪代码写 `SUPER.方法名(…)`。
- 子类要用父类的私有属性时，调用父类的 getter（见 §1 的名字改写）。

### 4. 多态

不同子类对同一个方法名给出不同的实现；调用方只管调用这个方法，具体执行哪个版本由对象自己的类决定。

```python
class Shape:
    def GetArea(self) -> float:
        return 0.0

    def Describe(self) -> str:
        return f"Area {self.GetArea():.2f}"    # calls the subclass version if it has one


class Square(Shape):
    def __init__(self, GivenSide: float) -> None:
        self.__Side = GivenSide

    def GetArea(self) -> float:                # overrides Shape.GetArea
        return self.__Side * self.__Side
```

`Square(3).Describe()` 返回 `"Area 9.00"`：`Describe` 只在 `Shape` 里写了一次，但里面的 `self.GetArea()` 调用的是 `Square` 的版本。

### 5. 包含（聚合）：「有一个」而不是「是一个」

一个类的属性里存着另一个类的对象（或对象数组），就是包含。例如二叉树类有一个结点数组：

```python
class TreeClass:
    def __init__(self) -> None:
        self.__Tree = [Node(-1) for _ in range(20)]   # Node, 20 elements
        self.__FirstNode = -1                          # INTEGER
        self.__NumberNodes = 0                         # INTEGER
```

- 树「有」结点，树不「是」结点：`TreeClass` **不应**继承 `Node`（ER s24 9618/42 Q2 p.44：有考生让 TreeClass 继承 Node，还在构造里错误地调用了父类构造）。
- 对象数组要真的放进对象：题目说「每个元素初始化为数据为 -1 的 Node 对象」，就要创建 20 个 `Node(-1)`；不能建空数组、整数数组，或只建 1 个、19 个（ECR P4 2024 p.20；ER s24 9618/42 Q2 p.44）。
- 不要写 `[Node(-1)] * 20`：20 个元素是同一个对象（与 L08 的 `[Record()] * n` 同理）。

### 6. 创建与使用对象

- 创建的对象要存进变量（或数组元素）里，之后通过这个变量调用方法（ER s22 9618/41 Q2 p.37：有考生创建了对象却没有存起来；有的把方法当普通子程序调用、再把对象当参数传进去）。
- 参数名不要和类名相同，例如参数叫 `Node` 而类也叫 `Node`（ER s22 9618/41 Q2 p.37；ER s25 9618/43 Q3 p.49）。
- 用题目给的测试值创建对象，不要在构造调用里写死别的值（ER s22 9618/41 Q2 p.37）。

## 常见坑

1. **方法漏了 `self`**：Python 里调用时报 `TypeError: … takes 0 positional arguments but 1 was given`（ER s22、s23、s25 的 P4 报告多处点名；ECR P4 2024 p.17、p.23）。
2. **getter 带参数、或打印而不返回**（ER s22 9618/41 Q2 p.36；ER s23 9618/41 Q2 p.38）。
3. **构造函数多了参数**、给本应初始化为固定值的属性赋了参数值（ER s22 9618/41 Q2 p.36；ECR P4 2024 p.16）。
4. **自己写了一个叫 `Constructor` 的方法**，而不是用 `__init__`（ER s22 9618/41 Q2 p.36）。
5. **属性没有设为私有**：要写 `self.__Name`；写成 `self.Name` 就是公有的（ECR P4 2021 p.39：考生没有把属性声明为私有）。
6. **在类外或子类里直接访问私有属性**：`MyPet.__Name`、子类里的 `self.__Name`（指的是子类自己的改写名）都会出 `AttributeError`。用 getter（ER s22 9618/41 Q2 p.37）。
7. **子类没有调用父类构造**：父类的属性根本没有创建，调用继承来的 getter 时报 `AttributeError`。
8. **该用包含时用了继承**（ER s24 9618/42 Q2 p.44）。
9. **对象数组没有放进对象**，或写成 `[Node(-1)] * 20`（ECR P4 2024 p.20）。
10. **参数名和类名相同**（ER s22 9618/41 Q2 p.37；ER s25 9618/43 Q3 p.49）。
11. **方法名没照抄题目**：题目写 `GetData()`，就不要写成 `get_data()` 或 `getData()`。

## 延伸阅读

- CS50P Lecture 8 “Object-Oriented Programming” 讲义：[Classes](https://cs50.harvard.edu/python/notes/8/#classes)、[Inheritance](https://cs50.harvard.edu/python/notes/8/#inheritance)、[Operator Overloading](https://cs50.harvard.edu/python/notes/8/#operator-overloading)（选读）。CS50P 用 `@property` 写 getter/setter，P4 的习惯是照题目写 `GetX()` / `SetX()` 方法，两种都要看得懂。（CC BY-NC-SA 4.0）
- Think Python 3e（CC BY-NC-SA 4.0）：第 15 章 [15.1 Defining methods](https://allendowney.github.io/ThinkPython/chap15.html#defining-methods)、[15.6 The init method](https://allendowney.github.io/ThinkPython/chap15.html#the-init-method)；第 16 章 [16.7 Polymorphism](https://allendowney.github.io/ThinkPython/chap16.html#polymorphism)；第 17 章 [17.8 Parents and children](https://allendowney.github.io/ThinkPython/chap17.html#parents-and-children)、[17.9 Specialization](https://allendowney.github.io/ThinkPython/chap17.html#specialization)。
- 教材 Langfield & Duddell 2e：27.01–27.07 OOP（p.460–479：设计类、写 OOP 代码、继承、多态、包含）。书中伪代码与 2027–29 指南不同时以指南为准。
- 官方：伪代码指南 §10（p.28–29）；考纲 20.1（p.38）。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-pet-class/`](exercises/E01-pet-class/spec.md) | 类 | 是 | 私有属性、构造、getter/setter、修改自身状态的方法 |
| [`exercises/E02-trace-oop/`](exercises/E02-trace-oop/spec.md) | 干跑 | 否 | 读 `CLASS`/`INHERITS`/`SUPER`；子类不能直接访问父类私有属性 |
| [`exercises/E03-account-inheritance/`](exercises/E03-account-inheritance/spec.md) | 类 | 是 | 继承、父类构造、重写并调用父类方法 |
| [`exercises/E04-library-containment/`](exercises/E04-library-containment/spec.md) | 类 | 否 | 包含：对象数组、通过对方的方法访问其私有数据 |
| [`exercises/E05-shape-polymorphism/`](exercises/E05-shape-polymorphism/spec.md) | 类 | 否 | 多态：重写 `GetArea`，`Describe` 只写一次 |
