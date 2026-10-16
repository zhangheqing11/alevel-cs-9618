# L01/E03 · 分账：REAL、CONSTANT 与两位小数

| 属性 | 值 |
|:--|:--|
| id | `L01/E03` |
| 目录 | `ladder/levels/L01-variables-io/exercises/E03-bill-split/` |
| 形态 | `io`（见 `ladder/design.md` §7.2） |
| entry | `split_bill` |
| pseudocode | `true` |
| files | `[]` |
| skills | `declare-variables`, `type-conversion`, `output-format`, `input-prompt` |
| difficulty | 2 |
| title | `Split a restaurant bill with a service charge` |
| adapted_from | `CS50P Problem Set 0 "Tip Calculator" (https://cs50.harvard.edu/python/psets/0/tip/), CC BY-NC-SA 4.0; adapted: fixed service-charge constant, numeric input, bill shared between people, new output format` |
| 对应卡片小节 | L01 card §2、§3、§4、§6；常见坑 3、9、10 |

## 练习目标

用 `CONSTANT` 表示固定的服务费率；读入实数与整数两种输入；实数用 `/` 平分；Python 输出保留两位小数。

## 题面

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

## 接口

```python
SERVICE_RATE = 0.10


def split_bill() -> None:
    """Input bill (real) then people (int); print 'Total: x.xx' and 'Each: x.xx'."""
    raise NotImplementedError


if __name__ == "__main__":
    split_bill()
```

`answer.pseudo` 模板：

```pseudocode
CONSTANT ServiceRate = 0.10

PROCEDURE SplitBill()
   // declare your variables, then prompt, input, calculate and output

ENDPROCEDURE
```

## 必测行为

每个测试按顺序喂 2 行输入：账单、人数。期望输出恰好 2 行。

| # | 输入 | 期望输出行 | 说明 |
|:--|:--|:--|:--|
| B1 | `100`、`4` | `Total: 110.00`、`Each: 27.50` | 普通值；整数形式的账单也要能读 |
| B2 | `80`、`3` | `Total: 88.00`、`Each: 29.33` | 每人金额需要舍入显示 |
| B3 | `12.40`、`1` | `Total: 13.64`、`Each: 13.64` | 账单带小数；一个人 |
| B4 | `0`、`5` | `Total: 0.00`、`Each: 0.00` | 零元（边界） |
| B5 | `45`、`2` | `Total: 49.50`、`Each: 24.75` | 两位小数补零 |

T10 已核对：`bill * (1 + rate)`、`bill + bill * rate`、`bill * 1.1` 三种写法在以上数据上格式化结果相同，且都不在 `.5` 舍入临界点上。

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 每人金额用整除：`each = total // people`，输出 `Each: 27.00` | B1、B2、B3、B5 |
| M2 | 不格式化：`print(f"Total: {total}")`，输出 `Total: 110.00000000000001` | B1、B4 等 |
| M3 | 账单用 `int(input())` 读，`12.40` 抛 `ValueError` | B3 |

## 人工核对清单

- [ ] 伪代码：`CONSTANT ServiceRate = 0.10` 用 `=`，值是字面量（指南 p.8）。
- [ ] 伪代码：账单与结果 `DECLARE … : REAL`，人数 `DECLARE … : INTEGER`。
- [ ] 伪代码：每个 `INPUT` 前有 `OUTPUT` 提示语。
- [ ] 伪代码：说明了输出格式（如注释 `// output to 2 decimal places`）——指南 p.17：编程语言里格式化数字的做法要加说明。
- [ ] Python：常量全大写 `SERVICE_RATE`，计算里用常量而不是直接写 `0.10`。
- [ ] Python：用 `f"{x:.2f}"`，没有用 `round()` 代替格式化。

## 出处

改编自 CS50P Problem Set 0 “Tip Calculator”（<https://cs50.harvard.edu/python/psets/0/tip/>，David J. Malan，CC BY-NC-SA 4.0）。改动：小费百分比输入改为固定的服务费常量；输入改为纯数字；增加按人数平分；输出格式全部重写。
