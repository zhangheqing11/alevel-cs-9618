# L11/E05 · 递归遍历二叉树：中序输出、数结点、求高度

| 属性 | 值 |
|:--|:--|
| id | `L11/E05` |
| 目录 | `ladder/levels/L11-recursion-algorithms/exercises/E05-tree-traversal/` |
| 形态 | `function`（全局数组；测试直接给全局变量赋值建树，再检查输出、返回值与确实递归） |
| entry | `InOrder`（同一文件还有 `CountNodes`、`TreeHeight` 与全局变量） |
| pseudocode | `true` |
| files | `[]` |
| skills | `recursion`, `binary-tree`, `global-scope`, `boundary-values`, `p4-identifiers` |
| difficulty | 4 |
| title | `Recursive tree traversal: in-order output, count nodes, height` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L11 card §6；L10 card §6 |

## 练习目标

用递归处理 L10 的数组二叉树：基本情况是空指针 `-1`；一般情况分别处理左子树、当前结点、右子树。中序输出就是从小到大。

## 题面

### 中文导读

全局数组 `LeftPointer`、`TreeData`、`RightPointer` 与 `RootPointer` 同 L10/E05（10 个元素，空指针 `-1`）。写三个递归模块，参数都是一个结点下标 `NodePointer`（可以是 `-1`）：`InOrder(NodePointer)` 按中序输出以它为根的子树的数据（每行一个）；`CountNodes(NodePointer)` 返回这棵子树的结点数；`TreeHeight(NodePointer)` 返回这棵子树的高度（空树为 0，只有一个结点为 1）。测试会直接给全局变量赋值来建树。

### English task

The global arrays `LeftPointer`, `TreeData` and `RightPointer` and the global integer `RootPointer` store a binary search tree as in L10/E05 (10 elements, null pointer `-1`). The tests set these globals directly.

Write three recursive modules. Each takes a node index `NodePointer`, which may be `-1`:

- a procedure `InOrder()` that outputs the data in the subtree rooted at `NodePointer` using an in-order traversal, one value per line
- a function `CountNodes()` that returns the number of nodes in that subtree
- a function `TreeHeight()` that returns the height of that subtree: 0 for an empty tree, 1 for a single node, otherwise 1 more than the greater height of its two subtrees.

## 接口

```python
LeftPointer = [-1] * 10   # INTEGER, 10 elements
TreeData = [-1] * 10      # INTEGER, 10 elements
RightPointer = [-1] * 10  # INTEGER, 10 elements
RootPointer = -1          # INTEGER; -1 means the tree is empty


def InOrder(NodePointer: int) -> None:
    """Output the subtree rooted at NodePointer in order, one value per line."""
    raise NotImplementedError


def CountNodes(NodePointer: int) -> int:
    """Return the number of nodes in the subtree rooted at NodePointer."""
    raise NotImplementedError


def TreeHeight(NodePointer: int) -> int:
    """Return the height of the subtree rooted at NodePointer (0 if empty)."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: LeftPointer, TreeData, RightPointer : ARRAY[0:9] OF INTEGER; RootPointer : INTEGER
PROCEDURE InOrder(NodePointer : INTEGER)

ENDPROCEDURE

FUNCTION CountNodes(NodePointer : INTEGER) RETURNS INTEGER

ENDFUNCTION

FUNCTION TreeHeight(NodePointer : INTEGER) RETURNS INTEGER

ENDFUNCTION
```

## 必测行为

树 T1（L10/E05 依次插入 50、30、70、20、40、60 得到的树）：

```python
sol.TreeData = [50, 30, 70, 20, 40, 60, -1, -1, -1, -1]
sol.LeftPointer = [1, 3, 5, -1, -1, -1, -1, -1, -1, -1]
sol.RightPointer = [2, 4, -1, -1, -1, -1, -1, -1, -1, -1]
sol.RootPointer = 0
```

树 T2（依次插入 1、2、3、4、5，退化成一条链）：`TreeData = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1]`，`LeftPointer = [-1] * 10`，`RightPointer = [1, 2, 3, 4, -1, -1, -1, -1, -1, -1]`，`RootPointer = 0`。

递归检查的写法同 E01 的 B5。

| # | 树与调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | T1，`InOrder(0)` | 输出行 `["20", "30", "40", "50", "60", "70"]` | 中序 = 从小到大 |
| B2 | T1，`InOrder(1)`；`InOrder(-1)` | `["20", "30", "40"]`；没有输出 | 子树；空树（边界） |
| B3 | T1，`CountNodes(0)`、`CountNodes(1)`、`CountNodes(-1)` | `6`、`3`、`0` | |
| B4 | T1，`TreeHeight(0)`、`TreeHeight(2)`、`TreeHeight(3)`、`TreeHeight(-1)` | `3`、`2`、`1`、`0` | |
| B5 | T2，`InOrder(0)`；`CountNodes(0)`；`TreeHeight(0)` | `["1", "2", "3", "4", "5"]`；`5`；`5` | 退化的树 |
| B6 | 递归检查：T1 上分别包装 `InOrder`、`CountNodes`、`TreeHeight` 后从根调用 | 每个包装都被调用 ≥ 2 次 | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 写成前序（先输出、再左、再右）：B1 得 `50 30 20 40 70 60` | B1、B2 |
| M2 | `CountNodes` 只数左子树：`1 + CountNodes(LeftPointer[NodePointer])` | B3、B5 |
| M3 | `TreeHeight` 把两侧高度相加而不是取较大值：`TreeHeight(0)` 得 6（退化成链的 T2 碰巧正确） | B4 |

（基本情况漏判 `-1` 的错误在 Python 里会因 `TreeData[-1]` 不报错而一直递归，最后抛 `RecursionError`；可以作为额外的 M4，但 M1–M3 已足够。）

## 人工核对清单

- [ ] 伪代码：三个模块都以 `IF NodePointer <> -1 THEN …`（或 `IF NodePointer = -1 THEN RETURN 0`）开头；`InOrder` 里递归调用用 `CALL InOrder(LeftPointer[NodePointer])`。
- [ ] 伪代码：`CountNodes` 是 `RETURN 1 + CountNodes(LeftPointer[NodePointer]) + CountNodes(RightPointer[NodePointer])`；`TreeHeight` 取两侧较大值（自己用 IF 比较，不用 `max`）。
- [ ] 能写出前序、后序遍历，并说出三者只差在哪一行的位置。
- [ ] Python：没有把树转成 list 再 `sort()` 来输出（D10）。

## 出处

自编。依据：考纲 19.1–19.2（p.37）；L10 card §6。
