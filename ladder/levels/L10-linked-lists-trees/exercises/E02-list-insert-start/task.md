# L10/E02 · 链表：初始化空闲表、表头插入、遍历输出


### 中文导读

链表最多 6 个结点，存在全局数组 `ListData`（字符串）与 `ListPointer`（整数）里；`StartPointer` 指向第一个结点，`FreePointer` 指向第一个空闲结点，`-1` 是空指针。写三个模块：`InitialiseList()`、`InsertAtStart(Item)`、`OutputList()`，规则见英文题干。

### English task

A linked list of up to 6 nodes is stored in the global arrays `ListData` (`STRING`) and `ListPointer` (`INTEGER`), with indexes 0 to 5. The global integer `StartPointer` points to the first node in the list and `FreePointer` points to the first free node. The null pointer is `-1`.

Write:

- a procedure `InitialiseList()` that sets every element of `ListData` to `""`, links all 6 nodes into the free list in index order (node 0 points to node 1, …, node 5 points to `-1`), sets `StartPointer` to `-1` and `FreePointer` to 0
- a function `InsertAtStart()` that takes a string `Item`; it returns `False` if there are no free nodes, otherwise it takes the first free node, stores `Item` in it, makes it the first node of the list and returns `True`
- a procedure `OutputList()` that outputs the data of each node in list order, one item per line, or outputs `Empty list` if the list is empty.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] 全局数组按 D10 真实建出并注释类型与大小；指针初值、空指针 `-1` 照题目。
- [ ] `InsertAtStart` 的四步顺序：取 `NewNode ← FreePointer` → `FreePointer ← ListPointer[NewNode]` → 存数据 → `ListPointer[NewNode] ← StartPointer` → `StartPointer ← NewNode`。
- [ ] `OutputList` 的循环条件是 `Current != -1`；没有用 `for i in range(6)` 按数组顺序输出（ECR P4 2021 p.13、p.16）。
- [ ] 没有用 Python 的 `insert`/`append` 代替空闲表（D10；ECR P4 2021 p.15–16）。

## 出处

自编。误区依据：ECR P4 2021（9618_s21_42 Q1）p.9、p.13、p.15–16。
