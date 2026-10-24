## OP　面向对象编程 {#ch-OP}

<!-- auto:chapter-stats -->

### 核心思想

先把类图翻成“每个对象保存哪些状态”，再把方法说明翻成“收到什么、改变什么、返回什么”。属性、参数、局部变量是三种不同位置：参数只在这次调用中使用，`self.__属性` 随对象保留下来。`self` 指的就是点号前的那个对象。

七个题型就是一道 OOP 大题的出场顺序：**声明类**（OP-01：私有属性 + `__init__` 把参数存进属性、给固定初值）→ **存取**（OP-02：getter 返回属性、setter 把参数存进属性）→ **其他方法**（OP-03：按属性计算、改变状态、返回描述）→ **继承**（OP-04：`class B(A)`、`super().__init__(…)`、新增属性）→ **重写**（OP-05：子类同名方法覆盖父类，必要时先调 `super()`）→ **包含**（OP-06：一个类的属性是另一个类的对象数组）→ **创建对象并调用方法**（OP-07：用题给参数实例化，再调方法并用返回值）。MS 对类的声明给分很细——名字、私有、类型注释、构造参数一一对应（卷首通用得分规则 3）。P3-FP-04～FP-06 是同一套概念的理论面：术语定义、类图、`CLASS … ENDCLASS` 伪代码。

本章按构造（OP-01）、存取（OP-02）、状态计算（OP-03）、继承声明（OP-04）、重写（OP-05）、包含（OP-06）、创建与调用（OP-07）练。OP-01–05 与 OP-07 共用 s23/41 第 2 题，分别聚焦不同代码格；每张卡保留整道程序，便于独立运行。OP-06 用 w22/41 第 2 题区分“是一种”和“有一些”。类图必须回原页看，不能只凭方法名猜参数。

私有、公有按本题要求：本章主例用双下划线；题目明确要求 public 的结点类不可强行私有化。ADT 类的方法在实现链表、树的插入或遍历时走 LT 入口，不能因为出现 class 就套普通 OP 模板。

### 题型树
<!-- auto:type-tree -->

### P4-OP-01　声明类：私有属性与构造方法　{#P4-OP-01}

<!-- auto:stats P4-OP-01 -->

**考法**　从类图抄出属性、类型、构造参数与固定初值。写 class 与 __init__，本格只交类和构造方法。

**识别信号**　class …；private attributes；constructor；include attribute declarations using comments。

**解题思路**
1. 把类图属性分成两列：从参数来的值（本题 ID、MaxSpeed、IncreaseAmount）与题给初值（CurrentSpeed、HorizontalPosition 都是 0）。参数个数由前一列决定，不由属性总数决定。
2. 写 `class Vehicle:`，构造方法缩进在类里，`self` 后写三个显式参数。MS 的“三个参数”不含 Python 的 `self`。
3. 每个属性写成 `self.__属性 = 值  # TYPE`，既创建真实属性，也说明类型；本题要求 private，不能只写公有属性。
4. 如果属性是数组，先建足题给长度，再赋初值。字符串、整数、对象引用的空值按本题给定值写，不统一改成 0。
5. 证据格只复制题目要求的类头与构造；后续方法各交到后续格。

**Python 模板**（自包含骨架；参数、初值、私有要求照具体题目）

```python
# ---- 2(a)(i) ----
class Vehicle:
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP                           # STRING
        self.__MaxSpeed = MaxSpeedP               # INTEGER
        self.__IncreaseAmount = IncreaseAmountP   # INTEGER
        self.__CurrentSpeed = 0                   # INTEGER
        self.__HorizontalPosition = 0             # INTEGER
```

**得分表述**（引自对应 MS）
- 「Class header (and close where appropriate)」⟦9618_s23_41:2(a)(i)⟧
- 「5 (private) attribute declarations including data types」⟦9618_s23_41:2(a)(i)⟧
- 「Constructor header (and close where appropriate) taking 3 parameters (min)」⟦9618_s23_41:2(a)(i)⟧
- 「Assigning ID, MaxSpeed and IncreaseAmount to parameters」⟦9618_s23_41:2(a)(i)⟧
- 「Assigning CurrentSpeed and HorizontalPosition to 0」⟦9618_s23_41:2(a)(i)⟧

**得分点地图**（核验语料 2022–2026s、仅主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 26 行，其中 26 行拆点；下表由 `markpoints[].skills` 统计，不是每个标签各值一分）

| 技能标签 | 行数 |
|:--|--:|
| `class-definition` | 26 |
| `constructor` | 26 |
| `data-types` | 22 |
| `encapsulation` | 13 |
| `initialise-variables` | 6 |
| `object-reference` | 4 |

读图、参数、属性与调用方向是本型自查重点；单题分值与 Max 始终回本题 MS 核对。

**易错与失分**　考官报告指出，本题较弱作答没有按类图把 CurrentSpeed 与 HorizontalPosition 初始化为 0（9618_s23_41:2(a)(i)）。参数名只是构造时收到的值，方法结束后仍要靠 `self.__…` 保存。不要用注释代替真实属性或数组。

#### 代表题精讲　⟦9618_s23_41:2(a)(i)⟧

**在考什么**　5 个私有属性，3 个参数、2 个零初值；5 分，5 个独立得分点。 整道第 2 题 QP p.4–7（p.4 Vehicle 类图，p.6 Helicopter 类图，p.7 主程序数据）；MS p.12–25。

**完整作答**（整道第 2 题的最终程序；按代码格拆交，不能把整段程序重复贴进每一格）

```python
# ---- 2(a)(i) ----
class Vehicle:
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP                           # STRING
        self.__MaxSpeed = MaxSpeedP               # INTEGER
        self.__IncreaseAmount = IncreaseAmountP   # INTEGER
        self.__CurrentSpeed = 0                   # INTEGER
        self.__HorizontalPosition = 0             # INTEGER

    # ---- 2(a)(ii) ----
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    # ---- 2(a)(iii) ----
    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    # ---- 2(a)(iv) ----
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed


# ---- 2(b)(i) ----
class Helicopter(Vehicle):
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VertChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0               # INTEGER
        self.__VerticalChange = VertChangeP       # INTEGER
        self.__MaxHeight = MaxHeightP             # INTEGER

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    # ---- 2(b)(ii) ----
    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()                   # update horizontal motion in every case


# ---- 2(c) ----
def OutputCurrentPosition(ObjectToOutput):
    print("Current position =", ObjectToOutput.GetHorizontalPosition())
    print("Current speed =", ObjectToOutput.GetCurrentSpeed())
    if isinstance(ObjectToOutput, Helicopter):
        print("Current vertical position =", ObjectToOutput.GetVerticalPosition())


# ---- 2(d)(i) ----
if __name__ == "__main__":
    Car = Vehicle("Tiger", 100, 20)
    Heli = Helicopter("Lion", 350, 40, 3, 100)
    Car.IncreaseSpeed()
    Car.IncreaseSpeed()
    OutputCurrentPosition(Car)
    print()
    Heli.IncreaseSpeed()
    Heli.IncreaseSpeed()
    OutputCurrentPosition(Heli)
```

按 QP p.7 实参实际运行：汽车位置 60、速度 40；直升机位置 120、速度 80、高度 6，与 MS p.25 截图数值一致。另检查第六次汽车加速后速度仍为 100、位置为 400；直升机连续 34 次加速后高度为 100、速度为 350，触顶分支可运行。

