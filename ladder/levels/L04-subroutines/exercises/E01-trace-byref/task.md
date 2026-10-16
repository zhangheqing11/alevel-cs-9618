# L04/E01 · 干跑：BYVAL、BYREF 与函数调用


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能说出第 2 行为什么仍是 3、第 3 行为什么两个都变了。
- [ ] 能说出 `CALL AddOne(A)` 与 `A ← Twice(A) + Twice(1)` 的区别：过程调用是一条语句，函数调用是表达式的一部分（指南 p.22–23）。
- [ ] 能说出 Python 实现 BYREF 效果的三种办法（卡片 §4），并说明这里为什么选「返回元组」。

## 出处

自编。语法依据：指南 p.22（PROCEDURE、CALL、默认 BYVAL）、p.23（FUNCTION、RETURN）、p.24（BYREF、SWAP 例子）。
