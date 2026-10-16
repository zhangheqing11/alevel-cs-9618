# L08 · 记录 TYPE…ENDTYPE；用数组 + 指针实现栈与队列

> 考纲 10.1（记录）、10.4（ADT：栈、队列、链表；用数组实现）（考纲 p.28–29）；预习 19.1（A2：写出栈、队列的插入与删除算法，考纲 p.37）· 指南 §4（p.12–14）

## 本级目标

学完本级，你能：

1. 用 `TYPE … ENDTYPE` 定义记录，声明记录变量与记录数组，用点号读写字段；在 Python 里用只有属性的 class 表示记录（P4 的标准做法）。
2. 知道记录赋值在伪代码里是**复制**、在 Python 里只是**起别名**；正确建立「记录的数组」。
3. 用一个数组加一个栈顶指针实现栈（入栈、出栈、满、空）。
4. 用一个数组加队首、队尾指针和计数实现**循环**队列（入队、出队、绕回）。
5. 用栈解决一个小问题（括号配对）。AS 阶段（10.4）只要求会描述和使用这些结构；A2（19.1）要写出算法——本级两者都练。

## 伪代码 ↔ Python 对照

### 1. 记录类型（指南 p.13–14）

```pseudocode
TYPE StudentRecord
   DECLARE LastName : STRING
   DECLARE FirstName : STRING
   DECLARE DateOfBirth : DATE
   DECLARE YearGroup : INTEGER
   DECLARE FormGroup : CHAR
ENDTYPE

DECLARE Pupil1 : StudentRecord
DECLARE Form : ARRAY[1:30] OF StudentRecord
Pupil1.LastName ← "Johnson"
Pupil1.YearGroup ← 6
FOR Index ← 1 TO 30
   Form[Index].YearGroup ← Form[Index].YearGroup + 1
NEXT Index
```

```python
from datetime import date


class StudentRecord:
    """Record type: every field is given a value of the right type in __init__."""

    def __init__(self) -> None:
        self.last_name: str = ""
        self.first_name: str = ""
        self.date_of_birth: date = date(2000, 1, 1)
        self.year_group: int = 0
        self.form_group: str = " "      # CHAR


pupil1 = StudentRecord()
form = [StudentRecord() for _ in range(30)]   # ARRAY[1:30] OF StudentRecord -> indexes 0 to 29
pupil1.last_name = "Johnson"
pupil1.year_group = 6
for index in range(30):
    form[index].year_group = form[index].year_group + 1
```

| 伪代码 | Python | 说明 |
|:--|:--|:--|
| `TYPE StudentRecord` … `ENDTYPE`（p.13） | `class StudentRecord:` + `__init__` 里给每个字段赋初值 | P4 题目明说「A class declaration can be used to declare a record」（9618_s24_42 的说明，见 ECR P4 2024 p.5） |
| 每个字段 `DECLARE <name> : <type>`（p.13） | `self.<name> = <初值>`，可加类型标注 | Python 没有字段声明；用初值和注释表明类型（ER s23 9618/41 Q3 p.39、ECR P4 2021 p.39 要求说明类型） |
| `DECLARE Pupil1 : StudentRecord`（p.14） | `pupil1 = StudentRecord()` | 要加括号才是创建对象 |
| `Pupil1.LastName ← "Johnson"`（p.14） | `pupil1.last_name = "Johnson"` | 点号访问字段 |
| `DECLARE Form : ARRAY[1:30] OF StudentRecord`（p.14） | `form = [StudentRecord() for _ in range(30)]` | **不能**写 `[StudentRecord()] * 30`：30 个元素是同一个对象 |
| `Form[Index].YearGroup`（p.14） | `form[index].year_group` | 先下标、后点号 |
| `Pupil2 ← Pupil1`（p.14） | `pupil2 = copy.copy(pupil1)`（先 `import copy`） | 伪代码是复制；Python 的 `pupil2 = pupil1` 只是起别名 |

Python 也可以用 `@dataclass` 写记录（更短），但 P4 考官的范答用的是普通 class，本阶梯先用普通 class，L12 学 OOP 时再对比。

### 2. 枚举与指针（指南 p.12，了解即可）

- 枚举：`TYPE Season = (Spring, Summer, Autumn, Winter)`（p.12）↔ Python `enum.Enum`。考试里偶尔出现定义题。
- 指针：`TYPE TIntPointer = ^INTEGER`（p.12）。Python 没有指针；**本阶梯（以及 P4）用数组下标充当指针**：栈顶指针、队首队尾指针、链表的 next 指针（L10）都是整数下标。

