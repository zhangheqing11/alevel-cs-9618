# L04/E05 · 素数模块：在条件里调用函数


### 中文导读

写三个函数：`IsPrime(N)` 判断 N（≥ 0）是不是素数（0 和 1 不是）；`CountPrimes(Low, High)` 返回 Low 到 High（含两端）之间有几个素数，Low > High 时返回 0；`NextPrime(N)` 返回大于 N 的最小素数。后两个必须调用 `IsPrime()`。

### English task

Write pseudocode for three functions:

- `IsPrime()` takes an integer `N` (0 or more) and returns `TRUE` if `N` is a prime number, otherwise `FALSE`. 0 and 1 are not prime.
- `CountPrimes()` takes two integers `Low` and `High` and returns how many prime numbers there are from `Low` to `High` inclusive. It returns 0 if `Low` is greater than `High`.
- `NextPrime()` takes an integer `N` (0 or more) and returns the smallest prime number that is greater than `N`.

`CountPrimes()` and `NextPrime()` must use `IsPrime()`. Then write the Python functions `is_prime(n)`, `count_primes(low, high)` and `next_prime(n)`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`CountPrimes` 里写 `IF IsPrime(Number) = TRUE THEN`（或 `IF IsPrime(Number) THEN`）；`NextPrime` 里写 `WHILE IsPrime(Candidate) = FALSE`——**没有** `CALL IsPrime(…)`（ER s23 9618/22 Q8，p.18、p.22 点名）。
- [ ] 伪代码：每个函数都用 `RETURN` 交回结果，没有 `OUTPUT`（ER w25 p.15）。
- [ ] 伪代码：`IsPrime` 发现因数就立即 `RETURN FALSE` 也可以；用循环 + 标志也可以，但循环要能在找到因数后结束（不要用 FOR 套在 WHILE 里，ER w25 p.15）。
- [ ] 伪代码：局部变量（循环变量、计数器）都 `DECLARE`。
- [ ] Python：`count_primes`、`next_prime` 确实调用了 `is_prime`。

## 出处

自编。误区依据：ER s23 9618/22 Q8（p.18、p.22）；ER w25 9618/21（p.15）。语法依据：指南 p.23（FUNCTION、RETURN、函数只在表达式里调用）。
