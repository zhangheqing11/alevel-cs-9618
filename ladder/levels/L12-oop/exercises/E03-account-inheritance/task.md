# L12/E03 · 继承：储蓄账户重写取款方法


### 中文导读

按下面两张表写类 `Account` 与它的子类 `SavingsAccount`。所有属性都是私有的。储蓄账户最多取款 2 次；**失败的取款不占次数**。

### English task

| `Account` | |
|:--|:--|
| `AccountNumber : STRING` | private |
| `Balance : REAL` | private |
| `Constructor()` | takes the account number as a parameter; initialises `AccountNumber` to it and `Balance` to 0.0 |
| `GetAccountNumber()` | returns `AccountNumber` |
| `GetBalance()` | returns `Balance` |
| `Deposit()` | takes a real `Amount`; if `Amount` is greater than 0, adds it to `Balance` and returns `TRUE`, otherwise returns `FALSE` |
| `Withdraw()` | takes a real `Amount`; if `Amount` is greater than 0 and not greater than `Balance`, subtracts it from `Balance` and returns `TRUE`, otherwise returns `FALSE` |

| `SavingsAccount` (inherits from `Account`) | |
|:--|:--|
| `InterestRate : REAL` | private |
| `WithdrawalsLeft : INTEGER` | private |
| `Constructor()` | takes the account number and the interest rate as parameters; calls the parent constructor; initialises `InterestRate` to the rate and `WithdrawalsLeft` to 2 |
| `GetWithdrawalsLeft()` | returns `WithdrawalsLeft` |
| `AddInterest()` | deposits `Balance * InterestRate` into the account |
| `Withdraw()` | overrides the parent method: returns `FALSE` if `WithdrawalsLeft` is 0; otherwise calls the parent `Withdraw()`, and if that succeeds subtracts 1 from `WithdrawalsLeft`; returns the result of the parent method |

Write pseudocode for both classes, then write them in Python.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

## 人工核对清单

- [ ] 伪代码：`CLASS SavingsAccount INHERITS Account`；构造里第一句 `SUPER.NEW(GivenNumber)`；重写的 `Withdraw` 里 `Result ← SUPER.Withdraw(Amount)`（指南 p.28）。
- [ ] 伪代码：子类里读余额用 `GetBalance()`，没有直接写 `Balance`（父类的私有属性）。
- [ ] Python：`super().__init__(GivenNumber)`；`super().Withdraw(Amount)`；所有属性私有并有类型注释；每个方法都有 `self`。
- [ ] 能说出 `AddInterest` 为什么调用 `Deposit` 而不是直接改余额（封装：所有改余额的规则都在 `Deposit`/`Withdraw` 里）。

## 出处

自编。误区依据：ER s23 9618/41 Q2 p.38（继承：应调用父类构造、不要重新定义属性；重写时调用父类方法避免重复）。语法依据：指南 p.28–29。
