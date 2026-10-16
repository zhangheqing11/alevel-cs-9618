# L03/E04 · 投币机：REPEAT 累加到够数

| 属性 | 值 |
|:--|:--|
| id | `L03/E04` |
| 目录 | `ladder/levels/L03-iteration/exercises/E04-coin-machine/` |
| 形态 | `io`（见 `ladder/design.md` §7.2） |
| entry | `coin_machine` |
| pseudocode | `true` |
| files | `[]` |
| skills | `post-condition-loop`, `accumulator`, `declare-variables`, `logic-ops`, `boundary-values` |
| difficulty | 3 |
| title | `Coin machine: accumulate coins until the price is paid` |
| adapted_from | `CS50P Problem Set 2 "Coke Machine" (https://cs50.harvard.edu/python/psets/2/coke/), CC BY-NC-SA 4.0; adapted: new price and coin set, rejected-coin message, pseudocode-first REPEAT loop, new output format` |
| 对应卡片小节 | L03 card §3、§4、§5；L02 card §2 |

## 练习目标

用 `REPEAT … UNTIL` 累加直到达到目标（至少投一枚币，所以是后测循环）；用常量表示价格；用 `OR` 判断合法币值；注意「刚好够」的边界。

## 题面

### 中文导读

饮料价格 60 分。机器只收 10、20、50 分的硬币。每投一枚：合法就累加，不合法就输出 `Rejected: <币值>`；之后如果还没付够，输出 `Due: <还差多少>`。付够（等于或超过 60）后输出 `Change: <找零>`。价格写成常量。

### English task

A drinks machine sells one drink for 60 cents. It accepts only 10, 20 and 50 cent coins.

Write a procedure `CoinMachine()` that uses a constant `Price` with the value `60` and repeatedly prompts for and inputs one coin value (an integer) at a time:

- if the coin is 10, 20 or 50, add it to the amount paid; otherwise output `Rejected: ` followed by the coin value
- then, if the amount paid is still less than the price, output `Due: ` followed by the amount still due.

When the amount paid is at least the price, stop and output `Change: ` followed by the change.

Use a post-condition (`REPEAT … UNTIL`) loop. Then write the Python procedure `coin_machine()`.

## 接口

```python
PRICE = 60


def coin_machine() -> None:
    """Input coins until at least PRICE is paid; print Rejected/Due lines, then Change."""
    raise NotImplementedError


if __name__ == "__main__":
    coin_machine()
```

`answer.pseudo` 模板：

```pseudocode
CONSTANT Price = 60

PROCEDURE CoinMachine()
   DECLARE Coin : INTEGER
   DECLARE Paid : INTEGER
   // use a REPEAT ... UNTIL loop

ENDPROCEDURE
```

## 必测行为

每个测试喂入的行数恰好等于正确程序需要读的行数。

| # | 输入（按顺序） | 期望输出行 | 说明 |
|:--|:--|:--|:--|
| B1 | `50`、`10` | `Due: 10`、`Change: 0` | 刚好付够（边界） |
| B2 | `20`、`20`、`50` | `Due: 40`、`Due: 20`、`Change: 30` | 超付找零 |
| B3 | `5`、`50`、`1`、`20` | `Rejected: 5`、`Due: 60`、`Due: 10`、`Rejected: 1`、`Due: 10`、`Change: 10` | 非法币被拒，拒收后也显示 Due |
| B4 | `50`、`50` | `Due: 10`、`Change: 40` | |
| B5 | `10`、`10`、`10`、`10`、`10`、`10` | `Due: 50`、`Due: 40`、`Due: 30`、`Due: 20`、`Due: 10`、`Change: 0` | 最多枚数 |
| B6 | `20`、`20`、`20` | `Due: 40`、`Due: 20`、`Change: 0` | 刚好付够的另一种组合 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 结束条件写成 `paid > PRICE`（`UNTIL Paid > Price`）：刚好 60 时还要一枚币 → `feed_input` 抛 `AssertionError` | B1、B5、B6 |
| M2 | 不检查币值，任何币都收：B3 输出 `Due: 55`… | B3 |
| M3 | 每投一枚都无条件输出 `Due:`：B1 多出 `Due: 0` | B1–B6 |

## 人工核对清单

- [ ] 伪代码：`CONSTANT Price = 60`；`Paid ← 0` 在循环之前（指南 p.8）。
- [ ] 伪代码：`REPEAT … UNTIL Paid >= Price`（指南 p.20–21）；没有 `BREAK`。
- [ ] 伪代码：合法币值判断写成 `Coin = 10 OR Coin = 20 OR Coin = 50`（或用 CASE 的三个子句）；能说出指南 CASE 子句为什么不能写成 `10, 20, 50 :`（指南 p.19 每个子句是一个值或一个 `TO` 范围）。
- [ ] 每个 `INPUT` 前有提示语。
- [ ] Python：常量 `PRICE` 参与计算，没有在多处直接写 `60`。

## 出处

改编自 CS50P Problem Set 2 “Coke Machine”（<https://cs50.harvard.edu/python/psets/2/coke/>，David J. Malan，CC BY-NC-SA 4.0）。改动：价格与可收币值不同；增加拒收消息；规定先写 `REPEAT` 伪代码；输出格式全部重写。
