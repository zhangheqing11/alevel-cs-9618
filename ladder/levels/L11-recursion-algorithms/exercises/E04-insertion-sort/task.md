# L11/E04 · 插入排序：一次插入 + 完整排序


### 中文导读

`InsertOne(TheArray, Index)`：假设 `TheArray[0]` 到 `TheArray[Index - 1]` 已经按从小到大排好，把 `TheArray[Index]` 插到这一段里的正确位置——比它大的元素各往后挪一格，相等的不挪（保持稳定）；`Index` 之后的元素不动；`Index = 0` 时什么也不做。`InsertionSort(TheArray)`：对 `Index` 从 1 到最后依次调用 `InsertOne`，把整个数组原地排好。两个都不返回值。

### English task

- Write a procedure `InsertOne()` that takes an array of integers `TheArray` and an integer `Index`. Elements 0 to `Index - 1` are already in ascending order. The procedure moves the element at position `Index` into its correct place in that part of the array: every element greater than it moves up one place; equal elements do not move. Elements after `Index` are not changed. If `Index` is 0, nothing changes.
- Write a procedure `InsertionSort()` that takes `TheArray` and sorts it into ascending order by calling `InsertOne()` for each index from 1 to the last index.

Both procedures change the array in place and return nothing.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`InsertOne` 用 `ItemToInsert`、`Position` 与一个 BOOLEAN 标志结束内层循环；没有 `WHILE Position >= 0 AND TheArray[Position] > …` 这种依赖短路的写法（卡片 §4）。
- [ ] 伪代码：`InsertionSort` 是 `FOR Index ← 1 TO NumberItems - 1` / `CALL InsertOne(Index)`。
- [ ] Python：没有用 `sort()`、`sorted()`、`insert()`、`pop()` 代劳（D10）。
- [ ] 能说出插入排序与冒泡排序每一趟各做什么，以及已经有序时两者各要比较多少次（卡片 §4、§5）。

## 出处

自编。误区依据：ER s25 9618/43 Q2 p.48（写成冒泡或混合；缺少停止条件）；ER w22 9618/42 Q1 p.48（第二层循环写成冒泡）。依据：考纲 19.1（p.37）。
