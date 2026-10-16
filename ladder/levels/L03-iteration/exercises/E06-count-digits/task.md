# L03/E06 · 数位：选 REPEAT 还是 WHILE

| 属性 | 值 |
|:--|:--|
| id | `L03/E06` |
| 目录 | `ladder/levels/L03-iteration/exercises/E06-count-digits/` |
| 形态 | `function`（两个函数；见 `ladder/design.md` §7.2） |
| entry | `count_digits`（同一文件还有 `digit_sum`，两个都测） |
| pseudocode | `true` |
| files | `[]` |
| skills | `loop-choice`, `post-condition-loop`, `pre-condition-loop`, `div-mod`, `return-value` |
| difficulty | 3 |
| title | `Count and sum the digits of a number: choosing a loop` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L03 card §2、§3、§4、§6；L01 card §5 |

## 练习目标

用 `DIV 10` / `MOD 10` 逐位拆数；体会循环选择的后果：数「位数」时 0 也有 1 位，所以至少要执行一次（`REPEAT`）；求「数位和」时 0 的和为 0，用 `WHILE` 自然。再把其中一个改写成另一种循环（P2 常考的改写题）。

## 题面

### 中文导读

写两个函数，参数都是非负整数：`CountDigits` 返回它有几位（`0` 有 1 位，`100` 有 3 位）；`DigitSum` 返回各位数字之和（`1234` 的和是 10）。只能用 `DIV` 和 `MOD`，不能把数转成字符串。`CountDigits` 用 `REPEAT` 写，`DigitSum` 用 `WHILE` 写。最后在 `answer.pseudo` 末尾用注释回答：如果 `CountDigits` 改用 `WHILE Number > 0`，`CountDigits(0)` 会返回什么？为什么？

### English task

1. Write a function `CountDigits()` that takes a non-negative integer and returns the number of digits it has. For example, `CountDigits(0)` returns 1 and `CountDigits(100)` returns 3. Use a post-condition loop with `DIV`.
2. Write a function `DigitSum()` that takes a non-negative integer and returns the sum of its digits. For example, `DigitSum(1234)` returns 10. Use a pre-condition loop with `DIV` and `MOD`.
3. In a comment, explain what `CountDigits(0)` would return if it used `WHILE Number > 0` instead, and why.

Do not convert the number to a string. Then write the Python functions `count_digits(number)` and `digit_sum(number)`.

## 接口

```python
def count_digits(number: int) -> int:
    """Return how many digits the non-negative integer has (0 has 1 digit)."""
    raise NotImplementedError


def digit_sum(number: int) -> int:
    """Return the sum of the digits of the non-negative integer."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION CountDigits(Number : INTEGER) RETURNS INTEGER
   // use a REPEAT ... UNTIL loop and DIV

ENDFUNCTION

FUNCTION DigitSum(Number : INTEGER) RETURNS INTEGER
   // use a WHILE loop, DIV and MOD

ENDFUNCTION

// What would CountDigits(0) return with WHILE Number > 0, and why?
//
```

## 必测行为

| # | 调用 | 期望返回 | 说明 |
|:--|:--|:--|:--|
| B1 | `count_digits(0)` | `1` | 0 有 1 位（边界；决定循环类型） |
| B2 | `count_digits(7)`、`count_digits(10)` | `1`、`2` | 一位数；刚进位 |
| B3 | `count_digits(99)`、`count_digits(100)` | `2`、`3` | 进位边界 |
| B4 | `count_digits(123456)`、`count_digits(1000000)` | `6`、`7` | 大数 |
| B5 | `digit_sum(0)`、`digit_sum(5)` | `0`、`5` | 边界：0 与一位数 |
| B6 | `digit_sum(1234)`、`digit_sum(9999)` | `10`、`36` | 普通值 |
| B7 | `digit_sum(1000)`、`digit_sum(908)` | `1`、`17` | 含 0 的数位 |
| B8 | 两个函数的返回类型 | `int` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `count_digits` 用 `while number > 0:`，0 返回 `0`（其余正确） | B1 |
| M2 | `digit_sum` 用 `while number > 9:`（照搬指南 p.21 的 `WHILE Number > 9`），漏掉最高位：1234 返回 9，5 返回 0 | B5、B6、B7 |
| M3 | `count_digits` 计数器从 1 开始又在循环里先加 1：7 返回 2 | B1–B4 |

（三个 mutant 都不会死循环：M1、M3 每轮都 `number //= 10`。）

## 人工核对清单

- [ ] 伪代码：`CountDigits` 用 `REPEAT … UNTIL Number = 0`，`DigitSum` 用 `WHILE Number > 0 … ENDWHILE`（指南 p.20–21）。
- [ ] 伪代码：只用 `DIV`、`MOD`，没有 `/`，没有字符串函数；计数器、累加器先初始化；以 `RETURN` 返回、`ENDFUNCTION` 结束。
- [ ] 注释回答正确：`WHILE Number > 0` 时循环一次都不执行，`CountDigits(0)` 返回 0，而 0 实际有 1 位——这正是「至少执行一次」用 `REPEAT` 的理由。
- [ ] 加练（口头或注释）：把 `DigitSum` 改写成 `REPEAT` 版本，并说出要额外处理什么（0 的情况仍正确，但要确认循环条件）。
- [ ] Python：`count_digits` 用 `while True` + `break`；`digit_sum` 用 `while number > 0`；整除用 `//`。

## 出处

自编。语法依据：指南 p.15（DIV、MOD）、p.20–21（REPEAT、WHILE）、p.23（FUNCTION）。活动依据：SoW Unit 11 p.36（循环互改）；考纲 11.2「justify why one loop structure may be better suited」（考纲 p.29）。
