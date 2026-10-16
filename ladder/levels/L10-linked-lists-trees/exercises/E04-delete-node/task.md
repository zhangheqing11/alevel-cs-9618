# L10/E04 · 链表删除：结点还给空闲表


### 中文导读

全局数组与指针同 E02（6 个结点，空指针 `-1`）。写函数 `DeleteItem(Item)`：删除链表中**第一个**数据等于 `Item` 的结点，把它放到空闲表的最前面，返回 `True`；找不到返回 `False`，所有数组与指针都不变。测试会直接给全局变量赋值来建立删除前的状态，所以本题不需要写插入。

### English task

The global arrays `ListData` and `ListPointer`, and the global integers `StartPointer` and `FreePointer`, are as in E02 (6 nodes, null pointer `-1`).

Write a function `DeleteItem()` that takes a string `Item`. It finds the first node in the list whose data is `Item`, removes that node from the list, adds it to the start of the free list, and returns `True`. If no node holds `Item`, it returns `False` and changes nothing.

The tests set up the arrays and pointers directly, so you do not need to write any insert routine.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`Previous ← -1`、`Current ← StartPointer`；`WHILE Current <> -1 AND ListData[Current] <> Item` 时向前走；走到 `-1` 就 `RETURN FALSE`。
- [ ] 伪代码：`IF Previous = -1 THEN StartPointer ← ListPointer[Current] ELSE ListPointer[Previous] ← ListPointer[Current]`；然后 `ListPointer[Current] ← FreePointer`、`FreePointer ← Current`。
- [ ] Python：`global StartPointer, FreePointer`；没有用 `remove`、`pop` 或重建 list 代替指针操作。
- [ ] 能说出为什么删掉的结点不必清空 `ListData`。

## 出处

自编。依据：考纲 19.1「delete an item from … linked list」（p.37）；L10 card §5。