**与 MS 逐点对齐**（2(a)(i)，5 分；语料 MP 编号与 MS 圆点顺序一致）

| 语料 MP | MS 原文 | 作答对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Class header (and close where appropriate) | `class Vehicle:` | `class-definition` |
| 2 | 5 (private) attribute declarations including data types | 五个 `self.__…` 赋值及类型注释 | `encapsulation`、`data-types` |
| 3 | Constructor header (and close where appropriate) taking 3 parameters (min) | `def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):` | `constructor` |
| 4 | Assigning ID, MaxSpeed and IncreaseAmount to parameters | 前三个属性由三个参数赋值 | `constructor` |
| 5 | Assigning CurrentSpeed and HorizontalPosition to 0 | CurrentSpeed 与 HorizontalPosition 赋 0 | `constructor`、`initialise-variables` |

**证据格怎么交**　2(a)(i) 代码格放 Vehicle 类头与构造，保留缩进和类型注释；不要把后续 getter 混进这一格。

**直观**　类像空白登记表，构造方法把新车的型号与性能填进去，同时把仪表盘速度和里程归零。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s23_41_q2/`。前置 **L12 E01**。

**下一道变式**　⟦9618_s23_42:3(a)(i)⟧　Employee 多了 `PayYear2022 : ARRAY[0:51] OF REAL`：要建 52 格且每格 0.0，不能只建 51 格。QP p.8；MS p.23–24。

<!-- auto:drills P4-OP-01 -->

### P4-OP-02　getter 与 setter　{#P4-OP-02}

<!-- auto:stats P4-OP-02 -->

**考法**　写直接返回属性的 getter、把参数存进属性的 setter；多个相似方法常合并计一个余下方法分。

**识别信号**　Get… returns the attribute；Set… takes one parameter and assigns it。

**解题思路**
1. getter：`def GetX(self):`，`return self.__X`。本题“no parameter”指无显式业务参数，Python 仍必须有 `self`。
2. setter：`def SetX(self, XP):`，`self.__X = XP`；值来自参数，不在方法里另读 input。
3. 方法缩进在原来的类里；调用时对象写在点号前，如 `ThisNode.GetLeft()`。
4. 返回和输出分开：getter 返回给调用者；调用者需要展示时再 print。
5. 核对题目点名的全部方法，不能只写一个。不是每个 getter 都单独两分，按本格 MS 的分组清单给分。

**Python 模板**（本题 Node 的存取方法；三个属性均为 INTEGER）

```python
# ---- 2(a)(i) ----
class Node:
    def __init__(self, PData):
        self.__LeftPointer = -1  # INTEGER
        self.__Data = PData      # INTEGER
        self.__RightPointer = -1 # INTEGER

    # ---- 2(a)(ii) ----
    def GetLeft(self):
        return self.__LeftPointer

    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data

    # ---- 2(a)(iii) ----
    def SetLeft(self, NewLeft):
        self.__LeftPointer = NewLeft

    def SetRight(self, NewRight):
        self.__RightPointer = NewRight

    def SetData(self, NewData):
        self.__Data = NewData
```

**得分表述**（引自对应 MS）
- 「1 set method header (and end) with parameter …」⟦9618_s24_42:2(a)(iii)⟧
- 「…assigning parameter to correct attribute」⟦9618_s24_42:2(a)(iii)⟧
- 「Remaining 2 correct」⟦9618_s24_42:2(a)(iii)⟧

**得分点地图**（核验语料 2022–2026s、仅主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 26 行，其中 25 行拆点；下表由 `markpoints[].skills` 统计，不是每个标签各值一分）

| 技能标签 | 行数 |
|:--|--:|
| `getter-setter` | 25 |
| `return-value` | 19 |
| `object-reference` | 2 |
| `assign-value` | 1 |
| `nested-if` | 1 |
| `relational-ops` | 1 |

读图、参数、属性与调用方向是本型自查重点；单题分值与 Max 始终回本题 MS 核对。

**易错与失分**　考官报告指出，有考生给 getter 多传参数，或 print 而不 return（9618_s23_41:2(a)(ii)）；setter 中重新从用户读取数值也不合要求（9618_s23_41:2(a)(iii)）。把 `self.__X` 写成局部变量 `X` 不会更新对象。

#### 代表题精讲　⟦9618_s24_42:2(a)(iii)⟧

**在考什么**　为 Node 写三个 setter：SetLeft、SetRight、SetData 把传入的整数保存到对应属性，3 分、3 点。LeftPointer / RightPointer 存数组下标，不存 Node 对象。整题 QP p.6–9（p.6 Node 类图，p.7 TreeClass 类图与 setter 要求，p.8 插入/输出，p.9 七个测试数）；MS p.15–27（setter 清单与 Python 范例 p.18）。

**完整作答**（整道第 2 题的最终程序；按代码格拆交）

```python
# ---- 2(a)(i) ----
class Node:
    def __init__(self, PData):
        self.__LeftPointer = -1  # INTEGER
        self.__Data = PData      # INTEGER
        self.__RightPointer = -1 # INTEGER

    # ---- 2(a)(ii) ----
    def GetLeft(self):
        return self.__LeftPointer

    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data

    # ---- 2(a)(iii) ----
    def SetLeft(self, NewLeft):
        self.__LeftPointer = NewLeft

    def SetRight(self, NewRight):
        self.__RightPointer = NewRight

    def SetData(self, NewData):
        self.__Data = NewData


# ---- 2(b)(i) ----
class TreeClass:
    def __init__(self):
        self.__Tree = [Node(-1) for Count in range(20)]  # Node, 20 elements
        self.__FirstNode = -1    # INTEGER
        self.__NumberNodes = 0   # INTEGER

    # ---- 2(b)(ii) ----
    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__FirstNode = 0
            self.__NumberNodes = self.__NumberNodes + 1
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            NodeAccess = self.__FirstNode
            Direction = ""
            while NodeAccess != -1:
                Previous = NodeAccess
                if NewNode.GetData() < self.__Tree[NodeAccess].GetData():
                    NodeAccess = self.__Tree[NodeAccess].GetLeft()
                    Direction = "left"
                else:
                    NodeAccess = self.__Tree[NodeAccess].GetRight()
                    Direction = "right"
            if Direction == "left":
                self.__Tree[Previous].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[Previous].SetRight(self.__NumberNodes)
            self.__NumberNodes = self.__NumberNodes + 1

    # ---- 2(b)(iii) ----
    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for Count in range(self.__NumberNodes):
                print(self.__Tree[Count].GetLeft(), self.__Tree[Count].GetData(),
                      self.__Tree[Count].GetRight())


if __name__ == "__main__":
    # ---- 2(c)(i) ----
    TheTree = TreeClass()
    # ---- 2(c)(ii) ----
    for Data in [10, 11, 5, 1, 20, 7, 15]:
        TheTree.InsertNode(Node(Data))
    TheTree.OutputTree()
