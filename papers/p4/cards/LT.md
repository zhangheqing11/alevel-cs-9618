## LT　链表、二叉树与哈希表 {#ch-LT}

<!-- auto:chapter-stats -->

### 核心思想

LT 是 P4 第 2、3 题常见的“数据结构大题”：链表（LT-01、LT-02）、二叉树（LT-03、LT-04）、哈希表（LT-05）。一道大题通常 20–30 分，前面是声明与初始化，中间是插入、删除或查找，后面是遍历输出与截图。核验语料里每种结构只在 2–5 份卷里出现，但一旦出现就是整道大题，分值集中。

三种结构都有两种实现，题目会说清楚用哪一种，**照题目的数据结构写，不要换**：

| 结构 | 数组实现（下标作指针，空指针多为 –1） | 对象实现（结点对象互相引用，空用 `None`） |
|:--|:--|:--|
| 链表 | 二维数组 `LinkedList[i][0]` 数据、`[i][1]` 指针 + `FirstNode`、`FirstEmpty`（9618_w24_41） | `Node` 类（TheData、NextNode）+ `LinkedList` 类（HeadNode）（9618_s25_43） |
| 二叉树 | 二维数组 `[i][0]` 左指针、`[i][1]` 数据、`[i][2]` 右指针 + `RootPointer`、`FreeNode`（9618_w22_41、9618_w25_42） | `Node` 类（LeftNode、RightNode 是结点）（9618_s25_41），或 `Node` 对象数组 + 整数指针（9618_s24_42） |
| 哈希表 | 一维记录数组 + 溢出数组 `Spare`（9618_s25_42），或二维数组（每个散列值一行）（9618_w25_41） | — |

一句话主线：**指针就是“下一个去哪”**。数组实现里指针是下标，`CurrentPointer = LinkedList[CurrentPointer][1]`；对象实现里指针是对象引用，`Current = Current.GetNextNode()`。所有遍历都是“从起点出发、沿指针走、直到空指针”；所有插入都是“拿一个空结点 → 存数据 → 改指针”。

P4 与 P2 / P3 的分界：P2-DT-15 / DT-16、P3-CT-08 / CT-09 在纸上画指针图、补伪代码；P4 用 Python 上机实现，并用题给数据跑出结果截图。AS 的伪代码常用 1 起数组和 0 作空指针，P4 几乎都是 0 起下标、–1 作空指针——**以本题题干为准**。

### 题型树
<!-- auto:type-tree -->

### P4-LT-01　链表：声明初始化与遍历　{#P4-LT-01}

<!-- auto:stats P4-LT-01 -->

**考法**　①声明链表的二维数组（结点数 × 2）、起始指针与空闲表指针，按题给表初始化：数据全 –1、每个结点指向下一个、最后一个指针 –1（2–5 分）；②写遍历过程：从起始指针出发，沿指针输出每个结点的数据，到 –1 停（2–4 分）；③同样遍历空闲表；④对象实现：从 `HeadNode` 出发，用 `GetNextNode()` 走到 `None`，把数据拼成一个用空格分隔的字符串返回（3 分）。

**识别信号**　linked list；2D array … first dimension stores the data, second dimension stores the pointer；FirstNode / StartLinkedList、FirstEmpty / StartEmptyList；A pointer of –1 identifies that node as the last node；outputs the data in the linked list in order by following the pointers；Traverse() concatenates the integer data from the nodes。

**解题思路**
1. **初始化空闲表**：照题干的表——通常 `LinkedList[i] = [-1, i + 1]`，最后一个结点的指针改成 –1；起始指针 –1（空链表）、空闲表指针 0。题目给了具体数据表时（如 9618_s26_42），按表逐行赋值，起始指针、空闲指针照题给值。
2. **遍历模板**：`Current = 起始指针` → `while Current != -1:` → 处理 `LinkedList[Current][0]` → `Current = LinkedList[Current][1]`。先判断再访问，空链表时什么也不输出。
3. **对象实现**：`Current = self.__HeadNode` → `while Current != None:` → 处理 `Current.GetData()` → `Current = Current.GetNextNode()`。数据要用 getter 取（属性是私有的）。
4. **拼字符串**时数字先 `str()`，按题目要求的分隔符拼接，最后 `return`（循环外）。
5. 遍历**不改任何指针**：用局部变量 `Current` 走，不要动 `FirstNode`。

**Python 模板**

```python
LinkedList = []                    # INTEGER, 20 x 2: [i][0] data, [i][1] pointer
for x in range(20):
    LinkedList.append([-1, x + 1])   # empty list: every node points to the next
LinkedList[19][1] = -1             # last node
FirstNode = -1                     # INTEGER, start of the data list (empty)
FirstEmpty = 0                     # INTEGER, start of the empty list


def OutputLinkedList():
    Current = FirstNode
    while Current != -1:
        print(LinkedList[Current][0])
        Current = LinkedList[Current][1]
```

对象实现的遍历（`Node` 有 `GetData()`、`GetNextNode()`）：

```python
class LinkedList:
    def __init__(self):
        self.__HeadNode = None          # Node, None = empty list

    def Traverse(self):                 # returns STRING
        Result = ""
        Current = self.__HeadNode
        while Current != None:
            if Result != "":
                Result = Result + " "           # a space between values, none at the end
            Result = Result + str(Current.GetData())
            Current = Current.GetNextNode()
        return Result
```

**得分表述**（引自对应 MS）
- 「LinkedList declared as 2D array with (min) 20 × 2 elements (Integer) with all data initialised to -1, all nodes linked correctly」⟦9618_w24_41:3(a)⟧
- 「(Global) FirstNode (Int) initialised as -1 and (global) FirstEmpty (Int) initialised as 0」⟦9618_w24_41:3(a)⟧
- 「Following pointers until end reached and outputting data for each node」⟦9618_w24_41:3(c)(i)⟧
- 「Starts at head node and follows nodes using GetNextNode() until no nodes left …」⟦9618_s25_43:3(b)(iii)⟧
- 「… concatenates the data from each node and formats correctly」⟦9618_s25_43:3(b)(iii)⟧

**得分点地图**（口径：核验语料 2022–2026s、主题型为 LT-01 的行、去掉 `equivalent_of`，同一行同一标签计一次；s26 只进计数。共 6 行，全部拆了得分点，来自 3 份卷；“行数”为出现该标签的行数，脚本按 `markpoints[].skills` 统计）

| 技能标签 | 行数 | MS 常见写法 |
|:--|--:|:--|
| `linked-list` | 6 | starting at FirstNode / StartLinkedList；following pointers；all nodes linked correctly |
| `module-header` | 4 | Procedure header (and end) |
| `array-2d`、`pre-condition-loop`、`output-format` | 各 3 | 2D array with 20 × 2 elements；stopping when null pointer；outputting data of each node |
| `declare-array`、`global-scope`、`initialise-variables` | 各 2 | (Global) FirstNode … initialised as -1 |

**几乎每次都有的分**：“从起始指针出发”与“沿指针走到 –1 / None 并输出每个结点”——遍历题两三分全在这两句上。

**易错与失分**
- 二维数组建反：考官报告指出有考生建成 2 个元素、每个 20 格，而不是 20 个结点、每个 2 格（9618_w24_41:3(a)）；也有只写注释、没真正建出数组的。
- 遍历时不用二维数组、改去访问一维数组（9618_w24_41:3(c)(i) 的考官报告）。
- 对象实现只返回 HeadNode 的数据、不往下走（9618_s25_43:3(b)(iii) 的考官报告）；返回语句写进循环里，只拼了第一个。
- 起始指针、空闲指针初值写错或写反（9618_w24_41:3(a) 的考官报告）。
- 用 `while LinkedList[Current][1] != -1` 判断：最后一个结点不会输出。判断的应是 `Current` 本身。

