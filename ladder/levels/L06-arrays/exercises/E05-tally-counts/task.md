# L06/E05 · 骰子计数：计数数组与「值 → 下标」


### 中文导读

全局数组 `Rolls` 存了 `NumRolls` 次掷骰子的结果（每个都是 1 到 6）。写过程 `CountRolls()`：把每个点数出现的次数存进全局数组 `Tally : ARRAY[1:6] OF INTEGER`。再写函数 `MostFrequent()`：返回出现次数最多的点数；次数相同时返回较小的点数；一次都没掷时返回 0。Python 里 `tally(rolls)` 返回长度为 6 的 list（第 0 个元素是点数 1 的次数），`most_frequent(rolls)` 返回点数。

### English task

The global array `Rolls : ARRAY[1:100] OF INTEGER` stores `NumRolls` dice rolls; each roll is an integer from 1 to 6.

1. Write a procedure `CountRolls()` that stores in the global array `Tally : ARRAY[1:6] OF INTEGER` how many times each value from 1 to 6 was rolled. `Tally` must be initialised first.
2. Write a function `MostFrequent()` that returns the value rolled most often. If two or more values share the highest count, return the smallest of them. If `NumRolls` is 0, return 0.

Then write the Python functions:

- `tally(rolls)` returns a list of 6 integers; element 0 is the count of 1s, element 5 is the count of 6s
- `most_frequent(rolls)` returns the value as described above.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`CountRolls` 先 `FOR Value ← 1 TO 6` 把 `Tally[Value] ← 0`（ECR P2 2021 p.32：考生没有初始化计数数组），再 `FOR Index ← 1 TO NumRolls` 执行 `Tally[Rolls[Index]] ← Tally[Rolls[Index]] + 1`。
- [ ] 伪代码：`MostFrequent` 先判断 `NumRolls = 0`；找最大时用 `>`（不是 `>=`），保证并列时留下较小的点数。
- [ ] 伪代码：全局数组没有在模块里重新 `DECLARE`（ER w25 9618/21 Q4 p.18）。
- [ ] Python：能说出 `[0] * 6` 与逐个 `append` 的区别，以及为什么 `counts[roll - 1]` 要减 1。

## 出处

自编。误区依据：ECR P2 2021（9618_s21_22 Q6）p.32（计数数组未初始化）；ER w25 9618/21 Q4 p.18（全局数组声明成局部）。语法依据：指南 p.10–11（数组、用循环初始化）。
