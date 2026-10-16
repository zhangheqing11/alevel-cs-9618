# L02/E05 · 干跑：邮费函数（嵌套 IF 与 DIV）

| 属性 | 值 |
|:--|:--|
| id | `L02/E05` |
| 目录 | `ladder/levels/L02-selection/exercises/E05-trace-postage/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2） |
| entry | `postage` |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `nested-if`, `div-mod`, `operator-precedence` |
| difficulty | 2 |
| title | `Dry run: a postage function with nested IF and DIV` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L02 card §3、§4、§5；L01 card §5 |

## 练习目标

精确执行一段嵌套 IF（含 `DIV` 与括号）并预测返回值；把它译成 Python 函数；判断它能不能改写成 CASE（SoW Unit 11 p.35 的 IF ↔ CASE 互转活动）。

## 题面

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

## 接口

```python
PREDICTED: list[float] = []  # fill in by hand BEFORE writing postage()


def postage(weight: int, express: bool) -> float:
    """Translate the pseudocode function Postage() line by line."""
    raise NotImplementedError


# Could the weight bands be written as a CASE structure? Answer here:
```

（不需要 `answer.pseudo`。）

## 必测行为

期望值已用参考实现核对。浮点比对用 `pytest.approx(…, abs=1e-9)`。

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED` | 长度 6，逐项约等于 `[1.50, 3.00, 4.20, 5.40, 10.80, 13.20]` |
| B2 | `postage(100, False)`、`postage(0, False)` | `1.50`、`1.50`（`<= 100` 含 100） |
| B3 | `postage(101, False)`、`postage(500, False)` | `3.00`、`3.00` |
| B4 | `postage(501, False)` | `4.20`（`1 DIV 250 = 0`，再 `+ 1`） |
| B5 | `postage(750, False)`、`postage(1250, False)` | `5.40`、`7.80` |
| B6 | `postage(1001, False)` | `6.60` |
| B7 | `postage(751, True)`、`postage(1000, True)`、`postage(100, True)` | `10.80`、`13.20`、`3.00`（Express 翻倍） |
| B8 | 任一调用的返回类型 | `float` |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 第一层边界用 `<`：`if weight < 100`，`postage(100, False)` 返回 `3.00`；`PREDICTED` 第 1 项也写成 `3.00` | B1、B2 |
| M2 | `DIV` 译成 `/`：`((weight - 500) / 250 + 1) * 1.20`，501 返回约 `4.2048` | B4、B6、B7 |
| M3 | 漏了括号：`3.00 + (weight - 500) // 250 + 1 * 1.20`，750 返回 `5.20`；`PREDICTED` 也按此算 | B1、B5、B6、B7 |

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能解释为什么 750 克比 749 克贵（`250 DIV 250 = 1`）。
- [ ] 能说出两层嵌套为什么需要两个 `ENDIF`，以及 Python 用 `elif` 时为什么不需要。
- [ ] CASE 改写：重量段可以写成 `CASE OF Weight` / `0 TO 100 : …` / `101 TO 500 : …` / `OTHERWISE : …`（指南 p.19）；`Express` 的判断涉及另一个变量，只能留在 IF 里。
- [ ] Python：`IF Express = TRUE THEN` 译成 `if express:` 或 `if express == True:` 都对，前者更常见。

## 出处

自编。语法依据：指南 p.15（DIV）、p.18（嵌套 IF）、p.19（CASE）、p.23（FUNCTION）。活动依据：SoW Unit 11 p.35（IF 与 CASE 互转，并说明不能转换的情况）。
