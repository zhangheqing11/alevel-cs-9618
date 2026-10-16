# L03/E01 · 干跑：FOR、WHILE 与 REPEAT


### 中文导读

这段伪代码会输出 7 行。先手算，把每行输出按顺序写进 `PREDICTED`；再逐行译成 Python 的 `run_trace()`。特别注意：`FOR` 的终点**包含在内**；第五个 `FOR` 一次都不执行；`REPEAT` 不管条件如何先执行一次。

### English task

Dry-run the pseudocode below. Write the exact text of each line it outputs, in order, as strings in the list `PREDICTED`. Then translate it line by line into the Python function `run_trace()`, which must print exactly the same lines.

```pseudocode
DECLARE Count : INTEGER
DECLARE Total : INTEGER
DECLARE N : INTEGER
Total ← 0
FOR Count ← 1 TO 10 STEP 3
   Total ← Total + Count
NEXT Count
OUTPUT "A: ", Total
N ← 50
WHILE N > 9
   N ← N - 9
ENDWHILE
OUTPUT "B: ", N
N ← 5
REPEAT
   N ← N * 2
UNTIL N > 3
OUTPUT "C: ", N
FOR Count ← 5 TO 1 STEP -2
   OUTPUT "D: ", Count
NEXT Count
FOR Count ← 3 TO 1
   OUTPUT "E: ", Count
NEXT Count
OUTPUT "F: done"
```

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

## 人工核对清单

- [ ] `PREDICTED` 是先手算的。
- [ ] 能说出 `WHILE N > 9` 那段为什么停在 5（50→41→32→23→14→5）。
- [ ] 能说出若把 `REPEAT` 段改成 `WHILE N <= 3 … ENDWHILE`，输出会变成什么（`C: 5`），并解释两种循环的区别。
- [ ] Python 的 `REPEAT` 译法是 `while True` + 末尾 `if n > 3: break`（或等价的标志写法），条件没有取反。

## 出处

自编。语法依据：指南 p.20（FOR、STEP、起点大于终点不执行）、p.20–21（REPEAT）、p.21（WHILE；`WHILE Number > 9` 例子）。
