# L03/E01 · 干跑：FOR、WHILE 与 REPEAT

| 属性 | 值 |
|:--|:--|
| id | `L03/E01` |
| 目录 | `ladder/levels/L03-iteration/exercises/E01-trace-loops/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2） |
| entry | `run_trace` |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `count-loop`, `loop-step`, `pre-condition-loop`, `post-condition-loop`, `loop-bounds` |
| difficulty | 2 |
| title | `Dry run: FOR with STEP, WHILE and REPEAT` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L03 card §1、§2、§3；常见坑 1、2、3 |

## 练习目标

精确执行五个小循环：含终点的 `FOR`、带 `STEP` 的 `FOR`、负步长、一次都不执行的 `FOR`、`WHILE`，以及「条件一开始就成立仍要执行一次」的 `REPEAT`。再把它们逐个译成 Python，验证 `range` 的写法和 `REPEAT` 的译法。

## 题面

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

## 接口

```python
PREDICTED: list[str] = []  # fill in by hand BEFORE writing run_trace()


def run_trace() -> None:
    """Translate the pseudocode line by line; print exactly what OUTPUT displays."""
    raise NotImplementedError


if __name__ == "__main__":
    run_trace()
```

（不需要 `answer.pseudo`。）

## 必测行为

期望输出（共 7 行，已用参考实现核对）：

```text
A: 22
B: 5
C: 10
D: 5
D: 3
D: 1
F: done
```

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED` | 恰好等于上面 7 个字符串组成的列表 |
| B2 | `run_trace()` 输出的第 1 行 | `"A: 22"`（1+4+7+10：终点 10 被取到） |
| B3 | 第 3 行 | `"C: 10"`（`REPEAT` 先执行一次，即使 `N > 3` 一开始就成立） |
| B4 | 以 `D:` 开头的行 | `"D: 5"`、`"D: 3"`、`"D: 1"` 三行（负步长含终点 1） |
| B5 | 输出里没有以 `E:` 开头的行 | （起点大于终点，循环不执行） |
| B6 | `run_trace()` 全部输出行 | 与上面 7 行逐行完全相等 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `range(1, 10, 3)` 漏了终点：`A: 12`；`PREDICTED` 同样写 `"A: 12"` | B1、B2、B6 |
| M2 | 把 `REPEAT … UNTIL N > 3` 译成 `while not n > 3:`（先判断），得 `C: 5`；`PREDICTED` 写对 | B3、B6 |
| M3 | 负步长终点写成 `range(5, 1, -2)`：只有 `D: 5`、`D: 3`；`PREDICTED` 写对 | B4、B6 |

## 人工核对清单

- [ ] `PREDICTED` 是先手算的。
- [ ] 能说出 `WHILE N > 9` 那段为什么停在 5（50→41→32→23→14→5）。
- [ ] 能说出若把 `REPEAT` 段改成 `WHILE N <= 3 … ENDWHILE`，输出会变成什么（`C: 5`），并解释两种循环的区别。
- [ ] Python 的 `REPEAT` 译法是 `while True` + 末尾 `if n > 3: break`（或等价的标志写法），条件没有取反。

## 出处

自编。语法依据：指南 p.20（FOR、STEP、起点大于终点不执行）、p.20–21（REPEAT）、p.21（WHILE；`WHILE Number > 9` 例子）。