#### 代表题精讲　⟦9618_w24_41:3(c)(i)⟧

**在考什么**　链表把正整数存在全局二维数组 `LinkedList` 里：第一维下标是结点，`[i][0]` 存数据、`[i][1]` 存下一个结点的下标；可存 20 个结点；空结点数据为 –1，最后一个结点指针为 –1。`FirstEmpty` 是空闲表第一个结点（初值 0），`FirstNode` 是链表第一个结点（初值 –1）。3(c)(i) OutputLinkedList()：从 `FirstNode` 出发沿指针按顺序输出数据。2 分，MS 2 点。同一大题：3(a) 声明与初始化（2 分，LT-01）、3(b) InsertData() 表头插入（LT-02 的代表题）、3(c)(ii) 主程序调用、3(c)(iii) 截图、3(d)(i) RemoveData() 删除（LT-02）、3(d)(ii)(iii) 主程序与截图。讲解时请对照原卷 QP p.12（题干与初始化表、3(a)）、p.13（3(b) 的插入步骤表）、p.14（3(c)）、p.15（3(d)）；MS p.26–37。

**完整作答**（整道第 3 题的程序；`Question3_N24.py`）

```python
# ---- 3(a) ----
LinkedList = []                    # INTEGER, 20 x 2: [node][0] = data, [node][1] = pointer
for x in range(0, 20):
    LinkedList.append([-1, x + 1])   # every node points to the next one
LinkedList[19][1] = -1             # the last node ends the empty list
FirstNode = -1                     # INTEGER, no data yet
FirstEmpty = 0                     # INTEGER, first node of the empty list


# ---- 3(b) ----
def InsertData():
    global FirstNode, FirstEmpty
    for Count in range(5):
        if FirstEmpty == -1:                       # full: end the procedure
            return
        NewItem = int(input("Enter a positive integer "))
        NextEmpty = LinkedList[FirstEmpty][1]      # remember the rest of the empty list
        LinkedList[FirstEmpty][0] = NewItem        # store the data
        LinkedList[FirstEmpty][1] = FirstNode      # new node points to the old first node
        FirstNode = FirstEmpty                     # new node is now the first node
        FirstEmpty = NextEmpty


# ---- 3(c)(i) ----
def OutputLinkedList():
    CurrentPointer = FirstNode
    while CurrentPointer != -1:                    # -1 = end of the list
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = LinkedList[CurrentPointer][1]


# ---- 3(d)(i) ----
def RemoveData(ItemToRemove):
    global FirstNode, FirstEmpty
    if LinkedList[FirstNode][0] == ItemToRemove:   # the first node is removed
        Removed = FirstNode
        FirstNode = LinkedList[FirstNode][1]
    else:
        PreviousPointer = FirstNode
        CurrentPointer = LinkedList[FirstNode][1]
        Found = False
        while Found == False:                      # the item is in the list (QP)
            if LinkedList[CurrentPointer][0] == ItemToRemove:
                Found = True
            else:
                PreviousPointer = CurrentPointer
                CurrentPointer = LinkedList[CurrentPointer][1]
        LinkedList[PreviousPointer][1] = LinkedList[CurrentPointer][1]   # skip the node
        Removed = CurrentPointer
    LinkedList[Removed][0] = -1                    # give the node back to the empty list
    LinkedList[Removed][1] = FirstEmpty
    FirstEmpty = Removed


# ---- main program ----
if __name__ == "__main__":
    # 3(c)(ii)
    InsertData()
    OutputLinkedList()
    # 3(d)(ii)
    RemoveData(5)
    print("After")
    OutputLinkedList()
```

用 QP 的三组测试数据实际运行：输入 5 1 2 3 8，删除前输出 8 3 2 1 5（MS 3(c)(iii)「output of 8 3 2 1 5」⟦9618_w24_41:3(c)(iii)⟧）；输入 5 6 8 9 5，After 之后输出 9 8 6 5；输入 10 7 8 5 6，After 之后输出 6 8 7 10（MS 3(d)(iii) 两组都一致）。另用 Python 直接调用：空链表遍历什么也不输出；插满 20 个后 `FirstEmpty` 为 –1，再调用 InsertData 不读输入、不存；删除第一个、最后一个、中间结点后遍历正确，被删的 3 个结点能被下一次插入重新用上。

**与 MS 逐点对齐**（3(c)(i)，2 分，MS 2 点，编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure header (and end) starting with node at index FirstNode and outputting data LinkedList[FirstNode,0] | `def OutputLinkedList():`；`CurrentPointer = FirstNode`；`print(LinkedList[CurrentPointer][0])` | `module-header`、`linked-list`、`output-format` |
| 2 | Following pointers until end reached and outputting data for each node | `while CurrentPointer != -1:`、`CurrentPointer = LinkedList[CurrentPointer][1]` | `linked-list`、`pre-condition-loop`、`output-format` |

同题 3(a)（2 分）：二维数组 20 × 2、数据全 –1 且结点依次相连 / 两个全局指针初值 –1 与 0。

**MS 范例的两处缺陷**（照 MS 得分；自己写时按模板，D44 ④）：①3(a) 的 Python 范例只循环 `range(0, 19)` 建了 19 个结点，接着写 `LinkedList[19][0] = -1`，运行会 `IndexError`（MS p.27）；本作答循环 20 次再改最后一个指针。②3(c)(i) 的范例先输出再判断，链表为空时会去读 `LinkedList[-1]`（Python 里是最后一行，不报错但输出错）；本作答先判断 `!= -1` 再访问。

**证据格怎么交**　3(a) 与 3(c)(i) 各一格代码；3(a) 写在主程序里也可以（题目说 “for the main program”），但要看得出是全局变量。截图格见 MP-03：3(c)(iii) 要同时看到输入 5 1 2 3 8 与输出 8 3 2 1 5。

**直观**　链表像寻宝游戏：每个格子里有一件宝物和一张写着“下一站是几号格子”的纸条。从 `FirstNode` 号格子出发，读宝物、看纸条、去下一站，纸条写 –1 就结束。格子的物理顺序无所谓，纸条决定顺序。

**对应练习与阶梯**　真题练习 `practice/p4/9618_w24_41_q3/`（整道第 3 题）。前置阶梯 **L10 E01**（追踪链表）、**L10 E02**（初始化空闲表、表头插入、遍历输出）。

**下一道变式**　⟦9618_s25_43:3(b)(iii)⟧　（对象实现的链表：`LinkedList` 类的 Traverse() 从 `HeadNode` 出发，用 `GetNextNode()` 一直走到空，把每个结点的整数数据用空格拼成一个字符串返回。要点：`Current` 是对象不是下标，空是 `None`；数据用 getter 取；`return` 在循环外。讲解时请对照原卷 QP p.9。）

<!-- auto:drills P4-LT-01 -->

### P4-LT-02　链表：插入与删除结点　{#P4-LT-02}

<!-- auto:stats P4-LT-02 -->

**考法**　①数组实现、插在表头：判满（空闲表指针为 –1）→ 从空闲表取结点 → 存数据 → 新结点指向原第一个结点 → 更新起始指针与空闲指针（6 分，9618_w24_41:3(b)）；②数组实现、删除：先看第一个结点，否则沿指针找并记住前一个结点，找到后让前一个结点跳过它，把它还给空闲表（5 分，9618_w24_41:3(d)(i)）；③对象实现、插在表头：新建 Node、`SetNextNode(HeadNode)`、`HeadNode` 换成新结点（4 分，9618_s25_43:3(b)(ii)）；④对象实现、删除：空表返回 FALSE；表头匹配就把 `HeadNode` 换成下一个；否则沿结点找，找到让前一个结点的 `NextNode` 跳过它并返回 TRUE，走到底返回 FALSE（6 分，9618_s25_43:3(b)(iv)）。

