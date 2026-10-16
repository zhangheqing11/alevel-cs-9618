# L11/E03 · 二分查找：迭代与递归

| 属性 | 值 |
|:--|:--|
| id | `L11/E03` |
| 目录 | `ladder/levels/L11-recursion-algorithms/exercises/E03-binary-search/` |
| 形态 | `function`（两个函数；测试检查结果、读取元素的次数，以及递归版确实递归） |
| entry | `BinarySearch`（同一文件还有 `RecursiveBinarySearch`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `binary-search`, `recursion`, `div-mod`, `boundary-values`, `p4-identifiers` |
| difficulty | 4 |
| title | `Binary search: iterative and recursive` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L11 card §3 |

## 练习目标

写出两个版本的二分查找：迭代版用 `Low`/`High`/`Mid` 循环；递归版把 `Low`、`High` 作为参数，基本情况是 `Low > High`。测试会数你读了几次数组元素，线性查找通不过（ER s25 9618/43 Q2 p.49：要求二分查找却写了线性查找）。

## 题面

### 中文导读

`SearchArray` 已按从小到大排好。`BinarySearch(SearchArray, SearchItem)`：用循环做二分查找，找到返回下标（从 0 起），找不到返回 `-1`。`RecursiveBinarySearch(SearchArray, SearchItem, Low, High)`：在下标 `Low` 到 `High` 之间递归地二分查找，返回值同上。数组里没有重复值。

### English task

`SearchArray` is sorted into ascending order and contains no repeated values.

- Write a function `BinarySearch()` that takes `SearchArray` and an integer `SearchItem` and uses an **iterative** binary search. It returns the index of `SearchItem` (indexes start at 0), or `-1` if it is not found.
- Write a function `RecursiveBinarySearch()` that takes `SearchArray`, `SearchItem`, `Low` and `High`, and uses a **recursive** binary search on the elements from index `Low` to index `High`. It returns the index of `SearchItem`, or `-1` if it is not found.

## 接口

```python
def BinarySearch(SearchArray: list[int], SearchItem: int) -> int:
    """Iterative binary search: return the index of SearchItem, or -1."""
    raise NotImplementedError


def RecursiveBinarySearch(SearchArray: list[int], SearchItem: int, Low: int, High: int) -> int:
    """Recursive binary search between indexes Low and High: return the index, or -1."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION BinarySearch(SearchArray : ARRAY OF INTEGER, NumberItems : INTEGER, SearchItem : INTEGER) RETURNS INTEGER
   DECLARE Low : INTEGER
   DECLARE High : INTEGER
   DECLARE Mid : INTEGER

ENDFUNCTION

FUNCTION RecursiveBinarySearch(SearchArray : ARRAY OF INTEGER, SearchItem : INTEGER, Low : INTEGER, High : INTEGER) RETURNS INTEGER
   DECLARE Mid : INTEGER

ENDFUNCTION
```

（指南没有给出数组参数的写法；这里沿用 `schemas/examples` 的 `ARRAY OF INTEGER`，伪代码用 `NumberItems` 代替 Python 的 `len()`。）

## 必测行为

`A = [3, 8, 15, 22, 41, 56, 70, 89]`。递归版一律以 `Low = 0`、`High = len(SearchArray) - 1` 调用。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `BinarySearch(A, 22)`、`BinarySearch(A, 41)` | `3`、`4` | 中间附近 |
| B2 | `BinarySearch(A, 3)`、`BinarySearch(A, 89)` | `0`、`7` | 两端（边界） |
| B3 | `BinarySearch(A, 1)`、`BinarySearch(A, 100)`、`BinarySearch(A, 50)` | `-1`、`-1`、`-1` | 小于最小、大于最大、落在中间的空隙 |
| B4 | `BinarySearch([], 5)`、`BinarySearch([7], 7)` | `-1`、`0` | 空数组、一个元素 |
| B5 | `RecursiveBinarySearch(A, x, 0, 7)`，`x` 取 `3`、`89`、`22`、`1`、`100` | `0`、`7`、`3`、`-1`、`-1` | |
| B6 | `RecursiveBinarySearch([], 5, 0, -1)` | `-1` | 空范围 |
| B7 | 读取次数：`BIG` 是一个统计 `__getitem__` 调用次数的 `list` 子类，内容为 `0, 2, 4, …, 2046`（1024 个元素）；`BinarySearch(BIG, 2046)`、`BinarySearch(BIG, 1)`、`RecursiveBinarySearch(BIG, 2046, 0, 1023)` | 分别返回 `1023`、`-1`、`1023`；每次调用读取元素的次数都 ≤ 50 | 二分查找约读 20 次；线性查找要读约 1000 次 |
| B8 | 递归检查：计数包装 `sol.RecursiveBinarySearch` 后调用 `(A, 89, 0, 7)` | 结果 `7`，包装被调用 ≥ 2 次 | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 两个函数都写 `Mid = (Low + High) / 2`：实数下标，抛 `TypeError` | B1–B5、B7、B8 |
| M2 | 循环条件写成 `while Low < High`：只剩一个元素时没有检查，`89`、`3`、`41` 都返回 `-1` | B1、B2、B4、B7 |
| M3 | 递归版没有 `return` 递归调用的结果：除第一次就命中的情况外都返回 `None` | B5、B7、B8 |
| M4 | `BinarySearch` 写成线性查找（逐个比较）：结果正确，但读取次数约 1024 | B7 |

（不要做 `Low = Mid` 这种可能死循环的 mutant，见 design.md §7.5。）

## 人工核对清单

- [ ] 伪代码：`Mid ← (Low + High) DIV 2`；`WHILE Low <= High`；`Low ← Mid + 1` / `High ← Mid - 1`。
- [ ] 伪代码：递归版的基本情况 `IF Low > High THEN RETURN -1`；一般情况 `RETURN RecursiveBinarySearch(SearchArray, SearchItem, Mid + 1, High)` 等，函数调用不写 `CALL`。
- [ ] Python：没有用 `in`、`index()` 代劳（D10）——这两者不经过 `__getitem__`，B7 抓不到，靠这一条人工核对。
- [ ] 能说出二分查找的前提（已排序），以及 1024 个元素最多比较多少次。

## 出处

自编。题型参考 ER s24 9618/42 Q3(d)（p.45：要求写递归二分查找，找不到返回 -1）与 ER s24 9618/41 Q1(e)（p.39：要求写迭代版）。误区依据：ER s24 9618/42 Q3 p.45（递归函数里又套循环）；ER s25 9618/43 Q2 p.49（写成线性查找）。
