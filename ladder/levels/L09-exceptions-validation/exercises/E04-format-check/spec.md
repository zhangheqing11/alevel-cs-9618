# L09/E04 · 格式校验：不用异常（P2 写法）

| 属性 | 值 |
|:--|:--|
| id | `L09/E04` |
| 目录 | `ladder/levels/L09-exceptions-validation/exercises/E04-format-check/` |
| 形态 | `function` |
| entry | `ValidCode` |
| pseudocode | `true` |
| files | `[]` |
| skills | `input-validation`, `string-functions`, `char-compare`, `boolean-return`, `boundary-values` |
| difficulty | 3 |
| title | `Format check without exceptions` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L09 card §1、§4；L05 card §2、§3 |

## 练习目标

用插页函数和比较写出格式校验：长度检查 + 逐字符检查。体会 `IS_NUM` 不是「全是数字」的检查（它接受 `"1.5"`、`"-12"`），所以要逐个字符比较。

## 题面

### 中文导读

产品代码的格式是：正好 5 个字符，前 2 个是大写字母 A–Z，后 3 个是数字 0–9，例如 `AB123`。写函数 `ValidCode(Code)`，格式正确返回 `TRUE`，否则返回 `FALSE`。伪代码只能用插页函数；不要用 `IS_NUM` 检查后三位（想一想为什么）。

### English task

A product code must be exactly 5 characters long. The first 2 characters must be upper-case letters `A` to `Z`, and the last 3 characters must be digits `0` to `9`. For example, `AB123` is valid.

Write a function `ValidCode()` that takes a string `Code` and returns `TRUE` if it has this format, otherwise `FALSE`. Use only functions from the insert, and check each character with comparison operators. Then write the Python function `ValidCode(Code)`.

## 接口

```python
def ValidCode(Code: str) -> bool:
    """Return True if Code is 2 upper-case letters followed by 3 digits."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
FUNCTION ValidCode(Code : STRING) RETURNS BOOLEAN
   // length check, then check each character with MID() and comparisons

ENDFUNCTION
```

## 必测行为

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `ValidCode("AB123")`、`ValidCode("ZZ000")` | `True`、`True` | 有效 |
| B2 | `ValidCode("ab123")` | `False` | 小写字母 |
| B3 | `ValidCode("A1234")`、`ValidCode("AB12C")` | `False`、`False` | 字母与数字位置不对 |
| B4 | `ValidCode("AB12")`、`ValidCode("AB1234")`、`ValidCode("")` | `False`、`False`、`False` | 长度不对（边界） |
| B5 | `ValidCode("AB1.5")`、`ValidCode("AB-12")` | `False`、`False` | 能转成数字但不全是数字 |
| B6 | `ValidCode("AB 23")` | `False` | 含空格 |
| B7 | 返回类型 | `bool` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 后三位用「能否转成数字」检查：`float(Code[2:])` 成功就算有效，`"AB1.5"`、`"AB-12"`、`"AB 23"` 都被接受 | B5、B6 |
| M2 | 长度写成 `len(Code) >= 5`，只检查前 5 个字符：`"AB1234"` 被接受 | B4 |
| M3 | 字母检查不分大小写（先转大写再比较）：`"ab123"` 被接受 | B2 |

（M1 需要先检查长度并只在 `float()` 成功时返回 `True`，用 `try` 包住，`"AB12C"` 等仍返回 `False`。）

## 人工核对清单

- [ ] 伪代码：先 `IF LENGTH(Code) <> 5 THEN RETURN FALSE`；再用 `MID(Code, i, 1)` 逐个检查，字母 `>= 'A' AND <= 'Z'`，数字 `>= '0' AND <= '9'`。
- [ ] 伪代码：没有 `TRY`；没有用 `IS_NUM` 检查后三位，并能说出原因（`IS_NUM("1.5")`、`IS_NUM("-12")` 为 TRUE，插页 p.3）。
- [ ] 伪代码：返回 `TRUE`/`FALSE`；没有 `OUTPUT`。
- [ ] Python：可以用逐字符比较，也可以用 `isupper()`/`isdigit()`，但要能说出它们对非 ASCII 字符的行为与题意的差别。

## 出处

自编。函数依据：插页 9618_w25_in_21 p.2–3（LENGTH、MID、IS_NUM）；指南 p.16（比较、AND）。
