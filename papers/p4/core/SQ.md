## SQ　栈与队列：伪代码 ↔ Python 对照与模板 {#core-SQ}

P4 交的是 Python，但题干常给伪代码（如 9618_s23_41:3(b)(i) 的 PushAnimal()、9618_s22_41:3(b) 要补全的 Enqueue），你要能逐行翻成 Python。伪代码按 2027–29 指南书写；Python 按考场写法：**标识符照抄题目**（`StackPointer`、`Enqueue`，不改成 snake_case）、数组建成真实的 list 并用注释写类型与大小（D10 ①）、指针初值照题目（D10 ②）。

### 1. 声明

| 内容 | QP 里的伪代码 / 文字 | Python | 注意 |
|:--|:--|:--|:--|
| 栈数组 | `DECLARE StackData : ARRAY[0:9] OF INTEGER` / “a 1D array of 10 integers” | `StackData = [0] * 10  # INTEGER, 10 elements` | 只写 `StackData = []` 不建元素，拿不到大小分 |
| 元素初值 | “all elements initialised to –1” | `Queue = [-1] * 50` | 字符串 "–1" 就写 `["-1"] * 20` |
| null 值 | “initialise each element with a null value” | `Stack = [None] * 30` 或题目情境里合适的空值 | 9618_w25_41:1(a) |
| 指针 | `DECLARE TopOfStack : INTEGER`、`TopOfStack ← -1` | `TopOfStack = -1  # INTEGER` | 写在所有函数外面（全局） |
| 记录元素 | `DECLARE CircularQueue : ARRAY[0:4] OF SaleData` | `CircularQueue = []` 再循环 `append(SaleData("", -1))` | 不能 `[SaleData("", -1)] * 5`（五格同一个对象） |
| 记录包住数组与指针 | `TYPE Queue … ENDTYPE` | 类，`__init__` 里建 `QueueArray`、`Headpointer`、`Tailpointer` | 9618_w24_42:2(a) |

伪代码的数组下标上下界写在声明里（`[0:9]`、`[1:10]`）；Python 的 list 永远从 0 开始。P4 题目几乎都直接说明“the index of the first element is 0”，下标照题目用即可；QP 给的伪代码若是 1 起数组，翻成 Python 时把上下界整体减 1（满的条件、回绕的值都要跟着改）。

### 2. 在函数里改全局变量

| 伪代码 | Python | 说明 |
|:--|:--|:--|
| 过程直接给全局 `TopPointer ← TopPointer + 1` | 函数开头 `global TopPointer`，再 `TopPointer = TopPointer + 1` | 不写 `global` → `UnboundLocalError`（9618_w22_42:3(b) 的 MS Python 范例就漏写了 `HeadPointer`） |
| `Stack[TopPointer] ← Item` | `Stack[TopPointer] = Item` | 只改数组的一格，不需要 `global`；写上也无妨 |
| `BYREF HeadPointer : INTEGER`（9618_s22_41:3(b)） | Python 不能按引用传整数：改用全局变量（`global`），或把新值 `return` 回去 | 证据里照题目的参数顺序写函数头 |

### 3. 栈

| 部件 | 伪代码（指下一空位，初值 0） | Python |
|:--|:--|:--|
| 头 | `FUNCTION Push(DataToPush : INTEGER) RETURNS BOOLEAN` | `def Push(DataToPush):  # INTEGER, returns BOOLEAN` |
| 判满 | `IF StackPointer = 10 THEN` / `RETURN FALSE` / `ENDIF` | `if StackPointer == 10: return False` |
| 存、移 | `StackData[StackPointer] ← DataToPush`、`StackPointer ← StackPointer + 1` | `StackData[StackPointer] = DataToPush`、`StackPointer = StackPointer + 1` |
| 判空 | `IF StackPointer = 0 THEN` / `RETURN -1` / `ENDIF` | `if StackPointer == 0: return -1` |
| 取、移 | `ReturnData ← StackData[StackPointer - 1]`、`StackPointer ← StackPointer - 1` | 同左，`←` 换成 `=` |

另一种约定（指栈顶元素，初值 –1）：满 = `TopOfStack == 容量 - 1`；Push 先 `+ 1` 再存；Pop 先取 `Stack[TopOfStack]` 再 `- 1`；空 = `TopOfStack == -1`。

