# L05/E02 · 干跑：插页字符串函数

| 属性 | 值 |
|:--|:--|
| id | `L05/E02` |
| 目录 | `ladder/levels/L05-strings/exercises/E02-trace-strings/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2） |
| entry | `run_trace` |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `string-functions`, `string-index`, `loop-step` |
| difficulty | 2 |
| title | `Dry run: insert string functions` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L05 card §1、§2、§3、§4 |

## 练习目标

准确读出 `LEFT`/`RIGHT`/`MID`/`LENGTH`/`TO_UPPER`/`ASC`/`CHR`/`NUM_TO_STR` 的结果；读懂倒序、隔一个取字符的循环；把它们译成 Python 切片与内置函数。

## 题面

### 中文导读

这段伪代码会输出 8 行。先手算填 `PREDICTED`，再译成 Python 的 `run_trace()`。可以在 `solution.py` 里先写好上一题的 `left`/`right`/`mid` 再调用它们，也可以直接写切片。

### English task

Dry-run the pseudocode below and store each line it outputs, in order, in the list `PREDICTED`. Then translate it into the Python function `run_trace()`, which must print exactly the same lines.

```pseudocode
DECLARE Word : STRING
DECLARE Result : STRING
DECLARE Index : INTEGER
Word ← "Computer"
OUTPUT LENGTH(Word)
OUTPUT LEFT(Word, 3) & RIGHT(Word, 3)
OUTPUT MID(Word, 4, 2)
OUTPUT TO_UPPER(Word)
Result ← ""
FOR Index ← LENGTH(Word) TO 1 STEP -2
   Result ← Result & MID(Word, Index, 1)
NEXT Index
OUTPUT Result
OUTPUT ASC('C') - ASC('A')
OUTPUT CHR(ASC(MID(Word, 2, 1)) + 1)
OUTPUT NUM_TO_STR(LENGTH(Word) * 2) & "!"
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

期望输出（共 8 行，已用参考实现核对）：

```text
8
Comter
pu
COMPUTER
rtpo
2
p
16!
```

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED` | 恰好等于上面 8 个字符串组成的列表 |
| B2 | `run_trace()` 输出的第 2 行 | `"Comter"`（`&` 不加空格） |
| B3 | 第 3 行 | `"pu"`（从第 4 个字符起取 2 个） |
| B4 | 第 5 行 | `"rtpo"`（位置 8、6、4、2） |
| B5 | 第 7 行 | `"p"`（`'o'` 的下一个字符） |
| B6 | `run_trace()` 全部输出行 | 与上面 8 行逐行完全相等 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `MID(Word, 4, 2)` 译成 `word[4:6]`（没减 1），输出 `ut`；`PREDICTED` 写对 | B3、B6 |
| M2 | 循环里写 `word[index]`、`range(8, 0, -2)`：第一次就 `word[8]` 抛 `IndexError` | B4、B6 |
| M3 | 第 2 行写成 `print(word[:3], word[-3:])`，输出 `Com ter` | B2、B6 |

## 人工核对清单

- [ ] `PREDICTED` 是先手算的。
- [ ] 能说出 `FOR Index ← LENGTH(Word) TO 1 STEP -2` 依次取哪些位置，并写出对应的 `range`。
- [ ] 能说出 `ASC('C') - ASC('A')` 为什么是 2（字母在编码表里连续）。

## 出处

自编。函数依据：插页 9618_w25_in_21 p.2–3（LEFT、RIGHT、MID、LENGTH、TO_UPPER、NUM_TO_STR、ASC、CHR）；指南 p.20（STEP 负步长）。
