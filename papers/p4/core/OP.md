## OP　面向对象编程：伪代码 ↔ Python 对照与模板 {#core-OP}

类图不是让你自由设计接口，而是规定属性、类型、参数、初值与方法效果。P4 交 Python；下表用 2027–29 指南的 CLASS / PRIVATE / PUBLIC / NEW / SUPER 帮你读懂同一对象模型。标识符照题目写，类型用英文注释，类的方法始终缩进在类内。

### 1. 类、构造与属性

| 意图 | 伪代码 | Python | 注意 |
|:--|:--|:--|:--|
| 类声明 | `CLASS Vehicle` … `ENDCLASS` | `class Vehicle:` + 缩进 | 不用括号也能声明没有父类的类 |
| 私有属性 | `PRIVATE CurrentSpeed : INTEGER` | `self.__CurrentSpeed = 0  # INTEGER` | 要真实初始化；只写注释不会创建属性 |
| 公有属性 | `PUBLIC Data : INTEGER` | `self.Data = DataP  # INTEGER` | 仅在题目要求 public 时使用 |
| 构造头 | `PUBLIC PROCEDURE NEW(IDP : STRING, MaxSpeedP : INTEGER, IncreaseAmountP : INTEGER)` | `def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):` | MS 的 3 个参数不含 Python self |
| 保存参数 | `ID ← IDP` | `self.__ID = IDP` | 左边是属性，右边是本次传进来的值 |
| 固定初值 | `CurrentSpeed ← 0` | `self.__CurrentSpeed = 0` | 不擅自给它增加构造参数 |
| 实例化 | `Car ← NEW Vehicle("Tiger", 100, 20)` | `Car = Vehicle("Tiger", 100, 20)` | Python 不写 NEW；保存返回对象 |

两个对象各有自己的属性。下例输出 0 和 30：改 Second 不改变 First。

```python
class Vehicle:
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP                           # STRING
        self.__MaxSpeed = MaxSpeedP               # INTEGER
        self.__IncreaseAmount = IncreaseAmountP   # INTEGER
        self.__CurrentSpeed = 0                   # INTEGER
        self.__HorizontalPosition = 0             # INTEGER

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def SetCurrentSpeed(self, SpeedP):
        self.__CurrentSpeed = SpeedP


if __name__ == "__main__":
    First = Vehicle("First", 100, 20)
    Second = Vehicle("Second", 80, 10)
    Second.SetCurrentSpeed(30)
    print(First.GetCurrentSpeed(), Second.GetCurrentSpeed())
```

### 2. getter / setter / 状态计算

| 意图 | 伪代码 | Python |
|:--|:--|:--|
| getter 头 | `PUBLIC FUNCTION GetCurrentSpeed() RETURNS INTEGER` | `def GetCurrentSpeed(self):` |
| 返回属性 | `RETURN CurrentSpeed` | `return self.__CurrentSpeed` |
| setter 头 | `PUBLIC PROCEDURE SetCurrentSpeed(SpeedP : INTEGER)` | `def SetCurrentSpeed(self, SpeedP):` |
| setter 存值 | `CurrentSpeed ← SpeedP` | `self.__CurrentSpeed = SpeedP` |
| 调用 setter | `CALL Car.SetCurrentSpeed(30)` | `Car.SetCurrentSpeed(30)` |
| 调用 getter 并展示 | `OUTPUT Car.GetCurrentSpeed()` | `print(Car.GetCurrentSpeed())` |
| 带上限的状态更新 | 先增加、再 `IF … > MaxSpeed THEN` 封顶 | `if self.__CurrentSpeed > self.__MaxSpeed: …` |

getter 要返回数据，不能只输出；setter 接参数，不另读 input。名字以 Set 开头也可能要计算：s23/42 的 SetPay 把 Hours 乘时薪，存到 `PayYear2022[WeekNumber - 1]`，属于 OP-03。具体参数和返回类型按题干，不把表中的“无参数”套到 GetCard(Position) 这种容器取对象方法上。

### 3. 继承与重写

