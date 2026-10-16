# L11/E02 · 递归函数：阶乘、数位和、字符串反转


### 中文导读

三个函数都必须递归（函数里用自己的名字调用自己，不用循环）：`Factorial(N)` 返回 N!（N ≥ 0，0! = 1）；`SumDigits(N)` 返回非负整数 N 的各位数字之和（用 `DIV`/`MOD`）；`Reverse(Text)` 返回字符串倒过来的结果（空串的反转是空串）。

### English task

Write three recursive functions. Each must call itself; do not use loops.

- `Factorial()` takes an integer `N` (0 or more) and returns N! (0! is 1).
- `SumDigits()` takes an integer `N` (0 or more) and returns the sum of its digits. Use `DIV` and `MOD`.
- `Reverse()` takes a string `Text` and returns the characters of `Text` in reverse order. The reverse of the empty string is the empty string.

Write pseudocode for the three functions, then the Python functions `Factorial(N)`, `SumDigits(N)` and `Reverse(Text)`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：每个函数都先写基本情况（`IF N = 0 THEN RETURN 1`、`IF N < 10 THEN RETURN N`、`IF LENGTH(Text) = 0 THEN RETURN ""`），再写一般情况。
- [ ] 伪代码：一般情况是 `RETURN N * Factorial(N - 1)`、`RETURN (N MOD 10) + SumDigits(N DIV 10)`、`RETURN Reverse(RIGHT(Text, LENGTH(Text) - 1)) & LEFT(Text, 1)` 这类写法；函数调用在表达式里，没有 `CALL`。
- [ ] 能说出每个函数的递归调用为什么一定会到达基本情况。
- [ ] 能把 `Factorial` 改写成迭代版本，并说出两者在内存上的区别（卡片 §2）。

## 出处

自编。依据：考纲 19.2（p.37）；插页 9618_w25_in_21 p.2（LENGTH、LEFT、RIGHT）、p.4（DIV、MOD）。
