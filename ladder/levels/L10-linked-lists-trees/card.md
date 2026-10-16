# L10 · 链表与二叉树（数组 + 指针实现）

> 考纲 19.1（链表、二叉树的查找与插入；栈、队列、链表的删除；用其他结构实现 ADT；graph 只需描述）（考纲 p.37）；10.4（AS：用数组实现链表）（考纲 p.29）· 指南 §3（数组 p.10）、§4（记录与指针 p.12–14）

## 本级目标

学完本级，你能：

1. 用数组（记录数组，或两个/三个并行数组）加整数指针表示链表与二叉树；说出 start pointer、free（empty）list pointer、null pointer 的作用。
2. 初始化空闲表；沿指针遍历、查找链表；从空闲表取结点做表头插入与按序插入；删除结点并把它还给空闲表。
3. 在二叉查找树里插入与查找（比较、沿左/右指针走、更新父结点的指针）。
4. 按 P4 的要求写 Python：全局数组真实建出并注释类型与大小，空指针照题目约定（常为 -1），指针用 `global`；不用 Python 的 list 方法或 dict 代替题目规定的链表（D10）。

## 伪代码 ↔ Python 对照

### 1. 链表的数组表示

每个结点有数据和指向下一个结点的指针。指南里的「指针类型」（`TYPE TIntPointer = ^INTEGER`，p.12）在考试的链表题里几乎不用：结点放在数组里，**指针就是数组下标**，`-1` 表示空指针。

两种存法都常见（ECR P4 2021 p.16 的点评同时提到这两种结构：结点的记录类型，以及「一个存数据、一个存指针」的两个数组）：

```pseudocode
TYPE ListNode
   DECLARE Data : STRING
   DECLARE Pointer : INTEGER
ENDTYPE
DECLARE List : ARRAY[0:5] OF ListNode
DECLARE StartPointer : INTEGER
DECLARE FreePointer : INTEGER
```

```pseudocode
DECLARE ListData : ARRAY[0:5] OF STRING
DECLARE ListPointer : ARRAY[0:5] OF INTEGER
DECLARE StartPointer : INTEGER
DECLARE FreePointer : INTEGER
```

本级的伪代码与 Python 都用第二种（并行数组），数组下标从 0 起（指南 p.10 建议写明下界），与 P4 的 Python 一致。

一个例子（`StartPointer = 1`，`FreePointer = 3`）：

| 下标 | `ListData` | `ListPointer` |
|:--|:--|:--|
| 0 | `"Cat"` | 2 |
| 1 | `"Ant"` | 4 |
| 2 | `"Dog"` | -1 |
| 3 | `""` | 5 |
| 4 | `"Bee"` | 0 |
| 5 | `""` | -1 |

从 `StartPointer` 出发沿指针走：1 Ant → 4 Bee → 0 Cat → 2 Dog → 空。数组里的顺序（Cat、Ant、Dog…）**不是**链表的顺序。空闲结点也串成一条链：3 → 5 → 空。

### 2. 初始化：所有结点都在空闲表里

```pseudocode
PROCEDURE InitialiseList()
   DECLARE Index : INTEGER
   StartPointer ← -1                // the list is empty
   FreePointer ← 0                  // the first free node
   FOR Index ← 0 TO 4
      ListData[Index] ← ""
      ListPointer[Index] ← Index + 1
   NEXT Index
   ListData[5] ← ""
   ListPointer[5] ← -1              // the last free node
ENDPROCEDURE
```

```python
ListData = [""] * 6       # STRING, 6 elements
ListPointer = [-1] * 6    # INTEGER, 6 elements
StartPointer = -1         # INTEGER, -1 = null pointer
FreePointer = 0           # INTEGER


def InitialiseList() -> None:
    global StartPointer, FreePointer
    StartPointer = -1
    FreePointer = 0
    for Index in range(5):
        ListData[Index] = ""
        ListPointer[Index] = Index + 1
    ListData[5] = ""
    ListPointer[5] = -1
```

### 3. 遍历与查找：沿指针走，直到空指针

