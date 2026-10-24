## SQ　栈与队列 {#ch-SQ}

<!-- auto:chapter-stats -->

### 核心思想

SQ 是 P4 第 1 题最常见的情境：几乎每季都有一道“用数组实现栈或队列”的大题，一道大题 15–25 分，前面几小问的分都在本章。4 个题型分两块：

1. **写操作本身**（SQ-01 栈、SQ-02 线性队列、SQ-03 循环队列）：声明全局数组与指针 → 写 Push / Pop 或 Enqueue / Dequeue。得分点几乎是固定的一串：**函数头 → 判满（判空）→ 返回失败值 → 按约定移动指针并存（取）值 → 返回成功值或取出的值**。
2. **用操作完成处理**（SQ-04）：在另一个过程或主程序里反复调用已写好的 Pop / Dequeue（或按条件 Push 进不同的栈），检查返回值，循环到“空”为止，再做计算、配对、统计或压缩。

整章只有一条规则要反复练：**指针的约定照题目抄，不用自己的习惯**（D10 ②）。题目会写清楚指针指的是“最后一个元素”还是“下一个空位”、初值是 –1 还是 0，判满判空的条件、先移指针还是先存值，全由这一句决定。考官报告一再指出：题目给了初值，就要用这个初值（9618_s23_41:3(a)、9618_w22_42:3(a)）。

P4 与 P2 / P3 的分界：P2-DT-16、P3-CT-06 / CT-07 写的是伪代码（1 起数组）；P4 用 Python 上机写，数组是 0 起的 list，**题目给的下标就是 Python 的下标**（“The index of the first element in each array is 0”，9618_w23_42:1(a)(i)）。

本章的大题几乎都接着一小问“读文件，把每行 Push / Enqueue 进去”（FL-01）、一小问“主程序逐个调用并报告成败”（MP-02）和一张截图（MP-03）；这些在对应卡里讲，本章精讲把整道大题的程序写全，方便你从空文件一路写到截图。

### 题型树
<!-- auto:type-tree -->

### P4-SQ-01　数组实现栈　{#P4-SQ-01}

<!-- auto:stats P4-SQ-01 -->

**考法**　①声明全局栈数组（大小、类型、每个元素的初值）与栈顶指针（1–3 分）；②写 Push()：判满返回失败值，否则存入并移动指针、返回成功值（3–6 分）；③写 Pop()：判空返回题给的“空值”（–1、""、"No data"、–999），否则取出栈顶元素并移动指针（3–5 分）；④题干直接给 PushAnimal() / PopAnimal() 的伪代码，要你翻译成 Python；⑤“第二个栈的 Push / Pop 与第一个相同”，照抄改名（每个 1 分）。

**识别信号**　stack；A 1D array … is used to store the stack globally；StackPointer / TopOfStack / AnimalTopPointer；points to the next available space / stores the index of the last element；Push() … returns FALSE if the stack is full；Pop() returns … if the stack is empty。

**解题思路**
1. **先抄约定**（写在代码注释里）：数组名与大小、元素类型与初值、指针名、指针指“栈顶元素”还是“下一空位”、初值、Pop 在空栈时返回什么。核验语料去重后的 5 份栈题卷里，两种约定都出现过：指“下一空位”、初值 0（9618_s22_42、9618_s23_41、9618_w23_42）；指“最后一个元素”、初值 –1（9618_s25_42、9618_w25_41）。
2. **由约定推出四件事**（10 个元素为例）：

   | 约定 | 空栈 | 满栈 | Push 顺序 | Pop 取哪一格 |
   |:--|:--|:--|:--|:--|
   | 指下一空位，初值 0 | `Pointer == 0` | `Pointer == 10` | 先存 `Stack[Pointer]`，再加 1 | 先减 1 或直接取 `Stack[Pointer - 1]` |
   | 指栈顶元素，初值 –1 | `Pointer == -1` | `Pointer == 9` | 先加 1，再存 `Stack[Pointer]` | 先取 `Stack[Pointer]`，再减 1 |

3. **Push**：判满 → `return False`（或题给的 –1）；否则按上表移动指针并存值 → `return True`（或 1）。
4. **Pop**：判空 → 返回题给的空值；否则**先把栈顶元素存进局部变量**，再移动指针，最后返回这个变量。`return` 之后的语句不会执行，所以不能先 `return` 再移指针。
5. 函数里要给指针重新赋值，就必须先写 `global 指针名`；只改数组的某一格不需要 `global`（写上也不扣分，MS 范例都写了）。

**Python 模板**（指针指下一空位、初值 0；括号里是另一种约定的写法）

```python
Stack = [0] * 10          # INTEGER, 10 elements   (or [-1] * 20, ["-1"] * 20 … as the question says)
TopPointer = 0            # INTEGER, next free space   (last element: TopPointer = -1)


def Push(DataToPush):     # DataToPush : INTEGER, returns BOOLEAN
    global TopPointer
    if TopPointer == 10:                  # full   (last element: TopPointer == 9)
        return False
    Stack[TopPointer] = DataToPush        # store, then move   (last element: move, then store)
    TopPointer = TopPointer + 1
    return True


def Pop():                # returns INTEGER
    global TopPointer
    if TopPointer == 0:                   # empty   (last element: TopPointer == -1)
        return -1                         # the "empty" value given in the question
    ReturnData = Stack[TopPointer - 1]    # (last element: Stack[TopPointer])
    TopPointer = TopPointer - 1
    return ReturnData
```

题目给了伪代码时，逐行对应即可：

| QP 伪代码 | Python |
|:--|:--|
| `FUNCTION PushAnimal(DataToPush : STRING) RETURNS BOOLEAN` | `def PushAnimal(DataToPush):  # STRING, returns BOOLEAN` |
| `IF AnimalTopPointer = 20 THEN` | `if AnimalTopPointer == 20:` |
| `Animal[AnimalTopPointer] ← DataToPush` | `Animal[AnimalTopPointer] = DataToPush` |
| `RETURN FALSE` / `RETURN TRUE` | `return False` / `return True` |
| `ENDIF` / `ENDFUNCTION` | 缩进结束（没有对应语句） |

