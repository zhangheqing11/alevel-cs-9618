# L10/E03 · 有序链表：按序插入

| 属性 | 值 |
|:--|:--|
| id | `L10/E03` |
| 目录 | `ladder/levels/L10-linked-lists-trees/exercises/E03-ordered-insert/` |
| 形态 | `function`（全局数组；测试检查全局变量、返回值与输出） |
| entry | `InsertInOrder`（同一文件还有 `InitialiseList`、`OutputList` 与全局变量） |
| pseudocode | `true` |
| files | `[]` |
| skills | `linked-list`, `global-scope`, `pre-condition-loop`, `boundary-values`, `p4-identifiers` |
| difficulty | 4 |
| title | `Ordered linked list: insert in order` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L10 card §2、§3、§4（按序插入的四步） |

## 练习目标

写出链表最常考的算法：从空闲表取结点后，找到新数据的前驱，分「插在表头」与「插在中间/表尾」两种情况改两个指针。

## 题面

### 中文导读

沿用 E02 的全局数组和 `InitialiseList()`、`OutputList()`（可以照抄你 E02 的代码）。新写函数 `InsertInOrder(Item)`：把 `Item` 插到链表里，使链表始终按字母从小到大排列；和已有数据相等时，插在已有那一项的**后面**；没有空闲结点时返回 `False`。

### English task

Use the same global arrays as in E02 (`ListData`, `ListPointer`, `StartPointer`, `FreePointer`; 6 nodes; null pointer `-1`), and include `InitialiseList()` and `OutputList()` exactly as specified in E02.

Write a function `InsertInOrder()` that takes a string `Item`. It returns `False` if there are no free nodes. Otherwise it stores `Item` in the first free node and links that node into the list so that the list stays in ascending order. An item equal to one already in the list is placed after it. The function then returns `True`.

## 接口

```python
ListData = [""] * 6       # STRING, 6 elements
ListPointer = [-1] * 6    # INTEGER, 6 elements
StartPointer = -1         # INTEGER; -1 is the null pointer
FreePointer = -1          # INTEGER


def InitialiseList() -> None:
    """As in E02: empty the list and link all 6 nodes into the free list."""
    raise NotImplementedError


def OutputList() -> None:
    """As in E02: output each data item in list order, or 'Empty list'."""
    raise NotImplementedError


def InsertInOrder(Item: str) -> bool:
    """Store Item in the first free node and link it in ascending order; False if full."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: ListData : ARRAY[0:5] OF STRING
// global: ListPointer : ARRAY[0:5] OF INTEGER
// global: StartPointer : INTEGER; FreePointer : INTEGER
FUNCTION InsertInOrder(Item : STRING) RETURNS BOOLEAN
   DECLARE NewNode : INTEGER
   DECLARE Current : INTEGER
   DECLARE Previous : INTEGER

ENDFUNCTION
```

## 必测行为

每个测试先调用 `sol.InitialiseList()`。

| # | 操作（同一测试内按顺序） | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `InsertInOrder("M")` | `True`；`StartPointer == 0`；`ListPointer[0] == -1`；`FreePointer == 1` | 插入空表 |
| B2 | 依次插入 `"M"`、`"C"`、`"X"`、`"A"` | 都返回 `True`；`ListData[:4] == ["M", "C", "X", "A"]`；`ListPointer[:4] == [2, 0, -1, 1]`；`StartPointer == 3`；`FreePointer == 4` | 表头、中间、表尾都出现 |
| B3 | 接 B2，`OutputList()` | 输出行 `["A", "C", "M", "X"]` | |
| B4 | 接 B2，再插入 `"C"` | `True`；`ListPointer[1] == 4`、`ListPointer[4] == 0`；`OutputList()` 输出 `["A", "C", "C", "M", "X"]` | 相等的值插在已有那项之后 |
| B5 | 依次插入 `"F"`、`"E"`、`"D"`、`"C"`、`"B"`、`"A"`，再插入 `"Z"` | 前 6 次 `True`，第 7 次 `False`；`OutputList()` 输出 `A` 到 `F` 六行 | 一直插在表头；满表 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 忽略顺序，一律接到表尾（ECR P4 2021 p.16 的同类错误）：B3 输出 `M C X A` | B2、B3、B4、B5 |
| M2 | 插在中间时只写了 `ListPointer[Previous] ← NewNode`，没有让新结点指向原来的后继（写成 `-1`）：B4 插入第二个 `C` 后，`M`、`X` 丢失 | B4 |
| M3 | 没有处理「插在表头」的情况（`Previous = -1` 时也去改 `ListPointer[Previous]`，Python 里改的是 `ListPointer[-1]`）：`"C"`、`"A"` 挂不进链表，空闲表也被破坏 | B2、B3、B4、B5 |
| M4 | 相等时插在前面（比较用 `<` 而不是 `<=`）：B4 中 `ListPointer[4]` 指向 1 | B4 |

## 人工核对清单

- [ ] 伪代码：先判断 `FreePointer = -1`；取结点并存数据；`Previous ← -1`、`Current ← StartPointer`；`WHILE Current <> -1 AND ListData[Current] <= Item` 时向前走。
- [ ] 伪代码：`IF Previous = -1 THEN` 改 `StartPointer`，`ELSE` 改 `ListPointer[Previous]`；两种情况下新结点都先指向后继（`ListPointer[NewNode] ← StartPointer` 或 `← ListPointer[Previous]`）。
- [ ] 伪代码：没有 `BREAK`；`RETURN TRUE` / `RETURN FALSE`。
- [ ] Python：能说出 M3 为什么在 Python 里不报错（`ListPointer[-1]` 是最后一个元素），以及如何避免。

## 出处

自编。误区依据：ECR P4 2021（9618_s21_42 Q1(d)）p.16：考生把新数据追加到链表数组末尾，或没有更新上一个结点的指针。语法依据：指南 p.10、p.21、p.23。
