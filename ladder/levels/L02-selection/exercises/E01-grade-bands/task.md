# L02/E01 · 分数段：CASE 范围子句

| 属性 | 值 |
|:--|:--|
| id | `L02/E01` |
| 目录 | `ladder/levels/L02-selection/exercises/E01-grade-bands/` |
| 形态 | `function`（见 `ladder/design.md` §7.2） |
| entry | `grade` |
| pseudocode | `true` |
| files | `[]` |
| skills | `case-of`, `case-range`, `boundary-values`, `return-value` |
| difficulty | 2 |
| title | `Grade bands with a CASE structure` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L02 card §4、§5；常见坑 5、6 |

## 练习目标

用 `CASE OF` 的 `TO` 范围子句和 `OTHERWISE` 写多分支；在 Python 里用 `if/elif` 或 `match` 实现；按边界选测试值。

## 题面

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

## 接口

```python
def grade(mark: int) -> str:
    """Return "A"-"E", "U" for 0-100, or "Invalid" for any other mark."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION Grade(Mark : INTEGER) RETURNS STRING
   // use a CASE structure with ranges and an OTHERWISE clause

ENDFUNCTION
```

## 必测行为

| # | 调用 | 期望返回 | 说明 |
|:--|:--|:--|:--|
| B1 | `grade(85)` | `"A"` | 普通值 |
| B2 | `grade(100)`、`grade(80)` | `"A"`、`"A"` | A 段两端 |
| B3 | `grade(79)`、`grade(70)` | `"B"`、`"B"` | B 段两端 |
| B4 | `grade(69)`、`grade(60)`、`grade(59)`、`grade(50)` | `"C"`、`"C"`、`"D"`、`"D"` | C、D 段两端 |
| B5 | `grade(49)`、`grade(40)`、`grade(39)` | `"E"`、`"E"`、`"U"` | E/U 分界 |
| B6 | `grade(0)` | `"U"` | 最小合法值 |
| B7 | `grade(-1)`、`grade(101)` | `"Invalid"`、`"Invalid"` | 刚好越界（异常数据） |
| B8 | 任一调用的返回类型 | `str` | 不是 `None`、不是 `print` 出来的 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | A 段边界用 `>`：`if mark > 80`，80 返回 `"B"` | B2 |
| M2 | 分支顺序写反：先判断 `mark >= 40` 返回 `"E"`，85 也返回 `"E"` | B1–B4 |
| M3 | 漏了合法范围检查：101 返回 `"A"`，-1 返回 `"U"` | B7 |

## 人工核对清单

- [ ] 伪代码用的是 `CASE OF Mark`，范围写成 `80 TO 100 :`，最后是 `OTHERWISE :`，以 `ENDCASE` 结束（指南 p.19）。
- [ ] 每个分支都 `RETURN` 一个字符串，或先赋给变量再在 `ENDCASE` 后统一 `RETURN`；以 `ENDFUNCTION` 结束。
- [ ] 字符串用双引号（指南 p.7）。
- [ ] 能说出：如果把「`OTHERWISE : RETURN "Invalid"`」去掉，`Grade(101)` 会怎样。
- [ ] 能为本题列出全部边界测试值（每段两端 + -1、101）。

## 出处

自编。语法依据：指南 p.19（CASE、TO 范围、OTHERWISE）、p.23（FUNCTION、RETURN）。
