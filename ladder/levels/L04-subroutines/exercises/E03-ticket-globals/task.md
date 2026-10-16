# L04/E03 · 取号机：全局变量与 `global`


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：全局变量只在主程序里 `DECLARE` 一次；`TakeTicket` 与 `ResetTickets` 里没有再 `DECLARE NextNumber`（ER w25 p.16、p.18）。
- [ ] 伪代码：`TakeTicket` 先把当前号存进局部变量（如 `DECLARE ThisNumber : INTEGER`），更新两个全局变量后再 `RETURN ThisNumber`——因为 `RETURN` 一执行函数就结束（指南 p.23）。
- [ ] 伪代码：`ResetTickets` 是 `PROCEDURE`，没有 `RETURNS`。
- [ ] Python：只在**赋值**全局变量的函数里写 `global`；能说出为什么只读全局变量时不需要。
- [ ] 能说出这道题如果不用全局变量，Python 里还可以怎样写（例如把状态作为参数传入、函数返回新状态），以及 P4 题目说「global」时为什么必须用全局变量。

## 出处

自编。误区依据：ER w25 三个 variant 的 Q8 点评中的「Global versus local」（p.16、p.23、p.30），以及 9618/21 Q4「把全局数组声明成了局部」（p.18）。
