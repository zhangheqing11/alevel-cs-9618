## MP　主程序与测试证据 {#ch-MP}

<!-- auto:chapter-stats -->

### 核心思想

写好模块之后，还要用正确的顺序、参数和调用次数把它们串起来；有返回值就保存或直接使用。main 是流程的指挥者，截图是这个流程真实运行后的证据。main 的代码分和截图的证据分分别检查，不能只交其中一项。

这一章每道大题都会碰到，所以不单独排课：**第一道 P4 练习**时就学 MP-01（主程序按固定顺序调用模块并输出）和 MP-03（按题给数据运行并截图：输入过程、要求同屏的文件名都要在图里），MP-02（一串输入或给定值逐个交给模块并报告结果）在第一次遇到时学。主程序写在 `if __name__ == "__main__":` 下，提示语写在 `input("…")` 里（D13）。

MP-01 管固定调用链及简单驱动过程；MP-02 管一串数据逐个交给模块；MP-03 管截图。题目在 main 中做对象实例化、数组统计或输入校验时，要按承担主要得分点的结构去 OP、AR 或 PR，不因出现 “main program” 就全部归 MP（D43）。

### 题型树
<!-- auto:type-tree -->

### P4-MP-01　主程序：调用模块并输出结果　{#P4-MP-01}

<!-- auto:stats P4-MP-01 -->

**考法**　按题给顺序调用模块，保存/使用返回值，再输出；也含只做一次输入与调用的驱动过程。

**识别信号**　Write/Amend the main program；call … then …；store/use return value；before and after。

**解题思路**
1. 把题干动作列成顺序：六次 EnterRecord → 一次 Dequeue → 检查返回记录并输出 → 再一次 EnterRecord → 输出数组中的记录。
2. 每个会改变状态的函数只调用一次，立刻保存返回值；后续判断和输出都用保存的变量。
3. 核对函数返回什么：本题是 SaleData，不能把整个对象直接 print 后期待显示字段，也不能与整数 -1 比较。
4. 拿到空记录就输出错误信息；拿到有效记录才输出 ID 与 Quantity。最后输出这两个字段，而不是对象地址。
5. 判断题型看得分点。本题虽有 for 循环，但六次调用只是固定流程的一部分，语料主题型为 MP-01；不是见到 for 就改成 MP-02。

**Python 模板**（自包含流程骨架；教学自练无真题 MS，真实 ADT 仍按原题算法实现）

```python
def ReadData():
    return [10, 20, 30]  # INTEGER, 3 elements; teaching example


def Process(Data):
    Total = 0
    for Index in range(3):
        Total = Total + Data[Index]
    return Total


if __name__ == "__main__":
    DataFromModule = ReadData()
    Result = Process(DataFromModule)
    print(Result)
```

**得分表述**（引自对应 MS）
- 「Calling EnterRecord() 6 times before dequeue」⟦9618_s23_42:2(f)(i)⟧
- 「Calling Dequeue() and storing/using return value …」⟦9618_s23_42:2(f)(i)⟧
- 「… checking if an empty record is returned and outputting either the ID and quantity of returned record or outputting the error message if empty record」⟦9618_s23_42:2(f)(i)⟧
- 「Calling EnterRecord() again after dequeue」⟦9618_s23_42:2(f)(i)⟧
- 「Output the ID and quantity for all the records currently stored in CircularQueue」⟦9618_s23_42:2(f)(i)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 54 行，33 行拆了得分点；表格只统计已拆点行的 `markpoints[].skills`，1 分行不在标签计数里）

| 技能标签 | 行数 |
|:--|--:|
| `procedure-call` | 33 |
| `output-format` | 21 |
| `return-value` | 17 |
| `nested-if` | 6 |
| `input-prompt` | 5 |
| `type-conversion` | 3 |

自查时优先看“调用正确模块 → 参数正确 → 接住返回值 → 在正确位置输出”；不是一个标签固定对应一分。

**易错与失分**　考官报告指出，有考生调用 Dequeue 两次、第一次结果没有保存，或只输出对象/一个字段，没有显示 ID 与数量（9618_s23_42:2(f)(i)）。EnterRecord 中调用一次 Enqueue 就报告结果，属于 MP-01；不要把 Push/Enqueue 的实现再写一遍。