```

按 QP p.9 的顺序插入 10、11、5、1、20、7、15，实际输出如下，与 MS p.27 截图的七行一致。输出按数组存储顺序，不是树的中序遍历。

```text
2 10 1
-1 11 4
3 5 5
-1 1 -1
6 20 -1
-1 7 -1
-1 15 -1
```

另单独调用三个 setter 后通过 getter 读回 `(2, 12, 1)`，确认三次赋值分别落在左指针、数据、右指针；空树输出 `No nodes`，20 格初始化为 20 个独立 Node。

**与 MS 逐点对齐**（2(a)(iii)，3 分；语料 MP 编号与 MS 圆点顺序一致）

| 语料 MP | MS 原文 | 作答对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | 1 set method header (and end) with parameter … | `def SetLeft(self, NewLeft):`，接收一个业务参数 | `getter-setter` |
| 2 | …assigning parameter to correct attribute | `self.__LeftPointer = NewLeft` | `getter-setter` |
| 3 | Remaining 2 correct | SetRight 赋给 RightPointer；SetData 赋给 Data，方法头与参数正确 | `getter-setter` |

**证据格怎么交**　2(a)(iii) 格只贴 Node 内的三个 setter，保留类内缩进；2(a)(ii) 的三个 getter 交在另一个代码格。2(b)(ii) 格交 InsertNode，能看见用 SetLeft / SetRight 更新父结点指针；2(c)(ii) 格交实际创建、插入七个对象和调用 OutputTree 的 main；2(c)(iii) 截图显示上述七行。截图不能代替 setter 代码或调用链核对。

**直观**　Node 是一张结点卡：setter 改卡上的一个格子，getter 读格子；指针格写的是另一张卡在数组里的位置。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s24_42_q2/`；前置 **L12 E01**（存取方法）。

**下一道变式**　⟦9618_s23_41:2(a)(ii)⟧　换回 Vehicle 的四个 getter：GetCurrentSpeed、GetIncreaseAmount、GetMaxSpeed、GetHorizontalPosition 无业务参数，返回原属性；随后 2(a)(iii) 练两个 setter。QP p.4–5；MS p.14–16。代表题与变式来自不同卷。

<!-- auto:drills P4-OP-02 -->

### P4-OP-03　写类的其他方法　{#P4-OP-03}

<!-- auto:stats P4-OP-03 -->

**考法**　在对象方法里按属性计算、判断或改变状态；即使叫 Set…，需要计算工资时也属于本型。

**识别信号**　adds … to current …；cannot exceed …；calculates and stores；creates and returns a string。

**解题思路**
1. 从类图取属性，从方法说明取业务参数；Bird.Move 接方向和分钟数，不重新输入速度。
2. 先换算距离：`Distance = (self.__DistancePerHour / 60) * MinsFlying`。用 `/` 保留小数，不用 `//`。
3. 方向决定改哪个坐标：N/S 改 Y，E/W 改 X；北/东加，南/西减。一次调用只改一个坐标。
4. 方法里修改 `self.__XPosition` / `self.__YPosition`，只给局部变量赋值不会改变这只鸟的位置。
5. Move 只更新状态；GetPosition 返回字符串，主程序负责输出。QP 明说 Move 不必验证参数，输入验证放在 main。

**Python 模板**（本题 Bird；构造、getter 与状态方法完整放在同一类中）

```python
# ---- 1(a)(i) ----
class Bird:
    def __init__(self, pDistancePerHour, pSpecies):
        self.__DistancePerHour = pDistancePerHour  # REAL
        self.__Species = pSpecies                  # STRING
        self.__XPosition = 500.0                    # REAL
        self.__YPosition = 500.0                    # REAL

    # ---- 1(a)(ii) ----
    def GetSpecies(self):
        return self.__Species

    # ---- 1(a)(iii) ----
    def GetPosition(self):
        return "X = " + str(self.__XPosition) + " Y = " + str(self.__YPosition)

    # ---- 1(a)(iv) ----
    def Move(self, Direction, MinsFlying):
        Distance = (self.__DistancePerHour / 60) * MinsFlying
        if Direction == "N":
            self.__YPosition = self.__YPosition + Distance
        elif Direction == "S":
            self.__YPosition = self.__YPosition - Distance
        elif Direction == "E":
            self.__XPosition = self.__XPosition + Distance
        elif Direction == "W":
            self.__XPosition = self.__XPosition - Distance
```

**得分表述**（引自对应 MS）
- 「Method header (and end) taking direction and minutes flying as parameters」⟦9618_w25_42:1(a)(iv)⟧
- 「Calculation of distance using minutes flying parameter and attribute DistancePerHour」⟦9618_w25_42:1(a)(iv)⟧
- 「Selection based on direction parameter …」⟦9618_w25_42:1(a)(iv)⟧
- 「… north adding to YPosition and south subtracting from YPosition」⟦9618_w25_42:1(a)(iv)⟧
- 「… east adding to XPosition and west subtracting from XPosition」⟦9618_w25_42:1(a)(iv)⟧

**得分点地图**（核验语料 2022–2026s、仅主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 15 行，其中 14 行拆点；下表由 `markpoints[].skills` 统计，不是每个标签各值一分）

| 技能标签 | 行数 |
|:--|--:|
| `module-header` | 14 |
| `relational-ops` | 6 |
| `return-value` | 6 |
| `assign-value` | 5 |
| `nested-if` | 5 |
| `operator-precedence` | 3 |

读图、参数、属性与调用方向是本型自查重点；单题分值与 Max 始终回本题 MS 核对。

**易错与失分**　不能把 N/S 改成 X 或把 W 写成加法；分钟不是小时，71 km/h 飞 30 分钟应移动 35.5。Move 中不用 print 代替状态赋值，GetPosition 中不用 print 代替 return。

旧代表题的限速写法另须按同题 MS 判：考官报告讨论超过上限时不再加速的写法（9618_s23_41:2(a)(iv)），但 MS p.17 第 2 点明确接受 remove increase or assign maximum，即超过时**撤销本次增量或赋最大值**都可取该点；ER 的易错描述不覆盖 MS 的接受口径。Vehicle 的推荐实现（OP-01、OP-04、OP-05 的完整作答）采用赋最大值，并在所有路径上更新水平位置；不能把这条单题限速规则套到 Bird 的坐标上。

#### 代表题精讲　⟦9618_w25_42:1(a)(iv)⟧

**在考什么**　Move(Direction, MinsFlying) 用对象速度算距离，再按四方向更新坐标；5 分、5 点。整题 QP p.2–5（p.2 Bird 类图与 500.0 初值，p.3 getters，p.4 Move 与两鸟实参，p.5 main、验证和四次独立测试）；MS p.6–17（Move 清单 p.9、Python 范例 p.10，截图 p.17）。本题不读源文件；TreeData.txt 属于该卷第 3 题。

**完整作答**（整道第 1 题的最终程序；输入顺序是鸟号、分钟、方向；按代码格拆交）

