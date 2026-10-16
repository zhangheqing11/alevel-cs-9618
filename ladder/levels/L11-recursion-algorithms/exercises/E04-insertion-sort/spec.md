# L11/E04 · 插入排序：一次插入 + 完整排序

| 属性 | 值 |
|:--|:--|
| id | `L11/E04` |
| 目录 | `ladder/levels/L11-recursion-algorithms/exercises/E04-insertion-sort/` |
| 形态 | `function`（两个过程，原地修改 list；测试检查一次插入后的中间状态，以及 `InsertionSort` 确实调用了 `InsertOne`） |
| entry | `InsertionSort`（同一文件还有 `InsertOne`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `insertion-sort`, `pre-condition-loop`, `array-index`, `boundary-values`, `p4-identifiers` |
| difficulty | 4 |
| title | `Insertion sort: one insertion step, then the whole sort` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L11 card §4 |

## 练习目标

把插入排序拆成两层：`InsertOne` 只做「把一个元素插进已排好的前半」这一步，`InsertionSort` 对下标 1 到 n-1 依次调用它。测试检查一步之后的状态，这样冒泡排序式的「相邻交换一次」就通不过（ER s25 9618/43 Q2 p.48：写成冒泡排序或混合两者）。

## 题面

### 中文导读

`InsertOne(TheArray, Index)`：假设 `TheArray[0]` 到 `TheArray[Index - 1]` 已经按从小到大排好，把 `TheArray[Index]` 插到这一段里的正确位置——比它大的元素各往后挪一格，相等的不挪（保持稳定）；`Index` 之后的元素不动；`Index = 0` 时什么也不做。`InsertionSort(TheArray)`：对 `Index` 从 1 到最后依次调用 `InsertOne`，把整个数组原地排好。两个都不返回值。

### English task

- Write a procedure `InsertOne()` that takes an array of integers `TheArray` and an integer `Index`. Elements 0 to `Index - 1` are already in ascending order. The procedure moves the element at position `Index` into its correct place in that part of the array: every element greater than it moves up one place; equal elements do not move. Elements after `Index` are not changed. If `Index` is 0, nothing changes.
- Write a procedure `InsertionSort()` that takes `TheArray` and sorts it into ascending order by calling `InsertOne()` for each index from 1 to the last index.

Both procedures change the array in place and return nothing.

## 接口

```python
def InsertOne(TheArray: list[int], Index: int) -> None:
    """Insert TheArray[Index] into the sorted part TheArray[0..Index-1], in place."""
    raise NotImplementedError


def InsertionSort(TheArray: list[int]) -> None:
    """Sort TheArray in place by calling InsertOne() for Index = 1 .. len - 1."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: TheArray : ARRAY[0:99] OF INTEGER; NumberItems : INTEGER
PROCEDURE InsertOne(Index : INTEGER)
   // use a flag to end the inner loop (L11 card §4)

ENDPROCEDURE

PROCEDURE InsertionSort()

ENDPROCEDURE
```

## 必测行为

每个测试先建 list、调用后检查**同一个** list 对象的内容。T10 已用参考实现核对。

| # | 调用 | 调用后的 list | 说明 |
|:--|:--|:--|:--|
| B1 | `InsertOne([2, 5, 8, 3, 1], 3)` | `[2, 3, 5, 8, 1]` | 插到中间；最后的 1 不动 |
| B2 | `InsertOne([2, 3, 5, 8, 1], 4)` | `[1, 2, 3, 5, 8]` | 插到最前面（边界） |
| B3 | `InsertOne([1, 4, 9], 2)`、`InsertOne([4, 2, 1], 0)` | `[1, 4, 9]`、`[4, 2, 1]` | 已在正确位置；`Index = 0` |
| B4 | `InsertOne([5, 7, 6], 2)` | `[5, 6, 7]` | 只挪一个 |
| B5 | `InsertionSort([45, 12, 78, 3, 33, 12])` | `[3, 12, 12, 33, 45, 78]` | 含重复值 |
| B6 | `InsertionSort([])`、`InsertionSort([5])`、`InsertionSort([1, 2, 3])`、`InsertionSort([9, 7, 5, 3, 1])` | `[]`、`[5]`、`[1, 2, 3]`、`[1, 3, 5, 7, 9]` | 空、一个、已排好、逆序 |
| B7 | 把 `sol.InsertOne` 换成计数包装后调用 `sol.InsertionSort([4, 3, 2, 1, 0])` | 结果 `[0, 1, 2, 3, 4]`；包装被调用 ≥ 4 次 | 确实使用 `InsertOne` |
| B8 | 两个过程的返回值 | `None`；传入的 list 对象本身被修改 | 原地 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `InsertOne` 只和前一个元素比较、交换一次（冒泡式）：B1 得 `[2, 5, 3, 8, 1]`（B4 碰巧正确） | B1、B2、B5、B6、B7 |
| M2 | `InsertOne` 没有「到位就停」的条件：一路挪到最前面，B1 得 `[3, 2, 5, 8, 1]`（B2 碰巧正确） | B1、B3、B4、B5、B6、B7 |
| M3 | `InsertionSort` 漏了最后一个下标（`range(1, len(TheArray) - 1)`）：B6 逆序的例子得 `[3, 5, 7, 9, 1]` | B5、B6、B7 |
| M4 | `InsertionSort` 直接调用 `TheArray.sort()`：结果正确，但计数包装 0 次 | B7 |

## 人工核对清单

- [ ] 伪代码：`InsertOne` 用 `ItemToInsert`、`Position` 与一个 BOOLEAN 标志结束内层循环；没有 `WHILE Position >= 0 AND TheArray[Position] > …` 这种依赖短路的写法（卡片 §4）。
- [ ] 伪代码：`InsertionSort` 是 `FOR Index ← 1 TO NumberItems - 1` / `CALL InsertOne(Index)`。
- [ ] Python：没有用 `sort()`、`sorted()`、`insert()`、`pop()` 代劳（D10）。
- [ ] 能说出插入排序与冒泡排序每一趟各做什么，以及已经有序时两者各要比较多少次（卡片 §4、§5）。

## 出处

自编。误区依据：ER s25 9618/43 Q2 p.48（写成冒泡或混合；缺少停止条件）；ER w22 9618/42 Q1 p.48（第二层循环写成冒泡）。依据：考纲 19.1（p.37）。