#### 代表题精讲　⟦9618_s23_42:2(f)(i)⟧

**在考什么**　循环队列的完整驱动流程。4 分，MS 列五点但 Max 4；语料 MP1–MP5 对应五个圆点，不能叫作五分。QP p.5–7（p.7 六条数据表与主程序）；MS p.11–22，本小问清单 p.20、Python p.21。

**完整作答**（整道大题的最终可运行 Python；按注释定位本格）

```python
# ---- 2(a) ----
class SaleData:                          # record structure declared as a class
    def __init__(self, SaleIDp, Quantityp):
        self.SaleID = SaleIDp            # STRING
        self.Quantity = Quantityp        # INTEGER


# ---- 2(b) ----
CircularQueue = []                       # SaleData, 5 elements
for x in range(5):
    CircularQueue.append(SaleData("", -1))   # a separate empty record in each element
Head = 0                                 # INTEGER
Tail = 0                                 # INTEGER, element where the next record goes
NumberOfItems = 0                        # INTEGER


# ---- 2(c) ----
def Enqueue(RecordToAdd):                # RecordToAdd : SaleData, returns INTEGER
    global Tail, NumberOfItems
    if NumberOfItems == 5:               # full
        return -1
    CircularQueue[Tail] = RecordToAdd    # store at Tail ...
    Tail = Tail + 1                      # ... then move Tail
    if Tail == 5:                        # wrap round
        Tail = 0
    NumberOfItems = NumberOfItems + 1
    return 1


# ---- 2(d) ----
def Dequeue():                           # returns SaleData
    global Head, NumberOfItems
    RecordRemoved = SaleData("", -1)     # empty record for an empty queue
    if NumberOfItems != 0:
        RecordRemoved = CircularQueue[Head]
        Head = Head + 1
        if Head == 5:                    # wrap round
            Head = 0
        NumberOfItems = NumberOfItems - 1
    return RecordRemoved


# ---- 2(e) ----
def EnterRecord():
    ID = input("Enter ID ")
    Quantity = int(input("Enter quantity "))
    NewRecord = SaleData(ID, Quantity)
    if Enqueue(NewRecord) == -1:
        print("Full")
    else:
        print("Stored")


# ---- main program ----
if __name__ == "__main__":
    # 2(f)(i)
    for x in range(6):
        EnterRecord()
    Removed = Dequeue()
    if Removed.SaleID == "":
        print("Queue empty")
    else:
        print(Removed.SaleID, Removed.Quantity)
    EnterRecord()
    for x in range(5):
        print(CircularQueue[x].SaleID, CircularQueue[x].Quantity)
```

用原卷 QP p.7 顺序输入 ADF/10、OOP/1、BXW/5、XXZ/22、HQR/6、LLP/3，再输入 LLP/3。前六次尝试有五次 Stored、一次 Full；出队 ADF 10；再入队 Stored。最终按数组下标输出 LLP 3、OOP 1、BXW 5、XXZ 22、HQR 6，与 MS p.22 截图一致。

**与 MS 逐点对齐**（2(f)(i)，4 分，Max 4；下列 5 点最多取 4 分；语料编号与 MS 圆点顺序一致）

| 语料 MP | MS 原文 | 作答/可见证据对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Calling EnterRecord() 6 times before dequeue | `for x in range(6): EnterRecord()` | `procedure-call`、`count-loop` |
| 2 | Calling Dequeue() and storing/using return value … | `Removed = Dequeue()` | `procedure-call`、`return-value` |
| 3 | … checking if an empty record is returned and outputting either the ID and quantity of returned record or outputting the error message if empty record | 检查 Removed.SaleID，空则消息，否则输出两个字段 | `nested-if`、`output-format` |
| 4 | Calling EnterRecord() again after dequeue | 出队后再调 EnterRecord() | `procedure-call` |
| 5 | Output the ID and quantity for all the records currently stored in CircularQueue | 循环输出 CircularQueue 每条记录的 SaleID、Quantity | `count-loop`、`output-format`、`array-of-records` |