```python
# ---- 1(a)(i) ----
class Bird:
    def __init__(self, pDistancePerHour, pSpecies):
        self.__DistancePerHour = pDistancePerHour  # REAL
        self.__Species = pSpecies                  # STRING
        self.__XPosition = 500.0                    # REAL
        self.__YPosition = 500.0                    # REAL

    # ---- 1(a)(ii) ----
    def GetSpecies(self):
        return self.__Species

    # ---- 1(a)(iii) ----
    def GetPosition(self):
        return "X = " + str(self.__XPosition) + " Y = " + str(self.__YPosition)

    # ---- 1(a)(iv) ----
    def Move(self, Direction, MinsFlying):
        Distance = (self.__DistancePerHour / 60) * MinsFlying
        if Direction == "N":
            self.__YPosition = self.__YPosition + Distance
        elif Direction == "S":
            self.__YPosition = self.__YPosition - Distance
        elif Direction == "E":
            self.__XPosition = self.__XPosition + Distance
        elif Direction == "W":
            self.__XPosition = self.__XPosition - Distance


if __name__ == "__main__":
    # ---- 1(b) ----
    FirstBird = Bird(71.0, "Cockatiel")
    SecondBird = Bird(56.0, "Macaw")
    # ---- 1(c)(i) ----
    print(FirstBird.GetSpecies(), "is currently at", FirstBird.GetPosition())
    print(SecondBird.GetSpecies(), "is currently at", SecondBird.GetPosition())
    Choice = input("Enter 1 for Cockatiel or 2 for Macaw: ")
    while Choice != "1" and Choice != "2":
        Choice = input("Enter 1 or 2: ")
    while True:
        try:
            Time = int(input("Enter flying time in whole minutes (0 to 500): "))
            if Time >= 0 and Time <= 500:
                break
        except ValueError:
            pass
    Direction = input("Enter direction N, S, E or W: ").upper()
    while Direction != "N" and Direction != "S" and Direction != "E" and Direction != "W":
        Direction = input("Enter direction N, S, E or W: ").upper()
    if Choice == "1":
        FirstBird.Move(Direction, Time)
    else:
        SecondBird.Move(Direction, Time)
    print(FirstBird.GetSpecies(), "is currently at", FirstBird.GetPosition())
    print(SecondBird.GetSpecies(), "is currently at", SecondBird.GetPosition())
```

每个测试重新运行程序，让两鸟均从 `(500.0, 500.0)` 起飞。已按 QP p.5 实际运行四次：

| 测试输入（鸟号 / 分钟 / 方向） | Cockatiel 最终 X、Y | Macaw 最终 X、Y |
|:--|:--|:--|
| 1 / 60 / N | 500.0、571.0 | 500.0、500.0 |
| 2 / 30 / S | 500.0、500.0 | 500.0、472.0 |
| 1 / 30 / W | 464.5、500.0 | 500.0、500.0 |
| 2 / 60 / E | 500.0、500.0 | 556.0、500.0 |

四次输出都与 MS p.17 截图一致（第 4 次：Cockatiel 仍在 X = 500.0，Macaw 到 X = 556.0）。另跑无效鸟号 0、时间 −1/501/非整数、方向 Q 后重新输入的路径均可继续到正确结果；0 与 500 分钟边界也已核对。

**与 MS 逐点对齐**（1(a)(iv)，5 分；语料 MP 编号与 MS 圆点顺序一致）

| 语料 MP | MS 原文 | 作答对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Method header (and end) taking direction and minutes flying as parameters | `def Move(self, Direction, MinsFlying):` | `module-header` |
| 2 | Calculation of distance using minutes flying parameter and attribute DistancePerHour | `(self.__DistancePerHour / 60) * MinsFlying` | `operator-precedence` |
| 3 | Selection based on direction parameter … | if / elif 按 Direction 分支 | `nested-if` |
| 4 | … north adding to YPosition and south subtracting from YPosition | N 加 Y，S 减 Y | `nested-if`、`assign-value` |
| 5 | … east adding to XPosition and west subtracting from XPosition | E 加 X，W 减 X | `nested-if`、`assign-value` |

**证据格怎么交**　1(a)(iv) 格贴 Bird 内的 Move，能看到方法头、距离公式和四个分支；1(a)(iii) 另交返回 `X = … Y = …` 的 GetPosition；1(c)(i) 交输入验证、调用所选对象的 Move 和用 getter 输出的 main。1(c)(ii) 要四次独立测试截图，能看见输入和对应输出（MS p.17：第一测试 1 分、第二测试 1 分、第三与第四合计 1 分）；第 4 次按题干展示 Macaw 的更新值，不把截图鸟名错误当作程序目标。

**直观**　速度是每小时的路程，先换成这几分钟走了多远，再决定在平面图上向哪个方向移动。

**对应练习与阶梯**　真题练习 `practice/p4/9618_w25_42_q1/`；前置 **L12 E01**（对象状态与方法）、**L02 E01**（选择分支）。

**下一道变式**　⟦9618_s23_41:2(a)(iv)⟧　Vehicle.IncreaseSpeed 先加速、限制上限，再在所有路径更新水平位置；推荐超过时赋最大值，同时按本题 MS 接受撤销本次增量。QP p.4–5；MS p.17。代表题与变式来自不同卷。

<!-- auto:drills P4-OP-03 -->

### P4-OP-04　继承：声明子类　{#P4-OP-04}

<!-- auto:stats P4-OP-04 -->

**考法**　声明继承已有父类的子类；构造方法先把父类所需参数传上去，再保存子类新增属性。

**识别信号**　child class … inherits from …；calling parent constructor；新增属性与构造参数。

**解题思路**
1. 画清“是一种”：Helicopter 是 Vehicle，所以类头 `class Helicopter(Vehicle):`。
2. 子类构造接收 5 个显式参数：父类的 3 个，再加 VerticalChange 与 MaxHeight。
3. 调用 `super().__init__(IDP, MaxSpeedP, IncreaseAmountP)`；这里只传父类需要的值，且 super 版本不再显式传 self。
4. 子类只声明新增的 3 个私有属性：VerticalPosition 初值 0，另外两个保存参数，并注释 INTEGER。
5. 父类私有属性由父类构造建立；不要在子类重抄同名 `self.__CurrentSpeed`，那会变成子类另一份私有属性。

**Python 模板**（自包含骨架；参数、初值、私有要求照具体题目）

```python
# ---- 2(a)(i) ----
class Vehicle:
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP                           # STRING
        self.__MaxSpeed = MaxSpeedP               # INTEGER
        self.__IncreaseAmount = IncreaseAmountP   # INTEGER
        self.__CurrentSpeed = 0                   # INTEGER
        self.__HorizontalPosition = 0             # INTEGER

    # ---- 2(a)(ii) ----
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    # ---- 2(a)(iii) ----
    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    # ---- 2(a)(iv) ----
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed


# ---- 2(b)(i) ----
class Helicopter(Vehicle):
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VertChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0               # INTEGER
        self.__VerticalChange = VertChangeP       # INTEGER
        self.__MaxHeight = MaxHeightP             # INTEGER
```

**得分表述**（引自对应 MS）
- 「Class header (and end where appropriate) inheriting from Vehicle」⟦9618_s23_41:2(b)(i)⟧
- 「3 (private) attribute declarations with data types」⟦9618_s23_41:2(b)(i)⟧
- 「Constructor (and end where appropriate) with (min) 5 parameters」⟦9618_s23_41:2(b)(i)⟧
- 「Calling parent constructor with appropriate parameters」⟦9618_s23_41:2(b)(i)⟧
- 「Initialising VerticalPosition to 0 and VerticalChange and MaxHeight to attributes」⟦9618_s23_41:2(b)(i)⟧

**得分点地图**（核验语料 2022–2026s、仅主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 6 行，其中 6 行拆点；下表由 `markpoints[].skills` 统计，不是每个标签各值一分）

| 技能标签 | 行数 |
|:--|--:|
| `class-definition` | 6 |
| `constructor` | 6 |
| `inheritance` | 6 |
| `data-types` | 5 |
| `assign-value` | 2 |
| `module-header` | 2 |

