# L05/E01 · 插页函数库：用切片实现 LEFT / RIGHT / MID / LENGTH

| 属性 | 值 |
|:--|:--|
| id | `L05/E01` |
| 目录 | `ladder/levels/L05-strings/exercises/E01-insert-library/` |
| 形态 | `function`（四个函数） |
| entry | `mid`（同一文件还有 `left`、`right`、`length`） |
| pseudocode | `false` |
| files | `[]` |
| skills | `string-functions`, `string-index`, `boundary-values` |
| difficulty | 2 |
| title | `Insert library: LEFT, RIGHT, MID and LENGTH in Python` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L05 card §1、§2；常见坑 2、8 |

## 练习目标

把插页的四个字符串函数写成 Python 函数，参数含义与插页完全一致（1 起位置、`MID` 的第三个参数是长度）。以后把 P2 伪代码翻译成 Python 时，可以直接调用这四个函数，少犯下标错误。

## 题面

### 中文导读

按插页的定义写四个 Python 函数：`left(s, x)`、`right(s, x)`、`mid(s, x, y)`、`length(s)`。`mid` 的 `x` 是**从 1 开始**的起始位置，`y` 是取出的**长度**。可以假设参数总是合法的：`0 <= x <= len(s)`（`left`、`right`）；`x >= 1`、`y >= 0`、`x + y - 1 <= len(s)`（`mid`）。`length` 直接返回 `len(s)` 即可，写它只是为了四个函数名齐全。

### English task

Write Python functions that behave like the insert functions:

- `left(s, x)` returns the leftmost `x` characters of `s`
- `right(s, x)` returns the rightmost `x` characters of `s`
- `mid(s, x, y)` returns the string of length `y` starting at position `x` of `s`, where the first character is position 1
- `length(s)` returns the number of characters in `s`.

You may assume the parameters are always valid: `0 <= x <= len(s)` for `left` and `right`; `x >= 1`, `y >= 0` and `x + y - 1 <= len(s)` for `mid`.

## 接口

```python
def left(s: str, x: int) -> str:
    """LEFT(ThisString, x): the leftmost x characters."""
    raise NotImplementedError


def right(s: str, x: int) -> str:
    """RIGHT(ThisString, x): the rightmost x characters."""
    raise NotImplementedError


def mid(s: str, x: int, y: int) -> str:
    """MID(ThisString, x, y): y characters starting at position x (first position is 1)."""
    raise NotImplementedError


def length(s: str) -> int:
    """LENGTH(ThisString): the number of characters."""
    raise NotImplementedError
```

（不需要 `answer.pseudo`。）

## 必测行为

`S = "ABCDEFGH"`。B1–B4 是插页原例（插页 p.2）。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `left(S, 3)` | `"ABC"` | 插页例 |
| B2 | `right(S, 3)` | `"FGH"` | 插页例 |
| B3 | `mid(S, 2, 3)` | `"BCD"` | 插页例 |
| B4 | `length("Happy Days")` | `10` | 插页例 |
| B5 | `left(S, 0)`、`left(S, 8)` | `""`、`"ABCDEFGH"` | 边界 |
| B6 | `right(S, 0)`、`right(S, 8)` | `""`、`"ABCDEFGH"` | 边界：`x = 0` 必须是空串 |
| B7 | `mid(S, 1, 1)`、`mid(S, 8, 1)`、`mid(S, 1, 8)` | `"A"`、`"H"`、`"ABCDEFGH"` | 首、尾、整串 |
| B8 | `mid(S, 3, 0)` | `""` | 长度为 0 |
| B9 | `length("")` | `0` | 空串 |
| B10 | 返回类型 | 前三个返回 `str`，`length` 返回 `int` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `mid` 忘了把 1 起换成 0 起：`return s[x:x + y]`，B3 得 `"CDE"` | B3、B7 |
| M2 | `right` 写成 `s[-x:]`：`right(S, 0)` 返回整个串 | B6 |
| M3 | `mid` 把第三个参数当结束位置：`return s[x - 1:y]`，B3 得 `"BC"` | B3、B7 |

## 人工核对清单

- [ ] 能不看代码说出 `mid(s, x, y)` 对应的切片 `s[x - 1:x - 1 + y]`，并解释两个下标各自为什么这样写。
- [ ] 能说出 `right(s, x)` 为什么不能写成 `s[-x:]`。
- [ ] 能说出：插页规定参数不合法时报错（插页 p.2），而 Python 切片越界不报错——所以这四个函数在不合法参数下的行为与插页不同，本题不测。

## 出处

自编。函数定义：插页 9618_w25_in_21 p.2（LEFT、RIGHT、MID、LENGTH 及原例）；指南 p.16–17（RIGHT、LENGTH、MID）。
