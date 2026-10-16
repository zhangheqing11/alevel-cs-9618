# L06/E01 · 干跑：数组初始化、右移、复制与二维下标


### 中文导读

这段伪代码会输出 4 行。先手算填 `PREDICTED`，再译成 Python 的 `run_trace()`。注意两处 Python 与伪代码行为不同的地方：`Copy ← Nums` 在伪代码里是复制；二维数组在 Python 里要逐行新建。

### English task

Dry-run the pseudocode below and store each line it outputs, in order, in the list `PREDICTED`. Then translate it into the Python function `run_trace()`, which must print exactly the same lines. Use Python lists with indexes starting at 0.

```pseudocode
DECLARE Nums : ARRAY[1:5] OF INTEGER
DECLARE Copy : ARRAY[1:5] OF INTEGER
DECLARE Grid : ARRAY[1:2,1:3] OF INTEGER
DECLARE Index : INTEGER
DECLARE Row : INTEGER
DECLARE Column : INTEGER
FOR Index ← 1 TO 5
   Nums[Index] ← Index * Index
NEXT Index
OUTPUT Nums[2], " ", Nums[5]
FOR Index ← 4 TO 1 STEP -1
   Nums[Index + 1] ← Nums[Index]
NEXT Index
Nums[1] ← 0
OUTPUT Nums[1], " ", Nums[2], " ", Nums[5]
Copy ← Nums
Nums[3] ← 99
OUTPUT Copy[3], " ", Nums[3]
FOR Row ← 1 TO 2
   FOR Column ← 1 TO 3
      Grid[Row, Column] ← Row * 10 + Column
   NEXT Column
NEXT Row
OUTPUT Grid[2, 3], " ", Grid[1, 2]
```

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能说出为什么右移要从 4 往 1 倒着做。
- [ ] 能说出 `Copy ← Nums` 在伪代码里的含义（指南 p.11：同大小同类型的整个数组可以赋值），以及 Python 里要写 `nums[:]`、`list(nums)` 或 `nums.copy()`。
- [ ] 能把 `Grid[2, 3]` 写成 Python 的 `grid[1][2]`，并说出为什么不能写 `grid[1, 2]`。

## 出处

自编。语法依据：指南 p.10（数组声明、`A[n+1] ← A[n]`、二维下标）、p.11（整个数组赋值；用循环逐个赋值）、p.20（FOR、STEP）。
