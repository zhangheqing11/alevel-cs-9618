## LT　链表、二叉树与哈希表：伪代码 ↔ Python 对照与模板 {#core-LT}

题干常用伪代码描述结构（`DECLARE ArrayNodes : ARRAY[0:19, 0:2] OF INTEGER`，9618_w22_41）或给出要补全的递归伪代码（9618_w22_41:3(c)）；P4 交 Python。伪代码按 2027–29 指南书写；Python 照题目的标识符与下标，数组建成真实 list（D10 ①），指针初值照题目（D10 ②）。

### 1. 结构的声明

| 内容 | 伪代码 | Python | 注意 |
|:--|:--|:--|:--|
| 二维数组（链表） | `DECLARE LinkedList : ARRAY[0:19, 0:1] OF INTEGER` | `LinkedList = []`，循环 20 次 `append([-1, x + 1])` | 20 行、每行 2 格；不是 2 行、每行 20 格 |
| 二维数组（树） | `DECLARE TreeArray : ARRAY[0:49, 0:2] OF INTEGER` | 循环 50 次 `append([-1, -1, -1])` | 不能 `[[-1, -1, -1]] * 50`（50 行是同一个 list） |
| 访问元素 | `TreeArray[Row, 1]` | `TreeArray[Row][1]` | 伪代码一对方括号、逗号隔开；Python 两对方括号 |
| 记录数组（链表另一种写法） | `TYPE Node` / `DECLARE Data : STRING` / `DECLARE Pointer : INTEGER` / `ENDTYPE`；`DECLARE List : ARRAY[1:200] OF Node` | 类 + `List = []` 循环 `append(Node())` | `List[i].Pointer` 两边写法相同 |
| 空指针 | 题目给定：常为 `-1`（AS 伪代码题也有用 `0` 的） | 数组实现照题目用 `-1`；对象实现用 `None` | 判空写 `!= -1` 或 `!= None` |
| 起始 / 空闲指针 | `DECLARE FirstNode : INTEGER`，`FirstNode ← -1` | `FirstNode = -1  # INTEGER` | 全局；在函数里改要 `global` |

### 2. 链表：遍历、表头插入、删除

**遍历**

```pseudocode
CurrentPointer ← FirstNode
WHILE CurrentPointer <> -1
   OUTPUT LinkedList[CurrentPointer, 0]
   CurrentPointer ← LinkedList[CurrentPointer, 1]
ENDWHILE
```

```python
CurrentPointer = FirstNode
while CurrentPointer != -1:
    print(LinkedList[CurrentPointer][0])
    CurrentPointer = LinkedList[CurrentPointer][1]
```

**表头插入**（空闲表取结点）

| 步骤 | 伪代码 | Python |
|:--|:--|:--|
| 判满 | `IF FirstEmpty = -1 THEN` … `ENDIF` | `if FirstEmpty == -1:` |
| 记下空闲表的下一个 | `NextEmpty ← LinkedList[FirstEmpty, 1]` | `NextEmpty = LinkedList[FirstEmpty][1]` |
| 存数据 | `LinkedList[FirstEmpty, 0] ← NewItem` | `LinkedList[FirstEmpty][0] = NewItem` |
| 新结点指向原表头 | `LinkedList[FirstEmpty, 1] ← FirstNode` | `LinkedList[FirstEmpty][1] = FirstNode` |
| 新结点成为表头 | `FirstNode ← FirstEmpty` | `FirstNode = FirstEmpty` |
| 空闲表后移 | `FirstEmpty ← NextEmpty` | `FirstEmpty = NextEmpty` |

**删除**：两个指针一前一后走；找到后 `LinkedList[Previous][1] = LinkedList[Current][1]`；被删结点 `LinkedList[Current][1] = FirstEmpty`、`FirstEmpty = Current`。目标是第一个结点时只改 `FirstNode`。找的循环不依赖 `AND` 短路（D25）：用 `Found` 标志，或先判断 `Current != -1` 再在循环体里读数组。

### 3. 对象实现（结点互相引用）

| 意图 | 伪代码（P3 的 CLASS 写法，仅供对照） | Python |
|:--|:--|:--|
| 结点类 | `CLASS Node` / `PRIVATE TheData : INTEGER` / `PRIVATE NextNode : Node` / … / `ENDCLASS` | `class Node:` + `__init__` 里 `self.__TheData = TheDatap  # INTEGER`、`self.__NextNode = None  # Node` |
| 空引用 | 题目的 null | `None` |
| 走到下一个 | `Current ← Current.GetNextNode()` | `Current = Current.GetNextNode()` |
| 取数据 | `Current.GetData()` | `Current.GetData()`（属性私有，不能 `Current.__TheData`） |
| 新建结点 | `NewNode ← NEW Node(Data)` | `NewNode = Node(Data)` |
| 改链接 | `CALL NewNode.SetNextNode(HeadNode)` | `NewNode.SetNextNode(self.__HeadNode)` |