**证据格怎么交**　2(f)(i) 代码格交 main 中对应流程；2(f)(ii) 截图必须同时覆盖六条输入、五次 Stored 与一次 Full、出队 ADF 10、LLP 3 再次成功、五条最终记录。可以分多张保留全部过程；这些是本题一分截图的联合要求，不是五个独立分。

**直观**　模块像工位，返回值是工位交出来的成品；下一工位要拿这件成品，不能只喊一声模块名就走开。

**对应练习与阶梯**　`practice/p4/9618_s23_42_q2/`。前置 **L04 E01、L04 E02**。

**下一道变式**　⟦9618_s25_41:2(e)(i)⟧　ReadData 返回数组，主程序接住它，再传给 SplitData；不要丢掉返回值。QP p.5；MS p.29。

<!-- auto:drills P4-MP-01 -->

### P4-MP-02　主程序：循环输入并逐个调用　{#P4-MP-02}

<!-- auto:stats P4-MP-02 -->

**考法**　循环读取/生成/使用一串数据，每个值调用一次已写好的模块，并按本次返回值逐个报告结果。

**识别信号**　enter 11 numbers；each number as parameter；integers 1 to 25 inclusive；output if TRUE/FALSE。

**解题思路**
1. 先定循环边界：11 个输入用 range(11)，给定 1–25 用 range(1, 26)。Python 的右端不包含。
2. 在循环内取得本次整数，按题目要求 int 转换；提示语写在 input 中（D13）。
3. 每个值调用一次 Push，把返回布尔值用于 if；不直接写数组绕过 Push。
4. 成功、失败各有消息。失败也算这 11 次尝试中的一次，不能擅自重输直到全部成功。
5. 循环外调用输出过程；题目另要求出栈时，继续用 Pop，不手动移动指针。

**Python 模板**（自包含流程骨架；教学自练无真题 MS，真实 ADT 仍按原题算法实现）

```python
# ---- 1(a) ----
StackData = [0] * 10       # INTEGER, 10 elements (global)
StackPointer = 0           # INTEGER, next available space (global)


# ---- 1(b) ----
def PrintArray():
    print(StackPointer)
    for x in range(0, 10):
        print(StackData[x])


# ---- 1(c) ----
def Push(DataToPush):      # DataToPush : INTEGER, returns BOOLEAN
    global StackPointer
    if StackPointer == 10:              # full: next free space is past the end
        return False
    StackData[StackPointer] = DataToPush   # store first ...
    StackPointer = StackPointer + 1        # ... then move to the next free space
    return True


# Main-program slice: call only the existing Push and PrintArray.
if __name__ == "__main__":
    for Count in range(11):
        Value = int(input("Enter a number "))
        Stored = Push(Value)
        if Stored == True:
            print("Stored")
        else:
            print("Stack full")
    PrintArray()
```

**得分表述**（引自对应 MS）
- 「Inputting 11 numbers …」⟦9618_s22_42:1(d)(i)⟧
- 「…calling Push() with each number input as a parameter …」⟦9618_s22_42:1(d)(i)⟧
- 「…outputting appropriate message if TRUE returned」⟦9618_s22_42:1(d)(i)⟧
- 「…outputting appropriate message if FALSE returned」⟦9618_s22_42:1(d)(i)⟧
- 「Calling their output procedure after all 11 additions」⟦9618_s22_42:1(d)(i)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 11 行，11 行拆了得分点；表格只统计已拆点行的 `markpoints[].skills`，1 分行不在标签计数里）

| 技能标签 | 行数 |
|:--|--:|
| `procedure-call` | 11 |
| `count-loop` | 10 |
| `output-format` | 10 |
| `input-prompt` | 7 |
| `return-value` | 5 |
| `nested-if` | 4 |

自查时优先看“调用正确模块 → 参数正确 → 接住返回值 → 在正确位置输出”；不是一个标签固定对应一分。

**易错与失分**　考官报告指出，本题要求改 main，有考生却去改 Push；另有考生未把输入转为整数（9618_s22_42:1(d)(i)）。不要为了判断成功再调一次 Push；那会把一个输入存两次。

