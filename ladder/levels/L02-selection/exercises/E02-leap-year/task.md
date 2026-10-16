# L02/E02 · 闰年：复合条件与返回 BOOLEAN


### 中文导读

公历闰年规则：能被 4 整除的年份是闰年，但能被 100 整除的不是——除非它也能被 400 整除。写函数判断某年是不是闰年，返回 `TRUE`/`FALSE`（Python 返回 `True`/`False`）。

### English task

A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400.

Write a function `IsLeap()` that takes a year (a positive integer) and returns `TRUE` if it is a leap year and `FALSE` otherwise. Use `MOD`. Then write the Python function `is_leap(year)`, which returns a Boolean.

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

## 人工核对清单

- [ ] 伪代码：`MOD` 写成运算符，如 `Year MOD 4 = 0`（指南 p.15；插页 p.4）。
- [ ] 伪代码：复合条件每一半都完整，并用括号写清 `AND`/`OR` 的结合（指南 p.16）。
- [ ] 伪代码：返回 `TRUE`/`FALSE`（大写，无引号）；嵌套 IF 时每层都有 `ENDIF`；以 `ENDFUNCTION` 结束。
- [ ] Python：返回 `True`/`False`；能说出 `return year % 4 == 0 and …` 与 `if …: return True else: return False` 等价。

## 出处

自编。语法依据：指南 p.15–16（MOD、比较、逻辑运算）、p.18（IF）、p.23（FUNCTION）。
