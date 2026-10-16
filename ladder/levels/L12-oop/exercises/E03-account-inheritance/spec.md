# L12/E03 · 继承：储蓄账户重写取款方法

| 属性 | 值 |
|:--|:--|
| id | `L12/E03` |
| 目录 | `ladder/levels/L12-oop/exercises/E03-account-inheritance/` |
| 形态 | `function`（两个类；测试创建对象、调用方法，并检查继承关系与私有属性） |
| entry | `SavingsAccount`（同一文件还有 `Account`） |
| pseudocode | `true` |
| files | `[]` |
| skills | `inheritance`, `polymorphism`, `encapsulation`, `getter-setter`, `boolean-return` |
| difficulty | 4 |
| title | `Inheritance: a savings account overrides Withdraw` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L12 card §3 |

## 练习目标

写一个父类和一个子类：子类构造调用父类构造；子类新增属性与方法；子类重写父类方法，并在重写里调用父类版本（不重复父类的逻辑）；子类只通过父类的公有方法访问父类的私有数据。

## 题面

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

## 接口

```python
class Account:
    def __init__(self, GivenNumber: str) -> None:
        raise NotImplementedError   # self.__AccountNumber (STRING), self.__Balance (REAL)

    def GetAccountNumber(self) -> str:
        raise NotImplementedError

    def GetBalance(self) -> float:
        raise NotImplementedError

    def Deposit(self, Amount: float) -> bool:
        raise NotImplementedError

    def Withdraw(self, Amount: float) -> bool:
        raise NotImplementedError


class SavingsAccount(Account):
    def __init__(self, GivenNumber: str, GivenRate: float) -> None:
        raise NotImplementedError   # parent constructor; self.__InterestRate (REAL), self.__WithdrawalsLeft (INTEGER)

    def GetWithdrawalsLeft(self) -> int:
        raise NotImplementedError

    def AddInterest(self) -> None:
        raise NotImplementedError

    def Withdraw(self, Amount: float) -> bool:
        raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
CLASS Account

ENDCLASS

CLASS SavingsAccount INHERITS Account

ENDCLASS
```

## 必测行为

金额用 `pytest.approx(…, abs=1e-9)` 比较。T10 已用参考实现核对。

| # | 操作 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `A = Account("A1")`；`GetAccountNumber()`、`GetBalance()` | `"A1"`、`0.0` | 构造 |
| B2 | `A.Deposit(100.0)`、`A.Withdraw(30.0)` 后 `GetBalance()` | `True`、`True`；`70.0` | |
| B3 | 接 B2：`A.Withdraw(80)`、`A.Deposit(0)`、`A.Deposit(-5)`、`A.Withdraw(0)` | 都返回 `False`；余额仍 `70.0` | 无效金额（边界） |
| B4 | `S = SavingsAccount("S1", 0.05)`；`S.Deposit(200)`；`S.AddInterest()` 后 `GetBalance()` | `210.0` | 子类方法 + 继承来的方法 |
| B5 | 接 B4：`S.Withdraw(10)` 三次；然后 `GetBalance()`、`GetWithdrawalsLeft()` | `True`、`True`、`False`；`190.0`；`0` | 重写：最多 2 次 |
| B6 | `S2 = SavingsAccount("S2", 0.1)`；`Deposit(50)`；`Withdraw(100)`；然后 `GetWithdrawalsLeft()`；再 `Withdraw(10)` 三次 | `False`；`2`；`True`、`True`、`False`；最后余额 `30.0` | 失败的取款不占次数 |
| B7 | `SavingsAccount("S3", 0.05).AddInterest()` 后余额 | `0.0` | 余额为 0 时利息为 0（`Deposit(0)` 返回 `False`，不报错） |
| B8 | `isinstance(S, Account)`；`vars(S)` 的键 | `True`；恰好是 `{"_Account__AccountNumber", "_Account__Balance", "_SavingsAccount__InterestRate", "_SavingsAccount__WithdrawalsLeft"}` | 继承；子类没有重新定义父类属性 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `SavingsAccount.__init__` 没有调用父类构造：`Deposit` 时抛 `AttributeError` | B4–B8 |
| M2 | 重写的 `Withdraw` 不调用父类版本，自己写 `self.__Balance -= Amount`：Python 改写成 `_SavingsAccount__Balance`，抛 `AttributeError` | B5、B6 |
| M3 | 取款失败也减少 `WithdrawalsLeft` | B6 |
| M4 | 子类构造里重新定义 `self.__Balance = 0.0`（而不是调用父类构造）：`vars(S)` 多出 `_SavingsAccount__Balance`、少了父类属性 | B4–B8 |

## 人工核对清单

- [ ] 伪代码：`CLASS SavingsAccount INHERITS Account`；构造里第一句 `SUPER.NEW(GivenNumber)`；重写的 `Withdraw` 里 `Result ← SUPER.Withdraw(Amount)`（指南 p.28）。
- [ ] 伪代码：子类里读余额用 `GetBalance()`，没有直接写 `Balance`（父类的私有属性）。
- [ ] Python：`super().__init__(GivenNumber)`；`super().Withdraw(Amount)`；所有属性私有并有类型注释；每个方法都有 `self`。
- [ ] 能说出 `AddInterest` 为什么调用 `Deposit` 而不是直接改余额（封装：所有改余额的规则都在 `Deposit`/`Withdraw` 里）。

## 出处

自编。误区依据：ER s23 9618/41 Q2 p.38（继承：应调用父类构造、不要重新定义属性；重写时调用父类方法避免重复）。语法依据：指南 p.28–29。