#### 代表题精讲　⟦9618_s22_42:1(d)(i)⟧

**在考什么**　10 格整数栈、指针 0 指下一空位；主程序尝试添加 11 个数后输出。5 分、5 点。整题 QP p.2–3；MS p.4–12，本格清单 p.8、Python p.9，测试值在 QP p.3。

**完整作答**（整道大题的最终可运行 Python；按注释定位本格）

```python
# ---- 1(a) ----
StackData = [0] * 10       # INTEGER, 10 elements (global)
StackPointer = 0           # INTEGER, next available space (global)


# ---- 1(b) ----
def PrintArray():
    print(StackPointer)
    for x in range(0, 10):
        print(StackData[x])


# ---- 1(c) ----
def Push(DataToPush):      # DataToPush : INTEGER, returns BOOLEAN
    global StackPointer
    if StackPointer == 10:              # full: next free space is past the end
        return False
    StackData[StackPointer] = DataToPush   # store first ...
    StackPointer = StackPointer + 1        # ... then move to the next free space
    return True


# ---- 1(e)(i) ----
def Pop():                 # returns INTEGER
    global StackPointer
    if StackPointer == 0:               # empty
        return -1
    ReturnData = StackData[StackPointer - 1]   # top item is one below the pointer
    StackPointer = StackPointer - 1
    return ReturnData


# ---- main program ----
if __name__ == "__main__":
    # 1(d)(i)
    for x in range(0, 11):
        TempNumber = int(input("Enter a number "))
        if Push(TempNumber) == True:
            print("Stored")
        else:
            print("Stack full")
    PrintArray()
    # 1(e)(ii)
    Pop()
    Pop()
    PrintArray()
```

按 QP p.3 输入 11、12、…、21：十次 Stored、一次 Stack full；首次输出指针 10 与数组 11–20；再 Pop 两次后指针 8，数组仍为 11–20。MS p.12 明写出栈后的显示也可为 11–18 或末两格 null，不能把一种显示推广成唯一规则。

**与 MS 逐点对齐**（1(d)(i)，5 分；语料编号与 MS 圆点顺序一致）

| 语料 MP | MS 原文 | 作答/可见证据对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Inputting 11 numbers … | `for x in range(0, 11)` 中 int(input(...)) | `input-prompt`、`count-loop` |
| 2 | …calling Push() with each number input as a parameter … | 循环内 `Push(TempNumber)`，本次输入作为参数 | `procedure-call` |
| 3 | …outputting appropriate message if TRUE returned | True 时 print("Stored") | `output-format` |
| 4 | …outputting appropriate message if FALSE returned | False 时 print("Stack full") | `output-format` |
| 5 | Calling their output procedure after all 11 additions | 循环外 PrintArray() | `procedure-call` |

**证据格怎么交**　1(d)(i) 格交输入循环、成功/失败输出与循环后的 PrintArray；1(d)(ii) 截图要显示全部 11 个输入、十次成功、一次满栈和全部栈内容。1(e)(ii) 另交删除前后完整结果。

**直观**　像检票员逐张验票：每张只验一次，当场报告通过与否，全部验完才展示总表。

**对应练习与阶梯**　`practice/p4/9618_s22_42_q1/`。前置 **L03 E01、L08 E03**。

**下一道变式**　⟦9618_s25_41:1(c)⟧　不再读键盘，而是把 1–25 依次交给 Enqueue；输出每个整数与 Successful/Unsuccessful。QP p.3；MS p.12。

<!-- auto:drills P4-MP-02 -->

### P4-MP-03　运行测试并截图　{#P4-MP-03}

<!-- auto:stats P4-MP-03 -->

**考法**　运行题目指定测试并交截图；按该格 MS 核对可见内容，可能是控制台输出、输入过程或文本文件。

**识别信号**　Test your program；Take a screenshot of output(s)；contents and filename clearly visible。

