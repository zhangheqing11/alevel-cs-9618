# L04/E05 · 素数模块：在条件里调用函数

| 属性 | 值 |
|:--|:--|
| id | `L04/E05` |
| 目录 | `ladder/levels/L04-subroutines/exercises/E05-prime-modules/` |
| 形态 | `function`（三个函数） |
| entry | `is_prime`（同一文件还有 `count_primes`、`next_prime`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `module-header`, `boolean-return`, `procedure-call`, `boundary-values`, `pre-condition-loop` |
| difficulty | 3 |
| title | `Prime modules: calling a function inside a condition` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L04 card §2、§7；常见坑 1、2 |

## 练习目标

写一个返回 BOOLEAN 的函数，再在另外两个函数里**调用它**（放在 `IF` / `WHILE` 的条件里），不重写它的算法、不对函数写 `CALL`。

## 题面

### 中文导读

写三个函数：`IsPrime(N)` 判断 N（≥ 0）是不是素数（0 和 1 不是）；`CountPrimes(Low, High)` 返回 Low 到 High（含两端）之间有几个素数，Low > High 时返回 0；`NextPrime(N)` 返回大于 N 的最小素数。后两个必须调用 `IsPrime()`。

### English task

Write pseudocode for three functions:

- `IsPrime()` takes an integer `N` (0 or more) and returns `TRUE` if `N` is a prime number, otherwise `FALSE`. 0 and 1 are not prime.
- `CountPrimes()` takes two integers `Low` and `High` and returns how many prime numbers there are from `Low` to `High` inclusive. It returns 0 if `Low` is greater than `High`.
- `NextPrime()` takes an integer `N` (0 or more) and returns the smallest prime number that is greater than `N`.

`CountPrimes()` and `NextPrime()` must use `IsPrime()`. Then write the Python functions `is_prime(n)`, `count_primes(low, high)` and `next_prime(n)`.

## 接口

```python
def is_prime(n: int) -> bool:
    """Return True if n (>= 0) is prime; 0 and 1 are not prime."""
    raise NotImplementedError


def count_primes(low: int, high: int) -> int:
    """Return how many primes are in low..high inclusive (0 if low > high). Use is_prime()."""
    raise NotImplementedError


def next_prime(n: int) -> int:
    """Return the smallest prime greater than n. Use is_prime()."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION IsPrime(N : INTEGER) RETURNS BOOLEAN

ENDFUNCTION

FUNCTION CountPrimes(Low : INTEGER, High : INTEGER) RETURNS INTEGER
   // must use IsPrime()

ENDFUNCTION

FUNCTION NextPrime(N : INTEGER) RETURNS INTEGER
   // must use IsPrime()

ENDFUNCTION
```

## 必测行为

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `is_prime(0)`、`is_prime(1)` | `False`、`False` | 边界：不是素数 |
| B2 | `is_prime(2)`、`is_prime(3)` | `True`、`True` | 最小的素数 |
| B3 | `is_prime(4)`、`is_prime(9)`、`is_prime(25)` | `False`、`False`、`False` | 平方数 |
| B4 | `is_prime(97)` | `True` | |
| B5 | `count_primes(1, 10)`、`count_primes(1, 100)` | `4`、`25` | |
| B6 | `count_primes(2, 2)`、`count_primes(14, 16)`、`count_primes(10, 1)` | `1`、`0`、`0` | 两端都包含；没有素数；Low > High |
| B7 | `next_prime(0)`、`next_prime(1)`、`next_prime(2)` | `2`、`2`、`3` | 「大于」不含 N 本身 |
| B8 | `next_prime(13)`、`next_prime(97)` | `17`、`101` | |
| B9 | 返回类型 | `is_prime` 返回 `bool`；另外两个返回 `int` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `is_prime` 只写 `for i in range(2, n): if n % i == 0: return False` 后 `return True`，没有处理 0 和 1：两者都返回 `True` | B1、B5、B7 |
| M2 | `count_primes` 用 `range(low, high)`，不含 High：`count_primes(2, 2)` 返回 0 | B6 |
| M3 | `next_prime` 从 N 本身开始找：`next_prime(2)` 返回 2、`next_prime(13)` 返回 13 | B7、B8 |

（T10 已用参考实现核对：M1 下 `count_primes(1, 10)` 为 5，`next_prime(0)` 为 1。）

## 人工核对清单

- [ ] 伪代码：`CountPrimes` 里写 `IF IsPrime(Number) = TRUE THEN`（或 `IF IsPrime(Number) THEN`）；`NextPrime` 里写 `WHILE IsPrime(Candidate) = FALSE`——**没有** `CALL IsPrime(…)`（ER s23 9618/22 Q8，p.18、p.22 点名）。
- [ ] 伪代码：每个函数都用 `RETURN` 交回结果，没有 `OUTPUT`（ER w25 p.15）。
- [ ] 伪代码：`IsPrime` 发现因数就立即 `RETURN FALSE` 也可以；用循环 + 标志也可以，但循环要能在找到因数后结束（不要用 FOR 套在 WHILE 里，ER w25 p.15）。
- [ ] 伪代码：局部变量（循环变量、计数器）都 `DECLARE`。
- [ ] Python：`count_primes`、`next_prime` 确实调用了 `is_prime`。

## 出处

自编。误区依据：ER s23 9618/22 Q8（p.18、p.22）；ER w25 9618/21（p.15）。语法依据：指南 p.23（FUNCTION、RETURN、函数只在表达式里调用）。