**识别信号**　inserts … into the linked list；Each data item is inserted at the front of the linked list；FirstEmpty = –1 means full；removes a node from the linked list … added to the empty list；InsertNode() … uses the new node's method SetNextNode()；RemoveNode() … returns FALSE if the linked list is empty。

**解题思路**
1. **表头插入四步（数组）**，顺序不能乱：
   ① 判满 `FirstEmpty == -1` → 结束；
   ② `NextEmpty = LinkedList[FirstEmpty][1]`（先记下空闲表的下一个，后面会被覆盖）；
   ③ `LinkedList[FirstEmpty][0] = 数据`，`LinkedList[FirstEmpty][1] = FirstNode`；
   ④ `FirstNode = FirstEmpty`，`FirstEmpty = NextEmpty`。
2. **删除（数组）**：
   - 第一个结点就是目标：`FirstNode = LinkedList[FirstNode][1]`；
   - 否则用两个指针 `Previous`、`Current` 往下走，找到后 `LinkedList[Previous][1] = LinkedList[Current][1]`；
   - 被删结点还给空闲表：`LinkedList[Removed][1] = FirstEmpty`，`FirstEmpty = Removed`（MS 也接受接到空闲表末尾）。
3. **找的循环不要靠 `and` 短路**：`while Current != -1 and LinkedList[Current][0] != Item` 在 Python 里能用，但 MS 范例里把两个条件写反了顺序（先读数组再判 –1）；写成标志变量或分层 `if` 最稳（D25）。
4. **对象实现**：插入 = `NewNode = Node(Data)`、`NewNode.SetNextNode(self.__HeadNode)`、`self.__HeadNode = NewNode`；删除时比较的是 `Current.GetData()`，不是结点对象本身（9618_s25_43:3(b)(iv) 的考官报告）。
5. **方法要带 `self`**：写在类里的 InsertNode() 第一个参数是 `self`，属性用 `self.__HeadNode`（9618_s25_43:3(b)(ii) 的考官报告指出有考生写成了普通过程）。

**Python 模板**（对象实现；数组实现见代表题）

```python
class Node:
    def __init__(self, TheDatap):
        self.__TheData = TheDatap         # INTEGER
        self.__NextNode = None            # Node

    def GetData(self):
        return self.__TheData

    def GetNextNode(self):
        return self.__NextNode

    def SetNextNode(self, NextNodep):
        self.__NextNode = NextNodep


class LinkedList:
    def __init__(self):
        self.__HeadNode = None            # Node

    def InsertNode(self, Data):           # insert at the front
        NewNode = Node(Data)
        NewNode.SetNextNode(self.__HeadNode)
        self.__HeadNode = NewNode

    def RemoveNode(self, Data):           # returns BOOLEAN
        if self.__HeadNode == None:
            return False
        if self.__HeadNode.GetData() == Data:
            self.__HeadNode = self.__HeadNode.GetNextNode()
            return True
        Previous = self.__HeadNode
        Current = self.__HeadNode.GetNextNode()
        while Current != None:
            if Current.GetData() == Data:
                Previous.SetNextNode(Current.GetNextNode())   # skip Current
                return True
            Previous = Current
            Current = Current.GetNextNode()
        return False
```

**得分表述**（引自对应 MS）
- 「Checking if linked list is full (FirstEmpty = -1) …」⟦9618_w24_41:3(b)⟧
- 「FirstEmpty = LinkedList[FirstEmpty, 1] before any update to FirstEmpty ‘s pointer」⟦9618_w24_41:3(b)⟧
- 「… storing previous pointer through each loop…」⟦9618_w24_41:3(d)(i)⟧
- 「… when found, updating previous pointer to found node’s pointer」⟦9618_w24_41:3(d)(i)⟧
- 「Calling SetNextNode() for new node with HeadNode as parameter」⟦9618_s25_43:3(b)(ii)⟧
- 「Checking if head node equals parameter and returning TRUE if true …」⟦9618_s25_43:3(b)(iv)⟧

**得分点地图**（口径同 LT-01。共 5 行，全部拆了得分点，来自 3 份卷）

| 技能标签 | 行数 | MS 常见写法 |
|:--|--:|:--|
| `linked-list` | 5 | LinkedList[FirstEmpty, 1] = FirstNode；FirstNode = FirstEmpty；updating previous pointer |
| `module-header` | 5 | Procedure header (and end) with parameter |
| `pre-condition-loop` | 3 | following pointers in loop/recursive call |
| `object-reference`、`relational-ops`、`array-2d` | 各 2 | HeadNode.GetNextNode()；comparing to data to remove each time |

**几乎每次都有的分**：插入题的“判满”“存数据进空闲结点”“新结点指向原表头”“更新起始指针”“空闲指针后移”；删除题的“先查第一个结点”“记住前一个结点”“前一个结点跳过目标”。

**易错与失分**
- 先改 `LinkedList[FirstEmpty][1]` 再取空闲表的下一个：空闲表就断了。MS 专门给分「before any update to FirstEmpty ‘s pointer」⟦9618_w24_41:3(b)⟧。
- 只写了一部分：考官报告指出常见的是部分作答（多为函数头与“把数据存进正确位置”），能写出完整插入的很少（9618_w24_41:3(b)）；删除也只有少数人写全（9618_w24_41:3(d)(i)）。
- 用一维数组代替二维数组（9618_w24_41:3(b)、3(d)(i) 的考官报告）。
- 对象实现：把整数参数当成结点对象、或去找表尾再插（题目要求插在表头）（9618_s25_43:3(b)(ii) 的考官报告）；用结点对象与整数比较（9618_s25_43:3(b)(iv) 的考官报告）。
- 删除后忘了把结点还给空闲表（MS 9618_w24_41:3(d)(i) 有专门一分）。

#### 代表题精讲　⟦9618_w24_41:3(b)⟧

**在考什么**　（数据结构同 LT-01 代表题。）InsertData() 从用户输入 5 个正整数，**每个都插在链表的最前面**。QP p.13 的步骤表：不满时——把数据存进 `FirstEmpty` 指的结点；把这个结点的指针改成 `FirstNode` 的值；更新 `FirstNode` 与 `FirstEmpty`；满时——结束过程。链表末尾结点的指针是 –1。6 分，MS 列 7 点、Max 6（“1 mark each to max 6”）。讲解时请对照原卷 QP p.13；MS p.28–30。

**完整作答**　见 LT-01 代表题的整道第 3 题程序（`InsertData()` 在 `# ---- 3(b) ----` 一节，`RemoveData()` 在 `# ---- 3(d)(i) ----`），在 QP 三组测试数据上的运行结果也在那里。

**与 MS 逐点对齐**（3(b)，6 分，MS 7 点、Max 6，编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure header (and end) taking (min) 5 data items as input from the user | `def InsertData():`；循环 5 次 `int(input(...))` | `module-header`、`input-prompt` |
| 2 | Checking if linked list is full (FirstEmpty = -1) … | `if FirstEmpty == -1:` | `linked-list` |
| 3 | …ending procedure/loop/not doing anything further | `return` | `linked-list` |
| 4 | (otherwise) LinkedList[FirstEmpty, 0] = data input | `LinkedList[FirstEmpty][0] = NewItem` | `linked-list`、`array-2d` |
| 5 | LinkedList[FirstEmpty, 1] = FirstNode | `LinkedList[FirstEmpty][1] = FirstNode` | `linked-list` |
| 6 | FirstNode = FirstEmpty | `FirstNode = FirstEmpty` | `linked-list` |
| 7 | FirstEmpty = LinkedList[FirstEmpty, 1] before any update to FirstEmpty ‘s pointer | 先 `NextEmpty = LinkedList[FirstEmpty][1]`，最后 `FirstEmpty = NextEmpty` | `linked-list` |

