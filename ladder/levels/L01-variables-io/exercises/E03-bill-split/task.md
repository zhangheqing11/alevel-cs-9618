# L01/E03 · 分账：REAL、CONSTANT 与两位小数


### 中文导读

餐厅账单要加 10% 服务费，再由几个人平分。输入账单金额（可以有小数）和人数（至少 1 人），输出含服务费的总额和每人应付，都保留两位小数。服务费率写成常量。

### English task

A restaurant adds a 10% service charge to every bill. The total is then shared equally between a number of people.

Write a procedure `SplitBill()` that:

- uses a constant `ServiceRate` with the value `0.10`
- prompts for and inputs the bill amount (a real number) and then the number of people (an integer, at least 1)
- calculates the total including the service charge, and the amount each person pays
- outputs two lines in the form:

```text
Total: 110.00
Each: 27.50
```

In Python, write `split_bill()`. Both amounts must be printed with exactly two decimal places.

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示。除题目规定的输出外不要打印其他内容。

## 人工核对清单

- [ ] 伪代码：`CONSTANT ServiceRate = 0.10` 用 `=`，值是字面量（指南 p.8）。
- [ ] 伪代码：账单与结果 `DECLARE … : REAL`，人数 `DECLARE … : INTEGER`。
- [ ] 伪代码：每个 `INPUT` 前有 `OUTPUT` 提示语。
- [ ] 伪代码：说明了输出格式（如注释 `// output to 2 decimal places`）——指南 p.17：编程语言里格式化数字的做法要加说明。
- [ ] Python：常量全大写 `SERVICE_RATE`，计算里用常量而不是直接写 `0.10`。
- [ ] Python：用 `f"{x:.2f}"`，没有用 `round()` 代替格式化。

## 出处

改编自 CS50P Problem Set 0 “Tip Calculator”（<https://cs50.harvard.edu/python/psets/0/tip/>，David J. Malan，CC BY-NC-SA 4.0）。改动：小费百分比输入改为固定的服务费常量；输入改为纯数字；增加按人数平分；输出格式全部重写。
