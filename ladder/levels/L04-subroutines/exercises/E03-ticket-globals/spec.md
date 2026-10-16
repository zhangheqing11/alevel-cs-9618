# L04/E03 · 取号机：全局变量与 `global`

| 属性 | 值 |
|:--|:--|
| id | `L04/E03` |
| 目录 | `ladder/levels/L04-subroutines/exercises/E03-ticket-globals/` |
| 形态 | `function`（模块级全局变量 + 两个函数；测试检查函数返回值和全局变量的值） |
| entry | `take_ticket`（同一文件还有 `reset_tickets` 与全局变量 `next_number`、`issued`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `global-scope`, `return-value`, `module-header`, `accumulator` |
| difficulty | 2 |
| title | `Ticket machine: global variables and the global statement` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L04 card §5；常见坑 8、11 |

## 练习目标

用模块修改全局变量（P4 的常态）：伪代码里全局变量在主程序声明、模块里不重复声明；Python 里给全局整数重新赋值必须写 `global`。

## 题面

### 中文导读

取号机有两个全局变量：`NextNumber`（下一个要发的号，初始 1）和 `Issued`（已发出的号数，初始 0）。函数 `TakeTicket()` 返回当前的 `NextNumber`，然后把 `NextNumber` 加 1、`Issued` 加 1。过程 `ResetTickets(Start)` 把 `NextNumber` 设为 `Start`、`Issued` 设为 0。Python 里这两个全局变量写成模块级变量 `next_number`、`issued`。

### English task

A ticket machine uses two global integer variables:

- `NextNumber`, the number of the next ticket, initialised to 1
- `Issued`, the number of tickets issued so far, initialised to 0.

Write pseudocode for:

- the declaration and initialisation of the two global variables
- a function `TakeTicket()` that returns the value of `NextNumber`, then adds 1 to `NextNumber` and adds 1 to `Issued`
- a procedure `ResetTickets()` that takes an integer parameter `Start`, sets `NextNumber` to `Start` and sets `Issued` to 0.

Then write the Python version. The global variables are module-level variables `next_number` and `issued`, initialised when the file is loaded.

## 接口

```python
next_number = 1   # global: the number of the next ticket
issued = 0        # global: how many tickets have been issued


def take_ticket() -> int:
    """Return the current next_number, then add 1 to next_number and to issued."""
    raise NotImplementedError


def reset_tickets(start: int) -> None:
    """Set next_number to start and issued to 0."""
    raise NotImplementedError
```

（`starter.py` 里两个全局变量与初值照上面给出。）

`answer.pseudo` 模板：

```pseudocode
// global variables
DECLARE NextNumber : INTEGER
DECLARE Issued : INTEGER
NextNumber ← 1
Issued ← 0

FUNCTION TakeTicket() RETURNS INTEGER

ENDFUNCTION

PROCEDURE ResetTickets(Start : INTEGER)

ENDPROCEDURE
```

## 必测行为

`sol` fixture 每个测试都重新加载模块，所以每个测试开始时 `next_number == 1`、`issued == 0`。

| # | 操作（同一测试内按顺序） | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | 刚加载 | `sol.next_number == 1`、`sol.issued == 0` | 初值 |
| B2 | 连续调用 `take_ticket()` 三次 | 依次返回 `1`、`2`、`3`；之后 `sol.next_number == 4`、`sol.issued == 3` | 先返回、后加 1 |
| B3 | `reset_tickets(100)`，再 `take_ticket()` 两次 | 返回 `100`、`101`；之后 `sol.issued == 2` | 重置 |
| B4 | `take_ticket()` 一次，`reset_tickets(0)`，再 `take_ticket()` | 第二次返回 `0`；`sol.issued == 1` | 重置为 0（边界） |
| B5 | `take_ticket()` 的返回类型 | `int` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `take_ticket` 里漏了 `global next_number, issued`，第一次调用就抛 `UnboundLocalError` | B2、B3、B4、B5 |
| M2 | 在函数里重新声明同名局部变量（ER w25 p.16 点名的「Global versus local」错误）：`take_ticket` 开头写 `next_number = 1`、`issued = 0`（不写 `global`），之后每次都返回 `1`，全局变量不变 | B2、B3、B4 |
| M3 | 先加 1 再返回：第一张票返回 `2` | B2、B3、B4 |

## 人工核对清单

- [ ] 伪代码：全局变量只在主程序里 `DECLARE` 一次；`TakeTicket` 与 `ResetTickets` 里没有再 `DECLARE NextNumber`（ER w25 p.16、p.18）。
- [ ] 伪代码：`TakeTicket` 先把当前号存进局部变量（如 `DECLARE ThisNumber : INTEGER`），更新两个全局变量后再 `RETURN ThisNumber`——因为 `RETURN` 一执行函数就结束（指南 p.23）。
- [ ] 伪代码：`ResetTickets` 是 `PROCEDURE`，没有 `RETURNS`。
- [ ] Python：只在**赋值**全局变量的函数里写 `global`；能说出为什么只读全局变量时不需要。
- [ ] 能说出这道题如果不用全局变量，Python 里还可以怎样写（例如把状态作为参数传入、函数返回新状态），以及 P4 题目说「global」时为什么必须用全局变量。

## 出处

自编。误区依据：ER w25 三个 variant 的 Q8 点评中的「Global versus local」（p.16、p.23、p.30），以及 9618/21 Q4「把全局数组声明成了局部」（p.18）。
