# L06/E05 · 骰子计数：计数数组与「值 → 下标」

| 属性 | 值 |
|:--|:--|
| id | `L06/E05` |
| 目录 | `ladder/levels/L06-arrays/exercises/E05-tally-counts/` |
| 形态 | `function`（两个函数） |
| entry | `tally`（同一文件还有 `most_frequent`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `counting-array`, `array-index`, `accumulator`, `boundary-values`, `return-value` |
| difficulty | 3 |
| title | `Dice tally: a counting array indexed by value` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L06 card §1、§3；常见坑 4 |

## 练习目标

用一个计数数组按「值」作下标累加（`Tally[Roll] ← Tally[Roll] + 1`）；先把计数数组初始化为 0；在 Python 里把 1–6 的值换成 0–5 的下标；在计数数组里找最大值的位置，并按规则处理并列。

## 题面

### 中文导读

全局数组 `Rolls` 存了 `NumRolls` 次掷骰子的结果（每个都是 1 到 6）。写过程 `CountRolls()`：把每个点数出现的次数存进全局数组 `Tally : ARRAY[1:6] OF INTEGER`。再写函数 `MostFrequent()`：返回出现次数最多的点数；次数相同时返回较小的点数；一次都没掷时返回 0。Python 里 `tally(rolls)` 返回长度为 6 的 list（第 0 个元素是点数 1 的次数），`most_frequent(rolls)` 返回点数。

### English task

The global array `Rolls : ARRAY[1:100] OF INTEGER` stores `NumRolls` dice rolls; each roll is an integer from 1 to 6.

1. Write a procedure `CountRolls()` that stores in the global array `Tally : ARRAY[1:6] OF INTEGER` how many times each value from 1 to 6 was rolled. `Tally` must be initialised first.
2. Write a function `MostFrequent()` that returns the value rolled most often. If two or more values share the highest count, return the smallest of them. If `NumRolls` is 0, return 0.

Then write the Python functions:

- `tally(rolls)` returns a list of 6 integers; element 0 is the count of 1s, element 5 is the count of 6s
- `most_frequent(rolls)` returns the value as described above.

## 接口

```python
def tally(rolls: list[int]) -> list[int]:
    """Return [count of 1s, count of 2s, ..., count of 6s]."""
    raise NotImplementedError


def most_frequent(rolls: list[int]) -> int:
    """Return the most frequent value (smallest on a tie), or 0 if rolls is empty."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: Rolls : ARRAY[1:100] OF INTEGER
// global: NumRolls : INTEGER
// global: Tally : ARRAY[1:6] OF INTEGER
PROCEDURE CountRolls()

ENDPROCEDURE

FUNCTION MostFrequent() RETURNS INTEGER
   // assume CountRolls() has already been called

ENDFUNCTION
```

## 必测行为

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `tally([1, 6, 6, 3])` | `[1, 0, 1, 0, 0, 2]` | 普通；6 也要数到（最大值的下标） |
| B2 | `tally([])` | `[0, 0, 0, 0, 0, 0]` | 一定是 6 个 0，不是空 list |
| B3 | `tally([6, 6, 6, 6, 6])`、`tally([1, 2, 3, 4, 5, 6])` | `[0, 0, 0, 0, 0, 5]`、`[1, 1, 1, 1, 1, 1]` | |
| B4 | `most_frequent([1, 6, 6, 3])` | `6` | |
| B5 | `most_frequent([2, 2, 5, 5])`、`most_frequent([1, 2, 3, 4, 5, 6])` | `2`、`1` | 并列取较小值 |
| B6 | `most_frequent([4])`、`most_frequent([])` | `4`、`0` | 一次；没有数据 |
| B7 | 返回类型 | `tally` 返回长度 6 的 `list`，元素为 `int`；`most_frequent` 返回 `int` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 值没有换成下标：`counts[roll] += 1`，掷出 6 时抛 `IndexError`；掷出 1 时计到了点数 2 的位置 | B1、B3–B6 |
| M2 | 计数数组没有预先建好 6 个 0，而是只为出现过的值 `append`：`tally([])` 返回 `[]` | B1、B2、B3 |
| M3 | 并列时取较大值（比较用 `>=`）：`most_frequent([2, 2, 5, 5])` 返回 `5` | B5 |
| M4 | 返回最高的次数而不是点数：`most_frequent([1, 6, 6, 3])` 返回 `2` | B4、B6 |

（M4 在 B5 上碰巧对：`[2, 2, 5, 5]` 的最高次数恰好是 2，`[1, 2, 3, 4, 5, 6]` 恰好是 1。）

## 人工核对清单

- [ ] 伪代码：`CountRolls` 先 `FOR Value ← 1 TO 6` 把 `Tally[Value] ← 0`（ECR P2 2021 p.32：考生没有初始化计数数组），再 `FOR Index ← 1 TO NumRolls` 执行 `Tally[Rolls[Index]] ← Tally[Rolls[Index]] + 1`。
- [ ] 伪代码：`MostFrequent` 先判断 `NumRolls = 0`；找最大时用 `>`（不是 `>=`），保证并列时留下较小的点数。
- [ ] 伪代码：全局数组没有在模块里重新 `DECLARE`（ER w25 9618/21 Q4 p.18）。
- [ ] Python：能说出 `[0] * 6` 与逐个 `append` 的区别，以及为什么 `counts[roll - 1]` 要减 1。

## 出处

自编。误区依据：ECR P2 2021（9618_s21_22 Q6）p.32（计数数组未初始化）；ER w25 9618/21 Q4 p.18（全局数组声明成局部）。语法依据：指南 p.10–11（数组、用循环初始化）。
