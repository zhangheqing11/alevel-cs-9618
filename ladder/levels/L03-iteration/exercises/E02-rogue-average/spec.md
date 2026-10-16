# L03/E02 · 哨兵值求平均：WHILE + 预读

| 属性 | 值 |
|:--|:--|
| id | `L03/E02` |
| 目录 | `ladder/levels/L03-iteration/exercises/E02-rogue-average/` |
| 形态 | `io`（见 `ladder/design.md` §7.2） |
| entry | `rogue_average` |
| pseudocode | `true` |
| files | `[]` |
| skills | `sentinel-loop`, `pre-condition-loop`, `accumulator`, `output-format`, `input-prompt` |
| difficulty | 3 |
| title | `Count, total and average until a rogue value` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L03 card §2、§4、§5；常见坑 6、7 |

## 练习目标

写出标准的哨兵值循环：循环前预读、`WHILE` 不是哨兵就处理、循环体末尾再读；计数器与累加器在循环前初始化；处理「一个数据都没有」的情况，避免除以零。

## 题面

### 中文导读

一个一个地输入整数，输入 `-1` 表示结束（`-1` 本身不算数据；其他负数照常算）。输出个数、总和、平均值（1 位小数）。如果第一个就输入 `-1`，只输出一行 `No data`。伪代码必须用 `WHILE` 循环（想一想：为什么这里不适合用 `REPEAT`？）。

### English task

Write a procedure `RogueAverage()` that repeatedly prompts for and inputs integers until the rogue value `-1` is input. The rogue value is not part of the data; any other integer, including other negative numbers, is.

After the rogue value, output three lines:

```text
Count: 3
Total: 30
Average: 10.0
```

The average is output to one decimal place. If the first value input is `-1`, output the single line `No data` instead.

Use a pre-condition (`WHILE`) loop. Then write the Python procedure `rogue_average()`.

## 接口

```python
def rogue_average() -> None:
    """Input integers until -1; print Count/Total/Average (1 dp), or 'No data'."""
    raise NotImplementedError


if __name__ == "__main__":
    rogue_average()
```

`answer.pseudo` 模板：

```pseudocode
PROCEDURE RogueAverage()
   // use a WHILE loop: input the first value before the loop

ENDPROCEDURE
```

## 必测行为

每个测试喂入的行数恰好等于正确程序需要读的行数（最后一行总是 `-1`）。

| # | 输入（按顺序） | 期望输出行 | 说明 |
|:--|:--|:--|:--|
| B1 | `5`、`10`、`15`、`-1` | `Count: 3`、`Total: 30`、`Average: 10.0` | 普通情况 |
| B2 | `-1` | `No data` | 零个数据（边界）；不能除以零 |
| B3 | `0`、`-1` | `Count: 1`、`Total: 0`、`Average: 0.0` | 0 是合法数据 |
| B4 | `-5`、`5`、`-1` | `Count: 2`、`Total: 0`、`Average: 0.0` | 别的负数也是数据 |
| B5 | `7`、`8`、`-1` | `Count: 2`、`Total: 15`、`Average: 7.5` | 平均值有小数 |
| B6 | `1`、`2`、`2`、`-1` | `Count: 3`、`Total: 5`、`Average: 1.7` | 1.666… 显示为 1.7 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 先加再判断（或判断前已经计数），把 `-1` 也算进去：B1 得 `Count: 4`、`Total: 29`；B2 得 `Count: 1` 而不是 `No data` | B1–B6 |
| M2 | 结束条件写成 `while number > 0`：B3 输出 `No data`，B4 输出 `No data` | B3、B4 |
| M3 | 没有零数据的判断，B2 抛 `ZeroDivisionError` | B2 |

（M1 的参考写法：`while True: number = int(input()); count += 1; total += number; if number == -1: break`，不会死循环。）

## 人工核对清单

- [ ] 伪代码：循环前有一次 `INPUT`（预读），循环体末尾再 `INPUT`；条件是 `WHILE Number <> -1`（指南 p.21）。
- [ ] 伪代码：`Count ← 0`、`Total ← 0` 在循环之前；`Average` 声明为 `REAL`。
- [ ] 伪代码：零数据时用 `IF Count = 0 THEN … ELSE … ENDIF` 避免除以零。
- [ ] 每个 `INPUT` 前都有提示语，提示里说明 `-1` 结束。
- [ ] 能回答：为什么这里用 `WHILE` 而不用 `REPEAT`（第一个输入就可能是哨兵值，循环体可能一次都不执行）。

## 出处

自编。语法依据：指南 p.21（WHILE）、p.15（INPUT、OUTPUT、`/`）、p.18（IF）。
