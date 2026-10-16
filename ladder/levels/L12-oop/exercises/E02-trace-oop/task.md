# L12/E02 · 干跑：类、继承与 SUPER


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 人工核对清单

- [ ] `PREDICTED` 是先手算的；能说出第 2 行为什么是 9 而不是 6。
- [ ] 能说出第 3 行里 `Counters[2].Increment()` 调用的是哪个类的 `Increment`（多态），以及为什么 C 的计数没有变。
- [ ] Python：`super().__init__(GivenStep)`、`super().Increment()`；子类里用 `self.GetCount()` 读计数。

## 出处

自编。类的写法依据：指南 p.28–29（`CLASS`、`PRIVATE`、`NEW`、`INHERITS`、`SUPER`、`NEW <类名>(…)`、`对象.方法()`）。误区依据：ER s23 9618/41 Q2 p.38（继承时应调用父类构造、重写方法时调用父类方法）。
