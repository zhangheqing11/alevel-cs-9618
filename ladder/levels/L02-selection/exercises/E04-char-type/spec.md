# L02/E04 · 字符分类：字符范围比较

| 属性 | 值 |
|:--|:--|
| id | `L02/E04` |
| 目录 | `ladder/levels/L02-selection/exercises/E04-char-type/` |
| 形态 | `function`（见 `ladder/design.md` §7.2） |
| entry | `char_type` |
| pseudocode | `true` |
| files | `[]` |
| skills | `char-compare`, `relational-ops`, `logic-ops`, `nested-if`, `boundary-values` |
| difficulty | 2 |
| title | `Classify a character with range comparisons` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L02 card §1、§2；常见坑 3 |

## 练习目标

用「`Ch >= 'A' AND Ch <= 'Z'`」这种完整的两段比较判断字符范围（P2 字符串题的基本功）；测试紧挨在范围外的字符。

## 题面

### 中文导读

输入一个字符，返回它的类别：大写字母 `"upper"`、小写字母 `"lower"`、数字 `"digit"`、空格 `"space"`，其他一律 `"other"`。伪代码必须用比较运算（`>=`、`<=`、`=`）和 `AND` 实现；Python 版也请先用比较运算写（写法要求在人工核对里查）。

### English task

Write a function `CharType()` that takes a single character and returns:

- `"upper"` if it is an upper-case letter `'A'` to `'Z'`
- `"lower"` if it is a lower-case letter `'a'` to `'z'`
- `"digit"` if it is a digit `'0'` to `'9'`
- `"space"` if it is the space character
- `"other"` for any other character.

Use comparison operators and `AND` only (no built-in functions). Then write the Python function `char_type(ch)`.

## 接口

```python
def char_type(ch: str) -> str:
    """ch is a single character. Return "upper", "lower", "digit", "space" or "other"."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION CharType(Ch : CHAR) RETURNS STRING
   // use comparison operators and AND

ENDFUNCTION
```

## 必测行为

全部输入都是 ASCII 单字符。

| # | 调用 | 期望返回 | 说明 |
|:--|:--|:--|:--|
| B1 | `char_type("M")` | `"upper"` | 普通大写 |
| B2 | `char_type("A")`、`char_type("Z")` | `"upper"`、`"upper"` | 大写两端 |
| B3 | `char_type("a")`、`char_type("z")` | `"lower"`、`"lower"` | 小写两端 |
| B4 | `char_type("0")`、`char_type("9")` | `"digit"`、`"digit"` | 数字两端 |
| B5 | `char_type(" ")` | `"space"` | 空格 |
| B6 | `char_type("@")`、`char_type("[")` | `"other"`、`"other"` | 紧挨 `A` 之前、`Z` 之后 |
| B7 | `char_type(chr(96))`、`char_type("{")` | `"other"`、`"other"` | 紧挨 `a` 之前（反引号）、`z` 之后 |
| B8 | `char_type("/")`、`char_type(":")` | `"other"`、`"other"` | 紧挨 `0` 之前、`9` 之后 |

（B7 的第一个字符是反引号，ASCII 96；测试里可以直接写 `chr(96)`。）

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 下界用 `>`：`if ch > "A" and ch <= "Z"`，`"A"` 返回 `"other"` | B2 |
| M2 | `and` 写成 `or`：`if ch >= "A" or ch <= "Z"`，任何字符都返回 `"upper"` | B3–B8 |
| M3 | 数字范围漏了 0：`if "1" <= ch <= "9"`，`"0"` 返回 `"other"` | B4 |

## 人工核对清单

- [ ] 伪代码：CHAR 字面量用单引号（`'A'`）；空格是 `' '`（指南 p.7）。
- [ ] 伪代码：每个范围写成两个完整比较用 `AND` 连接，没有 `'A' <= Ch <= 'Z'` 这种链式写法（ECR P2 2021 p.27 点名过半截条件）。
- [ ] 伪代码：嵌套 IF 每层都有 `ENDIF`，或每个分支直接 `RETURN`；以 `ENDFUNCTION` 结束。
- [ ] Python：先用比较运算实现；之后可以对照 `ch.isupper()`、`ch.isdigit()` 等方法，但要知道它们对非 ASCII 字符的结果与本题规则不同（例如 `"É".isupper()` 为 `True`）。

## 出处

自编。语法依据：指南 p.7（CHAR 字面量）、p.16（比较、AND）；插页 9618_s26_in_21 p.4（CHAR 与 STRING 的比较区分大小写）。
