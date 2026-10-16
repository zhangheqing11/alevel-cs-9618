# L10/E03 · 有序链表：按序插入


### 中文导读

沿用 E02 的全局数组和 `InitialiseList()`、`OutputList()`（可以照抄你 E02 的代码）。新写函数 `InsertInOrder(Item)`：把 `Item` 插到链表里，使链表始终按字母从小到大排列；和已有数据相等时，插在已有那一项的**后面**；没有空闲结点时返回 `False`。

### English task

Use the same global arrays as in E02 (`ListData`, `ListPointer`, `StartPointer`, `FreePointer`; 6 nodes; null pointer `-1`), and include `InitialiseList()` and `OutputList()` exactly as specified in E02.

Write a function `InsertInOrder()` that takes a string `Item`. It returns `False` if there are no free nodes. Otherwise it stores `Item` in the first free node and links that node into the list so that the list stays in ascending order. An item equal to one already in the list is placed after it. The function then returns `True`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：先判断 `FreePointer = -1`；取结点并存数据；`Previous ← -1`、`Current ← StartPointer`；`WHILE Current <> -1 AND ListData[Current] <= Item` 时向前走。
- [ ] 伪代码：`IF Previous = -1 THEN` 改 `StartPointer`，`ELSE` 改 `ListPointer[Previous]`；两种情况下新结点都先指向后继（`ListPointer[NewNode] ← StartPointer` 或 `← ListPointer[Previous]`）。
- [ ] 伪代码：没有 `BREAK`；`RETURN TRUE` / `RETURN FALSE`。
- [ ] Python：能说出 M3 为什么在 Python 里不报错（`ListPointer[-1]` 是最后一个元素），以及如何避免。

## 出处

自编。误区依据：ECR P4 2021（9618_s21_42 Q1(d)）p.16：考生把新数据追加到链表数组末尾，或没有更新上一个结点的指针。语法依据：指南 p.10、p.21、p.23。
