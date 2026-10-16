# L10/E02 · 链表：初始化空闲表、表头插入、遍历输出

| 属性 | 值 |
|:--|:--|
| id | `L10/E02` |
| 目录 | `ladder/levels/L10-linked-lists-trees/exercises/E02-list-insert-start/` |
| 形态 | `function`（全局数组 + 三个过程/函数；测试检查全局变量、返回值与输出） |
| entry | `InsertAtStart`（同一文件还有 `InitialiseList`、`OutputList` 与全局变量） |
| pseudocode | `false` |
| files | `[]` |
| skills | `linked-list`, `global-scope`, `boundary-values`, `boolean-return`, `p4-identifiers` |
| difficulty | 3 |
| title | `Linked list: initialise the free list, insert at the start, output` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L10 card §2、§3、§4 |

## 练习目标

按 P4 的要求实现链表的三个基本操作：把 6 个结点全部串进空闲表；从空闲表取结点做表头插入（满了返回 False）；沿指针输出全部数据（空表时输出 `Empty list`）。

## 题面

### 中文导读

链表最多 6 个结点，存在全局数组 `ListData`（字符串）与 `ListPointer`（整数）里；`StartPointer` 指向第一个结点，`FreePointer` 指向第一个空闲结点，`-1` 是空指针。写三个模块：`InitialiseList()`、`InsertAtStart(Item)`、`OutputList()`，规则见英文题干。

### English task

A linked list of up to 6 nodes is stored in the global arrays `ListData` (`STRING`) and `ListPointer` (`INTEGER`), with indexes 0 to 5. The global integer `StartPointer` points to the first node in the list and `FreePointer` points to the first free node. The null pointer is `-1`.

Write:

- a procedure `InitialiseList()` that sets every element of `ListData` to `""`, links all 6 nodes into the free list in index order (node 0 points to node 1, …, node 5 points to `-1`), sets `StartPointer` to `-1` and `FreePointer` to 0
- a function `InsertAtStart()` that takes a string `Item`; it returns `False` if there are no free nodes, otherwise it takes the first free node, stores `Item` in it, makes it the first node of the list and returns `True`
- a procedure `OutputList()` that outputs the data of each node in list order, one item per line, or outputs `Empty list` if the list is empty.

## 接口

```python
ListData = [""] * 6       # STRING, 6 elements
ListPointer = [-1] * 6    # INTEGER, 6 elements
StartPointer = -1         # INTEGER; -1 is the null pointer
FreePointer = -1          # INTEGER


def InitialiseList() -> None:
    """Empty the list and link all 6 nodes into the free list."""
    raise NotImplementedError


def InsertAtStart(Item: str) -> bool:
    """Use the first free node to store Item as the new first node; False if full."""
    raise NotImplementedError


def OutputList() -> None:
    """Output each data item in list order, or 'Empty list'."""
    raise NotImplementedError
```

（`starter.py` 里四个全局变量的初值照上面给出；`InitialiseList()` 运行后才是可用的空链表。）

## 必测行为

每个测试先调用 `sol.InitialiseList()`（B6 除外）。

| # | 操作（同一测试内按顺序） | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `InitialiseList()` | `ListPointer == [1, 2, 3, 4, 5, -1]`；`ListData == [""] * 6`；`StartPointer == -1`；`FreePointer == 0` | 空闲表 |
| B2 | `OutputList()` | 输出行 `["Empty list"]` | 空表 |
| B3 | `InsertAtStart("A")`、`("B")`、`("C")` | 都返回 `True`；`ListData[:3] == ["A", "B", "C"]`；`ListPointer[:3] == [-1, 0, 1]`；`StartPointer == 2`；`FreePointer == 3` | 指针更新 |
| B4 | 接 B3，`OutputList()` | 输出行 `["C", "B", "A"]` | 沿指针、最新的在前 |
| B5 | 连续插入 7 次 | 前 6 次 `True`，第 7 次 `False`；`FreePointer == -1` | 满表（边界） |
| B6 | 先插入 2 个，再调用 `InitialiseList()` | 回到 B1 的状态 | 可以重新初始化 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 初始化时最后一个结点指向 6（`for i in range(6): ListPointer[i] = i + 1`）：B1 不对；第 7 次插入访问越界或返回 `True` | B1、B5 |
| M2 | `InsertAtStart` 没有更新 `FreePointer`：每次都写进同一个结点 | B3、B4、B5 |
| M3 | 新结点的指针没有指向原来的第一个结点（写成 `-1`）：`OutputList` 只输出最新的一项 | B3、B4 |
| M4 | 漏了 `global StartPointer, FreePointer`：第一次赋值就抛 `UnboundLocalError` | B1–B6 |

## 人工核对清单

- [ ] 全局数组按 D10 真实建出并注释类型与大小；指针初值、空指针 `-1` 照题目。
- [ ] `InsertAtStart` 的四步顺序：取 `NewNode ← FreePointer` → `FreePointer ← ListPointer[NewNode]` → 存数据 → `ListPointer[NewNode] ← StartPointer` → `StartPointer ← NewNode`。
- [ ] `OutputList` 的循环条件是 `Current != -1`；没有用 `for i in range(6)` 按数组顺序输出（ECR P4 2021 p.13、p.16）。
- [ ] 没有用 Python 的 `insert`/`append` 代替空闲表（D10；ECR P4 2021 p.15–16）。

## 出处

自编。误区依据：ECR P4 2021（9618_s21_42 Q1）p.9、p.13、p.15–16。