### 3. 栈：数组 + 栈顶指针（考纲 10.4、19.1）

后进先出（LIFO）。下面的伪代码用 1 起数组，`TopPointer = 0` 表示空栈：

```pseudocode
CONSTANT MaxSize = 8
DECLARE Stack : ARRAY[1:8] OF STRING
DECLARE TopPointer : INTEGER
TopPointer ← 0

FUNCTION Push(Item : STRING) RETURNS BOOLEAN
   IF TopPointer = MaxSize THEN
      RETURN FALSE                 // stack full
   ENDIF
   TopPointer ← TopPointer + 1
   Stack[TopPointer] ← Item
   RETURN TRUE
ENDFUNCTION

FUNCTION Pop() RETURNS STRING
   DECLARE Item : STRING
   IF TopPointer = 0 THEN
      RETURN ""                    // stack empty
   ENDIF
   Item ← Stack[TopPointer]
   TopPointer ← TopPointer - 1
   RETURN Item
ENDFUNCTION
```

```python
MAX_SIZE = 8
stack = [""] * MAX_SIZE   # ARRAY of 8 STRING -> indexes 0 to 7
top_pointer = -1          # -1 means the stack is empty (0-based indexes)


def push(item: str) -> bool:
    global top_pointer
    if top_pointer == MAX_SIZE - 1:
        return False      # stack full
    top_pointer = top_pointer + 1
    stack[top_pointer] = item
    return True


def pop() -> str:
    global top_pointer
    if top_pointer == -1:
        return ""         # stack empty
    item = stack[top_pointer]
    top_pointer = top_pointer - 1
    return item
```

- 两种约定都常见：1 起数组时空栈为 0；0 起数组时空栈为 -1。**P4 题目给了初值就照题目来**（ER s23 9618/41 Q3 p.39：题目要求栈顶指针初始化为 0，有考生写成了 -1）。
- 出栈不必清空元素，移动指针就够了：指针以上的位置都视为空。
- Python 里给全局指针重新赋值必须写 `global top_pointer`（L04 §5）。

### 4. 队列：线性与循环（考纲 10.4、19.1）

先进先出（FIFO）。只用 `Front`、`Rear` 两个指针、一直往后加的**线性队列**，出队后前面的位置就浪费了。**循环队列**在指针越过数组末尾时绕回开头，再用 `NumberOfItems` 判断满与空：

```pseudocode
CONSTANT QueueSize = 5
DECLARE Queue : ARRAY[1:5] OF STRING
DECLARE FrontPointer : INTEGER
DECLARE RearPointer : INTEGER
DECLARE NumberOfItems : INTEGER
FrontPointer ← 1
RearPointer ← 0
NumberOfItems ← 0

FUNCTION Enqueue(Item : STRING) RETURNS BOOLEAN
   IF NumberOfItems = QueueSize THEN
      RETURN FALSE                       // queue full
   ENDIF
   RearPointer ← RearPointer + 1
   IF RearPointer > QueueSize THEN
      RearPointer ← 1                    // wrap round
   ENDIF
   Queue[RearPointer] ← Item
   NumberOfItems ← NumberOfItems + 1
   RETURN TRUE
ENDFUNCTION

FUNCTION Dequeue() RETURNS STRING
   DECLARE Item : STRING
   IF NumberOfItems = 0 THEN
      RETURN ""                          // queue empty
   ENDIF
   Item ← Queue[FrontPointer]
   FrontPointer ← FrontPointer + 1
   IF FrontPointer > QueueSize THEN
      FrontPointer ← 1                   // wrap round
   ENDIF
   NumberOfItems ← NumberOfItems - 1
   RETURN Item
ENDFUNCTION
```

```python
QUEUE_SIZE = 5
queue = [""] * QUEUE_SIZE   # indexes 0 to 4
front_pointer = 0
rear_pointer = -1
number_of_items = 0


def enqueue(item: str) -> bool:
    global rear_pointer, number_of_items
    if number_of_items == QUEUE_SIZE:
        return False
    rear_pointer = (rear_pointer + 1) % QUEUE_SIZE     # wrap round
    queue[rear_pointer] = item
    number_of_items = number_of_items + 1
    return True


def dequeue() -> str:
    global front_pointer, number_of_items
    if number_of_items == 0:
        return ""
    item = queue[front_pointer]
    front_pointer = (front_pointer + 1) % QUEUE_SIZE   # wrap round
    number_of_items = number_of_items - 1
    return item
```

