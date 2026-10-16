# L01/E02 · 秒数换算：DIV 与 MOD


### 中文导读

输入一个秒数（0 到 86399 的整数），把它换算成「几小时、几分钟、几秒」输出，格式如 `1 h 2 min 5 s`。先在 `answer.pseudo` 里写伪代码过程 `SplitSeconds()`：要有提示、有 `DECLARE`、用 `DIV` 和 `MOD`。再在 `solution.py` 里写 Python 版 `split_seconds()`。

### English task

Write a procedure `SplitSeconds()` that:

- prompts for and inputs a whole number of seconds, from 0 to 86399
- outputs the same amount of time as hours, minutes and seconds, in the form `1 h 2 min 5 s`.

Use `DIV` and `MOD` in your pseudocode. Then write the Python procedure `split_seconds()`, which reads the number with `input()` and prints exactly one line in the same format.

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示。除题目规定的输出外不要打印其他内容。

## 人工核对清单

- [ ] 伪代码：`INPUT` 之前有 `OUTPUT` 提示语（ECR P2 2024 p.15 把漏提示列为常见错误）。
- [ ] 伪代码：每个变量都 `DECLARE … : INTEGER`；用 `DIV`、`MOD`，没有 `/`。
- [ ] 伪代码：`OUTPUT Hours, " h ", Minutes, " min ", Seconds, " s"` 这类逗号分隔写法，空格写在字符串里。
- [ ] 伪代码：以 `ENDPROCEDURE` 结束；关键字全大写，赋值用 `←`。
- [ ] Python：提示语写在 `input("…")` 里；用 f-string 输出。
- [ ] （可选）用常量 `CONSTANT SecondsPerHour = 3600` / `SECONDS_PER_HOUR = 3600`，并说出这样写的好处（指南 p.8）。

## 出处

自编。语法依据：指南 p.8（DECLARE、CONSTANT）、p.15（INPUT、OUTPUT、DIV、MOD）、p.22（PROCEDURE）。
