# L09/E01 · 安全转换：try/except ValueError + 范围检查

| 属性 | 值 |
|:--|:--|
| id | `L09/E01` |
| 目录 | `ladder/levels/L09-exceptions-validation/exercises/E01-convert-mark/` |
| 形态 | `function` |
| entry | `ConvertMark` |
| pseudocode | `false` |
| files | `[]` |
| skills | `exception-handling`, `input-validation`, `type-conversion`, `boundary-values`, `p4-identifiers` |
| difficulty | 2 |
| title | `Convert a mark safely with try and except` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L09 card §1、§2、§4 |

## 练习目标

用 `try`/`except ValueError` 处理「不是整数」的输入，再做范围检查；只捕捉预料到的异常；使用题目指定的标识符 `ConvertMark`、`MarkString`。

## 题面

### 中文导读

写函数 `ConvertMark(MarkString)`：如果 `MarkString` 能被 Python 的 `int()` 转成整数，并且这个整数在 0 到 100 之间（含两端），就返回这个整数；否则返回 `-1`。必须用 `try`/`except ValueError`，不要用不带类型的 `except:`。

### English task

Write a function `ConvertMark()` that takes a string parameter `MarkString`.

- If `MarkString` can be converted to an integer using `int()`, and the integer is between 0 and 100 inclusive, the function returns that integer.
- Otherwise the function returns `-1`.

Use exception handling (`try` / `except ValueError`) for the conversion.

## 接口

```python
def ConvertMark(MarkString: str) -> int:
    """Return the mark (0-100) represented by MarkString, or -1 if it is not valid."""
    raise NotImplementedError
```

（不需要 `answer.pseudo`。）

## 必测行为

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `ConvertMark("72")` | `72` | 普通 |
| B2 | `ConvertMark("0")`、`ConvertMark("100")` | `0`、`100` | 两端（边界） |
| B3 | `ConvertMark("101")`、`ConvertMark("-5")` | `-1`、`-1` | 刚越界 / 负数 |
| B4 | `ConvertMark("abc")`、`ConvertMark("")` | `-1`、`-1` | 不是数字（不能抛异常） |
| B5 | `ConvertMark("7.5")`、`ConvertMark("1e2")` | `-1`、`-1` | `int()` 不接受的写法 |
| B6 | `ConvertMark(" 72 ")` | `72` | `int()` 接受首尾空格 |
| B7 | 返回类型 | `int` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 没有异常处理：直接 `int(MarkString)`，`"abc"` 抛 `ValueError` | B4、B5 |
| M2 | 用 `isdigit()` 代替转换：`" 72 "` 返回 `-1` | B6 |
| M3 | 范围上端写成 `< 100`：`ConvertMark("100")` 返回 `-1` | B2 |

## 人工核对清单

- [ ] 用的是 `except ValueError:`，不是不带类型的 `except:` 或 `except Exception:`。
- [ ] `try` 块里只有转换那一行（或很少几行），范围检查放在 `try` 之外或 `else` 里。
- [ ] 函数名、参数名与题目一致（`ConvertMark`、`MarkString`）。
- [ ] 能说出 P2 的伪代码里怎样不用异常完成同样的检查（`IS_NUM` + `STR_TO_NUM` + `INT(Mark) = Mark`，卡片 §1）。

## 出处

自编。依据：考纲 20.2（p.38）；插页 9618_w25_in_21 p.2–3（IS_NUM、STR_TO_NUM）。
