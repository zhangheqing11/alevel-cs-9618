# L09/E02 · 输入校验：名字与分数分别检查、反复输入


### 中文导读

写两个函数。`InputName()`：反复输入，直到输入的是**正好 3 个大写字母**（A 到 Z），每次无效时输出 `Invalid name`，最后返回这个名字。`InputScore()`：反复输入，直到输入的是 0 到 1000（含两端）的整数，每次无效时输出 `Invalid score`，最后返回这个整数。两项分开校验：名字的问题不影响分数，反之亦然（ER s22 9618/41 Q1 p.36）。

### English task

Write two functions.

- `InputName()` repeatedly inputs a player name until it is exactly 3 characters long and every character is an upper-case letter `A` to `Z`. It outputs `Invalid name` after each invalid name and returns the valid name.
- `InputScore()` repeatedly inputs a score until it is an integer from 0 to 1000 inclusive. Use exception handling to detect input that is not an integer. It outputs `Invalid score` after each invalid score and returns the valid score as an integer.

Neither function outputs anything else.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] 名字的检查写成「长度正好 3」并逐个字符检查 `"A" <= Ch <= "Z"`（或 `isupper()` 加 `isalpha()` 等价写法）。
- [ ] `InputScore` 用 `try: int(…)` / `except ValueError:`；范围检查不放在 `except` 里。
- [ ] 两个函数各管各的：没有把名字和分数放进同一个循环一起判断。
- [ ] 提示语写在 `input("…")` 里（测试不检查提示语）；函数名与题目一致。

## 出处

思路改编自 CS50P Problem Set 3 “Fuel Gauge”（<https://cs50.harvard.edu/python/psets/3/fuel/>，David J. Malan，CC BY-NC-SA 4.0）：捕捉 `ValueError` 后重新输入。改动：改为名字与分数两项、规则与提示全部重写。误区依据：ER s22 9618/41 Q1 p.36（3 字符名字写成 `<= 3`；两项数据应分别校验）。
