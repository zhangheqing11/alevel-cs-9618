# L03/E06 · 数位：选 REPEAT 还是 WHILE


### 中文导读

写两个函数，参数都是非负整数：`CountDigits` 返回它有几位（`0` 有 1 位，`100` 有 3 位）；`DigitSum` 返回各位数字之和（`1234` 的和是 10）。只能用 `DIV` 和 `MOD`，不能把数转成字符串。`CountDigits` 用 `REPEAT` 写，`DigitSum` 用 `WHILE` 写。最后在 `answer.pseudo` 末尾用注释回答：如果 `CountDigits` 改用 `WHILE Number > 0`，`CountDigits(0)` 会返回什么？为什么？

### English task

1. Write a function `CountDigits()` that takes a non-negative integer and returns the number of digits it has. For example, `CountDigits(0)` returns 1 and `CountDigits(100)` returns 3. Use a post-condition loop with `DIV`.
2. Write a function `DigitSum()` that takes a non-negative integer and returns the sum of its digits. For example, `DigitSum(1234)` returns 10. Use a pre-condition loop with `DIV` and `MOD`.
3. In a comment, explain what `CountDigits(0)` would return if it used `WHILE Number > 0` instead, and why.

Do not convert the number to a string. Then write the Python functions `count_digits(number)` and `digit_sum(number)`.

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

## 人工核对清单

- [ ] 伪代码：`CountDigits` 用 `REPEAT … UNTIL Number = 0`，`DigitSum` 用 `WHILE Number > 0 … ENDWHILE`（指南 p.20–21）。
- [ ] 伪代码：只用 `DIV`、`MOD`，没有 `/`，没有字符串函数；计数器、累加器先初始化；以 `RETURN` 返回、`ENDFUNCTION` 结束。
- [ ] 注释回答正确：`WHILE Number > 0` 时循环一次都不执行，`CountDigits(0)` 返回 0，而 0 实际有 1 位——这正是「至少执行一次」用 `REPEAT` 的理由。
- [ ] 加练（口头或注释）：把 `DigitSum` 改写成 `REPEAT` 版本，并说出要额外处理什么（0 的情况仍正确，但要确认循环条件）。
- [ ] Python：`count_digits` 用 `while True` + `break`；`digit_sum` 用 `while number > 0`；整除用 `//`。

## 出处

自编。语法依据：指南 p.15（DIV、MOD）、p.20–21（REPEAT、WHILE）、p.23（FUNCTION）。活动依据：SoW Unit 11 p.36（循环互改）；考纲 11.2「justify why one loop structure may be better suited」（考纲 p.29）。
