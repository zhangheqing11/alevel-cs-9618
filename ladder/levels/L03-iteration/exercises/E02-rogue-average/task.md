# L03/E02 · 哨兵值求平均：WHILE + 预读


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

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示。除题目规定的输出外不要打印其他内容。

## 人工核对清单

- [ ] 伪代码：循环前有一次 `INPUT`（预读），循环体末尾再 `INPUT`；条件是 `WHILE Number <> -1`（指南 p.21）。
- [ ] 伪代码：`Count ← 0`、`Total ← 0` 在循环之前；`Average` 声明为 `REAL`。
- [ ] 伪代码：零数据时用 `IF Count = 0 THEN … ELSE … ENDIF` 避免除以零。
- [ ] 每个 `INPUT` 前都有提示语，提示里说明 `-1` 结束。
- [ ] 能回答：为什么这里用 `WHILE` 而不用 `REPEAT`（第一个输入就可能是哨兵值，循环体可能一次都不执行）。

## 出处

自编。语法依据：指南 p.21（WHILE）、p.15（INPUT、OUTPUT、`/`）、p.18（IF）。