```pseudocode
PROCEDURE OutputList()
   DECLARE Current : INTEGER
   Current ← StartPointer
   WHILE Current <> -1
      OUTPUT ListData[Current]
      Current ← ListPointer[Current]
   ENDWHILE
ENDPROCEDURE

FUNCTION FindItem(Item : STRING) RETURNS INTEGER
   DECLARE Current : INTEGER
   Current ← StartPointer
   WHILE Current <> -1
      IF ListData[Current] = Item THEN
         RETURN Current
      ENDIF
      Current ← ListPointer[Current]
   ENDWHILE
   RETURN -1
ENDFUNCTION
```

```python
def OutputList() -> None:
    Current = StartPointer
    while Current != -1:
        print(ListData[Current])
        Current = ListPointer[Current]


def FindItem(Item: str) -> int:
    Current = StartPointer
    while Current != -1:
        if ListData[Current] == Item:
            return Current
        Current = ListPointer[Current]
    return -1
```

循环条件是「当前结点不是空」（`Current <> -1`），不是「当前结点的指针不是空」——后者会漏掉最后一个结点。

### 4. 插入：先从空闲表取一个结点

表头插入（新结点成为第一个）：

```pseudocode
FUNCTION InsertAtStart(Item : STRING) RETURNS BOOLEAN
   DECLARE NewNode : INTEGER
   IF FreePointer = -1 THEN
      RETURN FALSE                       // no free nodes: the list is full
   ENDIF
   NewNode ← FreePointer
   FreePointer ← ListPointer[NewNode]   // remove the node from the free list
   ListData[NewNode] ← Item
   ListPointer[NewNode] ← StartPointer  // the new node points to the old first node
   StartPointer ← NewNode
   RETURN TRUE
ENDFUNCTION
```

```python
def InsertAtStart(Item: str) -> bool:
    global StartPointer, FreePointer
    if FreePointer == -1:
        return False
    NewNode = FreePointer
    FreePointer = ListPointer[NewNode]
    ListData[NewNode] = Item
    ListPointer[NewNode] = StartPointer
    StartPointer = NewNode
    return True
```

**按序插入**的思路（L10/E03 要写出完整算法）：

1. 同上，从空闲表取出 `NewNode`，存入数据。
2. 从 `StartPointer` 出发，用 `Previous` 记住上一个结点，沿指针走，直到走到空或遇到比新数据大的结点。
3. 如果 `Previous = -1`（新数据最小，或表是空的）：`ListPointer[NewNode] ← StartPointer`，`StartPointer ← NewNode`。
4. 否则：`ListPointer[NewNode] ← ListPointer[Previous]`，`ListPointer[Previous] ← NewNode`。

**顺序很重要**：先让新结点指向后继，再让前驱指向新结点；反过来写，后面的结点就丢了。

### 5. 删除：把结点接回空闲表

1. 沿指针找要删的结点 `Current`，同时记住 `Previous`；找不到就返回 FALSE。
2. 删的是第一个结点（`Previous = -1`）：`StartPointer ← ListPointer[Current]`；否则 `ListPointer[Previous] ← ListPointer[Current]`。
3. 把 `Current` 放到空闲表最前面：`ListPointer[Current] ← FreePointer`，`FreePointer ← Current`。

结点的数据不必清空：它已经不在链表里，下次插入时会被覆盖。

### 6. 二叉查找树：左指针、数据、右指针

```pseudocode
DECLARE LeftPointer : ARRAY[0:9] OF INTEGER
DECLARE TreeData : ARRAY[0:9] OF INTEGER
DECLARE RightPointer : ARRAY[0:9] OF INTEGER
DECLARE RootPointer : INTEGER     // -1 = empty tree
DECLARE FreeNode : INTEGER        // index of the next unused element
```

插入 `Item`：把它存进 `FreeNode` 位置（左右指针置 -1）；树空时 `RootPointer` 指向它；否则从根出发，`Item` 比当前结点小就往左、否则往右，直到要走的那一侧是空指针，把**那一侧的指针**改成新结点的下标。查找类似：相等就找到了，小往左、大往右，走到 -1 就是不存在。

**相等的值往哪边放，要事先定好**（本级规定：放右边）。ECR P4 2024 p.21–22 的考官范答只处理了「小于」和「大于」两种情况；如果插入一个已经存在的值，循环里两个分支都不执行，指针不再前进，循环永远不会结束。那道题的数据没有重复值，所以没出问题——自己写的时候不要留这个口子。

二叉树的**遍历**（中序输出就是从小到大）用递归写最自然，放在 L11/E05。

### 7. 用其他结构实现 ADT（考纲 19.1）

