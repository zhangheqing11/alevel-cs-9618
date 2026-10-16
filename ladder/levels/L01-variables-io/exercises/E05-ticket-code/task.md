# L01/E05 · 票号：数字与字符串的转换和连接

| 属性 | 值 |
|:--|:--|
| id | `L01/E05` |
| 目录 | `ladder/levels/L01-variables-io/exercises/E05-ticket-code/` |
| 形态 | `io`（见 `ladder/design.md` §7.2） |
| entry | `ticket_code` |
| pseudocode | `true` |
| files | `[]` |
| skills | `string-concat`, `type-conversion`, `output-format`, `input-prompt` |
| difficulty | 2 |
| title | `Build a ticket code from a name, row and seat` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L01 card §4、§6；常见坑 1、2、5 |

## 练习目标

分清「数字运算」和「字符串连接」：伪代码用 `&` 与 `NUM_TO_STR`（插页 p.2、p.4），Python 用 `+` 与 `str()` 或 f-string；亲眼看到忘记 `int()` 时 `"12" * 100` 的怪结果。

## 题面

### 中文导读

剧院的票号由姓名、一个短横线和一个数字组成，数字 = 排号 × 100 + 座号。例如 Mia 坐第 12 排 7 号，票号是 `Mia-1207`。输入姓名、排号、座号（排号和座号都是 1 到 99 的整数），输出两行：票号，以及「第几排第几座」。伪代码里用 `&` 和 `NUM_TO_STR` 拼出票号。

### English task

A theatre ticket code is made from the customer's name, a hyphen, and the number `Row * 100 + Seat`. For example, Mia in row 12, seat 7 has the code `Mia-1207`.

Write a procedure `TicketCode()` that:

- prompts for and inputs a name, a row number and a seat number (row and seat are integers from 1 to 99)
- builds the ticket code as a single string, using `&` and the function `NUM_TO_STR()` from the insert
- outputs two lines in the form:

```text
Your code is Mia-1207
Row 12, seat 7
```

Then write the Python procedure `ticket_code()` that inputs the name, row and seat (in that order, one per line) and prints the same two lines.

`NUM_TO_STR(x : <datatype1>) RETURNS <datatype2>` returns a string representation of a numeric value, e.g. `NUM_TO_STR(87.5)` returns `"87.5"`.（插页 p.2 原样）

## 接口

```python
def ticket_code() -> None:
    """Input name, row, seat; print 'Your code is <name>-<row*100+seat>' and 'Row <r>, seat <s>'."""
    raise NotImplementedError


if __name__ == "__main__":
    ticket_code()
```

`answer.pseudo` 模板：

```pseudocode
PROCEDURE TicketCode()
   // declare your variables, then prompt, input, build the code and output

ENDPROCEDURE
```

## 必测行为

每个测试按顺序喂 3 行输入：姓名、排号、座号。期望输出恰好 2 行。

| # | 输入 | 期望输出行 | 说明 |
|:--|:--|:--|:--|
| B1 | `Mia`、`12`、`7` | `Your code is Mia-1207`、`Row 12, seat 7` | 题面例子；座号只有 1 位 |
| B2 | `Bo`、`3`、`45` | `Your code is Bo-345`、`Row 3, seat 45` | 排号只有 1 位 |
| B3 | `Ann Lee`、`1`、`1` | `Your code is Ann Lee-101`、`Row 1, seat 1` | 姓名含空格；最小排座号 |
| B4 | `Zed`、`99`、`99` | `Your code is Zed-9999`、`Row 99, seat 99` | 最大排座号 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 排号、座号忘了 `int()`（`row = input()`、`seat = input()`），然后写 `code = name + "-" + row * 100 + seat`。`row * 100` 把字符串 `"12"` 重复 100 次，不报错，B1 的票号变成 `Mia-1212…127` | B1–B4 |
| M2 | `print("Your code is ", code)`：多出一个空格 | B1–B4 |
| M3 | 把数字部分写成字符串拼接而不是算术：`name + "-" + str(row) + str(seat)`，B1 得 `Mia-127` | B1、B3 |

（T10 已用参考实现核对 M1 不抛异常、M3 在 B2、B4 上恰好碰对——所以 M3 只会挂 B1、B3。）

## 人工核对清单

- [ ] 伪代码：`Row`、`Seat` 声明为 `INTEGER`，`Name`、`Code` 声明为 `STRING`。
- [ ] 伪代码：`Code ← Name & "-" & NUM_TO_STR(Row * 100 + Seat)`——用 `&`，不用 `+`（ECR P2 2021 p.45 点名）；数字先经 `NUM_TO_STR` 再连接。
- [ ] 伪代码：第二行可以用 `OUTPUT "Row ", Row, ", seat ", Seat`（逗号分隔，不需要转换），能说出它和 `&` 写法的区别。
- [ ] 每个 `INPUT` 前有提示语。
- [ ] Python：能说出 M1 为什么不报错却给出怪结果（`str * int` 是重复）。

## 出处

自编。语法与函数依据：指南 p.15（OUTPUT）、p.17（&）；插页 9618_s26_in_21 p.2（NUM_TO_STR）、p.4（& 运算符）。
