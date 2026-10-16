# L11/E03 · 二分查找：迭代与递归


### 中文导读

`SearchArray` 已按从小到大排好。`BinarySearch(SearchArray, SearchItem)`：用循环做二分查找，找到返回下标（从 0 起），找不到返回 `-1`。`RecursiveBinarySearch(SearchArray, SearchItem, Low, High)`：在下标 `Low` 到 `High` 之间递归地二分查找，返回值同上。数组里没有重复值。

### English task

`SearchArray` is sorted into ascending order and contains no repeated values.

- Write a function `BinarySearch()` that takes `SearchArray` and an integer `SearchItem` and uses an **iterative** binary search. It returns the index of `SearchItem` (indexes start at 0), or `-1` if it is not found.
- Write a function `RecursiveBinarySearch()` that takes `SearchArray`, `SearchItem`, `Low` and `High`, and uses a **recursive** binary search on the elements from index `Low` to index `High`. It returns the index of `SearchItem`, or `-1` if it is not found.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`Mid ← (Low + High) DIV 2`；`WHILE Low <= High`；`Low ← Mid + 1` / `High ← Mid - 1`。
- [ ] 伪代码：递归版的基本情况 `IF Low > High THEN RETURN -1`；一般情况 `RETURN RecursiveBinarySearch(SearchArray, SearchItem, Mid + 1, High)` 等，函数调用不写 `CALL`。
- [ ] Python：没有用 `in`、`index()` 代劳（D10）——这两者不经过 `__getitem__`，B7 抓不到，靠这一条人工核对。
- [ ] 能说出二分查找的前提（已排序），以及 1024 个元素最多比较多少次。

## 出处

自编。题型参考 ER s24 9618/42 Q3(d)（p.45：要求写递归二分查找，找不到返回 -1）与 ER s24 9618/41 Q1(e)（p.39：要求写迭代版）。误区依据：ER s24 9618/42 Q3 p.45（递归函数里又套循环）；ER s25 9618/43 Q2 p.49（写成线性查找）。
