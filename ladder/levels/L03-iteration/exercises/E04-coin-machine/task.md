# L03/E04 · 投币机：REPEAT 累加到够数


### 中文导读

饮料价格 60 分。机器只收 10、20、50 分的硬币。每投一枚：合法就累加，不合法就输出 `Rejected: <币值>`；之后如果还没付够，输出 `Due: <还差多少>`。付够（等于或超过 60）后输出 `Change: <找零>`。价格写成常量。

### English task

A drinks machine sells one drink for 60 cents. It accepts only 10, 20 and 50 cent coins.

Write a procedure `CoinMachine()` that uses a constant `Price` with the value `60` and repeatedly prompts for and inputs one coin value (an integer) at a time:

- if the coin is 10, 20 or 50, add it to the amount paid; otherwise output `Rejected: ` followed by the coin value
- then, if the amount paid is still less than the price, output `Due: ` followed by the amount still due.

When the amount paid is at least the price, stop and output `Change: ` followed by the change.

Use a post-condition (`REPEAT … UNTIL`) loop. Then write the Python procedure `coin_machine()`.

## 作答文件

在学生作答目录的 `solution.py` 中实现 `starter.py` 给出的接口。

先完成 `answer.pseudo`，再写 Python。伪代码写法由导师按下列清单人工核对。

提示语写在 `input("…")` 中，不要另用 `print` 输出提示。除题目规定的输出外不要打印其他内容。

## 人工核对清单

- [ ] 伪代码：`CONSTANT Price = 60`；`Paid ← 0` 在循环之前（指南 p.8）。
- [ ] 伪代码：`REPEAT … UNTIL Paid >= Price`（指南 p.20–21）；没有 `BREAK`。
- [ ] 伪代码：合法币值判断写成 `Coin = 10 OR Coin = 20 OR Coin = 50`（或用 CASE 的三个子句）；能说出指南 CASE 子句为什么不能写成 `10, 20, 50 :`（指南 p.19 每个子句是一个值或一个 `TO` 范围）。
- [ ] 每个 `INPUT` 前有提示语。
- [ ] Python：常量 `PRICE` 参与计算，没有在多处直接写 `60`。

## 出处

改编自 CS50P Problem Set 2 “Coke Machine”（<https://cs50.harvard.edu/python/psets/2/coke/>，David J. Malan，CC BY-NC-SA 4.0）。改动：价格与可收币值不同；增加拒收消息；规定先写 `REPEAT` 伪代码；输出格式全部重写。