7 点里拿到 6 点就是满分。注意 MS 用伪代码式的 `LinkedList[FirstEmpty, 1]`，Python 要写成 `LinkedList[FirstEmpty][1]`。

同题 3(d)(i) RemoveData()（5 分，MS 8 点、Max 5）：函数头带参数 / 比较 FirstNode 的数据 / 是就把 FirstNode 改成它的指针 / 否则沿指针循环 / 每次比较 / 记住前一个指针 / 找到后前一个指针改成目标的指针 / 被删结点接回空闲表。本作答 8 点全有。

**证据格怎么交**　3(b)、3(d)(i) 各一格代码，只放这一个过程。改过的过程（如后来又改了 InsertData）以最后能运行的版本为准。

**直观**　插在表头像往一摞盘子最上面放：从“空盘子架”（空闲表）拿最上面那个，放上食物，压在原来那摞的最上面；空盘子架的“最上面”换成下一个。删除像从一串回形针里摘掉一个：把它前一个直接扣到它后一个上，摘下来的放回空盘子架。

**对应练习与阶梯**　真题练习 `practice/p4/9618_w24_41_q3/`（同 LT-01）。前置阶梯 **L10 E02**（表头插入）、**L10 E03**（有序插入）、**L10 E04**（删除并还给空闲表）。

**下一道变式**　⟦9618_s25_43:3(b)(iv)⟧　（对象实现的 RemoveNode()：空表返回 FALSE；`HeadNode` 的数据等于参数就把 `HeadNode` 换成 `HeadNode.GetNextNode()` 并返回 TRUE；否则沿结点比较，找到后让前一个结点 `SetNextNode()` 到目标的下一个、返回 TRUE；走到底返回 FALSE。MS 7 点、Max 6。上面“Python 模板”的 RemoveNode 就是这一题的写法。讲解时请对照原卷 QP p.9。）

<!-- auto:drills P4-LT-02 -->

### P4-LT-03　二叉树：声明初始化与插入　{#P4-LT-03}

<!-- auto:stats P4-LT-03 -->

**考法**　①声明二维数组（结点数 × 3：左指针、数据、右指针）全部初始化为 –1，再声明 `RootPointer`、`FreeNode`（2–3 分）；②按题给表把已有结点写进数组，并初始化两个指针（2 分）；③写插入：判满 → 存进 `FreeNode` 结点 → 空树则设根 → 否则从根比较，小走左、大（或等）走右，走到空指针处，让父结点的左 / 右指针指向新结点 → `FreeNode` 加 1（6–7 分）；④对象实现：`Tree` 类里有 `Node` 对象数组（9618_s24_42）或结点之间互相引用（9618_s25_41），插入方法用 getter / setter 改左右结点。

**识别信号**　binary tree；left pointer, data, right pointer；ordered binary tree；RootPointer、FreeNode / NumberNodes；AddNode() / InsertNode() / Insert() … finds the position … updates the pointer of the new node's parent node；moving to the left node if the data is less than。

**解题思路**
1. **数组初始化**：`TreeArray.append([-1, -1, -1])` 循环结点数次（二维，不是 3 个一维）。
2. **插入的骨架**（数组实现）：
   ① 判满（`FreeNode == 结点数`）→ 输出 / 返回题给值；
   ② 新数据存进 `TreeArray[FreeNode][1]`；
   ③ 空树（`RootPointer == -1`）→ `RootPointer = FreeNode`（第一个结点就是 0）；
   ④ 否则 `Current = RootPointer`，循环：数据小于 `Current` 的数据 → 看左指针，是 –1 就把它改成 `FreeNode` 并结束，否则往左走；否则 → 同样处理右指针；
   ⑤ `FreeNode = FreeNode + 1`。
3. **相等的值往哪边**：题目说了就照题目（9618_s25_41:3(c)(iii)：greater than or equal → 右）；没说时照 MS 范例的写法把“不小于”放右边（9618_w25_42:3(b) 的范例就是 `if NodeData < … else` 右）。
4. **一个标志控制循环**：`Placed = False`，`while Placed == False:`；找到空位就置 `True`。每次循环都要**重新判断**左右，不能只判断一次就一直往左（9618_w25_42:3(b) 的考官报告）。
5. **对象实现**：比较用 `NewNode.GetData() < Current.GetData()`；看子结点用 `GetLeft()` / `GetRight()`；挂上用 `SetLeft(NewNode)` / `SetRight(NewNode)`（或改整数指针后存回数组）。

**Python 模板**（数组实现，见代表题的 `AddNode`）

```python
TreeArray = []                       # INTEGER, 50 x 3: left, data, right
for Row in range(50):
    TreeArray.append([-1, -1, -1])
RootPointer = -1                     # INTEGER, empty tree
FreeNode = 0                         # INTEGER, next free node
```

