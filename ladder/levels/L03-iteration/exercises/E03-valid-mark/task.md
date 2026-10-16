# L03/E03 · 输入校验：REPEAT…UNTIL ↔ while True + break


### 中文导读

写一个函数：反复输入分数，直到输入的是 0 到 100（含两端）之间的整数为止，然后返回这个分数。每次输入无效时输出一行 `Invalid: must be 0 to 100`；输入有效时不输出任何东西。（本题假设输入的一定是整数。）

### English task

Write a function `GetMark()` that:

- repeatedly prompts for and inputs an integer mark until the mark is between 0 and 100 inclusive
- outputs the message `Invalid: must be 0 to 100` each time an invalid mark is input
- returns the valid mark.

Use a post-condition (`REPEAT … UNTIL`) loop. You may assume every input is an integer.

Then write the Python function `get_mark()`. It reads the marks with `input()`, prints the message after each invalid mark, prints nothing else, and returns the valid mark as an `int`.

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示。除题目规定的输出外不要打印其他内容。

## 人工核对清单

- [ ] 伪代码：`REPEAT … UNTIL Mark >= 0 AND Mark <= 100`，条件两半都完整（指南 p.20–21、p.16）。
- [ ] 伪代码：循环里先 `OUTPUT` 提示再 `INPUT Mark`；无效时用 `IF … THEN OUTPUT … ENDIF` 给消息；循环后 `RETURN Mark`；没有 `BREAK`。
- [ ] Python：用 `while True` + `break`/`return`（或标志变量）；`UNTIL` 的条件照抄，没有取反。
- [ ] 提示语写在 `input("…")` 里（测试不检查提示语）。
- [ ] 能回答：为什么这里用 `REPEAT` 而不用 `WHILE`（至少要输入一次）。

## 出处

思路改编自 CS50P Lecture 2 讲义 “Improving with User Input”（<https://cs50.harvard.edu/python/notes/2/#improving-with-user-input>，David J. Malan，CC BY-NC-SA 4.0）：`while True` + `break` 的输入校验循环。改动：改为 0–100 的分数、加无效提示、改为返回值。语法依据：指南 p.20–21（REPEAT）、p.23（FUNCTION、RETURN）。
