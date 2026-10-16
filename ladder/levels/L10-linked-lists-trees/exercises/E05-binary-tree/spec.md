# L10/E05 · 二叉查找树：插入（含相等值）与查找

| 属性 | 值 |
|:--|:--|
| id | `L10/E05` |
| 目录 | `ladder/levels/L10-linked-lists-trees/exercises/E05-binary-tree/` |
| 形态 | `function`（全局数组；测试检查全局变量与返回值） |
| entry | `InsertNode`（同一文件还有 `SearchTree` 与全局变量） |
| pseudocode | `true` |
| files | `[]` |
| skills | `binary-tree`, `global-scope`, `pre-condition-loop`, `boundary-values`, `p4-identifiers` |
| difficulty | 4 |
| title | `Binary search tree: insert (including equal values) and search` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L10 card §6 |

## 练习目标

用三个并行数组和根指针实现二叉查找树：插入时从根往下比较、找到空的那一侧后更新**父结点**的指针；相等的值规定放右边（避免死循环）；查找沿同样的路径走。

## 题面

### 中文导读

树最多 10 个结点，存在全局数组 `LeftPointer`、`TreeData`、`RightPointer` 里（都是整数，初值 `-1`）；`RootPointer` 指向根（空树为 `-1`）；`FreeNode` 是下一个未用的下标（结点按 0、1、2… 依次使用，不删除）。写 `InsertNode(Item)`：树满返回 `False`；否则把 `Item` 存进 `FreeNode` 位置、链到正确的位置（比当前结点小往左，否则——包括相等——往右），返回 `True`。写 `SearchTree(Item)`：返回存有 `Item` 的结点下标（有相等值时返回最先找到的那个），没有返回 `-1`。

### English task

A binary search tree of up to 10 nodes is stored in three global arrays of integers, `LeftPointer`, `TreeData` and `RightPointer` (indexes 0 to 9, every element initialised to `-1`). The global integer `RootPointer` points to the root node (`-1` for an empty tree) and the global integer `FreeNode` is the index of the next unused element, starting at 0. Nodes are used in index order and are never deleted.

Write:

- a function `InsertNode()` that takes an integer `Item`. It returns `False` if the tree is full. Otherwise it stores `Item` in element `FreeNode` with both pointers set to `-1`, links the new node into the tree (go left if `Item` is less than the data in the current node, otherwise go right — so equal values go to the right), adds 1 to `FreeNode` and returns `True`
- a function `SearchTree()` that takes an integer `Item` and returns the index of the node that holds `Item`, or `-1` if it is not in the tree. If there are equal values, return the first one found on the path from the root.

## 接口

```python
LeftPointer = [-1] * 10   # INTEGER, 10 elements
TreeData = [-1] * 10      # INTEGER, 10 elements
RightPointer = [-1] * 10  # INTEGER, 10 elements
RootPointer = -1          # INTEGER; -1 means the tree is empty
FreeNode = 0              # INTEGER; index of the next unused element


def InsertNode(Item: int) -> bool:
    """Store Item in element FreeNode and link it into the tree; False if full."""
    raise NotImplementedError


def SearchTree(Item: int) -> int:
    """Return the index of the node holding Item, or -1."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: LeftPointer, TreeData, RightPointer : ARRAY[0:9] OF INTEGER
// global: RootPointer : INTEGER; FreeNode : INTEGER
FUNCTION InsertNode(Item : INTEGER) RETURNS BOOLEAN

ENDFUNCTION

FUNCTION SearchTree(Item : INTEGER) RETURNS INTEGER

ENDFUNCTION
```

## 必测行为

`sol` fixture 每个测试都重新加载模块（全局变量回到初值）。T10 已用参考实现核对。

| # | 操作（同一测试内按顺序） | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `SearchTree(5)`（空树） | `-1` | 空树 |
| B2 | `InsertNode(50)` | `True`；`RootPointer == 0`；`FreeNode == 1` | 第一个结点成为根 |
| B3 | 依次插入 `50, 30, 70, 20, 40, 60` | 都返回 `True`；`TreeData[:6] == [50, 30, 70, 20, 40, 60]`；`LeftPointer[:6] == [1, 3, 5, -1, -1, -1]`；`RightPointer[:6] == [2, 4, -1, -1, -1, -1]`；`FreeNode == 6` | 父结点指针 |
| B4 | 接 B3，`SearchTree` 查 `40`、`60`、`50`、`20` | `4`、`5`、`0`、`3` | 找得到 |
| B5 | 接 B3，`SearchTree` 查 `65`、`10` | `-1`、`-1` | 找不到 |
| B6 | 接 B3，再 `InsertNode(30)` | `True`；新结点下标 6；`LeftPointer[4] == 6`（30 往左到 30、相等往右到 40、比 40 小往左）；`SearchTree(30) == 1` | 相等值放右边；不死循环 |
| B7 | 依次插入 `0` 到 `10` 共 11 个数 | 前 10 次 `True`，第 11 次 `False`；`SearchTree(5) == 5` | 满树（边界） |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 方向写反（小的往右）：`LeftPointer`、`RightPointer` 互换 | B3、B6 |
| M2 | 只存数据、没有更新父结点的指针：除根以外都找不到 | B3、B4、B6、B7 |
| M3 | 相等的值不插入、直接返回 `True`：B6 中 `FreeNode` 仍是 6 | B6 |
| M4 | 第一个结点没有设 `RootPointer`：之后每次插入都以为树是空的，什么也没链上 | B2、B3、B4、B6、B7 |

（M3 是为了避免出现「相等时死循环」的 mutant：那样会拖垮 `make check`，见 design.md §7.5。）

## 人工核对清单

- [ ] 伪代码：先判满（`FreeNode = 10`）；存数据、两个指针置 -1；空树时 `RootPointer ← FreeNode`。
- [ ] 伪代码：从根出发的循环里，`IF Item < TreeData[Current] THEN` 往左，`ELSE` 往右；要走的那一侧是 -1 时，改**父结点**那一侧的指针并结束循环（用标志或 `RETURN`，不用 `BREAK`）。
- [ ] 伪代码：相等的值有明确去向（本题为右）——能说出 ECR P4 2024 p.21–22 的范答为什么在有重复值时会死循环。
- [ ] Python：比较的是 `TreeData[Current]`，不是结点对象（ECR P4 2024 p.23）；空树用 `RootPointer == -1` 判断。

## 出处

自编（树的形状与 9618_s24_42 Q2 的例子不同）。误区依据：ECR P4 2024（9618_s24_42 Q2）p.20–23；ER s24 9618/42 Q2 p.44。依据：考纲 19.1（p.37）。
