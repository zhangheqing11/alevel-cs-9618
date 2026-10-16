# L02/E05 · 干跑：邮费函数（嵌套 IF 与 DIV）


### 中文导读

读下面的函数 `Postage()`。**先不写 Python**：手算 6 次调用的返回值，按顺序填进 `PREDICTED`（数字列表）。然后把函数逐行译成 Python 的 `postage(weight, express)`。最后在 `solution.py` 末尾用注释回答：这个函数的 `Weight` 部分能不能改写成 CASE？如果能，写出 CASE 版本的伪代码（注释里写即可）。

### English task

Study the function `Postage()`.

1. Without running any code, work out the value returned by each of these calls, in order, and store the six values in the list `PREDICTED`:
   `Postage(100, FALSE)`, `Postage(101, FALSE)`, `Postage(501, FALSE)`, `Postage(750, FALSE)`, `Postage(751, TRUE)`, `Postage(1000, TRUE)`.
2. Translate the function into the Python function `postage(weight, express)`.
3. In a comment at the end of your file, state whether the weight bands could be written as a `CASE` structure, and if so, write the `CASE` version.

```pseudocode
FUNCTION Postage(Weight : INTEGER, Express : BOOLEAN) RETURNS REAL
   DECLARE Cost : REAL
   IF Weight <= 100 THEN
      Cost ← 1.50
   ELSE
      IF Weight <= 500 THEN
         Cost ← 3.00
      ELSE
         Cost ← 3.00 + ((Weight - 500) DIV 250 + 1) * 1.20
      ENDIF
   ENDIF
   IF Express = TRUE THEN
      Cost ← Cost * 2
   ENDIF
   RETURN Cost
ENDFUNCTION
```

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能解释为什么 750 克比 749 克贵（`250 DIV 250 = 1`）。
- [ ] 能说出两层嵌套为什么需要两个 `ENDIF`，以及 Python 用 `elif` 时为什么不需要。
- [ ] CASE 改写：重量段可以写成 `CASE OF Weight` / `0 TO 100 : …` / `101 TO 500 : …` / `OTHERWISE : …`（指南 p.19）；`Express` 的判断涉及另一个变量，只能留在 IF 里。
- [ ] Python：`IF Express = TRUE THEN` 译成 `if express:` 或 `if express == True:` 都对，前者更常见。

## 出处

自编。语法依据：指南 p.15（DIV）、p.18（嵌套 IF）、p.19（CASE）、p.23（FUNCTION）。活动依据：SoW Unit 11 p.35（IF 与 CASE 互转，并说明不能转换的情况）。
