# L10/E05 · 二叉查找树：插入（含相等值）与查找


### 中文导读

树最多 10 个结点，存在全局数组 `LeftPointer`、`TreeData`、`RightPointer` 里（都是整数，初值 `-1`）；`RootPointer` 指向根（空树为 `-1`）；`FreeNode` 是下一个未用的下标（结点按 0、1、2… 依次使用，不删除）。写 `InsertNode(Item)`：树满返回 `False`；否则把 `Item` 存进 `FreeNode` 位置、链到正确的位置（比当前结点小往左，否则——包括相等——往右），返回 `True`。写 `SearchTree(Item)`：返回存有 `Item` 的结点下标（有相等值时返回最先找到的那个），没有返回 `-1`。

### English task

A binary search tree of up to 10 nodes is stored in three global arrays of integers, `LeftPointer`, `TreeData` and `RightPointer` (indexes 0 to 9, every element initialised to `-1`). The global integer `RootPointer` points to the root node (`-1` for an empty tree) and the global integer `FreeNode` is the index of the next unused element, starting at 0. Nodes are used in index order and are never deleted.

Write:

- a function `InsertNode()` that takes an integer `Item`. It returns `False` if the tree is full. Otherwise it stores `Item` in element `FreeNode` with both pointers set to `-1`, links the new node into the tree (go left if `Item` is less than the data in the current node, otherwise go right — so equal values go to the right), adds 1 to `FreeNode` and returns `True`
- a function `SearchTree()` that takes an integer `Item` and returns the index of the node that holds `Item`, or `-1` if it is not in the tree. If there are equal values, return the first one found on the path from the root.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：先判满（`FreeNode = 10`）；存数据、两个指针置 -1；空树时 `RootPointer ← FreeNode`。
- [ ] 伪代码：从根出发的循环里，`IF Item < TreeData[Current] THEN` 往左，`ELSE` 往右；要走的那一侧是 -1 时，改**父结点**那一侧的指针并结束循环（用标志或 `RETURN`，不用 `BREAK`）。
- [ ] 伪代码：相等的值有明确去向（本题为右）——能说出 ECR P4 2024 p.21–22 的范答为什么在有重复值时会死循环。
- [ ] Python：比较的是 `TreeData[Current]`，不是结点对象（ECR P4 2024 p.23）；空树用 `RootPointer == -1` 判断。

## 出处

自编（树的形状与 9618_s24_42 Q2 的例子不同）。误区依据：ECR P4 2024（9618_s24_42 Q2）p.20–23；ER s24 9618/42 Q2 p.44。依据：考纲 19.1（p.37）。