**解题思路**
1. 先找到该截图格自己的 MS；把“必须看见”的数据逐项列出，不能照其他题的截图要求推断。
2. 从干净初始状态运行指定测试。题目要求同一次运行的 before/after，就在同一条程序流程里依次做；多组独立测试则分别重新运行。
3. 函数返回值要由 main 输出，不能因为内部结果正确却屏幕空白而漏掉证据分。
4. 输出过长可以分多张，保留有顺序、无遗漏的证据；本题两行就能放在同一张。
5. 截图贴到对应 screenshot 格。代码格与截图格分别对应不同得分点；文字抄写预期输出不能证明程序实际运行。

**Python 模板**（自包含流程骨架；教学自练无真题 MS，真实 ADT 仍按原题算法实现）

```python
def RunEvidence(CreateList):
    # CreateList is an actual populated LinkedList object, not expected text.
    print(CreateList.Traverse())
    CreateList.RemoveNode(30)
    print(CreateList.Traverse())
```

**得分表述**（引自对应 MS）
- 「Output of linked list with 50 40 30 20 10」⟦9618_s25_43:3(c)(ii)⟧
- 「Output of 2nd linked list with 50 40 20 10」⟦9618_s25_43:3(c)(ii)⟧
- 「Prompt and input of filename TheData.txt」⟦9618_s25_41:2(e)(ii)⟧
- 「Screenshot of data in red file. Filename must be shown in same screenshot as data」⟦9618_s25_41:2(e)(ii)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去 `equivalent_of`、每行每标签计一次；s26 只进计数。共 92 行，19 行拆了得分点；表格只统计已拆点行的 `markpoints[].skills`，1 分行不在标签计数里）

| 技能标签 | 行数 |
|:--|--:|
| `test-output` | 18 |
| `test-input-sequence` | 12 |
| `screenshot-file` | 1 |

截图一分行很多，不能从这张地图推断“只有 19 张截图题”。每格具体看什么由本格 MS 决定，不能把 test-output 的次数当作“每张截图必有一分输出”。

**易错与失分**　考官报告指出，本题需要再写输出语句才能生成证据，考生应分析这一点（9618_s25_43:3(c)(ii)）。s23/42 的考官报告还提醒，所有输出要可见，可用一张或多张截图（9618_s23_42:2(f)(ii)）。不把这解释成任何题都能删掉输入过程。

#### 代表题精讲　⟦9618_s25_43:3(c)(ii)⟧

**在考什么**　以对象链表的删除前后两行输出为证据，2 分、2 点。整题 QP p.7–10（Node 类图 p.7、LinkedList 类图 p.8、算法 p.9、测试 p.10）；MS p.33–45，截图清单与样例 p.45。

**完整作答**（整道大题的最终可运行 Python；按注释定位本格）

```python
# ---- 3(a)(i) ----
class Node:
    def __init__(self, DataP):
        self.__TheData = DataP          # INTEGER
        self.__NextNode = None          # Node

    # ---- 3(a)(ii) ----
    def GetData(self):
        return self.__TheData

    def GetNextNode(self):
        return self.__NextNode

    # ---- 3(a)(iii) ----
    def SetNextNode(self, NextNodeP):    # NextNodeP : Node
        self.__NextNode = NextNodeP


# ---- 3(b)(i) ----
class LinkedList:
    def __init__(self):
        self.__HeadNode = None          # Node

    # ---- 3(b)(ii) ----
    def InsertNode(self, Data):         # Data : INTEGER
        NewNode = Node(Data)
        NewNode.SetNextNode(self.__HeadNode)
        self.__HeadNode = NewNode

    # ---- 3(b)(iii) ----
    def Traverse(self):                 # returns STRING
        Result = ""
        Current = self.__HeadNode
        while Current != None:
            if Result != "":
                Result = Result + " "
            Result = Result + str(Current.GetData())
            Current = Current.GetNextNode()
        return Result

    # ---- 3(b)(iv) ----
    def RemoveNode(self, Data):         # Data : INTEGER, returns BOOLEAN
        if self.__HeadNode == None:
            return False
        if self.__HeadNode.GetData() == Data:
            self.__HeadNode = self.__HeadNode.GetNextNode()
            return True
        Previous = self.__HeadNode
        Current = self.__HeadNode.GetNextNode()
        while Current != None:
            if Current.GetData() == Data:
                Previous.SetNextNode(Current.GetNextNode())
                return True
            Previous = Current
            Current = Current.GetNextNode()
        return False


# ---- 3(c)(i) ----
if __name__ == "__main__":
    CreateList = LinkedList()
    CreateList.InsertNode(10)
    CreateList.InsertNode(20)
    CreateList.InsertNode(30)
    CreateList.InsertNode(40)
    CreateList.InsertNode(50)
    print(CreateList.Traverse())
    CreateList.RemoveNode(30)
    print(CreateList.Traverse())
```