**得分表述**（引自对应 MS）
- 「(global) TreeArray declared as a 2D array with 50 × 3 elements …」⟦9618_w25_42:3(a)⟧
- 「Checking if tree is empty (RootPointer = -1 // FreeNode = 0) and if so, storing 0 in RootPointer」⟦9618_w25_42:3(b)⟧
- 「(if not empty) Comparing parameter to data at index TreeArray[RootPointer][1] …」⟦9618_w25_42:3(b)⟧
- 「… updating parent node's appropriate pointer」⟦9618_w25_42:3(b)⟧
- 「If parameter >= first node, checking if there is a right node …」⟦9618_s25_41:3(c)(iii)⟧
- 「looping through all 20 × 3 elements of array …」⟦9618_w22_41:3(a)⟧

**得分点地图**（口径同 LT-01。共 9 行，全部拆了得分点，来自 5 份卷）

| 技能标签 | 行数 | MS 常见写法 |
|:--|--:|:--|
| `binary-tree` | 8 | comparing … accessing left / right node；updating parent node's pointer；RootPointer / FreeNode |
| `initialise-variables`、`array-2d` | 各 5 | 2D array with 50 × 3 elements … all initialised to –1 |
| `pre-condition-loop`、`relational-ops`、`module-header` | 各 4 | … until location found；if less than … if greater than |
| `nested-if`、`declare-array`、`global-scope`、`nested-loops` | 各 3 | Checking if tree is empty … storing 0 in RootPointer |

**几乎每次都有的分**：声明行的“二维数组 n × 3”“全部 –1”“两个指针初值”；插入行的“判满”“空树设根”“比较后左 / 右”“循环到空位”“改父结点指针”“FreeNode 加 1”。

**易错与失分**
- 二维数组的大小建错：考官报告指出常见的是少一格（19 × 1，9618_w22_41:3(a)）或少一列（50 × 2，9618_w25_42:3(a)），或只建了一维。
- 每次只判断一次方向、之后一直往左（或右）走（9618_w25_42:3(b) 的考官报告）。
- 题目用二维数组，却改用结点对象去访问指针属性（9618_w25_42:3(b) 的考官报告）——照题目的结构写。
- 忘了 `FreeNode + 1`，下一个数据会覆盖这一个。
- 忘了处理空树：根指针一直是 –1，后面所有插入都从 `TreeArray[-1]`（Python 的最后一行）开始比，不报错但全错。

#### 代表题精讲　⟦9618_w25_42:3(b)⟧

**在考什么**　程序把整数按升序存进有序二叉树，用二维数组实现：每个结点三项（左指针、数据、右指针），空值都存 –1，最多 50 个结点，结点不会被删除。3(a)：全局 `TreeArray` 每个结点三项初始化为 –1，全局 `RootPointer` 初值 –1、`FreeNode`（下一个空结点）初值 0。3(b) AddNode()：参数是要存的整数；存进下一个空结点；沿指针找到位置；更新新结点父结点的指针；树满时输出 "The tree is full"。7 分，MS 9 点、Max 7。同一大题：3(c) 主程序读 TreeData.txt 逐个 AddNode（FL-01）、3(d) WriteAllToFile() 写 Tree.txt（FL-03）、3(e)(i) 调用、3(e)(ii) 截图（文件内容与文件名）。讲解时请对照原卷 QP p.10（题干、3(a)、3(b)）、p.11（3(c)、3(d) 的示例表）、p.12（3(e)）；MS p.27–38（AddNode 清单 p.29、Python 范例 p.31–32，截图样例 p.38）。

**完整作答**（整道第 3 题的程序；`Question3_N25.py`，与 TreeData.txt 放在同一文件夹）

```python
# ---- 3(a) ----
TreeArray = []                       # INTEGER, 50 x 3: [node][0] left, [node][1] data, [node][2] right
for Row in range(50):
    TreeArray.append([-1, -1, -1])
RootPointer = -1                     # INTEGER, empty tree
FreeNode = 0                         # INTEGER, next free node


# ---- 3(b) ----
def AddNode(NodeData):               # NodeData : INTEGER
    global RootPointer, FreeNode
    if FreeNode == 50:                           # full
        print("The tree is full")
        return
    TreeArray[FreeNode][1] = NodeData            # store in the next free node
    if RootPointer == -1:                        # empty tree: new node is the root
        RootPointer = 0
    else:
        CurrentNode = RootPointer
        Placed = False
        while Placed == False:
            if NodeData < TreeArray[CurrentNode][1]:      # go left
                if TreeArray[CurrentNode][0] == -1:
                    TreeArray[CurrentNode][0] = FreeNode  # parent points to the new node
                    Placed = True
                else:
                    CurrentNode = TreeArray[CurrentNode][0]
            else:                                         # go right
                if TreeArray[CurrentNode][2] == -1:
                    TreeArray[CurrentNode][2] = FreeNode
                    Placed = True
                else:
                    CurrentNode = TreeArray[CurrentNode][2]
    FreeNode = FreeNode + 1


# ---- 3(d) ----
def WriteAllToFile():
    try:
        File = open("Tree.txt", "w")
        for Row in range(50):
            Line = str(TreeArray[Row][0]) + "," + str(TreeArray[Row][1]) + "," + str(TreeArray[Row][2])
            File.write(Line + "\n")
        File.close()
    except IOError:
        print("Could not write to Tree.txt")


# ---- main program ----
if __name__ == "__main__":
    # 3(c)
    try:
        File = open("TreeData.txt", "r")
        for Line in File:
            AddNode(int(Line.strip()))
        File.close()
    except IOError:
        print("TreeData.txt not found")
    # 3(e)(i)
    WriteAllToFile()
```

在官方源文件 TreeData.txt（50 个整数）上实际运行，写出的 Tree.txt 50 行与 MS 3(e)(ii) 的截图样例逐行一致（前几行 `1,40,2`、`6,4,3`、`8,82,17`、`9,8,4`，最后一行 `-1,12,-1`）。另用 Python 直接调用：依次加入 50、30、70、30、60 后，相等的 30 挂在第一个 30 的右边、60 挂在 70 的左边；存满 50 个结点后再调用输出 `The tree is full`。

**与 MS 逐点对齐**（3(b)，7 分，MS 9 点、Max 7，编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure header (and end) taking one (integer) parameter and storing parameter in array in index TreeArray[FreeNode][1] | `def AddNode(NodeData):`；`TreeArray[FreeNode][1] = NodeData` | `module-header`、`binary-tree` |
| 2 | Checking if tree is full (FreeNode = 50) and outputting "The tree is full" | `if FreeNode == 50: print("The tree is full")` | `binary-tree`、`output-format` |
| 3 | Checking if tree is empty (RootPointer = -1 // FreeNode = 0) and if so, storing 0 in RootPointer | `if RootPointer == -1: RootPointer = 0` | `binary-tree`、`nested-if` |
| 4 | (if not empty) Comparing parameter to data at index TreeArray[RootPointer][1] … | `CurrentNode = RootPointer`；`if NodeData < TreeArray[CurrentNode][1]:` | `binary-tree`、`relational-ops` |
| 5 | … if less than, accessing left node … | `CurrentNode = TreeArray[CurrentNode][0]` | `binary-tree` |
| 6 | … if greater than, accessing right node … | `CurrentNode = TreeArray[CurrentNode][2]` | `binary-tree` |
| 7 | … until location found … | `while Placed == False:` | `binary-tree`、`pre-condition-loop` |
| 8 | … updating parent node's appropriate pointer | `TreeArray[CurrentNode][0] = FreeNode` / `[2] = FreeNode` | `binary-tree` |
| 9 | Incrementing FreeNode | `FreeNode = FreeNode + 1` | `binary-tree` |

**证据格怎么交**　3(a)、3(b) 各一格代码。3(e)(ii) 的截图要打开 Tree.txt，**文件名与全部内容**都要看得见（MS：The screenshot must include the filename），一张放不下可以多张，但至少一张要同时有文件名（见 MP-03）。

**直观**　有序二叉树像一本按大小分岔的路标：每到一个结点问一句“比它小吗？”，小往左、不小往右，走到没有路的地方就在那里新开一个房间，并在上一个路口立牌子指向它。

**对应练习与阶梯**　真题练习 `practice/p4/9618_w25_42_q3/`（整道第 3 题）。前置阶梯 **L10 E05**（二叉查找树：插入与查找，含相等值）。

**下一道变式**　⟦9618_s24_42:2(b)(ii)⟧　（`TreeClass` 的方法 InsertNode()：树存在 `Node` 对象数组 `Tree` 里，结点的左右指针是整数下标；空树时把新结点放在 `NumberNodes` 位置、`FirstNode` 设 0；否则放进 `Tree[NumberNodes]`，从根用 `GetData()` 比较、`GetLeft()` / `GetRight()` 走，找到后用 `SetLeft()` / `SetRight()` 改父结点，`NumberNodes` 加 1。MS 7 点、Max 6。讲解时请对照原卷 QP p.8。）

<!-- auto:drills P4-LT-03 -->

### P4-LT-04　二叉树：查找与遍历　{#P4-LT-04}

<!-- auto:stats P4-LT-04 -->

**考法**　①补全题给的递归查找伪代码并写成 Python：找到返回结点下标，找不到返回 –1（5 分，按空计分 + 其余正确 1 分）；②写递归遍历：中序（左 → 根 → 右，输出升序）或后序（左 → 右 → 根），先判断左 / 右是否为空再递归（5–7 分）；③参数可以是结点下标、数组里的一行（结点三项），或结点对象；④主程序用根指针或根结点调用，并按返回值输出。

**识别信号**　recursive；in-order / post order traversal；visit the left node / visit the right node / output the root；searches the binary tree for a given value … return the index … return –1；OutputInOrder() outputs the data … in ascending numerical order；takes a Node object as a parameter。

**解题思路**
1. **遍历三行**，顺序就是名字：
   - 中序：`if 左 != 空: 递归(左)` → `输出当前` → `if 右 != 空: 递归(右)`；
   - 后序：`if 左 != 空: 递归(左)` → `if 右 != 空: 递归(右)` → `输出当前`；
   - 前序：`输出当前` → 左 → 右。
   输出只写**一次**，位置决定是哪种遍历。
2. **参数是什么就怎么取左右**：
   - 下标 `Root`：左 = `ArrayNodes[Root][0]`，递归 `PostOrder(ArrayNodes[Root][0])`；
   - 一行 `RootNode`（如 9618_w22_41 的 MS）：左 = `RootNode[0]`，递归 `PostOrder(ArrayNodes[RootNode[0]])`；
   - 对象 `Node`：左 = `Node.GetLeft()`，空是 `None`。
3. **递归查找**（下标版）：空（–1）→ 返回 –1；相等 → 返回下标；目标更小 → `return Search(左, 目标)`；更大 → `return Search(右, 目标)`。**递归调用前要写 `return`**，否则找到的结果传不回来。
4. **补全伪代码**：先把空填对，再逐行翻译；伪代码的二维下标 `ArrayNodes[Root, 1]` 在 Python 写成 `ArrayNodes[Root][1]`（9618_w22_41:3(c) 的考官报告专门提醒）。
5. **主程序**调用时传根：`PostOrder(ArrayNodes[RootPointer])` 或 `InOrder(RootPointer)`，与自己函数的参数类型一致（9618_w22_41:3(e)(i) 的考官报告：参数对不上是常见错误）。

**Python 模板**（下标作参数；空指针 –1）

```python
def InOrder(Root):                       # Root : INTEGER index of a node
    if ArrayNodes[Root][0] != -1:        # left subtree
        InOrder(ArrayNodes[Root][0])
    print(ArrayNodes[Root][1])           # the node itself
    if ArrayNodes[Root][2] != -1:        # right subtree
        InOrder(ArrayNodes[Root][2])


def SearchValue(Root, ValueToFind):      # returns INTEGER index, or -1
    if Root == -1:
        return -1
    if ArrayNodes[Root][1] == ValueToFind:
        return Root
    if ValueToFind < ArrayNodes[Root][1]:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    return SearchValue(ArrayNodes[Root][2], ValueToFind)
```

**得分表述**（引自对应 MS）
- 「checking if left node is −1 …」⟦9618_w22_41:3(d)⟧
- 「… if not recursive call with parameter as ArrayNodes[RootNode[0]]」⟦9618_w22_41:3(d)⟧
- 「all 3 in the correct order」⟦9618_w22_41:3(d)⟧
- 「1 mark for each completed statement (4)」⟦9618_w22_41:3(c)⟧
- 「Checking if left is null and recursive call if not null」⟦9618_s25_41:3(d)⟧
- 「Procedure header (and end) taking node as parameter, that is recursive」⟦9618_s25_41:3(d)⟧

**得分点地图**（口径同 LT-01。共 4 行，全部拆了得分点，来自 3 份卷）

| 技能标签 | 行数 | MS 常见写法 |
|:--|--:|:--|
| `binary-tree`、`recursion` | 各 4 | checking if left node is −1 … if not recursive call；correct order |
| `output-format`、`module-header` | 各 3 | outputting the element at the parameter；header … that is recursive |
| `relational-ops`、`array-2d` | 各 2 | checking if right pointer is null |

**几乎每次都有的分**：遍历题“函数头且递归”“左非空则递归”“输出当前”“右非空则递归”“顺序正确”——五六分都在模板的三行与顺序上。

**易错与失分**
- 输出写了不止一处，结果重复、顺序乱（9618_w22_41:3(d) 的考官报告）。
- 判断空指针用错：数组版判 –1，对象版判 `None`；在递归调用之后才判断，会访问 `ArrayNodes[-1]`。
- 递归查找漏写 `return`：最外层得到 `None`。
- 伪代码 `ArrayNodes[Root, 1]` 照抄进 Python list 访问，会在运行时抛出 `TypeError`：`Root, 1` 被当作一个 tuple 下标；应写 `ArrayNodes[Root][1]`（9618_w22_41:3(c) 的考官报告）。
- 主程序传的参数类型与自己写的函数不一致（9618_w22_41:3(e)(i) 的考官报告）。

#### 代表题精讲　⟦9618_w22_41:3(d)⟧

**在考什么**　二叉树存在全局二维数组 `ArrayNodes`（伪代码 `ARRAY[0:19, 0:2] OF INTEGER`）：`[i][0]` 左指针、`[i][1]` 数据、`[i][2]` 右指针，–1 表示空指针或空数据。3(b) 给了 7 行表（根在 0，`FreeNode` 初值 6、`RootPointer` 初值 0）。3(d) 后序遍历 PostOrder()：左非空就以左结点为根递归；右非空就以右结点为根递归；输出当前根；**参数是根结点**。7 分（MS 7 点，“1 mark per point (Max 7)”）。同一大题：3(a) 声明并全部置 –1（LT-03）、3(b) 写入表中数据（LT-03）、3(c) 补全递归查找 SearchValue()（LT-04）、3(e)(i) 主程序查 15 并后序遍历（MP-01）、3(e)(ii) 截图。讲解时请对照原卷 QP p.8（数组说明与 3(b) 的表）、p.9（3(c) 伪代码）、p.10（3(d) 的示例树：输出 3 9 25 60 50）、p.11（3(e)）；MS p.16–23（3(d) 清单与 Python 范例 p.21，截图样例 p.23）。

**完整作答**（整道第 3 题的程序；`Question3_N22.py`）

```python
# ---- 3(a) ----
ArrayNodes = []                     # INTEGER, 20 x 3: [i][0] left, [i][1] data, [i][2] right
for i in range(20):
    ArrayNodes.append([-1, -1, -1])

# ---- 3(b) ----
ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
FreeNode = 6                        # INTEGER, first free element
RootPointer = 0                     # INTEGER, first node in the tree


# ---- 3(c) ----
def SearchValue(Root, ValueToFind):         # Root, ValueToFind : INTEGER, returns INTEGER
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        else:
            if ArrayNodes[Root][1] == -1:
                return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    return -1


# ---- 3(d) ----
def PostOrder(RootNode):                    # RootNode : one node, a list [left, data, right]
    if RootNode[0] != -1:                   # left node not empty
        PostOrder(ArrayNodes[RootNode[0]])
    if RootNode[2] != -1:                   # right node not empty
        PostOrder(ArrayNodes[RootNode[2]])
    print(RootNode[1])                      # output the root last


# ---- main program ----
if __name__ == "__main__":
    # 3(e)(i)
    ReturnValue = SearchValue(RootPointer, 15)
    if ReturnValue == -1:
        print("Not found")
    else:
        print("Found at", ReturnValue)
    PostOrder(ArrayNodes[RootPointer])
```

实际运行输出 `Found at 1`，然后 10、9、3、15、58、20，与 MS 3(e)(ii) 的截图样例一致。另用 Python 直接调用：SearchValue 对 20、15、3、9、10、58 依次返回 0–5，对 99、4 返回 –1。

**与 MS 逐点对齐**（3(d)，7 分，MS 7 点，编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | (procedure) header (and end where appropriate) with one parameter (root node or index of root node) and at least one recursive call | `def PostOrder(RootNode):`，函数里调用 `PostOrder(...)` | `module-header`、`recursion` |
| 2 | checking if left node is −1 … | `if RootNode[0] != -1:` | `binary-tree`、`relational-ops` |
| 3 | … if not recursive call with parameter as ArrayNodes[RootNode[0]] | `PostOrder(ArrayNodes[RootNode[0]])` | `recursion`、`binary-tree` |
| 4 | checking if right node is −1 … | `if RootNode[2] != -1:` | `binary-tree`、`relational-ops` |
| 5 | …if not recursive call with parameter as ArrayNodes[RootNode[2]] | `PostOrder(ArrayNodes[RootNode[2]])` | `recursion`、`binary-tree` |
| 6 | outputting the element at the parameter RootNode[] | `print(RootNode[1])` | `output-format`、`array-2d` |
| 7 | all 3 in the correct order | 左 → 右 → 输出 | `binary-tree`、`recursion` |

MP1 写明参数是“root node or index of root node”都可以：若你用下标作参数（`PostOrder(Root)`，递归 `PostOrder(ArrayNodes[Root][0])`），主程序就要 `PostOrder(RootPointer)`——前后一致即可。3(c) 的补全（5 分）：四个空依次是 `Root`、`>`、`Root`、`1`（MS p.19 的伪代码），外加“其余正确”1 分；Python 里末尾补一句 `return -1`，所有路径都有返回值（MS 的 Java 范例也这样写）。

**证据格怎么交**　3(c)、3(d) 各一格代码。3(e)(ii) 截图要同时看到查找结果（Found at 1）和后序的 6 个数。

**直观**　后序就是“先把孩子们都安顿好，最后自己报到”：每个结点都先让左孩子、再让右孩子把整棵小树报完，自己最后报。所以树叶最先出现，根 20 最后出现。

**对应练习与阶梯**　真题练习 `practice/p4/9618_w22_41_q3/`（整道第 3 题）。前置阶梯 **L11 E05**（递归遍历：中序、数结点、求高度）、**L11 E01**（追踪递归）。

**下一道变式**　⟦9618_s25_41:3(d)⟧　（对象实现的中序遍历 OutputInOrder()：参数是 `Node` 对象；左结点不为空（`None`）就递归，输出当前结点的数据，右结点不为空就递归。MS 5 点：递归的头 / 左判空并递归 / 输出 / 右判空并递归 / 顺序正确。用 10、20、5、15、7 建树后输出 5 7 10 15 20（MS 3(e)(ii)）。讲解时请对照原卷 QP p.9。）

<!-- auto:drills P4-LT-04 -->

### P4-LT-05　哈希表　{#P4-LT-05}

<!-- auto:stats P4-LT-05 -->

**考法**　①声明哈希表：一维记录数组 + 溢出数组（9618_s25_42：200 + 100），或二维数组（每个散列值一行、每行若干格，9618_w25_41：100 × 10）；②初始化：每格放一个空记录（各字段 –1）或 `None`（2 分）；③散列函数：`Key MOD n` 并返回（2 分）；④插入：算散列值 → 该位置空就存，否则放进溢出数组的下一个空位（或同一行的下一个空格）（4–6 分）；⑤查找：算散列值 → 在那一行（或那一格加溢出区）里比较键 → 找到返回数据，找不到返回 "Not found"（5 分）。

**识别信号**　hash table；hash value；Key MOD 200 / key MOD 100；collision；stored in the next free space in Spare；calculated from the key field；searches the hash table for the record with the matching key field。

**解题思路**
1. **散列函数一行**：`return Key % 200`（伪代码 `MOD` = Python `%`）。参数是键，不是记录。
2. **插入**：`HashValue = CalculateHash(Record.Key)` → `if HashTable[HashValue].Key == -1:`（空记录）存入 → 否则在溢出区从头找**第一个**空位，存进去后**立刻停**（标志或 `break`）。不停就会把同一条记录存进所有空位（MS 专门给分 “storing in that index only”）。
3. **二维版本**：行 = 散列值，在这一行里从第 0 格往后找第一个空格存入；查找时在这一行里逐格比较键。
4. **查找**：算散列值 → 先看主表那一格（或那一行）→ 相等就返回数据 → 全部看完仍没有 → 返回 "Not found"。返回值在所有路径上都要有。
5. **空记录要每格单独新建**（循环里 `NewRecord(-1, -1, -1)`），判断空用某个字段等于 –1（或 `is None`），不要用 `== NewRecord(-1, -1, -1)`（两个不同对象永远不相等）。

**Python 模板**（一维表 + 溢出区）

```python
def CalculateHash(Key):                  # returns INTEGER
    return Key % 200


def InsertIntoHash(TheRecord):
    HashValue = CalculateHash(TheRecord.Key)
    if HashTable[HashValue].Key == -1:
        HashTable[HashValue] = TheRecord
    else:
        Index = 0
        Stored = False
        while Stored == False and Index < 100:
            if Spare[Index].Key == -1:
                Spare[Index] = TheRecord
                Stored = True
            Index = Index + 1


def GetRecord(Key):                      # 2D version: one row per hash value
    Row = Hash(Key)
    for Column in range(10):
        if HashTable[Row][Column] != None:
            if HashTable[Row][Column].Key == Key:
                return HashTable[Row][Column].Data
    return "Not found"
```

**得分表述**（引自对应 MS）
- 「Calculation of parameter MOD 200」⟦9618_s25_42:2(c)⟧
- 「Calling CalculateHash() with key from parameter record and storing/using return value」⟦9618_s25_42:2(d)⟧
- 「… otherwise, locating next free space in Spare …」⟦9618_s25_42:2(d)⟧
- 「… and storing in that index only (i.e. not in all other free spaces)」⟦9618_s25_42:2(d)⟧
- 「Iterating through 2nd dimension at HashTable[return value] and comparison to parameter …」⟦9618_w25_41:3(f)⟧
- 「… returning "Not found" if not found by the end of the dimension」⟦9618_w25_41:3(f)⟧

**得分点地图**（口径同 LT-01。共 8 行，其中 7 行拆了得分点（9618_s25_42:2(b)(i) 只有 1 分未拆），来自 2 份卷）

| 技能标签 | 行数 | MS 常见写法 |
|:--|--:|:--|
| `module-header` | 7 | Function header … taking one parameter and returning … |
| `hash-table` | 5 | Calculation of parameter MOD 200；Checking if HashTable at return value … is empty；locating next free space in Spare |
| `return-value`、`linear-search`、`procedure-call` | 各 3 | Calling Hash() … storing/using return value；iterating … comparison to parameter |
| `record-type`、`array-of-records`、`initialise-variables`、`div-mod`、`array-2d` | 各 2 | empty record with –1 in each of the 3 fields；2D array of 100 × 10 elements |

**几乎每次都有的分**：散列函数的“头 + 返回”与“MOD”；插入的“调用散列函数并用返回值”“检查那一格是否空”“冲突时找下一个空位并只存一次”。

**易错与失分**
- 冲突时把记录存进溢出区**每一个**空位：找到第一个空位就要停（9618_s25_42:2(d) MP6）。
- 散列函数传入整条记录、或对散列值再取一次 MOD。
- 初始化用 `[NewRecord(-1, -1, -1)] * 200`：200 格是同一个对象，存一条就全变了。
- 查找只看主表那一格、不看溢出区 / 同一行的其余格；或在循环里第一次不相等就返回 "Not found"。
- 返回 "Not found" 的语句写在循环里面，第一格不对就提前结束。

#### 代表题精讲　⟦9618_s25_42:2(d)⟧

**在考什么**　记录数组 `HashTable` 有 200 格，按 `Key MOD 200` 决定存在哪一格；两个键算出同一格就是冲突，冲突的记录按顺序放进第二个数组 `Spare`（100 格）的下一个空位。2(a) 记录 `NewRecord`（Key、Item1、Item2，都是整数）；2(b) 声明两个全局数组、Initialise() 每格放空记录（三个字段都是 –1）；2(c) CalculateHash()；2(d) InsertIntoHash()：参数是一条 NewRecord；用 CalculateHash() 算键的散列值；那一格是空记录就存进去，否则存进 Spare。可以假定 Spare 一定放得下。6 分，MS 6 点。同一大题：2(e) CreateHashTable() 读 HashData.txt、按逗号拆字段建记录并逐个插入（FL-02）、2(f)(i) PrintSpare() 输出溢出区里的键（AR-05）、2(f)(ii) 主程序、2(f)(iii) 截图。讲解时请对照原卷 QP p.6（题干、2(a)、2(b)）、p.7（2(c)–2(e)）、p.8（2(f)）；MS p.19–32（2(d) 清单 p.25、Python 范例 p.27，截图样例 p.32）。

**完整作答**（整道第 2 题的程序；`Question2_J25.py`，与 HashData.txt 放在同一文件夹）

```python
# ---- 2(a) ----
class NewRecord:                     # record declared as a class
    def __init__(self, Keyp, Item1p, Item2p):
        self.Key = Keyp              # INTEGER
        self.Item1 = Item1p          # INTEGER
        self.Item2 = Item2p          # INTEGER


# ---- 2(b)(i) ----
HashTable = [None] * 200             # NewRecord, 200 elements (global)
Spare = [None] * 100                 # NewRecord, 100 elements (global)


# ---- 2(b)(ii) ----
def Initialise():
    for Index in range(200):
        HashTable[Index] = NewRecord(-1, -1, -1)     # a separate empty record each time
    for Index in range(100):
        Spare[Index] = NewRecord(-1, -1, -1)


# ---- 2(c) ----
def CalculateHash(Key):              # Key : INTEGER, returns INTEGER
    return Key % 200                 # Key MOD 200


# ---- 2(d) ----
def InsertIntoHash(TheRecord):       # TheRecord : NewRecord
    HashValue = CalculateHash(TheRecord.Key)
    if HashTable[HashValue].Key == -1:               # this index is empty
        HashTable[HashValue] = TheRecord
    else:                                            # collision: next free space in Spare
        Index = 0
        Stored = False
        while Stored == False and Index < 100:
            if Spare[Index].Key == -1:
                Spare[Index] = TheRecord
                Stored = True                        # store in this one index only
            Index = Index + 1


# ---- 2(e) ----
def CreateHashTable():
    try:
        File = open("HashData.txt", "r")
        for Line in File:
            Fields = Line.strip().split(",")
            ThisRecord = NewRecord(int(Fields[0]), int(Fields[1]), int(Fields[2]))
            InsertIntoHash(ThisRecord)
        File.close()
    except IOError:
        print("HashData.txt not found")


# ---- 2(f)(i) ----
def PrintSpare():
    for Index in range(100):
        if Spare[Index].Key != -1:
            print(Spare[Index].Key)


# ---- main program ----
if __name__ == "__main__":
    # 2(f)(ii)
    Initialise()
    CreateHashTable()
    PrintSpare()
```

在官方源文件 HashData.txt（198 行，每行“键,项1,项2”，CRLF 行尾）上实际运行，PrintSpare 输出 61 个键，从 915、136、415 开始到 977、88 结束，与 MS 2(f)(iii) 的截图样例逐个一致。另用 Python 直接调用：CalculateHash(646) = 46；键 5、205、405 依次插入后，5 在主表第 5 格，205、405 分别在 Spare 的第 0、1 格，第 2 格仍空（只存一次）；没有数据文件时 CreateHashTable 输出提示、不崩溃。

**与 MS 逐点对齐**（2(d)，6 分，MS 6 点，编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure header (and end where appropriate) taking one record as a parameter | `def InsertIntoHash(TheRecord):` | `module-header`、`record-type` |
| 2 | Calling CalculateHash() with key from parameter record and storing/using return value | `HashValue = CalculateHash(TheRecord.Key)` | `procedure-call`、`hash-table` |
| 3 | Checking if HashTable at return value from CalculateHash is empty record … | `if HashTable[HashValue].Key == -1:` | `hash-table`、`array-of-records` |
| 4 | … if it is empty, store parameter in location | `HashTable[HashValue] = TheRecord` | `hash-table` |
| 5 | … otherwise, locating next free space in Spare … | `while … : if Spare[Index].Key == -1:` | `hash-table`、`linear-search` |
| 6 | … and storing in that index only (i.e. not in all other free spaces) | `Spare[Index] = TheRecord`、`Stored = True` 结束循环 | `hash-table`、`flag-variable` |

MS 的 Python 范例（p.27）用 `for x in range(0, 100)` + `break`；本作答用标志结束 `while`，两种都满足 MP6。MS 范例的记录类有 `GetKey()`；本题 QP 没要求私有属性，直接用 `.Key` 也可以。

**证据格怎么交**　2(b)(i)、2(b)(ii)、2(c)、2(d) 各一格代码。2(f)(iii) 截图要能看到全部输出（61 个键，一屏放不下就多截几张，见 MP-03）。

**直观**　哈希表像按学号尾数分的储物柜：学号 646 的同学去 46 号柜；46 号已经有人了，就去走廊尽头的“备用柜”（Spare）找第一个空的放进去，放好就走，不要每个空柜都塞一份。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s25_42_q2/`（整道第 2 题）。前置阶梯 **L06 E02**（线性查找：找到就停）、**L08 E01**（记录）、**L01 E02**（整除与取余）。

**下一道变式**　⟦9618_w25_41:3(f)⟧　（二维哈希表 `HashTable`（100 × 10，`Record` 对象），散列函数 `key MOD 100`。GetRecord()：参数是整数键；算散列值；在 `HashTable[散列值]` 那一行的 10 格里逐格比较键；找到返回该记录的数据，整行都没有返回 "Not found"。上面“Python 模板”里的 GetRecord 就是这一题的结构。3(g)(ii) 用 528、1128、1828、1062、39 测试，前四个分别得到 permission、peace、precedent、up，39 得到 Not found。讲解时请对照原卷 QP p.11。）

<!-- auto:drills P4-LT-05 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| LT-01 vs LT-02 | 只建表、沿指针输出或拼字符串 → LT-01；插入、删除、改指针 → LT-02 | 有没有改指针 |
| LT-01 vs AR-04 | 沿指针走（顺序由指针定）→ LT-01；按下标 0、1、2… 输出数组每一行 → AR-04 | 循环变量是 `Current = …[1]` 还是 `for i in range` |
| LT-03 vs LT-04 | 插入新结点、改父结点指针 → LT-03；查找、遍历输出、不改树 → LT-04 | 树变没变 |
| LT-03 vs OP-01 | 只声明 Node 类与构造方法 → OP-01；Tree 类的插入方法、或声明树的数组与指针 → LT-03 | 是不是在实现树的操作 |
| LT-04 vs RC-01 | 递归的对象是二叉树（左 / 右指针）→ LT-04；其他按描述写的递归 → RC-01 | 有没有左右结点 |
| LT-05 vs FL-02 | 散列函数、插入、按散列值查找 → LT-05；读文件拆字段建记录再调用插入 → FL-02 | 有没有打开文件 |
| 数组实现 vs 对象实现 | 指针是整数下标，空是 –1，`LinkedList[i][1]`；指针是对象引用，空是 `None`，`Node.GetNextNode()` | 题干是 2D array 还是 class Node |
| 中序 vs 后序 vs 前序 | 输出在两个递归之间 → 中序（升序）；在两个递归之后 → 后序；之前 → 前序 | 题干列出的三步顺序 |
