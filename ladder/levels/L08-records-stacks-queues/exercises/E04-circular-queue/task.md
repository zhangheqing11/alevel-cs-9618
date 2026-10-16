# L08/E04 · 循环队列：队首、队尾指针与绕回


### 中文导读

队列最多存 5 个字符串。伪代码用 1 起数组，`FrontPointer` 初值 1、`RearPointer` 初值 0、`NumberOfItems` 初值 0。Python 用 0 起 list，`front_pointer = 0`、`rear_pointer = -1`、`number_of_items = 0`。`Enqueue(Item)`：队满返回 `FALSE`，否则把 `Item` 放在队尾并返回 `TRUE`。`Dequeue()`：队空返回 `""`，否则移走并返回队首元素。两个指针越过数组末尾时都要绕回开头。

### English task

A circular queue holds up to 5 strings.

In pseudocode, the queue is the global array `Queue : ARRAY[1:5] OF STRING` with the global integers `FrontPointer` (initialised to 1), `RearPointer` (initialised to 0) and `NumberOfItems` (initialised to 0). Write:

- a function `Enqueue()` that takes a string `Item`; it returns `FALSE` if the queue is full, otherwise it adds `Item` at the rear of the queue and returns `TRUE`
- a function `Dequeue()` that returns the empty string if the queue is empty, otherwise it removes and returns the item at the front of the queue.

Both pointers wrap round to the first element when they move past the last element.

In Python, use the module-level variables given in the starter: `QUEUE_SIZE = 5`, `queue = [""] * QUEUE_SIZE`, `front_pointer = 0`, `rear_pointer = -1`, `number_of_items = 0`. Write `enqueue(item)` and `dequeue()` with the same behaviour.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：满/空都用 `NumberOfItems` 判断；入队「先移 `RearPointer`、绕回、再存」，出队「先取值、再移 `FrontPointer`、绕回」。
- [ ] 伪代码：绕回写成 `IF RearPointer > 5 THEN RearPointer ← 1 ENDIF`，或 `RearPointer ← (RearPointer MOD 5) + 1`；能说出后一种写法为什么要先 MOD 再加 1。
- [ ] 伪代码：入队、出队都没有移动其他元素（ER s23 9618/22 Q3 p.19）；两个函数用 `RETURN`。
- [ ] Python：`global` 写全了要赋值的三个变量；绕回用 `% QUEUE_SIZE`。

## 出处

自编。误区依据：ER s23 9618/22 Q3 p.19（循环队列：以为加入新数据前要移动或删除已有内容）。语法依据：指南 p.10（数组）、p.15（MOD）、p.23（FUNCTION）。
