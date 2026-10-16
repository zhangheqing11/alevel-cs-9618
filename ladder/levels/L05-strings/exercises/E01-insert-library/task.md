# L05/E01 · 插页函数库：用切片实现 LEFT / RIGHT / MID / LENGTH


### 中文导读

按插页的定义写四个 Python 函数：`left(s, x)`、`right(s, x)`、`mid(s, x, y)`、`length(s)`。`mid` 的 `x` 是**从 1 开始**的起始位置，`y` 是取出的**长度**。可以假设参数总是合法的：`0 <= x <= len(s)`（`left`、`right`）；`x >= 1`、`y >= 0`、`x + y - 1 <= len(s)`（`mid`）。`length` 直接返回 `len(s)` 即可，写它只是为了四个函数名齐全。

### English task

Write Python functions that behave like the insert functions:

- `left(s, x)` returns the leftmost `x` characters of `s`
- `right(s, x)` returns the rightmost `x` characters of `s`
- `mid(s, x, y)` returns the string of length `y` starting at position `x` of `s`, where the first character is position 1
- `length(s)` returns the number of characters in `s`.

You may assume the parameters are always valid: `0 <= x <= len(s)` for `left` and `right`; `x >= 1`, `y >= 0` and `x + y - 1 <= len(s)` for `mid`.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] 能不看代码说出 `mid(s, x, y)` 对应的切片 `s[x - 1:x - 1 + y]`，并解释两个下标各自为什么这样写。
- [ ] 能说出 `right(s, x)` 为什么不能写成 `s[-x:]`。
- [ ] 能说出：插页规定参数不合法时报错（插页 p.2），而 Python 切片越界不报错——所以这四个函数在不合法参数下的行为与插页不同，本题不测。

## 出处

自编。函数定义：插页 9618_w25_in_21 p.2（LEFT、RIGHT、MID、LENGTH 及原例）；指南 p.16–17（RIGHT、LENGTH、MID）。