在类的方法里访问自己的属性一律写 `self.__属性名`；方法的第一个参数是 `self`。

### 4. 二叉树

**插入**（数组实现，`Placed` 标志控制循环）

```pseudocode
TreeArray[FreeNode, 1] ← NodeData
IF RootPointer = -1 THEN
   RootPointer ← FreeNode
ELSE
   CurrentNode ← RootPointer
   Placed ← FALSE
   WHILE Placed = FALSE
      IF NodeData < TreeArray[CurrentNode, 1] THEN
         IF TreeArray[CurrentNode, 0] = -1 THEN
            TreeArray[CurrentNode, 0] ← FreeNode
            Placed ← TRUE
         ELSE
            CurrentNode ← TreeArray[CurrentNode, 0]
         ENDIF
      ELSE
         IF TreeArray[CurrentNode, 2] = -1 THEN
            TreeArray[CurrentNode, 2] ← FreeNode
            Placed ← TRUE
         ELSE
            CurrentNode ← TreeArray[CurrentNode, 2]
         ENDIF
      ENDIF
   ENDWHILE
ENDIF
FreeNode ← FreeNode + 1
```

Python 逐行对应：`←` 换成 `=`，`[CurrentNode, 0]` 换成 `[CurrentNode][0]`，`WHILE … ENDWHILE` 换成 `while …:` 加缩进，`TRUE` / `FALSE` 换成 `True` / `False`（完整代码见 LT-03 代表题）。

**递归遍历**

| 遍历 | 伪代码 | Python |
|:--|:--|:--|
| 中序 | `IF TreeArray[Root, 0] <> -1 THEN` / `CALL InOrder(TreeArray[Root, 0])` / `ENDIF` / `OUTPUT TreeArray[Root, 1]` / 右同理 | `if TreeArray[Root][0] != -1: InOrder(TreeArray[Root][0])`；`print(TreeArray[Root][1])`；右同理 |
| 后序 | 左、右两次递归之后才 `OUTPUT` | 两次递归之后才 `print` |
| 递归查找 | `RETURN SearchValue(ArrayNodes[Root, 0], ValueToFind)` | `return SearchValue(ArrayNodes[Root][0], ValueToFind)`（`return` 不能省） |

伪代码调用过程用 `CALL InOrder(…)`；Python 直接写 `InOrder(…)`。函数（有返回值）在两边都写在表达式或 `RETURN` 里。

### 5. 哈希表

| 意图 | 伪代码 | Python |
|:--|:--|:--|
| 散列值 | `RETURN Key MOD 200` | `return Key % 200` |
| 整除（对照） | `Key DIV 200` | `Key // 200` |
| 空记录 | 各字段 `-1` | `NewRecord(-1, -1, -1)`，每格单独新建 |
| 判空 | `IF HashTable[HashValue].Key = -1 THEN` | `if HashTable[HashValue].Key == -1:` |
| 找下一个空位并只存一次 | `WHILE Stored = FALSE AND Index <= 99` … `ENDWHILE` | `while Stored == False and Index < 100:` …（或 `for` + `break`） |
| 二维表的一行 | `HashTable[Row, Column]` | `HashTable[Row][Column]` |

### 6. 常见运行错误

| 现象 | 原因 | 改法 |
|:--|:--|:--|
| `IndexError` 在初始化时 | 循环少建了一个结点（如 `range(0, 19)` 后再访问下标 19；9618_w24_41:3(a) 的 MS Python 范例就是这样） | 循环结点数次，再改最后一个指针 |
| 遍历多输出一个 –1 或漏掉最后一个 | 先访问再判断，或判断 `LinkedList[Current][1] != -1` | `while Current != -1:` 先判断再访问 |
| 插入后空闲表丢了 | 先改了 `LinkedList[FirstEmpty][1]` 再取空闲表的下一个 | 先存 `NextEmpty` |
| `AttributeError: 'Node' object has no attribute '__TheData'` | 在类外直接读私有属性 | 用 getter |
| 递归查找返回 `None` | 递归调用前没写 `return` | `return SearchValue(…)` |
| `RecursionError` | 递归前没判断左 / 右是否为空，空指针 –1 又被当成下标 | 先 `if … != -1` 再递归 |