```pseudocode
FUNCTION Pop() RETURNS STRING
   DECLARE ReturnData : STRING
   IF AnimalTopPointer = 0 THEN
      RETURN ""
   ELSE
      ReturnData ← Animal[AnimalTopPointer - 1]
      AnimalTopPointer ← AnimalTopPointer - 1
      RETURN ReturnData
   ENDIF
ENDFUNCTION
```

```python
def PopAnimal():                  # returns STRING
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData
```

### 4. 线性队列与循环队列

| 部件 | 线性队列（Tail 指最后一个元素，两指针初值 –1） | 循环队列（Tail 指下一空位，三者初值 0） |
|:--|:--|:--|
| 判满 | `if TailPointer == N - 1:` | `if NumberOfItems == N:` |
| 入队 | `TailPointer = TailPointer + 1`，再 `Queue[TailPointer] = Data` | `Queue[Tail] = Data`，再 `Tail = Tail + 1` |
| 第一个元素 | `if HeadPointer == -1: HeadPointer = 0` | 不需要（Head 初值就是 0） |
| 回绕 | 没有 | `if Tail == N: Tail = 0` |
| 个数 | 可没有 | `NumberOfItems = NumberOfItems + 1` / `- 1` |
| 判空 | `if HeadPointer == -1 or HeadPointer > TailPointer:` | `if NumberOfItems == 0:` |
| 出队 | `Item = Queue[HeadPointer]`，再 `HeadPointer = HeadPointer + 1` | `Item = Queue[Head]`，`Head = Head + 1`，`if Head == N: Head = 0` |

回绕的两种写法都对：`IF Tail = 5 THEN` / `Tail ← 0` / `ENDIF`（MS 范例多用这种）；或 `Tail ← (Tail + 1) MOD 5`，Python 写 `Tail = (Tail + 1) % 5`。伪代码的 `MOD` 对应 Python 的 `%`，`DIV` 对应 `//`。

```pseudocode
FUNCTION Enqueue(RecordToAdd : SaleData) RETURNS INTEGER
   IF NumberOfItems = 5 THEN
      RETURN -1
   ENDIF
   CircularQueue[Tail] ← RecordToAdd
   Tail ← Tail + 1
   IF Tail = 5 THEN
      Tail ← 0
   ENDIF
   NumberOfItems ← NumberOfItems + 1
   RETURN 1
ENDFUNCTION
```

```python
def Enqueue(RecordToAdd):         # RecordToAdd : SaleData, returns INTEGER
    global Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    CircularQueue[Tail] = RecordToAdd
    Tail = Tail + 1
    if Tail == 5:
        Tail = 0
    NumberOfItems = NumberOfItems + 1
    return 1
```

### 5. 用操作处理数据（SQ-04）

| 意图 | 伪代码 | Python |
|:--|:--|:--|
| 出到空为止 | `Value ← Pop()` / `WHILE Value <> -999` / … / `Value ← Pop()` / `ENDWHILE` | `Value = Pop()` / `while Value != -999:` / … / `Value = Pop()` |
| 调用并检查返回值 | `IF Push(Item) = FALSE THEN` / `OUTPUT "Stack full"` / `ENDIF` | `if Push(Item) == False: print("Stack full")` |
| 只调一次 | `Result ← Dequeue()` 后用 `Result` | `Result = Dequeue()` 后用 `Result`；不要在 `if Dequeue() == …` 里再调一次 |
| 放回 | `CALL PushAnimal(AnimalReturned)`（函数结果不用时） | `PushAnimal(AnimalReturned)` |

Python 的 `while` 是前测循环，相当于伪代码的 `WHILE … ENDWHILE`；伪代码的后测循环 `REPEAT … UNTIL 条件` 在 Python 里写成 `while True:` … `if 条件: break`。

### 6. 常见运行错误

| 现象 | 原因 | 改法 |
|:--|:--|:--|
| `UnboundLocalError: local variable 'TopPointer' referenced before assignment` | 函数里给全局指针赋值，没写 `global` | 函数第一行 `global TopPointer` |
| `IndexError: list index out of range` | 判满写成 `> 10` 而指针已到 10；或数组没建出元素（`[]`） | 照约定写判满；`[0] * 10` |
| 出队的值总是同一个 | 先 `return` 再移指针，或移指针前没存下返回值 | 先存局部变量，再移指针，最后 `return` |
| 记录数组改一格五格都变 | `[SaleData("", -1)] * 5` | 循环里每次新建一个记录 |
| 读进来的值带 `\r\n`，比较总是不相等 | 源文件是 CRLF 行尾 | `Line.strip()`，数字再 `int(...)` |
