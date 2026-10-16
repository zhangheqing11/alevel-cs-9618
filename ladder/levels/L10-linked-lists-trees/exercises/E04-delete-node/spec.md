# L10/E04 · 链表删除：结点还给空闲表

| 属性 | 值 |
|:--|:--|
| id | `L10/E04` |
| 目录 | `ladder/levels/L10-linked-lists-trees/exercises/E04-delete-node/` |
| 形态 | `function`（全局数组；测试直接给全局变量赋值建立初始状态，再检查结果） |
| entry | `DeleteItem` |
| pseudocode | `true` |
| files | `[]` |
| skills | `linked-list`, `global-scope`, `pre-condition-loop`, `boundary-values`, `p4-identifiers` |
| difficulty | 4 |
| title | `Linked list: delete a node and return it to the free list` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L10 card §5 |

## 练习目标

写出链表删除：找到结点和它的前驱；分「删表头」与「删中间/表尾」改指针；把删掉的结点接到空闲表最前面；找不到时什么也不改。

## 题面

### 中文导读

全局数组与指针同 E02（6 个结点，空指针 `-1`）。写函数 `DeleteItem(Item)`：删除链表中**第一个**数据等于 `Item` 的结点，把它放到空闲表的最前面，返回 `True`；找不到返回 `False`，所有数组与指针都不变。测试会直接给全局变量赋值来建立删除前的状态，所以本题不需要写插入。

### English task

The global arrays `ListData` and `ListPointer`, and the global integers `StartPointer` and `FreePointer`, are as in E02 (6 nodes, null pointer `-1`).

Write a function `DeleteItem()` that takes a string `Item`. It finds the first node in the list whose data is `Item`, removes that node from the list, adds it to the start of the free list, and returns `True`. If no node holds `Item`, it returns `False` and changes nothing.

The tests set up the arrays and pointers directly, so you do not need to write any insert routine.

## 接口

```python
ListData = [""] * 6       # STRING, 6 elements
ListPointer = [-1] * 6    # INTEGER, 6 elements
StartPointer = -1         # INTEGER; -1 is the null pointer
FreePointer = -1          # INTEGER


def DeleteItem(Item: str) -> bool:
    """Remove the first node holding Item and add it to the start of the free list."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: ListData : ARRAY[0:5] OF STRING
// global: ListPointer : ARRAY[0:5] OF INTEGER
// global: StartPointer : INTEGER; FreePointer : INTEGER
FUNCTION DeleteItem(Item : STRING) RETURNS BOOLEAN
   DECLARE Current : INTEGER
   DECLARE Previous : INTEGER

ENDFUNCTION
```

## 必测行为

除 B5 外，每个测试先把全局变量设为下面的状态（链表 `A → C → M → X`，空闲表 `4 → 5`）：

```python
sol.ListData = ["M", "C", "X", "A", "", ""]
sol.ListPointer = [2, 0, -1, 1, 5, -1]
sol.StartPointer = 3
sol.FreePointer = 4
```

表中「链表」一列指沿指针读出的数据（测试里自己沿指针走一遍得到）。T10 已用参考实现核对全部期望值。

| # | 调用 | 返回 | 之后的 `ListPointer` | `StartPointer` | `FreePointer` | 链表 | 说明 |
|:--|:--|:--|:--|:--|:--|:--|:--|
| B1 | `DeleteItem("A")` | `True` | `[2, 0, -1, 4, 5, -1]` | `1` | `3` | C M X | 删表头 |
| B2 | `DeleteItem("M")` | `True` | `[4, 2, -1, 1, 5, -1]` | `3` | `0` | A C X | 删中间 |
| B3 | `DeleteItem("X")` | `True` | `[-1, 0, 4, 1, 5, -1]` | `3` | `2` | A C M | 删表尾 |
| B4 | `DeleteItem("Q")` | `False` | 不变 | `3` | `4` | A C M X | 找不到：什么也不改 |
| B5 | 先设 `ListData = ["A", "", "", "", "", ""]`、`ListPointer = [-1, 2, 3, 4, 5, -1]`、`StartPointer = 0`、`FreePointer = 1`，再 `DeleteItem("A")` | `True` | `[1, 2, 3, 4, 5, -1]` | `-1` | `0` | （空） | 删掉唯一的结点（边界） |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 没有处理删表头（`Previous = -1` 时也去改 `ListPointer[Previous]`）：`StartPointer` 不变 | B1、B5 |
| M2 | 删掉的结点没有还给空闲表：`FreePointer` 不变 | B1、B2、B3、B5 |
| M3 | 找不到时也改了东西：走到 -1 后仍执行「接回空闲表」，把 `FreePointer` 设成 -1 | B4 |

## 人工核对清单

- [ ] 伪代码：`Previous ← -1`、`Current ← StartPointer`；用标志变量（如 `Found`）控制 `WHILE`：循环里先判断 `Current = -1`（没找到，`RETURN FALSE`），否则再比较 `ListData[Current] = Item`（相等则 `Found ← TRUE`，否则 `Previous ← Current`、`Current ← ListPointer[Current]`）。**不要**写 `WHILE Current <> -1 AND ListData[Current] <> Item`——指南没有保证 `AND` 短路（D25，与 L11 card §4 同一口径）。
- [ ] 伪代码：`IF Previous = -1 THEN StartPointer ← ListPointer[Current] ELSE ListPointer[Previous] ← ListPointer[Current]`；然后 `ListPointer[Current] ← FreePointer`、`FreePointer ← Current`。
- [ ] Python：`global StartPointer, FreePointer`；没有用 `remove`、`pop` 或重建 list 代替指针操作。
- [ ] 能说出为什么删掉的结点不必清空 `ListData`。

## 出处

自编。依据：考纲 19.1「delete an item from … linked list」（p.37）；L10 card §5。
