# L12/E02 · 干跑：类、继承与 SUPER

| 属性 | 值 |
|:--|:--|
| id | `L12/E02` |
| 目录 | `ladder/levels/L12-oop/exercises/E02-trace-oop/` |
| 形态 | `trace`（见 `ladder/design.md` §7.2）；另外测两个类 |
| entry | `RunTrace`（同一文件还有类 `Counter`、`LimitedCounter`） |
| pseudocode | `false` |
| files | `[]` |
| skills | `trace-dry-run`, `translate-pseudocode`, `inheritance`, `polymorphism`, `encapsulation` |
| difficulty | 3 |
| title | `Dry run: classes, inheritance and SUPER` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L12 card §1、§3、§4 |

## 练习目标

读懂指南格式的类与继承：每个对象有自己的状态；子类重写方法并用 `SUPER` 调用父类版本；子类不能直接访问父类的私有属性，只能通过父类的方法。再译成 Python。

## 题面

### 中文导读

先手算下面程序输出的 3 行，填进 `PREDICTED`；再把两个类与主程序译成 Python。注意：`LimitedCounter` 的 `Increment` 是**先检查、后增加**，所以计数可能超过 `Limit`。Python 里 `LimitedCounter` 不能直接读 `Counter` 的私有属性 `__Count`，要用 `GetCount()`。

### English task

Dry-run the pseudocode below and store each line it outputs, in order, in the list `PREDICTED`. Then translate the two classes and the main program into Python. `RunTrace()` runs the main program and outputs exactly the same lines. In Python, the attributes are private (`self.__Count`, `self.__StepSize`, `self.__Limit`).

```pseudocode
CLASS Counter
   PRIVATE Count : INTEGER
   PRIVATE StepSize : INTEGER
   PUBLIC PROCEDURE NEW(GivenStep : INTEGER)
      Count ← 0
      StepSize ← GivenStep
   ENDPROCEDURE
   PUBLIC PROCEDURE Increment()
      Count ← Count + StepSize
   ENDPROCEDURE
   PUBLIC FUNCTION GetCount() RETURNS INTEGER
      RETURN Count
   ENDFUNCTION
ENDCLASS

CLASS LimitedCounter INHERITS Counter
   PRIVATE Limit : INTEGER
   PUBLIC PROCEDURE NEW(GivenStep : INTEGER, GivenLimit : INTEGER)
      SUPER.NEW(GivenStep)
      Limit ← GivenLimit
   ENDPROCEDURE
   PUBLIC PROCEDURE Increment()
      IF GetCount() < Limit THEN
         SUPER.Increment()
      ENDIF
   ENDPROCEDURE
ENDCLASS

// main program
DECLARE Counters : ARRAY[1:2] OF Counter
DECLARE Index : INTEGER
A ← NEW Counter(2)
B ← NEW Counter(5)
C ← NEW LimitedCounter(3, 7)
A.Increment()
A.Increment()
B.Increment()
OUTPUT A.GetCount(), " ", B.GetCount()
FOR Index ← 1 TO 4
   C.Increment()
NEXT Index
OUTPUT C.GetCount()
Counters[1] ← A
Counters[2] ← C
FOR Index ← 1 TO 2
   Counters[Index].Increment()
NEXT Index
OUTPUT Counters[1].GetCount(), " ", Counters[2].GetCount()
```

（`A ← NEW Counter(2)` 的写法见指南 p.29；方法调用 `A.Increment()` 见 p.28。）

## 接口

```python
PREDICTED: list[str] = []  # fill in by hand BEFORE writing the code


class Counter:
    def __init__(self, GivenStep: int) -> None:
        raise NotImplementedError   # self.__Count (INTEGER), self.__StepSize (INTEGER)

    def Increment(self) -> None:
        raise NotImplementedError

    def GetCount(self) -> int:
        raise NotImplementedError


class LimitedCounter(Counter):
    def __init__(self, GivenStep: int, GivenLimit: int) -> None:
        raise NotImplementedError   # call the parent constructor; self.__Limit (INTEGER)

    def Increment(self) -> None:
        raise NotImplementedError


def RunTrace() -> None:
    """Run the main program."""
    raise NotImplementedError


if __name__ == "__main__":
    RunTrace()
```

（不需要 `answer.pseudo`。）

## 必测行为

期望输出（共 3 行，已用参考实现核对）：

```text
4 5
9
6 9
```

| # | 检查 | 期望 |
|:--|:--|:--|
| B1 | `sol.PREDICTED` | 恰好等于上面 3 行 |
| B2 | `RunTrace()` 全部输出行（`output_lines`） | 与上面 3 行完全相等 |
| B3 | `X = LimitedCounter(3, 7)`，`Increment()` 四次后 `GetCount()` | `9`（先检查后增加：0→3→6→9，第四次不变） |
| B4 | `issubclass(LimitedCounter, Counter)`；`LimitedCounter(3, 7)` 的 `vars()` 键 | `True`；恰好是 `{"_Counter__Count", "_Counter__StepSize", "_LimitedCounter__Limit"}` | 
| B5 | `Counter(4)` 调用 `Increment()` 三次后 `GetCount()` | `12` |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | `LimitedCounter.Increment` 直接读父类私有属性：`if self.__Count < self.__Limit:`——Python 把它改写成 `self._LimitedCounter__Count`，抛 `AttributeError`；`PREDICTED` 写对 | B2、B3 |
| M2 | `LimitedCounter.__init__` 没有调用父类构造，而是自己写 `self.__Count = 0`：`GetCount()` 抛 `AttributeError` | B2、B3、B4 |
| M3 | `LimitedCounter` 没有重写 `Increment`（不限制）：第 2 行 `12`、第 3 行 `6 15`；`PREDICTED` 照此写 | B1、B2、B3 |

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能说出第 2 行为什么是 9 而不是 6。
- [ ] 能说出第 3 行里 `Counters[2].Increment()` 调用的是哪个类的 `Increment`（多态），以及为什么 C 的计数没有变。
- [ ] Python：`super().__init__(GivenStep)`、`super().Increment()`；子类里用 `self.GetCount()` 读计数。

## 出处

自编。类的写法依据：指南 p.28–29（`CLASS`、`PRIVATE`、`NEW`、`INHERITS`、`SUPER`、`NEW <类名>(…)`、`对象.方法()`）。误区依据：ER s23 9618/41 Q2 p.38（继承时应调用父类构造、重写方法时调用父类方法）。