读图、参数、属性与调用方向是本型自查重点；单题分值与 Max 始终回本题 MS 核对。

**易错与失分**　考官报告指出，有考生没有使用继承，重新声明全部属性；较强作答会在子类构造中调用父类构造（9618_s23_41:2(b)(i)）。仅写继承类头不会自动运行你重写的子类构造里的父类初始化，仍要明确调用。

#### 代表题精讲　⟦9618_s23_41:2(b)(i)⟧

**在考什么**　Helicopter 的声明与构造，5 分、5 点；本格不需要写其他方法。 整道第 2 题 QP p.4–7（p.4 Vehicle 类图，p.6 Helicopter 类图，p.7 主程序数据）；MS p.12–25。

**完整作答**（整道第 2 题的最终程序；按代码格拆交，不能把整段程序重复贴进每一格）

```python
# ---- 2(a)(i) ----
class Vehicle:
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP                           # STRING
        self.__MaxSpeed = MaxSpeedP               # INTEGER
        self.__IncreaseAmount = IncreaseAmountP   # INTEGER
        self.__CurrentSpeed = 0                   # INTEGER
        self.__HorizontalPosition = 0             # INTEGER

    # ---- 2(a)(ii) ----
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    # ---- 2(a)(iii) ----
    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    # ---- 2(a)(iv) ----
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed


# ---- 2(b)(i) ----
class Helicopter(Vehicle):
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VertChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0               # INTEGER
        self.__VerticalChange = VertChangeP       # INTEGER
        self.__MaxHeight = MaxHeightP             # INTEGER

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    # ---- 2(b)(ii) ----
    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()                   # update horizontal motion in every case


# ---- 2(c) ----
def OutputCurrentPosition(ObjectToOutput):
    print("Current position =", ObjectToOutput.GetHorizontalPosition())
    print("Current speed =", ObjectToOutput.GetCurrentSpeed())
    if isinstance(ObjectToOutput, Helicopter):
        print("Current vertical position =", ObjectToOutput.GetVerticalPosition())


# ---- 2(d)(i) ----
if __name__ == "__main__":
    Car = Vehicle("Tiger", 100, 20)
    Heli = Helicopter("Lion", 350, 40, 3, 100)
    Car.IncreaseSpeed()
    Car.IncreaseSpeed()
    OutputCurrentPosition(Car)
    print()
    Heli.IncreaseSpeed()
    Heli.IncreaseSpeed()
    OutputCurrentPosition(Heli)
```

按 QP p.7 实参实际运行：汽车位置 60、速度 40；直升机位置 120、速度 80、高度 6，与 MS p.25 截图数值一致。另检查第六次汽车加速后速度仍为 100、位置为 400；直升机连续 34 次加速后高度为 100、速度为 350，触顶分支可运行。

**与 MS 逐点对齐**（2(b)(i)，5 分；语料 MP 编号与 MS 圆点顺序一致）

| 语料 MP | MS 原文 | 作答对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Class header (and end where appropriate) inheriting from Vehicle | `class Helicopter(Vehicle):` | `inheritance`、`class-definition` |
| 2 | 3 (private) attribute declarations with data types | 三个新增私有属性及 INTEGER 注释 | `encapsulation`、`data-types` |
| 3 | Constructor (and end where appropriate) with (min) 5 parameters | 子类 __init__，5 个显式参数 | `constructor` |
| 4 | Calling parent constructor with appropriate parameters | `super().__init__` 传前三个参数 | `inheritance` |
| 5 | Initialising VerticalPosition to 0 and VerticalChange and MaxHeight to attributes | VerticalPosition 赋 0，另两属性赋新增参数 | `constructor`、`initialise-variables` |

**证据格怎么交**　2(b)(i) 格交子类类头与构造；不要只交 __init__ 而漏掉括号中的父类。

**直观**　子类像在基础车辆档案上加一页飞行资料：基础档案仍由 Vehicle 填，新页由 Helicopter 填。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s23_41_q2/`。前置 **L12 E03**。

**下一道变式**　⟦9618_s23_42:3(b)(i)⟧　Manager(Employee) 构造另接 BonusValue，调用父类构造传员工编号、时薪、职位三个值，再存奖金百分比。QP p.10；MS p.28–29。

<!-- auto:drills P4-OP-04 -->

### P4-OP-05　重写父类方法（多态）　{#P4-OP-05}

<!-- auto:stats P4-OP-05 -->

**考法**　子类用同名方法替换父类行为；需要保留父类动作时，在子类方法里调用 super().方法()。

**识别信号**　overrides the method from the parent class；同一个方法名，子类规则不同。

**解题思路**
1. 方法名与调用接口照题目：Helicopter 的 IncreaseSpeed 仍无显式参数。
2. 先做子类新增动作：高度增加 VerticalChange，超过 MaxHeight 就封顶。
3. 无论是否封顶，都调用 `super().IncreaseSpeed()` 完成速度与水平位置更新。
4. 不写 `self.IncreaseSpeed()` 来调用父类：这会再次进入当前子类版本，形成无限递归。
5. 主程序仍写 `Heli.IncreaseSpeed()`；Python 按对象的实际类选择子类版本，这就是本题体现的多态。

**Python 模板**（自包含骨架；参数、初值、私有要求照具体题目）

```python
# ---- 2(a)(i) ----
class Vehicle:
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP                           # STRING
        self.__MaxSpeed = MaxSpeedP               # INTEGER
        self.__IncreaseAmount = IncreaseAmountP   # INTEGER
        self.__CurrentSpeed = 0                   # INTEGER
        self.__HorizontalPosition = 0             # INTEGER

    # ---- 2(a)(ii) ----
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    # ---- 2(a)(iii) ----
    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    # ---- 2(a)(iv) ----
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed


# ---- 2(b)(i) ----
class Helicopter(Vehicle):
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VertChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0               # INTEGER
        self.__VerticalChange = VertChangeP       # INTEGER
        self.__MaxHeight = MaxHeightP             # INTEGER

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    # ---- 2(b)(ii) ----
    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()                   # update horizontal motion in every case
```

**得分表述**（引自对应 MS）
- 「Method header (overriding where required) with no parameter」⟦9618_s23_41:2(b)(ii)⟧
- 「Adding vertical change to vertical position …」⟦9618_s23_41:2(b)(ii)⟧
- 「…limiting to maximum height」⟦9618_s23_41:2(b)(ii)⟧
- 「Repeating/calling/using the code from original for horizontal increase (in every case)」⟦9618_s23_41:2(b)(ii)⟧

**得分点地图**（核验语料 2022–2026s、仅主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 7 行，其中 7 行拆点；下表由 `markpoints[].skills` 统计，不是每个标签各值一分）

| 技能标签 | 行数 |
|:--|--:|
| `module-header` | 7 |
| `polymorphism` | 7 |
| `nested-if` | 3 |
| `assign-value` | 2 |
| `inheritance` | 2 |
| `method-call` | 2 |

读图、参数、属性与调用方向是本型自查重点；单题分值与 Max 始终回本题 MS 核对。

**易错与失分**　考官报告指出，有考生高度过大时连水平速度和位置也不更新；较强作答调用父类方法避免重复代码（9618_s23_41:2(b)(ii)）。原 MS p.21 的 Python 封顶分支写了 `MaxHeightP`，它只在构造方法里是参数，本方法不能访问；本作答使用 `self.__MaxHeight`。照 MS 得分；自己写时修正该作用域问题（D44 ④）。

#### 代表题精讲　⟦9618_s23_41:2(b)(ii)⟧

**在考什么**　重写 IncreaseSpeed：4 个独立点，MS 写 to max 4；本题没有多余可选点，四点全要满足。 整道第 2 题 QP p.4–7（p.4 Vehicle 类图，p.6 Helicopter 类图，p.7 主程序数据）；MS p.12–25。

**完整作答**（整道第 2 题的最终程序；按代码格拆交，不能把整段程序重复贴进每一格）

```python
# ---- 2(a)(i) ----
class Vehicle:
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP                           # STRING
        self.__MaxSpeed = MaxSpeedP               # INTEGER
        self.__IncreaseAmount = IncreaseAmountP   # INTEGER
        self.__CurrentSpeed = 0                   # INTEGER
        self.__HorizontalPosition = 0             # INTEGER

    # ---- 2(a)(ii) ----
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    # ---- 2(a)(iii) ----
    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    # ---- 2(a)(iv) ----
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed


