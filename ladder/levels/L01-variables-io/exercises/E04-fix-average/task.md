# L01/E04 · 改错：三个分数的总分与平均分


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

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示。除题目规定的输出外不要打印其他内容。

## 人工核对清单

- [ ] 4 处错误全部找到，行号正确，改正写法符合指南（p.8 CONSTANT、p.15 OUTPUT）。
- [ ] 没有把正确的行当成错误（例如第 08 行的提示语是对的）。
- [ ] 改正后的完整过程：`Average` 为 `REAL`；`ENDPROCEDURE` 结束；关键字全大写。
- [ ] Python：`int(input(...))` 读三个分数；平均分用 `/`；`f"{average:.1f}"`。

## 出处

自编。错误类型参考 ECR P2 2024（9618_s24_22）p.10 的考官点评：求平均时漏括号、OUTPUT 缺分隔符。语法依据：指南 p.6（行号）、p.8、p.15。