**得分表述**（引自对应 MS）
- 「StackPointer initialised to 0」⟦9618_s22_42:1(a)⟧
- 「checking if stack is full …」⟦9618_s22_42:1(c)⟧
- 「(if not full) storing parameter to stack at StackPointer …」⟦9618_s22_42:1(c)⟧
- 「checking if stack is empty (StackPointer is 0) and returning -1」⟦9618_s22_42:1(e)(i)⟧
- 「Checking if stack is full (TopOfStack = 29) and, if it is, returning FALSE」⟦9618_w25_41:1(b)⟧
- 「(Otherwise) Accessing and returning item at TopOfStack (before it's decremented)」⟦9618_w25_41:1(c)⟧

**得分点地图**（口径：核验语料 2022–2026s、主题型为 SQ-01 的行、去掉 `equivalent_of`，同一行同一标签计一次；s26 只进计数。共 16 行，其中 15 行拆了得分点；下表“行数”指 15 行里出现该标签的行数，由脚本按 `markpoints[].skills` 统计）

| 技能标签 | 行数 | MS 常见写法 |
|:--|--:|:--|
| `stack-array` | 14 | checking if stack is full / empty；incrementing / decrementing the pointer；storing … at StackPointer |
| `module-header` | 10 | Function header (and end) taking one parameter |
| `return-value` | 6 | returning -1 / "" / "No data" if empty；returning the item removed |
| `declare-array`、`global-scope` | 各 5 | (Global) … array with n … elements |
| `array-index` | 5 | storing parameter … at TopOfStack position |
| `initialise-variables` | 4 | … initialised to 0 / –1 |
| `boolean-return` | 3 | returning FALSE … returning TRUE |

**几乎每次都有的分**：写 Push / Pop 的行里，“判满（判空）+ 失败值”“按约定移动指针”“用指针作下标存取”各占 1 分，与情境无关；声明的行里，“全局数组 + 大小”和“指针初值”各 1 分。

**易错与失分**
- 指针初值换成自己的习惯：考官报告指出，题目给了初值 0，仍有考生写成 –1（9618_s23_41:3(a)）。初值换了，判满判空、先存还是先移就全跟着错。
- 判满判空不用指针，而去逐格检查数组里有没有数据：考官报告指出这在数据没被删除、或数组一开始就有初值时不成立（9618_s22_42:1(c)、9618_s22_42:1(e)(i)）。
- 指针指“下一空位”时，Pop 取的是 `Pointer - 1` 那一格；考官报告指出常见错误是取 `Pointer` 那一格，或先覆盖再读（9618_s22_42:1(e)(i)）。
- 指针指“最后一个元素”时，满的条件是 `TopOfStack == 29`（30 个元素）；考官报告指出常见错误是写成大于 29（9618_w25_41:1(b)）。返回 –999 要返回整数，不是字符串 `"–999"`（9618_w25_41:1(c)）。
- Push 函数里用 `input()` 读数据，而不是用参数（9618_s22_42:1(c) 的考官报告）。
- 第二个栈照抄第一个时忘了改容量与指针名（PushColour 的栈只有 10 格，9618_s23_41:3(b)(iv)）。
- Python 的数组要真的建出来：`Stack = []` 只写注释不建元素，拿不到声明分（考官报告 9618_s23_41:3(a)，D10 ①）。

#### 代表题精讲　⟦9618_s22_42:1(c)⟧

**在考什么**　栈最多存 10 个整数；全局一维数组 `StackData` 存栈，全局变量 `StackPointer` **指向下一个可用空位、初值 0**。Push() 带一个整数参数：栈满返回 FALSE；不满就把参数放进栈、更新指针、返回 TRUE。6 分，MS 6 点。同一大题：1(a) 声明（3 分，SQ-01）、1(b) 输出整个栈与指针（AR-04）、1(d)(i) 主程序输入 11 个数逐个 Push（MP-02 的代表题）、1(d)(ii) 截图、1(e)(i) Pop()（5 分，SQ-01）、1(e)(ii) 出栈两次后再输出并截图（MP-03）。讲解时请对照原卷 QP p.2（题干、1(a)–1(c)）、p.3（1(d)、1(e)）；MS p.4–12。

**完整作答**（整道第 1 题的程序；`Question1_J22.py`）

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

用 QP 1(d)(ii) 的 11 个输入（11 到 21）实际运行：前 10 次输出 `Stored`，第 11 次输出 `Stack full`；第一次 PrintArray 输出 `10` 与 11…20；出栈两次后输出 `8` 与 11…20（Pop 只移指针、不删数据，MS 1(e)(ii) 写明 11–20、11–18 都接受）。另用 Python 直接调用：空栈 Pop 返回 –1；连续 Push 10 次都返回 True、第 11 次返回 False；再 Pop 10 次依次得到后进的值。

**与 MS 逐点对齐**（1(c)，6 分，MS 6 点；语料编号与 MS 圆点顺序一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | function Push() taking an integer parameter | `def Push(DataToPush):` | `module-header` |
| 2 | checking if stack is full … | `if StackPointer == 10:` | `stack-array` |
| 3 | …and returning FALSE | `return False` | `boolean-return` |
| 4 | (if not full) storing parameter to stack at StackPointer … | `StackData[StackPointer] = DataToPush` | `stack-array`、`array-index` |
| 5 | …incrementing StackPointer | `StackPointer = StackPointer + 1` | `stack-array` |
| 6 | …returning TRUE | `return True` | `boolean-return` |

同题 1(a)（3 分）：全局数组与指针 / 10 个整数元素 / 指针初值 0，各 1 分。1(e)(i)（5 分）：函数头且每条路径都返回数 / 判空（StackPointer 为 0）返回 –1 / 取栈顶元素 / 指针减 1 / 返回取出的值，各 1 分。

**证据格怎么交**　1(a)、1(c)、1(e)(i) 各是一格“program code”：把对应那段代码复制进去即可，但 1(a) 的格里要看得出数组与指针是**全局**的（写在所有函数外面）。改动过的函数以最后版本为准，每一格只放题目点名的那部分代码。

**直观**　StackPointer 像“下一个空停车位”的指示牌：车先停进牌子指的位置，再把牌子往后挪一格；牌子挪到 10 就是停满了。取车时最后停的那辆在牌子前一格。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s22_42_q1/`（整道第 1 题）。前置阶梯 **L08 E03**（数组栈，Python 版指针初值 –1，正好练另一种约定）、**L08 E05**（用栈解决问题）。

**下一道变式**　⟦9618_w25_41:1(b)⟧　（同样是整数栈，但 30 个元素、`TopOfStack` **指最后一个元素、初值 –1**：满的条件是 `TopOfStack == 29`，要先加 1 再存；1(c) 的 Pop 空栈返回整数 –999，先取 `Stack[TopOfStack]` 再减 1。正好是上表的另一行。讲解时请对照原卷 QP p.2–3。）

<!-- auto:drills P4-SQ-01 -->

### P4-SQ-02　数组实现线性队列　{#P4-SQ-02}

<!-- auto:stats P4-SQ-02 -->

**考法**　①声明全局队列数组与队首、队尾指针（有的还有 NumberItems），按题给初值初始化（1–3 分）；②写 Enqueue()：判满返回 FALSE，否则存入、移动队尾指针，**第一次入队时把队首设为 0**，返回 TRUE（4–7 分；有一题判满时只输出信息、是过程）；③写 Dequeue()：判空返回题给值，否则取出队首元素、队首后移（3–6 分）；④用记录结构（Python 写成类）把数组与两个指针包在一起，补全题给的 Enqueue 伪代码（9618_w24_42）。

**识别信号**　linear queue；QueueHead / HeadPointer、QueueTail / TailPointer；stores the index of the first element / last element / next free location；Enqueue() … returns FALSE if the queue is full；Dequeue() returns –1 / "false" / "Empty" if the queue is empty；没有“circular”、没有回到 0。

**解题思路**
1. **先抄约定**。核验语料去重后的 7 份线性队列卷里有两种：队尾指“最后一个元素”、两个指针初值都是 –1（9618_s24_41、9618_s25_43、9618_w25_43、9618_s26_41）；队尾指“下一空位”、初值 0，队首初值 –1（9618_w22_42、9618_w23_41、9618_w24_42）。队首永远指“第一个元素”。
2. **Enqueue**（N 个元素）：
   - 队尾指最后一个元素：满 = `Tail == N - 1`；先 `Tail + 1` 再存。
   - 队尾指下一空位：满 = `Tail == N`（MS 也接受 `> N - 1`）；先存 `Queue[Tail]` 再 `Tail + 1`。
   - 两种都要：**存入第一个元素时把 Head 从 –1 改成 0**（`if Head == -1: Head = 0`）。这是本型独有的一分。
3. **Dequeue**：空的条件要覆盖两种情况——从没存过（`Head == -1`），以及存过又全部取完（`Head > Tail`；队尾指下一空位时是 `Head == Tail`）。只写 `Head == -1` 会漏掉第二种（9618_s25_43:1(c) 的考官报告）。不空：先取 `Queue[Head]`，再 `Head + 1`，再返回。
4. **线性队列不回绕**：取走的格子不再使用，所以 Tail 到末尾就是满，哪怕前面空着。题目没说 circular 就不要写 `Tail = 0`。

**Python 模板**（队尾指最后一个元素，两个指针初值 –1）

```python
Queue = [-1] * 50         # INTEGER, 50 elements, all initialised to -1
HeadPointer = -1          # INTEGER, index of the first element
TailPointer = -1          # INTEGER, index of the last element


def Enqueue(Data):        # Data : INTEGER, returns BOOLEAN
    global HeadPointer, TailPointer
    if TailPointer == 49:                 # full   (tail = next free: TailPointer == 50)
        return False
    TailPointer = TailPointer + 1         # move, then store   (tail = next free: store, then move)
    Queue[TailPointer] = Data
    if HeadPointer == -1:                 # first item ever stored
        HeadPointer = 0
    return True


def Dequeue():            # returns INTEGER
    global HeadPointer
    if HeadPointer == -1 or HeadPointer > TailPointer:   # never used, or emptied
        return -1
    ReturnValue = Queue[HeadPointer]      # read before moving the pointer
    HeadPointer = HeadPointer + 1
    return ReturnValue
```

**得分表述**（引自对应 MS）
- 「(Global) HeadPointer and TailPointer initialised with –1」⟦9618_s25_43:1(a)⟧
- 「(Otherwise) storing data item at TailPointer + 1 (check incrementing)」⟦9618_s25_43:1(b)⟧
- 「Checking if this is the first element and incrementing/storing 0 in HeadPointer」⟦9618_s25_43:1(b)⟧
- 「Accessing and returning element at Queue[HeadPointer] (before HeadPointer is incremented)」⟦9618_s25_43:1(c)⟧
- 「… incrementing tail pointer (after adding to queue)」⟦9618_w22_42:3(b)⟧
- 「tail pointer declared initialised to 0」⟦9618_w22_42:3(a)⟧

**得分点地图**（口径同 SQ-01：核验语料 2022–2026s、主题型行、去掉 `equivalent_of`、同一行同一标签计一次、s26 只进计数。共 20 行，19 行拆了得分点；“行数”为这 19 行里出现该标签的行数）

| 技能标签 | 行数 | MS 常见写法 |
|:--|--:|:--|
| `queue-array` | 19 | Checking if queue is full / empty；incrementing TailPointer / HeadPointer；first element … HeadPointer to 0 |
| `module-header` | 13 | Function Enqueue() header (and end) taking one (integer) parameter |
| `array-index`、`return-value` | 各 7 | storing data item at TailPointer + 1；returning element at Queue[HeadPointer] |
| `initialise-variables` | 6 | … initialised to –1 / 0 |
| `boolean-return` | 5 | returning FALSE if full and TRUE if not full |
| `declare-array`、`global-scope` | 各 5 | (Global) Queue array with 50 integer elements |

**几乎每次都有的分**：Enqueue 的“判满 + FALSE”“存在正确位置”“移动队尾”“第一次入队把队首设为 0”；Dequeue 的“判空 + 题给值”“先取再移队首”。

**易错与失分**
- 把线性队列写成循环队列：考官报告指出这是 9618_s25_43 第 1 题最常见的错误，判满判空因此全错（9618_s25_43:1(b)、9618_s25_43:1(c)）。
- 把队列当栈：Enqueue 里去加 Head（9618_s25_43:1(b) 的考官报告）。
- 队尾指“下一空位”时先加 1 再存（9618_w22_42:3(b) 的考官报告）；队尾指“最后一个元素”时反过来，要先加 1 再存（9618_s25_43:1(b) 的考官报告）。
- 判空只写 `Head == -1`，漏掉“存过又取完”（9618_s25_43:1(c) 的考官报告）。
- 初值写反：考官报告指出常见错误是把队首设为 0、或把队尾设为 –1（9618_w22_42:3(a)）。
- 题目要求返回整数 –1 却返回字符串，或要求返回 "false"（字符串）却返回布尔值——照题目写的类型返回。

#### 代表题精讲　⟦9618_s25_43:1(b)⟧

**在考什么**　程序从文本文件读整数存进线性队列 `Queue`（最多 50 个元素）。`HeadPointer` 存第一个元素的下标、初值 –1；`TailPointer` 存**最后一个元素**的下标、初值 –1。Enqueue() 带一个整数参数：满了返回 FALSE；存入后返回 TRUE；按需要更新指针。6 分，MS 6 点。同一大题：1(a) 声明（3 分，SQ-02）、1(c) Dequeue()（5 分，SQ-02）、1(d) CreateQueue() 读 QueueData.txt 逐行入队（FL-01）、1(e)(i) 主程序出队求和（SQ-04 的变式）、1(e)(ii) 截图。讲解时请对照原卷 QP p.2（题干、1(a)、1(b)）、p.3（1(c)–1(e)）；MS p.7–18（1(b) 清单 p.9、Python 范例 p.10）。

**完整作答**（整道第 1 题的程序；`Question1_J25.py`，与 QueueData.txt 放在同一文件夹）

```python
# ---- 1(a) ----
Queue = [-1] * 50          # INTEGER, 50 elements, all -1
HeadPointer = -1           # INTEGER, index of the first element
TailPointer = -1           # INTEGER, index of the last element


# ---- 1(b) ----
def Enqueue(Data):         # Data : INTEGER, returns BOOLEAN
    global TailPointer, HeadPointer
    if TailPointer == 49:              # full: the last element is already used
        return False
    TailPointer = TailPointer + 1      # move first, then store
    Queue[TailPointer] = Data
    if HeadPointer == -1:              # first item ever stored
        HeadPointer = 0
    return True


# ---- 1(c) ----
def Dequeue():             # returns INTEGER
    global HeadPointer
    if HeadPointer == -1 or HeadPointer > TailPointer:   # never used, or all removed
        return -1
    ReturnValue = Queue[HeadPointer]   # read before moving the pointer
    HeadPointer = HeadPointer + 1
    return ReturnValue


# ---- 1(d) ----
def CreateQueue():
    try:
        File = open("QueueData.txt", "r")
        Line = File.readline()
        while Line != "":                          # loop until end of file
            Value = int(Line.strip())              # remove newline, convert
            if Enqueue(Value) == False:
                print("Queue full")
            Line = File.readline()
        File.close()
    except IOError:
        print("File not found")


# ---- main program ----
if __name__ == "__main__":
    # 1(e)(i)
    CreateQueue()
    Total = 0
    Value = Dequeue()
    while Value != -1:
        Total = Total + Value
        Value = Dequeue()
    print("Total:", Total)
```

在官方源文件 QueueData.txt（45 行，CRLF 行尾）上实际运行，输出 `Total: 3059`，与 MS 1(e)(ii)「screenshot showing 3059」⟦9618_s25_43:1(e)(ii)⟧ 一致。另用 Python 直接调用：空队列 Dequeue 返回 –1；入队 50 个都返回 True、第 51 个返回 False，此时 Head = 0、Tail = 49；再出队 50 个按入队顺序取回，之后 Dequeue 返回 –1（Head > Tail 的情况）；在没有数据文件的文件夹里调用 CreateQueue 输出提示、不崩溃。

**与 MS 逐点对齐**（1(b)，6 分，MS 6 点，编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function Enqueue() header (and end) taking one (integer) parameter | `def Enqueue(Data):` | `module-header` |
| 2 | Checking if Queue is full … | `if TailPointer == 49:` | `queue-array` |
| 3 | …returning FALSE if full and TRUE if not full | `return False` / `return True` | `boolean-return` |
| 4 | (Otherwise) storing data item at TailPointer + 1 (check incrementing) | 先 `TailPointer = TailPointer + 1`，再 `Queue[TailPointer] = Data` | `queue-array`、`array-index` |
| 5 | Incrementing TailPointer | `TailPointer = TailPointer + 1` | `queue-array` |
| 6 | Checking if this is the first element and incrementing/storing 0 in HeadPointer | `if HeadPointer == -1: HeadPointer = 0` | `queue-array` |

MS 的 Python 范例（p.10）用 `if TailPointer < 49:` 把“不满”放在前面，与本作答等价。1(c)（5 分）：函数头且各情况都返回 / 判空 / 空时返回 –1 / 先取 `Queue[HeadPointer]` 再移 / Head 加 1；MS 范例的判空写成 `HeadPointer > -1 and HeadPointer <= TailPointer` 的反面（p.13），与本作答相同。

**证据格怎么交**　1(a)、1(b)、1(c) 各一格代码。1(a) 要看得出三者是全局的、数组真的有 50 个 –1。1(e)(ii) 是截图格：只看输出里有没有 3059（见 MP-03）。

**直观**　排队买票：第一个人来时窗口才“开张”（Head 从 –1 变成 0）；后来的人站到队尾；窗口叫号从队首叫起。线性队列的队伍只往前走、不绕回，排到第 50 个位置就算满了。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s25_43_q1/`（整道第 1 题）。前置阶梯 **L08 E04**（循环队列，先把指针移动练熟；线性队列就是去掉绕回）、**L07 E03**（逐行读文件）。

**下一道变式**　⟦9618_w22_42:3(b)⟧　（100 个整数的线性队列，**队尾指下一空位、初值 0，队首初值 –1**：`TailPointer < 100` 才不满，先存 `Queue[TailPointer]` 再加 1，第一个元素时同样把 Head 设为 0。3(a) 的声明正好考这两个初值。注意 MS 的 Python 范例（MS p.21）函数里给 `HeadPointer` 赋值却只写了 `global Queue`、`global TailPointer`，照抄运行会报 `UnboundLocalError`——得分照 MS 清单，自己写时把 `HeadPointer` 也写进 `global`。讲解时请对照原卷 QP p.8。）

<!-- auto:drills P4-SQ-02 -->

### P4-SQ-03　数组实现循环队列　{#P4-SQ-03}

<!-- auto:stats P4-SQ-03 -->

**考法**　①声明循环队列数组、Head / Tail 指针与 NumberOfItems（元素可以是记录：先建空记录填满数组，2–4 分）；②写 Enqueue()：用个数判满，存入后 Tail 加 1、**到末尾回到 0**，个数加 1（6–7 分；一题是补全题给伪代码的 5 个空）；③写 Dequeue()：用个数判空，取出 Head 元素，Head 加 1 并回绕，个数减 1（6 分）。

**识别信号**　circular queue；NumberOfItems / NumberItems；Head / Tail 到末尾后回到开头（题干常不明说，靠“circular”一词）；returns −1 if the circular queue is full；returns a null or empty record if the circular queue is empty。

**解题思路**
1. **判满判空只看个数**：满 = `NumberOfItems == 容量`，空 = `NumberOfItems == 0`。不要用 Head、Tail 的大小关系判断（回绕后 Tail 可能比 Head 小）。
2. **回绕**：指针加 1 之后，若等于容量就设为 0（`if Tail == 5: Tail = 0`）。MS 也接受“若原来是 4 就设 0，否则加 1”的写法。Head 与 Tail 都要回绕。
3. **约定照题目**：Tail 指“下一空位”、三个变量初值都是 0（9618_s23_42、9618_s22_41）时，先存 `Queue[Tail]` 再移 Tail；Tail 指“最后一个元素”、指针初值 –1（9618_s25_41）时，先移再存，而且第一个元素要把两个指针都设成 0、取空后再把两个指针设回 –1（该题 MS 的单独得分点）。
4. **个数同步**：Enqueue 成功个数加 1，Dequeue 成功个数减 1。
5. **元素是记录**时：数组每一格放一个**单独的**空记录（循环里每次新建一个），Dequeue 在空队列时返回一个空记录（ID 为 ""、数量为 –1），而不是 –1 或 None（9618_s23_42:2(d) 的考官报告）。

**Python 模板**（Tail 指下一空位，三者初值 0）

```python
Queue = [""] * 10         # STRING, 10 elements
Head = 0                  # INTEGER, index of the first item
Tail = 0                  # INTEGER, index where the next item goes
NumberOfItems = 0         # INTEGER


def Enqueue(NewItem):     # NewItem : STRING, returns BOOLEAN
    global Tail, NumberOfItems
    if NumberOfItems == 10:               # full
        return False
    Queue[Tail] = NewItem
    Tail = Tail + 1
    if Tail == 10:                        # wrap round
        Tail = 0
    NumberOfItems = NumberOfItems + 1
    return True


def Dequeue():            # returns STRING
    global Head, NumberOfItems
    if NumberOfItems == 0:                # empty
        return ""                         # the value given in the question
    Item = Queue[Head]
    Head = Head + 1
    if Head == 10:                        # wrap round
        Head = 0
    NumberOfItems = NumberOfItems - 1
    return Item
```

**得分表述**（引自对应 MS）
- 「Global variables Head, Tail and NumberOfItems all initialised to 0」⟦9618_s23_42:2(b)⟧
- 「… increments Tail and resets to 0 if 5」⟦9618_s23_42:2(c)⟧
- 「Increments number of items and returns 1」⟦9618_s23_42:2(c)⟧
- 「Incrementing Head and changing value 0 if it is 4/5」⟦9618_s23_42:2(d)⟧
- 「Checking if queue is full (NumberItems = 20) and returning FALSE」⟦9618_s25_41:1(b)⟧
- 「… changing head pointer to 0 if it's more than 9 after incrementing」⟦9618_s22_41:3(c)⟧

**得分点地图**（口径同 SQ-01。共 9 行，全部拆了得分点，来自 3 份卷；“行数”为出现该标签的行数）

| 技能标签 | 行数 | MS 常见写法 |
|:--|--:|:--|
| `queue-array` | 9 | Checks if queue is full / empty；increments Tail and resets to 0；decrement number of items |
| `module-header` | 6 | Function Enqueue() header (and end) taking one parameter |
| `return-value` | 4 | returns -1 / returning appropriate empty record |
| `initialise-variables` | 3 | Head, Tail and NumberOfItems all initialised to 0 |
| `declare-array` | 3 | QueueArray declared as 1D array as string with 10 elements |
| `record-type`、`array-of-records`、`global-scope` | 各 2 | One record declared setting ID to "" and Quantity to -1 … stored in all 5 array elements |

**几乎每次都有的分**：用个数判满判空、指针加 1 后回到 0（Enqueue、Dequeue 各一次）、个数加减 1。

**易错与失分**
- 忘了回绕，写成线性队列：考官报告指出较弱的答卷只把 Tail 加 1、不回到 0（9618_s23_42:2(c)），9618_s25_41:1(b) 的考官报告也说很少有人写对循环队列。
- 不用个数判满，去逐格找空位（9618_s23_42:2(c) 的考官报告）。
- 初值换成 –1：考官报告指出题目给了初值就要用（9618_s23_42:2(b)）。
- Dequeue 空时返回 –1、None，而题目要的是空记录（9618_s23_42:2(d) 的考官报告）；`return` 写在改指针之前，后面的语句永远执行不到（同一份考官报告）。
- 记录数组用 `[SaleData("", -1)] * 5`：五格是同一个对象，改一格五格都变；要在循环里每次新建。

#### 代表题精讲　⟦9618_s23_42:2(c)⟧

**在考什么**　每笔销售有 ID 与数量（如 "ABC" 与 2），存进循环队列。2(a) 声明记录 `SaleData`；2(b) 全局数组 `CircularQueue`（5 个元素）、全局 `Head`、`Tail`、`NumberOfItems`，初值都是 0，数组每格放一个空记录（ID 为 ""、数量 –1）。2(c) Enqueue()：参数是一条新记录，**插入在 Tail 指的那一格**，更新指针与个数；满了返回 –1，成功返回 1。6 分，MS 6 点。同一大题：2(d) Dequeue()（6 分，SQ-03）、2(e) EnterRecord() 输入并入队（MP-01）、2(f)(i) 主程序、2(f)(ii) 截图。讲解时请对照原卷 QP p.5（题干、2(a)–2(c)）、p.6（2(d)、2(e)）、p.7（2(f) 的六条记录表）；MS p.11–22（2(c) 的 Python 范例在 p.15，2(d) 在 p.17）。

**完整作答**（整道第 2 题的程序；`Question2_J2023.py`）

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

按 QP p.7 的表输入 ADF 10、OOP 1、BXW 5、XXZ 22、HQR 6、LLP 3，再输入 LLP 3，实际运行输出：5 次 `Stored`、1 次 `Full`、`ADF 10`、`Stored`，最后五行 `LLP 3`、`OOP 1`、`BXW 5`、`XXZ 22`、`HQR 6`——与 MS 2(f)(ii) 的截图样例一致（第二次入队的 LLP 回绕到了下标 0）。另用 Python 直接调用：空队列 Dequeue 返回 ID 为 "" 的空记录；连入 5 条都返回 1、第 6 条返回 –1；出一条再入一条后 Tail 回到 1。

**与 MS 逐点对齐**（2(c)，6 分，MS 6 点，编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function Enqueue() header (and end) taking one parameter (type SaleData) | `def Enqueue(RecordToAdd):` | `module-header` |
| 2 | Checks if queue is full … | `if NumberOfItems == 5:` | `queue-array` |
| 3 | … and returns -1 | `return -1` | `return-value` |
| 4 | (otherwise) Inserts parameter to CircularQueue[Tail] … | `CircularQueue[Tail] = RecordToAdd` | `queue-array`、`array-of-records` |
| 5 | … increments Tail and resets to 0 if 5 | `Tail = Tail + 1`；`if Tail == 5: Tail = 0` | `queue-array` |
| 6 | Increments number of items and returns 1 | `NumberOfItems = NumberOfItems + 1`；`return 1` | `queue-array`、`return-value` |

2(d)（6 分）：函数头 / 判空 / 空时返回空记录 / 返回 Head 处的记录 / Head 加 1 并回绕 / 个数减 1。2(b)（4 分）：数组 5 格 SaleData / 三个变量初值 0 / 建一个空记录 / 存进全部 5 格。

**证据格怎么交**　2(a)–2(e) 每格一段代码。2(b) 的格里要同时看到声明和“填满 5 个空记录”的循环。2(f)(ii) 的截图要能看到全部输入、5 次 Stored 与 1 次 Full、出队的 ADF 10、再次存入的 LLP 3、最后 5 条记录（MS 列了这五样，见 MP-03）。

**直观**　一张 5 个座位的圆桌：新客人坐到 Tail 指的座位，Tail 往下一个座位走，走过第 5 个座位就回到第 1 个；桌上坐满 5 人（数人数，不看座位号）就不能再坐。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s23_42_q2/`（整道第 2 题）。前置阶梯 **L08 E04**（循环队列：两个指针都绕回）、**L08 E01**（记录）。

**下一道变式**　⟦9618_s25_41:1(b)⟧　（20 个整数的循环队列，`HeadPointer`、`TailPointer` 初值 –1，`NumberItems` 初值 0：用 `NumberItems = 20` 判满；队列为空时第一个元素要把两个指针都设为 0；否则 Tail 先加 1、到 20 回到 0，再存。1(d) 的 Dequeue 还多一个得分点：取完最后一个元素后把两个指针设回 –1。讲解时请对照原卷 QP p.2–3。）

<!-- auto:drills P4-SQ-03 -->

### P4-SQ-04　用栈或队列的操作完成处理　{#P4-SQ-04}

<!-- auto:stats P4-SQ-04 -->

**考法**　在过程、函数或主程序里调用已写好的 ADT 操作完成一件事：①两个栈各出一个配对输出，缺一方时把另一方放回（9618_s23_41:3(c)）；②出栈直到空，找最大最小（9618_w25_41:1(e)）或按运算符计算（9618_s25_42:1(e)）；③出队直到返回 –1，求和（9618_s25_43:1(e)(i)）；④出队后统计到记录数组（9618_w23_41:2(c)(iii)）、做游程压缩（9618_w25_43:2(e)）；⑤按条件把参数 Push 进不同的栈（元音 / 辅音，9618_w23_42:1(b)(i)）并在主程序里按选择出栈（9618_w23_42:1(d)(i)）。4–7 分。

**识别信号**　uses Pop() / Dequeue() to …；pops each integer from the stack until the stack is empty；repeatedly … until the return value is –1 / "False"；pops the next item from both …；If there is no data in …, … is pushed back；If the parameter is a vowel, it is pushed onto …。

**解题思路**
1. **只通过操作访问数据**：用 `Pop()` / `Dequeue()` 的返回值，不去直接读数组或指针。考官报告指出直接遍历栈数组是常见错误（9618_w25_41:1(e)），也有考生不用返回值、改去手动检查指针判断队列空没空（9618_s25_43:1(e)(i)）。
2. **每次调用只调一次、先存下返回值**：`Value = Pop()`，后面的判断与计算都用 `Value`。在 `while` 条件里调一次、循环体里又调一次，会丢掉一个值（9618_w25_41:1(e) 的考官报告）。
3. **“直到空”用哨兵循环**：先取一次，`while Value != 空值:` 处理，循环末尾再取一次。空值就是 Pop / Dequeue 在空时返回的那个值（–1、–999、""、"False"），要与前面小问一致。
4. **检查失败再补救**：配对类题目，任何一方取回空值时，按题目把另一方 Push 回去并输出提示；两方都有才输出结果。
5. **处理部分按题目**：求和、最值（自己比较，不用 `max()`，D10 ③）、计数、拼字符串。算法本身若 ≥ 2 分会进副题型（如游程压缩 → PR-02）。

**Python 模板**（出到空为止 + 处理）

```python
def ProcessAll():
    Total = 0
    Highest = -1                     # set from the first value, or a value below the range
    Value = Pop()                    # call once, keep the return value
    while Value != -999:             # the "empty" value returned by Pop()
        Total = Total + Value
        if Value > Highest:
            Highest = Value
        Value = Pop()                # next value at the end of the loop
    print("Total", Total, "Highest", Highest)
```

**得分表述**（引自对应 MS）
- 「Calling Dequeue() and storing/using return value …」⟦9618_s25_43:1(e)(i)⟧
- 「… repeatedly until return value is –1」⟦9618_s25_43:1(e)(i)⟧
- 「Checking if no colour and outputting "No colour" …」⟦9618_s23_41:3(c)⟧
- 「….pushing the removed animal back onto the stack」⟦9618_s23_41:3(c)⟧
- 「Looping until the stack is empty」⟦9618_s25_42:1(e)⟧
- 「Finds and outputs highest value from returned values」⟦9618_w25_41:1(e)⟧

**得分点地图**（口径同 SQ-01。共 8 行，全部拆了得分点，来自 7 份卷；“行数”为出现该标签的行数）

| 技能标签 | 行数 | MS 常见写法 |
|:--|--:|:--|
| `procedure-call` | 7 | Calling Pop() / Dequeue() and storing/using return value |
| `module-header` | 6 | Procedure header (and end) |
| `output-format`、`nested-if`、`accumulator`、`return-value` | 各 5 | outputting "No colour"；adding together all return values；outputting the total |
| `stack-array` | 3 | pushing the removed animal back onto the stack |
| `sentinel-loop` | 3 | … repeatedly until return value is –1 / "False" |

**几乎每次都有的分**：“调用操作并存下返回值”与“循环到返回空值为止”，再加处理结果的输出。

**易错与失分**
- 直接读栈的数组，而不是调用 Pop（9618_w25_41:1(e) 的考官报告）。
- 在循环条件里调用一次、循环体里又调用一次，第一次的返回值没用上（9618_w25_41:1(e) 的考官报告）。
- 不检查返回值就输出：考官报告指出颜色用完时程序会出错（9618_s23_41:3(c)）。
- 不知道空队列时 Dequeue 返回 –1，改去检查指针（9618_s25_43:1(e)(i) 的考官报告）——用前面小问写好的返回值约定。
- 找最大最小直接用 `max()` / `min()`：题目要你写算法时不给分（D10 ③）。

#### 代表题精讲　⟦9618_s23_41:3(c)⟧

**在考什么**　两个栈：`Animal`（最多 20 个动物名）与 `Colour`（最多 10 个颜色），指针 `AnimalTopPointer`、`ColourTopPointer` 都**指下一空位、初值 0**；PopAnimal() / PopColour() 空时返回 ""。OutputItem()：从两个栈各出一个，同一行输出“颜色 动物”（如 "black horse"）；`Colour` 没数据时把动物 Push 回 `Animal` 并输出 "No colour"；`Animal` 没数据时把颜色 Push 回 `Colour` 并输出 "No animal"。5 分（MS：1 mark each to max 5，共 5 点）。同一大题：3(a) 声明、3(b)(i)(ii)(iv) 两个栈的 Push / Pop（SQ-01，QP 给了伪代码）、3(b)(iii)(v) ReadData() 读两个文件入栈（FL-01）、3(d)(i) 主程序调用 ReadData() 与 4 次 OutputItem()（MP-01）、3(d)(ii) 截图。讲解时请对照原卷 QP p.8（3(a)、3(b)(i) 伪代码）、p.9（3(b)(ii)–(iv)）、p.10（3(b)(v)–3(d)）；MS p.26–38（3(c) 的 Python 范例在 p.37）。

**完整作答**（整道第 3 题的程序；`Question3_J2023.py`，与 AnimalData.txt、ColourData.txt 放在同一文件夹）

```python
# ---- 3(a) ----
Animal = [""] * 20          # STRING, 20 elements
Colour = [""] * 10          # STRING, 10 elements
AnimalTopPointer = 0        # INTEGER, next free space in Animal
ColourTopPointer = 0        # INTEGER, next free space in Colour


# ---- 3(b)(i) ----
def PushAnimal(DataToPush):          # DataToPush : STRING, returns BOOLEAN
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True


# ---- 3(b)(ii) ----
def PopAnimal():                     # returns STRING
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData


# ---- 3(b)(iv) ----
def PushColour(DataToPush):          # DataToPush : STRING, returns BOOLEAN
    global ColourTopPointer
    if ColourTopPointer == 10:       # Colour has 10 elements, not 20
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True


def PopColour():                     # returns STRING
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData


# ---- 3(b)(iii) and 3(b)(v) ----
def ReadData():
    try:
        File = open("AnimalData.txt", "r")
        for Line in File:
            PushAnimal(Line.strip())
        File.close()
    except IOError:
        print("AnimalData.txt not found")
    try:
        File = open("ColourData.txt", "r")
        for Line in File:
            PushColour(Line.strip())
        File.close()
    except IOError:
        print("ColourData.txt not found")


# ---- 3(c) ----
def OutputItem():
    ColourReturned = PopColour()
    AnimalReturned = PopAnimal()
    if ColourReturned == "":
        print("No colour")
        if AnimalReturned != "":         # only push back a real animal
            PushAnimal(AnimalReturned)
    elif AnimalReturned == "":
        print("No animal")
        PushColour(ColourReturned)
    else:
        print(ColourReturned, AnimalReturned)


# ---- main program ----
if __name__ == "__main__":
    # 3(d)(i)
    ReadData()
    for Count in range(4):
        OutputItem()
```

在官方源文件（AnimalData.txt 8 行、ColourData.txt 10 行，CRLF 行尾，最后一行不换行）上实际运行，输出 `pink hamster`、`blue elephant`、`white eagle`、`yellow rabbit`，与 MS 3(d)(ii) 的截图样例一致（后进先出：最后读入的 hamster、pink 最先出来）。另用 Python 直接调用：继续调用到动物用完时输出 `No animal`，颜色被放回（ColourTopPointer 停在 2）；只有动物、没有颜色时输出 `No colour`，动物被放回；在没有数据文件的文件夹里调用 ReadData 输出提示、不崩溃。

**与 MS 逐点对齐**（3(c)，5 分，MS 5 点，编号一致）

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure heading (and close where appropriate) and outputting the colour and animal using PopColour() and PopAnimal() (only if both are successfully popped) | `def OutputItem():`；两个返回值都非空时 `print(ColourReturned, AnimalReturned)` | `module-header`、`procedure-call`、`output-format` |
| 2 | Checking if no colour and outputting "No colour" … | `if ColourReturned == "": print("No colour")` | `nested-if`、`output-format` |
| 3 | ….pushing the removed animal back onto the stack | `PushAnimal(AnimalReturned)` | `procedure-call`、`stack-array` |
| 4 | Checking if no animal and outputting "No animal" … | `elif AnimalReturned == "": print("No animal")` | `nested-if`、`output-format` |
| 5 | …pushing the removed colour back onto the stack | `PushColour(ColourReturned)` | `procedure-call`、`stack-array` |

**MS 范例的一个边界**：MS 的 Python 范例（p.37）在颜色为空时直接 `PushAnimal(AnimalReturned)`，如果两个栈同时为空，会把空串 "" 压进 Animal。QP 没定义“两个都空”怎么办；本作答只在取到真实动物时放回，得分点不受影响（照 MS 得分；自己写时按模板处理边界，D44 ④）。

**证据格怎么交**　3(c) 一格代码。3(d)(ii) 截图只要显示四行输出（MS 只给了截图样例，没有文字清单）。

**直观**　两摞卡片，一摞颜色、一摞动物，每次各翻最上面一张拼成一句话；哪一摞翻空了，就把另一张放回它那一摞的最上面，喊一声“没有颜色了”或“没有动物了”。

**对应练习与阶梯**　真题练习 `practice/p4/9618_s23_41_q3/`（整道第 3 题）。前置阶梯 **L08 E05**（括号配对：反复 Push / Pop 并检查返回值）、**L03 E02**（哨兵循环）。

**下一道变式**　⟦9618_w25_41:1(e)⟧　（FindValues()：反复 Pop() 直到栈空——Pop 在空栈时返回 –999——同时找出最大值与最小值并带说明输出。注意用一个变量存每次的返回值，自己比较大小，不用 `max()` / `min()`。讲解时请对照原卷 QP p.3。）

<!-- auto:drills P4-SQ-04 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| SQ-01 vs SQ-04 | 写 Push / Pop 本身（判满判空、移指针）→ SQ-01；调用写好的 Push / Pop 去做别的事 → SQ-04 | 函数名是不是 Push / Pop |
| SQ-02 vs SQ-03 | 指针到末尾就是满、不回到 0 → SQ-02；有 circular、到末尾回到 0、用个数判满判空 → SQ-03 | 有没有 circular 与 NumberOfItems |
| SQ-04 vs MP-02 | 在模块里循环 Pop / Dequeue 处理数据 → SQ-04；主程序把一串输入或题给数据逐个 Push / Enqueue 并报告成败 → MP-02 | 数据是“取出来处理”还是“放进去报告” |
| SQ-04 vs FL-01 | 读文件、每行 Push / Enqueue（文件得分点在场）→ FL-01；数据已在栈 / 队列里，取出来处理 → SQ-04 | 有没有打开文件 |
| SQ-01 ～ SQ-03 vs AR-04 | 写操作 → SQ；只按下标顺序输出整个数组与指针（如 PrintArray）→ AR-04 | 输出还是存取 |
| 指针两种约定 | 指最后一个元素（初值 –1）：先移后存、取当前格；指下一空位（初值 0）：先存后移、取前一格 | 题干的 “index of the last element” / “next free space” |
| 栈 vs 队列的空值 | Pop / Dequeue 在空时返回什么由题目定（–1、–999、""、"False"、空记录），后面的 SQ-04 小问用同一个值作哨兵 | 看前面小问的题干 |
