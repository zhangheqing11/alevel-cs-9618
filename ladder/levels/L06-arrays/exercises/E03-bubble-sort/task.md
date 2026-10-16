# L06/E03 · 冒泡排序：按分数降序排两个并行数组


### 中文导读

全局数组 `Names`、`Marks` 是并行数组，`NumStudents` 是人数。写过程 `SortByMark()`：用冒泡排序把学生按分数**从高到低**排好，名字跟着分数一起移动；分数相同的学生保持原来的先后顺序（只在前一个分数**严格小于**后一个时才交换）。要用交换标志：一趟没有交换就提前结束。Python 里两个 list 作为参数传入，**原地**排序，不返回新 list。

### English task

The global arrays `Names` (`ARRAY[1:50] OF STRING`) and `Marks` (`ARRAY[1:50] OF INTEGER`) are parallel arrays; the global integer `NumStudents` is the number of elements in use.

Write a procedure `SortByMark()` that uses a bubble sort to put the students into descending order of mark. When two marks are swapped, the two names must also be swapped. Students with equal marks must stay in their original order, so only swap when the first mark is strictly less than the second. Use a flag so that the sort stops when a pass makes no swaps.

Then write the Python function `sort_by_mark(names, marks)`. It sorts the two lists in place and returns `None`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：外层 `REPEAT … UNTIL` 或 `WHILE` 带 `Swapped` 标志；内层 `FOR J ← 1 TO Boundary`，`Boundary` 从 `NumStudents - 1` 起每趟减 1。
- [ ] 伪代码：比较 `Marks[J] < Marks[J + 1]`；交换用临时变量，分数与名字各用一个临时变量（类型不同）。
- [ ] 伪代码：`J + 1` 不会超过 `NumStudents`（ER w22 9618/22 Q7 p.25：上界导致比较越界）。
- [ ] Python：没有调用 `sort()`、`sorted()`。
- [ ] 能说出：为什么用 `<` 而不是 `<=` 时同分的学生顺序不变（冒泡排序是稳定的）。

## 出处

自编。题型参考 ER w22 9618/22 Q7（p.24–25：两个数组同时交换的冒泡排序）。误区依据：ECR P4 2021（9618_s21_42）p.25（降序写成升序；内层循环上界过大）。语法依据：指南 p.10（数组）、p.20–21（FOR、REPEAT）、p.22（PROCEDURE）。