| 意图 | 伪代码 | Python |
|:--|:--|:--|
| 子类头 | `CLASS Helicopter INHERITS Vehicle` | `class Helicopter(Vehicle):` |
| 调父类构造 | `SUPER.NEW(IDP, MaxSpeedP, IncreaseAmountP)` | `super().__init__(IDP, MaxSpeedP, IncreaseAmountP)` |
| 调父类同名方法 | `CALL SUPER.IncreaseSpeed()` | `super().IncreaseSpeed()` |
| 调继承的方法 | `Heli.GetCurrentSpeed()` | `Heli.GetCurrentSpeed()` |
| 子类重写 | 子类声明同名方法 | 子类写同名 def、按子类规则执行 |

`super()` 的调用不再显式传 self；写 `Vehicle.__init__(self, …)` 时才要传。子类不能用 `self.__CurrentSpeed` 直接取父类的私有属性：双下划线的名字在不同类中会分别改写。用父类 getter / setter，或调用父类完整方法。

下面是独立可运行的“重写后仍复用父类”骨架。到达最大值时仍可再次调用；不会递归调用自己。

```python
class Account:
    def __init__(self, BalanceP):
        self.__Balance = BalanceP  # REAL

    def Add(self, Amount):
        self.__Balance = self.__Balance + Amount

    def GetBalance(self):
        return self.__Balance


class BonusAccount(Account):
    def __init__(self, BalanceP, BonusP):
        super().__init__(BalanceP)
        self.__Bonus = BonusP      # REAL, percentage

    def Add(self, Amount):
        UpdatedAmount = Amount * (1 + self.__Bonus / 100)
        super().Add(UpdatedAmount)


if __name__ == "__main__":
    Item = BonusAccount(0.0, 10.0)
    Item.Add(50.0)
    print(round(Item.GetBalance(), 2))
```

这是教学自练骨架，无真题 MS；运行结果为 55.0。真题用卡片中的整题程序。调用 `self.Add` 会再次进入子类方法；想复用父类逻辑就写 `super().Add`。

### 4. 包含与对象数组

| 情境 | 写法 | 要检查 |
|:--|:--|:--|
| Hand 有十个 Card 槽位，先放五张 | `self.__Cards = [None] * 10  # Card, 10 elements`，再给前五格赋 Card 参数 | 真有十格；参数是 Card 对象 |
| 每格都要一个初值对象 | 循环中每次调用构造，再 append 或赋给固定槽位 | 不用 `[Card(...)] * 10` 共用一个实例 |
| 容器取对象 | `return self.__Cards[Position]` | 返回的是对象，随后才能 `.GetColour()` |
| 容器加对象 | 判满 → `数组[当前个数] = 新对象` → 个数加一 → True | 失败时不更新计数 |
| 二维对象数组 | 每行新建 list，每格新建对象 | 不能把同一行复制十次 |

Hand 不继承 Card；Station 不继承 Train。它们“有”这些对象。题给数组下标决定长度：0–9 是十格，0–51 是五十二格。Python 都从 0 起；若题干把周数写作 1–52，存取时统一减一，而不是把数组多建一格遮住问题。

### 5. 运行错误定位

| 现象 | 检查 |
|:--|:--|
| 方法报参数个数不符 | def 是否漏 self；调用 super 时是否多传 self |
| AttributeError | 构造是否真正初始化属性；拼写是否一致；子类是否直接访问父类私有属性 |
| getter 调用后得到 None | 是否 print 而未 return；是否漏返回分支 |
| RecursionError | 重写方法里是否错误地写 self.同名方法 |
| 两个对象互相影响 | 数组、属性是否误放在类体作为共享值；是否复制同一个对象引用 |
| 只有上限测试时报 NameError | 是否把 __init__ 参数名用到另一个方法中，而未使用 self 保存的属性 |

阶梯入口：L12 E01 私有属性与方法、E03 继承、E04 包含、E05 多态。题型卡的整题程序用于真题运行；本对照表帮助你解释每一行为什么这样写。
