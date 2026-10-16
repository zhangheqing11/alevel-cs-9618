# L02/E04 · 字符分类：字符范围比较


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

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

## 人工核对清单

- [ ] 伪代码：CHAR 字面量用单引号（`'A'`）；空格是 `' '`（指南 p.7）。
- [ ] 伪代码：每个范围写成两个完整比较用 `AND` 连接，没有 `'A' <= Ch <= 'Z'` 这种链式写法（ECR P2 2021 p.27 点名过半截条件）。
- [ ] 伪代码：嵌套 IF 每层都有 `ENDIF`，或每个分支直接 `RETURN`；以 `ENDFUNCTION` 结束。
- [ ] Python：先用比较运算实现；之后可以对照 `ch.isupper()`、`ch.isdigit()` 等方法，但要知道它们对非 ASCII 字符的结果与本题规则不同（例如 `"É".isupper()` 为 `True`）。

## 出处

自编。语法依据：指南 p.7（CHAR 字面量）、p.16（比较、AND）；插页 9618_w25_in_21 p.4（CHAR 与 STRING 的比较区分大小写）。
