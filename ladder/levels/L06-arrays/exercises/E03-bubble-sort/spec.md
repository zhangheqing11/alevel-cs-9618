# L06/E03 · 冒泡排序：按分数降序排两个并行数组

| 属性 | 值 |
|:--|:--|
| id | `L06/E03` |
| 目录 | `ladder/levels/L06-arrays/exercises/E03-bubble-sort/` |
| 形态 | `function`（原地修改两个 list，返回 `None`） |
| entry | `sort_by_mark` |
| pseudocode | `true` |
| files | `[]` |
| skills | `bubble-sort`, `parallel-arrays`, `array-index`, `loop-bounds`, `byval-byref` |
| difficulty | 4 |
| title | `Bubble sort two parallel arrays into descending order` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L06 card §5、§6；常见坑 3 |

## 练习目标

写出带交换标志、逐趟缩短的冒泡排序；降序（比较方向）；交换时两个并行数组同步交换；分数相同的学生保持原来的先后次序；原地修改 list（Python 里 list 参数的「BYREF 效果」）。

## 题面

### 中文导读

全局数组 `Names`、`Marks` 是并行数组，`NumStudents` 是人数。写过程 `SortByMark()`：用冒泡排序把学生按分数**从高到低**排好，名字跟着分数一起移动；分数相同的学生保持原来的先后顺序（只在前一个分数**严格小于**后一个时才交换）。要用交换标志：一趟没有交换就提前结束。Python 里两个 list 作为参数传入，**原地**排序，不返回新 list。

### English task

The global arrays `Names` (`ARRAY[1:50] OF STRING`) and `Marks` (`ARRAY[1:50] OF INTEGER`) are parallel arrays; the global integer `NumStudents` is the number of elements in use.

Write a procedure `SortByMark()` that uses a bubble sort to put the students into descending order of mark. When two marks are swapped, the two names must also be swapped. Students with equal marks must stay in their original order, so only swap when the first mark is strictly less than the second. Use a flag so that the sort stops when a pass makes no swaps.

Then write the Python function `sort_by_mark(names, marks)`. It sorts the two lists in place and returns `None`.

## 接口

```python
def sort_by_mark(names: list[str], marks: list[int]) -> None:
    """Bubble sort marks into descending order in place, moving names with them."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: Names : ARRAY[1:50] OF STRING
// global: Marks : ARRAY[1:50] OF INTEGER
// global: NumStudents : INTEGER
PROCEDURE SortByMark()
   // bubble sort with a flag; swap names and marks together

ENDPROCEDURE
```

## 必测行为

每个测试先建 list、调用 `sol.sort_by_mark(names, marks)`，再检查**同一个** list 对象的内容。

| # | 调用前 `names` / `marks` | 调用后 `names` / `marks` | 说明 |
|:--|:--|:--|:--|
| B1 | `["Ann", "Bo", "Cy", "Dee"]` / `[64, 88, 71, 90]` | `["Dee", "Bo", "Cy", "Ann"]` / `[90, 88, 71, 64]` | 普通 |
| B2 | `["P", "Q", "R", "S"]` / `[10, 20, 30, 40]` | `["S", "R", "Q", "P"]` / `[40, 30, 20, 10]` | 原来是升序（最坏情况） |
| B3 | `["A", "B", "C"]` / `[70, 85, 70]` | `["B", "A", "C"]` / `[85, 70, 70]` | 同分保持原顺序 |
| B4 | `["W", "X", "Y", "Z"]` / `[60, 60, 60, 60]` | 不变 | 全部同分 |
| B5 | `["Solo"]` / `[50]` | 不变 | 一个元素 |
| B6 | `[]` / `[]` | `[]` / `[]` | 空（边界） |
| B7 | 返回值 | `None`；传入的两个 list 对象本身被修改（不是新建 list） | 原地 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 只交换分数，名字不动：B1 的 `names` 仍是 `["Ann", "Bo", "Cy", "Dee"]` | B1、B2、B3 |
| M2 | 比较方向写反（`>`），排成升序（ECR P4 2021 p.25 点名） | B1、B2、B3 |
| M3 | 同分也交换（`<=`）：用固定趟数 `for i in range(n - 1): for j in range(n - 1 - i)` 实现，B3 得 `["B", "C", "A"]` | B3、B4 |
| M4 | 内层循环越界：`for j in range(len(marks))`，访问 `marks[j + 1]` 抛 `IndexError` | B1–B5 |
| M5 | 不原地修改：函数里 `marks = sorted(marks, reverse=True)` 等，调用者的 list 不变 | B1、B2、B3、B7 |

（M3 用固定趟数实现，避免在同分时因标志永远为 TRUE 而死循环。）

## 人工核对清单

- [ ] 伪代码：外层 `REPEAT … UNTIL` 或 `WHILE` 带 `Swapped` 标志；内层 `FOR J ← 1 TO Boundary`，`Boundary` 从 `NumStudents - 1` 起每趟减 1。
- [ ] 伪代码：比较 `Marks[J] < Marks[J + 1]`；交换用临时变量，分数与名字各用一个临时变量（类型不同）。
- [ ] 伪代码：`J + 1` 不会超过 `NumStudents`（ER w22 9618/22 Q7 p.25：上界导致比较越界）。
- [ ] Python：没有调用 `sort()`、`sorted()`。
- [ ] 能说出：为什么用 `<` 而不是 `<=` 时同分的学生顺序不变（冒泡排序是稳定的）。

## 出处

自编。题型参考 ER w22 9618/22 Q7（p.24–25：两个数组同时交换的冒泡排序）。误区依据：ECR P4 2021（9618_s21_42）p.25（降序写成升序；内层循环上界过大）。语法依据：指南 p.10（数组）、p.20–21（FOR、REPEAT）、p.22（PROCEDURE）。