| ADT | 本阶梯的实现 | Python 现成的结构 |
|:--|:--|:--|
| 栈、队列 | L08：数组 + 指针 | `list` 的 `append`/`pop`；`collections.deque` |
| 链表 | 本级：数组 + 指针 + 空闲表 | 没有直接对应 |
| 二叉树 | 本级：三个并行数组 + 根指针 | 没有直接对应 |
| 字典（dictionary） | 键值对 | `dict` |
| 图（graph） | 只需描述特点与用途，**不要求写代码**（考纲 p.37） | — |

P4 题目规定「用数组实现」时，就必须用数组 + 指针：ECR P4 2021 p.13、p.15–16 的点评里，有考生用 Python 的 list 或 dict 代替题目要求的链表、把新数据直接追加到末尾，没有使用题目规定的指针，这些部分都不得分。

## 常见坑

1. **按数组顺序输出，而不是沿指针输出**（ECR P4 2021 p.13、p.16）。
2. **插入时直接追加到数组末尾**，不用空闲表指针；或者**没有更新前驱结点的指针**，新结点「挂」不上链表（ECR P4 2021 p.16）。
3. **没有按题目声明并初始化 start / free 指针**（ECR P4 2021 p.9：题目要求把 `startPointer` 设为 0、`emptyList` 设为 5，考生漏了）。指针初值照题目给的写（D10）。
4. **空指针用错**：题目约定 `-1`，就不要用 0 或 `None`（ER s25 9618/43 Q3 p.49：很多考生没有给 `HeadNode`、`NextNode` 赋合适的空值）。
5. **Python 里 `-1` 当下标不报错**：`ListData[-1]` 是最后一个元素。所以每次用指针取元素之前都要先判断 `!= -1`，否则程序不崩溃、结果却是错的。
6. **插入方式没读清**：题目要求插在表头，却遍历到表尾再插（ER s25 9618/43 Q3 p.49）。
7. **树的结点数组用整数初始化**，而不是题目要求的结点对象；或只初始化了 1 个、19 个元素（ECR P4 2024 p.20；ER s24 9618/42 Q2 p.44）。
8. **比较了结点对象而不是结点里的数据**；或用「数组是不是空的」判断树是否为空（ECR P4 2024 p.23）。应该比较 `TreeData[Current]`，用 `RootPointer = -1` 判断空树。
9. **相等的值没有规定去向**：见 §6。
10. **忘了 `global`**：`StartPointer`、`FreePointer`、`RootPointer`、`FreeNode` 在函数里被重新赋值。
11. **改指针的顺序写反**：先改了前驱的指针，后继就找不到了。

## 延伸阅读

- 教材 Langfield & Duddell 2e：13.10 Linked lists（p.229）；23.05 ADTs（p.415）、23.06 Linked lists（p.415）、23.07 Binary trees（p.418）、23.10 Graphs（p.424）、23.12 Dictionaries（p.428）。书中伪代码与 2027–29 指南不同时以指南为准。
- 官方：考纲 19.1（p.37）；SoW Unit 10（p.33：用 index / data / pointer 三列的表格演示链表的插入与删除）。
- 公开课：CS50P 与 Think Python 3e 都没有「数组 + 指针」的链表与二叉树，本级不列公开课讲次。

## 练习

| 练习 | 形态 | 先写伪代码 | 练什么 |
|:--|:--|:--|:--|
| [`exercises/E01-trace-linked-list/`](exercises/E01-trace-linked-list/spec.md) | 干跑 | 否 | 沿指针遍历；从空闲表取结点做表头插入 |
| [`exercises/E02-list-insert-start/`](exercises/E02-list-insert-start/spec.md) | 函数（全局数组） | 否 | 初始化空闲表、表头插入、遍历输出、满表 |
| [`exercises/E03-ordered-insert/`](exercises/E03-ordered-insert/spec.md) | 函数（全局数组） | 是 | 按序插入：找前驱、改两个指针 |
| [`exercises/E04-delete-node/`](exercises/E04-delete-node/spec.md) | 函数（全局数组） | 是 | 删除：表头、中间、表尾；结点还给空闲表 |
| [`exercises/E05-binary-tree/`](exercises/E05-binary-tree/spec.md) | 函数（全局数组） | 是 | 二叉查找树的插入（含相等值）与查找 |