- 绕回在 1 起数组里写成 `IF RearPointer > QueueSize THEN RearPointer ← 1`，或 `RearPointer ← (RearPointer MOD QueueSize) + 1`；0 起的 Python 写 `(rear_pointer + 1) % QUEUE_SIZE`。
- 加入新元素时不需要移动已有的元素（ER s23 9618/22 Q3 p.19：常见错误是以为要先移动或删除队列里已有的内容）。

### 5. Python 的 list 方法与「数组 + 指针」

Python 的 `append` / `pop()` 可以直接当栈用，`collections.deque` 可以当队列用。但 P4 题目要求「用数组实现」时，必须写出数组和指针：ECR P4 2021 p.15–16 的点评里，有考生把题目要求的链表写成了普通 list、直接把新数据追加到末尾，没有使用题目规定的指针，因此不得分。

## 常见坑

1. **`TYPE` 定义写错**：字段前漏 `DECLARE`、漏 `ENDTYPE`、在 `TYPE` 头前面加 `DECLARE`、给字段写取值范围（ECR P2 2024 p.12；ER s24 9618/22 Q3 p.18；ER s22 9618/23 Q5 p.22 还有人把 TYPE 写成了过程声明）。
2. **记录数组声明写错**：元素类型写成 `STRING` 而不是记录类型、范围里用逗号（ECR P2 2024 p.13）。
3. **点号用错**：把「数组下标 + 字段名」写成二维下标，例如用 `Loan[Index, 1]` 代替 `Loan[Index].CandidateID`（ER w25 p.16 的例子，这里按指南写成方括号；另见 ER w24 9618/22 Q8 p.23、9618/23 Q8 p.28）。正确顺序是**先下标、后点号**。
4. **Python 的 `[Record()] * n`**：所有元素是同一个对象，改一个全变。
5. **Python 的 `pupil2 = pupil1`**：没有复制，改 `pupil1` 的字段 `pupil2` 也变。
6. **忘了 `global`**：`push`/`pop` 里给 `top_pointer` 赋值报 `UnboundLocalError`。
7. **满栈判断差一**：0 起数组时满栈是 `top_pointer == MAX_SIZE - 1`；写成 `== MAX_SIZE` 会多入一次，访问越界。
8. **出栈先减指针再取值**：取到的是下面那一个元素。顺序是「取值 → 减指针」；入栈是「加指针 → 存值」。
9. **队列不绕回**：队尾指针加到数组末尾以后报越界（Python `IndexError`），或者在还有空位时就报「满」。
10. **指针初值不照题目**（ER s23 9618/41 Q3 p.39）。
11. **该写数组 + 指针时用了 list 方法**（ECR P4 2021 p.15–16）。

## 延伸阅读

- Think Python 3e 第 14 章（CC BY-NC-SA 4.0）：[14.1 Programmer-defined types](https://allendowney.github.io/ThinkPython/chap14.html#programmer-defined-types)、[14.2 Attributes](https://allendowney.github.io/ThinkPython/chap14.html#attributes)、[14.4 Objects are mutable](https://allendowney.github.io/ThinkPython/chap14.html#objects-are-mutable)、[14.5 Copying](https://allendowney.github.io/ThinkPython/chap14.html#copying)。
- CS50P Lecture 8 讲义：[Classes](https://cs50.harvard.edu/python/notes/8/#classes)（只看「用 class 存一组属性」的部分，方法与继承留到 L12）。（CC BY-NC-SA 4.0）
- 教材 Langfield & Duddell 2e：13.02 The record type（p.211）、13.07–13.09 ADTs / Stacks / Queues（p.227–228）；A2 的 23.08–23.09 Stacks / Queues（p.421–422）、26.01 Records（p.447）。书中伪代码与 2027–29 指南不同时以指南为准。
- 官方：伪代码指南 §4（p.12–14）；SoW Unit 10（p.33：用纸格表演栈与队列、用 index/data/pointer 三列的表演示链表）。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-book-records/`](exercises/E01-book-records/spec.md) | 函数 + 记录类 | 是 | `TYPE` ↔ class；记录数组上的计数与查找 |
| [`exercises/E02-trace-records-alias/`](exercises/E02-trace-records-alias/spec.md) | 干跑 | 否 | 记录赋值 = 复制；记录数组的正确建法 |
| [`exercises/E03-array-stack/`](exercises/E03-array-stack/spec.md) | 函数（全局数组 + 指针） | 是 | 入栈、出栈、满、空 |
| [`exercises/E04-circular-queue/`](exercises/E04-circular-queue/spec.md) | 函数（全局数组 + 指针） | 是 | 入队、出队、绕回、满、空 |
| [`exercises/E05-bracket-check/`](exercises/E05-bracket-check/spec.md) | 函数 | 是 | 用栈检查括号配对 |
