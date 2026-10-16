# L02/E01 · 分数段：CASE 范围子句


### 中文导读

把 0–100 的分数换成等级：80–100 为 A，70–79 为 B，60–69 为 C，50–59 为 D，40–49 为 E，0–39 为 U；不在 0–100 之间的返回 `"Invalid"`。伪代码必须用 CASE 结构（范围子句 + OTHERWISE）。Python 可以用 `if/elif` 或 `match`。

### English task

Write a function `Grade()` that takes an integer mark and returns the grade as a string:

| Mark | Grade |
|:--|:--|
| 80 to 100 | `"A"` |
| 70 to 79 | `"B"` |
| 60 to 69 | `"C"` |
| 50 to 59 | `"D"` |
| 40 to 49 | `"E"` |
| 0 to 39 | `"U"` |
| any other value | `"Invalid"` |

Your pseudocode must use a `CASE` structure with ranges and an `OTHERWISE` clause. Then write the Python function `grade(mark)`.

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

## 人工核对清单

- [ ] 伪代码用的是 `CASE OF Mark`，范围写成 `80 TO 100 :`，最后是 `OTHERWISE :`，以 `ENDCASE` 结束（指南 p.19）。
- [ ] 每个分支都 `RETURN` 一个字符串，或先赋给变量再在 `ENDCASE` 后统一 `RETURN`；以 `ENDFUNCTION` 结束。
- [ ] 字符串用双引号（指南 p.7）。
- [ ] 能说出：如果把「`OTHERWISE : RETURN "Invalid"`」去掉，`Grade(101)` 会怎样。
- [ ] 能为本题列出全部边界测试值（每段两端 + -1、101）。

## 出处

自编。语法依据：指南 p.19（CASE、TO 范围、OTHERWISE）、p.23（FUNCTION、RETURN）。
