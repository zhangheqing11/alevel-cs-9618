# L09/E04 · 格式校验：不用异常（P2 写法）


### 中文导读

产品代码的格式是：正好 5 个字符，前 2 个是大写字母 A–Z，后 3 个是数字 0–9，例如 `AB123`。写函数 `ValidCode(Code)`，格式正确返回 `TRUE`，否则返回 `FALSE`。伪代码只能用插页函数；不要用 `IS_NUM` 检查后三位（想一想为什么）。

### English task

A product code must be exactly 5 characters long. The first 2 characters must be upper-case letters `A` to `Z`, and the last 3 characters must be digits `0` to `9`. For example, `AB123` is valid.

Write a function `ValidCode()` that takes a string `Code` and returns `TRUE` if it has this format, otherwise `FALSE`. Use only functions from the insert, and check each character with comparison operators. Then write the Python function `ValidCode(Code)`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：先 `IF LENGTH(Code) <> 5 THEN RETURN FALSE`；再用 `MID(Code, i, 1)` 逐个检查，字母 `>= 'A' AND <= 'Z'`，数字 `>= '0' AND <= '9'`。
- [ ] 伪代码：没有 `TRY`；没有用 `IS_NUM` 检查后三位，并能说出原因（`IS_NUM("1.5")`、`IS_NUM("-12")` 为 TRUE，插页 p.3）。
- [ ] 伪代码：返回 `TRUE`/`FALSE`；没有 `OUTPUT`。
- [ ] Python：可以用逐字符比较，也可以用 `isupper()`/`isdigit()`，但要能说出它们对非 ASCII 字符的行为与题意的差别。

## 出处

自编。函数依据：插页 9618_w25_in_21 p.2–3（LENGTH、MID、IS_NUM）；指南 p.16（比较、AND）。
