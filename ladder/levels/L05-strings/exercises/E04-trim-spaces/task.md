# L05/E04 · 去掉首尾空格：长度表达式不差一


### 中文导读

写函数 `TrimSpaces()`：去掉字符串开头和结尾的空格字符（只管空格 `' '`），中间的空格保留。例如 `"  IF X > 13 THEN  "` 变成 `"IF X > 13 THEN"`；全是空格的串变成空串。伪代码只能用插页函数，不能用 `TRIM` 之类不存在的函数。

### English task

Write a function `TrimSpaces()` that takes a string and returns it with all leading and trailing space characters removed. Spaces between other characters are kept. A string made only of spaces becomes the empty string.

Use only functions from the insert. Then write the Python function `trim_spaces(text)`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：去开头空格，例如 `WHILE Text <> "" AND LEFT(Text, 1) = ' '` / `Text ← RIGHT(Text, LENGTH(Text) - 1)`；去结尾空格用 `LEFT(Text, LENGTH(Text) - 1)`。
- [ ] 伪代码：判空写在取字符之前（卡片常见坑 12）；全是空格的串不会让 `LEFT`/`RIGHT` 收到负数长度。
- [ ] 伪代码：每个 `LEFT`/`RIGHT` 的返回值都赋回了变量（ER s22 9618/22 Q7 p.19）；以 `RETURN Text` 结束，不是 `OUTPUT`。
- [ ] 能用 `"  IF"` 代入自己写的长度表达式，验证不差一。

## 出处

自编。题意参考 9618_s24_22 Q8(b) 的 `DeleteSpaces()`（只去开头空格），本题扩展为首尾都去。误区依据：ECR P2 2024 p.26–27（范答长度差一；考官点评「长度参数差一很常见」）。函数依据：插页 9618_w25_in_21 p.2。
