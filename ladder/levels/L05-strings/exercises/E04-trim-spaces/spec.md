# L05/E04 · 去掉首尾空格：长度表达式不差一

| 属性 | 值 |
|:--|:--|
| id | `L05/E04` |
| 目录 | `ladder/levels/L05-strings/exercises/E04-trim-spaces/` |
| 形态 | `function` |
| entry | `trim_spaces` |
| pseudocode | `true` |
| files | `[]` |
| skills | `string-functions`, `string-index`, `pre-condition-loop`, `boundary-values` |
| difficulty | 3 |
| title | `Remove leading and trailing spaces` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L05 card §2；常见坑 3、5、12 |

## 练习目标

用 `LEFT`/`RIGHT`/`LENGTH` 反复截掉首尾的空格，写对每一个长度表达式；循环条件先判空串、再取字符；考虑全是空格、空串这些边界。

## 题面

### 中文导读

写函数 `TrimSpaces()`：去掉字符串开头和结尾的空格字符（只管空格 `' '`），中间的空格保留。例如 `"  IF X > 13 THEN  "` 变成 `"IF X > 13 THEN"`；全是空格的串变成空串。伪代码只能用插页函数，不能用 `TRIM` 之类不存在的函数。

### English task

Write a function `TrimSpaces()` that takes a string and returns it with all leading and trailing space characters removed. Spaces between other characters are kept. A string made only of spaces becomes the empty string.

Use only functions from the insert. Then write the Python function `trim_spaces(text)`.

## 接口

```python
def trim_spaces(text: str) -> str:
    """Return text without leading or trailing space characters (' ' only)."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION TrimSpaces(Text : STRING) RETURNS STRING
   // remove leading spaces, then trailing spaces

ENDFUNCTION
```

## 必测行为

测试只用空格作空白字符（不含制表符、换行），所以 Python 写成手动循环、`strip(" ")` 或 `strip()` 都能通过。

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `trim_spaces("  IF X > 13 THEN  ")` | `"IF X > 13 THEN"` | 首尾都有 |
| B2 | `trim_spaces("abc")` | `"abc"` | 没有空格 |
| B3 | `trim_spaces("   ")` | `""` | 全是空格（边界） |
| B4 | `trim_spaces("")` | `""` | 空串（边界） |
| B5 | `trim_spaces(" a b ")` | `"a b"` | 中间空格保留 |
| B6 | `trim_spaces("a")` | `"a"` | 一个字符 |
| B7 | `trim_spaces("  x")`、`trim_spaces("x  ")` | `"x"`、`"x"` | 只有一侧有空格 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 长度差一（与 ECR P2 2024 p.26 范答同类的错）：数出开头空格数 `k`，`if k > 0: text = text[k + 1:]`，再去尾空格；B1 得 `"F X > 13 THEN"` | B1、B5、B7 |
| M2 | 删掉所有空格：`text.replace(" ", "")`，B5 得 `"ab"` | B1、B5 |
| M3 | 只去开头：`text.lstrip(" ")`，B7 第二个得 `"x  "` | B1、B5、B7 |

（M1 只在开头有空格时才删多一个字符：B2、B6 不受影响。）

## 人工核对清单

- [ ] 伪代码：去开头空格用标志变量（如 `Trimming`）控制 `WHILE`：循环里先判断 `Text = ""`（置标志为 FALSE），否则在内层 `IF` 里判断 `LEFT(Text, 1) = ' '`（是则 `Text ← RIGHT(Text, LENGTH(Text) - 1)`，否则置标志为 FALSE）；去结尾空格同理，用 `RIGHT(Text, 1)` 和 `LEFT(Text, LENGTH(Text) - 1)`。**不要**写 `WHILE Text <> "" AND LEFT(Text, 1) = ' '`——指南没有保证 `AND` 短路，空串时 `LEFT(Text, 1)` 的调用格式不对（D25）。
- [ ] 伪代码：判空写在取字符之前（卡片常见坑 12）；全是空格的串不会让 `LEFT`/`RIGHT` 收到负数长度。
- [ ] 伪代码：每个 `LEFT`/`RIGHT` 的返回值都赋回了变量（ER s22 9618/22 Q7 p.19）；以 `RETURN Text` 结束，不是 `OUTPUT`。
- [ ] 能用 `"  IF"` 代入自己写的长度表达式，验证不差一。

## 出处

自编。题意参考 9618_s24_22 Q8(b) 的 `DeleteSpaces()`（只去开头空格），本题扩展为首尾都去。误区依据：ECR P2 2024 p.26–27（范答长度差一；考官点评「长度参数差一很常见」）。函数依据：插页 9618_w25_in_21 p.2。
