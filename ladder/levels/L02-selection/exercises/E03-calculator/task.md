# L02/E03 · 计算器：按字符 CASE、CASE 里嵌 IF


### 中文导读

依次输入：一个整数、一个运算符（`+ - * / %` 之一）、另一个整数。输出 `Result: <结果>`。`/` 是普通除法（结果是实数），`%` 是取余（伪代码里用 `MOD`）。除数为 0 时（`/` 或 `%`）输出 `Error: division by zero`；运算符不在这五个里时输出 `Error: unknown operator`。

### English task

Write a procedure `Calculator()` that:

- prompts for and inputs an integer `Num1`, then an operator character `Operator`, then an integer `Num2`
- uses a `CASE` structure on `Operator`:
  - `'+'`, `'-'`, `'*'`: output `Result: ` followed by the integer result
  - `'/'`: output `Result: ` followed by the real result of `Num1 / Num2`
  - `'%'`: output `Result: ` followed by `Num1 MOD Num2`
  - any other character: output `Error: unknown operator`
- for `'/'` and `'%'`, outputs `Error: division by zero` instead if `Num2` is 0.

Then write the Python procedure `calculator()`. Print the result of `/` exactly as Python displays a float (for example `3.5`, `2.0`).

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示。除题目规定的输出外不要打印其他内容。

## 人工核对清单

- [ ] 伪代码：`CASE OF Operator`，CHAR 值用单引号 `'+'`，`OTHERWISE` 是最后一个子句，以 `ENDCASE` 结束（指南 p.7、p.19）。
- [ ] 伪代码：`'/'` 与 `'%'` 两个子句里各有 `IF Num2 = 0 THEN … ELSE … ENDIF`；子句内多条语句按指南格式换行缩进（p.19）。
- [ ] 伪代码：取余用 `Num1 MOD Num2`，不是 `%`。
- [ ] 伪代码：三个 `INPUT` 前都有提示语。
- [ ] Python：`num1`、`num2` 用 `int()`，运算符保持字符串；用 `if/elif/else` 或 `match` 都可以。

## 出处

改编自 CS50P Problem Set 1 “Math Interpreter”（<https://cs50.harvard.edu/python/psets/1/interpreter/>，David J. Malan，CC BY-NC-SA 4.0）。改动：一行表达式改为三次输入；增加 `%`（MOD）；增加除零与未知运算符的处理；输出格式重写。
