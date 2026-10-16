# L04/E01 · 干跑：BYVAL、BYREF 与函数调用

| 属性 | 值 |
|:--|:--|
| id | `L04/E01` |
| 目录 | `ladder/levels/L04-subroutines/exercises/E01-trace-byref/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2）；另有三个辅助函数也要测 |
| entry | `run_trace`（同一文件还有 `add_one`、`swap`、`twice`） |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `byval-byref`, `return-value`, `procedure-call` |
| difficulty | 2 |
| title | `Dry run: BYVAL, BYREF and function calls` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L04 card §1、§2、§4 |

## 练习目标

读懂 BYVAL 与 BYREF 对调用者变量的不同影响；分清 `CALL` 过程与在表达式里调用函数；把 BYREF 过程译成「返回元组」的 Python 函数。

## 题面

### 中文导读

下面的程序会输出 4 行。先手算，把每行输出写进 `PREDICTED`。然后把它译成 Python：`AddOne` 译成 `add_one(n)`（打印一行、不返回值）；`Swap` 的 BYREF 效果用**返回元组**实现：`swap(x, y)` 返回 `(y, x)`，调用处写 `a, b = swap(a, b)`；`Twice` 译成 `twice(n)`。最后 `run_trace()` 按主程序的顺序执行并打印同样的 4 行。

### English task

Dry-run the program below and store each line it outputs, in order, in the list `PREDICTED`. Then translate it into Python:

- `add_one(n)` prints the line from `AddOne` and returns nothing
- `swap(x, y)` returns the two values swapped, as a tuple; the caller writes `a, b = swap(a, b)` to get the effect of `BYREF`
- `twice(n)` returns `n * 2`
- `run_trace()` runs the main program and prints exactly the same lines.

```pseudocode
DECLARE A : INTEGER
DECLARE B : INTEGER

PROCEDURE AddOne(BYVAL N : INTEGER)
   N ← N + 1
   OUTPUT "In AddOne: ", N
ENDPROCEDURE

PROCEDURE Swap(BYREF X : INTEGER, Y : INTEGER)
   DECLARE Temp : INTEGER
   Temp ← X
   X ← Y
   Y ← Temp
ENDPROCEDURE

FUNCTION Twice(N : INTEGER) RETURNS INTEGER
   RETURN N * 2
ENDFUNCTION

A ← 3
B ← 8
CALL AddOne(A)
OUTPUT "A: ", A
CALL Swap(A, B)
OUTPUT "A: ", A, " B: ", B
A ← Twice(A) + Twice(1)
OUTPUT "A: ", A
```

（`Swap` 的头里 `BYREF` 只写了一次：按指南 p.24，连续的同一传递方式不必重复，所以 `X`、`Y` 都是 BYREF。）

## 接口

```python
PREDICTED: list[str] = []  # fill in by hand BEFORE writing the functions


def add_one(n: int) -> None:
    """Print 'In AddOne: <n + 1>'. The caller's variable must not change (BYVAL)."""
    raise NotImplementedError


def swap(x: int, y: int) -> tuple[int, int]:
    """Return (y, x): Python's way of getting the effect of BYREF X, Y."""
    raise NotImplementedError


def twice(n: int) -> int:
    """Return n * 2."""
    raise NotImplementedError


def run_trace() -> None:
    """Run the main program: A = 3, B = 8, then the six statements in order."""
    raise NotImplementedError


if __name__ == "__main__":
    run_trace()
```

（不需要 `answer.pseudo`。）

## 必测行为

期望输出（共 4 行，已用参考实现核对）：

```text
In AddOne: 4
A: 3
A: 8 B: 3
A: 18
```

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED` | 恰好等于上面 4 个字符串组成的列表 |
| B2 | `run_trace()` 全部输出行（`output_lines`） | 与上面 4 行逐行完全相等 |
| B3 | `run_trace()` 输出的第 2 行 | `"A: 3"`（BYVAL：`AddOne` 改的是副本） |
| B4 | `run_trace()` 输出的第 3 行 | `"A: 8 B: 3"`（BYREF：两个变量都被交换） |
| B5 | `swap(1, 2)`、`swap(5, 5)` | `(2, 1)`、`(5, 5)` |
| B6 | `twice(5)`、`twice(0)`、`twice(-4)` | `10`、`0`、`-8` |
| B7 | `add_one(5)` | 输出恰好一行 `In AddOne: 6`；返回值是 `None` |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 把 BYVAL 当成 BYREF：`run_trace()` 里写 `a = a + 1` 再打印，得到 `A: 4`、`A: 8 B: 4`；`PREDICTED` 也这样写 | B1、B2、B3、B4 |
| M2 | 照抄 BYREF：`swap(x, y)` 在函数里交换局部变量后不返回（返回 `None`），`run_trace()` 里只写 `swap(a, b)`；输出 `A: 3 B: 8`、`A: 8` | B2、B4、B5 |
| M3 | `twice` 用 `print(n * 2)` 代替 `return`：`run_trace()` 计算 `twice(a) + twice(1)` 时抛 `TypeError` | B2、B6 |

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能说出第 2 行为什么仍是 3、第 3 行为什么两个都变了。
- [ ] 能说出 `CALL AddOne(A)` 与 `A ← Twice(A) + Twice(1)` 的区别：过程调用是一条语句，函数调用是表达式的一部分（指南 p.22–23）。
- [ ] 能说出 Python 实现 BYREF 效果的三种办法（卡片 §4），并说明这里为什么选「返回元组」。

## 出处

自编。语法依据：指南 p.22（PROCEDURE、CALL、默认 BYVAL）、p.23（FUNCTION、RETURN）、p.24（BYREF、SWAP 例子）。