# ---- 2(b)(i) ----
class Helicopter(Vehicle):
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VertChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0               # INTEGER
        self.__VerticalChange = VertChangeP       # INTEGER
        self.__MaxHeight = MaxHeightP             # INTEGER

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    # ---- 2(b)(ii) ----
    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()                   # update horizontal motion in every case


# ---- 2(c) ----
def OutputCurrentPosition(ObjectToOutput):
    print("Current position =", ObjectToOutput.GetHorizontalPosition())
    print("Current speed =", ObjectToOutput.GetCurrentSpeed())
    if isinstance(ObjectToOutput, Helicopter):
        print("Current vertical position =", ObjectToOutput.GetVerticalPosition())


# ---- 2(d)(i) ----
if __name__ == "__main__":
    Car = Vehicle("Tiger", 100, 20)
    Heli = Helicopter("Lion", 350, 40, 3, 100)
    Car.IncreaseSpeed()
    Car.IncreaseSpeed()
    OutputCurrentPosition(Car)
    print()
    Heli.IncreaseSpeed()
    Heli.IncreaseSpeed()
    OutputCurrentPosition(Heli)
```

按 QP p.7 实参实际运行：汽车位置 60、速度 40；直升机位置 120、速度 80、高度 6，与 MS p.25 截图数值一致。另检查第六次汽车加速后速度仍为 100、位置为 400；直升机连续 34 次加速后高度为 100、速度为 350，触顶分支可运行。

**与 MS 逐点对齐**（2(b)(ii)，4 分；语料 MP 编号与 MS 圆点顺序一致；MS 写 to max 4）

| 语料 MP | MS 原文 | 作答对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Method header (overriding where required) with no parameter | Helicopter 内同名 `IncreaseSpeed(self)` | `polymorphism`、`module-header` |
| 2 | Adding vertical change to vertical position … | 先增加 VerticalPosition | `assign-value` |
| 3 | …limiting to maximum height | 比较并限制到 self.__MaxHeight | `relational-ops`、`nested-if` |
| 4 | Repeating/calling/using the code from original for horizontal increase (in every case) | if 外 `super().IncreaseSpeed()`，所有路径都做水平变化 | `inheritance`、`polymorphism` |

**证据格怎么交**　2(b)(ii) 格交子类同名方法；2(c) 格另交 OutputCurrentPosition。后者只在实际对象为 Helicopter 时多输出高度，MS 的 `//` 表示替代方案，不是额外分。

**直观**　同一个“加速”按钮装在汽车和直升机上，汽车只向前，直升机还上升；调用按钮的语句不用改。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s23_41_q2/`。前置 **L12 E03、L12 E05**。

**下一道变式**　⟦9618_s23_42:3(b)(ii)⟧　Manager.SetPay 先把小时数变为 `Hours * (1 + BonusValue / 100)`，再调用父类 SetPay，不能只乘 BonusValue。QP p.10；MS p.29。

<!-- auto:drills P4-OP-05 -->

### P4-OP-06　包含：容器类　{#P4-OP-06}

<!-- auto:stats P4-OP-06 -->

**考法**　一个类包含另一类的对象数组，并写存取、追加或展示这些对象的方法。

**识别信号**　Hand has Cards : ARRAY[0:9] OF Card；constructor takes five Card objects；AddTrain、GetObject。

**解题思路**
1. 分清“有”和“是”：Hand 有 Card 对象，Hand 不是一种 Card；写独立 `class Hand:`，不用继承。
2. 真实创建 10 格私有数组 `self.__Cards = [None] * 10`，注释元素类型 Card 与大小。None 表示尚未放牌的槽位，不是假造 10 张相同的牌。
3. 构造参数是五个 Card 对象，把它们分别放到 0–4；FirstCard 固定 0、NumberCards 固定 5。
4. GetCard(Position) 返回数组中的 Card 对象，调用者再对这张牌调用 GetNumber / GetColour。
5. 如果题目要求每格初始化成一个对象，要在循环内每次新建对象，不能 `[Card(...)] * 10` 共享同一个实例。若要 Add，先判满，成功存入后再加计数。

**Python 模板**（自包含骨架；参数、初值、私有要求照具体题目）

```python
# ---- 2(a)(i) ----
class Card:
    def __init__(self, NumberP, ColourP):
        self.__Number = NumberP     # INTEGER
        self.__Colour = ColourP     # STRING

    # ---- 2(a)(ii) ----
    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


# ---- 2(b)(i) ----
class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = [None] * 10   # Card, 10 elements; unused slots are None
        self.__Cards[0] = Card1
        self.__Cards[1] = Card2
        self.__Cards[2] = Card3
        self.__Cards[3] = Card4
        self.__Cards[4] = Card5
        self.__FirstCard = 0         # INTEGER
        self.__NumberCards = 5       # INTEGER

    # ---- 2(b)(ii) ----
    def GetCard(self, Position):     # Position : INTEGER, returns Card
        return self.__Cards[Position]
```

**得分表述**（引自对应 MS）
- 「class Hand declaration (and end where appropriate)」⟦9618_w22_41:2(b)(i)⟧
- 「private attribute declarations; FirstCard as integer, NumberCards as integer」⟦9618_w22_41:2(b)(i)⟧
- 「private attribute array named Cards of type Card with 10 elements」⟦9618_w22_41:2(b)(i)⟧
- 「constructor with 5 Card objects as parameters」⟦9618_w22_41:2(b)(i)⟧
- 「assigning each Card parameter to the array (in constructor)」⟦9618_w22_41:2(b)(i)⟧

**得分点地图**（核验语料 2022–2026s、仅主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 13 行，其中 12 行拆点；下表由 `markpoints[].skills` 统计，不是每个标签各值一分）

| 技能标签 | 行数 |
|:--|--:|
| `array-of-objects` | 9 |
| `module-header` | 8 |
| `getter-setter` | 5 |
| `return-value` | 5 |
| `array-2d` | 4 |
| `class-definition` | 4 |

读图、参数、属性与调用方向是本型自查重点；单题分值与 Max 始终回本题 MS 核对。

**易错与失分**　考官报告指出，有考生把 Hand 写成 Card 的子类；还有考生给 Hand 构造传数字和颜色，而不是五个 Card 对象（9618_w22_41:2(b)(i)、2(b)(iii)）。MS p.11 的 Python 范例只 append 五次，没有真正建出题给的 10 格；本作答建足 10 格。p.13 的 CalculateValue 范例 `range(0, 4)` 漏第五张牌，本作答用 range(5)；按 QP 与语言无关得分点写（D10、D31）。

#### 代表题精讲　⟦9618_w22_41:2(b)(i)⟧

**在考什么**　Hand 类声明与构造，6 分、6 点；类图在 QP p.4，写代码要求在 p.6。 整道第 2 题 QP p.4–7（p.4 两张类图，p.5 测试卡表）；MS p.8–15。

**完整作答**（整道第 2 题的最终程序；按代码格拆交，不能把整段程序重复贴进每一格）

```python
# ---- 2(a)(i) ----
class Card:
    def __init__(self, NumberP, ColourP):
        self.__Number = NumberP     # INTEGER
        self.__Colour = ColourP     # STRING

    # ---- 2(a)(ii) ----
    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


