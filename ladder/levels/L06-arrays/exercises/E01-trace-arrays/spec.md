# L06/E01 · 干跑：数组初始化、右移、复制与二维下标

| 属性 | 值 |
|:--|:--|
| id | `L06/E01` |
| 目录 | `ladder/levels/L06-arrays/exercises/E01-trace-arrays/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2） |
| entry | `run_trace` |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `array-index`, `array-copy`, `array-2d`, `loop-step` |
| difficulty | 3 |
| title | `Dry run: array initialisation, shifting, copying and 2D indexes` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L06 card §1、§2、§3 |

## 练习目标

精确执行数组操作：用循环初始化；把元素整体右移一位（倒着移）；整个数组赋值（伪代码是复制）；二维数组的行列下标。再译成 Python：下标减 1、二维用 `g[r][c]`、复制要真复制。

## 题面

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

## 接口

```python
PREDICTED: list[str] = []  # fill in by hand BEFORE writing run_trace()


def run_trace() -> None:
    """Translate the pseudocode; print exactly what OUTPUT displays."""
    raise NotImplementedError


if __name__ == "__main__":
    run_trace()
```

（不需要 `answer.pseudo`。）

## 必测行为

期望输出（共 4 行，已用参考实现核对）：

```text
4 25
0 1 16
4 99
23 12
```

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED` | 恰好等于上面 4 个字符串组成的列表 |
| B2 | `run_trace()` 输出的第 2 行 | `"0 1 16"`（从后往前移，元素没有被覆盖） |
| B3 | 第 3 行 | `"4 99"`（`Copy` 是复制，不跟着 `Nums` 变） |
| B4 | 第 4 行 | `"23 12"`（二维数组两行互不影响） |
| B5 | `run_trace()` 全部输出行 | 与上面 4 行逐行完全相等 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | Python 里写 `copy = nums`（起别名）：第 3 行变成 `99 99`；`PREDICTED` 写对 | B3、B5 |
| M2 | 右移时从前往后移（`for i in range(1, 5): nums[i] = nums[i - 1]`），覆盖成 `0 1 1`；`PREDICTED` 也照此写 | B1、B2、B5 |
| M3 | 二维 list 写成 `[[0] * 3] * 2`：两行是同一个 list，第 4 行变成 `23 22`；`PREDICTED` 写对 | B4、B5 |

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能说出为什么右移要从 4 往 1 倒着做。
- [ ] 能说出 `Copy ← Nums` 在伪代码里的含义（指南 p.11：同大小同类型的整个数组可以赋值），以及 Python 里要写 `nums[:]`、`list(nums)` 或 `nums.copy()`。
- [ ] 能把 `Grid[2, 3]` 写成 Python 的 `grid[1][2]`，并说出为什么不能写 `grid[1, 2]`。

## 出处

自编。语法依据：指南 p.10（数组声明、`A[n+1] ← A[n]`、二维下标）、p.11（整个数组赋值；用循环逐个赋值）、p.20（FOR、STEP）。
