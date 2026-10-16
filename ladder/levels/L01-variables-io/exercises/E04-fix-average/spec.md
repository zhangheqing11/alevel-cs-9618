# L01/E04 · 改错：三个分数的总分与平均分

| 属性 | 值 |
|:--|:--|
| id | `L01/E04` |
| 目录 | `ladder/levels/L01-variables-io/exercises/E04-fix-average/` |
| 形态 | `io`（见 `ladder/design.md` §7.2） |
| entry | `mark_summary` |
| pseudocode | `true` |
| files | `[]` |
| skills | `find-fix-errors`, `operator-precedence`, `declare-constant`, `output-format`, `type-conversion` |
| difficulty | 2 |
| title | `Find and correct the errors: total and average of three marks` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L01 card §3、§4、§5；常见坑 2、4、6 |

## 练习目标

练 P2 的「找出并改正错误」题：在一段有 4 处错误的伪代码里找出错误、写出改正后的完整过程；再写出行为正确的 Python。错误类型取自 ECR P2 2024 p.10 的考官点评（求平均漏括号、OUTPUT 缺分隔符）以及 CONSTANT、数据类型两类基础错误。

## 题面

### 中文导读

下面的过程 `MarkSummary()` 想输入三个整数分数，输出总分和平均分，但写错了 4 处（每处错误在不同的行）。在 `answer.pseudo` 里：先用注释列出每处错误的行号、错在哪、改成什么；再写出改正后的完整过程。最后在 `solution.py` 里写行为正确的 Python 版 `mark_summary()`：平均分保留 1 位小数。

### English task

The procedure `MarkSummary()` should input three integer marks and output their total and their average. The pseudocode contains **four** errors, each on a different line.

1. In `answer.pseudo`, list each error as a comment: the line number, the error, and the correction. Then write the corrected procedure in full.
2. Write the Python procedure `mark_summary()`. It inputs three integer marks (one per line) and prints:

```text
Total: 215
Average: 71.7
```

The average is printed to one decimal place.

```pseudocode
01 PROCEDURE MarkSummary()
02    DECLARE Mark1 : INTEGER
03    DECLARE Mark2 : INTEGER
04    DECLARE Mark3 : INTEGER
05    DECLARE Total : INTEGER
06    DECLARE Average : INTEGER
07    CONSTANT Count ← 3
08    OUTPUT "Enter three marks"
09    INPUT Mark1
10    INPUT Mark2
11    INPUT Mark3
12    Total ← Mark1 + Mark2 + Mark3
13    Average ← Mark1 + Mark2 + Mark3 / Count
14    OUTPUT "Total: " Total
15    OUTPUT "Average: ", Average
16 ENDPROCEDURE
```

（行号按指南 §1.4（p.6）的方式写在左侧，不属于伪代码本身。）

参考答案（**只给导师与 T14 用，不写进 `task.md`**）：

| 行 | 错误 | 改正 |
|:--|:--|:--|
| 06 | 平均分不一定是整数，`Average` 不能是 `INTEGER` | `DECLARE Average : REAL` |
| 07 | 常量用 `=` 定义（指南 p.8） | `CONSTANT Count = 3` |
| 13 | 只有 `Mark3` 被除；缺括号（也可直接用 `Total`） | `Average ← Total / Count` 或 `Average ← (Mark1 + Mark2 + Mark3) / Count` |
| 14 | `OUTPUT` 的多个值之间缺逗号分隔（指南 p.15） | `OUTPUT "Total: ", Total` |

## 接口

```python
def mark_summary() -> None:
    """Input three integer marks; print 'Total: <t>' and 'Average: <a to 1 dp>'."""
    raise NotImplementedError


if __name__ == "__main__":
    mark_summary()
```

`answer.pseudo` 模板：

```pseudocode
// Errors found (line number, error, correction):
// Line __ :
// Line __ :
// Line __ :
// Line __ :

PROCEDURE MarkSummary()
   // write the corrected procedure here

ENDPROCEDURE
```

## 必测行为

每个测试按顺序喂 3 行输入。期望输出恰好 2 行。

| # | 输入 | 期望输出行 | 说明 |
|:--|:--|:--|:--|
| B1 | `60`、`70`、`85` | `Total: 215`、`Average: 71.7` | 普通值（71.666… → 71.7） |
| B2 | `0`、`0`、`0` | `Total: 0`、`Average: 0.0` | 全零（边界） |
| B3 | `100`、`100`、`99` | `Total: 299`、`Average: 99.7` | 接近满分 |
| B4 | `1`、`2`、`2` | `Total: 5`、`Average: 1.7` | 1.666… 显示为 1.7 |
| B5 | `50`、`50`、`51` | `Total: 151`、`Average: 50.3` | 50.333… |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 照抄第 13 行的优先级错误：`average = m1 + m2 + m3 / 3`，B1 输出 `Average: 158.3` | B1、B3、B4、B5 |
| M2 | 平均分用整除：`average = total // 3`，B1 输出 `Average: 71.0` | B1、B3、B4、B5 |
| M3 | 用 `round` 代替格式化：`print(f"Average: {round(total / 3)}")`，B1 输出 `Average: 72` | B1–B5 |

## 人工核对清单

- [ ] 4 处错误全部找到，行号正确，改正写法符合指南（p.8 CONSTANT、p.15 OUTPUT）。
- [ ] 没有把正确的行当成错误（例如第 08 行的提示语是对的）。
- [ ] 改正后的完整过程：`Average` 为 `REAL`；`ENDPROCEDURE` 结束；关键字全大写。
- [ ] Python：`int(input(...))` 读三个分数；平均分用 `/`；`f"{average:.1f}"`。

## 出处

自编。错误类型参考 ECR P2 2024（9618_s24_22）p.10 的考官点评：求平均时漏括号、OUTPUT 缺分隔符。语法依据：指南 p.6（行号）、p.8、p.15。