# ---- 2(b)(i) ----
class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = [None] * 10   # Card, 10 elements; unused slots are None
        self.__Cards[0] = Card1
        self.__Cards[1] = Card2
        self.__Cards[2] = Card3
        self.__Cards[3] = Card4
        self.__Cards[4] = Card5
        self.__FirstCard = 0         # INTEGER
        self.__NumberCards = 5       # INTEGER

    # ---- 2(b)(ii) ----
    def GetCard(self, Position):     # Position : INTEGER, returns Card
        return self.__Cards[Position]


# ---- 2(c)(i) ----
def CalculateValue(Player):         # Player : Hand, returns INTEGER
    Score = 0
    for Count in range(5):
        CardGot = Player.GetCard(Count)
        Score = Score + CardGot.GetNumber()
        Colour = CardGot.GetColour()
        if Colour == "red":
            Score = Score + 5
        elif Colour == "blue":
            Score = Score + 10
        elif Colour == "yellow":
            Score = Score + 15
    return Score


if __name__ == "__main__":
    # ---- 2(a)(iii) ----
    OneRed = Card(1, "red")
    TwoRed = Card(2, "red")
    ThreeRed = Card(3, "red")
    FourRed = Card(4, "red")
    FiveRed = Card(5, "red")
    OneBlue = Card(1, "blue")
    TwoBlue = Card(2, "blue")
    ThreeBlue = Card(3, "blue")
    FourBlue = Card(4, "blue")
    FiveBlue = Card(5, "blue")
    OneYellow = Card(1, "yellow")
    TwoYellow = Card(2, "yellow")
    ThreeYellow = Card(3, "yellow")
    FourYellow = Card(4, "yellow")
    FiveYellow = Card(5, "yellow")
    # ---- 2(b)(iii) ----
    Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, OneYellow)
    Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue)
    # ---- 2(c)(ii) ----
    Player1score = CalculateValue(Player1)
    Player2score = CalculateValue(Player2)
    if Player1score > Player2score:
        print("Player 1 wins")
    elif Player1score < Player2score:
        print("Player 2 wins")
    else:
        print("It's a draw")
```

在 QP 的 15 张牌及两组手牌上实际运行，输出 `Player 2 wins`，与 MS p.15 一致。直接调用 CalculateValue 得到玩家 1 为 46、玩家 2 为 85；第五张牌实际参与，数组确有 10 格。

**与 MS 逐点对齐**（2(b)(i)，6 分；语料 MP 编号与 MS 圆点顺序一致）

| 语料 MP | MS 原文 | 作答对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | class Hand declaration (and end where appropriate) | `class Hand:` | `class-definition` |
| 2 | private attribute declarations; FirstCard as integer, NumberCards as integer | FirstCard、NumberCards 私有且注释 INTEGER | `encapsulation`、`data-types` |
| 3 | private attribute array named Cards of type Card with 10 elements | self.__Cards 为 10 格 Card 槽位、私有 | `containment`、`array-of-objects`、`declare-array` |
| 4 | constructor with 5 Card objects as parameters | __init__ 接五个 Card 对象 | `constructor` |
| 5 | assigning each Card parameter to the array (in constructor) | 参数逐个赋给 Cards[0]…Cards[4] | `constructor`、`array-of-objects` |
| 6 | initialising FirstCard to 0 and NumberCards to 5 (in constructor) | FirstCard 设 0，NumberCards 设 5 | `constructor`、`initialise-variables` |

**证据格怎么交**　2(b)(i) 格交 Hand 类头、三个属性的初始化和构造；2(b)(ii) 格另交 GetCard；2(c)(iii) 截图应显示 Player 2 wins。

**直观**　一只牌盒有十个槽位，先装进五张牌；拿到某个槽位里的牌，再问那张牌的数字与颜色。牌盒本身不是一张牌。

**对应练习与阶梯**　真题练习 `practice/p4/9618_w22_41_q2/`。前置 **L12 E04**。

**下一道变式**　⟦9618_w25_41:2(c)(i)⟧　Station 包含 Train 数组，构造保存站号与站台数；NumberTrains 初值 0。接着练 2(c)(ii) 的 AddTrain：满时 False，存入并更新个数后 True。QP p.6–7；MS p.18–20。

<!-- auto:drills P4-OP-06 -->

### P4-OP-07　创建对象并调用方法　{#P4-OP-07}

<!-- auto:stats P4-OP-07 -->

**考法**　在主程序或普通模块中实例化对象，用该对象的方法更新状态并取值输出。

**识别信号**　instantiate … with the identifier …；with correct parameters；call … twice；using get methods。

**解题思路**
1. 对照题表，把每一个对象的类、变量名、实参顺序和类型写清；Chewie 是 Parrot，Nighteyes 是 Wolf，Copper 用 Animal。
2. 先创建并保存对象，再对这些对象调用方法；不要把类名覆盖成对象变量名。
3. `SetTerritorySize(Change)` 的动作是加上 Change，减少 20 就传 −20；不能传 +20，也不能只在外部直接改属性。
4. 在 Chewie 上调用 ChangeNumberWords(2)，再输出所有动物更新后的 Description 返回值。
5. `Animal1.Description()` 生成字符串但不会显示；写 `print(Animal1.Description())`。主程序不重写一份描述文字来代替真实方法调用。

**Python 模板**（自包含骨架；参数、初值、私有要求照具体题目）

```python
class Counter:
    def __init__(self, ValueP):
        self.__Value = ValueP  # INTEGER

    def Increase(self):
        self.__Value = self.__Value + 1

    def GetValue(self):
        return self.__Value


if __name__ == "__main__":
    Item = Counter(0)
    Item.Increase()
    print(Item.GetValue())
