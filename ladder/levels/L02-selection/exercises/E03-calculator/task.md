# L02/E03 · 计算器：按字符 CASE、CASE 里嵌 IF

| 属性 | 值 |
|:--|:--|
| id | `L02/E03` |
| 目录 | `ladder/levels/L02-selection/exercises/E03-calculator/` |
| 形态 | `io`（见 `ladder/design.md` §7.2） |
| entry | `calculator` |
| pseudocode | `true` |
| files | `[]` |
| skills | `case-of`, `nested-if`, `div-mod`, `type-conversion`, `input-prompt` |
| difficulty | 3 |
| title | `Five-operator calculator with a CASE structure` |
| adapted_from | `CS50P Problem Set 1 "Math Interpreter" (https://cs50.harvard.edu/python/psets/1/interpreter/), CC BY-NC-SA 4.0; adapted: three separate inputs, MOD operator added, division-by-zero and unknown-operator messages, new output format` |
| 对应卡片小节 | L02 card §5；L01 card §5；常见坑 4、10 |

## 练习目标

对一个 CHAR 变量用 `CASE OF` 分支，`OTHERWISE` 处理非法运算符；在分支里再嵌 IF 处理除数为零；体会 `/` 与 `MOD` 的结果类型不同。

## 题面

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

## 接口

```python
def calculator() -> None:
    """Input num1, operator, num2 (one per line); print 'Result: ...' or an error message."""
    raise NotImplementedError


if __name__ == "__main__":
    calculator()
```

`answer.pseudo` 模板：

```pseudocode
PROCEDURE Calculator()
   DECLARE Num1 : INTEGER
   DECLARE Num2 : INTEGER
   DECLARE Operator : CHAR
   // prompt and input, then use a CASE structure on Operator

ENDPROCEDURE
```

## 必测行为

每个测试按顺序喂 3 行输入：`num1`、`operator`、`num2`。期望输出恰好 1 行。

| # | 输入 | 期望输出行 | 说明 |
|:--|:--|:--|:--|
| B1 | `7`、`+`、`5` | `Result: 12` | 加 |
| B2 | `7`、`-`、`10` | `Result: -3` | 减，结果为负 |
| B3 | `6`、`*`、`7` | `Result: 42` | 乘 |
| B4 | `7`、`/`、`2` | `Result: 3.5` | 除：实数结果 |
| B5 | `6`、`/`、`3` | `Result: 2.0` | 能整除时仍是实数 |
| B6 | `17`、`%`、`5` | `Result: 2` | 取余 |
| B7 | `5`、`/`、`0` | `Error: division by zero` | 除零（异常数据） |
| B8 | `5`、`%`、`0` | `Error: division by zero` | 取余也要查除零 |
| B9 | `5`、`^`、`2` | `Error: unknown operator` | OTHERWISE 分支 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `/` 用整除 `num1 // num2`，B4 输出 `Result: 3` | B4、B5 |
| M2 | 只在 `/` 分支查除零，`%` 分支直接 `num1 % num2`，B8 抛 `ZeroDivisionError` | B8 |
| M3 | `if operator == "+" or "-":` 的真值陷阱：任何运算符都进第一个分支做加法，B2 输出 `Result: 17` | B2、B3、B4、B9 等 |

## 人工核对清单

- [ ] 伪代码：`CASE OF Operator`，CHAR 值用单引号 `'+'`，`OTHERWISE` 是最后一个子句，以 `ENDCASE` 结束（指南 p.7、p.19）。
- [ ] 伪代码：`'/'` 与 `'%'` 两个子句里各有 `IF Num2 = 0 THEN … ELSE … ENDIF`；子句内多条语句按指南格式换行缩进（p.19）。
- [ ] 伪代码：取余用 `Num1 MOD Num2`，不是 `%`。
- [ ] 伪代码：三个 `INPUT` 前都有提示语。
- [ ] Python：`num1`、`num2` 用 `int()`，运算符保持字符串；用 `if/elif/else` 或 `match` 都可以。

## 出处

改编自 CS50P Problem Set 1 “Math Interpreter”（<https://cs50.harvard.edu/python/psets/1/interpreter/>，David J. Malan，CC BY-NC-SA 4.0）。改动：一行表达式改为三次输入；增加 `%`（MOD）；增加除零与未知运算符的处理；输出格式重写。