按 QP 依次插入 10、20、30、40、50（表头插入），运行直接输出两行：`50 40 30 20 10` 与 `50 40 20 10`，与 MS p.45 一致。另测空表/找不到返回 False，删除表头、表尾、中间结点返回 True、链表顺序正确。

**与 MS 逐点对齐**（3(c)(ii)，2 分；语料编号与 MS 圆点顺序一致）

| 语料 MP | MS 原文 | 作答/可见证据对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Output of linked list with 50 40 30 20 10 | 第一行 print(CreateList.Traverse())，显示 50 40 30 20 10 | `test-output` |
| 2 | Output of 2nd linked list with 50 40 20 10 | RemoveNode(30) 后第二次 print，显示 50 40 20 10 | `test-output` |

**整题代码的边界核对**　3(b)(iv) 有七个独立点、Max 6：方法与布尔返回、空表、表头匹配、改 HeadNode、沿结点比较、找到后改链接且 True、找不到 False。本作答七点都覆盖。MS p.41 的 Python 范例会在找不到时访问空的 NextNode，且非表头删除路径漏了布尔返回；本作答先判 Current，再访问并明确返回（D25、D31、D44）。

**另外一种截图：文本文件证据**　⟦9618_s25_41:2(e)(ii)⟧（QP p.5、MS p.29）明确分两点：MP1 显示提示与输入 TheData.txt；MP2 显示红色数字文件的真实内容，且文件名必须与内容出现在同一张截图。用文本编辑器打开程序生成的 Red.txt，保留文件名和内容；不要只拍控制台打印，也不要裁掉文件名。本题 MS 没列逐个数字，不另外编造一串“必拍数字”。这是本题的文件要求，不套到前面的链表两行输出截图。

**证据格怎么交**　3(c)(ii) 截图只按该格两个点：完整显示删除前五个数与删除后四个数、顺序正确。该格没有要求拍源代码或键盘输入；3(c)(i) 代码仍交到自己的代码格。

**直观**　截图像实验记录：记录里必须能看到本次实验要求证明的现象；实验装置正确也不能代替记录。

**对应练习与阶梯**　`practice/p4/9618_s25_43_q3/`。前置 **L10 E02、L12 E01**。

**下一道变式**　⟦9618_s23_42:2(f)(ii)⟧　改成循环队列的一分截图：要同时覆盖六条输入、Stored/Full、ADF 10 出队、LLP 3 重试成功和五条最终记录。QP p.7；MS p.22；本章 MP-01 已给完整程序。

<!-- auto:drills P4-MP-03 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| MP-01 与 MP-02 | 固定流程/一次驱动 → MP-01；一串值逐个交给模块 → MP-02；具体以该行得分点为准 | 不仅看有没有 for |
| MP 与 SQ-04 | 调用一次 Enqueue 后报告是驱动；反复 Pop/Dequeue 后统计/配对是 SQ-04 | 数据是否靠出栈/出队持续取得并处理 |
| main 与 OP-07 | 创建对象与调用方法承担主要点时去 OP-07 | 不是只看 main program 两词 |
| 代码格与截图格 | 代码证明结构；截图证明指定测试结果 | Copy code / Take screenshot |
| return 与 print | return 交给调用者；print 才在控制台展示 | 截图是否有结果 |
| MS 圆点数与分值 | 有 Max 时最多取该值；一分截图可有多个联合内容要求 | 不按条目数机械数分 |
| 控制台输出与文件证据 | 文件格要看到实际文件及文件名；打印同样数字不能替代 | 本题 MS 的 Filename must be shown |