```

**得分表述**（引自对应 MS）
- 「Calling SetTerritorySize(-20) for instance of Nighteyes」⟦9618_s25_42:3(d)(ii)⟧
- 「Calling ChangeNumberWords(2) for instance of Chewie」⟦9618_s25_42:3(d)(ii)⟧
- 「Calling Description() for all 3 animals (after any updates) and outputting return values」⟦9618_s25_42:3(d)(ii)⟧

**得分点地图**（核验语料 2022–2026s、仅主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 36 行，其中 32 行拆点；下表由 `markpoints[].skills` 统计，不是每个标签各值一分）

| 技能标签 | 行数 |
|:--|--:|
| `object-instantiation` | 21 |
| `method-call` | 18 |
| `output-format` | 14 |
| `getter-setter` | 8 |
| `array-of-objects` | 4 |
| `input-prompt` | 4 |

读图、参数、属性与调用方向是本型自查重点；单题分值与 Max 始终回本题 MS 核对。

**易错与失分**　考官报告指出，有考生直接改对象属性而不调用更新方法，或调用 Description 后没有输出返回值（9618_s25_42:3(d)(ii)）；还有考生把三个对象都建成 Animal，或把对象变量命名成类名（9618_s25_42:3(d)(i)）。遍历对象数组按顺序输出、getter 只是取值手段时，入口是 AR-04；本题型看实例化和方法调用的主要得分点（D43）。

#### 代表题精讲　⟦9618_s25_42:3(d)(ii)⟧

**在考什么**　main 针对 Wolf 与 Parrot 调用不同的状态方法，再对三个动物调用同名 Description 并输出返回值；3 分、3 点。整题 QP p.9–12（p.9 Animal 类图与描述格式，p.10 Parrot 类图，p.11 Wolf 类图，p.12 创建实参与 main）；MS p.33–45（本行清单及 Python 范例 p.44，截图 p.45）。不读取文件，全部数据来自 QP p.12。

**完整作答**（整道第 3 题的最终程序；按代码格拆交）

```python
# ---- 3(a)(i) ----
class Animal:
    def __init__(self, pName, pSound, pSize, pIntelligence):
        self.Name = pName                  # STRING
        self.Sound = pSound                # STRING
        self.Size = pSize                  # INTEGER
        self.Intelligence = pIntelligence  # INTEGER

    # ---- 3(a)(ii) ----
    def Description(self):
        Message = "The animal's name is " + self.Name + ", it makes a " + self.Sound
        Message = Message + ", its size is " + str(self.Size)
        Message = Message + " and its intelligence level is " + str(self.Intelligence)
        return Message


# ---- 3(b)(i) ----
class Parrot(Animal):
    def __init__(self, pName, pSound, pSize, pIntelligence, pWingSpan, pNumberWords):
        super().__init__(pName, pSound, pSize, pIntelligence)
        self.WingSpan = pWingSpan        # INTEGER
        self.NumberWords = pNumberWords  # INTEGER

    def ChangeNumberWords(self, Change):
        self.NumberWords = self.NumberWords + Change

    # ---- 3(b)(ii) ----
    def Description(self):
        Message = super().Description() + ". It has a wingspan of " + str(self.WingSpan)
        Message = Message + "cm and can say " + str(self.NumberWords) + " words."
        return Message


# ---- 3(c)(i) ----
class Wolf(Animal):
    def __init__(self, pName, pSound, pSize, pIntelligence, pTerritorySize):
        super().__init__(pName, pSound, pSize, pIntelligence)
        self.TerritorySize = pTerritorySize  # INTEGER

    def SetTerritorySize(self, Change):
        self.TerritorySize = self.TerritorySize + Change

    # ---- 3(c)(ii) ----
    def Description(self):
        return super().Description() + ". Its territory is " + str(self.TerritorySize) + " square miles."


if __name__ == "__main__":
    # ---- 3(d)(i) ----
    Animal1 = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
    Animal2 = Wolf("Nighteyes", "Howl", 8, 7, 100)
    Animal3 = Animal("Copper", "Neigh", 10, 6)
    # ---- 3(d)(ii) ----
    Animal2.SetTerritorySize(-20)
    Animal1.ChangeNumberWords(2)
    print(Animal1.Description())
    print(Animal2.Description())
    print(Animal3.Description())
```

实际运行得到三个完整描述：Chewie / Squawk / size 1 / intelligence 10 / wingspan 30cm / **31 words**；Nighteyes / Howl / size 8 / intelligence 7 / **80 square miles**；Copper / Neigh / size 10 / intelligence 6。全部字段与 MS p.45 截图一致。运行调用记录另核对 Wolf.SetTerritorySize 的 Change=−20、Parrot.ChangeNumberWords 的 Change=2，以及更新后调用三个对象的 Description；确认输出包含各返回字符串。

MS p.40 清单中简写 Territory / SetTerritory，QP p.11 和 MS p.41 Python 用 TerritorySize / SetTerritorySize，本程序统一按后者。MS p.42 Python 范例用 `it's territory is`，QP p.11 要 `. Its territory is `；程序按 QP 格式与 MS 语言无关得分点写，不照抄范例笔误。

**与 MS 逐点对齐**（3(d)(ii)，3 分；语料 MP 编号与 MS 圆点顺序一致）

| 语料 MP | MS 原文 | 作答对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Calling SetTerritorySize(-20) for instance of Nighteyes | `Animal2.SetTerritorySize(-20)`，100 加 −20 得 80 | `method-call` |
| 2 | Calling ChangeNumberWords(2) for instance of Chewie | `Animal1.ChangeNumberWords(2)`，29 加 2 得 31 | `method-call` |
| 3 | Calling Description() for all 3 animals (after any updates) and outputting return values | 更新后分别 `print(Animal1.Description())`、Animal2、Animal3；动态选择各自实现 | `method-call`、`output-format`、`polymorphism` |

**证据格怎么交**　3(d)(i) 格交三个对象的实例化；3(d)(ii) 格交两次更新与三次 print 调用，能看见对象、参数符号及先更新后取描述的顺序；3(d)(iii) 截图显示三个完整描述，尤其 31 words 与 80 square miles（MS p.45 两分：三条完整准确信息；正确更新值）。类、构造、Description 分别交 3(a)–(c) 的对应代码格。截图里的正确数字不能证明调用已经发生，代码也须逐项核对（D46）。

**直观**　先让狼缩小领地、让鹦鹉学两词，再请每只动物介绍自己；介绍来自对象当前状态。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s25_42_q3/`；前置 **L12 E01、L12 E03、L12 E05**（对象方法、继承、多态）。

**下一道变式**　⟦9618_s23_41:2(d)(i)⟧　创建 Vehicle("Tiger", 100, 20) 与 Helicopter("Lion", 350, 40, 3, 100)，各加速两次并输出。QP p.7；MS p.24–25。不同卷练习“先创建、再调用、最后输出”的同一条链。

<!-- auto:drills P4-OP-07 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| 属性、参数、局部变量 | 属性随对象保留；参数是本次输入；局部变量只在模块内使用 | `self.__X` 与 `XP` |
| getter 与输出 | getter return，主程序 print；不是用 print 替代 return | MS 的 returning |
| OP-02 与 OP-03 | 直接取值/存值是 OP-02；按状态计算工资、年龄等是 OP-03，不能只按 Set/Get 前缀判断 | 方法实际动作 |
| OP-04 与 OP-06 | “是一种”才继承；“有对象数组”用包含 | Helicopter 是 Vehicle；Hand 有 Card |
| OP-03 与 OP-05 | 普通状态方法是 OP-03；子类同名重写是 OP-05 | overrides parent |
| super 与 self | super 指向父类实现；self 的同名调用会选到子类版本 | 在重写方法内部是否会重复调用自己 |
| OP 与 LT | 类的方法实现链表/树的插入、删除、遍历时按 ADT 操作进 LT | InsertNode、Traverse 的操作 |
| OP-07 与 AR-04 | 实例化/方法调用承担主要得分点 → OP-07；按下标遍历输出对象数组 → AR-04（D43） | getter 是目的还是取值手段 |
