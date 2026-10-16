# L02/E02 · 闰年：复合条件与返回 BOOLEAN

| 属性 | 值 |
|:--|:--|
| id | `L02/E02` |
| 目录 | `ladder/levels/L02-selection/exercises/E02-leap-year/` |
| 形态 | `function`（见 `ladder/design.md` §7.2） |
| entry | `is_leap` |
| pseudocode | `true` |
| files | `[]` |
| skills | `logic-ops`, `nested-if`, `div-mod`, `boolean-return`, `boundary-values` |
| difficulty | 2 |
| title | `Leap year test with compound conditions` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L02 card §2、§4、§6；常见坑 9 |

## 练习目标

把一条带「除非」的规则写成正确的复合条件（或嵌套 IF）；用 `MOD` 判断整除；函数返回真正的布尔值。

## 题面

### 中文导读

公历闰年规则：能被 4 整除的年份是闰年，但能被 100 整除的不是——除非它也能被 400 整除。写函数判断某年是不是闰年，返回 `TRUE`/`FALSE`（Python 返回 `True`/`False`）。

### English task

A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400.

Write a function `IsLeap()` that takes a year (a positive integer) and returns `TRUE` if it is a leap year and `FALSE` otherwise. Use `MOD`. Then write the Python function `is_leap(year)`, which returns a Boolean.

## 接口

```python
def is_leap(year: int) -> bool:
    """Return True if year is a leap year in the Gregorian calendar."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION IsLeap(Year : INTEGER) RETURNS BOOLEAN
   // use MOD, and AND / OR / NOT or nested IF statements

ENDFUNCTION
```

## 必测行为

| # | 调用 | 期望返回 | 说明 |
|:--|:--|:--|:--|
| B1 | `is_leap(2024)` | `True` | 能被 4 整除 |
| B2 | `is_leap(2023)` | `False` | 不能被 4 整除 |
| B3 | `is_leap(1900)`、`is_leap(2100)` | `False`、`False` | 能被 100 整除但不能被 400 整除 |
| B4 | `is_leap(2000)`、`is_leap(2400)` | `True`、`True` | 能被 400 整除 |
| B5 | `is_leap(4)`、`is_leap(1)` | `True`、`False` | 很小的年份 |
| B6 | 任一调用的返回值 | `type(result) is bool` | 不是字符串 `"TRUE"`，不是 0/1 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 只判断 `year % 4 == 0`，1900 返回 `True` | B3 |
| M2 | 漏了 400 的例外：`year % 4 == 0 and year % 100 != 0`，2000 返回 `False` | B4 |
| M3 | 返回字符串：`return "TRUE"` / `return "FALSE"` | B1–B6 |

## 人工核对清单

- [ ] 伪代码：`MOD` 写成运算符，如 `Year MOD 4 = 0`（指南 p.15；插页 p.4）。
- [ ] 伪代码：复合条件每一半都完整，并用括号写清 `AND`/`OR` 的结合（指南 p.16）。
- [ ] 伪代码：返回 `TRUE`/`FALSE`（大写，无引号）；嵌套 IF 时每层都有 `ENDIF`；以 `ENDFUNCTION` 结束。
- [ ] Python：返回 `True`/`False`；能说出 `return year % 4 == 0 and …` 与 `if …: return True else: return False` 等价。

## 出处

自编。语法依据：指南 p.15–16（MOD、比较、逻辑运算）、p.18（IF）、p.23（FUNCTION）。
