# L11/E05 · 递归遍历二叉树：中序输出、数结点、求高度


### 中文导读

全局数组 `LeftPointer`、`TreeData`、`RightPointer` 与 `RootPointer` 同 L10/E05（10 个元素，空指针 `-1`）。写三个递归模块，参数都是一个结点下标 `NodePointer`（可以是 `-1`）：`InOrder(NodePointer)` 按中序输出以它为根的子树的数据（每行一个）；`CountNodes(NodePointer)` 返回这棵子树的结点数；`TreeHeight(NodePointer)` 返回这棵子树的高度（空树为 0，只有一个结点为 1）。测试会直接给全局变量赋值来建树。

### English task

The global arrays `LeftPointer`, `TreeData` and `RightPointer` and the global integer `RootPointer` store a binary search tree as in L10/E05 (10 elements, null pointer `-1`). The tests set these globals directly.

Write three recursive modules. Each takes a node index `NodePointer`, which may be `-1`:

- a procedure `InOrder()` that outputs the data in the subtree rooted at `NodePointer` using an in-order traversal, one value per line
- a function `CountNodes()` that returns the number of nodes in that subtree
- a function `TreeHeight()` that returns the height of that subtree: 0 for an empty tree, 1 for a single node, otherwise 1 more than the greater height of its two subtrees.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：三个模块都以 `IF NodePointer <> -1 THEN …`（或 `IF NodePointer = -1 THEN RETURN 0`）开头；`InOrder` 里递归调用用 `CALL InOrder(LeftPointer[NodePointer])`。
- [ ] 伪代码：`CountNodes` 是 `RETURN 1 + CountNodes(LeftPointer[NodePointer]) + CountNodes(RightPointer[NodePointer])`；`TreeHeight` 取两侧较大值（自己用 IF 比较，不用 `max`）。
- [ ] 能写出前序、后序遍历，并说出三者只差在哪一行的位置。
- [ ] Python：没有把树转成 list 再 `sort()` 来输出（D10）。

## 出处

自编。依据：考纲 19.1–19.2（p.37）；L10 card §6。
