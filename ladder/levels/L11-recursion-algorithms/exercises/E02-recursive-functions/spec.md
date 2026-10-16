# L11/E02 · 递归函数：阶乘、数位和、字符串反转

| 属性 | 值 |
|:--|:--|
| id | `L11/E02` |
| 目录 | `ladder/levels/L11-recursion-algorithms/exercises/E02-recursive-functions/` |
| 形态 | `function`（三个函数；测试检查结果，并用计数包装检查确实递归） |
| entry | `Factorial`（同一文件还有 `SumDigits`、`Reverse`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `recursion`, `return-value`, `div-mod`, `string-functions`, `boundary-values` |
| difficulty | 3 |
| title | `Recursive functions: factorial, digit sum, reverse a string` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L11 card §1、§2 |

## 练习目标

为三个问题各找出基本情况与「更小的问题」，写成递归函数；体会递归函数必须**返回**递归调用的结果。

## 题面

### 中文导读

三个函数都必须递归（函数里用自己的名字调用自己，不用循环）：`Factorial(N)` 返回 N!（N ≥ 0，0! = 1）；`SumDigits(N)` 返回非负整数 N 的各位数字之和（用 `DIV`/`MOD`）；`Reverse(Text)` 返回字符串倒过来的结果（空串的反转是空串）。

### English task

Write three recursive functions. Each must call itself; do not use loops.

- `Factorial()` takes an integer `N` (0 or more) and returns N! (0! is 1).
- `SumDigits()` takes an integer `N` (0 or more) and returns the sum of its digits. Use `DIV` and `MOD`.
- `Reverse()` takes a string `Text` and returns the characters of `Text` in reverse order. The reverse of the empty string is the empty string.

Write pseudocode for the three functions, then the Python functions `Factorial(N)`, `SumDigits(N)` and `Reverse(Text)`.

## 接口

```python
def Factorial(N: int) -> int:
    """Return N! recursively (N >= 0)."""
    raise NotImplementedError


def SumDigits(N: int) -> int:
    """Return the sum of the digits of N recursively (N >= 0)."""
    raise NotImplementedError


def Reverse(Text: str) -> str:
    """Return Text reversed, recursively."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION Factorial(N : INTEGER) RETURNS INTEGER

ENDFUNCTION

FUNCTION SumDigits(N : INTEGER) RETURNS INTEGER
   // use DIV and MOD

ENDFUNCTION

FUNCTION Reverse(Text : STRING) RETURNS STRING
   // use LENGTH(), LEFT(), RIGHT() or MID()

ENDFUNCTION
```

## 必测行为

递归检查的写法同 E01 的 B5：把模块里的函数换成计数包装，调用后计数应 ≥ 2。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `Factorial(0)`、`Factorial(1)` | `1`、`1` | 基本情况（边界） |
| B2 | `Factorial(5)`、`Factorial(10)` | `120`、`3628800` | |
| B3 | `SumDigits(0)`、`SumDigits(7)` | `0`、`7` | 一位数（边界） |
| B4 | `SumDigits(1234)`、`SumDigits(9999)`、`SumDigits(1000)` | `10`、`36`、`1` | |
| B5 | `Reverse("")`、`Reverse("a")` | `""`、`"a"` | 边界 |
| B6 | `Reverse("abc")`、`Reverse("Hello")`、`Reverse("racecar")` | `"cba"`、`"olleH"`、`"racecar"` | |
| B7 | 递归检查：`Factorial(5)`、`SumDigits(1234)`、`Reverse("abc")` | 三者的计数包装都被调用 ≥ 2 次 | 确实递归 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `Factorial` 的基本情况只写 `N = 1`：`Factorial(0)` 一直递归下去，抛 `RecursionError` | B1 |
| M2 | `SumDigits` 写成 `while` 循环（结果正确） | B7 |
| M3 | `Reverse` 把顺序拼反：`Text[0] + Reverse(Text[1:])`，`"abc"` 得 `"abc"` | B6 |

（M1 不会卡住 `make check`：Python 在约 1000 层时抛 `RecursionError`。）

## 人工核对清单

- [ ] 伪代码：每个函数都先写基本情况（`IF N = 0 THEN RETURN 1`、`IF N < 10 THEN RETURN N`、`IF LENGTH(Text) = 0 THEN RETURN ""`），再写一般情况。
- [ ] 伪代码：一般情况是 `RETURN N * Factorial(N - 1)`、`RETURN (N MOD 10) + SumDigits(N DIV 10)`、`RETURN Reverse(RIGHT(Text, LENGTH(Text) - 1)) & LEFT(Text, 1)` 这类写法；函数调用在表达式里，没有 `CALL`。
- [ ] 能说出每个函数的递归调用为什么一定会到达基本情况。
- [ ] 能把 `Factorial` 改写成迭代版本，并说出两者在内存上的区别（卡片 §2）。

## 出处

自编。依据：考纲 19.2（p.37）；插页 9618_w25_in_21 p.2（LENGTH、LEFT、RIGHT）、p.4（DIV、MOD）。
